#!/usr/bin/env python3
"""Build the public garden from archived/ and explicitly public drafts/ only."""
from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import quote, unquote, urlsplit

from standard_site import build_index, verification_path
from garden_analytics import (ArticleLinks, build_word_index, build_link_index,
                              render_word_index_page, render_link_index_page)

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = 'markdown+footnotes+pipe_tables+strikeout+tex_math_dollars-implicit_figures-smart'


def run_pandoc(data, source, target):
    return subprocess.run(['pandoc', '-f', source, '-t', target, '--wrap=none'],
                          input=data, text=True, capture_output=True, check=True).stdout


def metadata(value):
    kind, content = value.get('t'), value.get('c')
    if kind == 'MetaList':
        return [metadata(x) for x in content]
    if kind == 'MetaBool' or kind == 'MetaString':
        return content
    if kind == 'MetaInlines':
        return ''.join(x.get('c', '') if x['t'] == 'Str' else ' ' for x in content).strip()
    return ''


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def slugify(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')


def load_posts(root):
    posts, ids, routes = [], set(), set()
    for folder, section in [('archived', 'archive'), ('drafts', 'drafts')]:
        for path in sorted((root / folder).glob('*.md')):
            if path.name == 'README.md':
                continue
            if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
                raise ValueError(f'Article symlinks are not publication inputs: {path}')
            text = path.read_text()
            if not text.startswith('---\n'):
                raise ValueError(f'Article needs frontmatter: {path}')
            _, header, body = text.split('---', 2)
            properties = json.loads(run_pandoc('---'+header+'---\n', MARKDOWN, 'json'))
            doc = json.loads(run_pandoc(body, MARKDOWN+'-yaml_metadata_block', 'json'))
            meta = {k: metadata(v) for k, v in properties['meta'].items()}
            if not meta.get('title') or not meta.get('content_id'):
                raise ValueError(f'Title and content_id are required: {path}')
            if section == 'drafts' and meta.get('visibility') != 'public':
                raise ValueError(f'Draft must explicitly say visibility: public: {path}')
            if meta.get('visibility') == 'private':
                raise ValueError(f'Private article is not a publication input: {path}')
            slug = meta.get('slug') or re.sub(r'^\d{4}-\d{2}-\d{2}-', '', path.stem)
            if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', slug):
                raise ValueError(f'Invalid slug: {slug}')
            route = f'{section}/{slug}.html'
            if meta['content_id'] in ids or route in routes:
                raise ValueError(f'Duplicate article ID or route: {path}')
            ids.add(meta['content_id']); routes.add(route)
            posts.append({'path': path, 'source': str(path.relative_to(root)), 'section': section,
                          'slug': slug, 'route': route, 'meta': meta, 'doc': doc})
    return sorted(posts, key=lambda p: (str(p['meta'].get('date', '')), p['slug']), reverse=True)


def load_permalinks(root):
    path = root / 'site/permalinks.json'
    routes = json.loads(path.read_text()) if path.exists() else {}
    if not isinstance(routes, dict):
        raise ValueError('Permalinks must map content_id to a permanent path')
    seen = set()
    for content_id, route in routes.items():
        if not isinstance(route, str) or not re.fullmatch(r'p/[a-z0-9][a-z0-9_-]*\.html', route):
            raise ValueError(f'Invalid permalink for {content_id}: {route}')
        if route in seen:
            raise ValueError(f'Duplicate permalink: {route}')
        seen.add(route)
    return routes


def assign_permalinks(posts, routes):
    for post in posts:
        content_id = post['meta']['content_id']
        if content_id not in routes:
            raise ValueError(f'Unregistered permalink for {content_id}; run make register-urls')
        post['route'] = routes[content_id]


def register_permalinks(root=ROOT):
    routes = load_permalinks(root)
    config = json.loads((root / 'site/garden.json').read_text())
    reserved = set(routes.values()) | set(config.get('withdrawn_routes', [])) | set(config.get('redirects', {}))
    added = 0
    for post in load_posts(root):
        content_id = post['meta']['content_id']
        if content_id in routes:
            continue
        route = 'p/' + post['slug'] + '.html'
        if route in reserved:
            raise ValueError(f'Permalink already reserved: {route}; choose a unique slug')
        routes[content_id] = route
        reserved.add(route)
        added += 1
    if added:
        (root / 'site/permalinks.json').write_text(json.dumps(dict(sorted(routes.items())), indent=2) + '\n')
    print(f'Registered {added} new permalinks; existing URLs unchanged')


def public_asset(root, source, raw):
    url = urlsplit(raw)
    path = (source.parent / unquote(url.path)).resolve()
    media = (root / 'media').resolve()
    if not path.is_relative_to(media) or not path.is_file():
        raise ValueError(f'Article asset must be a real file inside media/: {source.name}: {raw}')
    return path, path.relative_to(root).as_posix()


def build(root=ROOT):
    root = root.resolve()
    config = json.loads((root / 'site/garden.json').read_text())
    base = config['url'].rstrip('/')
    posts = load_posts(root)
    if not posts:
        raise ValueError('No public articles found')
    assign_permalinks(posts, load_permalinks(root))
    atproto = build_index(root, config, posts)
    atproto_uris = {entry['content_id']: entry['uri'] for entry in atproto['documents']} if atproto else {}
    by_path = {p['path'].resolve(): p for p in posts}
    by_slug = {p['slug']: p for p in posts}
    by_id = {p['meta']['content_id']: p for p in posts}
    aliases = config.get('slug_aliases', {})
    redirects = dict(config.get('redirects', {}))
    withdrawn = set(config.get('withdrawn_routes', []))
    for post in posts:
        # Both old collection paths survive a later move or filename change.
        for section in ['archive', 'drafts']:
            old = section + '/' + Path(post['route']).name
            target = '/' + post['route']
            if old in redirects and redirects[old] != target:
                raise ValueError(f'Conflicting redirect: {old}')
            redirects[old] = target
    for route in withdrawn:
        if not re.fullmatch(r'[a-z0-9][a-z0-9/_-]*\.html', route):
            raise ValueError(f'Unsafe withdrawn route: {route}')
        if route in redirects or any(p['route'] == route for p in posts):
            raise ValueError(f'Withdrawn route is still public: {route}')
    for old, target in aliases.items():
        if target not in by_slug:
            raise ValueError(f'Alias refers to missing article: {old} -> {target}')
        by_slug[old] = by_slug[target]
    output = root / '_site'
    if output.is_symlink():
        raise ValueError('_site must not be a symlink')
    source_commit = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=root, capture_output=True, text=True).stdout.strip()
    source_dirty = bool(subprocess.run(['git', 'status', '--porcelain'], cwd=root, capture_output=True, text=True).stdout.strip())

    def esc(value):
        return html.escape(str(value), quote=True)

    def frame(title, body, route='', section='', document_uri=None, script=None):
        canonical = base + '/' + route
        page_title = 'Data Leverage Digital Garden' if title == 'Data Leverage' else title + ' · Data Leverage'
        standard_links = f'<link rel="site.standard.publication" href="{esc(atproto["publication"]["uri"])}">' if atproto else ''
        if document_uri:
            standard_links += f'<link rel="site.standard.document" href="{esc(document_uri)}">'
        extras = f'<link rel="stylesheet" href="/analytics.css"><script src="/{esc(script)}" defer></script>' if script else ''
        return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(page_title)}</title><link rel="canonical" href="{esc(canonical)}">
{standard_links}
<link rel="stylesheet" href="/site.css"><script src="/search.js" defer></script>{extras}</head>
<body><a class="skip" href="#main">Skip to content</a><header class="site-header">
<a class="brand" href="/">Data Leverage <span>Digital garden</span></a>
<nav aria-label="Main"><a href="/archive/" {'aria-current="page"' if section=='archive' else ''}>Archive</a>
<a href="/drafts/" {'aria-current="page"' if section=='drafts' else ''}>Public drafts</a><a href="/extras.html" {'aria-current="page"' if section=='extras' else ''}>Extras</a><a href="/#search">Search</a></nav></header>
<main id="main">{body}</main><footer><a href="https://dataleverage.substack.com/">Newsletter</a>
<a href="https://www.nickmvincent.com/">Nick Vincent</a><a href="{esc(config['source_url'])}">Source on GitHub</a></footer></body></html>'''

    def rows(selected):
        return '<ul class="article-list">' + ''.join(f'''<li><div class="list-meta">{esc(p['meta'].get('date','')[:10])}</div>
