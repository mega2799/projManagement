# Allegato 4.1 - Project Kick-Off Meeting
## v.2.1.0 – 2026-08-02

Verbale del meeting di avvio del progetto MaraffaOnline. Il kick-off segna il passaggio dalla pianificazione all'esecuzione: serve ad allineare il team su obiettivi, ruoli e regole operative prima dell'inizio dello sviluppo.

## Informazioni generali

- **Data e orario**: 15 ottobre 2025, 10:00–11:00
- **Modalità**: ibrida (sede PlayHeritage Labs + Zoom)
- **Facilitatore**: Marco Venturi (Project Manager)
- **Verbale a cura di**: Andrea Conti

## Partecipanti

| Nome | Ruolo | Presenza |
|------|-------|----------|
| Marco Venturi | Project Manager | In presenza |
| Elena Rossi | Tech Lead / Game Engine | In presenza |
| Sara Bianchi | Backend Developer | In presenza |
| Luca Moretti | UX / Frontend | In presenza |
| Andrea Conti | DevOps | In presenza |
| Giovanni Marchetti | Sponsor (Maraffa Forever) | Remoto |
| Francesca Giuliani | Esperta di dominio (Maraffa Forever) | Remoto |

## Materiali condivisi prima del meeting

Venerdì 10 ottobre sono stati inviati ai partecipanti il Project Overview Statement (Allegato 2.3), la WBS (3.1), il Gantt con il critical path (3.5), il Cash Flow (3.4) e le bozze di RASCI Matrix e Regole Operative (4.2), così da arrivare preparati e ridurre il tempo di presentazione durante il meeting.

## Temi trattati

Dopo il benvenuto e un breve giro di presentazioni, Marco ha ripreso vision e obiettivi del progetto (dettagliati nel POS, Allegato 2.3): realizzare entro il 15 maggio 2026 una piattaforma web per giocare al Maraffone in multiplayer, fedele alle regole ufficiali e con un'esperienza fluida, e i criteri di successo concordati in fase di Scoping (Allegato 2.2).

Elena ha ricapitolato lo scope dell'MVP — i sei sottosistemi di sviluppo (Game Engine, Backend, Real-Time, Frontend, Social & Community, Infrastructure) più le attività trasversali di Testing/QA, con la prioritizzazione MoSCoW dell'Allegato 3.2 — e ciò che resta esplicitamente fuori dalla prima release: app mobile nativa, modalità single-player contro AI, tornei e monetizzazione.

Sono state poi ripercorse la timeline e le milestone M1–M7 (dal Gantt, Allegato 3.5), con particolare attenzione all'attività più critica, il Frontend Tavolo da Gioco, che si trova sul percorso critico e sarà seguita da Luca con il supporto di Sara per i componenti più complessi. Marco ha ricordato la struttura di pagamento a corpo in tre tranche 50/25/25 (15 ottobre alla firma, 15 dicembre a valle del Backend Core, 15 febbraio al completamento del core di gioco), coerente con il Cash Flow (Allegato 3.4), e il budget complessivo di €25.000 con spese previste di €22.750.

Elena ha infine richiamato i rischi principali dalla Risk Rating Matrix (Allegato 2.4) — su tutti l'esperienza limitata del team con le tecnologie WebSocket e il rischio di scope creep — con le relative mitigazioni (spike tecnico e proof of concept sul real-time nei primi sprint; Change Request Process per lo scope). Andrea ha presentato gli strumenti di lavoro condivisi (GitLab per codice e CI/CD, Notion per documentazione e task tracking, Figma per il design, Zoom e Slack per la comunicazione) e la cadenza dei meeting ricorrenti. I ruoli e le responsabilità di dettaglio sono definiti nella RASCI Matrix (Allegato 4.2).

## Decisioni approvate

1. Timeline di 7 mesi confermata (15/10/2025 – 15/05/2026).
2. Budget di €25.000 confermato, senza incrementi.
3. Scope dell'MVP confermato (esclusi app mobile nativa, AI, tornei, monetizzazione).
4. RASCI Matrix e Regole Operative approvate (Allegato 4.2).
5. Calendario a 15 sprint da due settimane (Sprint 0–14), con Daily Standup dalle 09:00 a partire dal 16/10/2025.

## Action item

| # | Azione | Owner | Scadenza |
|---|--------|-------|----------|
| 1 | Inviti alle piattaforme (GitLab, Figma, Notion, Slack, Zoom) | Andrea Conti | 16/10 |
| 2 | Setup server Hetzner + Docker + CI/CD di base | Andrea Conti | 24/10 |
| 3 | Spike tecnico Socket.IO con test di latenza preliminare | Sara Bianchi | 27/10 |
| 4 | Database schema PostgreSQL (utenti, partite, mosse) | Sara Bianchi | 27/10 |
| 5 | Sprint 1 Planning (selezione user stories e stime) | Marco Venturi / Elena Rossi | 27/10 |
| 6 | Conferma date delle sessioni di validazione regole | Francesca Giuliani | 17/10 |
| 7 | Approvazione formale del verbale di kick-off | Giovanni Marchetti | 20/10 |

Gli action item sono tracciati su Notion.

## Prossimi appuntamenti

- Primo Daily Standup: 16/10/2025, 09:00
- Primo Project Status Meeting: venerdì 17/10/2025, 16:00
- Sprint 0 Review (setup infrastruttura + esito spike Socket.IO): venerdì 24/10/2025

---

**Redatto da**: Marco Venturi (Project Manager) — **Verbale a cura di**: Andrea Conti
**Approvato da**: Giovanni Marchetti (Project Sponsor, Maraffa Forever), 20/10/2025

**Storico revisioni**:
- **v.2.1.0**: Ruolo di Elena Rossi corretto da "Tech Lead / Backend" a "Tech Lead / Game Engine", in coerenza con Allegato 2.1, WBS/Gantt e RASCI v.1.4.0.
- **v.2.0.0**: Verbale snellito e reso più realistico. Rimossi i dialoghi Q&A ricostruiti, le citazioni sceneggiate, le tabelle che duplicavano altri allegati (effort per sottosistema, milestone, budget, top rischi) e i framework di processo sovra-dettagliati (SLA a ore, livelli decisionali, conflict resolution): il dettaglio resta nei rispettivi allegati, qui richiamati. Mantenuti partecipanti, temi trattati, decisioni, action item e prossimi passi.
- **v.1.1.0**: Revisione di coerenza — milestone allineate al Gantt (M1–M7) e pagamenti al Cash Flow (15 Ott / 15 Dic / 15 Feb); effort per sottosistema allineato ai totali del MoSCoW; calendario completato a 15 sprint (0–14); aggiunta la voce di budget Marketing/UAT/Celebrazione; refusi e valuta uniformati.
