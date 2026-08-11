# Allegato 4.2 - RASCI Matrix
## v.2.1.0 – 2026-08-10

> La RASCI Matrix è disponibile anche come companion visivo `Allegato4.2-RASCI.html` (matrice colorata attività × ruoli, con legenda R/A/S/C/I): apri il file nel browser e usa "Stampa → Salva come PDF". Questo documento `.md` resta il registro testuale completo (matrice per sottosistema, note e analisi delle responsabilità).

Questo documento definisce le **responsabilità del team** per ogni attività del progetto MaraffaOnline. Le regole di collaborazione quotidiana (problem solving, decision making, conflict resolution, brainstorming e cerimonie di team) sono nell'**Allegato 4.3 - Regole Operative**.

---

## Cos'è la RASCI Matrix

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

**Granularità**: la matrice assegna le responsabilità a **livello di attività della WBS** (Allegato 3.1), raggruppando in un'unica riga le attività con distribuzione di ruoli identica; i 160 task di dettaglio **ereditano la riga dell'attività** a cui appartengono, mentre le attività con una distribuzione diversa — le eccezioni volute, come la validazione delle regole con l'esperta, la UAT, il badge system o il disaster recovery plan — hanno una **riga dedicata**. Una matrice per singolo task ripeterebbe lo stesso schema di ruoli decine di volte, seppellendo proprio le eccezioni che la RASCI deve far risaltare.

---

## Ruoli del Team

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

## RASCI Matrix Dettagliata

### 1. Game Engine (Waterfall)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Implementazione delle regole di gioco — struttura dati e mazzo, distribuzione, ordine di forza, presa e turni (4 di Denari), punteggi (11pt interi/smazzata), Maraffa/Cricca, condizioni di vittoria, validazione mosse (WBS 1.1.1-1.1.5)** | I | C | I | A/R | S | - | - |
| **Detection casi edge (abbandono, timeout)** | I | - | I | A/R | S | - | - |
| **Validazione regole con Francesca (Sessione 1)** | A | R | S | C | C | - | - |

**Accountable e Responsible Principale**: Elena Rossi (Tech Lead / Game Engine Specialist) — sul Game Engine i due ruoli coincidono deliberatamente: è la specialista che implementa il sottosistema (vedi WBS e Gantt) e in un team di cinque la sovrapposizione A/R è accettata, bilanciata dal supporto di Sara, dalla code review e dalla validazione esterna delle regole
**Support**: Sara Bianchi (integrazione con il Backend Server)
**Consulted Critico**: Francesca Giuliani (Domain Expert)
**Unit e integration test del Game Engine**: vedi sezione 7 (Testing & QA)

---

### 2. Backend Server (Agile Iterativo)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **API di gioco e schema dati — registrazione e accesso ospite, stanze e lobby, avvio partita, middleware, tabelle DB, integration test (WBS 2.1.1, 2.2, 2.3.1)** | I | - | I | A | R | - | - |
| **Setup e task infra-related — progetto Node.js/Express, PostgreSQL, login JWT, rate limiting, migration scripts (supporto DevOps)** | I | - | I | A | R | - | S |
| **API con impatto sull'interfaccia — profili, statistiche, leaderboard, amicizie, documentazione Swagger (frontend consultato — WBS 2.1.2, 2.2.3)** | I | - | I | A | R | C | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend Developer)
**Support**: Andrea Conti (per infra-related tasks)

---

### 3. Real-Time Communication (Agile Adattivo)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Setup Socket.IO, PoC latenza (<500ms), load testing 100 partite e monitoring latency (supporto DevOps — WBS 3.1.1)** | I | - | I | A | R | - | S |
| **Eventi WebSocket di gioco, chat in-game (throttling 1 msg/s + filtro) e notifiche real-time (frontend consultato per l'integrazione — WBS 3.1.2)** | I | - | I | A | R | C | - |
| **Sincronizzazione stato 4 client (supporto frontend — WBS 3.2.1)** | I | - | I | A | R | S | - |
| **Gestione disconnessioni e reconnection (heartbeat 30s, sospensione max 5 min)** | I | - | I | A | R | - | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend Developer)
**Consulted**: Luca Moretti (per integration frontend)
**Support**: Andrea Conti (load testing, monitoring)

