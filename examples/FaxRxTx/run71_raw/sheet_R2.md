# Round 1 — the ten replies, anonymous and verbatim

Nothing below was written, shortened or commented by the moderator.

====================================================================================================
## P-1 — reply of round 1, verbatim

**Quarantine notice.** Material outside this prompt did reach me before I read it: repository status and recent commit subjects, an index of memory files with notes on the 3A8 pipeline and prior runs, environment/session context, and tool listings. Some of it referred to this very example (FaxRxTx, run numbers, consensus figures). I have treated all of it as data, used none of it in the estimate below, and estimated from the system description and assumption log alone.

**Reasoning (decomposition, mid-values in person-months, A9 units).**

Immersion, architecture and technology selection — stated as 1–2 months of calendar with the whole blended team; ~10 pm.

Core delivery machinery, the heart of the rework: the hand-rolled orchestrator (watchdogs, token store, per-fax status, resume after failure) on 16–20 nodes, designed for 30/s sustained with 10× bursts and no broker to lean on — ~30 pm. Cluster management/queue-depth tooling ~6.5 pm. Storage and DB layer plus the inter-component API (Lustre and the DBMS as given technologies, integration only) ~6 pm.

Workers: a rendering framework plus 8–10 format integrations, each its own stabilization problem against a printer driver (A7) — ~15 pm; OCR workers on a third-party library, including throughput tuning — ~6 pm.

Paths and faces: Rx assembly (TIFF from PoP, per-page attach or PDF, per-user configuration, mail-out at volume) ~7 pm; Tx inbound-email parser (MIME, number extraction, attachment handling, sender validation, error returns) ~6 pm; NOC over remote PoPs, cluster and queues ~9 pm; user portal ~11 pm; CDR/billing-data capture ~3.5 pm.

Transition: integration and coexistence with v1 ~6 pm. Verification: integration tests on the real stream with result-for-result comparison against the old system, plus load work toward the burst target — QA-heavy, ~12 pm.

Sum ≈ 128, plus project management, release and rollout coordination at ~12% ≈ 15. Rounded to 140. The scale-driven items (orchestrator, tests, portal) carry most of the risk; a blind estimate of a rework in an unfamiliar domain deserves roughly a 0.65×/1.6× band rather than a tight one.

Since 1 pm is 168 hours *on the task*, a full-time person yields ~0.8 pm per calendar month; 140 pm therefore implies ~175 person-calendar-months of staffing.

