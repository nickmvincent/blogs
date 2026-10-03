#!/usr/bin/env python3
"""Refresh the complete public Data Leverage archive from live Substack.

Requires Python 3, curl, and Pandoc. Raw fetches and validation reports are
local-only in ignored .import-cache/. Never commits, pushes, or publishes.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.import-cache'
BASE = 'https://dataleverage.substack.com'
FORMAT = 'markdown+footnotes+pipe_tables+strikeout+tex_math_dollars-implicit_figures-smart'
VOID = set('area base br col embed hr img input link meta param source track wbr'.split())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    if urlsplit(url).scheme != 'https':
        raise ValueError(f'Expected HTTPS: {url}')
    with tempfile.TemporaryDirectory() as temp:
        body, headers = Path(temp) / 'body', Path(temp) / 'headers'
        subprocess.run(['curl', '--fail', '--location', '--silent', '--show-error',
                        '--retry', '2', '--connect-timeout', '20', '--max-time', '90',
                        '--dump-header', str(headers), '--output', str(body), url], check=True)
        types = re.findall(r'^content-type:\s*([^;\r\n]+)', headers.read_text(), re.M | re.I)
        return body.read_bytes(), types[-1].strip() if types else ''


def capture_listing():
    posts, seen = [], set()
    for offset in range(0, 10000, 20):
        raw, _ = fetch(f'{BASE}/api/v1/archive?sort=new&offset={offset}&limit=20')
        (CACHE / f'listing-{offset}.json').write_bytes(raw)
        batch = json.loads(raw)
        if not isinstance(batch, list):
            raise ValueError('Archive endpoint did not return a list')
        if not batch:
            break
        for post in batch:
            if post['id'] in seen:
                raise ValueError('Duplicate post in listing; restart when publication is stable')
            seen.add(post['id'])
            posts.append(post)
    else:
        raise ValueError('Archive pagination did not terminate')
    result = {'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),
              'posts': posts, 'terminal_offset': offset}
    (CACHE / 'listing.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    return result


def extract_post(raw):
    page = raw.decode('utf-8')
    start = page.index('JSON.parse(', page.index('window._preloads')) + len('JSON.parse(')
    encoded, _ = json.JSONDecoder().raw_decode(page[start:])
    post = json.loads(encoded)['post']
    if not post.get('is_published') or post.get('audience') != 'everyone' or not post.get('body_html'):
        raise ValueError('Missing full public article body; refusing to archive a preview')
    return post


def capture_post(item):
    raw, _ = fetch(f"{BASE}/p/{item['slug']}")
    post = extract_post(raw)
    if post['id'] != item['id']:
        raise ValueError('Listing/page ID mismatch')
    (CACHE / f"{post['id']}.html").write_bytes(raw)
    (CACHE / f"{post['id']}.json").write_text(json.dumps({
        'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),
        'post': post}, ensure_ascii=False, indent=2) + '\n')
    print(f"Fetched {post['id']}: {post['title']}", flush=True)


class Node:
    def __init__(self, tag='', attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def descendants(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.descendants()

    def has_class(self, name):
        return name in (self.attrs.get('class') or '').split()


class Tree(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def pandoc(data, source, target):
    options = ['--reference-links'] if target == FORMAT else []
    return subprocess.run(['pandoc', '--from', source, '--to', target, '--wrap=none', *options],
                          input=data, text=True, capture_output=True, check=True).stdout


def convert(post, offline):
    notes, assets, embeds = {}, {}, []
    slug = post['slug']
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', slug):
        raise ValueError('Unexpected slug')
    tree = Tree(post['body_html']).root

    def local_image(url):
        if url in assets:
            return assets[url]
        manifest = CACHE / 'media.json'
        # The global media cache is populated sequentially during conversion.
        known = json.loads(manifest.read_text()) if manifest.exists() else {}
        if url in known and (ROOT / known[url]).is_file():
            relative = known[url]
        else:
            if offline:
                raise ValueError(f'Image missing from cache: {url}')
            data, mime = fetch(url)
            extension = {'image/jpeg': '.jpg', 'image/png': '.png', 'image/webp': '.webp',
                         'image/gif': '.gif', 'image/svg+xml': '.svg', 'image/avif': '.avif'}.get(mime)
            if not extension:
                raise ValueError(f'Unexpected image MIME type: {mime}')
            relative = f'media/{slug}/{digest(data)[:20]}{extension}'
            path = ROOT / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            known[url] = relative
            manifest.write_text(json.dumps(known, ensure_ascii=False, indent=2) + '\n')
        assets[url] = '../' + relative
        return assets[url]

    def render(node):
        if isinstance(node, str):
            return html.escape(node, quote=False)
        tag, attrs = node.tag, node.attrs
        if tag in {'script', 'style', 'svg', 'button', 'form', 'input', 'source'}:
            return ''
        if any(node.has_class(c) for c in ['subscription-widget', 'subscription-widget-wrap-editor',
                                          'image-link-expand', 'restack-image', 'view-image']):
            return ''
        if node.has_class('footnote'):
            number = next(n for n in node.descendants() if n.has_class('footnote-number'))
            content = next(n for n in node.descendants() if n.has_class('footnote-content'))
            key = '#' + number.attrs['id']
            if key in notes:
                raise ValueError('Duplicate footnote definition')
            notes[key] = pandoc(render(content), 'html', 'json')
            return ''
        if tag in {'iframe', 'video', 'audio'}:
            url = attrs.get('src') or next((n.attrs.get('src') for n in node.descendants()
                                           if n.attrs.get('src')), None)
            if url:
                url = urljoin(BASE, url)
                embeds.append(url)
                return f'<p><a href="{html.escape(url, quote=True)}">Embedded {tag}</a></p>'
        inside = ''.join(render(c) for c in node.children)
        if tag in {'figure', 'picture'} or (tag in {'div', 'section', 'span'} and not attrs.get('id')):
            return inside
        if tag == 'figcaption':
            return '<p>' + inside + '</p>'
        if tag == 'img':
            url = urljoin(BASE, attrs.get('src') or '')
            if not url.startswith('https://'):
                raise ValueError('Unrecognized image source')
            clean = {'src': local_image(url), 'alt': attrs.get('alt') or ''}
            if attrs.get('title'):
                clean['title'] = attrs['title']
        elif tag == 'a':
            if node.has_class('image-link'):
                return inside
            clean = {k: v for k, v in attrs.items() if k in {'href', 'id', 'title'} and v}
            if clean.get('href') and not clean['href'].startswith('#'):
                clean['href'] = urljoin(BASE, clean['href'])
        else:
            clean = {k: v for k, v in attrs.items() if k in {'id', 'colspan', 'rowspan', 'start'} and v}
        if not tag:
            return inside
        attributes = ''.join(f' {k}="{html.escape(v, quote=True)}"' for k, v in clean.items())
        return f'<{tag}{attributes}>' + ('' if tag in VOID else inside + f'</{tag}>')

    cleaned = render(tree)
    doc = json.loads(pandoc(cleaned, 'html', 'json'))
    used = set()

    def insert_notes(value):
        if isinstance(value, list):
            return [insert_notes(x) for x in value]
        if isinstance(value, dict):
            if value.get('t') == 'Link' and value['c'][2][0] in notes:
                key = value['c'][2][0]
                used.add(key)
                return {'t': 'Note', 'c': insert_notes(json.loads(notes[key])['blocks'])}
            return {k: insert_notes(v) for k, v in value.items()}
        return value

    doc = insert_notes(doc)
    if set(notes) != used:
        raise ValueError(f'Unreferenced footnotes: {set(notes) - used}')
    markdown = pandoc(json.dumps(doc), 'json', FORMAT).strip() + '\n'
    actual = json.loads(pandoc(markdown, FORMAT, 'json'))
    if text_signature(doc) != text_signature(actual):
        (CACHE / f'{slug}-debug.md').write_text(markdown)
        (CACHE / f'{slug}-expected.json').write_text(json.dumps(doc, ensure_ascii=False))
        (CACHE / f'{slug}-actual.json').write_text(json.dumps(actual, ensure_ascii=False))
        a, b = text_signature(doc), text_signature(actual)
        first = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        raise ValueError(f'Conversion changed article text near token {first}: {a[first:first+12]} -> {b[first:first+12]}')
    if link_signature(doc) != link_signature(actual):
        raise ValueError(f'Conversion changed links or images: {link_signature(doc) - link_signature(actual)}; extra {link_signature(actual) - link_signature(doc)}')
    return markdown, assets, embeds, len(notes), doc


def walk(value):
    if isinstance(value, dict):
        yield value
        for v in value.values():
            yield from walk(v)
    elif isinstance(value, list):
        for v in value:
            yield from walk(v)


def text_signature(doc):
    pieces = []
    for node in walk(doc['blocks']):
        if node.get('t') == 'Str':
            pieces.append(node['c'])
        elif node.get('t') in {'Code', 'CodeBlock', 'Math'}:
            pieces.append(node['c'][-1])
        elif node.get('t') in {'RawInline', 'RawBlock'} and node['c'][0] == 'html':
            pieces.append(re.sub('<[^>]*>', '', node['c'][1]))
    return re.findall(r'\w+|[^\w\s]', ' '.join(pieces))


def link_signature(doc):
    return Counter((n['t'], n['c'][2][0]) for n in walk(doc['blocks']) if n.get('t') in {'Link', 'Image'})


def frontmatter(meta):
    return '---\n' + ''.join(k + ': ' + json.dumps(v, ensure_ascii=False) + '\n' for k, v in meta.items()) + '---\n\n'


def archive_metadata(path):
    _, header, _ = path.read_text().split('---', 2)
    return {k: json.loads(v) for k, v in (line.split(':', 1) for line in header.strip().splitlines())}


def substack_paths():
    return [p for p in (ROOT / 'archived').glob('*.md')
            if str(archive_metadata(p).get('content_id', '')).startswith('substack/post/')]


def add_other_publications(lines):
    others = [p for p in (ROOT / 'archived').glob('*.md') if p not in substack_paths()]
    if not others:
        return
    lines.extend(['', '## Other published writing', '',
                  'These retain their documented earlier public versions; see frontmatter for capture provenance.', '',
                  '| Date | Article | Earlier publication |', '|---|---|---|'])
    for p in sorted(others, reverse=True):
        m = archive_metadata(p)
        title = m['title'].replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')
        lines.append(f"| {m.get('date', '')} | [{title}](archived/{p.name}) | [Source]({m['original_url']}) |")


def refresh(offline=False, fetch_only=False, reuse_pages=False):
    CACHE.mkdir(exist_ok=True)
    if offline or reuse_pages:
        listing = json.loads((CACHE / 'listing.json').read_text())
    else:
        listing = capture_listing()
        # Independent GETs only; modest concurrency limits requests to the publication.
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(capture_post, listing['posts']))
    if fetch_only:
        print(f"Fetched {len(listing['posts'])} complete public articles")
        return
    staged, rows, failures = {}, [], []
    for item in listing['posts']:
        try:
            capture = json.loads((CACHE / f"{item['id']}.json").read_text())
            post = capture['post']
            if extract_post((CACHE / f"{item['id']}.html").read_bytes())['body_html'] != post['body_html']:
                raise ValueError('Cached payload does not match retrieved page')
            markdown, assets, embeds, note_count, doc = convert(post, offline)
            meta = {'title': post['title'], 'subtitle': post.get('subtitle') or '',
                    'date': post['post_date'][:10], 'original_url': f"{BASE}/p/{post['slug']}",
                    'content_id': f"substack/post/{post['id']}",
                    'authors': [x['name'] for x in post.get('publishedBylines', [])],
                    'published_at': post['post_date'], 'source_updated_at': post.get('updated_at'),
                    'archived_at': capture['captured_at'],
                    'source_body_sha256': digest(post['body_html'].encode())}
            filename = f"{post['post_date'][:10]}-{post['slug']}.md"
            if filename in staged:
                raise ValueError('Duplicate archive filename')
            staged[filename] = frontmatter(meta) + markdown
            rows.append({'id': post['id'], 'file': 'archived/' + filename, 'title': post['title'],
                         'url': meta['original_url'], 'date': meta['date'], 'images': len(assets),
                         'footnotes': note_count, 'embeds': embeds,
                         'text_tokens': len(text_signature(doc))})
            print(f"Verified {filename}", flush=True)
        except Exception as error:
            failures.append({'id': item['id'], 'slug': item['slug'], 'error': str(error)})
            print(f"FAILED {item['slug']}: {error}", flush=True)
    report = {'listing_captured_at': listing['captured_at'], 'listed': len(listing['posts']),
              'converted': len(rows), 'failures': failures, 'posts': rows}
    (CACHE / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if failures:
        raise SystemExit(f'{len(failures)} conversion failures; existing Markdown has not been replaced')
    old_files = {p.name for p in substack_paths()}
    extras = old_files - set(staged)
    if extras:
        raise SystemExit(f'Existing files absent from live listing; review before changing anything: {sorted(extras)}')
    for filename, data in staged.items():
        (ROOT / 'archived' / filename).write_text(data)
    lines = ['# Substack archive', '',
             f"Captured {len(rows)} posts from the complete public Data Leverage listing on {listing['captured_at'][:10]}.",
             'Every listed post has a full retrieved body and a Markdown file. No failed or skipped posts.', '',
             '| Date | Article | Source |', '|---|---|---|']
    for row in sorted(rows, key=lambda x: (x['date'], x['id']), reverse=True):
        title = row['title'].replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')
        lines.append(f"| {row['date']} | [{title}]({row['file']}) | [Substack]({row['url']}) |")
    add_other_publications(lines)
    (ROOT / 'INDEX.md').write_text('\n'.join(lines) + '\n')
    check()


def check():
    report = json.loads((CACHE / 'report.json').read_text())
    listing = json.loads((CACHE / 'listing.json').read_text())
    assert not report['failures'], report['failures']
    assert {p['id'] for p in report['posts']} == {p['id'] for p in listing['posts']}
    ids = set()
    for row in report['posts']:
        path = ROOT / row['file']
        text = path.read_text()
        _, header, body = text.split('---', 2)
        meta = {k: json.loads(v) for k, v in (line.split(':', 1) for line in header.strip().splitlines())}
        assert meta['content_id'] not in ids
        ids.add(meta['content_id'])
        capture = json.loads((CACHE / f"{row['id']}.json").read_text())
        expected, _, _, _, _ = convert(capture['post'], offline=True)
        assert body.strip() == expected.strip(), f'Article differs from source conversion: {path}'
        assert meta['source_body_sha256'] == digest(capture['post']['body_html'].encode())
        doc = json.loads(pandoc(body, FORMAT, 'json'))
        for node in walk(doc['blocks']):
            if node.get('t') == 'Image':
                url = node['c'][2][0]
                assert not urlsplit(url).scheme, f'Remote image: {url}'
                assert (path.parent / url).is_file(), f'Missing image: {url}'
    assert len(substack_paths()) == len(ids)
    print(f'PASS: {len(ids)} Substack posts; complete listing coverage; unique IDs; source text/link round-trips; local images; footnotes')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['refresh', 'check'])
    parser.add_argument('--offline', action='store_true', help='Reuse the last captured listing and article pages')
    parser.add_argument('--fetch-only', action='store_true', help='Capture all pages without replacing Markdown')
    parser.add_argument('--reuse-pages', action='store_true', help='Reuse captured article pages, fetching any missing images')
    args = parser.parse_args()
    if args.command == 'check':
        check()
    else:
        refresh(args.offline, args.fetch_only, args.reuse_pages)
