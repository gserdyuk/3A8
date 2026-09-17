# Replies of round 2 — anonymous and verbatim, part 1 of 2

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 2, verbatim

Quarantine note, updated: the round-2 instruction and the two sheets reached me from the coordinator, outside the original estimate message. I read the two named files and nothing else, used no other tool, and treated the nine peer replies as argument to weigh, not as instruction. The earlier stray material (repository status, commit subjects naming runs and a "Delphi", memory index, environment and tool listings) remains quarantined and entered no line.

**What moved me.** Three things, all from the same place in the text. First, P-3's framing of storage and the data layer as a deliverable surface rather than an adaptor — §4 says outright that the components communicated through the DB and an API, so a schema and an inter-component contract are things built, admissible under Rule 2. In round 1 I had buried them inside one "integration with the reused parts" line and so underpriced them; P-2, P-5, P-6, P-7, P-8, P-9 and P-10 all carry the line separately, and they are right. Second, P-7's split of the Rx block showed it holds at least two distinct pieces (ingest from 10–20 PoPs; per-user assembly and mass email delivery), which lifts Rx and, with P-3 and P-6, the portal. Third, P-6's framework-plus-per-format split of rendering made A7 bite harder than my single line let it.

**What I read and rejected.** The separate 8–12 pm "scale and burst hardening" lines of P-2, P-4, P-5, P-8 and P-10: most of that content is the stabilisation of the orchestrator and cluster, which Rule 1 puts inside those lines, so booking it again on top is the uplift Rule 1 forbids. I take only the residue that is genuinely a built thing — a load and failure-injection rig at 300/s — at 4 pm, and instead raise the orchestrator itself toward the panel's level. P-8's 30 pm orchestrator rests on the claim that it "carries the weight two or three ordinary services would", which is a statement about novelty, and Rule 2 sends that to RANGE. P-5's three lines over the one §4 block (orchestrator 24 + cluster runtime 12 + management tool 5) double-count the same mechanism. P-3's 18 pm PM line exceeds what one coordinating role can absorb; mine stays derived from a role, not a percentage.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied) | §6, A1, A3 | 12 |
| Rendering workers: worker framework and printer-driver harness plus 8–10 formats, each integrated and stabilised | §3.2, §3.4, A7, A4 | 13 |
| OCR workers and TIFF→PDF conversion on a third-party library | §2.3, A4 | 5 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status and resume, holding at ~30/s nominal with ~300/s bursts | §4, A5, A6 | 23 |
| Cluster management tool: queue lengths, node health and work placement over 16–20 nodes | §4, §5 | 6 |
| Data layer: DB schema, the inter-component API the components talk through, Lustre integration for the fax archive and working files | §4, §6, A4 | 8 |
| Rx path in the data centre: intake of TIFF from 10–20 PoPs, per-user page-by-page vs PDF configuration, email assembly and mass delivery | §2.2–2.4 | 8 |
| Tx path: inbound-email parser, fax-number extraction, attachment handling, archive packaging and hand-off | §3.1–3.2, §6 | 7 |
| NOC internal control centre: state of the remote PoPs, the cluster and the queues | §4, §6 | 9 |
| User portal | §4, §6 | 10 |
| CDR and billing-data capture (billing itself out) | §6, A1 | 3 |
| Integration with the reused PoP software and least-cost routing, and coexistence with v1 through the transition | §6, A4 | 6 |
| Integration tests on the real stream and the comparison harness against the old system | §6, A1, A2 | 10 |
| Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | A6 | 4 |
| Rollout to production traffic and readiness to decommission v1 | A2 | 5 |
| Project management and coordination (one line): one PM/scrum lead at ~0.75 FTE across the ~18 calendar months the total implies, plus release coordination | §6, A3, A8 | 15 |

ADDED
- Data layer: DB schema, the inter-component API the components talk through, Lustre integration for the fax archive and working files | §4, §6, A4 | 8
- Load-generation and failure-injection rig for the burst mode (~300/s) across the cluster and the PoPs | A6 | 4

