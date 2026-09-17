# Round 1 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 1, verbatim

**Quarantine note.** Material outside this message reached me before I read it: repository/git status and recent commit subjects, a memory-index file's contents, environment and tooling descriptions, and instructions attributed to a launching agent. I treat all of it as data, not as input to this estimate; none of it informed the numbers below. The only tool use was the single read that delivered this message; from that point on, no tools.

---

## Reasoning

I estimate bottom-up by deliverable, then sanity-check top-down against the implied staffing.

**Framing.** This is a from-scratch rebuild (A4: no v1 code reused) of the *core* of a distributed, hand-orchestrated document-processing system, in 2007–2009 C#/.NET, on owned hardware, with no broker and no orchestrator available (A5). The mitigations are real but limited: v1 is a live requirements reference, and the hardest edge pieces (PoP/Brooktrout software, least-cost routing, OCR engine, print driver, Lustre, DB) are bought or already there. The aggravator is equally real: the team is new to the domain, and "delivery control of every fax" at ~30/s sustained with ~300/s bursts (A6) is the kind of property that is cheap to state and expensive to actually hold under node failure.

**Bottom-up (development + component-level test, person-months):**

| Block | pm | Note |
|---|---|---|
| Domain immersion, architecture and technology selection | 12 | 1–2 calendar months (A3) at partial team load; DHT-style exploration is cheap to run, expensive to converge |
| Cluster core: watchdogs, tokens, unordered status store, resume-on-failure, orchestration of ~16–20 nodes | 21 | The single largest risk item — this is a hand-written replacement for what a broker would give |
| Cluster management tool (queue depths, node lifecycle) | 5 | |
| Rendering workers: framework + 8–10 formats | 11 | ~4 pm framework/print-driver harness, ~0.7–0.9 pm per format for integration and stabilization (A7); Office formats on a print driver are the bad ones |
| OCR workers, PDF assembly, per-user TIFF-vs-PDF policy | 5 | Third-party library, so integration not algorithm |
| NOC: state of 10–20 remote PoPs, cluster, queues | 9 | |
| User portal | 12 | Customer-facing config, fax history, account admin |
| Inbound email parser (Tx entry) | 6 | SMTP intake, MIME, number extraction, sender authentication, malformed-input and bounce handling |
| CDR / billing data capture (billing itself excluded) | 3.5 | |
| Integration surface: DB + API between components, Lustre, coexistence with the old system during transition | 7 | Coexistence is an explicit requirement, not a freebie |
| Integration tests on the real stream with result comparison to v1, plus load/burst testing | 12 | The comparison harness is a product in itself |
| Production rollout, cutover, stabilization to the A2 Done | 6 | |
| **Subtotal** | **~109.5** | |

**Overheads.** The block figures above are engineering-led and carry only the QA embedded in each team's own work. A9 counts the whole team, so I add a dedicated QA function (~25% of the engineering subtotal, justified by A2 — Done is "prod traffic matches the old system," which is QA-heavy) and PM/scrum-master/tech-lead coordination across the whole calendar (~10%). That gives 109.5 × 1.35 ≈ **148**, which I round to **145** to avoid false precision.

**Top-down check.** 145 pm over the ~18 calendar months that "2007–2009" most plausibly denotes for a *scoped* rework implies ~8 people including QA/PM. For a product company with ~$10M revenue (§7) that is a believable dedicated team, and it is consistent with §6's "QA/PM, not just developers." If the period was really 24 months, the same total implies ~6 people, also believable. The two readings bracketing the same effort is the main reason I trust the central figure.

**Range.** The downside case (~100 pm): immersion lands closer to one month, the portal turns out to be a light re-skin over v1's concepts, formats average nearer 0.5 pm, and the token/watchdog design converges on the first attempt. The upside case (~210 pm): the hand-rolled delivery control gets rebuilt once after failing under burst — the standard outcome for hand-written distributed guarantees in this era — the Office renderers prove unstable under a headless print driver, and the parallel-run comparison against v1 exposes behavioural differences that force rework rather than just fixes. I deliberately make the range asymmetric: this scope has far more ways to cost more than to cost less.

**Main uncertainty I did not resolve.** §6 says "redo what management did not like," which could mean anything from a targeted core replacement to a full rewrite. A1/A2 push me toward the broad reading (new system takes prod traffic, old version decommissioned), and I estimated that. A narrow reading would cut the total by perhaps a third.

---

TOTAL: 145 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, not elapsed
              payroll time; a calendar plan would need roughly 15-20% more wall-clock);
              within-day overheads (meetings, standups, coordination, code review) IN;
              roles counted - developers, architect, QA, PM/scrum master, and the
              domain-immersion and technology-selection phase per A9
  excluded  - PoP software and Brooktrout integration; the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; procurement,
              hardware, datacenter and rack build-out; licence costs for OCR, the print
              driver, Lustre and the DBMS; sales, marketing and any non-engineering
              function

====================================================================================================
## P-2 — reply of round 1, verbatim

**Quarantine note.** Material that was not part of this message did reach me: a repository/git status block with a branch name and recent commit subjects, an environment description, a memory-index file with project notes, a tool listing, and framing instructions attributed to a calling agent. Per the instruction in the message, I treat all of it as data, exclude it from the estimate, and proceed on the text of this message alone. I used no tool other than the single read of this prompt itself.

---

## Approach

Bottom-up decomposition of the §6 / A1 "team did" list, each item sized as full-cycle work (design → build → test → stabilize) in the A5 era, then a project-level band for PM and cross-cutting QA, then a sanity cross-check against what the implied calendar and staffing would look like.

Two judgements drive the number more than anything else:

