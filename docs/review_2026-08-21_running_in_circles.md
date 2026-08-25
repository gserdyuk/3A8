# Review — 2026-08-21 — the circle is real, it has a mechanism, and the exit is one step away

**Requested by the author**: a general critique of the last months' work (runs 1–22, both generations),
recommendations, and fixes — after the author's own impression that "we are running in circles, and
even the attempt to break out (product model, work model) did not help."

**Written from the record only.** Every figure below is from the repository; sources are named per row.
Facts (§1) are separated from the diagnosis (§2–§6) and the diagnosis from the recommendations (§7),
so each can be disagreed with independently. House discipline applies to this document too: what would
overturn each claim is stated where it can be.

The verdict up front, in three sentences. **The impression is correct: the project has been optimising
run-to-run agreement of a single sensor for six weeks, and that programme has reached its floor — the
remaining spread does not shrink because rules only choose *which variable carries it*.** The Hotyn
generation did not fail: it stabilised everything except the one thing no rule was ever pointed at —
the magnitude scale, which is still sampled from the model's prior on every run. Pinning that last
variable (a rate table), restoring the second sensor (reference class has not run since 2026-08-05),
and putting validity ahead of further precision closes the circle with machinery that already exists.

---

## 1. The evidence, assembled

Nothing here is new; the contribution is putting the rows side by side.

| # | fact | value | source |
|---|---|---|---|
| E1 | Baseline, **no method at all**, Opus | mean 1074, **CV 8.55%** | run14 |
| E2 | Best-ever method CV (one batch, not significant vs E1) | 6.23% | run17 axis S; facts pack §2.6 |
| E3 | Typical method CV across 7 engine versions | 9–17% | facts pack §1 |
| E4 | Only spread difference in project history that clears significance | a **model** difference | facts pack §2.6 |
| E5 | Model gap without method → with method | ×1.409 → **×2.021** (t=14.70) | run16 |
| E6 | Version steps on the level vs the model effect | +0.4…+30% vs **×2.02** | facts pack §4.5 |
| E7 | Lytin output law | ΣE ≈ 10.38 pd × leaf count, ±8.9% | run17 §4b |
| E8 | Leaf **size** across models · leaf **count** across models | ×1.01–1.07 · ×1.87–1.97 | run17 §4a |
| E9 | Every pinned scalar across models (price/leaf, C3 share, multiplier) | within **3%** | facts pack §2.2 |
| E10 | Relocation 1: C1 pinned leaf size → | leaf count went free, ×1.97 | run16 |
| E11 | Relocation 2: M9 closure pinned leaf count → | within-element granularity, ×1.21 | run18 §3b |
| E12 | Relocation 3: M2 v1.1 pinned declaration depth → | parts per obligation ×1.42, anchored ×1.56 | run19 |
| E13 | Relocation 4: chain pinned item count (×1.005) → | **price per leaf ×1.288**, uniform (sd 0.105) | run22 |
| E14 | Step agreements, identical inputs | step 1 **J 0.308** / step 2 **J 0.969** / step 3 ΣE ×1.288 | runs 19, 21, 22 |
| E15 | Outcome comparisons in the Lytin+Hotyn era (runs 6–22, ~130 runs) | **zero** | BACKLOG "Next — validity" |
| E16 | The one pipeline-vs-fact encounter ever | FaxRxTx, **×4.2 overshoot**, 2026-08-05 | findings §12a |
| E17 | Level history, same RFP | 486 (manual) → 1074 (baseline) → 1626 (D4.0) → 890–1147 for **27 of 68 obligations** (Hotyn partial) | findings §9; runs 14, 16, 22 |
| E18 | Work projecting onto no obligation | 37% of items; 27–39% of effort | run20 §3; run22 raw |
| E19 | Reverse audit (work that traces to nothing) | designed, **never run** | BACKLOG mechanism B |
| E20 | Input ambiguity | 19/73 requirements flagged; excluding them: J 0.277→0.362 | run18 §3d |
| E21 | Completion spread between models · between repeats | ×4.56 · ×1.10 | run18; run19 |
| E22 | Convergent product-model gap findings | 6 runs, 2 instruments, same 7 gaps | run21; run22 §4 |
| E23 | Reference class sensor last ran | 2026-08-05 (FaxRxTx); **never in the Hotyn era** | findings §12a; absence since |
| E24 | Steps B–D (diagnosis, calibration, final range) last ran | 2026-08-05; never on BMS with any Hotyn artifact | same |

