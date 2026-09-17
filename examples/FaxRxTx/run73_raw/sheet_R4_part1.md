# Replies of round 3 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 3, verbatim

## VOTES

- **Load and burst / capacity rig (P-3 5, P-4 5, P-7 6, P-8 4, P-9 5; also P-5, P-10)** — **REJECT.** Rule 1: each line is built, tested *and stabilised*, and tuning the cluster to A6's mandatory throughput is that stabilisation. The text asks for exactly one testing deliverable, the §6 comparison against the old system; a generator built to prove a property is the testing of the orchestrator and cluster lines, not a separate thing the text asks for. I note six panelists now carry it, so it will likely survive — my own orchestrator line explicitly carries that tuning, and I would not take both.
- **Render worker frame / host as its own line (P-4 5, P-5 4, P-7 4)** — **KEEP.** §3.2/§4/A4: a printer-driver harness with process isolation and crash recovery is built once and amortised across formats; it is not inside the per-format work.
- **Comparison harness and integration tests on the real stream (P-4 8)** — **KEEP.** §6 names it and Rule 1 names it as the exemplar of testing that is itself a deliverable.
- **Rollout to production traffic, cutover, decommission readiness (P-4 4)** — **KEEP.** A2 puts taking prod traffic and v1 decommission inside Done; that is work, not friction.
- **Integration with the old system and coexistence through the transition (P-5 5, P-10 5)** — **KEEP.** §6 names it in so many words; separable from the harness and from cutover.
- **Rx path in the data centre (P-6 8, P-10 7)** — **KEEP.** §2.2–§2.4 is intake, per-user configuration, page-wise assembly and dispatch; a section with no line against it was the omission, as both authors say.
- **Cluster runtime: job distribution across ~16–20 nodes (P-8 5)** — **KEEP.** §4/§5 work, admissible provided the same distribution is not also priced inside that table's orchestrator; in P-8's table it is not.
- **PoP transport and integration with existing PoP software / reused routing (P-9 4; P-10's handoff line)** — **KEEP.** A4 excludes *developing* the PoP software and the router, not integrating with them; §2.2 and §3.2 are transport between Miami and 10–20 PoPs that someone must build.
- **REJECT (not contested): P-2's "TOTAL (sum)" row inside the table** — an arithmetic total is not a thing built and cites no section; Rule 2 admits only work as rows.
- *(Not a line, but flagged:)* P-6's declaration credits ~0.8 pm of on-task work per calendar person-month, which puts leave back inside the unit A9 defines as 168 hours worked.

**What moved me this round.** P-3, P-4, P-8 and P-9 each argued against my portal from the text rather than from position: §4 says only "the users' website", and A3's live v1 removes requirements discovery for exactly that surface — 11→9. P-2's reading of A4 on rendering (driver reused, so a format is print-check-fix) trims formats 12→11. P-5's double-counting point settles the orchestrator: I carry burst tuning inside it and therefore no rig, so 26→24, level with P-2, P-6 and P-10. Smaller convergences on Tx, NOC, the harness, coexistence and rollout, each where I sat above every stated argument. I reject, again, P-3's and P-8's round-1 pricing of the substrate as a queue wrapper — though both have since moved to 18–20 on that very ground.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), at the blended team's width | §6, A1, A3 | 10 |
| Render worker framework: job intake, process isolation, printer-driver harness, crash recovery | §3.2, §4, A4 | 5 |
| Per-format render integration and stabilisation, 8–10 formats | §3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion on the third-party library | §2.3, §2.4, A4 | 5 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax state, resume, no MQ — including its tuning to the nominal and burst rates | §4, A5, A6 | 24 |
| Cluster management tool: node/queue-length control, job distribution over ~16–20 nodes | §4, §5, A6 | 6 |
| Storage and data layer: Lustre integration, DB schema, inter-component API | §4, A4 | 8 |
| Rx pipeline: TIFF intake from PoPs, per-user configuration, page-wise TIFF or PDF assembly, email send | §2.1–§2.4 | 7 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | §3.1–§3.2, §6 | 6 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 8 |
| User portal | §4, §6 | 9 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 3 |
| Integration with the old system and coexistence for the transition | §6, A4 | 6 |
| Integration tests on the real stream + comparison harness against the old system | §6, A2 | 9 |
| Rollout to production traffic, cutover, v1 decommission readiness | A2 | 4 |
| Project management and coordination — one line | Rule 3, A3, A9 | 14 |

```
TOTAL: 135 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 hours worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion is
              outside the run per A9); within-day overheads (meetings, coordination,
              code review, standups) IN, inside each line; roles counted:
              architect/analyst, developers, QA, PM (PM as the single Rule 3 line);
              the immersion/architecture phase IN; load and burst tuning to A6 IN,
              inside the orchestrator and cluster lines rather than as a separate line
  excluded  - PoP software and Brooktrout send/receive, and the least-cost routing
              program, as products (integration with them sits inside the Rx/Tx lines);
              billing itself; development of the first version; post-launch operation
              and support; hardware, rack and data-center procurement; the OCR library,
              printer driver, Lustre and the DBMS as products (integration only);
              REQUIREMENTS.md, a different task; conversion of this total into a
              committed calendar plan
```

The PM line is derived, not a percentage: 121 pm of work lines at roughly eight to nine people implies ~14 calendar months, so one full-time PM/scrum lead across the span is 14 pm. TOTAL is the plain sum of the sixteen lines.

====================================================================================================
## P-2 — reply of round 3, verbatim

## VOTES

- **KEEP — Render-worker host/frame separated from per-format renderers** (P-4, P-5, P-7; S3.2/S4/A4). Process isolation, crash recovery and the driver harness are a build; A7 prices formats, not the host.
- **KEEP — Comparison harness and integration tests on the real stream** (P-4; §6, A2). §6 names it among what the team did, and Rule 1 names this exact case as admissible.
- **KEEP — Rollout to production traffic, cutover, decommission readiness** (P-4; A2). A2 puts taking prod traffic and decommissionability inside Done; it is work, not friction.
- **KEEP — Integration with the old system and coexistence through the transition** (P-5, P-10; §6, A4). §6 states it in its own words; separable from cutover, so not paid twice.
- **KEEP — Rx path in the data centre** (P-6, P-10; S2.2–S2.4). A whole section with no line against it is an omission under Rule 2.
- **KEEP — Cluster runtime, job distribution across the 16–20 nodes** (P-8; §4, §5, §6). §6 buys "the cluster itself" alongside the delivery mechanism; admissible where the orchestrator line does not already contain dispatch — P-8's does not.
- **KEEP — PoP transport and integration with the existing PoP software and reused routing** (P-9; §2.2, §3.2, §3.3, A4). A4 excludes building those, not integrating with them; the Miami↔10–20 PoP transport is a build. Caution to the panel: inadmissible for anyone whose Rx/Tx lines already span intake from and handoff to the PoPs.
- **REJECT — Load / burst / capacity rig** (P-3, P-4, P-7, P-8, P-9, and standing in P-5, P-10; §5, A6). A6 states burst resilience as a *property* of the design; the text asks for one harness, the §6 comparison against v1, and Rule 1 puts the rest of the testing inside the line it tests. Capacity tuning of the orchestrator and the cluster is those lines' own stabilisation. I expect this item to survive the vote; it does not enter my table, and my orchestrator and cluster lines carry that work explicitly rather than silently.
- **REJECT (not contested): my own "TOTAL (sum)" row inside the round-2 table** — P-9 is right, a total is not a line. Removed.
- **REJECT (not contested): a PM line derived as a percentage of the build — including my own round-2 line** — P-5 and P-8 are right that a rate on top of the lines is the uplift Rule 1 bars wearing Rule 3's hat. The line stays; its basis is now one coordinating head across the span the work lines imply.

**What else moved me.** P-8's absorption argument: a large orchestrator line quietly swallows dispatch and storage that stand as separate lines, and I am now itemizing cluster runtime separately — 24→22. P-4, P-8 and P-9 on the portal: A3's live v1 removes requirements discovery for that surface — 10→9, not to their 8, because §7 makes it the customer-facing surface of a Fortune-1000 service carrying the per-user configuration Rx depends on. Render host 6→5 toward the four panelists who converge at 4–5. Following my own KEEP votes, I split the merged transition line into coexistence (5) and cutover (4), split the cluster pair into runtime (5) and management tool (3), and lifted PoP transport (4) out of Rx and Tx, which drop to 5 each — the last two regroupings are total-neutral and only stop the table hiding what it pays for.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), at the blended team's width | S6, A1, A3 | 10 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resumption, failure survival | S4, A5, A6 | 22 |
| Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | S4, S5, S6 | 5 |
| Cluster management tool: queue lengths, node state | S4 | 3 |
| Render-worker host: job intake, printer-driver (Black Ice-class) harness, process isolation and crash recovery | S3.2, S4, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilized | S3.4, A7 | 10 |
| OCR workers, TIFF→PDF conversion on a third-party library | S2.3, S6, A4 | 5 |
| Rx path in the data centre: per-user configuration, page-wise TIFF or PDF assembly, outbound mail | S2.3, S2.4 | 5 |
| Tx path: inbound-email parser, recipient number extraction, archive packaging | S3.1, S6 | 5 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4 |
| Data layer: Lustre archive and working files, DB schema, the inter-component API | S4, A4 | 8 |
| NOC — state of the remote PoPs, the cluster and the queues | S4, S6 | 8 |
| User portal: per-user fax configuration, history | S4, S6 | 9 |
| CDR and billing-data capture (billing engine excluded) | S6, A1 | 3 |
| Integration tests on the real message stream with the comparison harness against the old system | S6, A2 | 9 |
| Integration with the old system and coexistence through the transition | S6, A4 | 5 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Project management and coordination — one line: 120 pm of work lines at a blended width of about eight implies ~15 calendar months, and one PM/scrum lead full-time across that span | Rule 3, A3, A8 | 15 |