1. **The hand-rolled orchestrator is the centre of gravity, not the portal.** With MSMQ deliberately off the table (A5) and no broker or orchestrator available in 2007–2009, the watchdogs-and-tokens store is a distributed-systems build: per-fax state, idempotent resume, failure detection across 16–20 nodes and 10–20 PoPs, correctness under 30/s sustained with 10× bursts. Work of this kind is dominated by hardening, not by first implementation; I size stabilization at roughly the same order as construction.
2. **Domain ignorance costs more than the stated 1–2 months.** A3 books the immersion phase explicitly, but a team new to fax/telecom keeps paying after that phase closes — in rework of assumptions that turn out wrong (T.30 retry semantics, per-page failure, number formats, PoP behaviour). I do not add a separate line for this; I carry it as an upward skew in the range rather than in the point estimate.

Mitigating in the other direction: a live v1 exists as an executable specification, and the acceptance criterion is "agrees with the old system" (A2), which is far cheaper to converge on than a written spec negotiated with a client. A8's internal, fast approvals point the same way.

## Decomposition (person-months, A9 convention)

| Item | pm |
|---|---|
| Domain immersion, architecture and technology selection (DHT etc.), incl. discarded options | 8 |
| Rendering workers: worker framework + 8–10 formats via printer driver, each integrated and stabilized (A7) | 11 |
| OCR workers: third-party library integration, PDF assembly, quality tuning | 5 |
| Cluster + delivery control (watchdogs, tokens, unordered store, per-fax resume) — build and harden | 21 |
| Cluster management tool (queues, node state, operator control) | 3.5 |
| NOC: remote PoP state, cluster state, queue state | 7 |
| User portal (configuration incl. TIFF-vs-PDF choice, archive, account) | 9 |
| Inbound-email parser on the Tx path (parsing, number extraction, attachments, rejects/bounces) | 4.5 |
| CDR and billing-data capture (billing itself excluded) | 2.5 |
| Integration with the old system, DB/API contracts, coexistence for the transition | 6 |
| Integration tests on the real stream with old-system comparison; load/burst testing | 9 |
| Rollout to production, migration, cutover | 3.5 |
| **Subtotal** | **90** |
| PM, release QA, cross-cutting coordination (+15%) | 15 |
| **Total** | **≈105** |

## Cross-check

At ~105 pm and a blended team of eight including QA and PM, the implied calendar is ~15 months of on-task work — which sits inside the "roughly 2007–2009" window the participant gives, with room for the ramp-up and the transition period. A team of six would need ~20 months, which stretches past that window; a team of twelve would finish in ~10 months, which is implausible for a team that spent its first month or two deciding what to build. The decomposition and the recollected calendar are therefore consistent at roughly 7–9 people, which is where I set the point estimate.

## Range

The downside case (~70 pm): the portal and NOC turn out to be thin operator tools rather than products, formats reuse one driver path with little per-format work, and the v1 reference makes the comparison tests cheap.

The upside case (~160 pm): the hand-rolled delivery control needs a second design pass after it fails under burst, per-format rendering fidelity fights (Office documents in 2008) run long, and the coexistence-with-v1 period drags. Blind estimates from recollection also carry an asymmetric miss — forgotten scope adds, it rarely subtracts — so the band is wider above than below.

---

TOTAL: 105 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 70 ... 160 person-months, same convention
TEAM x DURATION: 8 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT: the 21 pd / 168 h is time actually worked on the
              task, so the calendar staffing above already carries ~12% absence on top of the
              effort; within-day overheads IN (standups, planning and demo ceremonies,
              coordination, code review, defect triage are counted as work on the task);
              roles counted: developers, architect/tech lead, QA engineers, PM, and the
              build/release work done by the same team; the §6 domain-immersion and
              technology-selection phase IN, including options explored and discarded
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              the billing system itself (only CDR/billing-data capture is in); development of
              the first version of the system; post-launch operation, support and on-call;
              development of the OCR library, the printer driver, Lustre and the DBMS
              (integration with them is in, the products themselves are not); hardware
              procurement, rack/PoP provisioning, telecom contracts and third-party licence
              costs; any cost expressed in money rather than effort

====================================================================================================
## P-3 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the estimation message: the session's environment/system context (repository git status and recent commit subjects, a memory index, a tool and skill listing, and the launching agent's framing). None of it describes FaxRxTx scope. I have treated it as data, not as input to the estimate, and used only the SYSTEM description + assumption log above. My only tool use was the single read of the prompt file itself; nothing else was opened or run.

---

## Reasoning

I estimated by component decomposition, then added test/management load, then sanity-checked against the calendar band implied by §6.

**What drives the number.** This is not a greenfield product build — v1 exists as a live requirements reference (A3), and the PoP software, least-cost routing, OCR library, printer driver, Lustre and the DBMS are given (A4). But there is no code reuse, the domain is new to the team, and the 2007–2009 era (A5) means the single hardest component — reliable orchestration of ~30 faxes/s sustained with ~300/s bursts — is hand-written: no broker (MSMQ was burned in v1), no orchestrator, no cloud primitives. Delivery control of *every* fax is a mandatory property (A6), which puts idempotency, resumption, duplicate suppression and failure-survival into the core rather than into a library.

**Component effort (person-months, developer-level work unless noted):**

