# Allegato 2.12 - Scoping Approval Process
## v.1.0.0 – 2025-10-02 15:00:00

Questo documento descrive il processo formale di approvazione della **Fase di Scoping** del progetto MaraffaOnline, che conclude la prima fase del progetto e autorizza il passaggio alla Fase di Planning.

---

## Meeting di Approvazione Scoping

### Informazioni Generali

**Data**: 2 ottobre 2025
**Orario**: 14:00 - 17:00 (3 ore)
**Luogo**: Sala Riunioni "Heritage Lab" + Videoconferenza Zoom
**Modalità**: Ibrida (3 presenti, 4 remoti)

### Partecipanti

| Nome | Ruolo | Organizzazione | Presenza | Voto |
|------|-------|----------------|----------|------|
| **Giovanni Marchetti** | Project Sponsor | Maraffa Forever | Videoconferenza | ✅ Decisionale |
| **Francesca Giuliani** | Esperta Maraffa & Beta Tester Lead | Maraffa Forever | Videoconferenza | 🔹 Consultivo |
| **Marco Venturi** | CEO & Project Manager | PlayHeritage Labs | Presenza fisica | 🔹 Consultivo |
| **Elena Rossi** | Lead Developer | PlayHeritage Labs | Presenza fisica | 🔹 Consultivo |
| **Luca Moretti** | UX/UI Designer | PlayHeritage Labs | Presenza fisica | 🔹 Consultivo |
| **Sara Bianchi** | Backend Developer | PlayHeritage Labs | Videoconferenza | 🔹 Consultivo |
| **Andrea Conti** | DevOps Specialist | PlayHeritage Labs | Videoconferenza | 🔹 Consultivo |

**Legenda voto**:
- ✅ Decisionale: ha potere di approvazione/rifiuto
- 🔹 Consultivo: fornisce parere ma non blocca decisione

---

## Agenda del Meeting

### 1. Apertura e Recap Obiettivi (14:00 - 14:15)

**Conduttore**: Marco Venturi

**Contenuti**:
- Benvenuto e ringraziamento ai partecipanti
- Recap obiettivi fase di Scoping:
  - Definire chiaramente COSA deve essere costruito
  - Allineare aspettative tra PlayHeritage Labs e Maraffa Forever
  - Identificare rischi e vincoli prima di investire in sviluppo
  - Ottenere approvazione formale per procedere a Planning
- Panoramica documenti prodotti (12 allegati)

**Outcome**: Tutti allineati su scopo del meeting

---

### 2. Presentazione Documenti di Scoping (14:15 - 15:30)

**Conduttore**: Marco Venturi (con contributi di team members)

#### 2.1 Project Overview Statement (Allegato 2.3)
**Presentato da**: Marco Venturi
**Durata**: 10 minuti

**Punti chiave presentati**:
- **Problema**: Community dispersa geograficamente, nessuna piattaforma moderna per Maraffa online
- **Opportunità**: Validazione modello business PlayHeritage Labs + ricerca accademica
- **Goal**: Piattaforma web responsive multiplayer per Maraffa romagnola
- **6 Obiettivi principali** con criteri di successo e rischi

**Domande/Commenti Giovanni Marchetti**:
> "L'obiettivo 4 sulle funzionalità sociali è critico per noi. La chat in-game è davvero Must Have?"

**Risposta Marco Venturi**:
> "Sì, confermato Must Have. È nel core della richiesta: ricreare l'esperienza sociale del tavolo da gioco. Senza chat, perderemmo questo aspetto."

**Approvazione parziale**: ✅ Giovanni approva POS

---

#### 2.2 Conditions of Satisfaction (Allegato 2.2)
**Presentato da**: Marco Venturi
**Durata**: 10 minuti

**Punti chiave**:
- Timeline: 7 milestone temporali (ultima: 15/05/2026)
- Budget: €25.000 con 4 tranche di pagamento
- Requisiti tecnici: scalabilità 100 partite simultanee, latency < 500ms
- Requisiti qualitativi: soddisfazione beta tester ≥ 4.2/5

**Domande/Commenti Giovanni Marchetti**:
> "La latency di 500ms è sufficiente? Vorremmo un'esperienza fluida."

