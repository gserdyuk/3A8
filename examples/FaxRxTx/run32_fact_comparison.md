# Run 32 — FaxRxTx against fact: the raw comparison, the one calibration, the score

**2026-08-22.** Steps (d), (e) and (f) of the stage-3 plan. `FACT.md` was opened **after**
`run31_whole_model_assembly.md` was written and closed; the assembly document says so in its own first
paragraph and that is the check. No sensor in the chain ever saw the fact, and no parameter used to
produce the number was chosen while looking at it.

---

> **Superseded on one point, 2026-08-23 — see `run33_unit_of_the_fact.md`.** The fact's owner
> has since stated that the ~120 person-months is **staffed headcount x calendar**, and that this
> organisation's standing conversion from staffed presence to delivered work is 6/8. Restated in
> the estimate's unit the fact is **90 pm**, the miss is **x1.30** rather than x1.735, and `L-1`
> is **withdrawn**. Everything below is what was measured against the fact as stated, and stands
> as that record. Readings R10 and R11 in this document and in the session record are overturned
> and amended respectively.


## 1. The fact

**~120 person-months** — a team of about ten people including QA and PM, for about a year, 2007–2009.
Source: a participant's memory recorded 2026-07-17, no documentary sources, stated accuracy **±20%**,
so the honest window is **96–144 pm**.

The softness of the fact is a fact about the fact and it bounds every claim below. It does not,
however, rescue a miss larger than itself.

## 2. The raw comparison

| | pd | pm | against 120 |
|---|---:|---:|---|
| **Hotyn chain centre** (mean of the two classification repeats) | 1452.5 | **69.2** | **×0.58 — the fact is ×1.735 higher** |
| repeat 1 | 1475.4 | 70.3 | ×1.71 |
| repeat 2 | 1429.7 | 68.1 | ×1.76 |
| ΣO … ΣP, the honest extreme band | 639 … 2738 | 30.4 … 130.4 | **contains the fact**, at ~0.90 of the band's width |
| the fact's own window | 2016 … 3024 | 96 … 144 | the centre sits **below** the whole window |

**The chain under-estimates FaxRxTx by ×1.735.** The undershoot is larger than the fact's own ±20%
uncertainty by a wide margin: even taking the most favourable edge of the memory (96 pm), the miss is
×1.39.

## 3. The comparison that matters more — three generations on one project

FaxRxTx has now been estimated four times, by three different instruments, against one fact.

| date | instrument | bottom-up centre | against 120 | reference class P50 | against 120 |
|---|---|---:|---|---:|---|
| 2026-07-17 | Lytin-era, manual | **111.6 pm** | **×0.93 — passes ×1.3** | 160 pm | ×1.33 |
| 2026-07-17 | same, calibrated | 155 pm | ×1.29 — passes, just | — | — |
| 2026-08-05 | Lytin agent pipeline | **237.8 pm** | ×1.98 | 135 pm | **×1.13 — passes** |
| 2026-08-05 | same, calibrated | **503 pm** | **×4.19** | — | — |
| **2026-08-22** | **Hotyn chain** (this run) | **69.2 pm** | **×0.58** | not run on this case | — |

Three readings fall out of that table, and the third is the uncomfortable one.

**R9 — the bottom-up centre has swung ×3.4 across three generations of one method on one unchanged
project: 111.6 → 237.8 → 69.2.** The project did not change. The obligation list, the assumptions and
the fact did not change. What changed each time was how the instrument decomposes, and the answer moved
by more than a factor of three. *Overturned by:* showing that the three runs priced materially different
scopes — they did not; all three ran against `SYSTEM.md` §6 and the same assumption log.

**R10 — the reference class has been the closest instrument to the fact, twice, and it is the
instrument this project has invested least in.** ×1.33 and ×1.13, against the bottom-up's ×0.93, ×1.98,
×4.19 and ×0.58. One of the reference class's two readings passes the ×1.3 gate outright and the other
misses it by 0.03. *Overturned by:* a second outcome case where the class misses and the bottom-up
hits.

**R11 — every generation removed a degree of freedom, and the error did not shrink; it changed sign.**
Lytin-era judgement pricing overshot ×2 and, once calibrated, ×4.2. The Hotyn chain — model first, work
second, size classes third, prices in a pinned table no sensor ever sees — undershoots ×1.7. The
project's law of the record (R1: *everything priced from a table agrees*) is intact and was confirmed
again today (repeat spread ×1.032). **Agreement between runs went up and accuracy against the fact did
not.** *Overturned by:* three further outcome cases on which the tabled chain lands inside ×1.3.

R11 is the sharpest thing this session produced and it deserves to be stated without softening: the
variance programme succeeded on its own terms and the accuracy question turns out to be a different
question. `docs/review_2026-08-21_running_in_circles.md` argued that the magnitude was still being
sampled while the form was pinned. The magnitude is now pinned too — and it is pinned in the wrong
place.

## 4. Where the ×1.735 is, and where it is not

Four candidate explanations were named **before** the fact was opened (`run31…assembly.md` §4–§5).
Each is now sized against the gap of **1067.5 pd** (2520 − 1452.5).