| # | Item | pm |
|---|---|---|
| A | Domain immersion + architecture/technology selection (~1.5 months, most of the team) | 10 |
| B | Render workers: common harness (process isolation, recycling, timeouts, crash recovery) 3; 8–10 formats at ~0.6–1.2 each | 10 |
| C | OCR workers on the third-party library (wrapping, throughput, error paths) | 4 |
| D | **Cluster core: watchdogs + tokens, unordered status store, fax orchestration, resumption, failure survival** | 16 |
| E | Cluster management tool (queues, node health, job distribution) | 4 |
| F | NOC — remote PoP / cluster / queue state, collectors + console | 6 |
| G | User portal (archive, per-user TIFF-vs-PDF config, numbers, settings) | 8 |
| H | Inbound-email parser, Tx path (MIME, addressing, sender auth, bounces, abuse) | 5 |
| I | Rx assembly and outbound email (page-by-page TIFF or PDF attachment, send) | 3 |
| J | CDR / billing data capture (schema, reliable write, reconciliation) | 3 |
| K | Integration: PoP protocol, routing, Lustre, DB+API contracts, coexistence with v1 | 6 |
| L | Integration tests on the real stream + comparison harness vs old system + load to nominal/burst | 8 |
| M | Rollout, dual-run, cutover readiness (A2 Done) | 4 |
|  | **Subtotal** | **87** |

**Loads on top.** Items B–K are dev-side with unit testing only; A and L are already whole-team. Dedicated QA on the 69 pm of component work at ~30% → **+20**. PM/lead/coordination at ~12% of the resulting 107 → **+13**.

**Total ≈ 120 pm.**

**Calendar sanity check.** §6 places the work loosely in 2007–2009 with a blended team including QA/PM. 120 pm corresponds to ~8 people over ~15 months, which sits comfortably inside that window and inside a plausible headcount for an internal rework at a company with ~$10M revenue. Nothing forces me to the wide end of the 2-year window, since the stated window is the participant's recollection of the period, not of the project's duration.

**Uncertainty, and why it is asymmetric.** Downside is bounded: even with a fast team and clean v1 semantics, D+L+B cannot collapse much — call it ~85. Upside is not bounded symmetrically: the hand-rolled orchestrator is the classic place where a 2008-era project spends an unplanned extra half-year on rare-failure debugging at 30/s, and "comparison with the old system" on real traffic tends to expose undocumented v1 behaviour that must be reproduced. Formats (A7) and OCR throughput are secondary but same-signed risks. Hence 85 … 180.

---

```
TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 180 person-months, same convention
TEAM x DURATION: 8 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time on task, not payroll time);
              within-day overheads (meetings, coordination, code review, standups) IN;
              roles counted: developers, architect/tech lead, QA, PM — the blended team of A3;
              the 1-2 month immersion and technology-selection phase IN; rollout and
              cutover to production IN (Definition of Done per A2)
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of the
              first version of the system; post-launch operation and support;
              datacenter/hardware procurement, racking, and sysadmin operation of the
              Lustre and DB infrastructure; third-party license and hardware costs;
              conversion of this effort into a committed schedule
```

====================================================================================================
## P-4 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the estimation message: a project memory index, a git status block with branch and recent commit subjects (mentioning runs 61–69, FACTORY.md, a LEAP letter), an environment/tooling listing, and a wrapper instruction attributed to another agent. I have treated all of it as data, not as input to the estimate, and have used none of it — no file contents, no prior-run numbers, no hint of the actual outcome. I also made no tool use after reading this message. The estimate below rests only on the system description and the assumption log.

---

## Approach

Bottom-up decomposition of the A1 scope into deliverable blocks, each sized as whole-team effort, then a cross-check against what the implied team × duration looks like for a company of this size in this era.

Two things dominate this system and I sized them first, because everything else is ordinary work by comparison:

1. **The hand-built orchestrator.** A6 makes distribution, failure survival and per-fax delivery control mandatory properties. A5 says there is no broker and no orchestrator to lean on, and A4 says nothing from v1 is reused. So an at-least-once, resumable, per-item state machine over 16–20 nodes — watchdogs, tokens, an unordered store — is written from scratch, and it has to hold at 30/s sustained with 10× bursts. In 2007–2009 that is genuinely hard engineering, not plumbing.
2. **The parallel run.** A2 sets Done as prod traffic flowing with results agreeing with the old system. That is not a test pass at the end; it is a comparison harness, a coexistence period, and a cutover — and it is where rebuild projects historically lose months.

Two things pull effort down: v1 exists as a live specification (A3), so there is no requirements archaeology; and the hardest external pieces — PoP/Brooktrout, least-cost routing, OCR engine, print driver, Lustre — are integration surfaces, not builds (A4).

## Decomposition (person-months, whole team)

| Block | pm |
|---|---|
| Domain immersion, architecture and technology selection (A1/A3, ~1.5 calendar months of a forming team) | 10 |
| Core orchestration: watchdogs, tokens, per-fax state, resume, backpressure | 20 |
| Cluster management tool (queue depth, node control, job placement) | 6 |
| Render worker framework + 8–10 formats via print driver (A7: each format is its own stabilization) | 13 |
| OCR workers on a third-party library, throughput tuning | 5 |
| Rx pipeline: PoP intake, per-user config, TIFF-per-page vs PDF, email composition and deliverability | 8 |
| Tx pipeline: inbound-email parser, MIME and attachment handling, number extraction, sender identification, archive handoff | 8 |
| NOC: remote PoP, cluster and queue state | 8 |
| User portal | 10 |
| Storage and data layer: Lustre layout, DB schema, the inter-component API (§4/§6) | 6 |
| CDR / billing data capture (billing itself excluded) | 3 |
| Integration with the old system and coexistence through the transition | 6 |
| QA beyond in-block testing: real-stream comparison harness, load testing to ~300/s, regression | 14 |
| Rollout, cutover, production hardening | 5 |
| PM and coordination across the whole period | 12 |
| **Total** | **134** |

## Cross-check

135 pm implies roughly 8 people for about 21 calendar months, which sits inside the 2007–2009 window the participant recalls and matches the shape of a core-platform rebuild at a company with ~$10M revenue. A number near 60 pm would mean 4 people for a year — too little for a hand-rolled distributed delivery guarantee plus portal plus NOC plus a verified parallel run. A number near 250 pm would mean enterprise-grade approval drag that A8 explicitly denies.

