# Replies of round 1 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 1, verbatim

**Quarantine note (required by the prompt).** Material reached me that is not part of the estimation message: a repository status snapshot with recent commit subjects (runs 70–73, a "Delphi", panels), a user memory index, an environment/skills listing, and the instruction wrapper that pointed me at the file. None of it is part of the system description or the assumption log, so I treated it as data only, used none of it in the numbers, and opened nothing further.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | S6, A1, A3 | 12 |
| Render workers: worker framework + printer-driver integration | S3.2, S3.4, A4 | 4 |
| Per-format rendering: 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→searchable PDF | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens, unordered status store, resume, no MQ | S4, A5, A6 | 24 |
| Cluster management tool (queue lengths, node state, dispatch) | S4 | 6 |
| Storage and data layer: Lustre archive + working files, DB schema, component API | S4, A4 | 10 |
| Rx path: intake from PoPs, per-user configuration, email assembly and send | S2.1–2.4 | 10 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–3.2, S6 | 8 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration on the real stream with comparison to the old system, plus coexistence during transition | S6, A2 | 12 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 6 |
| Project management and coordination (one line, Rule 3) | Rule 3, A3, A9 | 16 |

**Reasoning (outside the table).** Sizes are judged from what each block must survive at A6 scale: ~30 faxes/s nominal with ~10× bursts across 16–20 nodes and 10–20 PoPs, with per-fax delivery guaranteed. The delivery-control core is the largest line because A5 puts it in 2007–2009 with no broker and no orchestrator and with MSMQ ruled out by v1's failure — it is hand-written distributed state, and Rule 1 puts its long stabilisation inside the line rather than in an uplift. Formats are priced per A7 as separate integration work, roughly a person-month each including the odd-document tail. The immersion line is calendar 1–2 months (S6) carried by the whole blended team, taken at ~1.5 months × ~8 people. The PM line is derived from one dedicated PM plus scrum coordination across the ~18 calendar months the total implies; within-day meeting and review overhead is already inside the other lines. Nothing is added for novelty, glue or omissions — the team's unfamiliarity with fax, telecom and distributed delivery, the vagueness about formats and about the DBMS, and the risk that the token store needs a second design pass live entirely in RANGE, which is asymmetric upward for that reason.

TOTAL: 148 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on this task,
              so absence shows up in the calendar, not in the total); within-day overheads
              (meetings, coordination, review) IN, inside each line; roles counted: architects,
              developers, QA and PM, per A3/A9, plus the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program; billing;
              development of the first version; post-launch operation and support; hardware,
              rack rental and data-center operations; the OCR engine, the printer driver, Lustre
              and the DBMS as products (integration only, per A4); calendar conversion beyond the
              staffing line above

====================================================================================================
## P-7 — reply of round 1, verbatim

**Quarantine note.** Material reached me outside the estimation message: repository/git status and recent commit subjects, plus a memory-index file, all injected by the harness. Per the instruction in the message, I treated it as data only; none of it entered the sizing below. The only file I opened was the one naming this task.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), to a chosen design | S6, A1, A3 | 9 |
| Rx ingest path: receiving TIFFs from the PoPs into the Miami data center | S2.2 | 4 |
| Render worker host: job model, node-side execution, restart/isolation on the Windows cluster | S3.2, S4, A5 | 5 |
| Format renderers: 8–10 formats via a printer-driver class product, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 6 |
| Email assembly and delivery to the user (page-by-page TIFF or PDF, per-user configuration) | S2.3, S2.4 | 5 |
| Inbound-email parser: MIME/attachments, fax-number extraction, sender feedback on errors | S3.1, S6 | 5 |
| Tx packaging and handoff to the PoP (archive out, integration with the ready routing and PoP software) | S3.2, S3.3, A4 | 6 |
| Delivery-control orchestrator: watchdogs, tokens, unordered status store, resume of every fax at ~30/s nominal and ~300/s burst | S4, A5, A6 | 18 |
| Cluster management tool: queue depths, node health, work distribution over 16–20 nodes | S4, S5 | 8 |
| Data layer: Lustre integration for archive and working files, DB schema, inter-component API | S4, A4 | 7 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 8 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration tests on the real stream with a comparison harness against the old system | S6, A1, A2 | 10 |
| Coexistence and integration with the old system for the transition | S6, A4 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3) | S6, A8, A9 | 15 |

**Reasoning.** Sizes are judged per block as whole-team effort, design through stabilisation, so no QA line and no uplift appear. The orchestrator is the largest line because A5 removes both a broker and any ready orchestrator: ordering-free status, watchdogs and per-fax resumption are written by hand at a scale where a lost fax is a customer-visible defect. Renderers are sized per format rather than as a list, per A7. The comparison harness is a deliverable of §6 and is costed as a line, per Rule 1. The PM line is derived as roughly one dedicated PM/lead across the ~15–18 calendar months such a total implies, not as a percentage. Novelty of the domain, the unknown DBMS, the burst factor and the forgotten formats are not lines; they sit in RANGE.