ADDED
- Cluster runtime: job distribution across ~16–20 Windows nodes on the private network | S4, S5, S6 | 5
- PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4
- Integration with the old system and coexistence through the transition | S6, A4 | 5
- Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4

(The first two are lifted out of my round-2 cluster and Rx/Tx lines and are total-neutral against them; the last two are the two halves of my round-2 combined transition line, 8 pm becoming 5 + 4.)

```
TOTAL: 135 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task; absence stretches the calendar, not the effort, and the calendar
              conversion is outside the run per A9); within-day overheads (meetings,
              coordination, code review, standups, demos) IN, inside the lines; roles
              counted: developers, architect/analyst, QA and PM - the whole blended team
              of S6/A3, including the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive, and the least-cost routing program,
              as products (integration with them is in); the billing engine (only
              CDR/billing-data capture is in); development of the first version; post-launch
              operation and support; hardware, rack and data-center procurement; the OCR
              engine, printer driver, Lustre and the DBMS as products; a separate load/burst
              rig as its own line - that work sits inside the orchestrator and cluster lines
              under Rule 1; REQUIREMENTS.md, which describes a different system; end-user
              training and documentation beyond what a line needs
```

**Report for the coordinator.** P-2, round 3. Votes: KEEP on seven distinct contested items (render host; comparison harness; rollout/cutover; coexistence with v1; Rx path; cluster runtime; PoP transport), REJECT on one — the load/burst rig, which seven of ten panels now carry, so it will almost certainly survive my objection. Two uncontested rejections: totals rows are not lines (mine had one, removed), and a PM line derived as a percentage of the build is Rule 1's uplift under Rule 3's hat (mine was, rebased on one coordinating head over the implied span). Total 154 → 136 → 135; range narrowed to 100–195. Four ADDED lines, of which two are total-neutral decompositions of existing lines and two are the split of my transition line; no new scope. Round-2 panel spread was 125–159 against round-1's 92–175, so the panel has converged sharply, with the remaining disagreement concentrated in two places: the orchestrator (18–26) and whether the burst rig is a line or is testing already inside one.

