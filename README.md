# Data Leverage digital garden

This is the source repository for [Data Leverage on GitHub Pages](https://nickmvincent.github.io/). The garden has two writing sections:

- **`archived/`**: previously published writing. Substack articles preserve their live published text at the recorded capture time; other articles preserve the documented earlier public version.
- **`drafts/`**: public working notes, including focus posts, stubs, and ideas. These can evolve freely and are visibly labeled as drafts.

Private drafts stay in the private `nickmvincent.com` repository. Nothing in that checkout is read by this garden’s build. **Everything committed to this public repository is public**, whether or not it appears on the site.

The wiki-book lives separately in `data-leverage-book`. It is not part of this build.

## Write

Use ordinary Markdown files with frontmatter. File placement selects Archive or Public drafts; a stable `content_id` identifies the article. Each public article has a permanent `/p/<slug>.html` URL recorded in `site/permalinks.json`, keyed by `content_id`. Changing its title, filename, or Archive/Public drafts placement does not change that URL.

For a public draft:

```yaml
---
title: A focused idea
content_id: garden/draft/a-focused-idea
slug: a-focused-idea
status: draft
visibility: public
---
```

For a new article, choose a readable `slug` and run `make register-urls` once. Registration only adds missing IDs; it never changes an existing URL. Commit the resulting registry entry alongside the article. Keep both the ID and registered path fixed, even if the title or slug later changes. Builds fail for an unregistered ID or duplicate permalink. Add `date`, `updated_at`, and `summary` when useful. Put images in `media/` and use relative Markdown links. Drafts require explicit `visibility: public`; archive files are public by their role. Private, ideation, and book folders are never publication inputs. The build rejects missing IDs, duplicate IDs/routes, unresolved internal references, and local assets outside `media/`.

Keep an archived publication intact when developing a new version: start a separate public draft with its own ID and a link back to the original. Focus posts and other unfinished pieces belong in `drafts/`, even when an earlier version was shared on Leaflet or the garden. An earlier public URL alone does not make a piece a finished archive entry; `original_url` retains that provenance.

## Preview and check

Requires Python 3 and Pandoc on your PATH. Archive refresh also uses curl; deployment uses the authenticated GitHub CLI and Git.

```sh
make preview         # http://127.0.0.1:8766
make build           # generated site in ignored _site/
make register-urls   # assign URLs to new IDs, leaving existing URLs fixed
make check           # build, publication-boundary tests, and local-link checks
make archive-check   # compare Substack Markdown with the captured source cache
```

The site provides Archive, Public drafts, full-text search, original-publication links, Markdown source links, and Extras with word/phrase frequencies and an outbound-link index. Words and Links retain their existing `/words.html` and `/links.html` URLs, search/sort/filter controls, and downloadable JSON indexes. Analytics rebuild from the same public articles as the site; private or withdrawn content is not an input. Word counts cover titles and rendered bodies (excluding common stopwords and URLs), showing up to 300 terms per size. Link counts cover outbound article anchors, including footnotes, excluding navigation, images, and links to this garden; maintenance findings are heuristics, not live availability checks. The existing garden’s article URLs redirect to their corresponding new pages. `site/garden.json` records those redirects and the deployment destination; `site/site.css` and `site/search.js` hold presentation and search behavior.

Old `microblogs/` Markdown paths retain compatibility pointers where their articles remain public; withdrawn notes have content-free notices. These old paths are not authoring inputs. To withdraw a draft, move its source out of this public repository, remove its permalink entry, and reserve its old URLs in `withdrawn_routes` in `site/garden.json`. Those URLs show a generic noindex notice and are excluded from listings and search. Moving a previously public file does not erase Git history or copies on other services.

## Update the Substack archive

[INDEX.md](INDEX.md) lists the captured Substack archive and the other archived publications.

```sh
make archive-refresh
make register-urls    # register any newly discovered Substack articles
make archive-check
git diff -- archived/
```

The importer follows the publication’s public archive endpoint to its terminal empty page, then reads every full public article page. Titles, dates, authors, source URLs, update/capture timestamps, and the body hash go in frontmatter. It preserves wording, structure, links, image captions, and footnotes; subscription and image-view controls are omitted. Markdown does not reproduce Substack’s exact page layout.

Raw pages, the source listing, media mapping, and detailed checks remain in ignored `.import-cache/`. The importer checks text and link round trips and local images before replacing Markdown. Existing files absent from the listing stop the refresh for review. Other archived publications and public drafts are left untouched. A fresh clone needs a refresh before the source-cache check is available.

The capture boundary is the dated public article listing: unpublished, deleted, or unlisted posts, comments, and Substack Notes are outside it. Restricted articles cause a failure rather than being recorded as complete previews. Interactive audio/video embeds, if present, remain links.

## GitHub Pages deployment

The URL stays `https://nickmvincent.github.io/`. The separate `nickmvincent/nickmvincent.github.io` repository remains the generated output host on `master`; **this repository is the source**. No cross-repository token, scheduled sync, or new publishing service is needed.

```sh
make deploy-preview  # temporary Pages checkout and proposed diff; no commit or push
make deploy          # explicitly commit/push the generated site to Pages
```

Deployment requires a clean blogs checkout whose HEAD matches pushed `origin/main`. It rebuilds from that source, checks local links, and records the source repository and commit in the generated `manifest.json`. Existing Pages workflows, custom-domain settings, and verification files are preserved. The deploy command never publishes to Substack or Leaflet.

Normal edits, previews, builds, checks, and archive refreshes do not commit, push, or deploy. The deploy preview report is in `.import-cache/deployment-preview.json` locally.

## Standard.site index on atproto

The garden generates a lightweight atproto index from its public Markdown. Records contain article titles, dates, summaries, tags, and permanent garden URLs. They contain no article bodies or Leaflet-specific content. Existing Leaflet publications remain independent; this workflow never updates them or creates Bluesky announcement posts.

Archived articles are included by default. Public drafts require an explicit `atproto: true` YAML boolean to opt in, and are identified as public drafts in their descriptions. Set `atproto: false` to exclude an archive entry. Indexed articles need a valid `date`; datetime values must include a timezone. `updated_at` is optional. Body-only edits do not alter a metadata-only record unless you also change its metadata.

`site/standard-site.json` stores the public account DID, the garden publication identity, and a stable record key per `content_id`. It contains no credentials. Preserve this registry across clones and edits. `make register-urls` also registers newly included articles locally. It keeps removed identities reserved and never publishes anything. For a different site starting without a registry, initialize once with `python3 scripts/standard_site.py register --did YOUR_PUBLIC_DID`.

```sh
make atproto-preview  # offline build and metadata preview; no credentials needed
make atproto-check    # read-only comparison against public records on your PDS
make atproto-sync     # explicitly publish the index after the site is deployed
make publish         # explicitly deploy the garden, then sync its index
```

The complete payload is generated at `_site/atproto-index.json`. Builds also generate publication verification under `.well-known/` and a `site.standard.document` link in each indexed page's head. Plain `make deploy` still deploys only the website. Deployment preserves unrelated verification files.

For live syncing, supply `ATPROTO_APP_PASSWORD` through the process environment (for example, via your password manager). The script does not load `.env` files, read the private sibling repository, save sessions, or print passwords/tokens. Authentication uses the registered DID and its currently resolved PDS. There is no additional service, subscription, or scheduled task.

The first activation requires reviewing, committing, and pushing this source to `origin/main`, then deploying it. Sync requires that clean pushed revision, a matching deployed manifest/index, and matching verification links before authenticating or writing records. `make publish` combines deployment and index sync for subsequent updates, allowing up to three minutes for Pages to serve the new build. If deployment succeeds but sync fails, rerun `make atproto-sync`; it updates fixed record identities, skips unchanged records, and uses compare-and-swap to avoid overwriting concurrent edits. No publication or article is deleted automatically. After withdrawing or opting out a previously indexed article, `make atproto-check` lists any retained remote records for separate removal after review.

Indexing makes the metadata available to compatible atproto readers; it does not guarantee discovery or announce the article in the Bluesky feed. Occasional Bluesky link posts can still point to the garden. See the upstream [document schema](https://standard.site/docs/lexicons/document/), [verification guide](https://standard.site/docs/verification/), and [Bluesky integration](https://bsky.network/docs/about-bluesky-content/app-integrations/). These implementation boundaries were checked against the published schemas on 2026-09-29.

## Migration provenance

The non-Substack garden articles were copied from the exact source revision recorded by the previous live Pages deployment, rather than current private working copies. Their frontmatter records the deployed source URL, revision, and source hash of the initial capture. Public drafts may subsequently incorporate newer author revisions; `updated_at` records an update to the garden copy. Historical GitHub microblogs retain links to their original committed versions. Local migration details are in `.import-cache/garden-migration/`.
