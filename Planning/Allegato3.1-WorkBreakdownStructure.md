# Allegato 3.1 - Work Breakdown Structure (WBS)
## v.1.0.0 – 2025-10-20 10:00:00

La Work Breakdown Structure (WBS) è la scomposizione gerarchica del lavoro necessario per completare il progetto MaraffaOnline. Seguendo il principio della **100% Rule**, la WBS include tutto il lavoro richiesto dal progetto, organizzato per deliverable piuttosto che per fasi.

---

## Struttura Gerarchica

La WBS è organizzata su 4 livelli:
1. **Sottosistema**: macro-aree tecniche del progetto
2. **Funzione**: raggruppamenti logici di attività
3. **Attività**: work package specifici
4. **Task**: unità atomiche di lavoro

---

## 1. Game Engine (Metodologia: Waterfall)

### 1.1 Logica di Gioco Maraffone

#### 1.1.1 Implementazione Regole Base
- **Task 1.1.1.1**: Definire struttura dati per carte (seme, valore, ordine)
- **Task 1.1.1.2**: Implementare mazzo da 40 carte italiane
- **Task 1.1.1.3**: Implementare algoritmo di distribuzione carte (2×5)
- **Task 1.1.1.4**: Codificare ordine di forza carte (3→2→A→Re→Cavallo→Fante→7→6→5→4)

#### 1.1.2 Sistema di Punteggio
- **Task 1.1.2.1**: Implementare calcolo punteggio carte (Asso=1pt, Figure/2/3=1/3pt)
- **Task 1.1.2.2**: Sviluppare arrotondamento per difetto (punti interi)
- **Task 1.1.2.3**: Implementare bonus ultima presa (+1 punto)
- **Task 1.1.2.4**: Calcolare totale mano (max 11 e 2/3 punti)

#### 1.1.3 Meccanica Turni
- **Task 1.1.3.1**: Implementare selezione briscola da chi ha 4 di denari
- **Task 1.1.3.2**: Validare obbligo di rispondere al seme
- **Task 1.1.3.3**: Determinare vincitore presa (briscola vs seme)
- **Task 1.1.3.4**: Gestire rotazione turni (senso antiorario)

#### 1.1.4 Regole Speciali
- **Task 1.1.4.1**: Rilevare Maraffa/Cricca (Asso+2+3 briscola)
- **Task 1.1.4.2**: Validare obbligo gioco Asso se Maraffa
- **Task 1.1.4.3**: Assegnare 3 punti bonus per Maraffa
- **Task 1.1.4.4**: Penalizzare mancato gioco Asso (-3 punti)

#### 1.1.5 Condizioni Vittoria
- **Task 1.1.5.1**: Verificare raggiungimento 41 punti + figura
- **Task 1.1.5.2**: Implementare variante corta (31 punti)
- **Task 1.1.5.3**: Determinare coppia vincitrice
- **Task 1.1.5.4**: Generare riepilogo fine partita

### 1.2 Validazione e Testing

#### 1.2.1 Unit Testing Regole
- **Task 1.2.1.1**: Test punteggio carte (30 test case)
- **Task 1.2.1.2**: Test vincitore presa (briscola/seme)
- **Task 1.2.1.3**: Test Maraffa/Cricca (casi positivi/negativi)
- **Task 1.2.1.4**: Test condizioni vittoria

#### 1.2.2 Integration Testing
- **Task 1.2.2.1**: Test partita completa simulata (4 giocatori bot)
- **Task 1.2.2.2**: Validare coerenza punteggi mano per mano
- **Task 1.2.2.3**: Test edge cases (pareggi, carte finali)

---

## 2. Backend Server (Metodologia: Agile Iterativo)

### 2.1 Autenticazione e Gestione Utenti

#### 2.1.1 Sistema di Autenticazione
- **Task 2.1.1.1**: Implementare registrazione utente (email + password)
- **Task 2.1.1.2**: Sviluppare login con JWT token
- **Task 2.1.1.3**: Implementare "Gioca come ospite" (sessione temporanea)
- **Task 2.1.1.4**: Gestire logout e invalidazione token

#### 2.1.2 Profilo Utente
- **Task 2.1.2.1**: CRUD operazioni profilo (avatar, nickname)
- **Task 2.1.2.2**: Calcolare statistiche utente (partite vinte/perse, win%)
- **Task 2.1.2.3**: Implementare storico partite
- **Task 2.1.2.4**: Gestire preferenze utente (notifiche, privacy)

