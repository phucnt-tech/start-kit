#!/usr/bin/env bash
set -euo pipefail

PORT=${PORT:-5000}
URL="http://localhost:${PORT}/health"

if command -v curl >/dev/null; then
  if curl -fsS "$URL" >/dev/null; then
    echo "[smoke] OK ${URL}"
  else
    echo "[smoke] FAIL ${URL}" >&2
    exit 1
  fi
else
  echo "curl not found; please check service manually" >&2
  exit 1
fi
