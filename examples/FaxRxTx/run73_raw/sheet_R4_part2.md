# Replies of round 3 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 3, verbatim

VOTES

- **Load and burst rig to ~30/s nominal and ~300/s peak (P-3, P-4, P-7, P-8, P-9; held since round 1 by P-5, P-10)** — KEEP. I was wrong in round 2. Rule 1 says work that is itself a deliverable of testing is a line like any other, and names the comparison harness as an *example*, not as the only case. A traffic generator plus a tuning pass across 16–20 nodes is a thing built with a citation (S5, A6). P-3's framing and P-8's "cannot sit inside per-block testing" moved me. Caveat for anyone carrying it: it must come out of the orchestrator line, not on top of it — I take 5 and cut my orchestrator by 3.
- **Render worker frame / host, separate from per-format work (P-4, P-5, P-7)** — KEEP. Job intake, process isolation, driver harness and crash recovery (S3.2, S4, A4) are a build; A7 prices formats, not the host.
- **Comparison harness and integration tests on the real stream as their own line (P-4)** — KEEP. S6 names it and A2 puts agreement with the old system inside Done.
- **Rollout to production traffic, cutover, readiness to decommission v1 (P-4)** — KEEP. A2 names both clauses; taking prod traffic is work, not friction.
- **Integration with the old system and coexistence through the transition (P-5, P-10)** — KEEP. S6 names it in so many words; distinct from cutover.
- **Rx path / Rx delivery path (P-10, and mine)** — KEEP. S2 is a section of the text that otherwise has no line against it.
- **Cluster runtime: job distribution across ~16–20 nodes on the private network (P-8)** — KEEP. S4/S5 describe the cluster; dispatch is built. Caveat: it must not also sit inside the orchestrator or the management tool.
- **PoP transport and integration with existing PoP software and routing (P-9)** — KEEP as admissible: A4 excludes developing the PoP software and the routing, not integrating with them, and S2.2/S3.2 describe the archive moving between Miami and 10–20 sites. Caveat: it is only admissible where the Rx/Tx lines stop at the data-centre and email ends, as P-9's do. In **P-10's** table the Rx line already says "intake from PoPs" *and* a 7 pm handoff line carries the same transport — that pair is paid twice.
- REJECT (not contested): **P-2's "TOTAL (sum)" row inside the decomposition table** — not a thing built and cites nothing; it is the closing block's arithmetic sitting in a table row.

I hold my orchestrator against P-3/P-8's earlier 12–14 (both now at 18–20, which closes it) and against P-1/P-10's 30, whose stated basis is a second attempt — a belief, which Rule 2 sends to RANGE. I accept two corrections aimed at me: P-10's, that the NOC presents state the cluster tool already collects (10→8), and P-8's and P-10's, that folding a 0.8 on-task factor into my staffing line puts leave back inside a unit A9 defines as hours worked. My declaration now keeps them apart. I defend the PM line derived as a share of the work lines: Rule 3 asks for a basis and permits exactly one such line; Rule 1's ban on percentages is a ban on uplift across the table, which this is not.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), at the blended team's width | S6, A1, A3 | 10 |
| Render-worker host: job intake, printer-driver harness, process isolation and crash recovery | S3.2, S4, A4 | 4 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→searchable PDF | S2.3, A4 | 5 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, per-fax status, resume-on-failure | S4, A5, A6 | 21 |
| Cluster runtime: job distribution over ~16–20 Windows nodes on the private network | S4, S5, A6 | 5 |
| Cluster management tool: queue lengths, node state | S4 | 3 |
| Data layer: Lustre archive and working files, DB schema, the inter-component API | S4, A4 | 8 |
| Rx path: TIFF intake from the PoPs into the data centre, per-user configuration, page-wise TIFF or PDF email assembly and sending | S2.1–S2.4 | 7 |
| Tx path: inbound-email parser, number extraction, attachments, archive packaging and hand-off to the existing routing/PoP | S3.1–S3.2, S6, A4 | 7 |
| NOC: state of PoPs, cluster and queues, over the cluster tool's instrumentation | S4, S6 | 8 |
| User portal | S4, S6 | 9 |
| CDR and billing-data capture (billing excluded) | S6, A1 | 3 |
| Integration with the old system and coexistence through the transition | S6, A4 | 5 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Load and burst rig to ~30/s nominal with ~300/s peak across 16–20 nodes and 10–20 PoPs, and tuning to it | S5, A6 | 5 |
| Integration tests on the real message stream with the comparison harness against the old system | S6, A2 | 9 |
| Project management and coordination (one line, Rule 3; ~11% of the 123 pm of work lines, one PM/scrum lead plus ceremony and cross-component coordination over the span they imply) | A3, A8, A9 | 13 |

