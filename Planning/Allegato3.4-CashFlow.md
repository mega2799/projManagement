# Allegato 3.4 - Cash Flow Management
## v.1.1.0 – 2025-10-28 18:00:00

La gestione del Cash Flow è critica per il successo del progetto MaraffaOnline, considerando il budget limitato di **€25.000** e la durata di **6 mesi** (15 ottobre 2025 - 15 marzo 2026). Questo documento traccia tutti i flussi finanziari in entrata (inflow) e in uscita (outflow) su base mensile, con visualizzazioni grafiche professionali.

---

## Tabella Cash Flow Mensile

| Mese | Periodo | Inflow (€) | Outflow (€) | Net Cash Flow (€) | Saldo Cumulativo (€) |
|------|---------|------------|-------------|-------------------|----------------------|
| **Mese 0** | 15 Ott - 31 Ott | €12.500 | €3.850 | €8.650 | €8.650 |
| **Mese 1** | 01 Nov - 30 Nov | €0 | €4.200 | -€4.200 | €4.450 |
| **Mese 2** | 01 Dic - 31 Dic | €6.250 | €4.200 | €2.050 | €6.500 |
| **Mese 3** | 01 Gen - 31 Gen | €0 | €4.200 | -€4.200 | €2.300 |
| **Mese 4** | 01 Feb - 28 Feb | €6.250 | €4.200 | €2.050 | €4.350 |
| **Mese 5** | 01 Mar - 15 Mar | €0 | €2.100 | -€2.100 | €2.250 |
| **TOTALE** | | **€25.000** | **€22.750** | **€2.250** | **€2.250** |

**Note**:
- **Inflow**: pagamenti ricevuti da Maraffa Forever in 4 tranche (50% upfront, 25% a metà progetto, 25% a fine)
- **Outflow**: spese operative mensili (salari, hosting, tools, licenze)
- **Saldo Finale**: €2.250 di surplus destinato a contingency e celebrazione lancio

### Visualizzazione Grafica Cash Flow Mensile

Il grafico seguente illustra l'andamento del Cash Flow durante i 6 mesi del progetto:

![Cash Flow MaraffaOnline - 6 Mesi](img/cash-flow-maraffaonline.png)

**Analisi del Grafico**:
- **Barre Verdi**: Inflow (pagamenti committente) concentrati in 3 momenti chiave (Mese 0, 2, 4)
- **Barre Rosse**: Outflow (spese operative) costanti per Mesi 1-4, ridotte in Mese 0 e 5
- **Linea Arancione**: Saldo cumulativo sempre positivo, con minimo di €2.300 nel Mese 3

**Insight**: Il saldo cumulativo non scende mai sotto €2.300, garantendo liquidità sufficiente per coprire le spese operative in ogni fase del progetto. La struttura di pagamento 50/25/25 è efficace per mantenere il cash flow positivo.

---

## Struttura Pagamenti Committente (Inflow)

| Tranche | Data | Importo (€) | % del Totale | Condizione |
|---------|------|-------------|--------------|------------|
| **1° Pagamento** | 15 Ott 2025 | €12.500 | 50% | Firma contratto + kickoff meeting |
| **2° Pagamento** | 15 Dic 2025 | €6.250 | 25% | Completamento fase Scoping + Planning |
| **3° Pagamento** | 15 Feb 2026 | €6.250 | 25% | Consegna MVP funzionante (beta) |
| **TOTALE** | | **€25.000** | **100%** | |

**Razionale**: Struttura pagamenti standard per progetti a budget fisso. Il 50% upfront garantisce liquidità iniziale per setup team e infrastruttura. I pagamenti successivi sono legati a milestone misurabili.

---

## Dettaglio Spese Mensili (Outflow)

### Mese 0 (15 Ott - 31 Ott) - €3.850

