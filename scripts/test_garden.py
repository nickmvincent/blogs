import json
from pathlib import Path
import tempfile
import unittest

from build_garden import load_posts, public_asset, check_links


class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        for name in ['archived','drafts','private','media']:(self.root/name).mkdir()

    def article(self, folder, name, extra=''):
        p=self.root/folder/name
        p.write_text('---\ntitle: Test\ncontent_id: test/'+name+'\n'+extra+'---\n\nBody\n\n---\n\nThis is a rule, not YAML.\n')
        return p

    def test_only_public_inputs_and_body_rules(self):
        self.article('archived','one.md')
        self.article('drafts','two.md','visibility: public\n')
        self.article('private','secret.md')
        self.assertEqual(len(load_posts(self.root)),2)

    def test_drafts_require_explicit_public_visibility(self):
        self.article('drafts','one.md')
        with self.assertRaisesRegex(ValueError,'visibility: public'):load_posts(self.root)

    def test_article_symlinks_are_rejected(self):
        hidden=self.article('private','secret.md')
        (self.root/'archived/alias.md').symlink_to(hidden)
        with self.assertRaisesRegex(ValueError,'symlinks'):load_posts(self.root)

    def test_assets_cannot_escape_media(self):
        source=self.article('drafts','one.md','visibility: public\n')
        self.article('private','secret.md')
        with self.assertRaisesRegex(ValueError,'inside media'):public_asset(self.root,source,'../private/secret.md')
        (self.root/'media/trick.txt').symlink_to(self.root/'private/secret.md')
        with self.assertRaisesRegex(ValueError,'inside media'):public_asset(self.root,source,'../media/trick.txt')

    def test_broken_fragment_fails_validation(self):
        (self.root/'index.html').write_text('<a href="#missing">Broken</a>')
        with self.assertRaisesRegex(ValueError,'fragment'):check_links(self.root)


if __name__=='__main__':unittest.main()