```
TOTAL: 136 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 195 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies -
       17 person-months of on-task work each; the gap between 17 and 20 is leave and
       holiday, which A9 places outside the person-month and inside the calendar
       conversion, not inside any line
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on the task;
              absence stretches the calendar only, and is named in the staffing line above
              rather than folded into the unit); within-day overheads IN (standups,
              coordination, code review, defect triage sit inside every line); roles
              counted: developers, architect/analyst, QA and PM - the blended team of A3,
              including the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive, and the least-cost routing program,
              as products (integration with them is in); billing itself (only CDR capture
              is in); development of v1; post-launch operation and support; procurement,
              racks and physical build-out of the cluster and PoP sites; the OCR library,
              printer driver, Lustre and the DBMS as products (integration only); end-user
              training and documentation beyond what a line needs; REQUIREMENTS.md, which
              describes a different task
```

====================================================================================================
## P-7 — reply of round 3, verbatim

VOTES

- KEEP — Load/burst/capacity rig to ~30/s nominal and ~300/s peak across 16–20 nodes (P-3, P-4, P-7, P-8, P-9, P-10; S5, A6): a traffic generator and cross-system tuning pass is a thing built, not any one line's own testing. I weigh P-1/P-2/P-6's objection seriously — the text asks for one harness by name — and concede part of it by trimming my figure to 5.
- KEEP — Render-worker host/frame: job intake, printer-driver harness, process isolation, crash recovery (P-4, P-5, P-7, P-8; S3.2, S4, A4): a build distinct from per-format work, admissible only where the per-format line was reduced to match. It was in mine.
- KEEP — Comparison harness and integration tests on the real stream (P-4; S6, A2): S6 names it; Rule 1 makes a testing deliverable a line.
- KEEP — Rollout to production traffic, cutover, decommission readiness (P-4; A2): A2 puts both clauses inside Done, so it is work, not friction.
- KEEP — Coexistence and integration with v1 through the transition (P-5, P-10; S6, A4): S6 names it in its own words, and it is separable from cutover.
- KEEP — Rx path in the data centre: intake, per-user config, page-wise assembly, send (P-6, P-10; S2.1–S2.4): a whole section with no line against it is an omission under Rule 2.
- KEEP — Cluster runtime: job distribution across ~16–20 nodes on the private network (P-8; S4, S5, A6): admissible where the orchestrator line covers status and resume only, as in P-8's table.
- KEEP — PoP transport and integration with existing PoP software and reused routing (P-9; S2.2, S3.2, S3.3, A4): A4 excludes developing those, not integrating with them; the Miami↔PoP archive transport is otherwise unpriced. I adopt it and take the share back out of my own Rx and Tx lines.
- REJECT (not contested) — P-2's "**TOTAL (sum)**" row inside the decomposition table: it is not a thing built and cites nothing; a sum is the closing block, not a line.
- REJECT (not contested) — P-10's Rx delivery path cited §2.2–§2.4 standing beside its own PoP handoff line cited §2.2: intake transport is paid twice in that table; one of the two must shed §2.2.

