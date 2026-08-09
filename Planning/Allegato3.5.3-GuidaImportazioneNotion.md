# Allegato 3.5.3 - Guida Importazione Gantt Chart in Notion
## v.1.1.0 – 2025-10-28 16:30

Questa guida spiega come importare il file CSV del Gantt Chart MaraffaOnline in Notion e configurare la visualizzazione Timeline (Gantt) ottimale.

> **Nota metodologica.** Questa guida descrive la procedura da seguire per chi volesse effettivamente importare il Gantt in Notion; per questo elaborato accademico i passaggi non sono stati eseguiti (nessun database Notion creato, nessun export PNG/PDF prodotto). Il Gantt è documentato tramite il CSV sorgente (`Allegato3.5.2-GanttData.csv`, che esiste realmente) e la ripartizione per sprint in `Allegato3.5-ProjectNetworkDiagram-Gantt.md`.

---

## File da Importare

**File**: `Allegato3.5.2-GanttData.csv`

**Contenuto**:
- 100+ attività del progetto MaraffaOnline
- 7 milestone principali
- Tutte le dipendenze e date del Critical Path
- Informazioni su assegnatari, sprint, story points, float

---

## Passo 1: Importazione in Notion

### 1.1 Creare un Nuovo Database

1. Apri Notion e vai al workspace dove vuoi creare il Gantt
2. Clicca su "New Page" o usa `/database` in una pagina esistente
3. Scegli "Table - Full page" per creare un database tabella
4. Rinomina la pagina: "MaraffaOnline - Gantt Chart"

### 1.2 Importare il CSV

1. Clicca sui tre puntini `...` in alto a destra del database
2. Seleziona "Merge with CSV"
3. Clicca "Upload a file" e seleziona `Allegato3.5.2-GanttData.csv`
4. Notion rileverà automaticamente le colonne dal CSV
5. Clicca "Import"

**Nota**: Notion creerà automaticamente le proprietà del database basandosi sulle colonne del CSV.

---

## Passo 2: Configurazione Proprietà Database

Dopo l'importazione, verifica e configura le seguenti proprietà:

### 2.1 Proprietà Essenziali per Gantt

| Nome Proprietà | Tipo Notion | Configurazione |
|----------------|-------------|----------------|
| **Nome Attività** | Title | Colonna principale (già impostata) |
| **Data Inizio** | Date | Formato: `DD/MM/YYYY` (es. 15/10/2025) |
| **Data Fine** | Date | Formato: `DD/MM/YYYY` (es. 25/10/2025) |
| **Status** | Select | Opzioni: `Not Started`, `In Progress`, `Completed`, `Blocked` |
| **Priority** | Select | Opzioni: `P0`, `P1`, `P2`, `P3` |
| **Assegnatario** | Person | Tagga membri del team (o lascia come Text se non hai membri Notion) |
| **Critical Path** | Checkbox | Selezionato = attività sul critical path |
| **Sprint** | Select | Opzioni: `Sprint 0`, `Sprint 1`, ..., `Sprint 14` |
| **Sottosistema** | Select | Opzioni: `Backend Server`, `Game Engine`, `Frontend Web`, `Real-Time Communication`, `Infrastructure`, `Social & Community`, `Testing`, `Launch`, `Milestone` |

### 2.2 Proprietà Aggiuntive

| Nome Proprietà | Tipo Notion | Descrizione |
|----------------|-------------|-------------|
| **Durata (giorni)** | Number | Durata attività in giorni lavorativi |
| **Story Points** | Number | Effort stimato (scala Fibonacci) |
| **Float (giorni)** | Number | Margine di ritardo senza impatto progetto |
| **Predecessori** | Text | ID attività che devono completarsi prima |
| **Note** | Text | Dettagli aggiuntivi sull'attività |

### 2.3 Conversione Tipi (se necessario)

Se Notion ha importato una colonna come "Text" invece del tipo corretto:

1. Clicca sull'header della colonna
2. Seleziona "Edit property"
3. Cambia "Property type" al tipo corretto (es. Date, Number, Select)
4. Clicca "Done"

**Attenzione**: Notion potrebbe non riconoscere automaticamente le date nel formato `YYYY-MM-DD` del CSV. Verifica che le colonne "Data Inizio" e "Data Fine" siano di tipo **Date**.

---

## Passo 3: Creare la Vista Timeline (Gantt Chart)

### 3.1 Aggiungere Vista Timeline

1. In alto a sinistra del database, clicca su "+ Add a view"
2. Seleziona "Timeline"
3. Rinomina la vista: "Gantt Chart - MaraffaOnline"
4. Clicca "Create"

### 3.2 Configurare la Timeline

Nella vista Timeline appena creata:

#### Layout Settings (clicca su `...` → "Layout")

