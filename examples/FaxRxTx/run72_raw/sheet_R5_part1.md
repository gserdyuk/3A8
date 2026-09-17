# Replies of round 4 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 4, verbatim

My round-3 table carries no fallen item. I was among the five who rejected the broad hardening wording, and I never had a "cluster runtime" line, so nothing is removed and no person-months move anywhere. My one A6 line is the narrow form the tally left standing: I have widened its wording to name the end-to-end campaign run on the rig, which was always inside that 4 pm, and I have not added to it — none of the fallen line's volume comes back under a new name. The block stabilisation those figures stood for stays where Rule 1 puts it, inside the orchestrator, cluster, rendering and path lines, and my declaration says so. My combined integration-and-coexistence line covers the interface work that also stands; I keep the two together rather than split, and the total is unaffected either way. No table row of mine is a sum.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | §6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness | §3.2, §4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | §3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | §2.3, §6, A4 | 6 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status and resume, holding at ~30/s nominal with ~300/s bursts | §4, A5, A6 | 23 |
| Cluster management tool: queue lengths, node health and work placement over 16–20 nodes | §4, §5 | 6 |
| Data layer: DB schema, the inter-component API the components talk through, Lustre integration for the fax archive and working files | §4, §6, A4 | 9 |
| Rx path in the data centre: intake of TIFF from 10–20 PoPs, per-user page-by-page vs PDF configuration, email assembly and mass delivery | §2.2–2.4 | 8 |
| Tx path: inbound-email parser, fax-number extraction, attachment handling, archive packaging and hand-off | §3.1–3.2, §6 | 8 |
| NOC internal control centre: state of the remote PoPs, the cluster and the queues | §4, §6 | 9 |
| User portal | §4, §6 | 10 |
| CDR and billing-data capture (billing itself out) | §6, A1 | 3 |
| Integration with the reused PoP software and least-cost routing, and coexistence with v1 through the transition | §6, A4 | 6 |
| Integration tests on the real stream and the comparison harness against the old system | §6, A1, A2 | 10 |
| Load-generation and failure-injection rig for the burst mode (~300/s) and the end-to-end campaign run on it across the cluster and the PoPs | A6 | 4 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.8 FTE across the ~18 calendar months the total implies, heavier in the planning phase, lighter in steady-state scrum | §6, A3, A8 | 14 |

TOTAL: 147 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 210 person-months, same convention
TEAM x DURATION: ~8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time on the task, so absence shows up in
              the calendar, not in the total); within-day overheads (meetings, coordination,
              review, scrum ceremonies) IN, inside each line, together with each block's own
              stabilisation to target scale, which is why no hardening line appears;
              roles counted: developers, architects, QA and PM, blended, plus the immersion and
              technology-selection phase
  excluded  - PoP software and Brooktrout send/receive, least-cost routing, billing itself,
              development of the first version, post-launch operation and support, hardware,
              rack rental and data-centre operations, the OCR library, printer driver, Lustre
              and the DBMS as products (integration only), the divergent REQUIREMENTS.md draft,
              and any calendar or hiring plan beyond the staffing line above

Report for the caller: four Delphi rounds completed as P-1 on the FaxRxTx blind estimate. My total moved 120 → 144 → 147 → 147 (held). The movement came from three arguments, not from anchoring on the panel spread: the DB-and-API spine of §4 is a built structure rather than glue (raised, and split out of an integration line); OCR and the render worker host were mispartitioned in my first table; and my PM line's stated basis did not match the number I wrote, which I corrected downward. I rejected the panel's most popular addition — a separate "scale and burst hardening" line carried by six participants — on the ground that A6 names those as mandatory properties of the blocks, so Rule 1 already puts their stabilisation inside the block lines; that item subsequently fell 5-of-10. I kept only the narrow residue, a load and failure-injection rig, which stood unopposed. Nothing in my final table is a fallen item, and the quarantined out-of-message material (repository status, commit subjects naming the runs and the Delphi, memory index, environment updates, tool listings) entered no line in any round.

====================================================================================================
## P-2 — reply of round 4, verbatim

My round-3 table carried no fallen item. The broad "scale and burst hardening — distribution, failure survival and delivery control" never appeared in it: what I carry is the narrow form that stands, a load-generation and failure-injection rig with the campaign run on it. I have sharpened its wording so nothing of the fallen item can hide inside it — hardening each block to target scale sits inside that block's own line, per Rule 1, and no person-months moved. The only other change is that the two standing items I had combined, the interfaces to the reused PoP software and routing and the coexistence with v1, are now visible as separate lines, 3 and 4, so the panel can compare them.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats via the printer-driver path, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 22 |
| Load-generation and failure-injection rig, and the end-to-end runs made on it at ~30/s nominal and ~300/s burst | S5, A6 | 6 |
| Cluster management tool: node and queue-length control, job placement over 16–20 nodes | S4, S5 | 6 |
| Rx path in the data centre: intake of TIFF from the PoPs, per-user configuration, e-mail assembly and dispatch | S2.2–2.4 | 9 |
| Tx path: inbound-mail parser, number extraction, attachment handling, archive hand-off to a PoP | S3.1–3.2, S6 | 8 |
| Data layer: DB schema and the API the components talk through; Lustre archive and working files | S4, S6, A4 | 9 |
| Interfaces to the reused PoP software and the least-cost routing program | S3.3, S6, A4 | 3 |
| Coexistence with v1 through the transition | S6, A4 | 4 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself out) | S6, A1 | 3 |
| Integration-test harness on the real stream with result comparison to the old system | S6, A1, A2 | 10 |
| Production rollout: cutover onto live traffic to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.8 FTE across the ~19 implied calendar months | S6, A8 | 14 |

