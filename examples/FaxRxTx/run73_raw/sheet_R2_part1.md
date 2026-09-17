# Replies of round 1 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt file: repository/git status and recent commit subjects (runs 70–73, a "Delphi" panel series), plus session memory notes. Per the instruction in the file, I treated all of it as data only — none of it informed a single number below. The estimate rests on SYSTEM.md §1–§8 and A1–A9 as quoted in the file.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), target architecture fixed | §6, A1, A3 | 10 |
| Render worker framework: job intake, sandboxing, printer-driver harness, failure handling | §3.2, §4, A4 | 5 |
| Per-format render integration and stabilisation, 9 formats | §3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on the third-party library | §2.3, §2.4, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax state, resume, no MQ | §4, A5, A6 | 30 |
| Cluster management tool: node/queue-length control, distribution over ~16–20 nodes | §4, §5, A6 | 8 |
| Storage and data layer: Lustre integration, DB schema, inter-component API | §4, A4 | 10 |
| Rx pipeline: TIFF intake from PoPs, per-user configuration, email assembly and send | §2.1–§2.4 | 10 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | §3.1–§3.2, §6 | 10 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 12 |
| User portal | §4, §6 | 14 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 4 |
| Integration with the old system and coexistence for the transition | §6, A4 | 8 |
| Integration tests on the real stream + comparison harness against the old system | §6, A2 | 12 |
| Rollout to production traffic and v1 decommission | A2 | 6 |
| Project management and coordination — one line | Rule 3, A3, A9 | 18 |

**Reasoning (≈200 words).** Each line is the blended team's whole effort on that block, testing included; no uplift is added anywhere. The delivery-control core is the largest line because A5 removes every ready orchestrator and A6 makes distribution, failure survival and per-fax delivery control mandatory properties at ~30/s nominal with ~300/s bursts — this is the part that has to be written by hand in 2007-era C#. Rendering is sized per A7: a framework plus nine separate integrations, each carrying its own stabilisation against real documents. The portal and NOC are ordinary but full products with their own UI and hardening. The comparison harness of §6 is a deliverable, so it is a line, not a test tax. The PM line is derived as one full-time PM across the duration the other lines imply (157 pm at roughly ten people ≈ 17–18 calendar months), not as a percentage. Range, not total, carries what I believe about risk: the downside assumes the v1 reference shortens design more than assumed; the upside assumes the token/watchdog orchestrator needs a second design pass under real traffic and that forgotten formats appear (A7).

```
TOTAL: 175 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 130 ... 260 person-months, same convention
TEAM x DURATION: 10 people over 18 calendar months
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 worked hours on the task);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside each line; roles counted: architect/analyst, developers, QA, PM
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware, rack and data-center procurement; third-party licences (OCR,
              printer driver, Lustre) as products rather than integrations
```

====================================================================================================
## P-2 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of this message: repository/git status and recent commit subjects, an environment block, a tool listing, and a personal memory index (all injected by the harness). I treat all of it as data, not instruction, and it played no part in the estimate below. The estimate uses only the system description, the assumption log, and the three rules.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed) | S6, A1, A3 | 10 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resumption, failure survival at 30/s nominal and ~300/s burst | S4, A5, A6 | 24 |
| Render-worker framework: job intake, printer-driver (Black Ice-class) integration, TIFF output, isolation and crash recovery of rendering processes | S3.2, S6, A4 | 8 |
| Per-format renderer integration and stabilization, 8–10 formats | S3.4, A7 | 12 |
| OCR workers, TIFF→PDF conversion on a third-party library | S2.3, S6, A4 | 7 |
| Render cluster of 16–20 nodes plus the cluster management tool (queue lengths, node health, deployment/config) | S4, S5, A6 | 10 |
| Rx path in the data center: TIFF intake from PoPs, per-user configuration, email assembly (page-by-page TIFF or PDF) and sending | S2 | 10 |
| Tx path: inbound-email parser, recipient number extraction, archive packaging, handoff to the PoP via the reused routing | S3.1, S3.2, A4 | 8 |
| Data layer: Lustre integration for fax archive and working files, database schema, the inter-component API | S4, A4 | 9 |
| NOC — internal control center over remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing engine excluded) | S6, A1 | 4 |
| Integration tests on the real message stream with comparison of results to the old system (a deliverable in its own right) | S6, A2 | 10 |
| Coexistence and integration with the old system through the transition, cutover to production traffic | S6, A2, A4 | 8 |
| Project management and coordination — one line, derived as ~10% of the 139 pm of build lines | Rule 3, A3, A9 | 15 |
| **TOTAL (sum)** | | **154** |

