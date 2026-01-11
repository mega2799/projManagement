# Allegato 3.3 - Product Backlog
## v.1.0.0 – 2025-10-25 09:00:00

Il **Product Backlog** è l'elenco prioritizzato di tutto il lavoro da completare per il progetto MaraffaOnline. Ogni item è stimato in **Story Points** (scala Fibonacci: 1, 2, 3, 5, 8, 13, 21) e assegnato a specifici **Sprint** da 2 settimane.

---

## Struttura Sprint e Timeline

**Durata progetto**: 6 mesi (15 ottobre 2025 - 15 marzo 2026)
**Sprint duration**: 2 settimane
**Numero Sprint**: 13 sprint totali
**Team capacity**: ~40 story points per sprint (considerando team di 5 persone)

### Calendario Sprint
| Sprint | Periodo | Focus Principale |
|--------|---------|------------------|
| Sprint 0 | 15-25 Ott 2025 | Setup infrastruttura, repository, CI/CD |
| Sprint 1 | 28 Ott - 08 Nov | Backend auth + Game Engine foundation |
| Sprint 2 | 11 Nov - 22 Nov | Game Engine regole Maraffone |
| Sprint 3 | 25 Nov - 06 Dic | Backend partite + Frontend homepage |
| Sprint 4 | 09 Dic - 20 Dic | Frontend dashboard + login |
| Sprint 5 | 23 Dic - 03 Gen | WebSocket foundation + Real-Time events |
| Sprint 6 | 06 Gen - 17 Gen | Frontend tavolo da gioco |
| Sprint 7 | 20 Gen - 31 Gen | Game Engine avanzato + sincronizzazione |
| Sprint 8 | 03 Feb - 14 Feb | Chat in-game + notifiche |
| Sprint 9 | 17 Feb - 28 Feb | Sistema amicizie + profili |
| Sprint 10 | 03 Mar - 14 Mar | Testing, bug fixing, polish |
| Sprint 11 | 17 Mar - 28 Mar | UAT con Maraffa Forever |
| Sprint 12 | 31 Mar - 11 Apr | Preparazione lancio |

---

## Nota: Ambito del Product Backlog

**IMPORTANTE**: Questo Product Backlog include **esclusivamente i sottosistemi gestiti con metodologie Agile** (Iterativo e Adattivo).

### Sottosistemi Inclusi nel Product Backlog

I seguenti sottosistemi utilizzano sprint e story points:
- **Backend Server** (Agile Iterativo)
- **Real-Time Communication** (Agile Adattivo)
- **Frontend Web** (Agile Iterativo)
- **Social & Community** (Incrementale con rilasci per sprint)

### Sottosistemi NON Inclusi nel Product Backlog

I seguenti sottosistemi seguono altre metodologie e sono tracciati **esclusivamente** in Work Breakdown Structure (Allegato 3.1) e Gantt Chart (Allegato 3.5):

- **Game Engine**: Metodologia **Waterfall** → Vedi WBS sezione 1
  - Approccio: Design → Implementation → Testing sequenziale
  - Requisiti stabili e completamente definiti (regole ufficiali Maraffone)
  - Non compatibile con sprint iterativi

- **Infrastructure & DevOps**: Metodologia **Incrementale** → Vedi WBS sezione 7
  - Approccio: rilasci continui e indipendenti
  - Lavoro distribuito su tutta la durata del progetto
  - Non organizzato in sprint, ma in attività on-demand

**Razionale Metodologico**: Il Product Backlog è uno strumento specifico di **Scrum/Agile** e deve includere solo work package gestiti con approcci iterativi/adattivi. Mischiare metodologie diverse nel Backlog comprometterebbe la coerenza della gestione sprint e la chiarezza dei ruoli (Product Owner, Scrum Master, Development Team).

---

## Note Metodologiche Agile

### Story Points - Scala di Riferimento
- **1 pt**: Task triviale (~1-2 ore) - es. "Aggiungere campo username a tabella users"
- **2 pt**: Task semplice (~3-4 ore) - es. "Endpoint GET /api/users/profile"
- **3 pt**: Task standard (~1 giorno) - es. "Form registrazione con validazione"
- **5 pt**: Task complesso (~2-3 giorni) - es. "Implementare JWT authentication"
- **8 pt**: Feature medio-grande (~4-5 giorni) - es. "Sistema creazione/join stanze"
- **13 pt**: Feature grande (~1 settimana) - es. "Tavolo da gioco completo con animazioni"
- **21 pt**: Epic (~2 settimane) - es. "Game Engine completo con tutte le regole"

---

## Product Backlog - Backend Server

