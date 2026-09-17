# Replies of round 3 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 3, verbatim

VOTES

- **P-1 — Data layer (DB schema, inter-component API, Lustre integration) | §4, §6, A4 | 8** — KEEP. S4 states outright that components communicate through the DB and an API; a schema and a contract are things built, and nine of ten tables carry them separately.
- **P-1 — Load-generation and failure-injection rig for the burst mode | A6 | 4** — KEEP. A rig is a built artefact, and Rule 1 says a deliverable of testing is a line like any other.
- **P-3 — Scale and burst hardening | S5, A6 | 6** — KEEP. Admissible only because it was carved out of the orchestrator (24 → 18), so it is a repartition, not an uplift.
- **P-4 — Render worker host (job model, node-side execution, restart/isolation) | S3.2, S4, A5 | 4** — KEEP. Distinct from a format integration; a split of an existing line, not new scope.
- **P-4 / P-8 / P-9 / P-10 — Production rollout and cutover to decommissioning of v1 | A2 | 4–5** — KEEP. A2's Definition of Done names prod traffic and decommissionability; that is work, and it is citable.
- **P-6 (mine) — Cluster runtime and burst hardening | S5, A6 | 10** — REJECT. At that size and wording it buys twice: "distribution over 16–20 nodes" is the core and the management tool, and the fixes are stabilisation Rule 1 puts inside each line. P-5 turned my own round-1 sentence against it correctly. Only the rig and the end-to-end campaign survive; I replace it at 6 and restore the core.
- **P-6 (mine) — Coexistence with v1 and integration with the reused PoP software and routing | S6, A4 | 6** — KEEP. A4 removes build cost, not integration cost, and nothing else in my table carries the v1 interfaces.
- **P-7 — End-to-end scale and burst hardening | S5, A6 | 7** — KEEP. Narrowed to work on the assembled system and offset by narrowing the orchestrator.
- **P-9 — Interface work with the reused components (PoP protocol, routing hookup) | S3.3, S6, A4 | 4** — KEEP. Same ground; in P-9's table it was previously priced at zero.
- **P-9 — Coexistence with the old system through the transition | S6, A4 | 5** — KEEP. A carve-out, and S6 names coexistence for the duration of the transition.
- **P-10 — Render worker host and printer-driver harness | S3.2, S4, A4 | 5** — KEEP. Same item as P-4's, same ground.
- **P-10 — Integration with the reused assets and coexistence with v1 | S6, A4 | 6** — KEEP. Same ground, carve-out declared.
- REJECT (not contested): none. Every line on the sheet cites a section or an assumption and names work; the remaining disagreements are about size and partition, which the rules leave to judgement.

**What moved me this round.** P-5 withdrew a hardening line by quoting my own Rule-1 reading back at me, and P-1, P-2 and P-9 made the same point from different directions: most of "hardening" is the stabilisation of the blocks it names, already inside them. My 10 pm line was the panel's largest and was partly an uplift in a line's clothes. I cut it to 6 — a load generator at ~300/s, failure injection across nodes and PoPs, and the cross-block tuning no single block owns — and returned the difference to the delivery-control core (20 → 22), where the panel now sits. Second, P-3 and P-10 showed a double count in my PM line: my own declaration puts standups, coordination and review inside every line, so a ~0.9 FTE coordinator on top charges some of those hours twice; 16 → 14 at ~0.8 FTE. Third, small convergence where I was above the panel with no argument of my own: data layer 10 → 9, Rx 10 → 9, NOC 10 → 9.

