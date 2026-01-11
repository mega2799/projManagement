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

### 1. Problem Solving Strategy

**Processo in 5 Step** (adattato da Agile Retrospective + Lean Problem Solving):

#### Step 1: Identify (Identificare il problema)
- **Chi**: Chiunque nel team può sollevare un problema
- **Dove**: Daily Standup, Slack #urgent, Project Status Meeting
- **Come**: Descrivere il problema con formato **"What? Where? When? Impact?"**

**Esempio**:
> "**What**: Latenza WebSocket superiore a 500ms. **Where**: Server staging. **When**: Da ieri sera dopo deploy. **Impact**: User experience degradata, gioco ingiocabile."

#### Step 2: Analyze (Analizzare la causa root)
- **Chi**: Responsible + Accountable + eventuali Consulted
- **Strumento**: **5 Whys** o **Fishbone Diagram** (Ishikawa)
- **Tempo**: Max 30 minuti di analisi (se serve più tempo, escalation a Tech Lead)

**5 Whys Example**:
1. Perché latenza è alta? → Server sovraccarico
2. Perché server è sovraccarico? → Troppi log in console
3. Perché troppi log? → Logger in modalità DEBUG in staging
4. Perché DEBUG in staging? → Manca env variable LOG_LEVEL
5. Perché manca? → Non documentato in deployment checklist

**Root Cause**: Deployment checklist incompleto

#### Step 3: Propose Solutions (Proporre soluzioni)
- **Chi**: Team brainstorming (vedi sezione Brainstorming)
- **Output**: 2-3 soluzioni alternative con pro/cons
- **Criterio**: Prioritizzare soluzioni rapide (<1 giorno) se impact è alto

**Esempio Soluzioni**:
- **A**: Aggiungere LOG_LEVEL=INFO in .env staging (10 min, fix immediato)
- **B**: Creare script di verifica env vars pre-deploy (1 giorno, previene future occorrenze)
- **C**: Upgrade server Hetzner a tier superiore (€100/mese extra, overkill)

**Decisione**: Implementare A subito + B come follow-up

#### Step 4: Implement (Implementare)
- **Chi**: Responsible assegnato (da RASCI o meeting decisionale)
- **Tracking**: Action item su Notion Database con deadline
- **Comunicazione**: Update su Slack quando completato

#### Step 5: Verify (Verificare efficacia)
- **Chi**: Accountable verifica che problema sia risolto
- **Quando**: Entro 24-48h dall'implementazione
- **Se non risolto**: Tornare a Step 2 (Analyze) con nuove informazioni

**Retrospective**: Tutti i problemi critici vengono discussi in Sprint Retrospective per prevenzione futura.

---

### 2. Decision Making Process

**Framework a 3 Livelli** (già definito nel Kick-Off Meeting):

#### Livello 1: Decisioni Operative (Quotidiane)
- **Scope**: Implementazione tecnica, naming, scelta librerie minori, fix bug
- **Decision Maker**: **Responsible** (developer che lavora sul task)
- **Consulenza**: Opzionale (pair programming, code review)
- **Timeline**: Immediata

**Esempio**: "Uso react-dnd o dnd-kit per drag & drop?" → Luca decide dopo test entrambe le librerie (2h POC)

#### Livello 2: Decisioni Tattiche (Settimanali)
- **Scope**: Architettura, API design, database schema, sprint backlog adjustment
- **Decision Maker**: **Tech Lead (Elena)** + **PM (Marco)** consensus
- **Consulenza**: Team input durante Sprint Planning o Status Meeting
- **Timeline**: Entro 48h da identificazione necessità decisione

**Esempio**: "Cambiamo da REST a GraphQL per API lobby?" → Elena + Marco valutano trade-off → Decisione: NO (troppo refactoring, benefici marginali nel MVP)

**Processo**:
1. Elena presenta opzioni tecniche (pro/cons)
2. Marco valuta impatto su timeline/budget/scope
3. Consultazione team (15 min in meeting)
4. Elena decide aspetto tecnico, Marco aspetto PM
5. Documentazione decisione su Confluence

