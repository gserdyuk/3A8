# Replies of round 1 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 1, verbatim

Quarantine notice: material reached me that is not part of the estimate message — repository status and recent commit subjects (including ones naming runs 70–73 and a "Delphi" exchange), a memory index, an environment block and a tool/skill listing. None of it is part of SYSTEM.md or the assumption log. I treated it as data, used none of it in the estimate, and continued.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | §6, A1, A3 | 12 |
| Rendering workers: worker framework plus 8–10 input formats integrated and stabilised via a printer-driver path | §3.2, §3.4, A7, A4 | 11 |
| OCR workers and TIFF→PDF conversion on a third-party library, per-user page-by-page vs PDF configuration | §2.3, A4 | 5 |
| Cluster with the delivery-control mechanism: watchdogs, tokens, unordered status store, resume of every fax at ~30/s nominal with ~300/s bursts | §4, A5, A6 | 20 |
| Cluster management tool: queue lengths, node health and work placement over 16–20 nodes | §4, §5 | 6 |
| NOC internal control centre: state of 10–20 PoPs, the cluster and the queues | §4, §6 | 8 |
| User portal | §4, §6 | 8 |
| Inbound-email parser on the Tx path: parse, extract fax number, attachments, archive hand-off to a PoP | §3.1–3.2, §6 | 6 |
| Rx path in the data centre: intake of TIFF from the PoPs, per-user configuration, email assembly and delivery | §2.2–2.4 | 6 |
| Integration with the reused parts: PoP software, least-cost routing, Lustre, the DB and the inter-component API | §4, §6, A4 | 8 |
| CDR and billing-data capture (billing itself out) | §6, A1 | 2 |
| Integration tests on the real stream and the comparison harness against the old system, plus coexistence during transition | §6, A1, A2 | 9 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 4 |
| Project management and coordination (one line): one PM/scrum lead at ~0.7 FTE across the ~22 calendar months, plus release coordination | §6, A3, A8 | 15 |

Reasoning. Line sizes are judged bottom-up per block at blended cost, each already carrying its own design, build, test and stabilisation. The two dominant lines are the hand-written orchestration (A5 — no broker, no orchestrator, MSMQ ruled out, and every fax must be individually tracked and resumed) and rendering, where A7 forbids treating extra formats as free. Immersion is taken as ~1.5 calendar months for a team of about eight. The reused assets (A4) cut build cost but not integration cost, so they appear as an integration line rather than as a discount. The comparison harness is a deliverable, not a testing uplift, so it sits inside the integration-test line. Nothing in the table stands for risk, novelty or friction; those live only in RANGE, which is wide downward because the sizes assume a design to nominal with burst resilience, and wide upward because the domain is new and the storage and cluster substrate was unusual for the era.

TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 175 person-months, same convention
TEAM x DURATION: 6 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time on the task); within-day overheads
              (meetings, coordination, review) IN, inside each line; roles counted: developers,
              architects, QA and PM, blended
  excluded  - PoP software, least-cost routing, billing, first-version development, post-launch
              operation, hardware and data-centre procurement, calendar conversion beyond the
              staffing line above

====================================================================================================
## P-2 — reply of round 1, verbatim

I read the file and follow it. One thing it requires me to report: material did reach me that is not part of that message — repository status and recent commit subjects, a memory index, an environment block and a skill list, all injected by the harness around the prompt. I quarantined it: none of it entered the estimate, and I used no tool other than the single read.

**Decomposition**

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team | S6, A1, A3 | 10 |
| Rendering workers: worker framework + 8–10 formats integrated and stabilised via the printer driver | S3.4, A7 | 15 |
| OCR workers and TIFF→PDF conversion on a third-party library, per-user page-by-page vs PDF | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 24 |
| Cluster management tool: node and queue-length control, job distribution over 16–20 nodes | S4, A6 | 10 |
| Rx path in the data centre: intake of TIFF from PoPs, user configuration, e-mail assembly and dispatch | S2.2–2.4 | 9 |
| Tx path: inbound-mail parser, number extraction, attachment handling, archive hand-off to a PoP | S3.1–3.2, A1 | 8 |
| Data layer: DB schema and the API the components talk through; Lustre archive and working files | S4, A4 | 10 |
| Integration with the reused PoP software and routing, plus coexistence with v1 through the transition | S6, A4 | 8 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| CDR / billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration-test harness on the real stream with result comparison to the old system | S6, A1, Rule 1 | 9 |
| Scale and burst hardening to ~30/s nominal with ~10× peaks: distribution, failure survival, load runs | A6 | 10 |
| Production rollout: cutover onto live traffic to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3) | S6, A8 | 15 |

**Reasoning (≈200 words)**

Each line is the blended team's whole effort on that block, testing included; no uplift is added anywhere.

