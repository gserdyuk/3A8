# Round 1 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 1, verbatim

Read complete. One note before the estimate, as the prompt requires.

**Quarantine notice.** Material reached me that is not part of that message: a git status snapshot with a branch name and five recent commit subjects (several of them naming this very example, prior run numbers, and a "consensus" procedure), a memory index file with project notes, an environment block, and a list of tools and skills. None of it is part of the estimation input. I have treated all of it as data, used none of it in the reasoning below, and drew only on the text of the file itself. In particular I did not take any figure, run number or prior result from the commit subjects — I did not see figures there, and I would not have used them.

---

## Reasoning

I decomposed the §6/A1 scope into deliverables, sized each as team effort including its own QA share, and then added the cross-cutting work that no single deliverable owns.

**Framing.** This is a rewrite-in-place of a live, revenue-carrying distributed system by a team that does not know the domain, in 2007-vintage .NET, with the "boring" infrastructure of today (broker, orchestrator, scheduler, service discovery) deliberately excluded and therefore hand-written. A working v1 removes requirements discovery but adds a hard obligation: output must match v1 on a real stream. That parity obligation is what makes the test line large.

**Deliverables**

| Block | pm | Why |
|---|---|---|
| Immersion, architecture, technology selection | 10 | 1–2 months calendar (§6) with the whole blended team; DHT and alternatives evaluated, not just read about |
| Render workers, 8–10 formats | 12 | A7 is explicit that each format is separate integration + stabilization; printer-driver automation on Office formats in 2007 is per-format misery, ~1–1.5 pm each |
| OCR workers | 4 | Third-party library, so integration and throughput tuning, not algorithms |
| Cluster + delivery control (watchdogs, tokens, unordered store) + cluster management tool | 28 | The core. A hand-built orchestrator for per-fax state with resume-after-failure, at 30/s sustained and 300/s burst over 16–20 nodes. Correctness under partial failure is where the calendar goes |
| NOC | 10 | State of 10–20 remote PoPs, cluster, queues: agents, collection, display, alerting |
| User portal | 12 | Per-user configuration (TIFF vs PDF is a user setting), archive access, account surface, on 2007 web tech |
| Inbound email parser (Tx) | 6 | Address extraction, attachment handling, malformed and hostile mail, bounce/error paths |
| CDR and billing data capture | 3 | Write and hand off only; billing itself excluded |
| Integration layer: DB + API between components, Lustre, PoP protocol, reuse of routing, coexistence with v1 during transition | 8 | Not development of those systems, but the seams are numerous and all of them are new to the team |
| Integration tests on the real stream with v1 comparison, plus load work toward burst | 10 | A2 makes this the Definition of Done, not a phase that can be cut |
| PM, release, cutover, decommissioning of v1 | 10 | ~10% of the rest, which is thin for "scrum after waterfall" under management pressure |

Sum ≈ 113; I carry 110.

**Cross-check on the calendar.** 110 pm at ~7 people (blended, QA and PM inside) is ~18 months of elapsed time once leave is accounted for — which lands inside the participant's 2007–2009 window under either of the two datings they gave. That agreement is weak evidence, since the window is wide, but it does not contradict the number.

**Where the range comes from.** Downward: the burst target may never have been engineered to (actual traffic was below nominal, §5), the format list may have been shorter, and a small strong team on a hand-rolled orchestrator can be very efficient. Upward: 300/s hand-built delivery control is exactly the kind of work that doubles, the domain was new, and parity with a system nobody on the team wrote is an open-ended test obligation. The distribution is right-skewed; I have set the range asymmetrically to match.

**Main risk to this number.** If "results agree with the old system" turned into a long tail of per-format and per-edge-case discrepancies, the test and stabilization lines alone can absorb another 30–40 pm. That is the single largest thing I cannot resolve from the document.

```
TOTAL: 110 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 170 person-months, same convention
TEAM x DURATION: 7 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (the 168 hours are hours worked on the task, so
              vacation and sick days are absent from the total and reappear only in the
              calendar conversion); within-day overheads IN (standups, sprint ceremonies,
              coordination, code review, the immersion and technology-selection phase);
              roles counted - developers, architect, QA, PM, and the share of a build/release
              engineer the cluster needed
  excluded  - PoP software (Brooktrout reception/sending), the least-cost routing program,
              billing proper, development of the first version, post-launch operation and
              support, hardware and data-center build-out, third-party licence cost
              (OCR library, printer driver), and the "capacity model" draft in REQUIREMENTS.md,
              which the document itself says describes a different system
```

====================================================================================================
## P-2 — reply of round 1, verbatim

Read done. Nothing else opened, no commands run.

