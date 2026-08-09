# Allegato 4.2 - RASCI Matrix e Regole Operative
## v.1.4.0 – 2026-08-02 11:00

> La RASCI Matrix è disponibile anche come companion visivo `Allegato4.2-RASCI.html` (matrice colorata task × ruoli, con legenda R/A/S/C/I): apri il file nel browser e usa "Stampa → Salva come PDF". Questo documento `.md` resta il registro completo (matrice dettagliata per sottosistema, Regole Operative e analisi).

Questo documento definisce le **responsabilità del team** attraverso la RASCI Matrix e le **regole operative** per garantire una collaborazione efficace durante l'intero ciclo di vita del progetto MaraffaOnline.

---

## Parte 1: RASCI Matrix

### Cos'è la RASCI Matrix

La **RASCI Matrix** (Responsibility Assignment Matrix) chiarisce chi fa cosa in ogni attività del progetto, riducendo le ambiguità e garantendo l'accountability.

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
- **Elena Rossi (ER)**: Tech Lead / Game Engine Specialist
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
| **Definizione struttura dati carte** | I | C | I | A/R | S | - | - |
| **Implementazione mazzo 40 carte** | I | C | I | A/R | S | - | - |
| **Algoritmo distribuzione 2×5** | I | C | I | A/R | S | - | - |
| **Codifica ordine forza carte** | I | C | I | A/R | S | - | - |
| **Implementazione regole presa (maggiore vince)** | I | C | I | A/R | S | - | - |
| **Logica briscola (determinazione e priorità)** | I | C | I | A/R | S | - | - |
| **Sistema turni 4 giocatori** | I | C | I | A/R | S | - | - |
| **Gestione chi inizia (4 di denari)** | I | C | I | A/R | S | - | - |
| **Calcolo punteggio fine presa** | I | C | I | A/R | S | - | - |
| **Tracciamento punteggio smazzata (11pt interi dopo arrotondamento)** | I | C | I | A/R | S | - | - |
| **Condizione vittoria (41pt + figura)** | I | C | I | A/R | S | - | - |
| **Gestione Maraffa/Cricca (A+2+3 briscola = +3pt)** | I | C | I | A/R | S | - | - |
| **Validazione mosse legali** | I | C | I | A/R | S | - | - |
| **Detection casi edge (abbandono, timeout)** | I | - | I | A/R | S | - | - |
| **Unit test logica di gioco (>90% coverage)** | I | C | I | A/R | S | - | - |
| **Validazione regole con Francesca (Sessione 1)** | A | R | S | C | C | - | - |

