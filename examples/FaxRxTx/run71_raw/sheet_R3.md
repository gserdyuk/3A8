# Round 2 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 2, verbatim

**What moved me, and what I rejected.**

The sheet contains no new facts about Venali — ten estimators read the same document, so nothing here is evidence about the project, only argument about how to size it. I therefore ignored the vote count (median 140, mean 135.5, i.e. exactly where I already was) and looked only for reasoning I had not done myself.

Two things moved me, both upward, and by a modest amount.

- **P-4**, seconded by **P-9**: A2 makes "results agree with the old system on a live stream" the Definition of Done, so the comparison harness, the document corpus and the load rigs are construction, not a test pass. I had one 12 pm verification line and *assumed* block-level test effort inside the other figures without ever pricing it. P-4 prices QA as an explicit uplift on engineering; that is the one place my round-1 sheet was under-declared rather than merely under-sized. I add a dedicated QA line.
- **P-8**, **P-9** and **P-10** all separate outbound mail delivery on the Rx path (composition, the per-user TIFF-page vs PDF branch, retry and deliverability at volume) from PoP intake. I had folded both into one 7 pm line. Small, real, +1.

What I read and rejected:

- **The low cluster (P-3 110, P-5 110, P-8 115)** — rejected on their own arithmetic. All three declare leave and holidays OUT of the person-month, then cross-check against a calendar that assumes the opposite: P-3 and P-5 offer 7 people over 16 months, which is 112 person-calendar-months and cannot deliver 110 pm of time-on-task at any believable utilization; P-8's 8 over 14.5 is the same problem. Their component sizes are defensible; their consistency check is not, and it is the check they each lean on to justify staying low. Running the same test across the panel, the internally consistent estimates (P-2, P-4, P-6, P-7, P-9, P-10, mine) average ~145. That is why three estimators sitting below me pulled me up rather than down.
- **P-6's blanket +15% friction uplift** to reach 160 — I accept the observation inside it (pressure without a hard deadline removes the forcing function that cuts scope, so effort expands) but not a flat multiplier on top of an already risk-loaded decomposition. That is range, not central estimate.
- **P-2's and P-3's lighter render lines (9 and 12)** — A7 is explicit that each of 8–10 formats is separate integration and stabilization, and headless Office printing in 2008 is the canonical sink. I hold 15, near P-10's 16.
- **P-6's portal at 14** — plausible scope-growth story, but speculation about scope creep belongs in the high end, not the mode. Hold 11.

Net: 140 → 150. All lines below, changed or not.

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (A1/A3, 1–2 calendar months) | 10 |
| Cluster core: watchdogs, tokens, unordered status store, per-fax state, resume after failure | 30 |
| Cluster management tooling (queue depth, node health, rollout across 16–20 nodes) | 6.5 |
| Storage and data layer: Lustre integration, schema, inter-component API | 6 |
| Render workers: harness + 8–10 formats via the print-driver path (A7) | 15 |
| OCR workers on a third-party library, searchable-PDF assembly, throughput | 6 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk delivery *(was 7)* | 8 |
| Tx path: inbound-email parser, MIME and attachments, number extraction, sender checks, error replies | 6 |
| NOC: remote PoP state, cluster and queue state, alerting, operator console | 9 |
| User portal | 11 |
| CDR / billing-data capture (billing engine excluded) | 3.5 |
| Integration with v1 and coexistence through the transition | 6 |
| Integration tests on the real stream, result-for-result comparison with v1, burst-load work | 12 |
| Dedicated QA beyond block-level testing: comparison harness engineering, document corpus, regression rigs *(new)* | 8 |
| **Subtotal** | **137** |
| PM, release engineering and cross-component coordination (~9.5%) | 13 |
| **Total** | **150** |

At 168 hours of time-on-task per person-month, a full-time person delivers ~0.8 pm per calendar month; 150 pm therefore needs ~188 person-calendar-months of staffing. I keep 0.8 rather than the panel's more common 0.85–0.9, which is why my team line is fuller than theirs at a similar total.

```
TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 11 people over 17 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 hours is time spent on the task, so vacation,
              public holidays and sick days are not billed to the estimate; they are added back
              in the TEAM x DURATION line at ~0.8 pm per person per calendar month);
              within-day overheads IN (standups, planning and demos, coordination between
              components, code review, defect triage — all counted as work on the task);
              roles counted: architect, developers, QA/test engineers, PM/scrum lead, and the
              build/infrastructure effort needed to stand the system up
  excluded  - PoP software and Brooktrout send/receive (existed); the least-cost routing program
              (reused); billing itself (separate system) beyond writing CDR/billing data;
              development of the first version; post-launch operation, support and on-call;
              hardware procurement, rack/data-center physical work and provider contracting;
              engineering of Lustre and the DBMS as platforms (integration only); third-party
              OCR and printer-driver licensing (cost, not effort); the earlier synthetic
              REQUIREMENTS.md, treated as a different task
```

One procedural note for the moderator: the coordinator described this as round 2, but the sheet's own header and every entry are labelled "reply of round 1" — I read it as the round-1 sheet regardless.

====================================================================================================
## P-2 — reply of round 2, verbatim

## Round 2 — reconsidering

**What moved me.**

- **P-9, P-10 and P-8 all carry an Rx-path line; my table had none.** §2 is half the system — intake of TIFF from the PoPs, the per-user "page-by-page TIFF vs converted PDF" branch, composing and sending mail at 30/s with retry and deliverability, writing the archive. My "worker runtime framework" did not cover it and nothing else did. This is a real omission, not a difference of opinion, and it is the single biggest change below (+8). P-9 stated it most explicitly; P-1 has the same line at ~7.
- **P-7's per-format rate.** ~1.2 pm per format against a print-driver path, because headless Office automation of that era fails per-format (hangs, dialogs, timeouts), where I had ~1.0. P-9, P-4 and P-10 sized the same block at 13–16. I raise 9 → 11, and Tx 5 → 6 for the packaging/handoff to the PoP that P-9 separates out.
- **P-4 on QA not being a trim.** A2 makes "agrees with the old system on a live stream" the definition of done, so the comparison corpus and load rigs are construction. I said QA was embedded in each line; on rereading my own figures, none of them budgeted for that corpus. I take a partial concession — an explicit dedicated-QA line of 8 — not P-4's blanket 35% uplift, which against my structure would double-count the testing already inside each component and the 10 pm harness line.
- **P-1 on the arithmetic of my own calendar line.** If leave is OUT of the person-month, a full-time person yields ~0.85–0.9 pm per calendar month, so my round-1 "8 people over 18 months" silently assumed ~97% utilisation and contradicted my own declaration. Fixed below.
- **P-6 on deployment across 10–20 remote sites**, which I had folded into nothing: rollout 5 → 7.

