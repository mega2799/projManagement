# Allegato 3.5 - Project Network Diagram & Gantt Chart
## v.1.0.0 – 2025-10-28 15:00:00

Questo documento descrive la struttura del **Project Network Diagram** (con Critical Path Method) e del **Gantt Chart** per il progetto MaraffaOnline. Gli elementi descritti devono essere visualizzati utilizzando software come Microsoft Project, GanttProject, o ProjectLibre.

---

## Part 1: Project Network Diagram (CPM - Critical Path Method)

### Introduzione al Network Diagram

Il Project Network Diagram rappresenta visivamente le **attività del progetto** (nodi) e le loro **dipendenze** (frecce). Utilizzando il **Critical Path Method (CPM)**, identifichiamo:
- **Critical Path**: la sequenza più lunga di attività dipendenti (nessun slack time)
- **Float/Slack**: tempo che un'attività può essere ritardata senza impattare il progetto
- **Early Start (ES) / Late Start (LS)**: date minime e massime per iniziare un'attività
- **Early Finish (EF) / Late Finish (LF)**: date minime e massime per completare un'attività

---

### Attività Principali del Progetto (Nodi)

| ID | Attività | Durata (giorni) | Predecessori | Successori |
|----|----------|-----------------|--------------|------------|
| **A** | Setup Infrastruttura | 10 | - | B, C |
| **B** | Backend Auth + Database | 15 | A | D, E |
| **C** | Game Engine Foundation | 15 | A | F |
| **D** | Backend Gestione Partite | 20 | B | G |
| **E** | WebSocket Server Setup | 10 | B | H |
| **F** | Game Engine Regole Core | 25 | C | I |
| **G** | Backend Persistenza Stato | 10 | D | J |
| **H** | Real-Time Eventi | 20 | E | K |
| **I** | Game Engine Punteggi e Maraffa | 20 | F | L |
| **J** | Frontend Homepage + Login | 15 | G | M |
| **K** | Chat + Disconnessioni | 10 | H | N |
| **L** | Game Engine Testing | 15 | I | O |
| **M** | Frontend Dashboard + Creazione Stanza | 15 | J | P |
| **N** | Sistema Amicizie | 15 | K | Q |
| **O** | Integration Testing Game Engine | 10 | L | R |
| **P** | Frontend Tavolo da Gioco | 30 | M | R |
| **Q** | Frontend Profili + Notifiche | 10 | N | S |
| **R** | Testing End-to-End | 15 | O, P | S |
| **S** | UAT + Bug Fixing | 20 | Q, R | T |
| **T** | Preparazione Lancio | 10 | S | - |

**Totale Attività**: 20 nodi principali

---

### Calcolo Critical Path

**Metodo Forward Pass** (calcolo Early Start e Early Finish):

| ID | Attività | Durata | ES | EF |
|----|----------|--------|----|----|
| A | Setup Infrastruttura | 10 | 0 | 10 |
| B | Backend Auth + Database | 15 | 10 | 25 |
| C | Game Engine Foundation | 15 | 10 | 25 |
| D | Backend Gestione Partite | 20 | 25 | 45 |
| E | WebSocket Server Setup | 10 | 25 | 35 |
| F | Game Engine Regole Core | 25 | 25 | 50 |
| G | Backend Persistenza Stato | 10 | 45 | 55 |
| H | Real-Time Eventi | 20 | 35 | 55 |
| I | Game Engine Punteggi e Maraffa | 20 | 50 | 70 |
| J | Frontend Homepage + Login | 15 | 55 | 70 |
| K | Chat + Disconnessioni | 10 | 55 | 65 |
| L | Game Engine Testing | 15 | 70 | 85 |
| M | Frontend Dashboard + Creazione Stanza | 15 | 70 | 85 |
| N | Sistema Amicizie | 15 | 65 | 80 |
| O | Integration Testing Game Engine | 10 | 85 | 95 |
| P | Frontend Tavolo da Gioco | 30 | 85 | 115 |
| Q | Frontend Profili + Notifiche | 10 | 80 | 90 |
| R | Testing End-to-End | 15 | 115 | 130 |
| S | UAT + Bug Fixing | 20 | 130 | 150 |
| T | Preparazione Lancio | 10 | 150 | 160 |

**Metodo Backward Pass** (calcolo Late Start e Late Finish):