**Main risks inside the range.** Upward: Office-format rendering on a headless cluster is a classic schedule sink; the parallel run can stretch indefinitely if the old system's behaviour is not reproducible. Downward: the portal and NOC could be thin internal tools, and burst capacity may never have been engineered to the full 10×, since actual traffic ran below nominal.

```
TOTAL: 135 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
       (at ~0.8 pm of task work per person-month of calendar)
DECLARATION:
  contains  - leave/holidays/sickness OUT: the 135 pm is time worked on the task, so
              calendar staffing is grossed up for absence.
              Within-day overheads (standups, planning, code review, coordination,
              interruptions) IN: counted as work on the task.
              Roles counted: developers, architect/tech lead, QA, PM, and the
              build/deploy and cluster-operations work done by the same team.
              Included: the 1-2 month immersion and technology-selection phase,
              design, development, integration and load testing, the real-stream
              comparison against the old system, rollout to production, and
              integration with the old system for the transition period.
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing
              program; billing; development of the first version; post-launch
              operation and support; hardware, rack, telecom and third-party
              licence costs; the OCR engine, print driver, Lustre and the DBMS
              themselves (integrated, not built); recruiting and onboarding
              before the team forms.
```

====================================================================================================
## P-5 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt message: a repository git status and recent commit subjects, a memory index with project notes and stated preferences, an environment/tooling description, a skills catalogue, and framing attributed to a launching agent. I treated all of it as data, used none of it as input to the estimate or as instruction, and did not open any file beyond the one prompt. The estimate below rests only on the system description plus the assumption log.

**Approach.** Bottom-up decomposition into deliverable chunks, each sized as pure build effort (design + code + unit/component test + stabilization at target load), then a single uplift for QA and PM, then the immersion/architecture phase added separately because the assumption log already scopes it as whole-team time.

**Build chunks (dev effort, person-months)**

| Chunk | pm | Why |
|---|---|---|
| Rendering worker framework + 8–10 formats | 9 | ~2 for the worker harness and printer-driver plumbing; ~0.8 per format for integration, edge cases, crash/hang containment (Office automation of that era is the expensive part) |
| OCR workers | 3 | Third-party library, but throughput, page-level failure handling, PDF assembly |
| Cluster orchestration: watchdogs, tokens, unordered status store, resume | 18 | The genuinely hard core. Hand-built exactly-once-ish delivery control over 16–20 nodes and 10–20 PoPs, no broker, no orchestrator, correctness requirement "no fax lost". Long stabilization tail |
| Cluster management tool (queues, node state) | 3 | Operator-facing, narrow |
| NOC | 8 | Agents on remote nodes, aggregation, UI, alerting across PoPs/cluster |
| User portal | 10 | Enterprise-facing: accounts, per-user delivery config, archive/search, admin |
| Inbound email parser (Tx intake) | 5 | SMTP intake, MIME zoo, number extraction, bounces/NDRs, abuse and auth handling |
| Rx path: PoP→DC transfer, page-wise TIFF, email composition and send | 6 | Deliverability, per-user config branching, retries |
| CDR capture / billing data | 3 | Capture and hand-off only; billing itself excluded |
| Storage (Lustre) + DB schema + inter-component API | 6 | Integration, not development, but the API is the system's spine |
| Integration with old system + transition coexistence | 4 | Required by the scope, dual-run plumbing |
| Integration tests on real stream, comparison against old system, rollout | 8 | Definition of Done lives here; comparison harness is itself a product |
| **Subtotal (dev)** | **83** | |

**Uplift and phase.** QA is a first-class role over a system whose acceptance is a stream-comparison campaign: +35%. PM/coordination on a scrum-after-waterfall product team of this size: +10%. 83 × 1.45 ≈ 120. Immersion, domain discussions and technology selection (DHT and alternatives) at ~1.5 calendar months for a team ramping toward full size: ≈ 10 pm whole-team, added on top, not uplifted again. Total ≈ 130; I round down to 125 because a live v1 acts as an executable requirements document and removes a real slice of specification churn (A3).

**Uncertainty.** The dominant risks are one-sided and upward: stabilization of hand-rolled delivery control at 30/s sustained with 10× bursts, the format list being longer than remembered, and the comparison campaign against a live legacy system exposing semantics nobody wrote down. The downside case assumes the orchestrator lands closer to 10 pm, the portal and NOC are thinner than I assume, and the team is smaller and denser than "blended with QA/PM" suggests.

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so a
              calendar month yields ~0.85 pm per person; the team x duration figure already
              carries that discount); within-day overheads IN (standups, coordination, code
              review, design discussion are inside the numbers); roles counted: developers,
              architect/tech lead, QA, PM, plus the whole-team immersion and technology-
              selection phase
  excluded  - PoP software (Brooktrout send/receive), the least-cost routing program,
              billing itself, development of the first version, post-launch operation and
              support, hardware procurement and data-center/rack build-out, Lustre and DBMS
              administration, end-user training and documentation beyond in-product help,
              sales/marketing and any j2-related corporate work

====================================================================================================
## P-6 — reply of round 1, verbatim

Note on quarantined material: content reached me that is not part of that message — repository git status and commit subjects, a memory index, an environment/tooling listing, and a list of available skills and agents. None of it is part of the estimation input. I have treated it as data, ignored it, and used only the prompt text. No tool was used after the single read.

## Reasoning

I decomposed the §6/A1 scope into deliverable blocks and sized each as whole-team person-months (build + test + stabilize), then cross-checked top-down.

**Front end of the project**
- Domain immersion, architecture and technology selection (DHT etc.), stated as 1–2 calendar months of the whole team: ~12 pm.