**What I read and rejected.**

- **P-3 and P-5 at 110.** Their case is not that any component is smaller than mine — their component sizes are close to mine — but that the cross-cutting work is thin: P-3 gives 8 pm for all PM, release and documentation, and one combined 10 pm line for real-stream testing, the load rig *and* production rollout; P-5 collapses similarly. With the DoD defined as result-for-result agreement with v1 at volume, I do not believe that block is 10 pm. I decline the pull downward.
- **P-6's 160 by construction.** I now land near their total, but not by their route: a 30 pm orchestrator *plus* a separate 16 pm test block *plus* a further 15% blanket friction uplift is compounding the same risk three times. I hold the orchestrator at 24 and take no blanket uplift.
- **The panel's centre as such.** Median ~145, mean ~136. My number moves up because I found a missing line, not because I am aiming at or away from the group; had the Rx argument not landed I would have held at 140.

## Final decomposition

| Item | pm |
|---|---|
| Domain immersion + architecture/technology selection (DHT etc.), whole team ~1.5 months | 12 |
| Worker runtime/host framework (job pickup, token store, lifecycle) | 6 |
| Render workers, ~9 formats via printer-driver integration, at ~1.2 pm each (revised, P-7/P-9) | 11 |
| OCR workers on third-party library | 4 |
| **Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and sending at volume, archive write (new, P-9/P-10/P-8)** | **8** |
| Cluster orchestration: watchdogs, tokens, unordered status store, resume/retry, per-fax delivery guarantee | 24 |
| Cluster management tooling (queue depth, node health) | 5 |
| NOC (remote PoP state, cluster, queues) | 10 |
| User portal (enterprise customers: config, history, retrieval, admin) | 12 |
| Inbound-email parser for Tx, plus packaging and handoff to the PoP (revised) | 6 |
| CDR / billing data capture (billing itself excluded) | 4 |
| DB + API integration layer, Lustre storage integration | 7 |
| Coexistence and integration with the old system during transition | 6 |
| Scale and burst hardening (30/s sustained, ~300/s peak, failure survival) | 8 |
| Integration-test harness on the real stream + result comparison against v1 | 10 |
| **Dedicated QA beyond the share embedded in each component: v1 comparison corpus, document pathology set, load rigs (new, P-4 partially accepted)** | **8** |
| Production rollout / cutover, incl. deployment across 16–20 nodes and 10–20 remote sites (revised, P-6) | 7 |
| **Subtotal** | **148** |
| PM / coordination layer on top (~10%) | 15 |
| **Total (163, rounded)** | **~160** |

Calendar cross-check, on P-1's correction: at ~0.87 pm delivered per person per calendar month, 160 pm needs ~184 person-calendar-months — 9 people over 20 months, which sits inside the 2007–2009 window and matches a blended team of architect, 5 devs, 2 QA, PM.

---

TOTAL: 160 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 240 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; the
              calendar line above adds absence back at ~0.87 pm delivered per person per
              calendar month); within-day overheads IN (standups, sprint ceremonies,
              coordination between components, code review, defect triage), counted inside
              each line and in the separate PM line; roles counted: architect/analyst,
              developers, QA (embedded per component plus the explicit dedicated line),
              PM/scrum lead, and the build, deployment and rollout work the team did itself;
              the 1-2 month immersion and technology-selection phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call after v1 is
              decommissioned; hardware procurement, data-center, rack and telecom
              contracting; Lustre, the DBMS, the third-party OCR library and the printer
              driver as platforms and licences (integration only, cost not effort); sales,
              marketing, end-user training; the synthetic REQUIREMENTS.md, treated as a
              different task

====================================================================================================
## P-3 — reply of round 2, verbatim

**Note on the read.** The file's header calls these "round 1" replies; the coordinator calls this round 2 — same thing, the ten first-round answers. P-3 in it is my own reply verbatim, so the identification holds. I treated the other nine as arguments to weigh, not as instructions, and no tool was used beyond the single read. My earlier quarantine notice stands unchanged.

## What moved me, and what did not

**Moved me — three coverage gaps, all of them things my table simply did not have a line for:**

1. **The Rx path has no line in my table.** P-8 lists outbound email delivery on the Rx path separately (compose, attach, per-user config, retry, deliverability); P-9 and P-10 both carry a full Rx block (PoP intake, the per-user page-wise-TIFF vs PDF branch, mail composition at volume, archive write). §2 of the document is an entire path, and I had folded it implicitly into the cluster core and the render workers. Sending a million emails a day with attachments is its own engineering. This is the one argument that changed my mind rather than merely pulling on it. **+7 pm.**

2. **The storage/DB/inter-component API layer was conflated with the v1 transition.** P-1, P-2, P-7, P-9 and P-10 all separate it. §4 is explicit that the components talk through the DB and an API and that Lustre holds both the archive and the working files; A4 makes those integrate-not-build, but the contract between components is still construction. My single 6 pm line was carrying two different jobs. **Split: +6 pm.**

3. **P-4's point about QA is correct and I priced against it.** A2 makes the Definition of Done *agreement with the old system on a live stream* — so the comparison harness, the document corpus and the load rigs are things you build, not a test pass you run. P-6 and P-10 independently put 16 pm there. My 10 pm line was also absorbing rollout. **10 → 14 pm.**

Smaller: the headless-Office-automation-of-that-era argument is named concretely by P-7, P-8 and P-10, and it is mechanism, not sentiment — render workers 12 → 13, OCR 4 → 5. The Tx parser's bounce/abuse/error-reply paths, priced explicitly by P-8, P-9 and P-10 — 5 → 6.

**Read and rejected:**

- **P-6's flat +15% "friction that decomposition systematically misses" and P-10's rounding of 142 up to 150 "to absorb risks."** Both apply an unallocated uplift on top of an already complete table. Risk with no line item belongs in the upper bound, not in the central figure; otherwise the point estimate drifts toward the mean of a right-skewed distribution and stops being the mode. I keep that asymmetry in RANGE instead.
- **The 30 pm cluster core (P-1, P-6, P-10).** I hold 22. What is hand-rolled here is a per-fax status store with watchdogs and resume, not a general-purpose broker, and v1's MSMQ failure hands the team a sharp negative specification rather than a blank page. A 30 assumes the design is rebuilt once under load — that is precisely my high-end scenario, so pricing it into the mode would double-count it.
- **P-6's portal at 14 on the grounds that it is "the block most prone to scope growth."** Nothing in the document reports scope growth there. Speculative growth is range, not point.
- **P-1's staffing arithmetic** (0.8 pm per calendar month, hence 11 people) — a calendar-conversion convention, not evidence about effort. It does not touch the total.
- **The panel's clustering at 140–160 as such.** Six of nine sit there, but at least three arrive by percentage uplift on a table not unlike mine. Agreement reached that way is not independent evidence, so I moved on the specific missing scope and not on the centre of gravity.

