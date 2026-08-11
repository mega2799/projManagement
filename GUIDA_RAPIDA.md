# Guida Rapida - Progetto MaraffaOnline

## Prima di Iniziare

**IMPORTANTE**: Ogni volta che lavori con Claude su questo progetto, ricordagli di leggere [claude.md](./claude.md)

```
"Ciao Claude, sto lavorando sul progetto MaraffaOnline.
Per favore leggi il file claude.md per avere il contesto ed il file GUIDA_RAPIDA per sapere cosa fare"
```

## Struttura del Lavoro

### Fase 1: Setup e Definizione ✅ COMPLETATA

- [x] Definire il contesto narrativo → **PlayHeritage Labs + Maraffa Forever**
- [x] Identificare i sottosistemi → **7 sottosistemi** (vedi `docs/sottosistemi_e_metodologie.md`)
- [x] Scegliere le metodologie → **Mix: Waterfall, Agile (Iterativo/Adattivo), Incrementale**
- [x] Scrivere Capitolo 1 - Introduzione → `Relazione/capitoli/01_introduzione.tex`

### Fase 2: Scoping

Creare tutti gli allegati della fase di Scoping (2.1 - 2.11)

### Fase 3: Planning

Creare tutti gli allegati della fase di Planning (3.1 - 3.5)

### Fase 4: Launching

Creare tutti gli allegati della fase di Launching (4.1 - 4.3)

### Fase 5: Monitoring & Control

Creare gli allegati di monitoraggio (5.1 - 5.2)

### Fase 6: Closing

Documentare la chiusura del progetto (6.1)

### Fase 7: Relazione Finale

Scrivere i 6 capitoli della relazione in LaTeX

## Come Lavorare con Claude

### 1. Definire il Contesto Narrativo

```
"Aiutami a creare il contesto narrativo per MaraffaOnline.
Devo inventare:
- Nome dell'azienda/startup
- Problema o opportunità di business
- Committente del progetto
- Obiettivo generale
Voglio qualcosa di originale e realistico."
```

### 2. Identificare i Sottosistemi

```
"Basandoti sul progetto MaraffaOnline, aiutami a identificare
i sottosistemi principali e le loro caratteristiche."
```

### 3. Scegliere le Metodologie

```
"Per ogni sottosistema di MaraffaOnline, aiutami a scegliere
la metodologia PM più adatta (Waterfall, Agile iterativo,
Agile adattivo, Incrementale) e a giustificare la scelta."
```

### 4. Creare un Allegato

```
"Creiamo l'Allegato 2.1 - Conditions of Satisfaction per MaraffaOnline.
Basati sulla struttura dell'esempio ma personalizza per il mio progetto."
```

### 5. Scrivere un Capitolo

```
"Scrivi il Capitolo 1 - Introduzione della relazione in LaTeX.
Usa il contesto che abbiamo definito per MaraffaOnline."
```

### 6. Creare Diagrammi/Grafici

```
"Crea il diagramma User Flow per MaraffaOnline in formato Mermaid/draw.io"
```

## Checklist Prima della Consegna

- [ ] Tutti gli allegati creati e riferiti nella relazione
- [ ] Relazione LaTeX completa (6 capitoli)
- [ ] PDF compilato correttamente
- [ ] Tutte le immagini/diagrammi presenti in /img/
- [ ] Ogni scelta metodologica ben argomentata
- [ ] Nessun plagio dalla relazione di riferimento
- [ ] Contesto narrativo originale e coerente
- [ ] Elaborato concordato con il docente
- [ ] Materiale pronto per la consegna (zip o PDF unico)

## Strumenti Utili

### LaTeX

```bash
cd Relazione
pdflatex main.tex
```

### Visualizzare TODO

Chiedi a Claude: "Mostrami la TODO list e dimmi su cosa lavorare"

### Creare Diagrammi

- Draw.io: <https://app.diagrams.net/>
- Mermaid: <https://mermaid.live/>
- Lucidchart: <https://www.lucidchart.com/>