### Sprint 1 (28 Ott - 08 Nov)
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-1.1 | Setup progetto Node.js + Express + PostgreSQL | 5 | Sprint 1 |
| P0 | US-1.2 | Implementare registrazione utente (email + password) | 5 | Sprint 1 |
| P0 | US-1.3 | Implementare login con JWT token | 5 | Sprint 1 |
| P0 | US-1.4 | Middleware autenticazione JWT | 3 | Sprint 1 |
| P1 | US-1.5 | Endpoint GET /api/users/profile | 2 | Sprint 1 |
| | **Totale Sprint 1** | | **20** | |

### Sprint 2 (11 Nov - 22 Nov)
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-1.6 | Accesso ospite (username temporaneo) | 3 | Sprint 2 |
| P0 | US-2.1 | Modello database per partite (matches table) | 3 | Sprint 2 |
| P0 | US-2.2 | Endpoint POST /api/matches/create (stanza pubblica/privata) | 5 | Sprint 2 |
| P0 | US-2.3 | Endpoint POST /api/matches/:id/join (con password validation) | 5 | Sprint 2 |
| P1 | US-2.4 | Gestione lobby: lista giocatori connessi (4/4) | 3 | Sprint 2 |
| | **Totale Sprint 2** | | **19** | |

### Sprint 3 (25 Nov - 06 Dic)
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-2.5 | Persistenza stato partita su PostgreSQL | 8 | Sprint 3 |
| P0 | US-2.6 | Endpoint GET /api/matches/:id (recupero stato) | 3 | Sprint 3 |
| P0 | US-2.7 | Endpoint DELETE /api/matches/:id (annulla partita) | 2 | Sprint 3 |
| P1 | US-3.1 | Modello database statistiche utente (stats table) | 3 | Sprint 3 |
| P1 | US-3.2 | Calcolo statistiche base (win/loss, win rate) | 5 | Sprint 3 |
| | **Totale Sprint 3** | | **21** | |

### Sprint 9 (17 Feb - 28 Feb) - Sistema Amicizie
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P2 | US-4.1 | Modello database amicizie (friendships table) | 3 | Sprint 9 |
| P2 | US-4.2 | Endpoint POST /api/friends/request (invia richiesta) | 3 | Sprint 9 |
| P2 | US-4.3 | Endpoint PUT /api/friends/request/:id/accept | 2 | Sprint 9 |
| P2 | US-4.4 | Endpoint GET /api/friends (lista amici) | 2 | Sprint 9 |
| P2 | US-4.5 | Presenza online/offline (integrazione WebSocket) | 5 | Sprint 9 |
| P3 | US-5.1 | Password recovery (reset via email) | 5 | Sprint 9 |
| | **Totale Sprint 9** | | **20** | |

**Totale Backend Server**: 80 story points (4 sprint)

---

## Product Backlog - Real-Time Communication

### Sprint 5 (23 Dic - 03 Gen) - WebSocket Foundation
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-6.1 | Setup Socket.IO server | 5 | Sprint 5 |
| P0 | US-6.2 | Gestione rooms per partite (room-based broadcast) | 5 | Sprint 5 |
| P0 | US-6.3 | Autenticazione WebSocket con JWT | 3 | Sprint 5 |
| P0 | US-6.4 | Heartbeat ogni 30s per rilevare disconnessioni | 3 | Sprint 5 |
| P1 | US-6.5 | Logging eventi WebSocket | 2 | Sprint 5 |
| | **Totale Sprint 5** | | **18** | |

### Sprint 6-7 (06 Gen - 31 Gen) - Eventi Real-Time
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-6.6 | Evento `player_joined` (giocatore entra in partita) | 2 | Sprint 6 |
| P0 | US-6.7 | Evento `game_started` (partita iniziata) | 2 | Sprint 6 |
| P0 | US-6.8 | Evento `card_played` (carta giocata da giocatore) | 5 | Sprint 6 |
| P0 | US-6.9 | Evento `hand_won` (mano vinta, punteggio aggiornato) | 5 | Sprint 6 |
| P0 | US-6.10 | Evento `game_ended` (partita terminata) | 3 | Sprint 7 |
| P0 | US-6.11 | Broadcast selettivo: eventi privati (carte in mano) | 5 | Sprint 7 |
| P1 | US-6.12 | Ottimizzazione payload (compressione JSON) | 3 | Sprint 7 |
| | **Totale Sprint 6-7** | | **25** | |

