# Allegato 3.5 - Project Network Diagram & Gantt Chart
## v.2.2.0 – 2026-08-23

> Per la versione visiva compatta (da usare come allegato PDF), vedi `Allegato3.5-NetworkGantt.html`: apri il file nel browser e usa "Stampa → Salva come PDF". Contiene il Network Diagram (20 nodi, asse = giorni lavorativi CPM) e il Gantt (stesse 20 attività, asse = calendario reale) in forma condensata; il dettaglio per sprint/sotto-task, le tabelle Forward/Backward Pass complete, l'analisi rischi e il processo di aggiornamento dinamico restano in questo documento.

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

> **Nota sulle durate.** Tutte le durate sono espresse in **giorni lavorativi netti** (lun-ven, escluse le festività italiane che cadono nella finestra di progetto: Immacolata, Natale, S. Stefano, Capodanno, Epifania, Lunedì dell'Angelo, 1° Maggio). I legami sono Finish-to-Start, con un'eccezione dichiarata: il legame **P → R è Start-to-Start con lag di 31 giorni** (fast tracking, vedi sezione "Critical Path Identificato").
>
> **Convenzione dei tempi (ES/EF/LS/LF).** Le tabelle usano la convenzione a *istanti cumulati* con partenza da 0 (il valore è il confine di fine giornata), quindi **EF = ES + durata** e slack = LS − ES. Le slide del corso usano la convenzione equivalente a *giorni di calendario* 1-based (ES del primo task = 1, **EF = ES + durata − 1**, LS = LF − durata + 1): le due notazioni differiscono di una costante e producono le stesse durate, gli stessi slack e lo stesso critical path.

| ID | Attività | Durata (gg lavorativi) | Predecessori | Successori |
|----|----------|-----------------|--------------|------------|
| **A** | Setup Infrastruttura | 9 | - | B, C |
| **B** | Backend Auth + Database | 9 | A | D, E |
| **C** | Game Engine Foundation | 9 | A | F |
| **D** | Backend Gestione Partite | 20 | B | G |
| **E** | WebSocket Server Setup | 9 | B | H |
| **F** | Game Engine Regole Core | 23 | C | I |
| **G** | Backend Persistenza Stato | 9 | D | J |
| **H** | Real-Time Eventi | 16 | E | K |
| **I** | Game Engine Punteggi e Maraffa | 16 | F | L |
| **J** | Frontend Homepage + Login | 11 | G | M |
| **K** | Chat + Disconnessioni | 10 | H | N |
| **L** | Game Engine Testing | 15 | I | O |
| **M** | Frontend Dashboard + Creazione Stanza | 15 | J | P |
| **N** | Sistema Amicizie | 15 | K | Q |
| **O** | Integration Testing Game Engine | 10 | L | R |
| **P** | Frontend Tavolo da Gioco | 40 | M | R (SS+31) |
| **Q** | Frontend Profili + Notifiche | 10 | N | S |
| **R** | Testing End-to-End | 11 | O (FS), P (SS+31) | S |
| **S** | UAT + Bug Fixing | 17 | Q, R | T |
| **T** | Preparazione Lancio | 9 | S | - |

**Totale Attività**: 20 nodi principali

### Raccordo con la WBS (tracciabilità Attività di rete ↔ Work Package)

I 20 nodi del network sono **aggregazioni delle 43 attività della WBS** (Allegato 3.1), dimensionate per l'analisi reticolare: il controllo dei tempi si esercita su questi nodi, mentre il dettaglio del lavoro resta tracciato nella WBS Dictionary. La tabella seguente documenta la corrispondenza.

| Nodo | Attività WBS di riferimento |
|------|------------------------------|
| **A** Setup Infrastruttura | 6.1.1, 6.1.2, 6.2.1, 6.2.2 (primo incremento: hosting, Docker, CI/CD) |
| **B** Backend Auth + Database | 2.1.1; 2.3.1 (tabelle utenti) |
| **C** Game Engine Foundation | 1.1.1; 1.1.3 (selezione briscola) |
| **D** Backend Gestione Partite | 2.2.1; 2.3.1 (tabelle partite/mosse) |
| **E** WebSocket Server Setup | 3.1.1 |
| **F** Game Engine Regole Core | 1.1.1 (ordine di forza); 1.1.3 (presa, turni, timeout) |
| **G** Backend Persistenza Stato | 2.2.2 |
| **H** Real-Time Eventi | 3.1.2; 3.2.1 (broadcast selettivo e validazioni) |
| **I** Game Engine Punteggi e Maraffa | 1.1.2, 1.1.4, 1.1.5 |
| **J** Frontend Homepage + Login | 4.1.1 |
| **K** Chat + Disconnessioni | 3.1.1 (reconnection), 3.2.2 (indicatori latency); 5.2.1 (chat in-game) |
| **L** Game Engine Testing | 1.2.1, 1.2.2 |
| **M** Frontend Dashboard + Creazione Stanza | 4.1.2, 4.1.3 |
| **N** Sistema Amicizie | 5.1.1, 5.1.2; 2.1.2 (profilo utente) |
| **O** Integration Testing Game Engine | 1.2.2; 7.2.1 (integration test) |
| **P** Frontend Tavolo da Gioco | 4.1.4, 4.1.5; 4.3 (animazioni e performance) |
| **Q** Frontend Profili + Notifiche | 4.2.1, 4.2.2 (responsive e accessibilità); 5.2.2; UI dello storico (2.2.3) |
| **R** Testing End-to-End | 7.2.1 (E2E Cypress) |
| **S** UAT + Bug Fixing | 7.2.2 |
| **T** Preparazione Lancio | 6.1 (deploy production), 6.3.1 (monitoring post-lancio), 7.1.1 (documentazione utente) |

> Le attività WBS **non riconducibili a nodi di rete** sono di natura continuativa o on-demand e non vincolano la schedula: la documentazione PM (7.1.2, prodotta lungo tutto il progetto), l'ottimizzazione delle query (2.3.2, attivata su evidenza di profiling), gli incrementi successivi di monitoring, logging e sicurezza (6.3.2, 6.4, attivati al bisogno secondo l'approccio incrementale) e la chat globale di lobby (5.2.1.1, Could Have). La loro copertura di responsabilità è comunque nella RASCI (Allegato 4.2).

