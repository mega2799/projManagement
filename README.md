# Progetto MaraffaOnline - Project Management

Relazione per l'esame di Project Management - Università di Bologna

## Struttura del Progetto

```
MaraffaOnline/
├── claude.md                    # File di contesto per Claude AI (LEGGERE SEMPRE)
├── README.md                    # Questo file
├── Relazione/                   # Relazione principale in LaTeX
│   ├── main.tex                # File principale LaTeX
│   ├── capitoli/               # Capitoli della relazione
│   │   ├── 01_introduzione.tex
│   │   ├── 02_scoping.tex
│   │   ├── 03_planning.tex
│   │   ├── 04_launching.tex
│   │   ├── 05_monitoring.tex
│   │   └── 06_closing.tex
│   └── bibliografia.bib        # Bibliografia (se necessaria)
├── Scoping/                    # Allegati fase Scoping
│   ├── Allegato2.1-ConditionsOfSatisfaction.md
│   ├── Allegato2.2-ProjectOverviewStatement.md
│   ├── Allegato2.3-RiskAnalysis.md
│   ├── Allegato2.4-BusinessModelCanvas.md
│   ├── Allegato2.5-AnalisiSWOT.md
│   ├── Allegato2.6-Prototyping.md
│   ├── Allegato2.7-RequirementsBreakdownStructure.md
│   ├── Allegato2.8-UserStories.md
│   └── Allegato2.9-UserFlow.md
├── Planning/                   # Allegati fase Planning
│   ├── Allegato3.1-WorkBreakdownStructure.md
│   ├── Allegato3.2-Moscow.md
│   ├── Allegato3.3-ProductBacklog.md
│   ├── Allegato3.4-CashFlow.md
│   └── Allegato3.5-ProjectNetworkDiagram-Gantt.md
├── Launching/                  # Allegati fase Launching
│   ├── Allegato4.1-RASCI.md
│   └── Allegato4.2-RegoleOperative.md
├── MonitoringControl/          # Allegati fase Monitoring & Control
│   ├── Allegato5.1-StoplightReports.md
│   └── Allegato5.2-EarnedValue.md
├── Closing/                    # Allegati fase Closing
│   └── Allegato6.1-FinalReport.md
└── img/                        # Immagini, diagrammi, grafici
    └── .gitkeep
```

## Progetto: MaraffaOnline

### Descrizione
Piattaforma web per giocare online a Maraffa, tradizionale gioco di carte italiano, con funzionalità multiplayer, chat, classifiche e tornei.

### Sottosistemi Principali
1. **Sistema di Autenticazione e Utenti**
2. **Game Logic (Regole Maraffa)**
3. **Middleware/Backend**
4. **Sistema di Chat**
5. **Frontend Web**
6. **Sistema di Classifiche e Tornei**

## Workflow di Lavoro

1. **Prima di iniziare una sessione**: Leggi sempre `claude.md`
2. **Controlla la TODO list**: Vedi lo stato dei task
3. **Lavora su un task**: Marca come "in_progress"
4. **Completa un task**: Marca come "completed"
5. **Salva il contesto**: Aggiorna `claude.md` se necessario

## Comandi Utili

### Compilare LaTeX
```bash
cd Relazione
pdflatex main.tex
bibtex main (se serve bibliografia)
pdflatex main.tex
pdflatex main.tex
```

### Vedere TODO list
Chiedi a Claude: "Mostrami la TODO list"

### Aggiornare TODO
Claude aggiornerà automaticamente i task completati

## Note Importanti

- Ogni allegato deve avere header con versione e data
- Usare sempre formato markdown per gli allegati
- Creare diagrammi con draw.io o Mermaid
- Salvare grafici in formato PNG o JPG nella cartella img/
- La relazione finale deve essere autosufficiente e ben argomentata

## Contatto Docente

Prima della consegna, concordare l'elaborato con:
- Marco A. Boschetti
- Email: marco.boschetti@unibo.it

## Riferimenti

- Relazione esempio: ../relazioneSofy.pdf
- Linee guida: ../slides/Progetto - Linee Guida - Ver.2.3.pdf
- Documentazione PM: ../PM_documentation/
