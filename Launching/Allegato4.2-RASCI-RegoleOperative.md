# Allegato 4.2 - RASCI Matrix e Regole Operative
## v.1.0.0 – 15/10/2025

Questo documento definisce le **responsabilità del team** attraverso la RASCI Matrix e le **regole operative** per garantire una collaborazione efficace durante l'intero ciclo di vita del progetto MaraffaOnline.

---

## Parte 1: RASCI Matrix

### Cos'è la RASCI Matrix

La **RASCI Matrix** (Responsibility Assignment Matrix) è uno strumento di Project Management che chiarisce chi fa cosa in ogni attività del progetto. Elimina ambiguità, riduce conflitti e garantisce accountability.

**RASCI** sta per:

| Ruolo | Significato | Descrizione |
|-------|-------------|-------------|
| **R** - Responsible | **Responsabile** | Chi **esegue** l'attività e lavora per completarla. Possono essere più persone. |
| **A** - Accountable | **Approvatore** | Chi **approva** il risultato finale e risponde del completamento. **DEVE essere uno solo** per attività. |
| **S** - Support | **Supporto** | Chi **supporta** il Responsible fornendo assistenza quando richiesta. |
| **C** - Consulted | **Consultato** | Chi viene **consultato** per la propria expertise prima/durante l'attività. Comunicazione bidirezionale. |
| **I** - Informed | **Informato** | Chi viene **tenuto informato** sullo stato di avanzamento. Comunicazione unidirezionale. |

**Principio Chiave**: Ogni attività DEVE avere esattamente un Accountable. Se ci sono troppi Accountable, nessuno è veramente responsabile.

---

### RASCI Matrix - MaraffaOnline

#### Ruoli del Team

**Stakeholder / Sponsor**:
- **Giovanni Marchetti (GM)**: Project Sponsor (Maraffa Forever)
- **Francesca Giuliani (FG)**: Domain Expert / Consulente Regole

**Project Team (PlayHeritage Labs)**:
- **Marco Venturi (MV)**: Project Manager
- **Elena Rossi (ER)**: Tech Lead / Backend Developer
- **Sara Bianchi (SB)**: Backend Developer
- **Luca Moretti (LM)**: UX Designer / Frontend Developer
- **Andrea Conti (AC)**: DevOps Engineer

---

### RASCI Matrix Dettagliata

#### Legenda Colori (per visualizzazione)

- **R** = Verde
- **A** = Arancione
- **S** = Viola
- **C** = Blu
- **I** = Giallo

---

## 1. Game Engine (Waterfall)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Definizione struttura dati carte** | I | C | I | A | R | - | - |
| **Implementazione mazzo 40 carte** | I | C | I | A | R | - | - |
| **Algoritmo distribuzione 2×5** | I | C | I | A | R | - | - |
| **Codifica ordine forza carte** | I | C | I | A | R | - | - |
| **Implementazione regole presa (maggiore vince)** | I | C | I | A | R | - | - |
| **Logica briscola (determinazione e priorità)** | I | C | I | A | R | - | - |
| **Sistema turni 4 giocatori** | I | C | I | A | R | - | - |
| **Gestione chi inizia (4 di denari)** | I | C | I | A | R | - | - |
| **Calcolo punteggio fine presa** | I | C | I | A | R | - | - |
| **Tracciamento punteggio mano (11pt totali)** | I | C | I | A | R | - | - |
| **Condizione vittoria (41pt + figura)** | I | C | I | A | R | - | - |
| **Gestione Maraffa/Cricca (A+2+3 briscola = +3pt)** | I | C | I | A | R | - | - |
| **Validazione mosse legali** | I | C | I | A | R | - | - |
| **Detection casi edge (abbandono, timeout)** | I | - | I | A | R | - | - |
| **Unit test logica di gioco (>90% coverage)** | I | C | I | A | R | - | - |
| **Validazione regole con Francesca (Sessione 1)** | A | R | S | C | C | - | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend Developer)
**Consulted Critico**: Francesca Giuliani (Domain Expert)

---

## 2. Backend Server (Agile Iterativo)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Setup progetto Node.js + Express** | I | - | I | A | R | - | S |
| **Configurazione database PostgreSQL** | I | - | I | A | R | - | S |
| **Schema DB: tabelle utenti** | I | - | I | A | R | - | - |
| **Schema DB: tabelle partite/mosse** | I | - | I | A | R | - | - |
| **API registrazione utente** | I | - | I | A | R | - | - |
| **API login + JWT token** | I | - | I | A | R | - | S |
| **API guest access (no registrazione)** | I | - | I | A | R | - | - |
| **API creazione lobby** | I | - | I | A | R | - | - |
| **API join lobby (4 giocatori max)** | I | - | I | A | R | - | - |
| **API start partita** | I | - | I | A | R | - | - |
| **API gestione profili utente** | I | - | I | A | R | C | - |
| **API statistiche personali** | I | - | I | A | R | C | - |
| **API leaderboard community** | I | - | I | A | R | C | - |
| **API sistema amicizie** | I | - | I | A | R | C | - |
| **Middleware autenticazione JWT** | I | - | I | A | R | - | - |
| **Middleware error handling** | I | - | I | A | R | - | - |
| **Rate limiting (protezione DDoS)** | I | - | I | A | R | - | S |
| **Database migration scripts** | I | - | I | A | R | - | S |
| **API documentation (Swagger/OpenAPI)** | I | - | I | A | R | C | - |
| **Integration test API (Jest)** | I | - | I | A | R | - | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend Developer)
**Support**: Andrea Conti (per infra-related tasks)

---

