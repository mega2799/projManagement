# Allegato 2.9 - User Stories
## v.1.0.0 – 2025-09-27 14:45:00

Le **User Stories** sono descrizioni concise delle funzionalità del sistema dal punto di vista dell'utente finale. Seguono il formato standard:

> **Come** [tipo di utente], **voglio** [azione/funzionalità], **così da** [beneficio/valore]

Ogni user story è validata secondo il principio **INVEST**:
- **I**ndependent (indipendente da altre storie)
- **N**egotiable (flessibile, non un contratto rigido)
- **V**aluable (valore percepibile per l'utente)
- **E**stimable (stimabile in termini di effort)
- **S**mall (piccola, completabile in uno sprint)
- **T**estable (testabile con criteri di accettazione chiari)

---

## Epic 1: Gestione Account Utente

### US-1.1: Registrazione Account 🟢 MUST HAVE

**Come** nuovo utente,
**voglio** registrarmi alla piattaforma con email e password,
**così da** poter salvare le mie statistiche e giocare con il mio profilo personalizzato.

**Criteri di Accettazione**:
- ✅ Form di registrazione con campi: email, password, conferma password, username
- ✅ Validazione email (formato corretto, univoca nel sistema)
- ✅ Password min 8 caratteri (almeno 1 maiuscola, 1 numero)
- ✅ Email di conferma inviata con link di attivazione
- ✅ Messaggio successo dopo conferma email
- ✅ Gestione errori: email già esistente, password debole

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 2
**Dipendenze**: Nessuna
**Test**: Automated (unit + integration)

---

### US-1.2: Login 🟢 MUST HAVE

**Come** utente registrato,
**voglio** effettuare il login con le mie credenziali,
**così da** accedere al mio account e giocare partite.

**Criteri di Accettazione**:
- ✅ Form di login con email e password
- ✅ Opzione "Ricordami" (mantiene sessione per 7 giorni)
- ✅ Redirect a dashboard dopo login successo
- ✅ Messaggio errore se credenziali errate (max 5 tentativi, poi blocco 15 min)
- ✅ Link "Password dimenticata?"

**Priorità**: MUST HAVE
**Story Points**: 3
**Sprint**: Sprint 2
**Dipendenze**: US-1.1
**Test**: Automated + Manual (UX flow)

---

### US-1.3: Accesso Ospite 🟢 MUST HAVE

**Come** visitatore curioso,
**voglio** provare la piattaforma senza registrarmi,
**così da** capire se il gioco mi piace prima di creare un account.

**Criteri di Accettazione**:
- ✅ Pulsante "Prova come ospite" nella homepage
- ✅ Generazione username temporaneo (es. "Ospite_4729")
- ✅ Accesso a tutte le funzionalità di gioco
- ✅ Nessun salvataggio statistiche
- ✅ Banner "Crea account per salvare progressi" visibile ma non invasivo
- ✅ Opzione conversione a account registrato dopo partita

**Priorità**: MUST HAVE
**Story Points**: 3
**Sprint**: Sprint 2
**Dipendenze**: Nessuna
**Test**: Manual (UX flow)

---

### US-1.4: Modifica Profilo 🔵 SHOULD HAVE

**Come** utente registrato,
**voglio** personalizzare il mio profilo (avatar, bio, username),
**così da** esprimere la mia identità nella community.

**Criteri di Accettazione**:
- ✅ Pagina "Impostazioni Profilo"
- ✅ Upload avatar (max 1MB, jpg/png)
- ✅ Cambio username (univocità controllata)
- ✅ Campo bio (max 200 caratteri)
- ✅ Anteprima modifiche prima del salvataggio

**Priorità**: SHOULD HAVE
**Story Points**: 5
**Sprint**: Sprint 4
**Dipendenze**: US-1.2
**Test**: Manual

---

### US-1.5: Reset Password 🔵 SHOULD HAVE

**Come** utente che ha dimenticato la password,
**voglio** ricevere un link di reset via email,
**così da** poter creare una nuova password e rientrare nel mio account.

**Criteri di Accettazione**:
- ✅ Link "Password dimenticata?" nel form login
- ✅ Invio email con token temporaneo (validità 1 ora)
- ✅ Pagina reset password con campo nuova password
- ✅ Conferma successo e redirect a login

**Priorità**: SHOULD HAVE
**Story Points**: 3
**Sprint**: Sprint 3
**Dipendenze**: US-1.1
**Test**: Manual

---

## Epic 2: Creazione e Join Partite

### US-2.1: Creazione Stanza Pubblica 🟢 MUST HAVE

**Come** giocatore,
**voglio** creare una stanza di gioco pubblica,
**così da** far unire altri giocatori casualmente e iniziare una partita.

**Criteri di Accettazione**:
- ✅ Pulsante "Crea partita" nella dashboard
- ✅ Modal/form con opzioni: nome stanza, tipo (pubblica/privata)
- ✅ Se pubblica: stanza visibile nella lobby pubblica
- ✅ Creator della stanza diventa "owner" (può kickare player)
- ✅ Lobby di attesa mostra 0/4 giocatori
- ✅ Countdown automatico quando 4/4 giocatori (10 secondi)

**Priorità**: MUST HAVE
**Story Points**: 8
**Sprint**: Sprint 3
**Dipendenze**: US-1.2
**Test**: Automated + Manual

---

### US-2.2: Creazione Stanza Privata 🟢 MUST HAVE

**Come** giocatore,
**voglio** creare una stanza privata con password,
**così da** giocare solo con amici specifici che conosco.

**Criteri di Accettazione**:
- ✅ Opzione "Privata" nel form creazione stanza
- ✅ Campo password (min 4 caratteri)
- ✅ Generazione link di invito univoco (es. `maraffaonline.it/join/ABC123`)
- ✅ Pulsante "Copia link" (clipboard API)
- ✅ Stanza NON visibile in lobby pubblica

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 3
**Dipendenze**: US-2.1
**Test**: Automated + Manual

---

### US-2.3: Join Stanza Pubblica 🟢 MUST HAVE

**Come** giocatore,
**voglio** unirmi a una stanza pubblica dalla lobby,
**così da** giocare con altri giocatori disponibili.

**Criteri di Accettazione**:
- ✅ Lista stanze pubbliche nella dashboard (filtro: stanze con posti liberi)
- ✅ Info visibili: nome stanza, giocatori connessi (X/4), owner
- ✅ Pulsante "Unisciti"
- ✅ Redirect alla lobby della stanza dopo join
- ✅ Messaggio errore se stanza piena o non più disponibile

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 3
**Dipendenze**: US-2.1
**Test**: Automated

---

### US-2.4: Join Stanza Privata Tramite Link 🟢 MUST HAVE

**Come** giocatore invitato,
**voglio** cliccare un link di invito e unirmi direttamente alla stanza,
**così da** giocare con i miei amici senza cercare manualmente.

**Criteri di Accettazione**:
- ✅ Link formato `maraffaonline.it/join/ABC123` apre modal di join
- ✅ Richiesta password (se stanza privata)
- ✅ Validazione password
- ✅ Join automatico se password corretta
- ✅ Messaggio errore se stanza piena o link non valido

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 3
**Dipendenze**: US-2.2
**Test**: Manual

---

### US-2.5: Invito Diretto Amici 🔵 SHOULD HAVE

**Come** giocatore,
**voglio** invitare direttamente un amico dalla mia lista,
**così da** non dover inviare manualmente il link.

**Criteri di Accettazione**:
- ✅ Pulsante "Invita amici" nella lobby stanza
- ✅ Lista amici online (checkbox)
- ✅ Invio notifica in-app agli amici selezionati
- ✅ Amico riceve notifica cliccabile che lo porta alla stanza

**Priorità**: SHOULD HAVE
**Story Points**: 8
**Sprint**: Sprint 5
**Dipendenze**: US-3.1 (Sistema amicizie)
**Test**: Manual

---

## Epic 3: Gameplay - Partita

### US-3.1: Avvio Partita 🟢 MUST HAVE

**Come** giocatore in lobby (4/4),
**voglio** che la partita inizi automaticamente,
**così da** non dover aspettare decisioni manuali.

**Criteri di Accettazione**:
- ✅ Countdown di 10 secondi quando 4/4 giocatori
- ✅ Messaggio "La partita inizia tra 10...9...8..."
- ✅ Distribuzione automatica 10 carte a giocatore
- ✅ Determinazione casuale primo giocatore
- ✅ Transizione a schermata tavolo da gioco
- ✅ Indicatore visivo "È il turno di [Nome]"

**Priorità**: MUST HAVE
**Story Points**: 8
**Sprint**: Sprint 4
**Dipendenze**: US-2.1, Game Engine
**Test**: Automated + Manual

---

### US-3.2: Giocare una Carta 🟢 MUST HAVE

**Come** giocatore durante il mio turno,
**voglio** cliccare una carta dalla mia mano e giocarla,
**così da** procedere con la partita.

**Criteri di Accettazione**:
- ✅ Carte nella mia mano sono cliccabili (evidenziate al hover)
- ✅ Click su carta valida: animazione carta vola al centro tavolo
- ✅ Carta giocata visibile a tutti i 4 giocatori
- ✅ Turno passa al giocatore successivo
- ✅ Non posso giocare carte durante il turno di altri
- ✅ Validazione server-side: carta deve essere legale (rispetto seme se possibile)
- ✅ Messaggio errore se carta illegale

**Priorità**: MUST HAVE
**Story Points**: 13 (complessa, integrazione real-time)
**Sprint**: Sprint 4
**Dipendenze**: US-3.1, Real-Time Communication
**Test**: Automated + Manual (critico)

---

### US-3.3: Visualizzare Punteggio 🟢 MUST HAVE

**Come** giocatore,
**voglio** vedere il punteggio aggiornato dopo ogni mano,
**così da** sapere se sto vincendo o perdendo.

**Criteri di Accettazione**:
- ✅ Barra punteggio sempre visibile: "Noi: 45 - Loro: 38"
- ✅ Aggiornamento real-time dopo ogni mano vinta
- ✅ Indicatore visivo "Mano vinta da [Coppia]" (es. banner temporaneo)
- ✅ Evidenziazione coppia in vantaggio (colore diverso)

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 4
**Dipendenze**: US-3.2, Game Engine
**Test**: Manual

---

### US-3.4: Gestione Timeout Turno 🟢 MUST HAVE

**Come** giocatore,
**voglio** che se un giocatore non gioca entro 30 secondi venga giocata automaticamente una carta casuale valida,
**così da** non bloccare la partita per colpa di un giocatore inattivo.

**Criteri di Accettazione**:
- ✅ Timer visibile durante turno (progress bar circolare, countdown)
- ✅ Avviso sonoro (opzionale) a 10 secondi rimanenti
- ✅ Se timeout scade: server gioca automaticamente carta casuale valida
- ✅ Messaggio "[Nome] ha esaurito il tempo, carta giocata automaticamente"
- ✅ Turno passa al giocatore successivo normalmente

**Priorità**: MUST HAVE
**Story Points**: 8
**Sprint**: Sprint 5
**Dipendenze**: US-3.2
**Test**: Automated + Manual

---

### US-3.5: Fine Partita e Risultato 🟢 MUST HAVE

**Come** giocatore,
**voglio** vedere una schermata di riepilogo a fine partita,
**così da** sapere chi ha vinto e le statistiche finali.

**Criteri di Accettazione**:
- ✅ Schermata "VITTORIA!" o "SCONFITTA" con animazione
- ✅ Punteggio finale: "121 - 98"
- ✅ Riepilogo mani vinte per coppia
- ✅ MVP (giocatore con più contributo punti)
- ✅ Pulsanti: "Rivincita" / "Torna alla lobby" / "Condividi risultato"
- ✅ Se rivincita: tutti i 4 devono accettare per ripartire

**Priorità**: MUST HAVE
**Story Points**: 8
**Sprint**: Sprint 5
**Dipendenze**: US-3.2, Game Engine
**Test**: Manual

---

### US-3.6: Dichiarazione "Maraffa" 🔵 SHOULD HAVE

**Come** giocatore esperto,
**voglio** dichiarare "Maraffa" quando ho 3 carte dello stesso seme,
**così da** ottenere punti bonus secondo le regole tradizionali.

**Criteri di Accettazione**:
- ✅ Pulsante "Dichiara Maraffa" visibile durante mio turno (solo se ho 3+ carte stesso seme)
- ✅ Click pulsante: mostro le 3 carte agli altri giocatori
- ✅ Bonus punti aggiunto al punteggio della coppia
- ✅ Validazione server-side: verifica effettiva presenza 3 carte

**Priorità**: SHOULD HAVE (regola tradizionale importante)
**Story Points**: 8
**Sprint**: Sprint 6
**Dipendenze**: US-3.2, validazione regole esperte Maraffa Forever
**Test**: Manual + validazione Francesca Giuliani

---

## Epic 4: Chat e Comunicazione

### US-4.1: Chat In-Game 🟢 MUST HAVE

**Come** giocatore,
**voglio** chattare con gli altri 3 giocatori durante la partita,
**così da** comunicare, scherzare e ricreare l'atmosfera sociale del gioco dal vivo.

**Criteri di Accettazione**:
- ✅ Box chat visibile nella schermata tavolo da gioco (laterale o collapsabile)
- ✅ Input testo + pulsante Invio
- ✅ Messaggi visibili in tempo reale a tutti i 4 giocatori
- ✅ Formato: "[Nome]: messaggio" con timestamp
- ✅ Throttling: max 1 messaggio/secondo per utente
- ✅ Filtro parole offensive (lista italiana)
- ✅ Chat persistente durante tutta la partita, cancellata a fine partita

**Priorità**: MUST HAVE
**Story Points**: 8
**Sprint**: Sprint 5
**Dipendenze**: Real-Time Communication (WebSocket)
**Test**: Manual + Load testing

---

### US-4.2: Chat Globale Lobby 🔸 COULD HAVE

**Come** giocatore nella dashboard,
**voglio** chattare con altri giocatori online,
**così da** socializzare mentre aspetto di entrare in partita.

**Criteri di Accettazione**:
- ✅ Box chat globale nella sidebar destra dashboard
- ✅ Messaggi pubblici visibili a tutti gli utenti online
- ✅ Throttling e moderazione come US-4.1

**Priorità**: COULD HAVE
**Story Points**: 5
**Sprint**: Backlog (post-MVP se tempo)
**Dipendenze**: US-4.1
**Test**: Manual

---

## Epic 5: Sistema Amicizie

### US-5.1: Aggiungere Amico 🔵 SHOULD HAVE

**Come** giocatore,
**voglio** cercare un altro utente per username e aggiungerlo come amico,
**così da** poterlo invitare facilmente a partite future.

**Criteri di Accettazione**:
- ✅ Pagina/sezione "Amici"
- ✅ Barra di ricerca per username
- ✅ Risultati ricerca con avatar + username
- ✅ Pulsante "Aggiungi amico" (invia richiesta)
- ✅ Notifica destinatario: "X ti ha inviato richiesta amicizia"
- ✅ Accettazione/rifiuto richiesta

**Priorità**: SHOULD HAVE
**Story Points**: 8
**Sprint**: Sprint 5
**Dipendenze**: US-1.2
**Test**: Manual

---

### US-5.2: Visualizzare Lista Amici 🔵 SHOULD HAVE

**Come** giocatore,
**voglio** vedere la lista dei miei amici con stato online/offline,
**così da** sapere chi è disponibile per giocare.

**Criteri di Accettazione**:
- ✅ Sidebar sinistra dashboard: "Amici Online" (verde) + "Amici Offline" (grigio)
- ✅ Aggiornamento real-time stato online/offline
- ✅ Click su amico: opzioni "Invita a partita" / "Visualizza profilo"

**Priorità**: SHOULD HAVE
**Story Points**: 5
**Sprint**: Sprint 5
**Dipendenze**: US-5.1
**Test**: Manual

---

## Epic 6: Statistiche e Profilo

### US-6.1: Visualizzare Statistiche Personali 🟢 MUST HAVE

**Come** giocatore registrato,
**voglio** vedere le mie statistiche (partite giocate, vinte, perse, win rate),
**così da** monitorare i miei progressi.

**Criteri di Accettazione**:
- ✅ Sezione "Le Mie Statistiche" in dashboard o profilo
- ✅ Metriche visualizzate:
  - Partite giocate
  - Partite vinte / perse
  - Win rate (%)
  - Punti totali accumulati
- ✅ Aggiornamento automatico dopo ogni partita

**Priorità**: MUST HAVE
**Story Points**: 5
**Sprint**: Sprint 6
**Dipendenze**: US-1.1, Backend persistenza dati
**Test**: Automated

---

### US-6.2: Statistiche Avanzate 🔸 COULD HAVE

**Come** giocatore appassionato di stats,
**voglio** vedere statistiche dettagliate (mani vinte, carte più giocate, ecc.),
**così da** analizzare il mio stile di gioco.

**Criteri di Accettazione**:
- ✅ Pagina "Statistiche Avanzate"
- ✅ Grafici: trend vittorie nel tempo, distribuzione carte giocate
- ✅ Confronto con media globale utenti

**Priorità**: COULD HAVE
**Story Points**: 13 (richiede analisi dati significativa)
**Sprint**: Backlog (post-MVP)
**Dipendenze**: US-6.1
**Test**: Manual

---

## Epic 7: Gestione Disconnessioni

### US-7.1: Riconnessione Automatica 🟢 MUST HAVE

**Come** giocatore che perde temporaneamente la connessione,
**voglio** potermi riconnettere automaticamente e riprendere la partita,
**così da** non perdere la partita per un problema tecnico temporaneo.

**Criteri di Accettazione**:
- ✅ Se disconnessione < 5 minuti: partita sospesa, stato salvato
- ✅ Messaggio agli altri giocatori: "[Nome] disconnesso, attendi riconnessione..."
- ✅ Tentativo automatico riconnessione lato client ogni 5 secondi
- ✅ Riconnessione: ripristino stato esatto (carte in mano, punteggio, turno corrente)
- ✅ Se > 5 minuti: partita annullata (nessun vincitore, no penalty stats)

**Priorità**: MUST HAVE
**Story Points**: 13 (complessa, critical path)
**Sprint**: Sprint 6
**Dipendenze**: Real-Time Communication, persistenza stato
**Test**: Manual (simulazione disconnessioni)

---

## Riepilogo User Stories per Sprint

### Sprint 2 (Settimane 3-4)
- US-1.1: Registrazione Account (5 pts)
- US-1.2: Login (3 pts)
- US-1.3: Accesso Ospite (3 pts)
**Total**: 11 pts

### Sprint 3 (Settimane 5-6)
- US-1.5: Reset Password (3 pts)
- US-2.1: Creazione Stanza Pubblica (8 pts)
- US-2.2: Creazione Stanza Privata (5 pts)
- US-2.3: Join Stanza Pubblica (5 pts)
- US-2.4: Join Tramite Link (5 pts)
**Total**: 26 pts

### Sprint 4 (Settimane 7-8)
- US-1.4: Modifica Profilo (5 pts)
- US-3.1: Avvio Partita (8 pts)
- US-3.2: Giocare una Carta ⭐ (13 pts - critica)
- US-3.3: Visualizzare Punteggio (5 pts)
**Total**: 31 pts

### Sprint 5 (Settimane 9-10)
- US-3.4: Timeout Turno (8 pts)
- US-3.5: Fine Partita (8 pts)
- US-4.1: Chat In-Game (8 pts)
- US-5.1: Aggiungi Amico (8 pts)
- US-5.2: Lista Amici (5 pts)
**Total**: 37 pts

### Sprint 6 (Settimane 11-12)
- US-3.6: Dichiarazione Maraffa (8 pts)
- US-6.1: Statistiche Personali (5 pts)
- US-7.1: Riconnessione Automatica (13 pts)
**Total**: 26 pts

---

## Backlog (Post-MVP, se tempo disponibile)
- US-2.5: Invito Diretto Amici (8 pts) - SHOULD HAVE
- US-4.2: Chat Globale (5 pts) - COULD HAVE
- US-6.2: Statistiche Avanzate (13 pts) - COULD HAVE

---

## Validazione Principio INVEST

Tutte le user stories sono state validate contro i criteri INVEST:

| Criterio | Verifica |
|----------|----------|
| **Independent** | ✅ Ogni story è autosufficiente (eccetto dipendenze esplicitate) |
| **Negotiable** | ✅ I criteri di accettazione sono chiari ma flessibili nei dettagli implementativi |
| **Valuable** | ✅ Ogni story porta valore percepibile all'utente o al business |
| **Estimable** | ✅ Tutte le storie hanno Story Points assegnati (Fibonacci: 3, 5, 8, 13) |
| **Small** | ✅ Nessuna story > 13 pts (max 1 sprint di lavoro) |
| **Testable** | ✅ Criteri di accettazione chiari e verificabili |

---

**Redatto da**: Marco Venturi (Project Manager) & Team PlayHeritage Labs
**Revisionato con**: Community Maraffa Forever (feedback su user experience)
**Data approvazione**: 28/09/2025