| Categoria | Voce di Spesa | Importo (€) | Motivazione |
|-----------|---------------|-------------|-------------|
| **Salari** | Stipendi team (5 persone, 0.5 mesi) | €2.500 | Fase setup e kickoff |
| **Infrastruttura** | Server dedicato Hetzner (€50/mese × 0.5) | €25 | Provisioning iniziale |
| **Tools** | Licenze Figma Pro (€15/mese × 5 utenti) | €75 | Design mockup approvati |
| **Tools** | Licenza JetBrains All Products (€25/mese) | €25 | IDE per sviluppo |
| **Tools** | Dominio maraffaonline.it (registrazione annuale) | €15 | Acquisto dominio |
| **Consulenza** | Validazione regole con Francesca Giuliani | €300 | Esperta Maraffa Forever |
| **Setup** | SSL Certificato Let's Encrypt (gratuito) | €0 | |
| **Setup** | GitLab CI setup (piano free) | €0 | |
| **Comunicazione** | Zoom Pro per daily meetings (€13/mese) | €13 | Team remoto |
| **Documentazione** | Confluence Cloud (€10/utente × 5) | €50 | Documentazione PM |
| **Contingency** | Buffer 10% | €347 | Imprevisti fase iniziale |
| **Subtotale Mese 0** | | **€3.850** | |

### Mese 1-4 (Nov - Feb) - €4.200/mese

| Categoria | Voce di Spesa | Importo (€/mese) | Motivazione |
|-----------|---------------|------------------|-------------|
| **Salari** | Stipendi team (5 persone, full-time) | €3.000 | Development sprint |
| **Infrastruttura** | Server dedicato Hetzner (€50/mese) | €50 | Hosting production + staging |
| **Database** | PostgreSQL hosting (incluso in server) | €0 | |
| **CDN** | Cloudflare Free Tier | €0 | DDoS protection + CDN |
| **Monitoring** | UptimeRobot Free Tier | €0 | Uptime monitoring |
| **Error Tracking** | Sentry (10K events/mese free) | €0 | Error tracking |
| **Tools** | Figma Pro (€15/mese × 5 utenti) | €75 | Design continuativo |
| **Tools** | JetBrains All Products (€25/mese) | €25 | IDE |
| **Comunicazione** | Zoom Pro (€13/mese) | €13 | Meeting team + stakeholder |
| **Documentazione** | Confluence Cloud (€10/utente × 5) | €50 | PM documentation |
| **Email Service** | SendGrid (100 email/giorno free) | €0 | Email transazionali (registrazione, password recovery) |
| **Storage** | Cloudinary Free Tier (25 GB) | €0 | Storage avatar utenti |
| **Testing** | BrowserStack (piano free) | €0 | Cross-browser testing |
| **Contingency** | Buffer 20% per imprevisti | €387 | Bug fixing, estensioni scope |
| **Subtotale Mesi 1-4** | | **€4.200** | |

**Totale Mesi 1-4**: €4.200 × 4 = **€16.800**

### Mese 5 (01 Mar - 15 Mar) - €2.100

| Categoria | Voce di Spesa | Importo (€) | Motivazione |
|-----------|---------------|-------------|-------------|
| **Salari** | Stipendi team (5 persone, 0.5 mesi) | €1.500 | Testing finale e lancio |
| **Infrastruttura** | Server dedicato Hetzner (€50/mese × 0.5) | €25 | |
| **Tools** | Figma + JetBrains + Zoom + Confluence (0.5 mesi) | €81 | Continuità tools |
| **Marketing** | Materiale comunicazione lancio (social media) | €200 | Post Facebook/Instagram per Maraffa Forever |
| **UAT** | Budget ringraziamento tester (10 utenti × €10) | €100 | Compenso simbolico community |
| **Celebrazione** | Team celebration (pizza + birre online) | €100 | Morale team post-lancio |
| **Contingency** | Buffer finale | €94 | Ultimi aggiustamenti |
| **Subtotale Mese 5** | | **€2.100** | |

---

## Dettaglio Spese per Categoria (6 mesi)

