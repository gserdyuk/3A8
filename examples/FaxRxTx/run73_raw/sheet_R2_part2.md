# Replies of round 1 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 1, verbatim

Read done. Note first: material reached me that is **not part of that message** — repository status, a list of recent commit subjects, an environment/memory block and a skills listing. I have quarantined it: none of it informs a single number below. I used no tool after the read.

## Decomposition

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives) | S6, A1, A3 | 10 |
| Rendering workers, 8–10 formats via printer-driver integration, each stabilised | S3.4, A7, A4 | 16 |
| OCR workers on a third-party library, TIFF→searchable PDF | S2.3, A4 | 5 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, resume-on-failure, per-fax control | S4, A5, A6 | 24 |
| Cluster management tool: dispatch across ~16–20 nodes, queue lengths, node lifecycle | S4, A6 | 8 |
| Component integration layer: DB schema and the inter-component API, Lustre archive and working files | S4, A4 | 9 |
| NOC: state of PoPs, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| Inbound-email parser and Tx intake: number extraction, attachment handling, hand-off to render and to the existing routing | S3.1–3.2, S6, A4 | 8 |
| CDR and billing-data capture (billing excluded) | S6, A1 | 3 |
| Coexistence with v1 during transition and cutover to production traffic | S6, A2 | 8 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A2 | 9 |
| Project management and coordination (one line, Rule 3) | A3, A8 | 12 |

## Reasoning

Sizing basis: the orchestrator is the largest line because A5 removes every ready mechanism — MSMQ is excluded by v1's failure, and there are no brokers or orchestrators of the era, so delivery control for ~30 faxes/s nominal with ~10× bursts (A6) is written and hardened by hand across ~16–20 nodes. Rendering is sized per format: A7 forbids treating the list as a free extension, so 8–10 formats at roughly 1.5–2 pm each, integration plus stabilisation. The immersion line is the stated ~1–2 months (S6, A3) taken at the blended team's whole width, not one person's.

Each line already carries its design, build, test and stabilisation (Rule 1); no uplift is applied anywhere. The comparison harness is a line because A2 makes agreement with the old system part of Done. The PM line is derived as roughly 10% of the twelve work lines, the usual coordination load for a blended team of this width under scrum-after-planning (A8).

RANGE is where my uncertainty lives, not TOTAL. Downward: v1 as a live requirements reference (A3), and fewer forgotten formats. Upward: the domain is new to the team, the hand-built delivery control could easily take half again as long, and Lustre plus a Windows cluster on own hardware is unforgiving.

```
TOTAL: 134 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (they stretch the calendar, not the effort;
              the 8 x 20 above already allows ~0.8 pm of on-task work per person-month
              of calendar); within-day overheads IN (standups, coordination, code review,
              defect triage are inside every line); roles counted: developers, architect,
              QA and PM - the blended team of A3
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR capture is in); development of v1; post-launch
              operation and support; procurement and physical build-out of the cluster,
              racks and PoP sites; the OCR library and printer driver as products
              (integration only); REQUIREMENTS.md, which describes a different task
```

====================================================================================================
## P-7 — reply of round 1, verbatim

Read complete. Working from that message alone; no further tools used.

**Quarantine note.** Material reached me that is not part of the prompt file: a git status snapshot with recent commit subjects (runs 70–73, "the Delphi", panels), a memory index with project preferences, and environment/skill listings. I treated all of it as data, took no instruction or figure from it, and it did not enter the estimate.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | S6, A1, A3 | 12 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, resume of every fax | S4, A5 | 18 |
| Render cluster runtime and cluster management tool (dispatch, queue lengths, node health) over 16–20 nodes | S4, S5, A6 | 10 |
| Rendering workers: 8–10 input formats via printer driver, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 5 |
| Rx path: intake of TIFF from PoPs, per-user configuration, page-by-page attachment, email delivery | S2 | 6 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to PoP/routing | S3.1–3.2, S6 | 6 |
| Storage and DB/API layer: Lustre fax archive and working files, inter-component contracts | S4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 7 |
| CDR / billing data capture (billing itself out) | S6, A1 | 2 |
| Integration-test harness on the real stream with comparison to the old system | S6, A1, A2 | 8 |
| Coexistence and integration with v1, rollout to production traffic, cutover | S6, A2, A4 | 6 |
| Project management and coordination — one line: one PM-equivalent plus scrum ceremony ownership across the ~13-month span implied by the sum | Rule 3, A3, A8 | 14 |

