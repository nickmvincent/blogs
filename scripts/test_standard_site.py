import contextlib
import copy
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from build_garden import build, register_permalinks
from standard_site import (Client, DOCUMENT, PUBLICATION, NoRedirect, StandardLinks,
                           apply_changes, clean_pushed_commit, list_records, read_registry,
                           register, remote_changes, resolve_pds, timestamp, verify_deployed,
                           wait_for_deployment)

DID = 'did:plc:doxvahqvyhyqf32v7wz7p5xk'


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ['site', 'archived', 'drafts', 'private']:
            (self.root / name).mkdir()
        self.config = {'title': 'Test garden', 'url': 'https://example.test',
                       'source_url': 'https://example.test/source', 'source_branch': 'main'}
        (self.root / 'site/garden.json').write_text(json.dumps(self.config))
        for name in ['site.css', 'search.js', 'analytics.css', 'words.js', 'links.js']:
            (self.root / 'site' / name).write_text('')
        self.article('archived', 'one')

    def article(self, folder, name, extra=''):
        source = self.root / folder / (name + '.md')
        source.write_text(f'---\ntitle: Article {name}\ncontent_id: test/{name}\nslug: {name}\n'
                          'date: 2026-09-20\nsummary: A brief summary.\n' + extra +
                          '---\n\nBODY-ONLY-MARKER not for the atproto record.\n')
        return source

    def prepare(self):
        with contextlib.redirect_stdout(io.StringIO()):
            register_permalinks(self.root)
            register(self.root, DID)
            build(self.root)
        return json.loads((self.root / '_site/atproto-index.json').read_text())

    def test_selection_metadata_and_verification(self):
        self.article('drafts', 'draft', 'visibility: public\n')
        self.article('drafts', 'opted-in', 'visibility: public\natproto: true\n')
        self.article('archived', 'opted-out', 'atproto: false\n')
        self.article('private', 'secret', 'visibility: private\n')
        index = self.prepare()
        self.assertEqual({x['content_id'] for x in index['documents']}, {'test/one', 'test/opted-in'})
        self.assertNotIn('BODY-ONLY-MARKER', json.dumps(index))
        self.assertNotIn('secret', json.dumps(index))
        self.assertEqual((self.root / '_site/.well-known/site.standard.publication').read_text().strip(), index['publication']['uri'])
        for entry in index['documents']:
            record = entry['record']
            self.assertNotIn('content', record)
            self.assertNotIn('textContent', record)
            self.assertEqual(record['publishedAt'], '2026-09-20T00:00:00.000Z')
            html = (self.root / '_site' / record['path'].lstrip('/')).read_text()
            self.assertEqual(StandardLinks(html).documents, [entry['uri']])
        self.assertIn('Public draft.', index['documents'][1]['record']['description'])
        for slug in ['draft', 'opted-out']:
            self.assertEqual(StandardLinks((self.root / f'_site/p/{slug}.html').read_text()).documents, [])

    def test_identity_survives_rename_edit_and_section_change(self):
        original = self.prepare()
        source = self.root / 'archived/one.md'
        text = source.read_text().replace('Article one', 'Changed title').replace('slug: one', 'slug: renamed')
        source.unlink()
        (self.root / 'drafts/renamed.md').write_text(text.replace('date:', 'visibility: public\natproto: true\ndate:'))
        changed = self.prepare()
        self.assertEqual(changed['documents'][0]['uri'], original['documents'][0]['uri'])
        self.assertEqual(changed['documents'][0]['record']['path'], '/p/one.html')
        self.assertEqual(changed['documents'][0]['record']['title'], 'Changed title')
        self.assertEqual(changed, self.prepare())

    def test_withdrawn_article_loses_verification_but_keeps_reserved_identity(self):
        self.article('archived', 'remaining')
        original = self.prepare()
        keys = read_registry(self.root)['documents']
        (self.root / 'archived/one.md').rename(self.root / 'private/one.md')
        current = self.prepare()
        self.assertEqual(read_registry(self.root)['documents'], keys)
        self.assertEqual(len(current['documents']), 1)
        self.assertFalse((self.root / '_site/p/one.html').exists())
        self.assertNotEqual(original, current)

    def test_invalid_date_and_non_boolean_opt_in_fail_before_registry_write(self):
        source = self.root / 'archived/one.md'
        source.write_text(source.read_text().replace('2026-09-20', 'not-a-date'))
        with self.assertRaisesRegex(ValueError, 'valid date'):
            self.prepare()
        self.assertFalse((self.root / 'site/standard-site.json').exists())
        self.article('archived', 'one', 'atproto: "false"\n')
        with self.assertRaisesRegex(ValueError, 'YAML boolean'):
            self.prepare()

    def test_registration_is_required_and_did_cannot_silently_change(self):
        self.prepare()
        self.article('archived', 'new')
        with contextlib.redirect_stdout(io.StringIO()):
            register_permalinks(self.root)
        with self.assertRaisesRegex(ValueError, 'Unregistered atproto'):
            build(self.root)
        with self.assertRaisesRegex(ValueError, 'account cannot be changed'):
            register(self.root, 'did:plc:aaaaaaaaaaaaaaaaaaaaaaaa')

    def test_sync_noops_preserves_extras_and_reports_retired_records(self):
        index = self.prepare()
        remote = {entry['uri']: {'uri': entry['uri'], 'cid': 'old-cid', 'value': copy.deepcopy(entry['record'])}
                  for entry in [index['publication'], *index['documents']]}
        entry = index['documents'][0]
        remote[entry['uri']]['value']['bskyPostRef'] = {'uri': 'at://example/post/one', 'cid': 'discussion-cid'}
        legacy_uri = f'at://{DID}/{DOCUMENT}/3lzrsw2kvwc2m'
        remote[legacy_uri] = {'uri': legacy_uri, 'cid': 'leaflet-cid',
                              'value': {'$type': DOCUMENT, 'site': 'at://leaflet/publication/old', 'content': {'text': 'untouched'}}}
        changes, retained = remote_changes(index, remote)
        self.assertEqual((changes, retained), ([], []))
        entry['record']['title'] = 'Updated metadata'
        changes, retained = remote_changes(index, remote)
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]['previous_cid'], 'old-cid')
        self.assertIn('bskyPostRef', changes[0]['record'])
        self.assertNotIn('content', changes[0]['record'])
        index['documents'] = []
        self.assertEqual(remote_changes(index, remote)[1], [entry['uri']])

    def test_conflicting_record_and_duplicate_publication_are_rejected(self):
        index = self.prepare()
        entry = index['documents'][0]
        foreign = {'uri': entry['uri'], 'cid': 'cid', 'value': {'$type': DOCUMENT, 'site': 'at://foreign/pub/one'}}
        with self.assertRaisesRegex(ValueError, 'another publication'):
            remote_changes(index, {entry['uri']: foreign})
        duplicate = {'uri': 'at://another/publication/one', 'cid': 'cid', 'value': index['publication']['record']}
        with self.assertRaisesRegex(ValueError, 'already exists'):
            remote_changes(index, {duplicate['uri']: duplicate})

    def test_deployed_content_and_verification_are_checked(self):
        index = self.prepare()
        base = self.config['url']
        values = {base + '/manifest.json': json.dumps({'source_commit': 'abc', 'source_dirty': False}),
                  base + '/atproto-index.json': json.dumps(index),
                  base + '/.well-known/site.standard.publication': index['publication']['uri']}
        entry = index['documents'][0]
        page_url = base + entry['record']['path']
        values[page_url] = '<html><head><link rel="site.standard.document" href="' + entry['uri'] + '"></head></html>'
        client = Client()
        with patch.object(client, 'request', side_effect=lambda url, data=None, token=None: values[url]):
            verify_deployed(client, index, 'abc')
            values[page_url] = '<head></head><body><link rel="site.standard.document" href="' + entry['uri'] + '"></body>'
            with self.assertRaisesRegex(ValueError, 'document verification'):
                verify_deployed(client, index, 'abc')
            with self.assertRaisesRegex(ValueError, 'Deploy this clean source'):
                verify_deployed(client, index, 'wrong-revision')