| Impostazione | Valore Consigliato |
|--------------|-------------------|
| **Show week numbers** | Attivato (per allinearsi agli sprint) |
| **Snap to grid** | Giorni (per allineamento preciso) |
| **Date property** | Data Inizio |
| **End date property** | Data Fine |
| **Show events as bars** | Attivato |
| **Show subpages** | Disattivato (se non usi pagine annidate) |

#### Properties Visible on Cards

Clicca su "Properties" in alto a destra della Timeline e seleziona quali mostrare sulle barre:

**Consigliato mostrare**:
- [x] Nome Attività (title)
- [x] Assegnatario
- [x] Critical Path (icona o colore)
- [x] Status
- [x] Durata (giorni)

**Nascondere** (per pulizia visuale):
- [ ] Note
- [ ] Predecessori
- [ ] Float (giorni)

---

## Passo 4: Personalizzazione Visuale

### 4.1 Colori per Critical Path

Per evidenziare visivamente le attività sul critical path:

1. Nella Timeline, clicca su un'attività con `Critical Path = Yes`
2. Clicca sull'icona colore (palette)
3. Seleziona **Rosso** per le attività critiche
4. Ripeti per tutte le attività con Critical Path = Yes

**Automazione (se disponibile)**:
- Se hai Notion Pro, puoi usare le formule per colorare automaticamente:
  - Formula: `if(prop("Critical Path"), "Red", "Default")`

### 4.2 Colori per Near-Critical (Float 1-5 giorni)

1. Filtra le attività con `Float (giorni) > 0` e `Float (giorni) <= 5`
2. Colora in **Arancione**

### 4.3 Colori per Non-Critical (Float > 5 giorni)

1. Filtra le attività con `Float (giorni) > 5`
2. Colora in **Verde**

### 4.4 Evidenziare Milestone

1. Filtra le righe con `Sottosistema = Milestone`
2. Colora in **Nero** o **Viola** (per distinguerle dalle attività)
3. Opzionale: Usa l'icona ◆ (rombo) per le milestone nel nome

---

## Passo 5: Filtri e Viste Aggiuntive

### 5.1 Vista "Solo Critical Path"

1. Crea nuova vista Timeline: "Critical Path Only"
2. Aggiungi filtro: `Critical Path` → `is checked`
3. Risultato: solo le attività rosse sul critical path

### 5.2 Vista "Per Sottosistema"

1. Crea nuova vista Timeline: "Per Sottosistema"
2. Raggruppa per: `Sottosistema`
3. Risultato: attività organizzate per Backend, Frontend, Game Engine, etc.

### 5.3 Vista "Per Assegnatario"

1. Crea nuova vista Timeline: "Per Assegnatario"
2. Raggruppa per: `Assegnatario`
3. Risultato: carico di lavoro per persona

### 5.4 Vista "Sprint Corrente"

1. Crea nuova vista Table: "Sprint Corrente"
2. Aggiungi filtro: `Sprint` → `is` → `Sprint 1` (modifica manualmente ogni 2 settimane)
3. Ordina per: `Data Inizio` (ascending)
4. Risultato: focus sulle attività del prossimo sprint

---

## Passo 6: Aggiornamento Dinamico durante il Progetto

### 6.1 Aggiornare Status Attività

Durante l'esecuzione del progetto:

1. Apri un'attività in corso
2. Cambia `Status` da `Not Started` → `In Progress` → `Completed`
3. La Timeline si aggiornerà automaticamente

### 6.2 Aggiungere Percentuale Completamento (Opzionale)

Se vuoi tracciare il progresso più granularmente:

1. Aggiungi nuova proprietà: `% Completato` (tipo Number, formato Percent)
2. Aggiorna manualmente ogni settimana (es. 0%, 25%, 50%, 75%, 100%)
3. Visualizza nella Timeline come barra di progresso

### 6.3 Slittamenti e Ricalcolo Critical Path

Se un'attività ritarda:

1. Modifica `Data Fine` dell'attività
2. Aggiorna manualmente le `Data Inizio` delle attività dipendenti (controllando colonna `Predecessori`)
3. **Nota**: Notion Timeline non ricalcola automaticamente le dipendenze (a differenza di MS Project). Devi aggiornare manualmente.

### 6.4 Aggiungere Nuove Attività

Se emerge un nuovo task durante il progetto:

1. Clicca "New" in fondo al database
2. Compila tutti i campi (Nome, Date, Predecessori, etc.)
3. L'attività apparirà automaticamente nella Timeline

---

## Passo 7: Esportazione e Condivisione

### 7.1 Condividere con Stakeholder

1. Clicca "Share" in alto a destra del database
2. Invita Giovanni Marchetti (committente) come "Can view"
3. Opzionale: abilita "Public access" per creare link condivisibile

