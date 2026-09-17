# Replies of round 4 — anonymous and verbatim, part 2 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-6 — reply of round 4, verbatim

My round-3 table carries neither fallen item. I withdrew "cluster runtime and burst hardening" in round 3 myself and replaced it with the narrow rig-and-campaign form that stands; the broad hardening wording appears nowhere in my table, and I have no "TOTAL (sum)" row. Nothing to remove, so the table is unchanged from round 3. The 2 pm I returned to the delivery-control core when I narrowed that line is not a fallen item moved sideways: it is named work that stays inside the core — per-fax status and resumption holding under the ~10× burst — which is precisely where the majority that rejected the broad line said it belongs. RANGE narrows slightly at the top, because three rounds of contest removed the double counting that made my upper end partly a hedge against my own partition; what remains at the top is the hand-written orchestrator overrunning, not bookkeeping.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure, no MQ | S4, A5 | 22 |
| End-to-end load and failure-injection rig and the campaign run on it across the cluster and the PoPs at ~30/s nominal and ~300/s peak | S5, A6 | 6 |
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
RANGE: 110 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on this task,
              so absence shows up in the calendar, not in the total); within-day overheads
              (meetings, coordination, review, scrum ceremonies) IN, inside each line, together
              with each block's own stabilisation to target scale, which is why there is no
              hardening line beyond the rig and its campaign and why the PM line is 0.8 FTE and
              not 1.0; roles counted: architects, developers, QA and PM, per A3/A9, plus the
              immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program (interface
              only); billing; development of the first version; post-launch operation and support;
              hardware, rack rental and data-center operations; the OCR engine, the printer driver,
              Lustre and the DBMS as products (integration only, per A4); the divergent
              REQUIREMENTS.md draft; calendar conversion beyond the staffing line above

====================================================================================================
## P-7 — reply of round 4, verbatim

**Fallen items in my table.** My round-3 table carried no line in either fallen form: the broad "distribution, failure survival and delivery control" wording was what I removed in round 3 myself, and I never had a "cluster runtime" line. What remains is the narrow form that stands — the rig and the campaign run on it. One correction all the same: my wording still said "multi-node tuning", which reaches into the hardening of the blocks that fell. I have cut that phrase and the 1 pm behind it, and I am not moving it into another line, because the work it stood for is the stabilisation Rule 1 already places inside the orchestrator, renderer and mail-path lines. No table row of mine is an arithmetic sum.

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
| Load-generation and failure-injection rig, and the end-to-end campaign run on it at ~30/s nominal with ~300/s peaks | S5, A6 | 5 |
| Cluster management tool: queue depths, node health, work placement over 16–20 nodes | S4, S5 | 6 |
| Data layer: Lustre integration for archive and working files, DB schema, inter-component API | S4, S6, A4 | 9 |
| NOC: state of 10–20 remote PoPs, the cluster and the queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration tests on the real stream with a comparison harness against the old system | S6, A1, A2 | 10 |
| Coexistence and integration with the old system for the transition | S6, A4 | 5 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.75 FTE across the ~18 calendar months this total implies, within-day coordination already inside the other lines | S6, A8, A9 | 14 |

TOTAL: 149 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 220 person-months, same convention
TEAM x DURATION: ~8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task, so absence
              lands in the calendar, not in the total); within-day overheads (meetings,
              coordination, code review, standups, scrum ceremonies) IN, inside each line,
              together with each block's own stabilisation to target scale; roles counted:
              analyst/architect, developers, QA, PM
  excluded  - PoP software and Brooktrout-side code; the least-cost routing program; billing
              proper; development of the first version; post-launch operation and support;
              hardware, rack and data-center procurement; the OCR library, printer driver,
              Lustre and the DBMS as products (integration only); the divergent
              REQUIREMENTS.md draft; conversion of this total into a committed calendar or
              hiring plan beyond the staffing line above

====================================================================================================
## P-8 — reply of round 4, verbatim

My round-3 table did carry one fallen item: my line "End-to-end scale and burst hardening: distribution and failure survival at ~30/s nominal with ~300/s peaks across 16–20 nodes and 10–20 PoPs" (S5, A6, 7 pm) is exactly the broad wording that fell. I have removed it. What stays, and only what I can name, is the item that stands in the narrow form: the load-generation and failure-injection rig for the burst mode and the end-to-end campaign run on it — a built thing, 4 pm. The remaining 3 pm was hardening of the blocks to target scale; the panel is right that Rule 1 already places that inside each block's line, so it goes nowhere and the total falls by 3. I carry no other fallen item, and the "TOTAL (sum)" row is out of the table, where the tally correctly says arithmetic belongs.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers: TIFF→PDF with digitisation on a third-party library | S2.3, S6, A4 | 6 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status and resume after failure, no MQ | S4, A5 | 23 |
| Cluster management tool: queue lengths, node control | S4 | 6 |
| Load-generation and failure-injection rig for the burst mode (~300/s), and the end-to-end campaign run on it across the cluster and the PoPs | S5, A6 | 4 |
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

The seventeen lines sum to 148.