## 3. Real-Time Communication (Agile Adattivo)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Setup Socket.IO server** | I | - | I | A | R | - | S |
| **Proof of Concept latency test (<200ms)** | I | - | I | A | R | - | S |
| **WebSocket event: player-join** | I | - | I | A | R | C | - |
| **WebSocket event: card-played** | I | - | I | A | R | C | - |
| **WebSocket event: turn-change** | I | - | I | A | R | C | - |
| **WebSocket event: game-state-update** | I | - | I | A | R | C | - |
| **WebSocket event: game-end** | I | - | I | A | R | C | - |
| **Sincronizzazione stato 4 client** | I | - | I | A | R | S | - |
| **Gestione disconnessione giocatore** | I | - | I | A | R | - | - |
| **Reconnection handling (30s timeout)** | I | - | I | A | R | - | - |
| **Notifiche real-time eventi partita** | I | - | I | A | R | C | - |
| **Load testing 50 partite simultanee** | I | - | I | A | R | - | S |
| **Monitoring latency con Sentry** | I | - | I | A | R | - | S |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend Developer)
**Consulted**: Luca Moretti (per integration frontend)
**Support**: Andrea Conti (load testing, monitoring)

---

## 4. Frontend Web (Agile Iterativo)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Setup progetto React + Vite** | I | - | I | A | - | R | S |
| **Configurazione Tailwind CSS** | I | - | I | A | - | R | - |
| **Design system (colori, tipografia, componenti)** | C | - | I | A | - | R | - |
| **Homepage / Landing page** | C | - | I | A | - | R | - |
| **Schermata registrazione/login** | I | - | I | A | - | R | - |
| **Dashboard utente** | C | - | I | A | - | R | - |
| **Lobby: creazione partita** | C | - | I | A | - | R | S |
| **Lobby: lista partite disponibili** | C | - | I | A | - | R | S |
| **Sala d'attesa (4 giocatori)** | C | - | I | A | - | R | - |
| **Tavolo da gioco virtuale** | C | C | I | A | S | R | - |
| **Rendering carte italiane (40 asset grafici)** | C | - | I | A | - | R | - |
| **Drag & drop carte (react-dnd o dnd-kit)** | I | - | I | A | S | R | - |
| **Animazioni giocata carte** | I | - | I | A | - | R | - |
| **Visualizzazione punteggio real-time** | I | C | I | A | S | R | - |
| **Indicatore turno corrente** | I | - | I | A | - | R | - |
| **Schermata fine partita (vincitore, punteggi)** | C | - | I | A | - | R | - |
| **Profili utente (avatar, statistiche)** | C | - | I | A | - | R | - |
| **Leaderboard community** | C | - | I | A | - | R | - |
| **Sistema notifiche UI (toast)** | I | - | I | A | - | R | - |
| **Responsive design (desktop + tablet)** | C | - | I | A | - | R | - |
| **Accessibilità (WCAG 2.1 AA)** | I | - | I | A | - | R | - |
| **Cross-browser testing (Chrome, Firefox, Safari)** | I | - | I | A | - | R | S |
| **Unit test componenti (Vitest)** | I | - | I | A | - | R | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Luca Moretti (UX Designer / Frontend Developer)
**Support**: Sara Bianchi (per componenti complessi React), Andrea Conti (cross-browser testing)
**Consulted**: Giovanni Marchetti (UX decisions), Francesca Giuliani (rendering corretto carte/punteggi)

---

## 5. Social & Community (Incrementale)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Sistema amicizie: richiesta/accettazione** | C | - | I | A | R | S | - |
| **Sistema amicizie: lista amici** | C | - | I | A | R | S | - |
| **Storico partite personali** | C | - | I | A | R | S | - |
| **Replay partite (visualizzazione mosse)** | C | - | I | A | R | S | - |
| **Leaderboard: classifica globale** | C | - | I | A | R | S | - |
| **Leaderboard: filtri (settimanale, mensile, all-time)** | C | - | I | A | R | S | - |
| **Badge/achievement system (opzionale MVP)** | C | - | A | C | R | S | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend) + Luca Moretti (Frontend)
**Consulted**: Giovanni Marchetti (feature priority)

---

