# FAQ Orale — Domande previste e risposte (MaraffaOnline)

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Domande che il professore può plausibilmente fare sull'elaborato, con la risposta "modello": terminologia del corso (dispense/knowledge_base) + numeri del progetto. Le risposte sono volutamente compatte: sono la traccia da espandere a voce.
> Documenti gemelli: `PREPARAZIONE-ORALE.md` (numeri e casi speciali) e `SCELTE-DI-PROGETTO.md` (il perché di ogni scelta).

---

## A. Inquadramento generale

**A1. Mi presenti il progetto in due minuti.**
MaraffaOnline è una piattaforma web multiplayer per la Maraffa romagnola, sviluppata da PlayHeritage Labs (spin-off UniBo di Cesena, cultural heritage gaming) per la community "Maraffa Forever" (~150 ex studenti dispersi per l'Italia/Europa, €25.000 di crowdfunding interno). Problema sociale e geografico: le app esistenti sono obsolete o single-player, la dimensione conviviale si è persa. 7 mesi (15/10/2025–15/05/2026), team di 5 part-time, contratto a corpo in 3 tranche. La cifra gestionale è l'**approccio ibrido**: 7 sottosistemi loosely coupled, a ciascuno il ciclo di vita PMLC più adatto, sincronizzati da una cadenza comune bi-settimanale. Chiusura on time e on budget: €22.750 su €25.000, CPI=SPI≈1, tutti i criteri delle Conditions of Satisfaction rispettati.

**A2. Perché questo è un "progetto" e non un'attività operativa?**
Per il PMBOK un progetto è un'iniziativa **temporanea** (inizio e fine definiti) che crea un risultato **unico**; per Wysocki (v2) è una sequenza finita di attività dipendenti il cui completamento fornisce il **business value atteso**. MaraffaOnline ha inizio/fine contrattuali, un deliverable unico (l'MVP) e un business value definito dal committente (rigiocare insieme a distanza); non è ripetitivo né segue procedure esistenti.

**A3. Qual è la scelta di Project Management più importante dell'elaborato?**
L'approccio ibrido per sottosistema (Allegato 2.10): la scelta del modello PMLC guidata dal **quadrante goal/solution di Wysocki** — Waterfall dove requisiti e soluzione sono chiari (Game Engine), Iterativo dove serve feedback (Backend/Frontend), Adattivo dove la soluzione è incerta (Real-Time), Incrementale dove il valore è rilasciabile a incrementi (Social, Infrastructure). Il costo è la sincronizzazione, gestito con cadenza comune, demo del venerdì, milestone di integrazione mensili e settimane 4/8/12 di sola integrazione.

**A4. In quale quadrante di Wysocki cade il progetto?**
Il progetto nel suo insieme ha **goal chiaro**; la **soluzione è chiara solo in parte** — per questo non un modello unico ma la scomposizione: Game Engine in TPM (goal e solution chiari → Linear), Real-Time in APM (solution non chiara → Adaptive), Backend/Frontend APM Iterative, Social/Infrastructure TPM Incremental. Il corso dice che all'aumentare dell'incertezza aumentano iterazioni, pianificazione just-in-time, risk management e coinvolgimento del cliente: è esattamente il gradiente tra i nostri sottosistemi.

**A5. Cosa fareste diversamente (lessons learned)?**
Cinque, tutte agganciate a strumenti: prototipare le UI complesse già in fase di stima (le animazioni da 8 SP erano sottostimate); tenere i domain expert nel loop anche durante lo sviluppo (caso Maraffa Should→Must a novembre); anticipare il cross-browser testing ai primi sprint con interfaccia, gli Sprint 5–6 (Safari costò 2 giorni allo Sprint 12); daily asincrono strutturato (Slackbot dallo Sprint 7); refactoring continuo 10–15% per sprint invece dello sprint di cleanup (Sprint 10).

---

## B. Scoping

**B1. Cos'è il POS e cosa contiene il vostro?**
Il Project Overview Statement è la descrizione sintetica del progetto per il **senior management** (idealmente una pagina), con 5 sezioni: Problem/Opportunity, Goal, Objectives, Success Criteria, Assumptions-Risks-Obstacles. Non è un contratto. Il nostro ha 6 obiettivi numerati con **tracciabilità 1:1**: ogni criterio di successo e ogni gruppo di rischi porta il numero dell'obiettivo — così l'audit finale (Cap. 6) verifica obiettivo per obiettivo.

**B2. Differenza tra goal e obiettivi? I vostri sono S.M.A.R.T.?**
Il goal è 1–2 frasi che circoscrivono l'ambito ("scoping statement"); gli obiettivi sono 5–6 statement necessari e sufficienti che definiscono incluso/escluso. S.M.A.R.T. (Doran): Specific, Measurable, Assignable, Realistic, Time-related. I nostri 6 obiettivi hanno criteri quantitativi (latenza ≤500ms, 100 partite simultanee, ≥4,2/5, 15/05/2026, €25.000±5%), responsabili (RASCI) e scadenze: sì.