### 2.2 Gestione Partite

#### 2.2.1 Creazione e Lobby
- **Task 2.2.1.1**: API creazione stanza (pubblica/privata)
- **Task 2.2.1.2**: Gestire password stanze private
- **Task 2.2.1.3**: Implementare sistema di inviti (link condivisibile)
- **Task 2.2.1.4**: Lista stanze disponibili (filtri pubbliche/amici)

#### 2.2.2 Stato Partita
- **Task 2.2.2.1**: Persistere stato partita su database
- **Task 2.2.2.2**: Gestire recupero partita in corso (reconnect)
- **Task 2.2.2.3**: Sincronizzare stato tra 4 giocatori
- **Task 2.2.2.4**: Implementare timeout turno (30 secondi)

#### 2.2.3 Storico e Statistiche
- **Task 2.2.3.1**: Salvare replay partite (mosse + timestamp)
- **Task 2.2.3.2**: Calcolare statistiche aggregate
- **Task 2.2.3.3**: Generare classifiche globali/amici

### 2.3 Database Design

#### 2.3.1 Schema PostgreSQL
- **Task 2.3.1.1**: Progettare schema tabelle (users, matches, moves, friendships)
- **Task 2.3.1.2**: Definire indici per query performance
- **Task 2.3.1.3**: Implementare migrazioni database
- **Task 2.3.1.4**: Configurare backup automatici

#### 2.3.2 Ottimizzazione Query
- **Task 2.3.2.1**: Query profiling per bottleneck
- **Task 2.3.2.2**: Implementare connection pooling
- **Task 2.3.2.3**: Caching query frequenti (Redis)

---

## 3. Real-Time Communication (Metodologia: Agile Adattivo)

### 3.1 WebSocket Server

#### 3.1.1 Setup Socket.IO
- **Task 3.1.1.1**: Configurare Socket.IO server (Node.js)
- **Task 3.1.1.2**: Implementare gestione rooms per partite
- **Task 3.1.1.3**: Autenticazione WebSocket (JWT)
- **Task 3.1.1.4**: Gestire disconnessioni/reconnessioni

#### 3.1.2 Eventi Real-Time
- **Task 3.1.2.1**: Evento "gioca_carta" (broadcast a 4 giocatori)
- **Task 3.1.2.2**: Evento "fine_mano" con punteggi aggiornati
- **Task 3.1.2.3**: Evento "chat_message" (solo stanza attiva)
- **Task 3.1.2.4**: Evento "notifica_turno" (push notification)

### 3.2 Sincronizzazione Stato

#### 3.2.1 Conflict Resolution
- **Task 3.2.1.1**: Validare mosse lato server (anti-cheat)
- **Task 3.2.1.2**: Gestire mosse simultanee (timestamp-based)
- **Task 3.2.1.3**: Implementare rollback per errori sincronizzazione

#### 3.2.2 Latency Management
- **Task 3.2.2.1**: Misurare latency client-server (ping/pong)
- **Task 3.2.2.2**: Indicatori latency UI (verde/giallo/rosso)
- **Task 3.2.2.3**: Compensazione lag per animazioni

---

## 4. Frontend Web (Metodologia: Agile Iterativo)

### 4.1 Interfaccia Utente React

#### 4.1.1 Homepage e Autenticazione
- **Task 4.1.1.1**: Sviluppare landing page (hero + CTA)
- **Task 4.1.1.2**: Form registrazione/login (validazione client-side)
- **Task 4.1.1.3**: Modale "Prova come ospite"
- **Task 4.1.1.4**: Pagina "Scopri le regole" (tutorial interattivo)

#### 4.1.2 Dashboard Utente
- **Task 4.1.2.1**: Layout dashboard (profilo + partite + amici)
- **Task 4.1.2.2**: Card "Partite attive" con stato
- **Task 4.1.2.3**: Pulsanti "Crea partita" / "Unisciti a partita"
- **Task 4.1.2.4**: Sidebar lista amici online (indicatori status)

#### 4.1.3 Lobby e Creazione Stanza
- **Task 4.1.3.1**: Form creazione stanza (nome, password, inviti)
- **Task 4.1.3.2**: Selezione amici da invitare (checkbox)
- **Task 4.1.3.3**: Generazione e copia link di invito
- **Task 4.1.3.4**: Waiting room (4 giocatori, pulsante "Inizia")

