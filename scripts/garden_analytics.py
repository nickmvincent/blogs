"""Public word/link indexes, carried forward from the original garden renderer.

Inputs are the current build's public articles only; no cached or sibling content.
The tables and browser controls retain the original analytics behavior.
"""
from __future__ import annotations
from collections import Counter
import html
from html.parser import HTMLParser
import re
from typing import Any
import urllib.parse



LINK_ISSUE_LABELS = {
    "bare-url-label": "Bare URL Label",
    "duplicate-in-article": "Repeated In Article",
    "duplicate-url": "Repeated URL",
    "insecure-http": "HTTP Link",
    "suspicious-domain": "Suspicious Domain",
    "tracking-query": "Tracking Query",
    "trailing-punctuation": "Trailing Punctuation",
}


LINK_ISSUE_DESCRIPTIONS = {
    "bare-url-label": "The visible link text is just the URL, which may be less readable.",
    "duplicate-in-article": "The same URL appears more than once in one post.",
    "duplicate-url": "The same URL appears in multiple places across the garden.",
    "insecure-http": "The link uses http rather than https.",
    "suspicious-domain": "The parsed domain looks unusual and may need a quick check.",
    "tracking-query": "The original link included query parameters that may be tracking or sorting noise.",
    "trailing-punctuation": "The URL may have included sentence punctuation by accident.",
}


TRAILING_URL_PUNCTUATION = ".,;:"


WORD_TOKEN_RE = re.compile(r"[a-z0-9]+(?:'[a-z0-9]+)?")


WORD_NGRAM_SIZES = (1, 2, 3)


WORD_NGRAM_LABELS = {
    1: "Words",
    2: "2-grams",
    3: "3-grams",
}


WORD_INDEX_MIN_COUNTS = {
    1: 3,
    2: 2,
    3: 2,
}


WORD_INDEX_LIMIT_PER_SIZE = 300


WORD_INDEX_STOPWORDS = {
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "also",
    "am",
    "an",
    "and",
    "any",
    "are",
    "aren't",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can",
    "can't",
    "cannot",
    "could",
    "couldn't",
    "did",
    "didn't",
    "do",
    "does",
    "doesn't",
    "doing",
    "don't",
    "down",
    "during",
    "each",
    "even",
    "few",
    "for",
    "from",
    "further",
    "had",
    "hadn't",
    "has",
    "hasn't",
    "have",
    "haven't",
    "having",
    "he",
    "he'd",
    "he'll",
    "her",
    "here",
    "here's",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "how's",
    "i",
    "i'd",
    "i'll",
    "i'm",
    "i've",
    "if",
    "in",
    "into",
    "is",
    "isn't",
    "it",
    "it's",
    "its",
    "itself",
    "let's",
    "may",
    "me",
    "more",
    "most",
    "might",
    "must",
    "mustn't",
    "my",
    "myself",
    "no",
    "nor",
    "not",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "ought",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "shan't",
    "she",
    "she'd",
    "she'll",
    "she's",
    "should",
    "shouldn't",
    "shall",
    "so",
    "some",
    "such",
    "than",
    "that",
    "that's",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "there's",
    "these",
    "they",
    "they'd",
    "they'll",
    "they're",
    "they've",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "us",
    "very",
    "was",
    "wasn't",
    "we",
    "we'd",
    "we'll",
    "we're",
    "we've",
    "were",
    "weren't",
    "what",
    "what's",
    "when",
    "when's",
    "where",
    "where's",
    "which",
    "while",
    "who",
    "who's",
    "whom",
    "why",
    "why's",
    "will",
    "with",
    "won't",
    "would",
    "wouldn't",
    "you",
    "you'd",
    "you'll",
    "you're",
    "you've",
    "your",
    "yours",
    "yourself",
    "yourselves",
}


# Strip known attribution parameters only; retain functional URL parameters.
TRACKING_QUERY_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid", "ref", "ref_src", "spm"}


def canonicalize_url(url):
    """Grouping key only: original destinations in the articles stay unchanged."""
    parsed = urllib.parse.urlsplit(url.strip())
    if parsed.scheme not in {"http", "https"}:
        return url.strip()
    host = parsed.netloc.lower().removeprefix("www.")
    query = urllib.parse.urlencode(sorted(
        (k, v) for k, v in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in TRACKING_QUERY_KEYS
    ))
    return urllib.parse.urlunsplit(("https", host, parsed.path.rstrip("/") or "/", query, ""))