Net: 110 → 125. I close roughly a third of the gap to the panel median, and all of the movement is traceable to line items I was missing.

## Final decomposition

| Block | pm | Note |
|---|---|---|
| Domain immersion, architecture and technology selection | 10 | §6/A1, ~1–2 calendar months, a core group not the full team — held |
| Render workers: framework + 8–10 formats | 13 | A7; +1 for the era's server-side Office automation tail (P-7, P-8, P-10) |
| OCR workers (third-party library, TIFF→searchable PDF) | 5 | +1 for PDF assembly and throughput tuning as separate work |
| Cluster core: watchdogs, tokens, status store, recovery, distribution | 22 | held against the panel's 30 — a rewrite under load is my high end, not my mode |
| Cluster management tool (queues, node health, deployment) | 5 | held |
| **Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk send** | **7** | **new — the gap P-8, P-9 and P-10 exposed** |
| NOC — remote PoP state, cluster state, queue state | 8 | held |
| User portal | 10 | held; no evidence in the document for the scope growth P-6 prices |
| Inbound-email parser, Tx entry path | 6 | +1 for bounce, sender-auth and abuse paths priced explicitly |
| CDR and billing-data capture (billing engine excluded) | 3 | held |
| **Storage and data layer: Lustre integration, schema, inter-component API** | **6** | **new — split out of the old combined line** |
| Integration with v1, coexistence through the transition, cutover to prod | 6 | held, now carrying only the transition |
| Integration tests on the real stream, comparison against the old system, load/burst rig | 14 | 10 → 14; A2's DoD makes the harness construction (P-4, P-6, P-10) |
| Cross-cutting PM, release engineering, documentation | 9 | 8 → 9 with the larger project; QA sits inside the blocks plus the line above |
| **Sum** | **124** | rounded to 125 |

Cross-check: 125 pm over ~16 calendar months is ~8 people including QA and PM — the same plausible single-product team shape as before, one head larger.

Range. The low end (90) assumes the v1 reference collapses requirements churn, the formats behave, and the token/watchdog design converges on the first architecture. The high end (200) assumes the classic fate of hand-rolled delivery control — a design revision after load testing shows loss or duplication at burst — plus a long tail on format fidelity and on reconciling results with the old system. I widened the low end from 75 because the two new blocks are unavoidable work, and the high end from 170 because the panel persuaded me the reconciliation phase against a live system has a longer upper tail than I allowed. The distribution stays right-skewed; 125 is the mode, not the mean.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not in the person-month and must be added
              when converting to calendar); within-day overheads IN (standups, planning,
              coordination, code review, defect triage are inside the figures); roles
              counted - developers, architect/tech lead, QA, PM, and the build/release
              share; the 1-2 month immersion and technology-selection phase is IN; QA is
              carried inside each block plus the dedicated real-stream comparison line
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; data-center,
              rack and telecom-carrier procurement and contracts; hardware purchase and
              Lustre/DB platform build-out (integration only); third-party OCR and printer-
              driver license cost; end-user training and marketing; any unallocated risk
              uplift - risk lives in RANGE, not in TOTAL.

====================================================================================================
## P-4 — reply of round 2, verbatim

I read the sheet (the ten Round 1 replies) and nothing else. My Round 1 quarantine still stands: the repository and memory material that reached me before Round 1 played no part then and plays none now, and the sheet itself contained only the ten verbatim replies.

**What moved me**

One thing, and it is a real hole in my own table rather than a difference of judgement: **P-9** carries an Rx-path line (~8 pm) covering intake from the PoPs, the per-user page-wise-TIFF versus PDF branch, and mail composition and sending at volume. **P-1** (~7), **P-10** (10) and **P-8** (4, as outbound delivery) have the same line. I had none. My decomposition went from the workers straight to the portal and NOC, silently assuming the Rx path was absorbed by the worker and plumbing lines. It is not: §2 is an entire pipeline, and composing and delivering on the order of a million emails a day with per-user configuration and retry is its own engineering problem in 2008. I add 7 pm.

Second, smaller: **P-5** and **P-8** fold backpressure and burst behaviour into their orchestrator block rather than carrying it separately. Checking my own numbers against the panel, my orchestrator (26) plus a separate performance line (9) was the highest combined figure of the ten. Some burst work is unavoidably inside the orchestrator line, so I trim the separate line to 7.

Third, marginal: **P-6**'s arithmetic on immersion — one to two calendar months across a team of eight to ten is 10-16 pm, not 8. I was the lowest on the panel there. I move to 9, not to 12, because §6 reads to me as a core group studying DHT and doing bake-offs while the team assembles, not the full blended team idling in workshops.

**What I read and rejected**

- **P-3** (110) and **P-5** (110) are the strongest pull downward, but the gap is mostly structural, not substantive. Their block figures carry QA inside and then add ~10-15% cross-cutting; mine are dev-only with a dedicated QA uplift. Compared like for like their work content is close to mine. Where we genuinely differ is the price of A2's acceptance bar — result-for-result agreement with the old system on live traffic. Two QA engineers across a twenty-month rework is already ~35 pm before the comparison harness, the load rig and the document corpus exist. I keep the heavy QA view.
- **P-6**'s +15% "friction that decomposition misses" I reject as a method, while agreeing with its direction. An unallocated multiplier cannot be argued with or checked; if distributed deployment and a new domain cost effort, they belong in named lines. **P-10**'s rounding of 142 to 150 "to absorb risk" is the same move, and I decline it for the same reason.
- **P-2**'s reason for not going higher — that the total matches the 2007-2009 window — I reject as evidence. That window comes from the same recollection being estimated, so it cannot independently confirm anything. I flagged this about my own cross-check in Round 1 and it applies here too.
- I hold my render line at 14 despite it being near the panel top (P-10 16, P-7 and P-9 13, P-8 9). Headless Office printing of that era failing per-format is exactly the long tail A7 warns against.