Read and rejected: P-8's core at 26 and P-5's merged 26 — both rest on how badly the block could overrun, which Rule 2 sends to RANGE. P-1's and P-10's CDR at 3 — no new argument, only a number, and a per-fax record at a million a day touches both paths and the DB; I hold 4. P-3's and P-7's claim that the coexistence line is already inside their data-layer and Tx lines is true of their tables, not mine.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure, no MQ | S4, A5 | 22 |
| End-to-end load and failure-injection rig and campaign across the cluster and the PoPs at ~30/s nominal and ~300/s peak | S5, A6 | 6 |
| Cluster management tool: queue lengths, node state, job placement over 16–20 nodes | S4 | 6 |
| Data layer: Lustre archive and working files, DB schema, the inter-component API | S4, S6, A4 | 9 |
| Rx path: intake of TIFF from the PoPs, per-user page-by-page or PDF configuration, email assembly and dispatch | S2.2–2.4 | 9 |
| Tx path: inbound-email parser, number extraction, archive packaging, handoff to routing/PoP | S3.1–3.2, S6 | 8 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 4 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Coexistence with v1 through the transition and integration with the reused PoP software and routing | S6, A4 | 6 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.8 FTE across the ~18 calendar months the total implies, the planning phase heavier and steady-state scrum lighter | Rule 3, A3, A8 | 14 |

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on this task,
              so absence shows up in the calendar, not in the total); within-day overheads
              (meetings, coordination, review, scrum ceremonies) IN, inside each line, together
              with each block's own stabilisation, which is why the PM line is 0.8 FTE and not
              1.0; roles counted: architects, developers, QA and PM, per A3/A9, plus the
              immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program (interface
              only); billing; development of the first version; post-launch operation and support;
              hardware, rack rental and data-center operations; the OCR engine, the printer driver,
              Lustre and the DBMS as products (integration only, per A4); the divergent
              REQUIREMENTS.md draft; calendar conversion beyond the staffing line above

====================================================================================================
## P-7 — reply of round 3, verbatim

VOTES

- **Data layer — DB schema, inter-component API, Lustre integration (P-1, 8)** — KEEP. §4 says outright that the components communicated through the DB and an API; a schema and a contract are things built, and nine of ten tables now carry the line separately.
- **Render worker host, split from per-format work (P-4, 4; P-10, 5)** — KEEP. §3.2 plus A5: a job model with node-side execution and restart on a Windows cluster is a different artefact from a format integration, and A7 keeps the formats priced on their own.
- **Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10)** — KEEP. A2's Definition of Done names taking prod traffic and decommissioning v1 as the finish line; it is not inside a test harness.
- **Coexistence with v1 through the transition (P-6, P-9, P-10)** — KEEP. §6 names running alongside the old system for the duration of the transition; distinct from the comparison harness, which is a test deliverable.
- **Load-generation and failure-injection rig (P-1, 4; P-9's "load rig and multi-node tuning", 6)** — KEEP. A built rig plus the end-to-end campaign at ~300/s across the assembled system, citable to S5/A6; no single block owns it.
- **Scale and burst hardening as system-wide work (P-3, 6; P-7, 7)** — KEEP, at that narrow width only. Same grounds; my own line sits here and I have cut it to the rig-and-campaign size.
- **Cluster runtime and burst hardening (P-6, 10)** — REJECT. The half described as "distribution over 16–20 nodes, failure survival" is the delivery-control core's own content; paid twice beside a 20 pm core.
- **Interface work with the reused components: PoP protocol and routing hookup (P-9, 4)** — REJECT. Already inside every Rx-ingest and Tx-handoff line on the sheet, mine included; A4 puts that cost where the path meets the PoP, not in a line of its own.
- REJECT (not contested): P-5's merged core at 26 — no line of the text distinguishes 26 from 20; the increment is the fear of a hand-written guarantee overrunning, which Rule 2 sends to RANGE.
- REJECT (not contested): my own round-2 cluster management tool at 8 — I was the lone outlier above a panel at 5–6, and §4 cites one console for queue lengths and node state; corrected below.

**What moved me this round.** P-3's Rule 1 argument against a full-time PM line is the sharpest thing on the sheet: my own declaration puts coordination, review and ceremonies *inside* every line, so charging 1.0 FTE on top bills the same hours twice. PM 16 → 14. P-1 through P-10 sit at 5–6 on the management console against my 8, with no text supporting the gap; 8 → 6. P-8's NOC argument — 10–20 remote PoPs, a 16–20 node cluster and the queues, with nothing to buy in that era — moves NOC 8 → 9. P-4 and P-6 price the render host at 4 where I had 5, and my rendering pair was the panel's top at 16; host 5 → 4. My Tx pair at 11 was above the panel's 7–8 while I was simultaneously rejecting P-9's separate reuse-interface line; since the handoff is inside my line I hold most of it, packaging 6 → 5. Hardening 7 → 6, narrowed to the rig and the end-to-end campaign, which is the only part not already stabilisation of a block. Net 156 → 150. I did not follow P-8 or P-5 upward on the core, nor P-6's compound runtime line, for the reasons voted above.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), to a chosen design, whole blended team | S6, A1, A3 | 12 |
| Rx ingest path: receiving TIFFs from the PoPs into the Miami data center | S2.2 | 4 |
| Render worker host: job model, node-side execution, restart/isolation on the Windows cluster | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 formats via a printer-driver class product, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, A4 | 6 |
| Email assembly and delivery to the user (page-by-page TIFF or PDF, per-user configuration) | S2.3, S2.4 | 5 |
| Inbound-email parser: MIME/attachments, fax-number extraction, sender feedback on errors | S3.1, S6 | 5 |
| Tx packaging and handoff to the PoP (archive out, interfaces to the ready routing and PoP software) | S3.2, S3.3, A4 | 5 |
| Delivery-control orchestrator: watchdogs, tokens, unordered status store, per-fax status and resume after failure | S4, A5 | 20 |
| End-to-end burst campaign: load-generation and failure-injection rig, multi-node tuning to ~30/s nominal and ~300/s peaks | S5, A6 | 6 |
| Cluster management tool: queue depths, node health, work placement over 16–20 nodes | S4, S5 | 6 |
| Data layer: Lustre integration for archive and working files, DB schema, inter-component API | S4, S6, A4 | 9 |
| NOC: state of 10–20 remote PoPs, the cluster and the queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration tests on the real stream with a comparison harness against the old system | S6, A1, A2 | 10 |
| Coexistence and integration with the old system for the transition | S6, A4 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.75 FTE across the ~18 calendar months this total implies, within-day coordination already inside the other lines | S6, A8, A9 | 14 |

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 220 person-months, same convention
TEAM x DURATION: ~8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task, so absence
              lands in the calendar, not in the total); within-day overheads (meetings,
              coordination, code review, standups, scrum ceremonies) IN, inside each line,
              together with each block's own stabilisation; roles counted: analyst/architect,
              developers, QA, PM
  excluded  - PoP software and Brooktrout-side code; the least-cost routing program; billing
              proper; development of the first version; post-launch operation and support;
              hardware, rack and data-center procurement; the OCR library, printer driver,
              Lustre and the DBMS as products (integration only); the divergent
              REQUIREMENTS.md draft; conversion of this total into a committed calendar or
              hiring plan beyond the staffing line above