| ID | Attività | Durata | LS | LF | Float (Slack) |
|----|----------|--------|----|----|---------------|
| A | Setup Infrastruttura | 10 | 0 | 10 | 0 |
| B | Backend Auth + Database | 15 | 10 | 25 | 0 |
| C | Game Engine Foundation | 15 | 10 | 25 | 0 |
| D | Backend Gestione Partite | 20 | 25 | 45 | 0 |
| E | WebSocket Server Setup | 10 | 25 | 35 | 0 |
| F | Game Engine Regole Core | 25 | 25 | 50 | 0 |
| G | Backend Persistenza Stato | 10 | 45 | 55 | 0 |
| H | Real-Time Eventi | 20 | 35 | 55 | 0 |
| I | Game Engine Punteggi e Maraffa | 20 | 50 | 70 | 0 |
| J | Frontend Homepage + Login | 15 | 55 | 70 | 0 |
| K | Chat + Disconnessioni | 10 | 55 | 65 | 0 |
| L | Game Engine Testing | 15 | 70 | 85 | 0 |
| M | Frontend Dashboard + Creazione Stanza | 15 | 70 | 85 | 0 |
| N | Sistema Amicizie | 15 | 70 | 85 | 5 |
| O | Integration Testing Game Engine | 10 | 85 | 95 | 0 |
| P | Frontend Tavolo da Gioco | 30 | 85 | 115 | 0 |
| Q | Frontend Profili + Notifiche | 10 | 85 | 95 | 5 |
| R | Testing End-to-End | 15 | 115 | 130 | 0 |
| S | UAT + Bug Fixing | 20 | 130 | 150 | 0 |
| T | Preparazione Lancio | 10 | 150 | 160 | 0 |

---

### Critical Path Identificato

**Critical Path**: **A → B → D → G → J → M → P → R → S → T**

**Durata Totale Critical Path**: **160 giorni lavorativi** (equivalenti a ~6.5 mesi considerando weekend e festività)

**Attività sul Critical Path** (Float = 0, nessun margine di ritardo):
1. A - Setup Infrastruttura (10 giorni)
2. B - Backend Auth + Database (15 giorni)
3. D - Backend Gestione Partite (20 giorni)
4. G - Backend Persistenza Stato (10 giorni)
5. J - Frontend Homepage + Login (15 giorni)
6. M - Frontend Dashboard + Creazione Stanza (15 giorni)
7. P - Frontend Tavolo da Gioco (30 giorni) → **ATTIVITÀ PIÙ CRITICA**
8. R - Testing End-to-End (15 giorni)
9. S - UAT + Bug Fixing (20 giorni)
10. T - Preparazione Lancio (10 giorni)

**Attività con Float (Near-Critical Path)**:
- **N - Sistema Amicizie**: Float = 5 giorni (può ritardare max 5 giorni senza impatto)
- **Q - Frontend Profili + Notifiche**: Float = 5 giorni

**Insight Critici**:
- **Frontend Tavolo da Gioco (P)** è l'attività singola più lunga (30 giorni) sul critical path. Qualsiasi ritardo qui impatta direttamente la data di lancio.
- **Backend e Game Engine** devono essere completati in sequenza rigida (nessun parallelismo possibile per attività critiche).
- **Sistema Amicizie** e **Profili** hanno margine di flessibilità (5 giorni) → possono essere posticipati se necessario.

---

### Struttura Visuale del Network Diagram

**Oggetti da Visualizzare nel Diagram**:

1. **Nodi (Rettangoli)**: Ogni nodo rappresenta un'attività e contiene:
   ```
   +---------------------------+
   | ID: A                     |
   | Attività: Setup Infra     |
   | Durata: 10 giorni         |
   +---------------------------+
   | ES: 0  | EF: 10           |
   | LS: 0  | LF: 10           |
   | Float: 0 (CRITICAL)       |
   +---------------------------+
   ```

2. **Frecce (Dipendenze)**: Collegano nodi predecessori a successori
   - **Frecce rosse spesse**: attività sul critical path
   - **Frecce blu sottili**: attività con float (non critiche)

3. **Milestone (Rombi)**: Punti di controllo chiave
   - ◆ Milestone 1: "Backend Core Completo" (dopo attività G)
   - ◆ Milestone 2: "Game Engine Completo" (dopo attività L)
   - ◆ Milestone 3: "Frontend Completo" (dopo attività P)
   - ◆ Milestone 4: "MVP Pronto" (dopo attività S)

4. **Legenda Colori**:
   - **Rosso**: attività sul critical path (Float = 0)
   - **Arancione**: attività near-critical (Float 1-5 giorni)
   - **Verde**: attività con float significativo (Float > 5 giorni)

