#!/usr/bin/env bash
set -euo pipefail

KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$(pwd)"
PRESET=""
DRY_RUN=0

usage() {
  cat <<'EOF'
Usage: bash starter-kit/apply.sh [--preset python|java-maven] [--dry-run]
- Run from repo root. Copies core kit files and optional preset.
- Existing files are never overwritten; if present, a .new copy is created.
EOF
}

copy_tree() {
  local src_root="$1"
  find "$src_root" -type f | while read -r src; do
    local rel="${src#$src_root/}"
    local dest="$TARGET_DIR/$rel"
    local dest_dir
    dest_dir="$(dirname "$dest")"
    mkdir -p "$dest_dir"
    if [[ -e "$dest" ]]; then
      dest="$dest.new"
    fi
    if [[ "$DRY_RUN" -eq 1 ]]; then
      echo "[dry-run] copy $rel -> ${dest#$TARGET_DIR/}"
    else
      cp "$src" "$dest"
      echo "copied: ${dest#$TARGET_DIR/}"
    fi
  done
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --preset)
      PRESET="$2"; shift 2;;
    --dry-run)
      DRY_RUN=1; shift;;
    -h|--help)
      usage; exit 0;;
    *)
      echo "Unknown arg: $1" >&2; usage; exit 1;;
  esac
done

if [[ "$TARGET_DIR" != */starter-kit* ]]; then
  : # ok
fi

CORE_DIR="$KIT_DIR/core"
copy_tree "$CORE_DIR"

if [[ -n "$PRESET" ]]; then
  case "$PRESET" in
    python) copy_tree "$KIT_DIR/presets/python";;
    java-maven) copy_tree "$KIT_DIR/presets/java-maven";;
    *) echo "Invalid preset: $PRESET" >&2; exit 1;;
  esac
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  exit 0
fi

cat <<'POST'
Done. Next steps:
- Review any *.new files for conflicts and merge manually.
- Fill STRUCTURE.template.md, PITFALLS.md, DECISIONS/ADR entries, CONTEXT_PACK.md.
- Run make setup && make check (or preset-specific commands):
  - python: make setup fmt lint test
  - java-maven: make setup fmt lint test
POST