====================================================================================================
## P-3 — reply of round 3, verbatim

VOTES

- **Load and burst rig (P-3 5, P-4 5, P-7 6, P-8 4, P-9 5; also P-5, P-10): REJECT.** It is my own addition and I vote it down. Rule 1's parenthetical admits "a comparison harness *the text asks for*" — S6 asks for exactly one harness, the comparison against the old system. S5 and A6 give the scale and make burst resilience a required property, but they do not ask for a rig as a deliverable; proving a property is the testing of the orchestrator and cluster lines, which Rule 1 has already put inside them. P-2's and P-6's reading is tighter than mine was. In round 2 I said that if the panel held it duplicated per-line stabilisation the honest correction was to delete it and not redistribute; I am doing that.
- **Render-worker frame/host (P-4 5, P-5 4, P-7 4): KEEP.** Job intake, process isolation, crash recovery and the printer-driver harness (S3.2, S4, A4) are built once and amortised; A7 prices formats, not the host.
- **Comparison harness and real-stream integration tests as a line (P-4 8): KEEP.** Named in S6, put inside Done by A2, and expressly admitted by Rule 1.
- **Rollout to production, cutover, decommission readiness (P-4 4): KEEP.** A2's Done has three clauses; "takes production traffic" and "v1 can be decommissioned" are work, not friction.
- **Integration with the old system and coexistence through the transition (P-5 5, P-10 5): KEEP.** S6 names it in its own words, and it is not the same event as cutover.
- **Rx path in the data centre (P-6 8, P-10 7): KEEP.** S2.2–S2.4 is a section of the text that must have a line against it. Admissible only where it is not already carried as sub-lines — I hold my own two.
- **Cluster runtime, job distribution over ~16–20 nodes (P-8 5): KEEP.** Distinct from a tool that reports queue lengths; S4 with S5.
- **PoP transport and integration with the existing PoP software and routing (P-9 4): KEEP.** S2.2 and S3.2 move TIFF between Miami and 10–20 sites, and A4 excludes *developing* those, not integrating with them. It persuaded me to split my own bundled line.
- **REJECT (not contested): P-2's "TOTAL (sum)" row inside the table** — arithmetic, not a thing built; Rule 3 puts the sum below the table.
- **Not a rejection, but a basis objection I accept (P-5, P-8):** a PM line derived as a percentage of the build is the uplift Rule 1 bars in different clothes. Rule 3 asks for a basis, so I have rederived mine as one PM-equivalent across the span the lines imply.

