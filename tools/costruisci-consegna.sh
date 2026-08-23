#!/usr/bin/env bash
# Costruisce il pacchetto di consegna dell'elaborato MaraffaOnline:
#   MaraffaOnline-Consegna/
#   ├── Relazione-MaraffaOnline.pdf     (con link cliccabili agli allegati)
#   └── Documentazione/<Fase>/*.pdf     (versione pulita: note interne rimosse)
# e produce MaraffaOnline-Consegna.zip
#
# I nomi (cartella "Documentazione", "Relazione-MaraffaOnline.pdf") devono
# restare questi: i link /URI relativi dentro la Relazione puntano a
# "Documentazione/<Fase>/<Allegato>.pdf".
#
# La Relazione va aperta NEL BROWSER (trascinarla in Chrome): i riferimenti
# agli allegati aprono i rispettivi PDF nella cartella Documentazione/.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$DIR/.." && pwd)"
cd "$DIR"

[ -d node_modules/marked ] && [ -d node_modules/pdf-lib ] || { echo "Installo le dipendenze (marked, pdf-lib)..."; npm install --silent; }

OUT="$REPO/MaraffaOnline-Consegna"
ZIP="$REPO/MaraffaOnline-Consegna.zip"
rm -rf "$OUT" "$ZIP"
mkdir -p "$OUT/Documentazione"

echo "== 1/3 Genero gli allegati PDF (versione consegna, note interne rimosse) =="
OUT_DIR="$OUT/Documentazione" node genera-allegati-pdf.mjs --clean "$@"

# Adegua i nomi alla convenzione dei link /URI della Relazione: per le coppie
# md+html con lo stesso stem (2.4, 2.5, 3.1, 3.2, 3.4, 4.2) la Relazione linka
# <stem>-Visuale.pdf (versione visiva, da HTML) e <stem>.pdf (registro testuale, da md),
# mentre il generatore produce <stem>.pdf (HTML) e <stem>-registro.pdf (md).
for reg in "$OUT/Documentazione"/*/*-registro.pdf; do
  [ -e "$reg" ] || continue
  base="${reg%-registro.pdf}"
  mv "$base.pdf" "$base-Visuale.pdf"
  mv "$reg" "$base.pdf"
done

# La guida di importazione Notion e' strumentazione interna: fuori dalla consegna.
# (I verbali ritirati - Scoping Meeting e Approval Process - sono in
#  Scoping/_ritirato-*.md: fuori dal pattern Allegato*, il generatore li ignora.)
rm -f "$OUT/Documentazione/Planning/Allegato3.5.3-GuidaImportazioneNotion.pdf"

echo "== 2/3 Compilo la Relazione =="
( cd "$REPO/Relazione" && tectonic main.tex >/dev/null )
cp "$REPO/Relazione/main.pdf" "$OUT/Relazione-MaraffaOnline.pdf"

echo "== 3/3 Creo lo ZIP =="
( cd "$REPO" && zip -r -q "$ZIP" "MaraffaOnline-Consegna" -x '*.DS_Store' )

echo
echo "Consegna pronta: $ZIP"
echo "Struttura:"
( cd "$OUT" && find . -type f ! -name '.DS_Store' | sort | sed 's|^\./|  |' )
echo
echo "NB: aprire Relazione-MaraffaOnline.pdf nel BROWSER (Apri con -> Chrome), non con doppio clic."
