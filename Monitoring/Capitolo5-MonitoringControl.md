# Capitolo 5 - Monitoring and Control

Per evitare problemi con il progetto MaraffaOnline, come ritardi o costi aggiuntivi, è necessario monitorarlo e controllarlo in maniera continua. La fase di monitoraggio e controllo non è una fase distinta che segue il lancio, ma piuttosto un'attività continua che accompagna l'intero ciclo di vita del progetto dalla fase di Launching fino alla Closing.

## 5.1 Monitoraggio Continuo

Come è già stato citato nel capitolo precedente durante la descrizione delle regole operative, nei sottosistemi che hanno adottato metodologie Agile (Backend Server, Real-Time Communication, Frontend Web) viene effettuato ogni mattina un Daily Standup di 15 minuti dalle 09:00 alle 09:15. Durante questo meeting ogni membro del team risponde a tre domande fondamentali: cosa ho fatto ieri, cosa farò oggi, e ho blocker che mi impediscono di procedere. Questo rituale quotidiano permette di individuare problemi emergenti prima che si accumulino e diventino critici.

Inoltre, a ogni sviluppatore è stato chiesto di utilizzare il software di gestione del progetto Notion Database per tenere traccia dei task assegnati, delle scadenze e dello stato di avanzamento. Ogni task nel database ha uno status (Todo, In Progress, Done) che viene aggiornato quotidianamente, permettendo a Marco Venturi, il Project Manager, di avere una visione in tempo reale dello stato del progetto senza dover necessariamente convocare meeting aggiuntivi.

Per favorire il monitoraggio e, quindi, la buona riuscita del progetto, PlayHeritage Labs ha deciso di attuare una linea guida nei confronti dei suoi collaboratori: gli sviluppatori sono incoraggiati a riportare i problemi il prima possibile, evitando che si accumulino in quello che in gergo viene chiamato "creep". Inoltre, sono stati istruiti sull'importanza di essere sinceri sulla situazione attuale, di quanto sia importante farla presente subito per evitare che peggiori ulteriormente e sull'importanza di porre domande quando qualcosa non è chiaro. PlayHeritage Labs promuove così un clima di apertura in cui i problemi vengono segnalati con tempestività, senza timore di penalizzazioni.

## 5.2 Project Status Meetings

Per ottenere informazioni sull'avanzamento complessivo del progetto rispetto alle milestone e al budget, sono stati effettuati dei Project Status Meetings di un'ora, ogni venerdì dalle 16:00 alle 17:00. A questi meeting partecipano obbligatoriamente Marco Venturi come presenter, Giovanni Marchetti come sponsor, ed Elena Rossi per la parte tecnica. Durante questi incontri viene presentato uno Stoplight Report che fornisce una visione sintetica ma efficace dello stato del progetto.

Il sistema stoplight, seppur contenga informazioni molto sintetiche, permette di capire immediatamente lo stato del progetto in quanto lo identifica con tre colori: verde, giallo e rosso. Il verde indica che il progetto sta procedendo come previsto senza scostamenti significativi. Il giallo indica che anche se ci sono degli scostamenti, la situazione è comunque sotto controllo e non richiede interventi urgenti. Il rosso segnala che ci sono problemi critici e quindi è necessario intervenire immediatamente con azioni correttive. Ogni area del progetto (Scope, Schedule, Budget, Quality, Risks) riceve un colore e una nota esplicativa che giustifica la valutazione.

Durante questi meeting settimanali viene anche aggiornato l'Issue Log, un documento mantenuto su Notion che contiene una lista di tutti i problemi che sono stati riscontrati durante il progetto, il loro stato di risoluzione, chi è responsabile della risoluzione, e la data prevista di chiusura. Questo log è fondamentale per garantire che nessun problema venga dimenticato o trascurato.

## 5.3 Sprint Review e Retrospective

Per i sottosistemi Agile, oltre al monitoraggio quotidiano tramite Daily Standup e quello settimanale tramite Project Status Meeting, è previsto un ulteriore livello di controllo rappresentato dalle Sprint Review e Sprint Retrospective che si tengono l'ultimo venerdì di ogni sprint dalle 14:00 alle 16:00.

