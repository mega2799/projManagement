# Allegato 2.3 - Project Overview Statement (POS)
## v.1.0.0 – 2025-09-18 16:45:12

### Problema
La community "Maraffa Forever", composta da 150 appassionati del gioco di carte tradizionale Maraffa, si trova dispersa geograficamente in tutta Italia e all'estero. I membri, un tempo compagni universitari in Romagna, non hanno più modo di giocare insieme a causa della distanza fisica. Le piattaforme online esistenti per la Maraffa sono:
- **Obsolete tecnologicamente** (interfacce datate, scarsa usabilità)
- **Non mantenute** (alcune non più funzionanti)
- **Limitate a single-player** contro intelligenza artificiale, perdendo completamente la dimensione sociale del gioco
- **Prive di funzionalità multiplayer real-time** per giocare con amici specifici

Questo impedisce alla community di mantenere viva la tradizione ludica e le relazioni sociali costruite attorno al gioco.

### Opportunità
Per **PlayHeritage Labs**, primo spin-off universitario dell'Università di Bologna specializzato in cultural heritage gaming, MaraffaOnline rappresenta:

1. **Validazione del Modello di Business**: primo progetto commerciale reale che permette di testare l'approccio alla digitalizzazione di giochi tradizionali e creare un portfolio credibile
2. **Ricerca Accademica**: materiale per pubblicazioni scientifiche su cultural heritage gaming, community-driven design e digitalizzazione di pratiche ludiche tradizionali. Il PM Marco Venturi utilizzerà il progetto come caso di studio per la propria tesi di dottorato
3. **Impatto Sociale**: contribuire alla preservazione di una tradizione ludica regionale e facilitare connessioni sociali significative tra persone geograficamente distanti
4. **Scalabilità Futura**: il successo di MaraffaOnline può aprire la strada a progetti simili per altri giochi regionali italiani (Briscola chiamata, Tresette, Scopone), creando un ecosistema di giochi tradizionali digitalizzati

### Goal
Realizzare **MaraffaOnline**, una piattaforma web responsive per giocare a Maraffa in multiplayer online (4 giocatori in tempo reale), che ricrei fedelmente l'esperienza sociale del gioco tradizionale romagnolo. La piattaforma deve diventare il punto di riferimento digitale per la community "Maraffa Forever" e potenzialmente per altre community di giocatori.

<br>

Ogni obiettivo è associato a un numero. Criteri di successo e rischi sono correlati all'obiettivo che ha lo stesso numero.

### Obiettivi

1. Implementare un Game Engine che riproduca fedelmente le regole della Maraffa tradizionale romagnola
2. Creare un sistema di comunicazione real-time che permetta partite fluide tra 4 giocatori geograficamente distribuiti
3. Sviluppare un'interfaccia web moderna, intuitiva e responsive che richiami l'atmosfera del tavolo da gioco reale
4. Implementare funzionalità sociali (stanze private, sistema amicizie, chat) per mantenere viva la dimensione comunitaria
5. Garantire scalabilità, affidabilità e sicurezza tecnica della piattaforma
6. Lanciare un MVP funzionale entro 6 mesi con budget di €25.000

### Criteri di Successo

1. **Game Engine**: Zero segnalazioni di errori nelle regole da parte degli esperti di Maraffa Forever durante il beta testing con 20 utenti. Validazione formale del motore di gioco da parte di Francesca Giuliani (esperta di Maraffa) entro il 30/10/2025.

2. **Real-Time Communication**: Latency massima di 500ms tra l'azione di un giocatore e l'aggiornamento dello stato per gli altri 3 giocatori. Supportare almeno 100 partite simultanee (400 giocatori concorrenti). Tasso di disconnessione < 2% durante le partite.

3. **Frontend & UX**: Valutazione media ≥ 4.2/5 da parte dei beta tester sulla facilità d'uso. Un nuovo utente deve riuscire a creare/joinare una partita entro 3 minuti dal primo accesso (misurato con user testing). Conformità WCAG 2.1 livello AA per accessibilità.

4. **Funzionalità Sociali**: Sistema di login funzionante nel 99% dei casi. Chat in-game con delay < 2 secondi. Possibilità di creare stanze private e invitare amici specifici. Almeno 80 utenti attivi della community nei primi 2 mesi post-lancio.

5. **Scalabilità e Affidabilità**: Uptime del 99% su base mensile. Tempo di risposta API < 200ms per il 95% delle richieste. Conformità GDPR per la gestione dei dati utente.

6. **Budget e Timeline**: Completamento del progetto entro il 15/03/2026. Rispetto del budget di €25.000 con scostamento massimo del ±5%. Rilascio di 4 milestone secondo calendario concordato con pagamenti scaglionati.

### Rischi