---

## 2. Diagnosis 1 — the circle's mechanism: variance is conserved, rules only relocate it

The project has already named this — *"the freedom relocates rather than disappearing"* (session
record R2) — and measured it four times (E10–E13). What the record has not yet said is **why it must
relocate**, and the why is what makes further rule-writing unprofitable:

Every rule so far constrains the **form** of the output — leaf size, coverage location, item
provenance, split conservation. The **magnitude** — "how much work is this?" — is at no point attached
to anything outside the run. Each run therefore samples its scale from the model's prior, and that
sample expresses itself through whichever output variable the rules left free. Pin the count and the
scale surfaces as price per leaf (E13); pin the price (Lytin's emergent 10.4 pd/leaf habit, E7) and it
surfaces as count (E8). The total is always `(a structure size) × (a sampled scale)`, and constraining
one factor moves the variance into the other. **The spread cannot fall below the spread of the sampled
scale, and the baseline measured exactly that floor: CV 8.55% with no method at all (E1), which no
engine version has significantly beaten (E2–E4).**

The rules were not useless — each one binds precisely what it names (co-location amount ×8.7→×1.07,
step 2 to 0.969, item count to ×1.005; E12–E14). That is the strongest argument *for* the programme's
method and *against* its target: **binding works every time it is aimed at a named variable, and the
one variable never aimed at is the scale itself.** Followed honestly to its end, the pinning programme
terminates in a design where the model contributes no numbers at all. The circle is the refusal to
take that last step. §7.2 takes it.

*Overturned by:* any future rule that reduces end-to-end ΣE spread materially below the methodless
baseline without externalising the scale. Four generations of rules have not.

## 3. Diagnosis 2 — precision is being optimised; validity has never been measured, and the gate guarantees the loop

The §12d gate — *repeatability first, then a regression set, then "robust"* — reads as discipline and
functions as an infinite loop: its first stage cannot be passed by rule-writing, because the
repeatability floor belongs to the model (E1–E4), not to the method. A gate whose first stage is
unpassable makes the second stage unreachable — which is the observed history: the regression set
(several cases end-to-end) has never happened; everything since run 6 is one case, BMS, which has no
outcome and can never say which level is right.

Meanwhile the level — the one quantity a client pays for — has drifted freely: 486 → 1074 → 1626 →
a Hotyn partial figure that extrapolates well above Lytin (E17). Each step was locally defensible
("more thorough"); the composition is unbounded, because the design ratchets upward: accretion and
completion only add, the crossing multiplies, C1 only splits, the floor rounds up, nothing may ever be
removed — and the instrument that would check the other direction (the reverse audit, E19) was
designed and never run, while 27–39% of priced effort projects onto no obligation, legally and
uninspected (E18). **A pipeline that is forbidden to under-count and never audited for over-counting
will drift upward forever, and no repeatability measurement can see it** — both runs drift together.

The only encounter with a fact ended ×4.2 off with every internal metric green (E16): *"the estimate
failed; the reporting did not."* That sentence should have redirected the project; instead the next
fourteen run-series measured agreement on a case where failure is unobservable.

*Overturned by:* nothing inside BMS. Only outcome comparisons can overturn or confirm a level.

## 4. Diagnosis 3 — the founding methodology was abandoned without a decision

METHODOLOGY.md defines the product: several sensors with decorrelated blind spots, a diagnosed
divergence, mechanical calibration, and **"a range with an explanation of the sources of uncertainty,
not a single number."** Since run 6, one sensor has been measured against itself; the reference-class
sensor has not run since 2026-08-05 and has never seen a Hotyn artifact; Steps B–D have never run in
this era (E23–E24). No center/corridor/reserve answer has ever been produced for BMS.

The drift is subtle and total: spread stopped being the **signal** (the honest width to be decomposed
and reported) and became a **defect** (something rules must remove). The founding documents say the
opposite — findings §6: the unexplained residual "is an honest measure of uncertainty, not noise to be
averaged away." Two runs of one sensor disagreeing ×1.29 is not primarily a calibration emergency; it
is a *component of the answer's width*, and the machinery for saying so (Steps B–D) exists, tested,
idle.

*Overturned by:* pointing at a Hotyn-era artifact where divergence between sensors was diagnosed
rather than suppressed. I could not find one.

## 5. Diagnosis 4 — the test bench cannot distinguish defect from honesty

BMS is one training RFP, no outcome, 19/73 requirements ambiguous (E20), with live contradictions
(R29 vs R38 — both estimator runs called it their largest basis risk). On such input, some part of the
step-1 disagreement is the honest width of the posterior over an under-determined document — two human
architects given the same list would also produce different trees, and **nobody has measured what
Jaccard two competent humans achieve on this list.** Without that control, "0.308 is low" is a
stipulation, not a finding. The project has measured the ambiguity *component* (E20) and correctly
declined to call it the explanation — but the remaining gap between 0.36 and the registered 0.9 has
two readings (instrument defect / legitimate design multiplicity), and no experiment on the books
separates them. Three relocations of the same freedom (E10–E13) are evidence for the second reading.

*Overturned by:* a human pair achieving J ≳ 0.7 under the same rules — that would relocate the blame
back onto the instrument.

## 6. Diagnosis 5 — what Hotyn actually built (and it is the way out)

Read the three steps against E9/E13/E14 and the pattern is exact:

> **Everywhere a number comes from a rule or a table, two runs agree to ~1. Everywhere a magnitude is
> sampled from the model, two runs differ ×1.3–2. Scalars transfer across models within 3%; sampled
> magnitudes do not.**

Step 2 is almost a function (0.969; every difference is one of three named classification calls).
Step 3 with the count pinned shows the disagreement as a **uniform level** — ratios 1.13–1.46,
sd 0.105, no outlier — the correctable kind, the shape of a missing constant. And the crossing
produces something no previous instrument had: a **reproducible size vector** — counted work items by
(element class × activity), traceable to requirements — a modern function-point analogue derived
straight from the RFP, with the coverage matrix and gap list attached (E22). Its unit price is the
only thing still sampled.

So the honest description is: **Hotyn did not fail to stabilise the estimator; it succeeded in
building a size-measurement instrument that lacks a price list.** The missing half is the parametric
method — which METHODOLOGY §2 has listed from the beginning, scheduled for Phase 2. The chain arrived
at Phase 2's doorstep and stopped, and the stopping looks like a circle.

A second genuine asset, named as such: across six runs and two instruments, the pipeline converged on
the same seven holes in the product model, plus the closure-violation and open-question lists
(E18, E22). **The pipeline is demonstrably better at finding missing scope and unaskable questions
than at producing numbers.** For the presale use case that list is half the value of the deliverable,
and no Lytin artifact ever produced it.

---

## 7. Recommendations, in order

**7.1 — Give the project an exit condition.** Nothing can finish while no target exists. Proposed
default, to be argued and then pinned: *on ≥4 cases with known outcomes, the calibrated P50 lands
within ×1.3 of actual on at least 3, and the reported P10–P90 covers actual on at least 3.* The
numbers are the author's to set; the requirement is that they exist and replace §12d's unpassable
stage 1. Repeatability becomes a budget line inside the reported range, not a gate.

**7.2 — Pin the last free variable: numbers from a table, judgements choose rows.**
`docs/proposal_rate_card.md` (written today) specifies it: `Hotyn-D 2.0` classifies each work item
(size class from countable drivers) and prices nothing; a pinned, versioned **rate table** — drafted
gap-blind, calibrated only against outcomes — supplies O/M/P per (activity × class × size class); a
script does the arithmetic. Registered predictions there: repeat-run ΣE ratio falls ×1.288 → ≤×1.05;
the cross-model gap on ΣE, ×2 throughout Lytin, collapses to the classification disagreement
(measured 74/77). This is not "dissolving a sensor" (§11.5's warning): it is naming the two sensors
that were braided inside Hotyn-D — a size measurer (already reproducible) and a rate holder (never
calibrated) — and giving the second its honest, calibratable form.

**7.3 — Produce the BMS deliverable the methodology promised.** Un-defer the whole-project estimate
(BACKLOG item), but deliver it in the METHODOLOGY format, which has never been done: center from the
table-priced work model · structure component from carrying **both** run-19 models through steps 2–3
(the ×1.65 stops being a scandal and becomes a stated width) · reserve from the reference-class tail ·
plus the unpriced-scope list (closure violations, E22) and the open-questions register. This requires
the reference-class sensor's first Hotyn-era run and the first Steps B–D of the era — all built, all
idle.

**7.4 — Validity, with the case that has a fact.** FaxRxTx end-to-end through Hotyn against FACT.md —
raw first, then calibrate, in that order (BACKLOG already states why). One case is a gross-error gate,
not a calibration set; it would have caught ×4.2. In parallel: acquire 3–5 documented outcomes (the
colleague, own history, published datasets as a stopgap for table priors). This is the only work that
can move the project's actual risk.

**7.5 — The human control on step 1.** One afternoon of the colleague's time: same 68 obligations,
same rules, build the model by hand. Measure human–human (if two are available) and human–machine
agreement with the registered metric. This prices the achievable ceiling for step 1 and decides
Diagnosis 4's open reading — cheaper than any further metric work.

**7.6 — Run the reverse audit once** on the final work model (mechanism B, already designed): findings
with citations, checking the 27–39% no-obligation share in the only direction the only-adds design
cannot see. One run, and the upward ratchet gets its first brake shoe.

**7.7 — Stop-list.** No new structural-agreement metrics for step 1 (three exist, all with known
failure modes; the next one will too). No new rules aimed at binding part-count or completion until
7.5 reports (three relocations are enough). No further Lytin work — C7 and the axis remainders in
BACKLOG are a closed generation's open tickets; close them as *superseded by Hotyn* rather than
leaving them to look like debts. No cross-model conversion constants as deliverables (the withdrawal
of 0.4896 was right; keep it withdrawn). Sonnet stays what the record shows it is — a diagnostic
tier, not a second reading of truth.

---

## 8. What this review does not claim

- **Not that the discipline was wasted.** The registration-before-measurement habit, raw preservation,
  corrections-on-the-record, and the twice-tested isolation layer are what made this diagnosis
  possible from documents alone. The same discipline pointed at validity would be rare in the field.
- **Not that J = 0.308 is fine** — that its meaning is undecidable without 7.5, and that the treatment
  of whatever part is real is propagation into the answer's width, not elimination by rule.
- **Not that the rate table buys truth.** It buys that the remaining spread lands in nameable,
  separately-improvable places: the table (calibrated on outcomes), the classification (measured,
  ~4% disagreement), the structure ensemble (reported as width), the class tail (owned by the
  reference sensor, as always). Truth still costs outcomes, which is why 7.4 outranks everything
  except 7.1.

Almost every ingredient above already exists somewhere in the project's own record — R2 names the
relocation, BACKLOG names the validity void, §11.5 names the parametric boundary, §12a names the
green-dashboard failure. What was missing was the assembly, and the willingness to conclude: **the
variance programme is complete. It ends by externalising the scale, not by another rule.**
