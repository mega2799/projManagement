# Scelte di Progetto — Registro ragionato delle decisioni (MaraffaOnline)

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Registro completo delle **considerazioni fatte e delle scelte di progetto** che hanno portato all'elaborato attuale, in versione **didattica**: prima di raccontare *come* abbiamo usato uno strumento, un riquadro di ripasso spiega *che cos'è*, con la terminologia del corso (dispense del prof. Boschetti, basate in gran parte sull'approccio di Robert Wysocki). Leggendolo dall'inizio alla fine si ripassa la teoria E si impara l'elaborato.
>
> **Convenzione**: i riquadri `> Ripasso —` contengono la teoria generale; il testo normale racconta il progetto. Documenti gemelli: `PREPARAZIONE-ORALE.md` (numeri a memoria e risposte pronte) e `FAQ.md` (domande previste all'orale con risposte).

---

## 1. Impostazione generale dell'elaborato

### 1.1 Il progetto e il contesto narrativo

> **Ripasso — Che cos'è un "progetto"?** Per il PMBOK (la guida del Project Management Institute) un progetto è un'iniziativa **temporanea** (ha inizio e fine definiti) intrapresa per creare un risultato **unico**. Per Wysocki (definizione "business value") è una sequenza finita di attività dipendenti tra loro il cui completamento fornisce il **business value atteso** — dove il business value è il valore *percepito dal destinatario*, non dal fornitore. Si contrappone all'attività operativa, che è continuativa e ripetitiva.

- **Scelta**: piattaforma web multiplayer per la Maraffa (MaraffaOnline), sviluppata da **PlayHeritage Labs** (spin-off dell'Università di Bologna a Cesena, nato nel 2023, specializzato in *cultural heritage gaming* — la digitalizzazione di giochi tradizionali) su commissione di **Maraffa Forever**, community di ~150 ex studenti romagnoli che ha raccolto €25.000 con un crowdfunding interno.
- **Motivazione**: (a) differenziazione totale dalla relazione di riferimento (Exploding Kittens: altro gioco, altra azienda, altro committente, altro problema — anti-plagio per costruzione); (b) la narrativa *spin-off + community* rende **internamente coerente ogni numero**: un budget piccolo (€25.000) è credibile solo se il team è part-time e il progetto ha valore strategico da "pilota"; l'esperta di dominio e i 20 beta tester escono naturalmente dalla community; il non-profit giustifica un break-even negativo senza doversi inventare ricavi.
- **Il problema è sociale e geografico**, non tecnologico: le app esistenti sono obsolete o solo single-player; la dimensione conviviale del gioco si è persa con la dispersione geografica del gruppo. Questo àncora il progetto alla definizione di business value di Wysocki: il valore è "poter rigiocare insieme a distanza", ed è la community stessa a definirlo.

### 1.2 Gestione, non implementazione

- **Scelta**: l'elaborato documenta la **gestione** del progetto, non il software (le linee guida del corso lo richiedono esplicitamente: "NON implementare il software"). Quindi: nessun codice, nessun mockup grafico prodotto davvero — i wireframe sono disegni ASCII con una nota metodologica che lo dichiara (Allegato 2.7), il Gantt è in forma tabellare + CSV + HTML generato da uno script.
- **Motivazione**: coerenza col mandato d'esame; l'attenzione va tutta su processi, motivazioni e coerenza incrociata dei numeri — che sono esattamente i criteri di valutazione delle linee guida (solidità delle argomentazioni, coerenza, originalità, uso di strumenti, conoscenza teorica).

### 1.3 I vincoli fondativi

> **Ripasso — Contratto "a corpo" vs "a consuntivo".** A corpo (*fixed price*, "chiavi in mano"): il prezzo è fisso, quindi il rischio delle stime sbagliate ricade sul **fornitore**; il committente ha certezza di spesa. A consuntivo (*time and materials*): si paga il tempo effettivamente lavorato, quindi il rischio passa al **committente**. Il corso suggerisce il consuntivo quando le stime sono molto incerte (approcci iterativi).
>
> **Ripasso — FTE.** *Full-Time Equivalent*: unità di misura del personale. 1 FTE = una persona a tempo pieno; una persona al 50% = 0,5 FTE. Serve a confrontare lo sforzo (giorni-uomo) con l'organico reale.

| Vincolo | Valore | Perché così |
|---|---|---|
| Durata | 7 mesi (15/10/2025 – 15/05/2026) | orizzonte credibile per un MVP con team piccolo; genera un vincolo temporale "vero" da gestire con CPM e fast tracking (vedi §4) |
| Budget | €25.000 fisso | viene dal crowdfunding: non è negoziabile → il rischio budget si *accetta* (non si può mitigare né trasferire) comprimendo i costi col part-time |
| Team | 5 persone part-time ~50% FTE (≈2,1 FTE medi) | risposta al vincolo economico; il progetto è un pilota, il valore per lo spin-off è strategico (portfolio, pubblicazioni, tesi di dottorato del PM) |
| Contratto | a corpo, 3 tranche 50/25/25 legate a milestone | il budget del committente è fisso → fixed-price; il 50% alla firma garantisce la liquidità per il setup; le tranche successive sono legate a milestone misurabili (Backend Core il 15/12, core di gioco il 15/02) |

### 1.4 Convenzioni documentali (scelte di forma, ma difendibili)

- **`.md` testuale = registro completo; `.html` companion = versione visiva a colori** per i contenuti a griglia (matrici di rischio, canvas, WBS ad albero, board MoSCoW, Gantt, RASCI). Motivo tecnico: il Markdown puro non supporta celle unite né colori affidabili nelle pipeline di stampa PDF; un HTML standalone con CSS sì.
- **Storico revisioni in ogni allegato**: le correzioni di coerenza sono documentate, non nascoste (es. la ricalibrazione del critical path da 170 a 141 giorni; la riclassificazione della Maraffa). All'orale è un punto di forza: mostra controllo di configurazione, cioè la capacità di tracciare *chi ha cambiato cosa e quando*.
- **Onestà documentale**: rimossi dai verbali i dialoghi ricostruiti e i punteggi inventati; le immagini non prodotte sono dichiarate tali; Notion è la *single source of truth* (l'unico posto dove un'informazione è "quella vera") del progetto narrato.

---

## 2. La scelta regina: approccio ibrido per sottosistema (Allegato 2.10)

È la decisione che caratterizza l'intero elaborato e da cui discendono quasi tutte le altre.

> **Ripasso — PMLC e il quadrante di Wysocki.** PMLC = *Project Management Life Cycle*, il ciclo di vita con cui si gestisce un progetto. Wysocki lo sceglie in base a due domande: **il goal è chiaro? la soluzione è chiara?** Ne esce una matrice 2×2:
> - Goal chiaro + soluzione chiara → **TPM** (*Traditional PM*): modelli **Linear** (tutte le fasi una volta sola — il classico **Waterfall**, "a cascata": requisiti → design → sviluppo → test → rilascio, senza tornare indietro) e **Incremental** (come Linear, ma il deliverable è consegnato a incrementi: "business value presto e spesso").
> - Goal chiaro + soluzione NON chiara → **APM** (*Agile PM*): modelli **Iterative** (si raffina la soluzione a ogni iterazione, con feedback) e **Adaptive** (l'incertezza è tale che il piano si adatta di continuo — es. **Scrum**).
> - Goal e soluzione entrambi non chiari → **xPM/Extreme** (ricerca ed esplorazione); soluzione chiara ma goal no → **MPx** ("Emertxe", una tecnologia in cerca di impiego).
>
> Regola del corso: all'aumentare dell'incertezza sulla soluzione aumentano le iterazioni, la pianificazione diventa *just-in-time*, il risk management pesa di più e serve più coinvolgimento del cliente.
>
> **Mini-glossario dei termini agili usati sotto**: **sprint** = iterazione a durata fissa (da noi 2 settimane) con pianificazione, sviluppo, demo e retrospettiva; **Scrum** = il framework agile con Product Owner, Scrum Master e team; **Kanban** = gestione a flusso continuo (niente sprint: i task scorrono su una board con limiti di lavoro in parallelo); **spike** = esperimento tecnico *time-boxed* (a tempo massimo prefissato) per ridurre un'incertezza prima di impegnarsi; **YAGNI** = "You Aren't Gonna Need It" (da eXtreme Programming): non costruire oggi ciò che non serve ancora.

- **Scelta**: il prodotto è scomposto in **7 sottosistemi *loosely coupled*** (debolmente accoppiati: dipendenze reciproche minime) e a ciascuno è applicato il modello PMLC più adatto, scelto valutando **incertezza dei requisiti e incertezza della soluzione** (il quadrante di Wysocki), più complessità tecnica, dipendenze e bisogno di feedback.

| Sottosistema | Modello | Motivazione primaria |
|---|---|---|
| Game Engine (le regole del gioco) | **Waterfall (Linear, TPM)** | regole fisse, documentate e validate dall'esperta Francesca Giuliani *prima* dello sviluppo; i test si possono scrivere a monte partendo da partite a risultato noto; il feedback continuo degli utenti non serve (le regole le conoscono già) |
| Backend Server (API, dati) | **Agile Iterativo (APM)** | obiettivi chiari, ma le API si raffinano col feedback del frontend che le consuma; sprint di 2 settimane con demo allo sponsor |
| Frontend Web (interfaccia) | **Agile Iterativo (APM)** | co-design con la community, demo bi-settimanali, user testing continuo |
| Real-Time Communication (sincronizzazione live dei 4 giocatori via WebSocket, un canale di comunicazione bidirezionale e persistente tra browser e server) | **Agile Adattivo (APM)** | incertezza massima: nessuno nel team ha esperienza WebSocket in produzione; si procede per spike, decision point go/no-go, flusso Kanban e pair programming |
| Social & Community (amicizie, chat, profili) | **Incrementale (TPM)** | feature indipendenti tra loro, prioritizzate con MoSCoW; se il tempo stringe i Must restano completi, niente feature "a metà" |
| Infrastructure & DevOps (server, deploy, monitoraggio) | **Incrementale (TPM)** | crescita per strati (hosting → CI/CD → monitoring), anti over-engineering: principio YAGNI |
| Mobile Application | **Won't Have** (Incrementale post-MVP) | l'app nativa iOS+Android costerebbe ≈ +120 giorni (+40% di effort): incompatibile con budget e 7 mesi; supplisce il sito responsive (87,5% di successo nello user testing) |

- **Alternative scartate**: una metodologia monolitica unica ("overhead inutile in alcuni casi e rigidità dannosa in altri" — es. fare Sprint Planning sul Game Engine non avrebbe senso); il modello **Extreme**, mai applicabile perché nessun sottosistema ha *sia* goal *sia* soluzione ignoti.
- **Il costo dichiarato dell'ibrido è la sincronizzazione**: sottosistemi che internamente seguono ritmi diversi vanno tenuti allineati. Soluzione: una **cadenza comune sovrapposta ai metodi** — scansione bi-settimanale per tutti (anche chi non lavora a sprint), demo allo sponsor il venerdì di fine sprint, milestone di integrazione mensili, e le settimane 4/8/12 dedicate solo a integrazione e bug fixing, senza nuove feature.
- **Benefici argomentati**: il rischio è gestito componente per componente; nessun overhead superfluo; il modello è riusabile su futuri giochi tradizionali (coerente con la mission dello spin-off).

---

## 3. Scelte di Scoping (Allegati 2.1–2.11)

> **Ripasso — Che cos'è lo Scoping.** È il primo dei 5 *process group* di Wysocki (Scoping → Planning → Launching → Monitoring & Controlling → Closing). Serve a definire il **perimetro**: cosa il progetto farà e — altrettanto importante — cosa NON farà. I suoi deliverable canonici: Conditions of Satisfaction, documento dei requisiti (RBS), scelta del modello PMLC, POS.

### 2.1 Project Scoping Meeting

> **Ripasso.** Il *Project Scoping Meeting* di Wysocki riunisce committente, PM e core team per documentare i requisiti e produrre il POS. Un buon verbale contiene decisioni numerate e *action item* (compiti assegnati) con owner e scadenza.

- Meeting del 15/09/2025 con **tutti** gli attori (sponsor Giovanni Marchetti, esperta di dominio Francesca Giuliani, team completo), in modalità ibrida. Decisioni chiave: approccio **web-first** (l'app nativa è rinviata), contratto a milestone, 20 beta tester dalla community, regole del gioco documentate dall'esperta. Il verbale ha decisioni numerate, action item, owner e scadenze.

### 2.2 Conditions of Satisfaction

> **Ripasso.** Le **CoS** sono le condizioni negoziate tra chi chiede (requestor) e chi fornisce (provider) che guidano requisiti e decisioni per tutto il ciclo di vita. Il ciclo di negoziazione del corso è: **Request → Clarify Request → Response → Agree on Response**. Non coincidono con gli obiettivi: aggiungono vincoli su date, budget, qualità, UX. Differenza dagli *acceptance criteria*: le CoS dicono **cosa** deve essere il risultato; gli acceptance criteria dicono **come verificare** che una singola funzionalità sia accettabile.

- **22 condizioni in 5 tipologie** (temporale, economica, tecnica, qualitativa, gestione del lavoro), negoziate con lo schema richiesta/risposta. Soglie tutte quantitative e verificabili: lancio 15/05/2026; €25.000; 100 partite simultanee (400 giocatori); latenza ≤500ms (il ritardo tra l'azione di un giocatore e l'aggiornamento per gli altri); API <200ms al 95° percentile (cioè il 95% delle risposte deve stare sotto quella soglia); uptime 99%; soddisfazione ≥4,2/5; 80% degli utenti completa la prima partita senza aiuto; accessibilità WCAG 2.1 AA (lo standard internazionale di accessibilità web, livello intermedio).
- **Scelta**: i criteri temporali sono tenuti ad alto livello, senza calendario per sottosistema — la scomposizione appartiene al Planning, non allo Scoping (separazione delle fasi).

### 2.3 Project Overview Statement

> **Ripasso.** Il **POS** è la descrizione sintetica del progetto per il *senior management* — idealmente una pagina — con **5 sezioni**: (1) Problema/Opportunità; (2) Goal (1-2 frasi che circoscrivono l'ambito); (3) Obiettivi (5-6 statement "necessari e sufficienti"); (4) Criteri di successo (quantitativi — il corso cita **IRACIS**: Increased Revenue, Avoided Cost, Improved Service); (5) Assunzioni, Rischi e Ostacoli. Il POS **non è un contratto**. Gli obiettivi devono essere **S.M.A.R.T.**: Specific, Measurable, Assignable, Realistic, Time-related (Doran).

- Struttura canonica in 5 sezioni, con una scelta distintiva: **tracciabilità numerica 1:1** tra i **6 obiettivi**, i criteri di successo e i rischi — ogni criterio e ogni gruppo di rischi porta il numero dell'obiettivo a cui si riferisce. Questo paga alla fine: l'audit di chiusura (Cap. 6) verifica obiettivo per obiettivo.
- Distinzione applicata tra le tre voci della sezione 5: **assunzione** = condizione data per vera su cui il piano si fonda (es. "pagamenti puntuali"); **rischio** = evento incerto con probabilità e impatto (es. inesperienza WebSocket); **ostacolo** = difficoltà nota e certa da superare (es. il budget per persona sotto mercato).

### 2.4 Risk Analysis

> **Ripasso.** Il ciclo di gestione dei rischi: **identificazione → assessment → mitigazione → monitoraggio**. L'assessment qualitativo usa la matrice **probabilità × impatto**: valore del rischio = P×I. Le **5 strategie di risposta** del corso: **Accept** (accettarlo consapevolmente), **Avoid** (eliminare la causa), **Mitigate** (agire *subito* per ridurre probabilità o impatto), **Contingency planning** (preparare un piano per *se e quando* si verifica), **Transfer** (spostarlo su altri: assicurazioni, outsourcing).

- **Matrice 4×4**: probabilità in 4 fasce (A = 0-25% … D = 76-100%) × impatto in 4 livelli (Trascurabile → Disastroso), valore = P×I da 1 a 16, con scala colori a **5 livelli** (abbiamo introdotto il "Rosso Critico" = 16 per isolare i 2 rischi top). **20 rischi**: 2 critici (16), 6 rossi (9–12), 7 arancioni, 5 gialli.
- **Strategie differenziate e motivate**:
  - **Inesperienza WebSocket (16) → Contingency**: non si può "mitigare subito" un'incognita di fattibilità; si riduce l'incertezza con uno **spike tecnico di 2 settimane** e si prepara il piano B — go/no-go al giorno 15 che attiva il consulente esterno Dr. Nardi (€2.000 già accantonati), escalation al committente al giorno 30.
  - **Budget insufficiente (16) → Accept**: il crowdfunding è quello che è — non mitigabile né trasferibile; accettato formalmente nel meeting di approvazione, compensato dal modello part-time e dal valore strategico del pilota.
  - **Scope creep (12) → Mitigate**: *scope creep* = crescita strisciante del perimetro per richieste continue; mitigato con il congelamento dei requisiti dopo il POS + un processo di Change Control rigoroso (vedi §5).
  - **Race conditions (12) → Mitigate**: *race condition* = errore che nasce quando due eventi concorrenti (es. due giocatori che agiscono insieme) arrivano in ordine imprevisto; mitigata con architettura **server-authoritative** (è sempre il server, non i client, a decidere lo stato vero della partita) + code review.

### 2.5 Business Model Canvas e 2.6 Analisi SWOT

> **Ripasso.** Il **BMC** (Osterwalder) descrive su una pagina come un'organizzazione *crea, distribuisce e cattura valore*, in **9 blocchi**: partner chiave, attività chiave, risorse chiave, proposta di valore, relazioni coi clienti, canali, segmenti di clientela, struttura dei costi, flussi di ricavo. La **SWOT** classifica i fattori **interni** (Strengths/Weaknesses, su cui hai controllo) ed **esterni** (Opportunities/Threats). La **matrice TOWS** è l'estensione operativa: incrocia i quadranti per generare strategie SO (usa le forze per cogliere le opportunità), WO, ST, WT.

- **BMC** per validare la sostenibilità: ripartizione del budget (70% sviluppo, 15% infrastruttura, 10% contingenza, 5% marketing/community); i ricavi futuri (manutenzione, licensing, freemium) dichiarati come *visione*, non promesse.
- **SWOT estesa a TOWS** con strategie incrociate esplicite (es. W1+T1 → contingenza consulente) e **4 azioni immediate** (pre-allerta del consulente, governance decisionale con lo sponsor, meeting GDPR con il legale, accordo di commitment del team) — un passo oltre la SWOT descrittiva, buon punto di originalità.
- Coerenza incrociata voluta: le debolezze/minacce della SWOT puntano esplicitamente ai rischi corrispondenti della matrice (W1 = rischio 2.1, W4 = 6.4, T2 = 6.2).

### 2.7 Prototyping

> **Ripasso — PoC vs prototipo vs MVP.** **PoC** (*Proof of Concept*) = esperimento che verifica la *fattibilità tecnica* ("si può fare?"); **prototipo** = mostra *aspetto e uso* per raccogliere correzioni prima di costruire ("è così che lo volevi?"); **MVP** (*Minimum Viable Product*) = la prima versione *funzionante* con le sole funzioni principali, che dà business value reale e feedback dal campo. Nel progetto: PoC = lo spike Socket.IO; prototipo = i mockup Figma; MVP = la release del 15 maggio.

- **Due versioni di mockup**: v1 commentata dalla community → v2 **approvata e vincolante** per il frontend (diventa il riferimento contrattuale del design). Processo di **co-design partecipativo**: workshop con 10 membri, wireframe, feedback, user testing della v2 con 8 membri usando il **Think Aloud Protocol** (l'utente esegue i compiti *pensando ad alta voce*, così emergono i punti di confusione) e la *task completion* (100%, 100%, 87,5%; soddisfazione 4,6/5).
- Decisione UX motivata dal testing: **click to play** (selezioni la carta con un clic) invece di *drag & drop* (trascinarla), perché più affidabile su mobile. Palette "calda" da osteria (rosso mattone, legno, verde bottiglia) per la fedeltà culturale.
- **Niente file grafici prodotti**: scelta dichiarata nel documento — l'elaborato gestisce il *processo* di design, non produce gli artefatti (coerente con §1.2).

### 2.8 RBS e 2.9 User Stories

> **Ripasso.** La **RBS** (*Requirements Breakdown Structure*) è la scomposizione gerarchica dei **requisiti** (Requirement → Function → Sub-function → Feature): dice *cosa* va consegnato ed è la base per scegliere il PMLC (più la RBS è completa e stabile, più ci si può permettere un approccio tradizionale). Le **user story** esprimono un requisito dal punto di vista dell'utente ("Come <ruolo> voglio <azione> così da <beneficio>") e devono rispettare **INVEST**: **I**ndependent (indipendenti tra loro), **N**egotiable (negoziabili), **V**aluable (portano valore), **E**stimable (stimabili), **S**mall (piccole), **T**estable (verificabili). Un'**epica** è una storia troppo grande, da spezzare.

- **RBS per sottosistema** con classificazione F/NF/C (funzionale / non funzionale / vincolo) e pre-etichette MoSCoW; requisiti con soglie concrete (token di sessione JWT valido 7 giorni, sospensione partita max 5 minuti in caso di disconnessione, ripristino del servizio entro 4 ore...). Fonte delle regole di gioco: la documentazione ufficiale della community, **validata formalmente dall'esperta** — è questo che rende stabili i requisiti del Game Engine e quindi giustifica il Waterfall (§2).
- **23 user story in 7 epiche**, ognuna con criteri di accettazione puntuali e approccio di test, più una tabella che verifica INVEST criterio per criterio. **Scelta di pulizia**: nel 2.9 non ci sono priorità, story point né sprint — quelli appartengono al Planning (Allegati 3.2 e 3.3). Separazione netta tra il *cosa* (Scoping) e il *quanto/quando* (Planning).

### 2.11 Approval Process

> **Ripasso.** Ogni fase di Wysocki si chiude con un **gate di approvazione**: il senior management/sponsor valuta i deliverable della fase e autorizza (o no) la successiva. Senza gate formale, lo scope resta ambiguo e contestabile.

- Meeting di approvazione dello Scoping il 02/10/2025, con **diritti di voto espliciti**: Marchetti è l'unico voto decisionale, tutti gli altri sono consultivi (governance anti-stallo decisa in SWOT). Esito: approvazione formale + 2 riserve (monitoraggio stretto del rischio WebSocket; sistema amicizie condizionato ai tempi) + pre-allerta del consulente. Autorizza il Planning.

---

## 4. Scelte di Planning (Allegati 3.1–3.5)

> **Ripasso — Perché si pianifica.** Wysocki: la pianificazione costa il 18-36% del tempo di progetto ma **riduce l'incertezza, aumenta la comprensione e migliora l'efficienza** (la "pain curve": il dolore evitato dopo vale più del tempo speso prima).

### 3.1 Work Breakdown Structure

> **Ripasso.** La **WBS** è la scomposizione gerarchica di **tutto il lavoro** necessario a soddisfare i requisiti (attenzione: la RBS scompone i *requisiti*, la WBS il *lavoro*). Regola cardine: la **100% rule** — la WBS deve coprire il 100% del lavoro, incluso il project management stesso; la somma dei figli deve equivalere al padre. Si può decomporre **per deliverable** (cosa si consegna) o per fasi (quando); il corso dà **6 test di completezza** per il singolo task: stato misurabile, confini definiti, deliverable associato, tempi/costi stimabili, durata accettabile, indipendenza. Il **WBS Dictionary** è il registro testuale che descrive ogni voce.

- **Decomposizione per deliverable** (non per fasi), 100% rule dichiarata, **4 livelli** (Sottosistema → Funzione → Attività → Task), **160 task** sui 6 sottosistemi attivi **+ una sezione trasversale** per PM, documentazione e QA — così anche il lavoro di gestione è dentro il 100%.
- La Mobile App (Won't Have) non genera task: la WBS copre lo scope della release; a decidere le priorità è il MoSCoW (nota di raccordo esplicita tra i due allegati).
- Il `.md` funge da WBS Dictionary; l'albero visuale sta nell'HTML companion. Rispetto ai 6 livelli canonici di Wysocki (Goal → Objective → Function → Sub-function → Activity → Task) ne usiamo 4: i primi due sono già assorbiti dalla struttura per sottosistemi della RBS.

### 3.2 MoSCoW

> **Ripasso.** **MoSCoW** (Dai Clegg) è una tecnica di prioritizzazione dei requisiti in 4 classi: **Must** (senza, il prodotto non è utilizzabile), **Should** (importanti ma sostituibili/rinviabili), **Could** (desiderabili, solo se avanza tempo), **Won't** (esplicitamente esclusi da questa release). Nasce dentro **DSDM** (*Dynamic Systems Development Method*, una delle prime metodologie agili), che raccomanda di distribuire lo sforzo ~**60/20/20**: i Could sono la "valvola di sfogo" che protegge la data di consegna — se sei in ritardo, tagli i Could senza toccare la promessa.

- **Definizione rigorosa di Must** (4 criteri: indispensabile all'uso / obbligo di legge / rischio di sicurezza / non negoziabile per il committente) — non un generico "importante", ma un test applicabile.
- **302 giorni-uomo** di effort totale: **Must 75,8% / Should 18,9% / Could 5,3%**, contro il target DSDM 60/20/20. **Scostamento dichiarato e motivato**: Game Engine e Real-Time sono il *core differentiator* — senza regole fedeli e partite fluide il prodotto non esiste; i Could compressi al 5,3% sono la scelta anti-scope-creep che protegge i 7 mesi. Won't espliciti e negoziati: app nativa, social login, IA, notifiche push, tornei.
- **Processo dinamico**: 3 revisioni datate (dopo il POS, dopo lo user testing, approvazione finale col committente) più una **riclassificazione in corso d'opera** — a novembre 2025 la Maraffa/Cricca passa da Should a Must su input dell'esperta, documentata con nota di revisione e raccontata nelle lessons learned.

### 3.3 Stime e Product Backlog

> **Ripasso — Le tecniche di stima consensuali.** Servono a stimare senza i *bias* individuali. **Delphi** (Project RAND, anni '50): ogni esperto dà la sua stima **in forma anonima** con motivazione; si condividono i risultati e si ripete per più round fino a convergenza — l'anonimato evita l'**ancoraggio** (il bias per cui la prima cifra sentita condiziona tutte le altre) e l'effetto autorità. **Planning Poker** (Scrum): il Product Owner presenta l'elemento, ognuno sceglie *in segreto* una carta della scala di **Fibonacci** (1, 2, 3, 5, 8, 13, 21 — cresce come l'incertezza), si scoprono insieme, si discutono le discrepanze e si ripete fino al consenso. Gli **story point** sono l'unità del Planning Poker: misurano la *complessità relativa*, non il tempo (sono adimensionali).
>
> **Ripasso — Effort vs Duration.** Lo **sforzo** (giorni-uomo, *effort*) misura il lavoro; la **durata** (giorni di calendario lavorativo) misura il tempo che passa. Non sono proporzionali: aggiungere persone non riduce la durata in modo lineare. Formula del corso: Labor = 0,75 × Duration (il 25% del tempo si perde in interruzioni). Corollario anti-illusione: *Effort ≠ Progress*.

- **Due tecniche di stima, una filosofia** (stima collettiva anti-bias): **Delphi** per il Game Engine — requisiti stabili, contesto tradizionale — e **Planning Poker** per i sottosistemi agili. Sapere il perché di ciascuna: Delphi evita l'ancoraggio su requisiti noti; il Poker aggiunge la discussione delle discrepanze, preziosa dove l'incertezza è alta.
- **Product Backlog**: la lista prioritizzata del lavoro dei sottosistemi agili. **Criterio di inclusione = natura del lavoro, non etichetta del sottosistema**: entra ciò che è esprimibile come user story rivolta all'utente e che scorre negli sprint (Backend, Real-Time, Frontend + le feature Social sotto il sottosistema che le implementa). Restano fuori il Game Engine (specifica congelata, validazione finale — è Waterfall) e l'Infrastructure (attività ricorrenti e on-demand, non user story): tracciati in WBS e Gantt. Motivo: il Backlog è uno strumento di Scrum; mescolarci lavoro con cicli di vita diversi ne comprometterebbe leggibilità e ruoli.
- **Capacità vs carico — la doppia lettura dichiarata** (il punto più insidioso dell'elaborato, da sapere bene):
  - **capacity 40 SP/sprint team-wide** = quanto il team *può* completare in uno sprint, includendo il lavoro di Game Engine e Infrastructure convertito in "punti equivalenti" (~131 SP; totale progetto ~441 SP);
  - **carico medio pianificato** = quanto è stato *effettivamente messo in piano*: ~37 SP/sprint team-wide (441 su Sprint 0–11) e ~28 SP/sprint di solo Backlog (310 SP su Sprint 1–11);
  - il margine tra 40 e 37 assorbe festività e variabilità delle stime. Due metriche, due usi: quella team-wide è il consuntivo consolidato per lo sponsor; quella di solo Backlog è il carico Scrum del team.
- **15 sprint (0–14)** allineati alle date del Gantt (griglia lunedì–venerdì); Sprint 5 natalizio (22 Dic – 2 Gen) pianificato a capacità ridotta (21/40 SP, carryover 19 = lavoro non finito che "trasloca" agli sprint successivi); Sprint 12–14 (UAT e lancio) non stimati in story point.
- **Definition of Done a 8 criteri** — la **DoD** è la checklist, fissata a inizio progetto e uguale per tutte le storie, che definisce quando un lavoro è *davvero* finito: codice committato, unit test con coverage >80% (il *coverage* è la percentuale di codice esercitata dai test), code review di un collega, integration test, documentazione aggiornata, deploy in staging, criteri di accettazione soddisfatti, approvazione del PO in Sprint Review.

### 3.4 Cash Flow Management

> **Ripasso.** Gestire il cash flow non significa solo chiudere in utile: significa che il **saldo cumulativo** (incassi meno uscite, mese per mese) non vada mai sotto zero — si può fallire *in utile* se la cassa finisce a metà strada. Strumenti: tabella **inflow/outflow** per periodo, saldo cumulativo, condizioni di incasso (anticipo, milestone, saldo). Due riserve distinte: la **contingency reserve** copre gli imprevisti *identificati* (rischi, change request); la **management reserve/surplus** è il margine che resta. Il **break-even** è il momento in cui i ricavi cumulati coprono i costi.

- **Ipotesi strutturale**: l'ultimo incasso arriva a metà progetto (15/02) → la coda (marzo–maggio) vive del saldo accumulato → l'outflow decresce nei mesi 5–7 (team ridotto su testing/UAT/lancio). Risultato: **saldo cumulativo sempre positivo, minimo €2.250 nell'ultimo mese**.
- **Contingency €4.664 (18,7%) distribuita nelle uscite mensili** come buffer operativo + **surplus finale €2.250 (9%)** destinato al supporto post-lancio: margine di sicurezza complessivo ~27,7%.
- **Break-even dichiaratamente negativo**: nello scenario base il freemium non copre nemmeno i costi operativi ("mai raggiunto"); in quello ottimistico servono ~84 mesi. Conclusione onesta: progetto **non-profit per la community**. Meglio ammetterlo che inventare ricavi — ed è un buon esempio d'esame di *analisi che porta a una conclusione negativa ma utile*.
- Controllo: report mensile al committente entro il 5 del mese, review settimanale, **soglie di variance con azioni graduate** (scostamento 5–10% → review delle spese; 10–15% → posticipo di Should/Could; >15% → escalation al committente).

### 3.5 Project Network Diagram e Gantt

> **Ripasso — CPM in 60 secondi.** Il **Project Network Diagram** rappresenta le attività e le loro **dipendenze** (formato *Activity-On-Node*: le attività sono nodi, le frecce sono precedenze). Su di esso si applica il **CPM** (*Critical Path Method*):
> 1. **Forward pass** (da sinistra): per ogni attività si calcolano **ES** (*Early Start*, il primo momento in cui può iniziare) ed **EF** (*Early Finish*).
> 2. **Backward pass** (da destra): si calcolano **LS/LF** (*Late Start/Late Finish*, l'ultimo momento in cui può iniziare/finire senza ritardare il progetto).
> 3. **Slack (o float)** = LS − ES: quanto un'attività può slittare senza danni. Le attività a **slack zero** formano il **critical path**, la catena che determina la durata del progetto: ogni loro ritardo si ripercuote per intero sulla fine. (Total float = ritardo senza impatto sul *progetto*; free float = senza impatto sul *task successivo*.)
>
> Le **dipendenze** possono essere: **FS** (Finish-to-Start, la classica: B inizia quando A finisce), **SS** (Start-to-Start: B inizia quando A *inizia*), FF, SF; il **lag** è un ritardo imposto sul legame (SS+31 = B inizia 31 giorni dopo l'inizio di A).
>
> **Ripasso — Comprimere la schedula.** Due tecniche: **fast tracking** = mettere in parallelo attività che erano in sequenza (non costa denaro, ma aumenta il rischio di *rework*, cioè di dover rifare lavoro se l'attività a monte cambia); **crashing** = aggiungere risorse alle attività critiche (costa denaro, e non scala linearmente). Monito del corso: "la compressione non è mai gratis". E: *Do not plan to use slack to bail out the project* — lo slack non va "speso" già in pianificazione.
>
> **Ripasso — Network vs Gantt.** Il network serve a *calcolare* (critical path, float, analisi what-if); il **Gantt** traduce tutto in **calendario** con barre e **milestone** (eventi a durata zero che segnano un traguardo) ed è lo strumento di monitoraggio e comunicazione. Prima si costruisce il network, poi se ne deriva il Gantt.

- **CPM completo**: 20 attività (A–T) con ES/EF/LS/LF e float calcolati con forward/backward pass. **Critical path: A→B→D→G→J→M→P→R→S→T = 141 giorni lavorativi**, esattamente i giorni lavorativi disponibili dal 15/10 all'08/05 (festività italiane escluse) → restano **5 giorni lavorativi di margine** prima del lancio del 15/05.
- **Scelta di ricalibrazione dichiarata**: le durate sono in giorni lavorativi netti; lo storico revisioni documenta che il percorso critico nominale della prima versione (170 giorni) non stava nei 146 disponibili, e come è stato ricalibrato — un errore intercettato e corretto *nel processo*, non nascosto.
- **Fast tracking esplicito**: il Testing End-to-End (R) è legato al Frontend Tavolo (P) con un vincolo **Start-to-Start + lag 31 giorni** — parte quando P ha completato 31 dei suoi 40 giorni, testando i moduli già congelati (login, dashboard, stanze) mentre P rifinisce le animazioni. Il costo è dichiarato: rischio di rework, mitigato sequenziando i test sui moduli stabili e con la suite automatizzata Cypress (rieseguibile a ogni modifica). Il **crashing** compare come leva alternativa nella sensitivity analysis: se P ritarda 10 giorni, +1 contractor esterno part-time ≈ €2.000 dal Contingency Buffer.
- **Float come strumento decisionale**: ramo Game Engine 22 giorni, ramo Chat/Social 37 giorni; analisi di sensibilità su 3 scenari (P+10 → comprimere la UAT o crashing; L+5 e N+10 → assorbiti dai float).
- **7 milestone, ciascuna con un reviewer dedicato** (M2 Backend Core → sponsor; M3 Game Engine → esperta; M6 UAT → i 10 tester...): il controllo è progettato insieme al piano, non aggiunto dopo.

---

## 5. Scelte di Launching (Allegati 4.1–4.2)

> **Ripasso.** Il **Launching** è il process group che avvia l'esecuzione: si forma il team, si fissano le **regole operative** (come si decide, come si gestiscono problemi e conflitti, come ci si riunisce), si definiscono ruoli e responsabilità e le procedure per i cambiamenti. Il **Kick-Off Meeting** è la cerimonia che annuncia l'approvazione del progetto e allinea tutti prima di partire.

### 4.1 Kick-Off Meeting

- **Un'ora sola, perché i materiali sono pre-condivisi il venerdì precedente** (POS, WBS, Gantt, Cash Flow, bozze di RASCI e regole): il meeting decide e allinea, non presenta. Ne escono 5 decisioni formali (timeline, budget "senza incrementi", scope MVP con esclusioni esplicite, RASCI/regole approvate, calendario dei 15 sprint) e 7 action item con owner e scadenza su Notion. Coerente con la regola "asynchronous-first" (vedi sotto).

### 4.2 RASCI Matrix

> **Ripasso.** La **RASCI** (variante della RACI) è la matrice di assegnazione delle responsabilità: per ogni attività, **R**esponsible = chi *esegue* (possono essere più d'uno), **A**ccountable = chi *approva e risponde* del risultato (**deve essere uno solo**: "se ci sono troppi Accountable, nessuno è responsabile"), **S**upport = chi aiuta su richiesta, **C**onsulted = chi va consultato (comunicazione a due vie), **I**nformed = chi va tenuto informato (a una via).

- Otto matrici (una per sottosistema + QA + PM), regola del singolo Accountable rispettata riga per riga.
- **Deroghe motivate, non incidenti**: Elena è **A/R sul Game Engine** (è la specialista; in un team di 5 la separazione totale sarebbe artificiosa; contrappesi: supporto di Sara, code review, validazione esterna delle regole); **A a Marco** sulle attività di natura gestionale (cerimonie, disaster recovery plan, priorità di prodotto); **A a Giovanni** su business e milestone; sulla **UAT i ruoli si ribaltano**: A = sponsor (è lui che accetta), R = l'esperta che conduce le sessioni. L'assegnazione dichiara di rispettare i carichi del Gantt: nessuno è Responsible di due sottosistemi negli stessi periodi.

### Regole operative

> **Ripasso — I tre stili decisionali del corso.** **Directive**: decide chi ha l'autorità, da solo (veloce, ma spreca le competenze del team); **Participative/Collaborative**: decide tutto il team insieme (coinvolge, ma è lento e può produrre compromessi mediocri — Wysocki avverte: "una decisione di consenso che accontenta tutti può comunque essere una cattiva decisione"); **Consultative**: decide chi ha l'autorità *dopo aver raccolto l'input del team* — il compromesso che teniamo noi.
>
> **Ripasso — Conflict resolution (Thomas-Kilmann).** Cinque stili lungo due assi (assertività × cooperazione): **Competing** (imporre), **Collaborating** (integrare le esigenze di tutti), **Compromising** (spartire), **Avoiding** (evitare), **Accommodating** (cedere). **"Disagree and commit"** = una volta deciso, anche chi era contrario si impegna a eseguire senza rimetterla in discussione.
>
> **Ripasso — 5 Whys.** Tecnica lean (Toyota) di *root cause analysis*: si chiede "perché?" ~5 volte risalendo dalla manifestazione del problema alla causa radice, per curare quella e non il sintomo.

- **Problem solving in 5 passi** con root cause analysis (5 Whys) e verifica di efficacia a valle: se il problema si ripresenta, si torna all'analisi.
- **Decision making consultivo su 3 livelli**: operativo (naming, librerie, bug fix → decide il Responsible del task), tattico (architettura, API, backlog → Tech Lead + PM, sentito il team, documentato), strategico (scope, budget, timeline → Sponsor, sulla base di un Project Impact Statement preparato dal PM). Regola d'oro: "decidere al livello più basso possibile" — velocità, decisioni prese da chi ha le informazioni, niente colli di bottiglia.
- **Conflict resolution progressiva in 3 fasi** (confronto diretto in privato → mediazione facilitata → decisione esecutiva) per 3 tipologie (tecnici → decide Elena su criteri oggettivi, poi disagree and commit; di priorità → decide Marco con MoSCoW e critical path; interpersonali → Marco facilitatore). Nel progetto nessun conflitto ha superato la fase 2.
- **Brainstorming strutturato in due fasi**: *divergent thinking* (produrre idee senza critiche: "Yes, and..." invece di "Yes, but...", conta la quantità) e *convergent thinking* (raggruppare con l'affinity mapping e selezionare col **dot voting** — ognuno ha N "puntini" da distribuire sulle idee preferite; ogni idea scelta riceve un owner e un next step).
- **Le 5 cerimonie**: **Daily Standup** 9:00–9:15 (in piedi, 3 domande: cosa ho fatto / cosa farò / cosa mi blocca — NON è la sede del problem solving, che va fatto dopo con i soli coinvolti); **Sprint Planning** (a inizio sprint: si selezionano le storie e si stimano); **Sprint Review** (a fine sprint: si mostra allo sponsor solo l'incremento "Done"; se chiede modifiche sostanziali si apre una Change Request); **Sprint Retrospective** (subito dopo, solo team: formato *Start/Stop/Continue* — cosa iniziare/smettere/continuare a fare — con la "Vegas rule": quel che emerge resta lì); **Project Status Meeting** settimanale con lo sponsor.
- **Comunicazione asynchronous-first**: prima i canali asincroni (Slack, email), i meeting solo quando servono; **Notion è la single source of truth** delle decisioni; **SLA di risposta** (*Service Level Agreement*: il tempo massimo di risposta concordato) commisurati alla priorità del messaggio. Email riservata alle comunicazioni formali.
- **Change management in 5 passi**: submission (modulo di Change Request) → **impact analysis** con **Project Impact Statement** (il documento, previsto dal corso, che analizza l'impatto del cambiamento su scope, tempi, costi, qualità e risorse e propone le opzioni: accettare, rinviare, rifiutare) → decisione dello sponsor → implementazione (aggiornando POS, WBS, Gantt, Backlog) → tracciamento nel Change Log. Doppio regime coerente con l'ibrido: i sottosistemi agili *accolgono* il cambiamento nel processo (si riprioritizza il backlog); quelli tradizionali lo valutano caso per caso.
- Il documento delle regole è un **living document**: review formale ogni 2 sprint, versionato, approvato dal team e firmato dallo sponsor.

---

## 6. Scelte di Monitoring & Control (Cap. 5)

> **Ripasso — Gli strumenti di controllo del corso.** Lo **Stoplight Report** dà a ogni area un semaforo: **verde** = "the project is progressing according to plan"; **giallo** = "c'è un problema, un Get Well plan è in atto, la situazione rientrerà"; **rosso** = "the project is failing, serve un intervento". L'**Issue Log** censisce ogni problema con owner, azione e stato, così nulla viene dimenticato. Il **Risk Log** fa lo stesso per i rischi, con probabilità e impatto *rivalutati* nel tempo (i rischi non sono statici). I 5 tipi di report del corso: current period, cumulative (mostrano i trend), exception (sintetici per il senior management), stoplight, variance.
>
> **Ripasso — EVM (Earned Value Management), le formule.** Tre grandezze alla data di controllo: **PV** (*Planned Value*: il valore del lavoro che *avresti dovuto* completare secondo il piano), **EV** (*Earned Value*: il valore del lavoro *effettivamente completato*, misurato col budget assegnato a quel lavoro), **AC** (*Actual Cost*: quanto hai *speso davvero*). Da cui:
> - **CV = EV − AC** (Cost Variance: negativa → stai spendendo più del valore che produci);
> - **SV = EV − PV** (Schedule Variance: negativa → sei in ritardo);
> - **CPI = EV / AC** e **SPI = EV / PV** (indici di efficienza: soglia 1; sotto 1 = oltre budget / in ritardo).
> Attenzione all'errore classico: confrontare AC con PV ("ho speso meno del previsto!") **non** misura l'efficienza — potresti aver speso poco solo perché hai fatto poco. L'efficienza si misura sempre passando dall'EV.

- **Monitoraggio su 3 livelli**: quotidiano (Daily Standup per i sottosistemi agili + board Notion aggiornata da ognuno), settimanale (Project Status Meeting di un'ora con lo sponsor, il venerdì), per sprint (Review + Retrospective). Più Issue Log e Risk Log su Notion.
- **Stoplight Report settimanale su 5 aree** (Scope, Schedule, Budget, Quality, Risks), ognuna con colore e nota che lo motiva.
- **EVM mensile** con una scelta metodologicamente forte: **l'EV matura solo sulle feature accettate dallo sponsor in Sprint Review** (Done secondo la DoD) — il valore "guadagnato" è certificato dal cliente, non autodichiarato dal team. PV = l'outflow cumulato del Cash Flow. Chiusura: **CPI = SPI = 1,00**, €22.750 spesi su €25.000.
- **Quality gate vincolanti per il "Done"**: coverage ≥85% (il gate di merge nella DoD è 80%, il target di progetto monitorato è 85%), zero bug critici aperti, code review (di Elena sulle parti critiche), latenza <500ms verificata con load test su 100 partite/400 giocatori. Nei report qualità: bug burn down (il grafico dei bug residui nel tempo) e soglia di **technical debt** — il "debito tecnico", cioè le scorciatoie di codice accumulate da ripagare poi — max 10% del tempo.
- **Strategia d'intervento a scala graduata** (ricalca la *Problem Escalation Strategy* del corso, che possiede una gerarchia fine di 7 passi): (1) c'è slack che assorbe? (2) leve del PM: riesaminare le dipendenze, parallelizzare, riallocare risorse, crashing; (3) leve del cliente: Project Impact Statement, rilasci multipli, estensione o riduzione dello scope. Nota bene: usare lo slack *a consuntivo* come primo assorbitore non contraddice il monito "do not plan to use slack" — quello vieta di *pianificare* contando sul float.
- **I due episodi-chiave da saper raccontare**:
  1. **Il ritardo di gennaio**: l'attività M (Frontend Dashboard e Creazione Stanza, sul critical path) accumula 3 giorni di ritardo. Il problema è visibile su **tre strumenti coerenti**: Stoplight (Schedule giallo), Gantt tracking (60% completato contro l'80% atteso), EVM (SV = −€900, CV = −€300, SPI = 0,94). Intervento: l'attività è critica, slack non ce n'è → leva PM: **recovery plan con pair programming** (Luca affiancato da Sara — riallocazione interna, non crashing a pagamento) → recupero completo entro febbraio, milestone invariate.
  2. **Il rischio WebSocket muore per gradi**: spike + PoC nello Sprint 2 misurano 180ms di latenza → il rating scende da 16 a 8 (la probabilità cala, dimostrata la padronanza) → il load test dello Sprint 6 (100 partite, 400 giocatori, <500ms) lo chiude come "Mitigato". È l'approccio adattivo che funziona: l'incertezza si riduce con esperimenti, non con le speranze.

---

## 7. Scelte di Closing (Cap. 6)

> **Ripasso — I 6 passi del Closing.** (1) Ottenere l'**accettazione formale** del deliverable dal committente; (2) assicurarsi che i deliverable siano **installati**; (3) che la **documentazione** sia completa; (4) far **firmare il Final Project Report**; (5) condurre il **post-implementation audit** (obiettivi raggiunti? vincoli rispettati? cliente soddisfatto? business value concretizzato? cosa si è imparato sulla metodologia?); (6) **celebrare** — le slide del corso vi dedicano una pagina intera. I 4 approcci di installazione: *phased* (a fasi), *by business unit*, *cut-over* (sostituzione secca), *parallel* (vecchio e nuovo insieme finché il nuovo non è verificato).

- **Accettazione formale lunedì 11/05/2026**: demo completa e **partita giocata personalmente dallo sponsor** — l'accettazione è esperienziale, non solo documentale; firma senza richieste di modifica.
- **Deploy in produzione a carico della community** (dichiarato fin dall'inizio del contratto): PlayHeritage consegna le immagini Docker (pacchetti software pronti da eseguire) + le istruzioni, con supporto remoto. Delimita con precisione il perimetro contrattuale del progetto.
- **Final Project Report (12/05)** in 9 sezioni; **audit post-implementazione (13/05) condotto insieme allo sponsor**, verificando ogni criterio delle CoS — qui paga la tracciabilità numerica del POS: 7 mesi rispettati, €22.750 su €25.000, latenza media 185ms, 80% di utenti autonomi alla prima partita, beta tester 4,5/5 contro il target 4,2.
- **5 lessons learned**, ognuna agganciata a uno strumento delle fasi precedenti (è questo che le rende difendibili): (1) prototipare le UI complesse già in fase di stima — le animazioni stimate 8 SP col Planning Poker erano sottostimate; (2) tenere gli esperti di dominio nel loop anche *durante* lo sviluppo, non solo nello Scoping — il caso Maraffa Should→Must; (3) anticipare il cross-browser testing ai primi sprint con interfaccia (5–6) — farlo solo allo Sprint 12 costò 2 giorni di fallback per Safari; (4) daily asincrono strutturato (uno Slackbot dallo Sprint 7) per i periodi di lavoro remoto; (5) refactoring continuo al 10–15% di ogni sprint invece di uno "sprint di pulizia" — lo Sprint 10 dedicato al debito tecnico ha mostrato poco valore visibile allo sponsor in Review.
- **Surplus €2.250 (9%)** destinato al supporto post-lancio; **celebrazione a budget (€100)**: persino la voce "celebrare" del Closing è pianificata. Sviluppi futuri stimati (app nativa €18–20k, tornei €8–10k, IA €12–15k) come pianificazione incrementale guidata dalle metriche post-lancio.

---

## 8. Rilievi emersi dall'audit incrociato del 2026-08-09 (registro storico + stato)

> Incoerenze trovate rileggendo integralmente tutti gli allegati. **Stato: le voci 1–8, 10–11 e i minori della voce 15 sono stati corretti negli allegati il 2026-08-09** (PDF e pacchetto di consegna rigenerati); restano *da sapere* come difendibili a voce le voci 9, 12, 13 e 14 (risposte pronte in `FAQ.md`, sezione G). In coda alla sezione: l'esito del secondo giro di audit a 5 lenti.

1. **US-3.1 (Allegato 2.9): "Determinazione casuale primo giocatore"** — contraddiceva RBS 1.1.2 e le regole ufficiali (inizia e sceglie la briscola chi ha il **4 di Denari**). Errore di fedeltà alle regole, cioè sull'obiettivo n. 1 del POS. **Corretto.**
2. **US-3.6 (Allegato 2.9): Maraffa descritta come "3 carte dello stesso seme"** — la Maraffa/Cricca è **Asso+2+3 del seme di briscola** (RBS 1.1.5 era corretta). **Corretto** (inclusi i criteri di accettazione e l'obbligo di giocare l'Asso per primo).
3. US-2.5 citava la dipendenza "US-3.1 (Sistema amicizie)": il sistema amicizie è US-5.1. **Corretto.**
4. **POS, assunzione "Team dedicato full-time per 7 mesi"** — in conflitto con il part-time ~50% FTE dichiarato ovunque. **Corretto**: ora recita "team dedicato al progetto per tutti i 7 mesi (impegno ~50% FTE, senza allocazioni su altri progetti)".
5. **Decision point WebSocket in tre versioni** (giorno 30 / 4 settimane / giorno 15). **Armonizzato** in tutti gli allegati sulla versione operativa del 2.10: giorno 15 = go/no-go dello spike che attiva il consulente; giorno 30 = escalation al committente.
6. **Allegato 3.1 firmato "Revisionato da: Luca Bianchi (Tech Lead)"** — persona inesistente (fusione di Luca Moretti e Sara Bianchi). **Corretto**: Elena Rossi.
7. **MoSCoW: percentuali nei titoli di sezione non allineate ai giorni**. **Corretto** (Backend ~70/~23/~6, Real-Time ~93/~7, Frontend ~74/~22/~4, Social ~17/~58/~25, Infrastructure ~73/~27).
8. **Password recovery con tre priorità diverse** (Should nel MoSCoW, P3 backend, P1 frontend). **Corretto**: P2 in entrambe le righe del Backlog, con nota sul form sviluppato su API mock.
9. **Picchi di carico Backlog**: Sprint 6 = 47 SP e Sprint 10 = 42 SP contro capacity 40 team-wide. *Difendibile*: la media pianificata resta ~37; i picchi si compensano con gli sprint leggeri adiacenti e il carryover è fisiologico — ma la media nasconde i picchi, e va ammesso.
10. **Cap. 5.11, "scostamento favorevole di €300"**: confrontava AC con PV — in EVM non è un risparmio (vedi il ripasso in §6). **Corretto**: ora riporta la CV vera (−€200 a febbraio, riassorbita fino a CV = 0 alla chiusura).
11. **Saldo di cassa di gennaio**: era calcolato sull'outflow pianificato (€4.650) invece che sull'effettivo. **Corretto**: €5.250.
12. **Surplus €2.250 con doppio uso narrativo**: nel 6.3 finanzia il supporto post-lancio, nel 6.7 "copre i costi operativi" dello spin-off. *Difendibile*: in un contratto a corpo il surplus è margine del fornitore, *impiegato* per garantire il supporto promesso — stessa cassa, dirlo così.
13. **Riclassificazione Maraffa senza Change Request formale esplicita**. *Difendibile*: la modifica fu discussa e approvata con lo sponsor nella sostanza del processo (compensata riducendo Could Have, tracciata con nota di revisione nella MoSCoW); nella forma, un CR numerato con Project Impact Statement sarebbe stato più rigoroso — coerente con la lesson learned sui domain expert.
14. **WCAG 2.1 AA è Should nella RBS ma criterio di successo nel POS/CoS**. *Difendibile*: il *core* dell'accessibilità è dentro i Must del frontend (contrasti, dimensioni target); l'etichetta Should riguarda la certificazione formale completa, comunque verificata a consuntivo.
15. Minori, tutti **corretti**: residuo "Jira" nella RBS (→ Notion); catering del BMC quadrato a €250; "velocity media finale" → "velocity media di regime (Sprint 1–7, escluso il natalizio)"; sotto-task e template del nodo CPM allineati alla v2.0.0.

**Secondo giro di audit (2026-08-09, 5 squadre: date/calendario, denaro, cast/riferimenti, regole di gioco, metriche) — esito.** Trovati e **corretti**: la griglia sprint del Backlog che correva da martedì a sabato (riallineata alla griglia lun–ven del Gantt: S1 28 Ott–7 Nov … S5 22 Dic–2 Gen … S11 16–31 Mar; etichette del CSV riallineate); l'accettazione formale datata domenica 10/05 → **lunedì 11/05** (Cap. 6 + relazione); il punteggio impossibile "41-38" in US-3.5 → "41-36" (79 non è esprimibile come 11n+3m: ogni smazzata distribuisce 11 punti interi più eventuali bonus Maraffa da 3); il totale punti per smazzata uniformato (10⅔ dalle carte + 1 di ultima presa = 11⅔ grezzi → 11 interi dopo l'arrotondamento per difetto, in RBS e RASCI); il lessico presa/smazzata dove il troncamento morde; il criterio busso/striscio/volo aggiunto a US-3.2; il break-even ottimistico ~50 → **~84 mesi** (al netto dei costi operativi); il PoC raccontato in due stadi coerenti (spike in Sprint 0 → PoC completo in Sprint 2); le milestone del network rinumerate M2/M3/M4/M6 (erano M1–M4 in conflitto con la tabella M1–M7, anche nello script HTML); il ritardo dello Sprint 7 attribuito all'attività M anche in §5.8; i codici rischio 2.1/6.2 al posto degli inesistenti R1/R4; tornei = Won't (non Could) nel Closing; il tutorial "Scopri le regole" non più spacciato per extra (era pianificato allo Sprint 6); PWA = Won't ovunque; gli SP dei task padre del CSV = somma dei figli (9 righe); notifiche in-app P1/Must e sidebar amici P2 nel Backlog/CSV; la sensitivity di N/Q precisata (i task Must di Q non sono de-scopabili); REQ-SOC-6.1 riqualificato come quota UI delle amicizie (niente doppio conteggio); "12 allegati" → 11; la chat 1-a-1 fantasma → chat globale lobby; PaaS/DigitalOcean/Confluence → stack canonico; coverage riconciliata (80% gate di merge, 85% target di progetto); riga chat in-game aggiunta alla RASCI; reconnection "30s" riformulata (heartbeat 30s, sospensione 5 min); le date nel weekend spostate a giorni feriali (approvazioni 2.4/2.9, materiali del kick-off venerdì 10/10, primo Status Meeting venerdì 17/10, Sprint 0 Review venerdì 24/10, review 19/12); l'action item del kick-off "approvazione Scoping/Planning" riqualificato in approvazione del verbale; la nota di superamento degli accordi preliminari nel 2.1; W1/W4/W3 della SWOT allineate; le versioni dei companion HTML allineate ai .md.

**Restano difendibili senza correzione** (risposte in FAQ §G): gli overlap FS minori non annotati nel CSV (H.7, I.7, J.5, K.5-6, Q.4 — micro-parallelismi interni alle attività); la 3ª tranche di domenica 15/02 (giorno fisso contrattuale); il doppio uso narrativo del surplus (voce 12); US-2.5 "candidata al rinvio" pur essendo Should (slittamento accettato formalmente dallo sponsor); l'effort del Game Engine 50 giorni nel MoSCoW contro i 73 della catena C-F-I-L-O nel network (il testing è nel QA trasversale, e le durate del network sono giorni di calendario con risorse part-time, non giorni-uomo).

**Punti di forza verificati con ricalcolo** (spendibili all'orale): i 160 task della WBS sono esatti; tutte le somme di MoSCoW (302 gg), Backlog (310 SP) e Cash Flow tornano; il CPM è corretto incluso il legame SS+31 (verificato anche dallo script di generazione dell'HTML); i 141 giorni lavorativi all'08/05/2026 sono esatti sul calendario reale (148 feriali − 7 festività) e il margine di 5 giorni è confermato; il CSV del Gantt è pulito rispetto a weekend e festività per tutte le 129 righe; la tabella EVM mensile è aritmeticamente coerente (tutti i CV/SV/CPI/SPI tornano); le matrici RASCI md e HTML coincidono cella per cella.

---

**Ultimo aggiornamento**: 2026-08-09 — versione didattica (riquadri "Ripasso" con la teoria del corso per ogni strumento); creato a valle della rilettura integrale di relazione e allegati, con audit di coerenza incrociata completato e correzioni applicate.
