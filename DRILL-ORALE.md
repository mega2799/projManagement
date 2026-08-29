# Drill Orale — domande-lampo su MaraffaOnline

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Uso: leggi la domanda, rispondi **a voce** in una riga, poi confronta. Le risposte sono deliberatamente secche — l'approfondimento è in `FAQ.md` (riferimenti tra parentesi), i numeri completi in `PREPARAZIONE-ORALE.md` §3, il perché delle scelte in `SCELTE-DI-PROGETTO.md`. Tutti i valori sono quelli della versione consegnata (zip del 26/08/2026).
>
> Metodo consigliato: un blocco al giorno negli ultimi giorni; segna con ✗ le domande sbagliate e ripeti solo quelle il giorno dopo.

---

## 1. Il progetto in numeri

- **Durata?** → 7 mesi, 15/10/2025–15/05/2026; 146 giorni lavorativi disponibili, 141 fino all'8/05.
- **Budget e consuntivo?** → €25.000 / €22.750; surplus €2.250 (9%) destinato al supporto post-lancio.
- **Contratto?** → a corpo (prezzo fisso), 3 tranche 50/25/25: 15/10 firma, 15/12 Backend Core, 15/02 core di gioco.
- **Team?** → 5 persone part-time ≈50% FTE (≈2,1 FTE medi); Marco Venturi è CEO, PM e Product Owner; Elena Rossi Tech Lead e Scrum Master.
- **Sottosistemi?** → 7: Game Engine, Backend, Real-Time, Frontend, Mobile (Won't Have), Social & Community, Infrastructure & DevOps.
- **Effort stimato?** → 302 giorni-uomo: Must 75,8% / Should 18,9% / Could 5,3%.
- **Critical path?** → 141 giorni lavorativi: A→B→D→G→J→M→P→R→S→T; fine T = 8/05; margine di 5 giorni lavorativi sul lancio.
- **Fast tracking?** → legame P→R Start-to-Start + lag 31: il Testing E2E parte sulla coda del Frontend Tavolo.
- **Attività più critica?** → P, Frontend Tavolo da Gioco, 40 giorni (2/02–27/03).
- **Float dei rami non critici?** → Game Engine 22 giorni; Chat/Social 37 giorni.
- **Sprint?** → 15 (Sprint 0–14) da 2 settimane; sviluppo negli Sprint 0–10; 11–14 = testing E2E, UAT, lancio.
- **Product Backlog?** → 310 SP; lavoro totale ≈441 SP equivalenti (310 + ≈94 Game Engine + ≈37 Infrastructure).
- **Capacity, carico, velocity?** → capacità 40 SP/sprint team-wide; carico medio ≈37 team-wide e ≈28 di solo Backlog; velocity di regime 38,3 (Sprint 1–7, escluso il natalizio).
- **Sprint natalizio?** → Sprint 5, 22/12–2/01: 21 SP su 40 (52,5%), carryover 19 pianificato, escluso dalla media.
- **EVM a gennaio?** → PV 14.100, EV 13.200, AC 13.500 → CV −€300, SV −€900, CPI 0,98, SPI 0,94; recuperato entro febbraio.
- **EVM a fine progetto?** → CPI = SPI ≈ 1,00.
- **Latenza?** → 185 ms media ai load test con 100 partite simultanee (400 giocatori), target <500 ms; PoC di Sprint 2: 180 ms.
- **Qualità?** → coverage >85% (la DoD chiede >80%); UAT: 80% completa una partita senza aiuto; beta tester 4,5/5 (target 4,2).
- **Rischi?** → 20; 2 critici a rating 16 (WebSocket e budget); 6 rossi a 9–12, tra cui race conditions (12) e scope creep (12).
- **Milestone?** → M1 27/10 · M2 19/12 · M3 30/01 · M4 27/03 · M5 31/03 · M6 24/04 · M7 15/05 — tutte rispettate.
- **Retrospective?** → 15; 30 action item, 28 implementati.
- **Cassa?** → saldo cumulativo sempre positivo, minimo €2.250 al Mese 7; contingency €4.664 (18,7%).
- **Prime 24 ore dal lancio?** → 50 registrati e 23 partite complete (attese: 20-30 utenti nella prima settimana).

## 2. Scoping

- **Chi c'era allo Scoping Meeting?** → sponsor Giovanni Marchetti, esperta Francesca Giuliani, PM Marco Venturi e tutto il team; 15/09/2025, ibrido; solo narrato nella relazione, senza allegato (FAQ G15).
- **Ordine dei documenti di Scoping?** → CoS 18/09 → POS 19/09 → RBS e User Stories 26/09 → approvazione 2/10 (due giorni oltre il 30/09 previsto, entro il margine).
- **CoS: quante e di che tipo?** → 22 condizioni in 5 tipologie: temporale, economica, tecnica, qualitativa, gestione del lavoro (FAQ B3).
- **Ciclo delle CoS?** → Request → Clarify Request → Response → Agree on Response.
- **CoS vs acceptance criteria?** → le CoS dicono *cosa* deve essere il risultato (dal committente); gli AC dicono *come verificare* una storia (dal team).
- **POS: sezioni?** → problema/opportunità, goal, 6 obiettivi numerati, criteri di successo correlati 1:1 agli obiettivi, assunzioni-rischi-ostacoli; non è un contratto (FAQ B1).
- **S.M.A.R.T.?** → Specific, Measurable, Assignable, Realistic, Time-related (Doran) — i 6 obiettivi lo sono (FAQ B2).
- **Assunzione / rischio / ostacolo?** → condizione data per vera / evento incerto con probabilità e impatto / difficoltà nota e certa (es. budget per persona sotto mercato) (FAQ B4).
- **Matrice dei rischi?** → 4×4: probabilità A–D × impatto Trascurabile→Disastroso; valore P×I da 1 a 16; scala colori a 5 livelli (Rosso Critico = 16).
- **Le 5 strategie di risposta?** → Accept, Avoid, Mitigate, Contingency, Transfer.
- **Rischio WebSocket?** → 16, Contingency: spike di 2 settimane, go/no-go al giorno 15 → consulente Nardi (€2.000 accantonati), escalation al committente al giorno 30; PoC Sprint 2 → rating 8; chiuso come Mitigato dopo il load test di Sprint 6 (FAQ B6).
- **Rischio budget?** → 16, Accept: il crowdfunding è fisso, non mitigabile né trasferibile; compensato con il part-time e il valore strategico del pilota (FAQ B5).
- **Rischio varianti regionali (1.2)?** → Avoid: adottata in Scoping la versione ufficiale delle regole, che elimina la fonte del rischio.
- **Rischio autenticazione (4.2)?** → Mitigazione: librerie consolidate, HTTPS, penetration test — azioni immediate, non un piano di contingenza.
- **SWOT: cosa la distingue?** → estesa a matrice TOWS con 4 azioni immediate; incrocia i rischi (W1 = rischio 2.1, W4 = 6.4, T2 = 6.2) (FAQ B8).
- **BMC in un non-profit?** → per verificare che il modello regga; break-even onesto ≈84 mesi → progetto dichiaratamente non-profit (FAQ B7).
- **Prototyping?** → mockup Figma v1 commentata → v2 approvata e vincolante; workshop con 10 membri (Miro); Think Aloud con 8; click to play invece di drag & drop.
- **PoC / prototipo / MVP?** → spike Socket.IO a 180 ms / mockup Figma / release del 15/05 (FAQ B9).
- **RBS: livello di dettaglio?** → si ferma al requisito (dice *cosa*, non *come*); dettaglio nelle US, soglie nelle CoS, tecnologie nel Planning; gli ID REQ-* della MoSCoW codificano la numerazione della RBS (FAQ B11).
- **User stories?** → 23 in 7 epiche, INVEST verificato criterio per criterio; niente priorità né story point (stanno nel Planning) (FAQ B10).
- **INVEST?** → Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Quadrante di Wysocki?** → goal chiaro/non chiaro × soluzione chiara/non chiara → TPM (Linear, Incremental), APM (Iterative, Adaptive), xPM (Extreme), MPx (Emertxe).
- **Metodologia per sottosistema?** → Game Engine Waterfall; Backend e Frontend Agile Iterativo; Real-Time Agile Adattivo; Social, Infrastructure e Mobile Incrementale (FAQ A3).
- **Scrum e Kanban nel quadrante del corso?** → Scrum è l'esempio di Adaptive; il PMLC di Kanban è iterativo senza sprint sincroni — noi usiamo la board a flusso come *strumento* sul Real-Time.
- **Il costo dell'ibrido?** → la sincronizzazione: cadenza bi-settimanale comune, demo il venerdì di fine sprint, milestone di integrazione mensili, settimane 4/8/12 solo integrazione.
- **Perché non Extreme?** → il goal è sempre chiaro; l'incertezza riguarda solo la soluzione del Real-Time → Adaptive (FAQ B13).

## 3. Planning

- **WBS: livelli e regole?** → 4 livelli (sottosistema, funzione, attività, task); 100% rule; 8/80 rule sulle 43 attività (≈7 giorni-uomo).
- **La "doppia lettura"?** → 43 attività = unità di stima e controllo (il "task" del corso); i 160 elementi di quarto livello = scomposizione operativa per lo Sprint Backlog (FAQ C1, C13).
- **I 6 test di completezza?** → stato misurabile, confini definiti, deliverable associato, tempi e costi stimabili, durata accettabile, indipendenza.
- **MoSCoW: gli Should?** → requisiti critici ma sostituibili o differibili se necessario — non "non critici".
- **Perché Must al 75,8% e non 60% come DSDM?** → il core di gioco è irrinunciabile; i Could sono tenuti bassi contro lo scope creep (FAQ C6).
- **Stime?** → Delphi (anonima, più round fino alla convergenza) sul Game Engine; Planning Poker con Fibonacci 1…21 sugli agili (FAQ C7).
- **Effort vs durata?** → 302 giorni-uomo di sforzo contro 141 giorni di calendario: 5 persone in parallelo ≈ 2,1 FTE (FAQ C2).
- **Tipi di dipendenza?** → FS, SS, FF, SF, più il lag; SS = la successiva non può iniziare prima che *inizi* la precedente.
- **Convenzione dei tempi CPM?** → istanti 0-based: EF = ES + durata; le slide usano giorni 1-based: EF = ES + durata − 1; equivalenti, stesso critical path (FAQ G16).
- **Slack?** → LS − ES (equivale a LF − EF); zero sul percorso critico.
- **Fast tracking vs crashing?** → sovrapporre attività (SS + lag) vs aggiungere risorse (costo); noi fast tracking su P→R (FAQ C4).
- **Gantt vs network?** → il network dà logica, ES/EF/LS/LF e critical path; il Gantt il calendario e le 7 milestone (FAQ C12).
- **Cash flow: colonne?** → inflow, outflow, netto mensile e Net Cash Flow = saldo cumulativo (Inflow Tot − Outflow Tot, come nelle slide).
- **Perché l'outflow cala alla fine?** → l'ultimo inflow è il 15/02: la coda marzo–maggio è finanziata dal saldo, con il team ridotto a testing, UAT e lancio (FAQ C10).
- **Ripartizione spese?** → salari €16.000 (64%), contingency €4.664 (18,7%), tools €1.111, consulenza €300, infrastruttura €275, marketing/UAT/celebrazione €400.
- **Approvazione del planning?** → meeting con lo sponsor con via libera all'esecuzione, narrato nella relazione (Cap. 3), senza verbale allegato.

## 4. Launching

- **Kick-off?** → 15/10/2025, ibrido, un'ora: visione, perimetro MVP, timeline e milestone, budget, rischi, regole operative; Allegato 4.1 (FAQ D6).
- **RASCI: le lettere?** → Responsible esegue; Accountable approva ed è uno solo per riga; Support; Consulted; Informed (FAQ D1).
- **RASCI: dimensione?** → 51 righe a livello attività in 8 aree; i task ereditano la riga; Elena A/R sul Game Engine (Sara a supporto); Marco A/R sulle attività di PM (FAQ D2).
- **Problem solving?** → 5 passi con causa root ("5 Whys"); i problemi critici tornano in retrospective per prevenirli.
- **Decision making?** → consultivo su 3 livelli: operativo (il Responsible), tattico (Elena + Marco), strategico (Giovanni, su Project Impact Statement) (FAQ D3).
- **Conflict resolution?** → 3 fasi: confronto diretto → mediazione (Marco o Elena) → decisione esecutiva; sui conflitti tecnici decide Elena, poi "disagree and commit" (FAQ D4).
- **Brainstorming?** → divergent thinking (nessuna critica, "Yes, and…") → convergent (affinity mapping, dot voting, owner e next step).
- **Meeting ricorrenti?** → Daily 09:00–09:15; Sprint Planning 2 h; Backlog Refinement 1 h; Sprint Review 1 h; Retrospective 1 h; Project Status Meeting il venerdì 16–17 con lo sponsor.
- **Comunicazione: i 3 principi?** → asincrono prima di tutto; trasparenza (Notion single source of truth); SLA di risposta proporzionati alla priorità.
- **Canali?** → Slack (generale, daily, tecnico, urgenze); email (formale verso sponsor ed esterni); Notion (verbali, status report, decisioni, Change Log, Issue Log).
- **Change Request?** → 5 passi: submission (form) → impact analysis (Project Impact Statement su scope, tempi, budget, qualità, risorse + opzioni) → decisione dello sponsor → implementation (POS, WBS, Gantt, Backlog) → tracking nel Change Log (FAQ D5).
- **Over-allocation?** → in caso di conflitto con altri progetti dello spin-off, MaraffaOnline ha la precedenza.

## 5. Monitoring & Control

- **I tre livelli di monitoraggio?** → Daily Standup (sottosistemi agili), Project Status Meeting settimanale con lo sponsor, Sprint Review e Retrospective.
- **Stoplight?** → verde in linea, giallo scostamento sotto controllo (recovery plan attivo), rosso serve intervento; 5 aree: scope, schedule, budget, quality, risks (FAQ E2).
- **Formule EVM?** → CV = EV − AC; SV = EV − PV; CPI = EV/AC; SPI = EV/PV (>1 bene, <1 male) (FAQ E1).
- **L'errore classico sull'EVM?** → confrontare AC con PV: non misura l'efficienza, serve l'EV (FAQ G8).
- **Quando matura l'Earned Value?** → solo quando lo sponsor accetta la feature in Sprint Review (misura 100-0).
- **Cosa è successo a gennaio?** → 3 giorni di ritardo sulla Dashboard (attività M, critica) → Stoplight giallo → pair programming Luca+Sara → recuperato entro febbraio, milestone intatte (FAQ E3).
- **Scala di escalation?** → prima lo slack disponibile, poi le leve del PM (dipendenze, riallocazione), infine la rinegoziazione con lo sponsor (FAQ E5).
- **Velocity: perché team-wide?** → una sola vista consolidata per lo sponsor, dichiarata come convenzione di reporting; la velocity "pura" di Backlog è ≈28 (FAQ E6).
- **Issue Log?** → su Notion; 17 blocker tecnici, 14 intercettati nei Daily entro 24 ore.
- **Il rischio 2.1 nel tempo?** → 16 → 8 dopo il PoC di Sprint 2 → Mitigato dopo il load test di Sprint 6 (FAQ E4).

## 6. Closing

- **I 6 passi del corso?** → accettazione formale → installazione → documentazione → firma del committente sul report finale → audit post-implementazione → celebrazione (FAQ F1).
- **Accettazione?** → lunedì 11/05: Giovanni gioca una partita completa e firma senza richiedere modifiche.
- **Installazione?** → approccio a fasi: beta con i 20 tester → go-live pubblico del 15/05; deploy eseguito dalla community con le Docker image; cut-over e parallel non applicabili (nessun sistema preesistente).
- **Project Notebook vs Final Project Report?** → il Notebook (Notion, dal primo giorno) contiene tutta la documentazione; il FPR è la sintesi.
- **Struttura del FPR?** → Executive Summary; livello di successo e performance; organizzazione e amministrazione; tecniche impiegate; pregi e difetti dell'approccio; raccomandazioni; appendici (POS, WBS, schedule, change request, deliverable).
- **Audit?** → 13/05 con lo sponsor, CoS per CoS: tutti gli obiettivi del POS raggiunti; il business value a regime è rimandato al monitoraggio post-lancio (FAQ F2).
- **Le domande dell'audit secondo il corso?** → obiettivi raggiunti? tempi, budget e specifiche rispettati? committente soddisfatto? business value concretizzato? lezione sulla metodologia? come l'ha seguita il team?
- **Le 5 lessons learned?** → prototipare le UI complesse già in fase di stima; domain expert anche durante lo sviluppo; cross-browser dagli Sprint 5-6; daily asincrono strutturato; refactoring al 10-15% di ogni sprint (FAQ A5).
- **Celebrazione?** → 15/05, a budget (€100), su Zoom con lo sponsor.
- **Sviluppi futuri?** → app nativa (4-5 mesi, €18-20k), tornei (2-3 mesi, €8-10k), single-player contro IA (3-4 mesi, €12-15k).

## 7. Le trappole (dove il professore può incastrarti)

- **"Gli Should sono importanti ma non critici?"** → No: sono critici, ma sostituibili se necessario.
- **"SS vuol dire che due attività partono insieme?"** → No: la successiva non può iniziare prima che inizi la precedente; B e C dopo A è divergenza di legami FS.
- **"Requisiti noti → Iterativo?"** → No: requisiti noti = TPM (Linear/Incremental); l'Iterativo si sceglie quando la soluzione NON è chiara.
- **"Accept significa fare qualcosa per ridurre il rischio?"** → No: Accept = nessuna azione possibile. Se elimini la fonte è Avoid, se riduci l'impatto subito è Mitigate, se pianifichi il "se succede" è Contingency.
- **"Contingency = azioni preventive?"** → No: contingency = cosa fare *se* l'evento si verifica; le azioni immediate sono Mitigate.
- **"Il Final Project Report è tutta la documentazione?"** → No: è la sintesi; il contenitore è il Project Notebook.
- **"Il task è il livello che non si stima?"** → Per il corso il task è proprio il livello a cui si stimano tempi, costi e risorse: nel nostro schema sono le 43 attività.
- **"Il numero di allegato è la sezione della relazione?"** → No: gli allegati di Scoping sono sequenziali 2.1–2.9; meeting e approval sono solo nella relazione (FAQ G15).
- **"Il PM è anche CEO e Product Owner: conflitto?"** → governato: voto decisionale allo sponsor, decisioni tecniche a Elena, il PM raccomanda (FAQ H17).
- **"Dove sono JPPS, PDS, Scope Bank, burn chart, Kolb?"** → non con quel nome; le risposte oneste sono in FAQ H8–H11.
- **"Il CSV e le immagini dei mockup esistono?"** → i mockup sono dichiarati non prodotti (nota metodologica nel 2.6): l'elaborato gestisce il *processo* di design, non produce gli asset.
