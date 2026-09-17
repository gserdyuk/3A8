# Round 3 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 3, verbatim

**What moved me, and what I rejected.**

Three arguments landed, and all three are about *my own bookkeeping* rather than about the system. The panel's round-2 centre (median 145, mean 147) is close to where I already sat, so I checked each move against the question "would I make this if no one else had said it?" before taking it.

- **P-6 and P-10, on a bundled cluster line.** Both diagnosed the identical defect in themselves: a ~30 pm "orchestrator" figure that was quietly reaching into the cluster-management tool and the burst-hardening work, which made it look like a top-of-panel number for a scope that was actually three things. My table has exactly that shape — 30 core *plus* 6.5 tool, with hardening declared to be "inside" the 30, i.e. 36.5 bundled against a panel central mass near 31. Unbundled honestly (24 core + 6 hardening + 5 tool = 35) the figure is checkable and trims 1.5. A6 makes burst survival mandatory, so it deserves a visible line, not a hiding place.
- **P-10, on the per-format rate**, after P-2 and P-8: A7 says each format is real work, not that each format is a small project — once a shared print-driver harness exists, the marginal format is ~1 pm, not 1.5–2. Nine of ten panelists now sit at 11–14 on that block and I was alone at 15. That is a mechanism argument, not a headcount, and I take it: 15 → 13.
- **P-9's self-correction on the QA seam**, with **P-7's** framing of it. P-9 caught themselves sizing blocks as blended deliverables (built *and* tested) and then stacking an uplift priced for a development-only base. My blocks are blended too, and my round-2 DECLARATION explicitly puts defect triage inside them — so part of the 8 pm dedicated-QA line I added last round was paid for twice. I keep the line, because the v1 comparison corpus and the document-pathology set genuinely are additive construction, but I scope it to those and trim to 7. P-7 is also right that this bookkeeping difference, not any disagreement about the system, explains much of the panel's apparent spread.

One thing pushed up: **P-2 and P-6** on deployment across 10–20 remote sites and 16–20 nodes as work my single transition line was not carrying. Coexistence and cutover go 6 → 7.

I also concede a convention point to **P-7**: my 0.8 pm per person-calendar-month double-counted. If meetings, ceremonies and coordination are declared IN as work on the task — as my own declaration says — then the only deduction left in the calendar conversion is genuine absence, roughly 12%. My own text disproved my own rate. I convert at 0.87 now, which shrinks the implied team from 11 to 9.

Read and rejected:

- **P-4's 32% and P-7's 25% QA uplifts** (both landing at 160–165). The premise is right and I have already paid for it; the mechanism is coherent only on a development-only base. On blended blocks it double-counts, which is precisely what P-9 found and fixed. Same conclusion, different bookkeeping — I do not follow them up.
- **P-3 at 125 and P-8 at 138** on the orchestrator (22 and 20), arguing that a live v1 is an executable specification of the delivery semantics so the rewrite-under-load is a tail, not the mode. I grant the premise and it is already why I am not above 150; but a hand-built per-fax delivery guarantee qualified to 300/s is not merely specified by v1's *failure*, and 24 + 6 is where the panel's own unbundled comparison lands.
- **Narrowing my range on the panel's convergence.** Ten agents reading one document and converging from 110–160 to 125–165 is shared reading, not new evidence about Venali. P-6 makes this point about the low end and P-7 and P-9 about the centre. So the range below is unchanged from round 2 even though my point estimate moved.

Net: 150 → 145. Every line below, changed or not.

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (A1/A3, 1–2 calendar months) | 10 |
| Cluster core: watchdogs, tokens, unordered status store, per-fax state, resume after failure *(was 30 bundled)* | 24 |
| Scale and burst hardening: 30/s sustained, ~300/s peak, failure survival on 2008 hardware *(new, split out)* | 6 |
| Cluster management tooling: queue depth, node health, control across 16–20 nodes *(was 6.5)* | 5 |
| Storage and data layer: Lustre integration, schema, inter-component API | 6 |
| Render workers: harness + 8–10 formats via the print-driver path (A7) *(was 15)* | 13 |
| OCR workers on a third-party library, searchable-PDF assembly, throughput | 6 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk delivery | 8 |
| Tx path: inbound-email parser, MIME and attachments, number extraction, sender checks, error replies | 6 |
| NOC: remote PoP state, cluster and queue state, alerting, operator console | 9 |
| User portal | 11 |
| CDR / billing-data capture (billing engine excluded) | 3.5 |
| Coexistence with v1 through the transition, cutover, rollout across 16–20 nodes and 10–20 sites *(was 6)* | 7 |
| Integration tests on the real stream, result-for-result comparison with v1, burst-load rig | 12 |
| Dedicated QA beyond in-block testing: v1 comparison corpus, document-pathology set, cross-product regression *(was 8, rescoped)* | 7 |
| **Subtotal** | **133.5** |
| PM, release engineering and cross-component coordination (~9%) | 12 |
| **Total (145.5, carried as 145)** | **145** |

Calendar cross-check on the corrected convention: at ~0.87 pm delivered per person per calendar month, 145 pm needs ~167 person-calendar-months — about 9 people over 18–19 months, inside the 2007–2009 window. I record, as P-4 did, that this window comes from the same recollection being estimated and so confirms nothing independently; it is a shape check, not evidence.

```
TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 9 people over 18.5 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time spent on the task, so vacation,
              public holidays and sick days are not billed to the estimate; the TEAM x DURATION
              line adds them back at ~0.87 pm delivered per person per calendar month, which is
              absence only - in rounds 1 and 2 I converted at 0.80, which wrongly deducted
              coordination time a second time, and that is corrected here);
              within-day overheads IN (standups, planning and demos, coordination between
              components, code review, defect triage - all counted as work on the task, inside
              the blocks and in the PM line);
              roles counted: architect, developers, QA/test engineers, PM/scrum lead, and the
              build/infrastructure effort needed to stand the system up;
              convention note: every block line is a blended deliverable that already carries
              its own test effort, so the dedicated-QA line covers only what is additive beyond
              that - a 25-35% uplift on these blocks would double-count
  excluded  - PoP software and Brooktrout send/receive (existed); the least-cost routing program
              (reused); billing itself (separate system) beyond writing CDR/billing data;
              development of the first version; post-launch operation, support and on-call;
              hardware procurement, rack/data-center physical work and provider contracting;
              engineering of Lustre and the DBMS as platforms (integration only); third-party
              OCR and printer-driver licensing (cost, not effort); end-user training and
              marketing; any unallocated risk uplift - risk lives in RANGE, not in TOTAL;
              the earlier synthetic REQUIREMENTS.md, treated as a different task
```

Procedural note, same off-by-one as last round: the sheet's header and every entry are labelled "round 2", while the coordinator calls this round 3. The content is the ten round-2 replies, which is what this round needs.

====================================================================================================
## P-2 — reply of round 3, verbatim

## Round 3 — final

**What moved me.**

- **P-9's diagnosis of the bookkeeping seam, applied to my own table.** P-9 found they had sized blocks as blended whole-team deliverables and then layered a large QA uplift on top, and cut it from 18 to 8. That is exactly the trap I was near in round 2; it confirms my dedicated-QA line of 8 is the right size against blended blocks, so I hold it rather than drift toward P-4's 32% or P-7's 25%. No number change, but it settles the one line I was least sure of.
- **P-10 on per-format rendering, which cuts against my round-2 move.** P-10 went 16 → 13, crediting my own round-1 argument that once a shared print-driver harness exists a format is ~0.5–1 pm, not a small project. Checking myself honestly: I carry a 6 pm worker framework *and* 11 pm of formats — 17 for rendering, the highest on the panel for that scope, where P-9, P-10 and P-6 price harness-plus-formats at 13 and P-1 at 15. My framework line is shared infrastructure serving render, OCR and Rx workers, so charging it in full and then a per-format rate that assumes a thin harness compounds. Framework 6 → 5, formats 11 → 10.
- **P-5 on the portal.** §4 and §6 describe accounts, delivery configuration, history and archive access and nothing more, and v1's portal is a live functional reference even though its code cannot be reused. Speculative scope growth is range, not mode. 12 → 11.
- **P-4's rejection of my round-1 calendar cross-check as evidence.** Correct, and I accept it as a caveat: the 2007–2009 window comes from the same recollection being estimated, so the team-and-duration line is an internal consistency check only. I also trim rollout 7 → 6, since node-level deployment is already inside the cluster-management line and only the remote-site rollout is additive.

