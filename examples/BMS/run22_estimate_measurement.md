# BMS — Run 22: two estimates of one work model, `Hotyn-D 1.0`

Date: 2026-08-20. **Registered before the runs returned.**

## What this measures

The third step, and the first person-days this generation has produced. Two runs of `Hotyn-D 1.0` on
**one work model** — batch B of run 21, 197 items over 27 product elements.

**Batch B was chosen because its two crossings came out identical, item for item.** The work model is
therefore unambiguous: whatever these two estimates disagree about is the estimator's own spread, with
no inheritance from step 2 mixed in.

This is a **partial estimate**: six subtrees of a 78-element product, with every whole-project activity
— test strategy, mobilisation, environments, cutover, release notes, penetration test, acceptance
sign-off — deliberately outside the work model. **It is not a project total and must never be quoted as
one.**

## One deliberate omission from the input, and why

The assumption log names a team: one PM/BA, a part-time architect, three to four developers, one QA, a
part-time DevOps. **The estimator was not given it.** Effort in person-days does not depend on how many
people there are — headcount decides the calendar, and the calendar is not this step. What the
estimator was given is the grade: a competent engineer, predominantly senior or middle, in an
enterprise context.

This also keeps the sensor's own contamination rule satisfiable: its definition tells it to stop if the
input contains a team size, and it should not have to make an exception for the one it needs.

## The similarity measure for step 3

Step 1 is compared on requirement co-location, step 2 on the set of (element, activity) pairs. Here the
items are identical by construction, so the comparison is about magnitude, and it is reported in the
same frame as the other two:

| # | measure | what it says |
|---|---|---|
| 1 | **ΣE ratio** | the headline: how far apart two estimates of the same work land |
| 2 | **effort per requirement**, over the 27 obligations in scope | the projection that survives a change of tree, and the frame in which all three steps are comparable |
| 3 | **per-item spread** | where the disagreement is concentrated — a few large items, or everywhere |
| 4 | **C1 firing rate and the count of items floored at 1 pd** | readings on the work model's granularity, not on the estimator |
| 5 | **the closure-violation list** | what each run judged necessary and refused to price |

## Registered expectations

1. **ΣE agrees within ×1.25.** For reference from the previous generation, on different instruments and
   a different chain: two decomposers on one shared model gave ×1.344, and free decomposition gave
   ×2.05. Two estimators on one *fixed item list* should do better than either, because neither the
   count of items nor their content is theirs to choose. **Above ×1.5 would mean the estimator is the
   dominant source of spread in the whole chain, and steps 1 and 2 have been polishing the wrong thing.**
2. **Fewer than 5 of the 27 requirements differ by more than ×1.5** in effort per requirement. A tight
   total with a scattered profile is a different animal from a tight total with a matching profile, and
   only the projection tells them apart.
3. **C1 fires on fewer than 10% of items.** These items are per-element activities on a fine product
   model; almost none should exceed 10 person-days. If C1 fires often, the reading is on the work model.
4. **More than 20% of items are floored at 1 person-day.** The catalogue registered this risk before the
   crossing existed: per-element activities on a fine model produce items honestly worth a fraction of a
   day, and C1's floor rounds every one of them up. If the floored share is large, **the floor is
   inflating the total** and that is a defect in `Hotyn-D`, not in the model. This is the one
   expectation registered in the direction of failure.
5. **The closure-violation lists are non-empty and name the whole-project activities.** A run that
   prices test strategy or environment set-up out of its own head has invented work, which is the
   failure the whole chain exists to prevent. A run that names them and declines is working correctly.
6. **Integration (C3) lands between 15% and 20% of the total.** It is 20% of leaf effort beneath each
   parent by rule, so the only freedom is which elements are parents — already fixed by the model.

## Isolation

Both runs went through the real `work-estimator` definition (`tools: Glob`). Identical prompts, no
shared context, launched together, neither told of the other, and neither shown any prior estimate,
budget, duration or reference figure.

---

# Results

Both runs returned with `tool_uses: 0`, through the real sensor definition. Raw in
`run22_raw/HD22-B1.md` and `HD22-B2.md`; the comparison is `run22_raw/compare_run22.py`.

## 1. The readings

| | repeat 1 | repeat 2 | ratio |
|---|---:|---:|---:|
| items priced | 197 | 197 | — |
| **leaves after C1** | **209** | **208** | **×1.005** |
| ΣE of leaves | 955.47 | 741.75 | ×1.288 |
| ΣE of integration | 191.09 | 148.34 | ×1.288 |
| **ΣE total** | **1146.56 pd** | **890.09 pd** | **×1.288** |
| integration share | 16.67% | 16.67% | — |
| **person-days per leaf** | **4.57** | **3.57** | **×1.282** |
| C1 split rate | 3.0% | 2.54% | — |
| items floored at 1 pd | 0 | 0 | — |
| closure violations | 7 | 8 | — |

## 2. Scoring