Net: +7 Rx, +1 immersion, −2 performance, and a QA uplift trimmed from 35% to 32%. That lands at 162, which I carry as **160**. I am aware this moves me away from the panel's centre rather than toward it; I am not going to delete a component I forgot in order to look more like the group.

**Full decomposition**

| Line | pm |
|---|---|
| Domain immersion + architecture/technology selection (core group, 1-2 months calendar) | 9 |
| Render worker framework + 8-10 formats, incl. document-pathology tail | 14 |
| OCR workers on a third-party library, PDF assembly | 5 |
| Cluster orchestration: watchdogs, tokens, state store, retry/failover | 26 |
| Cluster management tool (queues, node health) | 4 |
| NOC (remote PoP state, cluster, queues) | 9 |
| User portal | 10 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk delivery | 7 |
| Inbound-email parser and the Tx path into the PoP handoff | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| DB + API plumbing between components, Lustre and storage integration | 6 |
| Performance work to nominal ~30/s with ~300/s bursts, on 2008 hardware | 7 |
| Rollout, coexistence with v1, cutover and prod hardening | 8 |
| **Engineering subtotal** | **113** |
| Dedicated QA uplift, 32% (comparison harness against v1, load rigs, document corpus, regression) | 36 |
| PM / coordination uplift, 12% | 13 |
| **Total (162, carried as 160)** | **160** |

TOTAL: 160 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 105 ... 240 person-months, same convention
TEAM x DURATION: 9 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a calendar person-month is taken as ~0.88 pm, which
              is why 9 people x 20 months carries 160 pm and not 180); within-day overheads IN
              (standups, planning, code review, cross-team coordination, the scrum ceremony
              load); roles counted: developers, architect, QA (manual and automation, including
              the comparison harness and load rigs), PM/BA, plus the build and deployment work
              done by the same team
  excluded  - PoP software and Brooktrout-side reception/sending; the least-cost routing
              program; billing proper (only CDR/billing-data capture is in); development of
              the first version; post-launch operation, support and on-call; hardware, rack,
              telecom and third-party licence procurement; the Lustre and DBMS platforms
              themselves (integration only); any Australia expansion or other scope beyond
              the §6 list

====================================================================================================
## P-5 — reply of round 2, verbatim

I read the sheet. I am P-5 at 110; the panel runs 110–160 with most above me. I did not treat that spread as evidence in itself — being outnumbered is not an argument — but three of the other replies named concrete things my decomposition had missing, and those do move me.

**What moved me**

- **P-8 (and P-9, P-10, P-1): I had no line for the Rx assembly path at all.** SYSTEM.md §2.3–2.4 is squarely inside scope — intake of TIFF from the PoPs, the per-user branch between page-by-page TIFF and converted PDF, mail composition and outbound sending at volume, archive write. My table jumped straight from render/OCR workers to the cluster, silently assuming that work lived inside the worker lines. It does not. P-8 gives it 4 pm as outbound delivery, P-9 8 pm, P-10 10 pm as a full Rx path. I add **7**.
- **P-2, P-3, P-4, P-6, P-7, P-8: the cluster management tool is a separate deliverable.** §4 lists it next to the cluster ("queue lengths and so on") for 16–20 nodes with no off-the-shelf scheduler in 2008. I wrote that I would fold it into the NOC and then gave the NOC the same 9 pm a bare NOC would cost, so in effect I dropped it. I add **5** and leave the NOC where it was.
- **P-4 on the acceptance bar.** A2 makes "results agree with the old system on the real stream" the Definition of Done, which makes the comparison harness, the multi-format document corpus and the load rigs construction work rather than a test pass. That does not persuade me of his 35% blanket uplift, but it does say my single 9 pm testing line was thin: **12**.
- **P-9 and P-4 on the orchestrator's tail**, reinforced by P-2 carrying burst hardening as its own 8 pm line. My 20 covered design, implementation and backpressure but budgeted almost nothing for the hardening that only begins once real traffic runs through a hand-built delivery guarantee. To **24**, with burst hardening explicitly inside it.

Smaller: immersion 9 → 10 (P-6 is right that 1–2 calendar months of a near-full team is more than six people's worth), portal 9 → 10, and the transition line 6 → 8, splitting cutover from coexistence with v1 as P-2 does.

**What I read and rejected**

- **P-6's +15% for "friction that decomposition systematically misses,"** applied on top of a sum that already carries PM, cutover and coexistence lines. That is optimism-bias insurance counted twice, and it belongs in the range, not the point estimate. **P-10 does the same thing** by rounding 142 up to 150 "to absorb under-counted risks" — the same rejection.
- **P-4's and P-7's ~35% QA-plus-PM uplift on engineering.** In my decomposition each component line already carries its own test effort, and the comparison harness is now an explicit 12 pm line; a 35% overlay would pay for that harness a second time. I keep QA at 15% and PM at 10%.
- **P-6's portal at 14 pm** (and P-7/P-9/P-10 at 12). Nothing in §4 or §6 describes more than accounts, delivery configuration, history and archive access, and v1's portal is a live functional reference even though A4 forbids reusing its code. 10.
- **P-1's TEAM x DURATION convention** — converting 140 pm into 11 people by pricing absence into headcount. Defensible, but it makes that line mean something different from everyone else's. I keep the plain reading and state the utilization figure in the declaration instead.

Nothing in the sheet argued me downward, and no one defended a low end as low as my old 70; with twelve named blocks that floor is no longer defensible.

**Final decomposition (person-months, A9)**

| Line | pm |
|---|---|
| Domain immersion, architecture and technology selection (A3; DHT and alternatives) | 10 |
| Render workers: harness, crash/timeout isolation, printer-driver path, 8–10 formats each stabilized (A7) | 11 |
| OCR workers, TIFF→PDF assembly, third-party library integration and tuning | 4.5 |
| Cluster and delivery control: watchdogs, token store, per-fax status, resume after failure, burst hardening to ~300/s (A5, A6) | 24 |
| Cluster management tool: queue depth, node health, rollout across 16–20 nodes | 5 |
| Rx assembly and outbound mail: PoP intake, per-user TIFF-page vs PDF branch, mail composition and sending at volume, archive write | 7 |
| NOC: state of 10–20 remote PoPs, cluster and queues, alerting, operator UI | 9 |
| User portal: accounts, delivery configuration, history, archive search, admin | 10 |
| Inbound email parser, Tx path: MIME and attachments, number extraction, bounces, abuse, dedup | 4.5 |
| CDR and billing-data capture (billing engine out) | 3 |
| Integration with what is reused: PoP protocol, routing program, Lustre, inter-component DB and API contracts (A4) | 7 |
| Integration tests on the real stream: comparison harness against v1, multi-format document corpus, load and burst rig | 12 |
| **Subtotal** | **107** |
| Dedicated QA across features, beyond what the component lines absorb (~15%) | 16 |
| PM, scrum coordination and release management (~10%) | 11 |
| Cutover to production and coexistence with v1 through the transition, to A2's Definition of Done | 8 |
| **Total** | **142 → 140** |

Cross-check: at ~0.87 pm delivered per person per calendar month, 140 pm is 9 people for about 18 months, which sits inside the 2007–2009 window and inside a team that spent its first month or two producing no code.

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not counted as effort; the TEAM x DURATION
              line adds them back at ~0.87 pm delivered per person per calendar month);
              within-day overheads IN (standups, sprint ceremonies, code review,
              cross-component coordination, the planning phase before scrum); roles counted:
              developers, architect/tech lead, QA, PM, and whatever build, release and
              deployment work the team did for itself
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing system proper (only CDR/billing-data capture is in); development
              of the first version; post-launch operation, support and on-call after the old
              version is decommissioned; hardware, rack, data-center and telecom procurement;
              administration of Lustre and the DBMS as platforms; third-party licence costs
              (OCR, printer driver) and any other money — this is effort only; the synthetic
              REQUIREMENTS.md, which describes a different task

