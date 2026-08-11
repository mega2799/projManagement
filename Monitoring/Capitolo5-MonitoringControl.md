# Capitolo 5 - Monitoring and Control

Registro del monitoraggio di MaraffaOnline: strumenti usati, dati raccolti ed episodi gestiti. La discussione dell'approccio è nella relazione, Cap. 5.

## 5.1 Monitoraggio Continuo

Nei sottosistemi Agile (Backend, Real-Time, Frontend) ogni mattina un Daily Standup di 15 minuti (09:00–09:15): cosa ho fatto, cosa farò, blocker. Ogni sviluppatore tiene aggiornato lo stato dei propri task sulla board Notion, così il Project Manager ha visibilità continua senza convocare meeting aggiuntivi. La linea guida di PlayHeritage Labs è segnalare i problemi appena emergono, essere sinceri sullo stato del lavoro e fare domande quando qualcosa non è chiaro: un clima di apertura che evita l'accumularsi silenzioso dei ritardi (i vari "creep").

## 5.2 Project Status Meetings

Ogni venerdì dalle 16:00 alle 17:00, con Marco Venturi (presenter), Giovanni Marchetti (sponsor) ed Elena Rossi per la parte tecnica. Si presenta lo Stoplight Report — verde: come previsto; giallo: scostamenti sotto controllo; rosso: serve un intervento — su cinque aree (Scope, Schedule, Budget, Quality, Risks), ognuna con una nota che motiva il colore. Nello stesso meeting si aggiorna l'Issue Log su Notion (problema, stato, responsabile, data prevista di chiusura), così nessun problema viene dimenticato.

## 5.3 Sprint Review e Retrospective

L'ultimo venerdì di ogni sprint, dalle 14:00 alle 16:00. Nella Review il team dimostra le feature completate e Giovanni le accetta o le rifiuta: **solo le feature accettate contano come "Done" ai fini dell'Earned Value**. Nella Retrospective (solo team interno, formato Start/Stop/Continue) si scelgono due action item di miglioramento per lo sprint successivo.

## 5.4 Problem Solving Strategy

Davanti a uno scostamento l'intervento segue una scala graduata: prima si valuta se lo **slack** delle attività non critiche assorbe il ritardo (le attività sul critical path hanno slack zero: lì non c'è margine); poi le leve **project manager-based** — riesame delle dipendenze, parallelizzazione, riallocazione di risorse interne; solo se il problema persiste quelle **client-based**, con un Project Impact Statement allo sponsor e opzioni come i rilasci multipli (feature spostate dalla 1.0 alla 1.1) o l'estensione della timeline. La scarsità di risorse non riguarda questo progetto: MaraffaOnline ha precedenza sull'allocazione rispetto agli altri progetti di PlayHeritage Labs.

## 5.5 Reporting: Stoplight Reports

Pubblicato su Notion ogni venerdì sera dopo lo Status Meeting. L'esempio più significativo, fine Gennaio 2026:

| Area | Colore | Nota |
|------|--------|------|
| Scope | Verde | tutte le Must Have in sviluppo; nessuna change request aperta |
| Schedule | **Giallo** | Frontend Dashboard e Creazione Stanza (attività M, sul critical path) in ritardo di 3 giorni; recovery plan attivo (pair programming Luca+Sara) |
| Budget | Verde | Cost Variance di −€300, ampiamente dentro il Contingency Buffer; saldo di cassa positivo |
| Quality | Verde | coverage sopra il target, zero bug critici |
| Risks | Verde | rischio WebSocket declassato dopo il PoC (vedi §5.10) |

## 5.6 Earned Value Management

PV, EV e AC sono tracciati mensilmente su un foglio condiviso con lo sponsor (in sola lettura), con il grafico delle tre curve. A fine Gennaio 2026 il quadro era: PV = €14.100 (l'outflow cumulato pianificato dal Cash Flow), EV = €13.200, AC = €13.500 — quindi **CV = −€300** (ore extra sull'ottimizzazione della latenza WebSocket) e **SV = −€900**, che corrisponde ai 3 giorni di ritardo della Dashboard, recuperati entro fine Febbraio con il recovery plan.

| Mese | Periodo | PV (€) | EV (€) | AC (€) | CPI | SPI |
|------|---------|-------:|-------:|-------:|----:|----:|
| 0 | Ott 2025 | 3.000 | 2.950 | 2.900 | 1,02 | 0,98 |
| 1 | Nov 2025 | 6.700 | 6.550 | 6.500 | 1,01 | 0,98 |
| 2 | Dic 2025 | 10.400 | 10.100 | 10.200 | 0,99 | 0,97 |
| 3 | Gen 2026 | 14.100 | 13.200 | 13.500 | 0,98 | 0,94 |
| 4 | Feb 2026 | 17.800 | 17.300 | 17.500 | 0,99 | 0,97 |
| 5 | Mar 2026 | 19.800 | 19.600 | 19.700 | 0,99 | 0,99 |
| 6 | Apr 2026 | 21.600 | 21.500 | 21.550 | 1,00 | 1,00 |
| 7 | Mag 2026 | 22.750 | 22.750 | 22.750 | 1,00 | 1,00 |

