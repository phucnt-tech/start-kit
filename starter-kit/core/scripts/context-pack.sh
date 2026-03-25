#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: scripts/context-pack.sh <project> <feature>" >&2
  exit 1
fi
proj="$1"; feat="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/contexts/$proj/$feat"
mkdir -p "$dir"
ctx="$dir/context.md"
notes="$dir/notes-$(date +%Y%m%d).md"
if [[ ! -f "$ctx" ]]; then
  cat "$root/CONTEXT_PACK.md" > "$ctx"
  echo "created $ctx"
else
  echo "$ctx exists"
fi
if [[ ! -f "$notes" ]]; then
  echo "# Notes $(date +%Y-%m-%d)" > "$notes"
  echo "created $notes"
else
  echo "$notes exists"
fi
