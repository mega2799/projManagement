# Allegato 2.11 - Project Management Life Cycle Models
## v.1.0.0 – 2025-09-30 10:00:00

Questo documento descrive le **metodologie di Project Management** adottate per il progetto MaraffaOnline e giustifica la scelta di un **approccio ibrido** che combina modelli diversi per sottosistemi differenti.

---

## Introduzione: Perché un Approccio Ibrido?

PlayHeritage Labs ha scelto di **non adottare una singola metodologia monolitica** (es. solo Waterfall o solo Agile) ma di applicare il modello più adatto a ciascun sottosistema, in base a:
- **Grado di incertezza dei requisiti**
- **Complessità tecnica**
- **Dipendenze tra componenti**
- **Necessità di feedback continuo**

Questo approccio pragmatico è in linea con le best practice moderne di project management, che privilegiano l'**adattabilità** rispetto al dogmatismo metodologico.

---

## Modelli PM Utilizzati: Panoramica

### 1. Linear/Waterfall
**Quando**: Requisiti chiari, stabili e ben definiti fin dall'inizio
**Caratteristiche**:
- Fasi sequenziali: Analisi → Design → Implementazione → Test → Deploy
- Documentazione dettagliata upfront
- Modifiche costose e rare
- Validazione finale a fine sviluppo

### 2. Agile Iterativo (Scrum-like)
**Quando**: Requisiti noti ma necessità di feedback continuo
**Caratteristiche**:
- Sprint brevi (2 settimane)
- Incrementi funzionanti rilasciati regolarmente
- Demo bi-settimanali al committente
- Raffinamento continuo basato su feedback

### 3. Agile Adattivo (Kanban + Spike)
**Quando**: Alta incertezza tecnica, necessità di sperimentazione
**Caratteristiche**:
- Nessuno sprint rigido, flusso continuo
- Prototipazione rapida (spike tecnici)
- Pivot frequenti in base ai risultati
- Decision point espliciti per go/no-go

### 4. Incrementale
**Quando**: Componenti indipendenti che possono essere sviluppati e rilasciati in sequenza
**Caratteristiche**:
- Ogni incremento aggiunge valore standalone
- Prioritizzazione MoSCoW
- Release graduale di features
- Riduzione rischio di incompletezza

---

## Mappatura Sottosistemi → Metodologie

| # | Sottosistema | Metodologia | Motivazione Primaria |
|---|--------------|-------------|---------------------|
| 1 | Game Engine | **Waterfall** | Requisiti fissi (regole tradizionali) |
| 2 | Backend Server | **Agile Iterativo** | Integrazione continua con frontend |
| 3 | Real-Time Communication | **Agile Adattivo** | Alta incertezza tecnica |
| 4 | Frontend Web | **Agile Iterativo** | Feedback continuo UX |
| 5 | Mobile Application | **Incrementale** | Won't Have MVP, post-lancio |
| 6 | Social & Community | **Incrementale** | Features indipendenti prioritizzabili |
| 7 | Infrastructure & DevOps | **Incrementale** | Setup progressivo capabilities |

---

## Analisi Dettagliata per Sottosistema

### 1️⃣ Game Engine: Linear/Waterfall ✅

**Metodologia scelta**: **Waterfall** (modello lineare sequenziale)

**Motivazioni**:

1. **Requisiti completamente definiti e stabili**:
   - Le regole della Maraffa romagnola esistono da decenni
   - Nessuna ambiguità: la community fornisce documentazione completa
   - Non servono iterazioni per "scoprire" i requisiti
   - **Zero tolleranza per variazioni**: implementare regole sbagliate comprometterebbe la fedeltà al gioco tradizionale

2. **Validazione upfront possibile**:
   - Francesca Giuliani (esperta) valida la specifica delle regole prima dello sviluppo
   - Test case possono essere scritti in anticipo (partite di esempio con risultati noti)

3. **Bassa dipendenza da feedback utente durante sviluppo**:
   - Gli utenti non devono "provare" le regole per validarle (le conoscono già)
   - Feedback utente utile solo per UI/UX del gioco, non per la logica

4. **Efficienza massima**:
   - Analisi completa iniziale evita rework
   - Implementazione sistematica riduce bug
   - Test finale validazione against regolamento ufficiale