class ArticleLinks(HTMLParser):
    """Read anchors from rendered article bodies, excluding local garden links."""
    def __init__(self, text, site_url):
        super().__init__()
        self.site_host = urllib.parse.urlsplit(site_url).netloc.lower().removeprefix("www.")
        self.links = []
        self.current = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.current = None
            url = attrs.get("href", "")
            parsed = urllib.parse.urlsplit(url)
            if (parsed.scheme in {"http", "https"} and
                    parsed.netloc.lower().removeprefix("www.") != self.site_host):
                self.current = {"url": url, "label": "", "source": "article"}
                self.links.append(self.current)
        elif tag == "img" and self.current is not None:
            self.current["label"] += attrs.get("alt", "")

    def handle_data(self, data):
        if self.current is not None:
            self.current["label"] += data

    def handle_endtag(self, tag):
        if tag == "a":
            self.current = None


def clean_text_for_word_index(post):
    text = post["title"] + "\n\n" + post["text"]
    text = re.sub(r"https?://\S+", " ", text)
    return text.replace("’", "'").replace("‘", "'")



def normalize_word_token(token: str) -> str | None:
    normalized = token.lower().strip("'")
    if normalized.endswith("'s"):
        normalized = normalized[:-2]
    if len(normalized) < 2:
        return None
    if normalized.isdigit():
        return None
    return normalized


def tokens_for_word_index(post: Any) -> list[str]:
    tokens: list[str] = []
    for match in WORD_TOKEN_RE.finditer(clean_text_for_word_index(post).lower()):
        token = normalize_word_token(match.group(0))
        if token:
            tokens.append(token)
    return tokens


def is_content_word(token: str) -> bool:
    return token not in WORD_INDEX_STOPWORDS and not token.isdigit()


def ngrams_for_tokens(tokens: list[str], size: int) -> list[str]:
    if size < 1:
        return []
    rows: list[str] = []
    for index in range(0, len(tokens) - size + 1):
        phrase_tokens = tokens[index : index + size]
        if all(is_content_word(token) for token in phrase_tokens):
            rows.append(" ".join(phrase_tokens))
    return rows


def build_word_index(posts: list[dict]) -> dict[str, Any]:
    phrase_article_counts: dict[int, dict[str, Counter[str]]] = {size: {} for size in WORD_NGRAM_SIZES}
    article_lookup: dict[str, dict] = {}
    total_content_words = 0

    for item in posts:
        source_path = item["source"]
        article_lookup[source_path] = item
        tokens = tokens_for_word_index(item)
        total_content_words += sum(1 for token in tokens if is_content_word(token))
        for size in WORD_NGRAM_SIZES:
            article_counter = Counter(ngrams_for_tokens(tokens, size))
            for phrase, count in article_counter.items():
                phrase_article_counts[size].setdefault(phrase, Counter())[source_path] += count

    records: list[dict[str, Any]] = []
    sizes: list[dict[str, Any]] = []
    for size in WORD_NGRAM_SIZES:
        phrase_counts = phrase_article_counts[size]
        min_count = WORD_INDEX_MIN_COUNTS[size]
        sorted_phrases = sorted(
            phrase_counts.items(),
            key=lambda entry: (-sum(entry[1].values()), entry[0]),
        )
        visible_phrases = [
            (phrase, article_counts)
            for phrase, article_counts in sorted_phrases
            if sum(article_counts.values()) >= min_count
        ][:WORD_INDEX_LIMIT_PER_SIZE]
        sizes.append(
            {
                "n": size,
                "label": WORD_NGRAM_LABELS[size],
                "totalUnique": len(phrase_counts),
                "shown": len(visible_phrases),
                "minCount": min_count,
            }
        )

        for phrase, article_counts in visible_phrases:
            article_rows = []
            for source_path, count in sorted(article_counts.items(), key=lambda entry: (-entry[1], entry[0]))[:8]:
                item = article_lookup.get(source_path)
                if not item:
                    continue
                article_rows.append(
                    {
                        "title": item["title"],
                        "href": item["href"],
                        "sourcePath": source_path,
                        "category": item["category"],
                        "count": count,
                    }
                )
            top_article = article_rows[0] if article_rows else None
            records.append(
                {
                    "phrase": phrase,
                    "n": size,
                    "type": WORD_NGRAM_LABELS[size],
                    "count": sum(article_counts.values()),
                    "articleCount": len(article_counts),
                    "topArticle": top_article,
                    "articles": article_rows,
                }
            )

    return {
        "source": "Titles and rendered bodies of the current Archive and Public drafts; common English stopwords and URLs excluded. Up to 300 terms of each type.",
        "totalContentWords": total_content_words,
        "sizes": sizes,
        "terms": sorted(records, key=lambda record: (int(record["n"]), -int(record["count"]), str(record["phrase"]))),
    }


