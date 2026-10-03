# Public garden

- Read README.md and check Git status before editing. Preserve unrelated work and Git history.
- This public repository has two writing inputs: archived/*.md and drafts/*.md. Private drafts remain outside this repository. Never read sibling repositories as build inputs.
- Archived Substack articles preserve the published source at capture time. Do not rewrite their prose or substitute private local revisions. Other archived publications retain their documented public provenance.
- Public drafts require visibility: public and their own stable content_id. Book adaptations belong in the separate book repository.
- Keep content_id and its path in site/permalinks.json stable across title, file, and section changes. Register new IDs with make register-urls; never regenerate existing permalinks from titles.
- Keep images in media/. Keep old public article URLs working through site/garden.json redirects. Legacy microblogs are compatibility pointers or withdrawal notices, not authoring inputs. Withdrawn drafts belong outside this repository; leave only content-free noindex pages at their former URLs.
- Keep raw fetches, migration backups, and reports in ignored .import-cache/. Generated output belongs in ignored _site/.
- Run make check after garden changes; run make archive-check after Substack archive changes. Report the source boundary when claiming completeness.
- Do not commit, push, deploy, or change repository visibility without an explicit user request. Deployment must use a clean source revision matching origin/main and the configured Pages output repository.