The largest line is the hand-built orchestrator. In the 2007–2009 setting (A5) with MSMQ ruled out by v1's failure, per-fax status, watchdogs, tokens and resume are written from scratch — this is the piece that has no library behind it and has to hold at a million faxes a day.

Rendering is sized as a framework plus per-format work, because A7 says each format is its own integration and stabilisation, not a free list entry.

Immersion is sized as the team-month or two of S6 spread over the whole blended team, not one person's reading.

The PM line is one full-time PM/scrum lead across the build, about a tenth of the other lines.

Novelty, the team's ignorance of the domain, the forgotten formats, the vagueness of "16 or 20 nodes", and the risk that coexistence with v1 costs more than integration — none of these are lines. They are why RANGE is wide and asymmetric upward.

TEAM × DURATION assumes ~10.5 on-task person-months per person-calendar-year, matching the declaration below.

```
TOTAL: 165 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 120 ... 240 person-months, same convention
TEAM x DURATION: 10 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task); within-day overheads IN (standups, coordination, code review,
              scrum ceremonies are inside every line); roles counted: developers,
              architect, QA and PM, as one blended team per Rule 1
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing
              program, billing itself, development of the first version, post-launch
              operation and support, hardware and rack/telecom procurement, third-party
              licences (OCR library, printer driver, Lustre), and any calendar
              conversion beyond the implied staffing line above
```

====================================================================================================
## P-3 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt message: the session environment block (working directory, git status, recent commit subjects mentioning runs 70–73 and a "Delphi" exercise), a memory index, and a skills/tool listing. I treated all of it as data, used none of it, and proceeded from the prompt text alone.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed) | S6, A1, A3 | 12 |
| Rx path in the data center: intake of TIFF from the PoPs, per-user configuration, email composition and dispatch | S2.2–S2.4 | 10 |
| Rendering workers: 8–10 input formats through a printer-driver path, each integrated and stabilised | S3.2, S3.4, A7 | 14 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Inbound-email parser and the Tx assembly: address parsing, number extraction, archive hand-off to a PoP | S3.1–S3.2, S6 | 8 |
| Cluster with the delivery-control mechanism: watchdogs, tokens, unordered status store, resume — the hand-built orchestrator at nominal 30/s with 10× bursts | S4, A5, A6 | 24 |
| Cluster management tool: queue lengths, node state, operator actions | S4 | 6 |
| Storage and data layer: Lustre for archive and working files, the DB, the inter-component API | S4, A4 | 10 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A2 | 12 |
| Coexistence and integration with the old system, cutover, rollout to prod | S6, A1, A2 | 8 |
| Project management and coordination — one dedicated PM/coordination role across the ~18 calendar months the build implies | Rule 3, A8, A9 | 18 |

**Reasoning.** The shape of the estimate is set by three facts in the text. First, no reuse (A4): every line is built from zero, so the sizes are build-sizes, not adaptation-sizes. Second, the era (A5): what a broker or an orchestrator would supply today is hand-written here, which is why the watchdog-and-token cluster is the single largest line — it carries per-fax status, failure survival and resumption, and it must hold at burst (A6). Third, breadth: the scope is not one service but seven deliverable surfaces (Rx, Tx, cluster, NOC, portal, data layer, CDR) plus a test rig that the text names as a deliverable, so Rule 1 puts it in the table rather than on top.

Format counts (A7) are priced as ten small integrations rather than one renderer. The mitigating factor of a live v1 (A3) is real but partial: it removes requirements discovery, not domain learning, so the immersion line stays at the upper end of its stated 1–2 months across a full team.

Uncertainty that is not work stays out of TOTAL per Rule 2 and lands in RANGE: unnamed DBMS, forgotten formats, how hard Lustre proves under this load, and how much the old-system comparison drags at cutover.

```
TOTAL: 154 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 230 person-months, same convention
TEAM x DURATION: ~9 people over ~18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours of work on the task, not
              elapsed payroll time); within-day overheads IN (standups, coordination,
              code review, design discussion are inside every line per Rule 1);
              roles counted: architects, developers, QA and DevOps/infra engineers inside
              the lines, project management as the single top line per Rule 3
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and data-center operations; the third-party
              OCR library and printer driver themselves (integration only); conversion of
              this total into a committed calendar plan beyond the staffing shown above
```

====================================================================================================
## P-4 — reply of round 1, verbatim

I read the file; below is the reply it asks for.

