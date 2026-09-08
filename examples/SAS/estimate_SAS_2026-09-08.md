# SAS — the estimate, v1 — 2026-09-08

**The third complete answer this pipeline has produced, and the first written knowing that no
outcome will ever open**: a centre with its calibration, a corridor with its sources named, the
outside view with its tail, the scope that is *not* in any number, and the questions that move the
answer. Written to be read without the conversation behind it.

**Read this box before any number.**
- Every bottom-up figure rests on **rate table v0.1-h — external industry norms in net task hours,
  uncalibrated against any outcome**. The centre is "norms passed through a measured size vector",
  not a validated cost; the diagnosis says to read it as "the table's level ×1.50" until the table's
  level is checked gap-blind.
- The bottom-up stands on **one** product model (HM44-OA1). A second model of the same requirements
  differs ×1.017 in anchored structure (run 44) and has not been priced.
- **No outcome exists for this case and none will** (author, 2026-09-08): the RFP was never awarded
  to the estimating side. Nothing here is validated; the case scores repeatability, and position
  against human estimators if a scale appears, but never calibratability.
- The RFP is dated September 2018 and the norms are modern. Three instruments refused to adjust for
  the era, all for the same reason: the direction is undecidable.

---

## 1. The answer, three parts, not summable

Unit: **net hours of work on the task** — leave, holidays, sickness and presence overhead excluded.
In the comparison-layer convention (`docs/constants.md` §4a: 6 net hours per present day, ×1.10
leave, 21 days) one staffed person-month ≈ 114.5 net task hours.

