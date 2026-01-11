# Allegato 3.2 - MoSCoW Prioritization Analysis
## v.1.0.0 – 2025-10-22 14:00:00

Il metodo **MoSCoW** è una tecnica di prioritizzazione dei requisiti sviluppata da Dai Clegg per gestire le aspettative degli stakeholder e garantire che le risorse del progetto siano allocate sulle funzionalità più critiche. L'acronimo sta per:

- **M**ust Have: requisiti essenziali per il successo del progetto
- **S**hould Have: requisiti importanti ma non critici
- **C**ould Have: requisiti desiderabili ma non necessari
- **W**on't Have: requisiti esplicitamente esclusi dalla versione corrente

---

## Principi Applicati (Best Practices 2026)

### 1. Regola del 60/20/20
Seguendo le linee guida del **Dynamic Systems Development Method (DSDM)**, abbiamo applicato la seguente distribuzione dello sforzo:

- **Must Have**: ~60% dello sforzo totale
- **Should Have**: ~20% dello sforzo totale
- **Could Have**: ~20% dello sforzo totale

Questo garantisce che il progetto possa consegnare valore anche in caso di vincoli di tempo/budget, concentrando la maggior parte delle risorse sui requisiti critici.

### 2. Definizione Rigorosa di "Must Have"
Un requisito è classificato come **Must Have** solo se soddisfa **almeno uno** dei seguenti criteri:

1. Senza questo requisito, il prodotto non è utilizzabile
2. Il requisito è richiesto per legge (es. GDPR)
3. L'assenza del requisito crea un rischio di sicurezza inaccettabile
4. Il requisito è esplicitamente richiesto dal committente come non negoziabile

### 3. Approccio Dinamico
La categorizzazione MoSCoW è stata rivista **3 volte** durante la fase di Scoping:
- **28/09/2025**: Prima classificazione basata su POS
- **05/10/2025**: Revisione dopo user testing mockup v2
- **15/10/2025**: Approvazione finale con Giovanni Marchetti (Maraffa Forever)

---

## Categorizzazione Requisiti per Sottosistema

### 1. Game Engine

#### Must Have (100% dei requisiti)
**Razionale**: Il Game Engine è il core del prodotto. Senza le regole di gioco implementate correttamente, MaraffaOnline non può esistere.

| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-GE-1.1.1 | Implementazione regole Maraffone/Beccaccino | 15 | M |
| REQ-GE-1.1.2 | Gestione turni e fasi di gioco | 10 | M |
| REQ-GE-1.1.3 | Validazione mosse (anti-cheat) | 8 | M |
| REQ-GE-1.1.4 | Calcolo punteggi | 6 | M |
| REQ-GE-1.1.5 | Gestione situazioni speciali (Maraffa/Cricca) | 5 | M |
| REQ-GE-1.3 | Persistenza stato partita | 6 | M |
| **Totale** | | **50 giorni** | |

#### Won't Have
| ID Requisito | Descrizione | Razionale Esclusione |
|--------------|-------------|----------------------|
| REQ-GE-1.2 | Modalità single-player vs IA | Budget limitato, focus su multiplayer online. Feature futura (v1.1+) |

---

### 2. Backend Server

#### Must Have (~70%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-BE-2.1.1 | Registrazione utente | 4 | M |
| REQ-BE-2.1.2 | Login e sessioni JWT | 4 | M |
| REQ-BE-2.1.3 | Accesso ospite | 2 | M |
| REQ-BE-2.2.1 | Creazione stanza | 5 | M |
| REQ-BE-2.2.2 | Join stanza | 3 | M |
| REQ-BE-2.2.3 | Gestione lobby partita | 4 | M |
| REQ-BE-2.2.4 | Persistenza dati partita | 6 | M |
| REQ-BE-2.4.1 | Statistiche base (win/loss) | 3 | M |
| REQ-BE-2.5.1 | API RESTful standard | 8 | M |
| REQ-BE-2.5.2 | Performance API (< 200ms) | 5 | M |
| REQ-BE-2.5.3 | Sicurezza API | 6 | M |
| **Subtotale Must** | | **50 giorni** | |