====================================================================================================
## P-8 — reply of round 3, verbatim

VOTES

- **Data layer / DB schema + inter-component API + Lustre integration (P-1)** — KEEP: §4 states the components communicate through the DB and an API; a schema and a contract are things built, and nine of ten tables now carry them.
- **Load-generation and failure-injection rig for ~300/s bursts (P-1)** — KEEP: a rig is an artefact built, distinct from the per-block stabilisation Rule 1 already buys; P-1 keeps it narrow (4) and offsets nothing that was double-charged.
- **Scale and burst hardening, end-to-end (P-3 6, P-7 7, P-9 6)** — KEEP: A6 makes distribution and failure survival across 16–20 nodes and 10–20 PoPs properties of the assembled system, owned by no single block; all three disclose an offset in the core so the work is counted once.
- **Cluster runtime and burst hardening (P-6 10)** — KEEP: job distribution over the cluster is a thing built (S4, S5), and P-6 states the 24→20 core offset that keeps it from being a second charge.
- **Render worker host: job model, node-side execution, restart/isolation (P-4 4, P-10 5)** — KEEP: the host is a different thing from a format integration (S3.2, S4); a partition of rendering, disclosed by both.
- **Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10, all 4–5)** — KEEP: A2's Definition of Done names taking prod traffic and decommissioning v1; that is work, not a milestone marker.
- **Coexistence with v1 through the transition (P-6 6, P-9 5, P-10 6)** — KEEP: §6 names integration with the old system and coexistence for the duration of the transition as something the team did.
- **Interface work with the reused components: PoP protocol and least-cost routing hookup (P-9 4)** — REJECT: in P-9's own table the Rx pipeline already buys intake from the PoPs and the Tx pipeline already buys packaging and dispatch to them; the hookup is paid for inside those two lines, and P-4 and P-7 rejected P-1's equivalent line for the same reason.
- REJECT (not contested): **my own round-2 line "Integration with v1 and coexistence for the transition; interfaces to ready PoP and routing" (P-8, 7)** — the second clause is the item I just rejected in P-9, sitting inside my own Rx (§2.2 intake) and Tx (archive hand-off) lines. I strike that clause and the line becomes coexistence only.
- No other line on the sheet looks inadmissible to me under Rule 2; the round-2 tables no longer contain risk, glue or rounding lines.