#### Livello 3: Decisioni Strategiche (Mensili o On-Demand)
- **Scope**: Scope change, budget adjustment, timeline extension, metodologia shift
- **Decision Maker**: **Sponsor (Giovanni)** con input da **PM (Marco)** + **Tech Lead (Elena)**
- **Consulenza**: Tutta il team + Francesca (se impatta regole gioco)
- **Timeline**: Entro 1 settimana (urgenza permitting)

**Esempio**: "Cliente richiede mobile app nativa in MVP. Accettiamo?"
1. Marco prepara **Project Impact Statement** (vedi sezione 5, Change Management)
2. Elena stima effort: +80 giorni, +€10.000
3. Presentazione a Giovanni: opzioni (A) Accept + extend timeline, (B) Postpone to v1.1, (C) Reject
4. Giovanni decide: **(B) Postpone to v1.1** (MVP web only, mobile post-lancio)

**Regola d'Oro**: "Decide at the lowest level possible, escalate only when necessary."

---

### 3. Conflict Resolution Protocol

I conflitti sono naturali in progetti complessi. Il nostro protocollo garantisce risoluzione rapida ed equa.

#### Tipologie di Conflitto

**A. Conflitti Tecnici** (es. "Usiamo MongoDB o PostgreSQL?")
- **Resolver**: Tech Lead (Elena)
- **Input**: Entrambe le parti presentano argomenti (15 min ciascuno)
- **Decisione**: Elena decide basandosi su: performance, scalabilità, team expertise, time-to-market
- **Finale**: "Disagree and commit" - team si allinea anche se non tutti d'accordo

**B. Conflitti di Priorità** (es. "Implemento feature X o Y prima?")
- **Resolver**: PM (Marco) o Product Owner surrogate
- **Input**: Valutazione business value vs effort (MoSCoW matrix)
- **Decisione**: Marco decide basandosi su critical path + stakeholder value
- **Finale**: Task prioritizzato torna in Sprint Backlog

**C. Conflitti Interpersonali** (es. "X non rispetta i miei orari di lavoro")
- **Resolver**: PM (Marco) come facilitatore neutrale
- **Processo**: "Speak Truth to Power" conversation privata 1-on-1
- **Obiettivo**: Win-win solution, non imposizione
- **Escalation**: Se non risolto, escalation a HR PlayHeritage Labs (fuori scope progetto)

#### Processo di Risoluzione in 3 Fasi

**Fase 1: Direct Discussion (24h)**
- Le parti coinvolte parlano direttamente, senza intermediari
- Setting: privato (Zoom 1-on-1 o in presenza)
- Obiettivo: 80% dei conflitti si risolvono qui

**Fase 2: Facilitated Mediation (48h)**
- Marco (PM) o Elena (Tech Lead) facilita discussione
- Setting: meeting strutturato 30 min
- Formato:
  1. Parte A espone posizione (5 min)
  2. Parte B espone posizione (5 min)
  3. Identificazione interessi comuni (5 min)
  4. Brainstorming soluzioni (10 min)
  5. Decisione facilitatore (5 min)

**Fase 3: Executive Decision (72h)**
- Se Fase 2 fallisce, escalation a decisore finale:
  - Conflitto tecnico → Elena (Tech Lead)
  - Conflitto scope/priorità → Giovanni (Sponsor)
  - Conflitto interpersonale → HR
- Decisione è **finale e non appellabile**
- Team si allinea ("disagree and commit")

**Documentazione**: Conflitti di livello 2-3 vengono documentati su Confluence (Issue Log) per retrospective.

---

### 4. Brainstorming Sessions

Il brainstorming è usato per problem solving creativo, design thinking e generazione idee per feature.

#### Quando Usare Brainstorming

- Progettazione nuove feature complesse (es. "Come visualizzare Maraffa/Cricca bonus?")
- Problem solving per issue senza soluzione ovvia
- Sprint Retrospective (cosa migliorare)
- Design thinking per UX miglioramenti