**What I read and rejected.**

- **P-7 at 165.** Their 19 pm arithmetic correction was legitimate and I would have made it too. But the structure on top is not: a 25% QA overlay on a build subtotal that already contains a 12 pm real-stream comparison line, plus 12% PM on the engineering subtotal, puts QA at 23% of total by construction. That is the double count P-9 caught in themselves. **P-4's 32%** is internally coherent because their blocks are declared dev-only — I note the difference rather than adopt the structure.
- **P-3 at 125 and P-8 at 138.** Both moved up on the lines I also added, which is the right direction; where they stay low is compression of transition and rollout (P-3) and a 20 pm orchestrator (P-8). P-8's argument that a live v1 is an executable specification of the delivery semantics is the best case for the low side, and I grant it — it is why my orchestrator is 24 and not the 26–30 several of the panel carry, not a reason to go to 20.
- **P-1's 0.8 pm per person-calendar-month and 11 people.** I keep 0.87. P-9's check applies: an 11-engineer standing team is large for a company at Venali's revenue and nothing in the document suggests one.
- **The panel's convergence.** Mean 147, median 145, and everyone now carries an Rx line, most carry burst hardening separately, and most fixed their utilisation arithmetic. That convergence is shared structure, not independent evidence, so I moved on the two specific lines above and not toward the centre — my net change is −5, which happens to move me toward the group, but each pm of it is traceable.

## Final decomposition

| Item | pm |
|---|---|
| Domain immersion + architecture/technology selection (whole team ~1.5 months, per §6/A3) | 12 |
| Worker runtime/host framework, shared across render, OCR and Rx workers (revised, P-10) | 5 |
| Render formats: ~9 formats via the printer-driver path, incl. per-format stabilization (revised, P-10) | 10 |
| OCR workers on third-party library, searchable-PDF assembly | 4 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and sending at volume, archive write | 8 |
| Cluster orchestration: watchdogs, tokens, unordered status store, resume/retry, per-fax delivery guarantee | 24 |
| Cluster management tooling (queue depth, node health, deployment across 16–20 nodes) | 5 |
| NOC (remote PoP state, cluster, queues, alerting, operator UI) | 10 |
| User portal: accounts, delivery configuration, history and archive access, admin (revised, P-5) | 11 |
| Inbound-email parser for Tx, plus packaging and handoff to the existing router | 6 |
| CDR / billing-data capture (billing engine excluded) | 4 |
| DB schema + inter-component API, Lustre archive and working-file integration | 7 |
| Coexistence and integration with v1 through the transition | 6 |
| Scale and burst hardening (30/s sustained, ~300/s peak, failure survival on 2008 hardware) | 8 |
| Integration-test harness on the real stream + result-for-result comparison against v1 | 10 |
| Dedicated QA beyond the share embedded in each block: document pathology corpus, cross-product regression, defect triage (held at 8, P-9) | 8 |
| Production rollout / cutover to A2's DoD, incl. remote-site deployment (revised) | 6 |
| **Subtotal** | **144** |
| PM / coordination uplift (~10%) | 14 |
| **Total (158, rounded)** | **~155** |

Consistency check only, not evidence: at ~0.87 pm delivered per person per calendar month, 155 pm needs ~178 person-calendar-months — 9 people over 20 months. It fits the 2007–2009 window, but that window comes from the same recollection being estimated, so it confirms nothing (P-4's point, accepted).

---

TOTAL: 155 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 235 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; the
              calendar line above adds absence back at ~0.87 pm delivered per person per
              calendar month, and is a consistency check, not independent evidence);
              within-day overheads IN (standups, sprint ceremonies, cross-component
              coordination, code review, defect triage), counted inside each block and in
              the separate PM line; roles counted: architect/analyst, developers, QA
              (embedded per block plus the two explicit lines), PM/scrum lead, and the
              team's own build, deployment and rollout work; the 1-2 month immersion and
              technology-selection phase IN. Convention note: every block line is blended
              whole-team effort already carrying its own test share, so the QA and PM
              uplifts are deliberately small - a 25-35% overlay on these blocks would
              double-count.
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call after v1 is
              decommissioned; hardware procurement, data-center, rack and telecom
              contracting; Lustre, the DBMS, the third-party OCR library and the printer
              driver as platforms and licences (integration only, cost not effort); sales,
              marketing, end-user training; any unallocated risk uplift - the right tail
              lives in RANGE, not in TOTAL; the synthetic REQUIREMENTS.md, treated as a
              different task

====================================================================================================
## P-3 — reply of round 3, verbatim

**Note on the read.** Same off-by-one as before: the sheet is headed "Round 2" and holds the ten round-2 replies, which is what this round needs. P-3 is my own round-2 answer verbatim. The nine others are arguments to weigh, not instructions; the round-1 quarantine stands and extends here. No tool beyond the single read.

## What moved me

**1. Burst hardening is named work and I had it hidden (P-10, seconded by P-2, P-4, P-7, P-8).** P-10's rejection of the low cluster is aimed precisely at me and it lands: a decomposition that prices the orchestrator's *construction* but not its *qualification* to ~300/s is short, because A6 makes burst survival a mandatory property rather than an option. My 22 pm core line claimed to absorb it, which is exactly the "it's inside another line" move I have spent two rounds rejecting when others make it. P-7 found the identical fault in their own 22 and added 5 net of what the core already carries. I do the same. **+5.** Worth recording what this does: split out, my core-plus-burst is 27, which sits inside the panel's central mass (P-8 26, P-9 24, P-2 32, P-10 32, P-4 33). The apparent gap between my orchestrator and theirs was partly bookkeeping, not judgement.

**2. My immersion line contradicted my own team line (P-6).** P-6 argues from the text: §6 and A3 say *the team* did not know the domain and spent one to two months on discussions and technology selection — whole-team spend, not a core group's. P-4 defends my reading and stayed at 9, so the panel genuinely splits on it. What settles it is internal, not the vote: my own TEAM line says eight people, and 1.5 calendar months of eight people is ~11–12 pm, not 10. **10 → 11.**

**3. Rollout across the estate had no home (P-2, P-6, P-9).** P-2 raised rollout 5 → 7 for deployment across 16–20 nodes and 10–20 remote sites; P-9 split the same work out and found it cost 2 pm more once it stopped being crowded out. My single 6 pm line was carrying coexistence with v1, cutover *and* that rollout. **6 → 8.**

**4. My TEAM x DURATION line was arithmetically wrong, and P-1 is right about that.** I declared leave and holidays OUT and then converted at 8 people × 16 months = 128 person-calendar-months for 125 pm — ~0.98 pm delivered per person per calendar month, i.e. a working year with almost no absence. That contradicts my own declaration. P-10, P-2 and P-9 each caught the same fault in themselves. Fixed below at ~0.87.

But I reject the inference P-1 draws from it. P-1 uses this arithmetic to disqualify the low cluster's *totals* and then averages only the "internally consistent" estimates to ~145. The fault is in the calendar line, which is a derived cross-check, not in the effort sum, which is built bottom-up — P-8 says the same: correct arithmetic, changes staffing, not effort. My total does not move because of it.

## What I read and rejected

- **The 160–165 totals reached by a 25–35% QA uplift on a development-only base (P-4, P-7).** P-9's round-2 reply is the decisive text here, and it is a confession rather than a rebuttal: P-9 sized blocks as blended deliverables, added an 18 pm QA uplift anyway, saw the seam when the two conventions were laid side by side, and cut the uplift to 8. My blocks have been blended since round 1 — when I write "user portal: 10" I mean built and tested. A 35% overlay on that structure pays for the same testing twice. Four estimators using my convention (P-2, P-8, P-9, P-10) reject the mechanism while agreeing with its premise. P-7 concedes the point in their own "note on comparability": a good part of the 110-vs-165 spread on this panel is bookkeeping, not disagreement about the system. That is the single largest reason I remain below the median, and it is now better evidenced than it was in round 2.
- **The portal at 11–12 (P-1, P-6, P-7, P-9, P-10).** P-6 trims to 12 and states it is "on weight of numbers alone... the one change I hold with least conviction." An argument that concedes it is not an argument does not move me. Nothing in §4 or §6 describes more than accounts, delivery configuration, history and archive access, with v1 as a live functional reference. Hold 10.
- **The 26–30 orchestrator.** Held at 22, now with burst split out. A live v1 is an executable specification of the delivery semantics; the "rewritten once after load testing" case is what my right tail buys, and pricing it into the mode double-counts it.
- **P-6's characterisation of my verification as 9–10 pm.** That was my round-1 figure; I raised it to 14 in round 2 on P-4's argument, and P-6 was reading the old sheet.
- **The panel's centre as such.** Median ~145 after round 2, up from ~140 after round 1, on a panel where everyone read one document and no new fact entered. P-7 and P-9 both flag this: ten agents on one input are not ten independent samples. I moved 110 → 125 → 130, all of it traceable to named lines I was missing, and none of it to the centroid.

