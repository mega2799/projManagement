# Allegato 2.11 - Project Management Life Cycle Models
## v.1.1.0 – 2025-09-30

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

## Modelli PM utilizzati

Nel progetto sono stati impiegati quattro modelli, ciascuno con la propria condizione d'uso tipica:

| Modello | Quando si usa |
|---------|---------------|
| Linear/Waterfall | Requisiti chiari e stabili fin dall'inizio; fasi sequenziali con documentazione upfront e validazione finale |
| Agile Iterativo (Scrum-like) | Requisiti noti ma con necessità di feedback continuo; sprint di 2 settimane con demo al committente |
| Agile Adattivo (Kanban + Spike) | Alta incertezza tecnica; flusso continuo, prototipazione rapida (spike) e decision point go/no-go |
| Incrementale | Componenti indipendenti rilasciabili in sequenza; prioritizzazione MoSCoW e release graduale |

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

## Motivazione per sottosistema

Di seguito la giustificazione della scelta per ciascun sottosistema. Il dettaglio di pianificazione (fasi, sprint, incrementi) non è ripreso qui: è riportato nella WBS (Allegato 3.1), nel Product Backlog (Allegato 3.3) e nel Gantt (Allegato 3.5).

### 1. Game Engine — Waterfall

I requisiti sono fissi e non ambigui: le regole della Maraffa romagnola sono documentate e stabili, e la fedeltà al gioco tradizionale è vincolante (una regola sbagliata comprometterebbe l'intera esperienza). Questo consente di pianificare in anticipo — Francesca Giuliani approva la specifica delle regole prima dello sviluppo e i test case si scrivono a monte partendo da partite con risultato noto — mentre il feedback continuo conta poco, dato che gli utenti le regole le conoscono già. L'analisi upfront riduce rework e bug logici; il rischio tipico del Waterfall, le modifiche tardive costose, resta improbabile proprio per la stabilità dei requisiti.

### 2. Backend Server — Agile Iterativo

Il backend espone le API consumate dal frontend e ha bisogno di un ciclo di feedback rapido: provando le API, il team frontend segnala esigenze che portano ad adattarle in corsa, e anche lo schema del database viene ottimizzato iterativamente su dati realistici. L'iterazione permette di rilasciare valore in modo incrementale (autenticazione, gestione partite, integrazione WebSocket in sprint successivi) e di integrare di continuo, evitando il "big bang integration" di fine progetto con i relativi rischi.

### 3. Real-Time Communication — Agile Adattivo

È il sottosistema più incerto e il rischio tecnico più critico del progetto: nessuno nel team ha esperienza di WebSocket in produzione e una stima affidabile a monte non è possibile. Si procede quindi in modo adattivo, riducendo l'incertezza per gradi: si parte da uno spike time-boxed (quattro client che sincronizzano uno stato semplificato, con latenza target sotto i 500 ms) e da un decision point go/no-go al giorno 15; se lo spike fallisce si attiva la contingenza (consulente esterno Dr. Stefano Nardi) e, se al giorno 30 nemmeno con il consulente si ottengono risultati, si escala al committente. Il lavoro segue un flusso Kanban con priorità dinamica e pair programming Elena-Sara, anziché sprint rigidi.

### 4. Frontend Web — Agile Iterativo

Sul frontend il feedback continuo sull'esperienza d'uso è determinante: per ricreare il "calore" della tradizione non bastano mockup statici, servono prototipi interattivi provati dai beta tester. Da qui il co-design con la community: demo bi-settimanali con Maraffa Forever, sessioni di Think Aloud Protocol e A/B testing sulle scelte critiche (per esempio drag&drop contro click per giocare una carta). Le iterazioni del frontend, che consuma API ancora in evoluzione, sono tenute sincronizzate con gli sprint del backend.

### 5. Mobile Application — Incrementale (Won't Have per l'MVP)

L'app mobile nativa resta fuori dall'MVP per ragioni di budget: sviluppare iOS e Android in parallelo richiederebbe 3-4 mesi aggiuntivi non coperti dai €25.000. Nel frattempo la copertura mobile è garantita dal frontend web responsive, utilizzabile dal browser dei dispositivi con performance accettabili. È pianificata in modo incrementale dopo il lancio (prima iOS, poi Android, infine le feature mobile-specific), dato che le due piattaforme non hanno dipendenze reciproche.

### 6. Social & Community — Incrementale

Le funzionalità social sono in larga parte indipendenti tra loro (il sistema di amicizie funziona senza la chat globale, le statistiche prescindono dai profili pubblici), il che si sposa con una prioritizzazione MoSCoW netta e un rilascio a incrementi. Il vantaggio pratico è la riduzione del rischio: anche se il tempo dovesse stringere, i Must Have restano completati e non si rilascia nessuna feature "a metà".

### 7. Infrastructure & DevOps — Incrementale

Sull'infrastruttura l'approccio incrementale serve a evitare l'over-engineering: si parte da una configurazione minimale (single server) e si aggiunge complessità solo quando diventa realmente necessaria. Le capabilities crescono per layer — hosting e database indispensabili da subito, poi la CI/CD, poi il monitoring in produzione e infine l'auto-scaling solo se il traffico lo richiede — coerentemente col principio YAGNI ("You Aren't Gonna Need It").

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

La difficoltà principale di un approccio ibrido è tenere sincronizzati sottosistemi che internamente seguono ritmi diversi. La soluzione adottata è una cadenza comune sovrapposta ai singoli metodi: anche i sottosistemi Waterfall e Incrementale, che internamente non lavorano per sprint, si allineano a una scansione bi-settimanale, con demo al committente ogni venerdì e milestone di integrazione a cadenza mensile. Le settimane di integrazione (4, 8 e 12) non introducono nuove feature ma sono dedicate a integrazione e bug fixing.

---

## Conclusioni

L'approccio ibrido è la scelta più coerente con la natura di MaraffaOnline, per alcune ragioni di fondo. Innanzitutto per pragmatismo: i sottosistemi hanno caratteristiche molto diverse, e imporre un unico metodo sarebbe stato inefficiente. In secondo luogo per la gestione del rischio, che risulta calibrata sul singolo componente — il Waterfall contiene il rischio sul Game Engine (requisiti stabili), mentre l'Agile Adattivo governa quello sul Real-Time (incertezza massima). C'è poi un guadagno di efficienza, perché si evita l'overhead superfluo (uno sprint planning sul Game Engine non avrebbe senso) e si concentra il feedback continuo dove serve davvero, cioè su frontend e backend. Infine il modello è riutilizzabile: PlayHeritage Labs potrà applicarlo ad altri progetti futuri, per esempio la digitalizzazione di altri giochi tradizionali.

Alcune indicazioni metodologiche guideranno l'esecuzione: i decision point espliciti sono importanti per i sottosistemi ad alto rischio; la sincronizzazione tramite milestone comuni è preferibile a sprint rigidi imposti ovunque; e la documentazione a monte, tipica del Waterfall, riduce i bug logici dove i requisiti lo permettono.

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Lead Developer)

**Storico revisioni**:
- **v.1.1.0**: Snellimento. Rimossi i blocchi di pianificazione di dettaglio per sottosistema (fasi Waterfall, sprint plan, board Kanban, sequenze di incrementi) che duplicavano WBS, Product Backlog e Gantt; mantenuti le tabelle di sintesi, la matrice decisionale e la motivazione (ora concisa) di ciascuna scelta metodologica.
- **v.1.0.0**: Prima stesura con l'analisi dettagliata per sottosistema.