### Sprint 8 (03 Feb - 14 Feb) - Gestione Disconnessioni e Chat
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-6.13 | Disconnessione temporanea: partita sospesa (max 5 min) | 5 | Sprint 8 |
| P0 | US-6.14 | Riconnessione automatica con ripristino stato | 5 | Sprint 8 |
| P0 | US-6.15 | Disconnessione permanente: annulla partita | 3 | Sprint 8 |
| P0 | US-6.16 | Chat in-game testuale (4 giocatori) | 5 | Sprint 8 |
| P1 | US-6.17 | Throttling chat (max 1 msg/sec) + filtro parole offensive | 3 | Sprint 8 |
| P2 | US-6.18 | Indicatore latency visuale (verde/giallo/rosso) | 3 | Sprint 8 |
| | **Totale Sprint 8** | | **24** | |

**Totale Real-Time Communication**: 67 story points (4 sprint)

---

## Product Backlog - Frontend Web

### Sprint 3 (25 Nov - 06 Dic) - Setup e Homepage
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-7.1 | Setup progetto React + Vite + Tailwind CSS | 3 | Sprint 3 |
| P0 | US-7.2 | Design system: componenti base (Button, Card, Modal, Form) | 8 | Sprint 3 |
| P0 | US-7.3 | Homepage/Landing page (mockup v2) | 5 | Sprint 3 |
| P1 | US-7.4 | Pagina "Scopri le regole" (tutorial Maraffone) | 5 | Sprint 3 |
| | **Totale Sprint 3** | | **21** | |

### Sprint 4 (09 Dic - 20 Dic) - Autenticazione
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-7.5 | Form registrazione con validazione client-side | 5 | Sprint 4 |
| P0 | US-7.6 | Form login (email + password) | 3 | Sprint 4 |
| P0 | US-7.7 | Opzione "Prova come ospite" (modale) | 2 | Sprint 4 |
| P0 | US-7.8 | Gestione JWT token (store in localStorage) | 3 | Sprint 4 |
| P1 | US-7.9 | Password recovery (form + email flow) | 3 | Sprint 4 |
| | **Totale Sprint 4** | | **16** | |

### Sprint 5 (23 Dic - 03 Gen) - Dashboard/Lobby
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-7.10 | Layout dashboard (profilo + partite + amici) | 5 | Sprint 5 |
| P0 | US-7.11 | Card "Partite attive" con lista partite in corso | 5 | Sprint 5 |
| P0 | US-7.12 | Pulsanti "Crea partita" / "Unisciti a partita" | 2 | Sprint 5 |
| P0 | US-7.13 | Form creazione stanza (nome, password, inviti) | 5 | Sprint 5 |
| P1 | US-7.14 | Sidebar lista amici online (indicatori status) | 3 | Sprint 5 |
| | **Totale Sprint 5** | | **20** | |

### Sprint 6-7 (06 Gen - 31 Gen) - Tavolo da Gioco [CRITICO]
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-7.15 | Layout tavolo 4 giocatori (Nord/Sud/Est/Ovest) | 8 | Sprint 6 |
| P0 | US-7.16 | Renderizzare carte in mano (SVG o immagini) | 5 | Sprint 6 |
| P0 | US-7.17 | Click to play: seleziona carta e invia al server | 5 | Sprint 6 |
| P0 | US-7.18 | Area centrale: mostra 4 carte giocate | 3 | Sprint 6 |
| P0 | US-7.19 | Animazioni gioco carta (fly to center, 60fps) | 8 | Sprint 7 |
| P0 | US-7.20 | Timer turno con progress bar (30 secondi) | 5 | Sprint 7 |
| P0 | US-7.21 | Punteggio real-time (aggiornato dopo ogni mano) | 3 | Sprint 7 |
| P1 | US-7.22 | Indicatori latency per giocatore (colori) | 3 | Sprint 7 |
| P1 | US-7.23 | Chat in-game (collapsabile, integrata con WebSocket) | 5 | Sprint 7 |
| | **Totale Sprint 6-7** | | **45** | |

### Sprint 8 (03 Feb - 14 Feb) - Fine Partita e Mobile
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P0 | US-7.24 | Modale fine partita (vittoria/sconfitta + riepilogo) | 5 | Sprint 8 |
| P0 | US-7.25 | Pulsanti "Rivincita" / "Torna alla lobby" / "Condividi" | 3 | Sprint 8 |
| P0 | US-7.26 | Responsive design: layout verticale mobile | 8 | Sprint 8 |
| P0 | US-7.27 | Touch-friendly: pulsanti min 44×44px | 3 | Sprint 8 |
| P1 | US-7.28 | Animazioni microinterazioni (confetti vittoria) | 3 | Sprint 8 |
| | **Totale Sprint 8** | | **22** | |