**Fasi Waterfall applicate**:
```
1. ANALISI (Settimane 1-2)
   - Workshop con Francesca Giuliani
   - Documentazione regole complete (30+ pagine)
   - Identificazione casi limite (es. pareggio, maraffa dichiarata)

2. DESIGN (Settimana 3)
   - Architettura classi (Carta, Mazzo, Mano, Giocatore, Partita)
   - Algoritmi calcolo punteggio
   - Diagrammi UML

3. IMPLEMENTAZIONE (Settimane 4-6)
   - Codifica sistematica classe per classe
   - Unit test per ogni funzione
   - Code review obbligatoria

4. TEST (Settimana 7)
   - Test suite completo (300+ test case)
   - Simulazione partite contro risultati attesi
   - Validazione finale Francesca Giuliani

5. DEPLOYMENT (Settimana 8)
   - Integrazione con Backend Server
   - Deploy su server staging
```

**Rischi mitigati**:
- ✅ Evita scope creep (regole chiaramente delimitate)
- ✅ Riduce bug logici critici (analisi approfondita upfront)

**Rischi accettati**:
- ⚠️ Modifiche tardive costose (ma improbabili dato requisiti stabili)

---

### 2️⃣ Backend Server: Agile Iterativo (Scrum-like) ✅

**Metodologia scelta**: **Agile Iterativo**

**Motivazioni**:

1. **Integrazione continua necessaria**:
   - Il backend espone API per il frontend
   - Feedback rapido dal team frontend è critico per adattare API
   - Esempio: endpoint `/api/matches/create` potrebbe richiedere campi diversi da quelli inizialmente previsti

2. **Requisiti evoluti durante sviluppo**:
   - Struttura dati (database schema) può essere ottimizzata iterativamente
   - Query performance issues scoperti solo durante testing con dati reali

3. **Delivery incrementale di valore**:
   - Sprint 1: autenticazione base
   - Sprint 2: gestione partite CRUD
   - Sprint 3: integrazione WebSocket
   - Ogni sprint rilascia API utilizzabili dal frontend

4. **Riduzione rischio di integration hell**:
   - Integrazione continua evita "big bang integration" a fine progetto

**Sprint Planning (2 settimane per sprint)**:
```
SPRINT 1 (Settimane 3-4): Autenticazione
- User stories: US-1.1 (Registrazione), US-1.2 (Login), US-1.3 (Ospite)
- Deliverable: API /auth/* funzionanti
- Demo: registrazione + login via Postman

SPRINT 2 (Settimane 5-6): Gestione Partite
- User stories: US-2.1, US-2.2 (Creazione stanze)
- Deliverable: API /matches/* CRUD
- Demo: creazione stanza via frontend mockup

SPRINT 3 (Settimane 7-8): Integrazione Real-Time
- User stories: US-3.1, US-3.2 (Avvio partita, gioca carta)
- Deliverable: API integrate con WebSocket
- Demo: partita completa end-to-end

SPRINT 4 (Settimane 9-10): Features Sociali
- User stories: US-4.1 (Chat), US-5.1 (Amici)
- Deliverable: API amicizie + persistenza messaggi chat
- Demo: chat funzionante in partita

SPRINT 5 (Settimane 11-12): Statistiche & Polish
- User stories: US-6.1 (Stats), bug fixing
- Deliverable: API stats + ottimizzazioni performance
```

**Cerimonie Agile**:
- **Daily Stand-up**: 9:30 ogni mattina (15 min)
- **Sprint Review**: Demo bi-settimanale al committente (venerdì, 1h)
- **Sprint Retrospective**: Venerdì dopo demo (30 min)
- **Sprint Planning**: Lunedì inizio sprint (1h)

**Metriche monitorate**:
- Velocity (Story Points completati per sprint)
- Burn-down chart
- Code coverage (target: 80%+)

---

### 3️⃣ Real-Time Communication: Agile Adattivo (Kanban + Spike) ⚠️

**Metodologia scelta**: **Agile Adattivo** (approccio sperimentale)

**Motivazioni**:

1. **Incertezza tecnica massima** (RISCHIO CRITICO):
   - Nessuno nel team ha esperienza WebSocket production-ready
   - Problemi tecnici potrebbero richiedere pivot completo (es. cambio libreria Socket.IO → altro)
   - Non è possibile stimare accuratamente upfront

2. **Necessità di spike tecnici**:
   - **Spike** = time-boxed research/prototyping per ridurre incertezza
   - Settimane 1-2: Spike "WebSocket Proof-of-Concept"
     - Obiettivo: 4 client sincronizzano stato semplificato
     - Success criteria: latency < 500ms, sincronizzazione corretta
     - Go/No-Go decision point al giorno 15