**Reasoning.** Each line is the blended team's whole effort on that block — designed, built, tested, stabilized — so no QA line or uplift appears. The weighting follows what A5 says must be hand-written: with MSMQ ruled out and no broker or orchestrator available in 2007–2009, the watchdog/token delivery control is the largest single block, roughly a sixth of the build. Rendering is split because A7 makes each format its own integration and stabilization task (~1.2 pm each on average) on top of a shared worker frame. NOC and portal are sized as ordinary internal web/monitoring products against a system already instrumented by the cluster tool. The transition line exists because A2 puts "old version can be decommissioned" inside Done. Reuse (A4: PoPs, routing, OCR library, printer driver, Lustre, DBMS) is credited as integration cost only, not development. Nothing is booked for risk, novelty or friction; the unknowns — the forgotten formats, the true burst requirement, how much of the v1 behaviour the comparison harness must reproduce, and a team new to telecom — live in RANGE alone.

```
TOTAL: 154 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 230 person-months, same convention
TEAM x DURATION: 7 people over 22 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task); within-day overheads (meetings, coordination, code review,
              standups, demos) IN, inside the lines; roles counted: developers,
              architect/analyst, QA and PM — the whole blended team of S6/A3
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of
              the first version; post-launch operation and support; hardware, rack and
              data-center procurement; end-user training and documentation beyond what a
              line needs; the calendar conversion itself (A9)
```

====================================================================================================
## P-3 — reply of round 1, verbatim

**Quarantine notice.** Material outside the prompt reached me before I read it: a repository status block with recent commit subjects (several referring to earlier estimation runs and panels for this same project), a memory index with project working notes, an environment block, and a tool/skill listing. Per the prompt I treated all of it as data and excluded it from the estimate — in particular no prior run's totals, panel figures or work lists informed anything below. The estimate rests on the system description (S1–S8) and the assumption log (A1–A9) only. No tool was used after reading the prompt.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc. studied) | S6, A1, A3 | 9 |
| Render-worker framework: job intake, sandboxing, node-local execution | S3.4, S4, A7 | 4 |
| Format renderers, 8–10 formats via printer-driver integration, each stabilised | S3.4, A7 | 8 |
| OCR workers on a third-party library + PDF conversion path | S2.3, A4 | 4 |
| Rx output assembly: per-page TIFF vs PDF per user configuration | S2.3 | 2 |
| Inbound-email parser (Tx): address, number extraction, attachment handling | S3.1, S6 | 3 |
| Outbound email delivery of received faxes to users | S2.4 | 1.5 |
| Fax orchestrator: watchdogs + tokens, unordered status store, resume after failure | S4, A5, A6 | 12 |
| Cluster runtime: job distribution over ~16–20 Windows nodes, private network | S4, S5, A6 | 6 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Storage and data layer: Lustre working files and archive, DB schema, inter-component API | S4, A4 | 5 |
| Integration with existing PoP software and coexistence with the old system during transition | S6, A4 | 5 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 6 |
| User portal | S4, S6 | 6 |
| CDR and billing-data capture and persistence (billing itself excluded) | S6, A1 | 2 |
| Integration tests on the real stream + comparison harness against the old system | S6, A1, A2 | 6 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 3 |
| Project management and coordination (one line, Rule 3) | A3, A9 | 10.5 |