def domain_for_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host or "(no domain)"


def normalize_link_label(value: str) -> str:
    return " ".join(value.split())


def ordered_link_issue_codes(codes: list[str]) -> list[str]:
    seen = set(codes)
    return [code for code in LINK_ISSUE_LABELS if code in seen]


def query_was_normalized(raw_url: str, canonical_url: str) -> bool:
    raw_query = urllib.parse.parse_qsl(urllib.parse.urlsplit(raw_url).query, keep_blank_values=True)
    canonical_query = urllib.parse.parse_qsl(urllib.parse.urlsplit(canonical_url).query, keep_blank_values=True)
    return bool(raw_query) and sorted(raw_query) != sorted(canonical_query)


def base_link_issue_codes(url: str, canonical_url: str, label: str, domain: str) -> list[str]:
    codes: list[str] = []
    parsed = urllib.parse.urlsplit(url)
    normalized_label = normalize_link_label(label)

    if parsed.scheme == "http":
        codes.append("insecure-http")
    if url.strip().endswith(tuple(TRAILING_URL_PUNCTUATION)):
        codes.append("trailing-punctuation")
    if query_was_normalized(url, canonical_url):
        codes.append("tracking-query")
    if domain == "(no domain)" or ("." not in domain and domain != "localhost"):
        codes.append("suspicious-domain")
    if normalized_label.startswith(("http://", "https://")) or canonicalize_url(normalized_label) == canonical_url:
        codes.append("bare-url-label")

    return ordered_link_issue_codes(codes)