| Categoria | Totale (€) | % del Budget | Note |
|-----------|------------|--------------|------|
| **Salari Team** | €16.000 | 64.0% | 5 persone × 5.5 mesi (part-time mese 0 e 5) |
| **Infrastruttura** | €275 | 1.1% | Server dedicato Hetzner €50/mese × 5.5 mesi |
| **Tools e Licenze** | €1.111 | 4.4% | Figma, JetBrains, Zoom, Confluence, Dominio |
| **Consulenza Esperta** | €300 | 1.2% | Francesca Giuliani (validazione regole) |
| **Marketing Lancio** | €200 | 0.8% | Comunicazione social per community |
| **UAT e Testing** | €100 | 0.4% | Compenso tester Maraffa Forever |
| **Celebrazione** | €100 | 0.4% | Team celebration post-lancio |
| **Contingency Buffer** | €1.414 | 5.7% | Imprevisti e change requests |
| **TOTALE SPESE** | **€22.750** | **91.0%** | |
| **Surplus Finale** | **€2.250** | **9.0%** | Reserve per fase post-lancio |

### Visualizzazione Grafica Distribuzione Spese

Il grafico seguente mostra la distribuzione percentuale delle spese per categoria:

![Distribuzione Spese per Categoria](img/spese-categorie.png)

**Analisi del Grafico**:
- **Salari Team (64%)**: La voce di spesa predominante, coerente con un progetto ad alta intensità di lavoro qualificato (5 persone per 5.5 mesi)
- **Contingency Buffer (5.7%)**: Buffer adeguato secondo le best practices PM per progetti a budget fisso
- **Tools e Licenze (4.4%)**: Costi contenuti grazie all'utilizzo di free tier per molti servizi cloud
- **Infrastruttura (1.1%)**: Spese minime grazie a server dedicati economici (Hetzner €50/mese)
- **Surplus Finale (9%)**: Riserva per imprevisti post-lancio e scalabilità iniziale

**Insight**: L'allocazione del budget è ottimizzata per massimizzare il valore del team di sviluppo (64%), mantenendo contenuti i costi infrastrutturali (1.1%) e garantendo un buffer di sicurezza del 14.7% (Contingency 5.7% + Surplus 9.0%) per gestire imprevisti.

---

## Analisi Rischi Finanziari

### Rischio 1: Ritardo Pagamento Committente
**Probabilità**: Bassa
**Impatto**: Alto
**Mitigazione**:
- Contratto firmato con penali per ritardi pagamento
- Milestone pagamenti legate a deliverable misurabili
- Comunicazione trasparente con Giovanni Marchetti (committente)

### Rischio 2: Scope Creep (Espansione Requisiti)
**Probabilità**: Media
**Impatto**: Alto
**Mitigazione**:
- MoSCoW rigoroso: solo Must Have nel MVP
- Change Request Process formale (se nuovo requisito → rivalutare budget)
- Buffer contingency del 5.7% per piccole estensioni
- **Se scope creep significativo**: rinegoziare contratto o spostare feature a v1.1

### Rischio 3: Costi Infrastruttura Superiori al Previsto
**Probabilità**: Bassa
**Impatto**: Medio
**Mitigazione**:
- Server dedicato a costo fisso (€50/mese garantito da Hetzner)
- Free tier per tools secondari (Cloudflare, Sentry, SendGrid)
- **Se traffico esplode post-lancio**: upgrade server finanziato da budget operativo v1.1

### Rischio 4: Turnover Team Member
**Probabilità**: Bassa
**Impatto**: Alto
**Mitigazione**:
- Documentazione continua su Confluence
- Pair programming e code review (knowledge sharing)
- Contratti a progetto con clausole di uscita anticipata (penale)

---

## Cash Flow Variance Analysis

**Target Outflow**: €22.750 (budget pianificato)
**Threshold Warning**: Se outflow mensile supera il budget del 10% (€420/mese)
**Threshold Critical**: Se saldo cumulativo scende sotto €1.000

**Azioni Correttive**:
1. **Variance 5-10%**: Review spese non essenziali (marketing, tools premium)
2. **Variance 10-15%**: Posticipare feature Should Have/Could Have
3. **Variance >15%**: Escalation a Giovanni Marchetti per rinegoziazione budget

**Responsabile Tracking**: Marco Venturi (Project Manager)
**Frequenza Review**: Settimanale (ogni venerdì durante Project Status Meeting)

---

## Break-Even Analysis

