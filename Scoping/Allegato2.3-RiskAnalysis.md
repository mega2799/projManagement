# Allegato 2.3 - Risk Analysis
## v.1.3.0 – 2026-08-23

> Per la versione visiva compatta e a colori (da usare come allegato PDF), vedi `Allegato2.3-RiskMatrix.html`: apri il file nel browser e usa "Stampa → Salva come PDF".

<!--
Per l'analisi dei rischi si è scelto di utilizzare l'approccio **Risk Rating Matrix** che consiste nella creazione di una tabella che ha le probabilità che il rischio accada nelle righe e il livello di impatto del rischio nelle colonne.
-->

## Risk Rating Matrix

<!--
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
-->

**Colori (livello di rischio):**
- Verde (1-2): Rischio accettabile
- Giallo (3-4): Rischio da monitorare
- Arancione (6-8): Rischio significativo, richiede mitigazione
- Rosso (9-12): Rischio critico, richiede piano di contingenza
- Rosso Critico (16): Rischio massimo, priorità assoluta e piano di contingenza dedicato

<!--
### Matrice

La matrice seguente incrocia la **probabilità** (righe) con il **livello di impatto** (colonne). In ogni cella sono riportati il valore di rischio (Probabilità × Impatto) e i codici dei rischi che vi ricadono; il codice ha la forma *sottosistema.rischio* (vedi Risk Register più sotto). Il colore della cella indica il livello secondo la scala definita sopra.

<table>
  <tr>
    <th colspan="2" rowspan="2" style="background-color:#404040;color:#ffffff;text-align:center;padding:6px;">Valore di rischio<br>(P &times; I)</th>
    <th colspan="4" style="background-color:#404040;color:#ffffff;text-align:center;padding:6px;">Livello di impatto &rarr;</th>
  </tr>
  <tr>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">Trascurabile<br>(1)</th>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">Moderato<br>(2)</th>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">Grave<br>(3)</th>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">Disastroso<br>(4)</th>
  </tr>
  <tr>
    <th rowspan="4" style="background-color:#404040;color:#ffffff;text-align:center;padding:6px;">Probabilità<br>&uarr;</th>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">D &middot; Alta<br>(76-100%)</th>
    <td style="background-color:#FFEB84;color:#000000;text-align:center;padding:8px;"><strong>4</strong><br>&mdash;</td>
    <td style="background-color:#F4A259;color:#000000;text-align:center;padding:8px;"><strong>8</strong><br>2.3, 5.3</td>
    <td style="background-color:#E06666;color:#ffffff;text-align:center;padding:8px;"><strong>12</strong><br>&mdash;</td>
    <td style="background-color:#A61C00;color:#ffffff;text-align:center;padding:8px;"><strong>16</strong><br>2.1, 6.1</td>
  </tr>
  <tr>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">C &middot; Media-Alta<br>(51-75%)</th>
    <td style="background-color:#FFEB84;color:#000000;text-align:center;padding:8px;"><strong>3</strong><br>&mdash;</td>
    <td style="background-color:#F4A259;color:#000000;text-align:center;padding:8px;"><strong>6</strong><br>4.1</td>
    <td style="background-color:#E06666;color:#ffffff;text-align:center;padding:8px;"><strong>9</strong><br>1.3, 2.2, 5.1, 6.3</td>
    <td style="background-color:#E06666;color:#ffffff;text-align:center;padding:8px;"><strong>12</strong><br>2.4, 6.2</td>
  </tr>
  <tr>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">B &middot; Media-Bassa<br>(26-50%)</th>
    <td style="background-color:#63BE7B;color:#000000;text-align:center;padding:8px;"><strong>2</strong><br>&mdash;</td>
    <td style="background-color:#FFEB84;color:#000000;text-align:center;padding:8px;"><strong>4</strong><br>1.2, 3.3, 5.2</td>
    <td style="background-color:#F4A259;color:#000000;text-align:center;padding:8px;"><strong>6</strong><br>1.1, 3.1, 4.3, 6.4</td>
    <td style="background-color:#F4A259;color:#000000;text-align:center;padding:8px;"><strong>8</strong><br>&mdash;</td>
  </tr>
  <tr>
    <th style="background-color:#595959;color:#ffffff;text-align:center;padding:6px;">A &middot; Bassa<br>(0-25%)</th>
    <td style="background-color:#63BE7B;color:#000000;text-align:center;padding:8px;"><strong>1</strong><br>&mdash;</td>
    <td style="background-color:#63BE7B;color:#000000;text-align:center;padding:8px;"><strong>2</strong><br>&mdash;</td>
    <td style="background-color:#FFEB84;color:#000000;text-align:center;padding:8px;"><strong>3</strong><br>3.2</td>
    <td style="background-color:#FFEB84;color:#000000;text-align:center;padding:8px;"><strong>4</strong><br>4.2</td>
  </tr>