<div><a href="/{esc(p['route'])}">{esc(p['meta']['title'])}</a>
<p>{esc(p['meta'].get('subtitle') or p['meta'].get('summary') or '')}</p></div></li>''' for p in selected) + '</ul>'

    with tempfile.TemporaryDirectory(prefix='.garden-build-', dir=root) as temp:
        stage = Path(temp)
        def write(path, text):
            dest = stage / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
        assets, search, manifest, analytics = set(), [], [], []
        for post in posts:
            doc, meta, source = post['doc'], post['meta'], post['path']
            doc['meta'] = {}
            heading_id = 'article-title'
            if doc['blocks'] and doc['blocks'][0]['t'] == 'Header':
                first = doc['blocks'][0]
                heading_text = run_pandoc(json.dumps({'pandoc-api-version': doc['pandoc-api-version'], 'meta': {}, 'blocks': [first]}), 'json', 'plain').strip()
                if first['c'][0] == 1 and heading_text == meta['title']:
                    heading_id = first['c'][1][0] or heading_id
                    doc['blocks'].pop(0)
            authors = meta.get('authors') or meta.get('author') or ['Nick Vincent']
            if isinstance(authors, str): authors = [authors]
            byline = ', '.join(authors)
            updated = f" · Updated {esc(meta['updated_at'][:10])}" if meta.get('updated_at') else ''
            def resolve(raw, image=False):
                u = urlsplit(raw)
                if raw.startswith('ref:'):
                    key = raw.removeprefix('ref:')
                    target = by_id.get(key) or by_slug.get(key.split(':')[-1])
                    if target is None:
                        raise ValueError(f'Unresolved reference in {source}: {raw}')
                    return '/' + target['route']
                if u.scheme or u.netloc or not u.path:
                    return raw
                candidate = (source.parent / unquote(u.path)).resolve()
                if not image and candidate in by_path:
                    return '/' + by_path[candidate]['route'] + ('#' + u.fragment if u.fragment else '')
                if u.path.startswith('/'):
                    return raw
                asset, relative = public_asset(root, source, raw)
                assets.add((asset, relative))
                return '/' + quote(relative, safe='/') + ('#' + u.fragment if u.fragment else '')
            for node in walk(doc['blocks']):
                if node.get('t') in {'Image', 'Link'}:
                    node['c'][2][0] = resolve(node['c'][2][0], node['t'] == 'Image')
                elif node.get('t') in {'RawBlock', 'RawInline'} and node['c'][0] == 'html':
                    node['c'][1] = re.sub(r'\bsrc=([\"\x27])(.*?)\1',
                        lambda m: 'src=' + m[1] + esc(resolve(html.unescape(m[2]), True)) + m[1], node['c'][1])
            article = run_pandoc(json.dumps(doc), 'json', 'html5')
            plain = run_pandoc(json.dumps(doc), 'json', 'plain')
            analytics.append({'title': meta['title'], 'text': plain, 'source': post['source'],
                              'slug': post['slug'], 'date': meta.get('date', ''),
                              'category': 'Public drafts' if post['section'] == 'drafts' else 'Archive',
                              'href': '/' + post['route'], 'links': ArticleLinks(article, base).links})
            is_draft = post['section'] == 'drafts'
            original = meta.get('original_url') or meta.get('leaflet')
            original_link = f'<a href="{esc(original)}">{"Earlier published version" if is_draft else "Original publication"}</a>' if original else ''
            source_link = config['source_url'].rstrip('/') + '/blob/' + config['source_branch'] + '/' + quote(post['source'], safe='/')
            note = '<p class="status-note">Public draft · A working note that may change.</p>' if is_draft else '<p class="status-note">Published archive · Preserved from an earlier publication.</p>'
            body = f'''<article class="reader"><p class="eyebrow"><a href="/{post['section']}/">{"Public drafts" if is_draft else "Archive"}</a></p>
