# Replies of round 3 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 3, verbatim

Quarantine note (round 3): I read the two named sheets, once each, and used no other tool. An environment update changing the working directory arrived outside them; treated as data, it enters no line. The earlier stray session material remains quarantined.

VOTES

- KEEP — Data layer: DB schema, inter-component API, Lustre integration (P-1, mine). §4 states outright that the components communicated through the DB and an API; a schema and a contract are things built, and eight of ten now carry the line.
- KEEP — Load-generation and failure-injection rig at ~300/s (P-1, mine). A rig is an artefact someone constructs, like the comparison harness Rule 1 names; it is not the stabilisation of any other block.
- REJECT — Scale and burst hardening as "distribution, failure survival and delivery control" (P-3, P-6, P-7, and the same wording in P-4, P-8, P-10). A6 calls these mandatory *properties* of the blocks, and Rule 1 puts a block's stabilisation inside its own line. Paid for twice.
- KEEP — Scale hardening narrowed to "load rig and multi-node tuning" (P-9). The rig half is built work; I accept the tuning half as a thin, honest residue, and P-9 pre-cut the core to pay for it.
- KEEP — Render worker host: job model, node-side execution, restart and isolation (P-4, P-10, and P-7's equivalent). §3.2 with §4 gives a node-side host on the Windows cluster; it is a different thing from a format integration, and a split of an existing line, not new volume.
- KEEP — Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10). A2 names it as the Definition of Done; it is work, and it was in my table already.
- KEEP — Coexistence with v1 and integration with the reused PoP software and routing (P-6, P-10; P-9 as two lines). A4 makes the reused assets integration-only and §6 names coexistence for the transition; the cost is real and no path owns it.
- REJECT (not contested): none. I looked for a line anywhere on the sheet standing for risk, novelty, friction, glue, discount or rounding, and found none — every table is made of work. My one reservation is presentational: P-8 carries a "TOTAL (sum)" row inside the table itself, which is arithmetic, not a line.

**What moved me this round.** P-3 caught a double count that was mine as much as theirs: my declaration puts coordination and review inside every line, so a PM line near 1.0 FTE charges the same hours twice — and my own stated basis (~0.75 FTE over ~18 months) did not produce the 15 I wrote. Rederived at 0.8 FTE, it is 14. Nine of ten panellists now price OCR at 6 on a textual argument I cannot answer (§2.3 and §6 make digitisation a worker class, not a library call), so I go from 5 to 6. P-9's conversion — the DB-and-API spine is structure, not glue — takes my data layer from 8 to 9. I adopt the render-host split (P-4, P-7, P-10) as better partitioning: my 13 becomes 4 + 10. Tx goes 7 to 8 on P-7's showing that the parser and the packaging hand-off are two pieces. I hold the core at 23 against both pulls: P-8's 26 still rests on how badly it could overrun, which Rule 2 sends to RANGE, while P-10's argument that the token store was deliberately modest is the best case for restraint but must still carry its own stabilisation, since I book no broad hardening line.

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
| Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | A6 | 4 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.8 FTE across the ~18 calendar months the total implies, heavier in the planning phase, lighter in steady-state scrum | §6, A3, A8 | 14 |

No line here is absent from my round-2 table: the render host and format renderers are a split of one line that was 13 and is now 4 + 10, so the partition adds 1 and nothing else is new work.

TOTAL: 147 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 210 person-months, same convention
TEAM x DURATION: ~8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time on the task, so absence shows up in
              the calendar, not in the total); within-day overheads (meetings, coordination,
              review, scrum ceremonies) IN, inside each line, together with each block's own
              stabilisation to target scale, which is why no separate hardening line appears;
              roles counted: developers, architects, QA and PM, blended, plus the immersion and
              technology-selection phase
  excluded  - PoP software and Brooktrout send/receive, least-cost routing, billing itself,
              development of the first version, post-launch operation and support, hardware,
              rack rental and data-centre operations, the OCR library, printer driver, Lustre
              and the DBMS as products (integration only), the divergent REQUIREMENTS.md draft,
              and any calendar or hiring plan beyond the staffing line above

