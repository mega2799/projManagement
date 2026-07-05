# Guida Rapida - Creare Grafici Cash Flow in Excel

## File CSV Disponibili

Ho creato 3 file CSV pronti per l'importazione in Excel:

1. **CashFlow-Mensile.csv** - Flussi di cassa mensili (Inflow, Outflow, Net, Saldo)
2. **CashFlow-Categorie.csv** - Spese per categoria (per grafico a torta)
3. **CashFlow-Pagamenti.csv** - Struttura pagamenti committente (opzionale)

---

## Grafico 1: Cash Flow Mensile (Istogramma + Linea)

### Tipo: Grafico Combinato (Colonne Raggruppate + Linea)

**File da usare**: `CashFlow-Mensile.csv`

### Passo 1: Importa il CSV in Excel

1. Apri Excel
2. File → Apri → Seleziona `CashFlow-Mensile.csv`
3. I dati saranno importati automaticamente

### Passo 2: Crea il Grafico

1. **Seleziona dati**: colonne dalla A alla F (tutte le colonne)
2. **Inserisci** → **Grafici consigliati** → Cerca "Combinato"
3. Oppure: **Inserisci** → **Inserisci grafico combinato** → **Colonna a raggruppo - Linea su asse secondario**

### Passo 3: Configura il Grafico

**Asse Primario (Colonne)**:
- **Inflow (€)** → Colonna verde
- **Outflow (€)** → Colonna rossa
- **Net Cash Flow (€)** → Colonna blu (opzionale, puoi nasconderla se confonde)

**Asse Secondario (Linea)**:
- **Saldo Cumulativo (€)** → Linea arancione spessa con marker

### Passo 4: Formattazione Consigliata

**Titolo**: "Cash Flow MaraffaOnline - 7 Mesi (Ott 2025 - Mag 2026)"

**Asse X**: Mese (Mese 0, Mese 1, ..., Mese 7)

**Asse Y Primario (Sinistra)**: "Importo (€)" - Range 0 a 14.000

**Asse Y Secondario (Destra)**: "Saldo Cumulativo (€)" - Range 0 a 10.000

**Legenda**: Posizione in basso o a destra