**Risposta Elena Rossi**:
> "500ms è un target conservativo. Punteremo a < 300ms, ma 500ms è il limite di accettabilità. Per confronto, un blink umano è 300-400ms, quindi imperceptibile."

**Approvazione parziale**: ✅ Giovanni approva Conditions of Satisfaction

---

#### 2.3 Risk Analysis (Allegato 2.4)
**Presentato da**: Elena Rossi
**Durata**: 15 minuti

**Rischi critici evidenziati** (Valore 16/16):
1. **Esperienza limitata WebSocket**: Piano di contingenza con consulente Dr. Stefano Nardi
2. **Budget insufficiente**: Accettato per valore strategico progetto

**Domande/Commenti Francesca Giuliani**:
> "Sono preoccupata per il rischio 'Varianti regionali delle regole'. Come gestirete questo?"

**Risposta Marco Venturi**:
> "Abbiamo concordato di implementare la versione 'Maraffa Forever' ufficiale, documentata da te. Eventuali varianti saranno features future post-MVP. Questo è scritto nel Risk Management dell'allegato 2.4."

**Approvazione parziale**: ✅ Giovanni approva Risk Analysis con nota: "Monitorare strettamente rischio WebSocket"

---

#### 2.4 Business Model Canvas & SWOT (Allegati 2.5, 2.6)
**Presentato da**: Marco Venturi + Luca Moretti
**Durata**: 10 minuti

**Business Model Canvas - Highlights**:
- Revenue Streams: €25k progetto + potenziale €500/mese manutenzione post-lancio
- Key Partnerships: UniBo, Maraffa Forever, consulenti tecnici
- Value Proposition: riconnessione sociale + fedeltà tradizione

**SWOT - Highlights**:
- **Strengths**: Team multidisciplinare, supporto UniBo, community attiva
- **Weaknesses**: Esperienza limitata real-time (W1 - critico)
- **Opportunities**: Mercato inesplorato giochi tradizionali, pubblicazioni scientifiche
- **Threats**: Fallimento tecnico real-time (T1 - critico)

**Commenti Giovanni Marchetti**:
> "Apprezzo la trasparenza sui Weaknesses. Confidate di riuscire nonostante l'esperienza limitata?"

**Risposta Marco Venturi**:
> "Sì. Abbiamo identificato il rischio early, preparato piano di contingenza con esperto esterno, e avremo decision point al giorno 30. Non procederemo 'a speranza' ma con validazione continua."

**Approvazione parziale**: ✅ Giovanni approva BMC e SWOT

---

**PAUSA CAFFÈ (15:30 - 15:45)**

---

#### 2.5 Prototyping & User Flow (Allegati 2.7, 2.10)
**Presentato da**: Luca Moretti
**Durata**: 20 minuti

**Demo visiva**:
- Presentazione mockup v2 approvati (homepage, login, dashboard, tavolo da gioco)
- Walkthrough User Flow: da registrazione a fine partita
- Video recording user testing (Think Aloud Protocol con 8 beta tester)

**Feedback Francesca Giuliani**:
> "I mockup del tavolo da gioco sono fantastici! Catturano perfettamente l'atmosfera. Confermo approvazione."

**Feedback Giovanni Marchetti**:
> "Ottimo lavoro. Una richiesta: il pulsante 'Rivincita' deve essere molto visibile a fine partita, è una feature che useremo spesso."

**Risposta Luca Moretti**:
> "Preso nota. Lo renderemo prominente nella schermata fine partita, come mostrato nel mockup v2."

**Approvazione parziale**: ✅ Giovanni approva Prototyping e User Flow

---

#### 2.6 Requirements Breakdown Structure (Allegato 2.8)
**Presentato da**: Marco Venturi + Elena Rossi
**Durata**: 15 minuti

**Overview**:
- 7 sottosistemi dettagliati con requisiti funzionali, non funzionali, vincoli
- Prioritizzazione MoSCoW:
  - **Must Have**: Game Engine, Backend, Real-Time, Frontend, Chat in-game, Infrastructure
  - **Should Have**: Sistema amicizie, statistiche base
  - **Could Have**: Chat globale, classifiche
  - **Won't Have** (MVP): App mobile nativa, social login, tornei

**Domande/Commenti Giovanni Marchetti**:
> "Il sistema amicizie è 'Should Have', non 'Must Have'. Questo significa che potrebbe non esserci al lancio?"

