#!/usr/bin/env node
/*
 * Genera i PDF degli allegati di MaraffaOnline.
 *
 * Due tipi di sorgente:
 *   - Allegati HTML (matrici, canvas, semafori): stampati "as-is" con Chrome
 *     headless, forzando la resa dei colori di sfondo (print-color-adjust).
 *   - Allegati Markdown: convertiti in HTML con `marked` + un CSS di stampa,
 *     poi stampati con lo stesso Chrome headless.
 *
 * Regola di naming (per non duplicare gli allegati che hanno sia .md che .html):
 *   - se esiste l'HTML  -> <stem>.pdf viene generato dall'HTML (versione visiva)
 *   - il .md con lo stesso stem viene generato solo con --all, come
 *     <stem>-registro.pdf (il registro testuale completo)
 *   - un .md senza HTML gemello -> <stem>.pdf
 *
 * Uso:
 *   node genera-allegati-pdf.mjs                # tutti gli Allegato*.{md,html}
 *   node genera-allegati-pdf.mjs --all          # aggiunge i registri .md (-registro.pdf)
 *   node genera-allegati-pdf.mjs --capitoli     # include anche i Capitolo*.md (Monitoring/Closing)
 *   node genera-allegati-pdf.mjs --only 4.2     # solo i file il cui nome contiene "4.2"
 *   node genera-allegati-pdf.mjs --clean        # versione consegna: rimuove le note interne (callout companion, Storico revisioni)
 *
 * Variabili d'ambiente:
 *   CHROME_BIN   percorso all'eseguibile Chrome/Chromium (default: Chrome su macOS)
 *   OUT_DIR      cartella di output (default: <repo>/Allegati-PDF)
 */

import { readdir, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { marked } from 'marked';

const execFileAsync = promisify(execFile);

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '..');
const PHASES = ['Scoping', 'Planning', 'Launching', 'Monitoring', 'Closing'];

const OUT_DIR = process.env.OUT_DIR || path.join(REPO, 'Allegati-PDF');
const TMP_DIR = path.join(tmpdir(), 'maraffa-allegati-pdf');

const CHROME_CANDIDATES = [
  process.env.CHROME_BIN,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
].filter(Boolean);

const CHROME = CHROME_CANDIDATES.find((p) => existsSync(p));

// --- CLI args ---------------------------------------------------------------
const args = process.argv.slice(2);
const OPT_ALL = args.includes('--all');
const OPT_CAPITOLI = args.includes('--capitoli');
const OPT_CLEAN = args.includes('--clean');
const onlyIdx = args.indexOf('--only');
const ONLY = onlyIdx !== -1 ? (args[onlyIdx + 1] || '').toLowerCase() : null;

// Rimuove dalle sorgenti le note interne di lavorazione che non devono finire
// nella versione consegnata (attivo solo con --clean; i file su disco NON sono
// toccati, la pulizia avviene in memoria):
//   A) i callout in blockquote che rimandano al file companion .html/.md
//   B) la sezione "Storico revisioni"
//   C) i blocchi commentati <!-- ... --> (note interne, es. "Fonti e Riferimenti"):
//      marked li riemette nell'HTML e nel browser diventano commenti reali che
//      possono inghiottire il contenuto adiacente (o far trapelare le note stesse).
function sanitizeForDelivery(text) {
  // C) rimuove i blocchi commentati HTML prima di tutto
  text = text.replace(/<!--[\s\S]*?-->/g, '');
  const lines = text.split('\n');
  const out = [];
  const isHr = (s) => /^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(s);
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    // A) callout blockquote -> companion .html/.md
    if (/^\s*>/.test(line)) {
      let j = i;
      const block = [];
      while (j < lines.length && /^\s*>/.test(lines[j])) { block.push(lines[j]); j++; }
      const t = block.join(' ');
      if (/\.html\b|\bcompanion\b|Stampa\s*(→|->|&gt;)|registro (testuale|completo)|apri (il file )?nel browser/i.test(t)) {
        i = j - 1;
        if ((lines[i + 1] ?? '').trim() === '') i++; // consuma la riga vuota successiva
        continue;
      }
      out.push(...block);
      i = j - 1;
      continue;
    }
    // B) blocco "Storico revisioni" (marker + lista che segue)
    if (/\*\*Storico revisioni\*\*|^\s*#{1,6}\s*Storico revisioni/i.test(line)) {
      let k = i + 1;
      while (k < lines.length && (lines[k].trim() === '' || /^\s*[-*]\s/.test(lines[k]) || /^\s{2,}\S/.test(lines[k]))) k++;
      i = k - 1;
      // rimuove anche il separatore '---' che precedeva la sezione
      while (out.length && out[out.length - 1].trim() === '') out.pop();
      if (out.length && isHr(out[out.length - 1])) out.pop();
      continue;
    }
    // collassa i separatori '---' consecutivi (rimasti dopo aver tolto i blocchi sopra)
    if (isHr(line)) {
      let p = out.length - 1;
      while (p >= 0 && out[p].trim() === '') p--;
      if (p >= 0 && isHr(out[p])) continue;
    }
    out.push(line);
  }
  return out.join('\n').replace(/\n{3,}/g, '\n\n').trimEnd() + '\n';
}