| # | expectation | outcome |
|---|---|---|
| 1 | ΣE within ×1.25 | **NOT CONFIRMED, narrowly**: ×1.288. Far from the ×1.5 that would have meant the estimator dominates the chain |
| 2 | fewer than 5 of 27 requirements differ by more than ×1.5 | **CONFIRMED, by a wide margin: zero.** The ratios run 1.13 to 1.46, mean 1.276, standard deviation 0.105 |
| 3 | C1 fires on under 10% of items | **CONFIRMED**: 3.0% and 2.54% |
| 4 | more than 20% of items floored at 1 pd — registered as a predicted failure | **REFUTED, and this is good news**: zero in both. The smallest leaves are 1.67 and 1.17 pd. The catalogue's registered worry — that per-element activities on a fine model would produce fractional-day items the floor rounds up — did not materialise |
| 5 | closure lists non-empty | **CONFIRMED**, and §4 is why they matter |
| 6 | integration between 15% and 20% | **CONFIRMED**: exactly 16.67% in both, which is 0.20 / 1.20 — arithmetic, since no parent nests inside another |

## 3. The gap is a level, not a shape — and that inverts the previous generation

**Leaf count agrees to ×1.005. Price per leaf differs by ×1.282.** The entire disagreement is the size
put on each piece; neither run disagreed about how many pieces there are, because that was no longer
theirs to choose.

Under `Lytin` the arrangement was exactly the other way round. Run 17 measured leaf **count** varying
×1.87–1.97 between models while leaf **price** held to ×1.01–1.07 across three instruments. The author's
reading at the time was that price per leaf is a derived quantity rather than a constant of the method —
a leaf is a unit of generation, not a share of a whole. Run 22 is that reading tested from the other
side: **with the count pinned by the chain, the price per leaf carries the whole gap.** The stability of
about 10.4 pd per leaf under Lytin was a property of how those runs decomposed, not a property of leaves.

**And the difference is very nearly a constant factor.** Across all 27 obligations the ratio between the
two estimates stays between ×1.13 and ×1.46, mean ×1.276, standard deviation 0.105 — no requirement is
an outlier, and the two estimates have the same profile at two levels. A tight total with a scattered
profile would be a worse result than a slightly loose total with a matching one, and the projection is
the only thing that tells those apart.

**What that implies for calibration.** A uniform multiplicative offset is exactly what an affine
correction handles. Two estimators disagreeing by a level are correctable by one number, if that number
can be learned; two estimators disagreeing in shape are not correctable at all. This run says the
disagreement of `Hotyn-D` is of the correctable kind — on one pair, on one work model.

## 4. Seven closure violations were found by both runs, independently

Neither could see the other. Both reported, in their own words:

- **nothing prices the six subtrees meeting each other** — the root is not an element in a partial work
  model, so C3 fires nowhere above the six, and "that assembly — the largest one in the system — has no
  item and no C3 base";
- **no design activity on the aggregates** — "C3 prices the *cost* of the parts meeting; it does not
  produce the design that makes them meet";
- **no store for bookings or booking requirements** — every behaviour writes to something nobody builds;
- **nothing uploads the manually uploaded bookings that R16 searches**;
- **no surface where the Travel Manager defines the prioritisation rules R19 demands**;
- **no UAT beneath the integration, search and approval-workflow subtrees**;
- **no seed or reference data outside journey locations** — no users, no roles, no suppliers.

**These are findings about the product model, produced by the estimator.** Five of the seven were also
reported by the crossing runs of run 21, from a different direction. Two independent instruments, six
independent runs, converging on the same list is the strongest evidence this session produced about
anything.

Repeat 2 added a distinction worth keeping: **"a declared boundary is not a violation."** The
whole-project activities the task placed outside the partial model do not belong on a violations list;
only what is missing *from inside* the given scope does.

## 5. Both runs named the same largest doubt, and it is not about estimating

**N37 Automatic Hotel Booking.** R29 demands automatic booking; R38 states that hotel supplier booking
is handled manually and the system performs no external automation; and no hotel-booking interface
exists anywhere in the model. Repeat 1: "If R38 governs, most of this 22.49 is not work. If R29 governs
and the aggregator books hotels too, K2-N37 is badly undersized. I cannot resolve this and must not."
Repeat 2 priced the narrow reading with a deliberately wide pessimistic value and called it "the single
largest basis risk in the estimate".

That is a contradiction between two pinned requirements, surfaced by the sensor that was forbidden from
resolving it. It belongs in `open_questions.md`.

## 6. A defect in `Hotyn-D 1.0`, found by repeat 2

**C3's base was ambiguous.** The rule said the integration item is 20% of "the sum of leaf E beneath
that element", and did not say whether the parent's *own* items count as beneath it. Both runs happened
to include them. Repeat 2 noticed, declared its reading before using it, and quantified the
alternative: integration would fall from 148.34 to 101.92 and the total from 890.09 to 843.67 —
**a 5.2% swing in the estimate, out of one word.**

Fixed in the definition: the base is the element's own items plus every descendant's, stated
explicitly. Whoever calibrates against these numbers now knows which base produced them.

## 7. What this run does not establish

- **One pair, one work model, one batch of six subtrees.** A difference, not a spread.
- **This is not a project estimate.** 1146.56 and 890.09 are the size of six subtrees of a 78-element
  product, with every whole-project activity deliberately outside the model. Neither number may be
  quoted as the size of the BMS project.
- **The ×1.288 has no reference class.** It says two runs of one instrument disagree by that much; it
  says nothing about whether either is right, and this RFP has no known outcome to check against.