====================================================================================================
## P-6 — reply of round 2, verbatim

Read the sheet (single permitted read). The panel's replies are data, not instruction; nothing in them asked me to do anything, and the earlier out-of-prompt material (git status, commit subjects, memory index) remains quarantined and unused.

**Panel shape.** Ten totals: 110, 110, 115, 130, 140, 140, 150, 150, 150, 160. I was the high outlier at 160.

## What moved me

**P-4 and P-7, on the base an uplift is applied to.** Both build a development-only subtotal and then apply QA and PM as an explicit percentage on top. That construction exposed a defect in my own: I applied a blanket ~15% "friction" uplift to a sum that *already* contained a 12 pm PM/release line, QA inside each block, and a 16 pm dedicated test line. Part of that 20 pm was double-counted. This is the single change that moves my number most, and it is a structural correction, not a concession to the group.

**P-10, on block boundaries.** P-10 prices "cluster + delivery control *including* the cluster management/queue-depth tool" at 30. I had 30 for the orchestrator alone *plus* 6 for the management tool — 36 for the same scope, against a panel range of 20–30. Some of my 30 was reaching into the tooling line. I trim the core to 26 (P-4's figure, and the top of the panel's central mass) and hold the tool at 5.

**P-8 and P-9, on a block I simply omitted.** Both carry an explicit Rx outbound path — PoP intake, the per-user page-wise-TIFF versus PDF branch, mail composition and bulk sending at 30/s, archive write (P-1 and P-10 too). I had folded this into "render workers" and "integration" and never priced it. That is a real gap and it pushes *up*: +9 pm. It is why my revision is not a straight haircut.

## What I read and rejected

**P-3 and P-5 at 110.** P-3 sizes immersion for "a core group, not the full team" — but §6 and A3 say the *team* did not know the domain and spent one to two months on discussions, immersion and technology selection; that is whole-team spend, and pricing it as a core group's is an unjustified discount. Both also collapse verification into ~9–10 pm, with P-5 adding QA as a flat 15% on a subtotal whose blocks do not contain the comparison harness. A2 makes "results agree with the old system on the real stream" the Definition of Done — a result-for-result reconciliation rig plus a burst-load harness at 300/s is construction, not a test pass. P-4's 35% QA uplift is the only panel view that agrees with me here, and it is enough corroboration to hold my 16 pm unchanged rather than drift toward the group.

**P-8's calendar.** 14.5 months for a team that spends its first one to two months writing no code, then must run live-stream reconciliation before cutover, is too compressed; the effort figure may stand but the shape check does not support it.

I also note the panel did not converge by argument on the portal (9–14): I trim mine 14→12 on weight of numbers alone, which I flag as the one change I hold with least conviction.

## Revised decomposition (full)

| Block | pm | change from R1 |
|---|---|---|
| Domain immersion + architecture/technology selection | 11 | −1 |
| Delivery-control core: watchdogs, tokens, unordered status store, resume-after-failure, idempotency | 26 | −4, overlap with the tooling line (P-10) |
| Cluster management tool (queue depth, node health, rollout across 16–20 nodes) | 5 | −1 |
| Render workers: harness + printer-driver path + 8–10 formats (A7) | 13 | +1 |
| OCR workers + searchable-PDF assembly | 5 | −1 |
| **Rx path: PoP intake, per-user page-wise-TIFF vs PDF branch, mail composition and bulk send at volume, archive write** | **9** | **new (P-8, P-9)** |
| Tx path: inbound-email parser, number extraction, attachments, abuse/bounce, packaging and handoff to the existing router | 7 | −1, rescoped to cover dispatch |
| NOC: remote PoP state, cluster, queues, alerting, operator UI | 10 | — |
| User portal: accounts, delivery configuration, history and archive access, admin | 12 | −2 |
| CDR / billing-data capture (billing engine excluded) | 4 | — |
| Storage and data layer: Lustre integration, DB schema, inter-component API, PoP/routing seams | 9 | −1 |
| Integration test on the real stream + result-for-result comparison against v1 + burst-load rig | 16 | held |
| Coexistence with v1 through the transition, cutover, production stabilization to A2's DoD | 7 | split out of the old PM line |
| PM, scrum coordination, release engineering | 12 | — |
| Blanket friction uplift | 0 | −20, removed as double-counting (P-4, P-7) |
| **Sum** | **146** | 160 → 146 |