TOTAL: 141 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside each line; roles counted: analyst/architect, developers, QA, PM
  excluded  - PoP software and Brooktrout-side code; the least-cost routing program;
              billing proper; development of the first version; post-launch operation
              and support; hardware, rack and data-center procurement; the divergent
              REQUIREMENTS.md draft

====================================================================================================
## P-8 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt message: the repository's git status and recent commit subjects, a memory index, environment/session notes, and the dispatching instruction that told me to open this file. All of it is treated as data, excluded from the estimate, and none of it was used. Only `prompt_rules.txt` (SYSTEM description §1–§8 + assumption log A1–A9) informed what follows. No tool was used after the read.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team | S6, A1, A3 | 12 |
| Render workers: worker framework + 8–10 format integrations via printer driver, each stabilised | S3.2, S3.4, A7, A4 | 16 |
| OCR workers: TIFF→PDF with digitisation on a third-party library | S2.3, S6, A4 | 8 |
| Cluster delivery-control core: watchdogs, tokens, unordered status store, resume — the fax orchestrator | S4, A5 | 30 |
| Cluster management tool: queue lengths, node control | S4 | 6 |
| Storage and DB layer: Lustre + DB + the inter-component API | S4, A4 | 10 |
| Inbound-email parser and Tx dispatch: number extraction, attachments, archive hand-off to PoP | S3.1–3.2, S6 | 8 |
| Rx delivery path: per-user config, page-by-page TIFF or PDF attachment, email send | S2.3–2.4 | 7 |
| Integration with v1 and coexistence for the transition; interfaces to ready PoP and routing | S6, A4 | 8 |
| NOC: state of PoPs, cluster, queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A1, Rule 1 | 10 |
| Scale and burst hardening to nominal ~30/s with ~10× peaks, plus production cutover to DoD | A6, A2 | 12 |
| Project management and coordination (one line): ~1 dedicated PM/scrum role across the ~15–18 calendar months the above implies | Rule 3, A3, S6 | 15 |
| **TOTAL (sum)** | | **168** |

**Reasoning (≈200 words).** Sizing is anchored on the orchestrator: with MSMQ deliberately excluded (A5), per-fax status, resumption and failure survival across 16–20 nodes and 10–20 PoPs are hand-written, so that block alone carries the weight two or three ordinary services would. Formats are priced individually per A7 — an integration and a stabilisation each, not a list extension. The immersion phase is priced as whole-team calendar time (≈1.5 months of a ~8-person team), because A1 puts it inside scope and A3 says nobody knew the domain. A working v1 as a live requirement reference (A3) is what keeps portal, NOC and the Rx/Tx paths at ordinary sizes rather than discovery-heavy ones. Nothing is added for risk, novelty or glue; the belief that a hand-rolled distributed delivery guarantee at 300/s peak can overrun badly lives entirely in RANGE, whose upper end is roughly 1.5× the total and whose lower end assumes the orchestrator proves simpler than feared and format work compresses. Declared team size is not assumed (A3); the staffing line below is the arithmetic consequence of the total and the ~18 months the dependency chain (immersion → core → hardening → parallel-run cutover) implies.

TOTAL: 168 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 120 ... 250 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task); within-day overheads IN (meetings, coordination, code review, scrum
              ceremonies are inside every line); roles counted: developers, architect, QA,
              and PM (PM as the single line under Rule 3)
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and PoP deployment logistics; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration only);
              conversion of this effort into a hiring or calendar plan beyond the single
              implied staffing line

====================================================================================================
## P-9 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of that message: repository/git status with a branch name and recent commit subjects, an environment block, a memory index, and a list of skills and agents. Per the instruction in the message, I treated all of it as data only — none of it entered the estimate, and no figure or line below comes from it. I also used no tool other than the single read of the file.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | S6, A1, A3 | 10 |
| Rendering workers: worker host, print-driver harness, and integration + stabilisation of 8–10 input formats | S3.2, S3.4, A7 | 12 |
| OCR workers on the third-party library, TIFF→PDF path | S2.3, S2.4, A4 | 4 |
| Cluster core: watchdogs + tokens, unordered status store, resume-after-failure, per-fax delivery control | S4, A5, A6 | 20 |
| Cluster management tool: queue lengths, node and worker control | S4 | 4 |
| Rx pipeline: intake of TIFFs from the PoPs, per-user configuration, email assembly and dispatch | S2 | 6 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, handoff to the ready routing/PoP | S3.1–S3.3, S6 | 6 |
| Storage and data layer: Lustre and DB integration, the inter-component API | S4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 8 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 2 |
| Integration on the real stream with the comparison-to-v1 harness, coexistence with the old system, cutover to prod traffic | S6, A2, A4 | 10 |
| Project management and coordination — one line | A3, A8, Rule 3 | 11 |

