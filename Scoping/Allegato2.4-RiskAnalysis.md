# Allegato 2.4 - Risk Analysis
## v.1.0.0 – 2025-09-19 11:20:45

Per l'analisi dei rischi si è scelto di utilizzare l'approccio **Risk Rating Matrix** che consiste nella creazione di una tabella che ha le probabilità che il rischio accada nelle righe e il livello di impatto del rischio nelle colonne.

## Risk Rating Matrix

**Range delle probabilità:**
- Range A = 0-25% (Bassa)
- Range B = 26-50% (Media-Bassa)
- Range C = 51-75% (Media-Alta)
- Range D = 76-100% (Alta)

**Livello di impatto:**
- **Trascurabile**: impatto minimo, facilmente gestibile
- **Moderato**: impatto contenuto, richiede attenzione
- **Grave**: impatto significativo su qualità/tempi/costi
- **Disastroso**: impatto critico, può compromettere il progetto

**Calcolo Valore Rischio:**
- Probabilità A=1, B=2, C=3, D=4
- Impatto Trascurabile=1, Moderato=2, Grave=3, Disastroso=4
- Valore Rischio = Probabilità × Impatto

**Colori:**
- 🟢 Verde (1-2): Rischio accettabile
- 🟡 Giallo (3-4): Rischio da monitorare
- 🟠 Arancione (6-8): Rischio significativo, richiede mitigazione
- 🔴 Rosso (9-16): Rischio critico, richiede piano di contingenza

---

## Analisi Dettagliata dei Rischi

### OBIETTIVO 1: Game Engine

#### 1.1.1 Incomprensioni sulle regole della Maraffa tradizionale
- **Sottosistema**: Game Engine
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Grave
- **Valore rischio**: 6 (2×3)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Le regole della Maraffa romagnola possono avere sfumature e interpretazioni diverse. Senza una documentazione chiara, si rischia di implementare una versione non fedele.
- **Risk Management**: **Mitigazione**. Organizzare 3 sessioni di workshop con Francesca Giuliani (esperta Maraffa Forever) nelle prime 2 settimane del progetto. Creare un documento di specifica delle regole approvato formalmente. Validare l'implementazione con partite di test supervisionate da esperti.

#### 1.1.2 Varianti regionali delle regole
- **Sottosistema**: Game Engine
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 4 (2×2)
- **Colore rischio**: 🟡 Giallo
- **Descrizione**: Esistono varianti della Maraffa in diverse zone della Romagna. Il committente potrebbe non essere allineato internamente su quale versione preferire.
- **Risk Management**: **Accept**. Definire in fase di Scoping una versione ufficiale "Maraffa Forever" e documentarla esplicitamente. Eventuali varianti saranno implementate in versioni future post-MVP.

#### 1.1.3 Requisiti aggiuntivi scoperti durante sviluppo
- **Sottosistema**: Game Engine
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Grave
- **Valore rischio**: 9 (3×3)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Durante l'implementazione potrebbero emergere casi limite o situazioni di gioco non considerate inizialmente.
- **Risk Management**: **Mitigazione**. Approccio iterativo con demo bi-settimanali per scoprire problemi rapidamente. Freeze dei requisiti dopo la milestone 1 (30/10/2025): nuove richieste andranno in backlog per versioni future. Budget di contingenza del 10% riservato per piccoli aggiustamenti.

---

### OBIETTIVO 2: Real-Time Communication

#### 2.1.1 Esperienza limitata con tecnologie WebSocket ⚠️ RISCHIO CRITICO
- **Sottosistema**: Real-Time Communication
- **Probabilità**: D (76-100%)
- **Livello di impatto**: Disastroso
- **Valore rischio**: 16 (4×4)
- **Colore rischio**: 🔴🔴 Rosso Critico
- **Descrizione**: Il team PlayHeritage Labs non ha mai sviluppato sistemi real-time multiplayer. Questa è la componente tecnicamente più complessa del progetto. Il fallimento di questo sottosistema comprometterebbe l'intero progetto.
- **Risk Management**: **Piano di Contingenza**.
    - **Fase 1 (settimane 1-2)**: Spike tecnico dedicato con Elena Rossi e Sara Bianchi. Studio intensivo di WebSocket, Socket.IO, e best practices.
    - **Fase 2 (settimane 3-4)**: Prototipo proof-of-concept con 4 client che sincronizzano stato semplificato.
    - **Decision Point (giorno 30)**: Se il prototipo non funziona, attivare piano B: assumere consulente esterno esperto real-time gaming (budget di emergenza €2.000 riservato).
    - Contatto già identificato: **Dr. Stefano Nardi** (ex-sviluppatore senior di piattaforma multiplayer, disponibile per consulenze). Vedi Allegato Contatti.