def build_link_index(posts: list[dict]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for item in posts:
        links = item["links"]
        for index, link in enumerate(links, start=1):
            url = link["url"]
            canonical_url = canonicalize_url(url)
            domain = domain_for_url(canonical_url)
            label = normalize_link_label(link.get("label") or url)
            records.append(
                {
                    "domain": domain,
                    "url": url,
                    "canonicalUrl": canonical_url,
                    "label": label,
                    "source": link.get("source") or "markdown",
                    "occurrence": index,
                    "articleTitle": item["title"],
                    "articleSlug": item["slug"],
                    "articleDate": item["date"],
                    "category": item["category"],
                    "publication": "garden",
                    "sourcePath": item["source"],
                    "articleHref": item["href"],
                    "issueCodes": base_link_issue_codes(url, canonical_url, label, domain),
                }
            )

    canonical_counts = Counter(record["canonicalUrl"] for record in records)
    article_url_counts = Counter((record["sourcePath"], record["canonicalUrl"]) for record in records)
    for record in records:
        codes = list(record["issueCodes"])
        if canonical_counts[record["canonicalUrl"]] > 1:
            codes.append("duplicate-url")
        if article_url_counts[(record["sourcePath"], record["canonicalUrl"])] > 1:
            codes.append("duplicate-in-article")
        record["issueCodes"] = ordered_link_issue_codes(codes)
        record["issues"] = [
            {"code": code, "label": LINK_ISSUE_LABELS[code]}
            for code in record["issueCodes"]
        ]

    domain_counts = Counter(record["domain"] for record in records)
    article_counts = Counter(record["sourcePath"] for record in records)
    issue_counts = Counter(code for record in records for code in record["issueCodes"])
    return {
        "totalLinks": len(records),
        "totalDomains": len(domain_counts),
        "totalArticlesWithLinks": len(article_counts),
        "totalFindings": sum(issue_counts.values()),
        "byDomain": [
            {"domain": domain, "count": count}
            for domain, count in sorted(domain_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "byIssue": [
            {"code": code, "label": LINK_ISSUE_LABELS[code], "count": issue_counts[code]}
            for code in LINK_ISSUE_LABELS
            if issue_counts[code]
        ],
        "byArticle": [
            {"sourcePath": source_path, "count": count}
            for source_path, count in sorted(article_counts.items(), key=lambda item: (-item[1], item[0]))
        ],
        "links": sorted(records, key=lambda record: (record["domain"], record["articleTitle"].lower(), record["url"])),
    }


def title_attr(value: str | None) -> str:
    return f' title="{html.escape(value, quote=True)}"' if value else ""


def render_link_index_page(link_index: dict[str, Any]) -> str:
    links = link_index.get("links") if isinstance(link_index.get("links"), list) else []
    domain_rows = []
    for entry in link_index.get("byDomain", [])[:40]:
        if not isinstance(entry, dict):
            continue
        domain = str(entry.get("domain") or "")
        count = int(entry.get("count") or 0)
        domain_rows.append(
            f'<li><button type="button" data-domain-filter="{html.escape(domain)}"'
            f'{title_attr(f"Filter links to {domain}")}>{html.escape(domain)} ({count})</button></li>'
        )

    issue_rows = []
    for entry in link_index.get("byIssue", []):
        if not isinstance(entry, dict):
            continue
        code = str(entry.get("code") or "")
        label = str(entry.get("label") or code)
        count = int(entry.get("count") or 0)
        description = LINK_ISSUE_DESCRIPTIONS.get(code, "Maintenance finding for this link.")
        issue_rows.append(
            f'<li><button type="button" data-issue-filter="{html.escape(code)}" title="{html.escape(description)}">{html.escape(label)} ({count})</button></li>'
        )

    table_rows = []
    for record in links:
        if not isinstance(record, dict):
            continue
        href = str(record.get("articleHref") or "")
        article_title = str(record.get("articleTitle") or "")
        domain = str(record.get("domain") or "")
        url = str(record.get("url") or "")
        canonical_url = str(record.get("canonicalUrl") or url)
        label = str(record.get("label") or url)
        category = str(record.get("category") or "")
        issue_codes = [str(code) for code in record.get("issueCodes", []) if isinstance(code, str)]
        issue_labels = [
            str(issue.get("label") or issue.get("code") or "")
            for issue in record.get("issues", [])
            if isinstance(issue, dict)
        ]
        issue_text = " ".join(issue_codes + issue_labels)
        issue_cell = (
            "".join(
                f'<span class="finding-label">{html.escape(issue_label)}</span>'
                for issue_label in issue_labels
                if issue_label
            )
            or '<span class="muted">-</span>'
        )
        table_rows.append(
            f"""\
<tr data-link-row data-domain="{html.escape(domain)}" data-article="{html.escape(article_title)}" data-url="{html.escape(url)}" data-label="{html.escape(label)}" data-issues="{html.escape(' '.join(issue_codes))}" data-findings="{html.escape(issue_text)}">
  <td>{html.escape(domain)}</td>
  <td><a href="{html.escape(href)}">{html.escape(article_title)}</a><br><span class="muted">{html.escape(category)}</span></td>
  <td>{html.escape(label)}</td>
  <td class="review-column">{issue_cell}</td>
  <td class="url-cell"><a href="{html.escape(url)}">{html.escape(canonical_url)}</a></td>
</tr>"""
        )

    review_filters = (
        f"""\
    <details class="link-review-panel">
      <summary>Link review filters</summary>
      <p class="muted detail-note">Maintenance checks for duplicate links, tracking parameters, insecure URLs, and oddly parsed domains. They are mostly here to keep the garden tidy.</p>
      <ul class="finding-strip">
        {''.join(issue_rows)}
      </ul>
    </details>"""
        if issue_rows
        else ""
    )
    body = f"""\
    <section class="intro">
      <h1>Link Index</h1>
      <p class="dek"><span id="link-count" aria-live="polite">{len(links)} links</span> across {html.escape(str(link_index.get("totalDomains", 0)))} domains. Outbound article links in the current Archive and Public drafts. Counts represent link occurrences; destinations have not been checked for availability.</p>
    </section>
    <ul class="domain-strip">
      {''.join(domain_rows)}
    </ul>
    {review_filters}
    <div class="controls">
      <label>
        Search
        <input id="link-search" type="search" placeholder="Domain, article, URL, label, or finding">
      </label>
      <label>
        Sort
        <select id="link-sort">
          <option value="domain">Domain</option>
          <option value="article">Article</option>
          <option value="issues">Review findings</option>
          <option value="url">URL</option>
          <option value="label">Link text</option>
        </select>
      </label>
      <label class="review-toggle">
        <input id="show-link-review" type="checkbox">
        Show review findings
      </label>
    </div>
    <div class="table-wrap">
      <table id="link-table">
        <thead>
          <tr>
            <th>Domain</th>
            <th>Article</th>
            <th>Link text</th>
            <th class="review-column">Findings</th>
            <th>URL</th>
          </tr>
        </thead>
        <tbody>
          {''.join(table_rows)}
        </tbody>
      </table>
    </div>
"""
    return body


def render_word_index_page(word_index: dict[str, Any]) -> str:
    terms = word_index.get("terms") if isinstance(word_index.get("terms"), list) else []
    type_rows = []
    for entry in word_index.get("sizes", []):
        if not isinstance(entry, dict):
            continue
        n = int(entry.get("n") or 0)
        if n not in WORD_NGRAM_SIZES:
            continue
        label = str(entry.get("label") or WORD_NGRAM_LABELS[n])
        shown = int(entry.get("shown") or 0)
        type_rows.append(
            f'<li><button type="button" data-ngram-filter="{n}"'
            f'{title_attr(f"Show only {label.lower()}")}>{html.escape(label)} ({shown})</button></li>'
        )

    table_rows = []
    for record in terms:
        if not isinstance(record, dict):
            continue
        phrase = str(record.get("phrase") or "")
        n = int(record.get("n") or 0)
        type_label = str(record.get("type") or WORD_NGRAM_LABELS.get(n, "Term"))
        count = int(record.get("count") or 0)
        article_count = int(record.get("articleCount") or 0)
        top_article = record.get("topArticle") if isinstance(record.get("topArticle"), dict) else {}
        top_title = str(top_article.get("title") or "")
        top_href = str(top_article.get("href") or "")
        top_count = int(top_article.get("count") or 0)
        top_cell = (
            f'<a href="{html.escape(top_href)}">{html.escape(top_title)}</a>'
            f'<br><span class="muted">{top_count} use{"s" if top_count != 1 else ""}</span>'
            if top_href and top_title
            else '<span class="muted">-</span>'
        )
        table_rows.append(
            f"""\
<tr data-word-row data-ngram="{n}" data-type="{html.escape(type_label)}" data-phrase="{html.escape(phrase)}" data-count="{count}" data-article-count="{article_count}" data-top-article="{html.escape(top_title)}">
  <td class="phrase-cell">{html.escape(phrase)}</td>
  <td>{html.escape(type_label)}</td>
  <td>{count}</td>
  <td>{article_count}</td>
  <td>{top_cell}</td>
</tr>"""
        )

    source_note = str(word_index.get("source") or "")
    body = f"""\
    <section class="intro">
      <h1>Words</h1>
      <p class="dek"><span id="word-count" aria-live="polite">{len(terms)} terms</span> across {html.escape(str(word_index.get("totalContentWords", 0)))} filtered word uses. A frequency view of common words, 2-grams, and 3-grams across the garden.</p>
      {f'<p class="muted detail-note">{html.escape(source_note)}</p>' if source_note else ''}
    </section>
    <ul class="word-type-strip">
      {''.join(type_rows)}
    </ul>
    <div class="controls">
      <label>
        Search
        <input id="word-search" type="search" placeholder="Phrase, type, or article">
      </label>
      <label>
        Sort
        <select id="word-sort">
          <option value="count">Frequency</option>
          <option value="phrase">Phrase</option>
          <option value="type">Type</option>
          <option value="article-count">Article count</option>
          <option value="top-article">Top article</option>
        </select>
      </label>
    </div>
    <div class="table-wrap">
      <table id="word-table">
        <thead>
          <tr>
            <th>Phrase</th>
            <th>Type</th>
            <th>Uses</th>
            <th>Articles</th>
            <th>Top article</th>
          </tr>
        </thead>
        <tbody>
          {''.join(table_rows)}
        </tbody>
      </table>
    </div>
"""
    return body