**Risposta Marco Venturi**:
> "Should Have significa 'altamente desiderabile e ci impegniamo a farlo', ma se incontriamo ritardi critici, potremmo rinviarlo a versione 1.1 per rispettare la deadline del 15/03. Must Have invece è non negoziabile. Ma il nostro obiettivo è completare tutti i Should Have."

**Approvazione parziale**: ✅ Giovanni approva RBS con riserva: "Sistema amicizie è importante per la community, fate del vostro meglio per includerlo"

---

#### 2.7 User Stories (Allegato 2.9)
**Presentato da**: Sara Bianchi + Luca Moretti
**Durata**: 10 minuti

**Overview**:
- 7 Epic, 20+ User Stories
- Tutte validate secondo principio INVEST
- Story Points assegnati (Fibonacci: 3, 5, 8, 13)
- Organizzate per Sprint (Sprint 2-6)

**Highlight User Story critica**:
- **US-3.2: Giocare una Carta** (13 pts, Sprint 4)
  - User story più complessa, integra real-time + validazione regole
  - Critical path del progetto

**Approvazione parziale**: ✅ Giovanni approva User Stories

---

#### 2.8 PM Life Cycle Models (Allegato 2.11)
**Presentato da**: Marco Venturi
**Durata**: 15 minuti

**Approccio ibrido spiegato**:
- **Waterfall** per Game Engine (requisiti stabili)
- **Agile Iterativo** per Backend e Frontend (feedback continuo)
- **Agile Adattivo** per Real-Time (alta incertezza)
- **Incrementale** per Social Features e Infrastructure

**Domande/Commenti Giovanni Marchetti**:
> "Non è confusionario usare metodologie diverse? Come le coordinate?"

**Risposta Marco Venturi**:
> "Ottima domanda. Pur usando approcci diversi internamente, tutti i sottosistemi seguono sprint bi-settimanali comuni e demo al committente ogni 2 settimane. Questo garantisce sincronizzazione. È un approccio pragmatico: ogni sottosistema usa il metodo più efficace per le sue caratteristiche."

**Approvazione parziale**: ✅ Giovanni approva Metodologie (con fiducia nel team)

---

### 3. Discussione Aperta e Domande (16:15 - 16:45)

**Facilitatore**: Marco Venturi

#### Domanda 1 - Giovanni Marchetti:
> "Sono preoccupato per il budget di €25.000. È davvero sufficiente? Preferisco sapere ora se servono più soldi piuttosto che scoprirlo a metà progetto."

**Risposta Marco Venturi**:
> "È un budget molto limitato, lo riconosciamo apertamente. Ma per noi questo progetto ha valore oltre il profitto: ricerca accademica, portfolio, pubblicazioni. Abbiamo accettato consapevolmente. Il budget copre i costi operativi essenziali. Se emergono costi imprevisti (es. consulente WebSocket €2.000), li gestiamo internamente attingendo al 10% di contingenza già previsto."

**Approfondimento Elena Rossi**:
> "Per trasparenza: il team lavora part-time (50% FTE), bilanciando con altre attività accademiche. Questo rende il budget sostenibile. Non stiamo sacrificando qualità, ma ottimizzando efficienza."

**Risposta Giovanni**:
> "Apprezzo la trasparenza. Va bene, procediamo così. Ma teneteci aggiornati se incontrate problemi."

---

#### Domanda 2 - Francesca Giuliani:
> "Quando inizierete a coinvolgere i 20 beta tester? Vorrei prepararli."

**Risposta Luca Moretti**:
> "Beta testing iterativo inizierà da Sprint 3 (metà novembre). I primi test saranno su mockup interattivi e prime funzionalità (login, creazione stanza). Il testing intensivo del gameplay sarà Sprint 4-5 (dicembre-gennaio). Ti invieremo calendario dettagliato dopo approvazione Planning."

**Risposta Francesca**:
> "Perfetto. Preparerò i 20 volontari. Molti sono entusiasti di partecipare."

---

#### Domanda 3 - Giovanni Marchetti:
> "Cosa succede se al 'decision point' del giorno 30 sul WebSocket lo spike tecnico fallisce?"