Net: 125 → 130.

## Final decomposition

| Block | pm | Note |
|---|---|---|
| Domain immersion, architecture and technology selection | 11 | 10 → 11; whole-team reading (P-6), forced by my own eight-person team line |
| Render workers: framework + 8–10 formats via the print-driver path (A7) | 13 | held |
| OCR workers (third-party library, TIFF→searchable PDF, throughput) | 5 | held |
| Cluster core: watchdogs, tokens, unordered status store, per-fax state, resume after failure | 22 | held against 26–30; with the line below it totals 27, inside the panel's central mass |
| **Scale and burst hardening: 30/s sustained, ~300/s peak, failure survival on 2008 hardware** | **5** | **new — A6 makes it mandatory (P-10, P-7); sized net of what the core line already carries** |
| Cluster management tool (queue depth, node health) | 5 | held |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk send, archive write | 7 | held |
| NOC — remote PoP state, cluster state, queue state, alerting | 8 | held |
| User portal | 10 | held; the panel moved here by weight of numbers, not by argument |
| Inbound-email parser, Tx entry path | 6 | held |
| CDR and billing-data capture (billing engine excluded) | 3 | held |
| Storage and data layer: Lustre integration, schema, inter-component API | 6 | held |
| Coexistence with v1 through the transition, rollout across 16–20 nodes and 10–20 sites, cutover to A2's DoD | 8 | 6 → 8; rollout had no line of its own (P-2, P-6, P-9) |
| Integration tests on the real stream, result-for-result comparison against v1, load/burst rig | 14 | held at the round-2 figure |
| Cross-cutting PM, release engineering, documentation | 9 | held; ~7% because QA and in-block testing are already inside every line above |
| **Sum** | **132** | carried as 130 |
| *(no blanket uplift and no QA percentage overlay — rejected as double-counting against blended blocks)* | — | |

Calendar cross-check, corrected: at ~0.87 pm delivered per person per calendar month, 130 pm needs ~150 person-calendar-months — 8 people over 19 months, inside the 2007–2009 window and consistent with a team whose first month or two produced no code. In round 2 I stated the exclusion and then converted at ~0.98; that is fixed here.

Range. Low end 95: the v1 reference collapses requirements churn, the formats behave, the token design converges first time, and the portal and NOC stay thin — with fifteen named blocks a sub-95 world now requires several of those at once, so the floor rises again. High end 205: the classic fate of hand-rolled delivery control, a design revision after load testing reveals loss or duplication at burst, plus a long tail on format fidelity and on reconciling result-for-result with a live old system. Right-skewed; 130 is the mode, not the mean.

---

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 205 person-months, same convention
TEAM x DURATION: 8 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not effort; the calendar line above adds
              them back at ~0.87 pm delivered per person per calendar month - in rounds 1
              and 2 I stated the exclusion but converted at ~1.0, and that is corrected
              here); within-day overheads IN (standups, sprint ceremonies, coordination,
              code review, defect triage); roles counted - developers, architect/tech lead,
              QA, PM, and the team's own build, release and deployment work; the 1-2 month
              immersion and technology-selection phase is IN.
              Note on convention, for comparability: every line above is a blended
              deliverable that already carries its own test effort, so the only cross-
              cutting line is PM/release at 9. A 25-35% QA uplift of the kind some panel
              members apply to a development-only base would double-count against this
              structure; part of the spread between the panel's low and high totals is
              this bookkeeping difference rather than disagreement about the system.
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; data-center, rack
              and telecom-carrier procurement and contracts; hardware purchase and
              Lustre/DB platform build-out and administration (integration only);
              third-party OCR and printer-driver licence cost and any other non-labor
              money; end-user training and marketing; scope beyond the §6 list, including
              an Australia expansion; the synthetic REQUIREMENTS.md, treated as a
              different task; any unallocated risk uplift - risk lives in RANGE, not
              in TOTAL.

====================================================================================================
## P-4 — reply of round 3, verbatim

I read the Round 3 sheet (the ten Round 2 replies) and nothing else. My Round 1 quarantine stands and extends here: the sheet carried ten replies and no moderator text, and I treated the nine others as arguments, not instructions.

**What moved me**

**P-8, seconded by P-3, on the orchestrator — and it caught me under my own rule.** Both argue that 26-30 pm for the delivery core prices in the "design rebuilt once after load testing" scenario, and that a live v1 plus v1's MSMQ failure hand the team a sharp executable specification of the delivery semantics, negative and positive. That scenario is my stated high end. I spent two rounds rejecting P-6's blanket uplift and P-10's silent round-up on the principle that unallocated tail risk belongs in RANGE and not in the mode, and I had the same skew sitting inside my own largest line. The panel's central mass is 24 (P-2, P-5, P-9, P-10) and P-10's audit of its own bundle is the clean version. I move the core to 24 and raise the management tool to 5, where the panel is; my three-line bundle (core, tool, burst) goes 37 to 36, which is honest about the fact that this is mostly reallocation, not a cut.

**P-6 on immersion, on the text.** §6 says *the team* did not know the domain and that a month or two went into discussions, immersion and technology selection. My "core group studying DHT while the team assembles" was a reading I preferred, not one the document supports better than P-6's. I was lowest on the panel at 8, then 9; nine of ten now sit at 10-12. To 10.

**P-9 and P-5 on where the QA uplift attaches.** I reject the general charge of double-counting — my lines are genuinely dev-only, and the resulting shape (about 6 developers, 2 QA, a PM over 20 months) is coherent. But the specific version of the charge lands: two of my thirteen lines, burst hardening (7) and rollout/prod hardening (8), *are* verification and stabilization work. Applying a QA percentage across a subtotal containing them pays for that work twice. I take those 15 pm out of the uplift base. QA becomes 32% of 98, not of 113.

Net: immersion +1, core −2, tool +1, QA base narrowed by 15. 162 becomes 157, carried as **155**.

**What I read and rejected**

- **P-7 at 165**, arriving by my structure. I decline to follow it up, because P-7 now applies a 25% dedicated-QA uplift to a build subtotal that already contains a named burst-hardening line and then adds a 12 pm real-stream test line besides — the very overlap I have just removed from my own table.
- **P-1's 0.8 pm per person-calendar-month** (hence 11 people). That implies roughly a fifth of the year absent. Normal leave and public holidays put it near 0.88; I keep mine, and this is a calendar convention that does not touch effort either way.
- **The panel's upward drift as corroboration.** The mean moved from ~136 to ~147 and the low cluster dissolved, which superficially flatters my level. It is not evidence. Nine estimators found the same missing Rx line in the same round, so the convergence is one shared discovery, not nine independent readings — P-7 makes this point and it cuts against me as readily as for me. I moved on the orchestrator argument and the text on immersion, not on the drift.
- **My range.** Unchanged, deliberately. The tail drivers are the same ones I named in Round 1 — the hand-rolled delivery control rewritten under production load, and a reconciliation phase against a live system that drags. Having just removed that scenario from my central line, it would be incoherent to also trim the tail it lives in.

**Full decomposition**

| Line | pm |
|---|---|
| Domain immersion + architecture/technology selection (team-wide, 1-2 months calendar) | 10 |
| Render worker framework + 8-10 formats, incl. document-pathology tail | 14 |
| OCR workers on a third-party library, PDF assembly | 5 |
| Cluster orchestration: watchdogs, tokens, state store, retry/failover | 24 |
| Cluster management tool (queue depth, node health, rollout across 16-20 nodes) | 5 |
| NOC (remote PoP state, cluster, queues) | 9 |
| User portal | 10 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk delivery | 7 |
| Inbound-email parser and the Tx path into the PoP handoff | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| DB + API plumbing between components, Lustre and storage integration | 6 |
| Scale and burst hardening to ~30/s sustained, ~300/s peak, on 2008 hardware | 7 |
| Rollout, coexistence with v1, cutover and prod hardening | 8 |
| **Engineering subtotal** | **113** |
| Dedicated QA uplift, 32% of 98 (base excludes the burst and rollout lines, which are themselves verification): v1 comparison harness, load rigs, document corpus, regression | 31 |
| PM / coordination uplift, 12% of 113 | 13 |
| **Total (157, carried as 155)** | **155** |