Lo scostamento di Gennaio si riassorbe progressivamente fino a **CPI = SPI = 1,00 alla chiusura**; il consumo finale di €22.750 lascia il surplus di €2.250 documentato nel Cap. 6.

## 5.7 Gantt Chart Tracking

Il Gantt dinamico su Notion è aggiornato ogni settimana dal PM con le percentuali di completamento raccolte nei Daily e negli Status Meeting, ed è condiviso con lo sponsor. A Gennaio mostrava l'attività M al 60% invece dell'80% atteso, con la barra rossa sul critical path: la propagazione al Frontend Tavolo (P) avrebbe minacciato il lancio del 15 Maggio, e la visualizzazione immediata è ciò che ha fatto scattare il recovery plan per tempo.

## 5.8 Velocity Tracking per Sistemi Agile

La velocity monitorata è una metrica **gestionale a livello di team**: il target di 40 story point per sprint è una capacità *team-wide*, che comprende in punti equivalenti anche il lavoro di Game Engine e Infrastructure tracciato in WBS e Gantt — non la velocity Scrum del solo Backlog. Serve a dare allo sponsor una vista unica dell'avanzamento (la riconciliazione completa dei numeri è nella relazione, Cap. 3).

Nei primi sette sprint la velocity si è mantenuta tra 35 e 42 punti, con una **media di regime di 38,3**: la stima iniziale era realistica. Due sole eccezioni, entrambe spiegate: lo **Sprint 5** (22 Dic – 2 Gen), interamente natalizio e pianificato a capacità ridotta, ha completato 21 punti con un carryover riassorbito nei due sprint successivi — ed è escluso dalla media proprio perché non rappresentativo del ritmo; lo **Sprint 7** è sceso a 36 per il ritardo della Dashboard, lo stesso episodio visibile in Stoplight, Gantt ed EVM.

## 5.9 Quality Metrics

Perché una feature sia "Done" (e maturi Earned Value) valgono quattro quality gate: test coverage di almeno l'85%, nessun bug critico aperto, code review approvata (da Elena Rossi per le parti critiche: Game Engine e sincronizzazione Real-Time), e latenza sotto i 500ms verificata con load test automatizzati su 100 partite simultanee. Agli Status Meeting Elena porta il report qualità: coverage, andamento dei bug aperti per severità e technical debt, che per policy non deve superare il 10% del tempo di sviluppo.

## 5.10 Risk Monitoring

I rischi della Risk Rating Matrix (Allegato 2.4) sono rivisti a ogni Status Meeting su un Risk Log Notion: stato (Aperto / In Mitigation / Mitigato / Materializzato), probabilità e impatto rivalutati, azioni, owner.

- **Rischio 2.1 — inesperienza WebSocket**, il più critico (rating 16): lo spike tecnico e il proof of concept dello Sprint 2 misurano una latenza di 180ms e dimezzano il rating a 8; il load test dello Sprint 6 lo chiude come "Mitigato".
- **Rischio 6.2 — scope creep**: mai materializzato; la chiarezza del POS e il rigore del Change Request Process hanno retto, e Giovanni ha accettato di rinviare alla v1.1 le richieste che avrebbero toccato il critical path.

## 5.11 Risultati del Monitoraggio

Il consuntivo del monitoraggio, rispetto alle Conditions of Satisfaction: il ritardo massimo sul critical path è stato di 3 giorni, recuperato entro Febbraio, e il lancio del 15 Maggio 2026 è stato mantenuto; il budget ha chiuso con Cost Variance nulla; le regole del gioco sono state validate da Francesca Giuliani in tre momenti (specifica a Novembre, implementazione a fine Gennaio, validazione pre-UAT in Aprile); la latenza media misurata è 185ms; la UAT ha confermato che l'80% degli utenti completa una partita senza aiuto; le retrospective hanno prodotto 30 action item di miglioramento, 28 dei quali implementati.

Grazie a questo monitoraggio multilivello il progetto, collaudato internamente, ha superato la UAT ed è arrivato pronto al lancio pubblico. L'audit formale criterio per criterio, l'accettazione e le lezioni apprese sono nel Capitolo 6 - Closing.