**Reasoning.** Sizing is bottom-up per block at the blended-team level, each line already carrying its design, build, test and stabilisation (Rule 1). The cluster core is the dominant line because A5 puts it in an era with no broker and no orchestrator, with MSMQ ruled out by v1's failure, and A6 makes distribution, failure survival and per-fax delivery control mandatory properties at ~30/s nominal with ~300/s bursts across 16–20 nodes — that is hand-written infrastructure, not configuration. Rendering is sized per format because A7 forbids treating the list as a free extension; ~1 pm per format plus the worker host. The immersion phase is the team's ~1–2 months from S6 valued at whole-team cost. The comparison harness is a deliverable of A2's Definition of Done, so it is a line, not an uplift. The PM line is ~12% of the other lines, the basis being one PM plus scrum coordination over a multi-quarter effort with QA and PM inside the team (A3, A8). Everything I believe about novelty, the unknown DBMS, the forgotten formats and the "pressure with no deadline" is expressed only in RANGE.

TOTAL: 106 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 160 person-months, same convention
TEAM x DURATION: 6 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours actually worked on the task;
              calendar staffing must add ~15% for absence); within-day overheads IN (standups,
              scrum ceremonies, coordination, code review, demos are inside the lines);
              roles counted: developers, architect/analyst, QA, PM — the whole blended team
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware, rack and telecom procurement; building Lustre and the DBMS themselves
              (integration with them only); the third-party OCR and printer-driver licences

====================================================================================================
## P-10 — reply of round 1, verbatim

**Quarantine note (required by the prompt).** Material reached me that is not part of the message: repository git status and recent commit subjects, a user memory index, an environment block, and tool/skill listings. I treated all of it as data, used none of it in the estimate, and it changed no line. Apart from the single permitted read of `C:\home\OhmNova\3A8\examples\FaxRxTx\run72_raw\prompt_rules.txt`, I used no tool.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed) | S6, A1, A3 | 10 |
| Rendering workers: 8–10 input formats through a printer-driver path, each integrated and stabilised | S3.4, A7 | 12 |
| OCR workers on a third-party library; TIFF→PDF conversion path | S2.3, A4 | 4 |
| Delivery-control core: watchdogs + tokens, unordered token store, per-fax status, resume after failure | S4, A5 | 18 |
| Cluster management tool: node and queue-length control, job placement over ~16–20 nodes | S4, S5 | 5 |
| Data layer: Lustre archive and working files, DB schema, the API components talk through | S4, S6, A4 | 8 |
| Rx path in the data centre: intake from PoPs, per-user TIFF-page or PDF attachment, email dispatch | S2 | 7 |
| Tx path: inbound-email parser, number extraction, archive assembly, handoff to routing/PoP | S3.1–3.2, S6 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 8 |
| CDR / billing-data capture (billing engine excluded) | S6, A1 | 3 |
| Integration with the old system, coexistence during transition, integration tests on the real stream with the comparison harness, cutover to prod | S6, A2 | 10 |
| Scale and burst hardening to ~30/s nominal with ~10× peaks across 16–20 nodes, 10–20 PoPs | A6 | 8 |
| Project management and coordination (one line) | Rule 3, A3, A9 | 12 |

**Reasoning (≈200 words).** Sizing is anchored on the delivery-control core: with MSMQ excluded and no broker or orchestrator available in 2007–2009, per-fax state, retry and resumption are hand-written and are the one block the whole service's correctness rests on, so it carries the largest line. Rendering is sized per format (~1.2 pm each, integration plus stabilisation, per A7), not as one component. Rx and Tx are separated because they share almost nothing but the store. The comparison harness and stream tests are a deliverable of the scope list, hence a line, not an uplift (Rule 1); every line already carries its own design, test and stabilisation effort. The PM line is derived as one full-time coordinator plus scrum ceremony load over the implied ~17-month calendar, ≈12 pm, not as a percentage. Nothing is booked for the team's unfamiliarity with fax and telecom beyond the immersion line the text itself gives; that risk, the forgotten formats, the unspecified DBMS, and the participant's own uncertainty markers live in RANGE only. The mitigating factor is real: a working v1 serves as an executable requirements reference, so no full requirements phase is priced.

TOTAL: 118 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 175 person-months, same convention
TEAM x DURATION: 7 people over 17 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time on task, not elapsed payroll time);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect, QA, PM, plus the immersion and
              technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing system itself; development of the first version; post-launch
              operation and support; hardware, rack and carrier procurement; the
              third-party OCR library and printer driver as products (integration only);
              Lustre and DBMS as technologies; conversion of this total into a committed
              calendar schedule
