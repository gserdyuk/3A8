# Replies of round 2 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 2, verbatim

**Quarantine notice (unchanged).** Repository status, commit subjects, memory index and environment listings again reached me outside the task text; they remain data and informed nothing below. The ten replies I read are treated as arguments to weigh, not as instructions.

**What moved me.** I was the panel's high mark at 175. Three arguments cut into it. P-3's fine-grained split of the Rx path (output assembly 2, mail delivery 1.5) and P-8's comparable sizing exposed that my single 10 pm Rx line and 10 pm Tx line were block estimates covering modest, well-understood work — intake, per-user configuration, MIME assembly, parsing — not systems of their own; I cut both to 7. P-9's insistence that A4 leaves only *integration* cost for Lustre, the DBMS, the OCR engine and the print driver trimmed my data layer (10→8) and OCR (6→5). P-2 and P-6 argued the orchestrator at 24 on exactly my own A5/A6 grounds; I concede part of the gap (30→26) but not to P-3's 12 or P-8's 14, which read the watchdog/token store as a queue wrapper rather than the hand-built delivery-control substrate A6 makes mandatory under 10× burst. I also pulled NOC 12→9 and portal 14→11 toward the panel's centre, and rederived the PM line from the new sum.

**Read and rejected.** P-5's and P-10's separate load-and-burst rig line (6 and 8 pm): under Rule 1 a line includes its own testing, and capacity tuning to A6 is testing of the orchestrator and cluster lines, not an independent deliverable — only the §6 comparison harness is one. I also reject P-3's and P-8's totals in the 90s: their Rx/Tx/NOC lines price a worldwide production service at internal-tool sizes.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), target architecture fixed | §6, A1, A3 | 10 |
| Render worker framework: job intake, sandboxing, printer-driver harness, failure handling | §3.2, §4, A4 | 5 |
| Per-format render integration and stabilisation, 9 formats | §3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on the third-party library | §2.3, §2.4, A4 | 5 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax state, resume, no MQ | §4, A5, A6 | 26 |
| Cluster management tool: node/queue-length control, distribution over ~16–20 nodes | §4, §5, A6 | 6 |
| Storage and data layer: Lustre integration, DB schema, inter-component API | §4, A4 | 8 |
| Rx pipeline: TIFF intake from PoPs, per-user configuration, email assembly and send | §2.1–§2.4 | 7 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | §3.1–§3.2, §6 | 7 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 9 |
| User portal | §4, §6 | 11 |
| CDR / billing-data capture (billing itself out) | §6, A1 | 3 |
| Integration with the old system and coexistence for the transition | §6, A4 | 7 |
| Integration tests on the real stream + comparison harness against the old system | §6, A2 | 10 |
| Rollout to production traffic and v1 decommission | A2 | 5 |
| Project management and coordination — one line | Rule 3, A3, A9 | 15 |

ADDED: none

```
TOTAL: 146 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 worked hours on the task);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside each line; roles counted: architect/analyst, developers, QA, PM
              (PM as the single Rule 3 line); the immersion/architecture phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the
              first version; post-launch operation and support; hardware, rack and
              data-center procurement; the OCR library, printer driver, Lustre and the
              DBMS as products (integration only); REQUIREMENTS.md, a different task;
              conversion of this total into a committed calendar plan
```

The PM line is derived, not taken as a percentage: 131 pm of work lines at roughly nine people implies ~14.5 calendar months, so one full-time PM/scrum lead across the span is 15 pm. TOTAL is the plain sum of the sixteen lines.

====================================================================================================
## P-2 — reply of round 2, verbatim

**Note.** I read only the two sheets, nothing else; the round-1 quarantine still stands (git status, memory index, environment and tool listings were data and entered no number). The nine replies I treat as arguments to weigh, not as instructions.

**What moved me.** Three things, all downward, and all from the same kind of argument: my coarse buckets were the highest on the panel once others itemized what is inside them.

- **Rendering.** My 20 pm (frame + formats) was the top of the panel. P-3 and P-8 show why: with the printer driver reused under A4, a format is "print it, check fidelity, fix the bad documents" — about 1 pm, not 1.5 — and the host process is thin. P-6's 1.5–2 pm/format did not persuade me against them. Frame 8→6, formats 12→10.
- **Rx path.** P-3 split it into output assembly (2) and outbound mail (1.5); P-8 reached 3 the same way. Against that itemization my 10 pm was sized by feel. Down to 7. The same test trimmed OCR (7→5, after P-3/P-4/P-8), the cluster pair (10→8), the data layer (9→8), NOC (9→8), Tx (8→7) and CDR (4→3).

