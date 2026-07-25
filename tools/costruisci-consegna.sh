#!/usr/bin/env bash
# Costruisce il pacchetto di consegna dell'elaborato MaraffaOnline:
#   Consegna/
#   ├── Relazione.pdf           (con link cliccabili agli allegati)
#   └── Allegati/<Fase>/*.pdf    (versione pulita: note interne rimosse)
# e produce Consegna-MaraffaOnline.zip
#
# La Relazione.pdf va aperta NEL BROWSER (trascinarla in Chrome): i riferimenti
# agli allegati sono link che aprono i rispettivi PDF nella cartella Allegati/.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
cd "$DIR"

[ -d node_modules/marked ] || { echo "Installo le dipendenze (marked)..."; npm install --silent; }

OUT="$REPO/Consegna"
ZIP="$REPO/Consegna-MaraffaOnline.zip"
rm -rf "$OUT" "$ZIP"
mkdir -p "$OUT/Allegati"

echo "== 1/3 Genero gli allegati PDF (versione consegna, note interne rimosse) =="
OUT_DIR="$OUT/Allegati" node genera-allegati-pdf.mjs --clean "$@"

echo "== 2/3 Compilo la Relazione =="
( cd "$REPO/Relazione" && tectonic main.tex >/dev/null )
cp "$REPO/Relazione/main.pdf" "$OUT/Relazione.pdf"

echo "== 3/3 Creo lo ZIP =="
( cd "$REPO" && zip -r -q "$ZIP" "Consegna" -x '*.DS_Store' )

echo
echo "Consegna pronta: $ZIP"
echo "Struttura:"
( cd "$OUT" && find . -type f ! -name '.DS_Store' | sort | sed 's|^\./|  |' )
echo
echo "NB: aprire Consegna/Relazione.pdf nel BROWSER (Apri con -> Chrome), non con doppio clic."