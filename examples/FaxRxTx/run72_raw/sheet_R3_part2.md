# Replies of round 2 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 2, verbatim

**What moved me, and what I rejected.** Two arguments changed lines. First, P-5, P-4, P-2, P-8 and P-10 each carry a distinct scale-and-burst line citing A6/S5. I had folded burst work into the orchestrator, which hid that hardening to ~30/s nominal and ~300/s peak is system-wide work — load rigs, distribution over 16–20 nodes, profiling and fixes in the renderers, data layer and both mail paths — not a property of one block. I added that line and, to avoid double counting, cut the delivery-control core from 24 to 20, which is also where P-1 (20), P-7 (18) and P-10 (18) sit. Second, P-1 and P-7 argue that A4's reuse removes build cost but not integration cost, and that coexistence with a live v1 is separate work from the comparison harness. My round-1 line 13 combined them; I split it, which raises the pair from 12 to 16.

Read and rejected: P-9's 106 and P-1's 120 as low anchors — P-9 prices CDR capture at 2 across both paths and the DB, and folds coexistence, the comparison harness and cutover into one 10 pm line, which under-serves A2's Definition of Done (prod traffic taken, results agreeing, v1 decommissionable). Also rejected P-8's 30 pm orchestrator: at that size it absorbs hardening that belongs to the whole system.

No material outside the two sheets and the coordinator's instruction reached me this round.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | S6, A1, A3 | 12 |
| Render workers: worker framework + printer-driver integration | S3.2, S3.4, A4 | 4 |
| Per-format rendering: 8–10 formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→searchable PDF | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens, unordered status store, resume, no MQ | S4, A5 | 20 |
| Cluster runtime and burst hardening: distribution over 16–20 nodes, failure survival, load runs to ~30/s nominal and ~300/s peak | S5, A6 | 10 |
| Cluster management tool (queue lengths, node state, dispatch) | S4 | 6 |
| Storage and data layer: Lustre archive + working files, DB schema, component API | S4, A4 | 10 |
| Rx path: intake from PoPs, per-user configuration, email assembly and send | S2.1–2.4 | 10 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–3.2, S6 | 8 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A2 | 10 |
| Coexistence with v1 through the transition and integration with the reused PoP software and routing | S6, A4 | 6 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.9 FTE across the ~18 calendar months the total implies | Rule 3, A3, A8 | 16 |

ADDED
- Cluster runtime and burst hardening: distribution over 16–20 nodes, failure survival, load runs to ~30/s nominal and ~300/s peak | S5, A6 | 10
- Coexistence with v1 through the transition and integration with the reused PoP software and routing | S6, A4 | 6

(For the panel to contest cleanly: my round-1 line "Integration on the real stream with comparison to the old system, plus coexistence during transition" (12 pm) was split into the test-and-harness line (10) and the coexistence line above (6), and the delivery-control core was cut 24 → 20 as the offset for the hardening line.)

TOTAL: 157 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 115 ... 220 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on this task,
              so absence shows up in the calendar, not in the total); within-day overheads
              (meetings, coordination, review, scrum ceremonies) IN, inside each line; roles
              counted: architects, developers, QA and PM, per A3/A9, plus the immersion and
              technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program; billing;
              development of the first version; post-launch operation and support; hardware,
              rack rental and data-center operations; the OCR engine, the printer driver, Lustre
              and the DBMS as products (integration only, per A4); the divergent REQUIREMENTS.md
              draft; calendar conversion beyond the staffing line above

====================================================================================================
## P-7 — reply of round 2, verbatim

**What moved me.** Three arguments.

P-6 spelled out the immersion arithmetic — ~1.5 calendar months carried by the whole blended team of about eight. My 9 pm implicitly priced a six-person subset while my own staffing line said eight; P-3 and P-8 land in the same place. Raised to 12.

P-2, P-4, P-5, P-8 and P-10 each carry a separate end-to-end capacity line off A6. I had folded burst resilience into the orchestrator line's wording. A6 makes distribution, failure survival and delivery control mandatory *system* properties across 16–20 nodes and 10–20 PoPs; proving that at ~300/s is work done on the assembled system, not inside any one block. I split it out, narrowing the orchestrator to correctness and resumption and raising it to 20 (P-1 and P-9's figure), so the pair is 27 where I previously had 18.

P-3, P-5, P-6 and P-8 price the Lustre/DB/API spine at 10; every component talks through it (§4). Raised 7 to 9.