**What else moved me.** The orchestrator: all nine other panellists now sit at 20–26, and the stated basis is uniformly A5 removing every ready mechanism, not risk — P-4 and P-9 both named my 18 as inconsistent with my own citation, and P-8 conceded the same point moving 14→20. I go to 20. Smaller moves on argument: the NOC to 8 (P-8/P-9: the operations surface spans 10–20 remote WAN nodes as well as the cluster, S4), the data layer to 7 (P-1/P-10: S4 says the components communicated through the DB and an API, so schema and contracts are ours even though A4 gives Lustre and the DBMS), the harness to 9 (A2 makes parity with v1 across all formats part of Done). I rejected P-1's 26 and P-10's earlier 30 for the reason I gave in round 2, and P-1's and P-10's portal at 11–12, which S4's "the users' website" does not carry.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), at the blended team's width | S6, A1, A3 | 11 |
| Render-worker frame: job intake, process isolation, node-local execution, printer-driver harness, crash recovery | S3.2, S3.4, S4, A4 | 5 |
| Format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library + TIFF→PDF conversion path | S2.3, A4 | 5 |
| Rx output assembly: per-page TIFF vs PDF per user configuration | S2.3 | 3 |
| Outbound email delivery of received faxes at the nominal rate | S2.4, A6 | 3 |
| Inbound-email parser (Tx): address and number extraction, attachments, archive packaging | S3.1, S3.2, S6 | 5 |
| Fax orchestrator: watchdogs + tokens, unordered status store, per-fax state, resume after failure | S4, A5, A6 | 20 |
| Cluster runtime: job distribution over ~16–20 Windows nodes, private network | S4, S5, A6 | 6 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Storage and data layer: Lustre working files and archive, DB schema, inter-component API | S4, A4 | 7 |
| PoP transport and integration with the existing PoP software and the reused least-cost routing | S2.2, S3.2, S3.3, A4 | 4 |
| Coexistence with the old system for the duration of the transition | S6, A2, A4 | 3 |
| NOC: state of the remote PoPs, the cluster and the queues | S4, S6 | 8 |
| User portal (per-user fax configuration, history) | S4, S6 | 8 |
| CDR and billing-data capture and persistence (billing itself excluded) | S6, A1 | 3 |
| Integration tests on the real stream + comparison harness against the old system | S6, A1, A2 | 9 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Project management and coordination (one line, Rule 3): one PM/scrum-lead equivalent full time across the ~15 calendar months that 117 pm of delivery lines at a team of this width imply | A3, A8, A9 | 15 |