TOTAL: 155 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 240 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a calendar person-month is taken as ~0.88 pm, which
              is why 9 people x 20 months carries 155 pm and not 180); within-day overheads IN
              (standups, planning, code review, cross-team coordination, the scrum ceremony
              load); roles counted: developers, architect, QA (manual and automation, including
              the comparison harness and load rigs), PM/BA, plus the build and deployment work
              done by the same team. Convention note: lines 1-13 are development effort only,
              which is why the QA uplift is large; the uplift base excludes the two lines that
              are themselves verification work.
  excluded  - PoP software and Brooktrout-side reception/sending; the least-cost routing
              program; billing proper (only CDR/billing-data capture is in); development of
              the first version; post-launch operation, support and on-call; hardware, rack,
              telecom and third-party licence procurement; the Lustre and DBMS platforms
              themselves (integration only); any Australia expansion or other scope beyond
              the §6 list; any unallocated risk uplift - tail risk is carried in RANGE, not
              in TOTAL.

====================================================================================================
## P-5 — reply of round 3, verbatim

I read the sheet (the ten round-2 replies). Panel totals now 125, 138, 140, 140, 145, 145, 150, 160, 160, 165 — I was at 140. Nothing in it is new evidence about Venali; ten estimators read one document, so it is all argument about how to size it. I therefore ignored the centroid and the direction of drift and looked only for named defects in my own table. I found three, and one of them cuts my number.

**What moved me**

- **P-9, on a seam in my own bookkeeping — downward.** P-9 caught themselves sizing blocks as blended deliverables ("when I wrote 'user portal: 12 pm' I was picturing the portal built and tested") and then adding a large dedicated-QA uplift on top anyway, and cut it from 18 to 8. That is exactly my construction: my lines are whole-team effort, and I still layered 15% (16 pm) of extra QA over them while also carrying an explicit 12 pm comparison-harness line. What is genuinely additive beyond in-block testing is the document pathology corpus, cross-product regression and defect triage, not a second pass over every component. **QA uplift 16 → 9.** P-7's observation that much of the panel's 110-vs-165 spread is this bookkeeping difference rather than disagreement about the system is the same point, and it is the most useful thing in the sheet.
- **P-3, on a line of mine doing two jobs.** My 7 pm "integration with what is reused" was carrying both the storage and data layer (Lustre archive and working files, DB schema, the inter-component API that §4 says everything talks through) and the seams to the reused PoP software and router. P-3 caught the identical conflation in their own table and split it; P-1, P-7, P-9 and P-10 all carry the data layer separately at 6–9. Split: **storage and data layer 7, reused-component seams 4.**
- **P-10 and P-7, on burst qualification.** P-10's charge against the low cluster is specific: we price the orchestrator's construction but not its qualification to ~300/s, which A6 makes a mandatory property. I had answered this in round 2 by absorbing hardening into a 24 pm core, where — as P-10 says of their own bundled figure — it is invisible and therefore under-weighted. P-7's handling is the right one: name it, sized net of what the core already carries. **Core 24 → 21, plus a burst-and-scale hardening line of 6.**

Smaller, all on mechanism rather than count: render workers 11 → 12 (the per-format failure modes of 2008 headless Office automation, argued by P-7, P-8, P-10, and note that P-10 moved *down* to 13 on the same reading of A7); OCR 4.5 → 5; the Tx parser 4.5 → 6, because P-9, P-6 and P-10 rescope it to cover packaging and handoff to the PoP (§3.2), which nothing else in my table pays for.

Net: +10 on the base, −7 on QA, +2 on PM as a percentage of a larger base. 142 → 147, carried as 145. I checked the counterfactual before writing it down: had the QA correction landed me at 133 I would have reported 133, and I am aware that 145 is the panel median for the second round running.

**What I read and rejected**

- **P-1's refutation of the low cluster by its own calendar arithmetic.** Half of it lands: my round-1 cross-check (7 people over 16 months for 110 pm) did silently assume ~98% utilization against a declaration that put leave OUT, and I corrected that in round 2 by stating 0.87 explicitly. But P-1 uses the bad check to discount our *component* sizes and then averages "the internally consistent estimates" to ~145. A faulty cross-check makes the check wrong, not the blocks; and selecting whom to average by that test is not a method.
- **P-4's 32% and P-7's 25% QA uplift.** Coherent on their own dev-only tables, not transferable to mine: applied to blended blocks plus an explicit harness line they would pay for the same testing twice. This is the argument I moved *against* this round.
- **P-6's portal at 12, trimmed "on weight of numbers alone"** — they flag it themselves as their least-confident change. Moving on a headcount of opinions is the one thing a Delphi should not produce. I hold 10; nothing in §4 or §6 describes more than accounts, delivery configuration, history and archive access.
- **P-1's 0.8 pm per person-calendar-month** (about a fifth of the year absent). P-7 is right that ~0.87–0.9 matches a working year with normal leave and holidays.
- **The panel's upward drift as such** (mean ~136 → ~147). Some of it is a real shared discovery — nine of ten tables were missing the Rx path — but a mean marching in one direction across rounds is also the signature of herding, so I took none of it as evidence.
- **The 26–30 pm orchestrator figures** (P-1, P-4, P-6). P-8 and P-3 have the better argument: a live v1 is an executable specification of the delivery semantics, so "rewritten once after load testing" is the right tail, not the central case. My 21 + 6 sits below the bundled 30 deliberately.

**Final decomposition (person-months, A9; lines 1–15 are blended deliverables carrying their own test effort)**

| # | Line | pm |
|---|---|---|
| 1 | Domain immersion, architecture and technology selection (A3; DHT and alternatives) | 10 |
| 2 | Render workers: harness, crash/timeout isolation, printer-driver path, 8–10 formats each stabilized (A7) | 12 |
| 3 | OCR workers, TIFF→searchable PDF assembly, third-party library integration and throughput tuning | 5 |
| 4 | Cluster delivery-control core: watchdogs, token store over an unordered store, per-fax status, resume after node loss | 21 |
| 5 | Scale and burst hardening: ~30/s sustained, ~300/s peak, failure survival on 2008 hardware (A6) | 6 |
| 6 | Cluster management tool: queue depth, node health, rollout across 16–20 nodes | 5 |
| 7 | Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and sending at volume, archive write | 7 |
| 8 | NOC: state of 10–20 remote PoPs, cluster and queues, agents, alerting, operator UI | 9 |
| 9 | User portal: accounts, delivery configuration, history, archive search, admin | 10 |
| 10 | Tx path: inbound-email parser (MIME, attachments, number extraction, bounces, sender auth, abuse), packaging and handoff to the PoP | 6 |
| 11 | CDR and billing-data capture (billing engine out) | 3 |
| 12 | Storage and data layer: Lustre integration, archive layout, DB schema, the inter-component API (§4) | 7 |
| 13 | Integration seams with the reused components: PoP software, the least-cost router (A4) | 4 |
| 14 | Integration tests on the real stream: result-for-result comparison harness against v1, load and burst rig | 12 |
| 15 | Cutover to production and coexistence with v1 through the transition, to A2's Definition of Done | 8 |
| | *Subtotal* | *125* |
| 16 | Uplift: dedicated QA beyond in-block testing — document pathology corpus, cross-product regression, defect triage | 9 |
| 17 | Uplift: PM, scrum coordination and release engineering (~10%) | 13 |
| | **Total (147, carried as 145)** | **145** |

Cross-check: at ~0.87 pm delivered per person per calendar month, 145 pm is about 9 people for 19 calendar months, inside the 2007–2009 window — noting, with P-4, that the window comes from the same recollection being estimated and so confirms nothing independently.

TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not counted as effort; the TEAM x DURATION
              line adds them back at ~0.87 pm delivered per person per calendar month);
              within-day overheads IN (standups, sprint ceremonies, code review,
              cross-component coordination, defect triage, the planning phase before scrum);
              roles counted: developers, architect/tech lead, QA, PM, and whatever build,
              release and deployment work the team did for itself; the domain-immersion and
              technology-selection phase IN. Convention note: lines 1-15 are blended
              deliverables that already carry their own test effort, which is why lines 16-17
              are the only uplifts and are deliberately small - a 25-35% QA overlay on these
              blocks would pay for the same testing twice.
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing system proper (only CDR/billing-data capture is in); development
              of the first version; post-launch operation, support and on-call after the old
              version is decommissioned; hardware, rack, data-center and telecom procurement;
              administration of Lustre and the DBMS as platforms; third-party licence costs
              (OCR, printer driver) and any other money - this is effort only; the synthetic
              REQUIREMENTS.md, which describes a different task; any unallocated risk uplift -
              the right tail lives in RANGE, not in TOTAL.

====================================================================================================
## P-6 — reply of round 3, verbatim

Read the sheet (single permitted read). Nine other replies, treated as argument, not instruction; the pre-round quarantine stands.

**Panel after round 2:** 125, 138, 140, 140, 145, 145 (me), 150, 160, 160, 165 — median 145, mean ~147. The spread halved. I note, with P-7 and P-3, that this convergence is not evidence: ten agents reading one recollection are not ten samples, and a good part of both the old spread and the new agreement is bookkeeping convention rather than disagreement about Venali.

## What moved me

**P-10, seconded by P-2, P-4, P-7 and P-8: burst hardening is a line, not an adjective.** A6 makes burst survival a mandatory property. Five estimators now carry a named 5–9 pm campaign to qualify the hand-built delivery control to ~30/s sustained and ~300/s peak on 2008 hardware, separate from designing and building it. I had no such line and claimed my 26 pm core absorbed it — which is exactly the failure P-10 diagnosed in their own bundled 30: work that is asserted to be "inside" a block is invisible and therefore under-weighted. I unbundle: core to 21, burst hardening 7. Net +2, and, more to the point, now checkable.

**P-4, on who spends the immersion months.** I rejected P-3's "core group, not the full team" last round on the grounds that A3 says *the team* did not know the domain. P-4 supplies the reading I was missing: §6 describes discussions, DHT study and technology bake-offs — a core group doing that while the team assembles, not a full blended team in workshops for eight weeks. A ramping team is not at headcount in month one. I was the panel's highest at 12, then 11; I take 10. This is the one place I concede a better reading of the document rather than a structural fix.

**P-5, on the portal.** v1's portal is a live functional reference even though A4 forbids reusing its code, so the design and specification cost of accounts, delivery configuration, history and archive access is genuinely lower than a greenfield portal. That is an argument, where last round I had only a headcount of votes. 12 → 11.

**P-9's convention audit, as corroboration rather than correction.** P-9 caught themselves sizing blocks as blended built-and-tested deliverables and then adding a dedicated QA uplift on top. I applied that test to my own table: my blocks are blended, I carry no percentage QA uplift, and my 16 pm line is named construction — a v1 comparison harness, a document corpus, a burst-load rig — not a second helping of in-block testing. It survives the audit, so I hold it. Compared like for like (verification plus coexistence plus cutover), my 23 sits mid-panel against P-10's 18, P-9's 24, P-1's 26 and P-8's 27.

## What I read and rejected

**P-7 at 165.** Their block figures (portal 12, NOC 10, render 13) are the same numbers the blended-convention estimators use for built-and-tested deliverables, and a 25% QA uplift is then layered on top of them plus a separate 12 pm comparison-test line — QA reaching 39 of 165. This is precisely the seam P-9 found and closed in themselves. I credit P-7's honesty in catching their own 19 pm arithmetic drop, but the corrected structure still double-counts.

**P-3 at 125 and P-8 at 138.** P-3 still compresses and P-8 declines the orchestrator's hardening tail on the grounds that a live v1 is an executable specification of the delivery semantics. v1 is an executable specification of *what the system does*, not of how a token-and-watchdog scheme behaves at 300/s on hardware v1 never ran on — and MSMQ's failure proves the team had no working reference for the mechanism, only for the behaviour.

**P-1's 0.8 pm per person-calendar-month**, implying eleven standing engineers. That is a calendar convention, not evidence about effort; I keep ~0.88, where six of the panel now sit.

**The panel's centre as such.** My changes this round net to zero — minus one on immersion, minus one on portal, minus five on the core, plus seven on burst hardening. The table is materially better structured and the total is unchanged. I report that rather than manufacture movement.

## Final decomposition (full)

| Block | pm | change from R2 |
|---|---|---|
| Domain immersion + architecture/technology selection (ramping core group, 1–2 calendar months) | 10 | −1 (P-4) |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax state, resume after node loss, idempotency | 21 | −5, unbundled |
| Cluster management tool (queue depth, node health, deployment across 16–20 nodes) | 5 | — |
| **Scale and burst hardening: qualification to ~30/s sustained and ~300/s peak, failure survival, on 2008 hardware** | **7** | **new (P-10, P-2, P-4)** |
| Render workers: harness + printer-driver path + 8–10 formats, each stabilized separately (A7) | 13 | — |
| OCR workers + searchable-PDF assembly, throughput tuning | 5 | — |
| Rx path: PoP intake, per-user page-wise-TIFF vs PDF branch, mail composition and bulk send at volume, archive write | 9 | — |
| Tx path: inbound-email parser, MIME and attachments, number extraction, abuse/bounce, packaging and handoff to the existing router | 7 | — |
| NOC: remote PoP state, cluster, queues, agents, alerting, operator UI | 10 | — |
| User portal: accounts, delivery configuration, history and archive access, admin | 11 | −1 (P-5) |
| CDR / billing-data capture (billing engine excluded) | 4 | — |
| Storage and data layer: Lustre integration, DB schema, inter-component API, PoP/routing seams | 9 | — |
| Integration test on the real stream: result-for-result comparison harness against v1, document corpus, burst-load rig | 16 | held |
| Coexistence with v1 through the transition, rollout across sites, cutover and production stabilization to A2's DoD | 7 | — |
| PM, scrum coordination, release engineering | 12 | — |
| Blanket uplift | 0 | held at zero |
| **Sum** | **146** | 145 → 145 |

Rounded to 145. Blocks 1–14 are blended deliverables carrying their own in-block test effort; line 13 is additional named construction, not an uplift; line 15 is the only cross-cutting line. There is no percentage overlay anywhere in the table, and no unallocated risk — risk lives in RANGE.

I decline to narrow the range. The panel's numeric spread contracted, but nothing was learned about the project between rounds; the residual uncertainty — whether the token scheme survives its first encounter with production burst, how nasty the true format list was, how long reconciliation against a live v1 actually ran — is unchanged by ten agents agreeing with each other.

```
TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; the
              calendar line converts at ~0.88 pm delivered per person per calendar month,
              which is where absence is absorbed); within-day overheads (meetings,
              coordination, code review, standups, demos) IN, counted inside each block and
              in the explicit PM line; roles counted: developers, architect/tech lead, QA
              (in-block testing plus the v1 comparison harness, document corpus and load
              rigs), PM, and the team's own build, deployment and stabilization work on the
              cluster and PoP rollout; the domain-immersion and technology-selection phase IN.
              Convention note: blocks are blended built-and-tested deliverables, so there is
              no percentage QA or PM overlay - a 25-35%-style uplift on these figures would
              double-count.
  excluded  - PoP software (Brooktrout send/receive); the least-cost routing program; billing
              itself (only CDR/billing-data capture is in); development of the first version;
              post-launch operation, support and on-call once v1 is decommissioned; hardware,
              rack, data-center and telecom procurement and contracting; Lustre, the DBMS, the
              third-party OCR library and the printer driver as platforms and licences
              (integration only, cost not effort); sales, marketing, end-user training and
              documentation beyond what the portal and NOC need; recruitment and onboarding;
              scope beyond the §6 list, including any Australia expansion; the synthetic
              REQUIREMENTS.md, treated as a different task; any unallocated risk uplift.
```

====================================================================================================
## P-7 — reply of round 3, verbatim

I made the single permitted read of the round-2 sheet and no other tool call.

## What moved me