**What moved me.** P-1, P-7 and P-9 each made the same rule-based objection to my core at 26–30: my basis was that the block "carries the weight two or three ordinary services would", which is a claim about novelty, and Rule 2 sends novelty to RANGE. I cannot cite text for the excess, so the core goes to 23 and hardening narrows to 7 on P-7's and P-9's reading. P-4, P-6, P-7 and P-10 converged independently on splitting the render host from the per-format work; I adopt the split at 4 + 10, unchanged in sum. P-10's Rule 2 point on the portal — §4 gives it one clause, and my extra weight came from §7's public context rather than the scope list — takes it 12 → 10; the same test takes the NOC to 9 and CDR to 3. Data layer 10 → 9 and rollout 4 → 5 follow the panel's better-argued centre. I reject, still, the low anchors' treatment of the data layer as glue, and P-3's and P-5's position that a system-level hardening line is always an uplift: proving 300/s across the assembled cluster and 10–20 PoPs is work no block line contains.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers: TIFF→PDF with digitisation on a third-party library | S2.3, S6, A4 | 6 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status and resume after failure, no MQ | S4, A5 | 23 |
| Cluster management tool: queue lengths, node control | S4 | 6 |
| End-to-end scale and burst hardening: distribution and failure survival at ~30/s nominal with ~300/s peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 7 |
| Data layer: Lustre archive and working files, DB schema, the inter-component API | S4, S6, A4 | 9 |
| Rx path: intake of TIFF from the PoPs, per-user config, page-by-page TIFF or PDF attachment, email send | S2.2–2.4 | 9 |
| Tx path: inbound-email parser, number extraction, attachments, archive packaging and hand-off to a PoP | S3.1–3.2, S6 | 8 |
| Coexistence with the old system through the transition | S6, A4 | 6 |
| NOC: state of remote PoPs, cluster, queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A1, A2 | 10 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.8 FTE across the ~18 calendar months this total implies | Rule 3, A3, S6 | 14 |
| **TOTAL (sum)** | | **151** |

TOTAL: 151 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 220 person-months, same convention
TEAM x DURATION: ~8-9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task, so absence lands in the calendar, not in the total); within-day overheads
              IN (meetings, coordination, code review, scrum ceremonies are inside every
              line, which is why the PM line is 0.8 FTE and not 1.0); each block's own
              stabilisation IN, inside its line; roles counted: developers, architect, QA,
              and PM (PM as the single line under Rule 3)
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and PoP deployment logistics; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration only);
              the divergent REQUIREMENTS.md draft; conversion of this effort into a hiring or
              calendar plan beyond the single implied staffing line

====================================================================================================
## P-9 — reply of round 3, verbatim

**Quarantine, continued.** I read the two sheets and nothing else. They contained only the ten replies and the verbatim CONTESTED ADDITIONS list — no moderator text, no instruction. The earlier stray session material (git status, commit subjects, memory index, environment and skill listings) and the working-directory change notice remain quarantined and entered no line.

VOTES