**Layout Consigliato**: Diagramma a flusso da sinistra (inizio progetto) a destra (fine progetto), con attività parallele disposte verticalmente.

**Software Consigliati**:
- Microsoft Project (funzione "Network Diagram View")
- Lucidchart / Draw.io (per creare manualmente)
- GanttProject (open source, export PNG)

**File di Output**: `img/network-diagram-maraffaonline.png`

---

## Part 2: Gantt Chart

### Introduzione al Gantt Chart

Il Gantt Chart rappresenta il **calendario del progetto** con:
- **Barre orizzontali**: durata di ogni attività nel tempo
- **Frecce di dipendenza**: collegano attività predecessori a successori
- **Milestone**: marker temporali per deliverable chiave
- **Critical Path**: evidenziato in rosso

---

### Struttura del Gantt Chart MaraffaOnline

**Asse Temporale (Asse X)**:
- **Periodo**: 15 ottobre 2025 - 15 marzo 2026 (6 mesi)
- **Granularità**: settimane (26 settimane totali)
- **Suddivisione**: 13 sprint da 2 settimane ciascuno

**Attività (Asse Y)**: Elencate gerarchicamente per sottosistema

---

### Dettaglio Attività per Gantt Chart

#### Sprint 0 (15 Ott - 25 Ott)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| A | Setup Infrastruttura | 15-Ott | 25-Ott | 10 gg | - | Sì |
| A.1 | Provisioning server Hetzner | 15-Ott | 16-Ott | 1 gg | - | Sì |
| A.2 | Setup Docker + Compose | 17-Ott | 19-Ott | 3 gg | A.1 | Sì |
| A.3 | Setup GitLab CI/CD | 20-Ott | 23-Ott | 4 gg | A.2 | Sì |
| A.4 | Setup PostgreSQL + SSL | 24-Ott | 25-Ott | 2 gg | A.3 | Sì |

#### Sprint 1 (28 Ott - 08 Nov)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| B | Backend Auth + Database | 28-Ott | 08-Nov | 15 gg | A | Sì |
| B.1 | Registrazione utente | 28-Ott | 01-Nov | 4 gg | A | Sì |
| B.2 | Login JWT | 02-Nov | 05-Nov | 4 gg | B.1 | Sì |
| B.3 | Accesso ospite | 06-Nov | 08-Nov | 3 gg | B.2 | Sì |
| C | Game Engine Foundation | 28-Ott | 08-Nov | 15 gg | A | No |
| C.1 | Design architettura | 28-Ott | 01-Nov | 4 gg | A | No |
| C.2 | Modello carte + mazzo | 02-Nov | 05-Nov | 4 gg | C.1 | No |
| C.3 | Distribuzione carte | 06-Nov | 08-Nov | 3 gg | C.2 | No |

#### Sprint 2-3 (11 Nov - 06 Dic)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| D | Backend Gestione Partite | 11-Nov | 06-Dic | 20 gg | B | Sì |
| D.1 | Creazione stanza | 11-Nov | 18-Nov | 5 gg | B | Sì |
| D.2 | Join stanza | 19-Nov | 25-Nov | 5 gg | D.1 | Sì |
| D.3 | Gestione lobby | 26-Nov | 06-Dic | 10 gg | D.2 | Sì |
| F | Game Engine Regole Core | 11-Nov | 13-Dic | 25 gg | C | No |
| F.1 | Ordine forza carte | 11-Nov | 18-Nov | 5 gg | C | No |
| F.2 | Validazione mosse | 19-Nov | 29-Nov | 8 gg | F.1 | No |
| F.3 | Vincitore presa | 30-Nov | 06-Dic | 5 gg | F.2 | No |

#### Sprint 4-5 (09 Dic - 03 Gen)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| G | Backend Persistenza Stato | 09-Dic | 20-Dic | 10 gg | D | Sì |
| E | WebSocket Server Setup | 09-Dic | 20-Dic | 10 gg | B | No |
| H | Real-Time Eventi | 23-Dic | 17-Gen | 20 gg | E | No |
| I | Game Engine Punteggi | 14-Dic | 10-Gen | 20 gg | F | No |
| J | Frontend Homepage + Login | 23-Dic | 10-Gen | 15 gg | G | Sì |