TOTAL: 148 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task, so absence lands in the calendar, not in the total); within-day overheads
              IN (meetings, coordination, code review, scrum ceremonies are inside every
              line, which is why the PM line is 0.8 FTE and not 1.0); each block's own
              stabilisation to target scale IN, inside that block's line, not on top of it;
              roles counted: developers, architect, QA, and PM (PM as the single line under
              Rule 3)
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and PoP deployment logistics; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration only);
              the divergent REQUIREMENTS.md draft; conversion of this effort into a hiring or
              calendar plan beyond the single implied staffing line

====================================================================================================
## P-9 — reply of round 4, verbatim

My round-3 table carries no fallen item. The broad "scale and burst hardening" line and the "cluster runtime and burst hardening" line are both absent — I voted against the first and dropped my own version of it in round 3, and I never carried the second. No person-months were moved anywhere to compensate: the tuning and fixes that the fallen wording covered stay inside the cluster core, the renderers, the data layer and both mail paths, whose lines already include their stabilisation under Rule 1. I carry no "TOTAL (sum)" row either.

Two small adjustments follow from the tally. The rig item stands in the form "the rig with the end-to-end campaign run on it", so my line widens from 4 to 5 to cover building the rig and running the campaign across the cluster and the PoPs; the defects it turns up are fixed inside the blocks that own them, not here. The interface-work line stands for the panel, but I withdrew it in round 3 and do not reinstate it: that work sits in my Rx line (intake from the PoPs) and my Tx line (handoff to the ready routing and PoP), and pricing it twice is what I rejected.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives), target architecture agreed | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on the third-party library, TIFF→PDF with digitisation | S2.3, S2.4, A4 | 6 |
| Cluster core: watchdogs + tokens, unordered status store, resume-after-failure, per-fax delivery control, stabilised to nominal and burst | S4, A5, A6 | 22 |
| Load-generation and failure-injection rig for the burst mode (~300/s), and the end-to-end campaign run on it across the cluster and the PoPs | S5, A6 | 5 |
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

TOTAL: 147 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours actually worked on the task, so
              absence lands in the calendar, not in the total); within-day overheads IN (standups,
              scrum ceremonies, coordination, code review, demos sit inside every line, which is
              why the PM line is 0.8 FTE and not 1.0); each line also carries its own testing and
              its stabilisation to the A6 scale; roles counted: developers, architect/analyst,
              QA, PM — one blended team
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program itself
              (met at its interface only, inside the Tx line); billing; development of the first
              version; post-launch operation and support; hardware, rack and telecom procurement;
              Lustre and the DBMS as products (integration only); the third-party OCR and
              printer-driver licences; the divergent REQUIREMENTS.md draft; conversion of this
              total into a committed calendar or hiring plan beyond the staffing line above

====================================================================================================
## P-10 — reply of round 4, verbatim

**No fallen item appears in my table.** I removed the broad "scale and burst hardening" line myself in round 3 and voted it down; I never carried "cluster runtime and burst hardening"; my table has no "TOTAL (sum)" row.

One disclosure the tally asks for. When I removed my 8 pm hardening line in round 3 I did not discard all of it: 5 pm went to the narrow rig, which stands, and 2 pm went into the delivery-control core (20 → 22). I can name the work that stays there: proving watchdogs, tokens and per-fax resumption hold at nominal and under burst is that mechanism's own stabilisation, which Rule 1 places inside its line and which no other line pays for. The remaining 1 pm was dropped, not relocated. The rig stays at 5 with the end-to-end campaign run on it inside the line, per Rule 1 — the standing form of the item does not make it larger.

The interface work with the reused PoP software and routing stays merged into my coexistence line rather than standing alone, so it is paid once.

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
| Load-generation and failure-injection rig, and the end-to-end campaign run on it at nominal ~30/s and ~300/s burst across the cluster and the PoPs | S5, A6 | 5 |
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

---

**Report on the whole task.** I was P-10 across four Delphi rounds under the three rules, reading only the files permitted in each round (`prompt_rules.txt`, then the R2 and R3 sheets) and using no other tool.

- My total moved 118 → 145 → 150 → 150 person-months. The movement was driven by three arguments, not by anchoring on the panel: reuse cuts build cost but not integration cost (P-1); the render worker host is distinct from per-format integration (P-6, P-7, P-9); and A2's Definition of Done names cutover and coexistence as work my round-1 table had crushed into one line.
- I held against the panel's high end throughout — the 24–30 pm orchestrator — on the grounds that the text describes a deliberately modest mechanism, and against the 15–18 pm PM lines, since Rule 1 already puts coordination inside every line.
- In round 3 I voted down the broad "scale and burst hardening" line, including my own, as the uplift Rule 1 forbids; that item fell 5–10 panel-wide. I kept only the narrow load-and-failure-injection rig, which stands.
- The panel converged from a round-1 spread of 106–168 to 141–160, with my final at 150 near the centre. Every line in my final table cites a section or assumption; nothing stands for risk, novelty or rounding.

====================================================================================================
## CONTESTED ADDITIONS — every "ADDED" block of round 4, copied verbatim under its author's label

(no participant listed an addition)
