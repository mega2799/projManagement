# Allegato 4.1 - Project Kick-Off Meeting
## v.1.1.0 – 15/10/2025 10:00-11:00

Il **Project Kick-Off Meeting** segna l'inizio ufficiale della fase di esecuzione del progetto MaraffaOnline. Questo meeting rappresenta il momento in cui il team di progetto si allinea su obiettivi, ruoli, responsabilità e regole operative, trasformando la pianificazione in azione.

---

## Informazioni Generali

**Data**: 15 ottobre 2025
**Ora**: 10:00 - 11:00 (1 ora)
**Luogo**: Sala Riunioni PlayHeritage Labs + Zoom (ibrido)
**Facilitatore**: Marco Venturi (Project Manager)
**Scribe**: Andrea Conti (DevOps Engineer)

---

## Partecipanti

### Project Team (PlayHeritage Labs)

| Nome | Ruolo | Presenza |
|------|-------|----------|
| **Marco Venturi** | Project Manager | In presenza |
| **Elena Rossi** | Tech Lead / Backend Developer | In presenza |
| **Sara Bianchi** | Backend Developer | In presenza |
| **Luca Moretti** | UX Designer / Frontend Developer | In presenza |
| **Andrea Conti** | DevOps Engineer | In presenza |

### Stakeholder

| Nome | Ruolo | Presenza |
|------|-------|----------|
| **Giovanni Marchetti** | Project Sponsor (Maraffa Forever) | Remoto (Zoom) |
| **Francesca Giuliani** | Domain Expert (Maraffa Forever) | Remoto (Zoom) |

**Assenti**: Nessuno

---

## Pre-Meeting Materials Distribuiti

I seguenti documenti sono stati condivisi con tutti i partecipanti 3 giorni prima del meeting (12/10/2025):

1. **Project Overview Statement (POS)** - Scoping/Allegato2.3
2. **Work Breakdown Structure (WBS)** - Planning/Allegato3.1
3. **Gantt Chart e Critical Path** - Planning/Allegato3.5
4. **Cash Flow Management** - Planning/Allegato3.4
5. **RASCI Matrix** (bozza) - Launching/Allegato4.2
6. **Regole Operative** (bozza) - Launching/Allegato4.2

**Obiettivo pre-lettura**: Tutti i partecipanti arrivano preparati con domande/commenti specifici, riducendo il tempo di presentazione durante il meeting.

---

## Agenda del Meeting

### 1. Apertura e Benvenuto (5 minuti) - Marco Venturi

**Obiettivo**: Creare un clima positivo e collaborativo

**Contenuti**:
- Ringraziamento ai partecipanti per la presenza
- Breve storia del progetto: dalla proposta di Maraffa Forever alla firma del contratto (30 settembre 2025)
- Importanza strategica per PlayHeritage Labs: primo progetto di valorizzazione giochi tradizionali italiani
- Celebrazione: questo è l'inizio ufficiale di un'avventura a cui tutti teniamo

**Quote del PM**:
> "Oggi trasformiamo la pianificazione in azione. Nei prossimi 7 mesi il nostro obiettivo è portare il Maraffone, gioco che ha unito generazioni di appassionati, nell'era digitale senza perdere l'anima del gioco tradizionale."

---

### 2. Introduzione Partecipanti e Ruoli (10 minuti)

**Obiettivo**: Tutti conoscono tutti e comprendono le responsabilità di ciascuno

**Formato**: Giro di tavolo (2 minuti/persona)

Ogni partecipante si presenta seguendo questo template:
- Nome + Ruolo
- Background rilevante (esperienza con progetti simili)
- Responsabilità principali su MaraffaOnline
- Una skill che porto al team
- Una cosa che spero di imparare da questo progetto

**Esempio - Elena Rossi**:
> "Sono Elena, Tech Lead del progetto. Ho 8 anni di esperienza in architettura backend, ultimo progetto Node.js + PostgreSQL per piattaforma e-learning. Su MaraffaOnline sono responsabile della progettazione tecnica complessiva e dello sviluppo backend. Porto esperienza in sistemi scalabili, spero di imparare di più su WebSocket e real-time gaming."

**Output**: RASCI Matrix condivisa a schermo durante le presentazioni per visualizzare le responsabilità

---

### 3. Project Vision e Obiettivi (10 minuti) - Marco Venturi

