# Allegato 2.8 - Requirements Breakdown Structure (RBS)
## v.1.0.0 – 2025-09-25 10:30:00

La **Requirements Breakdown Structure (RBS)** è una decomposizione gerarchica dei requisiti del progetto MaraffaOnline, organizzata per sottosistema. Ogni requisito è classificato secondo le seguenti categorie:

- **F** = Funzionale (cosa il sistema deve fare)
- **NF** = Non Funzionale (qualità, performance, vincoli)
- **C** = Vincolo (constraint tecnico o di business)

I requisiti sono inoltre prioritizzati con il metodo **MoSCoW** (dettagliato in fase di Planning):
- **M** = Must Have (MVP)
- **S** = Should Have
- **C** = Could Have
- **W** = Won't Have (escluso dal MVP)

---

## 1. SOTTOSISTEMA: Game Engine

**Responsabile**: Elena Rossi
**Metodologia**: Waterfall
**Priorità**: MUST HAVE (core del prodotto)

### 1.1 Regole del Gioco

#### 1.1.1 Implementazione Regole Maraffa Romagnola [F, M]
- Gioco a 4 giocatori (2 coppie)
- Mazzo di 40 carte italiane
- Distribuzione 10 carte a giocatore
- Sistema di briscola (seme dominante)
- Calcolo punteggio tradizionale (Asso=11, Tre=10, Re=4, Cavallo=3, Fante=2)
- **Validazione**: approvazione formale da Francesca Giuliani (esperta Maraffa Forever)

#### 1.1.2 Gestione Turni e Fasi di Gioco [F, M]
- Determinazione primo giocatore (casuale al primo turno, poi vincitore mano precedente)
- Rotazione turni in senso orario
- Obbligo di rispondere al seme (se si possiede)
- Gestione dichiarazioni speciali (es. "Maraffa" - tre carte dello stesso seme)
- **Dipendenza**: sincronizzazione con Real-Time Communication

#### 1.1.3 Validazione Mosse [F, M]
- Controllo legalità carta giocata (rispetto seme, se posseduta)
- Prevenzione cheating (es. giocare carta non in mano)
- Gestione timeout turno (30 secondi)
- Mossa automatica se timeout scaduto (carta casuale valida)

#### 1.1.4 Calcolo Punteggi [F, M]
- Conteggio punti mano (chi vince la mano)
- Somma punteggi partita per coppia
- Condizione vittoria: prima coppia a 121 punti
- Gestione pareggio (rarissimo, ma possibile): mano supplementare

#### 1.1.5 Gestione Situazioni Speciali [F, S]
- Dichiarazione "Maraffa" (bonus punti)
- Gestione "capotto" (una coppia vince tutte le mani): punti raddoppiati
- Gestione carte particolari con regole speciali (se presenti nelle regole romagnole)

### 1.2 Intelligenza Artificiale (IA) [F, C]
- [-] **Won't Have** nel MVP: nessuna modalità single-player contro IA
- [+] Potenziale feature futura (post-MVP)
- **Motivazione esclusione**: focus su multiplayer online, budget/tempo limitato

### 1.3 Persistenza Stato Partita [F, M]
- Salvataggio stato partita sul server ogni mano
- Recupero stato in caso di disconnessione giocatore
- **Vincolo**: stato persistito per max 24 ore

---

## 2. SOTTOSISTEMA: Backend Server

**Responsabile**: Sara Bianchi
**Metodologia**: Agile Iterativo
**Priorità**: MUST HAVE

### 2.1 Autenticazione e Gestione Utenti

#### 2.1.1 Registrazione Utente [F, M]
- Registrazione via email + password
- Validazione email (confirmation link)
- Password hashing (bcrypt, min 8 caratteri)
- **NF**: Conformità GDPR (consenso privacy, data minimization)

#### 2.1.2 Login e Sessioni [F, M]
- Login con email + password
- Generazione JWT token (durata 7 giorni)
- Opzione "Ricordami" (refresh token)
- **NF**: Sicurezza - protezione contro brute force (rate limiting)

#### 2.1.3 Accesso Ospite [F, M]
- Generazione username temporaneo (es. "Ospite_1234")
- Session limitata (nessun salvataggio statistiche)
- Conversione account ospite → registrato (opzionale)

#### 2.1.4 Gestione Profilo [F, S]
- Modifica dati profilo (username, avatar, bio)
- Upload avatar personalizzato (max 1MB, formati jpg/png)
- **NF**: Storage - immagini salvate su CDN (es. Cloudinary)

#### 2.1.5 Password Recovery [F, S]
- Reset password via email
- Token temporaneo (validità 1 ora)

#### 2.1.6 Social Login [F, W]
- [-] **Won't Have** MVP: login con Google/Facebook
- [+] Considerato per v1.1 post-lancio