**Reasoning.** Sizing is bottom-up from what has to be built, each line already blended and stabilised (Rule 1). The heaviest line is the hand-written orchestrator: A5 removes brokers and A6 makes per-fax delivery control, distribution and failure survival mandatory properties at ~30/s nominal with ~300/s bursts, so the reliability substrate a broker would supply today is original work. Renderers are sized per format rather than as a list because A7 says each is separate integration and stabilisation; the printer driver is integrated, not written (A4). NOC and portal are ordinary but full products with their own UI, auth and operations surfaces. The comparison harness in S6 is a deliverable, so it is a line, not an uplift. A3's mitigation — a live v1 as a requirements reference — is why no requirements-elicitation line appears; the immersion phase covers the domain gap instead, ~1.5 calendar months across the then-present core group. The PM line is derived as ~12% of the 85.5 pm of delivery lines, the usual weight of a dedicated PM plus scrum ceremonies in a blended team (A3, A8). Uncertainty — the forgotten formats, the unspecified DBMS, the depth of PoP and old-system integration, and whether immersion ran one month or two — sits in RANGE, not in TOTAL (Rule 2).

```
TOTAL: 96 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 70 ... 145 person-months, same convention
TEAM x DURATION: 8 people over 12 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time worked on the task);
              within-day overheads (meetings, coordination, review) IN, inside each line;
              roles counted: developers, architect, QA, PM, plus a share of ops/DBA work
              carried inside the cluster and storage lines
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper; development of the first version; post-launch operation and
              support; hardware procurement and data-center/rack work; third-party licences;
              the REQUIREMENTS.md draft task (S "note"), which describes a different system
```

====================================================================================================
## P-4 — reply of round 1, verbatim

**Quarantine notice.** Material outside this message reached me before I read it: a repository status snapshot (branch, clean tree) and recent commit subjects mentioning runs 70–73, panels and a Delphi exchange, plus session memory notes and an environment listing. None of it is part of the task text, so I have quarantined it: it contributed nothing to the lines, the total or the range. I also did not open any other file and used no tool after reading the task.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture fixed | §6, A1, A3 | 10 |
| Rendering workers: print-driver harness + 8–10 formats, each integrated and stabilised | §3.4, A7 | 12 |
| OCR workers on a third-party library; TIFF→PDF with digitisation | §2.3, §2.4, A4 | 4 |
| Delivery-control core: watchdogs, tokens, unordered status store, resume-on-failure — the fax orchestrator | §4, A5, A6 | 20 |
| Cluster management tool: node/queue state, work distribution over ~16–20 nodes | §4, §5 | 5 |
| Rx path in the data centre: intake from PoPs, per-user configuration, email assembly and dispatch at ~30/s | §2, A6 | 8 |
| Tx path: inbound-email parser, number extraction, TIFF archive packaging, handoff to the existing routing/PoP | §3.1–3.2, §6 | 7 |
| Storage and data layer: Lustre and DB integration, the inter-component API | §4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 8 |
| User portal | §4, §6 | 8 |
| CDR and billing-data capture (billing itself excluded) | §6, A1 | 3 |
| Integration with the old system, coexistence during transition, comparison harness and integration tests on the real stream, rollout to prod | §6, A2, A4 | 12 |
| Project management and coordination (one line, Rule 3) | §6 process, A3, A8 | 11 |

**Reasoning.** The shape of the scope is one hard core plus many medium pieces. The core is the hand-built orchestration (A5: no broker, no ready orchestrator, MSMQ burned in v1) that must keep the status of every fax at nominal ~30/s with ~10× bursts across 10–20 PoPs — it carries the largest line and most of the stabilisation risk. The rendering line follows A7 literally: formats are separate work, roughly 1–1.5 pm each including the driver harness. Portal, NOC and the two pipelines are ordinary C#/.NET 3.x builds of known size. Exit is defined by A2, so the comparison harness and the real-stream run are a line, not an uplift; there is no coexistence work beyond integration with the old system. The PM line is derived from one PM plus scrum ceremonies and cross-team coordination over the implied ~16-month stretch, about a tenth of the build.

