#!/usr/bin/env python3
"""Build a metadata-only Standard.site index; remote writes require --apply."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import secrets
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = 'site/standard-site.json'
PUBLICATION = 'site.standard.publication'
DOCUMENT = 'site.standard.document'
TID = re.compile(r'[234567abcdefghij][234567abcdefghijklmnopqrstuvwxyz]{12}')


def https_url(value):
    parsed = urlsplit(value)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ValueError('Expected a public HTTPS URL without credentials, query, or fragment')
    return value.rstrip('/')


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', str(value)):
                raise ValueError('Datetime needs a timezone')
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
    except (TypeError, ValueError):
        raise ValueError(f'Indexed articles need a valid date (YYYY-MM-DD or timezone-aware datetime): {value!r}') from None


def selected(post):
    setting = post['meta'].get('atproto')
    if setting is not None and not isinstance(setting, bool):
        raise ValueError(f'atproto must be a YAML boolean: {post["source"]}')
    return setting if setting is not None else post['section'] == 'archive'


def read_registry(root):
    path = root / REGISTRY
    if not path.exists():
        return None
    registry = json.loads(path.read_text())
    if registry.get('version') != 1 or not re.fullmatch(r'did:plc:[a-z2-7]{24}|did:web:[a-zA-Z0-9.-]+', registry.get('did', '')):
        raise ValueError('Invalid Standard.site registry version or DID')
    keys = [registry['publication_rkey'], *registry['documents'].values()]
    if any(not isinstance(key, str) or not TID.fullmatch(key) for key in keys) or len(keys) != len(set(keys)):
        raise ValueError('Standard.site registry requires unique, valid TID record keys')
    https_url(registry['url'])
    return registry


def new_tid(used):
    alphabet = '234567abcdefghijklmnopqrstuvwxyz'
    while True:
        value = (time.time_ns() // 1000 << 10) | secrets.randbelow(1024)
        result = ''.join(alphabet[(value >> shift) & 31] for shift in range(60, -1, -5))
        if result not in used:
            used.add(result)
            return result


def register(root=ROOT, did=None):
    from build_garden import load_posts, load_permalinks, assign_permalinks
    config = json.loads((root / 'site/garden.json').read_text())
    posts = load_posts(root)
    assign_permalinks(posts, load_permalinks(root))
    registry = read_registry(root)
    if registry is None:
        if not did:
            raise ValueError('First run requires register --did YOUR_PUBLIC_DID')
        registry = {'version': 1, 'did': did, 'url': https_url(config['url']),
                    'publication_rkey': new_tid(set()), 'documents': {}}
    elif did and did != registry['did']:
        raise ValueError('The registered account cannot be changed by registration')
    used = {registry['publication_rkey'], *registry['documents'].values()}
    added = 0
    for post in posts:
        if selected(post):
            timestamp(post['meta'].get('date'))
            identity = post['meta']['content_id']
            if identity not in registry['documents']:
                registry['documents'][identity] = new_tid(used)
                added += 1
    # Validate everything before writing; removed IDs remain reserved for safe restoration.
    make_index(config, posts, registry)
    (root / REGISTRY).write_text(json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + '\n')
    print(f'Registered {added} article identities locally. No network requests or publishing.')


def checked_text(value, maximum, field):
    if not isinstance(value, str) or len(value) > maximum:
        raise ValueError(f'{field} must be text of at most {maximum} characters')
    return value


def make_index(config, posts, registry):
    base = https_url(config['url'])
    if base != registry['url']:
        raise ValueError('Garden URL changed; review the Standard.site publication migration first')
    did = registry['did']
    if not re.fullmatch(r'did:plc:[a-z2-7]{24}|did:web:[a-zA-Z0-9.-]+', did):
        raise ValueError('Invalid Standard.site DID')
    def uri(collection, key):
        return f'at://{did}/{collection}/{key}'
    publication_uri = uri(PUBLICATION, registry['publication_rkey'])
    index = {'version': 1, 'did': did, 'publication': {
        'uri': publication_uri,
        'record': {'$type': PUBLICATION, 'url': base,
                   'name': checked_text(config['title'], 500, 'Publication name'),
                   'preferences': {'showInDiscover': True}},
    }, 'documents': []}
    for post in sorted(posts, key=lambda p: p['meta']['content_id']):
        if not selected(post):
            continue
        meta = post['meta']
        identity = meta['content_id']
        if identity not in registry['documents']:
            raise ValueError(f'Unregistered atproto article: {identity}; run make register-urls')
        record = {'$type': DOCUMENT, 'site': publication_uri, 'path': '/' + post['route'],
                  'title': checked_text(meta['title'], 500, 'Title'),
                  'publishedAt': timestamp(meta.get('date'))}
        description = meta.get('subtitle') or meta.get('summary') or ''
        if post['section'] == 'drafts':
            description = 'Public draft. ' + description
        if description:
            record['description'] = checked_text(description.strip(), 3000, 'Description')
        if meta.get('updated_at'):
            record['updatedAt'] = timestamp(meta['updated_at'])
        if meta.get('tags'):
            if not isinstance(meta['tags'], list):
                raise ValueError(f'Tags must be a list: {post["source"]}')
            record['tags'] = [checked_text(tag, 128, 'Tag').lstrip('#') for tag in meta['tags']]
        index['documents'].append({'content_id': identity,
                                   'uri': uri(DOCUMENT, registry['documents'][identity]), 'record': record})
    return index


def build_index(root, config, posts):
    registry = read_registry(root)
    return make_index(config, posts, registry) if registry else None


def verification_path(base):
    return '.well-known/site.standard.publication' + urlsplit(base).path.rstrip('/')


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('Unexpected HTTP redirect; no credentials were forwarded')


class Client:
    """No token persistence, automatic retries, or response-body error logging."""
    def __init__(self):
        self.opener = build_opener(NoRedirect())

    def request(self, url, data=None, token=None):
        # Queries are allowed on XRPC reads, but credentials only go to HTTPS.
        https_url(url.split('?', 1)[0])
        headers = {'Accept': 'application/json', 'User-Agent': 'DataLeverage-StandardSite/1'}
        if token:
            headers['Authorization'] = 'Bearer ' + token
        if data is not None:
            headers['Content-Type'] = 'application/json'
        request = Request(url, data=json.dumps(data).encode() if data is not None else None, headers=headers)
        try:
            with self.opener.open(request, timeout=30) as response:
                return response.read().decode()
        except HTTPError as error:
            raise ValueError(f'HTTP {error.code} from {urlsplit(url).hostname}; request failed') from None
        except URLError:
            raise ValueError(f'Connection failed to {urlsplit(url).hostname}') from None

    def json(self, url, data=None, token=None):
        return json.loads(self.request(url, data, token))


def resolve_pds(client, did):
    url = 'https://plc.directory/' + did if did.startswith('did:plc:') else 'https://' + did.removeprefix('did:web:') + '/.well-known/did.json'
    document = client.json(url)
    if document.get('id') != did:
        raise ValueError('DID resolution returned a different identity')
    for service in document.get('service', []):
        if service.get('type') == 'AtprotoPersonalDataServer' and service.get('id') in {'#atproto_pds', did + '#atproto_pds'}:
            return https_url(service['serviceEndpoint'])
    raise ValueError('No PDS found in the public DID document')


def list_records(client, service, did, collection):
    result, seen, cursor = {}, set(), None
    while True:
        query = {'repo': did, 'collection': collection, 'limit': 100}
        if cursor:
            query['cursor'] = cursor
        page = client.json(service + '/xrpc/com.atproto.repo.listRecords?' + urlencode(query))
        for item in page['records']:
            result[item['uri']] = item
        cursor = page.get('cursor')
        if not cursor:
            return result
        if cursor in seen:
            raise ValueError('Repeated record-list cursor')
        seen.add(cursor)


def remote_changes(index, remote):
    publication = index['publication']
    publication_uri = publication['uri']
    for item in remote.values():
        value = item['value']
        if value.get('$type') == PUBLICATION and value.get('url', '').rstrip('/') == publication['record']['url'] and item['uri'] != publication_uri:
            raise ValueError('A garden publication already exists at another URI; adopt its identity before syncing')
    changes = []
    entries = [publication, *index['documents']]
    for entry in entries:
        record, uri = entry['record'], entry['uri']
        old = remote.get(uri)
        value = old['value'] if old else {}
        field = 'url' if record['$type'] == PUBLICATION else 'site'
        if old and (value.get('$type') != record['$type'] or value.get(field) != record[field]):
            raise ValueError('Refusing to overwrite a record owned by another publication: ' + uri)
        # Preserve optional additions made by other clients, such as a discussion reference.
        merged = dict(value)
        for managed in record.keys() | ({'description', 'tags', 'updatedAt'} if record['$type'] == DOCUMENT else set()):
            merged.pop(managed, None)
        merged.update(record)
        if not old or merged != value:
            changes.append({'uri': uri, 'record': merged, 'previous_cid': old['cid'] if old else None})
    desired = {entry['uri'] for entry in entries}
    retained = [uri for uri, item in remote.items() if item['value'].get('site') == publication_uri and uri not in desired]
    return changes, retained


class StandardLinks(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.documents = []; self.in_head = False; self.feed(text)
    def handle_starttag(self, tag, attrs):
        if tag == 'head': self.in_head = True
        attrs = dict(attrs)
        if self.in_head and tag == 'link' and attrs.get('rel') == DOCUMENT:
            self.documents.append(attrs.get('href'))
    def handle_endtag(self, tag):
        if tag == 'head': self.in_head = False


def verify_deployed(client, index, source_commit):
    base = index['publication']['record']['url']
    manifest = client.json(base + '/manifest.json')
    if manifest.get('source_commit') != source_commit or manifest.get('source_dirty') is not False:
        raise ValueError('Deploy this clean source revision before publishing its atproto index')
    if client.json(base + '/atproto-index.json') != index:
        raise ValueError('Deployed atproto index differs from the local build')
    origin = urlsplit(base)
    endpoint = f'{origin.scheme}://{origin.netloc}/' + verification_path(base)
    if client.request(endpoint).strip() != index['publication']['uri']:
        raise ValueError('Deployed publication verification does not match')
    for entry in index['documents']:
        page = client.request(base + entry['record']['path'])
        if StandardLinks(page).documents != [entry['uri']]:
            raise ValueError('Deployed document verification does not match: ' + entry['record']['path'])


def wait_for_deployment(client, index, source_commit, seconds):
    deadline = time.monotonic() + seconds
    while True:
        try:
            verify_deployed(client, index, source_commit)
            return
        except ValueError as error:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ValueError(f'{error}. No atproto writes were made; retry make atproto-sync after Pages is ready.') from None
            print('Waiting for the deployed garden to match this revision…', flush=True)
            time.sleep(min(10, remaining))


def clean_pushed_commit(root, config):
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=root, text=True).strip()
    if git('status', '--porcelain'):
        raise ValueError('Commit the reviewed blogs changes before syncing atproto')
    commit = git('rev-parse', 'HEAD')
    remote = git('ls-remote', 'origin', 'refs/heads/' + config['source_branch']).split()
    if not remote or remote[0] != commit:
        raise ValueError('Sync requires the current pushed source revision on ' + config['source_branch'])
    return commit


def apply_changes(client, service, did, changes):
    if not changes:
        return
    password = os.environ.get('ATPROTO_APP_PASSWORD')
    if not password:
        raise ValueError('Set ATPROTO_APP_PASSWORD in the process environment for explicit syncing')
    session = client.json(service + '/xrpc/com.atproto.server.createSession', {'identifier': did, 'password': password})
    if session.get('did') != did:
        raise ValueError('Authenticated account does not match the registered DID')
    token = session['accessJwt']
    for change in changes:
        collection, key = change['uri'].rsplit('/', 2)[-2:]
        result = client.json(service + '/xrpc/com.atproto.repo.putRecord', {
            'repo': did, 'collection': collection, 'rkey': key, 'record': change['record'],
            'swapRecord': change['previous_cid'],
        }, token)
        if result.get('uri') != change['uri']:
            raise ValueError('PDS returned an unexpected record URI; stop and inspect before retrying')
        print('Synced ' + change['uri'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['register', 'preview', 'sync'])
    parser.add_argument('--did', help='Public account DID, for initial local registration only')
    parser.add_argument('--apply', action='store_true', help='Explicitly publish after checking the deployed site')
    parser.add_argument('--wait-seconds', type=int, default=180,
                        help='Maximum retry window for deployed verification before live syncing (default: 180)')
    args = parser.parse_args()
    if args.wait_seconds < 0 or args.wait_seconds > 600:
        parser.error('--wait-seconds must be between 0 and 600')
    if args.apply and args.command != 'sync':
        parser.error('--apply is only valid with sync')
    if args.did and args.command != 'register':
        parser.error('--did is only valid with register')
    if args.command == 'register':
        register(did=args.did)
        return
    from build_garden import build
    config = json.loads((ROOT / 'site/garden.json').read_text())
    commit = clean_pushed_commit(ROOT, config) if args.apply else None
    build()
    path = ROOT / '_site/atproto-index.json'
    if not path.exists():
        raise ValueError('Run register --did YOUR_PUBLIC_DID first')
    index = json.loads(path.read_text())
    print(f'{len(index["documents"])} metadata-only articles → {index["publication"]["record"]["url"]}')
    if args.command == 'preview':
        for entry in index['documents']:
            print(entry['record']['path'] + ' — ' + entry['record']['title'])
        print('Offline preview: ' + str(path))
        return
    client = Client()
    service = resolve_pds(client, index['did'])
    remote = {}
    for collection in [PUBLICATION, DOCUMENT]:
        remote.update(list_records(client, service, index['did'], collection))
    changes, retained = remote_changes(index, remote)
    print(f'{len(changes)} records to create/update; {len(retained)} older garden records retained (never automatically deleted).')
    for uri in retained:
        print('Review retained record: ' + uri)
    if args.apply:
        wait_for_deployment(client, index, commit, args.wait_seconds)
        apply_changes(client, service, index['did'], changes)
        print('Index sync complete. No Leaflet records or Bluesky announcements were changed.')
    else:
        print('Read-only comparison. Use sync --apply only after reviewing and deploying this source revision.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error)) from None