### 2.2 Gestione Partite

#### 2.2.1 Creazione Stanza [F, M]
- Creazione stanza pubblica o privata
- Impostazione password (se privata)
- Generazione link di invito univoco
- **Vincolo**: Max 1000 stanze simultanee (limite infrastruttura)

#### 2.2.2 Join Stanza [F, M]
- Unirsi a stanza tramite link o codice
- Validazione password (se stanza privata)
- Gestione lista d'attesa (4 posti fissi)

#### 2.2.3 Gestione Lobby Partita [F, M]
- Visualizzazione giocatori connessi (4/4)
- Kick player (solo owner stanza)
- Start partita (quando 4 giocatori pronti)

#### 2.2.4 Persistenza Dati Partita [F, M]
- Salvataggio stato partita su database (PostgreSQL)
- Salvataggio storico partite completate
- **NF**: Performance - query ottimizzate, indici su user_id, match_id

### 2.3 Sistema Amicizie [F, S]

#### 2.3.1 Aggiunta Amici [F, S]
- Ricerca utenti per username
- Invio richiesta amicizia
- Accettazione/rifiuto richiesta

#### 2.3.2 Lista Amici [F, S]
- Visualizzazione lista amici
- Stato online/offline in tempo reale
- Notifica "Amico connesso"

#### 2.3.3 Invito Diretto [F, S]
- Invitare amico a partita specifica (notifica in-app)

### 2.4 Statistiche Utente [F, C]

#### 2.4.1 Statistiche Base [F, M]
- Partite giocate, vinte, perse
- Win rate (%)
- Punti totali accumulati

#### 2.4.2 Statistiche Avanzate [F, C]
- Mani vinte/perse
- Carta più giocata
- **Priorità**: Could Have (non critico per MVP)

### 2.5 API RESTful [NF, M]