---

### Calcolo Critical Path

**Metodo Forward Pass** (calcolo Early Start e Early Finish; per R vale il legame SS: ES(R) = ES(P) + 31):

| ID | Attività | Durata | ES | EF |
|----|----------|--------|----|----|
| A | Setup Infrastruttura | 9 | 0 | 9 |
| B | Backend Auth + Database | 9 | 9 | 18 |
| C | Game Engine Foundation | 9 | 9 | 18 |
| D | Backend Gestione Partite | 20 | 18 | 38 |
| E | WebSocket Server Setup | 9 | 18 | 27 |
| F | Game Engine Regole Core | 23 | 18 | 41 |
| G | Backend Persistenza Stato | 9 | 38 | 47 |
| H | Real-Time Eventi | 16 | 27 | 43 |
| I | Game Engine Punteggi e Maraffa | 16 | 41 | 57 |
| J | Frontend Homepage + Login | 11 | 47 | 58 |
| K | Chat + Disconnessioni | 10 | 43 | 53 |
| L | Game Engine Testing | 15 | 57 | 72 |
| M | Frontend Dashboard + Creazione Stanza | 15 | 58 | 73 |
| N | Sistema Amicizie | 15 | 53 | 68 |
| O | Integration Testing Game Engine | 10 | 72 | 82 |
| P | Frontend Tavolo da Gioco | 40 | 73 | 113 |
| Q | Frontend Profili + Notifiche | 10 | 68 | 78 |
| R | Testing End-to-End | 11 | 104 | 115 |
| S | UAT + Bug Fixing | 17 | 115 | 132 |
| T | Preparazione Lancio | 9 | 132 | 141 |

**Metodo Backward Pass** (calcolo Late Start e Late Finish):

