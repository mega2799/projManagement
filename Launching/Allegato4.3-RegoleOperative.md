# Allegato 4.3 - Regole Operative
## v.1.0.0 – 2026-08-10 10:00

Le Regole Operative definiscono come il team lavora insieme ogni giorno: problemi, decisioni, conflitti, generazione di idee e cadenza degli incontri. Approvate nel Project Kick-Off Meeting del 15/10/2025 (Allegato 4.1), valgono per tutti i sottosistemi qualunque sia il loro modello di ciclo di vita (Allegato 2.9). Responsible, Accountable e Consulted di ogni attività sono nell'**Allegato 4.2 - RASCI Matrix**.

---

## 1. Problem Solving

Approccio in cinque passi ispirato al Lean Problem Solving: si risale alla causa root prima di intervenire, così da non ripetere lo stesso problema.

| Passo | Contenuto | Chi |
|-------|-----------|-----|
| 1. Identificazione | Cosa succede, dove, da quando, con quale impatto | Chiunque nel team |
| 2. Causa root | Tecnica dei "5 Whys"; se si prolunga, escalation alla Tech Lead | Responsible + Accountable, Consulted da RASCI |
| 3. Soluzioni | Pro e contro; con impatto alto si privilegia l'intervento rapido | Team; scelta all'Accountable |
| 4. Implementazione | Assegnazione con deadline chiara | Responsible |
| 5. Verifica | Se il problema persiste si torna al passo 2 | Accountable |

I problemi critici vengono ripresi in Sprint Retrospective per capire come prevenirli: miglioramento del processo, non colpevolizzazione.

---

## 2. Decision Making

Approccio consultivo — via di mezzo tra direttivo e pienamente collaborativo: si raccolgono le prospettive del team, ma la responsabilità decisionale resta chiara. Regola d'oro: **decidere al livello più basso possibile, con escalation solo quando necessario**, così che decida chi ha le informazioni più rilevanti.

| Livello | Esempi | Chi decide |
|---------|--------|-----------|
| **Operativo** | Naming convention, librerie minori, fix di bug | Responsible del task (confronto in pair programming o code review) |
| **Tattico** | Architettura, design delle API, schema del database, backlog | Elena Rossi (tecnica) + Marco Venturi (tempi, budget, scope) |
| **Strategico** | Scope, budget, timeline, metodologia | Giovanni Marchetti (Sponsor), su Project Impact Statement del PM |

Le decisioni tattiche sono documentate su Notion; Francesca Giuliani è coinvolta in tutto ciò che riguarda le regole del gioco.

---

## 3. Conflict Resolution

I conflitti sono fisiologici: serve un protocollo che ne garantisca una gestione rapida ed equa. Si procede per **fasi progressive**: (1) confronto diretto tra le parti, in privato, che risolve la maggior parte dei casi alla fonte; (2) mediazione facilitata da Marco o Elena; (3) decisione esecutiva, finale e vincolante. I casi oltre la fase 1 finiscono nell'Issue Log e si rivedono in retrospective.

| Tipo di conflitto | Chi decide | Criteri |
|-------------------|-----------|---------|
| Tecnico (architettura, tecnologie) | Elena Rossi (Tech Lead) | Performance, scalabilità, competenze, time-to-market; poi "disagree and commit" |
| Di priorità (quale feature prima) | Marco Venturi (PM) | Valore vs effort (MoSCoW), critical path, valore per lo stakeholder |
| Di scope o budget | Giovanni Marchetti (Sponsor) | Impatto sul triangolo scope-tempi-budget |
| Interpersonale | Marco come facilitatore neutrale | Soluzione win-win; se irrisolto, escalation alle HR di PlayHeritage Labs (fuori scope) |

---

## 4. Brainstorming

Usato per il problem solving creativo, il design thinking e le feature senza soluzioni ovvie; utile anche in retrospective. Si lavora su lavagna fisica, o su Miro con qualcuno in remoto. Due fasi:

- **Divergent thinking** — generare il maggior numero di idee: nessuna critica, quantità prima della qualità, "Yes, and..." invece di "Yes, but...". Un facilitatore modera e coinvolge i più silenziosi, uno scribe annota tutto.
- **Convergent thinking** — selezionare: affinity mapping delle idee simili, dot voting, e per ogni idea scelta un owner Responsible, un next step (proof of concept, spike o implementazione) e una deadline.

Tecniche usate a seconda del contesto: giro di tavolo per coinvolgere i più introversi, brevi sketch a tempo per i problemi di UI/UX.

---

## 5. Team Meetings

Sei riunioni ricorrenti più incontri ad-hoc: pochi meeting ben definiti, con le sole persone interessate al problema.