#### Formato Sessione (30-45 minuti)

**Pre-Brainstorming** (1 giorno prima):
- Marco o Elena convoca meeting
- Condivide topic + contesto + obiettivo
- Partecipanti riflettono in anticipo (no preparazione richiesta, ma consigliata)

**Durante la Sessione**:

**1. Warm-up** (5 min)
- Icebreaker per stimolare creatività
- Esempio: "Descrivete Maraffa in 3 parole non tecniche"

**2. Divergent Thinking** (15 min) - Generare idee
- **Regole**:
  - No criticism (nessuna idea è stupida)
  - Quantity over quality (più idee = meglio)
  - Build on others' ideas ("Yes, and..." invece di "Yes, but...")
  - Wild ideas welcome
- **Facilitatore** (Marco): Time-keep + incoraggia silenti a partecipare
- **Scribe** (Andrea o Luca): Annota tutte le idee su whiteboard/Miro

**3. Convergent Thinking** (15 min) - Valutare e selezionare
- Raggruppare idee simili (affinity mapping)
- Votazione: ogni partecipante ha 3 voti (dot voting)
- Identificare top 3 idee

**4. Action Plan** (10 min) - Trasformare in azioni
- Top 3 idee → assegnare owner (Responsible)
- Definire next step (POC, spike, research, implementation)
- Deadline next step

**Post-Brainstorming**:
- Scribe pubblica note su Confluence entro EOD
- Action item aggiunti a Notion Database

#### Tecniche di Brainstorming

**Tecnica 1: Round Robin**
- Giro di tavolo: ognuno propone 1 idea a turno
- Utile per coinvolgere introversi

**Tecnica 2: Brainwriting (6-3-5)**
- 6 persone, 3 idee ciascuno, 5 minuti
- Passano foglio al vicino → leggono idee altrui → aggiungono 3 varianti
- Risultato: 108 idee in 30 minuti

**Tecnica 3: Crazy 8s** (per UI/UX)
- 8 minuti, 8 sketch rapidi di soluzioni
- Utile per Luca (Designer) quando progetta interfacce

---

### 5. Team Meetings Management

Gestiamo 5 tipologie di meeting ricorrenti + meeting ad-hoc. Ogni meeting ha regole chiare per efficienza.

#### Meeting Tipologia 1: Daily Standup

**Frequenza**: Ogni giorno lavorativo, 09:00-09:15 (15 min esatti)
**Partecipanti**: Team interno (MV, ER, SB, LM, AC)
**Format**: In piedi (standing) per mantenere brevità, Zoom se qualcuno remoto

**Struttura** (3 domande per persona, max 2 min/persona):
1. **Cosa ho fatto ieri?** (focus su task completati)
2. **Cosa farò oggi?** (commitment specifico)
3. **Ho blocker?** (impedimenti che richiedono aiuto)

**Regole**:
- No problem solving durante standup (parcheggiare e risolvere dopo)
- No status report prolungati (dettagli in Project Status Meeting)
- Inizia puntuale alle 09:00 (chi arriva tardi perde il turno)
- Facilitatore (Marco): time-keep + nota blocker per follow-up

**Output**:
- Blocker list → risoluzione immediata post-standup (Responsible + Accountable)
- Update Notion Database task status

**Esempio Standup Update** (Sara):
> "Ieri: completato API creazione lobby, test coverage 95%. Oggi: inizio API join lobby, stimo 4h. Blocker: nessuno."

#### Meeting Tipologia 2: Sprint Planning

**Frequenza**: Primo lunedì di ogni sprint (ogni 2 settimane), 09:00-10:30 (1.5h)
**Partecipanti**: Team interno + Giovanni (opzionale, se vuole input su priorità)

**Obiettivo**: Selezionare user stories dal Product Backlog per il prossimo sprint

**Agenda**:
1. **Sprint Goal Definition** (10 min) - Marco + Elena
   - Esempio Sprint 3: "Completare Backend Auth + POC Socket.IO"