**Read and rejected.** P-8's orchestrator at 30 — roughly a fifth of their total on one block, argued from how badly it "can overrun". That belief is exactly what Rule 2 sends to RANGE, so I did not follow it into TOTAL. P-1's single 8 pm "integration with the reused parts" line — my Tx-handoff and data-layer lines already carry those costs, and adopting it would double count. P-9's OCR at 4 and CDR at 2 — thin for a per-fax record at a million a day. P-5's cluster runtime as a twelfth line beside the management tool — my render worker host covers node-side execution.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), to a chosen design | S6, A1, A3 | 12 |
| Rx ingest path: receiving TIFFs from the PoPs into the Miami data center | S2.2 | 4 |
| Render worker host: job model, node-side execution, restart/isolation on the Windows cluster | S3.2, S4, A5 | 5 |
| Format renderers: 8–10 formats via a printer-driver class product, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 6 |
| Email assembly and delivery to the user (page-by-page TIFF or PDF, per-user configuration) | S2.3, S2.4 | 5 |
| Inbound-email parser: MIME/attachments, fax-number extraction, sender feedback on errors | S3.1, S6 | 5 |
| Tx packaging and handoff to the PoP (archive out, integration with the ready routing and PoP software) | S3.2, S3.3, A4 | 6 |
| Delivery-control orchestrator: watchdogs, tokens, unordered status store, per-fax status and resume after failure | S4, A5 | 20 |
| End-to-end scale and burst hardening: distribution and failure survival at ~30/s nominal with ~300/s peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 7 |
| Cluster management tool: queue depths, node health, work distribution over 16–20 nodes | S4, S5 | 8 |
| Data layer: Lustre integration for archive and working files, DB schema, inter-component API | S4, A4 | 9 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 8 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration tests on the real stream with a comparison harness against the old system | S6, A1, A2 | 10 |
| Coexistence and integration with the old system for the transition | S6, A4 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one dedicated PM/scrum lead at ~0.9 FTE across the ~18 calendar months this total implies | S6, A8, A9 | 16 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| End-to-end scale and burst hardening: distribution and failure survival at ~30/s nominal with ~300/s peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 7 |

TOTAL: 156 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 225 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside each line; roles counted: analyst/architect, developers, QA, PM
  excluded  - PoP software and Brooktrout-side code; the least-cost routing program;
              billing proper; development of the first version; post-launch operation
              and support; hardware, rack and data-center procurement; the OCR library,
              printer driver, Lustre and the DBMS as products (integration only);
              the divergent REQUIREMENTS.md draft

====================================================================================================
## P-8 — reply of round 2, verbatim

**Quarantine note (round 2).** The two panel sheets and the coordinator's round-2 instruction are the sanctioned input for this round and are treated as such; everything else that arrived with them — a working-directory change notice and the earlier session/repository material — remains quarantined and entered no line.

**What moved me.** Three arguments, all against my own numbers. P-10 and P-9 priced OCR at 4 on the ground that A4 makes it a third-party library integration, not a build; I was carrying 8 for work I cannot point to, so I cut to 6. P-6 split rendering into a worker framework plus per-format units and landed at 14; that partition is better evidence than my lump of 16, so I took 14. P-7 and P-10 at 18 on the delivery-control core forced me to check mine of 30 — I hold the shape but trim to 26, noting that my orchestrator plus cluster-management pair (32) already sits below P-5's equivalent trio (41) and level with P-2 (34), so the apparent outlier was partly a partitioning artefact. P-4 and P-7 also convinced me that integration with reused, ready components is bounded work: 8 → 7. Separately, P-1, P-3, P-4, P-6 and P-10 all cite §2.2 in their Rx line; my round-1 Rx line cited only §2.3–2.4 and silently omitted intake of TIFFs from the PoPs, so that line is corrected upward to 9.