| ID | Attività | Durata | LS | LF | Float (Slack) |
|----|----------|--------|----|----|---------------|
| A | Setup Infrastruttura | 9 | 0 | 9 | 0 |
| B | Backend Auth + Database | 9 | 9 | 18 | 0 |
| C | Game Engine Foundation | 9 | 31 | 40 | 22 |
| D | Backend Gestione Partite | 20 | 18 | 38 | 0 |
| E | WebSocket Server Setup | 9 | 55 | 64 | 37 |
| F | Game Engine Regole Core | 23 | 40 | 63 | 22 |
| G | Backend Persistenza Stato | 9 | 38 | 47 | 0 |
| H | Real-Time Eventi | 16 | 64 | 80 | 37 |
| I | Game Engine Punteggi e Maraffa | 16 | 63 | 79 | 22 |
| J | Frontend Homepage + Login | 11 | 47 | 58 | 0 |
| K | Chat + Disconnessioni | 10 | 80 | 90 | 37 |
| L | Game Engine Testing | 15 | 79 | 94 | 22 |
| M | Frontend Dashboard + Creazione Stanza | 15 | 58 | 73 | 0 |
| N | Sistema Amicizie | 15 | 90 | 105 | 37 |
| O | Integration Testing Game Engine | 10 | 94 | 104 | 22 |
| P | Frontend Tavolo da Gioco | 40 | 73 | 113 | 0 |
| Q | Frontend Profili + Notifiche | 10 | 105 | 115 | 37 |
| R | Testing End-to-End | 11 | 104 | 115 | 0 |
| S | UAT + Bug Fixing | 17 | 115 | 132 | 0 |
| T | Preparazione Lancio | 9 | 132 | 141 | 0 |

---

### Critical Path Identificato

**Critical Path**: **A → B → D → G → J → M → P → R → S → T**

**Durata Totale Critical Path**: **141 giorni lavorativi** — esattamente i giorni lavorativi disponibili dal 15 ottobre 2025 all'8 maggio 2026, al netto di weekend e festività italiane. Il lancio del 15 maggio conserva così **5 giorni lavorativi (≈1 settimana) di margine** dopo la fine dell'ultima attività (T).

**Fast tracking dichiarato (P → R)**: per far stare il percorso critico nei sette mesi di calendario si è applicata una compressione della schedula di tipo *fast tracking*: il Testing End-to-End (R) non attende la fine del Frontend Tavolo da Gioco (P), ma parte quando P ha completato 31 dei suoi 40 giorni (legame **Start-to-Start con lag di 31 giorni**), lavorando sui moduli già consegnati mentre P chiude animazioni e rifiniture. La compressione non è gratis: introduce un rischio di rework sui test eseguiti su moduli poi ritoccati, accettato e mitigato dal fatto che l'Integration Testing del Game Engine (O) si chiude prima dell'avvio di R e che gli ultimi 2 giorni di R cadono comunque dopo la fine di P.

**Attività sul Critical Path** (Float = 0, nessun margine di ritardo):
1. A - Setup Infrastruttura (9 giorni)
2. B - Backend Auth + Database (9 giorni)
3. D - Backend Gestione Partite (20 giorni)
4. G - Backend Persistenza Stato (9 giorni)
5. J - Frontend Homepage + Login (11 giorni)
6. M - Frontend Dashboard + Creazione Stanza (15 giorni)
7. P - Frontend Tavolo da Gioco (40 giorni) → **ATTIVITÀ PIÙ CRITICA**
8. R - Testing End-to-End (11 giorni, in fast tracking su P)
9. S - UAT + Bug Fixing (17 giorni)
10. T - Preparazione Lancio (9 giorni)

**Attività con Float (slack disponibile)**:
- **Ramo Game Engine (C, F, I, L, O)**: Float = 22 giorni. Il Game Engine e il suo testing non sono sul critical path: pur essendo una catena lunga, si completano prima che il ramo Frontend (critico) arrivi al testing End-to-End (R).
- **Ramo Chat/Social (E, H, K, N, Q)**: Float = 37 giorni. Sistema Amicizie, Chat, Profili e Notifiche dispongono del margine più ampio, dovuto al fatto che il ramo critico Backend → Frontend Tavolo è nettamente più lungo.