<h1 id="{esc(heading_id)}">{esc(meta['title'])}</h1><p class="subtitle">{esc(meta.get('subtitle') or meta.get('summary') or '')}</p>
<div class="article-meta">{esc(meta.get('date','')[:10])} · {esc(byline)}{updated} {original_link}</div>{note}
<div class="article-body">{article}</div><p class="source-link"><a href="{esc(source_link)}">View Markdown source</a></p></article>'''
            write(post['route'], frame(meta['title'], body, post['route'], post['section'], atproto_uris.get(meta['content_id'])))
            search.append({'title': meta['title'], 'section': post['section'], 'url': '/' + post['route'],
                           'summary': meta.get('subtitle') or meta.get('summary') or '', 'text': plain})
            manifest.append({'content_id': meta['content_id'], 'source': post['source'], 'route': post['route'],
                             'section': post['section'], 'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
        descriptions = {'archive': 'Previously published articles, preserved with their original source links.',
                        'drafts': 'Work in progress.'}
        labels = {'archive': 'Archive', 'drafts': 'Public drafts'}
        sections = {key: [p for p in posts if p['section'] == key] for key in descriptions}
        for key, selected in sections.items():
            body = f'<div class="collection"><p class="eyebrow">Data Leverage</p><h1>{labels[key]}</h1><p class="lede">{descriptions[key]}</p><p class="count">{len(selected)} articles</p>{rows(selected)}</div>'
            write(key + '/index.html', frame(labels[key], body, key + '/', key))
        home = '''<div class="collection"><p class="eyebrow">Nick Vincent’s writing</p><h1>Data Leverage</h1>
