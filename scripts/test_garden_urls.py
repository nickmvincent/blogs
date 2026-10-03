import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from build_garden import build, load_permalinks, register_permalinks


class StableURLTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ['drafts', 'archived', 'private', 'media', 'site']:
            (self.root / folder).mkdir()
        self.config = {
            'url': 'https://example.test', 'source_url': 'https://example.test/source',
            'source_branch': 'main', 'redirects': {},
        }
        self.save_config()
        for name in ['site.css', 'search.js', 'analytics.css', 'words.js', 'links.js']:
            (self.root / 'site' / name).write_text('')

    def save_config(self):
        (self.root / 'site/garden.json').write_text(json.dumps(self.config))

    def article(self, slug, body='Article body.'):
        path = self.root / 'drafts' / (slug + '.md')
        path.write_text(f'---\ntitle: First title\ncontent_id: test/{slug}\n'
                        f'slug: {slug}\nvisibility: public\n---\n\n{body}\n')
        return path

    def run_quietly(self, function):
        with contextlib.redirect_stdout(io.StringIO()):
            function(self.root)

    def test_title_filename_slug_and_section_changes_keep_registered_url(self):
        source = self.article('original')
        self.run_quietly(register_permalinks)
        self.run_quietly(build)
        registry_before = (self.root / 'site/permalinks.json').read_bytes()
        source.write_text(source.read_text().replace('First title', 'New title').replace('slug: original', 'slug: different'))
        source.rename(self.root / 'archived/renamed-file.md')
        self.run_quietly(register_permalinks)
        self.run_quietly(build)
        self.assertEqual((self.root / 'site/permalinks.json').read_bytes(), registry_before)
        page = (self.root / '_site/p/original.html').read_text()
        self.assertIn('New title', page)
        self.assertIn('https://example.test/p/original.html', page)
        self.assertFalse((self.root / '_site/p/different.html').exists())
        for section in ['drafts', 'archive']:
            self.assertIn('url=/p/original.html', (self.root / f'_site/{section}/original.html').read_text())
        results = json.loads((self.root / '_site/search-index.json').read_text())
        self.assertEqual(results[0]['url'], '/p/original.html')
        self.assertEqual(results[0]['section'], 'archive')

    def test_new_article_requires_explicit_url_registration(self):
        self.article('new')
        with self.assertRaisesRegex(ValueError, 'make register-urls'):
            self.run_quietly(build)

    def test_duplicate_permalink_is_rejected(self):
        (self.root / 'site/permalinks.json').write_text(json.dumps({
            'test/one': 'p/same.html', 'test/two': 'p/same.html',
        }))
        with self.assertRaisesRegex(ValueError, 'Duplicate permalink'):
            load_permalinks(self.root)

    def test_withdrawal_removes_old_content_and_search_but_preserves_notice(self):
        removed = self.article('removed', 'Distinctive private sentence 8731. [Reference](https://removed.example/)')
        self.article('remaining')
        self.run_quietly(register_permalinks)
        self.run_quietly(build)
        removed.rename(self.root / 'private/removed.md')
        registry = load_permalinks(self.root)
        registry.pop('test/removed')
        (self.root / 'site/permalinks.json').write_text(json.dumps(registry))
        self.config['withdrawn_routes'] = ['p/removed.html', 'drafts/removed.html', 'archive/removed.html']
        self.save_config()
        self.run_quietly(build)
        for path in (self.root / '_site').rglob('*'):
            if path.is_file():
                self.assertNotIn('Distinctive private sentence 8731.', path.read_text())
        results = json.loads((self.root / '_site/search-index.json').read_text())
        self.assertEqual(len(results), 1)
        for name in ['word', 'link']:
            index = (self.root / f'_site/data/{name}-index.json').read_text()
            self.assertNotIn('removed', index)
            self.assertNotIn('distinctive', index)
            page = (self.root / f'_site/{name}s.html').read_text()
            self.assertNotIn('http-equiv="refresh"', page)
            self.assertIn(f'/{name}s.js', page)
        for route in self.config['withdrawn_routes']:
            notice = (self.root / '_site' / route).read_text()
            self.assertIn('Page unavailable', notice)
            self.assertIn('content="noindex"', notice)
        self.article('removed', 'Attempt to reuse retired URL.')
        with self.assertRaisesRegex(ValueError, 'already reserved'):
            self.run_quietly(register_permalinks)


if __name__ == '__main__':
    unittest.main()