**B3. Cosa sono le Conditions of Satisfaction e come le avete costruite?**
Sono le condizioni negoziate tra requestor e provider che guidano requisiti e decisioni per tutto il ciclo di vita; il ciclo del corso è **Request → Clarify Request → Response → Agree on Response**. Le nostre: 22 condizioni in 5 tipologie (temporale, economica, tecnica, qualitativa, gestione del lavoro), negoziate con Giovanni Marchetti e tutte con soglie misurabili. Differenza dagli acceptance criteria: le CoS dicono **cosa** deve essere il risultato (dal committente/PO); gli acceptance criteria dicono **come verificare** che sia accettabile (dal team, per singola storia).

**B4. Differenza tra assunzione, rischio e ostacolo (sezione 5 del POS)?**
Assunzione = condizione data per vera su cui il piano si fonda (es. "regole documentate entro il 25/09", "pagamenti puntuali"); rischio = evento incerto con probabilità e impatto, gestito con la matrice (es. inesperienza WebSocket); ostacolo = difficoltà nota da superare (es. €714/mese/persona, coordinamento di tester distribuiti). Se un'assunzione cade, spesso diventa un rischio materializzato.

**B5. Come avete valutato i rischi? Perché il budget è "Accept" e non mitigato?**
Matrice qualitativa P×I: probabilità in 4 range (A–D) × impatto in 4 livelli (Trascurabile→Disastroso), valore 1–16, scala colori a 5 livelli. 20 rischi: 2 critici (16), 6 rossi, 7 arancioni, 5 gialli. Strategie del corso: Accept, Avoid, Mitigate, Contingency, Transfer. Il budget (16) è **Accept** perché non è mitigabile (il crowdfunding è quello) né trasferibile: lo si accetta consapevolmente — deciso formalmente nel meeting di approvazione — compensandolo col modello part-time e col valore strategico del pilota per lo spin-off.

**B6. Differenza tra Mitigate e Contingency? Perché sul WebSocket avete scelto la contingency?**
Mitigate = agire **subito** per ridurre probabilità/impatto; Contingency = pianificare **cosa fare se** l'evento si verifica. Sull'inesperienza WebSocket non si può "mitigare" un'incognita di fattibilità: si riduce l'incertezza con uno **spike time-boxed** e si prepara il piano B — go/no-go al giorno 15 che attiva il consulente esterno (Dr. Nardi, €2.000 accantonati), escalation al committente al giorno 30. Poi il PoC dello Sprint 2 (latenza 180ms) ha dimezzato il rating (16→8) e il load test dello Sprint 6 lo ha chiuso "Mitigato".

**B7. A cosa serve un Business Model Canvas in un progetto non-profit?**
A verificare che il modello regga: chi crea, distribuisce e cattura il valore (9 blocchi di Osterwalder). Il valore qui è duale: per la community (riconnessione sociale, fedeltà alle regole) e per PlayHeritage (validazione del modello, portfolio, pubblicazioni). La cattura economica attuale è il crowdfunding (25k in 3 tranche); i ricavi futuri (manutenzione, licensing, freemium) sono dichiarati come visione. Il cash flow contiene anche una **break-even analysis onesta**: il freemium non copre i costi → progetto non-profit per la community, e lo scriviamo.

**B8. SWOT e Risk Analysis non sono ridondanti?**
No: la SWOT classifica **fattori** interni (S/W, controllabili) ed esterni (O/T), la Risk Analysis valuta **eventi** con probabilità e impatto. Sono collegate esplicitamente (W1 = rischio 2.1, W4 = 6.4, T2 = 6.2) e la nostra SWOT va oltre la descrizione: **matrice incrociata TOWS** con strategie SO/WO/ST/WT e 4 azioni immediate (pre-allerta consulente, governance decisionale, meeting GDPR, accordo di commitment).

**B9. PoC, prototipo e MVP nel vostro progetto?**
PoC = verifica di fattibilità tecnica → lo **spike Socket.IO** dello Sprint 2 (4 client, latenza 180ms). Prototipo = mostra aspetto/uso per correggere → i **mockup Figma v1→v2** (v1 commentata dalla community, v2 approvata e vincolante). MVP = prima versione funzionante che dà business value → la **release del 15 maggio**. Tre strumenti, tre incertezze diverse: tecnica, di design, di valore.

**B10. Come sono fatte le vostre user stories? Cos'è INVEST?**
23 storie in 7 epiche, formato Connextra ("Come… voglio… così da…") con criteri di accettazione puntuali e approccio di test. INVEST (Wake): Independent, Negotiable, Valuable, Estimable, Small, Testable — verificato in tabella criterio per criterio. Scelta di pulizia: nel 2.9 **non** ci sono story points, priorità né sprint — quelli appartengono al Planning (MoSCoW 3.2 e Product Backlog 3.3): separazione tra "cosa" e "quanto/quando".