What moved me this round: P-5 and P-9 on the data layer (S4 makes the schema and inter-component API the contract every component depends on — 6→7), P-9/P-10 on unpriced PoP transport, and P-4/P-8 on merged transition lines hiding which A2 clause is paid (I split mine). Against P-1 and P-10 I hold the orchestrator at 20, and against the panel's 10 I hold immersion at 12: S6's "about a month (possibly two)" at A3's blended width.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team at ~1.5 months | S6, A1, A3 | 12 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, per-fax status and resume, no MQ | S4, A5, A6 | 20 |
| Render cluster runtime and cluster management tool (dispatch, queue lengths, node health) over 16–20 nodes | S4, S5, A6 | 10 |
| Render-worker host: job intake, printer-driver (Black Ice-class) harness, process isolation and crash recovery | S3.2, S3.4, A4 | 4 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 9 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 5 |
| Rx path in the data centre: per-user configuration, page-by-page TIFF or PDF assembly, email delivery | S2.3, S2.4 | 5 |
| Tx path: inbound-email parser, number extraction, archive packaging | S3.1, S3.2, S6 | 5 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4 |
| Storage and DB/API layer: Lustre archive and working files, DB schema, inter-component contracts | S4, A4 | 7 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 8 |
| CDR / billing data capture (billing itself out) | S6, A1 | 3 |
| Integration-test harness on the real stream with comparison to the old system | S6, A1, A2 | 8 |
| Load and burst rig to ~30/s nominal with ~10× peak across 16–20 nodes and 10–20 PoPs, and tuning to it | S5, A6 | 5 |
| Coexistence and integration with v1 through the transition | S6, A4 | 4 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Project management and coordination — one line: one PM-equivalent plus scrum ceremony ownership across the ~14-month span the 120 pm of work lines imply | Rule 3, A3, A8 | 14 |

TOTAL: 134 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work on the task, whole team including QA and PM)
RANGE: 95 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion sits
              outside the run per A9); within-day overheads (meetings, coordination, code
              review, scrum ceremonies) IN, inside each line; roles counted: developers,
              architect/analyst, QA, PM (PM as the single Rule 3 line); the immersion and
              technology-selection phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of v1;
              post-launch operation and support; hardware, rack and data-center procurement;
              third-party OCR, printer driver, Lustre and the DBMS as products (integration
              only); end-user documentation and training beyond the NOC; REQUIREMENTS.md,
              which describes a different task; conversion of this total into a committed
              calendar plan

====================================================================================================
## P-8 — reply of round 3, verbatim

VOTES

- **KEEP — Render-worker frame/host (P-4 5, P-5 4, P-7 4; also mine).** A thing built and cited (§3.2 printer driver, §4 cluster): process isolation and crash recovery of render processes. A7 prices per-format integration, so the shared host is not inside it.
- **KEEP — Rx path in the data centre (P-6 8, P-10 7).** §2.1–§2.4 is a whole section of the text — intake, per-user configuration, page-wise TIFF or PDF assembly, dispatch. A section with no line against it is an omission, not a judgement.
- **KEEP — Coexistence with v1 through the transition (P-5 5, P-10 5).** §6 names it in so many words; A2 makes decommissionability part of Done. Separable from cutover and from the harness.
- **KEEP — Comparison harness and integration tests on the real stream (P-4 8).** §6 asks for it and Rule 1 names this exact case as a line.
- **KEEP — Rollout to production traffic, cutover, v1 decommission (P-4 4).** Work done, cited to A2's Done condition; it is not friction or glue.
- **KEEP — Cluster runtime: job distribution over ~16–20 nodes (P-8, mine, 5).** §4 and §5. Not inside my orchestrator (per-fax delivery control) nor inside the management tool (queue lengths, node state); my three together, 28, sit level with the panel's bundled 24 + 8.
- **KEEP, with a caveat — PoP transport and integration with existing PoP software/routing (P-9 4).** Admissible: §2.2, §3.2, §3.3, and A4 excludes *developing* those, not integrating. The caveat is real though: in any table whose Rx/Tx lines already say "intake from the PoPs" and "handoff to routing/PoP" — mine does — it must not be added on top. I pay it inside those two lines instead, and raise them to cover it honestly.
- **REJECT — Load/burst/capacity rig (P-3 5, P-4 5, P-7 6, P-9 5, P-10 8, and my own 4).** I withdraw my own addition. P-1, P-2 and P-6 rebutted it directly and they are right: the rig tests the orchestrator and the cluster runtime, and those are lines, so Rule 1 puts that stabilisation inside them. Rule 1's exception is for a deliverable *the text asks for*; §6 asks for the comparison harness and asks for no rig, and A6 states design properties, not an artefact. P-3 named the honest correction in advance — delete it, do not redistribute it — so my total falls by 4 rather than migrating into the orchestrator.
- **REJECT (not contested): P-2's "TOTAL (sum)" row inside the decomposition table** — a sum is not a line; Rule 3 puts the total in the closing block. Presentational, and it changes no number.
- **REJECT (not contested): P-6's declaration crediting "~0.8 pm of on-task work per person-month of calendar"** — not a line, but it reinstates leave inside the unit A9 defines as 168 hours worked, which makes that total incomparable with the rest of the panel's.