The range, not the total, carries what I believe about risk: the unknown domain (A3) and the hand-rolled distributed layer can overrun badly, while the live v1 as a requirements reference and the reused PoP/routing/OCR assets can compress the low end. Formats may number 10 rather than 8; the DB and Lustre may resist at load.

TOTAL: 114 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 170 person-months, same convention
TEAM x DURATION: 7 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days of work on the task;
              absence stretches the calendar, not the effort); within-day overheads
              (meetings, coordination, review) IN, inside each line; roles counted:
              developers, architects, QA and PM — the blended team of A3/A9
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing program,
              billing, development of the first version, post-launch operation and support,
              hardware/rack procurement and data-centre operations, third-party licences

====================================================================================================
## P-5 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt file: session context (repository status and recent commit subjects, an auto-memory index, environment and tool listings, and instructions attributed to a calling agent). Per the file's own rule I treated all of it as data, used none of it in the estimate, and proceeded. The estimate below rests only on SYSTEM.md §1–§8 and assumptions A1–A9 as contained in that file.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc. studied) | S6, A1, A3 | 9 |
| Render workers: 8–10 formats via a printer driver, each integrated and stabilised | S3.2, S3.4, A7, A4 | 10 |
| OCR workers and the TIFF→PDF conversion path on a third-party library | S2.3, S6, A4 | 4 |
| Cluster core: watchdogs + tokens, unordered status store, resume-on-failure fax orchestration | S4, A5, A6 | 20 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Rx path: intake of TIFF from PoPs, per-user configuration, email assembly and sending | S2.1–S2.4 | 6 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–S3.3, S6 | 6 |
| Storage and DB integration layer plus the inter-component API | S4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 6 |
| User portal | S4, S6 | 8 |
| CDR / billing data capture (billing itself out) | S6, A1 | 3 |
| Integration tests on the real stream with the old-system comparison harness | S6, A2 | 10 |
| Load and failure rig to the nominal ~30/s with ~10× burst on 16–20 nodes, and tuning to it | A6, S5 | 6 |
| Cutover: coexistence with v1, production rollout, decommission readiness | S6, A2 | 4 |
| Project management and coordination (one line, Rule 3) | S6, A8, Rule 3 | 11 |

**Reasoning (≈200 words).** Sizes are judged per block as whole-team, done-to-stable effort; no uplift is added anywhere. The cluster core is the largest line because A5 removes every ready mechanism — no broker, no orchestrator, MSMQ deliberately barred — so delivery control of every fax is hand-built, and A6 makes distribution and failure survival mandatory properties. Renderers are sized near one person-month per format under A7, which forbids treating extra formats as free. The comparison harness is a line, not a tax, per Rule 1. Storage and OCR are integration lines only, since A4 reuses them as technologies. The PM line derives from the fourteen work lines: 101 pm spread over a blended team of roughly nine implies about eleven calendar months of continuous coordination, hence eleven person-months at one coordinating head.

The range is wide downward and upward for reasons kept out of TOTAL: a live v1 as reference (A3) could cut the parser, portal and NOC lines sharply, while the unordered-store orchestrator is the classic place a 2007-era team loses a quarter to correctness under burst.

```
TOTAL: 112 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 165 person-months, same convention
TEAM x DURATION: 9 people over 12 calendar months (6 over 18 fits the same total)
DECLARATION:
  contains  - leave/holidays/sickness OUT (hours counted are hours worked on the task);
              within-day overheads (meetings, coordination, review, scrum ceremonies) IN;
              roles counted: analysts/architects, developers, QA, PM - the whole blended team,
              including the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing itself;
              development of the first version; post-launch operation and support; hardware,
              data-center and PoP rack procurement; Lustre and DBMS administration;
              the third-party OCR library and the printer driver as products
```