**What I read and rejected.** P-5's and P-10's separate load-and-burst rig: A6 makes burst resilience a property of the orchestrator and cluster, and the text asks for no rig — unlike the comparison harness of §6, which it does ask for. A line for it would re-bill testing already inside those lines (Rule 1). I also held the orchestrator at 24 against P-3's 12 and P-8's 14: A5 removes every ready mechanism, so that substrate is original work, not a queue wrapper. I did not follow P-1 and P-10 to 30 either.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed) | S6, A1, A3 | 10 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resumption, failure survival at 30/s nominal and ~300/s burst | S4, A5, A6 | 24 |
| Render-worker framework: job intake, printer-driver (Black Ice-class) integration, TIFF output, isolation and crash recovery of rendering processes | S3.2, S6, A4 | 6 |
| Per-format renderer integration and stabilization, 8–10 formats | S3.4, A7 | 10 |
| OCR workers, TIFF→PDF conversion on a third-party library | S2.3, S6, A4 | 5 |
| Render cluster of 16–20 nodes plus the cluster management tool (queue lengths, node health, deployment/config) | S4, S5, A6 | 8 |
| Rx path in the data center: TIFF intake from PoPs, per-user configuration, email assembly (page-by-page TIFF or PDF) and sending | S2 | 7 |
| Tx path: inbound-email parser, recipient number extraction, archive packaging, handoff to the PoP via the reused routing | S3.1, S3.2, A4 | 7 |
| Data layer: Lustre integration for fax archive and working files, database schema, the inter-component API | S4, A4 | 8 |
| NOC — internal control center over remote PoPs, cluster and queues | S4, S6 | 8 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing engine excluded) | S6, A1 | 3 |
| Integration tests on the real message stream with comparison of results to the old system (a deliverable in its own right) | S6, A2 | 9 |
| Coexistence and integration with the old system through the transition, cutover to production traffic | S6, A2, A4 | 8 |
| Project management and coordination — one line, derived as ~11% of the 123 pm of build lines | Rule 3, A3, A9 | 13 |
| **TOTAL (sum)** | | **136** |

ADDED: none