// --- CSS di stampa per gli allegati Markdown --------------------------------
// Caricato da file esterno cosi' e' modificabile senza toccare lo script.
const MD_PRINT_CSS = await readFile(path.join(__dirname, 'allegato-md.css'), 'utf8');

function wrapMarkdownHtml(bodyHtml, baseHref, title) {
  return `<!doctype html><html lang="it"><head><meta charset="utf-8">
<title>${title}</title>
<base href="${baseHref}">
<style>${MD_PRINT_CSS}</style>
</head><body>${bodyHtml}</body></html>`;
}

// Inietta il forzamento colori in un HTML gia' pronto. Il @page (formato e
// orientamento) di default viene aggiunto SOLO se il file non ne definisce uno,
// per non sovrascrivere scelte come "A4 landscape" degli allegati larghi (WBS,
// Gantt, Network Diagram).
function prepareHtml(rawHtml, baseHref) {
  const hasOwnPage = /@page\b/i.test(rawHtml);
  const defaultPage = hasOwnPage ? '' : '@page { size: A4; margin: 12mm; }';
  const inject = `<base href="${baseHref}">
<style>
  * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  ${defaultPage}
</style>`;
  if (rawHtml.includes('</head>')) return rawHtml.replace('</head>', inject + '</head>');
  if (rawHtml.includes('<body')) return rawHtml.replace(/<body[^>]*>/, (m) => m + inject);
  return inject + rawHtml;
}

async function printToPdf(html, outPdf) {
  await mkdir(TMP_DIR, { recursive: true });
  const tmpHtml = path.join(TMP_DIR, path.basename(outPdf).replace(/\.pdf$/i, '') + '.html');
  await writeFile(tmpHtml, html, 'utf8');
  await execFileAsync(CHROME, [
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=8000',
    `--print-to-pdf=${outPdf}`,
    pathToFileURL(tmpHtml).href,
  ], { maxBuffer: 1024 * 1024 * 64 });
  await rm(tmpHtml, { force: true });
}

async function buildTask({ src, out, kind }) {
  const baseHref = pathToFileURL(path.dirname(src) + path.sep).href;
  let raw = await readFile(src, 'utf8');
  if (OPT_CLEAN) raw = sanitizeForDelivery(raw);
  let html;
  if (kind === 'md') {
    const body = marked.parse(raw, { gfm: true, breaks: false });
    html = wrapMarkdownHtml(body, baseHref, path.basename(src));
  } else {
    html = prepareHtml(raw, baseHref);
  }
  await printToPdf(html, out);
}

async function main() {
  if (!CHROME) {
    console.error('ERRORE: eseguibile Chrome/Chromium non trovato. Imposta CHROME_BIN.');
    process.exit(1);
  }

  await mkdir(OUT_DIR, { recursive: true });
  const tasks = [];

  for (const phase of PHASES) {
    const dir = path.join(REPO, phase);
    if (!existsSync(dir)) continue;
    const files = (await readdir(dir)).filter((f) => {
      const isAllegato = /^Allegato.*\.(md|html)$/i.test(f);
      const isCapitolo = OPT_CAPITOLI && /^Capitolo.*\.md$/i.test(f);
      return isAllegato || isCapitolo;
    });

    // Raggruppa per stem (nome senza estensione) per gestire le coppie md+html.
    const byStem = new Map();
    for (const f of files) {
      const ext = path.extname(f).slice(1).toLowerCase();
      const stem = f.slice(0, -(ext.length + 1));
      if (!byStem.has(stem)) byStem.set(stem, {});
      byStem.get(stem)[ext] = path.join(dir, f);
    }

    const outPhaseDir = path.join(OUT_DIR, phase);
    for (const [stem, srcs] of byStem) {
      if (ONLY && !stem.toLowerCase().includes(ONLY)) continue;

      if (srcs.html) {
        tasks.push({ phase, src: srcs.html, kind: 'html', out: path.join(outPhaseDir, `${stem}.pdf`) });
      }
      if (srcs.md) {
        if (!srcs.html) {
          tasks.push({ phase, src: srcs.md, kind: 'md', out: path.join(outPhaseDir, `${stem}.pdf`) });
        } else if (OPT_ALL) {
          tasks.push({ phase, src: srcs.md, kind: 'md', out: path.join(outPhaseDir, `${stem}-registro.pdf`) });
        }
      }
    }
  }

  if (tasks.length === 0) {
    console.log('Nessun allegato da generare (controlla i filtri --only/--capitoli).');
    return;
  }

  console.log(`Genero ${tasks.length} PDF in ${path.relative(REPO, OUT_DIR)}/ con ${path.basename(CHROME)}\n`);
  let ok = 0;
  for (const t of tasks) {
    await mkdir(path.dirname(t.out), { recursive: true });
    process.stdout.write(`  [${t.phase}] ${path.basename(t.out)} ... `);
    try {
      await buildTask(t);
      console.log('OK');
      ok++;
    } catch (err) {
      console.log('FALLITO');
      console.error(`     ${err.message.split('\n')[0]}`);
    }
  }
  await rm(TMP_DIR, { recursive: true, force: true });
  console.log(`\nCompletati ${ok}/${tasks.length} PDF -> ${OUT_DIR}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
