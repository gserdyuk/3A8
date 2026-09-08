<!-- ORCHESTRATOR HEADER, added at saving 2026-09-08. Not part of the sensor's reply.
run: 48 · reading: RK48 · engine (sensor's own stamp): Lytin-K 1.1 · model (launch record): the harness's `opus`
alias, i.e. Claude Opus 5 · agent: rates-step-c · prompt: project brief, assumption log v1 (sanitised), the
bottom-up structure with both repeats' layer totals and compositions, the coverage report (holes, closure
violations, carried-unpriced) — no reference-class figure, no target, no gap · tool_uses: 0 · duration 245 s ·
received complete; taken from the harness transcript file, verbatim. -->

# Step C calibration parameters

**Engine: `Lytin-K 1.1`**
**Calibrating: `Hotyn-M 1.1` / `Hotyn-W 1.1` / `Hotyn-D 2.0` × rate table `v0.1-h`**

Pairing note for downstream: the structure engines are at 1.1 while the sizing engine is at 2.0. My rates are stated against a structure of the `Hotyn-*1.1` shape and a net-task-hour rate convention. If either the structure engines or the rate table are re-versioned, this parameter set does not transfer without re-derivation.

---

## 1. Input inventory

Received:

1. Project description — X-Customer Member Application Solution RFP, September 2018, three modules plus cross-cutting obligations.
2. Assumption log v1 (approved): A1, A2, A4–A12, A16, A17, A19, and the A0 carried-unpriced list.
3. Bottom-up estimate: engine chain, two independent repeats, layer table (element-attached / integration / once-scoped), composition by top-level subsystem, composition by activity, element-class and size-class counts.
4. Coverage report: carried categories, named holes (31 items repeat 1 / 14 items repeat 2), the performance-test closure violation, carried-unpriced A0 obligations, ~30 sizing-sensor closure violations, and the structural facts bearing on blind spots.

**Explicit confirmation:** I was given **no reference-class forecast, no quantiles, no target total, no budget, no deadline, no outcome, and no statement of any gap.** Nothing in this message asks me to make corrections sum to anything. No contamination to report.

**Quarantined, not used:** the harness prepended ambient repository information (a git status line, a branch name, recent commit subjects, an untracked directory name, and a memory index). I did not read it as input and did not act on it. It contains no forecast or target that would trigger a contamination stop; it is simply not my input. No repository files were read.

**Anomaly noted, not a stop:** the totals of the two repeats (38 069 / 38 168) are present. These are the estimate's own output, which I am supposed to see — they are not a target and not a class number, and I have used them only to identify which layer each multiplier attaches to.

---

## 2. Double-counting check

Base: the coverage report, item by item, against the standard blind spots of bottom-up estimation.

