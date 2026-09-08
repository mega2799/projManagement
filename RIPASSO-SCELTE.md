# Ripasso — Difendere le scelte all'orale

> **File di studio interno** — NON è un deliverable e non va incluso nella consegna.
> Foglio di sintesi per l'ultimo ripasso: l'orale è una conversazione in cui il docente ripercorre le scelte e chiede **come sono state prese**, **perché non altre**, **cosa faresti di diverso**. Qui c'è solo l'essenziale in forma pronunciabile; il dettaglio è nei documenti gemelli — `SCELTE-DI-PROGETTO.md` (§1.5, §9, §10), `FAQ.md` (sezione G per le domande scomode), `DRILL-ORALE.md` (domande-lampo), `PREPARAZIONE-ORALE.md` (numeri a memoria).

---

## 1. La regola dei due registri

| Domanda | Registro | Come suona |
|---|---|---|
| *"Cosa avete fatto quando il rischio WebSocket si è alzato?"* | **Dentro la narrazione** | Spike time-boxed, go/no-go al giorno 15, consulente pre-allertato, rating da 16 a 8 |
| *"Come hai pensato il cash flow?"* · *"Come ti è venuto in mente di usare il BMC?"* | **Da progettista** | "Sono partito da questo vincolo, ho applicato questa regola del corso, ho verificato questa coerenza" |

I due errori speculari: **restare nella finzione** quando la domanda è sul processo (sembra che tu non distingua i piani); **liquidare con "è inventato"** (sembra che i numeri siano casuali).

## 2. Da dove viene ogni numero — le quattro ancore

1. **Vincolo dato a monte**: €25.000, 7 mesi, 5 persone, lancio 15/05 → dati del problema.
2. **Regola del corso**: contingency ≈19%, 8/80 rule, 100% rule, saldo mai negativo, MoSCoW.
3. **Derivazione aritmetica**: 302 giorni-uomo, critical path 141 giorni, capacity 40 SP, velocity 38,3.
4. **Plausibilità di dominio, dichiarata come tale**: hosting, licenze, tariffa del consulente.

Nessuna delle quattro richiede che il progetto sia realmente accaduto.

## 3. Cash flow — la catena completa (30 secondi)

> Il budget non è un output del planning: **è un vincolo dello scoping**. I €25.000 sono la Condition of Satisfaction economica, la cifra del crowdfunding, non negoziabile. Quindi la domanda del Planning non era "quanto costa?" ma **"ci sta dentro?"**. Da lì: 302 giorni-uomo stimati con Delphi e Planning Poker → 5 persone al ≈50% FTE per 7 mesi → €16.000 di salari, il 64%. Le tariffe che ne escono sono sotto mercato, e infatti sono dichiarate come **ostacolo** nel POS, non nascoste. Poi contingency €4.664 (18,7%) e surplus €2.250 (9%). **La forma della curva discende da un vincolo**: l'ultimo incasso è il 15/02, quindi marzo–maggio vivono di saldo, quindi l'outflow *deve* calare nei mesi 5–7 — e infatti in quel periodo il Gantt non ha più sviluppo ma testing, UAT e lancio. Il saldo cumulativo tocca il minimo a €2.250 e non va mai sotto zero.

## 4. Le scelte-cardine e il costo dell'alternativa

**Regola d'oro: una scelta si difende dicendo cosa costava l'alternativa, non elogiando l'opzione scelta.**

| Scelta | Alternativa | Cosa costava |
|---|---|---|
| Ibrido per sottosistema | Metodologia unica | Overhead dove non serve (Sprint Planning su requisiti congelati), rigidità dove serve flessibilità |
| Waterfall sul Game Engine | Scrum anche lì | Cerimonie senza informazione nuova: le regole sono fisse da decenni e validate prima di partire |
| Contratto a corpo 50/25/25 | Time & materials | Il committente perdeva la certezza di spesa su un budget da crowdfunding non rinnovabile |
| POS | Project Charter | Un documento che conferisce al PM un'autorità che già ha (è CEO e PO) |
| RBS + WBS Dictionary + Kick-Off | PDS | Un secondo documento con le stesse 5 sezioni del POS, da tenere allineato a ogni cambiamento |
| Must al 75,8% | 60/20/20 di DSDM | Tagliare nel core: senza regole fedeli e partite fluide il prodotto non esiste |
| Fast tracking su P→R | Crashing | €2.000 di contractor invece di rischio di rework gestibile (tenuto come leva di riserva) |
| Installazione a fasi | Cut-over o parallel | Entrambe presuppongono un legacy da sostituire: non c'era |