My round-2 load-and-burst rig is gone and nothing was moved into another line to replace it, as I undertook. The total is almost unchanged at 132 against 131, but its composition is not: −5 on the rejected rig, +2 on the orchestrator, +1 each on the NOC, the data layer, the harness and the derived PM line, and my one bundled PoP/coexistence line split neutrally into 4 + 3.

```
TOTAL: 132 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion is
              outside the run per A9); within-day overheads (meetings, coordination,
              code review, scrum ceremonies) IN, inside each line; roles counted:
              developers, architect, QA, PM (PM as the single Rule 3 line, derived from
              headcount x implied duration, not as a percentage); the immersion and
              technology-selection phase IN; capacity and burst tuning IN, inside the
              orchestrator and cluster lines rather than as a line of its own
  excluded  - PoP software (Brooktrout reception/sending) and the least-cost routing
              program as products, integration with them only; billing proper; development
              of the first version; post-launch operation and support; hardware procurement
              and data-center/rack work; the OCR library, printer driver, Lustre and the
              DBMS as products (integration only); the REQUIREMENTS.md draft task, which
              describes a different system
```

Quarantine unchanged: repository status, commit subjects, memory notes and environment listings reached me outside the task text and informed no figure. The two sheets were read once each and no other tool was used.

====================================================================================================
## P-4 — reply of round 3, verbatim

**Round 3 — P-4.** Two sheets read once each; nothing else. Quarantine unchanged: the session material outside the task text (git status, commit subjects, memory notes, environment listings) remains data and entered no figure.

VOTES