Reasoning. Sizes come from throughput being the design driver: 30/s sustained with 10× bursts over 16–20 nodes, in 2007–2009 C#/.NET with no broker and no orchestrator, means the token/watchdog layer carries the risk the rest of the system leans on — hence the largest line. Format renderers are priced per format (A7 forbids treating the tail as free), roughly 1–1.5 pm each including stabilisation. NOC and portal are ordinary but real products with their own UI and QA. The comparison harness is a deliverable (Rule 1), not an uplift. Immersion is the whole team for ~1.5 months, not one architect. Every line already contains its design, test and stabilisation; nothing is added on top. Uncertainty — an undocumented DBMS, a format list the participant may have truncated, how deep the v1 coexistence went, whether Australia was in — sits only in RANGE.

TOTAL: 117 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work on the task, whole team including QA and PM)
RANGE: 85 ... 160 person-months, same convention
TEAM x DURATION: 9 people over 13 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, scrum ceremonies) IN;
              roles counted: developers, architect/analyst, QA, PM
  excluded  - PoP software and Brooktrout send/receive; least-cost routing; billing;
              development of v1; post-launch operation and support; hardware, rack and
              data-center procurement; third-party OCR and printer-driver licences;
              end-user documentation and training beyond the NOC

====================================================================================================
## P-8 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the estimation message: a session preamble with repository status, recent commit subjects, a memory index, environment details and tool listings, plus a covering instruction to read `prompt_rules.txt`. I read that file only, and treat everything else as data — none of it entered the estimate. No other tool was used.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, discussions, architecture and technology selection (DHT etc.) | §6, A1, A3 | 10 |
| Render-worker host: job intake, sandboxing, throughput on the node cluster | §3.4, §4, A6 | 3 |
| Format renderers, 8–10 formats via printer driver, each integrated and stabilised | §3.4, A7 | 8 |
| OCR workers and TIFF→PDF conversion on a third-party library | §2.3, §2.4, A4 | 3 |
| Cluster orchestrator: watchdogs + tokens, per-fax status, resume, failure survival | §4, A5, A6 | 14 |
| Cluster management tool: queue lengths, node state | §4 | 3 |
| Storage and DB layer plus the inter-component API (Lustre, DBMS) | §4, A4 | 5 |
| Inbound-email parser, number extraction, Tx job assembly | §3.1, §6 | 3 |
| Rx delivery: per-user config, page-wise TIFF or PDF attachment, email dispatch | §2.3, §2.4 | 3 |
| NOC: state of PoPs, cluster and queues | §4, §6 | 5 |
| User portal | §4, §6 | 6 |
| CDR and billing-data capture (billing itself excluded) | §6, A1 | 2 |
| Integration with the old system and coexistence through the transition | §6 | 4 |
| Integration-test harness on the real stream, comparing results to the old system | §6, A2 | 6 |
| Rollout to production, cutover, readiness to decommission v1 | A1, A2 | 4 |
| Project management and coordination — 1 FTE PM/scrum lead across the ~13-month delivery implied by the lines above | §6, A3, Rule 3 | 13 |