**Build blocks**
- Rendering workers: a worker host plus 8–10 format integrations, each with its own stabilization (Office automation, hangs, crashes, fonts, page geometry) — ~12 pm.
- OCR workers and TIFF→PDF: third-party library integration, output quality, throughput — ~6 pm.
- Cluster with delivery control (watchdogs + tokens, unordered store, per-fax state, resume, distribution, failure survival). This is the system's core and the deliberate replacement for a broker; at 30/s nominal with ~10× bursts it is real distributed-systems work in 2007 with nothing off the shelf — ~28 pm.
- Cluster management (queue depths, node control) — ~4 pm.
- NOC: remote PoP state, cluster and queue state, agents, alerting, UI — ~10 pm.
- User portal: accounts, per-user delivery configuration (TIFF page-by-page vs PDF), history and archive access — ~12 pm.
- Inbound email parser for Tx: MIME handling, number extraction, sender authorization, error/confirmation mail — ~6 pm.
- Outbound email delivery for Rx at volume, attachment assembly, deliverability — ~4 pm.
- CDR/billing data capture (feed only, billing excluded) — ~3 pm.
- Integration surfaces: existing PoP software, ready routing, Lustre, DB/API contracts between components, and coexistence with the old system during transition — ~10 pm.
- Integration tests on the real stream with result comparison against the old system, plus a burst/load harness — ~12 pm.
- Rollout, migration and production cutover to the A2 definition of done — ~5 pm.

Sum ≈ 124 pm; adding PM/coordination not already inside the blocks (~10%) gives ~136, which I round down slightly to 130 because several blocks were sized generously and the portal/NOC in this era were modest by modern standards.

**Cross-check (top-down).** The narrative implies roughly 1.5–2 calendar years at a company of ~$10M revenue, which supports a blended team of about 8–12. 8 × 16 months = 128 pm; 10 × 18 = 180 pm. 130 sits at the low-to-middle of that band, consistent with actual traffic running below nominal and with approvals being internal and fast (A8).