**Insight Critici**:
- **Frontend Tavolo da Gioco (P)** è l'attività singola più lunga (40 giorni) sul critical path. Qualsiasi ritardo qui impatta direttamente la data di lancio.
- Il **Backend** (B → D → G) è sul critical path e va completato in sequenza rigida; il **Game Engine** (C → F → I → L → O), pur sviluppandosi in parallelo, dispone di 22 giorni di float e non condiziona la data di lancio.
- **Sistema Amicizie** e **Profili** hanno un ampio margine di flessibilità (37 giorni) → possono essere posticipati o ridotti senza impatto sulla milestone finale.

---

### Struttura Visuale del Network Diagram

**Oggetti da Visualizzare nel Diagram**:

1. **Nodi (Rettangoli)**: Ogni nodo rappresenta un'attività e contiene:
   ```
   +---------------------------+
   | ID: A                     |
   | Attività: Setup Infra     |
   | Durata: 9 giorni          |
   +---------------------------+
   | ES: 0  | EF: 9            |
   | LS: 0  | LF: 9            |
   | Float: 0 (CRITICAL)       |
   +---------------------------+
   ```

2. **Frecce (Dipendenze)**: Collegano nodi predecessori a successori
   - **Frecce rosse spesse**: attività sul critical path
   - **Frecce blu sottili**: attività con float (non critiche)

3. **Milestone (Rombi)**: Punti di controllo chiave (numerazione allineata alla tabella milestone del Gantt, M1-M7)
   - ◆ M2: "Backend Core Complete" (dopo attività G)
   - ◆ M3: "Game Engine Complete" (dopo attività L)
   - ◆ M4: "Frontend Core Complete" (dopo attività P)
   - ◆ M6: "UAT Approved" (dopo attività S)

4. **Legenda Colori**:
   - **Rosso**: attività sul critical path (Float = 0)
   - **Arancione**: attività near-critical (Float 1-5 giorni)
   - **Verde**: attività con float significativo (Float > 5 giorni)

**Layout Consigliato**: Diagramma a flusso da sinistra (inizio progetto) a destra (fine progetto), con attività parallele disposte verticalmente.

**Software Consigliati**:
- Microsoft Project (funzione "Network Diagram View")
- Lucidchart / Draw.io (per creare manualmente)
- GanttProject (open source, export PNG)

**File di Output** (non prodotto per questo elaborato): `img/network-diagram-maraffaonline.png` — nella pratica reale generato con uno dei software sopra; qui il diagramma è documentato tramite l'elenco delle Attività Principali, il template del nodo e la tabella Critical Path Identificato di questo stesso documento.

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
- **Periodo**: 15 ottobre 2025 - 15 maggio 2026 (7 mesi)
- **Granularità**: settimane (30 settimane totali)
- **Suddivisione**: 15 sprint da 2 settimane ciascuno (Sprint 0-14)

**Attività (Asse Y)**: Elencate gerarchicamente per sottosistema

---

### Dettaglio Attività per Gantt Chart

#### Sprint 0 (15 Ott - 27 Ott)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| A | Setup Infrastruttura | 15-Ott | 27-Ott | 9 gg | - | Sì |
| A.1 | Provisioning server Hetzner | 15-Ott | 15-Ott | 1 gg | - | Sì |
| A.2 | Setup Docker + Compose | 16-Ott | 17-Ott | 2 gg | A.1 | Sì |
| A.3 | Setup GitLab CI/CD | 20-Ott | 23-Ott | 4 gg | A.2 | Sì |
| A.4 | Setup PostgreSQL + SSL | 24-Ott | 27-Ott | 2 gg | A.3 | Sì |