| part | value (net task hours, A1 scope) | ≈ staffed person-months | what it is |
|---|---|---|---|
| **Centre** | **57 423 – 57 791** | **≈ 503** | the calibrated bottom-up: table-priced assembly 38 069–38 168 × the gap-blind Step C chain (×1.50–1.52): declared holes + closure violations + three coarse XL leaves, each with 20% integration; five once-scoped non-functional verification and content additions; precedentedness and coordination ×1.15; scope growth ×1.18 |
| **Corridor** | **48 092 – 74 123** | 420 – 647 | the spread of the calibration rates (low/central/high) — **the rates' band, not percentiles**, per the rate agent's own constraint. It contains the rates' uncertainty and nothing else: not the model's own spread, not class heterogeneity, not the table's level, not the era |
| **Reserve** | **unresolved between two readings** | | the raw class tail, uncalibrated, both readings kept apart: P80 **37 620 / 75 264**, P90 **50 160 / 99 960** net task hours (RC46-2 / RC46-1, at each reading's own centre conversion). The calibrated centre sits at ≈P63 of one reading and **above P90 of the other**; the diagnosis names the trilemma — the chain overshoots, or that reading's level is low, or its size regime is wrong — and does not resolve it |

**The outside view, for the same scope** (`Lytin-R 1.1`, two identical launches, each declaring its
own unit; converted at the house factor 0.75, `constants.md` §5b, which both declarations contain):

| net task hours | P10 | P50 | P80 | P90 |
|---|---|---|---|---|
| RC46-1 (380 PM at 168 recorded h, leave outside) | 22 680 | **47 880** | 80 640 | 107 100 |
| RC46-2 (215 PM at 152 charged h, leave inside) | 14 250 | **24 510** | 37 620 | 50 160 |

Right-skewed, P90/P50 ≈ 2.0–2.2 in both — the shape agrees within 8%; the level differs ×1.95 at
P50 (×1.77 before any conversion). Neither reading quoted a P95; both said the class contains
non-delivery beyond P90 and declined to number it.

**The raw chain, for the record:** 38 118 net task hours (repeat band 38 069–38 168, ×1.0026),
with its own O/M/P corridor at ρ = 0.5 of 30 000–46 200 — a declared convention, not a measurement,
and three times narrower than either class reading.

## 2. What the diagnosis established (run 48, Steps B–D)

- **Units were reconciled before anything was attributed, from the three declarations themselves.**
  The two class readings define a person-month differently on every axis (21 days / 168 h / leave
  outside against 19 days / 152 h / leave inside) and the differences nearly cancel in net task hours
  (117.6 against 114.0 per PM). Units explain **4–7%** of the class-vs-class gap. The naive
  number-against-number comparison would have **inverted** the diagnosis: it shows the chain 17%
  above the lower reading, where the converted figure is 56% above.
- **The largest quantity in the comparison is the class against itself: ×1.82 at the median after
  conversion**, three times the distance from the chain to the nearer reading. Attributed to one free
  parameter closed two ways — the functional-size regime behind the ISBSG anchor, one reading closing
  it with a number and the other with words — plus a staffing anchor about two different crews and
  misclassification leaning opposite ways at equal confidence.
- **Calibration is one-directional, so it cannot meet both readings.** Every Step C correction points
  up. Against the higher reading the gap is explained 100% with a +12 900 h overshoot; against the
  lower, **explained share 0%** and the gap widens ×2.43; the class-vs-class gap is addressed by no
  rate. The report says so in those words instead of manufacturing convergence.
- **False convergence was checked and refused**: the raw chain (38 118 h) lands within 1.3% of the
  lower reading's P80 (37 620 h) — only at that reading's central conversion factor; at either end of
  its own declared band the coincidence disappears.
- **The rate agent moved its rates down, decisively**, because the coverage report showed the
  estimate carries integration at 59 parents, two test and two UAT cycles, four environments,
  migration with rehearsals, and a penetration test. No integration, test, management, security,
  environment or documentation uplift was applied. What remains is two modest globals and named,
  bounded residuals.

## 3. What is inside the centre

153 pinned obligations (146 product, 7 work) → 246-element product model → 1 650 crossed work items
on 245 elements + a 23-item once-scoped layer, priced by size classes counted from named things (187
sizeable leaves, class agreement 85.0%, total agreement ×1.0026). Includes: element design, build and
review · test design and two execution cycles with two defect cycles per parent · staged UAT ×2 and
user documentation at every surface-bearing parent · integration at 20% of leaf effort at all 59
parents **including the root (4 833 h)** · four environments, pipeline, promotion, cutover, hosting
· migration: source profiling, mapping, ETL, load and reconciliation across 22 stores, two rehearsals
· security review, external penetration test, remediation · operational runbook, handover pack,
release notes, acceptance record · mobilisation, planning, reporting, risk · requirement elaboration
· via the calibration: the 31/14 named holes, the real share of ~30 closure violations, the three
coarse XL leaves (notification engine, record import service, attribute profiles), a load test against
the five response-time targets, a failover and backup/DR exercise, a WCAG 2.0 A evaluation, a
cross-browser matrix, initial in-application help content, a first-in-domain and committee-client
factor, and scope growth from business rules and an identity protocol the client has not yet chosen.

## 4. What is NOT in any number, by name

1. **The post-production support period and transition service (W-4)** — carried on every side,
   awaiting **the term and the service level**. Priced by a rate per unit time once they exist — a
   different instrument. All three instruments exclude it consistently; the one-sided risk that the
   class anchors contain a warranty period inside the team's tenure is named and unpriced.
2. **The impact analysis on deviation from the client's technical standards (NFR-5)** — read at
   count 0; returns as an addition, not a multiplier, if the reading changes.
3. **The refused readings** (declared narrowings that may reverse): all user and role administration
   inside the identity system (A4) · bespoke connectors to named accounting and ERP products (A6) ·
   a public resolver behind the digital identifier (A9) · industry-specific code paths (A10) · a
   third-party business-intelligence product (A14) · a distributed delivery in place of one team at
   one site · no penetration test. Each is a step change, not a multiplier — not in the base, and not
   priced as options on this case (no step-event round was run).
4. **The rate table's level** — the one uncovered spot acting multiplicatively on the whole centre;
   a narrow gap-blind round is requested, not run.
5. **The era** — eight years between the document and the norms; direction undecidable by three
   independent instruments.
6. **Tail and failure events** — late or changed identity platform, undefined business rules,
   committee stalemate, unreconcilable migration data: inside the class quantiles, not in any
   bottom-up item, hence in the reserve and nowhere else.
7. **Effort→calendar conversion** and team availability: a separate step, deliberately.

## 5. The decisions and questions that move this answer

**Two facts, in order of leverage — both instrument questions, neither a client question:**

1. **One declared functional size for the first release**, counted by an instrument blind to both
   class figures, and `Lytin-R` re-run with that size on its input. The two class readings closed
   this parameter two ways and diverged ×1.6–2.2 on it; the diagnosis expects a declared size to
   collapse the class-vs-class ×1.82 to about ×1.2, after which "inside against outside" becomes a
   meaningful question for the first time on this case. The project's function-point counter
   (`Hotyn-P 1.0`) is that instrument.
2. **An external, gap-blind check of rate table v0.1-h's level** against a productivity norm — the
   one factor that moves the calibrated centre more than the whole Step C spread does.

**For the client (from the open-questions register):** over what period and at what service level
does post-production support run (Q14) · does the solution deviate from any technical standard (Q15)
· where do users and roles live, and which protocol will the identity system speak (Q1) · do
"external systems such as QuickBooks or SAP" require product connectors (Q2) · which barcode
symbologies (Q5) · what is the "digital GIN" — a snippet or a resolvable identifier (Q6) · what is
the latency behind "near real-time" (Q12) · which applications are the migration source and which
entity kinds move (Q13) · plus the register's remaining questions, all unasked because this document
has no client behind it.

**Known model and catalogue findings (converged on by independent instruments):** whether a parent
holding only design statements draws test activities, and whether a store written at run time has a
migration count — the crossing's 25 judgement refusals and the sizing repeats' one disagreement are
the same two questions · the GIN/LN twin enumeration (one object or two) · the crosser sees element
names, not obligation texts, so the performance-test activity fired on one statement of 24 · the
bottom-up declares its unit and losses but not its roles.

## 6. Provenance

`Hotyn-M 1.1` (product model, n = 2, Opus) → `Hotyn-W 1.1` (crossing × technology declaration,
catalogue 1.4 with one amendment proposal, seven batches) → `Hotyn-D 2.0` (size classification,
n = 2, Opus) × rate table v0.1-h (`Hotyn-K`, gap-blind) → assembly script → base branch {38 069,
38 168} · `Lytin-R 1.1` ×2 (outside view, Opus, gap-blind, units withheld) · `Lytin-K 1.1` (Step C
rates, gap-blind) · `Lytin-G 1.1` (Steps B–D, Opus, told that no outcome exists). Every sensor on
Claude Opus 5 — one model coordinate throughout. Runs 44–48; raw transcriptions and scripts under
`examples/SAS/run*_raw/`. Every isolation layer held; protocol findings on record: both product-model
replies truncated in transit with no resumption available (run 44), and the diagnostician answering
in the language of the memory index it quarantined (run 48).