**Read and rejected.** P-9's 106 and P-10's 118 get there mainly by pricing the NOC at 7 and the portal at 7–8. I reject that: the NOC watches 10–20 remote PoPs, a 16–20 node cluster and the queues (§4, §5) with no era tooling to buy, and the portal is the customer surface of an enterprise service with per-user delivery configuration (§2.3, §7). I hold 10 and 12. I also reject P-9's and P-1's merging of cutover into the test line — cutover to the point v1 can be decommissioned is A2's own work and should be visible, so I split it out instead.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team | S6, A1, A3 | 12 |
| Render workers: worker framework + 8–10 format integrations via printer driver, each stabilised | S3.2, S3.4, A7, A4 | 14 |
| OCR workers: TIFF→PDF with digitisation on a third-party library | S2.3, S6, A4 | 6 |
| Cluster delivery-control core: watchdogs, tokens, unordered status store, resume — the fax orchestrator | S4, A5 | 26 |
| Cluster management tool: queue lengths, node control | S4 | 6 |
| Storage and DB layer: Lustre + DB + the inter-component API | S4, A4 | 10 |
| Inbound-email parser and Tx dispatch: number extraction, attachments, archive hand-off to PoP | S3.1–3.2, S6 | 8 |
| Rx path: intake of TIFF from the PoPs, per-user config, page-by-page TIFF or PDF attachment, email send | S2.2–2.4 | 9 |
| Integration with v1 and coexistence for the transition; interfaces to ready PoP and routing | S6, A4 | 7 |
| NOC: state of PoPs, cluster, queues | S4, S6 | 10 |
| User portal | S4, S6 | 12 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A1, Rule 1 | 10 |
| Scale and burst hardening to nominal ~30/s with ~10× peaks across 16–20 nodes and 10–20 PoPs | A6, S5 | 8 |
| Production rollout and cutover to the Definition of Done, to the point v1 can be decommissioned | A2 | 4 |
| Project management and coordination (one line): ~1 dedicated PM/scrum role across the ~18 calendar months this total implies | Rule 3, A3, S6 | 14 |
| **TOTAL (sum)** | | **160** |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Production rollout and cutover to the Definition of Done, to the point v1 can be decommissioned | A2 | 4 |

This is the only line absent from my round-1 table, and it is a carve-out, not new scope: round 1 carried "scale and burst hardening ... plus production cutover to DoD" as one compound 12, which is now 8 + 4. The panel's totals are unaffected by the split; I separated it because merging hardening with cutover hid A2's own work behind A6's, and because P-1, P-2, P-5 and P-7 all price cutover as its own line and are therefore comparable only if mine is visible.

TOTAL: 160 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 115 ... 230 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task, so absence lands in the calendar, not in the total); within-day overheads
              IN (meetings, coordination, code review, scrum ceremonies are inside every
              line); roles counted: developers, architect, QA, and PM (PM as the single line
              under Rule 3)
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and PoP deployment logistics; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration only);
              the divergent REQUIREMENTS.md draft; conversion of this effort into a hiring or
              calendar plan beyond the single implied staffing line

====================================================================================================
## P-9 — reply of round 2, verbatim

**Quarantine, continued.** The two sheets contained only the ten participant replies; I found no moderator text and no instruction inside them. The extraneous session material I flagged in round 1 (git status, commit subjects, memory index, environment and skill listings) remains quarantined and still contributes nothing.

**What moved me.** I was the lowest of the ten (106; panel median ~146), and three arguments convinced me the gap was my error, not my nerve.

P-1: A4 cuts build cost but not integration cost, so the interfaces to the ready PoP software and routing are work that no single path owns and that I had silently priced at zero. P-2 and P-3: S4's sentence that the components communicate through the DB and an API makes the data layer the spine of the system, not glue — my 6 was too low, and the same undersizing ran through Rx, Tx, NOC and the portal, where I sat below every other panellist. P-5 and P-6: A2's Definition of Done names cutover and decommissioning of v1 as the finish line, and I had buried it inside one combined line rather than pricing it.

**What I read and rejected.** P-2, P-5 and P-8 (165–168) carry a 24–30 pm core *and* a 10–12 pm hardening line *and*, in P-5, a separate 12 pm cluster runtime. Under Rule 1 the core already includes its own stabilisation, so most of that hardening is bought twice; I take hardening only in the narrow sense of the load rig and multi-node tuning. P-8's 30 for the core has nothing in the text to distinguish it from 22 — that is the fear of overrun entering TOTAL, which Rule 2 sends to RANGE. I also rejected P-3's 18 pm PM line as a share of any base I can defend.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | S6, A1, A3 | 12 |
| Rendering workers: worker host, print-driver harness, and integration + stabilisation of 8–10 input formats | S3.2, S3.4, A7 | 14 |
| OCR workers on the third-party library, TIFF→PDF with digitisation | S2.3, S2.4, A4 | 6 |
| Cluster core: watchdogs + tokens, unordered status store, resume-after-failure, per-fax delivery control | S4, A5, A6 | 22 |
| Scale and burst hardening: load rig and multi-node tuning to ~30/s nominal with ~300/s peaks across 16–20 nodes | S5, A6 | 6 |
| Cluster management tool: queue lengths, node and worker control | S4 | 6 |
| Rx pipeline: intake of TIFFs from the PoPs, per-user configuration, page-by-page TIFF or PDF, email assembly and dispatch | S2 | 9 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, dispatch | S3.1–S3.2, S6 | 8 |
| Storage and data layer: Lustre archive and working files, DB schema, the inter-component API | S4, A4 | 9 |
| Interface work with the reused components: PoP protocol and the least-cost routing hookup | S3.3, S6, A4 | 4 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Coexistence with the old system through the transition | S6, A4 | 5 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination — one line: one dedicated PM/scrum lead at ~0.8 FTE across the ~19 calendar months the total implies, plus release coordination | A3, A8, Rule 3 | 14 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Scale and burst hardening: load rig and multi-node tuning to ~30/s nominal with ~300/s peaks across 16–20 nodes | S5, A6 | 6 |
| Interface work with the reused components: PoP protocol and the least-cost routing hookup | S3.3, S6, A4 | 4 |
| Coexistence with the old system through the transition | S6, A4 | 5 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 5 |