Durante la Sprint Review, che dura un'ora dalle 14:00 alle 15:00, il team dimostra a Giovanni Marchetti le feature completate durante lo sprint. Questa è l'occasione in cui lo stakeholder può verificare che il lavoro svolto corrisponda effettivamente alle sue aspettative e fornire feedback immediato. Se emergono discrepanze tra quanto sviluppato e quanto atteso, queste vengono discusse e il Product Backlog viene aggiornato di conseguenza. Giovanni ha il potere di accettare o rifiutare i deliverable presentati, e solo le feature accettate vengono considerate "Done" ai fini del calcolo dell'Earned Value.

Immediatamente dopo, dalle 15:00 alle 16:00, si tiene la Sprint Retrospective, un safe space riservato esclusivamente al team interno senza la presenza di Giovanni. Durante questa sessione il team riflette su cosa ha funzionato bene nello sprint appena concluso, cosa può essere migliorato, e quali azioni concrete intraprendere per il prossimo sprint. Utilizzando il formato "Start/Stop/Continue", il team identifica due action items prioritari per il miglioramento continuo del processo. Questa pratica ha permesso al team di MaraffaOnline di ottimizzare progressivamente il proprio modo di lavorare, risolvendo inefficienze e riducendo gli attriti.

## 5.4 Problem Solving Strategy

Per quanto riguarda la strategia di risoluzione dei problemi, PlayHeritage Labs ha adottato un approccio graduale che parte dalla valutazione della necessità di un intervento. Quando emerge un problema durante un Daily Standup o un Project Status Meeting, il primo step è determinare se gli slack presenti nel Project Network Diagram permettono di assorbirlo senza impattare la data di lancio finale. Nel progetto MaraffaOnline, il critical path ha una durata di 141 giorni lavorativi — esattamente i giorni lavorativi disponibili nei sette mesi fino all'8 Maggio, festività escluse — e qualsiasi ritardo su attività che si trovano su questo percorso critico (identificate con slack pari a zero) impatta direttamente la milestone finale.

Se il problema può essere assorbito grazie allo slack disponibile su attività non critiche, si procede semplicemente monitorando la situazione senza interventi invasivi. Se invece il problema impatta il critical path, si procede a livello project manager-based esaminando le dipendenze tra i task per capire se è possibile riorganizzare il lavoro, ad esempio parallelizzando attività che erano state pianificate in sequenza, o utilizzando la tecnica del "crashing" che prevede l'aggiunta di risorse per accelerare task critici.

Se il problema persiste e non è risolvibile con le strategie project manager-based, si procede con l'applicazione delle strategie client-based. In questo caso Marco convoca Giovanni per un meeting straordinario e presenta un Project Impact Statement che analizza l'impatto del problema su scope, time, budget, quality e resources. Vengono presentate diverse opzioni, come la negoziazione di un approccio basato su rilasci multipli dove alcune feature vengono spostate dalla versione 1.0 alla versione 1.1 post-lancio, oppure l'estensione della timeline con rinegoziazione del contratto. Come indicato nelle regole operative, l'assenza o scarsità di risorse non è un problema che tange questo progetto, in quanto MaraffaOnline ha la precedenza sull'allocazione delle risorse rispetto ad altri progetti di PlayHeritage Labs.

## 5.5 Reporting: Stoplight Reports

Affinché le informazioni sul progetto siano accurate, tempestive e complete, PlayHeritage Labs ha deciso di mantenere diversi tipi di report. Il principale strumento di reporting utilizzato durante i Project Status Meeting settimanali è lo Stoplight Report. Questo documento, pubblicato su Notion ogni venerdì sera dopo il meeting, fornisce una panoramica immediata dello stato di salute del progetto.

Ogni Stoplight Report contiene una tabella con cinque aree critiche: Scope, Schedule, Budget, Quality e Risks. Per ciascuna area viene assegnato un colore (verde, giallo, rosso) e una nota che spiega la motivazione del colore assegnato. Ad esempio, a fine Gennaio 2026 lo Stoplight Report mostrava:

- **Scope: Verde** - Tutte le feature Must Have sono in sviluppo secondo il piano. Nessuna change request aperta da Giovanni.
- **Schedule: Giallo** - Il Frontend Dashboard e Creazione Stanza (attività M, sul critical path) ha accumulato 3 giorni di ritardo a causa della complessità inaspettata del flusso di creazione stanza e inviti. Recovery plan attivo: Luca Moretti è affiancato da Sara Bianchi in pair programming. Previsto recupero entro fine Sprint 9.
- **Budget: Verde** - Costi cumulati €13.500 contro €14.100 pianificati; CV di -€300 (2,3% dell'Earned Value), ampiamente entro il Contingency Buffer. Saldo di cassa positivo a €4.650.
- **Quality: Verde** - Test coverage all'87%, superiore al target dell'85%. Zero bug critici aperti. Tutti i test di integrazione superati.
- **Risks: Verde** - Rischio latenza WebSocket declassato (rating 16 → 8) dopo il proof of concept e chiuso come "Mitigato" dopo il load test dello Sprint 6.

Questa sintesi permette a Giovanni di comprendere immediatamente se il progetto richiede la sua attenzione su aspetti specifici o se può procedere con fiducia. I colori gialli segnalano le aree da monitorare prima che diventino rosse e richiedano interventi drastici.

## 5.6 Earned Value Management

Oltre agli Stoplight Reports, un altro strumento fondamentale per il monitoraggio del progetto è l'Earned Value Management (EVM). Questa tecnica permette di integrare misure di scope, schedule e costi per valutare le performance del progetto e prevedere gli outcome futuri. L'EVM utilizza tre metriche principali: il Planned Value (PV), che rappresenta il valore del lavoro che dovrebbe essere stato completato secondo il piano; l'Earned Value (EV), che rappresenta il valore del lavoro effettivamente completato; e l'Actual Cost (AC), che rappresenta i costi reali sostenuti per il lavoro completato.

Per il progetto MaraffaOnline, Marco Venturi ha creato un foglio di calcolo Excel condiviso con Giovanni (in modalità read-only per lo sponsor) dove vengono tracciati mensilmente i valori di PV, EV e AC. Questi dati vengono poi visualizzati in un grafico che mostra l'andamento delle tre curve nel tempo. Il grafico permette di identificare rapidamente se il progetto è on schedule (EV allineato con PV), under budget (AC inferiore a EV), o se ci sono problemi di performance (EV inferiore a PV indica che si sta producendo meno valore di quanto pianificato).

Di seguito viene riportato un frammento del grafico Earned Value relativo al periodo Ottobre 2025 - Gennaio 2026, corrispondente ai primi quattro mesi del progetto MaraffaOnline:

```
Earned Value Management - MaraffaOnline (Ott 2025 - Gen 2026)

  €25.000 ┤
          │                                          ╱──── PV (Planned Value)
  €20.000 ┤                                      ╱───
          │                                  ╱───     ╱─── AC (Actual Cost)
  €15.000 ┤                              ╱───      ╱──
          │                          ╱───       ╱──    ── EV (Earned Value)
  €10.000 ┤                      ╱───        ╱──
          │                  ╱───         ╱──
   €5.000 ┤              ╱───          ╱──
          │          ╱───           ╱──
       €0 ┼──────╱───────────────╱────────────────────
          Ott    Nov         Dic         Gen
               Tempo (Mesi)

Legenda:
- PV (arancione tratteggiata): Budget pianificato cumulativo
- EV (rosso): Valore del lavoro completato
- AC (blu): Costi effettivi sostenuti
```

Nel grafico si può notare come durante i primi quattro mesi del progetto ci sia stata una buona aderenza tra le tre curve. A fine Gennaio 2026, il progetto mostrava i seguenti valori:

- **Planned Value (PV)**: €14.100 - Questo è il budget che era pianificato per i primi 4 mesi secondo il Cash Flow Management (€3.000 per il Mese 0 + €3.700 × 3 mesi per Novembre, Dicembre e Gennaio).
- **Earned Value (EV)**: €13.200 - Valore del lavoro effettivamente completato, leggermente inferiore al pianificato.
- **Actual Cost (AC)**: €13.500 - Costi reali sostenuti, leggermente superiori al valore guadagnato.

Da questi valori possiamo calcolare due indici fondamentali:

**Cost Variance (CV) = EV - AC = €13.200 - €13.500 = -€300**

La Cost Variance negativa indica che il progetto ha speso €300 in più rispetto al valore prodotto. Questo scostamento, pari al 2,3% del valore guadagnato, è considerato accettabile e rientra ampiamente nel Contingency Buffer del 18,7% previsto nel Cash Flow Management. La causa principale di questo lieve overrun è stata la necessità di dedicare ore extra al sistema Real-Time Communication per ottimizzare la latenza WebSocket, come identificato nel rischio R1 della Risk Rating Matrix.

**Schedule Variance (SV) = EV - PV = €13.200 - €14.100 = -€900**

La Schedule Variance negativa indica che il progetto è leggermente in ritardo rispetto al piano, con un valore di €900 di lavoro non ancora completato rispetto a quanto pianificato. Questo corrisponde al ritardo di 3 giorni accumulato dal Frontend Dashboard e Creazione Stanza menzionato nello Stoplight Report. Tuttavia, grazie al recovery plan attivato (pair programming Luca + Sara), il ritardo è stato recuperato entro la fine di Febbraio 2026.

Si può notare come nel complesso il progetto abbia mantenuto le tre linee relativamente vicine, segno di una buona capacità di pianificazione e esecuzione. In altri momenti dell'anno, in particolare durante i mesi di Ottobre e Novembre 2025 quando il team lavorava principalmente su sistemi Waterfall e setup infrastrutturale con requisiti ben definiti, si è riusciti per lunghi periodi a mantenere le tre linee molto vicine.

### Riepilogo EVM mensile (Ott 2025 - Mag 2026)

Per completezza, ecco la tabella riassuntiva dei valori EVM mese per mese fino alla chiusura del progetto:

| Mese | Periodo | PV cumulato (€) | EV cumulato (€) | AC cumulato (€) | CV (€) | SV (€) | CPI | SPI |
|------|---------|----------------:|----------------:|----------------:|-------:|-------:|----:|----:|
| 0 | Ott 2025 | 3.000 | 2.950 | 2.900 | +50 | -50 | 1,02 | 0,98 |
| 1 | Nov 2025 | 6.700 | 6.550 | 6.500 | +50 | -150 | 1,01 | 0,98 |
| 2 | Dic 2025 | 10.400 | 10.100 | 10.200 | -100 | -300 | 0,99 | 0,97 |
| 3 | Gen 2026 | 14.100 | 13.200 | 13.500 | -300 | -900 | 0,98 | 0,94 |
| 4 | Feb 2026 | 17.800 | 17.300 | 17.500 | -200 | -500 | 0,99 | 0,97 |
| 5 | Mar 2026 | 19.800 | 19.600 | 19.700 | -100 | -200 | 0,99 | 0,99 |
| 6 | Apr 2026 (UAT) | 21.600 | 21.500 | 21.550 | -50 | -100 | 1,00 | 1,00 |
| 7 | Mag 2026 (Launch) | 22.750 | 22.750 | 22.750 | 0 | 0 | 1,00 | 1,00 |

I valori di PV corrispondono all'outflow cumulato pianificato nel Cash Flow Management (Allegato 3.4). La traiettoria mostra come il leggero overrun di Gennaio (CV=-300, SV=-900) sia stato progressivamente assorbito attraverso il recovery plan, fino a chiudere a fine progetto con CPI=1,00 e SPI=1,00. Il consumo finale di €22.750 lascia il surplus di €2.250 documentato nel Cap 6 - Closing.

## 5.7 Gantt Chart Tracking

Un ulteriore strumento di monitoraggio utilizzato è il Gantt Chart dinamico mantenuto su Notion Database. A differenza del Gantt statico creato durante la fase di Planning, questo Gantt viene aggiornato settimanalmente da Marco Venturi per riflettere lo stato attuale del progetto. Ogni attività nel Gantt ha associata una percentuale di completamento che viene aggiornata sulla base delle informazioni raccolte durante i Daily Standup e i Project Status Meeting.

Il Gantt Chart è particolarmente utile per visualizzare il critical path e identificare rapidamente quali attività sono in ritardo e quale impatto questo ritardo ha sulla data di lancio finale. Durante il mese di Gennaio 2026, ad esempio, il Gantt mostrava chiaramente che l'attività "Frontend Dashboard + Creazione Stanza" (ID: M nel Project Network Diagram) era al 60% invece dell'80% previsto, evidenziando visivamente con una barra rossa che questa attività sul critical path stava accumulando un ritardo (3 giorni su 15 di durata) che, propagandosi al successivo Frontend Tavolo da Gioco (P), avrebbe potuto compromettere il lancio del 15 Maggio 2026.

Questa visualizzazione immediata ha permesso a Marco di attivare tempestivamente il recovery plan, evitando che il problema si aggravasse ulteriormente. Il Gantt viene condiviso con Giovanni durante i Project Status Meeting per fornirgli una visione complessiva dell'avanzamento temporale del progetto.

## 5.8 Velocity Tracking per Sistemi Agile

Per i sottosistemi che utilizzano metodologie Agile, un'ulteriore metrica di monitoraggio è la velocity, ovvero il numero di story points che il team riesce a completare in ogni sprint. La velocity è fondamentale per fare previsioni realistiche su quando determinate feature saranno completate e per identificare se il team sta migliorando la propria produttività nel tempo o se sta incontrando difficoltà.

**Nota metodologica sulla velocity tracciata**: I 40 story points/sprint sono la **capacity team-wide** stimata — quanto il team può completare in uno sprint — e aggregano il lavoro sulle user stories del Product Backlog (Allegato 3.3, 310 SP) e quello sui sottosistemi gestiti con altre metodologie (Game Engine in Waterfall e Infrastructure & DevOps in Incrementale, ~131 SP equivalenti). Il piano carica in media ~37 SP/sprint team-wide (441 SP sugli sprint di sviluppo 0-11) e ~28 SP/sprint di solo Backlog (310 SP sugli Sprint 1-11); il margine tra capacità e carico medio assorbe festività e variabilità. Gli Sprint 12-14 (UAT, lancio) non sono stimati in story points, mentre lo Sprint 11 ospita solo le rifiniture del tavolo in fast tracking con il testing E2E. La metrica monitorata in questo capitolo è quindi una velocity *gestionale* a livello di team, non la velocity Scrum pura, per dare a Giovanni Marchetti una visione unica e consolidata dell'avanzamento del lavoro su tutto il progetto.

Nel Product Backlog di MaraffaOnline era stata stimata una velocity target di 40 story points per sprint (ogni 2 settimane). Durante i primi sette sprint del progetto (Novembre 2025 - Gennaio 2026), la velocity effettiva è stata:

- **Sprint 1** (28 Ott - 08 Nov): 38 story points completati su 40 pianificati (95%)
- **Sprint 2** (11 Nov - 22 Nov): 42 story points completati su 40 pianificati (105%)
- **Sprint 3** (25 Nov - 06 Dic): 40 story points completati su 40 pianificati (100%)
- **Sprint 4** (09 Dic - 20 Dic): 35 story points completati su 40 pianificati (87,5%) - Impatto festività
- **Sprint 5** (23 Dic - 03 Gen): 21 story points completati su 40 pianificati (52,5%) - Sprint interamente a cavallo delle festività natalizie
- **Sprint 6** (06 Gen - 17 Gen): 39 story points completati su 40 pianificati (97,5%)
- **Sprint 7** (20 Gen - 31 Gen): 36 story points completati su 40 pianificati (90%) - Ritardo Frontend

Escludendo lo Sprint 5, che cade interamente nel periodo natalizio e non è rappresentativo del ritmo di regime, la velocity media è stata di 38,3 story points: leggermente inferiore al target di 40 ma molto vicina, a conferma che la stima iniziale era realistica e che il team stava lavorando in modo consistente. Lo Sprint 5 ha invece prodotto un carryover di 19 story points, riassorbito nei due sprint successivi. Il calo di velocity nello Sprint 7 è stato direttamente correlato al ritardo accumulato dal Frontend Tavolo da Gioco e ha innescato il recovery plan.

Durante le Sprint Retrospective, il team ha anche discusso i fattori che hanno influenzato la velocity, come ad esempio l'underestimation di alcune user stories particolarmente complesse o la necessità di dedicare tempo al refactoring per mantenere la qualità del codice. Queste riflessioni hanno permesso al team di migliorare progressivamente le proprie stime e di identificare pattern ricorrenti che causavano rallentamenti.

## 5.9 Quality Metrics

Oltre al monitoraggio di scope, schedule e budget, un'area critica per il successo del progetto MaraffaOnline è la qualità del software prodotto. PlayHeritage Labs ha stabilito dei quality gates che devono essere rispettati affinché una feature possa essere considerata "Done" e contribuire all'Earned Value:

1. **Test Coverage minimo 85%**: Ogni componente deve avere test unitari che coprono almeno l'85% del codice. Questo garantisce che le funzionalità siano verificate automaticamente e che eventuali regressioni vengano identificate rapidamente.

2. **Zero bug critici aperti**: Prima di considerare una feature completata, tutti i bug di severità critica devono essere risolti. I bug di severità media o bassa possono essere posticipati a sprint successivi se non bloccano funzionalità core.

3. **Code review approvata**: Ogni pull request deve essere rivista e approvata da almeno un altro membro del team prima del merge. Nel caso di modifiche particolarmente critiche (ad esempio, logica del Game Engine o sincronizzazione Real-Time), la code review deve essere effettuata da Elena Rossi, la Tech Lead.

4. **Performance requirements soddisfatti**: Per il sistema Real-Time Communication, la latenza deve essere inferiore a 500ms. Questo viene verificato attraverso load test automatizzati che simulano 100 partite simultanee (400 giocatori concorrenti), il carico previsto dalle Conditions of Satisfaction.

Durante i Project Status Meeting, Elena Rossi presenta un report sulle quality metrics che include:

- **Test Coverage attuale**: Monitorato attraverso tool di code coverage integrati nella CI/CD pipeline. Durante Gennaio 2026 il coverage era all'87%, superiore al target dell'85%.

- **Bug Burn Down**: Grafico che mostra il trend dei bug aperti nel tempo, suddivisi per severità. Un trend crescente indica problemi di qualità che richiedono attenzione immediata.

- **Code Complexity**: Metriche come il Cyclomatic Complexity per identificare porzioni di codice che potrebbero beneficiare di refactoring per migliorare la manutenibilità.

- **Technical Debt**: Stima del tempo necessario per "pulire" il codice e risolvere shortcuts presi per rispettare le deadline. PlayHeritage Labs ha stabilito che il technical debt non deve superare il 10% del tempo totale di sviluppo.

Queste metriche di qualità sono fondamentali per garantire che il progetto non stia accumulando problemi nascosti che potrebbero emergere durante la fase di UAT (User Acceptance Testing) o, peggio ancora, in produzione dopo il lancio.

## 5.10 Risk Monitoring

I rischi identificati durante la fase di Scoping attraverso la Risk Rating Matrix non sono statici ma evolvono nel tempo. Un rischio che inizialmente era valutato come "bassa probabilità - alto impatto" può diventare "alta probabilità - alto impatto" se le condizioni del progetto cambiano. Per questo motivo, durante ogni Project Status Meeting viene dedicato un segmento alla review dei rischi.

Marco Venturi mantiene un Risk Log su Notion che traccia lo stato di ciascun rischio identificato nella Risk Rating Matrix. Per ogni rischio viene monitorato:

- **Status attuale**: Aperto, In Mitigation, Mitigato, Materializzato (il rischio si è verificato)
- **Probabilità e Impatto aggiornati**: Rivalutati sulla base delle informazioni emerse durante il progetto
- **Azioni di mitigazione intraprese**: Cosa è stato fatto per ridurre la probabilità o l'impatto
- **Owner**: Chi è responsabile di monitorare il rischio e attivare il piano di contingenza

Durante i primi quattro mesi del progetto, il rischio R1 "Esperienza limitata con tecnologie WebSocket" è stato l'oggetto di attenzione maggiore. Inizialmente valutato come probabilità Alta (4) e impatto Disastroso (4) per un rating di 16 (Rosso Critico), è stato affrontato con uno spike tecnico di due settimane e, durante lo Sprint 2, con un proof of concept che ha mostrato una latenza di 180ms: la dimostrata padronanza della tecnologia ha ridotto la probabilità a Media-Bassa (2), portando il rating a 8 (Arancione). Il load test completo previsto per lo Sprint 6 ha confermato che con le ottimizzazioni implementate la latenza si mantiene sotto i 500ms anche con 100 partite simultanee (400 giocatori, il target delle Conditions of Satisfaction), permettendo di chiudere il rischio come "Mitigato".

Il rischio R4 "Scope creep da richieste committente" è rimasto costantemente monitorato ma non si è mai materializzato, grazie alla chiarezza del POS (Project Overview Statement) e al rigore con cui Marco ha applicato il Change Request Process. Giovanni Marchetti ha accettato che alcune feature nice-to-have venissero posticipate alla versione 1.1 quando la loro implementazione avrebbe impattato il critical path.

## 5.11 Risultati del Monitoraggio

Grazie al monitoraggio costante e ai sistemi di early warning implementati (Stoplight Reports, Earned Value Management, Velocity Tracking, Quality Metrics, Risk Monitoring), il progetto MaraffaOnline è riuscito a mantenere una traiettoria stabile verso gli obiettivi definiti nelle Conditions of Satisfaction.

Tutti i criteri previsti sono stati rispettati entro le tolleranze accettabili. Grazie al monitoraggio costante lungo l'intero ciclo di vita del progetto (Ottobre 2025 - Maggio 2026), il consuntivo sui diversi criteri è stato il seguente:

**Criteri Temporali**: Il progetto ha accumulato un massimo di 3 giorni di ritardo sul critical path durante Gennaio 2026, ma grazie al recovery plan il ritardo è stato recuperato entro fine Febbraio. La data di lancio del 15 Maggio 2026 è stata mantenuta.

**Criteri Economici**: Il budget di €25.000 è stato rispettato. A fine Febbraio 2026 (Mese 4) le spese totali erano di €17.500 su €17.800 pianificate, con uno scostamento favorevole di €300 (1,7%), ben all'interno del Contingency Buffer del 18,7%.

**Criteri Tecnici**: Tutte le regole del Maraffone/Beccaccino sono state implementate correttamente e validate da Francesca Giuliani durante la Sessione 1 di validazione (Novembre 2025). Il sistema Real-Time mantiene una latenza media di 185ms, sotto il target di 500ms. Il test coverage è stabilmente sopra l'85%.

**Criteri Qualitativi**: L'esperienza utente è stata validata in due momenti. Una prima sessione a Gennaio 2026 con 5 membri della community Maraffa Forever ha dato riscontri positivi sull'usabilità e portato a piccole migliorie implementate nello Sprint 11. La User Acceptance Testing ufficiale, condotta con 10 tester della community nella prima metà di Maggio 2026, ha poi confermato che l'80% degli utenti è riuscito a completare una partita senza aiuto, soddisfacendo il criterio di usabilità definito nelle Conditions of Satisfaction.

**Criteri di Gestione del Lavoro**: Il team ha lavorato in modo coeso e collaborativo. Le Sprint Retrospective hanno prodotto 30 action items di miglioramento continuo nel corso dei 15 sprint, di cui 28 sono stati completamente implementati, portando a un progressivo aumento dell'efficienza del team.

Grazie a questo monitoraggio multilivello il progetto, collaudato internamente con successo, ha superato anche la fase finale di UAT ed è giunto pronto al lancio pubblico del 15 Maggio 2026. La chiusura formale, l'accettazione da parte del committente e le lezioni apprese sono descritte nel Capitolo 6 - Closing.