**B11. Differenza RBS/WBS?**
La RBS è la gerarchia dei **requisiti** (Requirement→Function→Sub-function→Feature), deliverables-based, intuitiva per il committente; la WBS è la gerarchia del **lavoro** necessario a soddisfarli. Nel processo di Wysocki la completezza della RBS è il fattore principale nella scelta del modello PMLC — da noi: RBS del Game Engine completa e stabile → Waterfall; RBS del Real-Time incerta → Adattivo.

**B12. Perché Waterfall sul Game Engine, nel 2026, per del software?**
Perché è il caso da manuale TPM: goal e solution chiari. Le regole sono fisse da decenni, documentate e **validate formalmente dall'esperta prima dello sviluppo**; i test case si scrivono a monte da partite a risultato noto; il feedback iterativo degli utenti non aggiunge nulla (le regole le conoscono già). Il rischio classico del waterfall — requisiti che cambiano tardi — qui è improbabile per costruzione. Usare Scrum sul Game Engine sarebbe overhead senza beneficio.

**B13. Perché non avete considerato il modello Extreme?**
Il quadrante xPM richiede goal **e** solution entrambi non chiari (R&S, esplorazione). Da noi il goal è sempre chiaro; l'incertezza massima (Real-Time) riguarda solo la soluzione → Adattivo, non Extreme. MPx (solution chiara, goal non chiaro) nemmeno si applica.

---

## C. Planning

**C1. Come sapete che la vostra WBS è completa?**
Con la **100% rule** (dichiarata): la WBS copre tutto il lavoro, inclusa la sezione trasversale di PM/documentazione/QA. Il corso dà anche i **6 test di completezza** di Wysocki per il singolo task: stato/completamento misurabili, inizio-fine ben delimitati, deliverable associato, tempi/costi stimabili, durata accettabile, indipendenza. I nostri 160 task a 4 livelli (Sottosistema→Funzione→Attività→Task) li rispettano; abbiamo semplificato i 6 livelli canonici in 4 perché il livello Goal/Objective è già assorbito dalla struttura per sottosistemi della RBS.

**C2. 302 giorni-uomo di stima ma 141 giorni di progetto: come si conciliano?**
Sono grandezze diverse: 302 giorni-uomo è l'**effort** aggregato (dal MoSCoW), 141 giorni lavorativi è la **duration** (dal CPM). Il corso insiste sulla relazione non lineare effort/durata. Con 5 persone part-time in parallelo su 6 sottosistemi: 302/141 ≈ 2,1 FTE medi, coerente con un team di 5 al ~50%.

**C3. Mi spieghi il Critical Path Method sul vostro network.**
20 attività AON con dipendenze FS (una SS+lag). **Forward pass** da sinistra (ES/EF), **backward pass** da destra (LS/LF), **slack = LS−ES**; il percorso a slack zero è il critical path: **A→B→D→G→J→M→P→R→S→T = 141 giorni lavorativi**, esattamente i giorni disponibili dal 15/10 all'08/05 festività escluse — restano 5 giorni lavorativi di margine sul lancio del 15/05. Rami non critici: Game Engine (C-F-I-L-O) float 22 gg, Chat/Social (E-H-K-N-Q) float 37 gg. L'attività più critica è P (Frontend Tavolo, 40 gg).

**C4. Fast tracking e crashing: differenza, e dove li avete usati?**
Entrambe comprimono la schedula: il **fast tracking** parallelizza attività sequenziali (es. trasformare FS in SS), il **crashing** aggiunge risorse a pagamento. Fast tracking usato davvero: **P→R Start-to-Start + lag 31** — il Testing E2E parte quando il Frontend Tavolo ha completato 31 giorni su 40, testando i moduli congelati. "La compressione non è mai gratis": il rischio di rework è dichiarato e mitigato (sequenziamento moduli, suite Cypress rieseguibile). Crashing previsto solo come leva di sensitivity: se P ritarda 10 gg, +1 contractor esterno part-time ≈ €2.000 (coperto dal Contingency Buffer).

**C5. Il corso dice "Do not plan to use slack to bail out the project". Ma il vostro primo livello di escalation è proprio lo slack: contraddizione?**
No: il monito vieta di **pianificare** contando sullo slack (schedulare già consumandolo). Noi lo usiamo a **consuntivo**, come primo assorbitore quando uno scostamento si è già verificato — è il livello 1 della Problem Escalation Strategy del corso (PM-based → resource-based → client-based). La baseline non assume mai il consumo del float.

**C6. Perché i Must Have sono al 75,8% se DSDM raccomanda ~60%?**
Scelta deliberata e documentata: Game Engine e Real-Time sono il core differentiator — senza regole fedeli e partite fluide il prodotto non esiste. In compenso i Could sono compressi al 5,3% (contro ~20%) in funzione anti-scope-creep. Il rovescio (meno margine di de-scoping) è compensato da contingency di budget 18,7%, float dei rami non critici e Won't Have espliciti già negoziati.