**P-9's diagnosis of a bookkeeping seam — and it is my seam too.** P-9 noticed their blocks were blended deliverables while their uplift was priced as if the blocks were dev-only, and cut the uplift accordingly. Applying that same test to my own table honestly: my render line prices 8–10 formats at ~1.2 each because A7 calls each one "integration and **stabilization**" work, and my orchestrator line at 22 prices "resume-after-failure, idempotency" — stabilization and failure-mode work *is* test effort. So my lines are not the clean dev-only base my declaration claimed, and a 25% dedicated-QA overlay on all of them pays for part of that twice. P-5, P-2 and P-10 make the same double-count objection to the 25–35% overlay; P-9 is the one who made it self-diagnosable rather than a matter of taste. QA uplift 25% → 18%, i.e. 27 → 20.

**P-10, on where burst qualification actually sits.** P-10 unbundled their cluster line and found it had been carrying the management tool; the reverse check on mine is the useful one. My core is 22, at the low end of the panel's 20–30 with its centre at 24–26 (P-2 24, P-9 24, P-10 24, P-4 26). A leaner core absorbs *less* qualification work, so my burst line — which I explicitly sized "net of what the core carries" — was set against an assumption I had not checked. Burst hardening 5 → 7, giving 29 combined, mid-panel rather than below it.

These two move in opposite directions and largely cancel: −7 and +2, net −5. I say that plainly rather than dress a 5 pm move as a reconsideration.

## What I read and rejected

- **P-4's defence of the 32% overlay.** P-4 and I were the only two on the dev-only-plus-large-uplift convention, and I now think P-9's seam cuts against both of us. P-4's headcount argument ("two QA engineers across a twenty-month rework is ~35 pm before the harness exists") is the strongest thing said for it, and it is why I trimmed to 18% rather than to the panel's typical 8 — but it argues for a *level*, not for the *mechanism* of a percentage on blocks that already contain stabilization.
- **P-1's consistency filter** — discarding the low cluster because P-3, P-5 and P-8 declare leave OUT and then cross-check against a calendar implying ~100% utilization, then averaging only the survivors to ~145. The arithmetic catch is right and worth making. Using it to weight *totals* is not: the TEAM x DURATION line is a derived display line. A sloppy conversion there convicts the conversion, not the effort estimate behind it.
- **P-6's portal trim 14 → 12 "on weight of numbers alone"** — flagged as low-conviction by P-6 themselves, and correctly so. I hold my portal at 12 on its own content, not because three others sit near it.
- **The convergence itself.** Eight of ten moved between rounds and most moved inward; the median sat at ~145 in round 1 and sits at ~145 now. A panel tightening around an unchanged centre is a property of the procedure, not new information about Venali. I remain the high end of the panel and am not closing the rest of that gap: what is left of it is almost entirely the QA/PM convention, which I have now made explicit and checked against headcount below.

## Full decomposition

| Line | pm |
|---|---|
| Domain immersion, architecture and technology selection (§6/A1, ~1–2 months calendar) | 10 |
| Render workers: harness plus 8–10 formats via the printer-driver path (A7, ~1.2 each) | 13 |
| OCR workers on a third-party library: pipeline, tuning, PDF assembly | 5 |
| Cluster delivery control: watchdogs, tokens, unordered status store, resume-after-failure, idempotency | 22 |
| Cluster management tool: queue depths, node state, control actions | 5 |
| NOC: remote PoP state, cluster state, queues, alerting | 10 |
| User portal: accounts, per-user delivery configuration, history and archive access | 12 |
| Rx path: PoP intake, TIFF-page vs PDF branch, mail composition and bulk delivery | 7 |
| Inbound email parser, Tx entry: MIME, attachments, number extraction, bounces, abuse | 6 |
| CDR and billing-data capture (billing engine excluded) | 4 |
| Storage and data layer: Lustre integration, schema, the inter-component API | 8 |
| Burst and scale hardening to ~30/s sustained and ~300/s peak on 2008 hardware *(5 → 7)* | 7 |
| *Build subtotal* | *109* |
| Integration tests on the real stream, result comparison against v1, coexistence seams | 12 |
| Production rollout, migration and stabilization to A2's Definition of Done | 6 |
| *Engineering subtotal* | *127* |
| Dedicated QA beyond the in-block stabilization and the harness line: document corpus, cross-product regression, defect triage, load rigs — 18% of the build subtotal *(was 25%)* | 20 |
| PM, release management and coordination, 12% of the engineering subtotal | 15 |
| **Total (162, carried as 160)** | **160** |

Consistency check on the convention, since that is where this panel actually disagrees: QA across both its lines is 32 of 160 (20%), PM is 15 (9%), together 29%. That is what a blended team of roughly 6 build-side people, 2 QA and 1 PM spends by headcount — the shape A9 asks to be counted. A total whose QA and PM together come to 12–15% implies a team with well under one full QA engineer, which contradicts §6's statement that QA and PM were on the team.

Calendar: 160 pm at ~0.9 pm delivered per person per calendar month is ~178 person-calendar-months. I move the team line to 9 over 20 months rather than 10 over 18, which answers my own round-2 misgiving that ten standing heads is large for a company at Venali's revenue, and still fits the 2007–2009 window.

TOTAL: 160 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 240 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on this
              task; the calendar line adds them back at ~0.9 pm delivered per person per
              calendar month, which is why 9 x 20 carries 160 pm and not 180); within-day
              overheads IN (standups, scrum ceremonies, coordination, code review, the
              planning phase before scrum); roles counted: developers, architect/tech lead,
              QA, PM, and the build/release work done by the same team. Note on convention:
              the build lines carry the developers' own stabilization work, so the QA uplift
              is only what a dedicated QA function adds beyond it; the immersion and
              technology-selection phase is IN; no unallocated risk uplift - the right tail
              is in RANGE only
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the first
              version of the system; post-launch operation and support; hardware procurement,
              data-center and rack build-out, telecom contracts; development of the third-party
              OCR library, the printer driver, Lustre and the DBMS (integration only); sales,
              marketing and anything touching the j2 litigation; the synthetic REQUIREMENTS.md,
              treated as a different task

====================================================================================================
## P-8 — reply of round 3, verbatim

**Round 3 — P-8, final.**

**What moved me.** Small, line-level, and all upward:

- **P-6** on the immersion line: §6 and A3 say *the team* did not know the domain and spent one to two months on discussion, immersion and technology selection. My "ramping team" reading discounted that; the discount is my invention, not the document's. 10 → 11 (I still decline P-2's 12, since the team demonstrably was not at full strength on day one).
- **P-9, P-6, P-10** on the Rx path: framed as a path rather than a component, §2 carries intake, the per-user branch, composition and bulk send *and* the archive write. My 6 covered the mail-out but not the archive write. 6 → 7.
- **P-3**, splitting the data layer out of the transition line, and **P-7/P-9/P-10** at 8: §4 makes the inter-component API the spine of a system with eight-plus talking parts. 6 → 7.
- **P-2 and P-6** on rollout across 16–20 nodes *and* 10–20 remote sites as work my single cutover line underweighted. 5 → 6.

**What I read and rejected.**

- **P-4's 32% and P-7's 25% QA uplifts.** **P-9** made my case better than I could: he found the same seam in his own table, saw that blocks sized as blended deliverables already contain their test effort, and cut his uplift 18 → 8. My blocks are blended and I carry an explicit 16 pm real-stream line, top of the panel. A further percentage overlay would buy the comparison harness twice.
- **P-10's round-2 charge against "the 110–115 cluster (P-3, P-5, P-8)" — no line for burst hardening.** It was fair against my round 1 and is now stale: I split out 6 pm for it last round, and my core plus hardening is 26, inside the panel's 22–32 combined band. I hold the core at 20 rather than 24–26 for the reason I gave: a live v1 is an executable specification of the delivery semantics, so a second architecture after load testing is my high end, not my mode.
- **P-6's portal at 12 "on weight of numbers alone"** — he flagged it himself as his least-held change. Moving on a headcount of opinions is exactly what a Delphi should not launder into evidence. Portal holds at 10.
- **P-7's observation about the panel's spread** I accept and act on: much of 125-vs-165 is bookkeeping (blended blocks with a PM-only uplift versus dev-only blocks with a 25–35% overlay), not disagreement about the system. That is a reason to distrust the spread, and equally a reason not to read the panel's centre as a signal.

I end at 143, close to the panel median of ~145. I want to be explicit that this is where four named lines put me, not where the group is; had they put me at 128 I would have reported 128. Ten agents reading one document are not ten independent samples, and their agreement is not evidence about Venali.

