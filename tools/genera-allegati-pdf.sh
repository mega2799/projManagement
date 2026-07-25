#!/usr/bin/env bash
# Wrapper: installa le dipendenze (solo la prima volta) e genera i PDF degli allegati.
# Uso: tools/genera-allegati-pdf.sh [--all] [--capitoli] [--only <testo>]
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

if [ ! -d node_modules/marked ]; then
  echo "Installo le dipendenze (marked)..."
  npm install --silent
fi

exec node genera-allegati-pdf.mjs "$@"