#### 2.1.2 Gestione disconnessioni e riconnessioni
- **Sottosistema**: Real-Time Communication
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Grave
- **Valore rischio**: 9 (3×3)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Un giocatore che perde la connessione durante una partita deve poter riconnettersi senza perdere lo stato di gioco. Implementare questo meccanismo è complesso.
- **Risk Management**: **Mitigazione**. Implementare sistema di "partita sospesa" che mantiene lo stato per 5 minuti. Server-side state persistence con Redis. Testing intensivo di scenari di disconnessione durante beta testing.

#### 2.1.3 Performance di rete variabile tra utenti
- **Sottosistema**: Real-Time Communication
- **Probabilità**: D (76-100%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 8 (4×2)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Alcuni utenti potrebbero avere connessioni lente (es. ADSL rurale). Questo potrebbe creare latency elevata e frustrare gli altri giocatori.
- **Risk Management**: **Mitigazione**. Implementare sistema di "quality of connection" indicator. Mostrare latency di ogni giocatore prima di iniziare la partita. Ottimizzare dimensione dei messaggi WebSocket (compressione dati). Requisito minimo di connessione: 2 Mbps.

#### 2.1.4 Race conditions e sincronizzazione stato
- **Sottosistema**: Real-Time Communication
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Disastroso
- **Valore rischio**: 12 (3×4)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Con 4 client che comunicano, potrebbero verificarsi race conditions dove due giocatori fanno azioni simultanee incompatibili. Bug di sincronizzazione potrebbero portare a stati di gioco inconsistenti tra i client.
- **Risk Management**: **Mitigazione**. Architettura server-authoritative: il server è l'unica fonte di verità per lo stato del gioco. I client inviano solo "intenzioni", il server valida e aggiorna. Implementare extensive logging per debug. Code review obbligatoria su tutto il codice real-time.

---

### OBIETTIVO 3: Frontend & UX

#### 3.1.1 Bilanciare modernità e familiarità
- **Sottosistema**: Frontend Web
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Grave
- **Valore rischio**: 6 (2×3)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Il target (25-45 anni) include sia nativi digitali sia persone abituate al gioco fisico. L'interfaccia deve essere moderna ma non alienante rispetto all'esperienza tradizionale.
- **Risk Management**: **Mitigazione**. Condurre sessioni di co-design con 10 utenti rappresentativi. Creare 2 versioni alternative di mockup e farle votare alla community. Ispirarsi a piattaforme di successo (es. Board Game Arena) mantenendo identità visiva legata alla tradizione romagnola.

#### 3.1.2 Scarsa partecipazione a user testing
- **Sottosistema**: Frontend Web
- **Probabilità**: A (0-25%)
- **Livello di impatto**: Grave
- **Valore rischio**: 3 (1×3)
- **Colore rischio**: 🟡 Giallo
- **Descrizione**: Se i beta tester non partecipano attivamente, il feedback sarà insufficiente e la UX potrebbe risultare inadeguata.
- **Risk Management**: **Mitigazione**. Coinvolgere i beta tester fin dall'inizio del progetto (non solo a fine sviluppo). Offrire incentivi: accesso anticipato, riconoscimento nei credits, gadget Maraffa Forever. Schedulare sessioni brevi (30 min) per ridurre l'impegno richiesto.

#### 3.1.3 Responsive design su tutti i dispositivi
- **Sottosistema**: Frontend Web
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 4 (2×2)
- **Colore rischio**: 🟡 Giallo
- **Descrizione**: Ottimizzare l'interfaccia del tavolo da gioco per schermi piccoli (mobile) potrebbe richiedere riprogettazione significativa.
- **Risk Management**: **Mitigazione**. Approccio mobile-first: progettare prima per schermi piccoli, poi adattare a desktop. Utilizzare framework responsive consolidato (es. Tailwind CSS). Testing su device reali (iOS, Android, tablet) durante tutto lo sviluppo.

---

### OBIETTIVO 4: Funzionalità Sociali

#### 4.1.1 Integrazione chat con sistema real-time
- **Sottosistema**: Social & Community
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 6 (3×2)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: La chat in-game deve funzionare parallelamente al sistema WebSocket delle partite senza interferenze o sovraccarichi.
- **Risk Management**: **Mitigazione**. Utilizzare lo stesso canale WebSocket per chat e game state (evitare multiple connessioni). Implementare throttling dei messaggi chat (max 1 messaggio/secondo per utente) per evitare spam e sovraccarico.

#### 4.1.2 Vulnerabilità nel sistema di autenticazione
- **Sottosistema**: Backend Server (User Management)
- **Probabilità**: A (0-25%)
- **Livello di impatto**: Disastroso
- **Valore rischio**: 4 (1×4)
- **Colore rischio**: 🟡 Giallo
- **Descrizione**: Dati utente compromessi o accessi non autorizzati danneggerebbero gravemente la reputazione del progetto.
- **Risk Management**: **Piano di Contingenza**. Utilizzare librerie di autenticazione consolidate (es. Passport.js, JWT). Password hashing con bcrypt. HTTPS obbligatorio. Penetration testing prima del lancio. Piano di incident response pronto: in caso di breach, notifica utenti entro 24h come da GDPR.

#### 4.1.3 Gestione privacy e GDPR
- **Sottosistema**: Backend Server
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Grave
- **Valore rischio**: 6 (2×3)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Il team non ha competenze legali specifiche su GDPR. Errori nella gestione dati potrebbero portare a sanzioni.
- **Risk Management**: **Mitigazione**. Consultare l'ufficio legale dell'Università di Bologna (servizio gratuito per spin-off). Implementare: privacy policy, cookie consent, diritto all'oblio (cancellazione account), data minimization (raccogliere solo dati strettamente necessari).

---

### OBIETTIVO 5: Scalabilità e Affidabilità

#### 5.1.1 Budget limitato per infrastruttura cloud
- **Sottosistema**: Infrastructure & DevOps
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Grave
- **Valore rischio**: 9 (3×3)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Servizi cloud con auto-scaling (AWS, Google Cloud) sono costosi. Il budget del progetto potrebbe non coprire i costi operativi mensili.
- **Risk Management**: **Mitigazione**. Strategia ibrida:
    - Hosting iniziale su server dedicato (Hetzner, OVH) a costo fisso basso (€50/mese)
    - Architettura predisposta per cloud migration se il progetto avrà successo post-lancio
    - Monitoraggio costi mensili strict con alert automatici
    - Ottimizzazione database (caching, query optimization) per ridurre risorse necessarie

#### 5.1.2 Esperienza limitata in DevOps
- **Sottosistema**: Infrastructure & DevOps
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 4 (2×2)
- **Colore rischio**: 🟡 Giallo
- **Descrizione**: Andrea Conti (DevOps specialist) ha competenze teoriche ma esperienza pratica limitata su deployment production-ready.
- **Risk Management**: **Mitigazione**. Utilizzare Platform-as-a-Service (PaaS) come Heroku o Railway per semplificare deployment. Adottare Docker per consistency tra ambienti. Implementare CI/CD pipeline con GitLab CI. Documentare ogni step di deployment.

#### 5.1.3 Picchi di traffico al lancio
- **Sottosistema**: Infrastructure & DevOps
- **Probabilità**: D (76-100%)
- **Livello di impatto**: Moderato
- **Valore rischio**: 8 (4×2)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Al lancio della piattaforma (15/03/2026), la community Maraffa Forever (150 persone) proverà ad accedere simultaneamente. Il sistema potrebbe non reggere il carico.
- **Risk Management**: **Mitigazione**. Load testing pre-lancio con strumenti come k6 o Artillery. Soft launch graduale: prima 20 beta tester, poi 50, poi 100, infine tutti. Implementare rate limiting e queue system. Comunicare alla community orari di accesso scaglionati.

---

### OBIETTIVO 6: Budget e Timeline

#### 6.1.1 Budget insufficiente per team di 5 persone ⚠️ RISCHIO CRITICO
- **Sottosistema**: Project Management
- **Probabilità**: D (76-100%)
- **Livello di impatto**: Disastroso
- **Valore rischio**: 16 (4×4)
- **Colore rischio**: 🔴🔴 Rosso Critico
- **Descrizione**: €25.000 per 5 persone per 6 mesi = €833/mese/persona, molto sotto la media di mercato per sviluppatori (€2.500-3.000/mese). Il team potrebbe demotivarsi o abbandonare il progetto.
- **Risk Management**: **Accept con consapevolezza**. PlayHeritage Labs accetta il budget limitato perché:
    1. È un progetto pilota con valore strategico oltre al profitto immediato
    2. Genera materiale per ricerca accademica (tesi dottorato, pubblicazioni)
    3. Crea portfolio credibile per futuri clienti
    4. Il team lavora part-time (50% FTE), mantenendo altre attività accademiche

    **Contingenza**: Se il progetto ha successo, negoziare con Maraffa Forever un contratto di manutenzione post-lancio (€500/mese) per garantire sostenibilità.

#### 6.1.2 Scope creep da richieste committente
- **Sottosistema**: Project Management
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Disastroso
- **Valore rischio**: 12 (3×4)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Il committente potrebbe richiedere nuove funzionalità durante lo sviluppo (es. "vogliamo anche tornei", "aggiungiamo modalità spettatore"), facendo esplodere lo scope.
- **Risk Management**: **Mitigazione**. Change Control Process rigoroso:
    1. Freeze dei requisiti dopo approvazione POS (22/09/2025)
    2. Ogni nuova richiesta passa attraverso Change Request Form
    3. Valutazione impact su tempi/costi
    4. Se approvata, negoziare: o estensione timeline, o incremento budget, o rimozione altra feature
    5. Product backlog per feature future (post-MVP)

#### 6.1.3 Sottostima complessità tecnica
- **Sottosistema**: Real-Time Communication, Frontend Web
- **Probabilità**: C (51-75%)
- **Livello di impatto**: Grave
- **Valore rischio**: 9 (3×3)
- **Colore rischio**: 🔴 Rosso
- **Descrizione**: Le stime iniziali potrebbero essere ottimistiche, specialmente per il real-time multiplayer. Ritardi tecnici si accumulano e compromettono la deadline.
- **Risk Management**: **Mitigazione**.
    - Agile iterativo per adattare le stime durante lo sviluppo
    - Buffer di contingenza del 20% su ogni stima (regola del planning poker)
    - Weekly retrospective per identificare rapidamente problemi
    - Se a metà progetto (15/12) si è in ritardo >15%, attivare piano B: ridurre scope (es. rimuovere statistiche/classifiche, rimandare a v1.1)

#### 6.1.4 Assenza di buffer temporale
- **Sottosistema**: Project Management
- **Probabilità**: B (26-50%)
- **Livello di impatto**: Grave
- **Valore rischio**: 6 (2×3)
- **Colore rischio**: 🟠 Arancione
- **Descrizione**: Il calendario è serrato: 6 mesi netti senza margini per imprevisti (malattia, bug critici, ritardi fornitori).
- **Risk Management**: **Mitigazione**. MoSCoW prioritization ferrea: concentrarsi sui Must Have, considerare Should/Could Have come opzionali. Completare i sottosistemi critici (1-2-3-4) entro gennaio, lasciando febbraio-marzo per testing, bug fixing e polish. Se necessario, lanciare MVP con feature ridotte ma funzionanti.

---

## Riepilogo Rischi Critici (Valore ≥ 12)

| Rischio | Sottosistema | Valore | Strategia |
|---------|--------------|--------|-----------|
| Esperienza limitata WebSocket | Real-Time Communication | 16 🔴🔴 | Piano di Contingenza (consulente esterno) |
| Budget insufficiente | Project Management | 16 🔴🔴 | Accept (valore strategico) |
| Race conditions sincronizzazione | Real-Time Communication | 12 🔴 | Mitigazione (server-authoritative) |
| Scope creep | Project Management | 12 🔴 | Mitigazione (change control) |

---

**Redatto da**: Elena Rossi (Lead Developer, PlayHeritage Labs)
**Revisionato da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Data approvazione**: 20/09/2025
