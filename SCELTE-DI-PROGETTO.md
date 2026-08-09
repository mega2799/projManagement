# Scelte di Progetto — Registro ragionato delle decisioni (MaraffaOnline)

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Registro completo delle **considerazioni fatte e delle scelte di progetto** che hanno portato all'elaborato attuale: per ogni decisione, la scelta, la motivazione e (dove utile) le alternative scartate e l'aggancio alla teoria del corso. È il "perché" dietro ogni documento.
> Documenti gemelli: `PREPARAZIONE-ORALE.md` (numeri a memoria e risposte pronte) e `FAQ.md` (domande previste all'orale con risposte).

---

## 1. Impostazione generale dell'elaborato

### 1.1 Il progetto e il contesto narrativo

- **Scelta**: piattaforma web multiplayer per la Maraffa (MaraffaOnline), sviluppata da **PlayHeritage Labs** (spin-off UniBo di Cesena, 2023, cultural heritage gaming) su commissione di **Maraffa Forever** (community di ~150 ex studenti romagnoli, crowdfunding interno di €25.000).
- **Motivazione**: (a) differenziazione totale dalla relazione di riferimento (Exploding Kittens: altro gioco, altra azienda, altro committente, altro problema — anti-plagio per costruzione); (b) la narrativa *spin-off + community* rende **internamente coerente ogni numero**: un budget piccolo (€25.000) è credibile solo se il team è part-time e il progetto ha valore strategico da pilota; l'esperta di dominio e i 20 beta tester escono naturalmente dalla community; il non-profit giustifica il break-even negativo.
- **Il problema è sociale e geografico**, non tecnologico: le app esistenti sono obsolete o single-player; la dimensione conviviale si è persa. Questo àncora il progetto alla definizione Wysocki di business value ("valore percepito dal destinatario").

### 1.2 Gestione, non implementazione

- **Scelta**: l'elaborato documenta la **gestione** del progetto (le linee guida lo richiedono esplicitamente: "NON implementare il software"). Nessun codice, nessun mockup grafico prodotto: i wireframe sono in ASCII con nota metodologica (Allegato 2.7), il Gantt è tabellare + CSV + HTML generato da script.
- **Motivazione**: coerenza col mandato d'esame; l'attenzione va tutta su processi, motivazioni e coerenza incrociata dei numeri — i criteri di valutazione delle linee guida (solidità delle argomentazioni, coerenza, originalità, strumenti, teoria).

### 1.3 I vincoli fondativi

| Vincolo | Valore | Perché così |
|---|---|---|
| Durata | 7 mesi (15/10/2025 – 15/05/2026) | orizzonte credibile per un MVP con team piccolo; genera un vincolo temporale "vero" da gestire con CPM e fast tracking |
| Budget | €25.000 fisso | dal crowdfunding: non negoziabile → il rischio budget si *accetta* (non si mitiga) comprimendo i costi (part-time) |
| Team | 5 persone part-time ~50% FTE (≈2,1 FTE medi) | risposta al vincolo economico; il progetto è pilota, il valore è strategico |
| Contratto | a corpo, 3 tranche 50/25/25 su milestone | budget fisso del committente → fixed-price; il 50% upfront garantisce liquidità per setup; le tranche legate a milestone misurabili (firma, Backend Core, core di gioco) |

### 1.4 Convenzioni documentali (scelte di forma, ma difendibili)

- **`.md` testuale = registro completo; `.html` companion = versione visiva a colori** per matrici/canvas/griglie (Risk Matrix, BMC, SWOT, WBS, MoSCoW, Cash Flow, Network+Gantt, RASCI). Motivo: il Markdown puro non fa celle unite né colori affidabili nelle pipeline PDF; l'HTML standalone con palette ufficiale di progetto sì.
- **Storico revisioni in ogni allegato**: le correzioni di coerenza sono documentate, non nascoste (es. ricalibrazione critical path da 170 a 141 gg; riclassificazione Maraffa). All'orale è un punto di forza: mostra controllo di configurazione.
- **Onestà documentale**: rimossi dialoghi ricostruiti e punteggi inventati dai verbali; le PNG non prodotte sono dichiarate tali; Notion è la single source of truth narrativa del progetto.

---

## 2. La scelta regina: approccio ibrido per sottosistema (Allegato 2.10)

È la decisione che caratterizza l'intero elaborato e da cui discendono quasi tutte le altre.

- **Scelta**: il prodotto è scomposto in **7 sottosistemi loosely coupled** e a ciascuno è applicato il ciclo di vita PMLC più adatto, scelto valutando **incertezza dei requisiti e incertezza della soluzione** (il quadrante goal/solution di Wysocki), più complessità tecnica, dipendenze e bisogno di feedback.

| Sottosistema | Modello | Motivazione primaria |
|---|---|---|
| Game Engine | **Waterfall (Linear, TPM)** | regole fisse, documentate e validate da Francesca Giuliani *prima* dello sviluppo; test case scrivibili a monte da partite a risultato noto; feedback continuo inutile (le regole gli utenti le conoscono già) |
| Backend Server | **Agile Iterativo (APM)** | obiettivi chiari, ma le API si raffinano col feedback del frontend che le consuma; sprint 2 settimane, demo allo sponsor |
| Frontend Web | **Agile Iterativo (APM)** | co-design con la community, demo bi-settimanali, user testing (Think Aloud) |
| Real-Time Communication | **Agile Adattivo (APM)** | incertezza massima: nessuna esperienza WebSocket; spike time-boxed, go/no-go, Kanban + pair programming Elena–Sara |
| Social & Community | **Incrementale (TPM)** | feature indipendenti, prioritizzate MoSCoW; se il tempo stringe i Must restano completi |
| Infrastructure & DevOps | **Incrementale (TPM)** | crescita per layer (hosting → CI/CD → monitoring), anti over-engineering (YAGNI) |
| Mobile Application | **Won't Have** (Incrementale post-MVP) | nativa iOS+Android ≈ +120 gg (+40% effort): incompatibile con budget e 7 mesi; supplisce il responsive web (87,5% success rate nello user testing) |

- **Alternative scartate**: metodologia monolitica unica ("overhead inutile in alcuni casi e rigidità dannosa in altri"); modello Extreme mai considerato perché nessun sottosistema ha *sia* goal *sia* solution ignoti.
- **Il costo dichiarato dell'ibrido è la sincronizzazione**, risolto con una **cadenza comune sovrapposta ai metodi**: scansione bi-settimanale per tutti (anche chi non lavora a sprint), demo il venerdì, milestone di integrazione mensili, settimane 4/8/12 dedicate a integrazione e bug fixing senza nuove feature.
- **Benefici argomentati**: rischio gestito per componente; nessun overhead superfluo (uno sprint planning sul Game Engine non avrebbe senso); modello riusabile su futuri giochi tradizionali (coerente con la mission dello spin-off).

---

## 3. Scelte di Scoping (Allegati 2.1–2.11)

### 2.1 Project Scoping Meeting
- Meeting del 15/09/2025 con **tutti** gli attori (sponsor, esperta di dominio, team completo), modalità ibrida. Decisioni chiave: **web-first** (mobile nativa rinviata), contratto a milestone, 20 beta tester dalla community, regole documentate da Giuliani. Verbale con decisioni numerate, action item, owner e scadenze — è il "Project Scoping Meeting" di Wysocki (deliverable: CoS, requisiti, POS).

### 2.2 Conditions of Satisfaction
- **22 condizioni in 5 tipologie** (temporale, economica, tecnica, qualitativa, gestione del lavoro), negoziate con lo schema **richiesta/risposta** (ciclo Request → Clarify → Response → Agree di Wysocki). Soglie tutte quantitative: 15/05/2026; €25.000; 100 partite simultanee (400 giocatori); latenza ≤500ms; API <200ms al 95° percentile; uptime 99%; soddisfazione ≥4,2/5; 80% utenti autonomi alla prima partita; WCAG 2.1 AA.
- **Scelta**: criteri temporali tenuti ad alto livello, senza calendario per sottosistema — la scomposizione è analisi successiva (separazione Scoping/Planning).

### 2.3 Project Overview Statement
- Struttura canonica in 5 sezioni, con una scelta distintiva: **tracciabilità numerica 1:1** tra i **6 obiettivi**, i criteri di successo e i rischi (ogni criterio e ogni gruppo di rischi porta il numero dell'obiettivo). Facilita l'audit finale (Cap. 6 verifica obiettivo per obiettivo).

### 2.4 Risk Analysis
- **Matrice 4×4** probabilità (A–D, range 25%) × impatto (Trascurabile→Disastroso), valore = P×I (1–16), con scala colori a **5 livelli** (introdotto "Rosso Critico 16" per isolare i 2 rischi top). **20 rischi**: 2 critici (16), 6 rossi (9–12), 7 arancioni, 5 gialli.
- **Strategie differenziate e motivate** (Accept/Mitigate/Contingency, come da corso):
  - **WebSocket (16) → Contingency**: spike tecnico 2 settimane + consulente esterno Dr. Nardi (€2.000 già accantonati) — non si può mitigare *subito* un'incognita di fattibilità, si pianifica cosa fare *se* lo spike fallisce.
  - **Budget (16) → Accept**: non mitigabile (il crowdfunding è quello) né trasferibile; accettato consapevolmente per il valore strategico del pilota, compensato dal modello part-time. Deciso formalmente nel meeting di approvazione (2.11).
  - **Scope creep (12) → Mitigate**: freeze dei requisiti dopo il POS + Change Control rigoroso.
  - **Race conditions (12) → Mitigate**: architettura **server-authoritative** + code review.

### 2.5 Business Model Canvas e 2.6 SWOT
- **BMC** (9 blocchi Osterwalder) per validare la sostenibilità: ripartizione del budget (70% sviluppo, 15% infrastruttura, 10% contingenza, 5% marketing/community), ricavi futuri (manutenzione, licensing, freemium) dichiarati come *visione*, non promesse.
- **SWOT estesa a matrice incrociata TOWS** (strategie SO/WO/ST/WT con coppie esplicite, es. W1+T1 → contingenza consulente) e **4 azioni immediate** — un passo oltre la SWOT descrittiva, buon punto di originalità.
- Coerenza incrociata voluta: W1 = rischio 2.1, W4 = rischio 6.4, T2 = rischio 6.2.

### 2.7 Prototyping
- **Due versioni di mockup**: v1 commentata dalla community → v2 **approvata e vincolante** per il frontend (riferimento contrattuale del design). Processo di **co-design partecipativo**: workshop con 10 membri, wireframe, feedback, user testing v2 con 8 membri (Think Aloud + task completion: 100%, 100%, 87,5%; soddisfazione 4,6/5).
- Decisione UX motivata da testing: **click to play** invece di drag & drop (affidabilità su mobile). Palette "calda" da osteria (rosso mattone, legno, verde bottiglia) per la fedeltà culturale.
- **Niente file grafici**: scelta dichiarata nel documento — l'elaborato gestisce il processo di design, non produce gli artefatti.

### 2.8 RBS e 2.9 User Stories
- **RBS per sottosistema** con classificazione F/NF/C e pre-etichette MoSCoW; requisiti con soglie concrete (JWT 7 giorni, sospensione partita max 5 min, RTO <4h, rate limiting 100 req/min...). Fonte regole: documentazione ufficiale della community, **validata formalmente da Giuliani** — è ciò che rende stabili i requisiti del Game Engine e quindi giustifica il Waterfall.
- **23 user stories in 7 epiche**, formato Connextra + criteri di accettazione + verifica INVEST tabellare. **Scelta di pulizia**: rimossi da ogni storia MoSCoW/Story Points/Sprint — appartengono al Planning (3.2, 3.3); il Product Backlog è l'unica fonte per l'assegnazione agli sprint. Separazione netta tra "cosa" (Scoping) e "quanto/quando" (Planning).

### 2.11 Approval Process
- Gate formale di fine fase: meeting del 02/10/2025 con **diritti di voto espliciti** (Marchetti unico decisionale, tutti gli altri consultivi — governance anti-stallo decisa in SWOT T6). Esito: approvazione + 2 riserve (monitoraggio WebSocket; amicizie condizionate a tempi) + pre-allerta del consulente. Autorizza il Planning.

---

## 4. Scelte di Planning (Allegati 3.1–3.5)

### 3.1 Work Breakdown Structure
- **Decomposizione per deliverable** (non per fasi), **100% rule** esplicita, **4 livelli** (Sottosistema → Funzione → Attività → Task), **160 task** sui 6 sottosistemi attivi **+ sezione 7 trasversale** (PM, documentazione, QA/UAT) — la 100% rule include il lavoro di gestione stesso.
- La Mobile App (Won't Have) non genera task: la WBS copre lo scope della release, la prioritizzazione la decide il MoSCoW (nota di raccordo esplicita).
- Il `.md` funge da **WBS Dictionary**; l'albero visuale è nell'HTML companion.

### 3.2 MoSCoW
- **Definizione rigorosa di Must** (4 criteri: indispensabile / obbligo di legge / sicurezza / non negoziabile per il committente) — non "importante", ma testabile.
- **302 giorni-uomo: Must 75,8% / Should 18,9% / Could 5,3%**, contro il target DSDM 60/20/20. **Scostamento dichiarato e motivato**: Game Engine e Real-Time sono il core differentiator (senza regole fedeli e partite fluide il prodotto non esiste); i Could compressi al 5,3% sono la scelta anti-scope-creep che protegge i 7 mesi. Won't espliciti: app nativa, social login, IA, push, tornei.
- **Processo dinamico**: 3 revisioni datate (post-POS, post-user-testing, approvazione col committente) + una **riclassificazione in corso d'opera** (novembre 2025: Maraffa/Cricca da Should a Must su input dell'esperta — documentata con nota di revisione e raccordata alle lessons learned).

### 3.3 Stime e Product Backlog
- **Due tecniche di stima, una filosofia** (stima collettiva anti-bias): **Delphi** per il Game Engine (requisiti stabili; stime anonime con motivazione, round fino a convergenza — evita l'ancoraggio) e **Planning Poker** con Fibonacci 1–21 per i sottosistemi Agile.
- **Criterio di inclusione nel Backlog = natura del lavoro, non etichetta metodologica del sottosistema**: entra ciò che è user story rivolta all'utente e scorre negli sprint (Backend, Real-Time, Frontend + le feature Social sotto il sottosistema che le implementa). Fuori: Game Engine (specifica congelata, validazione finale) e Infrastructure (attività ricorrenti/on-demand) — tracciati in WBS e Gantt. Motivo: mescolare cicli di vita diversi nel Backlog ne comprometterebbe leggibilità e ruoli Scrum.
- **Capacità vs carico, doppia lettura dichiarata**: capacity **40 SP/sprint team-wide** (aggrega Backlog + ~131 SP equivalenti di GE/Infra, totale ~441); carico medio pianificato **~37 team-wide** e **~28 di solo Backlog** (310 SP su Sprint 1–11); il margine assorbe festività e variabilità. Metrica gestionale per lo sponsor vs carico Scrum del team.
- **15 sprint (0–14)** allineati alle date del Gantt; Sprint 5 natalizio pianificato a capacità ridotta (21/40, carryover 19); Sprint 12–14 (UAT, lancio) non stimati in SP; **DoD a 8 criteri** (coverage >80%, code review, staging, approvazione PO...).

### 3.4 Cash Flow Management
- **Ipotesi strutturale**: l'ultimo inflow arriva a metà progetto (15/02) → la coda (mar–mag) è finanziata dal saldo cumulato → **outflow decrescente nei mesi 5–7** (team ridotto su testing/UAT/lancio). Risultato: **saldo cumulativo sempre positivo, minimo €2.250 all'ultimo mese**.
- **Contingency €4.664 (18,7%) distribuita mensilmente** come buffer per imprevisti/CR + **surplus finale €2.250 (9%)** destinato al post-lancio: margine di sicurezza complessivo ~27,7%.
- **Break-even analysis dichiaratamente negativa** (freemium non copre i costi operativi): conclusione onesta — progetto **non-profit per la community**, monetizzazione futura eventuale. Meglio dell'inventare ricavi.
- Controllo: report mensile al committente entro il 5 del mese, review settimanale, **soglie di variance con azioni graduate** (5–10% review spese; 10–15% posticipo Should/Could; >15% escalation).

### 3.5 Project Network Diagram e Gantt
- **CPM completo su AON**: 20 attività (A–T) con ES/EF/LS/LF e float da forward/backward pass. **Critical path A→B→D→G→J→M→P→R→S→T = 141 giorni lavorativi**, esattamente i giorni lavorativi 15/10→08/05 (festività italiane escluse) → **margine di 5 gg lavorativi** sul lancio del 15/05.
- **Scelta di ricalibrazione dichiarata** (v2.0.0): durate in giorni lavorativi netti, dopo che il percorso critico nominale (170 gg) non stava nei 146 disponibili — lo storico revisioni documenta il problema e la soluzione.
- **Fast tracking esplicito**: P→R **Start-to-Start + lag 31 gg** (il Testing E2E parte sui moduli congelati mentre il Frontend Tavolo rifinisce). Costo dichiarato ("la compressione non è mai gratis"): rischio di rework, mitigato sequenziando i test e con l'automazione Cypress. Il **crashing** compare come leva alternativa nella sensitivity (scenario 1: +1 dev part-time, ~€2.000).
- **Float come strumento decisionale**: ramo Game Engine 22 gg, ramo Chat/Social 37 gg; sensitivity a 3 scenari (P+10 → comprimere UAT o crashing; L+5 e N+10 → assorbiti dal float).
- **7 milestone, ciascuna con reviewer dedicato** (M2 Marchetti, M3 Giuliani, M6 i 10 tester UAT...): il controllo è progettato insieme al piano.

---

## 5. Scelte di Launching (Allegati 4.1–4.2)

### 4.1 Kick-Off Meeting
- **1 ora sola, perché i materiali sono pre-condivisi 3 giorni prima** (POS, WBS, Gantt, Cash Flow, bozze RASCI/regole): il meeting decide, non presenta. 5 decisioni formali (timeline, budget "senza incrementi", scope MVP con esclusioni esplicite, RASCI/regole, calendario 15 sprint), 7 action item con owner e scadenza su Notion.

### 4.2 RASCI Matrix
- **Regola cardine: un solo Accountable per attività** ("se ci sono troppi Accountable, nessuno è responsabile"). Otto matrici (una per sottosistema + QA + PM).
- **Deroghe motivate**, non incidenti: Elena **A/R sul Game Engine** (è la specialista; team di 5; bilanciata da supporto di Sara, code review e validazione esterna delle regole); **A a Marco** sulle attività di natura gestionale (cerimonie, disaster recovery plan, badge system = decisione di prodotto); **A a Giovanni** su business e milestone; sulla **UAT i ruoli si ribaltano** (A = sponsor, R = Giuliani per le sessioni). L'assegnazione dichiara di rispettare i carichi del Gantt (nessuno R di due sottosistemi negli stessi periodi).

### Regole operative
- **Problem solving in 5 passi** con root cause analysis (**5 Whys**, dai principi Lean) e verifica di efficacia a valle.
- **Decision making consultivo su 3 livelli** (operativo → decide il Responsible; tattico → Tech Lead + PM sentito il team; strategico → Sponsor su Project Impact Statement). Regola d'oro: "decidere al livello più basso possibile" — rapidità e decisioni prese da chi ha le informazioni.
- **Conflict resolution progressiva in 3 fasi** (confronto diretto → mediazione facilitata → decisione esecutiva) per 3 tipologie (tecnici → Elena, poi *disagree and commit*; priorità → Marco con MoSCoW e critical path; interpersonali → Marco facilitatore). Nel progetto nessun conflitto ha superato la fase 2.
- **Brainstorming** in due fasi (divergent: nessuna critica, "Yes, and..."; convergent: affinity mapping + dot voting con owner e deadline).
- **5 cerimonie**: Daily Standup 9:00–9:15 (non è la sede del problem solving), Sprint Planning, Sprint Review (si mostra solo l'increment "Done"; lo sponsor accetta o attiva il CR process), Retrospective (Start/Stop/Continue, "Vegas rule", 2 action item prioritari), Project Status Meeting settimanale col sponsor.
- **Comunicazione asincrona-first** (Slack/email; meeting solo se servono), **Notion single source of truth**, SLA di risposta per priorità. Email per le comunicazioni formali.
- **Change management in 5 passi** (submission → impact analysis con **Project Impact Statement** → decisione sponsor → implementazione → tracking nel Change Log). Doppio regime: i sottosistemi Agile accolgono il cambiamento nel processo, i tradizionali lo valutano caso per caso.
- Il documento è un **living document**: review ogni 2 sprint, versioning, approvazione consensuale + firma sponsor.

---

## 6. Scelte di Monitoring & Control (Cap. 5)

- **Monitoraggio su 3 livelli**: quotidiano (Daily per i sottosistemi Agile + board Notion), settimanale (Project Status Meeting di 1h con lo sponsor, venerdì), per sprint (Review + Retrospective). Più: Issue Log, Risk Log dinamico (probabilità/impatto rivalutati, stati Aperto/In Mitigation/Mitigato/Materializzato).
- **Stoplight Report a 5 aree** (Scope, Schedule, Budget, Quality, Risks), pubblicato ogni venerdì: verde = in linea, giallo = scostamento sotto controllo, rosso = intervento necessario.
- **EVM mensile** con una scelta metodologicamente forte: **l'EV matura solo sulle feature accettate dallo sponsor in Sprint Review** (Done secondo DoD) — lega l'Earned Value all'accettazione, non all'autodichiarazione. PV = outflow cumulato del Cash Flow. Chiusura: **CPI = SPI = 1,00**, €22.750 su €25.000.
- **Quality gates vincolanti per il Done**: coverage ≥85%, zero bug critici, code review (di Elena sulle parti critiche), latenza <500ms verificata con load test su 100 partite/400 giocatori. Report qualità con bug burn down e soglia di technical debt (max 10%).
- **Strategia d'intervento a scala graduata** (ricalca la Problem Escalation del corso): (1) lo slack assorbe? (2) strategie PM-based: dipendenze, parallelizzazione, crashing; (3) strategie client-based: Project Impact Statement, rilasci multipli, rinegoziazione.
- **I due episodi-chiave** (da raccontare all'orale):
  1. **Ritardo di gennaio**: attività M (Frontend Dashboard/Stanza, sul critical path) a −3 giorni → visibile in Stoplight (Schedule giallo), Gantt tracking (60% vs 80%) ed EVM (SV = −€900, CV = −€300, SPI 0,94) → recovery plan con **pair programming Luca+Sara** → recuperato entro febbraio senza toccare le milestone.
  2. **Rischio WebSocket**: spike + PoC in Sprint 2 (latenza 180ms) → rating da 16 a 8 → chiuso "Mitigato" dopo il load test dello Sprint 6. Il rischio più critico del progetto muore per riduzione progressiva dell'incertezza — è l'approccio adattivo che funziona.

---

## 7. Scelte di Closing (Cap. 6)

- **Accettazione formale il 10/05/2026**: demo completa e **partita giocata personalmente dallo sponsor** — l'accettazione è esperienziale, non solo documentale; firma senza richieste di modifica.
- **Deploy in produzione a carico della community** (dichiarato fin dall'inizio): PlayHeritage consegna Docker image + istruzioni di Andrea, con supporto remoto. Delimita il perimetro contrattuale del progetto.
- **Final Project Report (12/05)** in 9 sezioni; **audit post-implementazione (13/05) condotto con lo sponsor** verificando ogni criterio delle CoS — la tracciabilità numerica del POS paga qui: 7 mesi rispettati, €22.750, latenza 185ms, 80% utenti autonomi, beta tester 4,5/5 (target 4,2).
- **5 lessons learned**, ognuna agganciata a uno strumento delle fasi precedenti: (1) prototipare le UI complesse già in fase di stima (le animazioni da 8 SP erano sottostimate); (2) coinvolgere i domain expert *durante* lo sviluppo, non solo nello Scoping (caso Maraffa Should→Must); (3) anticipare il cross-browser testing agli Sprint 3–4 (Safari costò 2 giorni allo Sprint 12); (4) meccanismi asincroni strutturati (Slackbot per il daily dallo Sprint 7); (5) refactoring continuo al 10–15% per sprint invece dello sprint di cleanup (Sprint 10 povero di valore visibile per lo sponsor).
- **Surplus €2.250 (9%)** destinato al supporto post-lancio; **celebrazione a budget (€100)** — persino la voce "celebrare" del Closing Process Group è pianificata; sviluppi futuri stimati (app nativa €18–20k, tornei €8–10k, IA €12–15k) come pianificazione incrementale guidata dalle metriche post-lancio.

---

## 8. Rilievi emersi dall'audit incrociato del 2026-08-09 (registro storico + stato)

> Incoerenze trovate rileggendo integralmente tutti gli allegati. **Stato: le voci 1–8, 10–11 e i minori della voce 15 sono stati corretti negli allegati il 2026-08-09** (PDF rigenerati); restano *da sapere* come difendibili a voce le voci 9, 12, 13 e 14 (risposte pronte in `FAQ.md`, sezione G). In coda alla sezione: l'esito del secondo giro di audit a 5 lenti.

1. **US-3.1 (Allegato 2.9): "Determinazione casuale primo giocatore"** — contraddice RBS 1.1.2 e le regole ufficiali (inizia e sceglie briscola chi ha il **4 di denari**). Errore di fedeltà alle regole, cioè sull'obiettivo n. 1 del POS. **Da correggere.**
2. **US-3.6 (Allegato 2.9): Maraffa descritta come "3 carte dello stesso seme"** — la Maraffa/Cricca è **Asso+2+3 del seme di briscola** (RBS 1.1.5 è corretta). Anche i criteri di accettazione validerebbero la regola sbagliata. **Da correggere.**
3. US-2.5 cita la dipendenza "US-3.1 (Sistema amicizie)": il sistema amicizie è US-5.1. Refuso di cross-reference.
4. **POS, assunzione "Team dedicato full-time per 7 mesi"** — in conflitto con part-time ~50% FTE dichiarato in Risk 6.1, SWOT W2 e Allegato 2.11 (e con l'ostacolo "impegni accademici" nello stesso POS). Correggere in "team dedicato per l'intera durata (impegno ~50% FTE)" o difendere come "dedicato per tutti i 7 mesi".
5. **Decision point WebSocket in tre versioni**: giorno 30 (Risk 2.1), "4 settimane" (SWOT W1), **giorno 15 go/no-go + giorno 30 escalation al committente** (2.10). Lettura difendibile: il 2.10 è il raffinamento operativo — giorno 15 attiva il consulente, giorno 30 è l'escalation finale; Risk/SWOT citano solo quest'ultima.
6. **Allegato 3.1 firmato "Revisionato da: Luca Bianchi (Tech Lead)"** — persona inesistente (ibrido Luca Moretti/Sara Bianchi); il Tech Lead è Elena Rossi ovunque. Refuso di cast, facile da correggere.
7. **MoSCoW: percentuali nei titoli di sezione non allineate ai giorni** (Real-Time "~85%" ma è 93,3%; Frontend "~65%" ma 73,7%; Social "~40%" ma 16,7% Must). Residui pre-ricalcolo v1.1.0.
8. **Password recovery con tre priorità diverse**: Should nel MoSCoW, P3 backend (Sprint 9), P1 frontend (Sprint 6) — e la UI arriverebbe 3 sprint prima dell'API.
9. **Picchi di carico Backlog**: Sprint 6 = 47 SP e Sprint 10 = 42 SP di solo Backlog, sopra la capacity 40 team-wide (difesa: la media pianificata resta ~37; i picchi si compensano con gli sprint leggeri adiacenti e il carryover è fisiologico — ma la media nasconde i picchi).
10. **Cap. 5.11, "scostamento favorevole di €300"**: confronta AC (€17.500) con PV (€17.800) — in EVM non è un risparmio: a febbraio EV = €17.300 < AC, quindi CV = −€200 (leggermente sfavorevole). Stessa semantica scivolosa nello Stoplight di gennaio ("costi 13.500 vs pianificati 14.100" sotto la voce Budget). **Risposta corretta da dare se contestata: distinguere sempre AC-vs-PV (spesa vs piano) da CV = EV−AC (efficienza reale).**
11. **Saldo di cassa a gennaio**: lo Stoplight dice €4.650 (= incassi 18.750 − PV 14.100), ma con AC = 13.500 il saldo effettivo è €5.250. Numero calcolato sul pianificato anziché sull'effettivo.
12. **Surplus €2.250 con doppio uso**: nel 6.3 finanzia il supporto post-lancio, nel 6.7 "copre i costi operativi" dello spin-off. In un contratto a corpo il surplus è margine del fornitore: scegliere una narrazione (la più pulita: margine PlayHeritage, *impiegato* per garantire il supporto post-lancio promesso).
13. **Riclassificazione Maraffa senza Change Request formale esplicita**: il 4.2 riserva le decisioni di scope allo sponsor via PIS, ma il 6.5 dice "Marco ha riclassificato". Risposta pronta: la modifica fu discussa e approvata con lo sponsor nella cornice del processo (compensata riducendo Could Have), la nota di revisione nella MoSCoW ne è la traccia; formalmente sarebbe stato meglio un CR numerato.
14. **WCAG 2.1 AA è Should nella RBS ma criterio di successo nel POS/CoS** — se è criterio di successo dovrebbe essere Must. Risposta: il *core* dell'accessibilità è dentro i Must del frontend (contrasti, dimensioni target), l'etichetta Should della RBS riguarda la certificazione formale completa; a consuntivo è stata comunque verificata.
15. Minori: residuo "Jira" nella tracciabilità della RBS (ovunque è Notion); nel BMC i numeri della ripartizione non quadrano al centesimo (Marketing 1.250 vs somma voci 1.300; contingenza 2.500 vs 2.000 del consulente); etichetta "Apr 2026 (UAT)" nella tabella EVM vs UAT raccontata 1–10 maggio (stessa questione UAT già nota in PREPARAZIONE-ORALE §7.1); "velocity media finale 38,3" è in realtà la media Sprint 1–7 escluso il 5; primo Status Meeting datato sabato 18/10; sotto-task di F sommano 18 gg su 23.

**Secondo giro di audit (2026-08-09, 5 squadre: date/calendario, denaro, cast/riferimenti, regole di gioco, metriche) — esito.** Trovati e **corretti**: la griglia sprint del Backlog che correva da martedì a sabato (riallineata alla griglia lun–ven del Gantt: S1 28 Ott–7 Nov … S5 22 Dic–2 Gen … S11 16–31 Mar; etichette del CSV riallineate); l'accettazione formale datata domenica 10/05 → **lunedì 11/05** (Cap. 6 + relazione); il punteggio impossibile "41-38" in US-3.5 → "41-36" (79 non è esprimibile come 11n+3m); il totale punti per smazzata uniformato (10⅔ + 1 = 11⅔ grezzi → 11 interi dopo arrotondamento, in RBS e RASCI); il lessico presa/smazzata dove il troncamento morde; il criterio busso/striscio/volo aggiunto a US-3.2; il break-even ottimistico ~50 → **~84 mesi** (al netto dei costi operativi); PoC raccontato in due stadi coerenti (spike Sprint 0 → PoC completo Sprint 2); milestone del network rinumerate M2/M3/M4/M6 (erano M1–M4 in conflitto con la tabella M1–M7, anche nello script HTML); ritardo Sprint 7 attribuito a M anche in §5.8; codici rischio 2.1/6.2 al posto degli inesistenti R1/R4; tornei = Won't (non Could) nel Closing; tutorial "Scopri le regole" non più spacciato per extra (era pianificato allo Sprint 6); PWA = Won't ovunque; SP dei task padre del CSV = somma dei figli (9 righe); notifiche in-app P1/Must e sidebar amici P2 nel Backlog/CSV; sensitivity di N/Q precisata (i task Must di Q non sono de-scopabili); REQ-SOC-6.1 riqualificato come quota UI delle amicizie (niente doppio conteggio); "12 allegati" → 11; chat 1-a-1 fantasma → chat globale lobby; PaaS/DigitalOcean/Confluence → stack canonico; coverage riconciliata (80% gate di merge, 85% target di progetto); riga chat in-game aggiunta alla RASCI; reconnection "30s" riformulata (heartbeat 30s, sospensione 5 min); date nel weekend spostate a giorni feriali (approvazioni 2.4/2.9, kick-off materiali venerdì 10/10, primo Status Meeting venerdì 17/10, Sprint 0 Review venerdì 24/10, review 19/12); action item del kick-off "approvazione Scoping/Planning" riqualificato in approvazione del verbale; nota di superamento degli accordi preliminari nel 2.1; W1/W4/W3 della SWOT allineate; versioni dei companion HTML allineate ai .md.
**Restano difendibili senza correzione** (risposte in FAQ §G): overlap FS minori non annotati nel CSV (H.7, I.7, J.5, K.5-6, Q.4 — micro-parallelismi intra-attività); 3ª tranche di domenica 15/02 (giorno fisso contrattuale); doppio uso narrativo del surplus (6.3 vs 6.7: stessa cassa); US-2.5 "candidata al rinvio" pur essendo Should (slittamento accettato formalmente dallo sponsor); effort Game Engine 50 gg (MoSCoW) vs catena C-F-I-L-O di 73 gg (il testing è QA trasversale).

**Punti di forza verificati con ricalcolo** (spendibili all'orale): i 160 task della WBS sono esatti; tutte le somme di MoSCoW (302 gg), Backlog (310 SP) e Cash Flow tornano; il CPM è corretto incluso il legame SS+31 (verificato anche dallo script di generazione dell'HTML); i 141 giorni lavorativi al 08/05/2026 sono esatti sul calendario reale (148 feriali − 7 festività) e il margine di 5 giorni è confermato; il CSV del Gantt è pulito rispetto a weekend e festività per tutte le 129 righe; la tabella EVM mensile è aritmeticamente coerente (tutti i CV/SV/CPI/SPI tornano); le matrici RASCI md e HTML coincidono cella per cella.

---

**Ultimo aggiornamento**: 2026-08-09 — creato a valle della rilettura integrale di relazione (Cap. 1–6) e di tutti gli allegati, con audit di coerenza incrociata.