2. **Backlog Review** (15 min) - Marco
   - Top user stories dal Product Backlog (già prioritizzate MoSCoW)
   - Lettura acceptance criteria

3. **Story Estimation** (30 min) - Team
   - Planning Poker per user stories non stimate
   - Fibonacci: 1, 2, 3, 5, 8, 13, 21 story points

4. **Sprint Backlog Selection** (20 min) - Marco + Elena
   - Commitment: 40 story points (velocity storica)
   - Verificare che sprint goal sia achievable

5. **Task Breakdown** (15 min) - Team
   - Ogni user story → task tecnici (< 1 giorno)
   - Assegnazione Responsible (volontari prima, assegnazione dopo)

6. **Sprint Risks Review** (10 min) - Marco
   - Rischi specifici dello sprint (es. dipendenze esterne, assenze)

**Output**:
- Sprint Backlog definito su Notion Database
- Sprint Goal pubblicato su Confluence + Slack

#### Meeting Tipologia 3: Sprint Review

**Frequenza**: Ultimo venerdì di ogni sprint, 14:00-15:00 (1h)
**Partecipanti**: Team interno + Giovanni (mandatory) + Francesca (se demo regole gioco)

**Obiettivo**: Demo increment + feedback stakeholder

**Agenda**:
1. **Sprint Recap** (5 min) - Marco
   - Sprint goal, story points committed vs completati
   - Velocity trend

2. **Demo Increment** (30 min) - Developer che ha implementato
   - Live demo di feature completate ("Definition of Done")
   - Esempio Sprint 4: Sara mostra API lobby funzionanti (Postman demo)

3. **Feedback Stakeholder** (15 min) - Giovanni + Francesca
   - Commenti, domande, suggerimenti
   - Acceptance: Giovanni approva o richiede modifiche

4. **Product Backlog Adjustment** (10 min) - Marco
   - Re-prioritizzazione basata su feedback
   - Nuove user stories identificate

**Regole**:
- Demo SOLO feature "Done" (no WIP)
- No slides, only working software (o mockup Figma per UI)
- Giovanni può richiedere change (→ Change Request Process se impatta scope)

**Output**:
- Acceptance/Rejection di deliverable sprint
- Updated Product Backlog

#### Meeting Tipologia 4: Sprint Retrospective

**Frequenza**: Ultimo venerdì di ogni sprint, 15:00-16:00 (1h)
**Partecipanti**: Team interno SOLO (no Giovanni, no Francesca) - safe space

**Obiettivo**: Continuous improvement - cosa migliorare nel processo

**Agenda** (formato "Start/Stop/Continue"):
1. **Warm-up** (5 min) - Icebreaker
   - Esempio: "Rate your sprint energy: 1-10"

2. **Individual Reflection** (10 min) - Silenzio
   - Ognuno scrive post-it (fisici o Miro digitali):
     - **Start**: Cosa dovremmo iniziare a fare?
     - **Stop**: Cosa dovremmo smettere di fare?
     - **Continue**: Cosa funziona e dobbiamo mantenere?

3. **Sharing & Grouping** (15 min) - Team
   - Ognuno presenta i propri post-it (1 min/persona)
   - Facilitatore (Marco) raggruppa per temi

4. **Prioritization** (10 min) - Team
   - Dot voting: ognuno vota top 3 issues da risolvere
   - Identificare top 2 action items per prossimo sprint

5. **Action Plan** (15 min) - Team
   - Definire azioni concrete per top 2 issues
   - Assegnare owner (Responsible)
   - Esempio Action Item: "Andrea crea template PR checklist su GitLab (Owner: AC, Deadline: fine settimana)"

6. **Retrospective of Retrospective** (5 min) - Team
   - Meta-feedback: come migliorare la retrospettiva stessa?

**Output**:
- 2 action items per miglioramento processo
- Note pubblicate su Confluence (accessibili solo team interno)

**Regola "Vegas Rule"**: What happens in retrospective, stays in retrospective (no escalation a Giovanni se qualcuno critica processo, a meno di issue gravi tipo harassment)