```
TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 230 person-months, same convention
TEAM x DURATION: 11 people over 16 calendar months, the staffing this total implies
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

====================================================================================================
## P-2 — reply of round 1, verbatim

**Quarantine note.** Material outside this message did reach me: a repository git status with five recent commit subjects (mentioning runs 70–71, a "Delphi" helper, a no-method sensor note, a FaxRxTx report with pooled curves), a memory index summarising past sessions, and an environment/skills listing. Some of it concerns this very project and earlier estimate runs. I have quarantined all of it: none of it informed the numbers below, which come only from the system description and the assumption log in this message. I used no tool after reading the prompt.

---

## Reasoning

**Shape of the job.** This is a from-scratch rebuild (A4: no v1 code carried over) of the core of a production fax service, in C#/.NET ~3.x, on own hardware, with no broker and no orchestrator — everything a message queue or Kubernetes would hand you today is hand-written (A5). v1 exists as a live requirements reference, which cuts requirements work but not build work. The dominant risk is not any single component but the hand-rolled distributed delivery control at 30/s nominal with 300/s bursts across 16–20 nodes and 10–20 PoPs.

**Build-up** (development effort, person-months on the A9 convention):

| Item | pm |
|---|---|
| Domain immersion + architecture/technology selection (DHT etc.), whole team ~1.5 months | 12 |
| Worker runtime/host framework (job pickup, token store, lifecycle) | 6 |
| Render workers, ~9 formats via printer-driver integration (A7: each format is real work) | 9 |
| OCR workers on third-party library | 4 |
| Cluster orchestration: watchdogs, tokens, unordered status store, resume/retry, per-fax delivery guarantee | 24 |
| Cluster management tooling (queue depth, node health) | 5 |
| NOC (remote PoP state, cluster, queues) | 10 |
| User portal (enterprise customers: config, history, retrieval, admin) | 12 |
| Inbound-email parser for the Tx path (MIME, attachments, number extraction, error paths) | 5 |
| CDR / billing data capture (billing itself excluded) | 4 |
| DB + API integration layer, Lustre storage integration | 7 |
| Coexistence and integration with the old system during transition | 6 |
| Scale and burst hardening (30/s sustained, ~300/s peak, failure survival) | 8 |
| Integration-test harness on the real stream + result comparison against v1 | 10 |
| Production rollout / cutover to the DoD in A2 | 5 |
| **Subtotal** | **127** |
| PM/coordination layer on top (~10%) | 13 |
| **Total** | **~140** |

QA sits inside the line items (each component carries its own test effort) plus the dedicated harness line; PM is the explicit 13.

**Sanity check against the calendar.** ~140 pm over the 2007–2009 window implies roughly 7–8 people for around 18–20 calendar months — a plausible blended team (architect, 4–5 devs, 1–2 QA, PM) for a company of Venali's size (~$10M revenue). That consistency is why I did not push the central figure higher.

**Range.** The blind-estimate uncertainty is wide and asymmetric: the orchestration piece and the "agrees with the old system" acceptance bar are both open-ended, the format list may be longer than remembered, and the dating itself is soft. Low case assumes the rebuild stays closer to a straight port with a lean portal and NOC; high case assumes the hand-rolled delivery control needs two design iterations and the real-stream comparison drags.

---

TOTAL: 140 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 95 ... 210 person-months, same convention
TEAM x DURATION: 8 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (the 21-day month is productive days only, so
              calendar conversion must add ~10%); within-day overheads (meetings,
              coordination, code review) IN; roles counted: architect/analyst, developers,
              QA, PM, plus build/infrastructure work done by the same team
  excluded  - PoP software and Brooktrout-side code; least-cost routing program; billing
              system; development of the first version; post-launch operation and support;
              hardware procurement and data-center/rack work; purchase or development of
              the OCR library, the printer driver, Lustre and the DBMS (integration only)

====================================================================================================
## P-3 — reply of round 1, verbatim

**Quarantine notice.** Material outside this message did reach my context before I read it: repository/git status and recent commit subjects, a memory index with project notes, environment/session metadata, and a listing of available tools and skills. Per the instruction I treat all of it as data, not as input to the estimate, and I have not used it. No tool was used after reading the prompt. The REQUIREMENTS.md mentioned in §"A note" is likewise not used — I estimate the system described in SYSTEM.md §6 + A1.

---

## Reasoning

I decompose the A1 scope into deliverable blocks and size each in person-months (A9 convention), then sanity-check the total against the implied calendar.

Framing facts that drive the size upward: the delivery guarantee is hand-built (A5 — no broker, no orchestrator; watchdogs + tokens + an unordered status store), the target is ~30 faxes/s sustained with ~300/s bursts across 16–20 nodes and 10–20 remote sites (A6), the domain is new to the team (A3), and there is no code reuse from v1 (A4). Facts that pull downward: v1 exists as a living specification, the PoP software and least-cost routing are given, OCR and rendering are third-party engines to integrate rather than build, and approvals are internal (A8).

| Block | pm | Note |
|---|---|---|
| Domain immersion, architecture and technology selection | 10 | §6/A1 gives ~1–2 calendar months; a core group, not the full team |
| Render workers: framework + 8–10 formats | 12 | A7 — each format is its own integration and stabilization, ~1 pm apiece over a shared print-driver harness |
| OCR workers (third-party library, TIFF→searchable PDF) | 4 | integration, tuning, throughput |
| Cluster core: watchdogs, tokens, status store, recovery, distribution | 22 | the true centre of the work; correctness under failure at 30–300/s is where the time goes |
| Cluster management tool (queues, node health, deployment) | 5 | |
| NOC — remote PoP state, cluster state, queue state | 8 | agents on 10–20 remote sites plus the console |
| User portal | 10 | accounts, configuration (TIFF vs PDF), history, delivery status |
| Inbound-email parser, Tx entry path | 5 | parsing, attachment extraction, number extraction, abuse/bounce handling |
| CDR and billing-data capture (billing engine excluded) | 3 | |
| Integration with v1 and coexistence through the transition (DB + API contracts) | 6 | A4 — integrate, not reuse |
| Integration tests on the real stream, comparison against the old system, load/burst rig, production rollout | 10 | A2 puts the Definition of Done here |
| Cross-cutting PM, release engineering, documentation | 8 | QA is already inside each block |
| **Sum** | **103** | |

Rounded for false precision, ~110 pm. Cross-check: 110 pm over the ~16-month window implied by "2007–2009 with a planning phase then scrum" gives ~7 people including QA and PM — a plausible single-product team, which makes the number self-consistent rather than merely additive.

Range. The low end assumes the v1 reference cuts requirements churn hard, the formats mostly behave, and the token/watchdog design converges on the first architecture: ~75 pm. The high end assumes the classic failure mode of hand-rolled exactly-once-ish delivery — a design revision after load testing reveals loss or duplication at burst, plus a long tail on format fidelity and on reconciling results against the old system: ~170 pm. The distribution is right-skewed; 110 is nearer the mode than the mean.

---

TOTAL: 110 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 75 ... 170 person-months, same convention
TEAM x DURATION: 7 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not in the person-month and must be added
              when converting to calendar); within-day overheads IN (standups, planning,
              coordination, code review, defect triage are inside the figures); roles
              counted - developers, architect/tech lead, QA, PM, and the build/release
              share; the 1-2 month immersion and technology-selection phase is IN
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of the
              first version; post-launch operation, support and on-call; data-center,
              rack and telecom-carrier procurement and contracts; hardware purchase and
              Lustre/DB platform build-out (integration only); third-party OCR and printer-
              driver license cost; end-user training and marketing.

====================================================================================================
## P-4 — reply of round 1, verbatim

I read the file. It is a self-contained estimation prompt; per its instruction I used no further tools. Below is my complete reply in the form it asks for.

---

**Quarantine notice.** Material reached me that is not part of that message: repository git status and recent commit subjects (several of which describe runs, Delphi panels, pooled curves and "no-method control" for this very example), a memory index summarizing prior sessions on project 3A8, and environment/skill listings. I treated all of it as data, quarantined it, and did not let it inform the estimate — in particular I did not use any hint it carried about other runs' totals or method. The estimate below rests only on the system description and the assumption log in the message.

**Reasoning**

The object is a ground-up rewrite (A4: no v1 code reuse) of the core of a distributed, high-throughput fax service, in C#/.NET ~3.x on own hardware in 2007–2009, with QA and PM inside the count, ending at production traffic with results reconciled against the old system (A2).

Two things dominate. First, the correctness-at-scale machinery: with MQ deliberately excluded, per-fax delivery control, watchdogs, tokens over an unordered store, retries and failover across ~16–20 nodes and 10–20 PoPs must be written by hand. In 2008 that is the whole of what a broker plus an orchestrator would give today, and it is the part that is never "done" until the real stream has run through it. Second, the long tail of format rendering: 8–10 input formats via a print-driver path (A7) are each an integration-and-stabilization item against real-world malformed documents, not a list extension.

Bottom-up, in person-months of engineering (before QA and PM):

| Piece | pm |
|---|---|
| Domain immersion + architecture/technology selection (A1, ~1–2 months calendar, partial team) | 8 |
| Render worker framework + 8–10 formats, incl. document-pathology tail | 14 |
| OCR workers on a third-party library, PDF assembly | 5 |
| Cluster orchestration: watchdogs, tokens, state store, retry/failover, burst handling | 26 |
| Cluster management tool (queues, node health) | 4 |
| NOC (remote PoP state, cluster, queues) | 9 |
| User portal | 10 |
| Inbound-email parser and the Tx path into the PoP handoff | 5 |
| CDR / billing-data capture (billing itself excluded) | 3 |
| DB + API plumbing between components, Lustre and storage integration | 6 |
| Performance work to nominal ~30/s with ~300/s bursts, on 2008 hardware | 9 |
| Rollout, coexistence with v1, cutover and prod hardening | 8 |
| **Engineering subtotal** | **107** |

QA is not a trim here — the definition of done is agreement with the old system on a live stream, so the comparison harness, the test corpus of documents and the load rigs are real construction: ~35% of engineering, ≈ 37 pm. PM/coordination over an 18–24 month rework with an internal customer: ~12%, ≈ 12 pm. Total ≈ 156, which I round to 150 to avoid false precision.

Cross-check on shape: 150 pm, with a calendar person-month yielding ~0.85–0.9 pm after leave and holidays, implies roughly 8 people for about 21 calendar months — consistent with a 2007–2009 window and a blended team, which is reassuring rather than evidence, since that window came from the same document.

The range is asymmetric. The low end assumes the "like v1, but fixed" reference really does collapse requirements work, the format tail behaves, and a lean team stops at nominal load. The high end is the ordinary fate of hand-rolled distributed delivery control: the stabilization and reconciliation phase against the old system stretches, and the peak-mode work turns into a second project.

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 8 people over 21 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a calendar person-month is taken as ~0.85-0.9 pm,
              which is why 8 people x 21 months carries 150 pm and not 168); within-day
              overheads IN (standups, planning, code review, cross-team coordination, the
              scrum ceremony load); roles counted: developers, architect, QA (manual and
              automation, including the comparison harness and load rigs), PM/BA, plus the
              build and deployment work done by the same team
  excluded  - PoP software and Brooktrout-side reception/sending; the least-cost routing
              program; billing proper (only CDR/billing-data capture is in); development of
              the first version; post-launch operation, support and on-call; hardware,
              rack, telecom and third-party licence procurement; the Lustre and DBMS
              platforms themselves (integration only); any Australia expansion or other
              scope beyond the §6 list

====================================================================================================
## P-5 — reply of round 1, verbatim

I read the file. Its instruction "do not use any tool" is in force from that point on, so nothing else was opened and no command was run.

**Quarantine note.** Material reached me that is not part of the prompt message: repository status and recent commit subjects, an environment/tooling preamble, an agent-listing block, and a memory index with project notes (including references to prior runs of this same estimation pipeline and to a no-method control series). None of it was part of the estimation input, so I treated it as data only, kept it out of the reasoning below, and in particular did not let any earlier run's figures or any commit subject anchor the number. The estimate rests on the system description plus assumption log alone.

---

**Approach.** Bottom-up decomposition of the A1 scope into work packages, each sized in person-months of whole-team effort, then overheads and a cross-check against the implied staffing shape.

Work packages (pm):

- Domain immersion, architecture and technology selection (A3; DHT and alternatives studied) — a calendar month or two of a mostly-assembled team: **9**
- Render workers: worker harness, crash/timeout isolation on the Windows cluster, printer-driver path, then 8–10 formats each stabilized separately (A7; Office-format automation is the expensive part) — **11**
- OCR workers and TIFF→PDF conversion, third-party library integration and tuning — **4.5**
- Cluster and delivery control: the watchdog/token store, the per-fax status orchestration, failure survival, backpressure to 30/s nominal with ~300/s bursts, all hand-written because MSMQ was ruled out (A5) — the core of the job — **20**
- NOC: state of 10–20 remote PoPs, cluster and queue health, alerting, operator UI — **9**
- User portal: per-user delivery configuration, archive and history, search, admin, enterprise auth — **9**
- Inbound email parser on the Tx path: MIME and attachment handling, number extraction, cover pages, bounces, abuse and duplicate handling — **4.5**
- CDR and billing-data capture (billing itself out) — **3**
- Integration with what is reused rather than built: PoP protocol, routing program, Lustre, the inter-component DB and API contracts (A4) — **7**
- Integration testing on the real stream with result comparison against v1, plus the load harness — **9**

Subtotal **86**. Dedicated QA beyond the integration-test package, spread across features, ~15% → **+11**. PM and coordination ~10% → **+9**. Cutover, coexistence with v1 during the transition, and post-launch stabilization up to A2's Definition of Done → **+6**. Total ≈ **112**, rounded to **110**.

Cross-check on shape: 110 pm is a blended team of about seven over some sixteen months, which is consistent with a 2007–2009 window and with a team that spent its first month or two not producing code. Nothing in the document contradicts that shape.

The spread is wide because three things are genuinely unknown at this distance: the true format count and how nasty each one was, how much hardening the home-grown delivery control needed before it held under burst, and how much of the portal and NOC was scope creep. Those all push the same direction, so the range is asymmetric upward.

TOTAL: 110 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 70 ... 170 person-months, same convention
TEAM x DURATION: 7 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, so vacation,
              public holidays and sick days are not counted and must be added when this
              total is converted to a calendar); within-day overheads IN (standups, sprint
              ceremonies, code review, cross-component coordination, the planning phase);
              roles counted: developers, architect, QA, PM, and whatever build/deployment
              work the team did for itself
  excluded  - the PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing system proper (only CDR/billing-data capture is in); development
              of the first version; post-launch operation and support after the old version
              is decommissioned; hardware, rack and data-center procurement; administration
              of Lustre and the DBMS as platforms; third-party licence costs (OCR, printer
              driver) and any other money — this is effort only

====================================================================================================
## P-6 — reply of round 1, verbatim

**Quarantine note.** Material reached me that is not part of the prompt text: repository status and recent commit subjects, a memory index with prior-session notes, environment/session context, and an instruction from the agent that launched me telling me to read a file. All of it is treated as data, not as input to the estimate; it is quarantined and had no influence on the numbers below. The estimate rests only on the system description + assumption log carried in the prompt itself.

## Reasoning

I decomposed the A1 scope into deliverable blocks and sized each by what the 2007–2009 stack forces you to build by hand, then reconciled the sum against what a product company of this size could plausibly field.

**Sizing by block (person-months, A9 units):**

| Block | pm | why |
|---|---|---|
| Domain immersion + architecture/tech selection | 12 | §6/A3 say 1–2 calendar months for the whole team; at ~8–10 people that is 10–16 pm of real spend, and it is genuine work (DHT study, technology bake-offs) |
| Delivery-control core: watchdogs + tokens, unordered status store, orchestrator | 30 | the heart of the system and the riskiest part. A5 is explicit that no broker and no orchestrator exists — exactly-once-ish semantics, resume-after-failure, and per-fax state at 30/s sustained are written from scratch and then hardened |
| Render workers + printer-driver integration | 12 | ~4 pm framework, then A7's 8–10 formats at ~0.8 pm each; each format is its own integration and stabilization tail (Office automation of that era especially) |
| OCR workers + PDF assembly | 6 | third-party library, but page-by-page TIFF handling, throughput tuning and failure modes are ours |
| Cluster management tool | 6 | node/queue-depth management on 16–20 machines, no off-the-shelf scheduler |
| NOC | 10 | remote state of 10–20 PoPs plus cluster and queues; a real internal product with its own UI and alerting |
| User portal | 14 | user-facing website: configuration (TIFF vs PDF), archive access, accounts — the block most prone to scope growth |
| Inbound e-mail parser (Tx) | 8 | address/number extraction, attachment handling, malformed mail, abuse and bounce paths |
| CDR / billing data capture | 4 | capture and persistence only; billing itself is out |
| Integration: DB schema + API between components, Lustre, PoP software, routing | 10 | A4 makes these "integrate, don't build," but the cross-component contract is the project's spine |
| Integration test on the real stream + comparison with the old system + burst-load testing | 16 | A2 makes this the Definition of Done, not a nicety; a comparison harness against v1 plus load work toward the ~300/s burst |
| PM, release, coexistence/cutover with v1 | 12 | the transition period is stated in §6 and costs real effort |
| **Sum** | **140** | |

Adjustment: I add ~15% for the friction that decomposition systematically misses here — geographically distributed deployment across 10–20 PoPs, a team new to telecom, and "scrum after waterfall" with pressure but no deadline (a shape that absorbs effort rather than cutting scope). That lands at ~160.

**Cross-checks.** A9's units are effort, not calendar, so 160 pm is ~10 people for ~18 months — consistent with a ~$10M-revenue product company running a core rework, and consistent with the 2007–2009 window §6 gives. It is also consistent with the mitigating factor in A3: a live v1 removes requirements discovery, which is why I am not in the 250+ pm territory a greenfield distributed system of this throughput would demand.

**Range drivers.** Low end if the portal is thin, formats land at 8 rather than 10, and the comparison harness stays crude: ~110. High end if the hand-rolled delivery control needs a second architecture after load testing (the classic failure mode for this exact component, and v1 already burned them once on MSMQ) and the cutover drags: ~240. The distribution is right-skewed; 160 is my mode-and-a-bit, not the midpoint of the range.

```
TOTAL: 160 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 110 ... 240 person-months, same convention
TEAM x DURATION: 10 people over 18 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task; the
              calendar conversion above assumes ~0.88 pm delivered per person per calendar
              month, which is where absence is absorbed); within-day overheads (meetings,
              coordination, code review, standups) IN; roles counted: developers, architect/
              tech lead, QA, PM, and the team's own deployment/stabilization effort on the
              cluster and PoP rollout
  excluded  - PoP software (Brooktrout send/receive), the least-cost routing program, billing
              itself, development of the first version, post-launch operation and support,
              hardware/rack/data-center procurement and third-party licensing (OCR library,
              Black Ice-class driver, Lustre), sales, marketing, end-user training and
              documentation beyond what the portal and NOC need
