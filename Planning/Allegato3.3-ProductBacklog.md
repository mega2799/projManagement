# Allegato 3.3 - Product Backlog
## v.3.1.0 – 2026-08-02 12:00

Il **Product Backlog** è l'elenco prioritizzato del lavoro gestito a sprint per il progetto MaraffaOnline. Gli item derivano dalle User Stories (Allegato 2.9), sono stimati in **story points** (Planning Poker, scala Fibonacci) e assegnati a sprint da 2 settimane, in coerenza con le date del Gantt (Allegato 3.5).

**Ambito.** Il Backlog include solo il lavoro esprimibile come user story e realizzato negli sprint: **Backend Server**, **Real-Time Communication**, **Frontend Web** e le user story di **Social & Community** (tracciate sotto il sottosistema che le implementa). Restano esclusi il **Game Engine** (Waterfall) e l'**Infrastructure & DevOps** (Incrementale, attività on-demand): sono tracciati in WBS (Allegato 3.1) e Gantt (Allegato 3.5). *(Razionale nella relazione, Cap. 3 - Planning.)*

**Legenda.** Priorità: **P0-P1** = Must Have (P0 bloccante per il core), **P2** = Should Have, **P3** = Could Have (mappatura MoSCoW, Allegato 3.2). Story points: Fibonacci 1-21 (1 SP ≈ 1-2 ore; 8 SP ≈ 4-5 giorni; 13 SP ≈ 1 settimana). **Colonna US**: la user story dell'Allegato 2.9 da cui il task deriva; "—" indica task tecnici/abilitanti non riconducibili a una singola storia utente.

---

## Calendario Sprint

**Durata progetto**: 15 ottobre 2025 - 15 maggio 2026 · **15 sprint** (Sprint 0-14) da 2 settimane.

| Sprint | Periodo | Focus |
|--------|---------|-------|
| 0 | 15-27 Ott 2025 | Setup infrastruttura (fuori Backlog, vedi Gantt) |
| 1 | 28 Ott - 07 Nov | Backend auth + database foundation |
| 2 | 10 Nov - 21 Nov | Backend gestione partite |
| 3 | 24 Nov - 05 Dic | Backend lobby + statistiche |
| 4 | 08 Dic - 19 Dic | Backend persistenza + WebSocket foundation |
| 5 | 22 Dic - 02 Gen | Eventi Real-Time + Frontend foundation — **capacità ridotta** (festività), carryover pianificato |
| 6 | 05 Gen - 16 Gen | Frontend homepage, auth e dashboard + Real-Time eventi (fine) |
| 7 | 19 Gen - 30 Gen | Frontend stanze/lobby + chat e disconnessioni |
| 8 | 02 Feb - 13 Feb | Frontend tavolo da gioco (parte 1) + sistema amicizie |
| 9 | 16 Feb - 27 Feb | Frontend tavolo (parte 2) + social e profili |
| 10 | 02 Mar - 13 Mar | Animazioni tavolo + accessibilità/performance |
| 11 | 16 Mar - 31 Mar | Testing End-to-End + rifiniture tavolo (fast tracking, vedi Allegato 3.5) |
| 12 | 01 Apr - 24 Apr | UAT con Maraffa Forever + bug fixing |
| 13 | 27 Apr - 08 Mag | Preparazione lancio + deploy production |
| 14 | 11 Mag - 15 Mag | Production launch |

**Capacity e carico**: la capacità stimata del team è di **≈40 SP/sprint team-wide** (include il lavoro Game Engine/Infrastructure tracciato in WBS/Gantt, ≈131 SP equivalenti). Il piano carica in media **≈37 SP/sprint team-wide** (441 SP sugli Sprint 0-11) e **≈28 SP/sprint di solo Backlog** (310 SP sugli Sprint 1-11): il margine tra capacità e carico medio assorbe festività e variabilità. Lo Sprint 11 ospita solo le rifiniture del tavolo, in fast tracking con il Testing E2E; gli Sprint 12-14 (UAT, lancio) non sono stimati in story points. *(Riconciliazione delle metriche: relazione Cap. 3 e Cap. 5.)*

---

## Backend Server

