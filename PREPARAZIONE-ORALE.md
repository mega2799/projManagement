# Preparazione Orale — Progetto MaraffaOnline

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Serve a padroneggiare l'elaborato senza rileggere relazione e allegati: la storia, le scelte, i numeri e — soprattutto — le risposte pronte sui punti delicati. La teoria generale del corso sta in `../knowledge_base/` e `../studio/`; qui c'è **solo ciò che riguarda questo progetto**.
>
> **Da tenere sincronizzato**: se relazione o allegati cambiano, aggiornare anche questo file.

---

## 1. Il progetto in 90 secondi (elevator pitch)

MaraffaOnline è una piattaforma web multiplayer per giocare a **Maraffa** (Maraffone/Beccaccino), gioco di carte tradizionale romagnolo, in tempo reale a 4 giocatori. La sviluppa **PlayHeritage Labs**, spin-off dell'Università di Bologna (Cesena, nato nel 2023) specializzato in *cultural heritage gaming*, su commissione di **Maraffa Forever**, community informale di ~150 ex studenti romagnoli oggi dispersi per l'Italia e l'Europa, che ha raccolto **€25.000** con un crowdfunding interno. Il problema è sociale e geografico: le app esistenti sono obsolete o solo single-player contro IA, e la dimensione conviviale del gioco si è persa. Il progetto dura **7 mesi** (15 ottobre 2025 – 15 maggio 2026), è il **primo progetto pilota** dello spin-off (valida modello di business e metodologie, e fornisce materiale per pubblicazioni accademiche) e si chiude con successo: MVP lanciato puntuale, €22.750 spesi su 25.000, tutti i criteri di soddisfazione rispettati.

La cifra distintiva della **gestione** è l'approccio ibrido: il prodotto è scomposto in 7 sottosistemi *loosely coupled* e a ciascuno è applicato il ciclo di vita più adatto (Waterfall, Agile Iterativo, Agile Adattivo, Incrementale), con una cadenza comune bi-settimanale a tenerli sincronizzati.

## 2. Il cast (nomi da non confondere)

| Persona | Ruolo |
|---|---|
| **Marco Venturi** | CEO PlayHeritage Labs, **Project Manager** e Product Owner |
| **Elena Rossi** | Lead Developer / Tech Lead, specialista Game Engine, Scrum Master |
| **Sara Bianchi** | Backend Developer |
| **Luca Moretti** | UX/UI Designer e Cultural Heritage Expert (Frontend) |
| **Andrea Conti** | DevOps & Infrastructure Specialist |
| **Giovanni Marchetti** | **Committente/sponsor**, rappresentante di Maraffa Forever |
| **Francesca Giuliani** | Esperta di dominio (regole della Maraffa), valida la specifica del Game Engine |
| **Dr. Stefano Nardi** | Consulente esterno real-time, **di contingenza** (budget €2.000, attivabile sul rischio WebSocket) |

Il team lavora **part-time (~50% FTE)**: è la risposta al rischio "budget insufficiente" — il progetto ha valore strategico da pilota, quindi il rischio è stato *accettato* comprimendo i costi, non trasferito.

## 3. I numeri da sapere a memoria

