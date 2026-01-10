# Allegato 2.7 - Prototyping
## v.2.0.0 – 2025-09-28 16:00:00

Il prototyping è un passaggio fondamentale nella fase di Scoping per validare le scelte di design dell'interfaccia utente prima dell'implementazione. Per MaraffaOnline sono state create **due iterazioni** di mockup/wireframe:

1. **Versione 1 (v1)**: Mockup iniziali con annotazioni e commenti della community
2. **Versione 2 (v2)**: Mockup finali approvati dopo incorporazione feedback

---

## Approccio Metodologico

### Co-Design Partecipativo
Il processo di prototyping ha seguito l'approccio del **co-design con la community**:
- **26/09/2025**: Workshop iniziale con 10 membri di Maraffa Forever per raccogliere requisiti UX
- **28/09/2025**: Luca Moretti (UX Designer) crea primi wireframe low-fidelity
- **01/10/2025**: Sessione di feedback con community (annotazioni su mockup v1)
- **05/10/2025**: Iterazione e creazione mockup high-fidelity v2
- **07/10/2025**: Approvazione finale da parte di Giovanni Marchetti

### Tool Utilizzati
- **Figma**: design collaborativo, wireframe e mockup high-fidelity
- **Miro**: whiteboard collaborativa per workshop iniziale
- **Loom**: video walkthrough dei mockup per utenti remoti

---

## Schermate Principali Prototipate

### 1. Homepage / Landing Page

**Obiettivo**: Prima impressione, branding, call-to-action chiara

**Mockup v1 - Feedback Ricevuti**:
- [-] "Troppo minimale, sembra una app generica di gaming"
- [-] "Manca il 'calore' della tradizione romagnola"
- [-] "Non si capisce subito che è un gioco di carte tradizionale"
- [+] "Il layout è pulito e moderno"

**Mockup v2 - Modifiche Implementate**:
- [+] Aggiunto header con pattern di carte da gioco italiane stilizzate
- [+] Palette colori ispirata ai toni caldi dell'osteria (rosso mattone, legno, verde bottiglia)
- [+] Hero section con illustrazione custom: 4 persone al tavolo da gioco (stile illustrativo, non fotografico)
- [+] Tagline: "La Maraffa tradizionale romagnola, ora online. Gioca con i tuoi amici, ovunque siano."
- [+] CTA principale: "Inizia a giocare" + "Scopri le regole" (per nuovi utenti)

**Elementi chiave**:
```
+----------------------------------------------------------+
|  [Logo MaraffaOnline]        [Accedi] [Registrati]      |
+----------------------------------------------------------+
|                                                          |
|    [Illustrazione: tavolo da gioco con 4 persone]       |
|                                                          |
|    La Maraffa tradizionale romagnola, ora online.       |
|    Gioca con i tuoi amici, ovunque siano.               |
|                                                          |
|    [   Inizia a giocare   ]  [Scopri le regole]         |
|                                                          |
+----------------------------------------------------------+
| Come funziona | Perché MaraffaOnline | Testimonianze    |
+----------------------------------------------------------+
```

**File mockup**: `img/mockup-v2-homepage.png`

---

### 2. Schermata di Registrazione/Login

**Obiettivo**: Processo di autenticazione semplice e veloce

**Mockup v1 - Feedback Ricevuti**:
- [-] "Serve anche opzione 'Gioca come ospite' per chi vuole provare subito"
- [+] "Form semplice e chiaro"

**Mockup v2 - Modifiche Implementate**:
- [+] Aggiunta opzione "Prova come ospite" (accesso temporaneo senza registrazione)
- [+] Login con email + password
- [+] Opzione "Ricordami"
- [+] Link "Password dimenticata?"
- [!] Nota: Social login (Google, Facebook) considerato "Could Have" in MoSCoW, non nel MVP

**Elementi chiave**:
```
+-------------------------------------+
|      Accedi a MaraffaOnline         |
+-------------------------------------+
| Email: [________________]           |
| Password: [________________]        |
| [ ] Ricordami                       |
|                                     |
| [       Accedi       ]              |
|                                     |
| Password dimenticata?               |
| Non hai un account? Registrati      |
|                                     |
| --- oppure ---                      |
| [  Prova come ospite  ]             |
+-------------------------------------+
```

**File mockup**: `img/mockup-v2-login.png`

---

### 3. Dashboard Utente (Lobby)

**Obiettivo**: Hub centrale post-login, accesso a partite e funzionalità sociali

**Mockup v1 - Feedback Ricevuti**:
- [-] "Vogliamo vedere subito chi è online tra gli amici"
- [-] "Manca accesso rapido alle partite in corso"
- [+] "Pulsante 'Crea partita' ben visibile"