## 6. Infrastructure & DevOps (Incrementale)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Provisioning server Hetzner** | I | - | I | C | - | - | R |
| **Setup Docker containers (backend, frontend, db)** | I | - | I | C | - | - | R |
| **GitLab repository setup** | I | - | I | C | S | S | R |
| **GitLab CI/CD pipeline (build, test, deploy)** | I | - | I | C | S | S | R |
| **Ambiente staging** | I | - | I | C | - | - | R |
| **Ambiente production** | I | - | I | C | - | - | R |
| **SSL certificato (Let's Encrypt)** | I | - | I | C | - | - | R |
| **DNS setup (maraffaonline.it)** | I | - | I | C | - | - | R |
| **Cloudflare CDN + DDoS protection** | I | - | I | C | - | - | R |
| **Database backup automatico (daily)** | I | - | I | C | - | - | R |
| **Monitoring: Sentry (error tracking)** | I | - | I | C | S | - | R |
| **Monitoring: UptimeRobot (uptime)** | I | - | I | C | - | - | R |
| **Log aggregation (Winston)** | I | - | I | C | S | - | R |
| **Disaster recovery plan** | I | - | A | C | - | - | R |

**Accountable**: Marco Venturi (PM) per disaster recovery, Elena Rossi (Tech Lead) per setup tecnici
**Responsible Principale**: Andrea Conti (DevOps Engineer)
**Consulted**: Elena Rossi (decisioni architetturali)
**Support**: Sara Bianchi (backend integration), Luca Moretti (frontend deployment)

---

## 7. Testing & QA (Continuo)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Unit test Game Engine (Jest)** | I | C | I | A | R | - | - |
| **Unit test API Backend (Jest)** | I | - | I | A | R | - | - |
| **Unit test componenti Frontend (Vitest)** | I | - | I | A | - | R | - |
| **Integration test end-to-end (Playwright)** | I | - | I | A | S | S | R |
| **Load testing 50 partite simultanee (k6)** | I | - | I | A | S | - | R |
| **Security testing (SQL injection, XSS)** | I | - | I | A | S | - | R |
| **Accessibility testing (WCAG 2.1 AA)** | I | - | I | A | - | R | - |
| **Cross-browser testing (BrowserStack)** | I | - | I | A | - | R | S |
| **User Acceptance Testing: recruitment 10 tester** | A | S | R | C | - | - | - |
| **UAT: preparazione test plan** | C | C | R | S | - | S | - |
| **UAT: esecuzione sessioni test** | A | R | S | C | - | - | - |
| **UAT: raccolta feedback** | A | R | R | C | - | - | - |
| **Bug fixing post-UAT** | I | C | I | A | R | R | R |
| **Validazione finale regole (Sessione 2)** | A | R | S | C | C | - | - |

**Accountable UAT**: Giovanni Marchetti (sponsor approval)
**Responsible UAT Execution**: Francesca Giuliani (conduce sessioni con tester)
**Responsible Test Plan**: Marco Venturi (PM)
**Responsible Bug Fixing**: Tutti i developer (ER, SB, LM, AC)

---

## 8. Project Management (Trasversale)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Project Scoping Meeting** | C | C | R | C | C | C | C |
| **Project Planning (WBS, Gantt, Cash Flow)** | A | - | R | C | - | - | - |
| **Project Kick-Off Meeting** | A | I | R | I | I | I | I |
| **Daily Standup facilitation** | - | - | R | S | I | I | I |
| **Sprint Planning** | C | - | R | C | I | I | I |
| **Sprint Review** | A | C | R | R | R | R | R |
| **Sprint Retrospective** | - | - | R | I | I | I | I |
| **Project Status Meeting (weekly)** | A | I | R | C | - | - | - |
| **Cash Flow Tracking (monthly report)** | A | - | R | - | - | - | - |
| **Risk Management (weekly review)** | C | - | R | C | - | - | - |
| **Change Request evaluation** | A | C | R | C | - | - | - |
| **Stakeholder communication** | C | - | R | S | - | - | - |
| **Documentation Confluence** | I | - | R | S | S | S | S |
| **Final Project Report** | A | - | R | C | - | - | - |
| **Lessons Learned session** | C | C | R | C | C | C | C |
| **Project Closure celebration** | A | I | R | I | I | I | I |

**Accountable Principale**: Giovanni Marchetti (Project Sponsor) per approvazioni milestone
**Responsible Principale**: Marco Venturi (Project Manager)
**Support**: Elena Rossi (Tech Lead) per decisioni tecniche

---

## Analisi RASCI: Insights Chiave

### Distribuzione Responsabilità

**Accountable Frequency** (chi approva):
- **Giovanni Marchetti (Sponsor)**: 12 decisioni (milestone, budget, UAT, closure)
- **Elena Rossi (Tech Lead)**: 67 decisioni (tutte le attività tecniche)
- **Marco Venturi (PM)**: 15 decisioni (planning, status, change requests, UAT plan)

**Responsible Frequency** (chi esegue):
- **Sara Bianchi (Backend)**: 45 task (Game Engine, Backend Server, Real-Time)
- **Luca Moretti (Frontend/UX)**: 28 task (Frontend Web, Social UI)
- **Andrea Conti (DevOps)**: 18 task (Infrastructure, CI/CD, Testing automation)
- **Marco Venturi (PM)**: 12 task (planning, reporting, UAT coordination)
- **Francesca Giuliani (Expert)**: 3 task (validazione regole sessioni 1-2, conduzione UAT)

**Consulted Frequency** (expertise richiesta):
- **Francesca Giuliani**: 18 consultazioni (tutte attività legate a regole Maraffone)
- **Giovanni Marchetti**: 15 consultazioni (decisioni UX, feature priority, budget)
- **Elena Rossi**: 25 consultazioni (decisioni architetturali cross-team)

**Balanced Workload**: La distribuzione è equilibrata, con Sara (Backend) e Luca (Frontend) come Responsible principali, Elena come Accountable tecnico, Marco come orchestratore PM.

---

## Parte 2: Regole Operative

Le **Regole Operative** definiscono i processi per la gestione quotidiana del team e la risoluzione di problemi ricorrenti. Stabiliscono un framework condiviso per decision-making, conflict resolution, brainstorming e meeting management.

---

### 1. Problem Solving

Per il problem solving del progetto MaraffaOnline si è scelto di adottare un approccio strutturato in cinque passi, ispirato al metodo Lean Problem Solving e alle pratiche Agile. Questo approccio garantisce che i problemi vengano affrontati in modo sistematico e che le soluzioni siano efficaci e sostenibili nel tempo.

Quando un problema emerge, che sia durante il Daily Standup, in un messaggio su Slack o durante una Sprint Review, la prima responsabilità è identificarlo chiaramente. Chiunque nel team può sollevare un problema, ma è fondamentale che venga descritto in modo rigoroso affinché tutti possano comprenderlo. La descrizione deve rispondere a quattro domande: Cosa sta succedendo? Dove si verifica? Quando è iniziato? Quale impatto ha sul progetto? Ad esempio, se la latenza WebSocket supera i 500ms sul server di staging dopo un deploy, questo deve essere comunicato immediatamente perché rende il gioco praticamente ingiocabile.

Una volta identificato il problema, il passo successivo è analizzare la causa root. Questo compito spetta al Responsible dell'area coinvolta insieme all'Accountable, con eventuale supporto di persone Consulted secondo la RASCI Matrix. Per individuare la vera causa si utilizza la tecnica dei "5 Whys": ponendo ripetutamente la domanda "Perché?" si scava progressivamente fino alla radice del problema. Nel caso della latenza WebSocket, chiedendosi perché il server è sovraccarico, perché ci sono troppi log, perché il logger è in modalità DEBUG, si scopre che manca la configurazione della variabile d'ambiente LOG_LEVEL nel deployment checklist. Questa analisi deve essere rapida, al massimo 30 minuti, altrimenti si procede con escalation alla Tech Lead.

Identificata la causa root, il team procede con il brainstorming per proporre soluzioni alternative. Ogni soluzione viene valutata considerando i pro e i contro, e si privilegiano interventi rapidi quando l'impatto del problema è alto. Nel nostro esempio si potrebbero proporre tre soluzioni: una fix immediato aggiungendo LOG_LEVEL=INFO in staging (10 minuti), la creazione di uno script automatico di verifica pre-deploy per prevenire futuri problemi (1 giorno di lavoro), oppure un upgrade del server a un tier superiore (soluzione costosa e probabilmente eccessiva). La decisione finale spetta all'Accountable, che in questo caso sceglie di implementare subito la soluzione A e pianificare la B come follow-up.

L'implementazione della soluzione viene assegnata a un Responsible specifico e tracciata come action item su Notion Database con una deadline chiara. Quando il task è completato, si comunica l'update su Slack per tenere informato il team. Infine, l'Accountable verifica che il problema sia effettivamente risolto entro 24-48 ore dall'implementazione. Se il problema persiste, si torna indietro all'analisi con le nuove informazioni acquisite.

Tutti i problemi critici che emergono durante gli sprint vengono discussi nella Sprint Retrospective per capire come prevenirli in futuro. Questo approccio non solo risolve il problema immediato, ma contribuisce al miglioramento continuo del processo di sviluppo.

---

### 2. Decision Making

Per quanto riguarda il decision making del progetto MaraffaOnline si è adottato un approccio consultivo a tre livelli, che rappresenta una via di mezzo tra il metodo direttivo e quello completamente collaborativo. Questo approccio permette di beneficiare della varietà di prospettive e conoscenze del gruppo, garantendo al contempo che le decisioni finali siano coerenti con la visione strategica e le responsabilità del leader. Il metodo favorisce un ambiente di lavoro inclusivo e partecipativo, mantenendo però una chiara direzione e responsabilità decisionale.

Le decisioni sono state categorizzate in tre livelli di importanza, ciascuno con un proprio decision maker e processo. Al livello operativo troviamo le decisioni quotidiane sull'implementazione tecnica: la scelta di naming convention, librerie minori, o fix di bug. Queste decisioni spettano direttamente al Responsible che sta lavorando sul task, senza necessità di escalation. Ad esempio, quando Luca deve decidere se usare react-dnd o dnd-kit per il drag & drop delle carte, può autonomamente testare entrambe le librerie con un proof of concept di 2 ore e scegliere quella che preferisce. La consulenza di altri sviluppatori è opzionale e può avvenire attraverso pair programming o code review, ma la decisione finale rimane in capo al developer.

Il secondo livello riguarda le decisioni tattiche, che hanno un impatto più ampio sul progetto. Queste includono scelte architetturali, design delle API, schema del database, o aggiustamenti al backlog dello sprint. In questi casi il decision maker è la Tech Lead Elena Rossi insieme al Project Manager Marco Venturi, che devono raggiungere un consensus. Il processo prevede che Elena presenti le opzioni tecniche con i relativi pro e contro, Marco valuti l'impatto su timeline, budget e scope, si consulti brevemente il team durante uno Sprint Planning o Status Meeting, e infine Elena decida sull'aspetto tecnico mentre Marco su quello di project management. Ad esempio, se emerge la proposta di cambiare da REST a GraphQL per le API della lobby, Elena e Marco valutano insieme i trade-off e decidono di non procedere perché richiederebbe troppo refactoring per benefici marginali nel MVP. Ogni decisione tattica viene documentata su Confluence e deve essere presa entro 48 ore dall'identificazione della necessità.

Il terzo livello comprende le decisioni strategiche che impattano significativamente il progetto: modifiche allo scope, aggiustamenti al budget, estensioni della timeline, o cambiamenti metodologici. Queste decisioni spettano allo Sponsor Giovanni Marchetti, con input fondamentale dal Project Manager e dalla Tech Lead, e con consulenza di tutto il team e di Francesca Giuliani quando si tratta di aspetti legati alle regole del gioco. Se ad esempio il cliente richiede l'aggiunta di un'app mobile nativa nel MVP, Marco prepara un Project Impact Statement dettagliato, Elena stima l'effort aggiuntivo in 80 giorni e €10.000, si presentano a Giovanni tre opzioni (accettare ed estendere la timeline, posticipare alla versione 1.1, o rifiutare), e Giovanni prende la decisione finale. Il tempo per queste decisioni è generalmente di una settimana, salvo situazioni di urgenza.

La regola d'oro che guida tutto il processo decisionale è "decide at the lowest level possible, escalate only when necessary". Questo principio assicura che le decisioni vengano prese rapidamente da chi ha le informazioni più rilevanti, evitando colli di bottiglia e sovraccarico dei livelli decisionali superiori.

---

### 3. Conflict Resolution

Per la risoluzione dei conflitti si è scelto un approccio collaborativo e progressivo, che riconosce che i conflitti sono naturali in progetti complessi e che possono essere affrontati con un protocollo che garantisca risoluzione rapida ed equa.

I conflitti nel progetto MaraffaOnline possono essere di tre tipologie principali. I conflitti tecnici riguardano scelte architetturali o tecnologiche, come ad esempio la decisione tra MongoDB e PostgreSQL. In questi casi il resolver è la Tech Lead Elena Rossi, che ascolta gli argomenti di entrambe le parti (15 minuti ciascuna) e decide basandosi su criteri oggettivi come performance, scalabilità, expertise del team e time-to-market. Una volta presa la decisione, il team si allinea secondo il principio "disagree and commit": anche chi non è d'accordo si impegna a supportare la decisione finale. I conflitti di priorità emergono quando ci sono dubbi su quale feature implementare prima. In questo caso il resolver è il Project Manager Marco Venturi, che valuta il business value rispetto all'effort usando la matrice MoSCoW e decide basandosi sul critical path e sul valore per lo stakeholder. Il task prioritizzato torna nello Sprint Backlog. Infine ci sono i conflitti interpersonali, come quando un membro del team non rispetta gli orari di lavoro altrui. Qui Marco agisce come facilitatore neutrale attraverso una conversazione privata "speak truth to power", con l'obiettivo di trovare una soluzione win-win piuttosto che imporre una decisione. Se il conflitto non si risolve, si procede con escalation alle risorse umane di PlayHeritage Labs, che esula dallo scope del progetto.

Il processo di risoluzione segue tre fasi progressive. Nella prima fase, che dura al massimo 24 ore, le parti coinvolte parlano direttamente tra loro senza intermediari, in un setting privato via Zoom o in presenza. L'obiettivo è risolv ere il conflitto alla fonte: statisticamente l'80% dei conflitti si risolvono a questo livello. Se la discussione diretta non porta a una soluzione, si passa alla seconda fase di mediazione facilitata entro 48 ore. Marco o Elena facilitano un meeting strutturato di 30 minuti dove prima la parte A espone la propria posizione per 5 minuti, poi la parte B fa lo stesso, si identificano gli interessi comuni per altri 5 minuti, si fa brainstorming di possibili soluzioni per 10 minuti, e infine il facilitatore prende una decisione negli ultimi 5 minuti. Se anche questa fase fallisce, entro 72 ore dall'inizio del conflitto si procede con la terza fase di decisione esecutiva. L'escalation va al decisore appropriato: Elena per conflitti tecnici, Giovanni per conflitti di scope o priorità, HR per conflitti interpersonali. La decisione presa a questo livello è finale e non appellabile, e il team deve allinearsi. I conflitti che raggiungono la fase 2 o 3 vengono documentati su Confluence nell'Issue Log per essere discussi in retrospective.

---

### 4. Brainstorming

Per l'attività di brainstorming tutte le persone coinvolte si riuniscono in una stanza con una lavagna, oppure utilizzano strumenti digitali come Miro quando qualcuno lavora da remoto. Il brainstorming è utilizzato per problem solving creativo, design thinking e generazione di idee per feature complesse, come ad esempio decidere come visualizzare il bonus Maraffa/Cricca nell'interfaccia, o per affrontare issue senza soluzioni ovvie. È uno strumento prezioso anche durante le Sprint Retrospective quando si cerca di capire cosa migliorare nel processo di lavoro.

Le sessioni durano tipicamente tra 30 e 45 minuti e seguono un formato strutturato. Un giorno prima della sessione, Marco o Elena convocano il meeting condividendo il topic, il contesto e l'obiettivo, in modo che i partecipanti possano riflettere in anticipo. La preparazione non è richiesta ma è consigliata per aumentare la qualità del contributo. La sessione vera e propria inizia con un warm-up di 5 minuti, un icebreaker per stimolare la creatività, come chiedere a tutti di descrivere il gioco Maraffa in tre parole non tecniche.

Segue la fase di divergent thinking della durata di 15 minuti, dove l'obiettivo è generare il maggior numero possibile di idee. Durante questa fase valgono regole precise: nessuna critica è permessa perché nessuna idea è stupida, si privilegia la quantità sulla qualità, si incoraggia a costruire sulle idee altrui dicendo "Yes, and..." invece di "Yes, but...", e le idee stravaganti sono benvenute. Il facilitatore, tipicamente Marco, tiene il tempo e incoraggia i membri più silenziosi a partecipare, mentre uno scribe (Andrea o Luca) annota tutte le idee su una lavagna fisica o digitale. A turno ognuno riferisce un'idea al responsabile che scrive una parola chiave sulla lavagna, assicurando che tutti abbiano modo di partecipare e sentirsi coinvolti. Questo processo favorisce la creatività e l'originalità, stimolando pensieri divergenti e l'interazione tra diverse prospettive.

Nella fase successiva di convergent thinking, che dura altri 15 minuti, si passa dalla generazione alla valutazione. Le idee simili vengono raggruppate usando affinity mapping, poi ogni partecipante ha 3 voti da distribuire (dot voting) per identificare le top 3 idee più promettenti. Gli ultimi 10 minuti sono dedicati all'action plan: per ciascuna delle top 3 idee si assegna un owner Responsible, si definisce il next step (che può essere un proof of concept, uno spike di ricerca, o l'implementazione vera e propria), e si stabilisce una deadline. Al termine della sessione, lo scribe pubblica le note su Confluence entro fine giornata e gli action item vengono aggiunti al Notion Database.