### 7.2 Esportare come PDF/PNG

Notion Timeline non ha export PDF nativo. Workaround:

1. Apri Timeline in fullscreen (icona `⤢`)
2. Usa browser: `Ctrl/Cmd + P` → "Stampa"
3. Seleziona "Salva come PDF"
4. **Risultato**: `gantt-chart-maraffaonline.pdf`

Per PNG (screenshot):

1. Usa tool di screenshot (es. Snipping Tool, Cmd+Shift+4 su Mac)
2. Cattura l'intera Timeline
3. Salva come `img/gantt-chart-maraffaonline.png`

---

## Passo 8: Integrazione con Altri Tool

### 8.1 Sincronizzazione con Google Calendar

Se vuoi vedere le milestone nel calendario:

1. Crea una vista "Calendar" del database
2. Filtra solo `Sottosistema = Milestone`
3. Esporta calendario (.ics) e importa in Google Calendar

### 8.2 Export a Microsoft Project (Avanzato)

Se hai bisogno di calcoli automatici del Critical Path:

1. Esporta da Notion: Database → `...` → "Export" → "CSV"
2. Importa il CSV in Microsoft Project o GanttProject
3. Configura dipendenze con colonna `Predecessors`
4. MS Project calcolerà automaticamente Early Start, Late Finish, Float

---

## Troubleshooting Comune

### Problema 1: Date non Importate Correttamente

**Sintomo**: Colonne "Data Inizio" e "Data Fine" sono vuote o testuali

**Soluzione**:
1. Controlla che il CSV usi formato ISO: `YYYY-MM-DD` (es. 2025-10-15)
2. Riconverti colonne in tipo "Date" manualmente
3. Se necessario, usa formula Notion: `dateFormat(prop("Data Inizio"), "DD/MM/YYYY")`

### Problema 2: Attività non Appaiono nella Timeline

**Sintomo**: Alcune righe del database non sono visibili nella Timeline

**Soluzione**:
1. Verifica che abbiano sia `Data Inizio` che `Data Fine` compilate
2. Controlla filtri attivi nella vista Timeline (potrebbero nascondere attività)

### Problema 3: Barre Troppo Piccole (Attività 1-2 giorni)

**Sintomo**: Attività brevi sono difficili da cliccare

**Soluzione**:
1. Cambia zoom Timeline: clicca su "Week" → "Day" per granularità maggiore
2. Oppure raggruppa task brevi in attività composite (es. A.1, A.2 → A)

---

## Template Notion Consigliato

Se preferisci partire da un template Notion già configurato:

### Struttura Database Raccomandata

```
📊 MaraffaOnline - Gantt Chart
├── 🗂️ Viste:
│   ├── 📅 Timeline - Gantt Completo (default)
│   ├── 🔴 Critical Path Only
│   ├── 📦 Per Sottosistema
│   ├── 👤 Per Assegnatario
│   ├── 🗓️ Sprint Corrente
│   └── 📋 Tabella Completa
├── 🎨 Proprietà:
│   ├── Nome Attività (Title)
│   ├── Data Inizio (Date)
│   ├── Data Fine (Date)
│   ├── Status (Select: Not Started | In Progress | Completed | Blocked)
│   ├── Priority (Select: P0 | P1 | P2 | P3)
│   ├── Critical Path (Checkbox)
│   ├── Sprint (Select: Sprint 0-14)
│   ├── Sottosistema (Select: 9 opzioni)
│   ├── Assegnatario (Person o Text)
│   ├── Durata (giorni) (Number)
│   ├── Story Points (Number)
│   ├── Float (giorni) (Number)
│   ├── Predecessori (Text)
│   └── Note (Text)
└── 🔧 Automazioni (se Notion Pro):
    ├── Auto-colora Critical Path in rosso
    ├── Notifica quando Status = Blocked
    └── Alert quando Data Fine < Oggi e Status ≠ Completed
```

---

## Risorse Aggiuntive

### Guide Notion Ufficiali
- [Notion Timeline View Guide](https://www.notion.so/help/timelines)
- [Notion Database Properties](https://www.notion.so/help/database-properties)

### Alternative a Notion per Gantt
Se Notion non soddisfa le esigenze (es. calcolo automatico Critical Path):

- **Microsoft Project**: Standard di settore, calcolo CPM automatico
- **GanttProject**: Open source, gratuito, compatibile con MS Project
- **TeamGantt**: Online, collaborativo, sincronizzazione team
- **Asana**: Timeline view integrata con task management

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Ultima modifica**: 28/10/2025

**Supporto**: Per domande sull'importazione, contattare marco.venturi@playheritage.it

**Storico revisioni**:
- **v.1.1.0**: Chiarito che la procedura descritta non è stata eseguita per questo elaborato (nessun export prodotto).