class NetworkBoundaryTests(unittest.TestCase):
    def test_pages_propagation_retries_and_times_out_without_publishing(self):
        with patch('standard_site.verify_deployed', side_effect=[ValueError('old revision'), None]) as verify, \
                patch('standard_site.time.sleep') as sleep, \
                patch('standard_site.time.monotonic', side_effect=[0, 1]), \
                contextlib.redirect_stdout(io.StringIO()):
            wait_for_deployment(None, {}, 'revision', 20)
            self.assertEqual(verify.call_count, 2)
            sleep.assert_called_once_with(10)
        with patch('standard_site.verify_deployed', side_effect=ValueError('old revision')), \
                patch('standard_site.time.sleep') as sleep:
            with self.assertRaisesRegex(ValueError, 'No atproto writes were made'):
                wait_for_deployment(None, {}, 'revision', 0)
            sleep.assert_not_called()

    def test_date_conversion_rejects_ambiguous_datetimes(self):
        self.assertEqual(timestamp('2026-09-20T01:00:00-07:00'), '2026-09-20T08:00:00.000Z')
        with self.assertRaises(ValueError): timestamp('2026-09-20T01:00:00')

    def test_noop_needs_no_credentials_and_writes_use_compare_and_swap(self):
        client = Client()
        with patch.dict(os.environ, {}, clear=True), patch.object(client, 'json') as request:
            apply_changes(client, 'https://pds.test', DID, [])
            request.assert_not_called()
        uri = f'at://{DID}/{DOCUMENT}/3lzrsw2kvwc2m'
        change = {'uri': uri, 'record': {'$type': DOCUMENT}, 'previous_cid': None}
        with patch.dict(os.environ, {'ATPROTO_APP_PASSWORD': 'test-secret'}), patch.object(client, 'json') as request:
            request.side_effect = [{'did': DID, 'accessJwt': 'test-token'}, {'uri': uri}]
            with contextlib.redirect_stdout(io.StringIO()) as output:
                apply_changes(client, 'https://pds.test', DID, [change])
            data = request.call_args_list[1].args[1]
            self.assertIn('swapRecord', data)
            self.assertIsNone(data['swapRecord'])
            self.assertEqual(data['rkey'], '3lzrsw2kvwc2m')
            self.assertNotIn('test-secret', output.getvalue())
            self.assertNotIn('test-token', output.getvalue())
            request.reset_mock()
            request.side_effect = [{'did': 'did:plc:other', 'accessJwt': 'test-token'}]
            with self.assertRaisesRegex(ValueError, 'does not match'):
                apply_changes(client, 'https://pds.test', DID, [change])
            self.assertEqual(request.call_count, 1)

    def test_pds_resolution_is_bound_to_identity_and_https(self):
        client = Client()
        with patch.object(client, 'json', return_value={'id': DID, 'service': [
                {'id': '#atproto_pds', 'type': 'AtprotoPersonalDataServer', 'serviceEndpoint': 'https://pds.test'}]}):
            self.assertEqual(resolve_pds(client, DID), 'https://pds.test')
        with patch.object(client, 'json', return_value={'id': 'wrong'}):
            with self.assertRaisesRegex(ValueError, 'different identity'): resolve_pds(client, DID)
        with self.assertRaisesRegex(ValueError, 'HTTPS'):
            client.request('http://pds.test', token='test-token')
        with self.assertRaisesRegex(ValueError, 'redirect'):
            NoRedirect().redirect_request(None, None, 302, '', {}, 'https://another.test')

    def test_pagination_and_dirty_checkout_gate(self):
        client = Client()
        with patch.object(client, 'json', side_effect=[{'records': [], 'cursor': 'next'},
                {'records': [{'uri': 'second-page', 'value': {}}]}]) as request:
            self.assertIn('second-page', list_records(client, 'https://pds.test', DID, DOCUMENT))
            self.assertIn('cursor=next', request.call_args.args[0])
        with patch('standard_site.subprocess.check_output', return_value=' M README.md\n') as git:
            with self.assertRaisesRegex(ValueError, 'Commit the reviewed'):
                clean_pushed_commit(Path('.'), {'source_branch': 'main'})
            self.assertEqual(git.call_count, 1)


if __name__ == '__main__':
    unittest.main()
