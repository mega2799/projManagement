# Sottosistemi e Metodologie - MaraffaOnline

## Data: 2026-01-04
## Versione: 1.0

---

## Sottosistemi Identificati

### 1. Game Engine (Motore di Gioco)
**Descrizione**: Implementazione delle regole della Maraffa, logica di gestione partite, validazione mosse, calcolo punteggi.

**Metodologia**: **Waterfall**

**Motivazione**: Le regole della Maraffa tradizionale romagnola sono fisse e ben documentate. Non c'è necessità di adattamento o sperimentazione: il gioco esiste da decenni con regole consolidate. Un approccio sequenziale permette di:
- Analizzare accuratamente le regole esistenti
- Progettare l'architettura del motore
- Implementare in modo sistematico
- Validare attraverso test case completi

**Rischi**: Necessità di feedback da giocatori esperti per validare la correttezza dell'implementazione.

---

### 2. Backend Server (API e Business Logic)
**Descrizione**: REST API per operazioni CRUD, gestione sessioni e autenticazione, database management, business logic generale.

**Metodologia**: **Agile Iterativo**

**Motivazione**: Lo sviluppo delle API beneficia di iterazioni brevi con testing continuo. Ogni endpoint viene sviluppato, testato e integrato con il frontend in cicli rapidi. Questo approccio permette di:
- Identificare rapidamente problemi di integrazione
- Raffinare le API in base al feedback del team frontend
- Adattare la struttura dati alle esigenze emergenti
- Mantenere sincronizzazione tra backend e frontend

**Dipendenze**: Integrazione continua con Frontend Web e Game Engine.

---

### 3. Real-Time Communication (Comunicazione Multiplayer)
**Descrizione**: WebSocket server per partite in tempo reale, sincronizzazione stato del gioco tra 4 giocatori, gestione latency e disconnessioni.

**Metodologia**: **Agile Adattivo**

**Motivazione**: Questo sottosistema presenta la massima incertezza tecnica del progetto:
- Gestione della latency variabile tra giocatori
- Sincronizzazione dello stato in tempo reale
- Gestione di disconnessioni improvvise e riconnessioni
- Ottimizzazione delle performance di rete

Richiede sperimentazione continua, prototipazione rapida e possibili cambi di direzione tecnica (es. switch tra diverse librerie WebSocket o protocolli). Il team deve essere pronto ad adattare l'approccio in base ai risultati dei test di stress e performance.

**Rischi Alto**: Questo è il sottosistema tecnicamente più sfidante del progetto.

---

### 4. Frontend Web (Interfaccia Web)
**Descrizione**: Single Page Application, UI del tavolo da gioco, dashboard utente, responsive design.

**Metodologia**: **Agile Iterativo**

**Motivazione**: L'interfaccia utente richiede feedback continuo dalla community "Maraffa Forever". Il processo prevede:
- Mockup iniziali → Feedback committente
- Prototipo interattivo → User testing
- Iterazioni successive con miglioramenti UX
- Validazione continua con utenti target (25-45 anni)

L'obiettivo è ricreare l'esperienza del tavolo da gioco fisico in digitale, mantenendo l'intuitività e il calore sociale del gioco tradizionale. Questo richiede raffinamenti continui basati sul feedback degli utenti.

**Dipendenze**: Integrazione stretta con Backend Server e Real-Time Communication.

---

### 5. Mobile Application (App Mobile)
**Descrizione**: App nativa iOS/Android con UX ottimizzata per mobile.

**Metodologia**: **Incrementale**

**Motivazione**: Lo sviluppo mobile parte dopo la validazione del web. Le API backend sono già pronte e testate. L'approccio incrementale permette di:
- Sviluppare prima la versione iOS (più semplice da testare internamente)
- Poi sviluppare la versione Android
- Riutilizzare tutta la business logic già validata
- Aggiungere progressivamente features mobile-specific (notifiche push, offline mode)

**Priorità**: MoSCoW classificherà questo come "Should have" o "Could have", non è Must have per il lancio.

---

### 6. Social & Community Features (Funzionalità Sociali)
**Descrizione**: Sistema amicizie, chat (globale e in-game), statistiche e classifiche, profili utente.

**Metodologia**: **Incrementale**

**Motivazione**: Le funzionalità sociali sono indipendenti tra loro e possono essere sviluppate in sequenza prioritaria:
1. **Must Have**: Sistema di login e profilo base
2. **Must Have**: Creazione stanze private per giocare con amici
3. **Should Have**: Sistema di amicizie
4. **Should Have**: Chat in-game
5. **Could Have**: Statistiche personali e classifiche
6. **Could Have**: Chat globale/lobby

Ogni feature viene completata prima di passare alla successiva, riducendo il rischio di incompletezza.

**Analisi**: MoSCoW prioritization sarà fondamentale per questo sottosistema.

---

### 7. Infrastructure & DevOps (Infrastruttura)
**Descrizione**: Deployment pipeline, monitoring e logging, scalability e load balancing, backup e disaster recovery.

**Metodologia**: **Incrementale**

**Motivazione**: L'infrastruttura viene costruita progressivamente:
1. **Fase 1**: Setup base (hosting, database, CI/CD pipeline)
2. **Fase 2**: Monitoring e logging
3. **Fase 3**: Auto-scaling e load balancing
4. **Fase 4**: Backup automatici e disaster recovery

Ogni incremento aggiunge capacità senza stravolgere l'esistente. L'approccio incrementale riduce la complessità iniziale e permette di partire rapidamente con l'MVP.

---

## Matrice Riassuntiva

| Sottosistema | Metodologia | Motivazione Chiave | Livello Rischio |
|--------------|-------------|-------------------|-----------------|
| Game Engine | Waterfall | Requisiti fissi e ben definiti | Basso |
| Backend Server | Agile Iterativo | Integrazione continua con frontend | Medio |
| Real-Time Communication | Agile Adattivo | Alta incertezza tecnica | Alto |
| Frontend Web | Agile Iterativo | Feedback continuo UX necessario | Medio |
| Mobile Application | Incrementale | Parte dopo validazione web | Basso |
| Social & Community | Incrementale | Features indipendenti, prioritizzabili | Basso |
| Infrastructure & DevOps | Incrementale | Setup progressivo delle capabilities | Medio |

---

## Note per la Relazione

Questa scelta metodologica ibrida (mix di approcci) dovrà essere argomentata nella sezione **2.11 Project Management Life Cycle Models** della relazione.

**Punti chiave da enfatizzare**:
1. Approccio pragmatico: ogni sottosistema ha la metodologia più adatta
2. Gestione del rischio: Agile Adattivo per le parti più incerte
3. Efficienza: Waterfall per requisiti chiari e stabili
4. Prioritizzazione: Incrementale per features opzionali
5. Feedback: Iterativo dove serve coinvolgimento utenti

---

**Documento creato da**: Claude (con Matteo)
**Prossimo step**: Passare alla Fase 2 - Scoping