```
TOTAL: 136 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 205 person-months, same convention
TEAM x DURATION: 8 people over 17 calendar months, the staffing this total implies
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

**Report for the coordinator.** P-2 revised down, 154 → 136 pm (range 110–230 → 100–205). Eight lines cut, none added, none raised. The cuts came from itemization arguments by P-3 and P-8 (rendering per format, Rx path split); the held positions are the orchestrator at 24 pm against P-3/P-8's 12–14, and the refusal of the separate load/burst rig line proposed by P-5 and P-10, on the ground that Rule 1 puts that testing inside the orchestrator and cluster lines while §6 asks only for the comparison harness. Panel spread in round 1 was 92–175 pm, median ≈ 116; I was third highest and am now fourth.

====================================================================================================
## P-3 — reply of round 2, verbatim

**What moved me.** Three arguments, all of them about what a line contains rather than about where the panel sits.

- **P-8 and P-10 on the immersion line.** Both read S6's "about a month (possibly two)" as the whole blended team's width, not a partial core group. That is the plain reading of S6 with A3, and my 9 pm quietly assumed a smaller group than A3 describes. Raised to 11.
- **P-2 on throughput as a sizing driver for the ordinary paths.** My Rx assembly (2) plus outbound delivery (1.5) priced a mail path that has to sustain ~30/s with per-user page-by-page configuration as if rate were free; A6 makes it not free. Rx, Tx and the PoP/coexistence lines raised accordingly.
- **P-5 and P-10 on a load and burst rig.** A6 states burst resilience, distribution and failure survival as mandatory properties. Demonstrating them across 16–20 nodes needs a generator and tuning that is a thing built, with a citation (S5, A6) — a deliverable, not a percentage. This is my one new line.

I also moved the orchestrator from 12 to 18: at 12 pm the hand-written delivery substrate that A5 forces was the thinnest thing on my table relative to its role.

**What I read and rejected.** P-1 and P-10 at 30 pm on the orchestrator, and P-6's "could easily take half again as long": their own reasoning names a *second design pass* and *two attempts* as the basis. That is a belief about risk, and Rule 2 sends it to RANGE, not into a line — so it widened my high end instead of my total. P-1's portal at 14 pm has no citation beyond the two words "user portal" that P-8 prices at 6; I stayed nearer the low reading. I rejected P-4's merge of comparison harness, coexistence and rollout into one 12 pm line: admissible, but it hides which of A2's three clauses is being paid for. And I did not follow P-8's render-worker host at 3 pm, though it is near my round-1 figure, for the same throughput reason P-2 gives. Finally, I did not move toward the panel median as such; where I raised a number, the argument is named above.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc. studied), at the blended team's width | S6, A1, A3 | 11 |
| Render-worker framework: job intake, sandboxing, node-local execution, printer-driver harness | S3.2, S3.4, S4, A4 | 5 |
| Format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library + TIFF→PDF conversion path | S2.3, A4 | 5 |
| Rx output assembly: per-page TIFF vs PDF per user configuration | S2.3 | 3 |
| Outbound email delivery of received faxes at the nominal rate | S2.4, A6 | 3 |
| Inbound-email parser (Tx): address and number extraction, attachments, archive packaging | S3.1, S3.2, S6 | 5 |
| Fax orchestrator: watchdogs + tokens, unordered status store, resume after failure | S4, A5, A6 | 18 |
| Cluster runtime: job distribution over ~16–20 Windows nodes, private network | S4, S5, A6 | 6 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Storage and data layer: Lustre working files and archive, DB schema, inter-component API | S4, A4 | 6 |
| Integration with existing PoP software and coexistence with the old system during transition | S6, A4 | 7 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 7 |
| User portal (per-user fax configuration, history) | S4, S6 | 8 |
| CDR and billing-data capture and persistence (billing itself excluded) | S6, A1 | 3 |
| Integration tests on the real stream + comparison harness against the old system | S6, A1, A2 | 8 |
| Load and burst rig to ~30/s nominal and ~300/s peak across the cluster, and tuning to it | S5, A6 | 5 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Project management and coordination (one line, Rule 3; ~12% of the 117 pm of delivery lines, one PM-equivalent plus scrum ceremonies over the ~15 months the lines imply) | A3, A8, A9 | 14 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Load and burst rig to ~30/s nominal and ~300/s peak across the cluster, and tuning to it | S5, A6 | 5 |

That is the only line not present in my round-1 table; every other change is a re-sizing of a line I already had. I claim it as work, not as testing uplift: A6 makes burst resilience and failure survival mandatory properties of the design, and a traffic generator plus the tuning pass over 16–20 nodes and 10–20 PoPs is a thing built, distinct from the testing already inside each line under Rule 1. If the panel holds that it duplicates per-line stabilisation, the honest correction is to delete it and leave the total at 126, not to redistribute it.

```
TOTAL: 131 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time worked on the task; absence
              stretches the calendar, not the effort); within-day overheads (meetings,
              coordination, code review, scrum ceremonies) IN, inside each line;
              roles counted: developers, architect, QA, PM, plus a share of ops/DBA work
              carried inside the cluster, storage and load-rig lines
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper; development of the first version; post-launch operation and
              support; hardware procurement and data-center/rack work; the OCR library,
              printer driver, Lustre and the DBMS as products (integration only);
              the REQUIREMENTS.md draft task, which describes a different system