**Obiettivo**: Alignment su "perché stiamo facendo questo progetto"

#### 3.1 Il Problema

**Contesto**: La community Maraffa Forever (150 appassionati, età media 35 anni) è dispersa geograficamente e fatica a organizzare partite in presenza. Durante COVID-19 hanno provato soluzioni generiche (Tabletop Simulator, Discord + carte fisiche via webcam) ma l'esperienza era insoddisfacente.

**Need Statement**:
> "I giocatori di Maraffa hanno bisogno di una piattaforma dedicata che rispetti le regole ufficiali del Maraffone/Beccaccino e offra un'esperienza fluida per giocare online con amici, perché le soluzioni attuali non supportano le meccaniche specifiche del gioco e rendono frustrante l'esperienza."

#### 3.2 La Soluzione (Goal)

**Goal del Progetto**:
> Sviluppare **MaraffaOnline**, piattaforma web responsive per giocare a Maraffa in modalità multiplayer (4 giocatori), con regole ufficiali Maraffone/Beccaccino, sistema lobby, chat integrata e profili personalizzabili. Lancio MVP entro 15 maggio 2026 (7 mesi).

#### 3.3 Criteri di Successo (Success Metrics)

I criteri sono stati concordati con Giovanni Marchetti durante la fase di Scoping:

| Criterio | Target MVP | Misurazione |
|----------|------------|-------------|
| **Funzionalità** | 100% regole Maraffone implementate correttamente | Validazione con Francesca Giuliani + 10 tester community |
| **Performance** | Latenza < 500ms per azioni real-time | Load testing con 50 partite simultanee |
| **Usabilità** | 80% utenti completano prima partita senza aiuto | User testing con 10 membri Maraffa Forever |
| **Tempo** | Lancio MVP entro 15/05/2026 (7 mesi) | Rispetto Gantt Chart critical path (170 giorni lavorativi) |
| **Budget** | Spese entro €22.750 (91% di €25.000) | Cash flow tracking settimanale |
| **Adozione** | 50 utenti attivi settimanalmente dopo 1 mese dal lancio | Google Analytics + database query |

**Celebrazione**: Se raggiungiamo tutti i target, celebriamo con torneo inaugurale Maraffa Forever (online su MaraffaOnline!)

---

### 4. Scope e Deliverable (10 minuti) - Elena Rossi

**Obiettivo**: Chiarezza assoluta su cosa è dentro/fuori dal MVP

#### 4.1 In-Scope: i 6 sottosistemi di sviluppo dell'MVP + Testing & QA

I giorni indicano l'**effort totale stimato per sottosistema** (Must + Should + Could inclusi nell'MVP), come da Allegato 3.2 - MoSCoW.

1. **Game Engine** (Waterfall) - 50 giorni
   - Logica Maraffone completa (distribuzione, turni, punteggio, vittoria)
   - Gestione Maraffa/Cricca (Asso+2+3 briscola = +3pt)
   - Validazione mosse legali

2. **Backend Server** (Agile Iterativo) - 70 giorni
   - Autenticazione JWT (registrazione, login, guest)
   - API REST per gestione partite/lobby
   - Database PostgreSQL (utenti, partite, statistiche)

3. **Real-Time Communication** (Agile Adattivo) - 45 giorni
   - WebSocket con Socket.IO
   - Sincronizzazione stato partita 4 giocatori
   - Notifiche eventi real-time (turno, carte giocate)

4. **Frontend Web** (Agile Iterativo) - 76 giorni
   - UI responsive (desktop priority, tablet supportato)
   - Tavolo da gioco virtuale con drag & drop carte
   - Lobby, profili, statistiche personali

5. **Social & Community** (Incrementale) - 24 giorni
   - Sistema amicizie
   - Lista partite recenti con replay
   - Leaderboard community

6. **Infrastructure & DevOps** (Incrementale) - 37 giorni
   - Deploy Docker su Hetzner
   - CI/CD GitLab
   - Monitoring (Sentry, UptimeRobot)

7. **Testing & QA** (Continuo) - 20 giorni UAT
   - Unit test (Jest, Vitest)
   - Integration test
   - User Acceptance Testing con Maraffa Forever