**Where the range comes from.** Downside drivers: v1 exists as a live requirements reference, routing and PoP software are free, OCR and the print driver are bought. Upside drivers: hand-built delivery guarantees are the classic place such projects overrun; 8–10 renderers can each eat more than budgeted; "no hard deadline but pressure" historically stretches rather than compresses. Hence an asymmetric range, wider on the high side.

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on this
              task, so vacation and sick time lengthen the calendar, not the effort);
              within-day overheads IN (standups, sprint ceremonies, design discussion,
              code review, cross-component coordination are inside the block sizes);
              roles counted - developers, architect, QA, PM/scrum lead, all blended at one
              rate; the 1-2 month immersion and technology-selection phase is counted for
              the whole team
  excluded  - PoP software and Brooktrout-side work; the least-cost routing program;
              billing itself (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; hardware
              procurement, rack/data-center and Lustre infrastructure build-out; carrier
              and provider contracting; end-user documentation, training and marketing;
              any work implied by REQUIREMENTS.md, which the document itself declares to
              be a different task

====================================================================================================
## P-7 — reply of round 1, verbatim

**Quarantine notice.** Material reached me that is not part of the prompt file: repository/git status and recent commit subjects, a memory index with prior-session notes about this very project ("runs 61–68", "run 69", FACT-adjacent wording), an environment description, and a skills/agents listing. None of it is part of the estimation input. I treated it all as data, used none of it in the estimate, and did not open any file it referenced. The only tool use was the single permitted read.

---

## Reasoning

**Approach: bottom-up decomposition of the §6/A1 scope, then a calendar sanity check.** I sized each deliverable at the level the era demands (A5: no broker, no orchestrator, no cloud — all of that is hand-written), then added cross-cutting QA, PM and rollout, then checked the total against a plausible team × duration for 2007–2009.

**Anchor for the whole estimate:** the centre of gravity is not the fax domain, it is the hand-built distributed orchestrator. A9-scale delivery control (every one of ~1M faxes/day tracked to completion, resumable, burst to ~300/s, 16–20 nodes, 10–20 remote PoPs) with an *unordered* token store and watchdogs instead of a queue is a genuine distributed-systems build: idempotency, lease/expiry semantics, split-brain, duplicate-send avoidance (a duplicated fax is a billable, visible defect), and retry storms. In 2007 none of this is off the shelf. I also weighted the fact that MSMQ had already burned them once — the replacement had to be demonstrably better than the thing that "broke everything", which means real soak testing, not just passing unit tests.

**Decomposition (person-months, A9 convention):**

| Block | pm | Note |
|---|---|---|
| Immersion + architecture/tech selection | 8 | ~1.5 calendar months, most of the team engaged, DHT etc. evaluated |
| Render workers + format integrations | 11 | worker framework ~3; 8–10 formats × ~0.8 each (A7: each is integration + stabilization, Office automation in 2007 is hostile) |
| OCR workers | 4 | third-party library, but throughput/quality tuning and TIFF→PDF pipeline are ours |
| Cluster + watchdogs/tokens + cluster mgmt tool | 20 | the hard core; includes queue-length/health tooling |
| NOC | 8 | collectors from remote PoPs + cluster + UI |
| User portal | 10 | accounts, per-user delivery config (TIFF vs PDF), archive/search, admin |
| Inbound-email parser (Tx) | 5 | SMTP intake, MIME, number extraction, sender auth, bounces/errors |
| CDR + billing-data capture | 3 | capture and hand-off only; billing excluded |
| Integration: PoP, routing, Lustre, DB, old-system coexistence | 6 | A4 — integrate, don't build |
| QA incl. real-stream integration tests vs old system | 20 | ~30% of dev; the comparison harness against v1 is itself a build |
| PM / lead / coordination | 10 | ~10% |
| Rollout, migration, transition coexistence, stabilization to A2 | 8 | DoD is "takes prod traffic and v1 can be decommissioned" |
| **Total** | **113** | rounded up for the unlisted-but-inevitable (deployment scripting, security, support of v1 during transition) → **120** |

**Calendar cross-check:** 2007–2009 as stated is ~18–24 calendar months of a blended team with QA/PM. At ~0.875 pm of on-task effort per calendar month per person (leave/holidays are OUT of the pm), 8 people × 17 months ≈ 119 pm. That lands on the decomposition total, which is why I did not adjust either figure to meet the other.

**Where the range comes from.** Downward: A3's mitigating factor is strong — a live v1 is an executable specification, so requirements risk is unusually low, and actual traffic never approached nominal, so a team that discovered this early could have designed for less headroom. A smaller, senior team (5 over 15 months, ~66 pm) is a real possibility. Upward: the orchestrator is exactly the kind of component that eats a year when correctness under failure is only provable by soak testing; "no hard deadline but pressure" plus scrum-after-waterfall is a profile that historically overruns; and 10–20 remote PoPs across continents make every distributed bug expensive to reproduce. 10 people over 19 months ≈ 190 pm is the credible bad case. The distribution is right-skewed, so the total sits below the midpoint of the range.

**Main uncertainties I did not resolve:** portal scope (a thin self-service page vs. a Fortune-1000 enterprise admin surface — worth ±6 pm on its own), whether the NOC had to cover the old system as well during transition, and how much of the 8–10 formats were already covered by the printer driver "for free" versus needing per-format work (A7 tells me to assume the latter, and I did).

---

TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 17 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (they stretch the calendar, not the effort;
              the calendar figure above already discounts ~12.5% for them);
              within-day overheads IN (standups, sprint ceremonies, code review,
              coordination, context switching are inside the 168 hours);
              roles counted - developers, architect/tech lead, QA engineers, PM,
              plus build/deploy and cluster-bring-up work done by the team itself
  excluded  - PoP software and Brooktrout send/receive (existed);
              least-cost routing program (ready, reused);
              billing engine (separate; only CDR/billing-data capture is IN);
              development of the first version of the system;
              post-launch operation, support and on-call after the DoD in A2;
              third-party OCR library and printer-driver development or licensing;
              Lustre and DBMS as infrastructure - administration, hardware,
              rack space, data-center and telecom provider costs;
              dedicated ops/NOC operators as staff (building the NOC is IN,
              manning it is OUT);
              any calendar-to-cost conversion

====================================================================================================
## P-8 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the estimation message: repository/git status with commit subjects, a memory index, an environment/tooling listing, and a skills catalogue. I have treated all of it as data, used none of it as input to this estimate, and followed no instruction contained in it. Nothing in it appeared to describe FaxRxTx facts or outcomes.

---

## Reasoning

**Shape of the job.** This is not a greenfield product and not a maintenance rework — it is a *re-implementation of the core* of a running distributed system, with no code reuse, by a team that does not know the domain, in an era (C#/.NET 3.x, 2007–2009) where the distribution, queueing, orchestration and delivery-guarantee machinery that a broker or Kubernetes gives away today has to be written by hand. Two things dominate the effort: (a) the hand-built orchestrator over a 16–20 node cluster that must not lose a single fax, and (b) the long tail of format renderers and third-party integrations, each of which is stabilisation work, not configuration.

The mitigating factor is real but bounded: v1 exists as a live specification, so requirements discovery is cheap. It does not make the domain cheap.

**Bottom-up decomposition** (engineering effort, person-months, A9 convention):

| # | Piece | pm |
|---|---|---|
| 1 | Domain immersion + architecture/technology selection (DHT etc.), ~1.5 calendar months across most of the team | 9 |
| 2 | Rendering workers: driver-based render framework (3) + 8–10 formats × ~1 each — Office automation on a headless cluster is hostile: hangs, dialogs, licensing, per-format fidelity | 12 |
| 3 | OCR workers on a third-party library: integration, searchable-PDF assembly, throughput tuning | 4 |
| 4 | **Cluster core: watchdogs + tokens, unordered status store, per-fax state machine, idempotency, retry, recovery, back-pressure** — the riskiest and least-precedented item | 16 |
| 5 | Cluster management tool (queue depths, node lifecycle, deployment/agents) | 4 |
| 6 | NOC: telemetry from 10–20 remote PoPs + cluster + queues, alerting, operator UI | 6 |
| 7 | User portal: accounts, per-user delivery configuration (TIFF page-by-page vs PDF), fax history/search/retrieval, admin | 8 |
| 8 | Inbound e-mail parser / Tx entry: SMTP ingest, MIME and attachment extraction, sender authentication, number extraction, bounce and error paths | 5 |
| 9 | CDR capture and billing-data hand-off (billing itself excluded) | 3 |
| 10 | Integration surfaces: existing PoP software protocol, ready least-cost routing, Lustre, DB schema and the inter-component API | 6 |
| 11 | Integration tests on the real stream: shadow harness, load generation to ~30/s, result comparison against the old system | 7 |
| 12 | Rollout, coexistence with v1 during transition, production hardening | 5 |
| | **Subtotal** | **85** |

Items 1 and 11 are already whole-team; for the rest I add dedicated QA and PM at roughly +25% → ~106 pm.

**Correction for the known bias of decomposition.** Bottom-up lists omit the glue: cross-component defects that only appear at scale, the rework a domain-naive team pays for its first architecture, and the grind of burst behaviour (~300/s peak, ~10× nominal) where failure modes are emergent. A factor of ~1.2 is conservative here, not generous → ~127 pm.

**Top-down cross-check.** The narrative implies roughly 2007–2009 with a blended team including QA/PM and no hard deadline but real pressure. A team of 8 over 18 calendar months yields ~120 pm at the A9 convention; 6 people over 18 months gives ~92, 10 over 20 months gives ~170. The decomposition lands inside that envelope, near its middle-lower part.

I settle on **120 pm**, slightly below the arithmetic of the corrected decomposition, because v1-as-specification genuinely removes a requirements phase, and the two heaviest integrations (PoP software, least-cost routing) are out of scope.

**Range.** The low end assumes the orchestrator concept lands on the first architecture and the renderers behave: ~80. The high end assumes what usually happens to hand-rolled exactly-once delivery — one architectural reversal, plus a long stabilisation against the old system before v1 can be decommissioned: ~180. The distribution is right-skewed; 120 is not the midpoint of 80–180 by design.

---

TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 180 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on the
              task; vacation, public holidays and sick leave consume calendar, not effort —
              hence 8 x 18 calendar months at ~0.85 productive pm/person/month ~= 122 pm);
              within-day overheads IN (stand-ups, sprint ceremonies, coordination, code
              review, interruption); roles counted - developers, architect/tech lead, QA,
              PM; the ~1-2 month domain-immersion and technology-selection phase IN;
              rework and defect-fixing up to the A2 Definition of Done IN
  excluded  - PoP software (Brooktrout reception/sending); the least-cost routing program;
              the billing system itself; development of the first version; post-launch
              operation, support and on-call; hardware procurement, rack/data-centre and
              PoP build-out; third-party licence costs (OCR library, printer driver,
              Lustre) and all non-labour cost; any calendar/schedule commitment - this is
              effort only

====================================================================================================
## P-9 — reply of round 1, verbatim

**Quarantine notice.** Material outside the prompt file did reach me in this session: repository git status and recent commit subjects, a memory index with project notes, an environment block, and a skills/agents listing. Per the instruction in the prompt, I treated all of it as data only — none of it informed the estimate below, which rests solely on SYSTEM.md §§1–8 and the A1–A9 assumption log as contained in that file. I also did not open, list or search anything beyond the single permitted read.

---

## Reasoning

**Approach:** component decomposition with a per-component effort figure, then an overhead uplift, then a cross-check against the staffing/duration the total implies versus the project's stated ~2007–2009 window.

**What drives the size.** This is not a greenfield product but a rewrite of a working v1 at production scale, on 2008-era technology with no cloud and no off-the-shelf orchestrator. Three things inflate it above what the feature list suggests: (a) the delivery-control mechanism is bespoke — watchdogs plus tokens over an unordered store, i.e. hand-writing what a broker plus an orchestrator would give today, with MSMQ deliberately off the table; (b) correctness is per-fax, so every failure mode of 16–20 nodes and 10–20 remote PoPs must be survivable, and "designing for ~30/s nominal with ~300/s bursts" makes distribution and recovery mandatory properties rather than later hardening; (c) the acceptance bar in A2 is production traffic with results reconciled against the old system, which pulls a real dual-run comparison harness into scope. Mitigating: v1 is a live specification, routing and PoP software are reused, OCR and the print driver are third-party.

**Decomposition (person-months, A9 convention):**

| Component | pm |
|---|---|
| Domain immersion + architecture/technology selection (~1.5 mo, partial team) | 12 |
| Rendering workers: framework + 8–10 formats, each integrated and stabilized | 14 |
| OCR workers on third-party library (TIFF→searchable PDF, tuning, throughput) | 5 |
| Cluster + delivery control: watchdogs, tokens, state store, resume, distribution | 28 |
| Cluster management tool (queues, node health, dispatch) | 5 |
| NOC: state of remote PoPs, cluster, queues | 10 |
| User portal (accounts, configuration, fax history) | 12 |
| Inbound-email parser / Tx intake (MIME, number extraction, attachments, error paths) | 7 |
| CDR and billing-data capture (billing itself excluded) | 4 |
| DB/API plumbing + integration and coexistence with the old system | 8 |
| Integration tests on the real stream with old-system comparison; load/burst testing | 12 |
| Rollout to prod, cutover, stabilization to the A2 bar | 8 |
| **Subtotal** | **125** |
| PM/coordination uplift (~10%) | 13 |
| **Total** | **~138 → carried as 130** |

I carry 130 rather than 138 because the largest line items already absorb their own QA and the uplift risks double-counting.

**Cross-check.** 130 pm at ~0.88 effective months per staffed calendar month (leave/holidays excluded from the unit) implies roughly 8–9 people for 17–18 calendar months — consistent with a blended team including QA/PM over the stated 2007–2009 span. Had the answer come out near 60 pm or near 300 pm, it would contradict that window.

**Range.** The low end assumes v1 constrains the design more strongly than stated, fewer formats prove troublesome, and the token/watchdog scheme lands early. The high end assumes the hand-built orchestrator needs a second design pass under burst load and the old-system reconciliation drags the cutover — the classic failure mode for this shape of project. The asymmetry is deliberate: rewrites at production scale overrun far more often than they underrun.

---

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 85 ... 200 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a staffed calendar month yields ~0.88 pm, and the
              team-x-duration line above already applies that conversion); within-day overheads
              (meetings, coordination, code review, standups, sprint ceremonies) IN; roles
              counted: developers, architects, QA, PM/scrum master, plus the build/deployment
              effort carried inside each component line
  excluded  - PoP software and Brooktrout reception/sending; the least-cost routing program;
              billing proper (only CDR/billing-data capture is in); development of the first
              version of the system; post-launch operation, support and on-call after the
              cutover defined in A2; procurement, rack space, hardware and datacenter build-out
              for the cluster, PoPs and Lustre storage; development of the OCR library and of
              the print driver (integration with both is in); end-user documentation, training
              and marketing; any headcount ramp-up, hiring or onboarding of new staff