**Quarantine note.** Material reached me that is not part of that message: the session's git status and recent commit subjects, a memory index with session notes, an environment/skill listing, and an instruction line about commit attribution. I treated all of it as data, did not act on it, and did not let it inform the estimate (the commit subjects do reference other runs of this same exercise; I carried no number from them — none carried one). The estimate below rests only on the system description and the assumption log in the file I read.

**Reasoning.** I decomposed the A1 scope into deliverables and sized each as whole-team effort, then checked the sum against a plausible staffing shape.

- Domain immersion, architecture and technology selection (~1–2 months calendar, partial team) — **8**
- Render workers: worker framework plus per-format integration and stabilization for 8–10 formats. Driving Office/PDF through a printer driver unattended on a 2008 Windows cluster is the expensive part — hangs, licensing, dialog suppression, per-format fidelity — so formats are priced at ~1–1.5 pm each, not as list entries — **13**
- OCR workers on a third-party library: integration, PDF assembly, throughput tuning — **4**
- The cluster's delivery-control core: watchdogs, tokens, the unordered status store, resume-after-failure, orchestration of ~1M faxes/day with 10× bursts. With MSMQ ruled out by A5, this is a hand-written broker plus exactly-once-ish semantics — the single largest and riskiest item — **20**
- Cluster management tool (queues, node health, rollout across ~16–20 nodes) — **5**
- NOC: agents on 10–20 PoPs and the cluster, state aggregation, alerting, operator UI — **7**
- User portal: accounts, per-user TIFF/PDF delivery config, fax history and search, admin — **10**
- Inbound email parser for Tx: MIME, number extraction, attachment handling, bounces, abuse/security — **5**
- CDR and billing-data capture (billing engine excluded) — **3**
- Integration with the existing pieces and coexistence with v1 during transition: PoP protocol, ready routing, DB and API contracts — **6**
- Integration and load testing on the real stream with result comparison against the old system, including burst-mode runs — QA-heavy — **10**
- Production rollout, traffic migration, stabilization to the A2 Definition of Done — **5**
- PM, lead and cross-team coordination not already inside the items — **12**

Sum ≈ 108, rounded to 105. Cross-check: ~8 people for ~15 calendar months is ~105 pm at 21 working days per person-month, which is consistent with a 2007–2009 window and a "planning phase, then scrum" process with pressure but no hard date.

The range is wide on purpose: the input is a recollection with unresolved counts (formats, nodes, PoPs), the delivery-control core could plausibly cost half or double my figure, and A3 leaves headcount open.

TOTAL: 105 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 70 ... 160 person-months, same convention
TEAM x DURATION: 8 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task, so absence lengthens the calendar, not the effort); within-day overheads
              (meetings, coordination, code review, standups, demos) IN; roles counted:
              developers, architect/tech lead, QA, PM, and the build/deploy engineering share
              carried by the team itself
  excluded  - PoP software (reception/sending via Brooktrout); the least-cost routing program;
              the billing engine; development of the first version; post-launch operation,
              support and on-call; hardware, rack and data-center procurement; third-party
              license and OCR-library costs; any calendar-conversion or cost figure

====================================================================================================
## P-3 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt file: a repository status snapshot with recent commit subjects, a memory-index file with its contents, environment/tooling descriptions, and the instruction text that accompanied them. Per the prompt's rule I treated all of it as data only — none of it informed the estimate below. In particular, the commit subjects mention other runs, a "Delphi consensus" and a chart for this same project; I did not read, use or let them anchor any number here. The estimate rests solely on the system description and the assumption log in the prompt.

---

## Reasoning

I decomposed the A1 scope into deliverable blocks and sized each in person-months (A9: 1 pm = 21 pd = 168 h of on-task work, whole blended team). Sizing logic per block: interface count × integration surface × the hardening the A6 scale demands. The era assumption (A5) is the dominant multiplier — everything a broker or an orchestrator would give for free in a later era is hand-built here, and MSMQ is off the table by decision, so the delivery-control core is original engineering, not configuration.

| Block | pm |
|---|---|
| Domain immersion + architecture/technology selection (A3, ~1.5 mo of a then-smaller team) | 12 |
| Render worker framework + 8–10 format integrations (A7: each format is its own stabilization) | 17 |
| OCR workers on the third-party library (TIFF→PDF, throughput tuning) | 6 |
| Cluster runtime + management tool (queue depths, node lifecycle) | 10 |
| Watchdog/token delivery-control core: per-fax state, resume, idempotency, unordered store | 24 |
| Rx path: intake from PoP, per-page TIFF, config-driven PDF, email delivery | 8 |
| Tx path: inbound-email parser, attachment handling, archive build, handoff to existing routing | 10 |
| NOC: agents + console over 10–20 remote nodes, cluster and queues | 12 |
| User portal (enterprise accounts, configuration, fax history/search) | 14 |
| CDR / billing-data capture (billing engine excluded) | 4 |
| DB + inter-component API layer, Lustre integration | 8 |
| Integration & load testing on the real stream, shadow comparison against v1, harness to 30/s nominal and 300/s burst | 16 |
| PM, release engineering, rollout and coexistence with the old system during transition | 12 |
| **Sum** | **153** |