Il team utilizza diverse tecniche di brainstorming a seconda del contesto. La tecnica Round Robin prevede un giro di tavolo dove ognuno propone un'idea a turno, ed è particolarmente utile per coinvolgere i membri più introversi. Il Brainwriting 6-3-5 coinvolge 6 persone che scrivono 3 idee ciascuno in 5 minuti, poi passano il foglio al vicino che legge le idee altrui e aggiunge 3 varianti: il risultato è un totale di 108 idee in soli 30 minuti. Per problemi di UI/UX, Luca utilizza spesso la tecnica Crazy 8s, che consiste nel produrre 8 sketch rapidi di soluzioni in 8 minuti, forzando la creatività attraverso il vincolo temporale. Le idee raccolte vengono poi valutate e raffinate, permettendo di selezionare le soluzioni più promettenti per ulteriori sviluppi.

---

### 5. Team Meetings

Sono previste riunioni frequenti per garantire coordinamento e allineamento continuo tra i membri del team. Il progetto MaraffaOnline adotta cinque tipologie di meeting ricorrenti, ciascuna con un formato e obiettivi specifici, oltre a meeting ad-hoc convocati quando necessario.

Il Daily Standup è il cuore della comunicazione quotidiana. Si svolge ogni giorno lavorativo dalle 09:00 alle 09:15, con una durata fissa di 15 minuti esatti. Partecipano tutti i membri del team interno: Marco, Elena, Sara, Luca e Andrea. Il meeting si tiene in piedi per mantenere la brevità, ed è possibile partecipare via Zoom per chi lavora da remoto. Ogni persona risponde a tre domande in massimo 2 minuti: cosa ho fatto ieri (con focus sui task completati), cosa farò oggi (con un commitment specifico), e ho blocker che mi impediscono di procedere. Ad esempio, Sara potrebbe dire "Ieri ho completato l'API per la creazione della lobby con test coverage al 95%. Oggi inizio l'API per il join della lobby, stimo 4 ore. Non ho blocker". Il meeting inizia puntualmente alle 09:00 e chi arriva tardi perde il turno. Durante lo standup non si fa problem solving: i problemi vengono parcheggiati e risolti dopo con le sole persone coinvolte. Marco facilita il meeting tenendo il tempo e annotando i blocker per il follow-up immediato post-standup con Responsible e Accountable. Alla fine, lo stato dei task viene aggiornato sul Notion Database.