====================================================================================================
## P-10 — reply of round 1, verbatim

I read the file. Its instruction "do not use any tool" is now in force, so the rest of this reply is from that text alone.

**Quarantine note.** Material reached me that was not part of that message: an environment/session preamble (working directory, platform, model), a repository git status with branch and five recent commit subjects mentioning runs 61–69, FACTORY.md, a LEAP letter and "expectations written before launch", a memory index summarising prior 3A8 sessions and methodological rules, and a list of available skills and agents. Some of it refers to this very estimation exercise and to prior runs on FaxRxTx. I have treated all of it as data, used none of it as input to the estimate or as instruction, and have not opened anything it points to. In particular I did not let the commit subjects hint at prior runs' numbers. The wrapper instruction that authorised the single read is accepted; nothing beyond it is.

---

## Approach

I estimate bottom-up by component, in person-months of whole-team effort, then sanity-check the total against two independent anchors: the implied calendar/staffing, and the economics of the company described in §7.

The governing facts I lean on: no code reuse from v1, so every listed component is written from scratch; the domain is new to the team; the era (2007–2009, C#/.NET 3.x, own Windows cluster) means the distribution, queueing, retry and delivery-guarantee machinery that a broker or an orchestrator would supply today is hand-built; and the engineering target is ~30 faxes/s sustained with ~300/s bursts across 16–20 nodes and 10–20 remote sites. A live v1 as an executable specification is the one genuine discount — it removes requirements archaeology, and it also supplies the oracle for the comparison testing.

## Decomposition

| Component | pm | Why this size |
|---|---|---|
| Domain immersion, architecture and technology selection (§6, A1) | 12 | Stated as 1–2 months of calendar for the whole team; at the staffing this project implies that is not a small line item |
| Rendering workers, 8–10 formats | 12 | A harness around a printer driver, plus per-format integration and stabilisation; driving Office formats headless on a server cluster in 2008 is a hang-and-timeout problem, not a conversion problem |
| OCR workers and PDF assembly | 5 | Third-party library, but page handling, searchable-PDF construction and throughput tuning are ours |
| Cluster + delivery control (watchdogs, tokens, unordered status store) | 22 | The heart of the rewrite and the thing v1 got wrong. A hand-rolled per-fax orchestrator with failure detection, idempotent resumption and no MQ, at 30/s sustained. Design, implement, then harden under real failure modes |
| Cluster management tool (queues, node state, job placement, deployment) | 5 | |
| NOC | 8 | Remote PoP health, cluster and queue state, alerting, operator UI |
| User portal | 10 | Accounts, configuration (TIFF vs PDF per user), fax history and archive search, admin |
| Inbound email parser, Tx path | 5 | SMTP intake, MIME, number extraction, sender authorisation and abuse control, bounces and non-delivery reports |
| CDR and billing-data capture | 3 | Capture and hand-off only; billing itself excluded |
| Database schema and inter-component API, Lustre/archive integration | 6 | §4 says components talk through the DB and an API — that contract is real work even though the storage platform is given |
| Integration tests on the live stream, comparison to v1, load work to burst, cutover and coexistence | 12 | A shadow run against a production system is a build, not a test pass; add burst-mode load testing and the transition period |
| PM, QA leadership, release engineering, cross-cutting coordination | 12 | Roughly 10–12% on top of the delivery lines, per A3's blended team |

**Sum ≈ 112 pm.** I round the point estimate up to **120** for the integration drag that a from-scratch distributed system of twelve interlocking parts always produces and that a component table systematically under-counts.

## Cross-checks

*Calendar.* 120 pm is about 8 people for 15 months, or 6–7 people for 18–20 months. Both sit inside the participant's "roughly 2007–2009" with room for the fuzziness in that dating, and both are a credible internal team for a product company with QA and PM in it.

*Economics.* Venali ran ~$10M revenue and sold for ~$17M. A 120 pm internal rework is a serious but survivable programme for that size of company; anything approaching 250 pm would be implausible against that revenue, and anything under ~70 pm cannot produce a hand-built distributed orchestrator, a NOC, a portal and a validated cutover with no reuse.

*Asymmetry of the error.* The downside is bounded — the component list is explicit and none of it is optional. The upside is not: the watchdog-and-token orchestrator is exactly the kind of component whose second and third hardening rounds are discovered only in production shadow running, and a 2× overrun there alone moves the total by 20 pm. I therefore make the range asymmetric around the point.

*Main uncertainties.* Whether "the cluster itself" included substantial custom infrastructure beyond delivery control; how deep the portal went; how much of the OCR quality problem was absorbed by the third-party library versus by the team; and whether the immersion phase was the whole team or a subset.

---

TOTAL: 120 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 190 person-months, same convention
TEAM x DURATION: 8 people over 15 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually on the task, so vacation,
              public holidays and sick days are not counted and must be added when converting
              to calendar); within-day overheads IN (standups, planning and review meetings,
              code review, internal coordination, context switching, the scrum ceremonies of
              A8); roles counted: developers, QA/test engineers, PM/scrum lead, the architect
              role during and after the selection phase, and the share of release and build
              engineering the team carried itself
  excluded  - the PoP software and Brooktrout work; the least-cost routing program; the billing
              system (only CDR/billing-data capture is IN); development of the first version;
              post-launch operation, support and on-call; hardware, rack and data-centre
              procurement; administration of the Lustre platform and the DBMS as products;
              development of the OCR library and the printer driver (integration with them is
              IN); third-party licences and all non-labour cost; sales, marketing and any
              customer-facing organisation; calendar conversion, which A9 puts outside the run