#### 2.5.1 Endpoints Standard [NF, M]
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/users/profile`
- `POST /api/matches/create`
- `GET /api/matches/:id`
- **NF**: Documentazione API con Swagger/OpenAPI

#### 2.5.2 Performance [NF, M]
- Tempo di risposta < 200ms per 95% delle richieste
- Rate limiting: 100 req/min per utente
- **Strumento**: Monitoraggio con New Relic o Datadog

#### 2.5.3 Sicurezza [NF, M]
- HTTPS obbligatorio
- CORS configurato correttamente
- Input validation su tutti gli endpoint
- Protezione contro SQL injection (uso ORM)

---

## 3. SOTTOSISTEMA: Real-Time Communication

**Responsabile**: Elena Rossi + Sara Bianchi
**Metodologia**: Agile Adattivo
**Priorità**: MUST HAVE (core critico)

### 3.1 Connessione WebSocket

#### 3.1.1 Gestione Connessioni [NF, M]
- WebSocket server (Socket.IO)
- Supporto fino a 400 connessioni simultanee (100 partite × 4 giocatori)
- Heartbeat ogni 30 secondi per rilevare disconnessioni
- **NF**: Latency massima 500ms

#### 3.1.2 Autenticazione WebSocket [F, M]
- Autenticazione tramite JWT token al connect
- Rifiuto connessioni non autenticate

### 3.2 Sincronizzazione Stato Partita

#### 3.2.1 Eventi di Gioco in Tempo Reale [F, M]
- `player_joined`: giocatore entra in partita
- `game_started`: partita iniziata
- `card_played`: carta giocata da un giocatore
- `hand_won`: mano vinta, aggiornamento punteggio
- `game_ended`: partita terminata
- **Architettura**: Server-authoritative (server è fonte di verità)

#### 3.2.2 Broadcast Selettivo [F, M]
- Eventi broadcast solo ai 4 giocatori della partita (room-based)
- Eventi privati (es. carte in mano) solo al giocatore specifico

#### 3.2.3 Gestione Latency [NF, M]
- Ottimizzazione payload messaggi (compressione JSON)
- Lag compensation: predizione lato client (carte animate prima della conferma server)
- Indicatore latency visuale per utenti (verde/giallo/rosso)

### 3.3 Gestione Disconnessioni

#### 3.3.1 Disconnessione Temporanea [F, M]
- Partita sospesa per max 5 minuti
- Notifica altri giocatori: "Giocatore X disconnesso, attendi riconnessione..."
- Riconnessione automatica con ripristino stato

#### 3.3.2 Disconnessione Permanente [F, M]
- Se > 5 minuti: partita annullata (nessun vincitore)
- Opzione: sostituire giocatore con bot (Won't Have nel MVP)

### 3.4 Chat in Tempo Reale [F, S]

#### 3.4.1 Chat In-Game [F, M]
- Messaggi testuali tra i 4 giocatori della partita
- Throttling: max 1 messaggio/secondo per utente
- Moderazione: filtro parole offensive (lista italiana)

#### 3.4.2 Chat Globale [F, C]
- Chat generale nella lobby
- **Priorità**: Could Have (non critico)

#### 3.4.3 Emoji/Reactions [F, W]
- [-] Won't Have MVP
- [+] Considerato per versione futura

---

## 4. SOTTOSISTEMA: Frontend Web

**Responsabile**: Luca Moretti
**Metodologia**: Agile Iterativo
**Priorità**: MUST HAVE

### 4.1 Interfaccia Utente

#### 4.1.1 Implementazione Mockup Approvati [F, M]
- Homepage/Landing
- Login/Registrazione
- Dashboard/Lobby
- Creazione stanza
- Tavolo da gioco (schermata critica)
- Fine partita
- **Riferimento**: vedi Allegato 2.7 - Prototyping

#### 4.1.2 Design System [NF, M]
- Componenti riutilizzabili (button, card, modal, form)
- Style guide: palette colori, tipografia, spacing
- **Tool**: Figma per design, React component library

### 4.2 Responsive Design [NF, M]

#### 4.2.1 Supporto Multi-Device [NF, M]
- Desktop (1920x1080 e superiori)
- Tablet (768x1024)
- Mobile (375x667 e superiori)
- **Test**: Chrome, Firefox, Safari, Edge (ultime 2 versioni)

#### 4.2.2 Mobile-First Approach [NF, M]
- Layout adattivo (non solo scalato)
- Touch-friendly: pulsanti min 44x44px
- Tavolo da gioco verticale su mobile

### 4.3 Accessibilità [NF, S]

#### 4.3.1 Conformità WCAG 2.1 AA [NF, S]
- Contrasto colori sufficiente (min 4.5:1)
- Navigazione da tastiera completa (tab order logico)
- Screen reader friendly (aria-labels, semantic HTML)
- Focus indicators visibili

#### 4.3.2 Modalità Daltonici [NF, C]
- Palette alternativa per daltonici (rosso-verde)
- **Priorità**: Could Have

### 4.4 Performance Frontend [NF, M]

#### 4.4.1 Ottimizzazione Caricamento [NF, M]
- Lazy loading componenti non critici
- Code splitting (React.lazy)
- Immagini ottimizzate (WebP, responsive images)
- **Target**: First Contentful Paint < 2 secondi

#### 4.4.2 Bundle Size [NF, S]
- JavaScript bundle < 500KB (gzipped)
- Tree shaking per eliminare codice non usato

### 4.5 Animazioni e Feedback Visivo [NF, S]

#### 4.5.1 Microinterazioni [NF, S]
- Carte giocate volano al centro tavolo (animazione fluida 60fps)
- Confetti/celebrazione vittoria
- Loading spinners per operazioni async

---

## 5. SOTTOSISTEMA: Mobile Application

**Responsabile**: TBD (da definire)
**Metodologia**: Incrementale
**Priorità**: WON'T HAVE (MVP)

### 5.1 App Nativa iOS/Android [F, W]
- [-] **Esclusa dal MVP** (budget/tempo limitato)
- [+] **Alternativa MVP**: responsive web app utilizzabile da mobile browser
- **Pianificazione**: sviluppo app nativa in fase 2 post-lancio (se progetto di successo)

### 5.2 Progressive Web App (PWA) [F, C]
- Installabilità come app (Add to Home Screen)
- Service Worker per offline caching
- **Priorità**: Could Have (valutare in fase di planning)

---

## 6. SOTTOSISTEMA: Social & Community Features

**Responsabile**: Sara Bianchi + Luca Moretti
**Metodologia**: Incrementale
**Priorità**: MIXED (alcune Must, altre Should/Could)

### 6.1 Sistema Amicizie
**Vedi sezione 2.3 (Backend Server)** - Priorità: Should Have

### 6.2 Chat
**Vedi sezione 3.4 (Real-Time Communication)** - Priorità: Must Have (in-game), Could Have (globale)

### 6.3 Classifiche e Leaderboard [F, C]

#### 6.3.1 Classifica Globale [F, C]
- Top 100 giocatori per win rate
- Aggiornamento giornaliero
- **Priorità**: Could Have

#### 6.3.2 Classifica Amici [F, C]
- Confronto stats con amici
- **Priorità**: Could Have

### 6.4 Notifiche [F, S]

#### 6.4.1 Notifiche In-App [F, M]
- "È il tuo turno"
- "Amico ti ha invitato a partita"
- **Implementazione**: WebSocket events

#### 6.4.2 Notifiche Push [F, W]
- [-] Won't Have MVP (richiede app mobile o browser permission)
- [+] Considerato per fase 2

### 6.5 Profili Pubblici [F, S]

#### 6.5.1 Pagina Profilo Utente [F, S]
- Visualizzazione stats pubbliche
- Badge/achievements (Could Have)

---

## 7. SOTTOSISTEMA: Infrastructure & DevOps

**Responsabile**: Andrea Conti
**Metodologia**: Incrementale
**Priorità**: MUST HAVE (supporto a tutti i sottosistemi)

### 7.1 Hosting e Deployment

#### 7.1.1 Server Dedicato [C, M]
- Hetzner o OVH (server dedicato ~€50/mese)
- 8GB RAM, 4 cores, 200GB SSD
- **Vincolo**: Budget limitato, no cloud scalabile (AWS/GCP) nel MVP

#### 7.1.2 Containerizzazione [NF, M]
- Docker per tutti i servizi (backend, frontend, database)
- Docker Compose per orchestrazione locale
- **Beneficio**: Consistency tra ambienti dev/staging/production

#### 7.1.3 CI/CD Pipeline [NF, M]
- GitLab CI per automated testing e deployment
- Pipeline: test → build → deploy
- Deployment automatico su push a branch `main`

### 7.2 Database

#### 7.2.1 PostgreSQL [NF, M]
- Database relazionale per dati strutturati (utenti, partite)
- Backup automatici giornalieri
- **Performance**: Indici su colonne critiche (user_id, match_id)

#### 7.2.2 Redis [NF, S]
- Cache per sessioni utente
- Storage temporaneo stato partite in corso
- **Beneficio**: Riduce carico su PostgreSQL

### 7.3 Monitoring e Logging

#### 7.3.1 Logging [NF, M]
- Log centralizzati (Winston + Elasticsearch/Loki)
- Log levels: error, warn, info, debug
- **Retention**: 30 giorni

#### 7.3.2 Monitoring Performance [NF, M]
- Uptime monitoring (Pingdom o UptimeRobot free tier)
- Alert se downtime > 5 minuti
- **Target**: Uptime 99% mensile

#### 7.3.3 Error Tracking [NF, S]
- Sentry per tracking errori frontend/backend
- Alert automatici su errori critici

### 7.4 Sicurezza

#### 7.4.1 SSL/TLS [NF, M]
- Certificato SSL (Let's Encrypt gratuito)
- HTTPS obbligatorio su tutto il sito
- **Security Header**: HSTS, CSP

#### 7.4.2 Firewall e DDoS Protection [NF, S]
- Firewall configurato (solo porte 80, 443, 22)
- Cloudflare free tier per DDoS protection base

#### 7.4.3 Backup e Disaster Recovery [NF, M]
- Backup database giornaliero automatico
- Backup manuale pre-deployment
- **Recovery Time Objective (RTO)**: < 4 ore

### 7.5 Scalabilità [NF, S]

#### 7.5.1 Architettura Preparata per Scalabilità [NF, S]
- Codice stateless (no session affinity richiesta)
- Database connection pooling
- **Futuro**: Load balancer + multiple server instances (se necessario post-MVP)

---

## Riepilogo Priorità MoSCoW

### MUST HAVE (MVP - Lancio 15/03/2026)
- [+] Game Engine completo
- [+] Backend Server (auth, partite, API)
- [+] Real-Time Communication (WebSocket, sincronizzazione)
- [+] Frontend Web responsive
- [+] Chat in-game
- [+] Infrastructure base (hosting, database, CI/CD)

### SHOULD HAVE (Importante ma non critico)
- - Sistema amicizie
- - Profili utente personalizzabili
- - Statistiche avanzate
- - Accessibilità WCAG AA
- - Monitoring avanzato

### COULD HAVE (Desiderabile)
- - Chat globale
- - Classifiche/Leaderboard
- - PWA
- - Modalità daltonici
- - Statistiche molto avanzate

### WON'T HAVE (MVP - Pianificato per v1.1+)
- [-] App mobile nativa iOS/Android
- [-] Social login (Google/Facebook)
- [-] Modalità single-player vs IA
- [-] Notifiche push
- [-] Emoji/reactions
- [-] Tornei strutturati

---

## Tracciabilità Requisiti

Ogni requisito sarà tracciato attraverso:
- **ID univoco**: es. `REQ-GE-1.1.1` (Game Engine, sezione 1.1, punto 1)
- **User Story associata**: vedi Allegato 2.9
- **Test case**: definiti in fase di Planning
- **Issue tracking**: Jira board con label per sottosistema

---

**Redatto da**: Team PlayHeritage Labs (contributi di tutti i membri)
**Coordinato da**: Marco Venturi (Project Manager)
**Revisionato da**: Giovanni Marchetti (Project Sponsor)
**Data approvazione**: 26/09/2025