**Quarantine note.** Material reached me that is not part of that message — repository status, a branch and commit subjects, memory/index text, and environment notes. None of it is part of the system description or the assumption log, so I treated it as data, excluded it from the estimate, and continued.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives) | S6, A1, A3 | 12 |
| Rendering workers: 8–10 input formats through a printer driver, each integrated and stabilised | S3.4, A7, A4 | 14 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, S2.4, A4 | 6 |
| Cluster core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 24 |
| Cluster management tool (queue lengths, node state) | S4 | 6 |
| Rx path: intake of TIFF from the PoPs, per-user configuration, email assembly and dispatch | S2 | 10 |
| Tx path: inbound-email parser, fax-number extraction, archive packaging and handoff to a PoP | S3.1, S3.2, S6 | 8 |
| Data layer: Lustre and DB integration, inter-component API | S4, A4 | 8 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 9 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration with the old system and coexistence through the transition | S6, A4 | 5 |
| Integration tests on the real stream, comparison harness against the old system, rollout to prod | S6, A2 | 10 |
| Scale and burst hardening to ~30/s nominal with ~10× bursts across 16–20 nodes and 10–20 PoPs | S5, A6 | 8 |
| Project management and coordination (one line) | S6, A8, Rule 3 | 13 |

Reasoning. The sizes follow the blended team doing each block end to end, testing included, as Rule 1 requires. The heaviest line is the hand-built delivery control: with MSMQ deliberately excluded and no broker or orchestrator available in the 2007–2009 stack (A5), exactly-once-ish fax orchestration, watchdogs, tokens and recovery are written from scratch, and correctness under ~1M faxes/day is where the work concentrates. Rendering is sized per format because A7 says each format is its own integration and stabilisation, not a free list extension. Immersion is ~1.5 calendar months of the whole team, priced as team-months rather than a lone architect's time. Portal and NOC are ordinary application work on a new data model. The comparison harness against v1 is a deliverable, so it is a line, not an uplift. No reuse credit is taken against the lines (A4); what is reused is simply absent from the table. Everything I believe about novelty, an unknown domain, telecom friction, forgotten formats and the two-year dating uncertainty lives in RANGE only. The PM line is ~10% of the other lines, the usual share for a scrum team of this size with an internal, no-hard-deadline sponsor (A8).

TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task); within-day
              overheads (meetings, coordination, review) IN, inside each line; roles counted:
              developers, architect, QA, and PM as the single line on top
  excluded  - PoP software, least-cost routing, billing, post-launch operation, development of
              the v1 system, hardware/rack procurement and data-center operations, and the
              calendar conversion itself (A1, A4, A9)

====================================================================================================
## P-5 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt: repository/git status and recent commit subjects, a memory-index file listing, environment and tool-availability reminders, and an operator instruction about which file to read. I treated all of it as data, used none of it as input to this estimate, and proceeded.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | S6, A1, A3 | 10 |
| Rendering workers: worker framework + 8–10 formats via printer driver | S3.2, S3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 6 |
| Delivery-control orchestrator: watchdogs, tokens, unordered status store, resume | S4, A5 | 24 |
| Cluster runtime: job distribution over ~16–20 nodes, failure survival | S4, S5, A6 | 12 |
| Cluster management tool (queue lengths, node control) | S4 | 5 |
| Rx datacenter path: PoP intake, per-user config, email composition and send | S2 | 8 |
| Tx path: inbound-email parser, number extraction, archive hand-off | S3.1–3.2, S6 | 8 |
| Data layer: Lustre integration, fax archive, DB schema, inter-component API | S4, A4 | 10 |
| NOC: state of PoPs, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration with the old system and coexistence for the transition | S6, A4 | 6 |
| Integration tests on the real stream + comparison harness vs old system | S6, A2 | 10 |
| Scale and burst hardening to 30/s nominal, ~300/s peak | A6 | 10 |
| Production rollout, cutover, decommissioning of v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3) | A3, A8 | 15 |

**Reasoning (≈200 words).** Each line is the blended team's whole effort on that block, testing included; no QA line and no uplift are added. Sizing is driven by three things the text makes explicit. First, the era (A5): with MSMQ ruled out and no broker or orchestrator available, the delivery guarantee for every one of a million faxes a day is hand-written — that is why the watchdog/token orchestrator is the largest line by a wide margin, and why cluster runtime and hardening are separately substantial. Second, breadth (S4, S6): NOC, portal, both mail paths and the data layer are independent products sharing only the DB and API, so they add rather than overlap. Third, A7: formats are integration work, not list entries, so rendering is framework plus roughly a per-format unit.

The mitigating factor is a live v1 as the requirements reference (A3) — no greenfield requirements phase — offset by a team new to the domain and by zero code reuse (A4).

The PM line is derived as ~10 percent of the sixteen work lines across a roughly two-year effort with scrum after a planning phase (A8).

Uncertainty about the forgotten formats, the unspecified DBMS, and how much burst work "10×" truly demanded lives in RANGE, not in TOTAL.

```
TOTAL: 167 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 120 ... 240 person-months, same convention
TEAM x DURATION: ~8-9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect, QA, PM - one blended team
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR capture is in); development of the first version;
              post-launch operation and support; hardware, datacenter and network
              procurement; Lustre and DBMS administration; the third-party OCR and
              printer-driver licences (integrated, not built)
```
