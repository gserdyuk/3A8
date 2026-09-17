# Replies of round 2 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 2, verbatim

Round 2. Quarantine still stands: the session preamble (git status, commit subjects, memory index, environment and skill listings) played no part in any number. The two sheets contained only the ten replies, as stated.

**What moved me.** One thing, and it is a real defect in my round-1 table: I had no line for the Rx path itself. S2 describes intake of TIFF from the PoPs, per-user configuration, assembly of the email page-by-page or as PDF, and the send — and my only citation of S2 was the OCR line. P-2 and P-7 each carry that path as its own line, and P-1, P-4, P-5, P-8 and P-9 do too; under Rule 2 a whole section of the text with no line against it is an omission, not a judgement. I add it at 8 pm. The second, smaller move: P-3 and P-8 split rendering into a shared worker host plus per-format integrations, which shows how much the host amortises across formats; my 16 was the panel's top figure, so I trim to 14 while keeping A7's per-format cost. I also trim the portal to 10, toward the weight seven panelists give it.

**What I read and rejected.** P-5 and P-10 add a load-and-burst rig as its own line. The text asks for one harness — the comparison against the old system (S6) — and Rule 1 puts everything else's testing inside its line; load work on the orchestrator and cluster belongs to those lines, so a rig line would be a testing uplift wearing a line's clothes. I also reject P-3's 12 pm orchestrator: A5 removes every ready mechanism and A6 makes per-fax delivery control mandatory at ~30/s with ~300/s bursts, which is not twelve person-months of 2007 C#. Equally I do not follow P-1 and P-10 to 30; I hold 24. P-10's separate PoP-handoff line is now covered by my Rx and Tx lines.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives) | S6, A1, A3 | 10 |
| Rendering workers: printer-driver host plus 8–10 formats, each integrated and stabilised | S3.4, A7, A4 | 14 |
| OCR workers on a third-party library, TIFF→searchable PDF | S2.3, A4 | 5 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, resume-on-failure, per-fax control | S4, A5, A6 | 24 |
| Cluster management tool: dispatch across ~16–20 nodes, queue lengths, node lifecycle | S4, A6 | 8 |
| Component integration layer: DB schema and the inter-component API, Lustre archive and working files | S4, A4 | 9 |
| Rx path in the data centre: TIFF intake from the PoPs, per-user configuration, page-wise TIFF or PDF email assembly and sending | S2.1–S2.4 | 8 |
| NOC: state of PoPs, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 10 |
| Inbound-email parser and Tx intake: number extraction, attachment handling, hand-off to render and to the existing routing | S3.1–3.2, S6, A4 | 8 |
| CDR and billing-data capture (billing excluded) | S6, A1 | 3 |
| Coexistence with v1 during transition and cutover to production traffic | S6, A2 | 8 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A2 | 9 |
| Project management and coordination (one line, Rule 3: ~10% of the 126 pm of work lines) | A3, A8 | 13 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Rx path in the data centre: TIFF intake from the PoPs, per-user configuration, page-wise TIFF or PDF email assembly and sending | S2.1–S2.4 | 8 |

(No other line is new; the rendering and portal lines were present in round 1 and only changed in size.)

```
TOTAL: 139 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 205 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (they stretch the calendar, not the effort;
              the 8 x 21 above already allows ~0.8 pm of on-task work per person-month
              of calendar); within-day overheads IN (standups, coordination, code review,
              defect triage are inside every line); roles counted: developers, architect,
              QA and PM - the blended team of A3
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR capture is in); development of v1; post-launch
              operation and support; procurement and physical build-out of the cluster,
              racks and PoP sites; the OCR library, printer driver, Lustre and the DBMS
              as products (integration only); a separate load/burst rig as its own line
              (that work sits inside the orchestrator and cluster lines, per Rule 1);
              REQUIREMENTS.md, which describes a different task
```

====================================================================================================
## P-7 — reply of round 2, verbatim

Read both sheets. Revised — I moved up, but less than the panel's top half.

**What moved me.** Two arguments, both citable rather than atmospheric. P-5 (echoed by P-10) carries a separate load-and-burst rig line against A6/S5: A6 makes burst resilience a mandatory property, and proving ~30/s nominal with ~300/s peak across 16–20 nodes and 10–20 PoPs is itself a build, not a property of the orchestrator line. I had silently folded it in and under-priced it. P-1, P-2 and P-6 separate a render-worker framework from the per-format work; A7 prices each format as its own integration, which means the shared host was hidden inside my per-format number. I also accept the panel's weight on the orchestrator (P-2, P-4, P-5, P-6, P-9 all at 20–24 against my 18) — the argument is from A5 removing every ready mechanism, not from risk — and small corrections on portal and CDR, where I sat below every panelist.

