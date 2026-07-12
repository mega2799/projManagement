# Appunti per la Relazione (materiale estratto dagli allegati)

> **File di lavoro** — NON è un deliverable e NON è incluso in `main.tex`.
> Raccoglie i contenuti di **giustificazione/teoria** rimossi dagli allegati (che devono restare artefatti operativi, Sezione 2) per essere rielaborati nei **capitoli della relazione LaTeX** (Sezione 1 – descrizione dell'approccio). Ogni blocco indica l'allegato di provenienza.

---

## Cap. 3 — Planning

### Perché separare il Product Backlog (Agile) da WBS/Gantt (universale)
_Provenienza: Allegato 3.3 - Product Backlog (sezioni "Nota: Ambito" e "Perché Questa Separazione?")._

La separazione tra Product Backlog e WBS/Gantt è intenzionale e riflette la natura degli strumenti:

- **Product Backlog** = strumento Scrum/Agile puro. Gestito dal Product Owner (Marco Venturi), prioritizzato in modo continuo con MoSCoW dinamico, item stimati in story points (Fibonacci), organizzato per sprint con velocity tracking. Include **solo** i sottosistemi gestiti con approcci iterativi/adattivi: Backend Server, Real-Time Communication, Frontend Web, Social & Community.
- **WBS + Gantt** = strumenti di Project Management universali. Gestiti dal Project Manager, includono **tutte** le metodologie (Waterfall, Agile, Incrementale), attività stimate in giorni lavorativi, timeline con critical path analysis.

Mischiare metodologie diverse nel Backlog comprometterebbe la coerenza della gestione sprint e la chiarezza dei ruoli Scrum (Product Owner, Scrum Master, Development Team). Per questo Game Engine (Waterfall) e Infrastructure & DevOps (Incrementale) sono tracciati esclusivamente in WBS (Allegato 3.1) e Gantt (Allegato 3.5), non nel Backlog. In sintesi: per i sottosistemi Agile il Product Backlog è la fonte primaria della gestione operativa degli sprint; per la visione d'insieme del progetto si fa riferimento a WBS e Gantt.

### Lettura dei numeri di velocity (Scrum pura vs team-wide)
_Provenienza: Allegato 3.3 - Product Backlog ("Lettura dei numeri di Velocity"). Rilevante anche per il Cap. 5 - Monitoring & Control (dove si cita la velocity 38,3)._

- La **velocity di 38,3 SP/sprint** monitorata nel Cap. 5 è **team-wide**: somma il lavoro completato su tutto il progetto (Backlog Agile + Game Engine in Waterfall + Infrastructure Incrementale), non solo le user stories del Backlog.
- I **310 SP del Product Backlog Agile** sono il sottoinsieme di user stories gestite con Scrum (Backend/Real-Time/Frontend/Social): diviso per 15 sprint ≈ 21 SP/sprint di velocity Scrum pura.
- La differenza non è un'incoerenza: è la distinzione tra "metrica Scrum" (Backlog) e "metrica gestionale di team" (Monitoring). Utile spiegarla in relazione per prevenire la domanda all'orale.

---

## Registro: sezioni "Fonti e Riferimenti" commentate negli allegati

_Commentate con `<!-- -->` (non renderizzate, ma presenti nel file). Da reinserire o sostituire con fonti del corso (Wysocki, PMBOK, Scrum Guide) se in futuro lo si desidera._

- [x] `Planning/Allegato3.3-ProductBacklog.md`
- [x] `Planning/Allegato3.2-MoSCoW.md`
- [x] `Planning/Allegato3.4-CashFlow.md`
- [x] `Planning/Allegato3.5-ProjectNetworkDiagram-Gantt.md`
- [x] `Launching/Allegato4.1-ProjectKickOffMeeting.md`
- [x] `Launching/Allegato4.2-RASCI-RegoleOperative.md` — **NOTA**: oltre ai link-blog "RASCI Matrix", questo file conteneva riferimenti solidi ("Regole Operative": Scrum Guide 2020, PMBOK 7th Edition, Lean/Toyota, Atlassian Team Playbooks). Sono fonti valide del corso: valgono la pena di essere citate nella relazione o reinserite come bibliografia vera.

## Note su altri allegati snelliti

- **Allegato 3.1 - WBS**: la sezione "Note Metodologiche → Allineamento con Metodologie per Sottosistema" (che ripeteva l'Allegato 2.11) è stata condensata a un rimando. Il contenuto vive già in 2.11 e va nella relazione, Cap. 2/3.
- **Allegato 2.11 - Life Cycle Models**: la panoramica teorica dei 4 modelli PM (definizioni da manuale) è stata condensata in una legenda-tabella; la giustificazione applicata (mappatura per sottosistema, matrice decisionale, coordinamento) è rimasta perché è l'oggetto stesso dell'allegato.
- **Allegato 3.2 - MoSCoW**: i "Principi Applicati" (regola 60/20/20, definizione di Must Have, storico revisioni) sono criteri operativi applicati al progetto → tenuti; tolto solo il tag "(Best Practices 2026)" dal titolo.