```
TOTAL: 151 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task, so absence lands in the calendar, not in the total); within-day
              overheads IN (standups, coordination, code review, scrum ceremonies are
              inside every line, which is why the PM line is 0.8 FTE and not 1.0);
              each block's own stabilisation to target scale IN, inside that block's line;
              roles counted: developers, architect, QA and PM, as one blended team
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing
              program, billing itself, development of the first version, post-launch
              operation and support, hardware and rack/telecom procurement, the OCR
              library, printer driver, Lustre and the DBMS as products (integration
              only, per A4), the divergent REQUIREMENTS.md draft, and any calendar
              conversion beyond the implied staffing line above
```

Quarantine, closing note: the session material flagged in earlier rounds (repository status and commit subjects, memory index, environment block, skill list) and the later working-directory change reached me outside the estimation message; all were treated as data and entered no line. In this round I used no tool, as instructed.

**Report on the whole task.** I read `C:\home\OhmNova\3A8\examples\FaxRxTx\run72_raw\prompt_rules.txt` once and answered it, then took part in three further Delphi rounds, reading only the four sheets the coordinator named (`sheet_R2_part1.md`, `sheet_R2_part2.md`, `sheet_R3_part1.md`, `sheet_R3_part2.md`) and using no other tool. My estimate as P-2 moved 165 → 148 → 150 → 151 person-months. The drop came from removing a broad hardening line that double-counted stabilisation Rule 1 already puts inside each block, and from trimming three lines where I was the panel's outlier; the small rise afterwards came from pricing the immersion phase for the full team and splitting the render worker host from the per-format work. In the round-3 vote I rejected two items — "cluster runtime and burst hardening" and a duplicate reused-component interface line — and both outcomes matched the panel tally.

====================================================================================================
## P-3 — reply of round 4, verbatim

**My round-3 table carries no fallen item.** I rejected the broad hardening wording in round 3 myself and had already re-cut my line to the narrow form the tally upholds: an end-to-end load and failure-injection rig and the campaign run on it. That line stands unchanged at 5.

One disclosure the tally invites. When I narrowed that line in round 3 (6 → 5) I raised the delivery-control core from 18 to 20, so the pair went 24 → 25. That is not the fallen item moved sideways, and I can name the work that stays: distribution across 16–20 nodes and survival of node and PoP failure are properties of the watchdog-and-token mechanism itself, built into it and stabilised with it, which is exactly why the panel refused them a line of their own under Rule 1. They are named inside the core line and are counted once, there. What left my table with the fallen wording is the claim to a *separate* charge for hardening the other blocks to target scale — that charge is gone, not relocated. Two panellists at 20 (P-7, P-10) and one at 22 (P-9) price the core on this same reading.

No tool was used in this round. Nothing outside the coordinator's message reached me; the earlier quarantined material still enters no line.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed), whole blended team | S6, A1, A3 | 12 |
| Rx path in the data center: intake of TIFF from the PoPs, per-user page-by-page vs PDF configuration, email composition and dispatch | S2.2–S2.4 | 9 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Inbound-email parser and the Tx assembly: address parsing, number extraction, archive packaging and hand-off to a PoP | S3.1–S3.2, S6 | 8 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status, resume after failure, distribution and failure survival across the cluster, no MQ | S4, A5, A6 | 20 |
| End-to-end load and failure-injection rig, and the campaign run on it: the assembled system proven at ~30/s nominal and ~300/s peak across 16–20 nodes and 10–20 PoPs | S5, A6 | 5 |
| Cluster management tool: queue lengths, node state, operator actions | S4 | 6 |
| Storage and data layer: Lustre for archive and working files, the DB schema, the inter-component API | S4, S6, A4 | 9 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 3 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A1, A2 | 10 |
| Coexistence with the old system through the transition | S6, A4 | 5 |
| Production rollout and cutover to the point v1 can be decommissioned | A2 | 4 |
| Project management and coordination — one PM/scrum lead at ~0.7 FTE across the ~18 calendar months the total implies, the planning phase heavier and steady-state scrum lighter | Rule 3, A8, A9 | 13 |