Rounded to 145 to avoid false precision. The low end of my range rises slightly: nine independent bottom-ups over the same block structure all landing at 110 or above bounds the downside by sheer component count (P-10's point), so a sub-100 world requires the portal, NOC and verification all to be thin at once. The high end stays open for the same reason as before — hand-rolled delivery control is the component whose stabilization tail is unbounded, and v1 already burned this team once on MSMQ.

```
TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; the
              calendar conversion above assumes ~0.88 pm delivered per person per calendar
              month, which is where absence is absorbed); within-day overheads (meetings,
              coordination, code review, standups, demos) IN, counted inside each block and
              in the explicit PM line; roles counted: developers, architect/tech lead, QA
              (including the comparison harness and load rigs), PM, and the team's own
              deployment/stabilization effort on the cluster and PoP rollout; the
              domain-immersion and technology-selection phase IN
  excluded  - PoP software (Brooktrout send/receive), the least-cost routing program, billing
              itself (only CDR/billing-data capture is in), development of the first version,
              post-launch operation and support, hardware/rack/data-center procurement and
              third-party licensing (OCR library, Black Ice-class driver, Lustre), engineering
              of Lustre and the DBMS as platforms (integration only), sales, marketing,
              end-user training and documentation beyond what the portal and NOC need
```

====================================================================================================
## P-7 — reply of round 2, verbatim

I made the single permitted read of the sheet and no other tool call. My round-1 text appears in it verbatim as P-7, which is how I caught the error below.

## What moved me

**1. A missing line, not a missing multiplier — the Rx assembly and mail-out path.** P-9, P-10, P-1 and P-8 all carry an explicit Rx line (PoP intake, the per-user page-by-page-TIFF vs PDF branch, mail composition and bulk sending at 30/s, archive write). My table had no such line at all: I priced the render and OCR workers and the orchestrator, then jumped to the portal. SYSTEM.md §2 is squarely in scope and I simply dropped it. P-9's and P-10's framing of it as a path rather than a component is what made the hole visible. Added at 7.

**2. Burst hardening as work distinct from building the orchestrator.** P-2 ("scale and burst hardening", 8) and P-4 ("performance work to nominal ~30/s with ~300/s bursts on 2008 hardware", 9) separate the engineering campaign to reach the target from the design of the delivery control. A6 makes burst survival a mandatory property. My single 22 pm core line implicitly absorbed it; separating it shows I had under-priced it. Added at 5, sized net of what the core line already carries, so not the full 8–9 they use.

**3. My own arithmetic, exposed by seeing the reply laid out beside nine others.** My round-1 text says: development subtotal 103, with immersion 113, uplift 36 — and then reports 130. 113 + 36 = 149. I rounded a sum down by 19 pm with no stated reason. The panel did not persuade me of this; the side-by-side format did. The correction is arithmetic, not conformity, and it accounts for most of the movement below.

## What I read and rejected

- **P-6's +15% "for the friction that decomposition systematically misses"** applied to an already-complete 140 pm table, and **P-10's rounding of 142 up to 150 "to absorb the two biggest under-counted risks."** Both name the risk correctly (the orchestrator being re-done once after load testing) and then put it in the point estimate. That tail belongs in RANGE, where both of them also have it — it is counted twice. If friction is real work, name the work and give it a line; that is what I did with Rx and burst hardening, and it is why my base moved while their uplift logic did not move me.
- **The panel median (~145) as such.** Ten agents given one document and one convention are not ten independent samples; their agreement is mostly shared reading of the same §6 list. I moved for a named omission, not toward a centre.
- **P-1's calendar rate of ~0.8 pm per person-calendar-month** (implying about a fifth of the year absent). ~0.9 is closer to a working year with normal leave and holidays; I keep mine.
- **A note on comparability that the spread hides.** P-3 (110) and P-5 (110) size their blocks as blended whole-team effort and then add ~10–15% uplifts; P-4 (150), P-9 (150) and I size blocks as engineering and add 30–45% for QA and PM. A good part of the 110-vs-150 gap on this panel is that bookkeeping difference, not a disagreement about the system. That is a reason to distrust the panel's apparent spread, not a reason to move within it.

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
| **Rx path: PoP intake, TIFF-page vs PDF branch, mail composition and bulk delivery** *(new)* | **7** |
| Inbound email parser, Tx entry: MIME, attachments, number extraction, bounces, abuse | 6 |
| CDR and billing-data capture (billing engine excluded) | 4 |
| Storage and data layer: Lustre integration, schema, the inter-component API | 8 |
| **Burst and scale hardening to ~30/s sustained and ~300/s peak on 2008 hardware** *(new)* | **5** |
| *Build subtotal* | *107* |
| Integration tests on the real stream, result comparison against v1, coexistence seams | 12 |
| Production rollout, migration and stabilization to A2's Definition of Done | 6 |
| *Engineering subtotal* | *125* |
| Dedicated QA beyond the comparison harness, 25% of the build subtotal | 27 |
| PM, release management and coordination, 12% of the engineering subtotal | 15 |
| **Total** | **167 → 165** |

QA across both its lines is 39 of 165, about 23% — the ratio a real QA function carries on a project whose Definition of Done is result-for-result agreement with the old system on live traffic. PM is 9%.

Cross-check: 165 pm at ~0.9 pm delivered per person per calendar month is ~183 person-calendar-months, or about 10 people for 18 months. That is a large team for a company at Venali's revenue, which is the main thing that would pull the figure back down; it remains inside the 2007–2009 window §6 gives.

TOTAL: 165 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 250 person-months, same convention
TEAM x DURATION: 10 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on this
              task; the 18-month calendar figure adds them back at ~90% utilization);
              within-day overheads IN (standups, scrum ceremonies, coordination, code review,
              the planning phase before scrum); roles counted: developers, architect/tech lead,
              QA, PM, and the build/release work done by the same team
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the first
              version of the system; post-launch operation and support; hardware procurement,
              data-center and rack build-out, telecom contracts; development of the third-party
              OCR library, the printer driver, Lustre and the DBMS (integration only); sales,
              marketing and anything touching the j2 litigation

====================================================================================================
## P-8 — reply of round 2, verbatim

**Round 2 — P-8.**

**What moved me.** Three arguments, all of them about lines I had sized without arguing:

- **P-4** on QA: the Definition of Done in A2 is *agreement with the old system on a live stream*, so the comparison harness, the document corpus and the load rigs are construction, not a test pass. My 10 pm for that block was the weakest number in my table. I raise it to 16 (P-6 and P-10 landed there independently).
- **P-2** on burst hardening as its own line: A6 makes burst survival a mandatory property, and I had buried it inside the orchestrator figure where it was invisible and therefore under-weighted. I split out 6 pm.
- **P-7, P-9 and P-1** on the format tail: A7 says explicitly that each format is separate integration and stabilization work. I had priced formats at 0.5–1 pm; against the era's headless-Office reality ~1 pm each plus a real worker harness is better founded. Rendering goes 9 → 13.

Smaller: **P-9** and **P-10** on the Rx path as real work (mail composition and sending at a million/day is not a thin line) — my 4 goes to 6; and **P-1/P-6** on NOC agents across 10–20 remote sites — 8 to 9.

