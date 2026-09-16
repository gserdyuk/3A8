Perform Steps B and D for the case below: reconcile the declarations, diagnose the divergence between the bottom-up reading and the two outside-view readings, apply the supplied Step C corrections mechanically, and report the final answer in three parts. Everything you need is in this message; read no files.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Your engine definition's output format, sections 1–7. **State the final answer in net hours of work on the task** (the bottom-up's unit, INPUT 3b), and give, beside it, whatever conversion you apply to put the outside view in that unit, with its source. The orchestrator will convert to staffed person-months afterwards by the pinned convention in INPUT 3b; do not do that conversion for the final answer yourself.

---

# INPUT 1 — the project description (`SYSTEM.md`, with the struck lines marked in place)

# FaxRxTx (Venali) — system and task description

**Source:** the recollections of a project participant, recorded 2026-07-17 from their
account. A real commercial project (the company Venali, a data center in Miami).
Markers of uncertainty ("it seems," "I think," "I don't remember") are kept deliberately —
they are part of the input data, not editorial defects.

**Document status:** a fixed input for the 3A8 pipeline (the analog of
BMS_extracted.md in the BMS example). The estimate must rely only on this
document + the assumption log, with no access to the actual outcome.

---

## 1. What the system does

A worldwide fax send-and-receive service: at least Europe and the USA
(possibly Australia too — the participant does not remember exactly). The user receives
incoming faxes by email and sends outgoing faxes by emailing a special address.

## 2. Fax reception (Rx)

1. Geographically distributed points of presence (PoP) are placed at
   telecom providers: they worked with BT and with others too.
   Rack space is rented at the provider, a computer with **Brooktrout**
   boards is installed to receive faxes.
2. Received faxes, as TIFF files, are sent to the company's own data center
   in Miami.
3. In the data center, depending on the user's configuration, the fax is either
   attached to the email page by page (TIFF) or converted to PDF
   and attached to the email. Conversion to PDF included digitization (OCR) —
   this was handled by OCR workers.
4. The email is sent to the user. Conversion and sending are handled by
   **workers**.

## 3. Fax transmission (Tx)

1. The user sends an email to a specific address. The email is parsed,
   the recipient's fax number is extracted from it.
2. The document from the attachment is rendered to TIFF (via, it seems, the **Black Ice**
   printer driver) and sent as an archive to a point of presence, where it
   goes into the PSTN through the Brooktrout boards.
3. A **routing** program (least-cost routing) works: it decides which
   point of presence to send the TIFF files to, so that delivery is cheaper.
4. **Renderers** — for the main document formats: DOC, XLS, PPT, PDF,
   TXT, GIF, TIFF (the list is from memory; the participant may have forgotten
   something; on the order of 8–10 formats in all).

## 4. Infrastructure and key technical decisions

- **Its own cluster of Windows 7 computers** — for rendering and other
  tasks.
- **A cluster management tool** — queue lengths and so on.
- **A job queue (MQ) was not used**: using MSMQ in the previous version of the
  system broke everything. Instead — a home-grown system of
  **watchdogs and tokens** (an unordered store) that kept the status
  of each fax and resumed work if something went wrong. Essentially — an
  orchestrator of a large number of faxes.
- **Storage:** the **Lustre** file system (from HP, it seems) — it stored both the
  fax archive and the working files. There was also a database (the DBMS is not
  specified) — the components communicated through the DB and an API.
- **Development language:** C#.
- **NOC** — an internal control center: the state of the remote nodes (PoP),
  the cluster, and the queues (where there were any).
- **User portal** — the users' website.

## 5. Scale