#### Should Have (~20%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-BE-2.1.4 | Gestione profilo personalizzabile | 3 | S |
| REQ-BE-2.1.5 | Password recovery | 2 | S |
| REQ-BE-2.3.1 | Sistema amicizie (aggiunta amici) | 5 | S |
| REQ-BE-2.3.2 | Lista amici con presenza online | 4 | S |
| REQ-BE-2.3.3 | Invito diretto amici | 2 | S |
| **Subtotale Should** | | **16 giorni** | |

#### Could Have (~10%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-BE-2.4.2 | Statistiche avanzate (carta più giocata, etc.) | 4 | C |
| **Subtotale Could** | | **4 giorni** | |

#### Won't Have
| ID Requisito | Descrizione | Razionale Esclusione |
|--------------|-------------|----------------------|
| REQ-BE-2.1.6 | Social login (Google/Facebook) | Complessità implementazione vs valore aggiunto. Pianificato per v1.1 |

**Totale Backend**: 70 giorni (Must: 50, Should: 16, Could: 4)

---

### 3. Real-Time Communication

#### Must Have (~85%)
**Razionale**: WebSocket è critico per esperienza multiplayer real-time. Senza sincronizzazione, il gioco non è giocabile.

| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-RTC-3.1.1 | Gestione connessioni WebSocket (Socket.IO) | 8 | M |
| REQ-RTC-3.1.2 | Autenticazione WebSocket | 3 | M |
| REQ-RTC-3.2.1 | Eventi di gioco in tempo reale | 10 | M |
| REQ-RTC-3.2.2 | Broadcast selettivo (room-based) | 4 | M |
| REQ-RTC-3.2.3 | Gestione latency e lag compensation | 6 | M |
| REQ-RTC-3.3.1 | Disconnessione temporanea e reconnect | 5 | M |
| REQ-RTC-3.3.2 | Disconnessione permanente (annulla partita) | 2 | M |
| REQ-RTC-3.4.1 | Chat in-game testuale | 4 | M |
| **Subtotale Must** | | **42 giorni** | |

#### Could Have (~15%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-RTC-3.4.2 | Chat globale lobby | 3 | C |
| **Subtotale Could** | | **3 giorni** | |

#### Won't Have
| ID Requisito | Descrizione | Razionale Esclusione |
|--------------|-------------|----------------------|
| REQ-RTC-3.3.2b | Sostituzione giocatore con bot | Richiede IA (vedi REQ-GE-1.2). Non MVP. |
| REQ-RTC-3.4.3 | Emoji/reactions | Nice-to-have ma non essenziale. v1.1+ |

**Totale Real-Time**: 45 giorni (Must: 42, Could: 3)

---

### 4. Frontend Web

#### Must Have (~65%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-FE-4.1.1 | Implementazione mockup approvati (6 schermate) | 25 | M |
| REQ-FE-4.1.2 | Design system (componenti riutilizzabili) | 8 | M |
| REQ-FE-4.2.1 | Supporto multi-device (desktop, tablet, mobile) | 12 | M |
| REQ-FE-4.2.2 | Mobile-first approach | 6 | M |
| REQ-FE-4.4.1 | Ottimizzazione caricamento (FCP < 2s) | 5 | M |
| **Subtotale Must** | | **56 giorni** | |

#### Should Have (~25%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-FE-4.3.1 | Accessibilità WCAG 2.1 AA | 8 | S |
| REQ-FE-4.4.2 | Bundle size optimization (< 500KB) | 3 | S |
| REQ-FE-4.5.1 | Microinterazioni e animazioni | 6 | S |
| **Subtotale Should** | | **17 giorni** | |

#### Could Have (~10%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-FE-4.3.2 | Modalità daltonici | 3 | C |
| **Subtotale Could** | | **3 giorni** | |

**Totale Frontend**: 76 giorni (Must: 56, Should: 17, Could: 3)

---

### 5. Mobile Application

#### Won't Have (100%)
| ID Requisito | Descrizione | Razionale Esclusione |
|--------------|-------------|----------------------|
| REQ-MA-5.1 | App nativa iOS/Android | Budget €25.000 insufficiente per sviluppo nativo. Alternative: (1) responsive web utilizzabile da mobile, (2) sviluppo nativo in v2.0 se progetto di successo |
| REQ-MA-5.2 | Progressive Web App (PWA) | Could Have, valutato in sprint 4-5 se tempo disponibile |

---

### 6. Social & Community Features

