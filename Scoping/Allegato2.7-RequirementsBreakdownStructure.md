# Allegato 2.7 - Requirements Breakdown Structure (RBS)
## v.1.2.0 – 2026-08-23

La **Requirements Breakdown Structure (RBS)** è una decomposizione gerarchica dei requisiti del progetto MaraffaOnline, organizzata per sottosistema. Ogni requisito è classificato secondo le seguenti categorie:

- **F** = Funzionale (cosa il sistema deve fare)
- **NF** = Non Funzionale (qualità, performance, vincoli)
- **C** = Vincolo (constraint tecnico o di business)

I requisiti sono inoltre prioritizzati con il metodo **MoSCoW** (dettagliato in fase di Planning):
- **M** = Must Have (MVP)
- **S** = Should Have
- **C** = Could Have
- **W** = Won't Have (escluso dal MVP)

Ai nodi intermedi la classificazione è indicata solo quando è uniforme per tutti i requisiti figli.

> **Livello di dettaglio.** La RBS si ferma deliberatamente al livello di requisito: dice **cosa** il sistema deve fare, non *come*. Il dettaglio operativo vive nei documenti dedicati: i criteri di accettazione nelle **User Stories (Allegato 2.8)**, le regole di gioco complete nel **documento delle regole ufficiali** validato da Francesca Giuliani, le soglie misurabili nelle **Conditions of Satisfaction (Allegato 2.1)**, le scelte tecnologiche e le priorità consolidate in fase di Planning (**Allegato 3.2 - MoSCoW Analysis**, i cui ID `REQ-*` codificano la numerazione di questo documento).

---

## 1. SOTTOSISTEMA: Game Engine

**Responsabile**: Elena Rossi
**Metodologia**: Waterfall
**Priorità**: MUST HAVE (core del prodotto)

- **1.1 Regole del Gioco** [F, M]
  - **1.1.1 Implementazione Regole Maraffone/Beccaccino** [F, M] — *fonte normativa: documento delle regole ufficiali della community, con validazione formale di Francesca Giuliani*
  - **1.1.2 Gestione Turni e Fasi di Gioco** [F, M]
  - **1.1.3 Validazione Mosse (anti-cheat)** [F, M]
  - **1.1.4 Calcolo Punteggi** [F, M]
  - **1.1.5 Gestione Situazioni Speciali (Maraffa/Cricca)** [F, M]
- **1.2 Intelligenza Artificiale (IA)** [F, W] — *modalità single-player esclusa dall'MVP (focus sul multiplayer online, budget limitato); potenziale feature futura*
- **1.3 Persistenza Stato Partita** [F, M]

---

## 2. SOTTOSISTEMA: Backend Server

**Responsabile**: Sara Bianchi
**Metodologia**: Agile Iterativo
**Priorità**: MUST HAVE

- **2.1 Autenticazione e Gestione Utenti**
  - **2.1.1 Registrazione Utente** [F, M]
  - **2.1.2 Login e Sessioni** [F, M]
  - **2.1.3 Accesso Ospite** [F, M]
  - **2.1.4 Gestione Profilo** [F, S]
  - **2.1.5 Password Recovery** [F, S]
  - **2.1.6 Social Login** [F, W] — *rimandato a v1.1 post-lancio*
- **2.2 Gestione Partite** [F, M]
  - **2.2.1 Creazione Stanza** [F, M]
  - **2.2.2 Join Stanza** [F, M]
  - **2.2.3 Gestione Lobby Partita** [F, M]
  - **2.2.4 Persistenza Dati Partita** [F, M]
- **2.3 Sistema Amicizie** [F, S]
  - **2.3.1 Aggiunta Amici** [F, S]
  - **2.3.2 Lista Amici** [F, S]
  - **2.3.3 Invito Diretto** [F, S]
- **2.4 Statistiche Utente**
  - **2.4.1 Statistiche Base** [F, M]
  - **2.4.2 Statistiche Avanzate** [F, C]