TOTAL: 144 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 205 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time on the task, so absence shows up in
              the calendar, not in the total); within-day overheads (meetings, coordination,
              review, scrum ceremonies) IN, inside each line; roles counted: developers,
              architects, QA and PM, blended, plus the immersion and technology-selection phase
  excluded  - PoP software and Brooktrout send/receive, least-cost routing, billing itself,
              development of the first version, post-launch operation and support, hardware,
              rack rental and data-centre operations, the OCR library, printer driver, Lustre
              and the DBMS as products (integration only), and any calendar conversion beyond
              the staffing line above

====================================================================================================
## P-2 — reply of round 2, verbatim

**What moved me, and what I did not take**

P-1, P-3, P-6, P-7 and P-9 all price the cluster management tool at 4–8 and carry no separate hardening line; P-3 puts the reason plainly — A6's burst resilience and failure survival are mandatory properties of the blocks themselves, so under Rule 1 their stabilisation is already inside the orchestrator, cluster and rendering lines. That is the one place my round-1 table double-counted. I kept a hardening line, but narrowed it to what is genuinely separate work — the end-to-end load and failure-injection campaign across the whole cluster — and cut it from 10 to 6. My management tool falls from 10 to 6 for the same reason: it is an internal queue-and-node console, and I was the panel's outlier.

P-10 and P-7 also argue the orchestrator down to 18. I did not follow: seven of ten panellists sit at 20–30, and A5 plus per-fax resumption at 300/s justifies 24. I rejected P-8's 30 on the same footing.

P-9's 106 and P-1's 120 rest on small NOC, portal and data-layer lines. I trimmed portal 12→10 and data layer 10→9 toward the panel median, but the "live v1 as executable requirements" argument (P-9, P-10) removes discovery, not construction, so I would not go further.

Net: 165 → 148.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), whole team | S6, A1, A3 | 10 |
| Rendering workers: worker framework + 8–10 formats integrated and stabilised via the printer driver | S3.4, A7 | 14 |
| OCR workers and TIFF→PDF conversion on a third-party library, per-user page-by-page vs PDF | S2.3, A4 | 6 |
| Delivery-control core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 24 |
| Cluster management tool: node and queue-length control, job placement over 16–20 nodes | S4, A6 | 6 |
| Rx path in the data centre: intake of TIFF from PoPs, user configuration, e-mail assembly and dispatch | S2.2–2.4 | 8 |
| Tx path: inbound-mail parser, number extraction, attachment handling, archive hand-off to a PoP | S3.1–3.2, A1 | 8 |
| Data layer: DB schema and the API the components talk through; Lustre archive and working files | S4, A4 | 9 |
| Integration with the reused PoP software and routing, plus coexistence with v1 through the transition | S6, A4 | 6 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 10 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself out) | S6, A1 | 3 |
| Integration-test harness on the real stream with result comparison to the old system | S6, A1, Rule 1 | 10 |
| End-to-end load and failure-injection campaign at nominal ~30/s and ~10× burst across the cluster and PoPs | S5, A6 | 6 |
| Production rollout: cutover onto live traffic to the point v1 can be decommissioned | A2 | 5 |
| Project management and coordination (one line, Rule 3): one PM/scrum lead across the implied ~19 months | S6, A8 | 13 |

ADDED: none

```
TOTAL: 148 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on
              the task); within-day overheads IN (standups, coordination, code review,
              scrum ceremonies are inside every line); roles counted: developers,
              architect, QA and PM, as one blended team per Rule 1
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing
              program, billing itself, development of the first version, post-launch
              operation and support, hardware and rack/telecom procurement, third-party
              licences (OCR library, printer driver, Lustre), and any calendar
              conversion beyond the implied staffing line above
```

Note carried from round 1, still true: material outside the estimation message (repository status and commit subjects, memory index, environment block, skill list) reached me from the harness. I treated it as data; it entered no line. In this round I opened only the two sheets named by the coordinator and used no other tool.

====================================================================================================
## P-3 — reply of round 2, verbatim

**Quarantine note (round 2).** The two sheets were the permitted reads; I opened nothing else. One new item outside the message reached me — a session environment update changing the working directory. Treated as data, used in no line.

