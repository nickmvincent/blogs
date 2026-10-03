PYTHON ?= python3

.PHONY: build preview check archive-refresh archive-check register-urls deploy-preview deploy atproto-preview atproto-check atproto-sync publish
build:
	$(PYTHON) scripts/build_garden.py
preview: build
	$(PYTHON) -m http.server 8766 --bind 127.0.0.1 --directory _site
check: build
	$(PYTHON) -m unittest discover -s scripts -p 'test_*.py'
	$(PYTHON) scripts/build_garden.py --check
register-urls:
	$(PYTHON) scripts/build_garden.py --register-permalinks
	@if [ -f site/standard-site.json ]; then $(PYTHON) scripts/standard_site.py register; fi
archive-refresh:
	$(PYTHON) scripts/archive_substack.py refresh
archive-check:
	$(PYTHON) scripts/archive_substack.py check
deploy-preview:
	$(PYTHON) scripts/deploy_garden.py
deploy:
	$(PYTHON) scripts/deploy_garden.py --apply
atproto-preview:
	$(PYTHON) scripts/standard_site.py preview
atproto-check:
	$(PYTHON) scripts/standard_site.py sync
atproto-sync:
	$(PYTHON) scripts/standard_site.py sync --apply
publish: deploy
	$(PYTHON) scripts/standard_site.py sync --apply