#### Sprint 6-7 (06 Gen - 31 Gen)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| M | Frontend Dashboard + Stanza | 13-Gen | 31-Gen | 15 gg | J | Sì |
| L | Game Engine Testing | 13-Gen | 31-Gen | 15 gg | I | No |
| K | Chat + Disconnessioni | 20-Gen | 31-Gen | 10 gg | H | No |

#### Sprint 8-9 (03 Feb - 28 Feb)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| P | Frontend Tavolo da Gioco | 03-Feb | 14-Mar | 30 gg | M | Sì ← **CRITICO** |
| O | Integration Testing GE | 03-Feb | 14-Feb | 10 gg | L | No |
| N | Sistema Amicizie | 03-Feb | 21-Feb | 15 gg | K | No (Float 5) |
| Q | Frontend Profili + Notifiche | 24-Feb | 07-Mar | 10 gg | N | No (Float 5) |

#### Sprint 10-11 (03 Mar - 28 Mar)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| R | Testing End-to-End | 17-Mar | 31-Mar | 15 gg | P, O | Sì |

#### Sprint 12 (31 Mar - 11 Apr)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| S | UAT + Bug Fixing | 01-Apr | 24-Apr | 20 gg | R, Q | Sì |

#### Sprint 13 (Lancio)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| T | Preparazione Lancio | 27-Apr | 08-Mag | 10 gg | S | Sì |

**Data Lancio MVP**: **15 Maggio 2026** (con margine di 1 settimana post-preparazione)

---

### Milestone del Progetto

| Milestone | Data | Deliverable | Stakeholder Review |
|-----------|------|-------------|---------------------|
| **M1: Infrastructure Ready** | 25-Ott-2025 | Server + CI/CD operativi | Interno |
| **M2: Backend Core Complete** | 20-Dic-2025 | Auth + Partite + Persistenza | Giovanni Marchetti |
| **M3: Game Engine Complete** | 31-Gen-2026 | Regole + Testing validato | Francesca Giuliani |
| **M4: Frontend Core Complete** | 14-Mar-2026 | Homepage + Dashboard + Tavolo | Luca Moretti (UX Designer) |
| **M5: MVP Beta** | 31-Mar-2026 | Tutte le funzionalità Must Have | Team interno |
| **M6: UAT Approved** | 24-Apr-2026 | Approvazione community | Maraffa Forever (10 tester) |
| **M7: Production Launch** | 15-Mag-2026 | MaraffaOnline live | Giovanni Marchetti |

---

### Elementi Visuali del Gantt Chart

**Oggetti da Visualizzare**:

1. **Barre Attività**:
   - **Barra rossa**: attività sul critical path (nessun margine di errore)
   - **Barra arancione**: attività near-critical (float 1-5 giorni)
   - **Barra verde**: attività con float significativo (> 5 giorni)
   - **Altezza barra**: proporzionale all'effort (story points)

2. **Frecce Dipendenza**:
   - **Finish-to-Start (FS)**: la più comune (es. B dipende da A)
   - **Start-to-Start (SS)**: attività possono iniziare contemporaneamente (es. C e B partono insieme dopo A)
   - **Colore freccia rosso**: dipendenza critica
   - **Colore freccia grigio**: dipendenza non critica

3. **Milestone (Rombi neri)**: Posizionati sulla timeline alle date chiave

4. **Timeline Superiore**:
   ```
   Ott 2025  | Nov | Dic | Gen 2026 | Feb | Mar | Apr | Mag
   Sprint 0  | S1  | S2  | S3  | S4  | S5  | S6  | ...  | S12 | S13
   ```

5. **Legenda**:
   - Rosso = Critical Path
   - Arancione = Near-Critical
   - Verde = Non-Critical
   - ◆ = Milestone

6. **Indicatori di Progresso** (da aggiornare durante esecuzione):
   - Barra completamento % (es. "P - Frontend Tavolo: 60% completato")
   - Today line (linea verticale tratteggiata che indica "oggi")

---

### Rischi Evidenziati dal Gantt Chart

#### Rischio 1: Frontend Tavolo da Gioco (30 giorni sul Critical Path)
**Probabilità**: Alta
**Impatto**: Critico (ritardo diretto sulla data di lancio)
**Mitigazione**:
- Assegnare Luca Moretti (UX Designer) a tempo pieno
- Pair programming con Sara Bianchi per componenti complessi
- Mockup approvati in anticipo (già fatto in Scoping)
- Buffer: se P supera i 30 giorni, comprimere attività S (UAT) da 20 a 15 giorni