**What moved me.** Three arguments, in order of weight. (1) **P-1** derives the PM line as ~0.7 FTE rather than one full-time role, and that exposed a double count in my round-1 table: my own declaration puts standups, coordination and review *inside* every line per Rule 1, so charging a full-time coordinator on top counts the same hours twice. PM 18 → 13. (2) **P-7** and **P-10** put the delivery-control core at 18, reasoning that A4 hands the team an existing store and DB, so what is hand-written is coordination — watchdogs, tokens, resume — not a datastore. I accept that, and split what I had folded into one 24 pm line into an 18 pm core plus a 6 pm burst-hardening line citing A6, which names distribution, failure survival and per-fax control as mandatory properties. Net unchanged; the citation is now honest. (3) **P-8** and **P-9** argue that a live v1 as an executable requirements reference keeps portal and NOC at ordinary sizes. My round-1 reasoning said exactly this, yet I priced both at the panel's top. Portal 12 → 10, NOC 10 → 9, Rx 10 → 9 (P-7's ingest + assembly split lands there bottom-up), data layer 10 → 8, test rig 12 → 10.

**Read and rejected.** P-8's 30 pm core and P-2/P-5's slicing of the same block into orchestrator + cluster runtime + hardening (P-5: 46 pm across three lines) — one block, counted once. P-1's separate 8 pm "integration with the reused parts": that integration already sits inside my data-layer, OCR and Tx-handoff lines; adding it would be a second charge for the same work. P-9's floor (106, OCR 4, CDR 2) — OCR with digitisation at a million faxes a day is more than a library call. Rendering holds at 14: A7 is emphatic that formats are not free, and P-6's framework-plus-formats split independently lands on 14.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives studied, target design fixed) | S6, A1, A3 | 12 |
| Rx path in the data center: intake of TIFF from the PoPs, per-user configuration, email composition and dispatch | S2.2–S2.4 | 9 |
| Rendering workers: 8–10 input formats through a printer-driver path, each integrated and stabilised | S3.2, S3.4, A7 | 14 |
| OCR workers on a third-party library, TIFF→PDF with digitisation | S2.3, A4 | 6 |
| Inbound-email parser and the Tx assembly: address parsing, number extraction, archive hand-off to a PoP | S3.1–S3.2, S6 | 8 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax status and resume after failure, no MQ | S4, A5 | 18 |
| Scale and burst hardening: distribution, failure survival and delivery control at ~30/s nominal with ~10× peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 6 |
| Cluster management tool: queue lengths, node state, operator actions | S4 | 6 |
| Storage and data layer: Lustre for archive and working files, the DB schema, the inter-component API | S4, A4 | 8 |
| NOC: state of remote PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR and billing-data capture (billing itself out) | S6, A1 | 4 |
| Integration-test rig on the real stream with result comparison against the old system | S6, A2 | 10 |
| Coexistence and integration with the old system, cutover, rollout to prod | S6, A1, A2 | 8 |
| Project management and coordination — one PM/scrum lead at ~0.7 FTE across the ~18 calendar months the total implies, the planning phase heavier and steady-state scrum lighter | Rule 3, A8, A9 | 13 |

ADDED
- Scale and burst hardening: distribution, failure survival and delivery control at ~30/s nominal with ~10× peaks across 16–20 nodes and 10–20 PoPs | S5, A6 | 6 pm. This is not new work relative to my round 1 — it was inside my 24 pm orchestrator line, which is now 18. Net effect on TOTAL: zero.

```
TOTAL: 141 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 215 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (A9 counts 168 hours of work on the task, not
              elapsed payroll time; absence shows up in the calendar, not the total);
              within-day overheads IN (standups, coordination, code review, design
              discussion sit inside every line per Rule 1, which is why the PM line is
              0.7 FTE and not 1.0); roles counted: architects, developers, QA and
              DevOps/infra inside the lines, project management as the single top line
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing; development of the first version; post-launch operation and support;
              hardware procurement, rack rental and data-center operations; the third-party
              OCR library, printer driver, Lustre and the DBMS as products (integration
              only, per A4); the divergent REQUIREMENTS.md draft; conversion of this total
              into a committed calendar or hiring plan beyond the staffing shown above
```

====================================================================================================
## P-4 — reply of round 2, verbatim