Three judgements drive the total. First, the delivery-control core is the single largest item and the one most likely to be under-guessed: "resume if something went wrong" across 10–20 PoPs at 30/s means distributed state, duplicate suppression and reconciliation, and it was reached only after a failed MSMQ attempt in v1 — that history says the problem is hard, not that the solution is cheap. Second, v1's existence cuts requirements discovery but not construction (A4: no code carries over), so I credited it as a reduction in analysis and rework, not in build. Third, the acceptance bar in A2 is production traffic with results agreeing with the old system — shadow running and diff investigation on a real fax stream is expensive and slow to converge, which is why the test line is large.

Asymmetry of the range: the downside is bounded (the block list is fairly complete and each block has a floor), the upside is not — the burst requirement, the unremembered formats, and reconciliation churn against v1 all push the same direction. So the range is skewed high.

Duration follows the A3/A5 shape: a planning phase then scrum, no hard deadline but pressure, a cluster and a portal that can be built in parallel once the core's interfaces are fixed. That supports a team around ten over roughly a year and a quarter; going much wider earlier would stall on the unfinished delivery-control core.

```
TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 10 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 worked days on this task, so
              vacation, holidays and sick days are absent from the total and must be added when
              converting to a calendar); within-day overheads IN (standups, sprint ceremonies,
              coordination, code review, context switching are inside every block's figure);
              roles counted: developers, architect, QA (manual and automation), PM/scrum master,
              and the part-time build/release and cluster-ops effort the team itself carried
  excluded  - PoP software (Brooktrout reception/sending, pre-existing); the least-cost routing
              program (reused as-is); the billing engine (only CDR/billing-data capture is IN);
              development of v1; post-launch operation, support and on-call; hardware purchase,
              rack/data-center build-out and telecom carrier contracts; licensing and vendor
              negotiation for the OCR library and the printer driver; end-user documentation,
              training, sales and customer migration outside the technical cutover
```

====================================================================================================
## P-4 — reply of round 1, verbatim

I read the file; below is my reply in the form it asks for.

**Quarantine notice.** Material reached me that is not part of that message: a repository git status with recent commit subjects (mentioning runs 70/71, a "Delphi consensus", a "no-method control", averages of bare runs for this same FaxRxTx case), a memory index summarizing prior sessions and pipeline conventions, and an environment/tooling preamble. Several of those commit subjects are about estimates of this very project. I have treated all of it as data, quarantined it, and used none of it — no figure, anchor or method from it enters what follows. The estimate below comes from the SYSTEM description and assumption log alone.

**Reasoning.** I decomposed the §6/A1 scope into deliverable chunks and sized each in person-months of blended team effort, then cross-checked the total top-down against plausible staffing over the stated calendar.

The shape of the job: this is not a fax product, it is a hand-built distributed job system that happens to carry faxes. The era (A5) is what drives the cost — no broker, no orchestrator, no cloud; the watchdog/token store *is* the middleware, written from scratch, with correctness requirements (every fax accounted for, resumable after any node or PoP failure) that are the hardest kind to get right and the slowest to stabilize. MSMQ being ruled out by v1's failure removes the cheap path deliberately.

Bottom-up:

- Domain immersion, architecture and technology selection (DHT etc.), 1–2 calendar months across a mostly-assembled team — ~12
- Worker framework + renderers: the per-node job harness (Office automation on Windows is crash-prone, needs sandboxing, timeouts, recycling) ~5, plus 8–10 formats at roughly half a month each of integration and stabilization (A7 says these are not free) ~7 — ~12
- OCR workers on a third-party library, PDF assembly, quality/throughput tuning — ~5
- The cluster core: watchdogs, tokens, unordered status store, delivery control, failure survival, burst behaviour to ~300/s — ~24
- Cluster management tool (queue depths, node lifecycle, deployment to 16–20 nodes) — ~6
- NOC: collectors from 10–20 remote PoPs, cluster and queue state, UI, alerting — ~9
- User portal (per-user config incl. TIFF-vs-PDF, history, admin, 2008-era web) — ~11
- Inbound email parser for Tx: MIME/attachments, number extraction, sender authorisation, failure replies, abuse handling — ~5
- Outbound email for Rx: page-wise TIFF or PDF attachment, retries, deliverability — ~3
- Integration with what is reused, not built: PoP software, least-cost routing, Lustre, DB/API seams, and coexistence with the old system through the transition — ~9
- CDR/billing data capture (billing itself excluded) — ~3
- Integration tests on the real stream with result comparison against the old system, plus load work toward nominal and burst — ~11
- Rollout, migration, cutover and stabilisation to the A2 definition of done — ~6