#### Meeting Tipologia 5: Project Status Meeting (Weekly)

**Frequenza**: Ogni venerdì, 16:00-17:00 (1h)
**Partecipanti**: Marco (presenter) + Giovanni (mandatory) + Elena (co-presenter) + altri se richiesti

**Obiettivo**: Update esecutivo su salute progetto (scope, time, budget, quality, risks)

**Agenda**:
1. **Executive Summary** (5 min) - Marco
   - Overall project status: Green/Yellow/Red (stoplight)
   - Sprint corrente + progress verso milestone

2. **Scope Status** (10 min) - Marco
   - Feature completate vs pianificate
   - Change requests ricevute (se any)

3. **Schedule Status** (10 min) - Marco
   - Gantt progress: % complete su critical path
   - Milestone forecast (on time / at risk / delayed)
   - Ritardi e recovery plan

4. **Budget Status** (10 min) - Marco
   - Cash flow: spese correnti vs pianificate
   - Burn rate mensile
   - Proiezione surplus/deficit fine progetto

5. **Quality & Risks** (10 min) - Elena
   - Bugs aperti/chiusi (trend)
   - Test coverage (%)
   - Top 3 rischi attuali + mitigation status

6. **Decisions Needed** (10 min) - Marco + Giovanni
   - Item che richiedono decisione sponsor
   - Escalation conflict/issue se necessario

7. **Q&A** (5 min) - Giovanni

**Output**:
- **Stoplight Report** pubblicato su Confluence
- Decisioni Giovanni documentate (approvazioni, rejection, defer)

**Format Report**:
| Area | Status | Notes |
|------|--------|-------|
| Scope | 🟢 Green | Tutte feature Must Have on track |
| Schedule | 🟡 Yellow | Frontend Tavolo da Gioco 3 giorni indietro, recuperabile |
| Budget | 🟢 Green | Speso €8.200/€8.650 Mese 1 (sotto budget) |
| Quality | 🟢 Green | Test coverage 87%, bug critici 0 |
| Risks | 🟡 Yellow | Rischio latenza WebSocket in monitoring |

#### Meeting Ad-Hoc

**Trigger**: Urgency (blocker critico, escalation, decisione strategica)
**Convocazione**: Marco (PM) o Elena (Tech Lead)
**Timeline**: Entro 24h da identificazione urgenza
**Durata**: Max 30 min (focus ristretto)

**Esempio**: "Hetzner server down per manutenzione non pianificata → Meeting emergenza per disaster recovery plan"

---

### 6. Change Management Process

I **Change Request** sono richieste di modifica a scope, timeline o budget già approvati. Richiedono gestione formale per evitare scope creep.

#### Quando Si Attiva Change Request

**Trigger**:
- Stakeholder richiede nuova feature non nel POS
- Stakeholder richiede modifica feature già approvata (oltre bug fix)
- Team identifica impossibilità tecnica che richiede scope adjustment
- Evento esterno impatta progetto (es. cambio regolamento Maraffa ufficiale)

**Esempio Change Request**:
> "Giovanni richiede integrazione con Facebook per condivisione risultati partite."

#### Processo Change Request in 5 Step

**Step 1: Submission (Chi: Richiedente)**
- Compilare **Change Request Form** (template su Confluence)
- Campi richiesti:
  - Titolo change
  - Descrizione dettagliata
  - Motivazione business (perché è importante)
  - Priorità percepita (Low/Medium/High/Critical)

**Step 2: Impact Analysis (Chi: PM + Tech Lead, Tempo: 2-3 giorni)**
- Marco + Elena analizzano impatto su:
  - **Scope**: quali feature aggiunte/modificate/rimosse
  - **Time**: giorni aggiuntivi, impatto critical path
  - **Budget**: costi extra (team, tools, licenze)
  - **Quality**: impatto su test, rischi aggiuntivi
  - **Resources**: serve expertise esterna?

**Output**: **Project Impact Statement** (template):