**Risposta Elena Rossi**:
> "Attiviamo immediatamente il piano di contingenza: contrattiamo Dr. Stefano Nardi (consulente esperto real-time multiplayer già identificato). Abbiamo budget di emergenza €2.000 riservato. Se anche con il consulente non funziona entro altre 2 settimane (giorno 45), allora è escalation critica: meeting straordinario con voi per decidere se pivot architettura o altro."

**Risposta Marco Venturi**:
> "Saremo trasparenti. Non vi nasconderemo problemi. Comunicazione continua ogni 2 settimane proprio per questo."

**Risposta Giovanni**:
> "Bene. Fiducia totale, ma comunicazione trasparente è fondamentale."

---

#### Commento - Sara Bianchi:
> "Voglio sottolineare che, nonostante le sfide, siamo un team motivato e competente. Questo progetto ci appassiona non solo professionalmente ma anche personalmente. Crediamo nel valore culturale della Maraffa."

**Risposta Giovanni**:
> "Si vede. È uno dei motivi per cui abbiamo scelto voi. Andiamo avanti!"

---

### 4. Revisione Checklist Approvazione (16:45 - 16:55)

**Conduttore**: Marco Venturi

Verifica che tutti i deliverable della fase di Scoping siano completi e approvati:

| # | Allegato | Stato | Approvazione Giovanni |
|---|----------|-------|----------------------|
| 2.1 | Project Scoping Meeting | ✅ Completo | ✅ Approvato |
| 2.2 | Conditions of Satisfaction | ✅ Completo | ✅ Approvato |
| 2.3 | Project Overview Statement (POS) | ✅ Completo | ✅ Approvato |
| 2.4 | Risk Analysis | ✅ Completo | ✅ Approvato (con monitoraggio) |
| 2.5 | Business Model Canvas | ✅ Completo | ✅ Approvato |
| 2.6 | Analisi SWOT | ✅ Completo | ✅ Approvato |
| 2.7 | Prototyping | ✅ Completo | ✅ Approvato |
| 2.8 | Requirements Breakdown Structure | ✅ Completo | ✅ Approvato (con nota amicizie) |
| 2.9 | User Stories | ✅ Completo | ✅ Approvato |
| 2.10 | User Flow | ✅ Completo | ✅ Approvato |
| 2.11 | PM Life Cycle Models | ✅ Completo | ✅ Approvato |
| 2.12 | Approval Process (questo documento) | ✅ In compilazione | ⏳ In attesa firma |

**Verifica completezza**: ✅ Tutti i 12 allegati presenti e approvati

---

### 5. Approvazione Formale e Firma (16:55 - 17:00)

**Decisione Finale - Giovanni Marchetti (Project Sponsor)**:

> "Dopo aver esaminato tutti i documenti di Scoping e discusso apertamente rischi e aspettative, sono soddisfatto del lavoro svolto da PlayHeritage Labs. La fase di Scoping è stata condotta con professionalità, trasparenza e attenzione ai dettagli.
>
> **Approvo formalmente** la conclusione della Fase di Scoping e autorizzo il passaggio alla **Fase di Planning**.
>
> Confermo inoltre il pagamento della **prima tranche di €6.250** come da accordi (milestone: completamento Scoping entro 30/09/2025 - completata in anticipo il 02/10/2025).
>
> Auguro buon lavoro al team e confido nel successo del progetto MaraffaOnline!"

**Applauso e ringraziamenti reciproci**

---

## Firma Digitale del Documento

**Project Sponsor (Committente)**:

```
Nome: Giovanni Marchetti
Ruolo: Rappresentante Community Maraffa Forever
Data: 02/10/2025
Firma: [Firma digitale]

Approvazione: ✅ APPROVATA
```

**Project Manager (Fornitore)**:

```
Nome: Marco Venturi
Ruolo: CEO & Project Manager, PlayHeritage Labs
Data: 02/10/2025
Firma: [Firma digitale]

Impegno: Procedere con Fase di Planning entro 05/10/2025
```

---

## Decisioni e Action Items Post-Approvazione

### Decisioni Prese

