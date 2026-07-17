# Allegato 2.11 - Project Management Life Cycle Models
## v.1.0.0 – 2025-09-30 10:00:00

Questo documento descrive le metodologie di Project Management adottate per il progetto MaraffaOnline e giustifica la scelta di un approccio ibrido, che combina modelli diversi per sottosistemi differenti.

---

## Introduzione: perché un approccio ibrido?

PlayHeritage Labs ha deciso di non adottare una singola metodologia monolitica (per esempio solo Waterfall o solo Agile), ma di applicare a ciascun sottosistema il modello che meglio si adatta alle sue caratteristiche. I criteri usati per la scelta sono stati:

- il grado di incertezza dei requisiti;
- la complessità tecnica;
- le dipendenze verso gli altri componenti;
- la necessità di feedback continuo.

Si tratta di una scelta pragmatica: dove i requisiti sono stabili conviene pianificare in anticipo, dove invece l'incertezza è alta serve la flessibilità di iterare. Forzare un unico approccio su tutto il progetto avrebbe introdotto overhead inutile in alcuni casi e rigidità dannosa in altri.

---

## Modelli PM utilizzati: panoramica

Nel progetto sono stati impiegati quattro modelli, ciascuno con la propria condizione d'uso tipica:

| Modello | Quando si usa |
|---------|---------------|
| Linear/Waterfall | Requisiti chiari e stabili fin dall'inizio; fasi sequenziali con documentazione upfront e validazione finale |
| Agile Iterativo (Scrum-like) | Requisiti noti ma con necessità di feedback continuo; sprint di 2 settimane con demo al committente |
| Agile Adattivo (Kanban + Spike) | Alta incertezza tecnica; flusso continuo, prototipazione rapida (spike) e decision point go/no-go |
| Incrementale | Componenti indipendenti rilasciabili in sequenza; prioritizzazione MoSCoW e release graduale |

La mappatura di ciascun sottosistema su questi modelli, con la motivazione specifica, è dettagliata nelle sezioni seguenti.

---

## Mappatura sottosistemi → metodologie

| # | Sottosistema | Metodologia | Motivazione primaria |
|---|--------------|-------------|---------------------|
| 1 | Game Engine | Waterfall | Requisiti fissi (regole tradizionali) |
| 2 | Backend Server | Agile Iterativo | Integrazione continua con frontend |
| 3 | Real-Time Communication | Agile Adattivo | Alta incertezza tecnica |
| 4 | Frontend Web | Agile Iterativo | Feedback continuo UX |
| 5 | Mobile Application | Incrementale | Won't Have MVP, post-lancio |
| 6 | Social & Community | Incrementale | Features indipendenti prioritizzabili |
| 7 | Infrastructure & DevOps | Incrementale | Setup progressivo delle capabilities |

---

## Analisi dettagliata per sottosistema

### 1. Game Engine: Linear/Waterfall

Metodologia scelta: Waterfall (modello lineare sequenziale).

Il Game Engine è il candidato ideale per un approccio a cascata perché i suoi requisiti sono già definiti e stabili. Le regole della Maraffa romagnola esistono da decenni, non presentano ambiguità e sono documentate in modo completo dalla community: non c'è quindi bisogno di iterazioni per "scoprire" cosa realizzare. Al contrario, qui la fedeltà al gioco tradizionale è vincolante — implementare una regola sbagliata comprometterebbe l'intera esperienza — per cui la tolleranza alle variazioni è praticamente nulla.

La stabilità dei requisiti rende possibile una validazione a monte: Francesca Giuliani, esperta di gioco, approva la specifica delle regole prima che lo sviluppo cominci, e i test case possono essere scritti in anticipo partendo da partite di esempio con risultato noto. Durante lo sviluppo il feedback degli utenti conta poco sulla logica di gioco (gli utenti le regole le conoscono già) e resta utile solo per l'interfaccia. Un'analisi iniziale accurata riduce quindi il rework e i bug logici, e il test finale si limita a verificare l'aderenza al regolamento ufficiale.

Fasi Waterfall applicate:

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

L'approccio consente di contenere lo scope creep (le regole sono un perimetro chiuso) e di ridurre i bug logici critici grazie all'analisi upfront. Il rischio che accettiamo è quello tipico del Waterfall — modifiche tardive costose — che qui resta però improbabile proprio per la stabilità dei requisiti.

---

### 2. Backend Server: Agile Iterativo (Scrum-like)

Metodologia scelta: Agile Iterativo.

Il backend espone le API consumate dal frontend, e proprio per questo ha bisogno di un ciclo di feedback rapido: il team frontend, provando le API, segnala esigenze che portano ad adattarle in corsa. Un endpoint come `/api/matches/create`, per esempio, può richiedere campi diversi da quelli previsti all'inizio. Anche la struttura dati non è congelata a priori: lo schema del database viene ottimizzato iterativamente, e alcuni problemi di performance sulle query emergono solo testando con dati realistici.

