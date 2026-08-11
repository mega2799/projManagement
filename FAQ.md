# FAQ Orale — Domande previste e risposte (MaraffaOnline)

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Domande che il professore può plausibilmente fare sull'elaborato, con la risposta "modello" in versione **didattica**: ogni risposta è autosufficiente — definisce i termini e gli acronimi che usa, con la terminologia del corso (dispense/knowledge_base) e i numeri del progetto. Studiare le risposte equivale a ripassare la teoria *e* l'elaborato insieme.
>
> Come usarla: prima lettura integrale come ripasso; poi a campione, coprendo la risposta. Le risposte sono la traccia da espandere a voce, non da recitare. Documenti gemelli: `PREPARAZIONE-ORALE.md` (numeri e casi speciali) e `SCELTE-DI-PROGETTO.md` (il perché di ogni scelta, con riquadri di teoria).

---

## A. Inquadramento generale

**A1. Mi presenti il progetto in due minuti.**
MaraffaOnline è una piattaforma web multiplayer per la Maraffa romagnola, sviluppata da PlayHeritage Labs (spin-off dell'Università di Bologna a Cesena, specializzato nella digitalizzazione di giochi tradizionali) per la community "Maraffa Forever": ≈150 ex studenti dispersi per l'Italia e l'Europa che hanno raccolto €25.000 con un crowdfunding interno. Il problema è sociale e geografico: le app esistenti sono obsolete o solo single-player, e la dimensione conviviale del gioco si è persa. Il progetto dura 7 mesi (15/10/2025–15/05/2026), con un team di 5 persone part-time e un contratto a corpo (prezzo fisso) in 3 tranche. La cifra gestionale è l'**approccio ibrido**: 7 sottosistemi debolmente accoppiati, a ciascuno il ciclo di vita più adatto (Waterfall, Agile Iterativo, Agile Adattivo, Incrementale), tenuti sincronizzati da una cadenza comune bi-settimanale. Chiusura on time e on budget: €22.750 spesi su €25.000, indici di efficienza EVM entrambi a 1, tutti i criteri di soddisfazione rispettati.

**A2. Perché questo è un "progetto" e non un'attività operativa?**
Per il PMBOK un progetto è un'iniziativa **temporanea** (inizio e fine definiti) che crea un risultato **unico**; per Wysocki (definizione "business value") è una sequenza finita di attività dipendenti il cui completamento fornisce il **business value atteso** — dove il business value è il valore percepito dal *destinatario*. Un'attività operativa, al contrario, è continuativa e ripetitiva e segue procedure esistenti. MaraffaOnline ha inizio e fine contrattuali, un deliverable unico (l'MVP, *Minimum Viable Product*: la prima versione funzionante con le sole funzioni essenziali) e un valore definito dal committente: rigiocare insieme a distanza.

**A3. Qual è la scelta di Project Management più importante dell'elaborato?**
L'approccio ibrido per sottosistema (Allegato 2.10). La scelta del modello di ciclo di vita (PMLC, *Project Management Life Cycle*) è guidata dal **quadrante di Wysocki** — due domande: il goal è chiaro? la soluzione è chiara? — applicato componente per componente: Waterfall (sviluppo sequenziale a fasi, senza iterazioni) dove requisiti e soluzione sono chiari (Game Engine), Iterativo dove serve feedback continuo (Backend e Frontend), Adattivo dove la soluzione è incerta (Real-Time), Incrementale dove il valore si consegna a rilasci indipendenti (Social, Infrastructure). Il costo dell'ibrido è la sincronizzazione, gestito con una cadenza comune: scansione bi-settimanale per tutti, demo di fine sprint, milestone di integrazione mensili e settimane 4/8/12 dedicate solo a integrazione.

**A4. In quale quadrante di Wysocki cade il progetto?**
Il quadrante incrocia chiarezza del goal e della soluzione: goal e soluzione chiari → **TPM** (Traditional PM: modelli Linear e Incremental); goal chiaro ma soluzione incerta → **APM** (Agile PM: Iterative e Adaptive); nessuno dei due chiaro → xPM/Extreme. Il nostro progetto ha **goal sempre chiaro** ma la soluzione è chiara solo in parte — per questo non un modello unico ma la scomposizione: Game Engine in TPM/Linear, Real-Time in APM/Adaptive, Backend e Frontend in APM/Iterative, Social e Infrastructure in TPM/Incremental. La regola del corso conferma la scelta: all'aumentare dell'incertezza sulla soluzione servono più iterazioni, pianificazione just-in-time, più risk management e più coinvolgimento del cliente — che è esattamente il gradiente tra i nostri sottosistemi.

**A5. Cosa fareste diversamente (lessons learned)?**
Cinque lezioni, tutte agganciate a strumenti concreti: (1) prototipare le interfacce complesse già in fase di stima — le animazioni del tavolo, stimate 8 story point col Planning Poker, erano sottostimate; (2) tenere gli esperti di dominio nel loop anche *durante* lo sviluppo, non solo nello Scoping — a novembre l'esperta ci ha fatto riclassificare la Maraffa da Should a Must; (3) anticipare il cross-browser testing (la verifica su tutti i browser) ai primi sprint con interfaccia, gli Sprint 5–6 — farlo solo allo Sprint 12 costò 2 giorni di correzioni per Safari; (4) daily standup asincrono strutturato (uno Slackbot dallo Sprint 7) per i periodi di lavoro remoto; (5) refactoring continuo al 10–15% di ogni sprint invece di uno "sprint di pulizia" del debito tecnico — lo Sprint 10 dedicato al cleanup ha mostrato poco valore visibile allo sponsor.

---

## B. Scoping

**B1. Cos'è il POS e cosa contiene il vostro?**
Il Project Overview Statement è la descrizione sintetica del progetto destinata al **senior management** — idealmente una pagina — con 5 sezioni: Problema/Opportunità, Goal, Obiettivi, Criteri di successo, Assunzioni-Rischi-Ostacoli. Non è un contratto: serve a far approvare l'idea. Il nostro ha 6 obiettivi numerati con una **tracciabilità 1:1**: ogni criterio di successo e ogni gruppo di rischi porta il numero dell'obiettivo a cui si riferisce — così l'audit di chiusura (Cap. 6) ha potuto verificare obiettivo per obiettivo.

**B2. Differenza tra goal e obiettivi? I vostri sono S.M.A.R.T.?**
Il goal è 1–2 frasi che circoscrivono l'ambito (lo "scoping statement"); gli obiettivi sono 5–6 statement "necessari e sufficienti" che definiscono cosa è incluso e cosa no. S.M.A.R.T. è l'acronimo di Doran per gli obiettivi ben scritti: **S**pecific (specifici), **M**easurable (misurabili), **A**ssignable (assegnabili a qualcuno), **R**ealistic (realistici), **T**ime-related (con una scadenza). I nostri 6 obiettivi lo sono: hanno criteri quantitativi (latenza ≤500ms, 100 partite simultanee, soddisfazione ≥4,2/5, consegna 15/05/2026, budget €25.000±5%), responsabili (dalla matrice RASCI) e scadenze.

**B3. Cosa sono le Conditions of Satisfaction e come le avete costruite?**
Sono le condizioni negoziate tra chi chiede (requestor) e chi fornisce (provider) che guidano requisiti e decisioni per tutto il ciclo di vita; il ciclo di negoziazione del corso è **Request → Clarify Request → Response → Agree on Response** (richiesta, chiarimento, controproposta, accordo). Le nostre: 22 condizioni in 5 tipologie (temporale, economica, tecnica, qualitativa, gestione del lavoro), negoziate con lo sponsor e tutte con soglie misurabili. Differenza dagli acceptance criteria: le CoS dicono **cosa** deve essere il risultato (e vengono dal committente); gli acceptance criteria dicono **come verificare** che una singola funzionalità sia accettabile (e li scrive il team, storia per storia).

**B4. Differenza tra assunzione, rischio e ostacolo (sezione 5 del POS)?**
Un'**assunzione** è una condizione data per vera su cui il piano si fonda (es. "le regole saranno documentate entro il 25/09", "i pagamenti saranno puntuali"); un **rischio** è un evento *incerto* con una probabilità e un impatto, da gestire con la matrice (es. l'inesperienza WebSocket); un **ostacolo** è una difficoltà *nota e certa* da superare (es. il budget per persona sotto mercato). Il legame: se un'assunzione cade, spesso diventa un rischio materializzato.

**B5. Come avete valutato i rischi? Perché il budget è "Accept" e non mitigato?**
Con la matrice qualitativa **probabilità × impatto**: probabilità in 4 fasce (A = 0-25% … D = 76-100%) × impatto in 4 livelli (Trascurabile → Disastroso), valore del rischio = P×I da 1 a 16, scala colori a 5 livelli. 20 rischi: 2 critici (rating 16), 6 rossi, 7 arancioni, 5 gialli. Le 5 strategie di risposta del corso sono **Accept, Avoid, Mitigate, Contingency, Transfer** (accettare, evitare, mitigare subito, pianificare il "se succede", trasferire ad altri). Il rischio budget (16) è **Accept** perché non è mitigabile (il crowdfunding è quello) né trasferibile (nessuno lo assicura): lo si accetta consapevolmente — decisione formalizzata nel meeting di approvazione — compensandolo col modello part-time e col valore strategico del progetto pilota per lo spin-off.

**B6. Differenza tra Mitigate e Contingency? Perché sul WebSocket avete scelto la contingency?**
**Mitigate** = agire *subito* per ridurre probabilità o impatto; **Contingency** = preparare *ora* un piano da eseguire *se e quando* l'evento si verifica. Sull'inesperienza WebSocket (WebSocket = il canale di comunicazione bidirezionale e persistente tra browser e server, indispensabile per il gioco in tempo reale) non si può "mitigare subito" un'incognita di fattibilità: si riduce l'incertezza con uno **spike** — un esperimento tecnico *time-boxed*, cioè a tempo massimo prefissato (2 settimane) — e si prepara il piano B: decision point go/no-go al giorno 15 che attiva il consulente esterno (Dr. Nardi, €2.000 già accantonati), escalation al committente al giorno 30. Poi il proof of concept dello Sprint 2 ha misurato 180ms di latenza, dimezzando il rating da 16 a 8, e il load test dello Sprint 6 lo ha chiuso come "Mitigato".

**B7. A cosa serve un Business Model Canvas in un progetto non-profit?**
Il BMC (Osterwalder) descrive su una pagina come un'organizzazione *crea, distribuisce e cattura valore*, in 9 blocchi (partner, attività e risorse chiave; proposta di valore; relazioni, canali e segmenti di clientela; costi e ricavi). Serve anche qui: a verificare che il modello regga. Il valore è duale — per la community (riconnessione sociale, fedeltà alle regole) e per PlayHeritage (validazione del modello, portfolio, pubblicazioni) — e la cattura economica attuale è il crowdfunding; i ricavi futuri (manutenzione, licensing, freemium) sono dichiarati come visione. Il Cash Flow contiene anche una **break-even analysis onesta** (break-even = il momento in cui i ricavi cumulati coprono i costi): il freemium non copre i costi → progetto non-profit per la community, e lo scriviamo invece di inventare ricavi.

**B8. SWOT e Risk Analysis non sono ridondanti?**
No: la SWOT classifica **fattori** — interni (Strengths/Weaknesses, su cui hai controllo) ed esterni (Opportunities/Threats) — mentre la Risk Analysis valuta **eventi** incerti con probabilità e impatto. Le abbiamo collegate esplicitamente (la debolezza W1 = il rischio 2.1, W4 = 6.4, la minaccia T2 = 6.2) e la nostra SWOT va oltre la descrizione: è estesa a **matrice TOWS**, l'incrocio dei quadranti che genera strategie SO (usare le forze per cogliere le opportunità), WO, ST, WT — con coppie esplicite e 4 azioni immediate (pre-allerta del consulente, governance decisionale, meeting GDPR col legale, accordo di commitment del team).

**B9. PoC, prototipo e MVP nel vostro progetto?**
Tre strumenti per tre incertezze diverse. **PoC** (Proof of Concept) = verifica di *fattibilità tecnica* ("si può fare?") → lo spike Socket.IO con 4 client e latenza misurata 180ms. **Prototipo** = mostra *aspetto e uso* per correggere prima di costruire ("è così che lo volevi?") → i mockup Figma v1→v2 (v1 commentata dalla community, v2 approvata e vincolante). **MVP** = la prima versione *funzionante* che dà business value reale → la release del 15 maggio.

**B10. Come sono fatte le vostre user stories? Cos'è INVEST?**
23 storie in 7 epiche (un'epica è una storia troppo grande, da spezzare), nel formato "Come <ruolo> voglio <azione> così da <beneficio>", ognuna con criteri di accettazione puntuali e approccio di test. INVEST (Wake) è la checklist di qualità di una storia: **I**ndependent (indipendente dalle altre), **N**egotiable (negoziabile nel come), **V**aluable (porta valore all'utente), **E**stimable (stimabile), **S**mall (piccola), **T**estable (verificabile) — verificata in tabella criterio per criterio. Scelta di pulizia: nel 2.9 non ci sono priorità, story point né sprint, perché appartengono al Planning (Allegati 3.2 e 3.3): separazione tra il *cosa* (Scoping) e il *quanto/quando* (Planning).

**B11. Differenza RBS/WBS?**
La **RBS** (Requirements Breakdown Structure) è la gerarchia dei **requisiti** (Requirement → Function → Sub-function → Feature): dice *cosa* va consegnato, con un linguaggio comprensibile al committente. La **WBS** (Work Breakdown Structure) è la gerarchia del **lavoro** necessario a soddisfarli: dice *come si organizza il fare*. Nel processo di Wysocki la completezza della RBS è il fattore principale per scegliere il ciclo di vita: da noi, RBS del Game Engine completa e stabile → Waterfall; RBS del Real-Time incerta → Adattivo.

**B12. Perché Waterfall sul Game Engine, nel 2026, per del software?**
Perché è il caso da manuale del quadrante TPM: goal e soluzione entrambi chiari. Il Waterfall — sviluppo sequenziale a fasi (analisi → design → implementazione → test → validazione) senza iterazioni — è efficiente proprio quando i requisiti non cambieranno: le regole della Maraffa sono fisse da decenni, documentate e **validate formalmente dall'esperta prima dello sviluppo**; i test si scrivono a monte partendo da partite a risultato noto; il feedback iterativo degli utenti non aggiunge nulla (le regole le conoscono già). Il rischio classico del Waterfall — i requisiti che cambiano a lavori in corso — qui è improbabile per costruzione. Usare Scrum sul Game Engine sarebbe overhead senza beneficio.

**B13. Perché non avete considerato il modello Extreme?**
Il quadrante xPM richiede goal **e** soluzione entrambi non chiari — progetti di ricerca ed esplorazione, dove persino l'obiettivo si scopre strada facendo. Da noi il goal è sempre chiaro; l'incertezza massima (Real-Time) riguarda solo la *soluzione* → modello Adattivo, non Extreme. Nemmeno MPx si applica (è il caso inverso: una soluzione/tecnologia chiara in cerca di un goal).

---

## C. Planning

**C1. Come sapete che la vostra WBS è completa?**
Con la **100% rule**, dichiarata nell'allegato: la WBS copre il 100% del lavoro del progetto — inclusa la sezione trasversale di project management, documentazione e QA — e la somma dei figli equivale sempre al padre. Il corso dà anche i **6 test di completezza** per il singolo task: stato e completamento misurabili, inizio e fine ben delimitati, un deliverable associato, tempi e costi stimabili, durata entro un limite accettabile, indipendenza dagli altri task. I 6 test si applicano al livello di controllo, cioè alle nostre **43 attività** (work package da ≈7 giorni-uomo, dentro la *8/80 rule*): ognuna li rispetta. I 160 task del 4° livello sono la scomposizione operativa che alimenta lo Sprint Backlog, non l'unità di controllo (doppia lettura dichiarata nell'allegato). Abbiamo semplificato i 6 livelli canonici di Wysocki in 4 perché i livelli Goal/Objective sono già assorbiti dalla struttura per sottosistemi della RBS.

**C2. 302 giorni-uomo di stima ma 141 giorni di progetto: come si conciliano?**
Sono grandezze diverse. I 302 giorni-uomo sono l'**effort** (lo sforzo): il lavoro totale, sommato su tutte le persone. I 141 giorni lavorativi sono la **duration** (la durata): il tempo di calendario che passa. Il corso insiste che la relazione tra le due non è lineare (aggiungere persone non accorcia proporzionalmente). Con 5 persone part-time che lavorano in parallelo su 6 sottosistemi: 302 ÷ 141 ≈ 2,1 FTE medi (FTE = Full-Time Equivalent, "persone a tempo pieno equivalenti"), perfettamente coerente con un team di 5 al ≈50%.

**C3. Mi spieghi il Critical Path Method sul vostro network.**
Il Project Network Diagram rappresenta le 20 attività (A–T) come nodi e le dipendenze come frecce (formato Activity-On-Node). Il CPM procede così: (1) **forward pass**, da sinistra a destra, calcola per ogni attività Early Start ed Early Finish — il primo momento possibile di inizio e fine; (2) **backward pass**, da destra a sinistra, calcola Late Start e Late Finish — l'ultimo momento possibile senza ritardare il progetto; (3) lo **slack** (o float) = LS − ES è quanto un'attività può slittare senza danni. La catena delle attività a slack zero è il **critical path**: da noi **A→B→D→G→J→M→P→R→S→T = 141 giorni lavorativi**, esattamente i giorni disponibili dal 15/10 all'08/05 festività escluse — restano 5 giorni lavorativi di margine sul lancio del 15/05. I rami non critici hanno float: Game Engine (C-F-I-L-O) 22 giorni, Chat/Social (E-H-K-N-Q) 37 giorni. L'attività singola più critica è P, il Frontend del tavolo da gioco: 40 giorni.

**C4. Fast tracking e crashing: differenza, e dove li avete usati?**
Sono le due tecniche di **compressione della schedula** (schedule compression), cioè di accorciamento del calendario. Il **fast tracking** mette in parallelo attività che erano in sequenza: non costa denaro, ma aumenta il rischio di *rework* (se l'attività a monte cambia, il lavoro fatto in parallelo va rifatto). Il **crashing** aggiunge risorse alle attività critiche: costa denaro e non scala linearmente. Il monito del corso: "la compressione non è mai gratis". Fast tracking usato davvero: il legame **P→R Start-to-Start con lag di 31 giorni** — il Testing End-to-End (R) non aspetta la fine del Frontend Tavolo (P, 40 giorni), ma parte quando P ne ha completati 31, testando i moduli già congelati (login, dashboard, stanze) mentre P rifinisce le animazioni; il rischio di rework è dichiarato e mitigato sequenziando i test sui moduli stabili e con la suite automatizzata Cypress, rieseguibile a ogni modifica. Crashing previsto solo come leva di riserva nella sensitivity analysis: se P ritarda 10 giorni, +1 contractor esterno part-time ≈ €2.000 dal Contingency Buffer.

**C5. Il corso dice "Do not plan to use slack to bail out the project". Ma il vostro primo livello di escalation è proprio lo slack: contraddizione?**
No, e la distinzione è tra pianificare e reagire. Il monito vieta di **pianificare** contando sullo slack — cioè costruire una baseline che lo consuma già, lasciandosi senza margini. Noi lo usiamo **a consuntivo**: quando uno scostamento si è già verificato, la prima domanda è "c'è float che lo assorbe?" — è il primo gradino della Problem Escalation Strategy del corso (leve del PM → leve sulle risorse → leve del cliente). La nostra baseline non assume mai il consumo del float.

**C6. Perché i Must Have sono al 75,8% se DSDM raccomanda ≈60%?**
DSDM (Dynamic Systems Development Method, la metodologia agile in cui nasce il MoSCoW) raccomanda ≈60% Must / 20% Should / 20% Could proprio perché i Could sono la "valvola di sfogo": se sei in ritardo li tagli e salvi la data. La nostra distribuzione (75,8 / 18,9 / 5,3 su 302 giorni-uomo) è una **scelta deliberata e documentata**: Game Engine e Real-Time sono il *core differentiator* — senza regole fedeli e partite fluide il prodotto non esiste — quindi il Must è strutturalmente alto; in compenso i Could sono compressi al 5,3% in funzione anti-scope-creep. Il rovescio (meno margine di de-scoping) è compensato dal Contingency Buffer del 18,7% sul budget, dai float dei rami non critici e dai Won't Have già negoziati ed esclusi.

**C7. Come avete stimato? Perché due tecniche?**
Entrambe sono tecniche di **stima consensuale**, nate per neutralizzare i bias individuali; abbiamo scelto quella adatta a ciascun contesto. **Delphi** (per il Game Engine, tradizionale): ogni membro dà una stima *anonima* con motivazione, si condividono i risultati e si ripete per più round fino alla convergenza — l'anonimato evita l'**ancoraggio**, il bias per cui la prima cifra sentita condiziona tutte le altre. **Planning Poker** (per i sottosistemi agili): il Product Owner presenta l'elemento, ognuno sceglie in segreto una carta della scala di Fibonacci (1, 2, 3, 5, 8, 13, 21 — i salti crescono come cresce l'incertezza), si scoprono le carte insieme, si discutono le discrepanze e si ripete fino al consenso. Il corso cita anche la stima three-point, E = (O + 4M + P) / 6 con ottimistica/più probabile/pessimistica: non l'abbiamo usata, ma va saputa.

**C8. Cosa sono gli story points? 310 SP su 15 sprint fanno ≈21 a sprint, ma dichiarate una capacity di 40: non torna.**
Gli **story point** misurano la *complessità relativa* di un lavoro, non il tempo: sono adimensionali, si assegnano con il Planning Poker e si usano per pianificare quanta roba entra in uno sprint. La chiave della domanda è distinguere **capacità** da **carico**: i 40 SP/sprint sono la **capacity team-wide** — quanto il team *può* completare in uno sprint, includendo il lavoro di Game Engine e Infrastructure convertito in "punti equivalenti" (≈131 SP; totale progetto ≈441). Il **carico medio pianificato** è più basso: ≈37 SP/sprint a livello di team (441 su Sprint 0–11) e ≈28 SP/sprint di solo Backlog (310 su Sprint 1–11); il margine tra 40 e 37 assorbe festività e variabilità delle stime. La **velocity** (gli SP completati per sprint, misurati a consuntivo) media è 38,3 — coerente con la capacity. Due letture dichiarate esplicitamente: metrica gestionale consolidata per lo sponsor, carico Scrum per il team.

**C9. E lo sprint di Natale?**
Lo Sprint 5 (22/12–2/1) è pianificato **a capacità ridotta**: 21 SP completati su 40 (52,5%), con un *carryover* di 19 SP — il lavoro non finito che "trasloca" agli sprint successivi, dove è stato riassorbito. La media di velocity di 38,3 lo **esclude** dichiaratamente perché non rappresentativo del ritmo di regime: dirlo apertamente è onestà metodologica, non un trucco statistico.

**C10. Come funziona il vostro cash flow? Perché l'outflow decresce alla fine?**
Il Cash Flow Management traccia entrate (inflow) e uscite (outflow) per periodo e il **saldo cumulativo**: il principio del corso è che non basta chiudere in utile — si può fallire *in utile* se la cassa va sotto zero a metà strada. Gli incassi sono 3 tranche (12.500/6.250/6.250 a ottobre/dicembre/febbraio): l'ultimo arriva a metà progetto, quindi la coda (marzo–maggio) vive del saldo accumulato → l'outflow scende nei mesi 5–7 (team ridotto su testing, UAT e lancio). Risultato: saldo cumulativo **sempre positivo, minimo €2.250** nell'ultimo mese. Due riserve distinte: la **contingency** (€4.664, 18,7%, distribuita nei mesi) copre imprevisti e change request; il **surplus** finale (€2.250, 9%) è il margine che resta, destinato al supporto post-lancio.

**C11. Contratto a corpo con sottosistemi adattivi: il corso non suggerisce il time & materials quando le stime sono incerte?**
Sì: a corpo (fixed price) il rischio delle stime ricade sul fornitore, a consuntivo (time and materials) sul committente, e con stime incerte il corso suggerisce il consuntivo. Ma qui il vincolo dominante è il **budget fisso del committente** (un crowdfunding chiuso): il prezzo fisso era l'unica forma accettabile per la community. Il rischio di stima che il corpo scarica su di noi è gestito *dentro* il progetto: MoSCoW con Could sacrificabili, Contingency Buffer del 18,7%, spike anticipato sul rischio tecnico maggiore, e Won't Have negoziati che delimitano lo scope. È una risposta di risk management alla rigidità contrattuale.

**C12. A cosa serve il Gantt se avete già il network diagram?**
Sono due strumenti con due mestieri. Il **network** modella le *dipendenze logiche* e serve a **calcolare**: critical path, float, analisi what-if ("cosa succede se P ritarda?"). Il **Gantt** traduce tutto in **calendario**, con barre orizzontali e milestone (eventi a durata zero che segnano un traguardo), ed è lo strumento di monitoraggio e comunicazione: nel Cap. 5 mostra la linea dell'oggi, le percentuali di completamento e il ritardo di gennaio con la barra rossa. Il flusso dichiarato: prima il network, poi il Gantt che ne deriva; se c'è un cambiamento importante si ricalcola il network.

**C13. La WBS non è troppo dettagliata? Un task come "definire struttura dati per carte" non è implementazione più che gestione?**
La WBS ha una **doppia lettura dichiarata**. Il livello di **controllo gestionale** sono le 43 attività: work package con effort medio di ≈7 giorni-uomo, dentro la finestra della **8/80 rule** (la regola pratica per cui un work package dovrebbe valere tra 8 e 80 ore), ed è su queste che si esercitano stima, responsabilità (la RASCI è infatti a livello di attività) e schedulazione — il Project Network Diagram lavora su 20 attività aggregate, raccordate alla WBS da una **tabella di tracciabilità nell'Allegato 3.5**. I 160 task del 4° livello (≈2 giorni-uomo l'uno) sono la **scomposizione operativa**: alimentano lo Sprint Backlog dei sottosistemi agili e garantiscono la tracciabilità requisito → lavoro, e il loro dettaglio "tecnico" è uno dei quattro usi che il corso attribuisce alla WBS — il *thought process tool*: dimostra la padronanza del dominio senza cui le stime sarebbero indifendibili. Il controllo di progetto non si esercita mai sul singolo task da mezza giornata.

---

## D. Launching

**D1. Cos'è la RASCI e come l'avete applicata?**
È la matrice di assegnazione delle responsabilità (Responsibility Assignment Matrix, variante della RACI): per ogni attività, **R**esponsible = chi *esegue* (possono essere più d'uno), **A**ccountable = chi *approva e risponde del risultato* — e **deve essere uno solo per attività**: "se ci sono troppi Accountable, nessuno è veramente responsabile" — **S**upport = chi dà supporto operativo, **C**onsulted = chi va consultato (comunicazione a due vie), **I**nformed = chi va informato (a una via). Otto matrici (una per sottosistema più QA e PM), per un totale di **51 righe a livello di attività della WBS**: i task di dettaglio ereditano la riga dell'attività a cui appartengono, mentre le attività con distribuzione di ruoli diversa hanno riga dedicata — così le eccezioni risaltano invece di annegare nella ripetizione. Accountability ripartita per natura della decisione: tecnica a Elena (Tech Lead), cerimonie e coordinamento a Marco (PM), business e milestone a Giovanni (sponsor); sulla UAT i ruoli si ribaltano — A = sponsor, perché è lui che accetta, R = l'esperta che conduce le sessioni.

**D2. Elena è Accountable e Responsible sul Game Engine: non è un conflitto?**
È una sovrapposizione **dichiarata e motivata**, non una svista: è la specialista che implementa il sottosistema, e in un team di 5 la separazione totale dei ruoli sarebbe artificiosa. I contrappesi ci sono: il supporto di Sara, la code review obbligatoria, e soprattutto la **validazione esterna delle regole** da parte di Francesca Giuliani — che è il vero controllo di qualità del Game Engine, indipendente da chi lo ha scritto.

**D3. Che stile decisionale avete adottato?**
Il corso distingue tre stili: **directive** (decide chi ha l'autorità, da solo — veloce ma spreca le competenze del team), **participative/collaborative** (decide tutto il team — coinvolge ma è lento, e Wysocki avverte che "una decisione di consenso che accontenta tutti può comunque essere una cattiva decisione") e **consultative** (decide chi ha l'autorità *dopo aver raccolto l'input del team*). Abbiamo scelto il consultivo, articolato su **3 livelli**: operativo (naming, librerie, bug fix → decide il Responsible del task), tattico (architettura, API, backlog → Tech Lead + PM, sentito il team, con decisione documentata), strategico (scope, budget, timeline → Sponsor, sulla base di un Project Impact Statement preparato dal PM). Regola d'oro: decidere al livello più basso possibile — rapidità, decisioni prese da chi ha le informazioni, niente colli di bottiglia.

**D4. Come gestite i conflitti?**
Su due assi. Per **tipologia**: tecnici → decide Elena su criteri oggettivi (performance, scalabilità, competenze, time-to-market), e poi vale il *disagree and commit* — anche chi era contrario si impegna a eseguire senza rimetterla in discussione; di priorità → decide Marco con MoSCoW e critical path alla mano; interpersonali → Marco come facilitatore neutrale. Per **escalation**, tre fasi progressive: confronto diretto tra le parti in privato → mediazione facilitata → decisione esecutiva. Nel progetto nessun conflitto ha superato la fase 2. Il modello teorico di riferimento del corso (Thomas-Kilmann) classifica 5 stili lungo assertività e cooperazione — competing, collaborating, compromising, avoiding, accommodating: il nostro processo istituzionalizza il collaborating, con un fallback esecutivo per non restare bloccati.

**D5. Come gestite una richiesta di cambiamento?**
Con un processo formale in 5 passi, pensato contro lo *scope creep* (la crescita strisciante e non governata del perimetro): (1) **submission** con un modulo di Change Request (descrizione, motivazione di business, priorità percepita); (2) **impact analysis**: PM e Tech Lead redigono il **Project Impact Statement** — il documento, previsto dal corso, che analizza l'impatto del cambiamento su scope, tempi, budget, qualità e risorse e presenta le opzioni (accettare estendendo la timeline, rinviare alla release successiva, rifiutare) con una raccomandazione; (3) **decisione dello sponsor**; (4) **implementazione**, aggiornando POS, WBS, Gantt e Backlog; (5) **tracciamento** nel Change Log fino a chiusura. Doppio regime coerente con l'ibrido: i sottosistemi agili accolgono il cambiamento come parte del processo (si riprioritizza il backlog), quelli tradizionali lo valutano caso per caso. Nel progetto lo scope creep non si è mai materializzato, e lo sponsor ha accettato di rinviare alcune nice-to-have alla versione 1.1.

**D6. Perché il kick-off dura solo un'ora?**
Perché i materiali (POS, WBS, Gantt, Cash Flow, bozze di RASCI e regole operative) sono stati pre-condivisi il venerdì precedente (10 ottobre): il meeting serve a **decidere e allineare**, non a presentare documenti che tutti possono leggere prima. Ne escono 5 decisioni formali e 7 action item con owner e scadenza, tracciati su Notion. È l'applicazione della nostra regola di comunicazione "asynchronous-first": prima i canali asincroni, i meeting solo per ciò che li richiede davvero.

---

## E. Monitoring & Control

**E1. Mi scriva e commenti le formule dell'Earned Value.**
L'Earned Value Management confronta tre grandezze alla data di controllo: **PV** (Planned Value) = il valore del lavoro che *avresti dovuto* completare secondo il piano; **EV** (Earned Value) = il valore del lavoro *effettivamente completato*, misurato col budget assegnato a quel lavoro; **AC** (Actual Cost) = quanto hai *speso davvero*. Da queste: **CV = EV − AC** (Cost Variance: negativa = spendo più del valore che produco); **SV = EV − PV** (Schedule Variance: negativa = sono in ritardo); **CPI = EV/AC** e **SPI = EV/PV** (indici di efficienza, soglia 1). Esempio dal progetto, gennaio 2026: PV = €14.100, EV = €13.200, AC = €13.500 → CV = −€300 (piccolo extra-costo: ore extra sull'ottimizzazione WebSocket), SV = −€900 (i 3 giorni di ritardo della Dashboard), CPI = 0,98, SPI = 0,94. A chiusura: CPI = SPI = 1,00 su €22.750. Scelta metodologica da sottolineare: **l'EV matura solo sulle feature accettate dallo sponsor in Sprint Review** (Done secondo la Definition of Done) — il valore "guadagnato" è certificato dal cliente, non autodichiarato dal team.

**E2. Cos'è uno Stoplight Report? E gli altri tipi di report del corso?**
Lo Stoplight ("semaforo") assegna a ogni area un colore con le frasi canoniche del corso: **verde** = "the project is progressing according to plan"; **giallo** = "c'è un problema, un Get Well plan è in atto, la situazione rientrerà"; **rosso** = "the project is failing, serve un intervento". Il nostro è settimanale, su 5 aree (Scope, Schedule, Budget, Quality, Risks), ognuna con una nota che motiva il colore. Il corso elenca 5 tipi di report: **current period** (solo il periodo recente), **cumulative** (l'intera storia — mostrano i trend), **exception** (sintetici, per il senior management, solo gli scostamenti), **stoplight** (il semaforo applicabile agli altri) e **variance** (pianificato vs effettivo). Noi usiamo: stoplight settimanale, EVM mensile (che è un cumulative/variance), e il Gantt di tracking come status report visuale.

**E3. Cosa è successo a gennaio e come l'avete gestito?**
L'attività M (Frontend Dashboard e Creazione Stanza, **sul critical path**) accumula 3 giorni di ritardo per la complessità inattesa del flusso stanza/inviti. Il ritardo è visibile su **tre strumenti coerenti** — ed è questo il punto da vendere: Stoplight (Schedule giallo), Gantt tracking (60% completato contro l'80% atteso), EVM (SV = −€900, SPI = 0,94). Intervento con la scala graduata: l'attività è critica, quindi slack da consumare non ce n'è → leva del PM: **recovery plan con pair programming** — Luca affiancato da Sara, una riallocazione interna a costo zero, non un crashing a pagamento → recupero completo entro febbraio, milestone invariate. Morale: il monitoraggio multilivello ha trasformato un problema potenzialmente fatale (era sul percorso critico!) in uno scostamento gestito.

**E4. Come avete monitorato i rischi dopo lo Scoping?**
Il principio: i rischi **non sono statici**. Un **Risk Log** su Notion con stati espliciti (Aperto / In Mitigation / Mitigato / Materializzato), probabilità e impatto **rivalutati** a ogni Project Status Meeting settimanale. Caso guida: il rischio WebSocket parte a rating 16 (probabilità Alta × impatto Disastroso) → lo spike e il proof of concept dello Sprint 2 misurano 180ms e la probabilità scende → rating 8 → il load test dello Sprint 6 (100 partite, 400 giocatori, sotto i 500ms) lo chiude come "Mitigato". Il rischio di scope creep, invece, non si è mai materializzato: POS chiaro + Change Request Process rigoroso.

**E5. La vostra escalation è a 3 livelli; il corso ha una gerarchia più fine. La conosce?**
Sì, sette passi in ordine di invasività: (1) usare gli slack disponibili; (2) riesaminare le dipendenze Finish-to-Start per comprimerle; (3) riassegnare risorse dai task non critici; (4) negoziare risorse aggiuntive col resource manager; (5) proporre rilasci multipli (consegnare in più tranche); (6) chiedere un'estensione della schedula; (7) chiedere una modifica dello scope. I nostri 3 livelli (slack-based → PM-based → client-based) sono la stessa gerarchia raggruppata per "chi possiede la leva": i primi tre passi sono del PM, il quarto delle risorse, gli ultimi tre del cliente.

**E6. Perché monitorate la velocity se metà progetto non è Scrum?**
Per dare allo sponsor **una sola vista consolidata** dell'avanzamento: la capacity di 40 SP e la velocity misurata sono metriche *team-wide*, che aggregano il Product Backlog e il lavoro dei sottosistemi non-Scrum (Game Engine e Infrastructure) convertito in punti equivalenti. È dichiarato esplicitamente nel Cap. 5 con una nota metodologica: non è la velocity Scrum "pura" (quella è ≈28 SP/sprint di solo Backlog — la riconciliazione completa dei numeri sta nella relazione, Cap. 3), è una metrica gestionale. Se il professore chiede "ma si possono sommare punti di lavoro Waterfall?": sì, purché si dichiari che è una convenzione di reporting — ed è dichiarato.

---

## F. Closing

**F1. I passi del Closing secondo il corso, e nel vostro progetto?**
I sei passi canonici, tutti eseguiti: (1) **accettazione formale** del deliverable → firma di Giovanni lunedì 11/05, dopo aver **giocato personalmente una partita completa** (accettazione esperienziale, non solo documentale); (2) **installazione** → il deploy in produzione è a carico della community, come dichiarato fin dall'inizio: consegnate le immagini Docker con le istruzioni e il supporto remoto; (3) **documentazione** completa → su Notion + allegati; (4) **Final Project Report** firmato → consegnato il 12/05, 9 sezioni; (5) **post-implementation audit** → il 13/05, con lo sponsor, criterio per criterio sulle Conditions of Satisfaction; (6) **celebrazione** → il 15/05, con una voce di budget dedicata (€100): persino la festa è pianificata, come vogliono le slide.

**F2. Cosa verifica l'audit post-implementazione? Esito?**
Le domande canoniche del corso: gli obiettivi sono stati raggiunti? tempi, budget e specifiche rispettati? il committente è soddisfatto? il business value si è concretizzato? cosa si è imparato sulla metodologia scelta? Esito: 7 mesi rispettati (unico ritardo: 3 giorni a gennaio, recuperato entro febbraio), €22.750 su €25.000, latenza media 185ms contro il target di 500, 80% degli utenti autonomi alla prima partita, beta tester a 4,5/5 contro il target 4,2, zero errori di regole segnalati. Nota da giocarsi: il corso osserva che l'audit spesso **non** si fa (nessuno vuole pagarlo, o sapere come è andata davvero) — noi lo abbiamo fatto e documentato.

**F3. Il criterio "80 utenti attivi nei primi 2 mesi" come può dirsi soddisfatto alla chiusura del 15/05?**
Non può, alla lettera: è un criterio post-lancio, verificabile solo dopo. Risposta onesta: alla chiusura è **in traiettoria** — nelle prime 24 ore: 50 registrati e 23 partite complete, contro un'aspettativa di 20–30 utenti nella prima settimana — e resta in monitoraggio post-lancio a carico della community, con il supporto finanziato dal surplus. Il Closing dichiara soddisfatti i criteri *verificabili alla data*.

---

## G. Domande scomode (incoerenze note) — risposte pronte

**G1. La UAT è ad aprile (Gantt, M6 24/04) o a maggio (Cap. 5/6: 1–10/05)?**
(UAT = User Acceptance Testing: la validazione finale fatta dagli utenti reali, non dal team.) Lettura difendibile: la **UAT formale** è quella di aprile, come da piano (attività S, milestone M6 = approvazione del 24/04); a inizio maggio c'è una **sessione finale di validazione pre-lancio** con i 10 tester, che il racconto del Closing chiama impropriamente "UAT ufficiale". Da uniformare nel testo; il piano resta coerente.

**G2. La tranche del 15/12 è "a valle del Backend Core", ma la milestone M2 cade il 19/12.**
Sfasatura di 4 giorni: il pagamento era contrattualmente a data fissa (15/12), la review formale della milestone è il 19/12; il Backend Core (attività D e G del network) era di fatto completato prima della data di pagamento. Rilievo minore, da correggere allineando la formulazione contrattuale.

**G3. Il POS assumeva "team dedicato full-time", ma ovunque si parla di part-time 50%.**
Era un refuso del POS, corretto: l'assunzione ora recita "team **dedicato al progetto per tutti i 7 mesi** (impegno ≈50% FTE, senza allocazioni su altri progetti)". I numeri lo confermano: 302 giorni-uomo ÷ 141 giorni ≈ 2,1 FTE, coerente con 5 persone al 50%.

**G4. Il decision point del rischio WebSocket è al giorno 15 o al giorno 30?**
Sono **due checkpoint dello stesso piano di contingenza**, non piani diversi: al **giorno 15** il go/no-go dello spike — se lo spike fallisce si attiva il consulente esterno; al **giorno 30**, se nemmeno col consulente ci sono risultati, escalation al committente. La formulazione è stata armonizzata in tutti gli allegati (Risk 2.4, SWOT W1/T1, 2.10).

**G5. Nelle user stories c'erano regole del gioco sbagliate?**
Sì, due refusi dell'Allegato 2.9, individuati con un audit interno e **corretti** (insieme al punteggio d'esempio "41-38", impossibile col sistema a 11 punti interi per smazzata, ora "41-36"): le fonti normative — la RBS e il documento delle regole validato dall'esperta — hanno sempre detto correttamente che inizia e sceglie la briscola **chi ha il 4 di Denari**, e che la Maraffa è **Asso+2+3 del seme di briscola**. La catena di sicurezza del progetto è proprio questa: la specifica validata dall'esperta è la fonte di verità, e infatti in beta risultano zero segnalazioni di errori sulle regole.

**G6. €16.000 di salari per 5 persone per 7 mesi: sono realistici?**
A valori di mercato no, e non pretendono di esserlo: è un progetto **non-profit finanziato da un crowdfunding**, con un team part-time al ≈50% di uno spin-off universitario che dal pilota ricava valore non monetario (portfolio, pubblicazioni, la tesi di dottorato del PM). La SWOT lo dichiara apertamente come debolezza (W2: €714/mese-persona di budget contro i €2.500–3.000 di mercato) e il rischio budget è formalmente **accettato** da sponsor e team nel meeting di approvazione. La compensazione è strategica, non monetaria — e saperlo dire così è la risposta.

**G7. Lo Sprint 6 carica 47 SP di solo Backlog con una capacity dichiarata di 40: come lo spiegate?**
La capacity è team-wide e **media**: il piano carica in media 37 SP con margine sul 40, ma nei singoli sprint il carico oscilla (S6 = 47, però S2 = 13 e S3 = 16): i picchi si compensano con gli sprint leggeri adiacenti, e parte del carico di S6 è il carryover fisiologico dello sprint natalizio. A consuntivo la velocity si è mantenuta al ritmo di regime (~38) anche in quel periodo: il piano ha retto. Rilievo legittimo comunque: un bilanciamento più uniforme del carico sarebbe stato più pulito, e va ammesso.

**G8. Confrontare i costi effettivi con quelli pianificati ("ho speso meno del previsto") misura l'efficienza?**
No, ed è l'errore classico dell'EVM: AC < PV da solo può significare semplicemente "ho fatto meno lavoro del previsto". L'efficienza si misura passando dall'Earned Value: **CV = EV − AC**. Nel progetto, a febbraio: EV = €17.300, AC = €17.500 → CV = −€200, leggermente sfavorevole ma entro il buffer, con recupero completo nei mesi successivi (CV = 0 alla chiusura). Il Cap. 5 in una prima stesura usava "scostamento favorevole" per un confronto AC-vs-PV: è stato corretto proprio per questa ragione — e saperne spiegare il perché all'orale vale più della correzione stessa.

**G9. Contingency del 18,7% ma surplus del 9%: qual è la riserva vera?**
Sono due cose diverse, entrambe nel Cash Flow: la **contingency** (€4.664, 18,7% del budget) è distribuita nelle uscite mensili come buffer operativo per imprevisti e change request — e in parte è stata davvero consumata (le ore extra sull'ottimizzazione real-time); il **surplus** (€2.250, 9%) è ciò che resta a fine progetto, destinato al supporto post-lancio. Insieme formavano il margine di sicurezza iniziale, ≈27,7%. In termini di corso: contingency reserve la prima, management reserve la seconda.

**G10. La riclassificazione della Maraffa (Should→Must) è passata dal vostro Change Request Process?**
Nella sostanza sì: emersa nella Sessione 1 di validazione con l'esperta (novembre), valutata con lei e con il PM, **compensata riducendo Could Have** (impatto zero su tempi e budget — è la logica MoSCoW: il Must entra, qualcosa di meno prioritario esce) e approvata con lo sponsor; la traccia documentale è la nota di revisione nella MoSCoW. Nella forma, un Change Request numerato con Project Impact Statement sarebbe stato più rigoroso: lo ammettiamo, ed è coerente con la lesson learned sul coinvolgimento continuo dei domain expert.

**G11. Perché non avete usato MS Project?**
Scelta di strumenti dichiarata e coerente col budget: **Notion** (board, database, single source of truth, import CSV del Gantt), **Figma/Miro** per il design, **GitLab CI** per l'integrazione continua, **Excel/HTML** per i grafici e le viste a colori, più uno script Python che genera il Network+Gantt HTML dalle tabelle — tutto low-cost e replicabile. Il criterio delle linee guida ("uso di strumenti software") è dimostrato dagli artefatti prodotti e tenuti coerenti (CPM, Gantt, EVM), non dalla licenza usata.

**G12. Chi è "Luca Bianchi" che firmava la revisione della WBS?**
Un refuso di battitura (fusione di Luca Moretti e Sara Bianchi), individuato in audit interno e **corretto**: il revisore tecnico è la Tech Lead **Elena Rossi**.

**G13. Perché lo sforzo del Game Engine nel MoSCoW è 50 giorni ma la catena C-F-I-L-O del network dura 73 giorni?**
Perché misurano cose diverse: i 50 giorni del MoSCoW sono l'**effort dei requisiti** del sottosistema (giorni-uomo); la catena del network include anche il **testing** (GE Testing 15 giorni + Integration Testing 10), che nel MoSCoW sta nel QA trasversale, e le durate del network sono **giorni di calendario** con risorse part-time, non giorni-uomo. Il raccordo effort→durata passa per lo staffing (chi ci lavora e a che percentuale), non è mai 1:1.

**G14. Il critical path finisce l'8 maggio ma il lancio è il 15: allora un ritardo sul critical path non "impatta direttamente il lancio".**
Il percorso critico determina la data di **consegna** (fine dell'attività T, preparazione lancio): l'8/05. La settimana 8–15/05 è il margine di progetto che ospita accettazione (11/05), report (12/05) e audit (13/05): non è slack di attività — è una **management reserve di calendario**, il 5-10% che il corso raccomanda di tenere. Un ritardo sul critical path consuma prima quel margine e poi sposta il lancio: per questo i 3 giorni di gennaio andavano recuperati subito.

---

## H. Definizioni-lampo (ripasso finale)

| Termine | Risposta in una frase (terminologia del corso) |
|---|---|
| Progetto (PMBOK) | iniziativa **temporanea** per creare un risultato **unico**; temporaneo = inizio e fine definiti |
| Progetto (Wysocki v2) | sequenza finita di attività dipendenti che fornisce il **business value atteso** (valore percepito dal destinatario) |
| Programma vs Portfolio | progetti **interdipendenti** gestiti in modo coordinato vs progetti raggruppati **solo** per facilitarne la gestione |
| Scope Triangle | tempo, costi e risorse ai lati; **scope e qualità al centro**; base del Project Impact Statement e dell'escalation |
| I 4 creep | scope (cambiamenti dal piano), hope (ritardi nascosti "per speranza"), effort (lavoro senza progresso), feature (aggiunte non concordate) |
| IRACIS | le 3 componenti misurabili del business value: Increased Revenue, Avoided Cost, Improved Service |
| S.M.A.R.T. | Specific, Measurable, Assignable, Realistic, Time-related (Doran) — le proprietà di un obiettivo ben scritto |
| CoS | Conditions of Satisfaction: condizioni negoziate col ciclo richiesta/chiarimento/risposta/accordo; da noi 22 in 5 tipologie |
| POS | Project Overview Statement: 1 pagina per il senior management (problema, goal, obiettivi, criteri, assunzioni-rischi-ostacoli); non è un contratto |
| RBS vs WBS | gerarchia dei **requisiti** (cosa consegnare) vs gerarchia del **lavoro** (come organizzarlo); la completezza della RBS guida la scelta del PMLC |
| 100% rule | la WBS copre il 100% del lavoro, incluso il project management stesso; la somma dei figli = il padre |
| 8/80 rule | un work package dovrebbe valere tra 8 e 80 ore (1-10 giorni); le nostre 43 attività (≈7 gg-uomo) la rispettano |
| MoSCoW | Must/Should/Could/Won't (Dai Clegg, da DSDM); da noi 75,8/18,9/5,3 su 302 giorni-uomo, scostamento dal 60/20/20 motivato |
| INVEST | qualità di una user story: Independent, Negotiable, Valuable, Estimable, Small, Testable |
| DoD vs Acceptance Criteria | Definition of Done: checklist unica fissata a inizio progetto, per tutte le storie / criteri per la singola storia, a inizio iterazione |
| Delphi | stime **anonime** con motivazione, più round fino a convergenza (Project RAND); l'anonimato evita l'ancoraggio |
| Planning Poker | carte Fibonacci scelte in segreto, discussione delle discrepanze, ripetizione fino al consenso |
| Story point | misura **relativa e adimensionale** della complessità di un lavoro (non del tempo) |
| Velocity | story point completati per sprint, misurati a consuntivo; da noi 38,3 di regime |
| Effort vs Duration | sforzo (giorni-uomo) vs durata (calendario); relazione non lineare; corso: Labor = 0,75 × Duration; da noi 302 gg-uomo vs 141 gg |
| Forward/Backward pass | andata: calcola ES/EF (prime date possibili); ritorno: calcola LS/LF (ultime date senza ritardare il progetto) |
| Slack (float) | LS − ES: quanto un'attività può slittare senza danni; **zero sul critical path**; totale = senza impatto sul progetto, libero = sul task successivo |
| Critical path | la catena di attività a slack zero che determina la durata: da noi A→B→D→G→J→M→P→R→S→T = 141 giorni lavorativi |
| FS / SS / FF / SF + lag | i 4 tipi di dipendenza (Finish-to-Start la classica; Start-to-Start = partono "insieme") ; lag = ritardo imposto sul legame |
| SS + lag 31 | il nostro fast tracking: il Testing E2E parte quando il Frontend Tavolo ha completato 31 dei suoi 40 giorni |
| Fast tracking vs Crashing | parallelizzare attività sequenziali (gratis, ma rischio rework) vs aggiungere risorse (costa); "la compressione non è mai gratis" |
| Milestone | evento a durata zero che segna un traguardo verificabile; da noi M1–M7, ognuna con un reviewer dedicato |
| Management reserve | riserva del 5-10% (tempo o denaro) tenuta fuori dalla baseline; da noi la settimana 8–15/05 e il surplus del 9% |
| PV / EV / AC | pianificato alla data / valore del lavoro **fatto** / costo **speso**; l'efficienza si misura sempre passando dall'EV |
| CV, SV, CPI, SPI | EV−AC; EV−PV; EV/AC; EV/PV — soglia 1: sotto = oltre budget / in ritardo; da noi a chiusura entrambi 1,00 |
| Stoplight | verde "according to plan"; giallo "Get Well plan in place"; rosso "intervention required" |
| Issue Log / Risk Log | registro dei problemi (con owner, azione, stato) / registro dei rischi con probabilità e impatto **rivalutati** nel tempo |
| RASCI | Responsible esegue, Accountable approva (**uno solo per attività**), Support aiuta, Consulted è sentito, Informed è avvisato |
| Project Impact Statement | documento del PM sull'impatto di un cambiamento (scope/tempi/costi/qualità/risorse) con le opzioni e una raccomandazione |
| Scope Bank | "conto corrente" del tempo di riserva: le change request prelevano, i risparmi e le feature rimosse depositano |
| PMLC (5 modelli) | Linear e Incremental (TPM) — Iterative e Adaptive (APM) — Extreme (xPM); scelti col quadrante goal/solution di Wysocki |
| PoC / Prototipo / MVP | fattibilità tecnica / aspetto-uso per correggere prima / prima versione funzionante con business value |
| Spike | esperimento tecnico time-boxed per ridurre un'incertezza prima di impegnarsi |
| UAT | User Acceptance Testing: la validazione finale fatta dagli utenti reali; da noi 10 tester della community |
| Installazione (4 approcci) | phased (a fasi), by business unit, cut-over (sostituzione secca), parallel (vecchio+nuovo insieme); da noi consegna Docker con deploy al cliente |
| Post-implementation audit | obiettivi? vincoli? soddisfazione? business value concretizzato? lezioni sulla metodologia? |
| FTE | Full-Time Equivalent: 1 = una persona a tempo pieno; il nostro team: 5 persone × ≈50% ≈ 2,1 FTE medi effettivi |

---

**Ultimo aggiornamento**: 2026-08-11 — aggiunte C13 (granularità WBS) e riga 8/80; C1/D1 allineate a doppia lettura e RASCI a 51 righe; tilde→≈. Aggiornamento precedente: 2026-08-09 — versione didattica (risposte autosufficienti: termini e acronimi spiegati in ogni risposta); allineata allo stato post-audit degli allegati.