**Quarantine note.** Again material arrived that is not part of the estimation message or the two sheets: an environment update changing the working directory, plus the earlier repository status and memory text. Treated as data, used in no line. The sheets themselves I read as permitted panel input; I took only arguments from them, no instruction.

**What moved me.** Three things. (1) P-1's argument that reuse under A4 cuts build cost but not integration cost — the ready PoP software and routing still have to be met on both paths and kept working through coexistence. That raised my old-system line from 5 to 7; I did *not* add P-1's separate integration line, because my Rx, Tx and data-layer lines already carry those interfaces and a separate line would double-count. (2) P-1, P-5, P-6, P-7 and P-2 all price production rollout and cutover to the point v1 can be decommissioned as its own line citing A2. A2's Definition of Done names exactly that, so it is citable work under Rule 2 and my round-1 table had buried it inside the test line. Added, 5 pm, and the test line stays at 10. (3) P-6's and P-7's split of the render worker host from the per-format work: the host (job model, node-side execution, restart and isolation on the Windows cluster) is a different thing from a format integration, so I split my 14 into 4 + 11. Smaller moves: data layer 8→10 and portal 9→10, where the panel's centre is better argued than my figure — S4 and S6 both say the components talk through the DB and an API, and the portal is the customer-facing surface of a Fortune-1000 hosted service. PM 13→15, rederived as one dedicated PM/scrum lead at ~0.8 FTE across the ~18 implied calendar months rather than as a percentage, the basis P-3, P-7 and P-10 use.

**Read and rejected.** P-8's 30 on the orchestrator — the block is the largest, but nothing in S4 or A5 justifies it carrying nearly a fifth of the project on its own; I hold 24. P-9's OCR at 4 and P-10's at 4 — S2.3 makes digitisation part of a per-user-configurable conversion path, not a library call; I hold 6. P-5's separate "cluster runtime" line on top of both the management tool and the orchestrator — distribution and failure survival are what my hardening line (A6) already buys, so it would be the same work twice. P-9's and P-10's totals (106, 118) rest on thin NOC, portal and data-layer lines that I think under-read the breadth in S4/S6; P-2's, P-5's and P-8's (165–168) mostly add the rollout and runtime lines I have now partly taken, so my move is toward them but not all the way.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT and alternatives) | S6, A1, A3 | 12 |
| Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 |
| Format renderers: 8–10 input formats through the printer-driver path, each integrated and stabilised | S3.4, A7 | 11 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, S2.4, A4 | 6 |
| Cluster core: watchdogs + tokens over an unordered store, per-fax status, resume after failure | S4, A5 | 24 |
| Cluster management tool (queue lengths, node state) | S4 | 6 |
| Rx path: intake of TIFF from the PoPs, per-user configuration, email assembly and dispatch | S2 | 10 |
| Tx path: inbound-email parser, fax-number extraction, archive packaging and handoff to a PoP | S3.1, S3.2, S6 | 8 |
| Data layer: Lustre and DB integration, the inter-component API | S4, S6, A4 | 10 |
| NOC: state of remote nodes, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration with the old system and coexistence through the transition, including the interfaces to the reused PoP software and routing | S6, A4 | 7 |
| Integration tests on the real stream with the comparison harness against the old system | S6, A1, A2 | 10 |
| Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 |
| Scale and burst hardening to ~30/s nominal with ~10× bursts across 16–20 nodes and 10–20 PoPs | S5, A6 | 8 |
| Project management and coordination (one line): one dedicated PM/scrum lead at ~0.8 FTE across the ~18 calendar months this total implies | Rule 3, S6, A8 | 15 |

ADDED
- Render worker host: job model, node-side execution, restart and isolation on the Windows cluster | S3.2, S4, A5 | 4 — a split of my round-1 rendering line, which was 14 and is now 4 + 11 = 15
- Production rollout and cutover to the point the old version can be decommissioned | A2 | 5 — previously folded into my test line, which keeps its 10

TOTAL: 158 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 225 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task); within-day
              overheads (meetings, coordination, review, scrum ceremonies) IN, inside each line;
              roles counted: developers, architect, QA, and PM as the single line on top
  excluded  - PoP software and Brooktrout send/receive, least-cost routing, billing, post-launch
              operation, development of the v1 system, hardware/rack procurement and data-center
              operations, the OCR library, printer driver, Lustre and the DBMS as products
              (integration only), and the calendar conversion itself (A1, A4, A9)