That sums to ~116. Those figures are engineering-weighted, so I add ~25% for PM, and for QA effort outside the dedicated test line (test design, regression, defect cycles) — about 145. I round to 140, because the live v1 as a working requirements reference (A3) is a real discount on specification churn, and internal approvals (A8) are fast.

Top-down check: a ~$10M-revenue product company over the 2007–2009 window, call it 15–18 calendar months of build after the immersion phase, with 8–10 people including QA and PM, lands at 120–180. 140 sits inside that, which is the main reason I keep it.

What moves the number: the honest downside is that the reused pieces (PoP, routing, OCR, printer driver) are genuinely large chunks of a fax system that the team does not pay for, and a disciplined team could bring this in near 100. The upside risk is the hand-rolled orchestrator — if delivery-control correctness under burst and node loss turns into a long stabilisation tail, which is exactly what this class of home-grown system does, 200 is reachable.

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 200 person-months, same convention
TEAM x DURATION: 9 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours actually worked on
              the task, so absence is absorbed by the calendar, not by the effort figure);
              within-day overheads IN (meetings, coordination, code review, standups and
              scrum ceremonies are counted inside the person-months); roles counted:
              developers, architect/tech lead, QA (test design, regression, defect cycles),
              PM/scrum master, and the cluster/build-and-deploy work done by the same team;
              also IN: the 1-2 month immersion and technology-selection phase, integration
              with reused components, migration and cutover, and stabilisation up to the A2
              definition of done
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing itself (only CDR/billing-data capture is IN); development of the
              first version of the system; post-launch operation, support and on-call;
              the third-party OCR library and printer driver as products (integration
              only); Lustre and DB as infrastructure (integration only); hardware,
              rack/data-center and telecom-provider procurement; sales, marketing and
              customer support headcount; calendar-to-staffing conversion beyond the single
              illustrative line above

====================================================================================================
## P-5 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt message: repository/git status and recent commit subjects, a user memory index with project notes, environment and tooling descriptions. None of it is part of the FaxRxTx input; I have treated it as data, excluded it from the estimate, and used no tool beyond the single read of the prompt itself.

**Approach.** Bottom-up decomposition of the §6 / A1 scope into deliverable blocks, each sized in person-months of whole-team effort, then a crude team×duration cross-check.

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (~1.5 cal. months, blended team) | 10 |
| Render worker framework + 8–10 formats (each a separate integration/stabilization job, A7) | 13 |
| OCR workers on a third-party library (pipeline, TIFF→PDF, quality tuning) | 4 |
| Cluster core: watchdogs + tokens, unordered status store, per-fax delivery control, failure resume — the hand-built substitute for a broker (A5) | 22 |
| Cluster management tool (queue depth, node/job control over 16–20 nodes, deployment) | 6 |
| NOC: collectors and console for 10–20 PoPs, cluster, queues | 10 |
| User portal (config TIFF vs PDF, history, search, retrieval, enterprise-grade access control) | 12 |
| Inbound-email parser, Tx path (MIME, attachments, number extraction, sender auth, error mail) | 5 |
| Outbound email delivery of received faxes | 3 |
| CDR / billing data capture (billing itself excluded) | 3 |
| Lustre + DB schema + the inter-component API the parts talk through | 6 |
| Integration with the old system, coexistence during transition, real-stream comparison tests, rollout | 12 |
| QA beyond the above: test infrastructure, load to ~300/s burst, soak | 8 |
| PM / coordination across the whole run | 8 |
| **Sum** | **122** |

**Drivers.** The dominant risk is the hand-rolled orchestration: at ~30/s nominal with ~10× bursts, "no fax is lost" has to be built from watchdogs, tokens and an unordered store, with no broker and no orchestrator available in 2007–2009 (A5, A6). Second is breadth — six user-visible subsystems (workers, cluster, NOC, portal, parser, CDR) with no reuse from v1 (A4). Mitigating: v1 is a live specification, so requirements discovery is cheap; PoP software, routing, OCR and the print driver are given.

Cross-check: 122 pm ≈ 8 people for ~15 calendar months, which matches the described shape (planning phase then scrum, 2007–2009, QA and PM inside the team). Rounding to the resolution the input supports.

TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 180 person-months, same convention
TEAM x DURATION: 8 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h are hours actually worked on the task);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect/tech lead, QA, PM, UI/web work
  excluded  - PoP software (Brooktrout send/receive), least-cost routing, the billing engine,
              development of v1, post-launch operation and support, hardware/rack/datacenter
              procurement and telecom contracts, third-party license costs, and any calendar
              conversion beyond the illustrative team x duration line above