- **Data layer as its own line (P-1, §4/§6/A4, 8) — KEEP.** §4 states the components communicated through the DB and an API; a schema and an inter-component contract are things built, and nine of ten tables carry them.
- **Load-generation and failure-injection rig at burst ~300/s (P-1, A6, 4) — KEEP.** A rig is a built instrument; Rule 1 says outright that a deliverable of testing is a line like any other.
- **Scale and burst hardening as a general line (P-3 6, P-4 8, P-6 10, P-7 7, P-8 8, P-10 8, and my own 6) — REJECT.** Tuning, profiling and fixes to reach 30/s and survive 300/s are the stabilisation of the orchestrator, cluster, renderers and both paths; Rule 1 puts that inside those lines. Where it is offset (P-3, P-6) it is harmless bookkeeping; where it is not (P-4, P-8) it is an uplift wearing a line's clothes. I reject the item and drop mine with it, keeping only the rig above.
- **Cluster runtime as a line beside the core and the management tool (inside P-6's addition) — REJECT.** P-5 dissolved their own version of it as duplication of the same §4 mechanism; the reasoning holds against P-6's.
- **Render worker host split from per-format work (P-4 4, P-10 5) — KEEP.** Node-side job model, restart and isolation on the Windows cluster (§3.2, §4) is a different artefact from a format integration; it is a partition, so the per-format line must fall by the same amount.
- **Production rollout and cutover to the point v1 can be decommissioned (P-4 5, P-8 4, P-9 5, P-10 5) — KEEP.** A2's Definition of Done names prod traffic taken and v1 decommissionable; that is work, and it is not inside the comparison harness.
- **Coexistence with v1 through the transition (P-6 6, P-9 5, P-10 6) — KEEP.** §6 names integration with the old system and coexistence for the duration of the transition as scope in its own words.
- **Interface work with the reused PoP software and routing as a separate line (P-1 8, my own 4) — REJECT.** P-3, P-4 and P-7 are right against me: my Rx line already buys intake from the PoPs and my Tx line the handoff to the ready routing and PoP. I withdraw my own addition rather than defend it.

REJECT (not contested): none. Scanning all ten tables I find no line that fails Rule 2 on its face — every line names a thing built or a piece of work done and cites the text. The residual disagreements are about size and partitioning, which Rule 2 does not govern.

**What this costs me.** Two of my four round-2 additions fall by my own vote: the hardening line (−6, replaced by the 4 pm rig) and the reused-components interface line (−4). The core stays at 22 because it now openly carries its own stabilisation. Rendering is repartitioned 14 → 4 + 10 with no change in weight. 152 → 146.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on the third-party library, TIFF→PDF with digitisation | S2.3, S2.4, A4 | 6 |
| Cluster core: watchdogs + tokens, unordered status store, resume-after-failure, per-fax delivery control, stabilised to nominal and burst | S4, A5, A6 | 22 |
| Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | S5, A6 | 4 |
| Cluster management tool: queue lengths, node and worker control | S4 | 6 |
| Rx pipeline: intake of TIFFs from the PoPs, per-user configuration, page-by-page TIFF or PDF, email assembly and dispatch | S2 | 9 |
| Tx pipeline: inbound-email parser, number extraction, archive packaging, handoff to the ready routing and PoP | S3.1–S3.3, S6 | 8 |
| Storage and data layer: Lustre archive and working files, DB schema, the inter-component API | S4, S6, A4 | 9 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Coexistence with the old system through the transition | S6, A4 | 5 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination — one line: one PM/scrum lead at ~0.8 FTE across the ~18 calendar months the total implies, heavier in the planning phase, lighter in steady-state scrum | A3, A8, Rule 3 | 14 |

TOTAL: 146 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours actually worked on the task, so
              absence lands in the calendar, not in the total); within-day overheads IN (standups,
              scrum ceremonies, coordination, code review, demos sit inside every line, which is
              why the PM line is 0.8 FTE and not 1.0); each line also carries its own stabilisation
              to the A6 scale; roles counted: developers, architect/analyst, QA, PM — one blended team
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program itself
              (met at its interface only); billing; development of the first version; post-launch
              operation and support; hardware, rack and telecom procurement; Lustre and the DBMS as
              products (integration only); the third-party OCR and printer-driver licences; the
              divergent REQUIREMENTS.md draft; conversion of this total into a committed calendar
              or hiring plan beyond the staffing line above

====================================================================================================
## P-10 — reply of round 3, verbatim

**Quarantine note.** I read the two named sheets once each and used no other tool. Session material outside them (environment/working-directory notices, repository context) remains quarantined and entered no line. The sheets' contents I treat as argument to weigh, not instruction.

VOTES