### Sprint 9 (17 Feb - 28 Feb) - Social Features Frontend
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P2 | US-7.29 | Pagina profilo utente (stats + avatar) | 5 | Sprint 9 |
| P2 | US-7.30 | Lista amici (ricerca + richieste) | 5 | Sprint 9 |
| P2 | US-7.31 | Notifiche in-app (toast messages) | 3 | Sprint 9 |
| P3 | US-7.32 | Storico partite (tabella con paginazione) | 5 | Sprint 9 |
| | **Totale Sprint 9** | | **18** | |

### Sprint 10 (03 Mar - 14 Mar) - Accessibilità e Polish
| Priority | User Story ID | Task | Story Points | Status |
|----------|---------------|------|--------------|--------|
| P2 | US-7.33 | Accessibilità WCAG 2.1 AA (aria-labels, focus indicators) | 8 | Sprint 10 |
| P2 | US-7.34 | Ottimizzazione bundle size (code splitting, lazy loading) | 5 | Sprint 10 |
| P2 | US-7.35 | Performance audit (Lighthouse score > 90) | 5 | Sprint 10 |
| P3 | US-7.36 | Modalità daltonici (palette alternativa) | 3 | Sprint 10 |
| | **Totale Sprint 10** | | **21** | |

**Totale Frontend Web**: 163 story points (8 sprint)

---

## Riepilogo Effort per Sottosistema (Solo Agile)

| Sottosistema | Story Points | % del Totale | Sprint Coinvolti |
|--------------|--------------|--------------|------------------|
| Frontend Web | 163 | 38.0% | 3-10 |
| Game Engine | 94 | 21.9% | 1-8 |
| Backend Server | 80 | 18.6% | 1-3, 9 |
| Real-Time Communication | 67 | 15.6% | 5-8 |
| Infrastructure & DevOps | 37 | 8.6% | 0-6 |
| **Totale** | **441** | **100%** | |

---

## Velocity Tracking e Burn-down

### Velocity Stimata
- **Team size**: 5 persone (Elena Rossi, Sara Bianchi, Luca Moretti, Andrea Conti, Marco Venturi part-time)
- **Capacity per sprint**: ~40 story points (8 pts/persona/sprint)
- **Sprint totali**: 13
- **Capacity totale**: ~520 story points
- **Backlog totale**: 441 story points
- **Buffer**: 79 story points (15.2% contingency)

### Monitoraggio Velocity
Alla fine di ogni sprint, il team registrerà:
1. Story points completati (velocity effettiva)
2. Story points portati al sprint successivo (carryover)
3. Impedimenti e blockers
4. Aggiustamenti a stime future

**Target**: velocity stabile tra 35-45 pts/sprint dopo i primi 3 sprint di calibrazione.

---

## Definition of Done (DoD)

Un item del Product Backlog è considerato **Done** solo quando:

1. [+] Codice scritto e committed su repository
2. [+] Unit tests scritti e passati (coverage > 80%)
3. [+] Code review approvata da almeno 1 peer
4. [+] Integration tests passati
5. [+] Documentazione API/componente aggiornata
6. [+] Deploy su ambiente staging riuscito
7. [+] Acceptance criteria (da User Story) soddisfatti
8. [+] Product Owner ha approvato (demo sprint review)

---

## Gestione Cambiamenti al Backlog

### Processo di Aggiunta Nuovi Item
1. Stakeholder propone nuovo requisito
2. Product Owner (Marco Venturi) valuta con MoSCoW
3. Se approvato: team stima in story points (planning poker)
4. Item inserito nel backlog con priorità
5. Se Must Have: verificare impatto su timeline e budget

### Sprint Planning Meeting
**Quando**: Primo giorno di ogni sprint
**Partecipanti**: Tutto il team + Giovanni Marchetti (committente, opzionale)
**Output**: Sprint Backlog (item selezionati per il prossimo sprint)

### Backlog Refinement
**Frequenza**: Metà sprint (ogni settimana dispari)
**Durata**: 1 ora
**Obiettivo**: Stimare nuovi item, rivalutare priorità, dividere epics

---

## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices Agile/Scrum 2026:
- [Atlassian - Product Backlog Tips](https://www.atlassian.com/agile/scrum/backlogs)
- [Atlassian - Story Points Estimation](https://www.atlassian.com/agile/project-management/estimation)
- [Scrum Alliance - Story Point Estimation Guide](https://resources.scrumalliance.org/Article/story-point-estimation)
- [Asana - Story Points Guide 2025](https://asana.com/resources/story-points)
- [Mountain Goat Software - Agile Estimating](https://www.mountaingoatsoftware.com/agile/agile-estimation-estimating-with-story-points)

---

**Redatto da**: Marco Venturi (Product Owner, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Scrum Master / Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 25/10/2025