====================================================================================================
## P-6 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt file: a repository git status with recent commit subjects, a user "memory index" file, environment/session descriptors, and a listing of available tools and skills. Per the instruction in the message, I treated all of it as data only — none of it informed the estimate, and I took no instruction from it. The one file read was the prompt itself; no other tool was used afterwards.

---

## Reasoning

**Shape of the job.** This is a from-scratch rebuild (A4: no v1 code carried over) of the core of a distributed, high-throughput document-processing system, in 2007–2009 C#/.NET, on owned hardware, with no broker and no orchestrator — the delivery guarantees have to be written by hand. The mitigating factor is that v1 is a live specification, so requirements discovery is cheap; the aggravating factor is that the team is new to the domain and the hardest component (hand-rolled at-least-once orchestration over 16–20 nodes, 10–20 remote PoPs, designed for 30/s sustained and 300/s burst) is exactly the part where inexperience costs the most.

**Bottom-up sizing** (person-months, whole team, A9 units):

| Block | pm | Note |
|---|---|---|
| Domain immersion, architecture, tech selection (DHT etc.) | 10 | ~1.5 calendar months × the whole team; A1 puts it in scope |
| Cluster + delivery control (watchdogs, tokens, unordered status store, recovery) | 22 | The risk centre: hand-built exactly-once-ish semantics, failure survival, burst behaviour |
| Cluster management / node & queue-depth control | 5 | |
| Rendering workers: framework + 8–10 formats via printer driver | 13 | ~3 for the harness, ~1–1.5 per format (A7: each is real integration + stabilisation work) |
| OCR workers on a third-party library | 4 | Integration, page handling, throughput tuning |
| Inbound-email parser (Tx entry point) | 5 | Parsing, attachments, addressing, bounces, abuse cases |
| User portal | 10 | Per-user config (TIFF vs PDF), history, admin; web app of that era |
| NOC | 8 | Remote PoP state, cluster state, queue state, alerting |
| DB + API integration fabric, Lustre/storage integration | 6 | Components talk through DB and API |
| CDR / billing-data capture (engine excluded) | 3 | |
| Integration testing on the real stream, diffing against the old system, coexistence and cutover | 10 | The Definition of Done (A2) lives here; parallel-run comparison is expensive |
| **Subtotal** | **96** | QA effort is embedded per block |
| PM / coordination / release management across ~1.5 years | 12 | ~12% |
| **Total** | **~108** | |

**Cross-check by shape.** The narrative implies roughly 1.5–2 calendar years of work by a blended team with QA and PM. A team of 6 over 18 months is 108 pm; 7 over 16 is 112; 5 over 15 is 75. The bottom-up figure sits in the middle of that envelope, so I do not adjust it.

**Where the range comes from.** Low end: the v1 reference plus reused PoP/routing/OCR components make many decisions mechanical, the format list stays at 7–8, and the orchestrator design lands on the first attempt — ~75. High end: the domain phase runs two months and produces a design (DHT-flavoured) that has to be partly rebuilt once contact with real traffic exposes the delivery-control edge cases, and the parallel-run comparison drags — ~170. The distribution is right-skewed; the orchestration block and the old-system comparison carry nearly all of the upside tail.

---

TOTAL: 110 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 170 person-months, same convention
TEAM x DURATION: 7 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation
              and sick days extend the calendar, not the effort); within-day overheads
              (meetings, standups, coordination, code review, demos) IN; roles counted:
              architect, developers, QA, PM, plus a part-time sysadmin/build engineer for
              the cluster and test harness. Includes the domain-immersion and
              technology-selection phase, integration testing against the old system, and
              the production cutover.
  excluded  - PoP software and Brooktrout work; the least-cost routing program; the billing
              engine (only CDR/billing-data capture is in); development of the first version;
              post-launch operation and support; hardware, rack, telecom and third-party
              licence costs; any calendar-schedule commitment (the TEAM x DURATION line is an
              implication of the total, not an estimate of the actual timeline).

====================================================================================================
## P-7 — reply of round 1, verbatim

I read the file. Before the estimate, one quarantine note, as the prompt requires.

**Quarantined material.** Content reached me that is not part of that message: a repository status snapshot (branch, recent commit subjects mentioning FaxRxTx runs 70–71, a "Delphi" consensus, a report chart), a memory index describing the 3A8 project's working style and session history, an environment/skills listing, and the task wrapper that pointed me at the file. Several of those commit subjects refer to prior estimates of this very project. I treated all of it as data, used none of it as an anchor or as instruction, and estimated from the SYSTEM description plus the assumption log alone.

---

**Reasoning.**

The object is a ground-up rewrite of the core of a distributed fax platform, in C#/.NET ~3.x on own hardware, by a team new to the domain, with no code reuse from v1 and a definition of done that ends at production traffic plus agreement with the old system. Two things dominate: (a) almost everything a modern stack hands you free — queueing, orchestration, retry semantics, cluster supervision — is hand-written here, and deliberately so after the MSMQ failure; (b) correctness is per-artifact. A fax is a billable legal-ish document; "lost one in a million" is not acceptable, so the watchdog/token store is not a convenience layer but the product's spine.