| Sprint | Priorità | US (2.9) | Task | SP |
|:------:|:--------:|------|------|:--:|
| 1 | P0 | — | Setup progetto Node.js + Express + PostgreSQL | 5 |
| 1 | P0 | US-1.1 | Registrazione utente (email + password) | 5 |
| 1 | P0 | US-1.2 | Login con JWT token | 5 |
| 1 | P0 | US-1.2 | Middleware autenticazione JWT | 3 |
| 1 | P1 | US-1.4 | Endpoint GET /api/users/profile | 2 |
| 1 | P0 | US-1.3 | Accesso ospite (username temporaneo) | 3 |
| 2 | P0 | US-2.1 | Modello database partite (matches table) | 3 |
| 2 | P0 | US-2.1/2.2 | POST /api/matches/create (stanza pubblica/privata) | 5 |
| 2 | P0 | US-2.3/2.4 | POST /api/matches/:id/join (password validation) | 5 |
| 3 | P1 | US-3.1 | Gestione lobby: lista giocatori connessi (4/4) | 3 |
| 3 | P0 | US-7.1 | GET /api/matches/:id (recupero stato) | 3 |
| 3 | P0 | US-7.1 | DELETE /api/matches/:id (annulla partita) | 2 |
| 3 | P1 | US-6.1 | Modello database statistiche utente | 3 |
| 3 | P1 | US-6.1 | Calcolo statistiche base (win/loss, win rate) | 5 |
| 4 | P0 | US-7.1 | Persistenza stato partita su PostgreSQL | 8 |
| 8 | P2 | US-5.1 | Modello database amicizie (friendships table) | 3 |
| 8 | P2 | US-5.1 | POST /api/friends/request (invia richiesta) | 3 |
| 8 | P2 | US-5.1 | PUT /api/friends/request/:id/accept | 2 |
| 8 | P2 | US-5.2 | GET /api/friends (lista amici) | 2 |
| 9 | P2 | US-5.2 | Presenza online/offline (integrazione WebSocket) | 5 |
| 9 | P2 | US-1.5 | Password recovery (reset via email) | 5 |
| | | | **Totale Backend Server (6 sprint)** | **80** |

## Real-Time Communication

| Sprint | Priorità | US (2.9) | Task | SP |
|:------:|:--------:|------|------|:--:|
| 4 | P0 | — | Setup Socket.IO server | 5 |
| 4 | P0 | — | Gestione rooms per partite (room-based broadcast) | 5 |
| 4 | P0 | — | Autenticazione WebSocket con JWT | 3 |
| 4 | P0 | US-7.1 | Heartbeat ogni 30s per rilevare disconnessioni | 3 |
| 4 | P1 | — | Logging eventi WebSocket | 2 |
| 5 | P0 | US-3.1 | Evento `player_joined` | 2 |
| 5 | P0 | US-3.1 | Evento `game_started` | 2 |
| 5 | P0 | US-3.2 | Evento `card_played` | 5 |
| 5 | P0 | US-3.3 | Evento `hand_won` (punteggio aggiornato) | 5 |
| 6 | P0 | US-3.5 | Evento `game_ended` | 3 |
| 6 | P0 | US-3.2 | Broadcast selettivo: eventi privati (carte in mano) | 5 |
| 6 | P1 | — | Ottimizzazione payload (compressione JSON) | 3 |
| 7 | P0 | US-7.1 | Disconnessione temporanea: partita sospesa (max 5 min) | 5 |
| 7 | P0 | US-7.1 | Riconnessione automatica con ripristino stato | 5 |
| 7 | P0 | US-7.1 | Disconnessione permanente: annulla partita | 3 |
| 7 | P0 | US-4.1 | Chat in-game testuale (4 giocatori) | 5 |
| 7 | P1 | US-4.1 | Throttling chat (1 msg/sec) + filtro parole offensive | 3 |
| 7 | P2 | — | Indicatore latency visuale (verde/giallo/rosso) | 3 |
| | | | **Totale Real-Time Communication (4 sprint)** | **67** |

## Frontend Web