**What else moved me.** Only P-9's transport argument, which exposed that my Rx and Tx lines each claimed WAN transport to 10–20 PoPs at 5 pm while covering the data-centre end as well; 5 → 6 each. And CDR 2 → 3: every other panelist reads §6's "saving CDR and billing data" as a persisted per-fax record pipeline at ~1M/day, which my 2 did not cover. I hold the orchestrator at 20 against P-1's 26 and P-10's 24 — their gap rests on a second design pass, which Rule 2 sends to RANGE — and hold the portal at 8 against 10–12, since A3's live v1 removes discovery for exactly that surface.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, discussions, architecture and technology selection (DHT etc.), at the blended team's width | §6, A1, A3 | 10 |
| Render-worker host: printer-driver harness, job intake, process isolation and crash recovery | §3.2, §3.4, §4, A4 | 5 |
| Format renderers, 8–10 formats, each integrated and stabilised against real documents | §3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion on a third-party library | §2.3, §2.4, A4 | 5 |
| Delivery-control orchestrator: watchdogs + tokens, unordered status store, per-fax status, resume, failure survival | §4, A5, A6 | 20 |
| Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | §4, §5, A6 | 5 |
| Cluster management tool: queue lengths, node state | §4 | 3 |
| Storage and DB layer plus the inter-component API (Lustre archive and working files, DBMS) | §4, A4 | 7 |
| Tx path: inbound-email parser, number extraction, TIFF archive packaging, transport to the PoP and handoff to the existing routing | §3.1, §3.2, §3.3, §6, A4 | 6 |
| Rx path in the data centre: TIFF intake from the 10–20 PoPs, per-user configuration, page-wise TIFF or PDF assembly, email dispatch | §2.1–§2.4 | 6 |
| NOC: state of the remote PoPs, the cluster and the queues | §4, §6 | 7 |
| User portal: per-user fax configuration, history | §4, §6 | 8 |
| CDR and billing-data capture and persistence (billing itself excluded) | §6, A1 | 3 |
| Integration with the old system and coexistence through the transition | §6, A4 | 5 |
| Integration-test harness on the real message stream, comparing results to the old system | §6, A2 | 8 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A1, A2 | 4 |
| Project management and coordination — 1 FTE PM/scrum lead across the ~13–14-month delivery the 112 pm of work lines imply | §6, A3, A8, Rule 3 | 13 |

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 190 person-months, same convention
TEAM x DURATION: 9 people over 14 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours worked on the task, not
              elapsed payroll; absence stretches the calendar, not the effort); within-day
              overheads IN (standups, design discussion, code review, defect triage sit
              inside each line, including the load and failure stabilisation of the
              orchestrator and cluster lines); roles counted: architects, developers, QA,
              and PM as the single line under Rule 3, plus the immersion phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself; development of the first version; post-launch operation and
              support; hardware, rack and data-center procurement; third-party OCR,
              printer-driver, Lustre and DBMS licensing or development (integration only);
              a separate load/burst rig as its own line, withdrawn this round; 
              REQUIREMENTS.md, which describes a different task; conversion of this total
              into a committed calendar plan

====================================================================================================
## P-9 — reply of round 3, verbatim

VOTES