#### Must Have (~40%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-SOC-6.4.1 | Notifiche in-app ("È il tuo turno") | 4 | M |
| **Subtotale Must** | | **4 giorni** | |

#### Should Have (~40%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-SOC-6.1 | Sistema amicizie (vedi Backend 2.3) | 11 | S |
| REQ-SOC-6.5.1 | Profili pubblici utenti | 3 | S |
| **Subtotale Should** | | **14 giorni** | |

#### Could Have (~20%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-SOC-6.3.1 | Classifica globale (top 100) | 4 | C |
| REQ-SOC-6.3.2 | Classifica amici | 2 | C |
| **Subtotale Could** | | **6 giorni** | |

#### Won't Have
| ID Requisito | Descrizione | Razionale Esclusione |
|--------------|-------------|----------------------|
| REQ-SOC-6.4.2 | Notifiche push | Richiede app mobile o browser permission complessa. v1.1+ |

**Totale Social**: 24 giorni (Must: 4, Should: 14, Could: 6)

---

### 7. Infrastructure & DevOps

#### Must Have (~80%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-INF-7.1.1 | Server dedicato (Hetzner/OVH) | 3 | M |
| REQ-INF-7.1.2 | Containerizzazione (Docker) | 5 | M |
| REQ-INF-7.1.3 | CI/CD pipeline (GitLab CI) | 6 | M |
| REQ-INF-7.2.1 | PostgreSQL setup e backup | 4 | M |
| REQ-INF-7.3.1 | Logging centralizzato | 3 | M |
| REQ-INF-7.3.2 | Monitoring performance (uptime) | 2 | M |
| REQ-INF-7.4.1 | SSL/TLS (Let's Encrypt) | 1 | M |
| REQ-INF-7.4.3 | Backup e disaster recovery | 3 | M |
| **Subtotale Must** | | **27 giorni** | |

#### Should Have (~20%)
| ID Requisito | Descrizione | Effort (giorni) | Priorità |
|--------------|-------------|-----------------|----------|
| REQ-INF-7.2.2 | Redis caching | 3 | S |
| REQ-INF-7.3.3 | Error tracking (Sentry) | 2 | S |
| REQ-INF-7.4.2 | Firewall e DDoS protection (Cloudflare) | 2 | S |
| REQ-INF-7.5.1 | Architettura preparata per scalabilità | 3 | S |
| **Subtotale Should** | | **10 giorni** | |

**Totale Infrastructure**: 37 giorni (Must: 27, Should: 10)

---

## Riepilogo Globale per Categoria

### Must Have (MVP Core - 229 giorni)
| Sottosistema | Giorni Must | % del Totale Must |
|--------------|-------------|-------------------|
| Game Engine | 50 | 21.8% |
| Backend Server | 50 | 21.8% |
| Real-Time Communication | 42 | 18.3% |
| Frontend Web | 56 | 24.5% |
| Social & Community | 4 | 1.7% |
| Infrastructure | 27 | 11.8% |
| **Totale Must Have** | **229** | **100%** |

### Should Have (71 giorni)
| Sottosistema | Giorni Should | % del Totale Should |
|--------------|---------------|---------------------|
| Backend Server | 16 | 22.5% |
| Frontend Web | 17 | 23.9% |
| Social & Community | 14 | 19.7% |
| Infrastructure | 10 | 14.1% |
| **Totale Should Have** | **71** | **100%** |

### Could Have (20 giorni)
| Sottosistema | Giorni Could | % del Totale Could |
|--------------|--------------|-------------------|
| Backend Server | 4 | 20.0% |
| Real-Time Communication | 3 | 15.0% |
| Frontend Web | 3 | 15.0% |
| Social & Community | 6 | 30.0% |
| **Totale Could Have** | **20** | **100%** |

### Won't Have (Esclusi da MVP)
- App mobile nativa iOS/Android
- Social login (Google/Facebook)
- Modalità single-player vs IA
- Notifiche push
- Emoji/reactions in chat
- Tornei strutturati

---

## Distribuzione Effort (60/20/20 Rule)

| Categoria | Giorni | % dello Sforzo | Target DSDM |
|-----------|--------|----------------|-------------|
| Must Have | 229 | 71.6% | ~60% |
| Should Have | 71 | 22.2% | ~20% |
| Could Have | 20 | 6.2% | ~20% |
| **Totale** | **320** | **100%** | |

**Analisi della Distribuzione**:
- **Must Have al 71.6%**: leggermente sopra il target del 60%, ma giustificato dalla natura critica del Game Engine e Real-Time Communication (core product differentiator).
- **Should Have al 22.2%**: allineato perfettamente al target del 20%. Include features importanti come sistema amicizie e accessibilità.
- **Could Have al 6.2%**: sotto il target del 20%. Scelta deliberata per ridurre rischi di scope creep e garantire consegna MVP in 6 mesi.

---

## Decisioni Strategiche e Trade-off

### 1. Esclusione App Mobile Nativa
**Decisione**: Won't Have nel MVP
**Razionale**:
- Sviluppo nativo iOS + Android richiederebbe ~120 giorni aggiuntivi (40% effort in più)
- Budget €25.000 insufficiente per assumere sviluppatori mobile
- **Alternativa**: responsive web app ottimizzata per mobile browser
- **Validazione**: user testing ha confermato che la web app mobile è usabile (87.5% success rate, vedi Allegato 2.7)

**Trade-off accettati**:
- [-] Nessuna integrazione nativa (notifiche push, vibrazione, etc.)
- [-] Performance leggermente inferiore rispetto a nativa
- [+] Time-to-market più veloce (6 mesi vs 9-10 mesi)
- [+] Budget rimane nei limiti

### 2. Sistema Amicizie come "Should Have"
**Decisione**: Should Have (non Must Have)
**Razionale**:
- Funzionalità sociale importante ma non bloccante per giocare
- Utenti possono invitare amici tramite link condivisibile anche senza sistema amicizie
- Può essere rilasciata in sprint successivi senza impattare core gameplay

**Approvazione stakeholder**: Giovanni Marchetti (Maraffa Forever) ha concordato che il sistema amicizie può essere aggiunto post-MVP se il budget iniziale risulta insufficiente.

### 3. Chat Globale come "Could Have"
**Decisione**: Could Have
**Razionale**:
- Chat in-game (4 giocatori) è Must Have per comunicazione durante partita
- Chat globale lobby è nice-to-have ma non essenziale
- Rischio moderazione: chat pubblica richiede moderazione attiva (costo nascosto)

---

## Criterio di Successo MVP

Il progetto MaraffaOnline sarà considerato **MVP completo e lanciabile** se e solo se:

1. [+] **Tutti i requisiti Must Have sono implementati e testati**
2. [+] **Almeno l'80% dei requisiti Should Have sono completati**
3. [+] **User Acceptance Testing supera il 90% di success rate** (target: 95%)
4. [+] **Performance targets raggiunti**:
   - API response time < 200ms (95th percentile)
   - WebSocket latency < 500ms
   - Frontend FCP < 2 secondi
5. [+] **Approvazione formale committente** (Giovanni Marchetti, Maraffa Forever)

**Se vincoli di budget/tempo emergono**: i requisiti Could Have saranno i primi ad essere tagliati, seguiti dai Should Have in ordine di impatto minore.

---

## Processo di Revisione MoSCoW

La categorizzazione MoSCoW sarà **rivista** nei seguenti momenti:

1. **Fine Sprint Review** (ogni 2 settimane): verifica se priorità cambiano in base a feedback
2. **Milestone Review** (ogni mese): checkpoint formale con stakeholder
3. **Change Request Process**: se emergono nuovi requisiti, applicare MoSCoW prima di approvarli

**Responsabile**: Marco Venturi (Project Manager)
**Stakeholder coinvolti**: Giovanni Marchetti (committente), Elena Rossi (Tech Lead), Luca Moretti (UX Designer)

---

## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices del metodo MoSCoW 2026:
- [Atlassian - Understanding MoSCoW Prioritization](https://community.atlassian.com/forums/App-Central-articles/Understanding-the-MoSCoW-prioritization-How-to-implement-it-into/ba-p/2463999)
- [Agile Business Consortium - DSDM MoSCoW Prioritisation](https://www.agilebusiness.org/dsdm-project-framework/moscow-prioririsation.html)
- [ProductPlan - MoSCoW Method Overview](https://www.productplan.com/glossary/moscow-prioritization/)
- [EdStellar - Implementing MoSCoW in 2026](https://www.edstellar.com/blog/moscow-prioritization)

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 22/10/2025