**Final decomposition (person-months, A9 units)**

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (whole team, ~1.5 months) | 11 |
| Render worker harness (job pickup, crash/timeout isolation on the Windows cluster) | 4 |
| Render formats: ~9 formats through the print-driver path, ~1 pm each (A7) | 9 |
| OCR workers on a third-party library, searchable-PDF assembly, throughput tuning | 5 |
| Cluster core: watchdogs + tokens over an unordered store, per-fax status, resume, idempotency, retries | 20 |
| Scale and burst hardening to ~30/s sustained and ~300/s peak, failure survival (A6) | 6 |
| Cluster management tool (queue depths, node control, rollout across 16–20 nodes) | 5 |
| NOC: agents on 10–20 remote PoPs, cluster and queue state, alerting, operator UI | 9 |
| User portal: accounts, TIFF-page vs PDF configuration, history and archive access, admin | 10 |
| Inbound-email parser, Tx entry (SMTP, MIME, number extraction, sender auth, bounces, abuse) | 6 |
| Rx path: PoP intake, per-user assembly, mail composition and sending at volume, archive write | 7 |
| CDR / billing-data capture (billing engine excluded) | 3 |
| Storage and data layer: Lustre archive and working files, DB schema, the inter-component API | 7 |
| Integration with the existing PoP software and routing; coexistence with v1 through the transition | 6 |
| Integration testing on the real stream, result-for-result comparison against the old system, load/burst rig | 16 |
| Cutover and production rollout across the cluster and the remote sites, to A2's Definition of Done | 6 |
| Uplift: PM, coordination and release management beyond what the blended blocks absorb (~10%) | 13 |
| **Total** | **143** |

TOTAL: 143 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so
              absences are not counted as effort; the calendar line adds them back at
              ~0.87 pm delivered per person per calendar month, which is why 9 x 18
              carries 143 pm and not 162); within-day overheads (meetings, coordination,
              code review, standups, demos) IN, counted inside each block and in the
              separate PM line; roles counted: developers, architect/tech lead, QA, PM,
              and the team's own build/release and deployment work; the domain-immersion
              and technology-selection phase IN. Convention note: every block above is a
              blended deliverable that already carries its own test effort, so the PM line
              is the only uplift and QA appears as the explicit real-stream verification
              block rather than as a percentage overlay; a 25-35% uplift on these blocks
              would double-count. No unallocated risk uplift is included - the right tail
              lives in RANGE, not in TOTAL.
  excluded  - PoP software (reception/sending via Brooktrout); the least-cost routing
              program; the billing system itself (only CDR/billing-data capture is in);
              development of the first version; post-launch operation, support and
              on-call; hardware procurement, data-center and telecom provisioning,
              rack/PoP build-out; Lustre and the DBMS as platforms (integration only);
              third-party license costs (OCR, print driver) and any other non-labor cost;
              sales, marketing and end-user training; scope beyond the §6 list; the
              synthetic REQUIREMENTS.md, treated as a different task.

====================================================================================================
## P-9 — reply of round 3, verbatim

**What moved me**

**P-10, seconded by P-7, on burst qualification as a line rather than a clause.** P-10's formulation is the one that landed: a decomposition that prices the orchestrator's *construction* but not its *qualification to ~300/s* is short by exactly that amount, and A6 makes burst survival a mandatory property rather than an option. My line 2 carried the words "burst behaviour" in its label, which is precisely the kind of clause that hides work — I could not have said how many of the 24 pm were spent on it. Unbundling honestly: the delivery-control core is 22, and the campaign to reach 30/s sustained and 300/s peak is 6, because it is not confined to the orchestrator — it reaches the render workers, the Lustre paths, the DB contention and the mail-out. Net +4. P-7's discipline here is the one I followed: size the new line *net* of what the old line already carried, not at the 8–9 the others use who never had it inside.

**P-3, P-6, P-8 and P-10 on the harness line.** Four estimators moved to or held 12–16 for real-stream testing and the v1 comparison, each citing A2's "the results agree with the old system." P-3 raised 10→14 on finding their line was also absorbing rollout — which is the same discovery I made last round and fixed by splitting rollout out. Having split it, my remaining 10 was sized for the folded version and never re-examined. 10 → 12.

**P-6 on the immersion phase, textually.** §6 says "the team, meanwhile, did not know the domain," which reads as whole-team spend; my "partial team" discount was doing work the text does not support. I move 9 → 10, the panel's mode, not to P-6's 11–12, since a team also ramps.

Small: Tx 8 → 7, because P-6 rescoped theirs to exactly my scope (parser plus dispatch/handoff) at 7 and I was top of the panel at 8.

**What I read and rejected**

- **P-7's 165.** The arithmetic slip they caught in themselves is real and creditable. But the resulting structure has a 27 pm QA uplift (25% of the build subtotal) stacked on a table that *already* carries a 12 pm real-stream comparison line and a 6 pm rollout line. That is the exact double-count I removed from my own table in round 2, re-entering through a percentage. P-7 also mis-reads me in passing as sizing blocks dev-only and adding 30–45%; that was my round-1 structure and it is what I repudiated.
- **P-4's 32% QA uplift (160).** Same objection, and I note P-4 declines to delete a forgotten component to look like the group — I respect that and apply it to myself below. But my blocks are blended, so the premise that justifies their uplift does not hold against my base.
- **P-2's 160.** Reached by adding a genuine Rx line (which I already had), then a dedicated-QA line, a burst line, a rollout increase and a 10% PM layer on a subtotal that also contains a separate 10 pm harness. The individual moves are each defensible; the accumulation is not checked against the whole.
- **P-3's 125.** They closed a third of their gap on named omissions, which is the right method. What remains missing is the burst-qualification line — P-10's argument applies to them precisely, and it is roughly the size of their residual gap to me.
- **P-1's 0.8 pm per calendar month, hence 11 people.** Still rejected. A working year with normal leave, public holidays and sickness is ~0.85–0.9, which is where seven of the ten now sit. 0.8 implies a fifth of the year absent.
- **P-10's remaining round-up** (143 summing, 145 stated). They correctly removed their round-1 round-up of 142→150 and then rounded again for "false precision." Minor, but the sum is the estimate.
- **Convergence.** Panel round 2 runs 125–165, median ~145. I now land on 150, which is inside that mass, and I want to be plain that I got there by adding 6 and subtracting 1 for reasons I can name. Two of my three moves are upward and one of them contradicts the direction I moved last round. I am reporting that rather than smoothing it.

**Final decomposition (person-months, A9)**

| # | Line | pm |
|---|---|---|
| 1 | Domain immersion, architecture and technology selection (whole team ramping, 1–2 calendar months) | 10 |
| 2 | Delivery-control core: watchdogs, tokens, unordered status store, per-fax state, resume after node loss (construction only) | 22 |
| 3 | Scale and burst qualification across the pipeline: 30/s sustained, ~300/s peak, failure survival on 2008 hardware — sized net of line 2 | 6 |
| 4 | Cluster management tool (queue depth, node health, control and rollout across 16–20 nodes) | 6 |
| 5 | Render workers: worker framework + 8–10 formats via the print-driver path, each stabilized separately | 13 |
| 6 | OCR workers on a third-party library, TIFF→searchable PDF, throughput tuning | 5 |
| 7 | Rx path: PoP intake, per-user page-wise TIFF vs PDF, mail composition and sending at volume, archive write | 8 |
| 8 | Tx path: inbound-mail parser (MIME, attachments, number extraction, error replies), packaging and dispatch to the existing router | 7 |
| 9 | Storage and data layer: Lustre integration, archive layout, DB schema, the inter-component API | 8 |
| 10 | NOC: state of 10–20 remote PoPs, cluster and queues, agents, alerting, operator UI | 10 |
| 11 | User portal: accounts, delivery configuration, history and archive access, admin | 12 |
| 12 | CDR / billing-data capture (billing engine excluded) | 3 |
| 13 | Integration tests on the real stream, result-for-result comparison harness against v1, load and burst rig | 12 |
| 14 | Coexistence with v1 through the transition, rollout across sites, cutover to the A2 Definition of Done | 6 |
| | *Subtotal, blended engineering (each block carries its own test effort)* | *128* |
| 15 | Uplift: dedicated QA beyond in-block testing — document pathology corpus, cross-product regression, defect triage | 8 |
| 16 | Uplift: PM, scrum coordination, release engineering (~10%) | 13 |
| | **Total** | **149 → 150** |

