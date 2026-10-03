import unittest

from garden_analytics import (ArticleLinks, build_link_index, build_word_index,
                              canonicalize_url, ngrams_for_tokens,
                              render_link_index_page, render_word_index_page)


def article(name, text='', links=None):
    return {'title': name, 'text': text, 'source': f'archived/{name}.md',
            'href': f'/p/{name}.html', 'slug': name, 'date': '2026-10-02',
            'category': 'Archive', 'links': links or []}


class AnalyticsTests(unittest.TestCase):
    def test_frequency_counts_article_counts_and_adjacent_phrases(self):
        index = build_word_index([
            article('First', 'data leverage data leverage data leverage'),
            article('Second', 'data leverage and data leverage'),
        ])
        terms = {row['phrase']: row for row in index['terms']}
        self.assertEqual(terms['data']['count'], 5)
        self.assertEqual(terms['data leverage']['count'], 5)
        self.assertEqual(terms['data leverage']['articleCount'], 2)
        self.assertEqual(terms['data leverage']['topArticle']['href'], '/p/First.html')
        self.assertEqual(ngrams_for_tokens(['data', 'and', 'leverage'], 2), [])
        self.assertNotIn('and', terms)
        self.assertIn('/p/First.html', render_word_index_page(index))

    def test_outbound_anchors_include_footnotes_but_not_local_links_or_images(self):
        parsed = ArticleLinks('''<p><a href="https://source.example/p?id=7&amp;utm_source=x">A <em>study</em></a>
            <a href="/p/local.html">Local</a><a href="#fn1">1</a>
            <a href="https://garden.example/p/local.html">Garden</a>
            <img src="https://images.example/p.png">
            <a href="mailto:hello@example.test">Email</a></p>
            <aside><a href="https://source.example/p?id=7">Footnote</a></aside>''',
            'https://garden.example')
        self.assertEqual(len(parsed.links), 2)
        self.assertEqual(parsed.links[0]['label'], 'A study')
        index = build_link_index([article('First', links=parsed.links)])
        self.assertEqual(index['totalLinks'], 2)
        self.assertEqual(index['totalDomains'], 1)
        record = index['links'][0]
        self.assertEqual(record['canonicalUrl'], 'https://source.example/p?id=7')
        self.assertIn('duplicate-in-article', record['issueCodes'])
        self.assertTrue(any('tracking-query' in x['issueCodes'] for x in index['links']))
        self.assertIn('/p/First.html', render_link_index_page(index))

    def test_tracking_normalization_retains_functional_parameters_and_safe_markup(self):
        self.assertEqual(canonicalize_url('http://www.example.test/path/?q=a&empty=&utm_source=x#part'),
                         'https://example.test/path?empty=&q=a')
        links = [{'url': 'http://example.test/?q=a&sort=date', 'label': '<script>bad</script>'}]
        index = build_link_index([article('First', links=links)])
        self.assertNotIn('tracking-query', index['links'][0]['issueCodes'])
        self.assertIn('insecure-http', index['links'][0]['issueCodes'])
        page = render_link_index_page(index)
        self.assertNotIn('<script>bad</script>', page)
        self.assertIn('&lt;script&gt;bad&lt;/script&gt;', page)


if __name__ == '__main__':
    unittest.main()