- Render-worker frame / host (P-4, P-5, P-7; also carried by P-1, P-2, P-3, P-8) — KEEP. Printer-driver harness, process isolation and crash recovery of render processes is a build (§3.2, §4, A4), and once formats are priced per format under A7 it is not inside them.
- Comparison harness and integration tests on the real stream (P-4) — KEEP. §6 asks for it by name and Rule 1 names exactly this as a line, not an uplift; all ten carry it.
- Rollout to production traffic, cutover, v1 decommission readiness (P-4) — KEEP. A2 puts taking production traffic and decommission readiness inside Done; cutover is work, not friction.
- Load and burst rig (P-3, P-4, P-7, P-8, P-9; opposed by P-1, P-2, P-6) — KEEP, trimmed. A6 makes burst survival a mandatory property and a generator plus tuning pass over 16–20 nodes is a thing built; but P-1/P-2/P-6 are partly right that per-line stabilisation already pays for some of it, so I cut mine 5 → 4 rather than redistribute.
- Integration with the old system / coexistence through the transition (P-5, P-10) — KEEP. §6 names it in so many words; it is separable from cutover, which A2 states separately.
- Rx path in the data centre (P-6, P-10) — KEEP. §2.2–§2.4 is a whole section describing per-user configuration, page-wise assembly and dispatch; a section with no line against it is an omission under Rule 2.
- Cluster runtime, job distribution across 16–20 nodes (P-8) — KEEP. §4/§5 work with a citation. In my own table it is paid inside the cluster line, which I raise rather than split.
- PoP transport and integration with existing PoP software and reused routing (P-9; P-10's handoff line) — KEEP. A4 excludes developing the PoP software and the routing, not integrating with them (§2.2, §3.2, §3.3). I do not add the line myself: my Rx (8) and Tx (7) lines are above the panel's middle precisely because they carry both ends of that transport, and adding it would double-pay.
- REJECT (not contested): P-2's "**TOTAL (sum)** | | **154/136**" row inside the table — an arithmetic result is not a thing built and cites no section; Rule 3 puts the sum in the closing block, not in the table.

**What moved me, and what I rejected.** Four small raises, all on argument. OCR 4 → 5: nine panelists price the conversion path at 5, and P-8's reason holds — it is an integration carrying throughput obligations at ~1M faxes/day, not a library call. Storage 6 → 7, on P-5: Lustre and the DBMS are given by A4, but §4 says the components talk through the DB and an API, and that schema and contract are ours. Cluster 5 → 6, on P-8/P-3: my single line has to cover dispatch runtime as well as queue-length and node control. Harness 8 → 9, on P-1/P-2/P-5/P-10: A2's bar is agreement with the old system on real traffic, which means reproducing enough of v1's behaviour to compare against it. Against that, the rig comes down 1. The PM line is a self-correction, not a concession: at 12 it contradicted its own stated basis of one coordinating head across the implied span, so it is rederived at 14.

Rejected again: P-1 at 26 and P-10 at 24 on the orchestrator, whose stated grounds remain a second design pass — Rule 2 sends that to RANGE; I hold 20 with six others. P-1's portal at 11 and P-10's at 12: §4 says "the users' website" and A3 gives a live v1 as the requirements reference. P-3's 18 orchestrator stays below what its own A5 citation implies. And I reject regression toward the panel's centre as a reason in itself: nothing above moved because of where anyone sits.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), at the blended team's width | §6, A1, A3 | 10 |
| Render worker frame: job intake, process isolation, printer-driver (Black Ice-class) integration, crash recovery | §3.2, §4, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | §3.4, A7 | 10 |
| OCR workers on a third-party library; TIFF→PDF conversion path with digitisation | §2.3, §2.4, A4 | 5 |
| Delivery-control core: watchdogs, tokens, unordered status store, resume-on-failure — the fax orchestrator | §4, A5, A6 | 20 |
| Cluster runtime and management tool: dispatch over ~16–20 nodes on the private network, queue lengths, node state | §4, §5, A6 | 6 |
| Rx path in the data centre: TIFF intake from the PoPs, per-user configuration, page-wise TIFF or PDF assembly, email dispatch | §2.2–§2.4, A6 | 8 |
| Tx path: inbound-email parser, number extraction, TIFF archive packaging, handoff to the existing routing/PoP | §3.1–§3.3, §6, A4 | 7 |
| Storage and data layer: Lustre archive and working files, DB schema, the inter-component API | §4, A4 | 7 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 8 |
| User portal | §4, §6 | 8 |
| CDR and billing-data capture (billing itself excluded) | §6, A1 | 3 |
| Integration with the old system and coexistence through the transition | §6, A4 | 6 |
| Comparison harness and integration tests on the real message stream against the old system | §6, A2 | 9 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Load and burst rig to ~30/s nominal and ~300/s peak across 16–20 nodes, and tuning to it | §5, A6 | 4 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at full time across the ~15 calendar months the 120 pm of work lines imply at the staffing below, less the planning-phase coordination already inside the immersion line | §6 process, A3, A8 | 14 |

