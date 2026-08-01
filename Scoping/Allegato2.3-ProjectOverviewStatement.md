# Allegato 2.3 - Project Overview Statement (POS)

## v.1.1.0 – 2025-09-18 16:45

### Problema

La community "Maraffa Forever" (150 membri, ex-studenti universitari in Romagna) è geograficamente dispersa in Italia ed Europa. Non può più giocare insieme a causa della distanza fisica. Le piattaforme online esistenti sono obsolete, non mantenute o prive di multiplayer real-time, impedendo alla community di mantenere viva la tradizione ludica e le relazioni sociali.

### Opportunità

Per **PlayHeritage Labs** (spin-off UniBo specializzato in cultural heritage gaming):
- Validazione del modello di business e creazione portfolio credibile
- Materiale per pubblicazioni scientifiche e tesi di dottorato
- Contributo alla preservazione tradizione ludica regionale
- Scalabilità futura verso altri giochi regionali italiani

### Goal

Realizzare **MaraffaOnline**, piattaforma web responsive per giocare a Maraffa in multiplayer (4 giocatori real-time), ricreando fedelmente l'esperienza sociale del gioco tradizionale romagnolo.

<br>

Ogni obiettivo è associato a un numero. Criteri di successo e rischi sono correlati all'obiettivo che ha lo stesso numero.

### Obiettivi

1. Implementare un Game Engine che riproduca fedelmente le regole della Maraffa tradizionale romagnola
2. Creare un sistema di comunicazione real-time che permetta partite fluide tra 4 giocatori geograficamente distribuiti
3. Sviluppare un'interfaccia web moderna, intuitiva e responsive che richiami l'atmosfera del tavolo da gioco reale
4. Implementare funzionalità sociali (stanze private, sistema amicizie, chat) per mantenere viva la dimensione comunitaria
5. Garantire scalabilità, affidabilità e sicurezza tecnica della piattaforma
6. Lanciare un MVP funzionale entro 7 mesi con budget di €25.000

### Criteri di Successo

1. Zero errori nelle regole segnalati dagli esperti durante beta testing. Validazione formale entro il 30/10/2025.
2. Latency ≤ 500ms. Supportare 100 partite simultanee (400 giocatori). Disconnessioni < 2%.
3. Valutazione ≥ 4.2/5 sulla facilità d'uso. Nuovo utente crea/joina partita in ≤ 3 minuti. Conformità WCAG 2.1 AA.
4. Login funzionante nel 99% dei casi. Chat delay < 2s. Almeno 80 utenti attivi nei primi 2 mesi.
5. Uptime 99% mensile. API response time < 200ms (95% richieste). Conformità GDPR.
6. Completamento entro 15/05/2026. Budget €25.000 (±5%). Rilascio milestone con pagamenti scaglionati (3 tranche 50/25/25).

### Rischi

I rischi sono raggruppati per obiettivo (stesso numero della sezione Obiettivi); i due più critici sono evidenziati.

**1. Fedeltà alle regole della Maraffa**
- Incomprensioni sulle regole della Maraffa tradizionale
- Varianti regionali delle regole che potrebbero creare controversie
- Requisiti aggiuntivi scoperti durante lo sviluppo

**2. Comunicazione real-time tra i giocatori**
- Esperienza limitata del team con le tecnologie WebSocket *(rischio critico)*
- Complessità nella gestione di disconnessioni e riconnessioni
- Performance di rete variabile tra gli utenti
- Race conditions e bug di sincronizzazione dello stato tra 4 client

**3. Interfaccia web moderna e responsive**
- Difficoltà nel bilanciare modernità e familiarità dell'interfaccia
- Scarsa partecipazione alle sessioni di user testing
- Responsive design che potrebbe richiedere più tempo del previsto

**4. Funzionalità sociali**
- Integrazione della chat che potrebbe interferire con il sistema real-time
- Vulnerabilità nel sistema di autenticazione
- Gestione della privacy (GDPR) che richiede competenze legali esterne

**5. Scalabilità, affidabilità e sicurezza**
- Budget limitato per un'infrastruttura cloud scalabile
- Mancanza di esperienza del team in DevOps
- Picchi di traffico al lancio che potrebbero sovraccaricare il sistema

**6. MVP nei tempi e nel budget**
- Budget di €25.000 molto limitato per un team di 5 persone su 7 mesi *(rischio critico)*
- Scope creep da richieste del committente
- Sottostima delle complessità tecniche (in particolare il real-time)
- Assenza di buffer temporale nel calendario

### Assunzioni

- Community fornirà documentazione regole entro 25/09/2025
- 20 membri disponibili come beta tester per tutto il progetto
- Committente disponibile per meeting bi-settimanali
- Accesso infrastrutture universitarie senza costi
- Pagamenti milestone puntuali
- Utilizzo solo tecnologie open-source (no licenze a pagamento)
- Team dedicato full-time per 7 mesi
- Francesca Giuliani disponibile 2 volte/mese per consulenze
- Hosting e deployment gestiti da PlayHeritage Labs
- App mobile nativa rinviata a fase 2 post-MVP

### Ostacoli

- Competenze limitate in real-time multiplayer gaming
- Budget ristretto (€714/mese/persona)
- Dipendenza dalla partecipazione attiva della community
- Bilanciamento con impegni accademici del team
- Primo progetto PM formale per PlayHeritage Labs
- Timeline aggressiva (7 mesi)
- Difficoltà coordinamento user testing con utenti geograficamente distribuiti
- Gestione aspettative elevate della community

---

**Redatto da**: Marco Venturi (CEO & Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Lead Developer, PlayHeritage Labs)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 19/09/2025

**Storico revisioni**:
- **v.1.1.0**: Rifatta la sezione Rischi con un raggruppamento leggibile per obiettivo (la numerazione annidata precedente rendeva poco chiara la corrispondenza rischio-obiettivo); evidenziati i due rischi critici. Contenuto dei rischi invariato.
- **v.1.0.0**: Prima stesura del Project Overview Statement.