| Sprint | Priorità | US (2.9) | Task | SP |
|:------:|:--------:|------|------|:--:|
| 5 | P0 | — | Setup progetto React + Vite + Tailwind CSS | 3 |
| 5 | P0 | — | Design system: componenti base (Button, Card, Modal, Form) | 8 |
| 6 | P0 | — | Homepage/Landing page (mockup v2) | 5 |
| 6 | P1 | — | Pagina "Scopri le regole" (tutorial Maraffone) | 5 |
| 6 | P0 | US-1.1 | Form registrazione con validazione client-side | 5 |
| 6 | P0 | US-1.2 | Form login (email + password) | 3 |
| 6 | P0 | US-1.3 | Opzione "Prova come ospite" (modale) | 2 |
| 6 | P0 | US-1.2 | Gestione JWT token (store in localStorage) | 3 |
| 6 | P2 | US-1.5 | Password recovery (form su API mock; integrazione con l'API in Sprint 9) | 3 |
| 6 | P0 | — | Layout dashboard (profilo + partite + amici) | 5 |
| 6 | P0 | US-2.3 | Card "Partite attive" con lista partite in corso | 5 |
| 7 | P0 | US-2.1/2.3 | Pulsanti "Crea partita" / "Unisciti a partita" | 2 |
| 7 | P0 | US-2.1/2.2 | Form creazione stanza (nome, password, inviti) | 5 |
| 7 | P2 | US-5.2 | Sidebar lista amici online (indicatori status) | 3 |
| 8 | P0 | US-3.2 | Layout tavolo 4 giocatori (Nord/Sud/Est/Ovest) | 8 |
| 8 | P0 | US-3.2 | Renderizzare carte in mano (SVG o immagini) | 5 |
| 9 | P0 | US-3.2 | Click to play: seleziona carta e invia al server | 5 |
| 9 | P0 | US-3.2 | Area centrale: mostra 4 carte giocate | 3 |
| 9 | P2 | US-6.1 | Pagina profilo utente (stats + avatar) | 5 |
| 9 | P2 | US-5.1/5.2 | Lista amici (ricerca + richieste) | 5 |
| 9 | P1 | — | Notifiche in-app "È il tuo turno" (toast messages, REQ-SOC-6.4.1 Must) | 3 |
| 10 | P0 | US-3.2 | Animazioni gioco carta (fly to center, 60fps) | 8 |
| 10 | P0 | US-3.4 | Timer turno con progress bar (30 secondi) | 5 |
| 10 | P0 | — | Responsive design: layout verticale mobile | 8 |
| 10 | P0 | — | Touch-friendly: pulsanti min 44×44px | 3 |
| 10 | P3 | US-6.1 | Storico partite (tabella con paginazione) | 5 |
| 10 | P2 | — | Accessibilità WCAG 2.1 AA (aria-labels, focus indicators) | 8 |
| 10 | P2 | — | Ottimizzazione bundle size (code splitting, lazy loading) | 5 |
| 11 | P0 | US-3.3 | Punteggio real-time (aggiornato dopo ogni presa) | 3 |
| 11 | P2 | — | Indicatori latency per giocatore (colori) | 3 |
| 11 | P1 | US-4.1 | Chat in-game (collapsabile, integrata con WebSocket) | 5 |
| 11 | P0 | US-3.5 | Modale fine partita (vittoria/sconfitta + riepilogo) | 5 |
| 11 | P0 | US-3.5 | Pulsanti "Rivincita" / "Torna alla lobby" / "Condividi" | 3 |
| 11 | P1 | US-3.5 | Animazioni microinterazioni (confetti vittoria) | 3 |
| 11 | P2 | — | Performance audit (Lighthouse score > 90) | 5 |
| 11 | P3 | — | Modalità daltonici (palette alternativa) | 3 |
| | | | **Totale Frontend Web (7 sprint)** | **163** |

**Totale Product Backlog: 310 story points.** Le user story di Social & Community sono conteggiate nel sottosistema che le implementa: amicizie (US-5.x) e statistiche (US-6.1) nel Backend, chat in-game (US-4.1) nel Real-Time, le rispettive interfacce nel Frontend. Il lavoro del Game Engine copre le user story di gameplay (US-3.x) per la parte di regole, tracciata in WBS/Gantt.

---

## Definition of Done

Un item è **Done** solo quando:

1. Codice scritto e committed su repository
2. Unit test scritti e passati (coverage > 80%, gate minimo di merge; il target di progetto monitorato nei quality gate è 85%, vedi Cap. 5)
3. Code review approvata da almeno 1 peer
4. Integration test passati
5. Documentazione API/componente aggiornata
6. Deploy su ambiente staging riuscito
7. Acceptance criteria (da User Story) soddisfatti
8. Product Owner ha approvato (demo in Sprint Review)

---

**Redatto da**: Marco Venturi (Product Owner, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Scrum Master / Tech Lead)

**Storico revisioni**:
- **v.2.0.0** (28/10/2025): separazione del Product Backlog dal lavoro tracciato in WBS/Gantt.
- **v.3.0.0** (02/08/2026): snellimento in artefatto operativo — tabelle unificate per sottosistema, legenda P0-P3 ↔ MoSCoW, ambito compresso. Note metodologiche, riepiloghi percentuali, velocity tracking e processo di gestione del backlog spostati nella relazione (Cap. 3 e Cap. 5), nell'Allegato 4.3 (cerimonie) e nel registro `Relazione/_appunti-per-relazione.md`.
- **v.3.1.0** (02/08/2026): revisione di tracciabilità e coerenza col Gantt. La colonna US ora punta alle **user story reali dell'Allegato 2.9** (la numerazione precedente era autonoma e collideva con quella del 2.9); i task tecnici sono marcati "—". Assegnazioni agli sprint riallineate alle **date del Gantt/CSV** (Allegato 3.5): il lavoro frontend scorre ora negli Sprint 5-11 (il tavolo da gioco negli Sprint 8-11, coerente con l'attività P di febbraio-marzo), il Real-Time negli Sprint 4-7. Nota capacity riscritta in termini di capacità (≈40) vs carico medio (≈37 team-wide, ≈28 solo Backlog).