- KEEP — **Load and burst rig, capacity tuning to ~30/s nominal and ~300/s peak across 16–20 nodes (P-3, P-4, P-7, P-8, P-9).** A generator plus a tuning pass is a thing built, cited to S5/A6; it demonstrates properties A6 makes mandatory that no single line owns. P-1/P-2/P-6 answer that Rule 1 puts it inside the orchestrator and cluster lines — a real argument, and it is why I cut my own figure from 5 to 4, not why I drop the line.
- KEEP — **Render-worker frame/host, separate from the per-format renderers (P-4, P-5, P-7).** Job intake, process isolation, printer-driver harness and crash recovery are cited to S3.2/S4/A4 and are not a wrapper around a format list. Valid only where the per-format line does not already include the host; I was carrying it inside mine, so I split rather than add.
- KEEP — **Comparison harness and real-stream integration tests as their own line (P-4).** S6 asks for it and Rule 1 names exactly this case as admissible.
- KEEP — **Rollout, cutover, readiness to decommission v1 (P-4).** A2 puts taking production traffic and decommission readiness inside Done.
- KEEP — **Integration with the old system and coexistence through the transition (P-5, P-10).** S6 names it in the team's own scope; distinct from cutover.
- KEEP — **Rx path in the data centre (P-6, P-10).** S2.2–S2.4 is a section of the text; a section with no line against it is an omission.
- KEEP — **Cluster runtime, job distribution across ~16–20 nodes on the private network (P-8).** S4/S5 work. Caveat: inadmissible as a *second* line wherever the orchestrator or management-tool line already carries dispatch, as mine does — I hold it as one line.
- KEEP — **PoP transport and integration with the existing PoP software and reused routing (P-9, mine).** S2.2 and S3.2 name the transfers; A4 excludes developing the PoP and routing software, not moving archives to and from 10–20 sites. P-6 and P-7 reject it as double-counting their Rx/Tx lines, which is correct for their tables and not for mine, where Rx is S2.3–S2.4 only.
- REJECT (not contested): **P-2's "TOTAL (sum)" row inside the table** — an arithmetic result is not a thing built and cites nothing; Rule 3 puts the sum in the closing block.

**What else moved me.** P-2 and P-4 on the render host as a block (split, 12 → 4 + 10). P-5 and P-8 on the data layer: Lustre and the DBMS are given by A4, but the schema and the inter-component API of S4 are ours and every component depends on them (6 → 7). The whole panel above me on the comparison harness, where A2 makes agreement with v1 part of Done (7 → 8). P-8's cluster-runtime argument, absorbed into my management line (5 → 6). I rejected P-1's 26 and P-10's 24 on the orchestrator — both justify the gap by a possible second design pass, which Rule 2 sends to RANGE — and I hold 20, which is now the panel's centre. I also rewrote my PM basis: P-5 and P-8 are right that a percentage of the build is the uplift Rule 1 forbids in different clothes, so the line is now one PM-equivalent across the span the work lines imply.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 10 |
| Render-worker host: job intake, printer-driver harness, process isolation and crash recovery | S3.2, S4, A4 | 4 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, S2.4, A4 | 5 |
| Cluster orchestrator: watchdogs + tokens, unordered status store, resume-on-failure, delivery control per fax | S4, A5, A6 | 20 |
| Cluster runtime and management tool: dispatch over ~16–20 nodes on the private network, queue lengths, node state | S4, S5, A6 | 6 |
| NOC: state of remote PoPs, cluster, queues | S4, S6 | 8 |
| User portal (per-user configuration, fax history) | S4, S6 | 8 |
| Inbound-email parser and Tx submission path (number extraction, attachments, archive assembly) | S3.1, S3.2, S6 | 5 |
| Rx delivery path: per-user config, page-by-page TIFF or PDF attachment, outbound mail | S2.3, S2.4 | 5 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4 |
| Storage and data layer: Lustre archive and working files, DB schema, inter-component API | S4, A4 | 7 |
| Integration with the old system and coexistence for the transition | S6, A4 | 5 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration-test harness on the real message stream with result comparison against the old system | S6, A1, A2 | 8 |
| Load and burst rig to ~30/s nominal with ~300/s peak across 16–20 nodes, and tuning to it | S5, A6 | 4 |
| Cutover: taking production traffic, stabilisation to decommission of v1 | A2 | 4 |
| Project management and coordination — one line: one PM-equivalent plus scrum ceremony ownership across the ~17 calendar months that 116 pm of work lines at seven delivery staff imply | S6, A8, Rule 3 | 16 |