Lo Sprint Planning si tiene il primo lunedì di ogni sprint, quindi ogni due settimane, dalle 09:00 alle 10:30 per una durata totale di un'ora e mezza. Partecipa tutto il team interno, con Giovanni che può unirsi opzionalmente se vuole dare input sulle priorità. L'obiettivo è selezionare le user stories dal Product Backlog per il prossimo sprint. Il meeting inizia con la definizione dello Sprint Goal in 10 minuti da parte di Marco ed Elena: per esempio, "Completare Backend Auth + POC Socket.IO" per lo Sprint 3. Segue una review del backlog di 15 minuti dove Marco presenta le top user stories già prioritizzate secondo la matrice MoSCoW e ne legge i criteri di accettazione. La parte centrale del meeting, 30 minuti, è dedicata alla stima delle story tramite Planning Poker: il team assegna story points usando la scala Fibonacci (1, 2, 3, 5, 8, 13, 21) alle user stories non ancora stimate. Nei successivi 20 minuti Marco ed Elena selezionano le stories che entreranno nello Sprint Backlog, con un commitment tipicamente di 40 story points basato sulla velocity storica, verificando che lo sprint goal sia raggiungibile. Segue il task breakdown di 15 minuti dove ogni user story viene scomposta in task tecnici di durata inferiore al giorno e si assegnano i Responsible, chiedendo prima volontari e solo poi assegnando i task rimanenti. Gli ultimi 10 minuti sono dedicati alla review dei rischi specifici dello sprint, come dipendenze esterne o assenze programmate. Il meeting produce due output: lo Sprint Backlog definito su Notion Database e lo Sprint Goal pubblicato su Confluence e Slack.

