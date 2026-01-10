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
- Verde (1-2): Rischio accettabile
- Giallo (3-4): Rischio da monitorare
- Arancione (6-8): Rischio significativo, richiede mitigazione
- Rosso (9-16): Rischio critico, richiede piano di contingenza

---

## Rischi

1. 1. Incomprensioni sulle regole della Maraffa tradizionale
       - Sottosistema: Game Engine
       - Probabilità: B
       - Livello di impatto: Grave
       - Valore rischio: 6
       - Colore rischio: Arancione
       - Descrizione: Sfumature e interpretazioni diverse delle regole
       - Risk Management: Mitigazione. Workshop con esperta Francesca Giuliani. Documento formale regole approvato.
   2. Varianti regionali delle regole
       - Sottosistema: Game Engine
       - Probabilità: B
       - Livello di impatto: Moderato
       - Valore rischio: 4
       - Colore rischio: Giallo
       - Descrizione: Varianti Maraffa in zone diverse della Romagna
       - Risk Management: Accept. Definire versione ufficiale "Maraffa Forever" in Scoping.
   3. Requisiti aggiuntivi scoperti durante sviluppo
       - Sottosistema: Game Engine
       - Probabilità: C
       - Livello di impatto: Grave
       - Valore rischio: 9
       - Colore rischio: Rosso
       - Descrizione: Casi limite emergenti durante implementazione
       - Risk Management: Mitigazione. Demo bi-settimanali. Freeze requisiti dopo milestone 1.

2. 1. Esperienza limitata con tecnologie WebSocket (RISCHIO CRITICO)
       - Sottosistema: Real-Time Communication
       - Probabilità: D
       - Livello di impatto: Disastroso
       - Valore rischio: 16
       - Colore rischio: Rosso Critico
       - Descrizione: Team senza esperienza in real-time multiplayer
       - Risk Management: Piano di Contingenza. Spike tecnico 2 settimane. Decision point giorno 30: se fallisce, consulente esterno Dr. Stefano Nardi (budget €2.000).
   2. Gestione disconnessioni e riconnessioni
       - Sottosistema: Real-Time Communication
       - Probabilità: C
       - Livello di impatto: Grave
       - Valore rischio: 9
       - Colore rischio: Rosso
       - Descrizione: Complessità riconnessione senza perdere stato gioco
       - Risk Management: Mitigazione. Sistema "partita sospesa" (5 min). State persistence con Redis.
   3. Performance di rete variabile tra utenti
       - Sottosistema: Real-Time Communication
       - Probabilità: D
       - Livello di impatto: Moderato
       - Valore rischio: 8
       - Colore rischio: Arancione
       - Descrizione: Connessioni lente potrebbero frustrare giocatori
       - Risk Management: Mitigazione. Indicator quality of connection. Ottimizzazione messaggi WebSocket.
   4. Race conditions e sincronizzazione stato
       - Sottosistema: Real-Time Communication
       - Probabilità: C
       - Livello di impatto: Disastroso
       - Valore rischio: 12
       - Colore rischio: Rosso
       - Descrizione: Bug sincronizzazione tra 4 client
       - Risk Management: Mitigazione. Architettura server-authoritative. Code review obbligatoria.

3. 1. Bilanciare modernità e familiarità
       - Sottosistema: Frontend Web
       - Probabilità: B
       - Livello di impatto: Grave
       - Valore rischio: 6
       - Colore rischio: Arancione
       - Descrizione: Interfaccia moderna ma non alienante per target 25-45 anni
       - Risk Management: Mitigazione. Co-design con 10 utenti. Votazione su 2 mockup alternativi.
   2. Scarsa partecipazione a user testing
       - Sottosistema: Frontend Web
       - Probabilità: A
       - Livello di impatto: Grave
       - Valore rischio: 3
       - Colore rischio: Giallo
       - Descrizione: Feedback insufficiente se beta tester non partecipano
       - Risk Management: Mitigazione. Coinvolgimento da inizio progetto. Incentivi (accesso anticipato, credits, gadget).
   3. Responsive design su tutti i dispositivi
       - Sottosistema: Frontend Web
       - Probabilità: B
       - Livello di impatto: Moderato
       - Valore rischio: 4
       - Colore rischio: Giallo
       - Descrizione: Ottimizzazione mobile potrebbe richiedere riprogettazione
       - Risk Management: Mitigazione. Approccio mobile-first. Framework responsive (Tailwind CSS).

