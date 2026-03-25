#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: scripts/resume.sh <project> <feature>" >&2
  exit 1
fi
proj="$1"; feat="$2"
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/contexts/$proj/$feat"
ctx="$dir/context.md"
latest_notes=$(ls -1 "$dir"/notes-*.md 2>/dev/null | sort | tail -n1 || true)

echo "== Resume: $proj / $feat =="
if [[ -f "$ctx" ]]; then
  echo "Context file: $ctx"
else
  echo "(missing context.md; run context-pack.sh)"
fi
if [[ -n "$latest_notes" ]]; then
  echo "Latest notes: $latest_notes"
else
  echo "No notes yet."
fi

echo "-- Suggested checklist --"
echo "1) git status; git diff"
echo "2) read $ctx"
if [[ -n "$latest_notes" ]]; then
  echo "3) tail -n 40 $latest_notes"
fi
echo "4) rerun last failing tests if any"