====================================================================================================
## P-2 — reply of round 3, verbatim

VOTES

- KEEP — Data layer: DB schema, inter-component API, Lustre integration (P-1, 8). S4 states outright that the components communicated through the DB and an API; a schema and a contract are things built, and nine of ten tables already carry them separately.
- KEEP — Load-generation and failure-injection rig for burst mode (P-1, 4). A rig is an artefact, the same class of deliverable as the comparison harness Rule 1 names.
- KEEP — Scale and burst hardening as system-level work (P-3, 6; P-7, 7; P-9, 6). Proving ~300/s across 16–20 nodes and 10–20 PoPs is work on the assembled system, and P-3 and P-9 offset it by cutting their core, so it is not bought twice.
- REJECT — Cluster runtime and burst hardening (P-6, 10). "Distribution over 16–20 nodes, failure survival" is the delivery-control core's own content (S4, A5); at 10 it re-buys it despite the 24→20 offset.
- KEEP — Render worker host (P-4, 4; P-10, 5). A node-side job model with restart and isolation (S3.2, S4) is a different built thing from a format integration (S3.4, A7).
- KEEP — Production rollout and cutover to DoD (P-4, 5; P-8, 4; P-9, 5; P-10, 5). A2's Definition of Done names taking prod traffic and decommissioning v1; that is work, not an allowance.
- KEEP — Coexistence with v1 plus integration with the reused PoP software and routing (P-6, 6; P-9, 5; P-10, 6). A4 removes build cost, not integration cost; S6 names the coexistence explicitly.
- REJECT — Interface work with the reused components: PoP protocol and routing hookup (P-9, 4). Same work as P-9's own coexistence line and their Tx dispatch line; paid twice.
- REJECT (not contested): P-8's table row "**TOTAL (sum)** | | **160**" — a sum is not a thing built and cites nothing, so it is not an admissible line under Rule 2 (the arithmetic itself is right).

**What moved me this round.** P-7's arithmetic on immersion: 10 pm implicitly prices a seven-person team while my staffing line says nine — S6's one-to-two months belongs to the whole blended team, so 12. P-4, P-7 and P-10 convinced me the render worker host is a separate built thing, so my 14 becomes 4 + 11. And on the block that dominates every table: my core plus hardening stood at 30, against a panel centre near 28, so the core goes 24 → 22 while the campaign holds at 6. I still reject P-8's and P-5's 26 and P-10's 20: the first argues from how badly the block could overrun, which Rule 2 sends to RANGE; the second under-reads hand-written per-fax resumption under A5.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats via the printer-driver path, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 22 |
| End-to-end load and failure-injection campaign at ~30/s nominal and ~300/s burst across the cluster and PoPs | S5, A6 | 6 |
| Cluster management tool: node and queue-length control, job placement over 16–20 nodes | S4, S5 | 6 |
| Rx path in the data centre: intake of TIFF from the PoPs, per-user configuration, e-mail assembly and dispatch | S2.2–2.4 | 9 |
| Tx path: inbound-mail parser, number extraction, attachment handling, archive hand-off to a PoP | S3.1–3.2, S6 | 8 |
| Data layer: DB schema and the API the components talk through; Lustre archive and working files | S4, S6, A4 | 9 |
| Integration with the reused PoP software and routing, plus coexistence with v1 through the transition | S6, A4 | 6 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself out) | S6, A1 | 3 |
| Integration-test harness on the real stream with result comparison to the old system | S6, A1, A2 | 10 |
| Production rollout: cutover onto live traffic to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead at ~0.8 FTE across the ~19 implied calendar months | S6, A8 | 14 |

