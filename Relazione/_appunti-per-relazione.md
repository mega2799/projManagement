# Appunti per la Relazione (materiale estratto dagli allegati)

> **File di lavoro** — NON è un deliverable e NON è incluso in `main.tex`.
> Raccoglie i contenuti di **giustificazione/teoria** rimossi dagli allegati (che devono restare artefatti operativi, Sezione 2) per essere rielaborati nei **capitoli della relazione LaTeX** (Sezione 1 – descrizione dell'approccio). Ogni blocco indica l'allegato di provenienza.

---

## Cap. 3 — Planning

### Perché separare il Product Backlog (Agile) da WBS/Gantt (universale)
_Provenienza: Allegato 3.3 - Product Backlog (sezioni "Nota: Ambito" e "Perché Questa Separazione?")._

La separazione tra Product Backlog e WBS/Gantt è intenzionale e riflette la natura degli strumenti:

- **Product Backlog** = strumento Scrum/Agile puro. Gestito dal Product Owner (Marco Venturi), prioritizzato in modo continuo con MoSCoW dinamico, item stimati in story points (Fibonacci), organizzato per sprint con velocity tracking. Include **solo** il lavoro che scorre attraverso gli sprint: i sottosistemi iterativi/adattivi (Backend Server, Real-Time Communication, Frontend Web) e le user story di Social & Community (sottosistema Incrementale, ma realizzato dagli stessi team nelle stesse iterazioni e quindi tracciato sotto il sottosistema che lo implementa).
- **WBS + Gantt** = strumenti di Project Management universali. Gestiti dal Project Manager, includono **tutte** le metodologie (Waterfall, Agile, Incrementale), attività stimate in giorni lavorativi, timeline con critical path analysis.

Mischiare metodologie diverse nel Backlog comprometterebbe la coerenza della gestione sprint e la chiarezza dei ruoli Scrum (Product Owner, Scrum Master, Development Team). Per questo Game Engine (Waterfall) e Infrastructure & DevOps (Incrementale) sono tracciati esclusivamente in WBS (Allegato 3.1) e Gantt (Allegato 3.5), non nel Backlog. In sintesi: per i sottosistemi Agile il Product Backlog è la fonte primaria della gestione operativa degli sprint; per la visione d'insieme del progetto si fa riferimento a WBS e Gantt.

### Lettura dei numeri di velocity (Scrum pura vs team-wide)
_Provenienza: Allegato 3.3 - Product Backlog ("Lettura dei numeri di Velocity"). Rilevante anche per il Cap. 5 - Monitoring & Control (dove si cita la velocity 38,3)._

- La **velocity di 38,3 SP/sprint** monitorata nel Cap. 5 è **team-wide**: somma il lavoro completato su tutto il progetto (Backlog + Game Engine in Waterfall + Infrastructure Incrementale), non solo le user stories del Backlog. La media esclude lo Sprint 5 (22 Dic - 02 Gen), a capacità ridotta per le festività.
- Inquadramento definitivo (agosto 2026): **capacità vs carico**. La **capacity team-wide è ~40 SP/sprint** (quanto il team può completare); il **carico medio pianificato** è **~37 SP/sprint team-wide** (441 SP = 310 Backlog + ~131 equivalenti GE/Infra, sugli sprint di sviluppo 0-11) e **~28 SP/sprint di solo Backlog** (310 SP sugli Sprint 1-11). Il margine capacità-carico assorbe festività e variabilità. Lo Sprint 11 ospita solo le rifiniture del tavolo in fast tracking col testing; gli Sprint 12-14 non sono stimati in SP.
- **Attenzione, numeri superati da non reintrodurre**: "21 SP/sprint" (310/15, denominatore sbagliato) e "31 SP/sprint su Sprint 1-10" (superato quando gli sprint del backlog sono stati riallineati alle date del Gantt, v.3.1.0: il backlog è caricato sugli Sprint 1-11).
- La differenza tra le misure non è un'incoerenza: è la distinzione tra "metrica Scrum" (Backlog) e "metrica gestionale di team" (Monitoring). Utile spiegarla in relazione per prevenire la domanda all'orale.

### Critical path: 141 giorni lavorativi (NON 170) e fast tracking P→R
_Provenienza: revisione di coerenza di agosto 2026 (Allegato 3.5 v.2.0.0)._

- Il vecchio valore **170 gg era impossibile**: tra il 15 Ott 2025 e il 15 Mag 2026 ci sono solo **146 gg lavorativi** netti (festività italiane escluse). Le durate erano nominali, mai nettate sul calendario (es. B = "15 gg" dentro uno sprint di 2 settimane = 9 gg lavorativi reali). **Non reintrodurre 170.**
- Valore corretto: **141 gg lavorativi** = 15 Ott → 8 Mag (fine di T); il lancio del 15 Mag conserva 5 gg lavorativi (~1 settimana) di margine.
- **Fast tracking P→R**: legame Start-to-Start con lag 31 gg — R (Testing E2E, 17-31 Mar = Sprint 11) parte quando P ha completato 31/40 gg. È compressione della schedula da manuale (dispensa 7 - Planning: tabella FS/SS/FF/SF + Lag e "compressione della schedula"; "la compressione non è mai gratis" → rischio rework dichiarato e mitigato). Ottimo argomento d'orale.
- Float ricalcolati: ramo Game Engine **22 gg** (era 30), ramo Chat/Social **37 gg** (era 50).
- Milestone allineate: M1 27-Ott, M2 19-Dic, M3 30-Gen, **M4 27-Mar** (era 14-Mar, incoerente con la fine di P), M5 31-Mar, M6 24-Apr, M7 15-Mag.
- L'HTML dell'Allegato 3.5 si rigenera con `tools/genera-networkgantt-html.py` (contiene asserzioni di coerenza sulla catena critica).

### Contenuti rimossi dall'Allegato 2.9 con la revisione v.1.2.0 (02/08/2026)
_Rimosso il "Riepilogo User Stories per Sprint" (Sprint 2-6 con story points): era pianificazione dentro un documento di Scoping — stesso vizio già ripulito da CoS v.1.1.0 e 2.10 v.1.1.0 — e contraddiceva il calendario del Product Backlog. L'assegnazione delle US agli sprint vive solo nell'Allegato 3.3, la cui colonna US punta (da v.3.1.0) alle user story reali del 2.9._

### Contenuti rimossi dall'Allegato 3.3 con lo snellimento v.3.0.0 (02/08/2026)
_L'allegato è stato ridotto ad artefatto operativo (tabelle unificate per sottosistema + calendario sprint + DoD). Contenuti rimossi e loro destinazione:_

- **Scala story point con esempi** (1 pt ≈ 1-2h "aggiungere campo username"... 21 pt ≈ epic 2 settimane): ridotta a una riga di legenda nell'allegato; gli esempi discorsivi non servono altrove (la tecnica Planning Poker è già descritta in relazione §3.3).
- **Riepilogo effort con percentuali** (Frontend 163 SP = 52,6%, Backend 80 = 25,8%, Real-Time 67 = 21,6%): i subtotali restano nelle tabelle; le percentuali erano analisi ridondante. Se servisse un commento sulla concentrazione dell'effort sul Frontend, va in relazione §3.4.
- **Nota sui ~441 SP equivalenti** (310 Backlog + ~94 Game Engine + ~37 Infrastructure): la riconciliazione completa è già in relazione §3.4 e nel Cap. 5 Monitoring (nota metodologica velocity). Nell'allegato resta la riga di capacity.
- **Sezione Velocity Tracking e Burn-down** (target 35-45 SP/sprint, monitoraggio a fine sprint, carryover): materiale di monitoring → già coperto dal Cap. 5 (velocity effettive Sprint 1-7, media 38,3 escluso lo Sprint 5 natalizio).
- **Gestione Cambiamenti al Backlog** (proposta stakeholder → valutazione MoSCoW del PO → stima team → inserimento; Sprint Planning; Backlog Refinement a metà sprint, 1h): le cerimonie sono documentate nell'Allegato 4.3 - Regole Operative; il processo di change è nel Cap. 4 (Change Request) e nella sintesi del 4.3. Il **Backlog Refinement** (metà sprint, 1h) è stato **recuperato** il 2026-08-10 nella tabella delle cerimonie del 4.3.
- **Tabella "Relazione con Altri Documenti"** (Backlog ⊂ WBS; implementa MoSCoW; ~70% del budget; Gantt unifica): contenuto di raccordo da relazione, già coperto da §3.4.

---

## Registro: sezioni "Fonti e Riferimenti" commentate negli allegati

_Commentate con `<!-- -->` (non renderizzate, ma presenti nel file). Da reinserire o sostituire con fonti del corso (Wysocki, PMBOK, Scrum Guide) se in futuro lo si desidera._

- [x] `Planning/Allegato3.3-ProductBacklog.md`
- [x] `Planning/Allegato3.2-MoSCoW.md`
- [x] `Planning/Allegato3.4-CashFlow.md`
- [x] `Planning/Allegato3.5-ProjectNetworkDiagram-Gantt.md`
- [x] `Launching/Allegato4.1-ProjectKickOffMeeting.md`
- [x] `Launching/Allegato4.2-RASCI.md` — solo link-blog divulgativi sulla RACI/RASCI: non citabili come bibliografia.
- [x] `Launching/Allegato4.3-RegoleOperative.md` — **NOTA**: qui i riferimenti sono solidi (Scrum Guide 2020 per le cerimonie e la DoD, PMBOK 7th Edition per conflict resolution e change control, Lean/Toyota per i 5 Whys, Atlassian Team Playbooks per i working agreements). Sono fonti valide del corso: valgono la pena di essere citate nella relazione o reinserite come bibliografia vera.

## Note su altri allegati snelliti

- **Capitolo5-MonitoringControl (2026-08-11, due passate)**: snellito da ≈4.200 a ≈1.300 parole (da 9 a ≈3-4 pagine PDF). Prima passata: Stoplight e velocity in tabella, via teoria EVM e grafico ASCII. Seconda passata (calibrata sul Cap. 5 di relazioneSofy.pdf, che è UNA pagina di prosa senza numeri): **tolte le percentuali decorative** — % per singolo sprint, "2,3% dell'EV", "−1,2%", coverage 87% puntuale, Cyclomatic Complexity — la tabella velocity è diventata prosa (restano 38,3 di regime, il 21 natalizio col carryover e il calo dello Sprint 7), la riconciliazione ≈131/≈37/≈28 rimanda alla relazione Cap. 3, la tabella EVM perde le colonne CV/SV (derivabili; restano PV/EV/AC/CPI/SPI). La tabella EVM mensile e lo Stoplight di gennaio restano perché richiesti dalle linee guida ("Earned Value reports", "Stoplight reports"). Numerazione 5.1–5.11 invariata.

- **Capitolo6-Closing (2026-08-11)**: snellito da ≈3.100 a ≈1.300 parole (da 7 a ≈4 pagine PDF), trasformandolo in registro operativo: audit post-implementazione e lessons learned convertiti in **tabelle** (criterio→verifica; sfida→cosa è successo→lezione), fattori di successo in elenco, tagliate le conclusioni narrative e l'introduzione sull'importanza della fase (contenuti già coperti, in forma concentrata, dalla relazione `06_closing.tex`). Numerazione sezioni 6.1–6.8 invariata (la ex 6.9 "Conclusioni" è assorbita in coda alla 6.8); **tutti i fatti e i numeri conservati** (11/05 partita+firma, 12/05 report 9 sezioni, 13/05 audit, 185ms, 4,5/5, 80%, 30/28 action item, 17/14 blocker, velocity 38,3, surplus €2.250, 5 lessons con i loro numeri, stime sviluppi futuri, 24h: 50 registrati/23 partite).

- **Allegato 4.2 → 4.2 + 4.3 (2026-08-10)**: la RASCI Matrix e le Regole Operative erano un unico allegato da 14 pagine. Separate: il 4.2 resta la matrice (registro testuale + companion HTML visuale), il 4.3 raccoglie le regole operative riscritte in forma schematica (una tabella per regola invece della prosa), con l'aggiunta delle sintesi di Change Management e Comunicazione a supporto delle sezioni 4.4 e 4.5. Motivazione: destinatari e cicli di aggiornamento diversi, e la relazione di riferimento adotta la stessa separazione in due allegati.

- **Allegato 3.1 - WBS**: la sezione "Note Metodologiche → Allineamento con Metodologie per Sottosistema" (che ripeteva l'Allegato 2.11) è stata condensata a un rimando. Il contenuto vive già in 2.11 e va nella relazione, Cap. 2/3.
- **Allegato 2.11 - Life Cycle Models**: la panoramica teorica dei 4 modelli PM (definizioni da manuale) è stata condensata in una legenda-tabella; la giustificazione applicata (mappatura per sottosistema, matrice decisionale, coordinamento) è rimasta perché è l'oggetto stesso dell'allegato.
- **Allegato 3.2 - MoSCoW**: i "Principi Applicati" (regola 60/20/20, definizione di Must Have, storico revisioni) sono criteri operativi applicati al progetto → tenuti; tolto solo il tag "(Best Practices 2026)" dal titolo.