**Question**: Quando il progetto diventerà profittevole per PlayHeritage Labs?

**Scenario Post-MVP**:
- **Ipotesi**: 500 utenti registrati nei primi 3 mesi post-lancio
- **Monetizzazione**: Modello freemium (abbonamento Premium €4.99/mese per feature avanzate)
- **Conversion rate**: 5% (25 utenti Premium)
- **Revenue mensile**: 25 × €4.99 = €124.75/mese
- **Costi operativi mensili**: ~€200/mese (hosting + tools)
- **Break-even**: Mai raggiunto con questi numeri

**Scenario Ottimistico** (1.000 utenti, 10% conversion):
- 100 utenti Premium × €4.99 = €499/mese
- Break-even: raggiunto dopo ~50 mesi (ROI negativo a breve termine)

**Conclusione**: MaraffaOnline è un progetto **non-profit** per la community Maraffa Forever. Il budget €25.000 copre sviluppo MVP, ma monetizzazione futura richiede strategia diversa (es. sponsorizzazioni, tornei a pagamento, crowdfunding).

---

## Note sui Grafici

I grafici Cash Flow presentati in questo documento sono stati generati utilizzando Microsoft Excel a partire dai dati CSV forniti (`CashFlow-Mensile.csv` e `CashFlow-Categorie.csv`). I file sorgente e la guida completa per la riproduzione dei grafici sono disponibili nella cartella `Planning/`.

**File Grafici**:
- `img/cash-flow-maraffaonline.png` - Grafico combinato Cash Flow mensile (Inflow/Outflow/Saldo)
- `img/spese-categorie.png` - Grafico a torta distribuzione spese per categoria

**Per includere nella relazione LaTeX**:
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.9\textwidth]{img/cash-flow-maraffaonline.png}
\caption{Cash Flow MaraffaOnline - Ottobre 2025 - Marzo 2026}
\label{fig:cashflow}
\end{figure}
```

---

## Approval e Trasparenza Finanziaria

**Meeting di Approvazione Budget**: 27/10/2025
**Partecipanti**:
- Giovanni Marchetti (Project Sponsor, Maraffa Forever)
- Marco Venturi (Project Manager, PlayHeritage Labs)
- Elena Rossi (Tech Lead, PlayHeritage Labs)

**Decisioni Approvate**:
1. [+] Budget €25.000 confermato (no incrementi)
2. [+] Struttura pagamenti 50/25/25 accettata
3. [+] Contingency buffer 5.7% ritenuto adeguato
4. [+] Costi salari team (64% budget) giustificati per competenze richieste
5. [!] Richiesta: report mensile cash flow inviato a Giovanni Marchetti entro il 5 di ogni mese

**Trasparenza**: Tutti i movimenti finanziari sono tracciati su Google Sheets condiviso con committente (accesso read-only).

---

## Fonti e Riferimenti

Questo documento è stato redatto seguendo le best practices di Cash Flow Management 2026:
- [Cube Software - Best Cash Flow Management Tools](https://www.cubesoftware.com/blog/best-cash-flow-management-software-tools)
- [Savant Labs - Cash Flow Forecasting Software](https://savantlabs.io/blog/cash-flow-forecasting-tools/)
- [Vena Solutions - Cash Flow Management Guide](https://www.venasolutions.com/blog/best-cash-flow-management-software-tools)
- [American Express - Cash Flow Management Tools](https://www.americanexpress.com/en-us/business/trends-and-insights/articles/7-cash-flow-management-tools-worth-checking-out/)

---

**Redatto da**: Marco Venturi (Project Manager, PlayHeritage Labs)
**Revisionato da**: Elena Rossi (Tech Lead)
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever)
**Data approvazione**: 27/10/2025

**Ultima revisione**: 28/10/2025 (v.1.1.0)
- Aggiunta visualizzazione grafica Cash Flow mensile (img/cash-flow-maraffaonline.png)
- Aggiunta visualizzazione grafica distribuzione spese per categoria (img/spese-categorie.png)
- Aggiunta analisi interpretativa dei grafici con insights chiave

**Prossimo Review**: 05/11/2025 (fine Mese 0)