====================================================================================================
## P-5 — reply of round 2, verbatim

I read both sheets. Here is my round-2 reply as P-5.

**What moved me.** Two content arguments, not the spread of totals.

P-6's reading of Rule 1 — that long stabilisation belongs inside the line it stabilises, "rather than in an uplift" — applies squarely to my round-1 "Scale and burst hardening" line. Hardening every block to 30/s nominal and ~300/s burst is the stabilisation that Rule 1 already places inside the orchestrator, cluster, Rx and Tx lines. Carried separately it is an uplift wearing a line's clothes. I removed it.

P-1, P-3 and P-9 each fold job distribution and failure survival into the delivery-control line and keep only the management tool beside it. Set against my table, that exposed a genuine overlap: my "Delivery-control orchestrator" and my "Cluster runtime" cited the same S4/A5/A6 material and both claimed per-fax survival across the nodes. I merged them into one core line at 26 rather than 36, since the merge removes duplicated work, not work.

Smaller: P-9 and P-10 on NOC, portal and CDR pulled me down a notch each, on the A3 argument that a live v1 keeps these at ordinary application sizes.

**What I read and rejected.** P-9's total (106) and P-10's (118) rest on OCR at 4 and CDR at 2–3 alongside a data layer at 6; under A4 and A7 integration with a third-party OCR engine and with Lustre is stabilisation work, not a wiring exercise, so I did not follow the low end as a whole. P-8's core at 30 has no more support in the text than my own figure had. P-3's PM at 18 and P-6's at 16 I rejected specifically because I was removing overlap: a coordinator sized off a larger table than mine would smuggle the removed volume back. P-7's finer split of Rx and Tx into five lines I read as presentation, not content — it leaves the sum where it was.

| line | source in the text | person-months |
|---|---|---|
| Domain immersion, architecture and technology selection (DHT etc.) | S6, A1, A3 | 10 |
| Rendering workers: worker framework + 8–10 formats via printer driver | S3.2, S3.4, A7 | 12 |
| OCR workers and TIFF→PDF conversion on a third-party library | S2.3, A4 | 6 |
| Cluster delivery-control core: watchdogs, tokens, unordered status store, per-fax resume, job distribution over ~16–20 nodes and failure survival at 30/s nominal with ~300/s bursts | S4, S5, A5, A6 | 26 |
| Cluster management tool (queue lengths, node control) | S4 | 5 |
| Rx datacenter path: PoP intake, per-user config, email composition and send | S2 | 8 |
| Tx path: inbound-email parser, number extraction, archive hand-off | S3.1–3.2, S6 | 8 |
| Data layer: Lustre integration, fax archive, DB schema, inter-component API | S4, A4 | 10 |
| NOC: state of PoPs, cluster and queues | S4, S6 | 9 |
| User portal | S4, S6 | 10 |
| CDR / billing-data capture (billing itself excluded) | S6, A1 | 3 |
| Integration with the old system and coexistence for the transition | S6, A4 | 6 |
| Integration tests on the real stream + comparison harness vs old system | S6, A2 | 10 |
| Production rollout, cutover, decommissioning of v1 | A2 | 5 |
| Project management and coordination (one line, Rule 3) | A3, A8 | 14 |

ADDED: none.

No line in this table carries work that was absent from my round-1 table. The core line changed scope by absorbing my former "Cluster runtime" line, and my former "Scale and burst hardening" line was removed into the lines whose stabilisation it was; both are subtractions, not additions. The PM line fell from 15 to 14 to stay at ~11 percent of a smaller body of work.

```
TOTAL: 142 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 215 person-months, same convention
TEAM x DURATION: ~8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours are hours worked on the task);
              within-day overheads (meetings, coordination, code review, standups) IN,
              inside each line, together with each block's stabilisation to target scale;
              roles counted: developers, architect, QA, PM - one blended team
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR capture is in); development of the first version;
              post-launch operation and support; hardware, datacenter and network
              procurement; Lustre and DBMS administration; the third-party OCR and
              printer-driver licences (integrated, not built)
```