**Nota sugli effort**: la somma degli effort dei 6 sottosistemi di sviluppo è di circa 302 giorni-uomo; grazie al parallelismo tra sottosistemi (vedi Project Network Diagram, Allegato 3.5) il progetto si completa in **170 giorni lavorativi sul Critical Path** (~7 mesi di calendario).

#### 4.2 Out-of-Scope (Won't Have in MVP)

**Esplicitamente escluso dal MVP v1.0**:
- App mobile nativa iOS/Android (solo web responsive)
- Modalità single-player contro AI
- Tornei automatici con bracket
- Monetizzazione (abbonamenti Premium)
- Internazionalizzazione (solo italiano nel MVP)
- Integrazione social login (Facebook, Google)
- Voice chat (solo chat testuale)

**Razionale**: Focus su core experience multiplayer per validare product-market fit. Feature avanzate spostate a v1.1+ post-lancio.

**Gestione Scope Creep**: Qualsiasi nuovo requisito NON previsto nel POS richiede Change Request Process formale (vedi Regole Operative).

---

### 5. Timeline e Milestone (10 minuti) - Marco Venturi

**Obiettivo**: Tutti comprendono quando succede cosa e le date critiche

#### 5.1 Fasi del Progetto

**Overview 7 mesi**:

```
Ott 2025      Nov 2025 - Feb 2026    Mar 2026       Apr-Mag 2026
│             │                      │              │
Setup         Sviluppo core          MVP Beta       UAT + Lancio
Sprint 0      Sprint 1-8             Sprint 9-11    Sprint 12-14
│             │                      │              │
Kick-off      M2 → M3                M4 → M5        M6 → M7 (LANCIO)
15/10         20/12 → 31/01          14/03 → 31/03  24/04 → 15/05
```

#### 5.2 Milestone Critiche

Le milestone tecniche seguono il Project Network Diagram e il Gantt (Allegato 3.5):

| Milestone | Data | Deliverable | Owner |
|-----------|------|-------------|-------|
| **M1: Infrastructure Ready** | 25/10/2025 | Server + CI/CD operativi | Andrea Conti |
| **M2: Backend Core Complete** | 20/12/2025 | Auth + gestione partite + persistenza | Elena Rossi |
| **M3: Game Engine Complete** | 31/01/2026 | Regole Maraffone implementate e validate | Elena Rossi |
| **M4: Frontend Core Complete** | 14/03/2026 | Homepage + Dashboard + Tavolo da gioco | Luca Moretti |
| **M5: MVP Beta** | 31/03/2026 | Tutte le feature Must Have integrate e testate internamente | Marco Venturi |
| **M6: UAT Approved** | 24/04/2026 | Approvazione community (10 tester) | Giovanni Marchetti |
| **M7: Public Launch** | 15/05/2026 | Deploy produzione + Lancio community | Marco Venturi |

**Pagamenti** (struttura 50/25/25, dettaglio in Allegato 3.4 - Cash Flow):
- **1° pagamento** €12.500 (50%) — 15/10/2025, alla firma del contratto e kickoff
- **2° pagamento** €6.250 (25%) — 15/12/2025, a valle del Backend Core (M2)
- **3° pagamento** €6.250 (25%) — 15/02/2026, a metà progetto

**Slack Time**: 0 giorni sul Critical Path → ogni ritardo impatta direttamente la data di lancio

**Critical Path Awareness**: L'attività più critica è **Frontend Tavolo da Gioco (40 giorni, Sprint 8-11)**. Luca Moretti sarà dedicato full-time con supporto di Sara Bianchi per componenti complessi.

#### 5.3 Sprint Calendar (Agile Subsystems)

**15 Sprint da 2 settimane** (15/10/2025 - 15/05/2026):

- **Sprint 0** (15-25 Ott): Setup + Scoping finalization
- **Sprint 1-4** (28 Ott - 20 Dic): Backend + Real-Time foundation
- **Sprint 5-8** (23 Dic - 14 Feb): Frontend core + Integration
- **Sprint 9-11** (17 Feb - 31 Mar): Feature completion + Bug fixing
- **Sprint 12** (01 - 24 Apr): UAT con Maraffa Forever
- **Sprint 13-14** (27 Apr - 15 Mag): Polish + Production Launch