L'iterazione permette inoltre di rilasciare valore in modo incrementale — autenticazione, gestione partite, integrazione WebSocket in sprint successivi — così che il frontend abbia sempre API utilizzabili. Infine, integrare di continuo evita il classico "big bang integration" a fine progetto, con tutti i rischi di integration hell che comporta.

Sprint planning (2 settimane per sprint):

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

Cerimonie Agile:

- Daily stand-up: 9:30 ogni mattina (15 min)
- Sprint review: demo bi-settimanale al committente (venerdì, 1h)
- Sprint retrospective: venerdì dopo la demo (30 min)
- Sprint planning: lunedì a inizio sprint (1h)

Metriche monitorate: velocity (story point completati per sprint), burn-down chart, code coverage (obiettivo 80%+).

---

### 3. Real-Time Communication: Agile Adattivo (Kanban + Spike)

Metodologia scelta: Agile Adattivo (approccio sperimentale).

Questo è il sottosistema più incerto, e per noi il rischio tecnico più critico dell'intero progetto: nessuno nel team ha esperienza di WebSocket in produzione, i problemi che possono emergere sono tali da imporre anche un cambio di libreria (per esempio abbandonare Socket.IO), e una stima affidabile a monte semplicemente non è possibile. Per questo abbiamo scelto di procedere in modo adattivo, riducendo l'incertezza per gradi anziché pianificare su ipotesi fragili.

Il primo passo è uno spike, cioè un lavoro di ricerca e prototipazione time-boxed pensato per abbassare l'incertezza. Nelle settimane 1-2 lo spike "WebSocket Proof-of-Concept" ha un obiettivo preciso — quattro client che sincronizzano uno stato semplificato — con criteri di successo misurabili (latenza sotto i 500 ms, sincronizzazione corretta) e un punto di decisione go/no-go fissato al giorno 15. I decision point sono espliciti proprio perché il rischio è alto: se lo spike fallisce al giorno 15 si attiva il piano di contingenza (il consulente esterno Dr. Stefano Nardi); se al giorno 30 nemmeno con il consulente si ottengono risultati, si passa a un'escalation verso il committente, perché a quel punto è in gioco la fattibilità del progetto.

Il lavoro non segue sprint rigidi ma un flusso continuo su board Kanban, con priorità dinamica: se emerge un bug critico, l'intero team ci si concentra. Elena e Sara lavorano in pair programming intensivo, sia per la difficoltà del problema sia per condividere conoscenza su una tecnologia nuova per tutti.

Board Kanban:

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

WIP limit: massimo 2 task in progress (focus a scapito del parallelismo).

Fasi adattive:

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

I rischi principali sono presidiati su tre fronti: un piano di contingenza chiaro (il consulente esterno), il rilevamento precoce dei problemi (grazie allo spike a monte) e un percorso di escalation definito nel caso peggiore.

---

### 4. Frontend Web: Agile Iterativo (Scrum-like)

Metodologia scelta: Agile Iterativo.

Sul frontend il feedback continuo sull'esperienza d'uso è determinante: l'interfaccia deve ricreare il "calore" della tradizione, e per capirlo non bastano mockup statici — i beta tester devono provare prototipi interattivi, così da poter iterare rapidamente sul design. Da qui il co-design con la community: demo bi-settimanali con Maraffa Forever, sessioni di Think Aloud Protocol e A/B testing sulle scelte critiche (per esempio drag&drop contro click per giocare una carta). Il frontend, inoltre, consuma API ancora in evoluzione, quindi le sue iterazioni vanno tenute allineate con gli sprint del backend.

Sprint sincronizzati con il backend:

```
SPRINT 1 (Settimane 3-4): Login & Registrazione
- Implementazione form con validazione real-time
- Integrazione API /auth/*
- Demo: flusso completo registrazione → login

SPRINT 2 (Settimane 5-6): Dashboard & Creazione Stanze
- Implementazione dashboard con lista stanze
- Form creazione stanza (pubblica/privata)
- Demo: creazione e join stanza

SPRINT 3 (Settimane 7-8): Tavolo da Gioco (CRITICO)
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

Tecniche UX adottate: mockup interattivi (prototipi Figma) prima di scrivere codice, user testing ogni 2 settimane con 5 utenti rappresentativi, e misurazione della System Usability Scale (SUS) al termine di ogni sprint con obiettivo 75+.

---

### 5. Mobile Application: Incrementale (Won't Have per l'MVP)

Metodologia scelta: Incrementale, ma rinviata a dopo l'MVP.

L'app mobile nativa resta fuori dall'MVP per una ragione di risorse: sviluppare in parallelo iOS e Android richiederebbe 3-4 mesi aggiuntivi, che il budget di €25.000 non copre. Nel frattempo la copertura mobile è garantita dal frontend web responsive, utilizzabile dal browser dei dispositivi e con performance accettabili su iPhone e Android moderni: questo permette di ridurre lo scope dell'MVP senza rinunciare all'usabilità da mobile.

Pianificazione futura (v1.1, post-lancio):

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

L'ordine è pensato in ottica incrementale: ogni fase rilascia un'app funzionante e autonoma, iOS e Android non hanno dipendenze reciproche, e si parte da iOS perché la community di Maraffa Forever usa prevalentemente iPhone.

---

### 6. Social & Community Features: Incrementale

Metodologia scelta: Incrementale.

Le funzionalità social si prestano bene a un rilascio a incrementi perché sono in larga parte indipendenti tra loro: il sistema di amicizie funziona senza la chat globale, la chat in partita non ha bisogno delle classifiche, le statistiche prescindono dai profili pubblici. Questa indipendenza si sposa con una prioritizzazione MoSCoW netta — chat in-game e login/profilo base come Must Have, amicizie come Should Have, classifiche e chat globale come Could Have, tornei e achievement esclusi dall'MVP. Il vantaggio pratico è la riduzione del rischio: anche se il tempo dovesse stringere, i Must Have restano completati e non si rilascia nessuna feature "a metà".

Sequenza incrementale:

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

L'approccio riduce il rischio di arrivare alla scadenza con funzioni incomplete, rende possibile un rilascio anticipato (soft launch) se serve, e fa sì che il feedback sugli incrementi già rilasciati orienti lo sviluppo dei successivi.

---

### 7. Infrastructure & DevOps: Incrementale

Metodologia scelta: Incrementale.

Sull'infrastruttura l'approccio incrementale serve soprattutto a evitare l'over-engineering: si parte da una configurazione minimale (single server) e si aggiunge complessità solo quando diventa realmente necessaria, senza sostenere costi inutili all'inizio. Le capabilities crescono per layer: hosting e database sono indispensabili da subito (Layer 1), la CI/CD riduce gli errori di deployment (Layer 2), il monitoring dà visibilità sui problemi in produzione (Layer 3), l'auto-scaling arriva solo se il traffico lo richiede (Layer 4).

Sequenza incrementale:

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

In questo modo i costi iniziali restano contenuti (niente over-provisioning), ogni incremento viene validato prima di introdurre l'ulteriore complessità, e la scalabilità resta predisposta ma non implementata in anticipo, coerentemente col principio YAGNI ("You Aren't Gonna Need It").

---

## Matrice decisionale: quale metodologia per quale sottosistema?

| Caratteristica del sottosistema | Waterfall | Agile Iterativo | Agile Adattivo | Incrementale |
|----------------------------|-----------|-----------------|----------------|--------------|
| Requisiti completamente noti | Sì | No | No | Parziale |
| Feedback continuo necessario | No | Sì | Sì | No |
| Alta incertezza tecnica | No | No | Sì | No |
| Features indipendenti prioritizzabili | No | Parziale | No | Sì |
| Integrazione continua con altri sistemi | No | Sì | Parziale | No |

---

## Coordinamento tra metodologie diverse

La difficoltà principale di un approccio ibrido è tenere sincronizzati sottosistemi che internamente seguono ritmi diversi. La soluzione adottata è una cadenza comune sovrapposta ai singoli metodi: anche i sottosistemi Waterfall e Incrementale, che internamente non lavorano per sprint, si allineano a una scansione bi-settimanale, con demo al committente ogni venerdì e milestone di integrazione a cadenza mensile.

A titolo di esempio, la prima milestone (fine ottobre) prevede: Game Engine (Waterfall) con la fase di implementazione conclusa, Backend (Agile Iterativo) allo Sprint 2 completato, Real-Time (Agile Adattivo) con lo spike PoC validato, Frontend (Agile Iterativo) allo Sprint 2 completato, Infrastructure (Incrementale) all'incremento 3 (CI/CD) completato. Le settimane 4, 8 e 12 sono dedicate a integration sprint, in cui non si introducono nuove feature ma ci si concentra su integrazione e bug fixing.

---

## Conclusioni

L'approccio ibrido si è rivelato la scelta più coerente con la natura di MaraffaOnline, per alcune ragioni di fondo. Innanzitutto per pragmatismo: i sottosistemi hanno caratteristiche molto diverse, e imporre un unico metodo sarebbe stato inefficiente. In secondo luogo per la gestione del rischio, che risulta calibrata sul singolo componente — il Waterfall contiene il rischio sul Game Engine (requisiti stabili), mentre l'Agile Adattivo governa quello sul Real-Time (incertezza massima). C'è poi un guadagno di efficienza, perché si evita l'overhead superfluo (uno sprint planning sul Game Engine non avrebbe senso) e si concentra il feedback continuo dove serve davvero, cioè su frontend e backend. Infine il modello è riutilizzabile: PlayHeritage Labs potrà applicarlo ad altri progetti futuri, per esempio la digitalizzazione di altri giochi tradizionali.

Tra le indicazioni che porteremo con noi: i decision point espliciti sono cruciali per i sottosistemi ad alto rischio; la sincronizzazione tramite milestone comuni funziona meglio di sprint rigidi imposti ovunque; e la documentazione a monte, tipica del Waterfall, riduce in modo sensibile i bug logici dove i requisiti lo permettono.

---

Redatto da: Marco Venturi (Project Manager, PlayHeritage Labs)
Revisionato da: Elena Rossi (Lead Developer) e team completo
Approvato da: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
Data approvazione: 01/10/2025