**What I read and rejected.** P-1 and P-10 at 30 pm for the orchestrator, near a fifth of the build: their own text justifies it by "two attempts" and a second design pass under burst, which is a belief about risk and belongs in RANGE, never in TOTAL (Rule 2). I widened my high end instead. I reject P-3's and P-8's 12–14 pm orchestrator for the mirror-image reason: it prices the substrate as a queue wrapper, which A5 forbids. I hold immersion at 12 against the panel median of 10: S6 says 1–2 months and A3 says the whole blended team, so 1.5 months at team width is the literal reading. I rejected P-10's separate PoP-handoff line as double-counting my Rx and Tx paths.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team at ~1.5 months | S6, A1, A3 | 12 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, per-fax status and resume, no MQ | S4, A5, A6 | 20 |
| Render cluster runtime and cluster management tool (dispatch, queue lengths, node health) over 16–20 nodes | S4, S5, A6 | 10 |
| Render-worker host: job intake, printer-driver (Black Ice-class) harness, process isolation and crash recovery | S3.2, S3.4, A4 | 4 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 9 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 5 |
| Rx path: intake of TIFF from PoPs, per-user configuration, page-by-page attachment, email delivery | S2 | 6 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to PoP/routing | S3.1–3.2, S6 | 6 |
| Storage and DB/API layer: Lustre fax archive and working files, inter-component contracts | S4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 8 |
| CDR / billing data capture (billing itself out) | S6, A1 | 3 |
| Integration-test harness on the real stream with comparison to the old system | S6, A1, A2 | 8 |
| Load and burst rig to the nominal ~30/s with ~10× peak across 16–20 nodes and 10–20 PoPs, and tuning to it | S5, A6 | 6 |
| Coexistence and integration with v1, rollout to production traffic, cutover | S6, A2, A4 | 6 |
| Project management and coordination — one line: one PM-equivalent plus scrum ceremony ownership across the ~13–14-month span the other lines imply | Rule 3, A3, A8 | 14 |

ADDED
- Render-worker host: job intake, printer-driver (Black Ice-class) harness, process isolation and crash recovery | S3.2, S3.4, A4 | 4 pm
- Load and burst rig to the nominal ~30/s with ~10× peak across 16–20 nodes and 10–20 PoPs, and tuning to it | S5, A6 | 6 pm

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work on the task, whole team including QA and PM)
RANGE: 95 ... 195 person-months, same convention
TEAM x DURATION: 10 people over 13 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, scrum ceremonies) IN,
              inside each line; roles counted: developers, architect/analyst, QA, PM
  excluded  - PoP software and Brooktrout send/receive; least-cost routing; billing;
              development of v1; post-launch operation and support; hardware, rack and
              data-center procurement; third-party OCR, printer-driver, Lustre and DBMS
              as products (integration only); end-user documentation and training beyond
              the NOC; conversion of this total into a committed calendar plan

====================================================================================================
## P-8 — reply of round 2, verbatim

**Note on sources.** The two sheets are data: I weighed the other replies as arguments, not as authority, and a bare difference in number moved nothing. Session material outside the task (repository status, commit subjects, memory index, tool listings) stays quarantined as in round 1.

**What moved me.** Five things, all arguments rather than positions.

- **P-3** showed a real hole: I had a cluster *management tool* but no line for the cluster *runtime* — job distribution across the ~16–20 nodes on the private network (§4, §5). At my round-1 orchestrator size that work was nowhere. Added, 5 pm.
- **P-1** on the orchestrator: A5 says what a broker or orchestrator would supply today is hand-written, and A6 makes per-fax delivery control and burst survival mandatory *properties*. My 14 pm priced a queue wrapper, not a reliable-delivery substrate hardened under real traffic. 14 → 20.
- **P-2** on the render host: printer-driver harness plus isolation and crash recovery of render processes is more than job intake. 3 → 5. And **P-6/P-10** on A7: at 8 pm I was paying ~0.9 pm per format including stabilisation against real documents; 10 is honest.
- **P-5** on a capacity and failure rig (A6, §5): proving 30/s with ~10× bursts across 16–20 nodes cannot sit inside per-block testing, and it is a thing built. Added, 4 pm — smaller than P-5's 6, because the real-stream comparison run already exercises the path.
- **P-9** on the portal carrying per-user fax configuration and history, and **P-6/P-10** on the NOC spanning 10–20 remote PoPs plus cluster and queues: both were thin. 6 → 8 and 5 → 7. The Lustre archive at ~1M faxes/day plus the inter-component API (§4) likewise, 5 → 7. OCR is an integration with throughput obligations, 3 → 5.