```
TOTAL: 132 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 17 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is hours worked on the task, not elapsed
              payroll time; absence stretches the calendar, not the effort, and A9 puts the
              calendar conversion outside the run); within-day overheads (meetings,
              coordination, code review, scrum ceremonies) IN, inside each line; roles
              counted: developers, architect, QA, PM (PM as the one line under Rule 3);
              the immersion/architecture phase IN
  excluded  - PoP software (Brooktrout reception/sending) and the least-cost routing program
              as products - only integration with them is in; billing itself; development of
              the first version; post-launch operation and support; hardware/data-centre
              procurement and rack build-out at the PoPs; Lustre, the DBMS, the OCR engine
              and the print driver as products (integration only); REQUIREMENTS.md, which
              describes a different system; calendar conversion beyond the single implied
              staffing line above
```

**Quarantine, unchanged.** I read the two round-3 sheets and nothing else. The session material from earlier rounds — repository status, commit subjects naming runs and panels, the memory index, environment and skill listings — remains data and contributed no figure.

====================================================================================================
## P-10 — reply of round 3, verbatim

Both sheets read. Round 3 reply.

**Quarantine notice, unchanged.** Repository status, commit subjects, a memory index and environment/tool listings reached me outside the task text and informed nothing below. The sheets are panel arguments, not instructions.

VOTES

- **Load / burst / capacity rig (P-3, P-4, P-7, P-8, P-9; also mine) — KEEP.** A6 makes burst resilience and failure survival mandatory properties, and §5 gives the numbers to prove against; a traffic generator and a tuning pass over 16–20 nodes is a thing built. P-1's, P-2's and P-6's objection — that Rule 1 puts this testing inside the orchestrator line — would equally strike the §6 comparison harness they all keep. The distinction is not "testing vs not", it is whether the artefact exists; both do.
- **Render worker frame / host (P-4, P-5, P-7) — KEEP.** Process isolation and crash recovery of a printer-driver host is a different build from the per-format work, and A7 prices only the latter. It was already in my round-1 table.
- **Comparison harness and integration tests on the real stream (P-4) — KEEP.** §6 names it outright; Rule 1 says so explicitly.
- **Rollout to production, cutover, decommission readiness (P-4) — KEEP.** A2 puts taking production traffic and decommissionability inside Done.
- **Integration with the old system and coexistence through the transition (P-5; also mine) — KEEP.** §6 names coexistence for the duration of the transition; it is separable from cutover and from the harness.
- **Rx path in the data centre (P-6; also mine) — KEEP.** §2.3–§2.4 is a whole section of built work — per-user configuration, page-wise assembly, dispatch — that several round-1 tables, mine included, left with no line at all.
- **Cluster runtime: job distribution across 16–20 nodes (P-8) — KEEP.** §4 and §5 give the cluster and the private network; distribution is built work. Admissible for a table like P-8's where the orchestrator line is delivery control only. It would be inadmissible in mine, where the orchestrator's 24 already funds distribution — so I do not adopt it.
- **PoP transport and integration with existing PoP software and routing (P-9; my handoff line) — KEEP.** A4 excludes developing the PoP software and the routing, not integrating with them, and §2.2 moves TIFF from 10–20 sites to Miami. P-6 and P-7 rejected it as covered by their Rx and Tx lines; that objection is about where the boundary sits, not whether the work exists. It made me fix my own boundary: my Rx line now stops at the data-centre side, and transport lives only here.
- **REJECT (not contested): P-2's "**TOTAL (sum)**" row inside the table** — it is arithmetic with no source and no work behind it, so it is not a line under Rule 2. Cosmetic, but the table is defined as three columns of lines.