- **2.5 API RESTful** [NF, M]
  - **2.5.1 Endpoints Standard** [NF, M]
  - **2.5.2 Performance API (risposta < 200ms)** [NF, M]
  - **2.5.3 Sicurezza** [NF, M]

---

## 3. SOTTOSISTEMA: Real-Time Communication

**Responsabile**: Elena Rossi + Sara Bianchi
**Metodologia**: Agile Adattivo
**Priorità**: MUST HAVE (core critico)

- **3.1 Connessione WebSocket**
  - **3.1.1 Gestione Connessioni (100 partite simultanee, latenza ≤ 500ms)** [NF, M]
  - **3.1.2 Autenticazione WebSocket** [F, M]
- **3.2 Sincronizzazione Stato Partita**
  - **3.2.1 Eventi di Gioco in Tempo Reale** [F, M] — *architettura server-authoritative: il server è l'unica fonte di verità sullo stato di gioco*
  - **3.2.2 Broadcast Selettivo** [F, M]
  - **3.2.3 Gestione Latency** [NF, M]
- **3.3 Gestione Disconnessioni** [F, M]
  - **3.3.1 Disconnessione Temporanea (sospensione max 5 minuti, ripristino dello stato)** [F, M]
  - **3.3.2 Disconnessione Permanente (oltre 5 minuti: partita annullata)** [F, M]
- **3.4 Chat in Tempo Reale**
  - **3.4.1 Chat In-Game** [F, M]
  - **3.4.2 Chat Globale (lobby)** [F, C]
  - **3.4.3 Emoji/Reactions** [F, W]

---

## 4. SOTTOSISTEMA: Frontend Web

**Responsabile**: Luca Moretti
**Metodologia**: Agile Iterativo
**Priorità**: MUST HAVE

- **4.1 Interfaccia Utente**
  - **4.1.1 Implementazione Mockup Approvati** [F, M] — *riferimento visivo vincolante: mockup v2 dell'Allegato 2.6 - Prototyping*
  - **4.1.2 Design System** [NF, M]
- **4.2 Responsive Design** [NF, M]
  - **4.2.1 Supporto Multi-Device (desktop, tablet, mobile; Chrome, Firefox, Safari, Edge)** [NF, M]
  - **4.2.2 Mobile-First Approach** [NF, M]
- **4.3 Accessibilità**
  - **4.3.1 Conformità WCAG 2.1 AA** [NF, S]
  - **4.3.2 Modalità Daltonici** [NF, C]
- **4.4 Performance Frontend**
  - **4.4.1 Ottimizzazione Caricamento (First Contentful Paint < 2s)** [NF, M]
  - **4.4.2 Bundle Size (< 500KB)** [NF, S]
- **4.5 Animazioni e Feedback Visivo** [NF, S]
  - **4.5.1 Microinterazioni** [NF, S]

---

## 5. SOTTOSISTEMA: Mobile Application

**Responsabile**: TBD (da definire)
**Metodologia**: Incrementale
**Priorità**: WON'T HAVE (MVP)

- **5.1 App Nativa iOS/Android** [F, W] — *esclusa dall'MVP (budget e tempo limitati); alternativa MVP: web app responsive utilizzabile da mobile browser; sviluppo pianificabile post-lancio*
- **5.2 Progressive Web App (PWA)** [F, W] — *valutata come Could in fase di analisi, esclusa dall'MVP in fase di planning; rivalutabile in v1.1*

---

## 6. SOTTOSISTEMA: Social & Community Features

**Responsabile**: Sara Bianchi + Luca Moretti
**Metodologia**: Incrementale
**Priorità**: MIXED (alcune Must, altre Should/Could)

- **6.1 Sistema Amicizie** [F, S] — *vedi sezione 2.3 (Backend Server)*
- **6.2 Chat** — *vedi sezione 3.4 (Real-Time Communication): in-game Must, globale Could*
- **6.3 Classifiche e Leaderboard** [F, C]
  - **6.3.1 Classifica Globale** [F, C]
  - **6.3.2 Classifica Amici** [F, C]
- **6.4 Notifiche**
  - **6.4.1 Notifiche In-App** [F, M]
  - **6.4.2 Notifiche Push** [F, W]