**Cerimonie Agile** (da Sprint 1):
- **Daily Standup**: Ogni giorno 09:00-09:15 (in presenza/Zoom)
- **Sprint Planning**: Primo lunedì dello sprint, 09:00-10:30
- **Sprint Review**: Ultimo venerdì dello sprint, 14:00-15:00 (con Giovanni Marchetti remoto)
- **Sprint Retrospective**: Ultimo venerdì dello sprint, 15:00-16:00 (solo team interno)

**Product Backlog Velocity**: Target 40 story points/sprint (basato su stima Planning Poker)

---

### 6. Budget e Risorse (5 minuti) - Marco Venturi

**Obiettivo**: Trasparenza finanziaria e vincoli di risorse

#### 6.1 Budget Overview

**Budget Totale**: €25.000
**Spese Pianificate**: €22.750 (91%)
**Surplus/Contingency**: €2.250 (9%)

**Breakdown per Categoria**:
- **Salari Team** (64%): €16.000 - 5 persone × 7 mesi FTE part-time (compenso ridotto coerente con natura spin-off accademico)
- **Infrastruttura** (1.1%): €275 - Hetzner server €50/mese
- **Tools e Licenze** (4.4%): €1.111 - Figma, JetBrains, Zoom, Confluence
- **Consulenza** (1.2%): €300 - Francesca Giuliani (validazione regole)
- **Marketing, UAT e Celebrazione** (1.6%): €400 - comunicazione lancio, compenso tester, team celebration
- **Contingency Buffer** (18.7%): €4.664 - Imprevisti + change requests + buffer estensione progetto 7 mesi

**Cash Flow**: Vedi Allegato 3.4. Saldo minimo €2.250 nel Mese 7 (prima metà Maggio 2026), sempre positivo.

**Tracking**: Report mensile a Giovanni Marchetti entro il 5 di ogni mese.

#### 6.2 Allocazione Risorse Team

**Commitment Time** (15 Ott 2025 - 15 Mag 2026):

| Team Member | Mese 0 (Ott) | Mesi 1-6 (Nov-Apr) | Mese 7 (Mag) | Totale FTE |
|-------------|--------------|---------------------|--------------|------------|
| Marco Venturi (PM) | 50% | 100% | 50% | 7 mesi FTE |
| Elena Rossi (Tech Lead) | 50% | 100% | 50% | 7 mesi FTE |
| Sara Bianchi (Backend) | 50% | 100% | 50% | 7 mesi FTE |
| Luca Moretti (Frontend/UX) | 50% | 100% | 50% | 7 mesi FTE |
| Andrea Conti (DevOps) | 50% | 100% | 50% | 7 mesi FTE |

**Razionale part-time Mese 0 e Mese 7**: Setup iniziale e fase UAT finale richiedono meno intensità. Ottimizzazione costi.

**External Resources**:
- **Francesca Giuliani**: 2 sessioni di validazione regole (3h ciascuna) - Novembre 2025 e Aprile 2026
- **Tester Community**: 10 membri Maraffa Forever per UAT (compenso simbolico €10 ciascuno)

---

### 7. Rischi e Assunzioni (5 minuti) - Elena Rossi

**Obiettivo**: Awareness condivisa dei rischi TOP 5 e piani di mitigazione

#### 7.1 Top 5 Risks (da Risk Rating Matrix - Allegato 2.4)

| Rischio | Probabilità | Impatto | Rating | Mitigazione |
|---------|-------------|---------|--------|-------------|
| **R1: Esperienza limitata con WebSocket / real-time** | Alta (4) | Disastroso (4) | 16 (Rosso Critico) | Spike tecnico di 2 settimane (Sprint 0-1) + PoC Socket.IO in Sprint 2. Decision point al giorno 30: se non risolto, consulente esterno Dr. Stefano Nardi (budget €2.000). Load testing anticipato Sprint 6. |
| **R2: Budget insufficiente per il team** | Alta (4) | Disastroso (4) | 16 (Rosso Critico) | Accept: progetto pilota a valore strategico. Team part-time (50% FTE), compensi ridotti coerenti con la natura di spin-off accademico. Buffer di contingenza monitorato settimanalmente. |
| **R3: Race conditions e sincronizzazione dello stato** | Media-Alta (3) | Disastroso (4) | 12 (Rosso) | Architettura server-authoritative. Code review obbligatoria sul modulo real-time. Test di concorrenza con 4 client simulati. |
| **R4: Scope creep da richieste del committente** | Media-Alta (3) | Disastroso (4) | 12 (Rosso) | MoSCoW rigoroso. Change Request Process formale. Freeze requisiti dopo il POS. Giovanni informato che nuovi requisiti → estensione timeline o riduzione scope. |
| **R5: Sottostima della complessità tecnica** | Media-Alta (3) | Grave (3) | 9 (Rosso) | Sviluppo agile iterativo. Buffer 20% sulle stime. Se ritardo >15% a metà progetto: riduzione dello scope (Could/Should). |