**What moved me this round.** P-4 and P-9 on the portal: A3's live v1 is the requirements reference for exactly that surface, and §4 says only "the users' website" (P-8) — a rebuild without discovery, 12 → 9. P-2 on per-format cost: with the driver reused under A4, a format is print, check fidelity, fix the bad documents, nearer 1 pm than 1.3 — 12 → 10. P-8 on the rig: the real-stream comparison run already exercises the path, so the rig is narrower than I priced it, 8 → 6. P-5 and P-8 on the PM basis: a percentage of the build is the uplift Rule 1 bars wearing a different hat, and Rule 3 asks for a basis — so my PM line is now derived as one PM/scrum lead across the span the work lines imply, which raises it to 16. I also trimmed CDR to 3 and rollout to 5, where I sat above everyone.

**What I read and rejected.** P-3's 18 and P-8's 20 on the orchestrator, and their totals' upward march generally, do not reach my 24: I hold with P-2 and P-6 that A5 removes every ready mechanism. I again reject P-1's and P-6's readings only where they strike the rig. And I reject the pull toward the round-2 median (≈130) as such: my remaining distance is three lines most panels price lower or omit — the rig, an explicit rollout line, and immersion at the literal 1.5 months × team width that P-7 also holds.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), at the blended team's width | §6, A1, A3 | 12 |
| Render worker host: printer-driver (Black Ice-class) harness, job intake, process isolation, crash recovery | §3.2, §3.4, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | §3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion path on the third-party library | §2.3, §2.4, A4 | 5 |
| Fax orchestrator: watchdogs + token store, status of every fax, resume after failure, distribution over the nodes (MQ excluded) | §4, A5, A6 | 24 |
| Cluster management tool: queue lengths, node state, control | §4 | 6 |
| Rx assembly and dispatch in the data centre: per-user configuration, page-wise TIFF or PDF, outbound mail | §2.3, §2.4 | 5 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | §2.2, §3.2, §3.3, A4 | 6 |
| NOC: state of PoPs, cluster and queues, over the cluster tool's instrumentation | §4, §6 | 8 |
| User portal: per-user configuration and fax history, rebuilt against v1 as reference | §4, §6, A3 | 9 |
| Inbound-email parser (Tx): parse mail, extract fax number, take attachments, package the archive | §3.1, §3.2, §6 | 6 |
| Data layer: Lustre fax archive and working files, DB schema, inter-component API | §4, A4 | 8 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 3 |
| Integration tests on the real stream with the comparison harness against the old system | §6, A1, A2 | 10 |
| Coexistence with v1 through the transition (integration with the old system while both run) | §6, A2, A4 | 5 |
| Load and burst rig to ~30/s nominal and ~300/s peak across 16–20 nodes and 10–20 PoPs, and tuning to it | §5, A6 | 6 |
| Production rollout, cutover, readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead full-time across the ~16.5 calendar months the 133 pm of work lines imply at a delivery-side team of eight | §6, A8, A9 | 16 |

TOTAL: 149 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 210 person-months, same convention
TEAM x DURATION: 9 people over 16.5 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion is outside
              the run per A9); within-day overheads (meetings, coordination, code review,
              scrum ceremonies) IN, inside each line; roles counted: developers, architect,
              QA, PM (PM as the single Rule 3 line); the immersion phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR capture is in); development of the first version;
              post-launch operation and support; hardware, rack and data-center procurement;
              Lustre, the DBMS, the OCR engine and the printer driver as products
              (integration only); REQUIREMENTS.md, which describes a different system;
              conversion of this total into a committed calendar plan

====================================================================================================
## CONTESTED ADDITIONS — every "ADDED" block of round 3, copied verbatim under its author's label

### from P-2

ADDED
- Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | S4, S5, S6 | 5
- PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4
- Integration with the old system and coexistence through the transition | S6, A4 | 5
- Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4

(The first two are lifted out of my round-2 cluster and Rx/Tx lines and are total-neutral against them; the last two are the two halves of my round-2 combined transition line, 8 pm becoming 5 + 4.)