**C7. Come avete stimato? Perché due tecniche?**
**Delphi** per il Game Engine (Waterfall): stime individuali **anonime** con motivazione, più round fino a convergenza — adatta a requisiti stabili, evita l'ancoraggio. **Planning Poker** per l'Agile: carte Fibonacci (1–21) scelte in modo indipendente, discussione delle discrepanze, ripetizione fino al consenso. Stessa filosofia consensus-based, strumento calibrato sul contesto. Il corso cita anche il three-point (E=(O+4M+P)/6): non l'abbiamo usato, ma so descriverlo.

**C8. Cosa sono gli story points? 310 SP su 15 sprint fanno ~21 a sprint, ma dichiarate capacity 40: non torna.**
Gli SP misurano la complessità relativa, non il tempo (adimensionali, scala Fibonacci). La chiave è **capacità vs carico**: 40 SP/sprint è la **capacity team-wide**, che include il lavoro di Game Engine e Infrastructure stimato in punti equivalenti (~131 SP; totale progetto ~441). Il **carico medio pianificato** è ~37 team-wide (441 su Sprint 0–11) e ~28 di solo Backlog (310 su Sprint 1–11): il margine assorbe festività e variabilità. Velocity misurata: 38,3 — coerente con la capacity. Due letture dichiarate: metrica gestionale consolidata per lo sponsor, carico Scrum per il team.

**C9. E lo sprint di Natale?**
Sprint 5 (22/12–2/1) pianificato a capacità ridotta: 21 SP completati su 40 (52,5%), carryover di 19 riassorbito nei due sprint successivi. La media di 38,3 lo **esclude** dichiaratamente perché non rappresentativo del regime: onestà metodologica, non un trucco.

**C10. Come funziona il vostro cash flow? Perché l'outflow decresce alla fine?**
Inflow in 3 tranche (12.500/6.250/6.250 a ott/dic/feb); l'ultimo incasso è a metà progetto, quindi la coda (mar–mag) vive del saldo cumulato → l'outflow scende nei mesi 5–7 (team ridotto su testing/UAT/lancio). Saldo cumulativo **sempre positivo, minimo €2.250** all'ultimo mese. Il corso distingue l'utile (differenza a fine progetto) dalla **gestione del cash flow** (evoluzione nel tempo: si può essere in utile e restare senza cassa): il piano è costruito proprio su quel principio. Contingency €4.664 (18,7%) distribuita mensilmente + surplus finale €2.250 (9%).

**C11. Contratto a corpo con sottosistemi adattivi: il corso non suggerisce il time & materials quando le stime sono incerte?**
Sì, ma qui il vincolo dominante è il **budget fisso del committente** (crowdfunding): il fixed-price era l'unica forma accettabile per la community. Il rischio di stima che il corpo scarica sul fornitore è gestito **dentro** il progetto: MoSCoW con Could sacrificabili, contingency 18,7%, spike early sul rischio tecnico maggiore, e Won't Have negoziati che delimitano lo scope. È una risposta di risk management alla rigidità contrattuale.

**C12. A cosa serve il Gantt se avete già il network diagram?**
Il network modella le **dipendenze logiche** e serve a calcolare schedula, critical path e float (analisi what-if); il Gantt traduce tutto in **calendario** con barre e milestone ed è lo strumento di monitoraggio e comunicazione (nel Cap. 5: today line, % completamento, barre rosse sul ritardo di gennaio). Workflow dichiarato: prima il network, poi il Gantt; se c'è un major change si ricalcola il network.

---

## D. Launching

**D1. Cos'è la RASCI e come l'avete applicata?**
Responsibility Assignment Matrix: **R**esponsible esegue, **A**ccountable approva e risponde del risultato (**uno solo per attività** — "se ci sono troppi Accountable nessuno è responsabile"), **S**upport aiuta, **C**onsulted è sentito (bidirezionale), **I**nformed è aggiornato (unidirezionale). Otto matrici (una per sottosistema + QA + PM). Accountability ripartita per natura: tecnica a Elena, cerimonie/coordinamento a Marco, business e milestone a Giovanni; sulla UAT i ruoli si ribaltano (A = sponsor, R = Giuliani).

**D2. Elena è Accountable e Responsible sul Game Engine: non è un conflitto?**
È una sovrapposizione **dichiarata e motivata**: è la specialista che implementa il sottosistema, in un team di 5 la separazione totale sarebbe artificiosa. I contrappesi ci sono: supporto di Sara, code review obbligatoria, e soprattutto la **validazione esterna delle regole** (Francesca Giuliani), che è il vero controllo di qualità del Game Engine.