**Responsabile Risk Management**: Marco Venturi
**Frequenza Review**: Settimanale durante Project Status Meeting (ogni venerdì 16:00)

#### 7.2 Assunzioni Critiche

Le seguenti assunzioni sono alla base del piano. Se invalidate, richiedono re-pianificazione:

1. **Tecnologia**: Stack Node.js + React + Socket.IO è adeguato per 50 partite simultanee (testato in POC)
2. **Regole**: Le regole Maraffone documentate in `Scoping/REGOLE-UFFICIALI-MARAFFONE.md` sono corrette e complete (validate da Francesca Giuliani)
3. **Disponibilità Team**: Nessun membro avrà assenze prolungate (>5 giorni consecutivi) durante Mesi 1-4
4. **Infrastruttura**: Server Hetzner €50/mese è sufficiente per carico MVP (max 200 utenti concorrenti)
5. **Stakeholder**: Giovanni Marchetti approva deliverable entro 3 giorni lavorativi da submission

**Processo di Gestione**: Se un'assunzione viene invalidata, escalation immediata a Marco Venturi → meeting straordinario con Giovanni Marchetti → decisione go/no-go entro 48h.

---

### 8. Comunicazione e Strumenti (5 minuti) - Andrea Conti

**Obiettivo**: Tutti sanno dove trovare informazioni e come comunicare

#### 8.1 Communication Plan

**Canali Ufficiali**:

| Tipo Comunicazione | Strumento | Frequenza | Partecipanti |
|--------------------|-----------|-----------|--------------|
| **Daily Standup** | Zoom + Slack #daily | Ogni giorno 09:00-09:15 | Team interno (5 persone) |
| **Sprint Review** | Zoom | Ogni 2 settimane (venerdì 14:00) | Team + Giovanni Marchetti |
| **Project Status Meeting** | Zoom | Settimanale (venerdì 16:00) | Team + Giovanni Marchetti |
| **Monthly Cash Flow Report** | Email + Google Sheets | Mensile (entro il 5) | Marco → Giovanni |
| **Urgent Issues** | Telefono + Slack #urgent | On-demand (risposta < 2h) | Chiunque → Marco |
| **Change Requests** | Email formale + Confluence | On-demand | Giovanni → Marco |

**Response Time SLA**:
- **Urgent** (blocker produzione): < 2 ore
- **High** (impedisce lavoro): < 4 ore
- **Medium** (rallenta lavoro): < 1 giorno
- **Low** (nice to have): < 3 giorni

#### 8.2 Strumenti di Lavoro

**Piattaforme Condivise**:

| Strumento | Utilizzo | Owner | Accesso |
|-----------|----------|-------|---------|
| **GitLab** | Code repository + CI/CD | Andrea Conti | Team interno |
| **Confluence** | Documentazione PM + tecnica | Marco Venturi | Team + Giovanni (read-only) |
| **Figma** | Design mockup + prototype | Luca Moretti | Team + Giovanni (view) |
| **Notion Database** | Gantt Chart + task tracking | Marco Venturi | Team + Giovanni (view) |
| **Google Sheets** | Cash flow tracking | Marco Venturi | Team + Giovanni (read-only) |
| **Slack Workspace** | Chat team (canali: #general, #dev, #daily, #urgent) | Andrea Conti | Team interno |
| **Zoom** | Meeting video | Marco Venturi | Team + Giovanni |

**Onboarding**: Andrea Conti invia inviti a tutte le piattaforme entro 16/10/2025 EOD.

#### 8.3 Documentation Standards

**Confluence Structure**:
```
MaraffaOnline/
├── Project Management/
│   ├── Scoping/ (Allegati 2.1-2.12)
│   ├── Planning/ (Allegati 3.1-3.5)
│   ├── Launching/ (Allegati 4.1-4.2)
│   └── Status Reports/ (weekly updates)
├── Technical Documentation/
│   ├── Architecture/
│   ├── API Specifications/
│   └── Database Schema/
└── Meeting Notes/
    ├── Daily Standups/
    ├── Sprint Reviews/
    └── Retrospectives/
```

**Regola d'Oro**: "Se non è documentato su Confluence, non esiste." Ogni decisione importante va tracciata.

---

### 9. Regole Operative e RASCI Matrix (5 minuti) - Marco Venturi

**Obiettivo**: Chiarezza su processi decisionali e responsabilità

#### 9.1 RASCI Matrix Overview

**Riferimento**: Vedi Allegato 4.2 - RASCI Matrix per assegnazioni dettagliate

**Principi Chiave**:
- **R (Responsible)**: Chi esegue l'attività (può essere multiplo)
- **A (Accountable)**: Chi approva il risultato (DEVE essere uno solo per attività)
- **S (Support)**: Chi fornisce supporto al Responsible
- **C (Consulted)**: Chi viene consultato per expertise
- **I (Informed)**: Chi viene informato dello stato

**Esempio dal nostro progetto**:
- **Task**: Implementazione logica punteggio Maraffone
  - **R**: Sara Bianchi (scrive il codice)
  - **A**: Elena Rossi (approva code review)
  - **S**: -
  - **C**: Francesca Giuliani (valida correttezza regole)
  - **I**: Marco Venturi, Giovanni Marchetti

**Escalation Path**:
1. Issue → Responsible tenta di risolvere
2. Se blocco → Accountable decide
3. Se conflitto → Project Manager decide
4. Se impatto budget/scope/timeline → Sponsor decide

#### 9.2 Decision Making Framework

**Livelli di Decisione**:

| Livello | Tipo Decisione | Decision Maker | Esempio |
|---------|----------------|----------------|---------|
| **Operativo** | Implementazione tecnica quotidiana | Responsible (dev team) | Scelta libreria CSS, naming variabili |
| **Tattico** | Scelte architetturali | Tech Lead (Elena) + PM approval | Database schema, API design |
| **Strategico** | Scope, budget, timeline | PM + Sponsor | Change request, estensione milestone |

**Regola**: Ogni decisione deve essere presa al livello più basso possibile. Escalation solo se impatta livelli superiori.

#### 9.3 Conflict Resolution

**Processo in 3 step**:
1. **Direct Discussion** (entro 24h): Le parti coinvolte parlano direttamente
2. **Facilitated Mediation** (entro 48h): Marco Venturi facilita discussione
3. **Executive Decision** (entro 72h): Elena Rossi (Tech Lead) o Giovanni Marchetti (Sponsor) decide

**Tip**: "Disagree and commit". Dopo una decisione, il team si allinea anche se non tutti sono d'accordo.

---

### 10. Q&A e Chiarimenti (10 minuti)

**Obiettivo**: Rispondere a tutte le domande/dubbi dei partecipanti

**Domande raccolte**:

**Q1 (Giovanni Marchetti)**: "Come garantite che le regole implementate siano davvero quelle del Maraffone e non di varianti regionali?"

**A1 (Elena Rossi)**: "Abbiamo creato un documento di riferimento ufficiale (`REGOLE-UFFICIALI-MARAFFONE.md`) basato su 4 fonti autorevoli (Wikipedia, Giochi STARS, Cavallore, Blog Bartolini). Francesca Giuliani validerà l'implementazione a metà sviluppo (Novembre) e nella fase finale del progetto (Aprile). Inoltre, durante lo Sprint Review 6 (fine Dicembre) faremo una demo live con te e Francesca per conferma."

---

**Q2 (Luca Moretti)**: "Ho notato che il Frontend Tavolo da Gioco è sul critical path con 40 giorni. È realistico? Mi preoccupa."

**A2 (Marco Venturi + Elena Rossi)**: "È la task più critica, hai ragione. Abbiamo preso 3 misure di mitigazione: (1) I mockup sono già approvati in fase Scoping, quindi zero incertezza su design. (2) Sara Bianchi farà pair programming con te per i componenti React complessi (drag & drop carte, animazioni). (3) Se necessario, comprimeremo UAT da 20 a 15 giorni per recuperare slack. Avrai supporto full-time."

**A2-bis (Elena)**: "Inoltre, ho già identificato 2 librerie candidate per drag & drop (react-dnd, dnd-kit) che semplificheranno molto. Le testiamo in Sprint 1 anche se il tavolo inizia in Sprint 8."

---

**Q3 (Andrea Conti)**: "Per il monitoring, Sentry free tier è sufficiente o rischiamo di sforare i 10K eventi/mese?"

**A3 (Marco Venturi)**: "Abbiamo budget contingency. Se in Sprint 6-7 vediamo che siamo vicini al limite, upgradiamo a piano Business (~€25/mese). È coperto dal buffer. Meglio avere monitoring completo che risparmiare ~€150 totali e perdere visibilità su bug."

---

**Q4 (Francesca Giuliani)**: "Quando esattamente mi chiamate per le validazioni?"

**A4 (Elena Rossi)**: "Ti contattiamo per 2 sessioni da 3 ore ciascuna:
- **Sessione 1**: Fine Novembre 2025 (dopo Sprint 2) - Validazione logica di gioco implementata
- **Sessione 2**: Aprile 2026 - Test end-to-end partita completa
Ti confermiamo date precise almeno 2 settimane prima. Compenso €300 totale (€150/sessione)."

---

**Q5 (Sara Bianchi)**: "Chi decide le priorità all'interno di uno sprint se ci sono conflitti tra feature?"

**A5 (Marco Venturi)**: "Product Backlog è già prioritizzato (MoSCoW in Allegato 3.2). Durante Sprint Planning, Elena (Tech Lead) + Marco (PM) decidono insieme lo Sprint Backlog. Se emerge conflitto durante lo sprint, Elena decide su aspetti tecnici, Marco su aspetti di business. In caso di stallo, Giovanni ha final say."

---

**Nessuna altra domanda? Procediamo alla chiusura.**

---

### 11. Action Items e Next Steps (5 minuti) - Marco Venturi

**Obiettivo**: Tutti sanno esattamente cosa fare dopo questo meeting

#### Action Items Assegnati

| ID | Action Item | Owner | Deadline | Deliverable |
|----|-------------|-------|----------|-------------|
| **AI-001** | Inviare inviti a tutte le piattaforme (GitLab, Confluence, Figma, Notion, Slack, Zoom) | Andrea Conti | 16/10/2025 EOD | Email di conferma a team |
| **AI-002** | Creare struttura Confluence secondo standard documentato | Marco Venturi | 17/10/2025 | Confluence workspace setup |
| **AI-003** | Setup server Hetzner + Docker + GitLab CI pipeline base | Andrea Conti | 25/10/2025 | Infra funzionante + documentazione |
| **AI-004** | Proof of concept Socket.IO (2 client, echo message) | Sara Bianchi | 27/10/2025 | Demo funzionante + latency test |
| **AI-005** | Finalizzare database schema PostgreSQL (utenti, partite, mosse) | Elena Rossi | 27/10/2025 | ER diagram + migration scripts |
| **AI-006** | Preparare Sprint 1 Planning: selezionare user stories, stimare story points | Marco Venturi + Elena Rossi | 27/10/2025 | Sprint 1 Backlog pronto |
| **AI-007** | Confermare disponibilità per Sessione Validazione 1 (fine Nov) | Francesca Giuliani | 18/10/2025 | Email conferma date |
| **AI-008** | Approvazione formale documenti Scoping+Planning | Giovanni Marchetti | 20/10/2025 | Email approval (via libera all'esecuzione) |

**Tracking**: Tutti gli action item sono tracciati su Notion Database con status (Todo/In Progress/Done).

#### Next Meetings

| Meeting | Data | Ora | Scopo |
|---------|------|-----|-------|
| **Daily Standup (primo)** | 16/10/2025 | 09:00 | Kickstart comunicazione quotidiana |
| **Sprint 0 Review** | 27/10/2025 | 14:00 | Review setup infra + POC Socket.IO |
| **Sprint 1 Planning** | 28/10/2025 | 09:00 | Pianificazione primo sprint sviluppo |
| **Project Status Meeting #1** | 18/10/2025 | 16:00 | Stato avanzamento prima settimana |

---

### 12. Closing e Celebrazione (5 minuti) - Marco Venturi

**Obiettivo**: Chiudere con energia positiva e senso di appartenenza

**Recap Key Takeaways**:
1. Abbiamo un piano solido: 170 giorni lavorativi, 6 sottosistemi di sviluppo, critical path identificato
2. Budget controllato: €22.750 spese su €25.000, cash flow sempre positivo
3. Team completo e competente: ognuno ha ruolo chiaro (RASCI Matrix)
4. Stakeholder allineato: Giovanni e Francesca supportano la visione
5. Strumenti in place: Confluence, GitLab, Figma, Notion pronti per l'uso

**Celebrazione Kickoff**:
> "Non stiamo solo costruendo software: stiamo portando online un gioco che fa parte della cultura ludica romagnola e che unisce la community Maraffa Forever. Buon lavoro a tutti."

**Chiusura**:
> "Il progetto MaraffaOnline è ufficialmente LANCIATO. Ci vediamo domani alle 09:00 per il primo Daily Standup. Buon lavoro a tutti!"

**Fine Meeting**: 11:00

---

## Meeting Minutes Summary

**Decisioni Chiave Approvate**:
1. Timeline 7 mesi confermata (15/10/2025 - 15/05/2026)
2. Budget €25.000 confermato, no incrementi
3. Scope MVP confermato (out: mobile app, AI, tornei, monetizzazione)
4. RASCI Matrix approvata (Allegato 4.2)
5. Regole Operative approvate (Allegato 4.2)
6. Sprint calendar: 15 sprint da 2 settimane (Sprint 0-14)
7. Daily Standup 09:00-09:15 da 16/10/2025

**Rischi Evidenziati**:
- Frontend Tavolo da Gioco (40 giorni) su critical path → mitigazione con pair programming
- Esperienza WebSocket → spike tecnico Sprint 0-1 + PoC Sprint 2 (consulente esterno come contingenza)
- Scope Creep → Change Request Process rigoroso

**Prossimi Milestone**:
- 27/10/2025: Fine Sprint 0 (Setup + POC)
- 28/10/2025: Sprint 1 Planning
- 20/12/2025: M2 - Backend Core Complete (2° pagamento €6.250 a metà Dicembre)

**Sentiment Check**: Tutti i partecipanti esprimono fiducia nel piano e commitment al progetto.

---

## Post-Meeting Follow-Up

**Documenti Pubblicati**:
- Questo verbale (Allegato 4.1) caricato su Confluence entro 16/10/2025
- Action items importati su Notion Database

**Comunicazioni Inviate**:
- Email riepilogo a tutti i partecipanti (16/10/2025 15:00)
- Registrazione Zoom condivisa su Google Drive (solo audio, no video per privacy)

**Approvazione Formale**:
- Giovanni Marchetti: approvazione formale entro 20/10/2025 (via libera all'esecuzione; 2° pagamento a metà Dicembre secondo Cash Flow)

---

<!-- Sezione "Fonti e Riferimenti" commentata (link a blog esterni, non necessari in un allegato di progetto). Reinseribile o sostituibile con fonti del corso; registro in Relazione/_appunti-per-relazione.md.
## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices per Project Kick-Off Meeting 2026:

- [Asana - Ultimate Kickoff Meeting Template](https://asana.com/templates/kickoff-meeting)
- [TeamGantt - How to Run Project Kickoff Meetings Like a Pro](https://www.teamgantt.com/guide/project-kickoff-meetings)
- [Digital Project Manager - Project Kickoff Guide 2025](https://thedigitalprojectmanager.com/project-management/project-kickoff-guide/)
- [Atlassian - Planning Project Kickoff Meetings](https://www.atlassian.com/work-management/project-management/project-kickoff)
-->

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Scribe**: Andrea Conti (DevOps Engineer)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever) - 20/10/2025

**Data meeting**: 15/10/2025 10:00-11:00
**Prossimo review**: Sprint 0 Review (27/10/2025)

**Storico revisioni**:
- **v.1.1.0**: Revisione di coerenza. Milestone allineate al Gantt (M1-M7, Allegato 3.5) e pagamenti alle date del Cash Flow (15 Ott / 15 Dic / 15 Feb, Allegato 3.4); effort per sottosistema allineato ai totali del MoSCoW (Backend 70, Real-Time 45, Frontend 76, Social 24, Infrastructure 37); 2ª sessione di validazione di Francesca spostata ad Aprile; calendario sprint completato a 15 sprint (Sprint 0-14); aggiunta la voce di budget Marketing/UAT/Celebrazione (€400); corretti refusi e uniformata la valuta (€).