La Sprint Review si tiene l'ultimo venerdì di ogni sprint dalle 14:00 alle 15:00. Partecipa il team interno più Giovanni in modo obbligatorio e Francesca quando si dimostrano funzionalità legate alle regole del gioco. L'obiettivo è mostrare l'increment completato e raccogliere feedback dallo stakeholder. Marco apre con un recap di 5 minuti sullo sprint goal, confrontando gli story points committed con quelli effettivamente completati e mostrando il trend della velocity. La parte centrale, 30 minuti, è la demo dal vivo delle feature completate secondo la "Definition of Done", condotta dal developer che le ha implementate. Ad esempio, nello Sprint 4 Sara potrebbe dimostrare le API della lobby funzionanti usando Postman. Seguono 15 minuti di feedback da Giovanni e Francesca con commenti, domande e suggerimenti, al termine dei quali Giovanni decide se accettare i deliverable o richiedere modifiche. Gli ultimi 10 minuti sono dedicati all'aggiustamento del Product Backlog da parte di Marco, con re-prioritizzazione basata sui feedback ricevuti e identificazione di eventuali nuove user stories. È importante che vengano dimostrate solo feature completamente "Done", no work in progress, e si preferisce mostrare software funzionante piuttosto che slide. Se Giovanni richiede modifiche sostanziali allo scope, si attiva il Change Request Process formale. Il meeting produce due output: l'accettazione o il rifiuto dei deliverable dello sprint e l'aggiornamento del Product Backlog.

Immediatamente dopo, lo stesso venerdì dalle 15:00 alle 16:00, si tiene la Sprint Retrospective. Questo è un safe space riservato esclusivamente al team interno, senza Giovanni né Francesca. L'obiettivo è il miglioramento continuo: capire cosa ha funzionato e cosa può essere migliorato nel processo di lavoro. Si utilizza il formato "Start/Stop/Continue". Il meeting inizia con un warm-up di 5 minuti, un icebreaker come chiedere a tutti di valutare l'energia dello sprint da 1 a 10. Seguono 10 minuti di riflessione individuale in silenzio dove ognuno scrive su post-it fisici o digitali su Miro tre categorie di osservazioni: cosa dovremmo iniziare a fare (Start), cosa dovremmo smettere di fare (Stop), e cosa funziona e dobbiamo mantenere (Continue). Nella fase di sharing and grouping di 15 minuti, ogni persona presenta i propri post-it in un minuto mentre Marco facilita raggruppando le osservazioni per temi comuni. La prioritizzazione dura 10 minuti e usa il dot voting: ognuno vota i tre issues più importanti da risolvere, identificando collettivamente i top 2 action items per il prossimo sprint. Gli ultimi 15 minuti sono dedicati all'action plan: si definiscono azioni concrete per i top 2 issues, si assegna un owner Responsible e una deadline. Ad esempio, un action item potrebbe essere "Andrea crea template PR checklist su GitLab entro fine settimana". Si chiude con 5 minuti di meta-feedback sulla retrospettiva stessa per migliorare anche questo processo. Vale la "Vegas Rule": ciò che viene detto in retrospective rimane in retrospective e non viene escalato a Giovanni, a meno di problemi gravi come harassment. Il meeting produce 2 action items concreti per miglioramento processo e note pubblicate su Confluence accessibili solo al team interno.