**D3. Che stile decisionale avete adottato?**
Il corso distingue directive, participative/collaborative e **consultative**: abbiamo scelto il consultivo — decide chi ha l'autorità dopo aver raccolto input — articolato su **3 livelli**: operativo (decide il Responsible), tattico (Tech Lead + PM, sentito il team, documentato), strategico (Sponsor, su **Project Impact Statement** preparato dal PM). Regola d'oro: decidere al livello più basso possibile — rapidità, decisioni prese da chi ha le informazioni, niente colli di bottiglia.

**D4. Come gestite i conflitti?**
Tre tipologie, tre decisori (tecnici → Elena su criteri oggettivi, poi *disagree and commit*; priorità → Marco con MoSCoW e critical path; interpersonali → Marco facilitatore) e **tre fasi progressive**: confronto diretto → mediazione facilitata → decisione esecutiva. Nel progetto nessun conflitto ha superato la fase 2. Il modello teorico del corso (Thomas-Kilmann) ha 5 stili: competing, collaborating, compromising, avoiding, accommodating — il nostro processo istituzionalizza il collaborating con fallback esecutivo.

**D5. Come gestite una richiesta di cambiamento?**
Processo formale in 5 passi: submission (Change Request Form) → **impact analysis** con Project Impact Statement (scope/tempi/budget/qualità/risorse + 3 opzioni e raccomandazione del PM) → decisione dello sponsor → implementazione (aggiornando POS, WBS, Gantt, Backlog) → tracking nel Change Log. Doppio regime coerente con l'ibrido: i sottosistemi Agile accolgono il cambiamento nel processo (backlog reprioritizzato), i tradizionali valutano caso per caso. Nel progetto: scope creep mai materializzato; Giovanni ha accettato di posticipare alcune nice-to-have alla 1.1.

**D6. Perché il kick-off dura solo un'ora?**
Perché i materiali (POS, WBS, Gantt, Cash Flow, bozze RASCI/regole) sono stati pre-condivisi il venerdì precedente (10 ottobre): il meeting serve a decidere e allineare, non a presentare. Ne escono 5 decisioni formali e 7 action item con owner e scadenza su Notion. È coerente con la nostra regola "asynchronous-first".

---

## E. Monitoring & Control

**E1. Mi scriva e commenti le formule dell'Earned Value.**
PV = valore pianificato del lavoro previsto a una data; EV = valore del lavoro **effettivamente completato** (misurato col budget di quel lavoro); AC = costo effettivo sostenuto. **CV = EV−AC** (negativa: spendo più del valore prodotto); **SV = EV−PV** (negativa: in ritardo); **CPI = EV/AC**; **SPI = EV/PV** (soglia 1). Nel progetto, a gennaio 2026: PV 14.100, EV 13.200, AC 13.500 → CV = −€300, SV = −€900, CPI 0,98, SPI 0,94 (i 3 giorni di ritardo della Dashboard). A chiusura: CPI = SPI = 1,00 su €22.750. Scelta metodologica: **l'EV matura solo sulle feature accettate dallo sponsor in Sprint Review** (Done secondo DoD) — niente autocertificazione del progresso.

**E2. Cos'è uno Stoplight Report? E gli altri tipi di report del corso?**
Variante a semaforo applicabile agli altri report: verde = "progressing according to plan"; giallo = "problema, Get Well plan in atto, la situazione rientrerà"; rosso = "failing, serve intervento". Il nostro è settimanale su 5 aree (Scope, Schedule, Budget, Quality, Risks) con nota motivante. Il corso elenca 5 tipi: current period, cumulative (trend), exception (per il senior management), stoplight, variance (pianificato vs effettivo) — noi usiamo stoplight settimanale, EVM mensile (cumulative/variance) e il Gantt tracking come status report visuale.

**E3. Cosa è successo a gennaio e come l'avete gestito?**
L'attività M (Frontend Dashboard e Creazione Stanza, **sul critical path**) accumula 3 giorni di ritardo per la complessità del flusso stanza/inviti. Il ritardo è visibile su tre strumenti coerenti: Stoplight (Schedule giallo), Gantt tracking (60% vs 80% atteso), EVM (SV −€900, SPI 0,94). Intervento con scala graduata: l'attività è critica quindi lo slack non c'è → strategia PM-based: **recovery plan con pair programming Luca+Sara** (riallocazione interna, non crashing a pagamento) → recupero completo entro febbraio, milestone invariate. Il caso dimostra l'early warning del monitoraggio multilivello.

**E4. Come avete monitorato i rischi dopo lo Scoping?**
I rischi non sono statici: **Risk Log** su Notion con stati (Aperto / In Mitigation / Mitigato / Materializzato), probabilità e impatto **rivalutati** a ogni Project Status Meeting. Caso guida: WebSocket 16 → spike+PoC Sprint 2 (180ms) → 8 → chiuso Mitigato dopo il load test Sprint 6 (100 partite/400 giocatori). Lo scope creep non si è mai materializzato (POS chiaro + CR process rigoroso).

