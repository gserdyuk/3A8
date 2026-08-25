# Run 33 — the unit of the fact, and what it does to every score the project has

**2026-08-23.** Amends `run32_fact_comparison.md`. It does not replace it: run 32 records what was
measured against the fact **as stated**, and stands. This document records what the fact's owner then
said the fact means.

---

> **SUPERSEDED, 2026-08-24 — see `run34_person_hours.md`.** The author has ruled that one table
> person-day is an assigned working day of **6 person-hours** ("two person-days for an adapter" =
> 12 hours, not 16). The 6 h/day therefore multiplies **both** sides of the comparison and cancels;
> applying it to the fact alone, as **§§3-5 below do**, was the double count §10.1 warned against.
> **§§2-6 of this document are withdrawn.** The fact is not 90 pm; the only conversion is the
> presence fraction, and the chain as it stands fails at x1.45-1.58. §§1, 9 and 10 stand.


> **Amended within the day — see §10.** The author has since said that holidays and leave are
> **on top of** the 6/8, and that the 6/8 is within-day effectiveness (meetings, training, other).
> That makes the conversion a product of two factors, not one, and raises a **double-count risk**
> that §10 states against this document's own interest. **The single figure of 90 pm in §§3-5 below
> is one reading of several and is not settled.** The scoring in §4 and the rescoring in §5 are
> conditional on it; §10 gives the full range and the two thresholds that matter.


## 1. What was asked, and what came back

`docs/diagnosis_2026-08-23_the_gap.md` §6 put one question at the top of the elimination programme,
above everything requiring a run:

> *Were those ten people full-time on this project for the whole year, or is ten the headcount that was
> staffed to it?*

The author's answer, 2026-08-23, verbatim in substance:

> **It is staffed headcount.** And: **in our practice an 8-hour working day is 6 person-hours.**

So `FACT.md`'s "~120 person-months" is **10 people on the staff × 12 calendar months** — a
headcount × calendar product — and the organisation's standing conversion from staffed presence to
delivered work is **6 / 8 = 0.75**.

## 2. Why this is a unit correction and not a calibration

The rate table's rows are external norms of the form *"one-operation adapter including auth, mapping
and error handling: M = 2 pd"*. Such a norm means an engineer **working on it** finishes in about two
days. It contains no annual leave, no public holidays, no sickness, no internal duties, no bench.

The fact's 2520 days (120 pm × 21) contains all of them, because it was reconstructed as *ten people on
the payroll for a year*.

The two sides were therefore never in the same unit, and no amount of estimating would have closed
that. **This is the same class of act as A7 v3** — where the author adjudicated that a person-day means
one assigned working day — applied for the first time to the **fact's** side of the comparison rather
than the estimate's.

**The fact restated in the estimate's unit: 120 × 0.75 = 90 person-months = 1890 pd.**

## 3. The fitting risk, stated before the result

`docs/diagnosis_2026-08-23_the_gap.md` §4(a) published a sensitivity table **before** the question was
answered, and that table shows the 75% row landing at ×1.301 — a hair outside the ×1.3 gate. So the
answer's consequence was visible in advance. Three things keep this from being a fit, and one does not:

- **The answer is a standing organisational convention**, not a number chosen for this case. "In our
  practice" is a statement about how this organisation plans every project.
- **The question was registered before the answer**, in a document written for that purpose.
- **The convention was supplied by the owner of the fact**, who is the only person entitled to say what
  the fact means.
- **But** the direction that would help was known when the question was asked, and that cannot be
  undone.

**The safeguard, and it should be taken now rather than argued about later: pin the conversion as a
standing rule that applies to every outcome the project ever scores**, in the assumption log, with no
reference to FaxRxTx. A convention that applies to one case is a fit; a convention that applies to all
of them is a unit. Proposed as **A13**: *an outcome reconstructed as headcount × calendar is staffed
presence, not delivered work, and converts at the organisation's declared utilisation before it is
compared with any estimate.*

## 4. The score, restated

Gate: `[90 ÷ 1.3, 90 × 1.3]` = **69.23 … 117.0 pm**.

| | pm | against 90 | gate |
|---|---:|---|---|
| Hotyn chain, **centre** | 69.17 | ×0.77 | **fails by 1.35 pd — 0.09%** |
| Hotyn chain, repeat 1 | 70.25 | ×0.78 | **PASSES** |
| Hotyn chain, repeat 2 | 68.08 | ×0.76 | fails |

The centre sits **1.35 person-days below the threshold on a total of 1452.5**. One of the two
classification repeats passes and the other does not. Nobody should read that as a pass or as a fail:
it is a result indistinguishable from the gate, on a fact whose own stated accuracy is ±20% — a window
four hundred times wider than the margin. **What can be said is that the miss is no longer a gross
error: it went from ×1.735 to ×1.30.**

And with the two corrections that need no new run — the coverage holes the sensors named (+182 pd) and
the four scope decisions (+151 pd) — the corrected estimate is **1786 pd = 85.0 pm**, and the gap is
**×1.059**. Those corrections still have to be adjudicated on their merits; the point is that nothing
exotic is left to explain.