The last two were carved out of my round-1 combined integration line, which I now split; the first two are genuinely new work I had priced at nothing. I expect the hardening line to be contested as double-counting against the core, and I have pre-emptively cut the core's growth (20 → 22, not 24) to keep it honest.

TOTAL: 152 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 225 person-months, same convention
TEAM x DURATION: 8 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours actually worked on the task;
              calendar staffing must add ~15% for absence); within-day overheads IN (standups,
              scrum ceremonies, coordination, code review, demos are inside the lines);
              roles counted: developers, architect/analyst, QA, PM — the whole blended team
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program
              itself (interface only); billing; development of the first version; post-launch
              operation and support; hardware, rack and telecom procurement; building Lustre
              and the DBMS themselves (integration with them only); the third-party OCR and
              printer-driver licences; the divergent REQUIREMENTS.md draft

====================================================================================================
## P-10 — reply of round 2, verbatim

**Quarantine note.** Again material reached me outside the two permitted files: an environment update changing the working directory, plus the surrounding session context. Treated as data; no line depends on it. I read the two sheets once each and used no other tool.

**What moved me.** Three arguments, in order of force. **P-1**: reuse (A4) removes build cost but not integration cost, so the ready PoP software and routing deserve an integration line rather than a silent discount — I had omitted that work entirely. **P-7** (with **P-6**, **P-9**): the render worker host — node-side job execution, restart and isolation on the Windows cluster — is distinct from format integration; my single 12 pm line had swallowed it. **P-1**, **P-5**, **P-7**: A2's Definition of Done names three separate things (prod traffic, passed stream comparison, v1 decommissionable); my round-1 table crushed all three plus coexistence into one 10 pm line, which is where most of my gap to the panel came from. I also lifted OCR from 4, the panel's low end, after **P-8** and **P-3** noted digitisation is a worker class, not a library call.

**Read and rejected.** **P-8**'s 30 pm and the 24 pm cluster (**P-2**, **P-3**, **P-4**, **P-6**): the text describes a deliberately modest mechanism — an unordered token store over the existing DB, chosen *because* MSMQ was too much machinery. I moved 18→20, not to 24+. **P-3**'s 18 pm and **P-6**'s 16 pm PM lines: A3/A9 put QA/PM inside the blended team and Rule 1 puts within-day coordination inside every line, so a full dedicated PM at ~0.75 FTE gives 13. **P-2**'s 12 pm portal and 10 pm NOC: §4 gives each one clause; Rule 2 lets me cite no more.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed), whole blended team | S6, A1, A3 | 11 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 5 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers on a third-party library; TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens, unordered token store, per-fax status, resume after failure | S4, A5 | 20 |
| Cluster management tool: node and queue-length control, job placement over ~16–20 nodes | S4, S5 | 6 |
| Data layer: Lustre archive and working files, DB schema, the API components talk through | S4, S6, A4 | 9 |
| Rx path in the data centre: intake from PoPs, per-user TIFF-page or PDF attachment, email dispatch | S2 | 8 |
| Tx path: inbound-email parser, number extraction, archive assembly, handoff to routing/PoP | S3.1–3.2, S6 | 7 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 8 |
| User portal | S4, S6 | 9 |
| CDR / billing-data capture (billing engine excluded) | S6, A1 | 3 |
| Integration with the reused assets (PoP software, least-cost routing) and coexistence with v1 through the transition | S6, A4 | 6 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Scale and burst hardening to ~30/s nominal with ~10× peaks across 16–20 nodes, 10–20 PoPs | A6 | 8 |
| Project management and coordination (one line): one dedicated PM/scrum lead at ~0.75 FTE across the ~18 calendar months the total implies | Rule 3, A3, A8 | 13 |

ADDED