</table>

**Distribuzione dei 20 rischi**: 2 a livello Rosso Critico (valore 16), 6 Rossi (9-12), 7 Arancioni (6-8), 5 Gialli (3-4), nessuno Verde. La concentrazione nell'area alta della matrice — dominata da **Real-Time Communication** e **Project Management** — conferma che sono questi i due sottosistemi che richiedono la massima attenzione gestionale e i piani di contingenza dedicati.
-->

### Risk Register

Tabella di sintesi di tutti i rischi identificati, con codice *sottosistema.rischio*, probabilità, impatto, valore e livello di rischio. Il dettaglio completo di descrizione e strategia è riportato nella sezione "Rischi" più avanti.

| Codice | Rischio | Sottosistema | Prob. | Impatto | Valore | Livello | Strategia (sintesi) |
|--------|---------|--------------|:-----:|---------|:------:|---------|---------------------|
| 1.1 | Incomprensioni sulle regole della Maraffa | Game Engine | B | Grave | 6 | Arancione | Mitigazione — workshop con Francesca Giuliani; regole approvate formalmente |
| 1.2 | Varianti regionali delle regole | Game Engine | B | Moderato | 4 | Giallo | Avoid — adottata in Scoping la versione ufficiale "Maraffa Forever": elimina l'ambiguità delle varianti |
| 1.3 | Requisiti aggiuntivi scoperti in sviluppo | Game Engine | C | Grave | 9 | Rosso | Mitigazione — demo bi-settimanali; freeze requisiti dopo milestone 1 |
| 2.1 | Esperienza limitata con WebSocket | Real-Time Communication | D | Disastroso | 16 | Rosso Critico | Contingenza — spike tecnico 2 settimane; consulente esterno (budget €2.000) |
| 2.2 | Gestione disconnessioni e riconnessioni | Real-Time Communication | C | Grave | 9 | Rosso | Mitigazione — sistema "partita sospesa" (5 min); state persistence con Redis |
| 2.3 | Performance di rete variabile tra utenti | Real-Time Communication | D | Moderato | 8 | Arancione | Mitigazione — indicatore qualità connessione; ottimizzazione messaggi |
| 2.4 | Race conditions e sincronizzazione stato | Real-Time Communication | C | Disastroso | 12 | Rosso | Mitigazione — architettura server-authoritative; code review obbligatoria |
| 3.1 | Bilanciare modernità e familiarità | Frontend Web | B | Grave | 6 | Arancione | Mitigazione — co-design con 10 utenti; votazione su 2 mockup |
| 3.2 | Scarsa partecipazione a user testing | Frontend Web | A | Grave | 3 | Giallo | Mitigazione — coinvolgimento precoce; incentivi (accesso anticipato, gadget) |
| 3.3 | Responsive design su tutti i dispositivi | Frontend Web | B | Moderato | 4 | Giallo | Mitigazione — approccio mobile-first; framework Tailwind CSS |
| 4.1 | Integrazione chat con sistema real-time | Social & Community | C | Moderato | 6 | Arancione | Mitigazione — stesso canale WebSocket; throttling (1 msg/sec) |
| 4.2 | Vulnerabilità nel sistema di autenticazione | Backend Server | A | Disastroso | 4 | Giallo | Mitigazione — Passport.js/JWT; HTTPS obbligatorio; penetration testing |
| 4.3 | Gestione privacy e GDPR | Backend Server | B | Grave | 6 | Arancione | Mitigazione — ufficio legale UniBo; privacy policy, cookie consent, diritto all'oblio |
| 5.1 | Budget limitato per infrastruttura cloud | Infrastructure & DevOps | C | Grave | 9 | Rosso | Mitigazione — server dedicato (€50/mese); architettura pronta per cloud migration |
| 5.2 | Esperienza limitata in DevOps | Infrastructure & DevOps | B | Moderato | 4 | Giallo | Mitigazione — configurazione Docker standardizzata e CI/CD GitLab riducono il presidio DevOps richiesto |
| 5.3 | Picchi di traffico al lancio | Infrastructure & DevOps | D | Moderato | 8 | Arancione | Mitigazione — load testing; soft launch graduale; rate limiting |
| 6.1 | Budget insufficiente per team | Project Management | D | Disastroso | 16 | Rosso Critico | Accept — progetto pilota a valore strategico; team part-time (50% FTE) |
| 6.2 | Scope creep da richieste committente | Project Management | C | Disastroso | 12 | Rosso | Mitigazione — Change Control Process rigoroso; freeze requisiti dopo POS |
| 6.3 | Sottostima complessità tecnica | Real-Time, Frontend | C | Grave | 9 | Rosso | Mitigazione — agile iterativo; buffer 20%; riduzione scope se ritardo >15% |
| 6.4 | Assenza di buffer temporale | Project Management | B | Grave | 6 | Arancione | Mitigazione — MoSCoW prioritization; sottosistemi critici completati entro gennaio |

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
       - Risk Management: Avoid. Adottata in Scoping la versione ufficiale "Maraffa Forever" documentata dall'esperta: elimina la fonte del rischio (le varianti regionali).
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
       - Risk Management: Piano di Contingenza. Spike tecnico 2 settimane. Decision point go/no-go al giorno 15: se lo spike fallisce, si attiva il consulente esterno Dr. Stefano Nardi (budget €2.000); al giorno 30, escalation al committente.
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
       - Risk Management: Mitigazione. Librerie consolidate (Passport.js, JWT). HTTPS obbligatorio. Penetration testing.
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
       - Risk Management: Mitigazione. Configurazione Docker standardizzata. CI/CD con GitLab (deploy automatizzato, meno presidio manuale).
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
       - Descrizione: €714/mese/persona sotto media mercato
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
       - Descrizione: 7 mesi senza margini imprevisti
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
**Data approvazione**: 22/09/2025

**Storico revisioni**:
- **v.1.3.0**: Audit teorico sulle 5 strategie di risposta: rischio 1.2 da Accept ad **Avoid** (adottare la versione ufficiale elimina la fonte del rischio: per il corso Accept = nessuna azione possibile), rischio 4.2 da Contingenza a **Mitigazione** (le azioni elencate sono tutte preventive immediate). Companion HTML allineato.
- **v.1.2.0**: Rinumerato da Allegato 2.4 a **Allegato 2.3**: ritirati dagli allegati i verbali ex 2.1 (Project Scoping Meeting) ed ex 2.11 (Approval Process), ora solo narrati nella relazione; numerazione degli allegati di Scoping resa sequenziale (2.1–2.9), come nella relazione di riferimento. Contenuto invariato.
- **v.1.1.0**: Aggiornata la legenda dei colori (introdotto il livello "Rosso Critico" per il valore 16) e aggiunto il Risk Register tabellare di sintesi (codice, probabilità, impatto, valore, livello e strategia per ogni rischio).
- **v.1.0.0**: Prima stesura dell'analisi dei rischi (definizioni, elenco rischi per sottosistema, riepilogo rischi critici).