**Read and rejected.** P-1's and P-10's 30-pm orchestrator: right direction, wrong magnitude — at that size it silently absorbs the cluster dispatch and storage work that I carry as separate lines and that A4 credits as given technologies; taking both would double count. P-1's 14-pm portal: §4 says only "the users' website" — nothing in the text supports a product of that weight. P-2's and P-6's PM line derived as ~10% of the build: Rule 3 asks for a basis, and a percentage of the lines is the uplift Rule 1 bars, wearing a different hat; I keep headcount × implied duration. P-4's single 12-pm line merging integration, coexistence, harness and rollout: admissible, but it hides the one piece §6 actually names as a deliverable. P-6's declaration crediting 0.8 pm of work per calendar person-month: that puts leave back inside the unit A9 defines as hours worked.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, discussions, architecture and technology selection (DHT etc.) | §6, A1, A3 | 10 |
| Render-worker host: printer-driver harness, job intake, process isolation and crash recovery | §3.2, §3.4, §4, A4 | 5 |
| Format renderers, 8–10 formats, each integrated and stabilised against real documents | §3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion on a third-party library | §2.3, §2.4, A4 | 5 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, per-fax status, resume, failure survival | §4, A5, A6 | 20 |
| Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | §4, §5, A6 | 5 |
| Cluster management tool: queue lengths, node state | §4 | 3 |
| Storage and DB layer plus the inter-component API (Lustre archive and working files, DBMS) | §4, A4 | 7 |
| Tx path: inbound-email parser, number extraction, TIFF archive packaging, handoff to the existing routing/PoP | §3.1, §3.2, §6, A4 | 5 |
| Rx path in the data centre: TIFF intake from the PoPs, per-user configuration, page-wise TIFF or PDF assembly, email dispatch | §2.2, §2.3, §2.4 | 5 |
| NOC: state of the remote PoPs, the cluster and the queues | §4, §6 | 7 |
| User portal: per-user fax configuration, history | §4, §6 | 8 |
| CDR and billing-data capture (billing itself excluded) | §6, A1 | 2 |
| Integration with the old system and coexistence through the transition | §6, A4 | 5 |
| Integration-test harness on the real message stream, comparing results to the old system | §6, A2 | 8 |
| Capacity and failure rig to the nominal ~30/s with ~10× burst over 16–20 nodes, and tuning to it | §5, A6 | 4 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A1, A2 | 4 |
| Project management and coordination — 1 FTE PM/scrum lead across the ~14-month delivery the lines above imply | §6, A3, A8, Rule 3 | 14 |

ADDED
- Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | §4, §5, A6 | 5
- Capacity and failure rig to the nominal ~30/s with ~10× burst over 16–20 nodes, and tuning to it | §5, A6 | 4

(Two round-1 lines were broadened rather than added: the Rx line now carries intake of TIFF from the PoPs into the data centre, §2.2, and the Tx line now carries archive packaging and handoff, §3.2. Both stay single lines.)

TOTAL: 127 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 190 person-months, same convention
TEAM x DURATION: 9 people over 14 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours worked on the task, not
              elapsed payroll; absence stretches the calendar, not the effort); within-day
              overheads IN (standups, design discussion, code review, defect triage sit
              inside each line); roles counted: architects, developers, QA, and PM as the
              single line under Rule 3, plus the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself; development of the first version; post-launch operation and
              support; hardware, rack and data-center procurement; third-party OCR,
              printer-driver, Lustre and DBMS licensing or development (integration only);
              REQUIREMENTS.md, which describes a different task; conversion of this total
              into a committed calendar plan

====================================================================================================
## P-9 — reply of round 2, verbatim

**What moved me.** Three arguments, all of them about work I had left unpriced rather than about risk.