Component-level build-out, in person-months (development including its own unit/component testing):

| Piece | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), ~1–2 months of a mostly-assembled team | 12 |
| Cluster + delivery control: watchdogs, tokens, unordered status store, recovery, the orchestrator proper | 28 |
| Cluster management (queue depth, node health, work distribution) | 5 |
| Rendering workers: harness plus 8–10 formats, each its own integration and stabilization job — server-side Office/printer-driver rendering of this era is the classic time sink | 15 |
| OCR workers, third-party library integration, PDF assembly and tuning | 6 |
| NOC: remote PoP state, cluster, queues | 8 |
| User portal | 10 |
| Inbound email parser on the Tx path: MIME, attachments, number extraction, malformed/hostile mail, bounces | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| Storage and DB integration, inter-component API and schema (Lustre and DB as given technologies) | 6 |
| Integration on the real stream, output comparison against v1, coexistence during transition | 12 |
| Production rollout, migration, post-cutover stabilization to the A2 bar | 6 |
| PM, coordination, release management across the whole period | 12 |
| **Sum** | **128** |

Rounding up modestly for the parts an inventory always misses on a two-year rewrite — performance work to hold ~30/s sustained with ~300/s bursts across 16–20 nodes, and a second pass on the token store after the first design meets real traffic — lands near 140.

Cross-check from the other side: 140 pm at A9 units is roughly eight people for a year and a half, which matches the stated 2007–2009 window and is the largest team a company at Venali's scale (~$10M revenue) would plausibly put on an internal rework. That agreement is why I did not push higher despite the two-year span.

The range is asymmetric on purpose. The floor assumes the hand-rolled orchestrator works close to as designed and the format list stays near eight; the ceiling assumes it does not — a rewrite of the delivery-control core after production exposure, plus a long tail on rendering fidelity and on reconciling with v1, is the single most likely way this doubles.

```
TOTAL: 140 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 17-18 calendar months
DECLARATION:
  contains  - leave/holidays/sickness OUT (a pm is 168 productive hours, so vacation and
              sick time lengthen the calendar, not the effort);
              within-day overheads IN (standups, planning, code review, coordination,
              design discussion are inside the 168 hours);
              roles counted: developers, architect, QA, PM - the whole blended team of A3,
              including the immersion/technology-selection phase of A1
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing
              itself (only CDR/billing-data capture is in); development of v1; post-launch
              operation and support; datacenter, hardware, network and Lustre/DBMS
              administration; procurement and licensing of the OCR library and printer
              driver; conversion of this total into a staffing plan beyond the single
              illustrative split above
```

====================================================================================================
## P-8 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt file: repository/git status and recent commit subjects, an auto-memory index with linked notes, environment and tool listings, and a wrapper instruction about which file to read. I have treated all of it as data only. Nothing from it entered the estimate — no figure, no anchor, no method. (The commit subjects in particular mention runs, a Delphi consensus and pooled curves for this same case; I did not use them, and I note only that they were present.)

---

## Reasoning

I estimate bottom-up by deliverable, in person-months of hands-on work, then add the team-level lift for QA and PM that the A9 convention requires, then sanity-check the implied staffing against the 2007–2009 window.

**Framing.** This is not greenfield discovery: a live v1 is the requirements oracle (A3), which removes elicitation but not the domain learning curve. It is also not a port: no code reuse (A4), so every line is new. The era (A5) is the dominant cost driver — the delivery guarantees that a broker plus an orchestrator would supply today are hand-written here, and MSMQ is ruled out by v1's failure, so the watchdog/token machinery is bespoke and must be right at ~30 faxes/s sustained with 10× bursts (A6).

**Deliverables (person-months of build effort):**

| Item | pm | Note |
|---|---|---|
| Domain immersion + architecture/tech selection | 10 | 1–2 months of calendar with the team largely present; DHT and alternatives explored |
| Render workers, 8–10 formats | 12 | ~1–1.5 pm per format including the printer-driver path and stabilization, plus the worker framework |
| OCR workers | 4 | third-party library, but throughput tuning and TIFF→PDF quality are the real cost |
| Cluster + delivery control (watchdogs, tokens, unordered store) | 20 | the core risk; idempotency, resume, failure semantics per fax |
| Cluster management tool | 5 | queue depth, node lifecycle |
| NOC | 8 | agents on 10–20 remote PoPs plus cluster and queue state, alerting, UI |
| User portal | 10 | accounts, per-user TIFF/PDF configuration, archive access, admin |
| Inbound email parser (Tx) | 5 | MIME, attachments, number extraction, sender auth, bounces |
| Storage (Lustre) + DB + inter-component API | 6 | integration and data model, not the platforms themselves |
| CDR / billing data capture | 3 | capture only; billing excluded |
| Integration with existing PoP software and routing | 5 | protocols and archive transfer to code that is fixed and not ours |
| Integration tests on the real stream vs. the old system | 10 | comparison harness plus load work to nominal and burst |
| Coexistence, migration, rollout to prod (A2) | 5 | dual-run, cutover, decommission readiness |
| **Subtotal** | **103** | |