**Mockup v2 - Modifiche Implementate**:
- [+] Sidebar sinistra: profilo utente + lista amici online
- [+] Centro: card "Partite attive" + "Crea nuova partita"
- [+] Destra: chat globale (opzionale, "Should Have")
- [+] Notifiche in tempo reale: "È il tuo turno in Partita #123"

**Elementi chiave**:
```
+----------------+---------------------------+--------------+
| Profilo        | PARTITE                   | Amici Online |
| [Avatar]       |                           |              |
| Nome Utente    | Partite in corso:         | • Marco ●    |
|                | [Partita #123 - Turno tuo]| • Giulia ●   |
| Stats:         | [Partita #124 - Aspetta]  | • Luca       |
| Vinte: 45      |                           |              |
| Perse: 38      | [+ Crea nuova partita]    | Chat Globale |
| Win%: 54%      | [+ Unisciti a partita]    | (Could Have) |
|                |                           |              |
| [Impostazioni] | Storico partite           |              |
| [Logout]       | [Vedi tutte]              |              |
+----------------+---------------------------+--------------+
```

**File mockup**: `img/mockup-v2-dashboard.png`

---

### 4. Creazione Stanza di Gioco

**Obiettivo**: Permettere di creare partite private e invitare amici specifici

**Mockup v1 - Feedback Ricevuti**:
- [-] "Dobbiamo poter impostare password per stanza privata"
- [-] "Serve opzione per invitare direttamente utenti dalla lista amici"
- [+] "Link di invito condivisibile è ottimo"

**Mockup v2 - Modifiche Implementate**:
- [+] Nome stanza personalizzabile
- [+] Opzioni: pubblica / privata (con password)
- [+] Invito tramite link condivisibile (copia/incolla)
- [+] Selezione diretta amici dalla lista (invito via notifica in-app)
- [+] Impostazioni: abilita/disabilita chat vocale (future feature)

**Elementi chiave**:
```
+----------------------------------------+
|      Crea Nuova Partita                |
+----------------------------------------+
| Nome stanza:                           |
| [es: "Partita tra amici"]              |
|                                        |
| Tipo:                                  |
| ( ) Pubblica                           |
| (•) Privata (con password)             |
|     Password: [______]                 |
|                                        |
| Invita giocatori:                      |
| [ Cerca amici...]                    |
| [ ] Marco Venturi                      |
| [ ] Giulia Rossi                       |
| [ ] Luca Bianchi                       |
|                                        |
| Link di invito:                        |
| maraffaonline.it/join/ABC123           |
| [Copia link]                           |
|                                        |
| [Annulla]          [Crea partita]      |
+----------------------------------------+
```

**File mockup**: `img/mockup-v2-crea-stanza.png`

---

### 5. Tavolo da Gioco (Partita in Corso) ⭐ SCHERMATA CRITICA

**Obiettivo**: Interfaccia principale del gioco, ricreare esperienza del tavolo fisico

**Mockup v1 - Feedback Ricevuti**:
- [-] "Le carte sono troppo piccole, difficile riconoscere i semi"
- [-] "Manca visualizzazione chiara di chi ha vinto l'ultima mano"
- [-] "Vogliamo vedere le carte giocate precedentemente nella mano"
- [+] "Disposizione 4 giocatori intorno al tavolo è intuitiva"
- [+] "Pulsante 'Gioca carta' chiaro"

**Mockup v2 - Modifiche Implementate**:
- [+] Carte ingrandite del 30%
- [+] Semi e valori ben leggibili anche su mobile
- [+] Indicatore visivo "Mano vinta da [Nome Giocatore]"
- [+] Area "Carte giocate" visibile lateralmente
- [+] Timer di turno (30 secondi) con progress bar
- [+] Indicatore latency per ogni giocatore (verde/giallo/rosso)

**Layout del tavolo**:
```
                    [Giocatore Nord]
                    (carte coperte)
                         ●●●

     [Ovest]                              [Est]
     (carte)      +------------------+    (carte)
       ●●●        |                  |      ●●●
       ●●●        |   TAVOLO DA      |      ●●●
       ●●●        |   GIOCO          |      ●●●
                  |                  |
                  | Carte giocate:   |
                  | [7♥] [A♣][2♦][R♠]|
                  +------------------+

                    [Giocatore Sud - TU]
                    []
                    ↑ Clicca carta da giocare

Timer: [========>     ] 18s
Punteggio: Noi 45 - Loro 38
Chat: [...]
```