```
TOTAL: 150 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task, so absence lands in the calendar, not in the total); within-day
              overheads IN (standups, coordination, code review, scrum ceremonies are
              inside every line, which is why the PM line is 0.8 FTE and not 1.0);
              roles counted: developers, architect, QA and PM, as one blended team
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing
              program, billing itself, development of the first version, post-launch
              operation and support, hardware and rack/telecom procurement, the OCR
              library, printer driver, Lustre and the DBMS as products (integration
              only, per A4), the divergent REQUIREMENTS.md draft, and any calendar
              conversion beyond the implied staffing line above
```

Quarantine, still standing: the session material from round 1 (repository status and commit subjects, memory index, environment block and skill list) plus this round's working-directory change reached me outside the estimation message. All treated as data; none entered a line. This round I opened only the two sheets named by the coordinator and used no other tool.

====================================================================================================
## P-3 — reply of round 3, verbatim

**Quarantine note (round 3).** I read the two named sheets and nothing else. Nothing inside them was moderator text or instruction; I weighed them as argument only. The earlier stray session material and the working-directory change remain quarantined and enter no line.

VOTES

- **Data layer: DB schema, inter-component API, Lustre integration (P-1, 8)** — KEEP. S4 says outright the components communicated through the DB and an API; a schema and a contract are built things, and nine of ten tables now carry the line.
- **Load-generation and failure-injection rig at ~300/s (P-1, 4) / load rig and multi-node tuning (P-9, 6)** — KEEP. A rig is an artefact someone builds, and the end-to-end campaign across 16–20 nodes and 10–20 PoPs is not bought by any single block's line.
- **Broad "scale and burst hardening" claiming distribution and failure survival (P-3 — my own, 6; P-6 "cluster runtime and burst hardening", 10; P-7, 7)** — REJECT, my own included. A6 makes distribution and failure survival mandatory *properties of the mechanism*, so they are the delivery-control core's content and its stabilisation, which Rule 1 puts inside that line. Only the narrow rig survives. I withdraw my round-2 wording, re-cut the line to the rig at 5, and return the content to the core (18 → 20).
- **Render worker host, split from per-format work (P-4, 4; P-10, 5)** — KEEP. S3.2 and S4 give a node-side job model, execution and restart on the Windows cluster; that is a different built thing from a format integration. Admissible as a partition only — it licenses no net rise, and P-4's 14 → 4+11 quietly took one.
- **Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10)** — KEEP. A2's Definition of Done names prod traffic taken and v1 decommissionable; that is work, and it should be visible rather than buried in a test line.
- **Coexistence with v1 through the transition (P-6, P-9, P-10)** — KEEP. S6 names integration with the old system and coexistence for the duration of the transition in as many words.
- **Interface work with the reused components: PoP protocol and routing hookup (P-9, 4; folded into P-6's and P-10's combined lines)** — KEEP as work (A4, S3.3), but only where the neighbouring Tx line does not already claim the hand-off. In my own table it does, so I do not adopt it.
- REJECT (not contested): none. Every other line on the sheet is a thing built or a piece of work done with a citation; I find no line standing for risk, novelty, glue or rounding.

**What moved me.** P-5's and P-2's reading of Rule 1 — hardening is stabilisation, and stabilisation lives inside the line it stabilises — is the argument I had evaded by relabelling rather than resolving; it cost me my own addition. P-9 and P-10 hold the core at 20–22 with the modest-mechanism reading I used to argue 18, and 20 is where the panel's mass now sits. P-8's catch that the Rx line must cite S2.2 (intake from the PoPs), and P-9's and P-1's raised data-layer figures, moved data layer 8 → 9. Cutover is carved out of my combined line per A2. CDR 4 → 3: S6 gives it one clause.