### Creare Grafici

- Excel/LibreOffice Calc per grafici Cash Flow ed Earned Value
- Python matplotlib per grafici personalizzati

## Domande Frequenti

**Q: Posso copiare dalla relazione di esempio?**
A: NO. Usa la struttura e impara l'approccio, ma crea contenuto completamente originale.

**Q: Devo implementare il software?**
A: NO. L'obiettivo è dimostrare capacità di gestione progetto, non di sviluppo.

**Q: Quanto deve essere lunga la relazione?**
A: Non c'è limite specifico, ma la relazione di esempio è circa 12 pagine + allegati.

**Q: Devo usare tutti gli strumenti visti a lezione?**
A: Devi usare quelli appropriati al tuo progetto, giustificando le scelte.

## Link Utili

- Email docente: <marco.boschetti@unibo.it>
- Relazione esempio: ../relazioneSofy.pdf
- Linee guida: ../slides/Progetto - Linee Guida - Ver.2.3.pdf

---

## Stato Progetto

### ✅ Fase 1: Introduzione - COMPLETATA

**Contesto Narrativo Definito**:
- Azienda: PlayHeritage Labs (spin-off UniBo)
- Committente: Maraffa Forever (150 appassionati)
- Budget: €25.000 | Durata: 7 mesi
- Target: 25-45 anni

**Gioco**: Maraffone (Beccaccino/Trionfo)
- Regole ufficiali documentate in: `Scoping/REGOLE-UFFICIALI-MARAFFONE.md`
- Punteggio: Assi=1pt, Figure/2/3=1/3pt, Carte 4-7=0pt
- Vittoria: 41 punti e una figura (o 31 variante corta)
- Maraffa/Cricca: Asso+2+3 di briscola = 3 punti bonus

### ✅ Fase 2: Scoping - COMPLETATA

**Documenti Creati (Allegati 2.1-2.11)**:
- Project Scoping Meeting
- Conditions of Satisfaction
- Project Overview Statement (POS)
- Risk Analysis (Risk Rating Matrix)
- Business Model Canvas
- Analisi SWOT
- Prototyping (mockup v1 → v2)
- Requirements Breakdown Structure (RBS)
- User Stories (formato INVEST)
- PM Life Cycle Models
- Approval Process

**Correzioni Regole Maraffone**: Tutti i documenti ora rispettano le regole ufficiali del Maraffone/Beccaccino (punteggio corretto, vittoria a 41 punti, ecc.)

### ✅ Fase 3: Planning - COMPLETATA

**7 Sottosistemi Identificati**:

1. Game Engine → Waterfall
2. Backend Server → Agile Iterativo
3. Real-Time Communication → Agile Adattivo
4. Frontend Web → Agile Iterativo
5. Mobile Application → Won't Have (MVP)
6. Social & Community → Incrementale
7. Infrastructure & DevOps → Incrementale

**Documenti Creati (Allegati 3.1-3.5)**:
1. ✅ Work Breakdown Structure (WBS) - Scomposizione gerarchica completa (6 sottosistemi di sviluppo + PM trasversale; 43 attività, 160 task)
2. ✅ MoSCoW Analysis - Prioritizzazione di 302 giorni-uomo (Must 75,8%, Should 18,9%, Could 5,3%)
3. ✅ Product Backlog - 15 sprint, solo il lavoro che scorre negli sprint (Backend, Real-Time, Frontend + user story Social)
4. ✅ Cash Flow Management - Budget €25.000, 7 mesi, con grafici Excel
5. ✅ Project Network Diagram + Gantt Chart - Critical Path 141 giorni lavorativi (fast tracking P→R), CSV per Notion

**Note Metodologiche**:
- Product Backlog include SOLO il lavoro esprimibile come user story e realizzato negli sprint; Game Engine (Waterfall) e Infrastructure (Incrementale) restano in WBS/Gantt
- Game Engine (Waterfall) e Infrastructure (Incrementale) documentati in WBS/Gantt
- Grafici Cash Flow creati con Excel e integrati nel documento