```
TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 225 person-months, same convention
TEAM x DURATION: 8 people over 22 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours actually worked on the
              task, so absence is not billed as effort; the calendar line above adds it back at
              ~0.85 pm delivered per person per calendar month, so 8 x 22 person-calendar-months
              carries 150 pm and not 176); within-day overheads IN (standups, sprint ceremonies,
              cross-component coordination, code review, defect triage); roles counted:
              developers, architect/tech lead, QA, PM, and the team's own build, release and
              deployment work; the domain-immersion and technology-selection phase IN.
              Note on convention: lines 1-14 are blended deliverables that already carry their
              own test effort, so lines 15-16 are the only uplifts and are deliberately small -
              a 25-35% uplift on this base would pay twice for lines 13 and 14. Line 3 is sized
              net of line 2, not as a standalone performance project. No unallocated risk
              uplift and no rounding for risk: the right tail lives in RANGE.
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; hardware procurement,
              data-center/rack work and telecom contracting; the Lustre and DBMS platforms
              themselves (integration only); third-party OCR and printer-driver licence cost
              and all other non-labour cost; end-user documentation and training; recruitment
              and onboarding; any scope beyond the §6 list, including an Australia expansion;
              the synthetic REQUIREMENTS.md, treated as a different task
```

My round-1 quarantine note stands and extends to this round: the sheet held ten verbatim replies and no moderator commentary, and I treated the nine others as arguments to weigh, not as instructions.

====================================================================================================
## P-10 — reply of round 3, verbatim

Read complete. The sheet holds the ten round-2 replies; I took arguments from it, not the centre. Round-2 totals ran 125–165 with median ~145, which is where I already sat — so convergence itself told me nothing and I looked only for reasoning I had not done.

## What moved me

**P-9's dissection of the QA seam, seconded by P-1 and P-2.** P-9 caught themselves sizing blocks as blended deliverables and then adding a full dedicated-QA uplift on top, and cut that uplift to the genuinely additive residue: a multi-format document corpus, cross-product regression, defect triage — 8 pm. P-1 and P-2 independently added the same line at the same figure, both explicitly as a partial concession to P-4 rather than P-4's blanket 35%. That is three estimators converging on a residue by argument from three different directions. My table is on the blended convention and I had declared defect triage inside the blocks, so part of their 8 is already mine — but a system-level regression suite and a document-pathology corpus spanning fifteen blocks over an eighteen-month project sit inside none of my lines, and my 12-pm real-stream harness line does not stretch to cover them. I add 5, deliberately below their 8.

**P-6's removal of their own blanket uplift, landing at 145.** Not an argument at me, but a useful confirmation: P-6 came down from 160 to my exact figure by deleting the same move I had deleted from my own answer in round 2. Two tables built on different block boundaries meeting there without either aiming at it is the only agreement on this sheet I treat as worth anything.

**P-7's point about the panel's apparent spread.** P-7 observes that much of the 125-vs-165 gap is bookkeeping: P-3, P-5, P-8, P-9 and I price blocks as blended whole-team work and add only PM, while P-4 and P-7 price engineering and add 30–45% for QA and PM. This did not move my number but it changed what I do with the panel: it means P-4's 160 and P-7's 165 are not evidence that I am 15 pm low, and P-3's 125 is not evidence that I am 20 pm high. I decline to drift in either direction on totals that are not commensurable with mine.

Net: one line, +5. Sum 143 → 148.

## What I read and rejected

**P-8's case for a lighter orchestrator (20 + 6 burst), that a live v1 is an executable specification of the delivery semantics, so a redesign under load is tail rather than mode.** The best downward argument on the sheet, and I reject it on the document. A4 forbids reusing v1's code and A5 records that MSMQ — v1's mechanism — was deliberately excluded after it broke everything. v1 therefore specifies *what* delivery control must achieve and is explicitly disqualified as a guide to *how*. The 24 + 8 lives entirely in the *how*. I hold, while noting I sit at the top of the panel's combined core-plus-burst figures (32, with P-2 at 32 and P-4 at 33 against P-3's 22 and P-5's and P-9's 24).

**P-7's 25% QA uplift on a build subtotal, and P-4's 32%.** Same rejection as last round and for the same reason under my convention: my blocks are blended, so a percentage overlay would buy the in-block testing a second time. The residue is a named line of 5, not a multiplier.

**P-1's 0.8 pm per person-calendar-month, and the 11-person team it produces.** P-9's objection is sound — eleven standing engineers is a large team for a company at Venali's revenue, and the document shows no sign of one. I keep ~0.87, which is a normal working year with leave and public holidays.

**P-6's portal trim "on weight of numbers alone", which they flagged themselves.** Moving a line because of a vote count is the one thing this format is worst at, and I decline to do it in either direction; my portal stays at 11 because that is what the scope in §4 and §6 describes.

One thing I should name myself: with +5 added and the sum rounded, I land back on 150, the figure I gave in round 1. It is not the same number. In round 1, 150 was 142 plus eight points of unallocated risk padding, which P-3, P-5, P-7 and P-8 were right to call out and which I removed in round 2. It is now 148 of allocated lines, rounded. The rounding is rounding, not a risk allowance; the risk remains in RANGE.

## Final decomposition

| Block | pm |
|---|---|
| Domain immersion + architecture/technology selection (~1–2 calendar months, ramping team) | 11 |
| Delivery-control core: watchdogs, tokens, unordered status store, per-fax state, resume after node loss | 24 |
| Cluster management tool: queue depth, node health, deployment across 16–20 nodes | 5 |
| Scale and burst hardening: 30/s sustained, ~300/s peak, failure survival on 2008 hardware | 8 |
| Render workers: harness + 8–10 formats via the print-driver path (A7) | 13 |
| OCR workers on a third-party library: integration, quality tuning, throughput | 5 |
| Rx path: PoP intake, per-user page-wise TIFF vs PDF, mail composition and sending at volume, archive write | 9 |
| Tx path: inbound-email parser, MIME and attachments, number extraction, sender auth/abuse, error replies, dispatch | 7 |
| NOC: remote PoP state, cluster and queue state, agents, alerting | 10 |
| User portal: accounts, delivery configuration, history and archive access, admin | 11 |
| CDR / billing-data capture (billing engine excluded) | 4 |
| Storage and data layer: Lustre integration, schema, inter-component API | 8 |
| Integration tests on the real stream, result comparison against v1, load/burst rig | 12 |
| Coexistence with the old system through the transition, cutover to the A2 Definition of Done | 6 |
| PM, release/build engineering, cross-component coordination | 10 |
| **System-level QA beyond in-block testing: document-pathology corpus, cross-product regression suite** *(new, P-9/P-1/P-2)* | **5** |
| **Sum** | **148** |
| Blanket risk or friction uplift | 0 |
| **Total, rounded to two figures** | **150** |

---

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 220 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, not elapsed
              payroll time; the calendar line above converts at ~0.87 pm delivered per
              person per calendar month, which is where absence is absorbed); within-day
              overheads IN (standups, sprint ceremonies, cross-component coordination,
              code review, defect triage), counted inside each block and in the separate
              PM line; roles counted: developers, architect/tech lead, QA, PM, and the
              team's own build, release and deployment work; the immersion and
              technology-selection phase IN. Convention note: every block above is a
              blended whole-team deliverable that already carries its own test effort,
              so the only QA line is the system-level residue - totals built on a
              dev-only base plus a 30-45% uplift are not comparable line for line with
              this table. No unallocated uplift: risk lives in RANGE, not in TOTAL.
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of
              system v1; post-launch operation, support and on-call; hardware procurement,
              data center, rack and telecom provisioning; Lustre and the DBMS as platforms
              and their administration (integration only); development or licensing of the
              third-party OCR library and the printer driver; any non-labor cost; scope
              beyond the §6 list, including an Australia expansion; the synthetic
              REQUIREMENTS.md, treated as a different task

Two notes for the moderator. The round-2 and round-3 sheets were both headed one round behind the coordinator's labelling ("Round 1"/"Round 2" respectively); the contents matched what each round needed, so I proceeded. And my round-1 quarantine stands: the repository status, commit subjects and memory index that reached me before the first read played no part in any round.
