# Allegato 2.3 - Project Overview Statement (POS)

## v.1.0.0 – 2025-09-18 16:45:12

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
6. Lanciare un MVP funzionale entro 6 mesi con budget di €25.000

### Criteri di Successo

1. Zero errori nelle regole segnalati dagli esperti durante beta testing. Validazione formale entro il 30/10/2025.
2. Latency ≤ 500ms. Supportare 100 partite simultanee (400 giocatori). Disconnessioni < 2%.
3. Valutazione ≥ 4.2/5 sulla facilità d'uso. Nuovo utente crea/joina partita in ≤ 3 minuti. Conformità WCAG 2.1 AA.
4. Login funzionante nel 99% dei casi. Chat delay < 2s. Almeno 80 utenti attivi nei primi 2 mesi.
5. Uptime 99% mensile. API response time < 200ms (95% richieste). Conformità GDPR.
6. Completamento entro 15/03/2026. Budget €25.000 (±5%). Rilascio 4 milestone con pagamenti scaglionati.

### Rischi

1. 1. Incomprensioni sulle regole della Maraffa tradizionale
   2. Varianti regionali delle regole potrebbero creare controversie
   3. Requisiti aggiuntivi scoperti durante sviluppo
2. 1. Esperienza limitata con tecnologie WebSocket (RISCHIO ALTO)
   2. Complessità nella gestione disconnessioni/riconnessioni
   3. Performance di rete variabile tra utenti
   4. Race conditions e bug di sincronizzazione stato tra 4 client
3. 1. Difficoltà nel bilanciare modernità e familiarità dell'interfaccia
   2. Scarsa partecipazione a sessioni di user testing
   3. Responsive design potrebbe richiedere più tempo del previsto
4. 1. Integrazione chat potrebbe interferire con sistema real-time
   2. Vulnerabilità nel sistema di autenticazione
   3. Gestione privacy GDPR richiede competenze legali esterne
5. 1. Budget limitato per infrastruttura cloud scalabile
   2. Mancanza esperienza team in DevOps
   3. Picchi di traffico al lancio potrebbero sovraccaricare sistema
6. 1. Budget €25.000 molto limitato per team di 5 persone per 6 mesi (RISCHIO ALTO)
   2. Scope creep da richieste committente
   3. Sottostima complessità tecniche (real-time)
   4. Assenza di buffer temporale nel calendario

### Assunzioni

- Community fornirà documentazione regole entro 25/09/2025
- 20 membri disponibili come beta tester per tutto il progetto
- Committente disponibile per meeting bi-settimanali
- Accesso infrastrutture universitarie senza costi
- Pagamenti milestone puntuali
- Utilizzo solo tecnologie open-source (no licenze a pagamento)
- Team dedicato full-time per 6 mesi
- Francesca Giuliani disponibile 2 volte/mese per consulenze
- Hosting e deployment gestiti da PlayHeritage Labs
- App mobile nativa rinviata a fase 2 post-MVP

### Ostacoli

- Competenze limitate in real-time multiplayer gaming
- Budget ristretto (€833/mese/persona)
- Dipendenza dalla partecipazione attiva della community
- Bilanciamento con impegni accademici del team
- Primo progetto PM formale per PlayHeritage Labs
- Timeline aggressiva (6 mesi)
- Difficoltà coordinamento user testing con utenti geograficamente distribuiti
- Gestione aspettative elevate della community

---

**Redatto da**: Marco Venturi (CEO & Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Lead Developer, PlayHeritage Labs)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 19/09/2025