| Cosa | Valore |
|---|---|
| Durata | 7 mesi: 15 Ott 2025 → 15 Mag 2026 |
| Giorni lavorativi disponibili | **146** (festività italiane escluse); 141 fino all'8 Mag |
| **Critical path** | **141 giorni lavorativi** (A→B→D→G→J→M→P→R→S→T), fine T = 8 Mag, **margine 5 gg lavorativi** sul lancio |
| Budget / consuntivo | €25.000 / **€22.750** → surplus €2.250 (9%), destinato al supporto post-lancio |
| Pagamenti | contratto a corpo, 3 tranche **50/25/25**: 15 Ott (firma), 15 Dic (Backend Core), 15 Feb (core di gioco) |
| Effort stimato (MoSCoW) | **302 giorni-uomo**: Must 75,8% / Should 18,9% / Could 5,3% |
| Sottosistemi | **7** (6 di sviluppo attivi + Mobile App = Won't Have) |
| WBS | 4 livelli, ~160 task, 100% rule |
| Sprint | **15** (Sprint 0–14) da 2 settimane; sviluppo negli **Sprint 0–10**, gli 11–14 sono testing E2E, UAT, lancio |
| Product Backlog | **310 SP**; lavoro totale ~**441 SP** equivalenti (310 + ~94 Game Engine + ~37 Infrastructure) |
| Capacity / carico | **40 SP/sprint team-wide** = capacità stimata; carico medio pianificato **~37 team-wide** (441 SP su Sprint 0-11) e **~28 solo Backlog** (310 SP su Sprint 1-11); velocity misurata **38,3** |
| Sprint 5 (natalizio) | 22 Dic–2 Gen: **21 SP su 40** (52,5%), carryover 19, **escluso** dalla media |
| Float | ramo Game Engine **22 gg**, ramo Chat/Social **37 gg** |
| Fast tracking | legame **P→R Start-to-Start + lag 31 gg** (Testing E2E in overlap sulla coda del Frontend Tavolo) |
| Attività più critica | **P — Frontend Tavolo da Gioco, 40 giorni** (2 Feb – 27 Mar) |
| EVM | CPI = SPI ≈ **1,00** a fine progetto; a gennaio CV = −€300, SV = −€900 (ritardo 3 gg sulla Dashboard, attività M), recuperati entro febbraio |
| Qualità | test coverage **>85%** (DoD richiede >80%); latenza media **185ms** (target <500ms); PoC Sprint 2: 180ms |
| UAT | **80% degli utenti** completa una partita senza aiuto (criterio CoS rispettato) |
| Rischi | **20 rischi**, 2 critici (rating 16): WebSocket e budget; 6 rossi (9–12) tra cui race conditions (12) e scope creep (12) |
| Retrospettive | 30 action item di miglioramento, 28 implementati |
| Milestone | M1 27 Ott · M2 19 Dic · M3 30 Gen · M4 27 Mar · M5 31 Mar · M6 24 Apr · M7 15 Mag |

## 4. Le regole del gioco (quanto basta per l'orale)

4 giocatori in 2 coppie, 40 carte italiane, 10 a testa. Chi ha il **4 di denari** sceglie la briscola e apre. Punti: Assi = 1; figure, 2 e 3 = ⅓; ultima presa = 1. Vittoria a **41 punti + almeno una figura**. **Maraffa (o Cricca)** = Asso+2+3 di briscola in mano = 3 punti bonus (va giocato l'Asso per primo). Ordine di forza: 3 > 2 > A > Re > Cavallo > Fante > 7…4. Le regole ufficiali sono state **documentate e validate da Francesca Giuliani** prima dello sviluppo: è questo che rende i requisiti del Game Engine stabili e giustifica il Waterfall.

## 5. Racconto per fasi (cosa abbiamo fatto e perché)

### Scoping (Allegati 2.1–2.11)

Tutto parte dal **Project Scoping Meeting** (2.1) con sponsor, esperta di dominio e team completo: visione condivisa, primi confini, individuazione dei sottosistemi. Le **Conditions of Satisfaction** (2.2) sono negoziate con Giovanni secondo lo schema richiesta/risposta e coprono **5 tipologie**: temporale (MVP entro 15 Mag 2026), economica (≤ €25.000), tecnica (regole fedeli, latenza <500ms, API <200ms), qualitativa (80% utenti autonomi in partita, valutazione ≥4,2/5, WCAG 2.1 AA), gestione del lavoro. Il **POS** (2.3) condensa problema, opportunità, goal e **6 obiettivi numerati** (Game Engine fedele; real-time fluido a 4; UI moderna responsive; funzionalità sociali; scalabilità/sicurezza; MVP in 7 mesi a €25.000), ciascuno con criteri di successo misurabili e rischi correlati.

La **Risk Analysis** (2.4) usa la Risk Rating Matrix probabilità×impatto: 20 rischi, di cui **2 critici a rating 16** — l'inesperienza del team con WebSocket (contingenza: spike tecnico di 2 settimane + consulente Nardi a €2.000) e il budget risicato (accettato: team part-time, valore strategico) — più scope creep (12, mitigato con Change Control rigoroso e freeze dei requisiti dopo il POS) e race conditions (12, architettura server-authoritative). **BMC** (2.5) e **SWOT** (2.6) inquadrano la strategia: punto di forza la co-creazione con una community motivata (20 beta tester), debolezza chiave la stessa inesperienza real-time. Il **Prototyping** (2.7) produce mockup Figma in due versioni — v1 commentata da Giovanni, v2 approvata e **vincolante** per il frontend. La **RBS** (2.8) organizza i requisiti per sottosistema, le **User Stories** (2.9) li esprimono secondo **INVEST**, e il **Life Cycle Models** (2.10) assegna la metodologia a ogni sottosistema (vedi §6.1). Chiusura con **Approval Process** (2.11): approvazione formale del perimetro.

### Planning (Allegati 3.1–3.5)

La **WBS** (3.1) decompone il lavoro su 4 livelli (~160 task, 100% rule) per i 6 sottosistemi attivi + attività trasversali di PM/QA. La **MoSCoW** (3.2) prioritizza: 302 giorni-uomo con Must al 75,8% — sopra il target DSDM del 60%, scelta motivata dalla criticità di Game Engine e Real-Time — e Could compressi al 5,3% in funzione anti-scope-creep. Le **stime** usano **Delphi** per il Game Engine (Waterfall: stime anonime, più round fino a convergenza) e **Planning Poker** per i sottosistemi Agile (Fibonacci 1–21). Il **Product Backlog** (3.3) raccoglie il lavoro che scorre negli sprint (310 SP, vedi §6.2). Il **Cash Flow** (3.4) mostra saldo cumulativo sempre positivo con minimo €2.250 nell'ultimo mese. Il **Network Diagram + Gantt** (3.5) applica il CPM: percorso critico di 141 giorni lavorativi con fast tracking dichiarato (vedi §6.3). La fase si chiude con il meeting di approvazione della pianificazione.

### Launching (Allegati 4.1–4.2)

**Kick-Off Meeting** il 15 Ott 2025 con team, sponsor ed esperta: visione, perimetro MVP, timeline con milestone, budget, rischi, regole operative. La **RASCI** (4.2) assegna per ogni attività Responsible/Accountable/Support/Consulted/Informed con la regola **un solo Accountable per task**. Le **regole operative** comprendono: problem solving con root cause analysis (**5 Whys**), decision making su **3 livelli** (operativo/tattico/strategico, "decidere al livello più basso possibile"), conflict resolution progressiva in **3 fasi** (discussione diretta → mediazione facilitata → decisione esecutiva; mai servita oltre la fase 2), brainstorming e cerimonie (Daily Standup 9:00–9:15, Sprint Planning, Review, Retrospective, Project Status Meeting). **Comunicazione**: asincrona-first su Slack/email, Notion come *single source of truth*, SLA di risposta per priorità. **Gestione del cambiamento**: Change Request formalizzato (submission → impact analysis con Project Impact Statement → decisione sponsor → implementazione → tracciamento); i sottosistemi Agile accolgono il cambiamento nel processo, quelli tradizionali lo valutano caso per caso.

### Monitoring & Control (Cap. 5 + documento di dettaglio)

Monitoraggio su **3 livelli**: quotidiano (Daily Standup per i sottosistemi Agile), settimanale (Project Status Meeting di 1h con lo sponsor), per sprint (Review + Retrospective). Issue Log su Notion. Reporting con **Stoplight Report** (verde/giallo/rosso su Scope, Schedule, Budget, Quality, Risks) e **EVM** (PV/EV/AC → CPI, SPI). L'episodio-chiave da raccontare: a **gennaio 2026** il Frontend Dashboard e Creazione Stanza (M) accumula **3 giorni di ritardo** sul percorso critico (CV=−€300, SV=−€900, stoplight giallo) → scala d'intervento graduata (prima lo slack, poi le dipendenze, solo alla fine la rischedulazione) → **recovery plan** con pair programming Luca+Sara → recupero completo entro febbraio, CPI=SPI=1,00 a fine progetto. Il rischio WebSocket viene *chiuso* nel percorso: spike + PoC in Sprint 2 (latenza 180ms) → rating da 16 a 8 → mitigato dopo il load test dello Sprint 6.

### Closing (Cap. 6 + documento di Closing)

**Accettazione formale** l'11 Mag 2026 (lunedì, quattro giorni prima del lancio): Giovanni testa personalmente una partita completa e firma senza chiedere modifiche. Il deploy in produzione è a carico della community (Docker image + istruzioni di Andrea). **Final Project Report** consegnato il 12 Mag. **Audit post-implementazione**: tutti gli obiettivi POS raggiunti (7 mesi, 141 gg di critical path rispettati, €22.750, regole validate, latenza 185ms, 80% utenti autonomi). **Lessons learned** principali: (1) prototipare le feature UI complesse già in fase di stima; (2) coinvolgere gli esperti di dominio anche durante lo sviluppo, non solo nello Scoping; (3) anticipare il testing cross-browser (fu fatto solo allo Sprint 12: le animazioni CSS su Safari costarono 2 giorni di fallback); (4) evitare di accumulare technical debt da smaltire tutto insieme (il cleanup dello Sprint 10 ha ridotto il valore visibile per lo sponsor in quella Review) — meglio il 10–15% di ogni sprint. Chiusura con celebrazione e interesse dello sponsor per sviluppi futuri (app nativa, tornei, single-player IA).

## 6. I casi speciali — risposte pronte (QUI si vince l'orale)

### 6.1 «Perché quattro metodologie diverse? Non è più complicato?»

I criteri di scelta sono **l'incertezza dei requisiti e l'incertezza della soluzione** (matrice in Allegato 2.10):
- **Game Engine → Waterfall**: regole documentate, stabili e vincolanti (validate da Francesca Giuliani prima dello sviluppo); test case scrivibili a monte da partite a risultato noto; il feedback continuo conta poco perché gli utenti le regole le conoscono già.
- **Backend e Frontend → Agile Iterativo**: obiettivi chiari ma serve feedback continuo dello sponsor (demo regolari a Giovanni).
- **Real-Time → Agile Adattivo**: incertezza massima (le latenze con Socket.IO reggeranno?) → sperimentazione rapida, spike, decision point go/no-go.
- **Social e Infrastructure → Incrementale**: valore rilasciabile in incrementi indipendenti prioritizzati MoSCoW.

Il costo dell'ibrido è la **sincronizzazione**: risolto con una cadenza comune sovrapposta — scansione bi-settimanale anche per chi non lavora a sprint, demo bi-settimanali il venerdì di fine sprint (in Sprint Review), milestone di integrazione mensili, settimane 4/8/12 dedicate a integrazione e bug fixing senza nuove feature. Benefici: rischio gestito per componente, niente overhead superfluo (uno sprint planning sul Game Engine non avrebbe senso), modello riusabile su futuri giochi tradizionali.

### 6.2 «Perché Social & Community sta nel Product Backlog se è Incrementale?» ⚠️

Il criterio di inclusione nel Backlog **non è l'etichetta metodologica del sottosistema ma la natura del lavoro**: entra ciò che è esprimibile come *user story rivolta all'utente finale* e realizzato *dentro gli sprint*. Le feature Social (amicizie, chat in-game, profili, statistiche) sono user story a tutti gli effetti, sviluppate dagli stessi team nelle stesse iterazioni — quindi nel Backlog compaiono **sotto il sottosistema che le implementa** (amicizie US-5.x e statistiche US-6.1 nel Backend, chat US-4.1 nel Real-Time, le rispettive interfacce nel Frontend; per questo nel riepilogo non c'è una riga "Social"). La colonna US del backlog punta alle user story dell'Allegato 2.9; i task tecnici/abilitanti sono marcati "—". Restano fuori il **Game Engine** (Waterfall su specifica congelata, validazione finale) e l'**Infrastructure** (attività ricorrenti e on-demand, non riconducibili a user story): tracciati in WBS e Gantt. Mescolare cicli di vita diversi nel Backlog ne comprometterebbe leggibilità e chiarezza dei ruoli Scrum.

### 6.3 «Il critical path è di 141 giorni: come ci sta in 7 mesi? E il fast tracking?» ⚠️

I numeri: tra il 15 Ott 2025 e il 15 Mag 2026 ci sono **146 giorni lavorativi** netti (weekend e festività italiane esclusi). Il percorso critico **A→B→D→G→J→M→P→R→S→T dura 141**, cioè esattamente i giorni lavorativi fino all'**8 maggio** (fine di T, Preparazione Lancio): il lancio del 15 conserva **5 giorni (~1 settimana) di margine**. Tutte le durate sono in giorni lavorativi netti, coerenti con le date del Gantt.

Per farcelo stare è stata applicata una **compressione della schedula di tipo fast tracking** (tecnica delle slide, dispensa 7 - Planning): il Testing End-to-End (R, 11 gg, 17–31 Mar = Sprint 11) non aspetta la fine del Frontend Tavolo (P, 40 gg, che chiude il 27 Mar), ma è legato a P con vincolo **Start-to-Start + lag 31 gg** — parte quando P ha completato 31 giorni su 40, testando i moduli già congelati (login, dashboard, stanze) mentre P rifinisce animazioni. «La compressione non è mai gratis» (cit. slide): il rischio di rework è dichiarato e mitigato — l'Integration Testing del Game Engine (O) chiude *prima* che R inizi, e gli ultimi 2 giorni di R cadono comunque dopo la fine di P.

Float: ramo Game Engine (C-F-I-L-O) **22 gg**, ramo Chat/Social (E-H-K-N-Q) **37 gg** → nessuno dei due condiziona il lancio. Sensitivity: se P ritarda 10 gg si consuma il margine e si comprime la UAT da 17 a 12 gg (+1 dev part-time, ~€2.000); se N ritarda 10 gg, assorbito dai 37 di float.

### 6.4 «302 giorni-uomo ma 141 giorni di progetto: come si conciliano?» ⚠️

Sono **grandezze diverse**: 302 giorni-uomo è lo *sforzo* aggregato del team (dalla MoSCoW), 141 giorni lavorativi è la *durata* (dal CPM). Cinque persone part-time che lavorano in parallelo sui sei sottosistemi: 302/141 ≈ **2,1 FTE medi**, perfettamente coerente con un team di 5 al ~50%.

### 6.5 «40 story points a sprint, ma il Backlog ne ha 310 su 15 sprint: non tornano ~21?» ⚠️

No, e la chiave è distinguere **capacità** da **carico**. I 40 SP/sprint sono la **capacity team-wide**: quanto il team *può* completare in uno sprint, includendo il lavoro di Game Engine e Infrastructure stimato in punti equivalenti (~131 SP, per un totale progetto di ~441). Il **carico medio pianificato** è più basso: ~**37 SP/sprint team-wide** (441 su Sprint 0-11) e ~**28 SP/sprint di solo Backlog** (310 su Sprint 1-11) — il margine tra capacità e carico assorbe festività (Sprint 5 natalizio) e variabilità delle stime. Gli Sprint 12-14 non sono stimati in SP (UAT, lancio); lo Sprint 11 ospita solo le rifiniture del tavolo, in fast tracking col testing E2E. Due livelli di lettura: metrica *gestionale* consolidata per lo sponsor (quella monitorata nel Cap. 5) e carico *Scrum* del team. La velocity misurata media è **38,3**, coerente con la capacity 40.

### 6.6 «E lo sprint di Natale?»

Lo Sprint 5 (22 Dic – 2 Gen) è pianificato **a capacità ridotta**: 21 SP completati su 40 (52,5%), con **carryover di 19 SP** riassorbito nei due sprint successivi. La media di 38,3 **lo esclude** perché non rappresentativo del ritmo di regime — dirlo esplicitamente mostra onestà metodologica, non un trucco.

### 6.7 «Perché il Must Have è al 75,8% se DSDM raccomanda 60%?»

Scelta deliberata e motivata: Game Engine e Real-Time sono il *core differentiator* — senza regole fedeli e partite fluide il prodotto non esiste. In compenso i Could Have sono compressi al 5,3% (contro ~20%) per ridurre il rischio di scope creep e proteggere la consegna in 7 mesi. Il trade-off è documentato nella MoSCoW con le esclusioni esplicite (Won't Have: app nativa, social login, single-player IA, notifiche push, tornei).

### 6.8 «Come avete stimato? Perché due tecniche?»

**Delphi** per il Game Engine: stime individuali *anonime* con motivazione, più round fino a convergenza — adatta a requisiti stabili e a evitare l'ancoraggio. **Planning Poker** per l'Agile: il PO presenta il task, carte Fibonacci (1,2,3,5,8,13,21) scelte in modo indipendente, discussione delle discrepanze, ripetizione fino al consenso. Stessa filosofia (stima collettiva anti-bias), strumento calibrato sul contesto.

### 6.9 «Raccontami di quando qualcosa è andato storto»

Due storie pronte. (1) **Ritardo di gennaio**: 3 giorni sul Frontend Dashboard e Creazione Stanza (attività M, sul percorso critico a monte del Tavolo) → visibile in Stoplight (Schedule giallo), nel Gantt tracking (M al 60% invece dell'80%) e in EVM (SV=−€900) → scala graduata d'intervento → pair programming Luca+Sara → recuperato entro febbraio senza toccare la milestone. (2) **Rischio WebSocket**: il più critico (rating 16) → spike tecnico + PoC in Sprint 2 con latenza misurata 180ms → rating dimezzato a 8 → chiuso dopo il load test dello Sprint 6. Morale in entrambi i casi: il monitoraggio multilivello ha trasformato problemi potenzialmente fatali in scostamenti gestiti.

### 6.10 Definizioni-lampo che possono chiedere sul progetto

- **100% rule (WBS)**: la WBS copre il 100% del lavoro, incluso il PM stesso (sezione 7 trasversale).
- **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable — applicato alle user stories (2.9).
- **DoD** (Backlog): codice committato, unit test >80% coverage, code review, integration test, doc aggiornata, deploy in staging, acceptance criteria ok, approvazione PO in Sprint Review.
- **RASCI**: un solo Accountable per task; Responsible esegue.
- **EVM**: PV pianificato, EV realizzato, AC costo effettivo; CPI=EV/AC, SPI=EV/PV; a fine progetto entrambi ≈1,00.
- **Stoplight**: verde in linea, giallo scostamento sotto controllo, rosso serve intervento.
- **Slack/Float**: LS−ES; zero sul percorso critico; 22 gg ramo Game Engine, 37 gg ramo Social.
- **SS+lag**: relazione di precedenza Start-to-Start con ritardo — usata per il fast tracking P→R (31 gg).

## 7. Punti aperti / incoerenze residue note ⚠️

Da sistemare prima della consegna, o quantomeno da **sapere** per non farsi sorprendere:

1. **UAT: aprile o maggio?** Gantt e Backlog collocano la UAT in **1–24 Apr** (M6 = approvazione 24 Apr); ma Cap. 5 e Cap. 6 raccontano la "UAT ufficiale" **1–10 Maggio**. Contraddizione da risolvere (la lettura più difendibile: UAT formale in aprile come da piano; a inizio maggio una sessione finale di *validazione pre-lancio*).
2. **Pagamento M2**: la tranche del 15 Dic è "a valle del Backend Core", ma M2 cade il 19 Dic — sfasatura di 4 giorni, minore.
3. **RASCI (Allegato 4.2), rilievi minori residui** (gli altri quattro — reconnection 30s, chat in-game senza riga, review del 15/12, assegnatario UAT nel CSV — sono stati **corretti** il 2026-08-09):
   - **Scrum Master**: il 3.3 firma «Elena Rossi (Scrum Master)», ma Daily e Retrospective nella RASCI sono facilitati da **Marco** — che è già PO (antipattern PO+SM; risposta pronta: "team di 5, facilitazione pragmaticamente in capo al PM; il presidio di processo Scrum era di Elena");
   - «Validazione regole»: A = Giovanni, ma il 2.10 dice che è **Francesca** ad approvare la specifica (risposta pronta: Francesca valida tecnicamente ed esegue le sessioni, R; lo sponsor approva formalmente, A).
4. **Sessioni di validazione regole (Francesca)**: il POS chiede la validazione formale della specifica «entro il 30/10/2025», il Cash Flow paga **2 sessioni** (Novembre 2025 e Aprile 2026, €150 l'una), ma il Gantt/CSV colloca una validazione a **fine gennaio** (task L.3, chiusura Game Engine Testing). Lettura difendibile: Ott/Nov = validazione della *specifica* (sessione pagata 1, quella in cui emerge la riclassificazione della Maraffa); Gennaio = validazione dell'*implementazione* dentro il GE Testing (Francesca coinvolta, non fatturata a parte); Aprile = validazione finale pre-UAT (sessione pagata 2).
5. **POS, criterio "80 utenti attivi nei primi 2 mesi"**: non è verificabile alla chiusura del 15/05 (il Closing dichiara comunque "criteri pienamente soddisfatti"); risposta pronta: il dato delle prime 24h (50 registrati, 23 partite) è ben oltre la traiettoria attesa, e il criterio resta in monitoraggio post-lancio a carico della community.
6. **Audit incrociato del 2026-08-09 — COMPLETATO E CORRETTO** (registro completo in `SCELTE-DI-PROGETTO.md` §8, risposte pronte in `FAQ.md` §G). Cinque squadre di verifica (date, denaro, cast/riferimenti, regole di gioco, metriche) hanno trovato e sono stati **corretti negli allegati**: le regole sbagliate nelle US-3.1/3.5/3.6 (4 di Denari, punteggio 41-36, Maraffa = A+2+3 di briscola); il "full-time" nel POS; il revisore fantasma "Luca Bianchi"; il decision point WebSocket armonizzato (g.15 consulente, g.30 escalation); la semantica EVM del Cap. 5 (CV vera, saldo €5.250); le percentuali MoSCoW di sezione; la **griglia sprint mar-sab riallineata a lun-ven** (S5 = 22 Dic-2 Gen); l'**accettazione spostata all'11/05** (il 10 era domenica); milestone del network rinumerate M2/M3/M4/M6; break-even ~84 mesi; ritardo Sprint 7 attribuito a M anche nel §5.8; rischi citati come 2.1/6.2 (non R1/R4); tornei = Won't; tutorial non più "extra"; PWA = Won't ovunque; SP padre del CSV = somma dei figli; più una ventina di refusi minori (date nel weekend, Jira/Confluence/PaaS/DigitalOcean, "12 allegati", chat 1-a-1 fantasma). **Restano da sapere** (difendibili a voce): i punti 1-5 sopra, il PoC in due stadi (spike Sprint 0 → PoC completo Sprint 2), REQ-SOC-6.1 letto come quota UI delle amicizie, gli overlap FS minori non annotati nel CSV (H.7, I.7, J.5, K.5-6, Q.4), la 3ª tranche di domenica 15/02 (data contrattuale fissa) e il doppio uso narrativo del surplus (6.3 supporto post-lancio vs 6.7 sostenibilità: stessa cassa, dirlo così).

Storico delle incoerenze **già risolte** (per contesto, se chiedono "cosa correggereste?"):
- Social & Community dichiarato "Agile" in contrasto col 2.10 → criterio della natura del lavoro (§6.2);
- velocity 40 vs 21 non tornava → riconciliazione capacità/carico (§6.5);
- critical path 170 gg impossibile nei 7 mesi → 141 gg + fast tracking (§6.3);
- M4 datata 14 Mar prima della fine di P → 27 Mar;
- RASCI: Elena "Backend Developer" e Sara Responsible del Game Engine mentre era già Responsible del Backend negli stessi sprint (conflitto di carico) → Elena A/R sul GE, Sara a supporto;
- load test a 50 partite vs criterio CoS di 100 → uniformato a 100 (RASCI, Cap. 5, Cap. 6);
- **tracciabilità US rotta**: il backlog usava 58 ID inesistenti nel 2.9 con collisioni di significato → colonna US rimappata sulle 23 user story reali del 2.9; rimosso dal 2.9 il "riepilogo per sprint" (pianificazione in Scoping, contraddiceva il 3.3);
- **tavolo da gioco a gennaio vs feb-mar**: gli sprint del backlog erano sfasati di ~1-2 sprint rispetto al Gantt su Frontend e Real-Time → riallineati alle date del Gantt (tavolo Sprint 8-11); il ritardo di gennaio è ora correttamente attribuito alla **Dashboard (M)**, e il "65% di P a gennaio" (impossibile: P inizia il 2 Feb) è diventato "60% di M";
- kickoff previsto il 25/09 nel 2.1 → 15/10; timeline mockup 2.7 che sforava l'approvazione dello Scoping → anticipata (v2 il 25/09, approvazione 01/10);
- Maraffa "era Should Have" solo nel racconto del Closing → riclassificazione documentata anche nella MoSCoW (nota di revisione, Novembre 2025);
- leaderboard detta "Should" nel Closing ma Could nella MoSCoW → corretto (Could, REQ-SOC-6.3);
- sprint di refactoring: era "Sprint 11" in conflitto col Testing E2E → Sprint 10;
- drag & drop vs click to play → uniformato a **click to play** ovunque (Closing, RASCI); Playwright → **Cypress**; Edge aggiunto al cross-browser; CoS comunicazione allineata (status settimanale + review bi-settimanale); "meeting di approvazione budget" del 27/10 riqualificato come approvazione del piano di cash flow.

## 8. Mappa: dove sta cosa

| Documento | Contenuto |
|---|---|
| `Relazione/main.tex` (Cap. 1–6) | Descrizione dell'approccio: motivazioni di ogni scelta, rimandi cliccabili agli allegati |
| 2.1 Scoping Meeting | verbale, partecipanti, decisioni (web-first, contratto a milestone) |
| 2.2 CoS | 5 tipologie di criteri negoziati richiesta/risposta |
| 2.3 POS | problema, opportunità, goal, 6 obiettivi, criteri, rischi, assunzioni, ostacoli |
| 2.4 Risk Analysis (+HTML) | matrice 20 rischi, 2 critici, mitigazioni |
| 2.5 BMC (+HTML) / 2.6 SWOT (+HTML) | inquadramento strategico |
| 2.7 Prototyping | mockup v1 commentata → v2 approvata (vincolante) |
| 2.8 RBS / 2.9 User Stories | requisiti per sottosistema / INVEST |
| 2.10 Life Cycle Models | matrice metodologia×sottosistema con motivazioni |
| 2.11 Approval | chiusura formale dello Scoping |
| 3.1 WBS (+visuale) | 4 livelli, ~160 task |
| 3.2 MoSCoW (+visuale) | 302 gg-uomo, 75,8/18,9/5,3 |
| 3.3 Product Backlog | 310 SP, calendario 15 sprint, tabelle per sottosistema, DoD |
| 3.4 Cash Flow (+visuale) | tabella mensile, tranche, minimo €2.250 |
| 3.5 Network+Gantt (+HTML, +CSV) | CPM completo, fast tracking, milestone; HTML rigenerabile con `tools/genera-networkgantt-html.py` |
| 4.1 Kick-Off | verbale 15 Ott, agenda, action items |
| 4.2 RASCI + Regole Operative (+visuale) | matrice ruoli, 5 Whys, 3 livelli decisionali, conflict resolution, cerimonie |
| Monitoring/Capitolo5 | EVM mensile, stoplight, velocity, quality metrics, risk monitoring |
| Closing/Capitolo6 | accettazione, audit, fattori di successo, lessons learned, celebrazione |

## 9. Criteri con cui verrà valutato l'elaborato (dalle linee guida)

1. **Solidità delle argomentazioni** — ogni scelta ha una motivazione esplicita (il "perché" di §6 è il cuore).
2. **Coerenza** — architettura e gestione allineate (da qui l'attenzione maniacale ai numeri incrociati).
3. **Originalità** — approccio ibrido per sottosistema, fast tracking dichiarato, doppia lettura della velocity.
4. **Uso di strumenti** — Notion (board + CSV import), Figma, GitLab CI/CD, Cypress, grafici Excel, HTML visuali.
5. **Conoscenza teorica** — dimostrata all'orale: per ogni artefatto sapere *cos'è in generale* (knowledge_base) e *come l'abbiamo usato qui* (questo file).

---

**Ultimo aggiornamento**: 2026-08-09 (sera) — audit incrociato a 5 lenti completato e correzioni applicate a tutti gli allegati (vedi §7.6); PDF e Relazione rigenerati; creati i documenti gemelli `SCELTE-DI-PROGETTO.md` (registro ragionato delle scelte) e `FAQ.md` (domande previste all'orale con risposte). Aggiornamento precedente: 2026-08-02 — allineato ad Allegato 3.3 v.3.1.0 (US reali del 2.9, sprint da Gantt), Allegato 3.5 v.2.0.0 (critical path 141 gg, fast tracking P→R), RASCI v.1.4.0, riconciliazione capacità 40 / carico 37-28, ritardo di gennaio su Dashboard (M), audit di coerenza incrociata completato.