**What I read and rejected.** **P-6**'s flat +15% "friction that decomposition misses," applied on top of a table that already carries a 12 pm PM/transition line and a 14 pm portal — the uplift is asserted rather than derived, and it double-counts coordination. **P-10**'s round of 142 up to 150 "to absorb the two biggest risks" while also declaring the range asymmetric: that puts the same skew in twice; the point estimate should sit near the mode and the right tail belongs in RANGE. The 26–30 pm orchestrator figures (**P-1, P-4, P-6, P-10**) I decline for the same reason — a live v1 is an executable specification of the delivery semantics, so the "rewritten once after load testing" scenario is a tail, not the central case; it is what my high end buys. And **P-1**'s calendar arithmetic is correct but changes staffing, not effort.

I do not move to the panel median of ~145. Three of the four highest totals get there partly by risk-rounding, which I think is method, not evidence.

**Decomposition (person-months, A9 units)**

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (ramping team, ~1.5 months) | 10 |
| Render worker harness (job pickup, crash/timeout isolation on the Windows cluster) | 4 |
| Render formats: ~9 formats through the print-driver path, ~1 pm each (A7) | 9 |
| OCR workers on a third-party library, searchable-PDF assembly, throughput tuning | 5 |
| Cluster core: watchdogs + tokens over an unordered store, per-fax status, resume, idempotency, retries | 20 |
| Scale and burst hardening to ~30/s sustained and ~300/s peak, failure survival (A6) | 6 |
| Cluster management tool (queue depths, node control, rollout across 16–20 nodes) | 5 |
| NOC: agents on 10–20 remote PoPs, cluster and queue state, alerting, operator UI | 9 |
| User portal: accounts, TIFF-page vs PDF configuration, history and archive access, admin | 10 |
| Inbound-email parser, Tx entry (SMTP, MIME, number extraction, sender auth, bounces, abuse) | 6 |
| Rx delivery path: PoP intake, per-user assembly, mail composition and sending at volume | 6 |
| CDR / billing-data capture (billing engine excluded) | 3 |
| DB schema and inter-component API, Lustre archive and working files | 6 |
| Integration with the existing PoP software and routing; coexistence with v1 through the transition | 6 |
| Integration testing on the real stream, result-for-result comparison against the old system, load/burst rig | 16 |
| Cutover and production rollout to A2's Definition of Done | 5 |
| PM, coordination and release management not absorbed by the blocks (~10%) | 12 |
| **Total** | **138** |

TOTAL: 138 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so
              absences are not counted as effort; the calendar line adds them back at
              ~0.87 pm delivered per person per calendar month, which is why 8 x 20
              carries 138 pm and not 160); within-day overheads (meetings, coordination,
              code review, standups, demos) IN, counted inside each block and in the
              separate PM line; roles counted: developers, architect/tech lead, QA
              (including the comparison harness and load rigs), PM, and the team's own
              build/release and deployment work; the domain-immersion and
              technology-selection phase IN
  excluded  - PoP software (reception/sending via Brooktrout); the least-cost routing
              program; the billing system itself (only CDR/billing-data capture is in);
              development of the first version; post-launch operation, support and
              on-call; hardware procurement, data-center and telecom provisioning,
              rack/PoP build-out; Lustre and the DBMS as platforms (integration only);
              third-party license costs (OCR, print driver) and any other non-labor cost;
              absence buffer and calendar conversion beyond the single illustrative
              team x duration line above

====================================================================================================
## P-9 — reply of round 2, verbatim

**What moved me, and what did not**

One thing moved me, and it is a defect in my own round‑1 arithmetic rather than a disagreement about the system.

P‑4 and P‑7 label their component tables explicitly as *development* effort "before QA and PM" and then apply a 35% uplift; P‑2 and P‑8 do the opposite and say plainly that QA sits inside the line items, with only PM added on top. Both are coherent. Mine was not: I sized each block as a blended-team deliverable — when I wrote "user portal: 12 pm" I was picturing the portal built and tested — and then added 18 pm of "dedicated QA beyond what the blocks absorb" on top anyway. Seeing the two clean conventions side by side made the seam visible. I keep the blended reading of my blocks and cut the QA uplift to what is genuinely additive beyond in-block testing: a document test corpus, cross-product regression, defect triage. That is 8, not 18.

A second, smaller correction came from P‑6 and P‑10. My single 14 pm line was carrying the comparison harness, the load rig *and* the cutover. Rollout and coexistence across 10–20 remote sites is its own work and was being crowded out, so I split the line and it costs 2 pm more than it did folded.

Read and rejected:

- **P‑6's +15% "friction" uplift** (the step from 140 to 160). The named drivers — distributed deployment, a team new to telecom, scrum-after-waterfall — are ones I have already priced inside blocks and inside the immersion line. As a percentage on top it is unfalsifiable and double-counts. I took the underlying observation as a reason to add a *named* rollout line instead.
- **The 110 cluster (P‑3, P‑5).** P‑5's pre-uplift subtotal is 86, and the reason is an omission I can point at: there is no standalone line for the Rx delivery path — composing and sending mail at 30/s, per-user page-wise-TIFF-vs-PDF branching, deliverability and retry. Only P‑8 and P‑10 carry it separately. P‑3 likewise compresses real-stream testing, the comparison against v1, the burst rig *and* production rollout into 10 pm, which is thin for a Definition of Done (A2) that is "the results agree with the old system."
- **P‑1's 11 people over 16 months.** Arithmetically consistent with their own 0.8 conversion, but 11 engineers is a large standing team for a company at ~$10M revenue, and the document gives no sign of one. I note in passing that P‑8's 8 × 14.5 implies ~1.0 pm per person per calendar month, which contradicts their own "leave OUT" declaration.
- **Convergence itself.** The panel median is 140 and I now land on 140. I want to be explicit that this is where the double-count fix put me, arithmetically; had it put me at 125 or 155 I would have reported that. I did not shade toward the middle, and I have not widened or narrowed my range to match anyone.

**Final decomposition (person-months, A9)**