#### Rischio 2: Testing End-to-End (15 giorni, dopo P)
**Probabilità**: Media
**Impatto**: Alto
**Mitigazione**:
- Iniziare testing E2E in parallelo con P (parziale overlap)
- Automatizzare test con Cypress per velocizzare

#### Rischio 3: Attività N e Q con Float 5 giorni
**Probabilità**: Bassa
**Impatto**: Medio
**Opportunità**: Se altre attività critiche ritardano, N e Q possono assorbire fino a 5 giorni di slittamento senza impatto finale.

---

### Aggiornamento Dinamico del Gantt

**Best Practice 2026**: Il Gantt Chart è un documento **vivo**, non statico.

**Frequenza Aggiornamento**: Settimanale (ogni venerdì durante Project Status Meeting)

**Modifiche Tracked**:
1. **Percentuale completamento** attività in corso
2. **Slittamenti date**: se un'attività ritarda, ricalcolare critical path
3. **Nuove attività**: se emergono change request, aggiungere al backlog e valutare impatto su critical path
4. **Rimozione attività**: se scope ridotto (es. feature Could Have tagliate), rimuovere dal Gantt

**Responsabile**: Marco Venturi (Project Manager)

**Strumenti Consigliati**:
- **Microsoft Project**: standard di settore, calcolo automatico critical path
- **GanttProject**: open source, export PNG/PDF
- **TeamGantt**: collaborativo, aggiornamenti real-time
- **Asana / Monday.com**: Gantt view integrata con task management

**File di Output**: `img/gantt-chart-maraffaonline.png` (aggiornato mensilmente per documentazione)

---

## Integrazione Network Diagram ↔ Gantt Chart

**Come i Due Strumenti si Completano**:

| Aspetto | Network Diagram | Gantt Chart |
|---------|-----------------|-------------|
| **Focus** | Dipendenze logiche | Calendario temporale |
| **Visualizzazione** | Grafo a nodi | Timeline a barre |
| **Critical Path** | Calcolato matematicamente (ES/LS/Float) | Evidenziato visivamente in rosso |
| **Utilizzo** | Analisi "what-if" (se attività X ritarda, che impatto?) | Monitoraggio progresso giornaliero |
| **Audience** | Project Manager, Tech Lead | Tutto il team + stakeholder |

**Workflow Consigliato**:
1. Creare **Network Diagram** per calcolare critical path e float
2. Trasferire dati in **Gantt Chart** per visualizzazione temporale
3. Durante esecuzione: aggiornare Gantt settimanalmente
4. Se major change: ricalcolare Network Diagram → aggiornare Gantt

---

## Sensitivity Analysis (Analisi di Sensibilità)

### Scenario 1: Frontend Tavolo ritarda di 10 giorni
**Impatto**: Data lancio slitta da 15 Maggio a 25 Maggio 2026
**Azioni Correttive**:
- Comprimere attività S (UAT) da 20 a 15 giorni
- Aggiungere 1 sviluppatore part-time su P per recuperare 5 giorni
- **Costo aggiuntivo**: ~€2.000 (salary 0.5 mesi)

### Scenario 2: Game Engine Testing (L) scopre bug critici (+5 giorni)
**Impatto**: L ha float? NO, L non è sul critical path ma O (Integration Testing) dipende da L.
- Se L slitta da 15 a 20 giorni → O inizia 5 giorni dopo → P non impattato (parallelo)
- **Nessun impatto su data lancio** (L ha margine di manovra)

### Scenario 3: Sistema Amicizie (N) ritarda di 10 giorni
**Impatto**: N ha 5 giorni di float.
- Ritardo 10 giorni → supera float di 5 giorni → entra nel critical path
- **Nuovo critical path**: A → B → E → H → K → N → Q → ... (se N supera margine)
- **Azione**: Posticipare N a post-lancio MVP (degradare da Should Have a Won't Have)

---

## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices di Project Management 2026:
- [Wrike - Critical Path Method Guide 2026](https://www.wrike.com/blog/critical-path-is-easy-as-123/)
- [ProjectManager - Critical Path on Gantt Chart](https://www.projectmanager.com/blog/critical-path-on-gantt)
- [TeamGantt - Critical Path Method Practical Guide](https://www.teamgantt.com/blog/critical-path)
- [Smartsheet - Ultimate Guide to CPM](https://www.smartsheet.com/critical-path-method)
- [Asana - Critical Path Method 2025](https://asana.com/resources/critical-path-method)

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 28/10/2025

**Prossimo Aggiornamento**: 05/11/2025 (fine Sprint 0)