Il Project Status Meeting si tiene ogni venerdì dalle 16:00 alle 17:00 ed è il punto di controllo settimanale con lo sponsor. Marco presenta, Giovanni partecipa obbligatoriamente, Elena co-presenta la parte tecnica, e altri membri possono essere invitati se necessario. L'obiettivo è fornire un update esecutivo sulla salute complessiva del progetto analizzando scope, time, budget, quality e risks. Marco apre con un executive summary di 5 minuti mostrando lo status generale usando il sistema stoplight (Verde/Giallo/Rosso) e il progresso verso le milestone. Seguono quattro sezioni di 10 minuti ciascuna: scope status con feature completate versus pianificate ed eventuali change request ricevute, schedule status con il progresso percentuale sul critical path del Gantt e forecast sulle milestone, budget status con il cash flow corrente versus pianificato e proiezione del surplus o deficit a fine progetto, e quality & risks presentati da Elena con trend dei bug aperti e chiusi, test coverage percentuale e top 3 rischi attuali con status della mitigazione. I successivi 10 minuti sono dedicati alle decisioni necessarie dove Marco e Giovanni discutono item che richiedono approvazione dello sponsor o escalation di conflitti critici. Si chiude con 5 minuti di Q&A da parte di Giovanni. Il meeting produce uno Stoplight Report pubblicato su Confluence e la documentazione delle decisioni prese da Giovanni. Il report usa un formato tabellare chiaro: ogni area (Scope, Schedule, Budget, Quality, Risks) ha un colore (verde, giallo o rosso) e una nota esplicativa.

In casi di urgenza vengono convocati meeting ad-hoc da Marco o Elena, tipicamente quando emerge un blocker critico, serve un'escalation immediata, o va presa una decisione strategica urgente. Questi meeting vengono organizzati entro 24 ore dall'identificazione dell'urgenza e durano al massimo 30 minuti con focus ristretto al problema specifico. Ad esempio, se il server Hetzner va giù per manutenzione non pianificata, si convoca immediatamente un meeting di emergenza per attivare il disaster recovery plan. Inoltre, sono previsti dei review meeting anche in concomitanza con il raggiungimento di una milestone importante. Nel caso si riscontrino problemi è consigliato indire una riunione con solamente le persone coinvolte, evitando di coinvolgere l'intero team quando non necessario.

---

### 6. Change Management

Le richieste di modifica allo scope, alla timeline o al budget già approvati richiedono una gestione formale per evitare il temuto scope creep che può compromettere il successo del progetto. Nel progetto MaraffaOnline si è adottato un processo strutturato in cinque passi che garantisce valutazione oggettiva e trasparenza nelle decisioni.

Un Change Request si attiva in quattro situazioni: quando lo stakeholder richiede una nuova feature non prevista nel Project Overview Statement, quando richiede modifiche a feature già approvate che vanno oltre semplici bug fix, quando il team identifica un'impossibilità tecnica che richiede aggiustamenti allo scope, o quando un evento esterno impatta il progetto come un ipotetico cambio del regolamento ufficiale del Maraffa. Ad esempio, se Giovanni richiede l'integrazione con Facebook per la condivisione dei risultati delle partite, questo attiverebbe il processo formale.

Il primo step è la submission: il richiedente compila un Change Request Form disponibile su Confluence indicando il titolo della modifica, una descrizione dettagliata, la motivazione business che spiega perché è importante, e la priorità percepita tra Low, Medium, High o Critical. Il secondo step è l'impact analysis condotta da Marco e Elena in 2-3 giorni lavorativi (esclusi weekend e festività; per Change Request ricevute nel weekend o in giorni festivi, il conteggio parte dal primo giorno lavorativo successivo). Analizzano l'impatto su cinque dimensioni: lo scope identificando quali feature andrebbero aggiunte, modificate o rimosse, il time calcolando i giorni aggiuntivi e l'impatto sul critical path, il budget stimando i costi extra per team, tools o licenze, la quality valutando l'impatto sui test e i rischi aggiuntivi, e le resources determinando se serve expertise esterna. L'output di questa analisi è un Project Impact Statement che presenta la richiesta di change, l'analisi dettagliata degli impatti, tre opzioni possibili come accettare ed estendere la timeline, differire a versione successiva o rifiutare completamente, e la raccomandazione del Project Manager con motivazione e benefici di ciascuna scelta.

Il terzo step è la decisione dello Sponsor. Marco presenta il Project Impact Statement a Giovanni che ha una settimana per decidere se accettare, defer o rifiutare. Se accetta e la modifica impatta significativamente budget o timeline, si rinegozia il contratto secondo le clausole contrattuali. Il quarto step, che si attiva solo se la richiesta è accettata, è l'implementation: si aggiornano tutti i documenti di progetto come POS, WBS, Gantt e Product Backlog, si comunica il change a tutto il team tramite Slack e nel successivo Project Status Meeting, e si assegna un Responsible per l'implementazione. Il quinto e ultimo step è il tracking: ogni Change Request viene tracciato su Confluence in un Change Log con status che evolve da Submitted a Under Review, poi Approved o Deferred o Rejected, e infine Implemented o Closed. Questo approccio strutturato garantisce che ogni modifica sia valutata oggettivamente e che le decisioni siano prese con piena consapevolezza delle conseguenze sul triangolo scope-time-budget.