3. **Decision points espliciti**:
   - **Giorno 15**: Se spike fallisce → attivare piano di contingenza (consulente esterno Dr. Stefano Nardi)
   - **Giorno 30**: Se con consulente non funziona → ESCALATION al committente (rischio progetto)

4. **Flessibilità massima**:
   - Niente sprint rigidi: lavoro continuo su board Kanban
   - Priorità dinamica: se bug critico scoperto, tutto il team switcha
   - Pair programming intensivo (Elena + Sara) per knowledge sharing

**Approccio Kanban Board**:
```
┌─────────────┬─────────────┬─────────────┬───────────┐
│ BACKLOG     │ IN PROGRESS │ TESTING     │  DONE     │
├─────────────┼─────────────┼─────────────┼───────────┤
│ • Gestione  │ • WebSocket │             │ • Spike   │
│   latency   │   server    │             │   PoC     │
│ • Gestione  │   setup     │             │           │
│   disconn.  │             │             │           │
│ • Chat      │             │             │           │
│   real-time │             │             │           │
└─────────────┴─────────────┴─────────────┴───────────┘
```

**WIP Limit**: Max 2 task in progress (focus vs parallelismo)

**Fasi adattive**:
```
FASE 1: SPIKE TECNICO (Settimane 1-2)
├─ Obiettivo: Provare fattibilità tecnica
├─ Team: Elena + Sara (dedicato 100%)
├─ Deliverable: Prototipo 4 client sincronizzati
└─ Go/No-Go: Giorno 15

FASE 2: IMPLEMENTAZIONE CORE (Settimane 3-5)
├─ Assumendo spike success
├─ Implementare:
│   ├─ Gestione connessioni
│   ├─ Room-based broadcasting
│   └─ Eventi di gioco
└─ Testing continuo con 4 device simultanei

FASE 3: HARDENING (Settimane 6-8)
├─ Gestione disconnessioni
├─ Ottimizzazione latency
├─ Load testing (100 partite simultanee)
└─ Bug fixing aggressivo
```

**Rischi gestiti**:
- ✅ **Piano di contingenza chiaro** (consulente esterno)
- ✅ **Early failure detection** (spike upfront)
- ✅ **Escalation path definito** (se tutto fallisce)

---

### 4️⃣ Frontend Web: Agile Iterativo (Scrum-like) ✅

**Metodologia scelta**: **Agile Iterativo**

**Motivazioni**:

1. **Feedback UX continuo essenziale**:
   - L'interfaccia deve ricreare il "calore" della tradizione
   - Beta tester devono provare mockup interattivi, non solo statici
   - Iterazioni rapide su design basate su feedback

2. **Co-design con community**:
   - Demo bi-settimanali con Maraffa Forever
   - Think Aloud Protocol sessions
   - A/B testing su scelte critiche (es. drag&drop vs click per giocare carta)

3. **Dipendenza dal backend**:
   - Frontend consuma API in evoluzione
   - Iterazioni allineate con sprint backend

**Sprint sincronizzati con Backend**:
```
SPRINT 1 (Settimane 3-4): Login & Registrazione
- Implementazione form con validazione real-time
- Integrazione API /auth/*
- Demo: flusso completo registrazione → login

SPRINT 2 (Settimane 5-6): Dashboard & Creazione Stanze
- Implementazione dashboard con lista stanze
- Form creazione stanza (pubblica/privata)
- Demo: creazione e join stanza

SPRINT 3 (Settimane 7-8): Tavolo da Gioco ⭐ (CRITICO)
- Implementazione schermata tavolo con 4 giocatori
- Animazioni carte
- Integrazione WebSocket per real-time
- Demo: partita completa giocabile

SPRINT 4 (Settimane 9-10): Chat & Features Sociali
- Chat in-game
- Sistema amicizie (UI)
- Demo: chat funzionante durante partita

SPRINT 5 (Settimane 11-12): Statistiche & Polish
- Pagina statistiche personali
- Ottimizzazioni performance (lazy loading, bundle size)
- Responsive design finale (mobile)
```

**Tecniche UX Agile**:
- **Mockup interattivi** (Figma prototypes) prima di codificare
- **User testing ogni 2 settimane** (5 utenti rappresentativi)
- **System Usability Scale (SUS)** misurato a fine ogni sprint (target: 75+)