**Accountable e Responsible Principale**: Elena Rossi (Tech Lead / Game Engine Specialist) — sul Game Engine i due ruoli coincidono deliberatamente: è la specialista che implementa il sottosistema (vedi WBS e Gantt) e in un team di cinque la sovrapposizione A/R è accettata, bilanciata dal supporto di Sara, dalla code review e dalla validazione esterna delle regole
**Support**: Sara Bianchi (integrazione con il Backend Server)
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
| **Proof of Concept latency test (<500ms)** | I | - | I | A | R | - | S |
| **WebSocket event: player-join** | I | - | I | A | R | C | - |
| **WebSocket event: card-played** | I | - | I | A | R | C | - |
| **WebSocket event: turn-change** | I | - | I | A | R | C | - |
| **WebSocket event: game-state-update** | I | - | I | A | R | C | - |
| **WebSocket event: game-end** | I | - | I | A | R | C | - |
| **Sincronizzazione stato 4 client** | I | - | I | A | R | S | - |
| **Gestione disconnessione giocatore** | I | - | I | A | R | - | - |
| **Reconnection handling (heartbeat 30s, sospensione max 5 min)** | I | - | I | A | R | - | - |
| **Chat in-game testuale (throttling 1 msg/s + filtro)** | I | - | I | A | R | C | - |
| **Notifiche real-time eventi partita** | I | - | I | A | R | C | - |
| **Load testing 100 partite simultanee (400 giocatori)** | I | - | I | A | R | - | S |
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
| **Interazione giocata carta (click to play) + animazioni** | I | - | I | A | S | R | - |
| **Animazioni giocata carte** | I | - | I | A | - | R | - |
| **Visualizzazione punteggio real-time** | I | C | I | A | S | R | - |
| **Indicatore turno corrente** | I | - | I | A | - | R | - |
| **Schermata fine partita (vincitore, punteggi)** | C | - | I | A | - | R | - |
| **Profili utente (avatar, statistiche)** | C | - | I | A | - | R | - |
| **Leaderboard community** | C | - | I | A | - | R | - |
| **Sistema notifiche UI (toast)** | I | - | I | A | - | R | - |
| **Responsive design (desktop + tablet)** | C | - | I | A | - | R | - |
| **Accessibilità (WCAG 2.1 AA)** | I | - | I | A | - | R | - |
| **Cross-browser testing (Chrome, Firefox, Safari, Edge)** | I | - | I | A | - | R | S |
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
| **Salvataggio mosse partita per replay (WBS 2.2.3.1)** | C | - | I | A | R | S | - |
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
| **Provisioning server Hetzner** | I | - | I | A | - | - | R |
| **Setup Docker containers (backend, frontend, db)** | I | - | I | A | - | - | R |
| **GitLab repository setup** | I | - | I | A | S | S | R |
| **GitLab CI/CD pipeline (build, test, deploy)** | I | - | I | A | S | S | R |
| **Ambiente staging** | I | - | I | A | - | - | R |
| **Ambiente production** | I | - | I | A | - | - | R |
| **SSL certificato (Let's Encrypt)** | I | - | I | A | - | - | R |
| **DNS setup (maraffaonline.it)** | I | - | I | A | - | - | R |
| **Cloudflare CDN + DDoS protection** | I | - | I | A | - | - | R |
| **Database backup automatico (daily)** | I | - | I | A | - | - | R |
| **Monitoring: Sentry (error tracking)** | I | - | I | A | S | - | R |
| **Monitoring: UptimeRobot (uptime)** | I | - | I | A | - | - | R |
| **Log aggregation (Winston)** | I | - | I | A | S | - | R |
| **Disaster recovery plan** | I | - | A | C | - | - | R |

**Accountable**: Marco Venturi (PM) per disaster recovery, Elena Rossi (Tech Lead) per setup tecnici
**Responsible Principale**: Andrea Conti (DevOps Engineer)
**Consulted**: Elena Rossi (decisioni architetturali)
**Support**: Sara Bianchi (backend integration), Luca Moretti (frontend deployment)

---

## 7. Testing & QA (Continuo)

| Task | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Unit test Game Engine (Jest)** | I | C | I | A/R | S | - | - |
| **Unit test API Backend (Jest)** | I | - | I | A | R | - | - |
| **Unit test componenti Frontend (Vitest)** | I | - | I | A | - | R | - |
| **Integration test end-to-end (Cypress)** | I | - | I | A | S | S | R |
| **Load testing 100 partite simultanee (k6)** | I | - | I | A | S | - | R |
| **Security testing (SQL injection, XSS)** | I | - | I | A | S | - | R |
| **Accessibility testing (WCAG 2.1 AA)** | I | - | I | A | - | R | - |
| **Cross-browser testing (BrowserStack)** | I | - | I | A | - | R | S |
| **User Acceptance Testing: recruitment 10 tester** | A | S | R | C | - | - | - |
| **UAT: preparazione test plan** | A | C | R | S | - | S | - |
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
| **Project Scoping Meeting** | A | C | R | C | C | C | C |
| **Project Planning (WBS, Gantt, Cash Flow)** | A | - | R | C | - | - | - |
| **Project Kick-Off Meeting** | A | I | R | I | I | I | I |
| **Daily Standup facilitation** | - | - | A | S | I | I | I |
| **Sprint Planning** | C | - | A | C | I | I | I |
| **Sprint Review** | A | C | R | R | R | R | R |
| **Sprint Retrospective** | - | - | A | I | I | I | I |
| **Project Status Meeting (weekly)** | A | I | R | C | - | - | - |
| **Cash Flow Tracking (monthly report)** | A | - | R | - | - | - | - |
| **Risk Management (weekly review)** | C | - | A | C | - | - | - |
| **Change Request evaluation** | A | C | R | C | - | - | - |
| **Stakeholder communication** | C | - | A | S | - | - | - |
| **Documentazione Notion** | I | - | A | S | S | S | S |
| **Final Project Report** | A | - | R | C | - | - | - |
| **Lessons Learned session** | A | C | R | C | C | C | C |
| **Project Closure celebration** | A | I | R | I | I | I | I |

**Accountable Principale**: Giovanni Marchetti (Project Sponsor) per approvazioni milestone
**Responsible Principale**: Marco Venturi (Project Manager)
**Support**: Elena Rossi (Tech Lead) per decisioni tecniche

---

## Analisi RASCI: distribuzione delle responsabilità

La matrice concentra la responsabilità esecutiva (R) sugli sviluppatori: Elena sul Game Engine, di cui è la specialista (e dove ricopre anche il ruolo di Accountable, con Sara a supporto per l'integrazione); Sara sul Backend e sul Real-Time; Luca sul Frontend e sulle interfacce social; Andrea sull'infrastruttura, la CI/CD e l'automazione dei test. L'assegnazione rispetta i carichi temporali del Gantt: nessuna persona risulta Responsible di due sottosistemi negli stessi periodi. L'accountability (A) è ripartita per natura dell'attività: a Elena, come Tech Lead, quella tecnica su sviluppo e infrastruttura; a Marco quella sulle cerimonie Agile e sul coordinamento di progetto; a Giovanni, come Sponsor, quella sulle decisioni di business e sulle milestone. Francesca è consultata (C) su tutte le attività legate alle regole del gioco.

---

## Parte 2: Regole Operative

Le **Regole Operative** definiscono i processi per la gestione quotidiana del team e la risoluzione di problemi ricorrenti. Stabiliscono un framework condiviso per decision-making, conflict resolution, brainstorming e meeting management.

---

### 1. Problem Solving

Per il problem solving si è adottato un approccio strutturato in cinque passi, ispirato al Lean Problem Solving e alle pratiche Agile, così che i problemi vengano affrontati in modo sistematico e le soluzioni risultino efficaci e sostenibili.

Il primo passo è l'identificazione chiara del problema: chiunque nel team può sollevarlo, ma deve descriverlo in modo rigoroso (cosa succede, dove, da quando e con quale impatto) affinché tutti lo comprendano. Segue l'analisi della causa root, a cura del Responsible e dell'Accountable dell'area coinvolta, con eventuale supporto dei Consulted secondo la RASCI Matrix; per individuare la vera causa si utilizza la tecnica dei "5 Whys", mantenendo l'analisi rapida e ricorrendo all'escalation alla Tech Lead se si prolunga. Individuata la causa, il team propone soluzioni alternative valutandone pro e contro e privilegiando gli interventi rapidi quando l'impatto è alto; la scelta finale spetta all'Accountable. La soluzione viene quindi assegnata a un Responsible con una deadline chiara e, una volta implementata, l'Accountable ne verifica l'efficacia; se il problema persiste si ritorna all'analisi con le nuove informazioni acquisite.

I problemi critici emersi durante gli sprint vengono ripresi nella Sprint Retrospective per capire come prevenirli in futuro, in un'ottica di miglioramento continuo del processo.

---

### 2. Decision Making

Per il decision making si è adottato un approccio consultivo, via di mezzo tra il metodo direttivo e quello pienamente collaborativo: consente di beneficiare delle diverse prospettive del gruppo mantenendo però una chiara direzione e responsabilità decisionale, coerente con la visione strategica.

Le decisioni sono organizzate su tre livelli. Le decisioni operative (implementazione tecnica quotidiana: naming convention, librerie minori, fix di bug) spettano direttamente al Responsible che lavora sul task, con consulenza opzionale del team tramite pair programming o code review. Le decisioni tattiche (scelte architetturali, design delle API, schema del database, aggiustamenti al backlog) sono prese in consensus dalla Tech Lead Elena Rossi, per l'aspetto tecnico, e dal Project Manager Marco Venturi, per l'impatto su tempi, budget e scope, dopo una breve consultazione del team; vengono documentate e prese in tempi rapidi. Le decisioni strategiche (modifiche a scope, budget, timeline o metodologia) spettano allo Sponsor Giovanni Marchetti, su input di Project Manager e Tech Lead e con il coinvolgimento di Francesca Giuliani quando riguardano le regole del gioco; in questi casi il PM predispone un Project Impact Statement con le opzioni possibili.

La regola d'oro che guida il processo è "decidere al livello più basso possibile, con escalation solo quando necessario": le decisioni vengono così prese rapidamente da chi ha le informazioni più rilevanti, evitando colli di bottiglia e il sovraccarico dei livelli superiori.

---

### 3. Conflict Resolution

Per la risoluzione dei conflitti si è scelto un approccio collaborativo e progressivo, che considera i conflitti come naturali in progetti complessi e li affronta con un protocollo che ne garantisca una gestione rapida ed equa.

Si distinguono tre tipologie di conflitto. I conflitti tecnici (scelte architetturali o tecnologiche) sono risolti dalla Tech Lead Elena Rossi, che ascolta gli argomenti di entrambe le parti e decide su criteri oggettivi quali performance, scalabilità, competenze del team e time-to-market; presa la decisione, il team si allinea secondo il principio "disagree and commit". I conflitti di priorità (quale feature realizzare prima) sono gestiti dal Project Manager Marco Venturi, che valuta il valore di business rispetto all'effort tramite la matrice MoSCoW e decide in base al critical path e al valore per lo stakeholder. I conflitti interpersonali sono affrontati da Marco come facilitatore neutrale, con l'obiettivo di una soluzione win-win e, se irrisolti, con escalation alle risorse umane di PlayHeritage Labs (che esula dallo scope del progetto).

Il processo segue tre fasi progressive: dapprima le parti si confrontano direttamente, senza intermediari e in un setting privato, riuscendo a risolvere alla fonte la maggior parte dei conflitti; se necessario si passa a una mediazione facilitata da Marco o Elena in un incontro strutturato; in ultima istanza si arriva a una decisione esecutiva presa dal decisore appropriato (Elena per i conflitti tecnici, Giovanni per scope e priorità, HR per quelli interpersonali), che è finale e a cui il team deve allinearsi. I conflitti che raggiungono la mediazione o la decisione esecutiva vengono registrati nell'Issue Log e ripresi in retrospective.

---

### 4. Brainstorming

Per il brainstorming le persone coinvolte si riuniscono davanti a una lavagna, fisica o digitale (Miro) quando qualcuno lavora da remoto. È impiegato per il problem solving creativo, il design thinking e la generazione di idee per feature complesse o issue senza soluzioni ovvie, ed è utile anche durante le Sprint Retrospective.

Le sessioni seguono un formato strutturato in due fasi. Nella fase di divergent thinking l'obiettivo è generare il maggior numero possibile di idee: non è ammessa alcuna critica, si privilegia la quantità sulla qualità e si incoraggia a costruire sulle idee altrui ("Yes, and..." invece di "Yes, but..."); un facilitatore modera e stimola la partecipazione anche dei più silenziosi, mentre uno scribe annota tutte le idee su una lavagna. Nella successiva fase di convergent thinking si passa dalla generazione alla valutazione: le idee simili vengono raggruppate (affinity mapping) e, tramite dot voting, si selezionano le più promettenti, per ciascuna delle quali si definisce un owner Responsible, un next step (proof of concept, spike di ricerca o implementazione) e una deadline.

A seconda del contesto il team ricorre a tecniche diverse, come un giro di tavolo per coinvolgere anche i più introversi o brevi sketch a tempo per i problemi di UI/UX. Le idee raccolte vengono infine raffinate per selezionare le soluzioni da sviluppare.

---

### 5. Team Meetings

Sono previste riunioni ricorrenti per garantire coordinamento e allineamento continuo. Il progetto adotta cinque tipologie di meeting, ciascuna con formato e obiettivi specifici, oltre a incontri ad-hoc convocati quando necessario.

Il Daily Standup è il cuore della comunicazione quotidiana del team interno: un incontro breve (15 minuti) in cui ciascuno riferisce cosa ha fatto, cosa farà e quali blocker lo ostacolano. Non è la sede del problem solving, che viene rimandato alle sole persone coinvolte; Marco facilita l'incontro tenendo il tempo e annotando i blocker per il follow-up immediato con Responsible e Accountable.

Lo Sprint Planning si tiene all'inizio di ogni sprint e serve a selezionare le user stories dal Product Backlog: si definisce lo Sprint Goal, si stimano le storie tramite Planning Poker (scala Fibonacci), si compone lo Sprint Backlog in base alla velocity storica e si scompongono le storie in task assegnati ai Responsible. Vi partecipa il team interno, con Giovanni in via opzionale per dare input sulle priorità.

La Sprint Review si tiene a fine sprint alla presenza obbligatoria dello sponsor Giovanni (e di Francesca quando si dimostrano funzionalità legate alle regole del gioco): il team mostra l'increment completato secondo la "Definition of Done" e raccoglie feedback, al termine dei quali Giovanni accetta i deliverable o richiede modifiche (attivando, se sostanziali, il Change Request Process). Si dimostrano solo feature effettivamente "Done", preferendo il software funzionante alle slide.

Subito dopo si tiene la Sprint Retrospective, uno spazio riservato al solo team interno e dedicato al miglioramento continuo: con il formato "Start/Stop/Continue" si individuano, tramite dot voting, i principali action item per lo sprint successivo, ciascuno con owner e deadline. Vale la "Vegas Rule": quanto emerge in retrospective non viene riportato all'esterno, salvo problemi gravi.

Il Project Status Meeting è il punto di controllo settimanale con lo sponsor: Marco presenta lo stato complessivo del progetto con il sistema stoplight (verde/giallo/rosso) su scope, tempi, budget, qualità e rischi, mentre Elena espone la parte tecnica; produce uno Stoplight Report e la documentazione delle decisioni prese da Giovanni.

In caso di urgenza (blocker critico, escalation immediata, decisione strategica non rinviabile) Marco o Elena convocano meeting ad-hoc, brevi e focalizzati sul problema specifico. Sono inoltre previsti review meeting in concomitanza con il raggiungimento di una milestone; quando emergono problemi è preferibile riunire solo le persone coinvolte, anziché l'intero team.

---

### 6. Change Management

Le richieste di modifica a scope, timeline o budget già approvati richiedono una gestione formale, per evitare lo scope creep che può compromettere il successo del progetto. Si è adottato un processo strutturato in cinque passi, che garantisce valutazione oggettiva e trasparenza nelle decisioni.

Un Change Request si attiva quando lo stakeholder richiede una nuova feature non prevista nel Project Overview Statement o modifiche sostanziali a feature già approvate, quando il team individua un'impossibilità tecnica che impone aggiustamenti allo scope, o quando un evento esterno impatta il progetto.

Il processo prevede cinque passi. La submission, con la compilazione di un Change Request Form che riporta descrizione, motivazione di business e priorità percepita. L'impact analysis, condotta da Marco ed Elena, che valuta l'impatto su scope, tempi, budget, qualità e risorse e produce un Project Impact Statement con le opzioni possibili (accettare ed estendere la timeline, differire a una versione successiva o rifiutare) e la raccomandazione motivata del PM. La decisione dello Sponsor, che sceglie se accettare, differire o rifiutare, rinegoziando il contratto quando l'impatto su budget o timeline è significativo. L'implementation, che aggiorna i documenti di progetto (POS, WBS, Gantt, Product Backlog), comunica il change al team e ne assegna la realizzazione a un Responsible. Il tracking, con registrazione di ogni richiesta in un Change Log fino alla chiusura. I sottosistemi Agile accolgono i cambiamenti come parte naturale del processo, mentre per quelli tradizionali ogni modifica è valutata caso per caso, così che ogni decisione sia presa con piena consapevolezza delle conseguenze sul triangolo scope-tempi-budget.

---

### 7. Communication

Per la comunicazione si seguono tre regole d'oro: privilegiare la comunicazione asincrona (Slack ed email) rispetto ai meeting, salvo urgenze; garantire trasparenza documentando le decisioni importanti su Notion, che funge da single source of truth; rispettare gli SLA di risposta commisurati alla priorità, dalle poche ore per le richieste urgenti che bloccano il lavoro fino ad alcuni giorni per quelle a bassa priorità.

Il team utilizza canali Slack dedicati, distinti per comunicazioni generali, aggiornamenti del daily standup, discussioni tecniche e urgenze (queste ultime da leggere entro poche ore). L'etiquette prevede l'uso dei thread per le discussioni lunghe, il tag delle persone solo quando si richiede un'azione specifica, la parsimonia nelle mention di massa e l'uso delle emoji reactions per un acknowledge rapido. L'email è riservata alle comunicazioni formali verso lo sponsor e verso gli enti esterni (report mensili, approvazioni di milestone, submission di Change Request, contratti), e segue un formato standard con subject categorizzato.

Tutta la documentazione rilevante — allegati di Project Management, note dei meeting, decisioni tecniche, Change Log e Issue Log — è archiviata su Notion e aggiornata con regolarità (note dei meeting a fine giornata, status report settimanali, change log in tempo reale), così che le informazioni restino sempre accessibili e tracciate.

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
- Versioning su Notion (v.1.0.0 → v.1.1.0 se modifiche)

**Commitment**: il team si impegna a seguire queste regole operative; eventuali criticità vengono discusse in retrospective in un'ottica di miglioramento continuo, non di colpevolizzazione.

**Firme** (simboliche):
- Marco Venturi (Project Manager)
- Elena Rossi (Tech Lead)
- Sara Bianchi (Backend Developer)
- Luca Moretti (UX Designer / Frontend Developer)
- Andrea Conti (DevOps Engineer)
- Giovanni Marchetti (Project Sponsor)

**Storico revisioni**:
- **v.1.4.0**: revisione di coerenza con WBS/Gantt. Corretta l'inversione dei ruoli sul Game Engine: Responsible è Elena Rossi (Game Engine Specialist, come da Allegato 2.1 e assegnazioni WBS/Gantt), non Sara Bianchi — che negli stessi sprint è già Responsible del Backend; sul Game Engine Elena cumula A/R con Sara a supporto. Ruolo di Elena corretto da "Backend Developer" a "Game Engine Specialist". Load testing allineato al criterio delle Conditions of Satisfaction: 100 partite simultanee (era 50). Cross-browser esteso a Edge (come da CoS) e interazione carta uniformata al Backlog (click to play, non drag & drop).
- **v.1.3.0**: snellimento anti-ridondanza. L'analisi RASCI è stata sintetizzata (rimossi i conteggi esaustivi per persona e la nota "Balanced Workload", sostituiti da una descrizione qualitativa della distribuzione R/A/C); alleggerite l'introduzione teorica e la sezione Brainstorming e ammorbidita la formula di commitment finale. Matrice per sottosistema e regole operative invariate nella sostanza.
- **v.1.2.0**: assegnato un Accountable a tutte le righe della matrice (ogni attività ha ora esattamente un Accountable) e ricalcolati i conteggi di responsabilità; refusi corretti.

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

**Versione**: v.1.4.0
**Prossimo review**: 19/12/2025 (venerdì, fine Sprint 4 — Milestone M2)