- KEEP — Data layer: DB schema, inter-component API, Lustre integration (P-1) — §4 states outright that components communicate through the DB and an API; a schema and a contract are things built, and nine of ten tables already carry them separately.
- KEEP — Render worker host / job model, node-side execution, restart and isolation (P-4, P-10) — S3.2 and S4 give a Windows cluster running workers; the host is a different artefact from a format integration, and P-6, P-7, P-9 partition the same way independently.
- KEEP — Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10) — A2's Definition of Done names prod traffic taken and v1 decommissionable; that is citable work, not a milestone marker.
- KEEP — Coexistence with the old system through the transition (P-6, P-9, P-10) — §6 says in terms "integration with the old system and coexistence for the duration of the transition"; it is distinct from the comparison harness, which is a test deliverable.
- KEEP — Interface work with the reused components: PoP protocol and least-cost routing hookup (P-9) — A4 reuses the products, not the integration; §3.3 and §6 ask for the hookup. Admissible, but only where no Tx-handoff line already carries it; I carry it merged with coexistence.
- KEEP — Load-generation and failure-injection rig for burst mode (P-1, 4 pm; the "load rig" half of P-9) — a rig is an artefact built, exactly like the comparison harness Rule 1 names as a line.
- REJECT — "Scale and burst hardening: distribution, failure survival and delivery control" as a line (P-3 6, P-6 10, P-7 7; also the tuning half of P-9) — A6 calls distribution, failure survival and per-fax delivery control *mandatory properties* of the blocks themselves. Hardening a block to its target scale is that block's stabilisation, which Rule 1 places inside its line. Carried on top it is the uplift Rule 1 forbids, whatever it is called. P-5's removal of their own such line is the correct reading.
- REJECT (not contested) — my own round-2 line "Scale and burst hardening to ~30/s nominal with ~10× peaks" (P-10, 8 pm) — same reason; I cannot vote down P-3/P-6/P-7 and keep mine. Its stabilisation content goes back inside the core (20 → 22); only the rig survives as a line, at 5.
- REJECT (not contested) — the row "**TOTAL (sum)** | | 168/160" inside P-8's table (S-none) — a sum is not a thing built and cites nothing; harmless arithmetically, inadmissible as a line under Rule 2.

**What else changed.** P-6's and P-7's immersion arithmetic (~1.5 calendar months carried by the whole blended eight) is plain, and my own staffing line says eight: 11 → 12. P-8's NOC argument is a citation, not a novelty claim — §4 and §5 give it 10–20 remote PoPs, a 16–20-node cluster and the queues, with nothing to buy in that era: 8 → 9. Portal 9 → 10, where nine of ten now sit, on §2.3's per-user delivery configuration being the portal's own surface. Rx 8 → 9 and Tx 7 → 8, both to the panel's bottom-up centre. PM basis unchanged at ~0.75 FTE, now over 18–19 implied months: 13 → 14. I still reject the 24–26 pm core (P-2, P-4, P-5, P-8): the mechanism described is an unordered token store over the existing DB, chosen because MSMQ was too much machinery, and "it can overrun badly" is a RANGE statement.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 5 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers on a third-party library; TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens, unordered token store, per-fax status, resume after failure, stabilised to nominal and burst | S4, A5, A6 | 22 |
| Cluster management tool: node and queue-length control, job placement over ~16–20 nodes | S4, S5 | 6 |
| Data layer: Lustre archive and working files, DB schema, the API components talk through | S4, S6, A4 | 9 |
| Rx path in the data centre: intake of TIFF from the PoPs, per-user TIFF-page or PDF attachment, email assembly and dispatch | S2.1–2.4 | 9 |
| Tx path: inbound-email parser, number extraction, archive assembly, handoff to routing/PoP | S3.1–3.2, S6 | 8 |
| NOC: state of 10–20 remote PoPs, the cluster and the queues | S4, S5, S6 | 9 |
| User portal, including per-user delivery configuration | S2.3, S4, S6 | 10 |
| CDR / billing-data capture (billing engine excluded) | S6, A1 | 3 |
| Integration with the reused assets (PoP software, least-cost routing) and coexistence with v1 through the transition | S3.3, S6, A4 | 6 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Load-generation and failure-injection rig for nominal ~30/s and ~300/s burst across the cluster and the PoPs | S5, A6 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.75 FTE across the ~19 calendar months the total implies | Rule 3, A3, A8 | 14 |

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time on task, not elapsed payroll time;
              calendar staffing must add for absence); within-day overheads (meetings,
              coordination, code review, standups, scrum ceremonies) IN, inside every line,
              together with each block's own stabilisation to target scale; roles counted:
              developers, architect, QA, PM, plus the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program
              (interface only); the billing system itself; development of the first version;
              post-launch operation and support; hardware, rack and carrier procurement; the
              third-party OCR library, printer driver, Lustre and the DBMS as products
              (integration only); the divergent REQUIREMENTS.md draft; conversion of this
              total into a committed calendar or hiring plan beyond the staffing line above

====================================================================================================
## CONTESTED ADDITIONS — every "ADDED" block of round 3, copied verbatim under its author's label

(no participant listed an addition)