1. **Obiettivo 1 (Game Engine)**
    1. Incomprensioni sulle regole della Maraffa tradizionale potrebbero portare a implementazioni errate
    2. Varianti regionali delle regole potrebbero creare controversie su quale versione implementare
    3. Requisiti aggiuntivi scoperti durante lo sviluppo potrebbero richiedere rework significativo

2. **Obiettivo 2 (Real-Time Communication)**
    1. **Rischio ALTO**: Esperienza limitata del team con tecnologie WebSocket e sincronizzazione real-time
    2. Gestione delle disconnessioni improvvise e riconnessioni potrebbe risultare tecnicamente complessa
    3. Performance di rete variabile tra utenti (alcuni con connessioni lente) potrebbe compromettere l'esperienza
    4. Sincronizzazione dello stato di gioco tra 4 client potrebbe generare race conditions e bug difficili da debuggare

3. **Obiettivo 3 (Frontend & UX)**
    1. Difficoltà nel bilanciare modernità e familiarità: l'interfaccia deve essere moderna ma riconoscibile per giocatori tradizionali
    2. Scarsa partecipazione degli utenti alle sessioni di user testing potrebbe limitare la qualità del feedback
    3. Responsive design su tutti i dispositivi (desktop, tablet, mobile) potrebbe richiedere più tempo del previsto

4. **Obiettivo 4 (Funzionalità Sociali)**
    1. Integrazione della chat potrebbe interferire con il sistema real-time delle partite
    2. Sistema di autenticazione vulnerabile potrebbe compromettere la sicurezza dei dati utente
    3. Gestione della privacy degli utenti (GDPR) potrebbe richiedere competenze legali esterne

5. **Obiettivo 5 (Scalabilità e Affidabilità)**
    1. Budget limitato potrebbe non permettere infrastruttura cloud scalabile (costi server elevati)
    2. Mancanza di esperienza del team in DevOps potrebbe causare problemi di deployment e monitoring
    3. Picchi di traffico inattesi (es. lancio della piattaforma) potrebbero sovraccaricare il sistema

6. **Obiettivo 6 (Budget e Timeline)**
    1. **Rischio ALTO**: €25.000 è un budget molto limitato per un team di 5 persone per 6 mesi
    2. Scope creep (richieste di nuove funzionalità da parte del committente) potrebbe far sforare i tempi
    3. Sottostima delle complessità tecniche (soprattutto real-time) potrebbe causare ritardi significativi
    4. Assenza di buffer temporale nel calendario: qualsiasi ritardo impatta direttamente la deadline finale

### Assunzioni

- La community "Maraffa Forever" fornirà documentazione completa e dettagliata delle regole ufficiali della Maraffa romagnola entro il 25/09/2025
- Almeno 20 membri della community saranno disponibili come beta tester durante tutto il progetto
- Il committente (Giovanni Marchetti) sarà disponibile per meeting bi-settimanali e fornirà feedback tempestivo sulle demo
- PlayHeritage Labs ha accesso alle infrastrutture universitarie (spazi di lavoro, connessione internet) senza costi aggiuntivi
- Il pagamento delle 4 milestone avverrà puntualmente secondo il calendario concordato
- Non saranno necessarie licenze software a pagamento: tutto il progetto utilizzerà tecnologie open-source
- Il team di 5 persone di PlayHeritage Labs sarà dedicato full-time al progetto per tutta la durata (6 mesi)
- Francesca Giuliani (esperta di Maraffa) sarà disponibile per consulenze sulle regole almeno 2 volte al mese
- L'infrastruttura di hosting e deployment sarà gestita da PlayHeritage Labs (non dal committente)
- Il lancio dell'app mobile nativa (iOS/Android) è rinviato a una fase 2 post-MVP: per il lancio del 15/03/2026 ci si concentra sulla versione web responsive

### Ostacoli

- **Competenze tecniche limitate**: il team non ha esperienza pregressa in real-time multiplayer gaming, tecnologia critica per il progetto
- **Budget estremamente ristretto**: €25.000 per 5 persone per 6 mesi equivale a circa €833/mese/persona, sotto il minimo di mercato per sviluppatori
- **Dipendenza dalla community**: il successo del progetto dipende dalla disponibilità e partecipazione attiva dei beta tester
- **Bilanciamento con attività accademica**: essendo uno spin-off universitario, alcuni membri del team hanno ancora impegni di ricerca/didattica che potrebbero entrare in conflitto
- **Assenza di esperienza in Project Management formale**: questo è il primo progetto strutturato di PlayHeritage Labs, con rischio di errori organizzativi
- **Timeline aggressiva**: 6 mesi per sviluppare una piattaforma multiplayer completa è una sfida significativa
- **Reperimento utenti per user testing**: difficoltà nel coordinare sessioni di testing con utenti geograficamente distribuiti
- **Gestione delle aspettative**: la community potrebbe avere aspettative elevate difficili da soddisfare con il budget disponibile

---

**Redatto da**: Marco Venturi (CEO & Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Lead Developer, PlayHeritage Labs)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 19/09/2025