- The nominal target volume — **~1,000,000 faxes per 10-hour day**
  (~30/s on average). The figure 10,000,000/day (~300/s) is a **burst estimate**,
  the peak mode ~10× the nominal. Actual traffic was even below the
  nominal (the participant's clarification, 2026-07-17).
- Points of presence (PoP): **10–20**.
- Nodes in the render cluster: **~16–20** (from memory: "probably 20," "maybe 16"),
  joined by a private network.

## 6. The team's scope (the object of the estimate)

Context: by the start of the work **a working first version of the system already
existed**. The task was to redo what management did not like in the
original version. The team, meanwhile, **did not know the domain**: about
a month (possibly two) went into discussions, immersion in the subject
area, and technology selection (they studied DHT and other mechanisms).
There was no code reuse ("no reference base classes") —
only integration with the old system and coexistence for the duration
of the transition.

**What the team did (included in the estimate):**

- the stage of domain immersion and architecture/technology selection
  (they considered DHT and the like) — about 1–2 months;
- the printing (rendering) and OCR workers — OCR on a third-party library;
- the cluster itself with the delivery-control mechanism (watchdogs + tokens, §4);
- the NOC;
- the user portal;
- the inbound-email parser (the Tx path);
- saving CDR and billing data (billing itself is out of scope);
- integration tests on the real message stream with comparison of the
  results to the "old system."

**What the team did not do (out of the estimate):**

- the software on the PoPs (reception/sending via Brooktrout) — already existed;
- the routing program (least-cost) — was ready, reused;
- billing — was separate.

The components communicated through the database and an API.

**Process:** "scrum after waterfall" — first a planning phase, then
scrum. There was no hard deadline, but there was pressure. The team included
QA/PM, not just developers. [struck by the orchestrator: the calendar period of the work]

## 7. Public context (open sources, 2026-07-17)

- Venali, Inc. — Miami, hosted enterprise internet fax for Fortune 1000
  (healthcare, retail, finance/insurance).
- [struck by the orchestrator: the company's later acquisition, its price and revenue, and a dating inference for the development period]

## 8. The estimation task

Estimate the **effort in person-months** for the scope from §6 — blind,
from this document and the assumption log only.

[struck by the orchestrator: a note on where the outcome is kept]

---

[struck by the orchestrator: a closing note about an unrelated draft document]

---

# INPUT 2 — the assumption log (`assumptions.md`), verbatim

# FaxRxTx — Assumption Log (fixed before the runs, 2026-07-17)

Assumptions that close the gaps in SYSTEM.md. Agreed before estimation begins; all
runs (decomposition, reference class, …) must use the same assumptions — otherwise
their ranges are not comparable. Run input: SYSTEM.md + this file. FACT.md is not
passed into the runs.

## A1. Estimation scope
The full cycle for the "the team did" list from SYSTEM.md §6: the phase of domain
immersion and architecture/technology selection (~1–2 months) + design + development +
testing + rollout to production of the new version of the core functionality replacing
the first version.
- Included: rendering and OCR workers, the cluster with the delivery-control
  mechanism (watchdogs + tokens), NOC, the user portal, the inbound-email parser,
  saving CDR/billing data, integration tests on the real stream with comparison to the
  old system.
- **Not included:** the PoP software, the routing program, billing, post-launch
  operation, development of the first version of the system.

## A2. Definition of Done
The new system takes production traffic in prod; the integration tests on the real
stream have passed, the results agree with the old system; the old version can be
decommissioned.

## A3. Team and starting conditions
The team **did not know the domain** — immersion in the subject area, discussions,
and technology selection took ~1–2 months (included in A1). Mitigating factor: a
working v1 exists as a live reference of requirements ("like v1, but fix what we don't
like") — there is no full-scale requirements gathering from scratch, but the domain
(fax protocols, telecom, distributed delivery) is new to the team. Blended composition,
including QA and PM. The team's headcount is **not** part of the assumptions
(the volume of work is estimated, not the calendar).

## A4. Reuse
No first-version code in the new one ("no reference base classes"). Reused: the
ready PoP software, the ready routing, a third-party OCR library, rendering via a
printer driver (Black Ice-class), the existing storage infrastructure (Lustre) and the
DB as technologies — we do not develop these, only integrate with them.

## A5. Technological era
2007–2009: C#/.NET ~3.x, a Windows cluster on our own hardware, no clouds and no
ready orchestrators (what a message broker/Kubernetes would give today is written by
hand — watchdogs, tokens, delivery control). MSMQ deliberately excluded from the
negative experience of v1.

## A6. Target scale
The engineering target — **~1 million faxes / 10-hour day (~30/s on average)**,
with bursts up to ~10× (**~300/s**, "10 million/day" — an estimate of the peak mode).
A cluster of ~16–20 nodes, 10–20 PoPs. The estimate is made for designing to the
nominal with burst resilience: distribution, surviving failures, and delivery control
of every fax are mandatory properties, not options.

## A7. Rendering formats
8–10 input formats (DOC, XLS, PPT, PDF, TXT, GIF, TIFF + possibly 1–3 forgotten
ones). Each format is a separate piece of integration and stabilization work, not a
"free" extension of the list.

## A8. Organizational context
A product company (Venali), an internal rework by management decision. There is no
hard deadline, but there is pressure. The process — a planning phase, then scrum.
Approvals are internal, faster than the enterprise client of the BMS example.
Accounted for in reference class (decomposition, by construction, does not see it).

## A9. Units
Estimation in **person-months** (1 pm ≈ 21 pd ≈ 168 hours), the total effort of the
whole team, including QA/PM and the architecture-selection phase. Conversion to a
calendar duration is a separate step, not part of the runs.

---

# INPUT 3a — the case profile, pinned before any number (§1–§4; the rest of the form concerns the outcome and is withheld)

### 1. Team

| field | value |
|---|---|
| grade mix | **unknown.** SYSTEM §6 / A3: a blended team including QA and PM, not only developers. No grade is stated |
| domain experience | **first system in this domain.** A3: the domain (fax protocols, telecom, distributed delivery) was new; ~1–2 months of immersion and technology selection. Mitigation: a working v1 is a live reference of requirements |
| presence fraction actually experienced | **unknown** |

### 2. Overheads

| field | value |
|---|---|
| net task hours a present day delivers | **unknown → the default 6** (`docs/constants.md` §4a) |
| what a booked day contains | **unknown.** Process is scrum after a planning phase (A8), so scrum ceremonies are inside the booked day |
| leave, holidays, sickness factor | **unknown → the default ×1.10** |
| what is booked to the project and what elsewhere | **unknown.** Out of scope by A1: PoP software, routing, billing, post-launch operation, v1 development |

### 3. Process

| field | value |
|---|---|
| stages actually run | a planning / immersion phase (F48, ~1–2 months calendar), then scrum development; integration tests on the real message stream compared with the old system (F49, F50); rollout to production (F51); the old version decommissionable (F52). No client acceptance stage — an internal rework in a product company (A8) |
| cycle counts and environment count | from `technology_declaration.md` §2: environments dev, stage, prod (3, a scope decision); test execution cycles 2 (policy); UAT cycles 0 |
| visible scope decisions | `C-DIRECT` vs `C-UAT` · `E-DSP` vs `E-SINGLE` · `G-SEED` vs `G-MIGRATE` · `U-OPS-USER` vs `U-NONE` (`technology_declaration.md` §1, §5); `SA-NONE` vs `SA-PENTEST` recorded as a sensitivity |
| organisation | product company (Venali, Miami), internal rework by management decision, no hard deadline but pressure; internal approvals (A8) |
| era | 2007–2009, C#/.NET ~3.x, own Windows cluster, no cloud, no ready orchestrator, no message queue (A5). The rate table is modern; the era transfer is not pre-adjusted (`technology_declaration.md` §4(i)) |

### 4. Staffing of every separately-priced stage

| stage | headcount | duration share, if known |
|---|---|---|
| F48 — domain immersion and architecture/technology selection | **unknown.** SYSTEM §6 says the team went through it; A3 removes headcount from the assumptions deliberately. Any row that scales with headcount must refuse to price until it is declared | calendar ~1–2 months (SYSTEM §6, A1) |
| F49 / F50 — parallel-stream integration testing and comparison | **unknown** | unknown |
| F51 / F52 — cutover and decommissioning | **unknown** | unknown |

# INPUT 3b — the pinned unit and presence convention of this instrument (`docs/instrument.md` §0, verbatim)

## 0. The unit

> **Effort is working time spent solving the task, stated in person-hours.** One person-day, where
> one is used for readability, is 8 such hours; a week is 40.
>
> **Leave, public holidays, sickness, bench time and non-project duties are not included, and are
> not parameters of this method.** Neither is the effective yield of an assigned working day, nor
> working days per month. How an organisation behaves is a true and important fact about that
> organisation and not a fact about the work.
>
> **If you need days of presence, convert by the pinned convention** (`docs/constants.md` §4a,
> author's ruling 2026-08-27): **6 net task hours per present day, ×1.10 for leave, 21 days a month**
> — so 1 staffed person-month ≈ 114.5 net task hours. A case whose organisation is known to differ
> states its own value in its case profile *before* any estimate exists; absent that, this is it.
> The conversion lives in the comparison layer and in no rate row.

---

# INPUT 4 — the bottom-up reading (runs 61–64, `Hotyn` chain × Claude Opus 5)

**Declaration.** Unit: **net hours of work on the task** (INPUT 3b). Losses (leave, holidays, sickness): **outside**. Within-day overhead: outside, except the activity rows that name it (planning and tracking per subsystem, status reporting, risk management, mobilisation). Roles: the delivery team's hours on each activity (design, build, test, review, requirement elaboration, planning, documentation, environments). Source of every value: rate table v0.1-h — external industry norms, one sample, **uncalibrated against any outcome**, modern (no era adjustment). Scope: the pinned technology declaration — bespoke construction · test-based assurance, 2 test cycles · direct to production, no acceptance stage · one team · dev/stage/prod · seeded data, **no legacy migration** · operational and user documentation · **no security/compliance assurance**.

**Chain.** Product model `HM61-1` (`Hotyn-M 2.1`; the second repeat `HM61-2` built 91 elements / 75 leaves against 84 / 68, leaf ratio ×1.10; accreted coverage-set Jaccard 0.51; `HM61-1` was closed because it was the repeat that closed without a defect report) → work model (`Hotyn-W 1.2`, 521 element-attached items, 4 batches) → size classes (`Hotyn-D 2.0`, two repeats per batch, 95.6% class agreement) → assembly script (E = (O+4M+P)/6; integration C3 = 20% of the leaf effort beneath every parent incl. the root) → demanded-work addendum (`Hotyn-K 1.1`, gap-blind).

**Readings.**

| sizing repeat | assembly (product + once layer) | demanded-work addendum | **raw chain total** | sd at ρ = 0.5 (convention, not measured) |
|---|---:|---:|---:|---:|
| 1 | 10094 | 100 | **10194** | 1672 |
| 2 | 9746 | 100 | **9846** | 1625 |

Repeat band 9846–10194 (×1.035), centre 10020 net task hours.

The assembly's own printout (both repeats, named holes, composition by subtree):

```
=== assembly: FaxRxTx · model HM61-1 (84 elements, 68 leaves, 16 parents) · crossing run 62 · sizing run 63 · 2 repeats
=== declared: K-BESPOKE, A-TB, C-DIRECT, D-TEAM, E-DSP, G-SEED, U-OPS-USER, SA-NONE · environments ['dev', 'stage', 'prod'] · test cycles 2 · UAT cycles 0 · migration rehearsals 0 · model bracket M
=== repeat 1: sized 64 · distribution {'S': 33, 'M': 26, 'L': 4, 'XL': 1} · unsizeable ['L27', 'L38', 'L51', 'L56']
  element leaf E (incl. root per-parent items): 6576.7 h
  C3 all parents:                               3143.9 h   of which root C3: 1315.3
  once + per-environment layer [M]:            373.0 h  (16 items)
  GRAND TOTAL:                                  10094 net person-hours  (= 1261.7 pd at 8 h)
  corridor, rho = 0.5:  sd 1648 h · P10 7982 · P90 12206  (x0.79 / x1.21 of the centre)
  XL leaves 1, own effort 189.0 h: L15
  named holes (27):
      ('L27', 'K1', 'unsizeable (M10)')
      ('L27', 'K2', 'unsizeable (M10)')
      ('L27', 'A2', 'unsizeable (M10)')
      ('L27', 'A3', 'unsizeable (M10)')
      ('L27', 'A4', 'unsizeable (M10)')
      ('L32', 'G1', 'special count unsizeable')
      ('L32', 'G2', 'special count unsizeable')
      ('L32', 'G3', 'special count unsizeable')
      ('L38', 'K1', 'unsizeable (M10)')
      ('L51', 'K1', 'unsizeable (M10)')
      ('L38', 'K2', 'unsizeable (M10)')
      ('L51', 'K2', 'unsizeable (M10)')
      ('L38', 'A2', 'unsizeable (M10)')
      ('L51', 'A2', 'unsizeable (M10)')
      ('L38', 'A3', 'unsizeable (M10)')
      ('L51', 'A3', 'unsizeable (M10)')
      ('L38', 'A4', 'unsizeable (M10)')
      ('L51', 'A4', 'unsizeable (M10)')
      ('L51', 'A10', 'unsizeable (M10)')
      ('L38', 'G1', 'special count unsizeable')
      ('L38', 'G2', 'special count unsizeable')
      ('L38', 'G3', 'special count unsizeable')
      ('L56', 'K1', 'unsizeable (M10)')
      ('L56', 'K2', 'unsizeable (M10)')
      ('L56', 'A2', 'unsizeable (M10)')
      ('L56', 'A3', 'unsizeable (M10)')
      ('L56', 'A4', 'unsizeable (M10)')
=== repeat 2: sized 63 · distribution {'S': 34, 'M': 25, 'L': 4, 'XL': 0} · unsizeable ['L27', 'L38', 'L46', 'L51', 'L56']
  element leaf E (incl. root per-parent items): 6350.5 h
  C3 all parents:                               3023.0 h   of which root C3: 1270.1
  once + per-environment layer [M]:            373.0 h  (16 items)
  GRAND TOTAL:                                  9747 net person-hours  (= 1218.3 pd at 8 h)
  corridor, rho = 0.5:  sd 1601 h · P10 7695 · P90 11798  (x0.79 / x1.21 of the centre)
  XL leaves 0, own effort 0.0 h: 
  named holes (31):
      ('L27', 'K1', 'unsizeable (M10)')
      ('L27', 'K2', 'unsizeable (M10)')
      ('L27', 'A2', 'unsizeable (M10)')
      ('L27', 'A3', 'unsizeable (M10)')
      ('L27', 'A4', 'unsizeable (M10)')
      ('L32', 'G1', 'special count unsizeable')
      ('L32', 'G2', 'special count unsizeable')
      ('L32', 'G3', 'special count unsizeable')
      ('L38', 'K1', 'unsizeable (M10)')
      ('L51', 'K1', 'unsizeable (M10)')
      ('L38', 'K2', 'unsizeable (M10)')
      ('L51', 'K2', 'unsizeable (M10)')
      ('L46', 'K3', 'unsizeable (M10)')
      ('L38', 'A2', 'unsizeable (M10)')
      ('L51', 'A2', 'unsizeable (M10)')
      ('L38', 'A3', 'unsizeable (M10)')
      ('L51', 'A3', 'unsizeable (M10)')
      ('L38', 'A4', 'unsizeable (M10)')
      ('L51', 'A4', 'unsizeable (M10)')
      ('L51', 'A10', 'unsizeable (M10)')
      ('L38', 'G1', 'special count unsizeable')
      ('D03', 'G1', 'special count unsizeable')
      ('L38', 'G2', 'special count unsizeable')
      ('D03', 'G2', 'special count unsizeable')
      ('L38', 'G3', 'special count unsizeable')
      ('D03', 'G3', 'special count unsizeable')
      ('L56', 'K1', 'unsizeable (M10)')
      ('L56', 'K2', 'unsizeable (M10)')
      ('L56', 'A2', 'unsizeable (M10)')
      ('L56', 'A3', 'unsizeable (M10)')
      ('L56', 'A4', 'unsizeable (M10)')
=== composition, repeat 1 - per top-level subtree: element items + C3 inside the subtree
   N10    Inbound fax path                         elements  15  items   1402 h  C3    477 h  subtotal   1878 h
   N20    Outbound fax path                        elements  25  items   2020 h  C3    741 h  subtotal   2761 h
   N30    Job orchestration                        elements   5  items    424 h  C3     85 h  subtotal    508 h
   N40    Processing cluster                       elements   8  items    659 h  C3    204 h  subtotal    862 h
   N50    Storage and records                      elements   9  items    435 h  C3     87 h  subtotal    522 h
   N60    NOC                                      elements   5  items    346 h  C3     69 h  subtotal    416 h
   N70    User portal                              elements   5  items    319 h  C3     64 h  subtotal    382 h
   N80    Old system coexistence                   elements   4  items    176 h  C3     35 h  subtotal    211 h
   N90    System-wide properties                   elements   5  items    337 h  C3     67 h  subtotal    404 h
   L39    Inter-component API                      elements   1  items     65 h  C3      0 h  subtotal     65 h
   L56    First-version core function set, as repl elements   1  items      4 h  C3      0 h  subtotal      4 h
   root own per-parent items 391 h · root C3 1315 h · once/per-env 373 h
```

**Demanded-work addendum (`Hotyn-K 1.1`, verbatim below):** W-F49 (one pass of integration tests on live traffic) and W-F52 (establishing the old version can be decommissioned) priced; **W-F48 (domain immersion and architecture/technology selection) and W-F50 (comparison with the old system until outputs agree) refused** — headcount and parallel-run period undeclared.

<details><summary>HK64-1, verbatim</summary>

# Hotyn-K 1.1: Rate table addendum, whole-model once-only rows W-F48, W-F49, W-F50, W-F52

## 1. Contamination check

My context included repository information I wasn't given as input: a git status naming an untracked run file, recent commit subjects mentioning a test report, and a memory index mentioning run directories. I set it aside and did not use it. None of it carried a figure I could have used. The pasted input (Inputs 1–3) contains no effort figure, total, budget or duration, so it is clean and I proceeded. I read no files.

## 2. Declaration

1. **Unit.** Values are in **hours of work on the task (net hours)**. A recorded, assigned working day is **not** the unit: meetings, general coordination and interruptions are not inside. My base rates are natively in **engineer-days**, so each row shows both, converted at **1 engineer-day = 8 net hours**. The hours column is the one to sum with the table these rows join.
2. **Losses.** Annual leave, public holidays and sickness are **outside** the values. The base rates are of the form "this takes about N engineer-days", and that form never contains them.
3. **Roles.** A value is the **total hours of the delivery team** on the activity, however many people do it, including peer review of that activity's own work products. It excludes:
   - client-side staff;
   - production operations staff acting for the client;
   - project management above the task.
4. **Source conventions and the disagreement between them.**
   - All rows below come from one family: practitioner rules of thumb for enterprise delivery, stated in engineer-days.
   - That family is loose about what a day is. Some sources mean a net task day of about 8 h. Others mean an assigned day, which holds about 5.5–6.5 net hours.
   - I read them as net days and converted at 8 h. If a source really meant assigned days, my hours are **overstated by a factor of about 1.23–1.45** (8/6.5 to 8/5.5).
   - I did not adjust for this. It is a known, sized inconsistency, and resolving it is calibration work.

## 3. Rows — single-size, scope `once`, no element class

| row id | activity | kind (staffing rule) | O pd | M pd | P pd | **O h** | **M h** | **P h** | basis | stamp |
|---|---|---|---|---|---|---|---|---|---|---|
| W-F48 | domain immersion and architecture/technology selection | **scales with headcount and period** | — | — | — | — | — | — | **refused**, see F-1 | — |
| W-F49 | integration tests on the real message stream | **does not scale with either** (bounded scope defined below) | 3 | 7 | 16 | **24** | **56** | **128** | Setting up and running a shadow or mirrored-traffic test against live enterprise message traffic typically takes one to two engineer-weeks. That covers: arranging the traffic tap or replay, clearance to handle production data, isolating the system under test so it causes no outbound side effects, one run of the integration suite, and sorting the failures. It runs long when data-protection approval or side-effect suppression is hard. | external norm, uncalibrated v0.1 |
| W-F50 | comparison with the old system until outputs agree | **scales with the parallel-run period**, and honest M > 10 pd | — | — | — | — | — | — | **refused**, see F-2 | — |
| W-F52 | establishing the old version can be decommissioned | **does not scale with either** (waiting out the parallel period is calendar time, not effort) | 2 | 4 | 10 | **16** | **32** | **80** | Retiring one enterprise application usually takes a few engineer-days when its interfaces are known. The work is: list who consumes it and what depends on it, confirm nothing is still owed on it, arrange archiving or retention of its data, get sign-off, remove the routing, and switch it off. It runs long when hidden consumers or retention duties surface. | external norm, uncalibrated v0.1 |

**What W-F49 covers:** setting up the live-stream test and running it once, then sorting the failures. It does **not** cover:
- a sustained soak window (that part scales with the period; see F-3);
- fixing the defects found (that belongs to the development activities).

**What W-F52 covers:** the establishing work and the switch-off. It does **not** cover:
- the production cutover (already priced by a catalogue activity);
- migrating data off the predecessor, if the client requires it (that is a separate activity the catalogue would have to hold);
- the waiting period itself.

## 4. Findings

- **F-1: W-F48 refused, missing parameters.** The effort equals headcount × stage length. As worded, the activity is time-boxed, not bounded by what it produces. Both parameters (the stage's **headcount** and its **calendar duration**) are undeclared, and I will not guess them.
  - *Catalogue objection:* nothing in the delivered system shows this activity is finished, so no size driver can exist for it.
  - *Suggested fix:* restate it as work bounded by its outputs, e.g. "evaluate one candidate technology" (per candidate) plus "write one architecture decision record" (per decision). Those could be priced.
- **F-2: W-F50 refused, for two separate reasons.**
  - (a) "Until they agree" over a parallel run means the monitoring and sorting effort grows with the **length of the parallel-run period**, which is undeclared.
  - (b) Even ignoring the period, the honest M is **above 10 pd**. The work includes: building a comparator keyed on message identity, normalising legitimate differences (ids, timestamps, ordering), and deciding each class of discrepancy on both systems. Some of those decisions will involve defects in the old system, which need a ruling from the client. Across a normal number of discrepancy classes, that exceeds two engineer-weeks.
  - *Needs a split in the catalogue:*
    - "build the output comparator" (once, bounded);
    - "decide one class of discrepancy" (per class, with the class count as the driver);
    - "monitor the parallel run" (per week of the period, with headcount and period declared).
- **F-3: W-F49 has a hidden period dependency.** If the client means a soak window (live tests left running for some weeks) rather than one pass, that part scales with the period and is not in the row. The client's wording needs clarifying. If a soak is meant, it needs its own per-period row with the period declared.
- **F-4: W-F49 may double-count.** Integration effort already covered by the integration rate (C3, 20%), or by a catalogue integration-test activity, may overlap this row. The row prices only what running against live traffic adds on top of that. Whoever applies C3 must decide whether C3 also applies to these once-only rows. I don't make that call.
- **F-5: W-F52 driver weakness.** The effort depends on how many interfaces and consumers the old system has and what data-retention duties it carries. Nothing in the work model counts either, which is why P is 2.5× M. The row can be priced, but the catalogue could add a count of the old system's consumers as a driver.
- **Flags for M < 0.25 pd (2 h):** none.

## 5. Notes on use

- **Unit:** sum only the **hours** columns. They are net task hours, with losses outside and delivery-team roles only. The pd columns are there only to show the conversion (×8). If the table this addendum joins turns out to use assigned days anywhere, the two may not be summed without a declared conversion.
- **Team grade assumed:** competent engineers, senior/middle mix, enterprise delivery.
- **Provenance:** every priced row is stamped `external norm, uncalibrated v0.1`. No value comes from any run, estimate, total, budget or duration, and none refers to any project.
- **Calibration:** a separate job for someone else. It must never edit a row while looking at a gap that the edit would explain.
- **Refused rows:** W-F48 and W-F50 stay unpriced until the catalogue splits them or the case profile declares headcount and period. They should not be filled with placeholder values.

</details>

**The bottom-up's static blind-spot list** (`docs/instrument.md` §4, verbatim):

## 4. What the chain does not have

- **A measured corridor.** The bell the report draws for the bottom-up is built on an assumed
  correlation between items of **ρ = 0.5** — every rate cell's O/M/P summed as equicorrelated
  items, P10–P90 of ×1.54 (session 2026-08-26). The assumption may be true or not: the
  correlation between items has not been measured. The value was chosen because the bell's width
  changes slowly across ρ = 0.25–0.75 (edges move about ±20% over that threefold range), so the
  middle of that range was taken [a clause struck by the orchestrator]. Outside the range
  the width does move: ρ = 0 gives ×1.04, ρ = 1 gives ×1.87. `ΣO…ΣP` (×4.19) is six sigma of
  the same sum, not a percentile band. Consequence: the corridor test of the exit criterion is
  scored against an assumed ρ, not a measured one.
- **A calibrated table.** The rates are external norms, fixed as constants by decision, calibrated
  against no outcome yet.
- **A brake on over-counting.** The design only adds — accretion and completion add, the crossing
  multiplies, splitting inflates, the floor rounds up, nothing may be removed — and the instrument
  that would check the other direction (the reverse audit) is designed and has never been run.
- **Knowledge of the team.** Team capability spans ×2–3 between grade bands; the table declares the
  grade it assumes and nothing downstream reads it.

---

# INPUT 5 — the outside view, two independent launches of `Lytin-R 1.1` × Claude Opus 5 (run 65), verbatim

Both received INPUT 1 and INPUT 2 and nothing else. Do not average them; each declared its own unit.

## RC65-1

# Lytin-R 1.1: outside-view effort forecast for FaxRxTx (Venali)

**Engine:** `Lytin-R 1.1`

**Contamination check.**
- **Anchors in the input:** none. The input holds no work breakdown, no bottom-up estimate, no target, budget or deadline.
- **Scope list in §6 and A1:** this is a list of what is in and out of scope. It has no prices, so I treat it as a boundary, not a breakdown. I did not use it to price anything.
- **The "~1–2 months" immersion phase:** this is a phase length stated in the input. I did not use it to size the project.
- **Struck lines:** the orchestrator's struck lines (the calendar period, the acquisition data, where the outcome is kept) were not visible to me.
- **Ambient repository information:** the harness prepended a git status, recent commit subjects, a memory index and file names. Some of them name this case. All of it was present and I quarantined it: I did not use it, and I read no files. I worked from the two pasted inputs only.

---

## 1. The declaration

**1. Unit.** One unit is one **person-month of recorded, assigned working time**.
- 1 pm = 21 working days of about 8 attended hours = **168 hours**.
- Those hours include meetings, review, coordination, context switching and waiting. They are not hours of hands-on work on the task.
- Hands-on task time is typically 60–70% of recorded time in this class, so 1 pm ≈ 100–120 hours on the task itself.
- This is my own choice for this class. It happens to match A9. I did not adopt it because A9 uses it.

**2. Losses.** Annual leave, public holidays and sickness are **outside** my figures.
- A headcount-month on the calendar (one person on the team for one calendar month) includes about 10–15% losses: about 10% for a US-staffed team, about 15% for a European one.
- Recorded pm = calendar headcount-months × about 0.87. In the other direction: headcount-months = recorded pm ÷ 0.87, so a 12-month × 10-person team (120 headcount-months) is about 104 recorded pm.

**3. Roles.** Every role on the project team is counted:
- developers, architects, QA and test, PM / scrum master, the team's own build and release work;
- the domain-immersion and architecture-selection phase.

These are **explicitly outside**:
- production operations staff after cutover;
- management above the project;
- business stakeholders' time beyond normal product-owner availability;
- hardware procurement and physical installation;
- work at the PoPs;
- vendor staff for the OCR, driver and Lustre products.

**4. My sources' conventions, and where they disagree.**

| Anchor family | Native convention | What I converted |
|---|---|---|
| ISBSG (development-team effort, "level 1") | Recorded hours; leave excluded; covers the life cycle from specification to implementation; inception is often under-recorded | Hours ÷ 168. Added about 5–10% for under-recorded early-phase work. |
| COCOMO II | PM = **152 h**; leave excluded; nominal coverage is Elaboration + Construction only | × 152/168 = 0.905. Added about 6% for Inception and about 12% for Transition (from the model's own phase table). |
| Practitioner team × duration | Calendar headcount-months; losses **inside**; all charged heads | × 0.87 |

- **Size of the convention inconsistency:** if left unconverted, the conventions alone would separate the families by up to about 30–40%. After conversion, maybe ±10% remains, because the phase coverage of each source is uncertain.
- **Level disagreement:** separately from conventions, the families disagree in level by about **1.7×** (see §4). That gap comes from the class-level size assumption, not from units, and I report it rather than absorb it.

**Scope boundary.**
- **Covered:** the A1 list, from domain immersion through a production cutover meeting the A2 Definition of Done.
- **Exclusions honoured:** the PoP software, the routing program, billing, post-launch operation, and development of v1.
- **Categories at the edge**, where a boundary recalled or inferred wrongly could be larger than the estimating error:
  - migrating live data (user accounts, configurations, the fax archive) from v1. This is not stated either way; I assume it is inside, as part of "the old version can be decommissioned".
  - installing and configuring the render cluster and Lustre, and administering the environment during development. I assume it is partly inside.
  - the length of the parallel run and a support period right after cutover. I assume the parallel run is inside, and support after decommissioning is outside.
  - a staging or test environment that replays the real message stream. I assume it is inside.

---

## 2. The reference class

**Definition.** An **in-house second-generation rewrite of a distributed, high-throughput transaction-processing back-end with reliability requirements**.
- It comes with an operator console and a customer web portal.
- It is cut over by running in parallel with a live predecessor.
- It is built by a mid-sized blended team (roughly 6–15 people) inside a product company.
- The era is the 2000s–early 2010s .NET/Java, on company-owned hardware with no managed cloud.
- **Stage of estimation:** equivalent to an RFP or initial concept, i.e. **before discovery**. The description is a high-level recollection with no requirements baseline. At this stage the early-estimate error is widest and most biased towards underestimation.

**Membership criteria (structural).** A class member contains all of these branches of work:
- (a) custom distributed coordination and reliability infrastructure, written by hand rather than bought;
- (b) stateless processing workers that transform documents or media;
- (c) an internal operations or monitoring console;
- (d) a customer-facing self-service web portal;
- (e) integration with a legacy predecessor, plus a parallel-run cutover;
- (f) a learning phase in a domain new to the team.

A class member **lacks** these branches:
- telecom or edge software;
- the routing or rating engine;
- billing;
- hardware design;
- mobile or desktop client apps.

**Why this project is in it.** A1, A4, A5 and A6 place it in all six branches (a)–(f) and outside the excluded branches.

**What it is not in:**
- **Not a greenfield line-of-business web application.** That class lacks branches (a) and (e) and is smaller.
- **Not a full platform or middleware product build.** That class carries general-purpose infrastructure as a deliverable and is larger.
- **Not an incremental refactor of an existing product.** A4 rules out code reuse.

---

## 3. Base rates and anchors

### Absolute anchors (effort for projects of this class)

| # | Anchor | Value (recorded pm, 168 h, losses outside) | Source | Confidence in the shape | Confidence in the number |
|---|---|---|---|---|---|
| A-1 | Team × duration for in-house rewrites of mid-scale transaction back-ends with portal and console: typically 6–12 people over 12–24 calendar months → 72–288 headcount-months | about **65–250**, middle about 140 | Practitioner consensus | High | Low–medium |
| A-2 | Class-typical functional size for this structure is about 1,000–2,500 function points (FP), at an ISBSG delivery rate for 3GL/.NET new development and re-development of about 10–15 h/FP (median about 12) | about **70–220**, middle about 110 (≈107 before the +5–10% early-phase correction) | ISBSG repository benchmarks (Development & Enhancement), practitioner reading of the published medians | Medium | Low (the size band is a class assumption, not a measurement) |
| A-3 | COCOMO II Post-Architecture at class-typical size of 40–120 KSLOC (C# including portal and console). Scale exponent about 1.10; effort multipliers about 0.7–0.85, because a capable team is offset by unfamiliar domain and platform. Converted to 168 h, plus about 18% for Inception and Transition | about **120–480**, middle about 190 | Boehm et al., *Software Cost Estimation with COCOMO II* (2000) | Medium | Low (very sensitive to the size assumption) |
| A-4 | Median effort of challenged or completed business-systems projects of 50–150 KSLOC in the 2000s | about **100–300** | QSM SLIM industry trend lines, as generally reported | Medium | Low |

### Relative anchors (how actual effort compares with early estimates in this class)

| # | Anchor | Value | Source | Confidence in the shape | Confidence in the number |
|---|---|---|---|---|---|
| R-1 | Cone of uncertainty at the initial-concept stage | actual/estimate from 0.25× to 4×; about 0.5–2× once the product definition is approved | McConnell, *Software Estimation* (2006), after Boehm | High | Medium |
| R-2 | Average effort overrun of software projects | about 30–40% over the estimate; median above 1 | Moløkken-Østvold & Jørgensen, review of estimation surveys (2003) | High | Medium |
| R-3 | IT project cost overruns have a fat tail | about 1 in 6 overruns by about 200% | Flyvbjerg & Budzier, *HBR* (2011) | High (fat tail) | Medium |
| R-4 | Rewrites ("second-system effect") overrun more than new systems: about 1.5–3× the initial expectation is common, because the scope keeps growing until the new system matches everything the old one does | factor of 1.5–3 | Brooks (1975); practitioner consensus | Medium–high | Low |
| R-5 | Challenged projects overrun cost by about 45–56% on average (2000s CHAOS reports; method contested) | about 1.5× | Standish Group CHAOS | Medium | Low |

---

## 4. Synthesis

**How the absolute anchors compare.**
- The middles are about 110 (A-2), about 140 (A-1), about 190 (A-3) and about 100–300 (A-4).
- They **agree in order of magnitude**: all put the middle between about 100 and 200 pm.
- They **disagree in level by about 1.7×**. The disagreement is systematic: the parametric model (A-3), which counts phases and team environment in full, sits above the ISBSG-based anchor (A-2), which tends to under-record early-phase work.
- A-2 and A-3 both rest on an assumed class size, so they are not fully independent of each other. A-1 is independent of them, and it lands between them. This is the only cross-check this method has, and it holds loosely.
- I place the median at about **150 pm**, between the ISBSG and COCOMO middles and close to the practitioner middle.

**Where the relative anchors apply.** There is no early estimate to scale here, so I use the relative anchors only for the **shape** of the distribution:
- Pre-discovery stage (R-1) and a rewrite with hand-built infrastructure (R-4): the upper tail should reach about 2× the median at P90.
- Fat tail (R-3): P90 should not be trimmed.
- The lower tail is limited, because a rewrite rarely finishes much below the class typical once it has a parallel-run Definition of Done: about 0.5× the median at P10.

**Heterogeneity.** The class spread from A-1 alone is about 4× from low end to high end. I keep that width.

---

## 5. Distribution (recorded person-months, 168 h, losses outside)

| Quantile | Effort | Class scenario |
|---|---|---|
| **P10** | **80 pm** | A small, strong team that learns quickly (about 6–7 people over about 12–13 months). The architecture settles early and the hand-built reliability layer stays simple. The parallel run confirms agreement with the old system after a few iterations. The functionality to match is narrower than it first appeared, and the internal sponsor accepts a lean portal and console. |
| **P50** | **150 pm** | A typical run: a team of about 9–10 over about 17–18 months. Discovery is slower than planned and one architectural direction is dropped. Stabilising the reliability layer under load takes several rounds. The parallel run finds behavioural differences from v1 that have to be reproduced. Pressure without a deadline lets scope grow moderately. |
| **P80** | **240 pm** | Second-system growth: the rewrite absorbs "fix what we don't like" items beyond the original intent. The reliability and orchestration layer needs a partial redesign after load or failure testing. The parallel run drags on because small mismatches with the old system each need investigation. The team grows mid-project, which adds coordination cost. |
| **P90** | **310 pm** | Fat-tail case: a significant redesign or restart of the core coordination approach. Cutover is postponed more than once. Legacy coexistence and data migration become a sub-project of their own. The project runs about 2× the typical class duration, with a team of 12 or more at its peak. |

**Skew.** The distribution is right-skewed:
- P50 − P10 = 70 pm, while P90 − P50 = 160 pm.
- Ratios: P90/P50 ≈ 2.07 and P50/P10 ≈ 1.9.
- The skew is kept deliberately. The class tail beyond P90 is not bounded by this method: 400+ pm occurs in the class.

---

## 6. Assumption log of the method

### Part 1: the static blind-spot list (method metadata, reported verbatim, not findings of this run)

1. The specifics of this team.
2. The specifics of these integrations and dependencies.
3. The real difficulty of the particular features (no decomposition was done).
4. The quality and stability of this particular client or sponsor.
5. The dating of the base rates.
6. Management interventions that truncate the tail (de-scoping, changing the contract model, declaring victory early).
7. **Misclassification** — the risk that the class itself is wrong.

**My confidence split across the stated class and its neighbours (for item 7):**

| Class | Confidence | Which way it would move the answer |
|---|---|---|
| The stated class: in-house rewrite of a distributed transaction back-end with portal, console and parallel-run cutover | about 55% | — |
| Greenfield or modest line-of-business web application with back-end workers | about 20% | **Down**: median about 60–90 pm |
| Build of a distributed platform or home-grown middleware (the reliability infrastructure is the main product) | about 20% | **Up**: median about 220–350 pm, heavier tail |
| Incremental rework of an existing product with partial reuse | about 5% | **Strongly down**: median about 30–60 pm. A4 argues against this class. |

### Part 2: project-specific observations (kept separate from the list above)

- **The source is a recollection.** Lists of scope recalled after the fact tend to leave out work (migration, environments, operational tooling). That points to a scope that is really larger than stated, and it is a boundary risk rather than an estimating risk.
- **The mandate is ambiguous.** "Redo what management did not like" suggests a partial rework, while "no code reuse" suggests a full rewrite. I classified by the full rewrite (A4). If the mandate was narrower, the lower-neighbour class applies.
- **The base rates are roughly era-matched.** Most anchors date from the 2000s, which fits A5, so there is little dating correction to make. Even so, the ISBSG and QSM numbers are my reading of published medians, not a fresh query.
- **The fixed immersion phase does not size the project.** The input fixes the immersion phase at about 1–2 months. I did not use it as a scale anchor; the phase is simply inside the class scenarios.
- **Two management interventions matter most for the tail.** Declaring cutover before the parallel run fully agrees with the old system would pull P80 and P90 down. Without a hard deadline, nothing forces de-scoping, which leaves the upper tail open.

## RC65-2

# Lytin-R 1.1

**Engine:** `Lytin-R 1.1` (reference class forecasting, the outside view)
**Project:** FaxRxTx (Venali): a rework of the fax platform's core, as scoped in §6 and A1
**Stage of estimation:** a blind estimate made before any architecture work. A working v1 serves as the requirements. On Boehm's scale this sits between "concept of operation" and "requirements specified".

## 0. Contamination check

- **No work breakdown, bottom-up estimate, target number, budget or deadline.** The §6/A1 list sets the scope. It does not break the work into priced parts, so I used it only for the scope boundary and for deciding which class the project belongs to. The orchestrator's struck lines were removed before I received the input.
- **One partial duration.** The input says domain immersion took "about 1–2 months". That is the length of one phase, not a total. I did not use it as an anchor.
- **Ambient repository context was present and I set it aside.** The harness prepended a git status (including an untracked file name), recent commit subjects (one mentions a FaxRxTx test report) and a user memory index. None of it was read as input, acted on, or allowed to shape the numbers. I read no files and called no tools.
- **Verdict:** clean. The run went ahead.

---

## 1. The declaration

**1. Unit.** My unit is the **staffed person-month**: one person assigned to the project for one calendar month. It is recorded, assigned time. It includes that person's meetings, reviews, coordination, context switching and waiting. It is **not** hours of hands-on work on tasks. I use it because my strongest anchors are "team size × calendar duration", and that is their native unit.

**2. Losses.** Annual leave, public holidays and sickness are **inside** my figures, because a staffed month is a calendar month.
- A staffed month has about 21.7 weekdays. After leave, holidays and sickness, about 18.5–19.5 of them are days actually present. The lower value assumes European-style leave; the higher assumes US-style leave. The team's location is unknown.
- **Converting to the pipeline's unit (A9: 1 pm = 21 pd = 168 h):**
  - If A9's 21 pd are *present* working days: 1 staffed pm ≈ **0.88–0.93** pipeline pm.
  - If A9's 21 pd are *paid* days, with leave charged: 1 staffed pm ≈ **1.0** pipeline pm.
  - If A9's 168 h are *hours on task*: at about 5.5–6.5 task hours per present day, 1 staffed pm ≈ **0.60–0.75** pipeline pm.
- I did not apply any of these. The orchestrator should choose one and apply it once, visibly.

**3. Roles.** My figures count **every role charged to the project team**: developers, architect/tech lead, QA, PM/scrum master, and the team's own share of cutover and parallel-run work.
- **Outside:**
  - business management and product owners on the business side;
  - operations staff who buy, rack and run the Windows cluster and Lustre;
  - PoP field staff;
  - NOC operators, once it is running;
  - customer support;
  - the teams that own billing, routing and PoP software.

**4. My sources' conventions, and where they disagree.**

| Source family | Native convention | What I did |
|---|---|---|
| Practitioner consensus (team × duration) | Staffed calendar months, losses inside, whole team | Used as is (native) |
| ISBSG repository (from memory) | Recorded hours, "normalised work effort". The Level-1 resource convention covers the dev team including its PM/QA; leave is normally not recorded | Converted to staffed months at about 1 staffed pm ≈ 140–150 recorded hours |
| QSM / Putnam benchmarks | Person-months of staff effort, with a configurable hours-per-month (often around 152) | Treated as roughly staffed months, ±10% |
| Standish, Flyvbjerg–Budzier, Jørgensen, Boehm/McConnell | Ratios of actual to estimate; they have no unit | No conversion needed |

**Size of the disagreement:**
- ISBSG-style recorded hours versus staffed months: about **10–20%**. Recorded hours come out lower for the same team and calendar, because unrecorded overhead and leave fall away.
- Role coverage can add a further **~10%**. Some ISBSG submissions leave out part of PM/QA.
- The absolute anchors are therefore inconsistent by about **15–30% in level** before any real disagreement about size. The table in §3 gives them after conversion.

**Scope boundary.**
- **Covered (A1 and A2):** the discovery and architecture-selection phase, design, development, testing, the parallel run on the real traffic stream compared against the old system, and rollout, up to the point where v1 can be decommissioned.
- **Exclusions I honoured:** PoP software, the least-cost routing program, billing, post-launch operation, and v1 development.
- **Work at the edge of the scope** (any of these could move the actuals by double-digit percentages):
  - (a) Hyper-care after cutover. The definition of done (A2) ends at "v1 can be decommissioned", but post-launch operation is excluded, and stabilisation work straddles that line.
  - (b) Migrating customer configurations and the fax archive from v1.
  - (c) Keeping v1 alive and fixing it during the coexistence period.
  - (d) Setting up the cluster, Lustre and the database. Whether that is ops work or team work is unclear.
  - (e) Evaluating and licensing the OCR library and the printer driver.
  - (f) Training NOC operators and writing runbooks.

My distribution assumes the team carries (a), (b) and (c) in part, as projects in this class usually do. It assumes (d), (e) and (f) sit mostly outside.

---

## 2. The reference class

**Definition.** A product company rewrites a working production back-end platform in-house. The platform is a distributed, high-volume pipeline that processes transactions or messages. The rewrite includes:
- a custom-built reliability and orchestration layer;
- an operations console;
- a customer-facing web portal;
- a period of coexistence with the legacy system, verified by a parallel run.

The period is the pre-cloud .NET/Java era, roughly 2005–2010. The team is medium-sized, about 5–12 people with QA/PM included. The estimate is made before architecture work, with the old system standing in for the specification.

**Membership criteria.** These are structural: they describe which categories of work projects in the class contain.
1. **Contains:** a back-end processing pipeline built from distributed workers; home-grown delivery guarantees or orchestration (no off-the-shelf broker); an internal monitoring or operations UI; an external customer portal; integration with, and a parallel run against, a legacy system; and cutover.
2. **Does not contain:** firmware or edge/telecom protocol software; hardware design; billing or financial ledger systems; mobile clients; regulatory certification programmes.
3. **Organisation:** an internal product company, with no contractual client and no fixed-price contract.
4. **Nature of the work:** a rewrite (a "second system") with no code reuse, not a greenfield product and not an incremental refactor.

**Why this project is in it.** Every "contains" category is present in §6 and A1. The telecom edge (PoPs), routing and billing are expressly excluded, which puts the project in this class rather than a carrier-platform class. The organisational context (A8) and the no-reuse rewrite (A4) match criteria 3 and 4.

**Neighbouring classes it is not in:**
- **Carrier-grade telecom platforms or middleware built from scratch.** This project lacks that class's edge and protocol branch, and in any case that class runs larger.
- **Web/SaaS application rewrites with a thin back end.** This project carries a distributed-reliability branch and a parallel-run branch that such rewrites lack, and that class runs smaller.
- **Small skunkworks replacements** by 2–4 people. The input mentions a blended team with QA and PM and a formal planning phase, which is inconsistent with that class.

---

## 3. Base rates and anchors

### 3a. Absolute anchors: what projects in this class cost

All values are in staffed person-months after conversion (see §1).

| # | Anchor | Value | Source | Confidence (shape / number) |
|---|---|---|---|---|
| A-1 | In-house rewrites of mid-size production distributed platforms at product companies, 2005–2012: typically 5–12 people for 12–24 calendar months including the parallel run | 60–250 pm; median about **100–120** | Practitioner consensus | Shape: medium. Number: low–medium |
| A-2 | ISBSG redevelopment and new-development projects, medium-to-large size band, 3GL/.NET/Java: median peak team about 7–9, median duration about 10–14 months, strong right tail | About 70–110 pm central (recorded hours converted); P90 roughly 2.5× the median | ISBSG repository, general release data, recalled from memory | Shape: medium. Number: low (dated, recalled, and sensitive to the size band) |
| A-3 | QSM business/infrastructure systems of medium size: median duration about 9–13 months, peak staff about 7–10, effort growing steeply as schedule is compressed | About 60–120 pm central | QSM/Putnam benchmark publications, recalled | Shape: medium. Number: low |
| A-4 | "Second-system" rewrites of a working product: consistently take longer than planned, because of scope expansion ("fix everything we disliked") and parity-chasing against the old system | No number, only direction: pushes the class upward and widens the tail | Brooks, *The Mythical Man-Month* (1975); Spolsky, "Things You Should Never Do" (2000); practitioner consensus | Shape: high. Number: none |

### 3b. Relative anchors: how actuals compare with early estimates

| # | Anchor | Value | Source | Confidence (shape / number) |
|---|---|---|---|---|
| R-1 | Cone of uncertainty: at the concept-of-operation stage, actual effort falls within 0.5×–2× of the estimate; at requirements-specified, within 0.67×–1.5× | This project's stage sits between the two, so about **0.55×–1.8×** | Boehm, *Software Engineering Economics* (1981); McConnell (2006) | Shape: high. Number: medium (the original is partly judgement) |
| R-2 | Average effort overrun in software projects of about 30–40% against early estimates | Median actual/estimate about 1.2–1.4 | Moløkken-Østvold and Jørgensen, review of surveys (2003) | Shape: high. Number: medium |
| R-3 | IT projects: average cost overrun about 27%, with a fat tail; about 1 in 6 overran by about 200% | Tail ratio about 3× at roughly the P85–P90 level | Flyvbjerg and Budzier, HBR (2011), about 1,471 projects | Shape: high. Number: medium (mixed and public-sector-heavy sample) |
| R-4 | Challenged projects around 2009: average cost overrun about 45–55% | Supports a median ratio above 1 | Standish CHAOS (2009) | Shape: medium. Number: low (method widely criticised) |
| R-5 | Internal projects with no hard deadline tend to drift in scope more than contracted ones; the tail is longer and truncation comes later | Direction only | Practitioner consensus | Shape: medium. Number: none |

---

## 4. Synthesis

**The absolute anchors roughly agree.** A-1, A-2 and A-3 are largely independent (practitioner experience, a submitted-project repository, a vendor benchmark). Their centres fall at about 100–120, 70–110 and 60–120 staffed pm. They overlap across **about 80–115**. They disagree in level by about 20–30%, which is about the size of the unit and role-coverage inconsistency in §1. So part of the gap is a matter of convention rather than of size. A-1 is the native unit and describes the rewrite subtype most specifically, so I weight it most. I place the class median at about **105**.

**The relative anchors set the shape, not the level.** The absolute anchors are *actuals*, so they already contain the overruns. Applying R-2 or R-4 as a multiplier on top would count the overrun twice. I used the relative anchors only for the tail:
- R-1 gives a stage-appropriate spread of about 0.55×–1.8× around the median.
- R-3 says the tail beyond that is fat: about 3× the estimate for roughly one project in six.
- A-4 and R-5 push the right tail out further for this subtype: a rewrite, internal, no hard deadline.

**The class is heterogeneous.** Team sizes span about 2×, durations about 2×, and the scope of parallel run and coexistence varies a lot. I therefore kept the spread wide rather than averaging it away.

**The only cross-check** available inside this method is that the three absolute anchors agree. They do agree, loosely, and only to within the unit-convention noise. That limits how much confidence the P50 deserves.

---

## 5. Distribution

All values are in staffed person-months, with losses inside and the whole team counted (see §1).

| Quantile | Effort (staffed pm) | Ratio to P50 | Class scenario behind it |
|---|---|---|---|
| **P10** | **55** | 0.52× | A small, senior team of about 5–6 finishes in about 10 months. Discovery converges fast, and the reliability-layer design is right first time. The parallel run finds few discrepancies and cutover is clean. Management holds scope to "like v1, minus the specific complaints". |
| **P50** | **105** | 1.0× | About 7–9 people including QA/PM over about 13–15 months. A usual discovery phase, then one significant design revision of the orchestration layer. The parallel run takes several months and uncovers a steady trickle of parity gaps, which are fixed before cutover. Some scope growth ("while we're at it"). |
| **P80** | **175** | 1.67× | About 9–10 people over about 18–20 months. The home-grown reliability layer is reworked substantially after load or failure testing. Parity with v1 turns out to be a moving target, and cutover is postponed once or twice. Scope expands under pressure without a deadline to force a stop. The team carries part of v1's upkeep. |
| **P90** | **240** | 2.3× | About 10–12 people over about 20–24 months. The full second-system effect: the architecture is re-litigated mid-project, cutover is repeatedly deferred, the portal and operations tooling expand, and the parallel run turns into a prolonged co-operation period. This is the Flyvbjerg tail band. |

- **Beyond P90:** abandonment, restart or re-plan. Actuals of 300–400+ staffed pm are within the class's historical record, unless management cuts the tail (see blind spot 6).
- **Skew:** strongly right-skewed. P50 minus P10 is about 50; P90 minus P50 is about 135, roughly 2.7 times as long. P90/P10 is about 4.4, which reflects the class's heterogeneity and the stage of estimation. I did not make it symmetric.
- **In the pipeline's unit, for reference only:** at the 1.0× reading of A9, the values are unchanged. At the "168 task hours" reading, multiply by about 0.6–0.75. The orchestrator's conversion, not mine, should decide which applies.

---

## 6. Assumption log of the method

### 6a. Static blind spots (method metadata, reported verbatim; not findings of this run)

1. The specifics of this team.
2. The specifics of these integrations and dependencies.
3. The real difficulty of the particular features (no decomposition was done).
4. The quality and stability of this particular client or sponsor.
5. The dating of the base rates.
6. Management interventions that truncate the tail (de-scoping, changing the contract model, declaring victory early).
7. **Misclassification**: the risk that the class itself is wrong.

**Blind spot 7 for this run: how my confidence splits across classes, and which way each would move the answer.**

| Class | Confidence | Effect if this is the true class |
|---|---|---|
| Stated class: in-house rewrite of a distributed back-end platform with ops console, portal and parallel run | **55%** | None (this is the distribution above) |
| Carrier-grade or high-availability platform built from scratch (reliability layer treated as middleware product development) | **20%** | Moves the answer **up**, about 1.5–2.5× at every quantile, with a fatter tail |
| Web/SaaS application rewrite with a moderate back end | **20%** | Moves the answer **down**, about 0.5–0.7×, with a narrower tail |
| Small-team skunkworks replacement (2–4 people) | **5%** | Moves the answer **sharply down**, to about 0.25–0.4× |

The neighbours roughly balance around the stated class, so the P50 stays where it is. But they widen the effective range beyond what §5 shows on both sides, and more on the upper side.

### 6b. Project-specific observations (separate from the list above; not used to adjust any quantile)

- **Domain new to the team, with v1 standing in as the specification** (A3). The first pulls toward the upper side of the class and the second toward the lower. Because they pull in opposite directions, I did not adjust for either.
- **No hard deadline, but pressure, in an internal product company** (A8). This matches the class feature behind R-5, and it is already reflected in how long the right tail is. I made no further adjustment.
- **Hand-written orchestration instead of a broker, after the MSMQ failure** (A5). This is the branch most likely to decide whether the project behaves like the stated class or like its carrier-grade neighbour. I cannot assess it without decomposition, which is blind spot 3.
- **The "1–2 months" discovery figure** is a partial duration in the input. I did not use it as an anchor.
- **Unit ambiguity in A9.** "1 pm ≈ 21 pd ≈ 168 hours" does not say whether days are present or paid, or whether hours are recorded or on-task. That can move a comparison between methods by up to about 35% (see §1, field 2). It should be settled before any divergence between methods is attributed to estimating error.
- **Edge-of-scope items** (hyper-care, migration, v1 upkeep during coexistence). My class base rates include them in part. A method that excludes them strictly will read lower for reasons that have nothing to do with estimating skill.

No files were read or written in this run.

---

# INPUT 6 — the Step C corrections, `Lytin-K 1.1` × Claude Opus 5 (run 66), verbatim

It saw INPUT 1, INPUT 2 and the bottom-up reading (structure, totals, composition, coverage report). It never saw INPUT 5.

# Lytin-K 1.1 — Step C calibration parameters for FaxRxTx

**Engine:** `Lytin-K 1.1`

**Bottom-up chain being calibrated:**
- **Product model:** `HM61-1`, built by `Hotyn-M 2.1`. The other repeat, `HM61-2`, is not the target.
- **Other chain stages:**
  - work model by `Hotyn-W 1.2`
  - size classes by `Hotyn-D 2.0`
  - prices from rate table v0.1-h
  - demanded-work addendum by `Hotyn-K 1.1`
  - all sensors ran on Claude Opus 5
- **Engine pairing:** `Hotyn-K 1.1` is a different engine from `Lytin-K 1.1`. The version numbers match by coincidence and do not mean the engines match. If the rate table or `Hotyn-M` changes version, these parameters must be re-derived.

---

## 1. Input inventory

**What I was given**
- **INPUT 1:** the project description, with the orchestrator's struck lines marked in place (calendar period, acquisition and revenue, where the outcome is kept, an unrelated draft).
- **INPUT 2:** the assumption log A1–A9, verbatim.
- **INPUT 3:**
  - engine stamps
  - unit statement and pinned technology declaration
  - totals for both sizing repeats
  - composition of repeat 1
  - the 84-element structure
  - the coverage report

**Contamination check**
- **No forbidden content.** The prompt has no reference-class forecast, no quantiles, no target total, no budget, no deadline, no gap statement, and no instruction to make anything sum to anything. The struck lines were removed before I received them. I did not try to reconstruct them.
- **Numbers that are not targets:**
  - The bottom-up totals (10194 / 9846 h) are the estimate itself, which is allowed input.
  - The traffic figures (30/s, 300/s) describe system scale, not effort.
  - The note that actual traffic was below nominal is about load, not effort.
  - "1 pm ≈ 21 pd ≈ 168 h" is a unit convention.
- **Ambient context, quarantined.** The harness added context to my session: a git status, recent commit subjects (one names a FaxRxTx test report), the working directory, and a user memory index. None of it was used. It is not treated as contamination, and the run proceeds on the pasted input alone.
- **Files and tools.** No files were read and no tools were called.

**Confirmed:** I was **not** given any target, class output or gap figure.

---

## 2. Double-counting check

**Rule applied throughout:** if the estimate carries a category, I correct at most the part it leaves over (the residual). If it does not carry it, the correction is mine.

| Blind spot | What the estimate already carries | What stays open |
|---|---|---|
| Testing effort | Test design (A2), unit tests (A3), test execution (A5), defect resolution (A6), regression suite (A7), test data (A8) and contract tests (A10): about 3.9k of 6.6k element-item hours. Also test strategy (A1) and verification checklist (U1d). | Nothing general. Performance and burst testing is outside the declaration, so it is open. |
| Integration | C3 at 20% at every parent node, root included (3144 h). | Nothing. |
| Rework and defects | Defect resolution, 2 cycles per subsystem. | Only rework caused by requirement change (goes to growth). |
| Omitted work, named | Nothing: 5 named holes and 11 closure findings are priced at zero. | All of it, as itemised additions. |
| Omitted work, unnamed (requirement growth) | Nothing. The v1 reference lowers the risk; the itemised findings shrink the residual. | Residual growth. |
| Up-front domain immersion and architecture choice (W-F48) | Per-element design (K1), per-element requirement elaboration (D4) and mobilisation (D1). No system-level architecture or technology-selection item. | The phase itself. |
| Transition: parallel run, soak window, hyper-care (W-F50) | Cutover (E6), one-pass stream test (W-F49), decommission check (W-F52), runbook, handover pack and release notes (O2–O4), promotion procedure (E3). About 2% of the total. | Parallel-run comparison until outputs agree, soak window, stabilisation before decommission. |
| Project management | Planning and tracking (D2, 332 h), status reporting (D3), risk management (D6), mobilisation (D1). About 4%. | Residual PM/product-owner hours. |
| Within-day overhead (net task hours → working hours) | Only the named ceremony rows above. | Other ceremonies, interruptions, coordination and admin. |
| Era and team experience | Nothing: "no era adjustment anywhere". W-F48 covers only the immersion stage. | Tooling gap and the team's learning curve during construction. |
| Technical complexity of distributed delivery | Size classes count named things, not difficulty. Hand-built orchestration is present as elements (L32–L35, L47, L48). | The difficulty premium on those subtrees. |
| Legacy data migration | Declared out. D12 (account sync) covers ongoing sync only. | Initial load of user accounts (closure finding). Archive migration: see §4. |
| Cluster hosting and installation | Hosting set-up (E7, 3 envs, 47 h) and environment set-up (E1 prod, L). | Build-out of a 16–20-node cluster, private network and Lustre mounts. Buying the hardware stays out. |
| Security and compliance | Declared out. | Left out (§4). |
| Operating the old system during coexistence | Declared out. A1 excludes operation. | Left out (§4). |

**Partition result.** Every category above falls on exactly one side:
- **Mine:** the estimate carries it at zero or not at all.
- **Estimate's:** it carries the category and my correction is explicitly the residual. This applies to PM, transition, within-day overhead and migration.
- **Left out:** named in §4 and assigned elsewhere.

No category is both carried and corrected, and none is in neither.

**How the coverage report moved my rates**
- **No generic uplift for testing, integration or rework.** The estimate carries all three heavily. I apply none, and I do not apply a system-wide reliability factor (the COCOMO II "RELY" rating, required reliability) either.
- **Transition and PM are residuals, not full rates.** I subtract what is carried (about 2% and 4%) from the published ranges.
- **Omissions are itemised, not a blanket percentage.** The report names the holes and findings, so I price them as element additions. That lowers the unnamed-growth multiplier to a central 1.12, instead of the roughly 1.25 a generic "about 25% requirements change" figure would suggest.
- **Within-day overhead lowered.** Ceremony rows are partly carried, so I take the central from about ×1.33 down to ×1.25.
- **Sensitivities the declaration named but did not price** (performance testing, migration, hosting scale) become targeted additions where the source text shows the project needed them (A6, §4, §5, §6).

---

## 3. Corrections

### Declaration for the additions

This applies to corrections A1–A5 only. T1–T5 and G1–G2 are dimensionless factors and need no declaration.

1. **Unit.** Additions are given as **element-equivalents and activity rows**, to be priced by the same chain: rate table v0.1-h, its E = (O+4M+P)/6 rule, and C3 for elements placed under a parent. They therefore land in **net task hours**, the same unit as the estimate, so no conversion is needed. I give no amounts in hours or days of my own.
2. **Losses.** Leave, public holidays and sickness are **outside**. Within-day overhead is **outside** too; G1 carries it. A9's 168 h per person-month (21 working days × 8 h) is a unit with leave also outside, so the two units match on losses. The conversion to person-months belongs to the step that applies these parameters, and G1 must be applied before it.
3. **Roles.** The delivery team's hours (development, QA, PM), as the rate table's activities assign them.
4. **Source conventions.**
   - COCOMO II defines 1 PM = 152 h. A9 uses 168 h, a factor of ×1.105 between them. I take **only ratios** from COCOMO II, so this difference does not propagate.
   - Cohn counts ideal hours within an 8-hour day, which matches the day in A9.

### Correction table

Here "product base" means element items + all C3 + the root's own per-parent items, in each repeat.

| id | Name | Blind spot addressed | Form | Low – central – high | External source | Confidence |
|---|---|---|---|---|---|---|
| **A1** | Named holes priced | Unsized elements | pure addition (elements through the chain) | **L27** further renderers: 1 / 2 / 3 × S. **L38** DB schema: S / M / L. **L51** old-system interface: S / M / L. **L46**, repeat 2 only: 0 / S / M. **L56**: 0 / 0 / 0 (an umbrella whose content is its siblings; its inventory is in A2). L32 and D03 seed data: 0 / 0 / 0. | Counts from A7 (8–10 formats, 7 named). Prices from rate table v0.1-h. | medium |
| **A2** | Closure findings priced | Named missing work | pure addition (elements) | See the A2 breakdown below the table. Totals: low 5S; central 8S + 1M; high 6S + 4M. | Findings from the sizing sensors; prices from rate table v0.1-h. | medium-low |
| **A3** | Initial load of user accounts from v1 | Migration outside the declaration | pure addition (element, store/interface) | S / M / L | §6 (coexistence) and the closure finding; rate table v0.1-h. | medium |
| **A4** | Performance and burst testing | Testing outside the declaration | pure addition (activity rows + element) | Low: the table's performance-testing row on L47 only. Central: the row on L46 and L47, plus a load-generator element of class M (simulated PoP and mail stream). High: the same, with the load generator at L. | A6 gives measurable targets (30/s nominal, 300/s burst), which removes the crossing's reason for refusing. Prices from rate table v0.1-h. | medium |
| **A5** | Production cluster build-out | Hosting scale | pure addition (re-pricing existing rows) | Low: none. Central: E1-prod and E7 one size class up. High: two classes up. | §5: 16–20 nodes, private network, Lustre. Rate table v0.1-h. | low |
| **T1** | Complexity of distributed delivery | Difficulty not in the size classes | targeted multiplier on the items + C3 of subtrees N30 and N40 and of leaves L46, L47 (A1/A2 additions in them included) | ×1.00 – ×1.17 – ×1.34 | COCOMO II (Boehm et al. 2000), product complexity (CPLX) rating: Nominal 1.00, High 1.17, Very High 1.34. | medium-low |
| **T2** | Requirement growth, unnamed | Emergent scope | targeted multiplier on the product base after A1–A4 and T1 | ×1.05 – ×1.12 – ×1.25 | McConnell, *Code Complete* 2nd ed. §3.4, citing Boehm 1981 and Jones 1994/2000: about 25% requirements change on an average project. Jones: about 1–2% creep per month of design and coding. Set below the generic figure because a working v1 exists and the named findings are itemised. | medium-low |
| **T3** | W-F48, domain immersion and technology selection | Up-front phase | targeted multiplier on base B, applied as an addition | +4% – +8% – +15% | COCOMO II MBASE/RUP phase distribution: Inception 6% (range 2–15%) on top of Elaboration + Construction. Central set above 6% because the domain was new to the team (A3), with explicit technology study. This replaces the headcount × length form the rate author asked for, which is unanswerable by design (A3). | medium-low |
| **T4** | W-F50 plus soak window and pre-decommission stabilisation | Transition residual | targeted multiplier on B, as an addition | +3% – +7% – +14% | COCOMO II phase distribution: Transition 12% (range 0–20%), less the roughly 2% already carried. Conversion work is excluded here because A3 covers it. | medium-low |
| **T5** | PM and product-owner residual | Management | targeted multiplier on B, as an addition | +2% – +5% – +8% | Management at roughly 8–14% of total effort, as recalled from COCOMO II activity distributions and Jones, *Estimating Software Costs*; verify before relying on it. Carried about 4% is subtracted. | low |
| **G1** | Within-day overhead | Net task hours vs working hours | **global** multiplier | ×1.15 – ×1.25 – ×1.40 | Cohn, *Agile Estimating and Planning* (2005): about 4–6 productive hours per 8-hour day. Scrum Guide timeboxes: about 10–12% of sprint time in ceremonies. DeMarco & Lister, *Peopleware* (interruptions). Lowered for the carried planning and reporting rows. | medium |
| **G2** | Era tooling plus domain learning curve | Modern norms vs 2007–09 conditions and a new domain | **global** multiplier (one merged effect) | ×1.00 – ×1.15 – ×1.27 | COCOMO II use of software tools (TOOL): one rating step, ×1.09–1.15 (e.g. Nominal 1.00 vs High 0.90). Application experience (APEX): Low 1.10 vs Nominal 1.00, averaged over a team that learns as it goes, about ×1.05. Low bound: the table's norms turn out to be era-neutral. High bound: 1.15 × 1.10. | low-medium |

**A2 breakdown (low / central / high class per finding)**

| Closure finding | Low | Central | High |
|---|---|---|---|
| Inbound job hand-off to the workers (L35 partly covers it) | 0 | S | S |
| Faxes for unknown numbers | S | S | S |
| Submission-rejection notices | S | S | S |
| Fallback when the routing program gives no answer | S | S | M |
| Outbound status changes recorded in the token store | S | S | S |
| Clean-up of finished status entries | S | S | S |
| Registry of points of presence maintained after its seed load | 0 | S | S |
| Account creation and provisioning | S | M | M |
| Inventory of the first version's core functions | 0 | S | M |
| Initial migration of user accounts | — | — | — |
| Ending coexistence (W-F52 and E6 partly cover it) | 0 | S | M |

Initial account migration is priced once, as A3, and not here.

**Base B:** the repeat's total after steps 1–3 of §5, excluding the demanded-work addendum rows. T3, T4 and T5 are all taken from the **same B** and do not compound on each other.

**Rules:** both repeats receive the same parameters. Only A1's L46 line differs, because it applies to repeat 2 alone.

**Factors and amounts:**
- **Amounts** (the declaration applies): A1–A5.
- **Factors:** T1–T5 and G1–G2. T3–T5 are percentage factors that behave like additions in total.
- **Global multipliers:** exactly two, G1 and G2.

---

## 4. Deliberately uncorrected

- **Differences between the two sizing repeats and between the two product models.** The ×1.035 sizing spread and the ×1.10 leaf difference between `HM61-2` and `HM61-1` are variance from step 1, to be carried forward. They are not corrections, and I did not use ×1.10 as a rate anywhere.
- **Optimism bias in element sizes.** The prices are external table norms, not individual guesses, and PERT E is already applied. Any remaining bias belongs to the reference-class sensor.
- **Security and compliance assurance.** Healthcare and finance clients make it plausible, but neither the source nor A1 puts it in the team's scope. It stays a declared sensitivity.
- **Migration of the fax archive and configurations beyond accounts.** The source does not mention it. It is flagged for the orchestrator.
- **Operating the old system during coexistence, hyper-care after decommission, and buying the cluster hardware.** A1 excludes them (operation) or the organisation does them.
- **Tail events.** Examples: a repeat of the MSMQ-style collapse in the hand-built orchestrator, instability in the Black Ice or OCR libraries, Lustre problems, a failed parallel run forcing a redesign. None of these scales with anything as a multiplier; they belong to another sensor's tail.
- **Calendar and headcount effects** (pressure, team size, schedule compression). A3 excludes headcount, and the calendar period was struck.
- **Leave and holidays.** These belong to the unit conversion, not to calibration (see the declaration).

---

## 5. Order of application

Apply to each repeat separately.

1. **Structural additions A1–A5.** Add the elements under their parents and price them through the chain. Element items get C3 at every ancestor; A4's rows and A5's re-pricing are once items with no C3.
2. **T1.** Apply to the items + C3 of N30, N40, L46 and L47, including any additions from step 1 that sit there.
3. **T2.** Apply to the product base as it stands after step 2.
4. **Fix base B.** B is the total after step 3, excluding the demanded-work addendum.
5. **T3, T4, T5.** Compute each on that same B, in parallel, and add them.
6. **Add the demanded-work addendum** (W-F49, W-F52) unchanged.
7. **G2.** Apply to the whole total.
8. **G1.** Apply to the whole total.
9. **Unit conversion.** Only now convert to person-months (A9). This belongs to the step that applies these parameters and is not part of this output.

---

# INPUT 7 — the orchestrator's pricing of the Step C structural additions, and the chain applied in RK66's order

RK66 states additions A1–A5 as element fills to be priced "by the same chain". The orchestrator priced them with the pinned rate table (a script, `price_fills66.py`) and applied T1–T5, G2, G1 in RK66's §5 order to each repeat. **These are arithmetic, not new rates; you may recompute them, and you may reject a pricing choice below if it contradicts RK66 — say so; you may not change any rate.**

Pricing choices the orchestrator made where RK66 left them open:
- an added element gets the per-element activities its class receives in the crossing (behaviour / store: design, implementation, test design, unit tests, code review; interface: + contract testing; statement: statement realisation), and integration C3 = 20% × its number of ancestors (root included); no requirement elaboration, no change to per-parent items;
- classes and parents: L27 behaviour under N22; L38 store under N50; L51 interface under N80; L46 statement under N90 (repeat 2 only); A2 findings as behaviour under N10, N10, N21, N23, N30, N30, N90, N70, N00, N80 (in RK66's row order); A3 interface under N80; A4 load generator behaviour under N90, and A4's performance-testing rows as once items without C3 (size S: one measurable target each);
- **A5 is not priceable**: the table has no XL row for environment provisioning or hosting set-up (both already at L) — carried at zero, named;
- T1 base = items + C3 inside subtrees N30 and N40 + own items of L46, L47 (repeat 1: 1457 h; repeat 2: 1440 h) + additions placed there.

Central fills (repeat 2), net task hours — items, and items with C3:

| fill | class | size | items | with C3 |
|---|---|---|---:|---:|
| A1 L27 further-format renderers | behaviour | S | 28.1 | 45.0 |
| A1 L27 further-format renderers | behaviour | S | 28.1 | 45.0 |
| A1 L38 database schema | store | M | 55.7 | 77.9 |
| A1 L51 old-system interface | interface | M | 95.7 | 133.9 |
| A2 inbound job hand-off | behaviour | S | 28.1 | 39.4 |
| A2 faxes for unknown numbers | behaviour | S | 28.1 | 39.4 |
| A2 submission-rejection notices | behaviour | S | 28.1 | 45.0 |
| A2 routing-program fallback | behaviour | S | 28.1 | 45.0 |
| A2 outbound status recording | behaviour | S | 28.1 | 39.4 |
| A2 clean-up of finished status | behaviour | S | 28.1 | 39.4 |
| A2 PoP registry maintenance | behaviour | S | 28.1 | 39.4 |
| A2 account creation and provisioning | behaviour | M | 60.3 | 84.5 |
| A2 inventory of v1 core functions | behaviour | S | 28.1 | 33.8 |
| A2 ending coexistence | behaviour | S | 28.1 | 39.4 |
| A3 initial load of user accounts | interface | M | 95.7 | 133.9 |
| A4 load generator (PoP and mail stream) | behaviour | M | 60.3 | 84.5 |
| A1 L46 capacity statement (repeat 2) | statement | S | 17.3 | 24.3 |

The chain (net task hours; "product" excludes the once layer and the addendum; B = after T2 + once layer + A4 rows; T3–T5 each on the same B; then + addendum; then × G2; then × G1):

| repeat | level | raw total | + element fills | + once fills | product after T1 | product after T2 | B | after T3–T5 (addendum not yet added) | after G2 | after G1 | ×raw to G2 | ×raw to G1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | low | 10194 | 473.3 | 17.3 | 10193.9 | 10703.6 | 11094.0 | 12092.4 | 12192.4 | 14021.3 | ×1.196 | ×1.375 |
| 1 | central | 10194 | 964.9 | 34.7 | 10946.6 | 12260.2 | 12667.9 | 15201.4 | 17596.7 | 21995.8 | ×1.726 | ×2.158 |
| 1 | high | 10194 | 1479.3 | 34.7 | 11722.1 | 14652.6 | 15060.3 | 20632.6 | 26330.3 | 36862.5 | ×2.583 | ×3.616 |
| 2 | low | 9846 | 473.3 | 17.3 | 9846.8 | 10339.2 | 10729.5 | 11695.2 | 11795.2 | 13564.4 | ×1.198 | ×1.378 |
| 2 | central | 9846 | 989.1 | 34.7 | 10624.9 | 11899.9 | 12307.6 | 14769.1 | 17099.5 | 21374.4 | ×1.737 | ×2.171 |
| 2 | high | 9846 | 1527.8 | 34.7 | 11434.1 | 14292.6 | 14700.3 | 20139.4 | 25704.0 | 35985.6 | ×2.610 | ×3.655 |

Note for the units reconciliation: RK66 labels G1 as "net task hours vs working hours" — a multiplier that moves the figure out of the bottom-up's declared unit. INPUT 3b's convention also contains a net-hours-per-present-day figure. Whether G1 and that convention overlap is yours to reconcile before anything is attributed.