#### 4.1.4 Tavolo da Gioco
- **Task 4.1.4.1**: Layout tavolo 4 giocatori (Nord/Sud/Est/Ovest)
- **Task 4.1.4.2**: Renderizzare carte in mano (click to play)
- **Task 4.1.4.3**: Area centrale carte giocate (4 carte)
- **Task 4.1.4.4**: Animazioni gioco carta (fly to center)
- **Task 4.1.4.5**: Timer turno con progress bar (30s)
- **Task 4.1.4.6**: Indicatori latency per giocatore
- **Task 4.1.4.7**: Chat in-game (collapsabile)

#### 4.1.5 Schermata Fine Partita
- **Task 4.1.5.1**: Modale "Vittoria/Sconfitta" con confetti
- **Task 4.1.5.2**: Riepilogo punteggio finale
- **Task 4.1.5.3**: Tabella mani vinte per coppia
- **Task 4.1.5.4**: Pulsanti "Rivincita" / "Torna alla lobby" / "Condividi"

### 4.2 Responsive Design

#### 4.2.1 Adattamento Mobile
- **Task 4.2.1.1**: Layout verticale tavolo da gioco (mobile)
- **Task 4.2.1.2**: Carte scrollabili orizzontalmente
- **Task 4.2.1.3**: Pulsanti tattili grandi (min 44×44 px)
- **Task 4.2.1.4**: Chat drawer laterale (collapsabile)

#### 4.2.2 Accessibilità
- **Task 4.2.2.1**: Modalità alto contrasto (daltonici)
- **Task 4.2.2.2**: Screen reader support (aria-labels)
- **Task 4.2.2.3**: Navigazione da tastiera (tab index)

### 4.3 Ottimizzazione Performance

#### 4.3.1 Bundle Size
- **Task 4.3.1.1**: Code splitting per route (lazy loading)
- **Task 4.3.1.2**: Tree shaking dipendenze non utilizzate
- **Task 4.3.1.3**: Minification e uglification

#### 4.3.2 Rendering Optimization
- **Task 4.3.2.1**: React.memo per componenti statici
- **Task 4.3.2.2**: useMemo/useCallback per calcoli costosi
- **Task 4.3.2.3**: Virtualizzazione liste lunghe (storico partite)

---

## 5. Social & Community (Metodologia: Incrementale)

### 5.1 Sistema Amicizie

#### 5.1.1 Gestione Amici
- **Task 5.1.1.1**: Ricerca utenti per nickname
- **Task 5.1.1.2**: Invio richiesta amicizia
- **Task 5.1.1.3**: Accetta/rifiuta richiesta
- **Task 5.1.1.4**: Rimuovi amico

#### 5.1.2 Presenza Online
- **Task 5.1.2.1**: Indicatore online/offline (WebSocket heartbeat)
- **Task 5.1.2.2**: Stato "In partita" / "Disponibile"
- **Task 5.1.2.3**: Notifiche amico online

### 5.2 Chat e Comunicazione

#### 5.2.1 Chat Testuale
- **Task 5.2.1.1**: Chat privata 1-a-1 con amici
- **Task 5.2.1.2**: Chat stanza di gioco (4 giocatori)
- **Task 5.2.1.3**: Storico messaggi (ultimi 100)
- **Task 5.2.1.4**: Moderazione messaggi (filtro parole offensive)

#### 5.2.2 Notifiche
- **Task 5.2.2.1**: Notifiche in-app (toast messages)
- **Task 5.2.2.2**: Badge contatore notifiche non lette
- **Task 5.2.2.3**: Centro notifiche (dropdown)

---

## 6. Infrastructure & DevOps (Metodologia: Incrementale)

### 6.1 Hosting e Deploy