---

### 5️⃣ Mobile Application: Incrementale ❌ (Won't Have MVP)

**Metodologia scelta**: **Incrementale** (ma rinviato post-MVP)

**Motivazioni**:

1. **Budget/tempo insufficienti**:
   - Sviluppare app nativa iOS + Android richiederebbe 3-4 mesi aggiuntivi
   - Budget €25.000 non copre sviluppo mobile

2. **Alternativa responsive web**:
   - Frontend web responsive utilizzabile da mobile browser
   - Performance accettabile su iPhone/Android moderni
   - Riduce scope MVP senza compromettere usabilità mobile

**Pianificazione futura (v1.1, post-lancio)**:
```
FASE 1: App iOS
├─ Utilizzare React Native (riuso codice)
├─ Focus su iPhone (mercato premium)
└─ Durata stimata: 2 mesi

FASE 2: App Android
├─ Port da iOS
├─ Testing su device popolari (Samsung, Xiaomi)
└─ Durata stimata: 1.5 mesi

FASE 3: Features Mobile-Specific
├─ Notifiche push
├─ Offline mode (cache partite recenti)
└─ Durata stimata: 1 mese
```

**Approccio incrementale**:
- Ogni fase rilascia app funzionante standalone
- Nessuna dipendenza tra iOS e Android
- Priorità iOS first (community Maraffa Forever usa prevalentemente iPhone)

---

### 6️⃣ Social & Community Features: Incrementale ✅

**Metodologia scelta**: **Incrementale**

**Motivazioni**:

1. **Features indipendenti tra loro**:
   - Sistema amicizie funziona senza chat globale
   - Chat in-game funziona senza classifiche
   - Statistiche funzionano senza profili pubblici

2. **Prioritizzazione MoSCoW chiara**:
   - **Must Have**: Chat in-game, login/profilo base
   - **Should Have**: Sistema amicizie
   - **Could Have**: Classifiche, chat globale
   - **Won't Have** (MVP): Tornei, achievements

3. **Riduzione rischio incompletezza**:
   - Anche se tempo scade, almeno Must Have completato
   - Nessuna feature "metà fatta" rilasciata

**Sequenza incrementale**:
```
INCREMENTO 1 (Sprint 2): Login & Profilo Base
├─ Registrazione, login, profilo minimale
├─ COMPLETO e funzionante
└─ Rilascio: API + frontend

INCREMENTO 2 (Sprint 4): Chat In-Game (MUST)
├─ WebSocket chat durante partita
├─ COMPLETO e funzionante
└─ Rilascio: integrato in gameplay

INCREMENTO 3 (Sprint 5): Sistema Amicizie (SHOULD)
├─ Ricerca utenti, richieste, lista amici
├─ COMPLETO e funzionante
└─ Rilascio: se tempo sufficiente

INCREMENTO 4 (Sprint 6): Statistiche Personali (MUST)
├─ Partite vinte/perse, win rate
├─ COMPLETO e funzionante
└─ Rilascio: integrato in profilo

INCREMENTO 5 (Backlog): Classifiche (COULD)
├─ Solo se tutto precedente completato
└─ Altrimenti rinviato a v1.1
```

**Vantaggi approccio**:
- ✅ Riduce rischio di deadline mancata con feature incomplete
- ✅ Permette rilascio anticipato (soft launch) se necessario
- ✅ Feedback utenti su incrementi precedenti informa sviluppo successivi

---

### 7️⃣ Infrastructure & DevOps: Incrementale ✅

**Metodologia scelta**: **Incrementale**

**Motivazioni**:

1. **Setup progressivo evita over-engineering**:
   - Partire con infrastruttura minimale (single server)
   - Aggiungere complessità solo quando necessario
   - Evitare costi infrastruttura inutili all'inizio

2. **Capabilities aggiunte per layer**:
   - Layer 1: Hosting + database (necessario da subito)
   - Layer 2: CI/CD (riduce errori deployment)
   - Layer 3: Monitoring (identifica problemi production)
   - Layer 4: Auto-scaling (solo se traffico lo richiede)

