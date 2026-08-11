# Capitolo 6 - Closing

Registro operativo della chiusura del progetto MaraffaOnline (11–15 Maggio 2026). La discussione dell'approccio è nella relazione, Cap. 6.

## 6.1 Accettazione Formale

Meeting di accettazione l'**11 Maggio 2026** (quattro giorni prima del lancio pubblico del 15), durata circa due ore: Marco Venturi ha dimostrato a Giovanni Marchetti tutte le funzionalità dell'MVP — registrazione e login, creazione e join delle lobby, tavolo virtuale con giocata click-to-play e animazioni, punteggio automatico secondo le regole ufficiali, riconoscimento della Maraffa/Cricca (+3 punti), vittoria a 41 punti più una figura. Le regole risultavano validate da Francesca Giuliani in **due sessioni** (Novembre 2025: specifica; Aprile 2026: validazione finale). Giovanni ha **giocato personalmente una partita completa** con tre membri del team e ha **firmato l'accettazione senza richiedere modifiche**.

Il deploy sui server di produzione definitivi era **a carico di Maraffa Forever** fin dagli accordi contrattuali: il team tecnico della community lo ha eseguito con le Docker image e le istruzioni di deployment preparate da Andrea Conti, con supporto remoto di PlayHeritage Labs.

## 6.2 Final Project Report

Consegnato a Giovanni il **12 Maggio 2026**, redatto da Marco Venturi con Elena Rossi per la parte tecnica, pubblicato su Notion (accesso completo a sponsor e team). Nove sezioni:

1. **Executive Summary** — obiettivi raggiunti, €22.750 su €25.000, timeline rispettata
2. **Project Overview** — genesi e contesto della community
3. **Scope Management** — allegati di Scoping (2.1-2.11)
4. **Planning Documentation** — allegati di Planning (3.1-3.5)
5. **Execution & Launch** — fase di Launching (4.1-4.3)
6. **Monitoring & Control** — Stoplight, Earned Value, velocity e quality metrics
7. **Technical Architecture** — stack (Node.js, React, Socket.IO, PostgreSQL), API, schema DB
8. **Lessons Learned** — dettaglio in §6.5
9. **Appendix** — verbali, grafici, mockup approvati, codice sorgente e documentazione API

## 6.3 Audit Post-Implementazione

Condotto da Marco Venturi **insieme a Giovanni Marchetti il 13 Maggio 2026**, verificando sistematicamente ogni criterio delle Conditions of Satisfaction. Esito: **tutti gli obiettivi del POS raggiunti**.

| Criterio (CoS) | Verifica |
|---|---|
| **Temporale** — lancio 15/05/2026 | Rispettato: 7 mesi esatti, 141 giorni lavorativi di critical path. Unico scostamento: 3 giorni a Gennaio sul Frontend Dashboard (attività M), recuperati entro Febbraio con il recovery plan (pair programming Luca+Sara) |
| **Economico** — budget €25.000 | Consumo €22.750; **surplus €2.250 (9%)** destinato, d'accordo con Giovanni, al supporto post-lancio (primi 3 mesi). Tranche 50/25/25 erogate puntualmente; saldo di cassa sempre positivo (minimo €2.250 al Mese 7) |
| **Tecnico** — regole fedeli, latenza <500ms | Regole implementate secondo `REGOLE-UFFICIALI-MARAFFONE.md` validato da Francesca (punteggi, Maraffa +3, vittoria 41+figura, 4 di denari); **latenza media 185ms** ai load test con 100 partite simultanee (400 giocatori), grazie alle ottimizzazioni degli Sprint 2-4 e al PoC anticipato |
| **Qualitativo** — usabilità e soddisfazione | UAT con 10 tester (compensati €10 ciascuno, a budget): **80% completa una partita senza aiuto**; questionario dei 20 beta tester: **4,5/5** (target 4,2); user testing di Gennaio (5 membri) con migliorie implementate nello Sprint 11; mockup Figma rispettati; WCAG 2.1 AA verificata; cross-browser OK su Chrome/Firefox/Safari/Edge |
| **Gestione del lavoro** — team e processo | 15 retrospective → **30 action item, 28 implementati**; velocity di regime **38,3 SP** (Sprint 1-7, escluso il natalizio) vs target 40; nessun conflitto oltre la fase 2 (mediazione); RASCI efficace nel chiarire i ruoli |

**Oltre il concordato**, apprezzati dallo sponsor: la qualità grafica del tavolo superiore ai mockup; la **leaderboard di community (Could Have, REQ-SOC-6.3) completata e integrata nell'MVP** grazie all'efficienza del team; il tutorial interattivo "Scopri le regole" (pianificato allo Sprint 6), prezioso per l'onboarding.

## 6.4 Fattori di Successo