| line | source in the text | person-months |
|---|---|---|
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 5 |
| Integration with the reused assets (PoP software, least-cost routing) and coexistence with v1 through the transition | S6, A4 | 6 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |

(For the panel to contest fairly: the last two are carved out of my round-1 line "Integration with the old system, coexistence during transition, integration tests… cutover to prod," which was 10 pm and is now the 10 pm test line alone. The net addition of those two is therefore +11, not +21.)

TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time on task, not elapsed payroll time;
              calendar staffing must add for absence); within-day overheads (meetings,
              coordination, code review, standups, scrum ceremonies) IN, inside every line;
              roles counted: developers, architect, QA, PM, plus the immersion and
              technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing system itself; development of the first version; post-launch
              operation and support; hardware, rack and carrier procurement; the
              third-party OCR library, printer driver, Lustre and the DBMS as products
              (integration only); the divergent REQUIREMENTS.md draft; conversion of this
              total into a committed calendar or hiring plan beyond the staffing line above

====================================================================================================
## CONTESTED ADDITIONS — every "ADDED" block of round 2, copied verbatim under its author's label

### from P-1

ADDED
- Data layer: DB schema, the inter-component API the components talk through, Lustre integration for the fax archive and working files | §4, §6, A4 | 8
- Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | A6 | 4

### from P-2

ADDED: none

### from P-3

ADDED
- Scale and burst hardening: distribution, failure survival and delivery control at ~30/s nominal with ~10× peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 6 pm. This is not new work relative to my round 1 — it was inside my 24 pm orchestrator line, which is now 18. Net effect on TOTAL: zero.

### from P-4

ADDED
- Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 — a split of my round-1 rendering line, which was 14 and is now 4 + 11 = 15
- Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 — previously folded into my test line, which keeps its 10

### from P-5

ADDED: none.

No line in this table carries work that was absent from my round-1 table. The core line changed scope by absorbing my former "Cluster runtime" line, and my former "Scale and burst hardening" line was removed into the lines whose stabilisation it was; both are subtractions, not additions. The PM line fell from 15 to 14 to stay at ~11 percent of a smaller body of work.

### from P-6

ADDED
- Cluster runtime and burst hardening: distribution over 16–20 nodes, failure survival, load runs to ~30/s nominal and ~300/s peak | S5, A6 | 10
- Coexistence with v1 through the transition and integration with the reused PoP software and routing | S6, A4 | 6

(For the panel to contest cleanly: my round-1 line "Integration on the real stream with comparison to the old system, plus coexistence during transition" (12 pm) was split into the test-and-harness line (10) and the coexistence line above (6), and the delivery-control core was cut 24 → 20 as the offset for the hardening line.)

### from P-7

ADDED

| line | source in the text | person-months |
|---|---|---|
| End-to-end scale and burst hardening: distribution and failure survival at ~30/s nominal with ~300/s peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 7 |

### from P-8

ADDED

| line | source in the text | person-months |
|---|---|---|
| Production rollout and cutover to the Definition of Done, to the point v1 can be decommissioned | A2 | 4 |

This is the only line absent from my round-1 table, and it is a carve-out, not new scope: round 1 carried "scale and burst hardening ... plus production cutover to DoD" as one compound 12, which is now 8 + 4. The panel's totals are unaffected by the split; I separated it because merging hardening with cutover hid A2's own work behind A6's, and because P-1, P-2, P-5 and P-7 all price cutover as its own line and are therefore comparable only if mine is visible.

### from P-9

ADDED

| line | source in the text | person-months |
|---|---|---|
| Scale and burst hardening: load rig and multi-node tuning to ~30/s nominal with ~300/s peaks across 16–20 nodes | S5, A6 | 6 |
| Interface work with the reused components: PoP protocol and the least-cost routing hookup | S3.3, S6, A4 | 4 |
| Coexistence with the old system through the transition | S6, A4 | 5 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 5 |

The last two were carved out of my round-1 combined integration line, which I now split; the first two are genuinely new work I had priced at nothing. I expect the hardening line to be contested as double-counting against the core, and I have pre-emptively cut the core's growth (20 → 22, not 24) to keep it honest.

### from P-10

ADDED

| line | source in the text | person-months |
|---|---|---|
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 5 |
| Integration with the reused assets (PoP software, least-cost routing) and coexistence with v1 through the transition | S6, A4 | 6 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |

(For the panel to contest fairly: the last two are carved out of my round-1 line "Integration with the old system, coexistence during transition, integration tests… cutover to prod," which was 10 pm and is now the 10 pm test line alone. The net addition of those two is therefore +11, not +21.)