| # | Decisione | Responsabile | Scadenza |
|---|-----------|--------------|----------|
| 1 | Approvata Fase di Scoping completa | Giovanni Marchetti | ✅ 02/10/2025 |
| 2 | Autorizzato passaggio a Fase di Planning | Giovanni Marchetti | ✅ 02/10/2025 |
| 3 | Confermato pagamento 1° tranche €6.250 | Giovanni Marchetti | 10/10/2025 |
| 4 | Monitoraggio speciale rischio WebSocket | Marco Venturi | Continuo |
| 5 | Sistema amicizie priorità alta (Should Have) | Marco Venturi | Pianificazione Sprint |

### Action Items

| # | Azione | Assegnato a | Scadenza | Stato |
|---|--------|-------------|----------|-------|
| 1 | Emettere fattura 1° tranche (€6.250) | Marco Venturi | 05/10/2025 | Not started |
| 2 | Iniziare Fase di Planning (WBS, Moscow, Gantt) | Team PlayHeritage Labs | 05/10/2025 | Not started |
| 3 | Inviare calendario beta testing a Francesca | Luca Moretti | 15/10/2025 | Not started |
| 4 | Archiviare tutti allegati Scoping in repository | Andrea Conti | 03/10/2025 | Not started |
| 5 | Preparare slide per Kick-Off Meeting (fase Launching) | Marco Venturi | 20/10/2025 | Not started |
| 6 | Contattare Dr. Stefano Nardi (consulente WebSocket) per pre-allerta | Elena Rossi | 10/10/2025 | Not started |

---

## Milestone Raggiunta

🎉 **MILESTONE 1 COMPLETATA: Fase di Scoping**

- **Data prevista**: 30/09/2025
- **Data effettiva**: 02/10/2025
- **Scostamento**: +2 giorni (trascurabile, entro margine)
- **Budget consumato**: €0 (fase interna PlayHeritage Labs)
- **Qualità**: Alta (approvazione senza riserve critiche)
- **Pagamento**: €6.250 autorizzato

**Status progetto**: 🟢 VERDE (on track)

---

## Prossime Tappe

### Fase 2: Planning (5-20 Ottobre 2025)

Obiettivi:
1. Creare Work Breakdown Structure (WBS) dettagliata
2. Applicare MoSCoW Analysis ai requisiti
3. Eseguire stime (Delphi Technique + Planning Poker)
4. Definire Product Backlog per sottosistemi Agile
5. Pianificare Cash Flow Management
6. Creare Project Network Diagram e Gantt Chart
7. Ottenere approvazione Planning da Giovanni Marchetti

**Deliverable Planning**: 6 allegati (vedi CLAUDE.md, sezione Planning)

**Prossimo meeting committente**: 20/10/2025 (Approval Planning)

---

## Appendice: Feedback Qualitativo

### Feedback Giovanni Marchetti (Project Sponsor)

**Soddisfazione complessiva**: 9/10

**Aspetti positivi**:
- "Documentazione estremamente dettagliata e professionale"
- "Trasparenza totale su rischi e limiti del budget"
- "Mockup visivi aiutano molto a visualizzare il prodotto finale"
- "Approccio pragmatico (ibrido) alle metodologie dimostra maturità"

**Aree di attenzione**:
- "Monitorare strettamente il rischio WebSocket, è il punto critico"
- "Mantenere comunicazione bi-settimanale come promesso"

### Feedback Francesca Giuliani (Esperta Maraffa)

**Soddisfazione complessiva**: 10/10

**Commento**:
> "I mockup del tavolo da gioco sono esattamente quello che sognavo! Rispecchiano perfettamente l'esperienza del gioco tradizionale. Non vedo l'ora di testare il prodotto finito."

### Feedback Team PlayHeritage Labs

**Sentiment team**: 🟢 Positivo, energizzato

**Commento Marco Venturi**:
> "Ottimo inizio. La fase di Scoping ci ha permesso di allinearci perfettamente con il committente. Ora abbiamo una roadmap chiara. Il vero lavoro inizia adesso con Planning e Development!"

---

## Allegati a Questo Documento

1. Registrazione meeting Zoom (3 ore, disponibile su richiesta)
2. Slide presentazione Scoping (PDF, 45 slide)
3. Email conferma pagamento 1° tranche (da ricevere entro 10/10)
4. Foto gruppo al termine del meeting

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Validato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data pubblicazione**: 03/10/2025
**Versione**: 1.0.0 - FINALE APPROVATA