- **P-5 and P-10** both carry a load-and-burst rig with capacity tuning to ~30/s nominal and ~300/s peak across 16–20 nodes, cited to §5/A6. My round-1 orchestrator line asserted that throughput but priced no rig to demonstrate it. That is a deliverable that cites the text, so under Rule 2 it is admissible as a line. Added, 5 pm.
- **P-10**'s handoff line (§2.2, §3.2, §3.3, A4): the TIFF archive transport between Miami and 10–20 PoPs, and integration with the existing PoP software and the reused routing. A4 excludes developing those, not integrating with them. My Rx and Tx lines covered only the data-centre and email ends. Added, 4 pm.
- **P-7 and P-10** on immersion: §6/A3 put the whole blended team in the 1–2 month phase, so A9 arithmetic gives ~10 pm, not 8. Raised. On the same reading of scope width I raised the NOC (it is the operations surface over remote WAN nodes plus the cluster, per P-1/P-6) and the cluster management tool by one.

**Read and rejected.** P-1's and P-10's 30 pm orchestrator: the stated basis is that the token store may need a second attempt — that is a belief about risk, which Rule 2 sends to RANGE, not into a line. I hold 20. P-1's PM at 18 and P-2's at 15 follow from their larger bodies, not from a different basis. P-2 puts a TOTAL row inside the table, which is not a line. I also reject the low bodies of P-3 (96) and P-8 (92): renderers at 8 pm for the whole format set and OCR at 3 pm contradict A7's explicit refusal to treat formats as a free extension. And I reject P-1's and P-6's portal at 12–14 — A3's live v1 removes requirements discovery for exactly this surface, so I hold 8.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 10 |
| Render workers: host process + 8–10 formats via printer driver, each integrated and stabilised | S3.2, S3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, S2.4, A4 | 5 |
| Cluster orchestrator: watchdogs + tokens, unordered status store, resume-on-failure, delivery control per fax | S4, A5, A6 | 20 |
| Cluster management tool (queue lengths, node/job control, dispatch over ~16–20 nodes) | S4, S5 | 5 |
| NOC: state of remote PoPs, cluster, queues | S4, S6 | 8 |
| User portal (per-user configuration, fax history) | S4, S6 | 8 |
| Inbound-email parser and Tx submission path (number extraction, attachments, archive assembly) | S3.1, S3.2, S6 | 5 |
| Rx delivery path: per-user config, page-by-page TIFF or PDF attachment, outbound mail | S2.3, S2.4 | 5 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4 |
| Storage and DB integration plus the inter-component API (Lustre, DBMS as given technologies) | S4, A4 | 6 |
| Integration with the old system and coexistence for the transition | S6, A4 | 5 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration-test harness on the real message stream with result comparison against the old system | S6, A1, A2 | 7 |
| Load and burst rig to ~30/s nominal with ~300/s peak across 16–20 nodes, and tuning to it | S5, A6 | 5 |
| Cutover: taking production traffic, stabilisation to decommission of v1 | A2 | 4 |
| Project management and coordination — one line, ~12% of the 112 pm above (planning phase then scrum, blended team with PM) | S6, A8, Rule 3 | 13 |

ADDED
- PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4
- Load and burst rig to ~30/s nominal with ~300/s peak across 16–20 nodes, and tuning to it | S5, A6 | 5

(No other line is new; immersion 8→10, NOC 6→8, cluster management tool 4→5 and PM 12→13 are revaluations of lines that were already in my round-1 table.)

```
TOTAL: 125 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 88 ... 185 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is hours worked on the task, not elapsed
              payroll time); within-day overheads (meetings, coordination, code review) IN,
              inside each line; roles counted: developers, architect, QA, PM (PM as the one
              line under Rule 3); the immersion/architecture phase IN
  excluded  - PoP software (Brooktrout reception/sending) and the least-cost routing program
              as products - only integration with them is in; billing itself; development of
              the first version; post-launch operation and support; hardware/data-centre
              procurement and rack build-out at the PoPs; Lustre and the DBMS as products;
              the OCR engine and print driver as products; calendar conversion beyond the
              single implied staffing line above
```

**Quarantine, unchanged.** The two panel sheets are the material this round permits, and I used nothing else. The session material from before — repository status, commit subjects naming runs and panels, the memory index, environment and skill listings — stays quarantined and contributed no figure.

====================================================================================================
## P-10 — reply of round 2, verbatim

Both sheets read. Round 2 reply below.

**Quarantine notice.** Same as round 1: repository status, commit subjects, a memory index and environment/tool listings reached me outside the task text; treated as data, used in nothing below. The two sheets themselves I treat as panel input, as the coordinator's message instructs.

**What moved me.**