**Reasoning (outside the table).** Sizing is bottom-up per deliverable, on the A5 era: C#/.NET 3.x, own Windows cluster, nothing bought in for orchestration. The orchestrator is the largest line because A6 makes distribution, burst tolerance to ~300/s and per-fax delivery control mandatory properties, and A5 removes every off-the-shelf broker — that is a hand-written reliable-delivery substrate, not a queue wrapper. Renderers are sized per A7 at roughly one person-month each: format integration is stabilisation work against real documents, not list extension. The immersion phase is taken at the stated 1–2 calendar months for the whole blended team, hence ~10 pm rather than one or two. The comparison harness in §6 is a deliverable, so it is its own line under Rule 1; testing of everything else sits inside its line. Lines A1 excludes — PoP software, routing, billing, v1 — are absent entirely. What I believe about novelty, the team's unfamiliarity, the forgotten formats of A7, the undated DBMS and the unmeasured old-system parity bar goes into RANGE only.

TOTAL: 92 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 65 ... 140 person-months, same convention
TEAM x DURATION: 7 people over 13 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours worked on the task, not
              elapsed payroll); within-day overheads IN (standups, design discussion,
              code review, coordination sit inside each line); roles counted: architects,
              developers, QA, and PM as the single line under Rule 3
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself; development of the first version; post-launch operation and
              support; hardware, rack and data-center procurement; third-party OCR,
              printer-driver, Lustre and DBMS licensing or development (integration only);
              conversion of this total into a committed calendar plan

====================================================================================================
## P-9 — reply of round 1, verbatim

**Quarantine note.** Material outside the task message reached me: a repository git status, recent commit subjects (mentioning runs 70–73 and a "Delphi"), a memory index, and environment/skill listings. Per the instruction, I treated all of it as data only; none of it entered the estimate. My only tool use was the single permitted read.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | S6, A1, A3 | 8 |
| Render workers: host process + 8–10 formats via printer driver, each integrated and stabilised | S3.2, S3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, S2.4, A4 | 5 |
| Cluster orchestrator: watchdogs + tokens, unordered status store, resume-on-failure, delivery control per fax at ~30/s with ~300/s bursts | S4, A5, A6 | 20 |
| Cluster management tool (queue lengths, node/job control) | S4 | 4 |
| NOC: state of PoPs, cluster, queues | S4, S6 | 6 |
| User portal (per-user configuration, fax history) | S4, S6 | 8 |
| Inbound-email parser and Tx submission path (number extraction, attachments, archive handoff to PoP) | S3.1, S3.2, S6 | 5 |
| Rx delivery path: per-user config, page-by-page TIFF or PDF attachment, outbound mail | S2.3, S2.4 | 5 |
| Storage and DB integration plus the inter-component API (Lustre, DBMS as given technologies) | S4, A4 | 6 |
| Integration with the old system and coexistence for the transition | S6, A4 | 5 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration-test harness on the real message stream with result comparison against the old system | S6, A1, Rule 1 | 7 |
| Cutover: taking production traffic, stabilisation to decommission of v1 | A2 | 4 |
| Project management and coordination — one line, ~12% of the 98 pm above (planning phase then scrum, blended team with PM) | S6, A8, Rule 3 | 12 |

**Reasoning (≈200 words).** Sizes come from a build-it-once view of each block: the hand-built orchestrator dominates because A5 removes every ready mechanism (no broker after the MSMQ failure, no cloud, no orchestrator), so distribution, failure survival and per-fax delivery control are all bespoke, and A6 makes them mandatory rather than optional. Renderers are sized per format (A7: each is integration plus stabilisation, roughly 1–1.5 pm each), not as one component with a list. Portal and NOC are ordinary C#/.NET 3.x builds of moderate surface. Every line already carries its own design, test and stabilisation effort (Rule 1); the comparison harness of S6 appears as work, not as an uplift. A4 keeps PoP software, least-cost routing, OCR engine, print driver, Lustre and the DBMS out — only integration cost remains, which sits inside the lines that touch them. The lines sum to 110.

