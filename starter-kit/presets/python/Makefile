SHELL := /bin/bash
PY ?= python3
VENV ?= .venv
ACT := source $(VENV)/bin/activate

.PHONY: setup fmt lint test check run smoke

setup:
	@if [[ ! -d $(VENV) ]]; then $(PY) -m venv $(VENV); fi
	$(ACT); pip install --upgrade pip
	$(ACT); pip install -r requirements-dev.txt

fmt:
	$(ACT); ruff format .
	$(ACT); black .

lint:
	$(ACT); ruff check .

test:
	$(ACT); pytest

check: fmt lint test

run:
	$(ACT); flask run --debug

smoke:
	@./scripts/smoke.sh