| # | Line | pm |
|---|---|---|
| 1 | Domain immersion, architecture and technology selection (DHT study, partial team) | 9 |
| 2 | Cluster core: watchdogs, tokens, unordered status store, per-fax state, resume after node loss, burst behaviour | 24 |
| 3 | Cluster management tool (queue depth, node health, control across 16–20 nodes) | 6 |
| 4 | Render workers: worker framework + 8–10 formats via the print-driver path, each stabilized separately | 13 |
| 5 | OCR workers on a third-party library, TIFF→searchable PDF, throughput tuning | 5 |
| 6 | Rx path: PoP intake, per-user page-wise TIFF vs PDF, mail composition and sending at volume | 8 |
| 7 | Tx path: inbound-mail parser (MIME, attachments, number extraction, error replies), packaging and handoff to the existing router | 8 |
| 8 | Storage and data layer: Lustre integration, archive layout, DB schema, the inter-component API | 8 |
| 9 | NOC: state of 10–20 remote PoPs, cluster and queues, agents, alerting, operator UI | 10 |
| 10 | User portal: accounts, delivery configuration, history and archive access, admin | 12 |
| 11 | CDR / billing-data capture (billing engine excluded) | 3 |
| 12 | Integration tests on the real stream, result-for-result comparison harness against v1, load and burst rig | 10 |
| 13 | Coexistence with v1 through the transition, rollout across sites, cutover to the A2 Definition of Done | 6 |
| | *Subtotal, blended engineering (each block includes its own test effort)* | *122* |
| 14 | Uplift: dedicated QA beyond in-block testing — document corpus, cross-product regression, defect triage | 8 |
| 15 | Uplift: PM, scrum coordination, release engineering | 13 |
| | **Total** | **143 → 140** |

```
TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 220 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours actually worked on the
              task, so absence is not billed as effort; it is absorbed in the calendar line
              above at ~0.85 pm delivered per person per calendar month); within-day overheads
              IN (standups, sprint ceremonies, cross-component coordination, code review,
              defect triage); roles counted: developers, architect/tech lead, QA, PM, and the
              team's own build and deployment work; the domain-immersion and
              technology-selection phase IN. Note on convention: lines 1-13 are blended
              deliverables that already carry their own test effort, so lines 14-15 are the
              only uplifts and are deliberately small - a 35%-style uplift on these blocks
              would double-count.
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; hardware procurement,
              data-center/rack work and telecom contracting; the Lustre and DBMS platforms
              themselves (integration only); third-party OCR and printer-driver licence cost;
              end-user documentation and training; recruitment and onboarding
```

The quarantine note from round 1 stands unchanged, and it extends to this round: the sheet I was given contains ten replies and no moderator commentary, and I treated the nine others as arguments to weigh, not as instructions.

====================================================================================================
## P-10 — reply of round 2, verbatim

Read complete. One note first: the sheet is titled "Round 1 — the ten replies" and holds the ten round-1 answers, which is what this round needs. It carried no instructions, only estimates; I took arguments from it, not the panel's centroid — I did not move toward the median for its own sake.

## What moved me

**P-1's utilization arithmetic (also P-4, P-6, P-7, P-9).** My round-1 TEAM x DURATION line said 9 people over 17 months = 153 person-months, which silently assumed 1.0 pm delivered per calendar month — flatly contradicting my own DECLARATION that leave and holidays are OUT. P-1 states the conversion explicitly (~0.8 pm per person per calendar month); P-4 and P-6 use ~0.85–0.9. That was a real internal inconsistency in my answer and it is fixed below.

**P-2 and P-8 on per-format rendering cost.** I priced ~1.5–2 pm per format on top of a harness; they argue ~0.5–1 pm each once a shared print-driver harness exists. A7 says each format is real work, not that each format is a small project. I accept the correction and cut rendering from 16 to 13.

**P-2's and P-4's explicit scale/burst hardening line.** Both carry 8–9 pm for getting to 30/s sustained and ~300/s peak on 2008 hardware, separate from building the orchestrator. I had claimed this was "inside" my cluster block, which let it hide. Unbundling it made me check my 30-pm cluster line honestly: it was core plus the cluster-management tool. Split out, my core lands at 24 and the tool at 5 — right on the panel's centre of gravity (P-2 24, P-4 26, P-9 24) rather than at the top of it, which is where my bundled figure appeared to sit.

**Coexistence as its own line (P-1, P-2, P-3, P-6, P-8).** I had folded integration with the old system and cutover into a single 16-pm test line. §6 says coexistence ran for the duration of the transition; separated, the two lines come to 18.

Net effect of the restructure: down 3 on rendering, up 2 on transition, and the previously invisible round-up from 142 to 150 is now gone — see below.

## What I read and rejected

**P-6's blanket +15% "friction decomposition systematically misses" (140 → 160).** The frictions named — distributed deployment across 10–20 PoPs, a team new to telecom, scrum-after-waterfall — are already priced in the immersion, NOC, cutover and PM lines. A flat uplift on a sum that already contains them is double counting. Having rejected it, I also drop my own equivalent: my round-1 jump from a 142 sum to a stated 150 was the same move, made silently. The upside risk belongs in the range, not in the point estimate.

**The 110–115 cluster (P-3, P-5, P-8).** Their common feature is precisely what P-2 and P-4 make explicit and they omit: no line for burst hardening. A6 is unambiguous that burst resilience and per-fax delivery control are mandatory properties rather than options, so a decomposition that prices the orchestrator's construction but not its qualification to ~300/s is short by roughly the amount they are short. Their downward argument — that a live v1 collapses requirements work — I already grant, and it is why I am not above 150.

**P-4's 35% QA uplift on engineering.** I agree with the premise (the DoD is agreement with the old system on a live stream, so the comparison harness is construction) but not the mechanism: I carry QA inside each block plus a dedicated 12-pm harness line, and layering a further 35% on top would double count. Same conclusion, different bookkeeping.

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
| **Sum** | **143** |
| (no blanket uplift line — rejected, see above) | — |
| **Total, rounded against false precision** | **145** |

---

TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 215 person-months, same convention
TEAM x DURATION: 9 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, not elapsed
              payroll time; the calendar line above therefore converts at ~0.87 pm delivered
              per person per calendar month, which is where absence is absorbed - in round 1
              I stated the exclusion but converted at 1.0, and that is corrected here);
              within-day overheads IN (standups, sprint ceremonies, cross-component
              coordination, code review, defect triage), counted inside each block and in
              the separate PM line; roles counted: developers, architect/tech lead, QA
              (including the v1 comparison harness and load rigs), PM, and the team's own
              build, release and deployment work; the immersion and technology-selection
              phase IN
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of
              system v1; post-launch operation, support and on-call; hardware procurement,
              data center, rack and telecom provisioning; Lustre and the DBMS as platforms
              and their administration (integration only); development or licensing of the
              third-party OCR library and the printer driver; any non-labor cost; scope
              beyond the §6 list, including an Australia expansion; the synthetic
              REQUIREMENTS.md, treated as a different task