#### Sprint 1 (28 Ott - 07 Nov)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| B | Backend Auth + Database | 28-Ott | 07-Nov | 9 gg | A | Sì |
| B.1 | Registrazione utente | 28-Ott | 31-Ott | 4 gg | A | Sì |
| B.2 | Login JWT | 03-Nov | 05-Nov | 3 gg | B.1 | Sì |
| B.3 | Accesso ospite | 06-Nov | 07-Nov | 2 gg | B.2 | Sì |
| C | Game Engine Foundation | 28-Ott | 07-Nov | 9 gg | A | No |
| C.1 | Design architettura | 28-Ott | 31-Ott | 4 gg | A | No |
| C.2 | Modello carte + mazzo | 03-Nov | 05-Nov | 3 gg | C.1 | No |
| C.3 | Distribuzione carte | 06-Nov | 07-Nov | 2 gg | C.2 | No |

#### Sprint 2-3 (10 Nov - 05 Dic)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| D | Backend Gestione Partite | 10-Nov | 05-Dic | 20 gg | B | Sì |
| D.1 | Creazione stanza | 10-Nov | 14-Nov | 5 gg | B | Sì |
| D.2 | Join stanza | 17-Nov | 21-Nov | 5 gg | D.1 | Sì |
| D.3 | Gestione lobby | 24-Nov | 05-Dic | 10 gg | D.2 | Sì |
| F | Game Engine Regole Core | 10-Nov | 11-Dic | 23 gg | C | No |
| F.1 | Ordine forza carte | 10-Nov | 14-Nov | 5 gg | C | No |
| F.2 | Validazione mosse | 17-Nov | 26-Nov | 8 gg | F.1 | No |
| F.3 | Vincitore presa | 27-Nov | 03-Dic | 5 gg | F.2 | No |

#### Sprint 4-5 (08 Dic - 02 Gen)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| G | Backend Persistenza Stato | 09-Dic | 19-Dic | 9 gg | D | Sì |
| E | WebSocket Server Setup | 09-Dic | 19-Dic | 9 gg | B | No |
| H | Real-Time Eventi | 22-Dic | 16-Gen | 16 gg | E | No |
| I | Game Engine Punteggi | 15-Dic | 09-Gen | 16 gg | F | No |
| J | Frontend Homepage + Login | 22-Dic | 09-Gen | 11 gg | G | Sì |

#### Sprint 6-7 (05 Gen - 30 Gen)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| M | Frontend Dashboard + Stanza | 12-Gen | 30-Gen | 15 gg | J | Sì |
| L | Game Engine Testing | 12-Gen | 30-Gen | 15 gg | I | No |
| K | Chat + Disconnessioni | 19-Gen | 30-Gen | 10 gg | H | No |

#### Sprint 8-9 (02 Feb - 27 Feb)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| P | Frontend Tavolo da Gioco | 02-Feb | 27-Mar | 40 gg | M | Sì ← **CRITICO** |
| O | Integration Testing GE | 02-Feb | 13-Feb | 10 gg | L | No |
| N | Sistema Amicizie | 02-Feb | 20-Feb | 15 gg | K | No (Float 37) |
| Q | Frontend Profili + Notifiche | 23-Feb | 06-Mar | 10 gg | N | No (Float 37) |

#### Sprint 10-11 (02 Mar - 31 Mar)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| R | Testing End-to-End | 17-Mar | 31-Mar | 11 gg | O (FS), P (SS+31) | Sì (fast tracking: in overlap con la coda di P, che chiude il 27-Mar) |

#### Sprint 12 (01 Apr - 24 Apr)
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| S | UAT + Bug Fixing | 01-Apr | 24-Apr | 17 gg | R, Q | Sì |

#### Sprint 13-14 (27 Apr - 15 Mag) - Preparazione e Lancio
| ID | Attività | Inizio | Fine | Durata | Predecessore | Critical Path |
|----|----------|--------|------|--------|--------------|---------------|
| T | Preparazione Lancio | 27-Apr | 08-Mag | 9 gg | S | Sì |

**Data Lancio MVP**: **15 Maggio 2026** (con margine di 1 settimana post-preparazione)

---

### Milestone del Progetto