---

### 4. Frontend Web (Agile Iterativo)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Schermate con scelte UX condivise con lo sponsor — design system, homepage, dashboard, sala d'attesa, rendering carte (40 asset), fine partita, profili, leaderboard, responsive design (WBS 4.1.1-4.1.3, 4.1.5, 4.2.1)** | C | - | I | A | - | R | - |
| **Lobby: creazione partita e lista partite disponibili (sponsor consultato, supporto DevOps)** | C | - | I | A | - | R | S |
| **Componenti tecnici UI — form login, Tailwind, animazioni, indicatore turno, toast, accessibilità WCAG 2.1 AA, unit test Vitest (WBS 4.2.2, 4.3)** | I | - | I | A | - | R | - |
| **Setup progetto React + Vite e cross-browser testing (supporto DevOps)** | I | - | I | A | - | R | S |
| **Tavolo da gioco virtuale (sponsor e domain expert consultati; supporto backend sui componenti complessi — WBS 4.1.4)** | C | C | I | A | S | R | - |
| **Interazione giocata carta (click to play) + animazioni (supporto backend)** | I | - | I | A | S | R | - |
| **Visualizzazione punteggio real-time (domain expert consultata)** | I | C | I | A | S | R | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Luca Moretti (UX Designer / Frontend Developer)
**Support**: Sara Bianchi (per componenti complessi React), Andrea Conti (cross-browser testing)
**Consulted**: Giovanni Marchetti (UX decisions), Francesca Giuliani (rendering corretto carte/punteggi)

---

### 5. Social & Community (Incrementale)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Feature social — sistema amicizie e presenza online, storico partite, salvataggio replay (WBS 2.2.3.1), leaderboard e filtri (sponsor consultato sulle priorità — WBS 5.1, 5.2)** | C | - | I | A | R | S | - |
| **Badge/achievement system (opzionale MVP — decisione di priorità di prodotto: Accountable è il PM)** | C | - | A | C | R | S | - |

**Accountable Principale**: Elena Rossi (Tech Lead)
**Responsible Principale**: Sara Bianchi (Backend) + Luca Moretti (Frontend)
**Consulted**: Giovanni Marchetti (feature priority)

---

### 6. Infrastructure & DevOps (Incrementale)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Infrastruttura e ambienti — server Hetzner, Docker, staging/production, SSL, DNS, Cloudflare, backup, uptime monitoring, hardening (WBS 6.1, 6.3.1, 6.4.1)** | I | - | I | A | - | - | R |
| **GitLab repository e pipeline CI/CD (supporto backend e frontend — WBS 6.2)** | I | - | I | A | S | S | R |
| **Error tracking e log aggregation — Sentry, Winston (supporto backend — WBS 6.3)** | I | - | I | A | S | - | R |
| **Disaster recovery plan (natura gestionale: Accountable è il PM)** | I | - | A | C | - | - | R |

**Accountable**: Marco Venturi (PM) per disaster recovery, Elena Rossi (Tech Lead) per setup tecnici
**Responsible Principale**: Andrea Conti (DevOps Engineer)
**Consulted**: Elena Rossi (decisioni architetturali)
**Support**: Sara Bianchi (backend integration), Luca Moretti (frontend deployment)

---

### 7. Testing & QA (Continuo)

| Attività | GM | FG | MV | ER | SB | LM | AC |
|------|----|----|----|----|----|----|-----|
| **Unit e integration test Game Engine (Jest, >90% coverage; casi edge)** | I | C | I | A/R | S | - | - |
| **Unit e integration test API Backend (Jest)** | I | - | I | A | R | - | - |
| **Unit test componenti Frontend e accessibility testing (Vitest; WCAG 2.1 AA)** | I | - | I | A | - | R | - |
| **Integration test end-to-end (Cypress; supporto backend e frontend)** | I | - | I | A | S | S | R |
| **Load testing (k6, 100 partite simultanee) e security testing (SQL injection, XSS)** | I | - | I | A | S | - | R |
| **Cross-browser testing (BrowserStack; supporto DevOps)** | I | - | I | A | - | R | S |
| **User Acceptance Testing: recruitment 10 tester** | A | S | R | C | - | - | - |
| **UAT: preparazione test plan** | A | C | R | S | - | S | - |
| **UAT: esecuzione sessioni test** | A | R | S | C | - | - | - |
| **UAT: raccolta feedback** | A | R | R | C | - | - | - |
| **Bug fixing post-UAT (tutti i developer)** | I | C | I | A | R | R | R |
| **Validazione finale regole (Sessione 2)** | A | R | S | C | C | - | - |