Repertorio completo, inclusi gli strumenti del corso non prodotti: `SCELTE-DI-PROGETTO.md` §9.

## 5. I punti deboli — da giocare per primi

Indicarli tu sposta il registro da interrogatorio a conversazione. Le risposte distese sono in `FAQ.md` §G.

- **Salari sotto mercato** (€714/mese-persona contro €2.500–3.000): dichiarato nella SWOT come debolezza W2, rischio budget formalmente **accettato**; la compensazione è strategica, non monetaria (G6).
- **Picchi di carico**: Sprint 6 a 47 SP contro capacity 40. La media pianificata di ≈37 regge, ma **la media nasconde i picchi** — un livellamento esplicito sarebbe stato più onesto (G7, §8 voce 9).
- **Riclassificazione della Maraffa senza Change Request numerata**: approvata nella sostanza e compensata riducendo i Could, ma la forma corretta era un CR con Project Impact Statement (G10, §8 voce 13).
- **Surplus con doppio uso narrativo**: in un contratto a corpo è margine del fornitore, *impiegato* per il supporto promesso — stessa cassa, va detto così (G9, §8 voce 12).
- **Niente MS Project**: Notion, Figma/Miro, GitLab CI, Excel/HTML e uno script Python. Il criterio "uso di strumenti" si dimostra con artefatti coerenti, non con la licenza (G11).
- **Il metodo di raccolta dei requisiti non è scritto nella RBS**: le evidenze ci sono tutte (workshop, interviste, prototipi, Think Aloud), mancano le etichette del corso (B14).

## 6. Cosa farei di diverso — i sei migliori

1. **Prototipare le UI complesse già in fase di stima** — le animazioni, stimate 8 SP, erano sottostimate.
2. **Esperti di dominio nel loop durante lo sviluppo**, non solo nello Scoping — il caso Maraffa Should→Must.
3. **Cross-browser testing agli sprint 5–6**, i primi con interfaccia — farlo al 12 costò 2 giorni per Safari.
4. **Una JPPS formale** come contenitore della pianificazione collettiva già avvenuta, con il PDS fra gli output.
5. **Un burn-down per sprint** accanto alla velocity: costo quasi nullo, lettura infra-sprint che lo Stoplight non dà.
6. **Un paragrafo "Metodo di raccolta dei requisiti" in testa alla RBS** e **IRACIS esplicito nel POS**: due righe che avrebbero reso immediato ciò che oggi va spiegato a voce.

Elenco completo su tre piani (progetto / gestione / documento): `SCELTE-DI-PROGETTO.md` §10.

## 7. Le frasi da avere in bocca

- *"Non sono partito dallo strumento: avevo il problema X, e il corso offre Y per quello."*
- *"L'alternativa era Z, e costava questo."*
- *"È un caso di studio costruito per l'esame: quello che ho preso sul serio è la coerenza interna — il critical path esce dalle durate della WBS, il cash flow dalle stime, la velocity dagli sprint del Gantt."*
- *"La scelta di fondo è stata tenere pochi documenti vivi invece di molti documenti fedeli al template: su un team di cinque, un artefatto che nessuno aggiorna fa più danno che assenza."*
- *"Questa è l'assunzione più fragile del piano, e se salta succede questo."*
- *"Ho trovato e corretto questi errori"* — tre giri di audit documentati, meglio di *"non ce ne sono"* (§8).

---

**Ultimo aggiornamento**: 2026-09-08 — prima stesura, estratta da `SCELTE-DI-PROGETTO.md` §1.5/§9/§10 e da `FAQ.md` §G. Nessun contenuto nuovo: se un dato cambia, si aggiorna la fonte e poi questa sintesi.