| Meeting | Quando (durata) | Partecipanti | Output |
|---------|-----------------|--------------|--------|
| **Daily Standup** | Ogni mattina 09:00–09:15 (15 min) | Team interno, facilita Marco | Fatto / farò / blocker; nessun problem solving in sede, i blocker vanno in follow-up |
| **Sprint Planning** | 1° giorno di sprint (2 h) | Team; Giovanni opzionale | Sprint Goal, stime in Planning Poker (Fibonacci), Sprint Backlog sulla velocity storica; storie scomposte in task assegnati ai Responsible |
| **Backlog Refinement** | Metà sprint (1 h) | Team interno | Chiarimento e stima delle storie del prossimo sprint, incluse le proposte già pesate con MoSCoW |
| **Sprint Review** | Ultimo giorno di sprint (1 h) | Team + Giovanni; Francesca se si dimostrano le regole | Demo del solo increment "Done" (software funzionante, non slide); accettazione o Change Request |
| **Sprint Retrospective** | Dopo la Review (1 h) | Solo team interno | "Start/Stop/Continue" + dot voting; action item con owner e deadline. Vale la "Vegas Rule" |
| **Project Status Meeting** | Venerdì 16:00–17:00 (1 h) | Marco, Elena, Giovanni | Stoplight Report su scope, tempi, budget, qualità, rischi; decisioni dello sponsor |
| **Ad-hoc** | Su necessità | Solo le persone coinvolte | Blocker critici, escalation, decisioni non rinviabili; review meeting alle milestone |

---

## 6. Change Management (sintesi)

Le modifiche a scope, timeline o budget già approvati seguono un processo formale, per evitare lo scope creep. Un Change Request si attiva su richiesta dello stakeholder (feature non prevista nel POS o modifica sostanziale), per impossibilità tecnica emersa in corso d'opera o per un evento esterno.

1. **Submission** — Change Request Form: descrizione, motivazione di business, priorità percepita.
2. **Impact analysis** — Marco ed Elena producono un **Project Impact Statement** con l'impatto su scope, tempi, budget, qualità e risorse, le opzioni (accettare estendendo la timeline, differire a una release successiva, rifiutare) e la raccomandazione motivata del PM.
3. **Decisione dello Sponsor** — accettare, differire o rifiutare; con impatto significativo su budget o timeline si rinegozia il contratto.
4. **Implementation** — aggiornamento di POS, WBS, Gantt e Product Backlog, comunicazione al team, assegnazione a un Responsible.
5. **Tracking** — registrazione nel Change Log fino alla chiusura.

I sottosistemi Agile accolgono il cambiamento come parte del processo; per quelli tradizionali ogni modifica è valutata caso per caso.

---

## 7. Comunicazione (sintesi)

Tre regole d'oro: **asincrono prima di tutto** (Slack ed email, i meeting solo se servono); **trasparenza** (le decisioni importanti si documentano su Notion, single source of truth); **SLA di risposta proporzionati alla priorità**, da poche ore per ciò che blocca il lavoro fino a qualche giorno per le richieste a bassa priorità.

| Canale | Uso |
|--------|-----|
| Slack (canali dedicati) | Comunicazioni generali, daily, discussioni tecniche, urgenze (da leggere entro poche ore) |
| Email | Comunicazioni formali verso sponsor ed enti esterni: report mensili, approvazioni di milestone, Change Request, contratti (subject categorizzato per tipo) |
| Notion | Allegati di PM, note dei meeting (aggiornate a fine giornata), status report settimanali, decisioni tecniche, Change Log (in tempo reale) e Issue Log |

Etiquette: thread per le discussioni lunghe, tag solo quando serve un'azione, parsimonia nelle mention di massa, emoji reactions per l'acknowledge rapido.

---

## Approvazione e adozione

Lette dal team prima del kick-off, chiarite in Q&A e approvate per consensus dal team e formalmente da Giovanni Marchetti (Sponsor) il **15/10/2025**. Sono un **living document**: review ogni 2 sprint in retrospective, modifiche approvate dal PM, versioning su Notion.

**Firme** (simboliche): Marco Venturi (Project Manager) · Elena Rossi (Tech Lead) · Sara Bianchi (Backend Developer) · Luca Moretti (UX Designer / Frontend Developer) · Andrea Conti (DevOps Engineer) · Giovanni Marchetti (Project Sponsor)

<!-- Riferimenti metodologici da valorizzare nella relazione (fonti solide, coerenti col corso): Scrum Guide 2020 per le cerimonie e la Definition of Done; PMI PMBOK 7th Edition per conflict resolution e change control; Lean Problem Solving / Toyota Production System per i 5 Whys; Atlassian Team Playbooks per i team working agreements. Registro in Relazione/_appunti-per-relazione.md. -->

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs) — **Revisionato da**: Elena Rossi (Tech Lead)
**Versione**: v.1.0.0 — **Prossimo review**: 19/12/2025 (venerdì, fine Sprint 4 — Milestone M2)

**Storico revisioni**:
- **v.1.0.0**: primo rilascio come allegato autonomo. Le Regole Operative erano la Parte 2 dell'Allegato 4.2, ora separate e riscritte in forma schematica (una tabella per regola al posto della prosa). Contenuti invariati nella sostanza; recuperato il Backlog Refinement fra le cerimonie e aggiunte le sintesi di Change Management e Comunicazione per le sezioni 4.4 e 4.5 della relazione.