---

### 7. Communication

Per la comunicazione del progetto MaraffaOnline si seguono tre regole d'oro. Prima regola: preferire la comunicazione asincrona tramite Slack o email ai meeting, salvo casi di urgenza. Seconda regola: garantire trasparenza totale documentando tutte le decisioni importanti su Confluence che funge da single source of truth. Terza regola: rispettare gli SLA di risposta stabiliti: le richieste urgenti che bloccano il lavoro richiedono risposta entro 2 ore, quelle ad alta priorità che rallentano il lavoro entro 4 ore, le richieste di media priorità entro 1 giorno, e quelle a bassa priorità entro 3 giorni.

Il team utilizza quattro canali Slack dedicati. Il canale general è per comunicazioni generali del team, celebrazioni e messaggi non urgenti. Il canale daily raccoglie gli aggiornamenti del daily standup, sia tramite Slackbot automatizzato che con backup scritto in caso di assenza. Il canale dev è riservato alle discussioni tecniche, alert di code review e notifiche di deploy. Il canale urgent è riservato esclusivamente ai blocker critici e tutti i membri devono leggerlo entro 2 ore. L'etiquette di Slack prevede di usare i thread per discussioni lunghe per evitare spam nel canale principale, di taggare persone solo quando si richiede un'azione diretta specifica, di evitare mention di massa come at-channel o at-here se non in caso di vera urgenza, e di usare emoji reactions per acknowledge rapido: la spunta verde significa "visto e ok", gli occhi significano "sto guardando".

L'email viene utilizzata solo per comunicazioni formali a Giovanni come il monthly cash flow report o le milestone approval, per la submission di Change Request, per contratti e approvazioni legali, e per comunicazioni con enti esterni come Hetzner o fornitori. Ogni email segue un formato standard con subject che include il progetto, una categoria come STATUS_UPDATE o MILESTONE o CHANGE_REQUEST o APPROVAL_NEEDED o RISK_ALERT, e il titolo specifico. Il body include contesto in una frase, situazione dettagliata, azione richiesta se presente, e deadline se applicabile.

Tutta la documentazione importante viene archiviata su Confluence. Questo include tutti gli allegati di Project Management delle fasi Scoping, Planning, Launching, Monitoring e Closing, le note di tutti i meeting come Sprint Review, Retrospective e Status Meeting, le decisioni tecniche importanti documentate come Architecture Decision Records, il Change Request log, e l'Issue log dei problemi ricorrenti. La frequenza di aggiornamento varia: le note dei meeting vengono pubblicate entro fine giornata dello stesso meeting, i status report vengono pubblicati settimanalmente il venerdì dopo il Project Status Meeting, e il change log viene aggiornato in real-time quando un cambiamento viene approvato. Questo sistema di comunicazione garantisce che le informazioni siano sempre accessibili, tracciate e che nulla vada perso nel tempo.

---

## Approvazione e Adozione

Queste **Regole Operative** sono state discusse e approvate durante il **Project Kick-Off Meeting** del 15/10/2025.

**Processo di Adozione**:
1. Tutti i team member hanno letto il documento pre-kickoff
2. Durante kickoff: Q&A e chiarimenti (10 min)
3. Approvazione consensus team interno
4. Approvazione formale Giovanni Marchetti (sponsor)

**Review e Aggiornamento**:
- Regole operative sono **living document** (non statiche)
- Review formale ogni **2 sprint** (monthly) durante retrospective
- Modifiche proposte → discussione team → approvazione Marco (PM)
- Versioning su Confluence (v.1.0.0 → v.1.1.0 se modifiche)

**Commitment**:
> "Noi sottoscritti ci impegniamo a seguire queste regole operative per garantire successo del progetto MaraffaOnline. Eventuali violazioni saranno discusse in retrospective per miglioramento continuo, non per colpevolizzazione."

**Firme** (simboliche):
- Marco Venturi (Project Manager)
- Elena Rossi (Tech Lead)
- Sara Bianchi (Backend Developer)
- Luca Moretti (UX Designer / Frontend Developer)
- Andrea Conti (DevOps Engineer)
- Giovanni Marchetti (Project Sponsor)

---

<!-- Sezione "Fonti e Riferimenti" commentata. NOTA: la sottosezione "RASCI Matrix" sono link a blog esterni; la sottosezione "Regole Operative" cita invece fonti solide del corso (Scrum Guide 2020, PMBOK 7th Edition, Lean/Toyota, Atlassian Team Playbooks) da valorizzare nella relazione. Registro in Relazione/_appunti-per-relazione.md.
## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices di Responsibility Assignment e Team Operating Rules 2026:

**RASCI Matrix**:
- [AIHR - RACI Template & Ultimate 2026 Guide](https://www.aihr.com/blog/raci-template/)
- [TeamGantt - RACI Chart Guide](https://www.teamgantt.com/blog/raci-chart-definition-tips-and-example)
- [Atlassian - RACI Chart](https://www.atlassian.com/work-management/project-management/raci-chart)
- [Project Management - RACI Matrix](https://project-management.com/understanding-responsibility-assignment-matrix-raci-matrix/)

**Regole Operative**:
- Agile Retrospective Best Practices (Scrum Guide 2020)
- Lean Problem Solving (Toyota Production System)
- Conflict Resolution Frameworks (PMI PMBOK 7th Edition)
- Team Working Agreements (Atlassian Team Playbooks)
-->

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 15/10/2025

**Versione**: v.1.0.0
**Prossimo review**: 15/12/2025 (fine Sprint 4, Milestone M2)