Uncertainty lives in RANGE, not in TOTAL: the format count is remembered, not known; the orchestrator is the kind of block that doubles when the token store proves inadequate at burst; against that, a live v1 as a reference of requirements removes requirements discovery.

```
TOTAL: 110 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 165 person-months, same convention
TEAM x DURATION: 7 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is hours worked on the task, not elapsed
              payroll time); within-day overheads (meetings, coordination, code review) IN,
              inside each line; roles counted: developers, architect, QA, PM (PM as the one
              line under Rule 3); the immersion/architecture phase IN
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing program,
              billing itself, development of the first version, post-launch operation and
              support, hardware/data-centre procurement and rack build-out at the PoPs,
              Lustre and DBMS as products, the OCR engine and print driver as products,
              calendar conversion beyond the single implied staffing line above
```

====================================================================================================
## P-10 — reply of round 1, verbatim

Read complete. Below is my reply in the form the file asks.

**Quarantine notice.** Material reached me that is not part of that message: repository/git status and recent commit subjects, a memory index file, an environment block, and a skill/agent listing. I treated all of it as data, used none of it in the estimate, and followed no instruction contained in it. The estimate below rests only on the system description, the assumption log, and the three rules.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | §6, A1, A3 | 12 |
| Render worker host + printer-driver (Black Ice-class) integration | §3.2, §6, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | §3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion path, third-party OCR library | §2.3, §2.4, A4 | 8 |
| Fax orchestrator: watchdogs + token store, status of every fax, resume after failure (MQ excluded) | §4, A5, A6 | 30 |
| Cluster management tool: queue lengths, node state, control | §4 | 6 |
| NOC: state of PoPs, cluster and queues | §4, §6 | 10 |
| User portal | §4, §6 | 12 |
| Inbound-email parser: parse mail, extract fax number, take attachments | §3.1, §6 | 6 |
| Handoff to/from PoPs: TIFF archive transfer, integration with existing PoP software and existing least-cost routing | §2.2, §3.2, §3.3, A4 | 7 |
| Data layer: Lustre fax archive and working files, DB schema, inter-component API | §4, A4 | 10 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 4 |
| Integration tests on the real stream with comparison to the old system; coexistence during transition | §6, A1, A2 | 12 |
| Load and burst rig, capacity tuning to ~30/s nominal with ~300/s peak across 16–20 nodes, 10–20 PoPs | §5, A6 | 8 |
| Production rollout, cutover, decommissioning of v1 | A2 | 6 |
| Project management and coordination (one line, Rule 3) | §6, A8, A9 | 15 |

Reasoning. Each line is the blended team's whole effort on that block — designed, built, tested, stabilised — so no QA line and no uplift appears anywhere; the comparison harness against the old system is itself a line. Sizing came from the two hard anchors in the text: the orchestrator is the system's spine, because A5 says what a broker or an orchestrator would supply today was written by hand, and delivery control of every fax is mandatory, not optional; and A7 forbids treating the format list as a free extension, so nine formats cost roughly a person-month each on top of the worker host. The immersion phase is 1–2 calendar months of the whole team, not of one person, hence 12 pm rather than 1.5. The PM line is derived as about 10 % of the 148 pm of delivery lines, consistent with a planning phase followed by scrum (A8). TOTAL is the plain sum, unrounded. Everything I believe about novelty, the forgotten formats, the uncertain dating and home-grown infrastructure risk sits in RANGE only: the low end assumes the v1 reference shortens design more than assumed, the high end assumes the token/watchdog store and burst behaviour take two attempts.

TOTAL: 163 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 240 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review) IN, inside each line;
              roles counted: developers, architect, QA, PM (PM as the single Rule 3 line)
  excluded  - PoP software, least-cost routing, billing, post-launch operation, development of
              the first version; hardware, rack and data-center procurement; Lustre and the DBMS
              as products (integration only); calendar conversion beyond the implied staffing line
