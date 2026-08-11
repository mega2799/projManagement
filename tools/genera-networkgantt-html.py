#!/usr/bin/env python3
"""Genera Planning/Allegato3.5-NetworkGantt.html dai dati CPM/Gantt verificati.

I dati sotto (durate, ES, float, date calendario) DEVONO restare allineati alle
tabelle Forward/Backward Pass e Sprint di Allegato3.5-ProjectNetworkDiagram-Gantt.md.
Percorso critico: A->B->D->G->J->M->P->R->S->T = 141 gg lavorativi (15 Ott -> 8 Mag),
con fast tracking P->R (legame Start-to-Start, lag 31 gg).

Uso:  python3 tools/genera-networkgantt-html.py
"""
from datetime import date

VERSION = "v.2.1.0"
CP_DAYS = 141
START = date(2025, 10, 15)

# id: (nome, ramo, durata gg lav, ES, float, inizio, fine, nome breve Gantt)
ACT = {
    'A': ("Setup Infrastruttura",                'crit', 9,  0,   0,  date(2025,10,15), date(2025,10,27), "A &middot; Setup Infrastruttura"),
    'B': ("Backend Auth + DB",                   'crit', 9,  9,   0,  date(2025,10,28), date(2025,11,7),  "B &middot; Backend Auth + DB"),
    'C': ("Game Engine Foundation",              'ge',   9,  9,   22, date(2025,10,28), date(2025,11,7),  "C &middot; Game Engine Foundation"),
    'D': ("Backend Gestione Partite",            'crit', 20, 18,  0,  date(2025,11,10), date(2025,12,5),  "D &middot; Backend Gestione Partite"),
    'E': ("WebSocket Server Setup",              'soc',  9,  18,  37, date(2025,12,9),  date(2025,12,19), "E &middot; WebSocket Server"),
    'F': ("Game Engine Regole Core",             'ge',   23, 18,  22, date(2025,11,10), date(2025,12,11), "F &middot; GE Regole Core"),
    'G': ("Backend Persistenza Stato",           'crit', 9,  38,  0,  date(2025,12,9),  date(2025,12,19), "G &middot; Backend Persistenza"),
    'H': ("Real-Time Eventi",                    'soc',  16, 27,  37, date(2025,12,22), date(2026,1,16),  "H &middot; Real-Time Eventi"),
    'I': ("Game Engine Punteggi e Maraffa",      'ge',   16, 41,  22, date(2025,12,15), date(2026,1,9),   "I &middot; GE Punteggi/Maraffa"),
    'J': ("Frontend Homepage + Login",           'crit', 11, 47,  0,  date(2025,12,22), date(2026,1,9),   "J &middot; FE Homepage + Login"),
    'K': ("Chat + Disconnessioni",               'soc',  10, 43,  37, date(2026,1,19),  date(2026,1,30),  "K &middot; Chat + Disconnessioni"),
    'L': ("Game Engine Testing",                 'ge',   15, 57,  22, date(2026,1,12),  date(2026,1,30),  "L &middot; GE Testing"),
    'M': ("Frontend Dashboard + Stanza",         'crit', 15, 58,  0,  date(2026,1,12),  date(2026,1,30),  "M &middot; FE Dashboard + Stanza"),
    'N': ("Sistema Amicizie",                    'soc',  15, 53,  37, date(2026,2,2),   date(2026,2,20),  "N &middot; Sistema Amicizie"),
    'O': ("Integration Testing GE",              'ge',   10, 72,  22, date(2026,2,2),   date(2026,2,13),  "O &middot; Integration Testing GE"),
    'P': ("Frontend Tavolo da Gioco",            'crit', 40, 73,  0,  date(2026,2,2),   date(2026,3,27),  "P &middot; FE Tavolo da Gioco"),
    'Q': ("Frontend Profili + Notifiche",        'soc',  10, 68,  37, date(2026,2,23),  date(2026,3,6),   "Q &middot; FE Profili + Notifiche"),
    'R': ("Testing End-to-End",                  'critR',11, 104, 0,  date(2026,3,17),  date(2026,3,31),  "R &middot; Testing E2E (SS+31 su P)"),
    'S': ("UAT + Bug Fixing",                    'crit', 17, 115, 0,  date(2026,4,1),   date(2026,4,24),  "S &middot; UAT + Bug Fixing"),
    'T': ("Preparazione Lancio",                 'crit', 9,  132, 0,  date(2026,4,27),  date(2026,5,8),   "T &middot; Preparazione Lancio"),
}
# archi FS (pred -> succ); il legame P->R (SS+31) è disegnato a parte
EDGES = [('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('D','G'),('E','H'),
         ('F','I'),('G','J'),('H','K'),('I','L'),('J','M'),('K','N'),('L','O'),
         ('M','P'),('N','Q'),('O','R'),('Q','S'),('R','S'),('S','T')]
CRIT_EDGES = {('A','B'),('B','D'),('D','G'),('G','J'),('J','M'),('M','P'),('R','S'),('S','T')}

FLOAT_GE, FLOAT_SOC = 22, 37
GANTT_MILESTONES = [date(2025,10,27), date(2025,12,19), date(2026,1,30), date(2026,3,27),
                    date(2026,3,31),  date(2026,4,24),  date(2026,5,15)]
MILE_LEGEND = [("M1","27 Ott 2025","Infrastructure Ready"),("M2","19 Dic 2025","Backend Core Complete"),
               ("M3","30 Gen 2026","Game Engine Complete"),("M4","27 Mar 2026","Frontend Core Complete"),
               ("M5","31 Mar 2026","MVP Beta"),("M6","24 Apr 2026","UAT Approved"),
               ("M7","15 Mag 2026","Production Launch")]

# ---------- layout network ----------
S_NET = 5.5          # px per giorno lavorativo
X0 = 60
ROW_Y = {'crit': 74, 'critR': 132, 'ge': 194, 'soc': 314}   # y del rettangolo (h=44)
def cy(row): return ROW_Y[row] + 22
def nx(k):  return X0 + ACT[k][3] * S_NET
def nw(k):  return ACT[k][2] * S_NET
def nend(k): return nx(k) + nw(k)

# ---------- layout gantt ----------
S_G = 3.55           # px per giorno di calendario
GX0 = 214            # x del 15 Ott
def gx(d): return GX0 + (d - START).days * S_G
def gw(a, b): return ((b - a).days + 1 - 1) * S_G  # larghezza = span in giorni

CSS = """  :root {
    --blu: #007bff;
    --viola: #6f42c1;
    --rosso-mattone: #b85450;
    --rosa: #e83e8c;
    --giallo: #ffc107;
    --grigio: #6c757d;
    --verde-bottiglia: #28a745;
    --legno: #fd7e14;
    --testo-scuro: #212529;
  }
  * { box-sizing: border-box; }
  body {
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    color: var(--testo-scuro);
    max-width: 1060px;
    margin: 24px auto;
    padding: 0 20px;
    line-height: 1.35;
  }
  h1 { font-size: 1.5rem; margin-bottom: 0.1rem; }
  .sub { color: #666; font-size: 0.85rem; margin-top: 0; margin-bottom: 14px; }
  h2 { font-size: 1.05rem; margin: 24px 0 8px; }
  h3 { font-size: 0.88rem; margin: 14px 0 6px; }
  .note {
    font-size: 0.76rem; color: #444; background: #f6f6f6;
    padding: 8px 12px; border-left: 4px solid var(--grigio); margin-bottom: 16px;
  }

  .stats-row { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 20px; }
  .stat {
    flex: 1 1 130px;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
    border: 1px solid #e9ecef;
  }
  .stat .value { font-size: 1.1rem; font-weight: 700; display: block; }
  .stat .label { font-size: 0.66rem; color: #666; text-transform: uppercase; letter-spacing: 0.02em; }
  .stat.crit .value { color: var(--rosso-mattone); }
  .stat.launch .value { color: var(--legno); }

  .chart-wrap { overflow-x: auto; margin-bottom: 8px; }
  svg { display: block; }

  .chart-legend { display: flex; flex-wrap: wrap; gap: 12px; font-size: 0.74rem; margin: 6px 0 14px; align-items: center; }
  .chart-legend span { display: inline-flex; align-items: center; gap: 5px; }
  .chip { width: 11px; height: 11px; border-radius: 3px; display: inline-block; }
  .chip.line { width: 16px; height: 3px; border-radius: 0; }
  .chip.diamond { width: 9px; height: 9px; border-radius: 2px; transform: rotate(45deg); display: inline-block; }

  .cp-strip {
    background: color-mix(in srgb, var(--rosso-mattone) 10%, white);
    border: 1px solid color-mix(in srgb, var(--rosso-mattone) 35%, white);
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 0.78rem;
    margin-bottom: 14px;
  }
  .cp-strip strong { color: var(--rosso-mattone); }
  .cp-strip .path { font-weight: 600; letter-spacing: 0.02em; }

  .id-legend {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 3px 14px;
    font-size: 0.68rem;
    background: #fafafa;
    border: 1px solid #eee;
    border-radius: 6px;
    padding: 8px 12px;
    margin-bottom: 18px;
  }
  .id-legend .grp-title { grid-column: 1 / -1; font-weight: 700; font-size: 0.7rem; margin-top: 6px; }
  .id-legend .grp-title:first-child { margin-top: 0; }
  .id-legend .grp-title.crit { color: var(--rosso-mattone); }
  .id-legend .grp-title.ge, .id-legend .grp-title.soc { color: var(--verde-bottiglia); }
  .id-legend .item b { display: inline-block; width: 14px; }

  .mile-legend {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px 14px;
    font-size: 0.68rem;
    margin-bottom: 16px;
  }
  .mile-legend .m { background: #fff8ec; border: 1px solid #f1dcb0; border-radius: 6px; padding: 5px 8px; }
  .mile-legend .m b { color: #7a4a00; }

  .sens-row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 16px; }
  .sens { flex: 1 1 280px; background: #f8f9fa; border: 1px solid #e9ecef; border-radius: 8px; padding: 9px 12px; font-size: 0.74rem; }
  .sens .stitle { font-weight: 700; font-size: 0.76rem; display: block; margin-bottom: 3px; }
  .sens .simpact { color: var(--verde-bottiglia); font-weight: 600; }
  .sens.crit-scenario .simpact { color: var(--rosso-mattone); }

  @media print {
    .note { display: none; }
    @page { size: A4 landscape; margin: 9mm; }
    body { margin: 0; max-width: none; }
    .page-break { page-break-before: always; }
  }"""


def network_svg():
    width = round(nend('T') + 40, 1)
    out = [f'<svg viewBox="0 0 {width} 380" width="{width}" height="380">', '<defs>',
           '<marker id="arrRed" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="var(--rosso-mattone)"/></marker>',
           '<marker id="arrBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="var(--blu)"/></marker>',
           '</defs>',
           '<text x="60" y="14" font-size="9" fill="#888">giorni lavorativi (CPM) &rarr;</text>']
    for g in range(0, CP_DAYS + 1, 20):
        x = round(X0 + g * S_NET, 1)
        out.append(f'<line x1="{x}" y1="20" x2="{x}" y2="366" stroke="#f0f0f0" stroke-width="1"/>')
        out.append(f'<text x="{x}" y="376" font-size="8" text-anchor="middle" fill="#999">{g}g</text>')
    out += ['<text x="4" y="90" font-size="9.5" font-weight="700" fill="var(--rosso-mattone)">CRITICO</text>',
            '<text x="4" y="101" font-size="7.3" fill="#999">float 0</text>',
            '<text x="4" y="210" font-size="9.5" font-weight="700" fill="var(--verde-bottiglia)">GAME</text>',
            '<text x="4" y="221" font-size="7.3" fill="#999">ENGINE</text>',
            f'<text x="4" y="231" font-size="7.3" fill="#999">float {FLOAT_GE}gg</text>',
            '<text x="4" y="330" font-size="9.5" font-weight="700" fill="var(--verde-bottiglia)">CHAT/</text>',
            '<text x="4" y="341" font-size="7.3" fill="#999">SOCIAL</text>',
            f'<text x="4" y="351" font-size="7.3" fill="#999">float {FLOAT_SOC}gg</text>']
    # archi
    for a, b in EDGES:
        ya, yb = cy(ACT[a][1]), cy(ACT[b][1])
        x1, x2 = round(nend(a), 1), round(nx(b) - 4, 1)
        if (a, b) in CRIT_EDGES:
            out.append(f'<line x1="{x1}" y1="{ya}" x2="{x2}" y2="{yb}" stroke="var(--rosso-mattone)" stroke-width="2.6" marker-end="url(#arrRed)"/>')
        else:
            out.append(f'<line x1="{x1}" y1="{ya}" x2="{x2}" y2="{yb}" stroke="var(--blu)" stroke-width="1.3" stroke-opacity="0.75" marker-end="url(#arrBlue)"/>')
    # legame SS P->R (fast tracking): freccia rossa tratteggiata dal corpo di P all'inizio di R
    xr = round(nx('R'), 1)
    out.append(f'<line x1="{xr}" y1="118" x2="{xr}" y2="{ROW_Y["critR"] - 4}" stroke="var(--rosso-mattone)" stroke-width="2" stroke-dasharray="4,2.5" marker-end="url(#arrRed)"/>')
    out.append(f'<text x="{xr - 5}" y="{ROW_Y["critR"] - 6}" font-size="7" text-anchor="end" fill="var(--rosso-mattone)" font-weight="700">SS+31</text>')
    # nodi
    for k, (nome, row, dur, es, fl, *_rest) in ACT.items():
        x, w, y = round(nx(k), 1), round(nw(k), 1), ROW_Y[row]
        tx = round(x + w / 2, 1)
        if row in ('crit', 'critR'):
            out.append('<g>')
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="5" fill="var(--rosso-mattone)"/>')
            out.append(f'<text x="{tx}" y="{y + 16}" font-size="12" font-weight="700" text-anchor="middle" fill="#fff">{k}</text>')
            out.append(f'<text x="{tx}" y="{y + 27}" font-size="7.6" text-anchor="middle" fill="#fff" opacity="0.9">{dur}gg &middot; ES{es}</text>')
            if row == 'critR':
                out.append(f'<text x="{tx}" y="{y + 37}" font-size="7.2" text-anchor="middle" fill="#fff" opacity="0.85">fast tracking</text>')
            out.append('</g>')
        else:
            out.append('<g>')
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="5" fill="color-mix(in srgb, var(--verde-bottiglia) 16%, white)" stroke="var(--verde-bottiglia)" stroke-width="1.3"/>')
            out.append(f'<text x="{tx}" y="{y + 16}" font-size="12" font-weight="700" text-anchor="middle" fill="#1e5b2f">{k}</text>')
            out.append(f'<text x="{tx}" y="{y + 27}" font-size="7.6" text-anchor="middle" fill="#1e5b2f" opacity="0.9">{dur}gg &middot; ES{es}</text>')
            out.append(f'<text x="{tx}" y="{y + 37}" font-size="7.2" text-anchor="middle" fill="#1e5b2f" opacity="0.85">float {fl}gg</text>')
            out.append('</g>')
    # milestone del network (rombi), numerazione allineata alla tabella Gantt M1-M7:
    # M2 dopo G (Backend Core), M3 dopo L (Game Engine), M4 dopo P (Frontend), M6 dopo S (UAT)
    for label, x, y in [('M2', nx('J'), 62), ('M3', nx('O'), 182), ('M4', nend('P'), 62), ('M6', nend('S'), 62)]:
        out.append(f'<g transform="translate({round(x,1)},{y})">')
        out.append('<path d="M0,-8 L8,0 L0,8 L-8,0 Z" fill="var(--testo-scuro)"/>')
        out.append(f'<text x="0" y="-12" font-size="7.5" text-anchor="middle" fill="var(--testo-scuro)" font-weight="700">{label}</text>')
        out.append('</g>')
    out.append('</svg>')
    return '\n'.join(out)


def gantt_svg():
    rows = ['A','B','D','G','J','M','P','R','S','T','C','F','I','L','O','E','H','K','N','Q']
    width = round(gx(date(2026, 5, 15)) + 30, 1)
    out = [f'<svg viewBox="0 0 {width} 454" width="{width}" height="454">']
    months = [(date(2025,11,1),'Nov'),(date(2025,12,1),'Dic'),(date(2026,1,1),'Gen'),
              (date(2026,2,1),'Feb'),(date(2026,3,1),'Mar'),(date(2026,4,1),'Apr'),(date(2026,5,1),'Mag')]
    for d, lab in months:
        x = round(gx(d), 1)
        out.append(f'<line x1="{x}" y1="24" x2="{x}" y2="434" stroke="#eee" stroke-width="1"/>')
        out.append(f'<text x="{round(x+3,1)}" y="20" font-size="9" fill="#888">{lab}</text>')
    out.append(f'<line x1="{GX0}" y1="24" x2="{GX0}" y2="434" stroke="#ccc" stroke-width="1.2" stroke-dasharray="2,2"/>')
    out.append(f'<text x="{GX0}" y="20" font-size="8.3" fill="#666" font-weight="600">15 Ott</text>')
    out.append('<rect x="0" y="30" width="6" height="200" fill="var(--rosso-mattone)"/>')
    out.append('<rect x="0" y="230" width="6" height="100" fill="var(--verde-bottiglia)"/>')
    out.append('<rect x="0" y="330" width="6" height="100" fill="var(--verde-bottiglia)"/>')
    band_w = round(width - 30 + 30 - 15.4, 1)  # come originale: fascia fino al bordo destro
    band_w = round(width - 16, 1)
    for i, k in enumerate(rows):
        ytxt, ybar = 44 + i * 20, 33 + i * 20
        if i % 2 == 0:
            out.append(f'<rect x="6" y="{30 + i * 20}" width="{band_w}" height="20" fill="#fafafa"/>')
        nome_g = ACT[k][7]
        ini, fin = ACT[k][5], ACT[k][6]
        x, w = round(gx(ini), 1), round(((fin - ini).days) * S_G, 1)
        out.append(f'<text x="10" y="{ytxt}" font-size="8.4" fill="#333">{nome_g}</text>')
        if ACT[k][1] in ('crit', 'critR'):
            out.append(f'<rect x="{x}" y="{ybar}" width="{w}" height="12" rx="3" fill="var(--rosso-mattone)"/>')
        else:
            fl = ACT[k][4]
            out.append(f'<rect x="{x}" y="{ybar}" width="{w}" height="12" rx="3" fill="var(--verde-bottiglia)" opacity="0.85"/>')
            out.append(f'<text x="{round(x + w + 4, 1)}" y="{ytxt - 1}" font-size="6.8" fill="#888">float {fl}gg</text>')
    for d in GANTT_MILESTONES:
        x = round(gx(d), 1)
        out.append(f'<line x1="{x}" y1="24" x2="{x}" y2="434" stroke="var(--legno)" stroke-width="1" stroke-dasharray="3,2"/>')
        out.append(f'<path transform="translate({x},24)" d="M0,-6 L6,0 L0,6 L-6,0 Z" fill="var(--legno)"/>')
    out.append('</svg>')
    return '\n'.join(out)


def main():
    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Project Network Diagram &amp; Gantt Chart - MaraffaOnline</title>
<style>
{CSS}
</style>
</head>
<body>

<h1>Project Network Diagram &amp; Gantt Chart &mdash; MaraffaOnline</h1>
<p class="sub">Allegato 3.5 &middot; {VERSION} &middot; PlayHeritage Labs</p>

<div class="note">Vista condensata: Network Diagram sui 20 nodi principali (asse = giorni lavorativi CPM, festivit&agrave; italiane escluse) e Gantt sulle stesse 20 attivit&agrave; (asse = calendario reale). Il dettaglio per sprint/sotto-task, l'analisi dei rischi e il processo di aggiornamento dinamico restano in <code>Allegato3.5-ProjectNetworkDiagram-Gantt.md</code>.</div>

<div class="stats-row">
  <div class="stat crit"><span class="value">{CP_DAYS}gg</span><span class="label">Critical Path (lavorativi)</span></div>
  <div class="stat"><span class="value">20</span><span class="label">Attivit&agrave; principali</span></div>
  <div class="stat"><span class="value">30 sett.</span><span class="label">15 Ott 2025 &rarr; 15 Mag 2026</span></div>
  <div class="stat"><span class="value">15</span><span class="label">Sprint (0&ndash;14, 2 sett.)</span></div>
  <div class="stat launch"><span class="value">15 Mag</span><span class="label">Lancio MVP 2026</span></div>
  <div class="stat"><span class="value">3</span><span class="label">Rami paralleli</span></div>
</div>

<h2>Network Diagram (Critical Path Method)</h2>

<div class="cp-strip"><strong>Critical Path ({CP_DAYS}gg lavorativi, float 0):</strong> <span class="path">A &rarr; B &rarr; D &rarr; G &rarr; J &rarr; M &rarr; P &rarr; R &rarr; S &rarr; T</span> &mdash; qualsiasi ritardo su questi nodi sposta la data di lancio. <strong>P (Frontend Tavolo da Gioco, 40gg)</strong> &egrave; il singolo nodo pi&ugrave; lungo sul percorso critico; <strong>R (Testing E2E)</strong> &egrave; in <strong>fast tracking</strong> (Start-to-Start con lag 31gg) sulla coda di P. La fine di T (8 Mag) lascia ~1 settimana di margine sul lancio del 15 Mag.</div>

<div class="chart-wrap">
{network_svg()}
</div>

<div class="chart-legend">
  <span><i class="chip" style="background:var(--rosso-mattone)"></i> Nodo critico (float 0)</span>
  <span><i class="chip" style="background:color-mix(in srgb, var(--verde-bottiglia) 16%, white); border:1.5px solid var(--verde-bottiglia)"></i> Nodo con float (&gt;5gg)</span>
  <span><i class="chip line" style="background:var(--rosso-mattone)"></i> Dipendenza critica</span>
  <span><i class="chip line" style="background:var(--blu)"></i> Dipendenza non critica</span>
  <span><i class="chip diamond" style="background:var(--testo-scuro)"></i> Milestone</span>
</div>
<div class="note" style="margin-top:-4px;">Nessuna attivit&agrave; ha float 1&ndash;5gg (fascia "near-critical" arancione della legenda originale): i due rami non critici hanno rispettivamente {FLOAT_GE}gg (Game Engine) e {FLOAT_SOC}gg (Chat/Social) di margine. Il legame tratteggiato <strong>SS+31</strong> indica il fast tracking di R sulla coda di P.</div>

<div class="id-legend">
  <div class="grp-title crit">Ramo Critico</div>
  <div class="item"><b>A</b>Setup Infrastruttura</div><div class="item"><b>B</b>Backend Auth + DB</div><div class="item"><b>D</b>Backend Gestione Partite</div><div class="item"><b>G</b>Backend Persistenza Stato</div>
  <div class="item"><b>J</b>Frontend Homepage + Login</div><div class="item"><b>M</b>Frontend Dashboard + Stanza</div><div class="item"><b>P</b>Frontend Tavolo da Gioco</div><div class="item"><b>R</b>Testing End-to-End (SS+31)</div>
  <div class="item"><b>S</b>UAT + Bug Fixing</div><div class="item"><b>T</b>Preparazione Lancio</div>
  <div class="grp-title ge">Ramo Game Engine (float {FLOAT_GE}gg)</div>
  <div class="item"><b>C</b>Game Engine Foundation</div><div class="item"><b>F</b>Game Engine Regole Core</div><div class="item"><b>I</b>Game Engine Punteggi e Maraffa</div><div class="item"><b>L</b>Game Engine Testing</div>
  <div class="item"><b>O</b>Integration Testing GE</div>
  <div class="grp-title soc">Ramo Chat/Social (float {FLOAT_SOC}gg)</div>
  <div class="item"><b>E</b>WebSocket Server Setup</div><div class="item"><b>H</b>Real-Time Eventi</div><div class="item"><b>K</b>Chat + Disconnessioni</div><div class="item"><b>N</b>Sistema Amicizie</div>
  <div class="item"><b>Q</b>Frontend Profili + Notifiche</div>
</div>

<div class="page-break"></div>
<h2>Gantt Chart</h2>
<p class="note" style="margin-top:0">Asse temporale = calendario reale: le barre includono weekend e festivit&agrave;, per questo appaiono pi&ugrave; lunghe dei giorni lavorativi del Network Diagram. La barra di R si sovrappone alla coda di P (fast tracking SS+31).</p>

<div class="chart-wrap">
{gantt_svg()}
</div>

<div class="chart-legend">
  <span><i class="chip" style="background:var(--rosso-mattone)"></i> Attivit&agrave; critica</span>
  <span><i class="chip" style="background:var(--verde-bottiglia); opacity:0.85"></i> Attivit&agrave; con float</span>
  <span><i class="chip diamond" style="background:var(--legno)"></i> Milestone (M1&ndash;M7)</span>
</div>

<div class="mile-legend">
{chr(10).join(f'  <div class="m"><b>{m}</b> &middot; {d} &mdash; {t}</div>' for m, d, t in MILE_LEGEND)}
</div>

<h2>Sensitivity Analysis (sintesi)</h2>
<div class="sens-row">
  <div class="sens crit-scenario"><span class="stitle">Scenario 1 &middot; P ritarda 10gg</span>Consumati i 5gg di margine, il lancio slitta di ~1 settimana. <span class="simpact">Azione:</span> comprimere S (UAT) 17&rarr;12gg + 1 dev part-time su P (+&euro;2.000).</div>
  <div class="sens"><span class="stitle">Scenario 2 &middot; L (+5gg bug critici)</span>L non &egrave; critico: il ritardo si propaga a O ma non a P (parallelo). <span class="simpact">Nessun impatto</span> sulla data di lancio (ramo GE: {FLOAT_GE}gg di float).</div>
  <div class="sens"><span class="stitle">Scenario 3 &middot; N ritarda 10gg</span>N ha {FLOAT_SOC}gg di float, ampiamente assorbente. <span class="simpact">Nessun impatto</span>: solo un ritardo &gt;{FLOAT_SOC}gg renderebbe critico il ramo Chat/Social.</div>
</div>

<div class="note">Dettaglio per sprint (attivit&agrave; + sotto-task con date), tabelle Forward/Backward Pass complete, analisi rischi con mitigazioni, integrazione Network&harr;Gantt e processo di aggiornamento dinamico: vedi <code>Allegato3.5-ProjectNetworkDiagram-Gantt.md</code>.</div>

</body>
</html>
"""
    import os
    path = os.path.join(os.path.dirname(__file__), '..', 'Planning', 'Allegato3.5-NetworkGantt.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Scritto {os.path.normpath(path)}")
    # verifica di coerenza: catena critica contigua e durata totale
    assert ACT['T'][3] + ACT['T'][2] == CP_DAYS, "EF(T) != durata critical path"
    for a, b in [('A','B'),('B','D'),('D','G'),('G','J'),('J','M'),('M','P'),('R','S'),('S','T')]:
        assert ACT[a][3] + ACT[a][2] == ACT[b][3], f"catena critica non contigua: {a}->{b}"
    assert ACT['P'][3] + 31 == ACT['R'][3], "lag SS P->R != 31"
    print(f"OK: critical path {CP_DAYS}gg, catena contigua, SS+31 verificato")


if __name__ == '__main__':
    main()