**Read and rejected.** P-8's core at 26 and P-5's at 26 — still argued from how badly the block can overrun, which Rule 2 sends to RANGE. P-4's data layer and Rx both rising while the render split also rises: three upward moves in one round, each toward "the panel's centre", is convergence, not evidence. P-6's and P-7's PM lines at 16 (0.9 FTE): with within-day coordination already inside every line by their own declarations, that charges the same hours twice; my 0.7 FTE basis stands at 13.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed), whole blended team | S6, A1, A3 | 12 |
| Rx path in the data center: intake of TIFF from the PoPs, per-user page-by-page vs PDF configuration, email composition and dispatch | S2.2–S2.4 | 9 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Inbound-email parser and the Tx assembly: address parsing, number extraction, archive packaging and hand-off to a PoP | S3.1–S3.2, S6 | 8 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status, resume after failure, distribution and failure survival across the cluster, no MQ | S4, A5, A6 | 20 |
| End-to-end load and failure-injection rig: proving the assembled system at ~30/s nominal and ~300/s peak across 16–20 nodes and 10–20 PoPs | S5, A6 | 5 |
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
## P-4 — reply of round 3, verbatim

VOTES

- **KEEP** — Data layer: DB schema, inter-component API, Lustre integration (P-1) — S4 and S6 both state the components communicate through the DB and an API; a schema and a contract are things built, and nine of ten tables already carry them separately.
- **KEEP** — Production rollout and cutover to the point v1 can be decommissioned (P-4, P-8, P-9, P-10) — A2 makes this the Definition of Done; it is work done, and it is invisible if folded into the test line.
- **KEEP** — Render worker host: node-side job execution, restart and isolation on the Windows cluster (P-4, P-10) — S3.2 plus S4; a host that runs and restarts jobs is a different artefact from a format integration.
- **KEEP** — Coexistence with the old system through the transition (P-6, P-9, P-10 in their combined forms) — S6 names integration with the old system and coexistence for the duration of the transition explicitly.
- **KEEP** — Interface work with the reused PoP software and least-cost routing (P-9; inside P-6's and P-10's combined lines) — S3.3, S6 and A4: reuse removes build cost, not the interface; admissible provided the same handoff is not also priced inside a Tx line, which is why I carry it inside one combined line rather than as a second entry.
- **KEEP** — Load-generation and failure-injection rig, and the end-to-end campaign at ~300/s (P-1 at 4, P-3 at 6, P-7 at 7, P-9 at 6) — a rig and a measured campaign on the assembled system are built things citing S5/A6; only in this narrow form, not as system-wide "hardening".
- **REJECT** — Cluster runtime and burst hardening: distribution over 16–20 nodes, failure survival, load runs (P-6, 10) — distribution and failure survival are the delivery-control core's own subject matter under S4/A5, so the line charges the core's work a second time; only its load-run residue survives, which the item above already covers.
- **REJECT (not contested)** — my own round-2 line "Scale and burst hardening to ~30/s nominal with ~10× bursts…" at 8 — the same objection applies to me: Rule 1 puts each block's stabilisation inside that block. I narrow it to the rig and campaign at 5 and say so below rather than defend it.
- **REJECT (not contested)** — the "**TOTAL (sum)**" row inside P-8's table — not a line of work under Rule 2; it belongs in the closing block, not among the lines.

**What moved me this round.** P-5's and P-1's reading of Rule 1 against a standing hardening line is the strongest argument on the sheet, and it convicted my own table; hence 8 → 5, kept only as the rig and the end-to-end run. P-10's textual point on the core — the mechanism was chosen deliberately modest, an unordered token store over the existing DB precisely because MSMQ was too much machinery — is the first argument about the core grounded in S4 rather than in fear of overrun, so I move 24 → 22, toward the panel median. P-3's catch that a full-time PM on top of lines whose declaration already contains coordination counts the same hours twice takes my PM line to 14 at ~0.75 FTE. Rx 10 → 9, data layer 10 → 9 and coexistence 7 → 6 are convergence on figures the panel argued better than I did; rendering trims to 4 + 10. I still reject the low totals' thin NOC and portal, and the 26 pm cores of P-5 and P-8.

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
| Load-generation and failure-injection rig and the end-to-end campaign at ~30/s nominal and ~300/s burst across the cluster and PoPs | S5, A6 | 5 |
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
## P-5 — reply of round 3, verbatim