### ✅ Fase 4: Launching - COMPLETATA

**Documenti Creati (Allegati 4.1-4.3)**:
1. ✅ Project Kick-Off Meeting - Meeting 15/10/2025 con agenda completa, Q&A, action items, next steps
2. ✅ RASCI Matrix (Allegato 4.2) - Responsibility assignment a livello di attività WBS (i task ereditano la riga dell'attività)
3. ✅ Regole Operative (Allegato 4.3) - Processi operativi (problem solving, decision making, conflict resolution, brainstorming, meetings, change management, comunicazione)

**Note**:
- RASCI Matrix a livello di attività WBS su 8 aree (6 sottosistemi + QA + PM), 51 righe
- Regole Operative definiscono 6 riunioni ricorrenti (Daily Standup, Sprint Planning, Backlog Refinement, Sprint Review, Retrospective, Status Meeting)
- Framework decisionale a 3 livelli (Operativo/Tattico/Strategico)
- Change Management Process formalizzato con Project Impact Statement

### ✅ Fase 5: Monitoring & Control - COMPLETATA

**Documento Creato**:
- ✅ Capitolo 5 - Monitoring and Control (integrato nella relazione, stile discorsivo)
  - Monitoraggio continuo (Daily Standup, Notion Database, cultura aziendale)
  - Project Status Meetings settimanali con Stoplight Reports
  - Sprint Review e Retrospective
  - Problem Solving Strategy
  - Earned Value Management con grafico
  - Gantt Chart tracking
  - Velocity tracking per sistemi Agile
  - Quality Metrics (test coverage, bug tracking, code quality)
  - Risk Monitoring
  - Risultati e rispetto criteri

**Note**:
- Documento discorsivo integrato nella relazione principale, non allegati separati (come nella relazione esempio)
- Include grafico Earned Value con analisi Cost Variance e Schedule Variance
- Descrive tutti gli strumenti di monitoring (Stoplight, EVM, Velocity, Quality Metrics)

### ✅ Fase 6: Closing - COMPLETATA

**Documento Creato**:

- ✅ Capitolo 6 - Closing (integrato nella relazione, stile discorsivo)
  - Accettazione formale (11 Maggio 2026, Giovanni firma senza modifiche)
  - Final Project Report (9 sezioni, consegnato 12 Maggio 2026)
  - Audit Post-Implementazione (tutti i criteri soddisfatti)
  - Fattori di Successo (5 fattori chiave identificati)
  - Sfide Affrontate e Lezioni Apprese (5 sfide con lezioni specifiche)
  - Soddisfazione Cliente e Sviluppi Futuri (3 progetti proposti)
  - Impatto Business PlayHeritage Labs
  - Celebrazione e Chiusura (15 Maggio 2026, lancio pubblico)

**Risultati Finali**:

- Budget: €22.750/€25.000 (surplus €2.250, 9%)
- Timeline: 7 mesi esatti (15 Ott 2025 - 15 Mag 2026)
- Critical Path: 141 giorni lavorativi rispettati
- Launch: 50 utenti e 23 partite nelle prime 24h

**Note**:

- Documento discorsivo come Capitolo 5, non allegati separati
- Include audit completo con verifica di tutti i criteri
- Documenta lessons learned per progetti futuri
- Prospettive di collaborazione futura con 3 sviluppi proposti

### 🎉 Fase 7: Relazione Finale - PRONTA PER COMPILAZIONE

**Tutti i capitoli completati**:

- ✅ Capitolo 1 - Introduzione
- ✅ Capitolo 2 - Scoping (Allegati 2.1-2.11)
- ✅ Capitolo 3 - Planning (Allegati 3.1-3.5)
- ✅ Capitolo 4 - Launching (Allegati 4.1-4.3)
- ✅ Capitolo 5 - Monitoring & Control
- ✅ Capitolo 6 - Closing

---

**Ultimo aggiornamento**: 2026-08-11