**Elementi UX critici**:
- **Drag & Drop** vs **Click to Play**: dopo user testing, scelto Click (più affidabile su mobile)
- **Animazioni**: carte giocate volano al centro del tavolo (feedback visivo)
- **Accessibilità**: modalità "alto contrasto" per daltonici

**File mockup**: `img/mockup-v2-tavolo-gioco.png`

---

### 6. Schermata Fine Partita

**Obiettivo**: Celebrare la vittoria/sconfitta, mostrare statistiche, incentivare replay

**Mockup v1 - Feedback Ricevuti**:
- [-] "Manca riepilogo delle mani vinte/perse"
- [+] "Pulsante 'Rivincita' è fondamentale"

**Mockup v2 - Modifiche Implementate**:
- [+] Messaggio grande: "VITTORIA!" o "SCONFITTA"
- [+] Riepilogo punteggio finale
- [+] Tabella mani vinte per coppia
- [+] MVP (Most Valuable Player) - giocatore con più contributo
- [+] Pulsanti: "Rivincita" / "Torna alla lobby" / "Condividi risultato"

**Elementi chiave**:
```
+----------------------------------------+
|           VITTORIA!                |
+----------------------------------------+
| Punteggio finale: 121 - 98             |
|                                        |
| Mani vinte:                            |
| Noi: ||||||||| (9)                     |
| Loro: |||||| (6)                       |
|                                        |
| MVP: Marco Venturi (65 punti)          |
|                                        |
| [  Rivincita  ]  [Torna alla lobby]   |
|                  [Condividi ]        |
+----------------------------------------+
```

**File mockup**: `img/mockup-v2-fine-partita.png`

---

## Responsive Design - Adattamenti Mobile

**Sfida principale**: Il tavolo da gioco con 4 giocatori e 10 carte in mano deve essere usabile anche su schermi piccoli (375x667 iPhone SE).

**Soluzione v2**:
- Layout verticale anziché tavolo quadrato
- Carte in mano scrollabili orizzontalmente
- Altri giocatori mostrati con avatar minimali + numero carte rimaste
- Chat collapsabile in drawer laterale
- Pulsanti tattili grandi (min 44x44 px per accessibilità)

**File mockup mobile**: `img/mockup-v2-mobile-tavolo.png`

---

## User Testing - Risultati v2

**Data**: 10-12/10/2025
**Partecipanti**: 8 membri Maraffa Forever (età 28-42)
**Metodo**: Think Aloud Protocol + Task Completion

**Task 1**: Registrati e crea una partita privata
- [+] Success rate: 8/8 (100%)
-  Tempo medio: 2min 15sec

**Task 2**: Gioca 3 mani di Maraffa
- [+] Success rate: 8/8 (100%)
-  Tempo medio per mossa: 8 secondi
-  Commenti: "È come giocare dal vivo", "Interfaccia molto chiara"

**Task 3**: Invita un amico via link
- [+] Success rate: 7/8 (87.5%)
- [!] 1 utente non ha trovato subito il pulsante "Copia link"

**Soddisfazione generale (scala 1-5)**:
- Media: 4.6/5
- "Molto soddisfatto": 6/8
- "Soddisfatto": 2/8

---

## Approvazione Finale

**Data**: 15/10/2025
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)

**Commento ufficiale**:
> "I mockup v2 catturano perfettamente l'esperienza che volevamo: moderna ma fedele alla tradizione. L'interfaccia del tavolo da gioco è intuitiva anche per chi non è esperto di tecnologia. Siamo entusiasti di vedere il prodotto finale!"

**Modifiche residue richieste** (da implementare in fase di sviluppo):
- Aggiungere effetto sonoro per notifica "È il tuo turno" (opzionale, disattivabile)
- Considerare emoji/reactions durante la partita (Could Have, non MVP)

---

## Allegati Grafici

I seguenti file grafici sono disponibili nella cartella `img/`:

1. `mockup-v1-homepage.png` (versione iniziale con annotazioni)
2. `mockup-v2-homepage.png` (versione finale approvata)
3. `mockup-v2-login.png`
4. `mockup-v2-dashboard.png`
5. `mockup-v2-crea-stanza.png`
6. `mockup-v2-tavolo-gioco.png` 7. `mockup-v2-fine-partita.png`
8. `mockup-v2-mobile-tavolo.png` (versione mobile)
9. `style-guide-maraffaonline.png` (palette colori, tipografia, componenti)
10. `user-flow-diagram.png` (vedi Allegato 2.10)

**Formato Figma**: Il file sorgente completo è disponibile su Figma:
`https://figma.com/file/maraffaonline-design-system`

---

**Redatto da**: Luca Moretti (UX/UI Designer, PlayHeritage Labs)
**Revisionato da**: Marco Venturi (Project Manager)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 15/10/2025