**E5. La vostra escalation è a 3 livelli; il corso ha una gerarchia più fine. La conosce?**
Sì, 7 passi: usare gli slack → esaminare le dipendenze FS (compressione) → riassegnare risorse da task non critici → negoziare risorse aggiuntive (resource manager) → rilasci multipli → estensione della schedula → modifica dello scope. I nostri 3 livelli (slack-based → PM-based → client-based) sono la stessa gerarchia raggruppata per "chi possiede la leva": PM, risorse, cliente.

**E6. Perché monitorate la velocity se metà progetto non è Scrum?**
Per dare allo sponsor **una** vista consolidata: la capacity 40 e la velocity sono metriche team-wide che aggregano Backlog + punti equivalenti di GE/Infrastructure. È dichiarato esplicitamente nel Cap. 5 (nota metodologica): non è velocity Scrum pura, è una metrica gestionale; il carico Scrum vero è ~28 SP/sprint. Se il professore chiede "si possono sommare punti Waterfall?": si può, purché si dichiari che è una convenzione di reporting — ed è dichiarato.

---

## F. Closing

**F1. I passi del Closing secondo il corso, e nel vostro progetto?**
(1) Accettazione formale del deliverable → firma di Giovanni lunedì 11/05 dopo aver **giocato personalmente una partita**; (2) installazione → deploy a carico della community (dichiarato dall'inizio; consegnate Docker image + istruzioni + supporto remoto); (3) documentazione completa → Notion + allegati; (4) Final Project Report firmato → consegnato il 12/05, 9 sezioni; (5) **post-implementation audit** → 13/05 con lo sponsor, criterio per criterio sulle CoS; (6) **celebrazione** → 15/05, a budget (€100).

**F2. Cosa verifica l'audit post-implementazione? Esito?**
Le domande canoniche: obiettivi raggiunti? tempi/budget/specifiche rispettati? committente soddisfatto? business value concretizzato? cosa si è imparato su metodologia e processo? Esito: 7 mesi rispettati (unico ritardo, 3 gg a gennaio, recuperato), €22.750 su €25.000, latenza media 185ms, 80% utenti autonomi alla prima partita, beta tester 4,5/5 (target 4,2), zero errori di regole segnalati. Il corso nota che spesso l'audit non si fa (nessuno vuole pagarlo/saperlo): noi lo abbiamo fatto e documentato.

**F3. Il criterio "80 utenti attivi nei primi 2 mesi" come può dirsi soddisfatto alla chiusura del 15/05?**
Non può, alla lettera: è un criterio post-lancio. Risposta onesta: alla chiusura è **in traiettoria** (prime 24h: 50 registrati, 23 partite complete, contro attese di 20–30 nella prima settimana) e resta in monitoraggio post-lancio a carico della community, con il supporto finanziato dal surplus. Il Closing dichiara soddisfatti i criteri verificabili alla data.

---

## G. Domande scomode (incoerenze note) — risposte pronte

**G1. La UAT è ad aprile (Gantt, M6 24/04) o a maggio (Cap. 5/6: 1–10/05)?**
Lettura difendibile: la **UAT formale** è quella di aprile come da piano (attività S, milestone M6 = approvazione); a inizio maggio c'è una **sessione finale di validazione pre-lancio** con i 10 tester, che il racconto del Closing chiama impropriamente "UAT ufficiale". Da uniformare; il piano resta coerente.

**G2. La tranche del 15/12 è "a valle del Backend Core", ma M2 cade il 19/12.**
Sfasatura di 4 giorni: il pagamento era contrattualmente a data fissa (15/12), la milestone di review formale è il 19/12; il Backend Core (attività D e G) era di fatto completato prima della data di pagamento. Rilievo minore, da correggere allineando la data o la formulazione contrattuale.

**G3. Il POS assume "team dedicato full-time", ma ovunque si parla di part-time 50%.**
Refuso del POS: l'assunzione corretta è "team **dedicato per l'intera durata** del progetto" (nessun distoglimento su altri progetti — infatti MaraffaOnline ha priorità di allocazione), con impegno ~50% FTE. Lo dimostrano i numeri: 302 giorni-uomo / 141 giorni ≈ 2,1 FTE. Da correggere nel testo.

**G4. Il decision point del rischio WebSocket è al giorno 15 o al giorno 30?**
La versione operativa (Allegato 2.10, il documento di dettaglio) è: **giorno 15 go/no-go dello spike** → si attiva il consulente; **giorno 30 escalation al committente** se nemmeno col consulente si hanno risultati. Risk Analysis e SWOT citano solo il secondo punto ("decision point giorno 30"). Non sono tre piani diversi ma due checkpoint dello stesso piano; la formulazione è stata armonizzata in tutti gli allegati (Risk 2.4, SWOT W1/T1, 2.10).

**G5. (Se scoperto) Nelle user stories, US-3.1 dice "primo giocatore casuale" e US-3.6 descrive la Maraffa come "3 carte dello stesso seme": non sono le regole sbagliate?**
Erano due refusi dell'Allegato 2.9, individuati con un audit interno e **corretti** (insieme al punteggio d'esempio "41-38", impossibile con il sistema a 11 punti per smazzata, ora "41-36"): le fonti normative — RBS 1.1.2/1.1.5 e il documento delle regole validato da Giuliani — hanno sempre detto correttamente che inizia e sceglie la briscola **chi ha il 4 di denari**, e che la Maraffa è **Asso+2+3 del seme di briscola**. La catena di sicurezza del progetto è proprio questa: la specifica validata dall'esperta è la fonte di verità, e infatti in beta risultano zero segnalazioni di errori sulle regole.