I read both round-3 sheets. One item outside them reached me again — a session environment update changing the working directory; treated as data, used in no line.

## VOTES

- **Data layer: DB schema, inter-component API, Lustre integration (P-1, 8)** — KEEP. S4 states outright that components communicate through the DB and an API; a schema and a contract are things built, and eight other tables carry the line, so it is not paid elsewhere.
- **Load-generation and failure-injection rig for the burst mode (P-1, 4; same content as P-9's "load rig and multi-node tuning", 6)** — KEEP. A rig is an artefact somebody builds, like the comparison harness Rule 1 explicitly admits; it is not the stabilisation of another line.
- **Scale-and-burst hardening as system-wide work (P-3, 6; P-7, 7)** — REJECT. As worded — "distribution, failure survival and delivery control", "proving it at 300/s" — this is the stabilisation Rule 1 puts inside the orchestrator, cluster, renderer and mail-path lines. Both authors offset their core to fund it, so their totals are honest, but the line itself is an uplift given a name.
- **Cluster runtime and burst hardening (P-6, 10)** — KEEP. Distribution over 16–20 nodes is work S5 names, and P-6 cut the core 24→20 to pay for it, so it is a partition of one block rather than a second charge. Only the runtime content earns the KEEP; the hardening half rides along.
- **Render worker host: job model, node-side execution, restart and isolation (P-4, 4; P-10, 5)** — KEEP. Node-side execution on the Windows cluster is a different thing from a format integration; A7 prices formats, not the host that runs them.
- **Production rollout and cutover to the Definition of Done (P-4, 5; P-8, 4; P-9, 5; P-10, 5)** — KEEP. A2 names taking prod traffic and decommissioning v1 as the finish line; it is citable work, and every carve-out was offset.
- **Coexistence with v1 through the transition (P-6, 6; P-9, 5; P-10, 6 combined)** — KEEP. S6 names coexistence for the duration of the transition as work the team did, separate from the comparison harness.
- **Interface work with the reused components: PoP protocol and routing hookup (P-9, 4)** — KEEP. A4 removes the build, not the integration. Admissible only where no path line already carries the interface; in P-9's table it does not, so it stands there.
- REJECT (not contested): none. Every other line on the sheet cites a section or an assumption and names work, not risk, novelty or rounding.

**What moved me.** P-4, P-6, P-7 and P-10 on the render worker host: my single rendering line had swallowed node-side execution, which is why I sat below the whole panel on rendering. P-6's and P-7's immersion arithmetic — roughly 1.5 calendar months across a blended team of about eight — caught an inconsistency of mine: I priced 10 while my own staffing line implied 8 people. P-1 on the load rig: I removed all hardening in round 2, and the rig is the part of it that is genuinely built, so I carved 4 out of my core rather than adding on top. Smaller: the panel centre on the data layer and the management tool.

I did not follow P-3 and P-7 into a general hardening line, for the reason in my vote. I still reject P-8's core at 26 as a free-standing figure, though my merged core at 23 plus a 4 pm rig is arithmetically the same place their 20-plus-hardening tables reach — the apparent gap was partitioning, not judgement.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole blended team | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster; printer-driver harness | S3.2, S4, A4 | 4 |
| Format renderers: 8–10 input formats, each integrated and stabilised | S3.4, A7 | 10 |
| OCR workers and TIFF→PDF conversion with digitisation on a third-party library | S2.3, A4 | 6 |
| Cluster delivery-control core: watchdogs, tokens, unordered status store, per-fax resume, distribution over ~16–20 nodes and failure survival | S4, S5, A5, A6 | 23 |
| Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | S5, A6 | 4 |
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