<section id="search" class="search"><label for="query">Search the garden</label><input id="query" type="search" placeholder="An idea, an article, a phrase…" autocomplete="off">
<p id="search-status" aria-live="polite"></p><ul id="search-results" class="article-list"></ul></section>'''
        for key in ['drafts', 'archive']:
            home += f'<section class="home-section"><div class="section-title"><h2>{labels[key]}</h2><a href="/{key}/">View all {len(sections[key])} →</a></div><p>{descriptions[key]}</p>{rows(sections[key][:5])}</section>'
        write('index.html', frame('Data Leverage', home + '</div>'))
        extras = '''<div class="collection"><p class="eyebrow">Explore the garden</p><h1>Extras</h1>
<p class="lede">Patterns in the writing: recurring words and phrases, and the sources linked along the way.</p>
<ul class="article-list"><li><div class="list-meta">Language</div><div><a href="/words.html">Words and phrases</a>
<p>Explore word, two-word, and three-word frequencies, with counts and links to the articles that use them.</p></div></li>
<li><div class="list-meta">References</div><div><a href="/links.html">Outbound links</a>
<p>Browse links by domain or article, search and sort them, and review duplicates and other maintenance findings.</p></div></li></ul>
<p class="count">Rebuilt with the site from its public Archive and Public drafts.</p></div>'''
        write('extras.html', frame('Extras', extras, 'extras.html', 'extras'))
        for name, index, render, title in [
                ('word', build_word_index(analytics), render_word_index_page, 'Words'),
                ('link', build_link_index(analytics), render_link_index_page, 'Link Index')]:
            data_path = f'data/{name}-index.json'
            write(data_path, json.dumps(index, ensure_ascii=False, indent=2) + '\n')
            body = (f'<div class="analytics"><p class="eyebrow"><a href="/extras.html">Extras</a> · '
                    '<a href="/words.html">Words</a> · <a href="/links.html">Links</a></p>' + render(index) +
                    f'<p class="source-link"><a href="/{data_path}">Download this index as JSON</a></p></div>')
            write(name + 's.html', frame(title, body, name + 's.html', 'extras', script=name + 's.js'))
        for route in withdrawn:
            write(route, '<!doctype html><html lang="en"><head><meta charset="utf-8">'
                  '<meta name="viewport" content="width=device-width,initial-scale=1">'
                  '<meta name="robots" content="noindex"><title>Page unavailable</title>'
                  '<link rel="stylesheet" href="/site.css"></head><body><main class="reader">'
                  '<h1>Page unavailable</h1><p>This page is no longer part of the public collection.</p>'
                  '<p><a href="/">Return to the garden</a></p></main></body></html>')
        for old, target in redirects.items():
            if old.startswith('/') or '..' in Path(old).parts or not old.endswith('.html'):
                raise ValueError(f'Unsafe redirect path: {old}')
            destination = stage / target.lstrip('/')
            if target.endswith('/'):
                destination /= 'index.html'
            if not destination.is_file():
                raise ValueError(f'Redirect target is missing: {old} -> {target}')
            if (stage / old).exists():
                raise ValueError(f'Redirect collides with a page: {old}')
            write(old, f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={esc(target)}"><link rel="canonical" href="{esc(base+target)}"><title>Article moved</title></head><body><a href="{esc(target)}">Continue to the article</a></body></html>')
        for source, relative in assets:
            dest = stage / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
        for name in ['site.css', 'search.js', 'analytics.css', 'words.js', 'links.js']:
            shutil.copy2(root / 'site' / name, stage / name)
        write('search-index.json', json.dumps(search, ensure_ascii=False))
        if atproto:
            write('atproto-index.json', json.dumps(atproto, ensure_ascii=False, indent=2) + '\n')
            write(verification_path(base), atproto['publication']['uri'] + '\n')
        write('manifest.json', json.dumps({'source_repository': config['source_url'], 'source_commit': source_commit, 'source_dirty': source_dirty,
              'posts': manifest, 'redirects': redirects, 'withdrawn_routes': sorted(withdrawn), 'assets': sorted(p for _, p in assets)}, indent=2) + '\n')
        write('.nojekyll', '')
        write('robots.txt', 'User-agent: *\nAllow: /\n')
        check_links(stage)
        if output.exists():
            shutil.rmtree(output)
        shutil.move(str(stage), output)
    print(f"Built {len(sections['archive'])} archived articles, {len(sections['drafts'])} public drafts, and {len(redirects)} redirects in {output}")


class PageLinks(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links = []; self.ids = set(); self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'): self.ids.add(attrs['id'])
        for name in (['href'] if tag == 'a' else ['src'] if tag == 'img' else []):
            if attrs.get(name): self.links.append(attrs[name])


def check_links(site):
    pages = {p: PageLinks(p.read_text()) for p in site.rglob('*.html')}
    for page, data in pages.items():
        for raw in data.links:
            u = urlsplit(raw)
            if u.scheme or u.netloc: continue
            target = site / unquote(u.path.lstrip('/')) if u.path.startswith('/') else page.parent / unquote(u.path)
            if not u.path: target = page
            elif u.path.endswith('/'): target /= 'index.html'
            if not target.exists(): raise ValueError(f'Broken local link: {page.name}: {raw}')
            if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
                raise ValueError(f'Broken fragment: {page.name}: {raw}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--register-permalinks', action='store_true')
    args = parser.parse_args()
    if args.register_permalinks:
        register_permalinks()
    elif args.check:
        check_links(ROOT / '_site')
        print('All generated local links and fragments resolve')
    else:
        build()