## 5. What this overturns — the project's whole outcome history, rescored

| run | pm | against 120 (as stated) | against 90 (delivered work) |
|---|---:|---|---|
| 2026-07-17 manual, raw | 111.6 | ×0.93 **pass** | ×1.24 **pass** |
| 2026-07-17 manual, calibrated | 155 | ×1.29 pass | ×1.72 fail |
| 2026-08-05 pipeline, raw | 237.8 | ×1.98 fail | ×2.64 fail |
| 2026-08-05 pipeline, calibrated | 503 | ×4.19 fail | ×5.59 fail |
| 2026-07-17 reference class P50 | 160 | ×1.33 fail | ×1.78 fail |
| 2026-08-05 reference class P50 | 135 | ×1.12 pass | ×1.50 fail |
| **2026-08-22 Hotyn chain** | **69.2** | ×0.58 fail | **×0.77, on the gate** |

Three readings of yesterday's session are now wrong and are withdrawn or amended.

**R10 is overturned.** *"The reference class has been the closest instrument to the fact, twice."* It
has not. Against the corrected fact the class overshoots by **×1.50 and ×1.78** and fails the gate on
both readings. The instrument that looked best was benefiting from the same unit error as everything
else, and it benefited most because it sat highest.

**R11 is amended.** *"Every generation removed a degree of freedom; agreement improved and accuracy did
not."* Agreement improved — ×1.032 stands. But accuracy did improve: against the corrected fact the
Hotyn chain is within 0.09% of the gate while the previous generation's calibrated answer is ×5.59 out.
What is true, and is the durable form of R11, is narrower: **the bottom-up centre still swung ×3.4
across three generations, and that swing is method variance and remains unexplained.**

**A new reading, and it is the sharpest thing in this document.**

> **R12 — every calibration this project has ever applied moved the answer *away* from the fact, and
> all three moved it the same way: up.** July: 111.6 → 155 (×1.24 → ×1.72). August: 237.8 → 503
> (×2.64 → ×5.59). And `L-1` would take 69.2 → 120 (×0.77 → ×1.33). Three calibrations, three
> overshoots, one direction. *Overturned by:* a calibration act on a case with a documented outcome
> that moves the centre towards it.

The mechanism is visible and was named in July 2026 as a hypothesis: calibration pulls the estimate
towards the ensemble P50, and the ensemble P50 is **high** — which the corrected fact now shows
directly, since both reference-class readings sit ×1.5–1.8 above it. The project has been calibrating
towards a class whose centre is above its only known outcome.

## 6. `L-1` is withdrawn

`run32_fact_comparison.md` §5 recorded a global level factor **`L-1` = ×1.735**, fitted on FaxRxTx at
n = 1, with three binding conditions. Condition 2 said: *"If the granularity experiment shows the
element count carries it, `L-1` must be withdrawn, not re-fitted."*

It is withdrawn now, for a different and stronger reason. The factor was ×1.735 against the fact as
stated, ×1.301 against the fact in the right unit, and ×1.059 once the two pending corrections are
applied. **A factor that shrinks by 40% when you fix a unit error, and by another 23% when you
adjudicate two lists that were already sitting there, was never a calibration** — it was a container
for everything not yet diagnosed.

Nothing replaces it. The chain is used uncalibrated until there is a second documented outcome.

**And FaxRxTx is no longer spent as evidence.** Run 32 §5 recorded that fitting `L-1` burned the case;
withdrawing `L-1` gives it back, because no parameter now in the chain was fitted on it. That matters:
it is the project's only outcome case and it was about to be lost to a factor that turns out to have
been mostly a unit error.

## 7. What the rate table gets back

The table was the prime suspect. `run32` §4 named the vintage — modern norms on a 2007–2009 stack — as
one of two candidates that could each carry the whole gap, and `docs/diagnosis…` added a team that did
not know the domain as a third. Both are per-element level effects and both would have needed two or
three further outcome cases to test.

**Neither is needed any more.** After the unit correction and the two pending adjudications the residue
is ×1.06, which is inside the noise of a fact with a ±20% memory band. That does not prove the vintage
costs nothing — it means **the evidence for it has evaporated**, and inventing a factor for it now would
be exactly the fitting this document exists to avoid.

`docs/rate_table.md` stays at v0.1 + A1. It was never the problem.

## 8. What is left, in order

1. **Pin A13** — the staffed-to-delivered conversion, as a standing rule for every outcome, not for
   this one.
2. **Adjudicate the 5 unsizeable elements and the 13 closure violations**, gap-blind. +182 pd if all
   stand. This is now the largest remaining term.
3. **Rule on the four scope decisions.** +151 pd if all four go the other way.
4. **The granularity experiment** — demoted. It was the decisive test when the gap was ×1.735 and the
   leaf layer would have had to be ×1.81. Against a residue of ×1.06 it is no longer diagnostic, and
   R8 loses most of its urgency: the total may still track element count, but nothing now requires it
   to.