| Blind spot | What the estimate already carries | What stays open (mine) |
|---|---|---|
| Decomposition incompleteness — missed low-level items | 1 650 work items over 245 elements; requirement elaboration per covering element | The **named holes** (31 items r1 / 14 r2) and the genuinely-missing share of the **~30 flagged closure violations** → T1, T2 |
| Requirements volatility after baseline | *Elaboration* of what is already known (1 031 h) | *Change and rework* once I-7 business rules and the NFR-3 protocol land → G1. Elaboration ≠ change; the split is clean |
| Integration and interface effort | 20% of subtree leaf effort at 59 parents incl. root (13 065 h); contract tests on 10 interfaces | **Nothing.** No integration uplift from me |
| Functional test and defect rework | Test design, implementation, review; 2 execution cycles + 2 defect-resolution cycles at every parent; regression suites; test data; 2 UAT support + 2 triage cycles; defect resolution 2 892 h | **Nothing on functional rework.** Only non-functional *execution* → A-1…A-4 |
| Non-functional verification | *Realisation and evidence* for 24 design statements; performance test on 1 statement (availability) | *Independent verification*: load test vs the five NFR-14 targets, failover exercise, backup/DR rehearsal, WCAG evaluation, browser matrix → A-1…A-4. Realisation carried / verification open — clean split |
| Project management and overhead | Planning per parent (1 007 h); mobilisation, status reporting, risk management, configuration management | **Nothing as a separate line.** Client-side approval friction only, folded into G2 |
| Environments, pipeline, deployment | Four environments, pipeline, promotion procedure, cutover, hosting set-up, runbook, release notes | **Nothing** |
| Migration | Source profiling, field mapping, ETL, load/reconciliation across 22 stores; two rehearsals | Four stores of undeclared predecessor origin (already inside T1's hole list) and the binary-content inventory (inside T2). Not charged twice |
| Security | Security review, external penetration test, remediation | **Nothing** |
| Documentation and handover | User documentation at every surface-bearing parent, runbook, handover pack, release notes, help *editor* | Initial in-application help **content** (A2 requires it in place; editor ≠ content) → A-5 |
| Precedentedness / team learning | Nothing — rate table v0.1-h is external norms at implied nominal experience | First-in-domain team, dense obligation set, committee-governed client → G2 |
| Size-class coarseness | Sizing at class level, two repeats, 85% agreement | Three XL leaves are coarse aggregates → T3 |
| Post-production support, NFR-5 analysis | Nothing — carried unpriced by A0 decision | **Left uncorrected** (parameterless; see §4) |
| Tail / failure events | Nothing | **Left uncorrected** — another sensor's tail (see §4) |

**Partition result: satisfied.** Every category above sits in exactly one column, or is split on an explicitly named seam. Three categories required a seam, and each seam is stated rather than assumed:

- requirements work — *elaboration* carried, *post-baseline change* mine;
- non-functional work — *realisation and evidence* carried, *independent verification execution* mine;
- migration — 22 declared stores carried, 4 undeclared-origin stores mine (once, inside T1).

One soft edge I will not pretend is sharp: accessibility and performance **fixes** arising from my added verification passes fall into the estimate's defect-resolution line, which is sized per parent and not per defect source. I am charging only for verification and re-verification, not for the fixes. If the applying step wants the fix work explicit, that is a scope question for Step B, not a rate for me.

### How the coverage report moved my rates

Decisively downward, and this is the single largest effect in this run. This estimate is thorough. It carries, with priced items, seven of the categories a generic "bottom-up forgets things" correction normally charges for: integration at every parent including the root, two full test-execution and defect cycles, two UAT cycles, four environments with pipeline and promotion, migration with two rehearsals, security review with external penetration test *and* remediation, and per-parent planning with once-scoped mobilisation, status reporting and risk management.

Concretely, the report suppressed corrections I would otherwise have proposed by default:

- **no integration uplift** (would normally be ×1.05–1.15 on a structure that priced integration only at the root) — the 20% non-compounding constant is applied at 59 parents, so the category is paid;
- **no test/rework multiplier** (would normally be ×1.15–1.35 where a single test pass is priced) — two execution cycles plus two defect cycles plus regression are carried, and defect resolution is 2 892 h, 12% of the element-attached layer, which is inside published rework norms;
- **no PM/overhead uplift** (would normally be +8–15%) — planning is per parent and the once-scoped management items exist;
- **no security uplift, no environment uplift, no documentation uplift**;
- **T2 placed at the low-middle of its external range, not the top** — because the closure violations were *enumerated by the estimate's own sensors and declared*, which is evidence of a thorough sweep, and because the report states in its own words that "some may be covered in another subtree."

What the report moved **upward**: nothing generic. It created exactly five pure additions, all of them non-functional verification and content items that the report itself names as absent, plus the two targeted multipliers whose *existence* the report established by enumerating the holes. I would not have known to charge for the load test at all without it; equally, I would have charged twice for testing without it.

Net: the report converted this from a "sparse estimate" profile — which would carry two globals in the 1.25–1.40 region plus an omissions charge — into a "thorough estimate" profile with modest globals and named, bounded, itemised residuals.

---

## 3. Corrections

### Declaration (applies to the pure additions A-1…A-5 only)

1. **Unit of my additions:** **net person-hours of work on the task.** Not days. No day-to-hour conversion is embedded.
2. **Losses:** **outside** the amounts. Leave, public holidays, sickness, presence overhead and within-day overhead are *not* included in any figure I state.
3. **Roles:** stated per addition in the table.
4. **Unit relative to the estimate:** **identical.** Rate table v0.1-h is stated in net person-hours of work on the task with losses outside every row. **No conversion is required, and I supply none.** The consumer may add my amounts to the estimate's layers directly. If the consuming step later converts to calendar days or billable days, it must convert my additions and the estimate together, by the same factor.
5. **Sources' conventions and the size of their disagreement:** my external anchors for the additions come from two convention families. Consultancy and vendor scoping figures are quoted in **8-hour billable days that include within-day overhead** but exclude leave. Engineering-norm sources (COCOMO II, ISBSG-style effort reporting) are in **effort hours excluding leave** but with varying treatment of within-day overhead. The disagreement between "billable day" and "net task hour" is conventionally **10–20%**. I deflated all vendor-day-derived central figures by **15%** to land in net task hours. The low/high spread of each addition therefore carries this convention disagreement *in addition to* substantive scope uncertainty — which is one reason the ranges are wide. Two of my sources (NIST SP 800-34 Rev.1, W3C WCAG-EM) publish **scope and procedure but no effort figures at all**; for those I derived hours from the described exercise scope and marked confidence down accordingly. This is stated so the downstream reader does not mistake a derived figure for a published one.

**Which corrections the declaration governs:** A-1 through A-5 are **amounts** and carry the unit. G1, G2, T1, T2, T3 are **dimensionless factors** and need none of it.

### Corrections table

| # | Name | Blind spot addressed | Form | Low / Central / High | External source | Confidence |
|---|---|---|---|---|---|---|
| **G1** | Undiscovered scope growth | Requirements volatility after baseline; rules and protocol not yet chosen | **Global multiplier** | **×1.10 / ×1.18 / ×1.30** | Capers Jones, *Estimating Software Costs* / *Applied Software Measurement*: requirements creep ~1–2% per calendar month after requirements sign-off for large projects, 10–35% total on projects of this class; Boehm's cone of uncertainty at pre-discovery / competitive-bid stage | Medium-high on the range, medium on the placement |
| **G2** | Precedentedness, coordination and estimator optimism (**merged**) | First-in-domain team; committee-governed enterprise client; generic optimism | **Global multiplier** | **×1.08 / ×1.15 / ×1.25** | COCOMO II (Boehm et al., 2000): APEX applications-experience effort multiplier, Low = 1.10, Very Low = 1.22; PREC precedentedness scale factor, Nominal→Low adds ≈0.0124 to the effort exponent (≈5–10% at this size); TEAM/SITE cohesion factors for a single-site single team are favourable and pull the low end down | Medium |
| **T1** | Declared holes, completion | Enumerated unpriced items in the existing structure | **Targeted multiplier** on the **element-attached layer** | **repeat 1: +1.5% / +2.5% / +4.0%**<br>**repeat 2: +0.7% / +1.2% / +2.0%** | Count is external to me (coverage report: 31 items r1, 14 r2, of 1 650). Range anchored on completion-by-class-mean substitution, standard practice for declared-hole closure; upper end reflects that several hole-bearing items (A-013 reference data store, A-065 group management) are aggregates likely above item mean | **High** — the count is enumerated, only per-item size is inferred |
| **T2** | Closure violations, real share | Missing *elements*, not merely missing items | **Targeted multiplier** on the **element-attached layer** | **+5% / +9% / +15%** | Jones: requirements completeness at RFP/pre-discovery typically 75–90%; Moløkken & Jørgensen (2003) review of estimation-error studies — omitted work is the dominant contributor to bottom-up underestimation, commonly 10–20% of eventual effort. Placement inside that range set by the report's own statement that some of the ~30 flagged items are covered elsewhere ("several are not"), implying roughly 40–60% real | Medium |
| **T3** | XL coarseness | Under-decomposed leaves are systematically underestimated | **Targeted multiplier** on the **three XL leaves only** (notification engine, record import service, basic/full attribute profiles) | **×1.15 / ×1.30 / ×1.50** | Jørgensen (2004), on decomposition and estimation accuracy: coarse work items show systematic downward bias relative to decomposed equivalents; standard three-point/PERT practice for un-decomposed aggregates | Medium-low. Note: 3 leaves of 187 — the total effect is small whatever the applying step chooses |
| **A-1** | Load and performance test vs NFR-14 | Non-functional verification, named hole | **Pure addition** | **180 / 320 / 560 net person-hours** | Industry performance-engineering engagement norms for a multi-module B2B application at production-like volume (500k prefixes / 10M GIN / 550k LN, five response-time targets at stated concurrency): scenario design, script build for key journeys, data seeding, two execution rounds, analysis, one retest after tuning. Vendor-day figures deflated 15% | Medium |
| **A-2** | Failover test execution + backup/DR rehearsal | Non-functional verification, named hole | **Pure addition** | **90 / 160 / 280 net person-hours** | NIST SP 800-34 Rev.1, contingency-plan testing and exercise guidance (functional exercise scope; **publishes procedure, not effort** — hours derived from described scope). Two exercises against the 99.9%-with-tested-failover obligation | Medium-low |
| **A-3** | WCAG 2.0 A conformance evaluation + re-verification | Non-functional verification; realisation carried, verification not | **Pure addition** | **120 / 200 / 340 net person-hours** | W3C WCAG-EM sampled-evaluation methodology (**publishes method, not effort**); vendor accessibility-audit scoping conventions of 40–120 h per sampled evaluation, scaled for three modules + admin + public anonymous tier, plus one re-verification pass. **Excludes remediation coding** — that sits in the estimate's defect-resolution line | Medium-low |
| **A-4** | Cross-browser verification matrix | Non-functional verification, named hole | **Pure addition** | **70 / 130 / 220 net person-hours** | Standard compatibility-matrix test practice: one full pass plus one regression pass across the surface set for IE9+ and current browsers. Vendor-day derived, deflated 15% | Medium |
| **A-5** | Initial in-application help content | Documentation residual — editor priced, content absent; A2 requires it in place | **Pure addition** | **90 / 160 / 280 net person-hours** | Technical-writing productivity norms (topic-based authoring, ~2–4 net hours per help topic including SME review) applied to three modules plus administration. **Scoped to in-app help only** — training materials are excluded by the RFP | Medium |

**Global-multiplier count: 2.** Compounded, G1×G2 spans **×1.19 (low·low) to ×1.63 (high·high)**, central **×1.36**. I state this only so the applying step sees the compounding it is committing to; it is a factor range, not a total. Generic optimism bias was **merged into G2**, not added as a third global, per the merge rule — it overlaps both precedentedness and creep, and charging it separately is exactly the failure mode the two-global cap exists to prevent. This is also why G1's central sits mid-range rather than at the top of the published creep band.

**Roles covered by the additions:** A-1 performance engineer, plus developer and infrastructure support. A-2 infrastructure/operations engineer, developer, test lead. A-3 accessibility-competent tester, plus front-end developer for verification only. A-4 tester. A-5 technical writer plus SME review time.

---

## 4. Deliberately uncorrected

1. **Post-production support period and transition service (A0).** Term and service level are unstated. A rate requires a base; there is none. This is a scope resolution for Step B, not a calibration parameter. I emit nothing for it — and specifically, I did **not** smuggle it into G1.
2. **NFR-5 impact analysis (A0, count 0).** Read as no deviation. If that reading changes, this returns as an addition, not as a multiplier.
3. **Tail and failure events.** The identity protocol being chosen late or changed mid-flight; the client failing to define I-7 business rules at all; committee stalemate on approval; predecessor migration data proving structurally unusable; loss of the competitive bid. None of these is a multiplier on anything — they are discrete branches with their own probabilities. **Another sensor's tail.** G1 covers ordinary creep, not scenario failure, and the two must not be conflated.
4. **The 15% class disagreement between repeats.** That is dispersion, not bias. It belongs to whatever step propagates spread, not to a central-value correction. I made no attempt to convert it into a rate.
5. **Era adjustment (A19).** The RFP is 2018, the norms are modern. I can defend no direction — tooling productivity has risen, but so have browser-matrix, accessibility and security expectations. No sourced index, so no correction. Flagged, not priced.
6. **The 20% non-compounding integration constant itself.** I do not second-guess the method's own constant. Adjusting it would be a third global effect by another name.
7. **The rate table's own uncalibrated status (v0.1-h, "uncalibrated against any outcome").** Whether the per-item rates are right is a question about the rate table, not about this estimate's structure. Correcting it here would require a global multiplier I cannot source, and I have spent both globals on effects I can.
8. **Losses, calendar and duration.** My unit is net task hours throughout. Any conversion to elapsed time or billable capacity is downstream and not mine.

---

## 5. Order of application

Apply in exactly this sequence. The applying step has no freedom to reorder.

1. **T1** — apply to the **element-attached layer** of the repeat in use (24 163 r1 / 24 221 r2), using the repeat-specific rate. Repeat 1 and repeat 2 take **different** T1 rates; do not average them before applying.
2. **T2** — apply to the **element-attached layer**, same base as step 1. T1 and T2 are both computed against the *original* element-attached figure, not against each other's output — they are disjoint item sets and must not compound.
3. **T3** — apply to the element-attached effort of the **three XL leaves only**. If that subset's effort is not separable, the applying step must say so and skip T3 rather than approximate it against the whole layer.
4. **Integration on the increments.** Apply the method's **own** 20% non-compounding constant to the sum of the T1+T2+T3 increments. Added items sit under parents like every other item and must carry integration exactly as the structure carries it. Do not apply my own factor here — use the structure's constant, unchanged.
5. **Structural subtotal** = estimate total + (T1+T2+T3 increments) + their integration from step 4. *I do not compute this and express no opinion on it.*
6. **Additions A-1…A-5** — add flat. These are once-scoped and environment-level items of the same family as the estimate's 840-hour once-scoped layer, which takes no integration. **They do not take the 20% constant.** (Sanity note for the applying step, not a target: my central additions sum to roughly the same magnitude as that existing once-scoped layer, which is the scale one should expect for five once-scoped verification and content items.)
7. **G2** — apply to the result of step 6. Precedentedness and coordination friction act on all work the team performs, including the added verification passes.
8. **G1** — apply last, to the G2-adjusted figure. Scope growth is growth in the body of work as it will actually be executed, i.e. at the team's real productivity, so it sits outside G2. The product is order-independent, but the order is fixed anyway to remove discretion.

Steps 7 and 8 are the only compounding in this parameter set. Everything else is additive by construction.