| candidate | what it would be worth | share of the gap |
|---|---:|---|
| **R8 — the total is element count × a constant** | to reach 2520 pd at this model's 15.0 pd/element you need ~168 elements, not 97 | **could carry all of it** |
| **the vintage** — modern norms applied to a 2007–2009 stack with no cloud, no broker, no orchestrator, everything hand-built | unquantified; a ×1.7 level effect on construction alone would carry the gap | **could carry all of it** |
| the four visible scope decisions (`SA-NONE`, `C-DIRECT`, `G-SEED`, `U-OPS-USER`) | switching all four the other way: roughly +140 pd | ~13% |
| the six named holes plus the defect-fixing hole | pricing the unpriced elements at the model's own mean: roughly +90 pd | ~8% |

**The two candidates that could each carry the whole gap are not separable at n = 1**, and a single
global level factor absorbs both without distinguishing them. That is the honest statement of what
today's calibration is and is not.

**They are separable by a cheap experiment, and it is worth naming precisely because it is cheap.**
Re-run `Hotyn-M` on the same pinned list with a granularity instruction that produces roughly 160–170
elements, and cross, size and price it with **no rate changed**. If the total tracks element count
towards ~2500 pd, the instrument is measuring the modelling act and the rate table's level is not the
problem. If it does not, the level is. Two supporting points already exist and both are consistent with
the linear reading: BMS at 78 elements → 17.3 pd/element, FaxRxTx at 97 → 15.0 pd/element, two very
different projects landing 7.7% apart in total.

## 5. Step (e) — the one permitted calibration

The plan allows exactly one act here at n = 1: **a single global level factor**, and nothing else. No
rate row is touched. No driver is re-read. No scope decision is revisited.

> **`L-1` = ×1.735**, from `120 pm ÷ 69.2 pm`.
> Fitted on FaxRxTx, 2026-08-22, n = 1, against a fact of stated accuracy ±20%.
> Applied, the chain's FaxRxTx centre becomes 120 pm by construction, which is not evidence of
> anything.

Three conditions bind it, and they are the reason it can be written down at all:

1. **It may never be scored against FaxRxTx.** `docs/exit_criterion.md` §3: no parameter may be
   evaluated against the case it was fitted on. FaxRxTx is now **spent** as evidence for the calibrated
   chain, and remains valid evidence only for the uncalibrated one.
2. **It is a level factor, not an explanation.** It conflates at least the two candidates in §4 that
   could each carry the whole gap. If the granularity experiment shows the element count carries it,
   `L-1` must be **withdrawn**, not re-fitted — a factor that corrects for a modelling artefact would
   double-count the moment the modelling changed.
3. **It does not enter `docs/rate_table.md`.** The table's own calibration rule forbids editing a row
   while looking at a gap the edit would explain. `L-1` is recorded here, as a chain-level parameter
   with its provenance, and the table stays at v0.1.

## 6. Step (f) — the score against `docs/exit_criterion.md` v1.0

The gate requires **at least 4 outcome cases**. We have **one**. What follows is therefore the
gross-error reading the criterion itself describes as its n < 4 use, not the gate.

| test | threshold | this case | verdict |
|---|---|---|---|
| **1 · centre** | calibrated P50 within `[actual ÷ 1.3, actual × 1.3]` = **92.3 … 156 pm** | **69.2 pm** | **FAIL.** Outside on the low side by ×1.34 beyond the gate; ×1.735 from the fact |
| **2 · corridor** | declared P10–P90 contains the actual | the chain declares **no P10–P90**. Its only band is ΣO…ΣP = 30.4 … 130.4 pm, which does contain 120 | **NOT SCOREABLE.** See below |
| **3 · provenance** | no parameter fitted on the case it is evaluated against | none was: the number in §2 was fixed before `FACT.md` was opened | **PASS** |

**On test 2, stated plainly rather than claimed as a pass.** ΣO…ΣP is the sum of every row's optimistic
value and every row's pessimistic value — it assumes perfect correlation across ~580 items and is not
a probabilistic interval of any kind. It spans ×4.3 from floor to ceiling. An interval that wide
"containing" the fact says nothing, and calling it a pass would be exactly the false convergence the
run-27 diagnosis refused in three frames. **The honest finding is that the Hotyn chain has no corridor
instrument at all** — it produces a centre and a non-percentile band, and the exit criterion's second
test cannot be applied to it until one exists. That is a gap in the method, discovered by trying to
score it.

**Overall verdict at n = 1: the instrument fails its centre test on the only case with a documented
outcome.** It is not the ×4 gross error the criterion was written to catch — the August 2026 pipeline
was that — but ×1.735 is a decisive miss against a ×1.3 gate, and it is a miss in the opposite
direction from every previous failure.

## 7. What this changes, and what it does not

**Does not change.** The rate-card design and the classifier/table split are vindicated on their own
claim: two independent classification repeats over 79 elements priced to **×1.032**, and the law of the
record (R1) holds. Nothing here argues for going back to judgement pricing — that generation's error on
this same project was ×4.2.

**Changes.** The project's binding question is no longer variance. It is **level**, and level has two
candidate homes — the granularity of the product model and the vintage of the rate table — which n = 1
cannot separate. The next work is not another sensor and not another rule; it is the granularity
experiment of §4, which costs one `Hotyn-M` run plus one crossing plus one sizing pass and settles
which of the two it is.

**Registered before it can be rationalised:** if the granularity experiment shows the total tracking
element count, then **the estimate is a function of how finely somebody chose to draw the model**, and
no amount of case law inside the sizing step touches that. The instrument would then need an anchor
that element count cannot move — and the only candidate the project has produced that behaves that way
is the reference class (R10).