5. **A corridor instrument.** Unchanged, and now the most important open item — exit-criterion test 2
   still cannot be applied, and the sharper the centre gets the more the corridor is what is missing.
6. **A second outcome case.** Unchanged, and cheaper than before: the chain is uncalibrated, so nothing
   has to be un-fitted first.

## 9. The methodological finding, which outlives FaxRxTx

**Three generations of this project interrogated the estimate and took the fact as given.** Twenty-plus
runs, four instrument generations, a rate card, a case-law register, an exit criterion — and the single
largest error term in the only comparison that could ever score any of it was in the fact's unit, and
it cost one question to find.

The rule that follows is cheap and should be standing: **an outcome is an input, and an input is pinned
and interrogated like any other.** `FACT.md` has never been pinned, never had an assumption log, and
never been asked what its numbers mean. It has a ±20% memory band on the duration and no stated band on
the headcount, and the headcount turned out to be the load-bearing figure.


---

## 10. Amendment, same day — the conversion is two factors, and one of them may double-count

The author, clarifying: **holidays and leave are on top**, and the 6/8 is *within-day* effectiveness —
"the rest is meetings, training and the like".

So the conversion from the fact as recorded to the estimate's unit is a product:

    120 pm staffed  ->  x L (days present, leave and holidays removed)  ->  x 0.75 (effective hours in a present day)  ->  table person-days

### 10.1 The double-count risk, stated against this document's interest

**The 0.75 may already be inside the rate table**, in which case applying it to the fact counts it
twice and every number in §§3-5 above is too favourable.

`assumptions.md` **A7 v3**, the author's own adjudication of 2026-08-22, says the table's unit is *"one
assigned working day - the convention the table's external sources natively record"*, and that v0.1's
"8 hours of net working time" wording was **superseded** with no value changed. An assigned working day
of a real professional contains their meetings. If that is what the table's rows mean, then a present
staffed day **is** one table person-day, the 6/8 cancels on both sides, and only `L` applies.

**The table's own basis lines point that way.** They are written in the language of elapsed working
days, not of heads-down hours: *"a day each plus a written note"* - *"two or three sessions with
experts, reading whatever material exists, a working note others can use, and one correction round"* -
*"roughly a day per action/task with shared plumbing"*. Those are descriptions of what a working person
gets through in a day, meetings included.

**This reading is the unfavourable one and it is the one the evidence currently supports.** It is
recorded here in that form deliberately: the favourable reading arrived after a sensitivity table had
already shown which answer would help, and the only protection against that is to argue the other side
as hard as it deserves.

### 10.2 The range, and the two thresholds that actually matter

Let `k` be the single conversion factor, table person-days per nominal staffed person-day.

| k | what k is | fact | gap, chain as it stands | gap, chain + the two pending adjudications |
|---:|---|---|---|---|
| 1.000 | no conversion at all (run 32's reading) | 120.0 pm | ×1.735 fail | ×1.411 fail |
| **0.880** | **leave + sick only — the table's day already has the meetings** | **105.6 pm** | **×1.527 fail** | **×1.242 PASS** |
| 0.860 | leave + holidays + sick, same reading | 103.2 pm | ×1.492 fail | ×1.214 PASS |
| 0.750 | effectiveness only, leave not removed (§§3-5 above) | 90.0 pm | ×1.301 fail by 0.09% | ×1.059 PASS |
| 0.660 | 0.88 × 0.75 — leave removed **and** 6/8 applied | 79.2 pm | ×1.145 PASS | ×0.932 PASS |
| 0.645 | 0.86 × 0.75, fuller leave | 77.4 pm | ×1.119 PASS | ×0.910 PASS |

Solved rather than tabulated:

- **The chain as it stands passes the ×1.3 gate iff `k` ≤ 0.749.** The author's 6/8 = 0.750 sits exactly
  on that line, which is why §4 above landed 1.35 pd short.
- **The chain with the two pending adjudications passes iff `k` ≤ 0.921** — that is, **as soon as any
  leave discount at all is admitted**, under every reading in the table above.

### 10.3 What follows

**The definitional argument decides whether the chain passes today. Adjudicating the two lists makes it
pass under every reading.** So the order of work does not change and the argument is not on the
critical path:

1. the 5 unsizeable elements and the 13 closure violations, gap-blind (+182 pd);
2. the four scope decisions (+151 pd);
3. and only then the unit ruling, which by that point moves a verdict that no longer turns on it.

**`L-1` stays withdrawn** — more firmly than in §6, because the factor now has to absorb a `k` nobody
has fixed, and a calibration parameter standing in for an undecided unit is the exact failure mode the
rate table's calibration rule was written against.

**A13 needs both factors, not one.** Proposed form: *an outcome reconstructed as headcount × calendar
is staffed presence; it converts to the estimate's unit by (a) the presence fraction and (b) the
within-day effectiveness — and (b) is applied **only if** the rate table's day is a net-work day rather
than an assigned working day. Which it is, is a property of the table and is declared once, in the
table.* Until that declaration exists, no outcome comparison in this project is fully defined - which
is the finding of §9 arriving one level deeper.