4. 1. Integrazione chat con sistema real-time
       - Sottosistema: Social & Community
       - Probabilità: C
       - Livello di impatto: Moderato
       - Valore rischio: 6
       - Colore rischio: Arancione
       - Descrizione: Chat deve funzionare senza interferire con WebSocket partite
       - Risk Management: Mitigazione. Stesso canale WebSocket. Throttling messaggi (1 msg/sec).
   2. Vulnerabilità nel sistema di autenticazione
       - Sottosistema: Backend Server
       - Probabilità: A
       - Livello di impatto: Disastroso
       - Valore rischio: 4
       - Colore rischio: Giallo
       - Descrizione: Dati compromessi danneggerebbero reputazione
       - Risk Management: Piano di Contingenza. Librerie consolidate (Passport.js, JWT). HTTPS obbligatorio. Penetration testing.
   3. Gestione privacy e GDPR
       - Sottosistema: Backend Server
       - Probabilità: B
       - Livello di impatto: Grave
       - Valore rischio: 6
       - Colore rischio: Arancione
       - Descrizione: Team senza competenze legali GDPR
       - Risk Management: Mitigazione. Consultare ufficio legale UniBo. Privacy policy, cookie consent, diritto oblio.
5. 1. Budget limitato per infrastruttura cloud
       - Sottosistema: Infrastructure & DevOps
       - Probabilità: C
       - Livello di impatto: Grave
       - Valore rischio: 9
       - Colore rischio: Rosso
       - Descrizione: Servizi cloud costosi
       - Risk Management: Mitigazione. Hosting iniziale server dedicato (€50/mese). Architettura pronta per cloud migration.
   2. Esperienza limitata in DevOps
       - Sottosistema: Infrastructure & DevOps
       - Probabilità: B
       - Livello di impatto: Moderato
       - Valore rischio: 4
       - Colore rischio: Giallo
       - Descrizione: Competenze teoriche, esperienza pratica limitata
       - Risk Management: Mitigazione. PaaS (Heroku/Railway). Docker. CI/CD con GitLab.
   3. Picchi di traffico al lancio
       - Sottosistema: Infrastructure & DevOps
       - Probabilità: D
       - Livello di impatto: Moderato
       - Valore rischio: 8
       - Colore rischio: Arancione
       - Descrizione: 150 persone accedono simultaneamente al lancio
       - Risk Management: Mitigazione. Load testing. Soft launch graduale. Rate limiting.
6. 1. Budget insufficiente per team (RISCHIO CRITICO)
       - Sottosistema: Project Management
       - Probabilità: D
       - Livello di impatto: Disastroso
       - Valore rischio: 16
       - Colore rischio: Rosso Critico
       - Descrizione: €833/mese/persona sotto media mercato
       - Risk Management: Accept. Progetto pilota con valore strategico. Team part-time (50% FTE).
   2. Scope creep da richieste committente
       - Sottosistema: Project Management
       - Probabilità: C
       - Livello di impatto: Disastroso
       - Valore rischio: 12
       - Colore rischio: Rosso
       - Descrizione: Nuove funzionalità durante sviluppo
       - Risk Management: Mitigazione. Change Control Process rigoroso. Freeze requisiti dopo POS.
   3. Sottostima complessità tecnica
       - Sottosistema: Real-Time, Frontend
       - Probabilità: C
       - Livello di impatto: Grave
       - Valore rischio: 9
       - Colore rischio: Rosso
       - Descrizione: Stime ottimistiche
       - Risk Management: Mitigazione. Agile iterativo. Buffer 20%. Se ritardo >15% a metà progetto: ridurre scope.
   4. Assenza di buffer temporale
       - Sottosistema: Project Management
       - Probabilità: B
       - Livello di impatto: Grave
       - Valore rischio: 6
       - Colore rischio: Arancione
       - Descrizione: 6 mesi senza margini imprevisti
       - Risk Management: Mitigazione. MoSCoW prioritization. Completare sottosistemi critici entro gennaio.

---

## Riepilogo Rischi Critici (Valore ≥ 12)

| Rischio | Sottosistema | Valore | Colore | Strategia |
|---------|--------------|--------|--------|-----------|
| Esperienza limitata WebSocket | Real-Time Communication | 16 | Rosso Critico | Piano di Contingenza (consulente esterno) |
| Budget insufficiente | Project Management | 16 | Rosso Critico | Accept (valore strategico) |
| Race conditions sincronizzazione | Real-Time Communication | 12 | Rosso | Mitigazione (server-authoritative) |
| Scope creep | Project Management | 12 | Rosso | Mitigazione (change control) |

---

**Redatto da**: Elena Rossi (Lead Developer, PlayHeritage Labs)
**Revisionato da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Data approvazione**: 20/09/2025
