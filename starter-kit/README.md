# Starter Kit (Reusable)

This kit adds predictable hygiene, docs, and automation to any repo. Run `bash starter-kit/apply.sh --preset <python|java-maven>` from repo root. Files are copied safely: if a target exists, a `.new` sibling is created.

## What you get
- Core: README/CONTRIBUTING templates, structure map, decisions/ADR template, pitfalls, context-pack (for task pause/resume), AI guidelines, editorconfig, gitignore, gitattributes, pre-commit, PR/Issue templates, basic Makefile, smoke/bootstrap scripts, CI skeleton.
- Presets:
  - **python**: black+ruff+pytest scaffold, make targets, requirements-dev, env example.
  - **java-maven**: spotless+checkstyle+spotbugs wiring, make targets, env example, Maven wrapper-friendly.

## Usage
Option A (shell):
1) From repo root: `bash starter-kit/apply.sh --preset python` (or `java-maven`).
2) Review any `*.new` files if there were conflicts; merge manually.
3) Run `make setup && make check` (or the preset's commands printed after apply).
4) Fill the templates (STRUCTURE, PITFALLS, DECISIONS/ADR, CONTEXT_PACK) with your repo info.

Option B (CLI Python):
```bash
python starter-kit/kitcli.py init --preset python --target .
python starter-kit/kitcli.py validate --preset python --target .
```
- `init`: copy files; existing files get `.new`.
- `validate`/`test`: check expected kit files (accepts `.new`).
```
## Idempotency
- Running again will not overwrite existing files; duplicates go to `.new`.
- Safe to re-run after pulling kit updates.

## Versioning
- Keep this folder vendored or track updates from source; changes are localized to `starter-kit/`.

## Context management (for frequent task switching)
- `contexts/<project>/<feature>/context.md` captures WHAT/WHY/HOW/NEXT.
- `contexts/<project>/<feature>/notes-YYYYMMDD.md` for session logs.
- `scripts/context-pack.sh` scaffolds these; `scripts/resume.sh` prints quick resume checklist.