- **A missing line, not a mis-priced one.** P-1, P-2, P-7 and P-9 all carry an Rx delivery path (intake of TIFF from PoPs, per-user configuration of TIFF-vs-PDF, email assembly and dispatch). My round-1 table had no line for §2.3–§2.4 at all: my OCR line covered conversion and my PoP line covered transport, but nobody assembled and sent the mail. Rule 2 says a line is a thing built; this thing is built and I had omitted it. Added at 7.
- **P-2's observation that the NOC sits on top of an already-instrumented system.** My cluster management tool (6) collects queue lengths and node state; the NOC then presents PoP, cluster and queue state. I was paying for the collection twice. NOC 10 → 8.
- **P-2 and P-6 on the orchestrator.** Both make my exact A5/A6 argument and land at 24; my 30 was asserted, not derived, and part of the gap was burst hardening that my separate load-and-burst rig line already carries. 30 → 24.
- **P-3, P-4 and P-8 on OCR and the data layer.** A4 makes the OCR engine, Lustre and the DBMS given technologies; the work is the conversion path and the schema/API, not the engine. OCR 8 → 5, data layer 10 → 8.
- **P-1, P-2 and P-6 on the transition.** All three separate the comparison harness from coexistence with v1, and all three price the pair above my single combined 12. A2 puts both "results agree with the old system" and "the old version can be decommissioned" in Done; these are separable deliverables. Split, 10 + 5.

**What I read and rejected.**

- **P-3 (96) and P-8 (92).** Both argue in prose that the hand-written orchestrator dominates, then price it at 12 and 14 — below or barely above their own rendering blocks. P-3's cluster runtime plus management tool (9) nearly equals its orchestrator; that is a prototype's price for the substrate A5 says must replace a broker and A6 says must survive failure at every fax. I do not follow their totals down.
- **P-4's single 12-pm line** merging old-system integration, coexistence, the comparison harness, the real-stream run and rollout. Five deliverables of A2 in one cell hides rather than decomposes.
- **P-6's declaration**, which folds a ~0.8 on-task factor into the 8 × 20 staffing arithmetic. A9 fixes a person-month as 168 hours worked; leave belongs to the calendar conversion, which A9 puts outside the run. My declaration keeps them apart.
- **The panel majority's omission of a load and burst rig.** Only P-5 and I have one. A6 states that burst resilience and delivery control of every fax are mandatory properties, not options; demonstrating ~300/s across 16–20 nodes is a thing built and measured, so it stays as a line at 8.
- **Regression toward the panel median as such.** My total stays near the top because of two lines most others lack (the burst rig, an explicit rollout/decommission line), not because of inflated per-line figures; I have re-priced five lines downward on argument and none upward without one.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | §6, A1, A3 | 12 |
| Render worker host + printer-driver (Black Ice-class) integration | §3.2, §6, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | §3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion path on the third-party library | §2.3, §2.4, A4 | 5 |
| Fax orchestrator: watchdogs + token store, status of every fax, resume after failure (MQ excluded) | §4, A5, A6 | 24 |
| Cluster management tool: queue lengths, node state, control | §4 | 6 |
| Rx delivery path: intake from PoPs, per-user configuration, page-wise TIFF or PDF assembly, outbound mail | §2.2–§2.4 | 7 |
| NOC: state of PoPs, cluster and queues, over the cluster tool's instrumentation | §4, §6 | 8 |
| User portal | §4, §6 | 12 |
| Inbound-email parser: parse mail, extract fax number, take attachments | §3.1, §6 | 6 |
| Handoff to/from PoPs: TIFF archive transfer, integration with existing PoP software and existing least-cost routing | §2.2, §3.2, §3.3, A4 | 7 |
| Data layer: Lustre fax archive and working files, DB schema, inter-component API | §4, A4 | 8 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 4 |
| Integration tests on the real stream with the comparison harness against the old system | §6, A1, A2 | 10 |
| Coexistence with v1 through the transition (integration with the old system while both run) | §6, A2, A4 | 5 |
| Load and burst rig, capacity tuning to ~30/s nominal with ~300/s peak across 16–20 nodes, 10–20 PoPs | §5, A6 | 8 |
| Production rollout, cutover, decommissioning of v1 | A2 | 6 |
| Project management and coordination (one line, Rule 3; ~10 % of the 145 pm of delivery lines) | §6, A8, A9 | 14 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Rx delivery path: intake from PoPs, per-user configuration, page-wise TIFF or PDF assembly, outbound mail | §2.2–§2.4 | 7 |
| Coexistence with v1 through the transition (integration with the old system while both run) | §6, A2, A4 | 5 |