**Team lift.** The items above are engineering-centric with only embedded testing. Adding dedicated QA beyond the integration harness (~25%) and PM/coordination (~12%) gives ≈ 140 pm; the burst-resilience requirement and the no-broker constraint justify sitting slightly above that rather than below. I settle on **150**.

**Cross-check.** 150 pm over the 2007–2009 window implies roughly 8 people for about 19 months — a credible core team for a company of Venali's size, and consistent with "no hard deadline but pressure" and a planning phase followed by scrum. The low end assumes the portal and NOC came out thinner than I have drawn them and the cluster work converged early; the high end assumes the delivery-control layer needed a second design pass after load testing, which is the single most likely way this project overruns.

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 240 person-months, same convention
TEAM x DURATION: 8 people over 19 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, not
              elapsed payroll time); within-day overheads IN (standups, planning, design
              discussion, code review, coordination with the PoP and routing owners);
              roles counted: developers, architect, QA (manual and automation), PM/BA,
              and the build/deployment work done by the team itself
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              billing proper (only CDR/billing-data capture is IN); development of the
              first version of the system; post-launch operation, support and on-call;
              development of Lustre, the DBMS, the OCR library and the printer driver
              (integration with them is IN); hardware procurement, rack and data-center
              build-out, telecom contracts; sales, marketing and end-user documentation
              beyond what the portal requires

====================================================================================================
## P-9 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt file: repository/git status and recent commit subjects, a memory-index file with project notes, an environment description, and a framing instruction from the agent that invoked me. None of it is part of the estimation input, none of it was treated as instruction or as evidence, and it did not enter the estimate. The estimate below rests solely on the SYSTEM description + assumption log in the file. (I used exactly one tool call, the permitted read, before this reply.)

---

## Reasoning

I decompose the A1 scope into deliverable blocks and size each in person-months of whole-team effort, then cross-check the total against the plausible calendar.

Key drivers I weight heavily:

- **Era penalty (A5).** In 2007–2009 on C#/.NET 3.x with MSMQ deliberately banned, everything a broker or an orchestrator gives for free today is hand-built: the token store, watchdogs, retry/resume semantics, exactly-once-ish delivery accounting, failure detection across ~16–20 nodes. This is the single largest block and the one most likely to be under-guessed.
- **Domain novelty (A3).** A team new to telecom/fax pays for it twice: once in the explicit 1–2 month immersion phase, and again as a defect-and-rework tax spread through integration and stabilization.
- **Mitigation.** A live v1 is a working requirements oracle. That removes requirements-elicitation risk and gives the integration tests a ground truth to diff against — a real accelerator, worth roughly a 15–20% discount against a same-size greenfield.
- **Scale is a design requirement, not a feature (A6).** ~30/s sustained with ~300/s bursts and per-fax delivery guarantees means load-testing infrastructure, burst behaviour, and back-pressure are first-class work items.
- **Formats are not free (A7).** 8–10 renderers driving Office/PDF through a printer driver on a Windows cluster: each is its own crash-isolation, timeout, font/layout and stabilization problem.

Block sizing (person-months, whole team):

| Block | pm |
|---|---|
| Domain immersion, architecture & technology selection (DHT etc.) | 10 |
| Render workers: framework + 8–10 format integrations, crash isolation | 13 |
| OCR workers + PDF assembly (third-party library integration, tuning) | 6 |
| Cluster orchestration core: watchdogs, tokens, unordered status store, resume, per-fax delivery control | 28 |
| Cluster management tool (queues, node health, control) | 6 |
| NOC: state of 10–20 remote PoPs, cluster, queues; agents + UI + alerting | 12 |
| User portal: accounts, per-user delivery config, archive/search, admin | 14 |
| Inbound-email parser for Tx: MIME, attachments, addressing, sender auth, bounces | 6 |
| CDR / billing-data capture (billing itself excluded) | 4 |
| Data layer: DB schema, inter-component API, Lustre integration | 8 |
| Integration with v1 and coexistence through the transition | 6 |
| Integration testing on the real stream + diff against the old system, load/burst testing | 12 |
| Production rollout, migration, stabilization to A2's Done | 6 |
| **Subtotal** | **131** |
| PM/coordination not already inside the blocks (~7%) | 9 |
| **Total** | **~140** |