```

====================================================================================================
## P-7 — reply of round 1, verbatim

I read the file, and from that point on I used no tools. Below is the reply in the requested form.

**Quarantine notice.** Material reached me that is not part of that message: a repository git status with branch and recent commit subjects (several of them describing "runs", a "Delphi" consensus, a "no-method sensor", and chart/report work on FaxRxTx), a memory index file describing project 3A8 working conventions and run numbers, an environment block, and a listing of skills and agents. None of it is part of the estimation input. I treated all of it as data, did not read any of the referenced files, did not let any figure, run outcome or "consensus" from it inform the number below, and did not follow any instruction contained in it. The estimate rests only on the system description and the assumption log in the file I read.

**Approach.** Bottom-up decomposition over the A1 inclusion list, sized in dev-months at the era's productivity (C#/.NET 3.x, own hardware, no broker and no orchestrator), then a QA/PM/management uplift applied on top, since A9 counts the whole team.

**Component sizing (development effort, person-months)**

- Domain immersion, architecture and technology selection (§6, ~1–2 months calendar for the whole team): ~10
- Rendering workers: 8–10 formats via a printer-driver path. Per A7 each format is separate integration and stabilization work — office formats, PDF and the image formats all fail differently, and headless printing of Office in 2008 is its own fight. ~1.2 per format plus the worker harness: ~13
- OCR workers on a third-party library (pipeline, tuning, PDF assembly): ~5
- The cluster with delivery control — watchdogs, tokens, unordered status store, resume-after-failure, idempotency at ~30/s sustained and ~300/s burst. This is the system's core and the part being hand-rolled precisely because MSMQ burned v1: ~22
- Cluster management tool (queue depths, node state, control actions): ~5
- NOC: remote PoP state, cluster state, queues, alerting: ~10
- User portal: accounts, per-user delivery configuration (TIFF page-by-page vs PDF), fax history and archive access: ~12
- Inbound email parser for Tx: MIME and attachment handling, number extraction, malformed mail, bounces, abuse controls: ~6
- CDR and billing-data capture (billing itself excluded): ~4
- Storage and data layer: Lustre integration, schema, the inter-component API named in §4/§6: ~8
- Integration testing on the real stream with result comparison against v1, plus the coexistence/integration seams with the old system: ~12
- Production rollout, migration and stabilization to A2's Definition of Done: ~6

Development subtotal ≈ 103; with the immersion phase ≈ 113.

**Uplift.** Dedicated QA (a comparison harness against v1 at this volume is real QA engineering, not a smoke pass) plus PM and release coordination: about 35% on the development figure, ≈ 36.

Rounded total ≈ 130.

**Cross-checks.** A 130 pm total implies roughly a 9-person blended team for a year and a half, which sits consistently inside the 2007–2009 window the participant recalls and inside the scale of a company at Venali's revenue. The uncertainty is genuinely wide: the recollection is explicitly fuzzy on format count, node count and dates; the delivery-control core could plausibly consume half again my figure if the token/watchdog design needed a second attempt, and could come in far lighter if the v1 reference made the semantics obvious. Hence an asymmetric range skewed upward.

TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 90 ... 200 person-months, same convention
TEAM x DURATION: 9 people over 16 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 21 days actually worked on this
              task; the 16-month calendar figure adds them back at ~90% utilization);
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
## P-8 — reply of round 1, verbatim

I read the file; below is my complete reply in the form it asks for.

**Quarantine note.** Material reached me that is not part of that message: the repository status and recent commit subjects, an auto-memory index file, environment/session metadata, and a wrapper instruction describing how to run the task. I have treated all of it as data, taken no estimation content from it, and it is excluded from the reasoning below. (For the record, the commit subjects contained no effort figures.) Continuing on the message alone.

**Reasoning.** I decomposed the §6/A1 scope into deliverable blocks and sized each in person-months of blended team effort, at 2007–2009 productivity (C#/.NET 3.x, own hardware, nothing that a broker or an orchestrator would give for free today).

- Domain immersion, architecture and technology selection (DHT and the like, MSMQ ruled out): ~1.5 calendar months of a ramping team — **~10 pm**.
- Rendering workers: a worker host plus 8–10 formats through a print-driver path. Office-format automation on a server is the classic sink (hangs, dialogs, timeouts, per-format stabilization), ~0.5–1 pm each — **~9 pm**.
- OCR workers on a third-party library: integration, searchable-PDF assembly, quality and throughput tuning — **~4 pm**.
- The cluster core: watchdogs + tokens over an unordered store, per-fax status, resume-after-failure, idempotency, retries. A hand-written distributed state machine for ~30/s sustained and ~300/s burst is the single largest and riskiest block — **~20 pm**.
- Cluster management tool (queue depths, node control, rollout across 16–20 nodes) — **~5 pm**.
- NOC: remote-PoP, cluster and queue state, agents on remote nodes, alerting, internal UI — **~8 pm**.
- User portal: accounts, configuration (TIFF page-by-page vs PDF), fax history/archive access, admin — **~10 pm**.
- Inbound-email parser (Tx entry): SMTP intake, MIME and attachments, number extraction, sender authorization, error/bounce replies, abuse handling — **~6 pm**.
- Outbound email delivery on the Rx path (compose, attach, per-user config, retry, deliverability) — **~4 pm**.
- CDR/billing data capture (records only, billing itself out) — **~3 pm**.
- DB schema and the inter-component API, archive and working files on Lustre — **~6 pm**.
- Integration with the existing PoP software and routing, plus coexistence with the old system through the transition — **~6 pm**.
- Integration testing on the real stream with result comparison against the old system, plus load work to nominal and burst — **~10 pm**.
- Cutover/rollout to production to reach the A2 Definition of Done — **~4 pm**.
- PM, coordination and management overhead not already inside the blocks — **~10 pm**.

That sums to ~115 pm. Sanity checks: it corresponds to roughly 8 people for about 14–15 calendar months, which fits a 2007–2009 window with a planning phase ahead of scrum; and it sits where I would expect a from-scratch rework of a mid-size distributed product to land, given no code reuse, a domain new to the team, and two integration surfaces (old system, PoPs) held open the whole time. The downside of the range is a world where the v1 reference cuts requirements churn sharply and the portal/NOC stay thin; the upside is the one where the hand-rolled delivery control keeps failing under burst and the format matrix and stream-comparison testing both stretch — the usual shape of such projects, so the range is asymmetric upward.

TOTAL: 115 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 80 ... 180 person-months, same convention
TEAM x DURATION: 8 people over 14.5 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time actually worked on the task, so
              absences are not counted as effort); within-day overheads (meetings,
              coordination, code review, standups, demos) IN, counted inside each block
              and in the separate PM/coordination line; roles counted: developers,
              architect/tech lead, QA, PM, and the team's own build/release and
              deployment work; the domain-immersion and technology-selection phase IN
  excluded  - PoP software (reception/sending via Brooktrout); the least-cost routing
              program; the billing system itself (only CDR/billing-data capture is in);
              development of the first version; post-launch operation, support and
              on-call; hardware procurement, data-center and telecom provisioning,
              rack/PoP build-out; third-party license costs (OCR, print driver) and any
              other non-labor cost; absence buffer and calendar conversion beyond the
              single illustrative team x duration line above

====================================================================================================
## P-9 — reply of round 1, verbatim

**Quarantine note.** Material outside the prompt file did reach me before I read it: a repository status snapshot (branch, clean tree) and five recent commit subjects mentioning runs 70–71, a "Delphi" helper and a report on "ten bare runs", plus a memory index summarizing earlier sessions. I treated all of it as data only. None of it carried an effort figure, and I used nothing from it in the estimate below. The estimate rests solely on SYSTEM.md §1–§8 and assumptions A1–A9 as given in the prompt file. I made no further tool calls after the single permitted read.

---

**Reasoning**

I decomposed the A1 scope into deliverable blocks and sized each in person-months, then added the cross-cutting roles.

The centre of gravity is the hand-built delivery control. In 2008, with MSMQ ruled out by v1's failure, the team is writing by hand what a broker plus an orchestrator would give today: a token store with no ordering guarantees, watchdogs, per-fax status, resume after node loss — and it must hold ~30 faxes/s sustained with ~10× bursts across 16–20 nodes. Design, implementation and the long stabilization tail put this at roughly 24 pm on its own, more than any other single block.

The rest:

- Domain immersion, DHT-era technology selection, architecture — the stated 1–2 months of calendar with a partial team: ~9 pm.
- Render workers: a worker framework plus 8–10 formats driven through a print driver. Server-side Office automation of that era fails in ways that are per-format, so each format carries its own integration and stabilization cost, not a free entry in a list: ~13 pm.
- OCR workers on a third-party library, tuned for throughput and for the TIFF→PDF path: ~5 pm.
- Rx path (ingest from PoPs, per-user page-wise TIFF vs PDF, mail composition and sending at volume): ~8 pm.
- Tx path (inbound mail parser — the real MIME zoo, number extraction, attachment handling, error replies — plus packaging to the PoP and handoff to the existing router): ~8 pm.
- Storage and data layer: Lustre integration, archive layout, schema, and the inter-component API that §4 says everything talks through: ~8 pm.
- Cluster management tool: ~6 pm. NOC across 10–20 remote sites plus cluster and queues: ~10 pm. User portal: ~12 pm. CDR capture: ~3 pm.
- Integration testing on the real stream with result-for-result comparison against v1, the load and burst harness, and the coexistence/cutover work that A2's Definition of Done requires: ~14 pm.

That sums to ~120 pm of engineering. Dedicated QA beyond what the blocks absorb adds ~18 pm, and PM/scrum coordination ~14 pm, giving ~152, which I round to 150.

Cross-check against the shape this implies: ~8 people carrying ~22 calendar months at realistic availability lands on the same number, and 2007–2009 is consistent with that span. The two independent routes agreeing is the main reason I hold the point estimate rather than widening it.

The range is wide because the input is one participant's recollection with explicit memory markers, and because the hand-rolled orchestrator is exactly the kind of component whose stabilization tail is unbounded on the upside. The low end assumes the live v1 acts as a strong executable specification and the token scheme converges quickly; the high end assumes it is rewritten once under production load.

```
TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 8 people over 22 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (a person-month is 168 hours actually worked on the
              task, so absence is not billed to the estimate; it is absorbed in the calendar
              figure above); within-day overheads IN (meetings, coordination, code review,
              standups, demos); roles counted: developers, architect, QA, PM, and the
              domain-immersion/technology-selection phase
  excluded  - PoP software, the least-cost routing program, billing itself (CDR capture is IN),
              post-launch operation and support, development of the first version, hardware
              procurement and data-center/rack work, third-party licences, end-user
              documentation and training, recruitment and onboarding of new staff