**Colori Consigliati**:
- Inflow: Verde (#28a745)
- Outflow: Rosso (#dc3545)
- Net Cash Flow: Blu (#007bff)
- Saldo Cumulativo: Arancione (#fd7e14) - Linea spessa con marker

**Griglia**: Attiva solo griglia orizzontale per maggiore leggibilità

### Passo 5: Aggiungi Annotazioni (Opzionale)

Usa **Inserisci → Forme → Freccia** per evidenziare eventi chiave:
- Freccia su "Mese 0": "1° Pagamento €12.500"
- Freccia su "Mese 2": "2° Pagamento €6.250"
- Freccia su "Mese 4": "3° Pagamento €6.250"

---

## Grafico 2: Spese per Categoria (Grafico a Torta)

### Tipo: Grafico a Torta con Percentuali

**File da usare**: `CashFlow-Categorie.csv`

### Passo 1: Importa il CSV in Excel

1. Apri nuovo foglio Excel (o usa nuovo tab)
2. File → Apri → Seleziona `CashFlow-Categorie.csv`

### Passo 2: Crea il Grafico a Torta

1. **Seleziona dati**: colonne A (Categoria) e B (Totale €)
2. **Inserisci** → **Grafici a torta** → **Torta 2D** o **Torta esplosa**
3. Oppure: **Grafici consigliati** → Seleziona "Torta"

### Passo 3: Formattazione

**Titolo**: "Distribuzione Spese per Categoria - MaraffaOnline"

**Etichette Dati**:
- Mostra: **Nome Categoria** + **Percentuale** + **Valore** (€)
- Posizione: Estremità verso l'esterno

**Legenda**: Nascosta (le etichette già mostrano tutto)

**Colori Consigliati** (in ordine di grandezza):
1. **Salari Team** (64%): Blu scuro (#003366) - fetta più grande
2. **Contingency Buffer** (18.7%): Grigio (#6c757d)
3. **Tools e Licenze** (4.4%): Verde (#28a745)
4. **Surplus Finale** (9%): Verde chiaro (#90ee90) - evidenziato
5. **Infrastruttura** (1.1%): Arancione (#fd7e14)
6. **Consulenza Esperta** (1.2%): Viola (#6f42c1)
7. **Marketing Lancio** (0.8%): Rosso (#dc3545)
8. **UAT e Testing** (0.4%): Giallo (#ffc107)
9. **Celebrazione** (0.4%): Rosa (#e83e8c)

**Tip**: Puoi "esplodere" (spostare) la fetta "Surplus Finale" per evidenziarla visivamente.

### Passo 4: Variante - Grafico a Barre Orizzontali

Se il grafico a torta risulta troppo affollato (troppe categorie piccole), usa:

1. **Inserisci** → **Grafico a barre** → **Barre raggruppate orizzontali**
2. Ordina per **Totale (€)** decrescente (Salari Team in alto)
3. Aggiungi **Etichette Dati** alla fine di ogni barra con la percentuale

---

## Grafico 3: Struttura Pagamenti (Opzionale)

### Tipo: Grafico a Cascata (Waterfall) o Colonne

**File da usare**: `CashFlow-Pagamenti.csv`

### Passo 1: Importa e Seleziona

1. Importa `CashFlow-Pagamenti.csv`
2. Seleziona colonne: **Tranche** (A) e **Importo (€)** (C)

### Passo 2: Crea Grafico

**Opzione A - Grafico a Colonne Semplice**:
1. **Inserisci** → **Grafico a colonne** → **Colonne raggruppate**
2. Colori: Blu per tutte le colonne

**Opzione B - Grafico a Cascata** (se Excel 2016+):
1. **Inserisci** → **Grafico a cascata**
2. Excel mostrerà automaticamente la progressione cumulativa dei pagamenti

### Passo 3: Formattazione

**Titolo**: "Struttura Pagamenti Committente - 3 Tranche"

**Asse X**: Tranche (1° Pagamento, 2° Pagamento, 3° Pagamento)

**Asse Y**: "Importo (€)" - Range 0 a 14.000

**Etichette Dati**: Mostra importo su ogni colonna

**Annotazioni**: Aggiungi box di testo con le condizioni:
- "50% upfront - Firma contratto"
- "25% milestone - Scoping + Planning"
- "25% finale - MVP beta"

---

## Tips Generali per Grafici Professionali

### Layout

- **Font**: Calibri o Arial, dimensione 10-12pt per testo, 14-16pt per titolo
- **Bordi**: Rimuovi bordi del grafico per aspetto pulito
- **Sfondo**: Bianco o grigio molto chiaro (#f8f9fa)
- **Griglia**: Solo linee orizzontali, colore grigio chiaro, linee sottili

### Colori

Usa la palette coerente con il progetto MaraffaOnline (vedi `Scoping/Allegato2.7-Prototyping.md`):
- **Rosso mattone** (#b85450) per spese/outflow
- **Verde bottiglia** (#28a745) per entrate/inflow
- **Legno/arancione** (#fd7e14) per saldo/evidenziazioni
- **Blu** (#007bff) per dati secondari

### Accessibilità

- **Non affidarti solo ai colori**: usa anche pattern o etichette
- **Contrasto elevato**: testo nero (#212529) su sfondo bianco
- **Dimensione minima testo**: 10pt per leggibilità

### Export per Relazione

**Per PDF LaTeX**:
1. **Fai clic destro** sul grafico → **Salva come immagine**
2. Formato: **PNG** (alta qualità, 300 DPI)
3. Salva in: `MaraffaOnline/img/cash-flow-maraffaonline.png`
4. Includi nella relazione con:
   ```latex
   \begin{figure}[h]
   \centering
   \includegraphics[width=0.8\textwidth]{img/cash-flow-maraffaonline.png}
   \caption{Cash Flow MaraffaOnline - Ottobre 2025 - Maggio 2026}
   \label{fig:cashflow}
   \end{figure}
   ```

**Per presentazioni PowerPoint/Google Slides**:
1. Copia il grafico da Excel (`Ctrl+C`)
2. Incolla in PowerPoint con **Incolla speciale** → **Immagine PNG**
3. Oppure: incolla come grafico collegato per aggiornamenti dinamici

---

## Esempi di Interpretazione per Relazione

### Grafico Cash Flow Mensile

**Insights da evidenziare nella relazione**:

> "Il grafico del Cash Flow evidenzia 3 momenti critici di inflow (Mese 0, 2, 4) corrispondenti ai pagamenti del committente. Il saldo cumulativo (linea arancione) mostra un andamento positivo per tutti i 7 mesi, con un minimo di €2.250 nel Mese 7 (Mag 2026), garantendo sempre liquidità sufficiente per coprire le spese operative anche nella seconda metà del progetto, priva di nuovi inflow. Il surplus finale di €2.250 (9% del budget) fornisce un buffer adeguato per imprevisti e celebrazione del lancio."

### Grafico Spese per Categoria

**Insights da evidenziare**:

> "La distribuzione delle spese evidenzia che il 64% del budget (€16.000) è allocato ai salari del team, coerentemente con un progetto ad alta intensità di lavoro qualificato. Il Contingency Buffer del 18.7% (€4.664) è allineato alle best practices PM per progetti software con scope evolutivo e durata di 7 mesi. Le spese infrastrutturali sono contenute all'1.1% grazie all'uso di server dedicati economici (Hetzner) e free tier per servizi cloud (Cloudflare, Sentry, SendGrid)."

---

## Troubleshooting

### Problema: CSV non si apre correttamente in Excel

**Soluzione**:
1. Apri Excel → **Dati** → **Da testo/CSV**
2. Seleziona il file CSV
3. Excel mostrerà anteprima: verifica separatore sia "**virgola**"
4. Clicca **Carica**

### Problema: Grafici sembrano "appiattiti" o poco leggibili

**Soluzione**:
1. Ridimensiona l'area del grafico: più largo (16:9 ratio)
2. Aumenta dimensione font delle etichette
3. Usa solo colori ad alto contrasto
4. Riduci numero di elementi nel grafico (es. nascondi "Net Cash Flow" se confonde)

### Problema: Percentuali nel grafico a torta si sovrappongono

**Soluzione**:
1. Usa "**Torta esplosa**" invece di torta normale
2. Oppure: sposta manualmente le etichette cliccandoci sopra
3. Alternativa: usa **Grafico a barre orizzontali** invece di torta

---

## File Salvati

I seguenti file sono pronti nella cartella `Planning/`:

- ✅ `CashFlow-Mensile.csv` → Per grafico temporale Inflow/Outflow/Saldo
- ✅ `CashFlow-Categorie.csv` → Per grafico a torta spese
- ✅ `CashFlow-Pagamenti.csv` → Per grafico pagamenti committente

**Prossimo step**: Importa in Excel e crea i grafici seguendo questa guida!

---

**Creato da**: Claude Code per MaraffaOnline Project Management
**Data**: 2025-10-28
**Basato su**: Allegato 3.4 - Cash Flow Management