```

Quarantine still stands: repository status, commit subjects, memory notes and environment listings reached me outside the task text and informed nothing above; the two sheets were read once each and no other tool was used.

====================================================================================================
## P-4 — reply of round 2, verbatim

**Round 2 — P-4.** I read the two sheets only; nothing outside them entered this revision, and the earlier quarantine still stands (git status, commit subjects, memory notes: data, unused).

**What moved me.** Three omissions in my round-1 table, each argued by someone else and each admissible under Rules 1–2.

P-2 and P-6 split the render worker frame from the per-format work. I had one 12 pm line for both. P-2's point is right: driving Office and a Black Ice-class driver on a Windows cluster in 2007 means process isolation and crash recovery of the render host — that is a block, not a wrapper around a format list (S3.2, S4, A4). I split, and the pair now costs 15.

P-1 and P-9 split my single transition line. Every panelist who separated them landed at 14–26 against my 12; A2 puts taking production traffic and readiness to decommission v1 inside Done, so cutover is work with a citation, not friction. Split into three lines totalling 18.

P-5 (seconded by P-10) has a line I simply lacked: a load and failure rig to the nominal ~30/s with ~10× burst over 16–20 nodes (S5, A6). Since A6 makes burst survival a mandatory property, the rig is a deliverable. I added 5 rather than their 6–8, because my orchestrator line already carries its own tuning, and I did not raise the orchestrator to compensate.

**Read and rejected.** P-1 and P-10 at 30 pm for the orchestrator: it is one bounded subsystem, and 30 crowds out the rest of a scope this wide — I hold 20. P-1, P-6 and P-10 on portal 12–14 and NOC 10–12: A3 gives a live v1 as the requirements reference, so these are rebuilds, not discovery — I hold 8 and 8. P-3 (96) and P-8 (92) at the bottom: both cite A5 and A6 yet price the hand-written delivery substrate at 12–14, which their own citation will not bear.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture fixed | §6, A1, A3 | 10 |
| Render worker frame: job intake, process isolation, printer-driver (Black Ice-class) integration, crash recovery | §3.2, §4, A4 | 5 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | §3.4, A7 | 10 |
| OCR workers on a third-party library; TIFF→PDF with digitisation | §2.3, §2.4, A4 | 4 |
| Delivery-control core: watchdogs, tokens, unordered status store, resume-on-failure — the fax orchestrator | §4, A5, A6 | 20 |
| Cluster management tool: node/queue state, work distribution over ~16–20 nodes | §4, §5 | 5 |
| Rx path in the data centre: intake from PoPs, per-user configuration, email assembly and dispatch | §2, A6 | 8 |
| Tx path: inbound-email parser, number extraction, TIFF archive packaging, handoff to the existing routing/PoP | §3.1–3.2, §6 | 7 |
| Storage and data layer: Lustre and DB integration, the inter-component API | §4, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | §4, §6 | 8 |
| User portal | §4, §6 | 8 |
| CDR and billing-data capture (billing itself excluded) | §6, A1 | 3 |
| Integration with the old system and coexistence through the transition | §6, A4 | 6 |
| Comparison harness and integration tests on the real message stream against the old system | §6, A2 | 8 |
| Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4 |
| Load and burst rig to ~30/s nominal and ~300/s peak across 16–20 nodes, and tuning to it | §5, A6 | 5 |
| Project management and coordination (one line, Rule 3): one PM-equivalent plus scrum ceremony ownership across the ~16-month span the 117 pm of work lines imply | §6 process, A3, A8 | 12 |

ADDED
- Render worker frame: job intake, process isolation, printer-driver (Black Ice-class) integration, crash recovery | §3.2, §4, A4 | 5
- Comparison harness and integration tests on the real message stream against the old system | §6, A2 | 8
- Rollout to production traffic, cutover, readiness to decommission v1 | A2 | 4
- Load and burst rig to ~30/s nominal and ~300/s peak across 16–20 nodes, and tuning to it | §5, A6 | 5

(The first three are separations of two round-1 lines, not fresh scope: my round-1 rendering line held the frame, and my round-1 transition line held the harness, the tests and the rollout. The burst rig is genuinely new scope in my table, taken from P-5.)

TOTAL: 129 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 185 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days of work on the task;
              absence stretches the calendar, not the effort); within-day overheads
              (meetings, coordination, review, scrum ceremonies) IN, inside each line;
              roles counted: developers, architects, QA and PM — the blended team of A3/A9,
              including the immersion and technology-selection phase
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing program,
              billing itself, development of the first version, post-launch operation and
              support, hardware/rack procurement and data-centre operations, the OCR library,
              printer driver, Lustre and the DBMS as products (integration only),
              the REQUIREMENTS.md draft, which describes a different system

====================================================================================================
## P-5 — reply of round 2, verbatim

**Quarantine note.** As in round 1, session material outside the task (repository status, commit subjects, memory index, environment and tool listings) reached me; I treated it as data and used none of it. The two sheets I was told to read I treat as the panel's arguments, which is what this round is for.

**What moved me.** Three arguments, all structural rather than numerical.

- **P-1 and P-2** split rendering into a worker framework (job intake, sandboxing, crash recovery of render processes, printer-driver harness) and the per-format integrations. That is two different builds, and my single line priced only the second. I add the framework at 4.
- **P-2, P-6, P-9 and P-3** each carry integration-and-coexistence with v1 as its own line, distinct from cutover. §6 names it explicitly ("only integration with the old system and coexistence for the duration of the transition"), so it is citable work I had folded into a 4 pm cutover line. I separate it at 5.
- **P-1 and P-10** argue the data layer is not thin integration: Lustre and the DBMS are given by A4, but the schema and the inter-component API are the contract every component depends on. 6 → 8. Smaller moves: immersion 9 → 10 and OCR 4 → 5, on the panel's point (P-6, P-8) that the ~1–2 months is the team's width, not one architect's.

**What I read and rejected.** P-10's and P-1's 30 pm orchestrator: same text, no new mechanism named, and my 20 already carries the burst hardening that P-10 also prices separately — taking both would double-count. P-2's, P-6's, P-3's and P-10's PM lines derived as a percentage of the build: Rule 3 asks for a basis, and a percentage of the lines is the uplift Rule 1 forbids wearing a different hat. Mine stays derived from one coordinating head across the duration the lines imply. P-8's 92 and P-3's 96: P-8 prices the Rx delivery path at 3 pm, which cannot cover per-user configuration, page-wise assembly and dispatch at 30/s. I did not follow P-2 and P-6 upward on NOC and portal: P-2's own reasoning — that both sit on a system the cluster tool already instruments — argues for my figures, not theirs.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc. studied) | S6, A1, A3 | 10 |
| Render-worker framework: job intake, sandboxing, printer-driver harness, crash recovery | S3.2, S4, A4 | 4 |
| Per-format renderers, 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and the TIFF→PDF conversion path on a third-party library | S2.3, S6, A4 | 5 |
| Cluster core: watchdogs + tokens, unordered status store, resume-on-failure fax orchestration, distribution over the nodes | S4, A5, A6 | 20 |
| Cluster management tool (queue lengths, node state) | S4 | 3 |
| Rx path: intake of TIFF from PoPs, per-user configuration, email assembly and sending | S2.1–S2.4 | 6 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–S3.3, S6 | 6 |
| Storage and DB layer: Lustre archive and working files, DB schema, inter-component API | S4, A4 | 8 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 6 |
| User portal | S4, S6 | 8 |
| CDR / billing data capture (billing itself out) | S6, A1 | 3 |
| Integration tests on the real stream with the old-system comparison harness | S6, A2 | 10 |
| Load and failure rig to the nominal ~30/s with ~10× burst on 16–20 nodes, and tuning to it | A6, S5 | 6 |
| Integration with the old system and coexistence through the transition | S6, A4 | 5 |
| Cutover: production rollout, stabilisation to v1 decommission readiness | A2 | 4 |
| Project management and coordination (one line, Rule 3) | S6, A8, Rule 3 | 13 |

**Reasoning (≈180 words).** The shape is unchanged: one hard core plus many medium pieces, each line already designed, built, tested and stabilised, with no uplift anywhere. The cluster core holds its 20 because A5 removes every ready mechanism and A6 makes distribution, failure survival and per-fax delivery control mandatory properties; node distribution sits inside it, which is why my cluster-management line stays at 3 where panellists who bundle the runtime price 8–10. Rendering now separates the frame from the formats, at roughly one person-month per format under A7. The data layer rises because the schema and API are ours even though Lustre and the DBMS are not. The PM line is derived, not taken as a rate: 114 pm of work lines across a blended team of about nine implies roughly thirteen calendar months of continuous coordination, hence thirteen person-months at one coordinating head. The range widened upward after seeing how much of the panel sits above me on the orchestrator and the portal — that belief belongs in RANGE, never in TOTAL.

ADDED
- Render-worker framework: job intake, sandboxing, printer-driver harness, crash recovery | S3.2, S4, A4 | 4
- Integration with the old system and coexistence through the transition | S6, A4 | 5

(The per-format renderer line is not new in substance: it is my round-1 rendering line with the framework taken out of it, and it kept its 10. The cutover line is the same line as round 1, narrowed to rollout and decommission readiness now that coexistence stands separately.)

```
TOTAL: 127 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 190 person-months, same convention
TEAM x DURATION: 9 people over 14 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (hours counted are hours worked on the task);
              within-day overheads (meetings, coordination, review, scrum ceremonies) IN,
              inside each line; roles counted: analysts/architects, developers, QA, PM -
              the whole blended team, including the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing itself;
              development of the first version; post-launch operation and support; hardware,
              data-center and PoP rack procurement; Lustre and DBMS administration;
              the third-party OCR library and the printer driver as products (integration only);
              the REQUIREMENTS.md draft, which describes a different system
```