```markdown
## Project Impact Statement - Change Request #12

**Change**: Integrazione Facebook condivisione risultati

**Impact Analysis**:
- **Scope**: +1 feature (Social Sharing), dipendenza Facebook SDK
- **Time**: +8 giorni (implementazione 5gg + test 3gg)
- **Budget**: +€150 (nessun costo SDK, solo effort team)
- **Quality**: Rischio: Facebook API deprecation, richiede monitoring
- **Resources**: Sara (5gg) + Luca (3gg)

**Opzioni**:
A. Accept → Estendere timeline 8 giorni (nuovo lancio 23/03/2026)
B. Defer → Implementare in v1.1 post-lancio
C. Reject → Non implementare (bassa priorità per MVP)

**Raccomandazione PM**: Opzione B (Defer to v1.1)
- Motivazione: MVP già completo senza social sharing, feature nice-to-have non Must Have
- Beneficio: Manteniamo timeline 15/03/2026
```

**Step 3: Decision (Chi: Sponsor, Tempo: 1 settimana)**
- Marco presenta Project Impact Statement a Giovanni
- Giovanni decide: Accept / Defer / Reject
- Se Accept → rinegoziare contratto se impatta budget/timeline (clausola contrattuale)

**Step 4: Implementation (Se Accept)**
- Aggiornare POS, WBS, Gantt, Product Backlog
- Comunicare change a tutto il team (Slack + Project Status Meeting)
- Assegnare Responsible per implementazione

**Step 5: Tracking**
- Change Request tracciato su Confluence (Change Log)
- Status: Submitted → Under Review → Approved/Deferred/Rejected → Implemented/Closed

---

### 7. Communication Protocols

**Golden Rules**:
1. **Asynchronous First**: Preferire Slack/email a meeting, salvo urgency
2. **Transparency**: Tutte le decisioni su Confluence (single source of truth)
3. **Response SLA**:
   - 🔴 Urgent (blocker): < 2h
   - 🟠 High (rallenta lavoro): < 4h
   - 🟡 Medium: < 1 giorno
   - 🟢 Low: < 3 giorni

#### Slack Channels

- **#general**: Comunicazioni generali team, celebrazioni, non-urgent
- **#daily**: Standup updates (automatizzato Slackbot + backup scritto se assenza)
- **#dev**: Discussioni tecniche, code review alerts, deploy notifications
- **#urgent**: Solo per blocker critici (tutti devono leggere entro 2h)

**Slack Etiquette**:
- Usare thread per discussioni lunghe (no spam channel principale)
- Taggare persone solo se richiesta azione diretta (@sara @luca)
- No @channel/@here se non urgency vera
- Usare emoji reactions per acknowledge (✅ = "visto e ok", 👀 = "sto guardando")

#### Email

**Quando usare email** (invece di Slack):
- Comunicazioni formali a Giovanni (monthly cash flow report, milestone approval)
- Change Request submission
- Contratti, approvazioni legali
- Comunicazioni esterne (Hetzner, fornitori)

**Email Standard Format**:
```
Subject: [MaraffaOnline] [Categoria] Titolo

Categoria = {STATUS_UPDATE, MILESTONE, CHANGE_REQUEST, APPROVAL_NEEDED, RISK_ALERT}

Body:
- Context (1 frase)
- Situation (dettagli)
- Action needed (se any)
- Deadline (se any)
```

#### Confluence Documentation

**Cosa documentare su Confluence**:
- Tutti gli allegati PM (Scoping, Planning, Launching, Monitoring, Closing)
- Meeting notes (Sprint Review, Retrospective, Status Meeting)
- Decisioni tecniche importanti (Architecture Decision Records - ADR)
- Change Request log
- Issue log (problemi ricorrenti)

**Update Frequency**:
- Meeting notes: entro EOD stesso giorno meeting
- Status reports: weekly (venerdì post-Status Meeting)
- Change log: real-time (quando cambiamento approvato)

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

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 15/10/2025

**Versione**: v.1.0.0
**Prossimo review**: 15/12/2025 (fine Sprint 4, Milestone M2)