TOTAL: 134 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 190 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours worked on the task; absence
              stretches the calendar, not the effort, and the calendar conversion sits
              outside the run); within-day overheads (meetings, coordination, code review,
              scrum ceremonies, defect triage) IN, inside each line; roles counted:
              developers, architects/analysts, QA and PM — the blended team of A3/A9,
              with the immersion and technology-selection phase IN
  excluded  - PoP software (Brooktrout reception/sending) and the least-cost routing
              program as products, only integration with them is in; billing itself;
              development of the first version; post-launch operation and support;
              hardware/rack procurement and data-centre build-out; the OCR engine, printer
              driver, Lustre and the DBMS as products (integration only); end-user training
              and documentation beyond what a line needs; the REQUIREMENTS.md draft, which
              describes a different system

====================================================================================================
## P-5 — reply of round 3, verbatim

VOTES

- **KEEP — Load / burst / capacity rig (P-3, P-4, P-7, P-8, P-9; also mine and P-10's).** A6 makes burst survival and per-fax delivery control mandatory properties across 16–20 nodes and 10–20 PoPs; a traffic generator and the tuning pass over the whole cluster is a thing built, cited to S5/A6. P-1, P-2 and P-6 are right that per-block stabilisation sits inside its own line — which is why the rig should be priced small, and I cut mine from 6 to 5 on P-8's point that the real-stream run already exercises the path. It is not an uplift: it does not scale with any other line.
- **KEEP — Render-worker framework / host / frame (P-4, P-7, mine).** Process isolation and crash recovery of a printer-driver host on a 2007 Windows cluster is a build under S3.2/S4/A4, and A7 prices formats as integrations, not as the host they run in. Not paid for inside the per-format line.
- **KEEP — Comparison harness and integration tests on the real stream (P-4).** §6 asks for it by name and Rule 1 names this exact case as a line.
- **KEEP — Rollout / cutover / readiness to decommission v1 (P-4).** A2 puts taking production traffic and decommission readiness inside Done; that is work with a citation, not friction.
- **KEEP — Integration with the old system and coexistence through the transition (mine, P-10).** §6 states it as the team's only relation to v1; distinct from cutover, which is the switch itself.
- **KEEP — Rx path in the data centre (P-6, P-10).** S2 is a whole section describing intake, per-user configuration, assembly and send. A section with no line against it is an omission.
- **KEEP — Cluster runtime: job distribution over ~16–20 nodes (P-8).** S4 and S5 name the cluster and the private network; dispatch across it is built. Caveat binding on me as much as anyone: whoever prices distribution inside the orchestrator must not also take this line. I asserted last round that mine was inside the core and never priced it, so I now carry it explicitly at 4 and hold the core at 20.
- **KEEP — PoP transport and integration with existing PoP software and the reused routing (P-9; P-10's handoff line).** A4 excludes developing the PoP software and routing, not integrating with them, and §2.2/§3.2 describe the transfer both ways. Caveat: it is inadmissible for anyone whose Rx and Tx lines already carry intake from and handoff to the PoPs. Mine do, so I do not take it.
- **REJECT (not contested): P-2's "TOTAL (sum)" row inside the table** — an arithmetic result is not a thing built and cites nothing; it belongs in the closing block.
- **REJECT (not contested): the basis of the PM lines derived as a flat percentage of the build (P-2 ~11%, P-3 ~12%, P-6 ~10%, P-9 ~12%, P-10 ~10%).** The line is allowed by Rule 3, but Rule 3 asks for the basis it is derived from, and a percentage of the other lines is exactly the proportional uplift Rule 1 forbids, relabelled. Mine stays one coordinating head across the duration the lines imply.

**What moved me this round.** P-8 and P-3 on cluster runtime: I had claimed distribution inside the core without pricing it, which left my orchestrator-plus-cluster block the lowest on the panel (23 against 25–32). P-8 and P-9 on the NOC as the operations surface over 10–20 WAN-remote PoPs, not a viewer on locally instrumented state — my 6 was the panel's floor. P-2, P-4 and P-8 on the render host at 5 rather than 4. Downward: P-8's overlap argument trims my harness to 9 and my rig to 5. I again reject P-1's and P-10's 24–26 orchestrator where the stated basis is a second design pass — that is RANGE, per Rule 2 — and P-3's earlier 12–14 reading for the mirror reason.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc. studied), at the blended team's width | S6, A1, A3 | 10 |
| Render-worker host: job intake, sandboxing, printer-driver harness, crash recovery | S3.2, S4, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and the TIFF→PDF conversion path on a third-party library | S2.3, S6, A4 | 5 |
| Delivery-control core: watchdogs + tokens, unordered status store, per-fax state, resume-on-failure (no MQ) | S4, A5, A6 | 20 |
| Cluster runtime: job distribution over ~16–20 Windows nodes on the private network | S4, S5, A6 | 4 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Rx path: intake of TIFF from PoPs, per-user configuration, email assembly and sending | S2.1–S2.4 | 6 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–S3.3, S6 | 6 |
| Storage and DB layer: Lustre archive and working files, DB schema, inter-component API | S4, A4 | 8 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal | S4, S6 | 8 |
| CDR / billing data capture (billing itself out) | S6, A1 | 3 |
| Integration tests on the real stream with the old-system comparison harness | S6, A2 | 9 |
| Load and failure rig to ~30/s nominal with ~10× burst on 16–20 nodes, and tuning to it | S5, A6 | 5 |
| Integration with the old system and coexistence through the transition | S6, A4 | 5 |
| Cutover: production rollout, stabilisation to v1 decommission readiness | A2 | 4 |
| Project management and coordination (one line, Rule 3) | S6, A8, Rule 3 | 13 |

**Reasoning (≈190 words).** Every line is the blended team's whole effort on that block, designed through stabilised, with nothing added on top. The three moves up are corrections of things I asserted but had not priced — cluster dispatch, the render host, the WAN-wide operations surface — and the two moves down come from a real overlap between the comparison run and the load rig. The delivery-control core holds at 20: A5 removes every ready mechanism and A6 makes per-fax control mandatory, but the distribution work that partly justified a larger figure now stands as its own line, so raising it too would double-count. The PM line is derived, not rated: 118 pm of work lines across a blended team of about nine implies roughly thirteen calendar months of continuous coordination, hence thirteen person-months at one coordinating head. The range carries what I believe and the table may not: the token store is the classic 2007-era block that takes two attempts, the remembered format list may be short, while a live v1 as requirements reference could compress the portal, NOC and parser together.

```
TOTAL: 131 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 195 person-months, same convention
TEAM x DURATION: 9 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task; absence
              stretches the calendar, not the effort, and A9 puts the calendar conversion
              outside the run); within-day overheads (meetings, coordination, review, scrum
              ceremonies) IN, inside each line; roles counted: analysts/architects,
              developers, QA, PM (PM as the single Rule 3 line); the immersion and
              technology-selection phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the first
              version; post-launch operation and support; hardware, data-center and PoP rack
              procurement and build-out; Lustre, the DBMS, the OCR engine and the printer
              driver as products (integration only); the REQUIREMENTS.md draft, which
              describes a different system; conversion of this total into a committed
              calendar plan
```