| Milestone | Data | Deliverable | Stakeholder Review |
|-----------|------|-------------|---------------------|
| **M1: Infrastructure Ready** | 27-Ott-2025 | Server + CI/CD operativi | Interno |
| **M2: Backend Core Complete** | 19-Dic-2025 | Auth + Partite + Persistenza | Giovanni Marchetti |
| **M3: Game Engine Complete** | 30-Gen-2026 | Regole + Testing validato | Francesca Giuliani |
| **M4: Frontend Core Complete** | 27-Mar-2026 | Homepage + Dashboard + Tavolo | Luca Moretti (UX Designer) |
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
   - **Start-to-Start (SS)**: la successiva non può iniziare prima che sia *iniziata* la precedente, eventualmente con lag (unico caso nel progetto: P → R, SS con lag 31); B e C partono insieme dopo A per semplice *divergenza* di due legami FS, non per un vincolo SS
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

#### Rischio 1: Frontend Tavolo da Gioco (40 giorni sul Critical Path)
**Probabilità**: Alta
**Impatto**: Critico (ritardo diretto sulla data di lancio)
**Mitigazione**:
- Assegnare Luca Moretti (UX Designer) a tempo pieno
- Pair programming con Sara Bianchi per componenti complessi
- Mockup approvati in anticipo (già fatto in Scoping)
- Buffer: se P supera i 40 giorni, comprimere attività S (UAT) da 17 a 12 giorni

#### Rischio 2: Testing End-to-End in fast tracking (11 giorni, in overlap con P)
**Probabilità**: Media
**Impatto**: Alto
**Descrizione**: R parte quando P ha completato 31 dei 40 giorni (legame SS+31): i test eseguiti sui moduli consegnati potrebbero richiedere rework se le rifiniture finali di P li modificano.
**Mitigazione**:
- Sequenziare R sui moduli congelati per primi (login, dashboard, flusso stanza); il tavolo da gioco si testa negli ultimi giorni di R, dopo la chiusura di P
- Automatizzare test con Cypress: il rework si riduce a ri-esecuzione della suite

#### Rischio 3: Attività N e Q con Float 37 giorni
**Probabilità**: Bassa
**Impatto**: Medio
**Opportunità**: N (Sistema Amicizie) e Q (Frontend Profili + Notifiche) dispongono di 37 giorni di float. Possono quindi slittare ampiamente senza impatto sulla data di lancio, oppure essere ridimensionate/posticipate per liberare risorse da spostare sul critical path (es. sul Frontend Tavolo da Gioco) in caso di necessità.

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

**File di Output** (non prodotto per questo elaborato): `img/gantt-chart-maraffaonline.png` (aggiornato mensilmente per documentazione) — il Gantt è documentato in forma tabellare/CSV in questo allegato e in `Allegato3.5.2-GanttData.csv` (che esiste realmente).

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
**Impatto**: la fine di T slitta oltre l'8 Maggio; consumati i 5 giorni di margine, il lancio slitta di ≈1 settimana (verso il 22 Maggio 2026)
**Azioni Correttive**:
- Comprimere attività S (UAT) da 17 a 12 giorni
- Aggiungere 1 sviluppatore part-time su P per recuperare 5 giorni
- **Costo aggiuntivo**: ≈€2.000 (contractor esterno senior per ≈0,5 mesi a tariffe di mercato; coperto dal Contingency Buffer)

### Scenario 2: Game Engine Testing (L) scopre bug critici (+5 giorni)
**Impatto**: L ha float? NO, L non è sul critical path ma O (Integration Testing) dipende da L.
- Se L slitta da 15 a 20 giorni → O inizia 5 giorni dopo → P non impattato (parallelo)
- **Nessun impatto su data lancio** (il ramo Game Engine ha 22 giorni di float)