```
TOTAL: 143 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours of work on the task, not
              elapsed payroll time; absence shows up in the calendar, not the total);
              within-day overheads IN (standups, coordination, code review, design
              discussion sit inside every line per Rule 1, which is why the PM line is
              0.7 FTE and not 1.0), as does each block's own stabilisation to target
              scale; roles counted: architects, developers, QA and DevOps/infra inside
              the lines, project management as the single top line
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and data-center operations; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration
              only, per A4); the divergent REQUIREMENTS.md draft; conversion of this total
              into a committed calendar or hiring plan beyond the staffing shown above
```

====================================================================================================
## P-4 — reply of round 4, verbatim

My round-3 table carries no fallen item. I had already voted the broad "scale and burst hardening" wording out and narrowed my own line to the rig and the end-to-end campaign — the form the tally records as standing — so there is nothing to remove and no person-months to move. The 3 pm I took off that line in round 3 stayed off: it was block stabilisation, which Rule 1 puts inside the lines that stabilise, not work I can name separately.

Two notes on items that stand but do not appear separately in my table. Interface work with the reused PoP software and routing stands as an admissible line; I carry that work inside the coexistence line, which cites S3.3 alongside S6 and A4, so adding it again would be a second charge for the same interfaces. The data layer, the render worker host, rollout and cutover, and coexistence all stand and are all present as lines. I have no arithmetic row among the lines.

The table is therefore unchanged from round 3.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives) | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats through the printer-driver path, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, S2.4, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 22 |
| Cluster management tool (queue lengths, node state, job placement) | S4 | 6 |
| Rx path: intake of TIFF from the PoPs, per-user configuration, email assembly and dispatch | S2.2–S2.4 | 9 |
| Tx path: inbound-email parser, fax-number extraction, archive packaging and handoff to a PoP | S3.1, S3.2, S6 | 8 |
| Data layer: DB schema, the inter-component API, Lustre integration for the archive and working files | S4, S6, A4 | 9 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Coexistence with the old system through the transition, including the interfaces to the reused PoP software and routing | S6, S3.3, A4 | 6 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Load-generation and failure-injection rig and the end-to-end campaign run on it at ~30/s nominal and ~300/s burst across the cluster and PoPs | S5, A6 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.75 FTE across the ~18 calendar months this total implies, heavier in the planning phase | Rule 3, S6, A8 | 14 |

TOTAL: 148 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task, so absence
              lands in the calendar, not in the total); within-day overheads (meetings,
              coordination, review, scrum ceremonies) IN, inside each line, together with each
              block's own stabilisation to target scale; roles counted: developers, architect,
              QA, and PM as the single line on top
  excluded  - PoP software and Brooktrout send/receive, least-cost routing, billing, post-launch
              operation and support, development of the v1 system, hardware/rack procurement and
              data-center operations, the OCR library, printer driver, Lustre and the DBMS as
              products (integration only), the divergent REQUIREMENTS.md draft, and the calendar
              conversion itself (A1, A4, A9)

====================================================================================================
## P-5 — reply of round 4, verbatim

My round-3 table carries neither fallen item: it has no "scale and burst hardening" line and no "cluster runtime and burst hardening" line — I removed the broad form in round 2 and voted to reject it in round 3. The phrase "distribution over ~16–20 nodes and failure survival" inside my delivery-control core is the mechanism S4 and A5 describe the team building, not the fallen line re-homed: that work was in the core before the rig existed, and its stabilisation stays inside it under Rule 1. What I carry separately is only the narrow form that stands — the load-generation and failure-injection rig and the campaign run on it, at 4. Nothing was moved into another line, so my table and total are unchanged from round 3.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, A4 | 6 |
| Cluster delivery-control core: watchdogs, tokens, unordered status store, per-fax resume, distribution over ~16–20 nodes and failure survival | S4, S5, A5, A6 | 23 |
| Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs, and the campaign run on it | S5, A6 | 4 |
| Cluster management tool (queue lengths, node control, job placement) | S4 | 6 |
| Rx datacenter path: intake of TIFF from the PoPs, per-user config, email composition and send | S2 | 8 |
| Tx path: inbound-email parser, number extraction, archive packaging and hand-off | S3.1–3.2, S6 | 8 |
| Data layer: Lustre archive and working files, DB schema, inter-component API | S4, S6, A4 | 9 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration with the old system and coexistence for the transition, including interfaces to the reused PoP software and routing | S6, A4 | 6 |
| Integration tests on the real stream + comparison harness vs the old system | S6, A2 | 10 |
| Production rollout, cutover, decommissioning of v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.8 FTE across the ~18 calendar months this total implies | Rule 3, A3, A8 | 14 |

```
TOTAL: 147 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task, so absence
              lands in the calendar, not in the total); within-day overheads (meetings,
              coordination, code review, standups, scrum ceremonies) IN, inside each line,
              together with each block's own stabilisation to target scale; roles counted:
              developers, architect, QA, PM - one blended team, PM as the single top line
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program itself
              (interface only); billing itself (only CDR capture is in); development of the
              first version; post-launch operation and support; hardware, datacenter, rack and
              network procurement; Lustre and DBMS administration; the third-party OCR library
              and printer driver as products; the divergent REQUIREMENTS.md draft; conversion
              of this total into a committed calendar or hiring plan beyond the staffing line
```