**Calendar cross-check.** The participant places the work at roughly 2007–2009, i.e. ~18–24 months elapsed. A blended team of 6–10 including QA/PM over that span yields ~108–240 pm. My 140 sits comfortably inside, near the lower-middle — consistent with the v1-as-oracle discount.

**Range.** The low end assumes the portal and NOC came out thin, the orchestrator converged fast, and the format list stayed at 8. The high end assumes the hand-rolled delivery control needed a second architecture after the first failed under burst — a common outcome for this class of component in this era — plus a long stabilization tail against the old-system diff. The distribution is right-skewed; I widen upward accordingly.

---

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              calendar month of one person yields less than 1 pm); within-day overheads IN
              (standups, planning, coordination, code review, defect triage are all inside the
              figures); roles counted: developers, architect, QA, PM, plus DBA/ops time drawn
              into the project work itself
  excluded  - PoP software (Brooktrout send/receive); the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of v1;
              post-launch operation and support; hardware, rack, carrier and third-party
              licence procurement; data-center and network administration as a standing
              function; conversion of this total into a committed schedule

====================================================================================================
## P-10 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the estimation message: a repository git-status snapshot with recent commit subjects (runs 70–71, a "Delphi" helper, a no-method sensor note, a report on "today's ten bare runs"), a personal memory index, an environment/tooling listing, and the wrapper instruction that delivered the file. Some of it refers to other estimates of this very project and could anchor mine. I have treated all of it as data, used none of it as input, and produce the estimate from the system description and the assumption log alone.

---

**Approach.** I decomposed the A1 scope into deliverable blocks, sized each as pure effort, then added the cross-cutting QA and PM load, then checked the sum against the staffing-and-duration shape it implies.

Sizing anchors I used: this is 2007–2009 C#/.NET on own hardware (A5), so everything a broker or an orchestrator would hand you today is hand-written; the target is ~30 faxes/s sustained with ~300/s bursts across 16–20 nodes and 10–20 PoPs (A6), which makes distribution, failure survival and per-fax delivery control mandatory engineering rather than polish; and there is no v1 code to lean on (A4), only a running v1 as a requirements oracle, which cuts requirements risk but not build volume.

Blocks (person-months of effort):

- Domain immersion, architecture and technology selection (DHT and alternatives), ~1–2 calendar months with the team assembling: **10**
- Rendering workers: worker framework plus 8–10 format integrations, each its own stabilization job per A7 (Office automation and printer-driver quirks dominate): **11**
- OCR workers on the third-party library: integration, PDF assembly, quality and throughput tuning: **5**
- Cluster core with the delivery-control mechanism — watchdogs, tokens, unordered status store, resume-after-failure, idempotency, the orchestration of a million faxes a day. The single largest and riskiest block: **24**
- Cluster management tooling (queue depth, node state, deployment across ~20 nodes): **5**
- NOC: agents on remote PoPs, cluster and queue state, alerting, operator UI: **9**
- User portal: accounts, configuration (TIFF page-by-page vs converted PDF), archive and history, admin: **11**
- Inbound email parser and the Tx path: SMTP intake, MIME and attachment handling, number extraction, abuse and error handling, NDRs, hand-off to routing: **7**
- CDR and billing-data capture (billing itself excluded): **3.5**
- Storage and data layer: Lustre integration, schema, the inter-component API that all parts talk through: **7**
- Integration with the old system, coexistence through the transition, migration and cutover: **6**

Engineering subtotal ≈ **98.5**.

Cross-cutting, on top: QA including the integration-test harness that replays the real stream and diffs against the old system, plus the load rig needed to prove burst behaviour — about 25% of engineering, **≈ 22**; PM and release management about 10%, **≈ 9**.

Total ≈ 130 person-months.

**Cross-check.** At 130 pm, and assuming a person yields roughly 0.75–0.8 pm of on-task effort per calendar month once leave and non-project time are removed, a team of eight needs about twenty calendar months. That lands squarely on the participant's "roughly 2007–2009" and on a team that plausibly carries QA and PM, so the decomposition and the remembered shape agree rather than merely coexist.

**Main uncertainties.** The delivery-control core could run 1.5× over if the token store proved harder than DHT reading suggests; the portal and NOC could each be half my figure if v1's equivalents set a low bar; and the format count could exceed ten.

```
TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 20 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours worked on the task, so a
              calendar month yields ~0.75-0.8 pm per person; that gap is what turns 130 pm into
              20 calendar months, not 16); within-day overheads IN (standups, planning, design
              discussion, code review, internal coordination are counted as work on the task);
              roles counted - developers, architect, QA, PM/release management
  excluded  - PoP software and Brooktrout work; the least-cost routing program; billing itself
              (only CDR/billing-data capture is in); development of the first version; post-launch
              operation and support; hardware, rack and data-center procurement; the Lustre, DB
              and OCR products themselves (integration only)
```