- **6.5 Profili Pubblici** [F, S]
  - **6.5.1 Pagina Profilo Utente** [F, S]

---

## 7. SOTTOSISTEMA: Infrastructure & DevOps

**Responsabile**: Andrea Conti
**Metodologia**: Incrementale
**Priorità**: MUST HAVE (supporto a tutti i sottosistemi)

- **7.1 Hosting e Deployment** [NF, M]
  - **7.1.1 Server Dedicato** [NF, M]
  - **7.1.2 Containerizzazione** [NF, M]
  - **7.1.3 CI/CD Pipeline** [NF, M]
- **7.2 Database**
  - **7.2.1 PostgreSQL** [NF, M]
  - **7.2.2 Redis (cache)** [NF, S]
- **7.3 Monitoring e Logging**
  - **7.3.1 Logging** [NF, M]
  - **7.3.2 Monitoring Performance (uptime ≥ 99% mensile)** [NF, M]
  - **7.3.3 Error Tracking** [NF, S]
- **7.4 Sicurezza**
  - **7.4.1 SSL/TLS** [NF, M]
  - **7.4.2 Firewall e DDoS Protection** [NF, S]
  - **7.4.3 Backup e Disaster Recovery (RTO < 4 ore)** [NF, M]
- **7.5 Scalabilità** [NF, S]
  - **7.5.1 Architettura Preparata per Scalabilità** [NF, S]

---

## Riepilogo Priorità MoSCoW

### MUST HAVE (MVP - Lancio 15/05/2026)
- Game Engine completo
- Backend Server (auth, partite, API)
- Real-Time Communication (WebSocket, sincronizzazione)
- Frontend Web responsive
- Chat in-game
- Infrastructure base (hosting, database, CI/CD)

### SHOULD HAVE (Importante ma non critico)
- Sistema amicizie
- Profili utente personalizzabili
- Accessibilità WCAG AA
- Monitoring avanzato

### COULD HAVE (Desiderabile)
- Chat globale
- Classifiche/Leaderboard
- Modalità daltonici
- Statistiche avanzate

### WON'T HAVE (MVP - Pianificato per v1.1+)
- App mobile nativa iOS/Android
- Social login (Google/Facebook)
- Modalità single-player vs IA
- Notifiche push
- Emoji/reactions
- Tornei strutturati

---

## Tracciabilità Requisiti

Ogni requisito sarà tracciato attraverso:
- **ID univoco**: es. `REQ-GE-1.1.1` (Game Engine, sezione 1.1, punto 1)
- **User Story associata**: vedi Allegato 2.8
- **Test case**: definiti in fase di Planning
- **Issue tracking**: board Notion con label per sottosistema

---

**Redatto da**: Team PlayHeritage Labs (contributi di tutti i membri)
**Coordinato da**: Marco Venturi (Project Manager)
**Revisionato da**: Giovanni Marchetti (Project Sponsor)
**Data approvazione**: 26/09/2025

**Storico revisioni**:
- **v.1.2.0**: Rinumerato da Allegato 2.8 a **Allegato 2.7**: ritirati dagli allegati i verbali ex 2.1 (Project Scoping Meeting) ed ex 2.11 (Approval Process), ora solo narrati nella relazione; numerazione degli allegati di Scoping resa sequenziale (2.1–2.9), come nella relazione di riferimento. Contenuto invariato.
- **v.1.1.0**: Asciugatura al livello di requisito: rimossi i dettagli operativi (criteri di accettazione, soglie implementative, scelte tecnologiche), che appartengono alle User Stories (2.9), al documento delle regole ufficiali, alla CoS (2.2) e al Planning (3.x); invariati numerazione, titoli e classificazioni, a cui restano agganciati gli ID `REQ-*` della MoSCoW (3.2). Corretto il tag di 1.2 (IA) da [F, C] a [F, W], in coerenza con il riepilogo e con REQ-GE-1.2; i nodi intermedi con figli a classificazione mista non portano più un tag proprio.
- **v.1.0.0**: Prima stesura.