**Accountable UAT**: Giovanni Marchetti (sponsor approval)
**Responsible UAT Execution**: Francesca Giuliani (conduce sessioni con tester)
**Responsible Test Plan**: Marco Venturi (PM)
**Responsible Bug Fixing**: Tutti i developer (ER, SB, LM, AC)

---

### 8. Project Management (Trasversale)

| Attività | GM | FG | MV | ER | SB | LM | AC |
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

## Approvazione

La RASCI Matrix è stata presentata e approvata durante il **Project Kick-Off Meeting del 15/10/2025** (Allegato 4.1), insieme alle Regole Operative (Allegato 4.3). Le assegnazioni sono un **living document**: le variazioni vengono discusse in Sprint Retrospective, approvate dal Project Manager e versionate su Notion.

---

<!-- Fonti consultate per la redazione della matrice (link a materiale divulgativo, non citabili come bibliografia del corso): AIHR - RACI Template Guide; TeamGantt - RACI Chart Guide; Atlassian - RACI Chart; project-management.com - RACI Matrix. Registro in Relazione/_appunti-per-relazione.md. -->

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)

**Versione**: v.2.1.0
**Prossimo review**: 19/12/2025 (venerdì, fine Sprint 4 — Milestone M2)

**Storico revisioni**:
- **v.2.1.0**: **potatura alla granularità di attività**. La matrice passa da una riga per task (124 righe, con l'82% delle righe che ripeteva una distribuzione di ruoli identica a un'altra) a una riga per attività della WBS o gruppo di attività con ruoli identici (51 righe): nessuna assegnazione è cambiata — ogni distribuzione di ruoli presente nella versione precedente conserva una riga — ma le eccezioni volute (validazione regole, UAT, badge system, disaster recovery) ora risaltano invece di annegare nella ripetizione. Aggiunta la nota "Granularità" e i riferimenti WBS nelle etichette.
- **v.2.0.0**: separazione dei due artefatti. Le Regole Operative, prima raccolte nella Parte 2 di questo documento, sono ora nell'**Allegato 4.3 - Regole Operative** (in forma schematica): la matrice e le regole di collaborazione hanno destinatari e cicli di aggiornamento diversi, e tenerle insieme produceva un allegato di 14 pagine. Rimossa la legenda colori (ridondante con il companion HTML) e l'introduzione alla Parte 2. Matrice invariata nella sostanza.
- **v.1.4.0**: revisione di coerenza con WBS/Gantt. Corretta l'inversione dei ruoli sul Game Engine: Responsible è Elena Rossi (Game Engine Specialist, come da Allegato 2.1 e assegnazioni WBS/Gantt), non Sara Bianchi — che negli stessi sprint è già Responsible del Backend; sul Game Engine Elena cumula A/R con Sara a supporto. Ruolo di Elena corretto da "Backend Developer" a "Game Engine Specialist". Load testing allineato al criterio delle Conditions of Satisfaction: 100 partite simultanee (era 50). Cross-browser esteso a Edge (come da CoS) e interazione carta uniformata al Backlog (click to play, non drag & drop).
- **v.1.3.0**: snellimento anti-ridondanza. L'analisi RASCI è stata sintetizzata (rimossi i conteggi esaustivi per persona e la nota "Balanced Workload", sostituiti da una descrizione qualitativa della distribuzione R/A/C). Matrice per sottosistema invariata nella sostanza.
- **v.1.2.0**: assegnato un Accountable a tutte le righe della matrice (ogni attività ha ora esattamente un Accountable) e ricalcolati i conteggi di responsabilità; refusi corretti.