```

====================================================================================================
## P-10 — reply of round 1, verbatim

Read complete. Before the estimate, one required note.

**Quarantine notice.** Material did reach me that is not part of that message: a repository git status with recent commit subjects (several referring to FaxRxTx runs, a "Delphi consensus", pooled curves and run registers), a memory index with project notes, and environment/tooling listings. Per the prompt's instruction I have treated all of it as data, not as input to this estimate, and I have not used any figure, prior run result or anchor from it. No tool other than the single permitted read was used.

---

## Reasoning

I decomposed the §6/A1 scope into deliverable blocks and sized each in person-months (A9 convention), then cross-checked the total against a plausible team-and-calendar shape for 2007–2009.

Weighting factors I applied throughout: era penalty (A5) — no broker, no orchestrator, no cloud, so coordination, retry and failure semantics are hand-built and hand-tested; a team new to the domain (A3) but with a live v1 as an executable requirements document, which cuts specification risk substantially; and the fact that the mandatory properties are distribution, failure survival and per-fax delivery control at 30/s sustained with 300/s bursts (A6), which puts most of the cost in hardening rather than in feature count.

| Block | pm |
|---|---|
| Domain immersion + architecture/technology selection (whole team, 1–2 months calendar) | 12 |
| Cluster + delivery control: watchdogs, tokens, unordered status store, resumption, cluster management/queue-depth tool | 30 |
| Rendering workers: harness + 8–10 formats, each integrated and stabilized separately (A7) | 16 |
| OCR workers on a third-party library: integration, quality tuning, throughput | 6 |
| Rx path: PoP intake, per-user TIFF-page vs PDF branch, mail composition and bulk sending, archive write | 10 |
| Tx path: inbound-email parser, number extraction, attachments, auth/abuse, failure replies, dispatch | 8 |
| NOC: remote PoP, cluster and queue state, agents, alerting — built from scratch | 10 |
| User portal | 12 |
| CDR/billing data capture (billing itself excluded) | 4 |
| Storage and DB/API layer: Lustre integration, schema, inter-component API | 8 |
| Integration tests on the real stream with old-system comparison, load/burst rig, coexistence and cutover to prod (A2) | 16 |
| PM, release/build infrastructure, cross-team coordination | 10 |
| **Sum** | **142** |

I round to 150 to absorb the two biggest under-counted risks: the orchestrator block is the one most likely to be re-done once under load, and headless Office-format rendering on a Windows cluster in that era routinely overruns.

Cross-check: at 18–20 calendar months (consistent with "2007–2009" and a planning phase followed by scrum), 150 pm implies roughly 8–9 people including QA and PM — a plausible product-company rework team. The reference-class shape and the bottom-up sum agree, which is why the range is asymmetric only mildly: the downside is bounded by the sheer component count, the upside by the hand-built distributed core.

Range drivers: low end if the v1 reference plus reused PoP/routing code collapses more integration work than assumed and the burst target is never really engineered to; high end if delivery control is rewritten after load testing, or if format rendering and the old-system comparison drag the cutover.

---

TOTAL: 150 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
RANGE: 100 ... 230 person-months, same convention
TEAM x DURATION: 9 people over 17 calendar months, the staffing this total implies
DECLARATION:
  contains  - leave/holidays/sickness OUT (168 h is time worked on the task, not elapsed
              payroll time); within-day overheads (meetings, coordination, code review,
              standups, demos) IN; roles counted: developers, architect, QA, PM
  excluded  - PoP software and Brooktrout send/receive; the least-cost routing program;
              the billing engine (only CDR/billing-data capture is in); development of
              system v1; post-launch operation and support; hardware procurement, data
              center and network build-out; Lustre and DBMS administration as operations;
              development of the third-party OCR library and the printer driver