- **Monitoraggio multilivello** (Daily, Status Meeting con Stoplight, EVM, velocity, quality metrics) come rete di early warning: dei **17 blocker tecnici, 14 intercettati nei Daily entro 24 ore**, nessuno arrivato al post-delivery; il ritardo di Gennaio assorbito senza toccare le milestone.
- **Metodologie differenziate per sottosistema** (Allegato 2.10): Waterfall sul Game Engine, Iterativo su Backend/Frontend, Adattivo sul Real-Time, Incrementale su Social/Infrastructure.
- **Leadership del PM** (PoC sul Real-Time in Sprint 2, recovery plan di Gennaio) e **sponsor collaborativo** (presente a tutti gli Status Meeting, rispettoso del Change Request Process).
- **Competenza del team** su uno stack consolidato, con sottosistemi loosely coupled.

## 6.5 Sfide Affrontate e Lezioni Apprese

| # | Sfida | Cosa è successo | Lezione |
|---|-------|-----------------|---------|
| 1 | **Interazione carte sottostimata** | Animazioni stimate 8 SP col Planning Poker; negli Sprint 8-10 la fluidità a 60fps sincronizzata via WebSocket si è rivelata ben più complessa; assorbita col pair programming Luca+Sara | Per le feature UI interattive complesse, **prototipare già in fase di stima** per validare la fattibilità e raffinare i numeri |
| 2 | **Riclassificazione della Maraffa** | Nata Should Have; nella Sessione 1 (Novembre 2025) Francesca chiarisce che senza riconoscimento automatico la piattaforma è inadeguata al gioco competitivo → riclassificata **Must** (REQ-GE-1.1.5, con nota di revisione nella MoSCoW), implementata in "Punteggi e Maraffa" compensando sui Could Have | Il coinvolgimento dei **domain expert deve continuare durante lo sviluppo**, non fermarsi allo Scoping |
| 3 | **Cross-browser testing tardivo** | Eseguito solo allo Sprint 12: su Safari alcune animazioni CSS non funzionavano (differenze nelle transitions) → 2 giorni extra di fallback per Luca | Iniziare il cross-browser **dagli Sprint 5-6** (prime feature UI), quando c'è ancora slack |
| 4 | **Daily sincrono nei periodi remoti** | Nelle festività di Dicembre il Daily delle 09:00 creava attriti → dallo Sprint 7 uno **Slackbot** raccoglie gli update asincroni sul canale #daily entro le 10:00 | Meccanismi asincroni strutturati aumentano la resilienza anche nei team collocati |
| 5 | **Technical debt accumulato** | Test mancanti e refactoring rinviati negli Sprint 5-8, smaltiti tutti insieme nello Sprint 10 (Elena, dopo l'Integration Testing del GE) → Sprint Review 10 povera di valore visibile per lo sponsor | Allocare il **10-15% di ogni sprint** al refactoring continuo invece di uno sprint di cleanup |

## 6.6 Soddisfazione del Cliente e Sviluppi Futuri

Nel meeting di accettazione dell'11 Maggio Giovanni ha espresso interesse per tre evoluzioni, da valutare nei 12 mesi successivi:

- **App mobile nativa** (iOS/Android; era Won't Have nell'MVP, Allegato 3.2) — stima preliminare 4-5 mesi, €18.000-20.000
- **Tornei automatizzati** (bracket, classifiche, premi simbolici; era Won't Have, pianificato per la v1.1+) — 2-3 mesi, €8.000-10.000
- **Single-player contro AI** (per fare pratica, possibile uso di ML) — 3-4 mesi, €12.000-15.000

Approccio proposto da Marco: pianificazione incrementale, partendo dalle feature a maggior valore secondo le **metriche di utilizzo post-lancio**.

## 6.7 Impatto sul Business di PlayHeritage Labs

MaraffaOnline è il primo progetto completo dello spin-off e ne valida la missione. Il surplus di €2.250 contribuisce alla sostenibilità operativa; il track record on time / on budget dà credibilità; il team ha consolidato competenze sullo stack e su un mix di metodologie riutilizzabile. La relazione con la community apre a possibili progetti su altri giochi tradizionali (Tresette, Scopa, Briscola, Scopone Scientifico).

## 6.8 Celebrazione e Chiusura

Il **15 Maggio 2026**, giorno del lancio, celebrazione a budget (voce dedicata, €100): pizza e birre online via Zoom, con Giovanni presente per ringraziare il team. Dato delle **prime 24 ore: 50 registrati e 23 partite complete**, oltre le attese (20-30 utenti nella prima settimana). Marco si è impegnato a organizzare entro un mese una retrospective finale in presenza.

Il progetto si chiude con tutti i criteri di successo soddisfatti, lo stakeholder soddisfatto e prospettive concrete di collaborazione futura: la conferma che un gioco tradizionale si può digitalizzare preservandone regole e spirito, applicando il Project Management con flessibilità e pragmatismo.

---

**Data chiusura progetto**: 15 Maggio 2026
**Final Project Report**: Approvato da Giovanni Marchetti il 12 Maggio 2026
**Audit Post-Implementazione**: Completato il 13 Maggio 2026
**Status Finale**: Tutti gli obiettivi raggiunti - Progetto chiuso con successo