### Scenario 3: Sistema Amicizie (N) ritarda di 10 giorni
**Impatto**: N dispone di 37 giorni di float.
- Ritardo di 10 giorni molto inferiore ai 37 giorni di float → N **non** entra nel critical path
- **Nessun impatto sulla data di lancio**: il ritardo viene interamente assorbito dallo slack disponibile
- Solo un ritardo superiore a 37 giorni renderebbe critico il ramo Chat/Social (A → B → E → H → K → N → Q → S); in quel caso l'azione sarebbe posticipare a post-lancio la parte Should/Could di N/Q (amicizie, profili, storico), mentre i task Must contenuti in Q (notifiche di turno, responsive) verrebbero riassegnati alle attività M/P per restare nella v1.0

---

<!-- Sezione "Fonti e Riferimenti" commentata (link a blog esterni, non necessari in un allegato di progetto). Reinseribile o sostituibile con fonti del corso; registro in Relazione/_appunti-per-relazione.md.
## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices di Project Management 2026:
- [Wrike - Critical Path Method Guide 2026](https://www.wrike.com/blog/critical-path-is-easy-as-123/)
- [ProjectManager - Critical Path on Gantt Chart](https://www.projectmanager.com/blog/critical-path-on-gantt)
- [TeamGantt - Critical Path Method Practical Guide](https://www.teamgantt.com/blog/critical-path)
- [Smartsheet - Ultimate Guide to CPM](https://www.smartsheet.com/critical-path-method)
- [Asana - Critical Path Method 2025](https://asana.com/resources/critical-path-method)
-->

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)

**Prossimo Aggiornamento**: 31/10/2025 (venerdì; primo aggiornamento settimanale dopo la chiusura dello Sprint 0)

**Storico revisioni**:
- **v.2.2.0**: Audit teorico: corretta la voce di legenda Start-to-Start (B e C dopo A partono insieme per divergenza di legami FS, non per vincolo SS; SS = la successiva non può iniziare prima che inizi la precedente); dichiarata la convenzione dei tempi a istanti 0-based (EF = ES + durata) e la sua equivalenza con la convenzione 1-based delle slide (EF = ES + durata − 1).
- **v.2.1.0**: Aggiunta la tabella di **raccordo con la WBS** (tracciabilità nodo di rete ↔ attività della WBS, con nota sulle attività continuative/on-demand che non formano nodi), a supporto della doppia lettura della WBS dichiarata nell'Allegato 3.1 v.1.3.0.
- **v.1.1.0**: Chiarito che i file immagine del network diagram e del Gantt non sono stati prodotti per questo elaborato; restano documentati tramite le tabelle/CSV già presenti.
- **v.1.2.0**: Creato il companion `Allegato3.5-NetworkGantt.html` — Network Diagram (grafo a 3 rami: Critico/Game Engine/Chat-Social, nodi posizionati per ES/EF, frecce rosse spesse sul critical path e blu sottili sulle non critiche, milestone M1-M4 a rombo) e Gantt Chart (20 barre su calendario reale 15-Ott-2025→15-Mag-2026, milestone M1-M7, colori per criticità) generati via script Python dai valori verificati delle tabelle Forward/Backward Pass e Sprint di questo documento. Sostituisce la descrizione puramente testuale della "Struttura Visuale" con un diagramma effettivamente colorato e a colpo d'occhio.
- **v.2.0.0**: Ricalibrazione del CPM sul calendario reale. Le durate precedenti erano nominali e la loro somma sul percorso critico (170 gg) superava i giorni lavorativi effettivamente disponibili nei 7 mesi di progetto (146 al 15 Mag). Tutte le durate sono ora espresse in giorni lavorativi netti (festività italiane escluse) e coerenti con le date del Gantt; il percorso critico risulta di **141 gg lavorativi** (15 Ott → 8 Mag) con ≈1 settimana di margine sul lancio del 15 Mag. Esplicitato il **fast tracking P→R** (legame Start-to-Start con lag 31 gg), che prima era un overlap non dichiarato nel Gantt; float ricalcolati (Game Engine 30→22, Chat/Social 50→37); milestone M1-M4 allineate alle nuove date di fine attività (in particolare M4 corretta da 14-Mar a 27-Mar, fine di P). Rigenerato l'HTML companion con lo script `tools/genera-networkgantt-html.py` (ora versionato).