#### 6.1.1 Ambiente Produzione
- **Task 6.1.1.1**: Setup VPS Linux (DigitalOcean/Hetzner)
- **Task 6.1.1.2**: Configurare Nginx reverse proxy
- **Task 6.1.1.3**: Certificati SSL (Let's Encrypt)
- **Task 6.1.1.4**: Domain setup (maraffaonline.it)

#### 6.1.2 Container Orchestration
- **Task 6.1.2.1**: Dockerfile per backend (Node.js)
- **Task 6.1.2.2**: Dockerfile per frontend (React build)
- **Task 6.1.2.3**: Docker Compose per stack completo (DB + Backend + Frontend)
- **Task 6.1.2.4**: Deploy automatizzato con GitHub Actions

### 6.2 CI/CD Pipeline

#### 6.2.1 Continuous Integration
- **Task 6.2.1.1**: GitHub Actions workflow per test automatici
- **Task 6.2.1.2**: Linting e code quality checks (ESLint, Prettier)
- **Task 6.2.1.3**: Build check per ogni PR

#### 6.2.2 Continuous Deployment
- **Task 6.2.2.1**: Deploy automatico su staging (branch develop)
- **Task 6.2.2.2**: Deploy production manuale (branch main)
- **Task 6.2.2.3**: Rollback automatico in caso di errori

### 6.3 Monitoring e Logging

#### 6.3.1 Application Monitoring
- **Task 6.3.1.1**: Setup monitoring uptime (UptimeRobot/Pingdom)
- **Task 6.3.1.2**: Error tracking (Sentry)
- **Task 6.3.1.3**: Performance monitoring (Response time, latency)

#### 6.3.2 Logging
- **Task 6.3.2.1**: Centralizzare log applicativi (Winston)
- **Task 6.3.2.2**: Log rotation e retention policy
- **Task 6.3.2.3**: Dashboard Grafana per metriche

### 6.4 Sicurezza

#### 6.4.1 Hardening Server
- **Task 6.4.1.1**: Configurare firewall (UFW)
- **Task 6.4.1.2**: Disabilitare login SSH root
- **Task 6.4.1.3**: Setup fail2ban per brute force protection
- **Task 6.4.1.4**: Aggiornamenti automatici sicurezza OS

#### 6.4.2 Application Security
- **Task 6.4.2.1**: Sanitizzazione input utente (XSS prevention)
- **Task 6.4.2.2**: Rate limiting API (DoS prevention)
- **Task 6.4.2.3**: SQL injection prevention (prepared statements)
- **Task 6.4.2.4**: CORS policy configurazione

---

## 7. Project Management

### 7.1 Documentazione

#### 7.1.1 Documentazione Tecnica
- **Task 7.1.1.1**: README principale del progetto
- **Task 7.1.1.2**: API documentation (Swagger/OpenAPI)
- **Task 7.1.1.3**: Guida deployment per DevOps
- **Task 7.1.1.4**: Regole ufficiali Maraffone (per team)

#### 7.1.2 Documentazione PM
- **Task 7.1.2.1**: Scoping documents (12 allegati)
- **Task 7.1.2.2**: Planning documents (5 allegati)
- **Task 7.1.2.3**: Launching documents (2 allegati)
- **Task 7.1.2.4**: Monitoring reports (settimanali)

### 7.2 Testing e QA

#### 7.2.1 Testing Automation
- **Task 7.2.1.1**: Unit tests (Jest) - coverage 80%+
- **Task 7.2.1.2**: Integration tests (Supertest)
- **Task 7.2.1.3**: E2E tests (Cypress) - critical paths

#### 7.2.2 User Acceptance Testing
- **Task 7.2.2.1**: UAT con 10 membri Maraffa Forever
- **Task 7.2.2.2**: Raccolta feedback tramite questionario
- **Task 7.2.2.3**: Bug fixing prioritizzato (critical → high → medium)
- **Task 7.2.2.4**: Approvazione finale committente

---

## Note Metodologiche

### Allineamento con Metodologie per Sottosistema

**Waterfall (Game Engine)**:
- Requisiti completi e stabili (regole Maraffone codificate)
- Design → Implementazione → Testing sequenziale
- Consegna unica a fine sottosistema

**Agile Iterativo (Backend, Frontend)**:
- Sprint da 2 settimane
- Iterazioni successive per migliorare features esistenti
- Demo a fine sprint con stakeholder

**Agile Adattivo (Real-Time Communication)**:
- Requisiti emergenti (latency, sincronizzazione)
- Sperimentazione tecnologica (WebSocket vs alternative)
- Adattamento continuo basato su metriche performance

**Incrementale (Social, Infrastructure)**:
- Rilasci successivi con funzionalità crescenti
- Versione base → estensioni progressive
- Deploy indipendenti per ogni incremento

### Integrazione con Altri Documenti

- **Requirements Breakdown Structure (Allegato 2.8)**: Definisce COSA consegnare
- **WBS (questo documento)**: Definisce COME organizzare il lavoro
- **Product Backlog (Allegato 3.3)**: Prioritizza le attività per sprint Agile
- **Gantt Chart (Allegato 3.5)**: Temporizza le attività con dipendenze

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Luca Bianchi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 20/10/2025