**Sequenza incrementale**:
```
INCREMENTO 1 (Settimana 1): Setup Base
├─ Server dedicato Hetzner (€50/mese)
├─ PostgreSQL installato
├─ SSH access configurato
└─ COMPLETO: ambiente dev funzionante

INCREMENTO 2 (Settimana 2): Containerizzazione
├─ Docker per backend, frontend, database
├─ Docker Compose per orchestrazione
└─ COMPLETO: ambiente replicabile

INCREMENTO 3 (Settimana 4): CI/CD Pipeline
├─ GitLab CI setup
├─ Automated testing su push
├─ Deploy automatico su branch main
└─ COMPLETO: deployment automatizzato

INCREMENTO 4 (Settimana 6): Monitoring
├─ Logging centralizzato (Loki)
├─ Uptime monitoring (UptimeRobot)
├─ Error tracking (Sentry)
└─ COMPLETO: visibilità production

INCREMENTO 5 (Settimana 10): Backup & Recovery
├─ Backup database giornaliero automatico
├─ Disaster recovery plan testato
└─ COMPLETO: resilienza dati

INCREMENTO 6 (Post-lancio, se necessario): Scalabilità
├─ Load balancer (solo se > 500 utenti simultanei)
├─ Database read replicas
└─ OPZIONALE: dipende da successo MVP
```

**Vantaggi approccio**:
- ✅ Riduce costi iniziali (no over-provisioning)
- ✅ Incrementi validati prima di aggiungere complessità
- ✅ Scalabilità preparata ma non implementata upfront (YAGNI principle)

---

## Matrice Decisionale: Quale Metodologia per Quale Sottosistema?

| Caratteristica Sottosistema | Waterfall | Agile Iterativo | Agile Adattivo | Incrementale |
|----------------------------|-----------|-----------------|----------------|--------------|
| Requisiti completamente noti | ✅ SÌ | ❌ No | ❌ No | 🔹 Parziale |
| Feedback continuo necessario | ❌ No | ✅ SÌ | ✅ SÌ | ❌ No |
| Alta incertezza tecnica | ❌ No | ❌ No | ✅ SÌ | ❌ No |
| Features indipendenti prioritizzabili | ❌ No | 🔹 Parziale | ❌ No | ✅ SÌ |
| Integrazione continua con altri sistemi | ❌ No | ✅ SÌ | 🔹 Parziale | ❌ No |

**Legenda**: ✅ SÌ (ottimo fit) | 🔹 Parziale (fit moderato) | ❌ No (non adatto)

---

## Coordinamento tra Metodologie Diverse

### Challenge: Come sincronizzare approcci diversi?

**Soluzione: Unified Sprint Cadence + Milestones Comuni**

Anche se i sottosistemi usano metodologie diverse, tutti seguono:
1. **Sprint bi-settimanali comuni** (anche se Waterfall/Incrementale non sprint-based internamente)
2. **Demo bi-settimanali al committente** (venerdì)
3. **Milestone mensili comuni** (sincronizzazione integrazione)

**Esempio Milestone 1 (Fine Ottobre)**:
- Game Engine (Waterfall): completata fase Implementazione
- Backend (Agile Iterativo): Sprint 2 completato (gestione partite)
- Real-Time (Agile Adattivo): Spike PoC validato
- Frontend (Agile Iterativo): Sprint 2 completato (dashboard)
- Infrastructure (Incrementale): Incremento 3 (CI/CD) completato

**Integration Points**:
- Settimana 4, 8, 12: Integration Sprint (no nuove feature, solo integrazione e bug fixing)

---

## Conclusioni e Raccomandazioni

### Perché l'Approccio Ibrido è la Scelta Giusta per MaraffaOnline

1. **Pragmatismo sopra dogmatismo**: ogni sottosistema ha caratteristiche diverse, forzare una singola metodologia sarebbe inefficiente

2. **Gestione rischio ottimale**:
   - Waterfall riduce rischio su Game Engine (requisiti stabili)
   - Agile Adattivo gestisce rischio su Real-Time (incertezza massima)

3. **Massimizzazione efficienza**:
   - Nessuno overhead inutile (es. sprint planning su Game Engine non serve)
   - Feedback continuo solo dove utile (frontend, backend)

4. **Scalabilità approccio**: questo modello ibrido è riutilizzabile per progetti futuri di PlayHeritage Labs (altri giochi tradizionali)

### Lezioni Apprese da Applicare

- ✅ **Decision point espliciti** cruciali per sottosistemi ad alto rischio
- ✅ **Sincronizzazione via milestone comuni** funziona meglio di sprint rigidi ovunque
- ✅ **Documentazione upfront** (Waterfall) riduce drasticamente bug logici

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Lead Developer) + Team completo
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 01/10/2025