Both are new lines rather than re-prices: the first fills a gap my round-1 table had between conversion and transport; the second was split out of my round-1 combined test-and-coexistence line, whose remainder is now 10.

TOTAL: 159 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 225 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion is outside
              the run per A9); within-day overheads (meetings, coordination, code review,
              scrum ceremonies) IN, inside each line; roles counted: developers, architect,
              QA, PM (PM as the single Rule 3 line); the immersion phase IN
  excluded  - PoP software and Brooktrout send/receive; least-cost routing; billing itself;
              development of the first version; post-launch operation and support; hardware,
              rack and data-center procurement; Lustre, the DBMS, the OCR engine and the
              printer driver as products (integration only); REQUIREMENTS.md, a different task

====================================================================================================
## CONTESTED ADDITIONS — every "ADDED" block of round 2, copied verbatim under its author's label

### from P-1

ADDED: none

### from P-2

ADDED: none

### from P-3

ADDED

| line | source in the text | person-months |
|---|---|---|
| Load and burst rig to ~30/s nominal and ~300/s peak across the cluster, and tuning to it | S5, A6 | 5 |

That is the only line not present in my round-1 table; every other change is a re-sizing of a line I already had. I claim it as work, not as testing uplift: A6 makes burst resilience and failure survival mandatory properties of the design, and a traffic generator plus the tuning pass over 16–20 nodes and 10–20 PoPs is a thing built, distinct from the testing already inside each line under Rule 1. If the panel holds that it duplicates per-line stabilisation, the honest correction is to delete it and leave the total at 126, not to redistribute it.

### from P-4

ADDED
- Render worker frame: job intake, process isolation, printer-driver (Black Ice-class) integration, crash recovery | §3.2, §4, A4 | 5
- Comparison harness and integration tests on the real message stream against the old system | §6, A2 | 8
- Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4
- Load and burst rig to ~30/s nominal and ~300/s peak across 16–20 nodes, and tuning to it | §5, A6 | 5

(The first three are separations of two round-1 lines, not fresh scope: my round-1 rendering line held the frame, and my round-1 transition line held the harness, the tests and the rollout. The burst rig is genuinely new scope in my table, taken from P-5.)

### from P-5

ADDED
- Render-worker framework: job intake, sandboxing, printer-driver harness, crash recovery | S3.2, S4, A4 | 4
- Integration with the old system and coexistence through the transition | S6, A4 | 5

(The per-format renderer line is not new in substance: it is my round-1 rendering line with the framework taken out of it, and it kept its 10. The cutover line is the same line as round 1, narrowed to rollout and decommission readiness now that coexistence stands separately.)

### from P-6

ADDED

| line | source in the text | person-months |
|---|---|---|
| Rx path in the data centre: TIFF intake from the PoPs, per-user configuration, page-wise TIFF or PDF email assembly and sending | S2.1–S2.4 | 8 |

(No other line is new; the rendering and portal lines were present in round 1 and only changed in size.)

### from P-7

ADDED
- Render-worker host: job intake, printer-driver (Black Ice-class) harness, process isolation and crash recovery | S3.2, S3.4, A4 | 4 pm
- Load and burst rig to the nominal ~30/s with ~10× peak across 16–20 nodes and 10–20 PoPs, and tuning to it | S5, A6 | 6 pm

### from P-8

ADDED
- Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | §4, §5, A6 | 5
- Capacity and failure rig to the nominal ~30/s with ~10× burst over 16–20 nodes, and tuning to it | §5, A6 | 4

(Two round-1 lines were broadened rather than added: the Rx line now carries intake of TIFF from the PoPs into the data centre, §2.2, and the Tx line now carries archive packaging and handoff, §3.2. Both stay single lines.)

### from P-9

ADDED
- PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4
- Load and burst rig to ~30/s nominal with ~300/s peak across 16–20 nodes, and tuning to it | S5, A6 | 5

(No other line is new; immersion 8→10, NOC 6→8, cluster management tool 4→5 and PM 12→13 are revaluations of lines that were already in my round-1 table.)

### from P-10

ADDED

| line | source in the text | person-months |
|---|---|---|
| Rx delivery path: intake from PoPs, per-user configuration, page-wise TIFF or PDF assembly, outbound mail | §2.2–§2.4 | 7 |
| Coexistence with v1 through the transition (integration with the old system while both run) | §6, A2, A4 | 5 |

Both are new lines rather than re-prices: the first fills a gap my round-1 table had between conversion and transport; the second was split out of my round-1 combined test-and-coexistence line, whose remainder is now 10.