**G6. €16.000 di salari per 5 persone per 7 mesi: sono realistici?**
In valori di mercato no, e non pretendono di esserlo: è un progetto **non-profit su crowdfunding**, con team part-time ~50% di uno spin-off universitario che valorizza il pilota (portfolio, pubblicazioni, tesi di dottorato del PM). La SWOT lo dichiara apertamente come debolezza (W2: €714/mese vs €2.500–3.000 di mercato) e il rischio budget è formalmente **accettato** dallo sponsor e dal team nel meeting di approvazione. La compensazione è strategica, non monetaria.

**G7. Lo Sprint 6 carica 47 SP di solo Backlog con capacity dichiarata 40: come lo spiegate?**
La capacity è team-wide e **media**: 37 SP pianificati di media con margine sul 40. Nei singoli sprint il carico oscilla (S6=47, ma S2=13, S3=16): i picchi sono compensati dagli sprint leggeri adiacenti e dal carryover fisiologico dello Sprint 5. A consuntivo la velocity di S6 è stata 39/40: il piano ha retto. Rilievo legittimo: un load balancing più uniforme sarebbe stato più pulito.

**G8. Nel Cap. 5 leggo "spese €17.500 su €17.800 pianificate: scostamento favorevole". In EVM confrontare AC con PV non misura l'efficienza. Concorda?**
Concordo: AC < PV da solo può voler dire semplicemente "in ritardo". La misura corretta è CV = EV−AC: a febbraio EV = 17.300, AC = 17.500 → CV = −€200, leggermente sfavorevole ma entro il buffer, con recupero completo nei mesi successivi (CV = 0 a chiusura). La frase del capitolo usa "favorevole" nel senso di cassa/spesa rispetto al piano, non di cost efficiency — formulazione da sistemare. *(Sapere anche: il saldo di cassa citato a gennaio, €4.650, è calcolato sull'outflow pianificato; su quello effettivo sarebbe €5.250.)*

**G9. Contingency 18,7% ma surplus 9%: quale dei due è la riserva?**
Sono due cose diverse, entrambe nel Cash Flow (3.4): la **contingency €4.664 (18,7%)** è distribuita nelle uscite mensili come buffer operativo per imprevisti e change request (e in parte è stata effettivamente consumata: ore extra sul Real-Time); il **surplus €2.250 (9%)** è ciò che resta a fine progetto, destinato al supporto post-lancio. Insieme formavano il margine di sicurezza iniziale (~27,7%).

**G10. La riclassificazione della Maraffa (Should→Must) è passata dal vostro Change Request Process?**
Nella sostanza sì: emersa nella Sessione 1 di validazione (novembre), valutata con l'esperta e il PM, **compensata riducendo Could Have** (impatto zero su tempi/budget) e approvata con lo sponsor; la traccia documentale è la nota di revisione nella MoSCoW. Nella forma, un CR numerato con Project Impact Statement sarebbe stato più rigoroso: è una delle cose che formalizzeremmo meglio — coerente con la lesson learned sul coinvolgimento continuo dei domain expert.

**G11. Perché non avete usato MS Project?**
Scelta di strumenti dichiarata: **Notion** (board, database, single source of truth, import CSV del Gantt), **Figma/Miro** (design), **GitLab CI** (delivery), **Excel/HTML** per grafici e viste a colori, più uno script Python che genera il Network+Gantt HTML dalle tabelle — tutto low-cost, coerente col budget e replicabile. Il valore didattico richiesto ("uso di strumenti software") è dimostrato dagli artefatti CPM/Gantt/EVM prodotti e mantenuti coerenti, non dalla licenza usata.

**G12. Chi è "Luca Bianchi" che firma la revisione della WBS?**
Refuso di battitura (fusione di Luca Moretti e Sara Bianchi), individuato in audit interno e **corretto**: il revisore tecnico è la Tech Lead **Elena Rossi**.

**G13. Perché lo sforzo del Game Engine nel MoSCoW è 50 giorni ma la catena C-F-I-L-O del network dura 73 giorni?**
Perché misurano cose diverse: i 50 giorni MoSCoW sono l'**effort dei requisiti** del sottosistema; la catena del network include anche **GE Testing (L, 15 gg) e Integration Testing (O, 10 gg)**, che nel MoSCoW stanno nel QA trasversale, e le durate del network sono *elapsed* con risorse part-time. Il raccordo effort→durata passa per lo staffing, non è 1:1.

**G14. Il critical path finisce l'8 maggio ma il lancio è il 15: allora un ritardo sul critical path non "impatta direttamente il lancio".**
Il percorso critico determina la data di **consegna** (fine T, preparazione lancio): l'8/05. La settimana 8–15/05 è il margine di progetto che ospita accettazione (10/05), report (12/05) e audit (13/05): non è slack di attività, è **management reserve** di calendario. Un ritardo sul CP consuma prima quel margine e poi sposta il lancio: per questo i 3 giorni di gennaio andavano recuperati subito.

---

## H. Definizioni-lampo (ripasso finale)

| Termine | Risposta in una frase (terminologia del corso) |
|---|---|
| Progetto (PMBOK) | iniziativa **temporanea** per creare un risultato **unico**; temporaneo = inizio e fine definiti |
| Progetto (Wysocki v2) | sequenza finita di attività dipendenti che fornisce il **business value atteso** |
| Programma vs Portfolio | progetti **interdipendenti** coordinati vs raggruppati solo per **facilitare la gestione** |
| Scope Triangle | tempo, costi, risorse ai lati; **scope e qualità al centro**; usato per Project Impact Statement ed escalation |
| I 4 creep | scope (cambiamento dal piano), hope (ritardo nascosto), effort (lavoro senza progresso), feature (aggiunte non concordate) |
| IRACIS | Increased Revenue, Avoided Cost, Improved Service — le 3 componenti misurabili del business value |
| S.M.A.R.T. | Specific, Measurable, Assignable, Realistic, Time-related (Doran) |
| CoS | condizioni negoziate richiesta/risposta che guidano requisiti e decisioni; da noi 21 in 5 tipologie |
| POS | 1 pagina per il senior management: problema/opportunità, goal, obiettivi, criteri, assunzioni-rischi-ostacoli |
| RBS vs WBS | gerarchia dei requisiti vs gerarchia del lavoro; la completezza della RBS guida la scelta del PMLC |
| 100% rule | la WBS copre il 100% del lavoro, incluso il project management stesso |
| MoSCoW | Must/Should/Could/Won't; da noi 75,8/18,9/5,3 su 302 gg-uomo, motivato |
| INVEST | Independent, Negotiable, Valuable, Estimable, Small, Testable |
| DoD vs Acceptance Criteria | a inizio progetto, per tutte le storie / per singola storia, a inizio iterazione |
| Delphi | stime anonime con motivazione, round fino a convergenza (Project RAND) |
| Planning Poker | carte Fibonacci indipendenti, discussione discrepanze, fino al consenso |
| Effort vs Duration | relazione non lineare; corso: Labor = 0,75 × Duration; da noi 302 gg-uomo vs 141 gg |
| Forward/Backward pass | EF = ES + durata − 1; LS = LF − durata + 1 (convenzione del corso); slack = LS−ES = LF−EF |
| Critical path | catena a slack zero che determina la durata: A→B→D→G→J→M→P→R→S→T = 141 gg |
| Total vs Free slack | ritardo senza impatto sul progetto vs sul task successivo |
| SS + lag | Start-to-Start con ritardo: il nostro fast tracking P→R (lag 31) |
| Fast tracking vs Crashing | parallelizzare vs aggiungere risorse a costo; "la compressione non è mai gratis" |
| PV / EV / AC | pianificato / maturato sul lavoro fatto / costo effettivo |
| CV, SV, CPI, SPI | EV−AC; EV−PV; EV/AC; EV/PV — soglia 1; a chiusura entrambi 1,00 |
| Stoplight | verde "according to plan"; giallo "Get Well plan in place"; rosso "intervention required" |
| RASCI | Responsible esegue, Accountable approva (**uno solo**), Support, Consulted, Informed |
| Project Impact Statement | documento del PM sull'impatto di un cambiamento (scope/tempi/costi/qualità/risorse) con opzioni |
| Scope Bank / riserva | 5–10% del tempo accantonato per i change; da noi contingency 18,7% sul budget |
| PMLC (5 modelli) | Linear, Incremental (TPM) — Iterative, Adaptive (APM) — Extreme (xPM); scelti col quadrante goal/solution |
| PoC / Prototipo / MVP | fattibilità tecnica / aspetto-uso per correzioni / prima versione con business value |
| Installazione (4 approcci) | phased, by business unit, cut-over, parallel — da noi consegna Docker con deploy al cliente |
| Post-implementation audit | obiettivi? vincoli? soddisfazione? business value? lezioni sulla metodologia? |

---

**Ultimo aggiornamento**: 2026-08-09 — creato a valle della rilettura integrale di relazione e allegati; allineato a PREPARAZIONE-ORALE.md e SCELTE-DI-PROGETTO.md §8 (nuovi rilievi).
