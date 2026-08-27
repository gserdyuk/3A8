# The constants of the WBS side — the complete list

**2026-08-25.** Every number that enters a bottom-up estimate and is not read out of the case itself.
The list is short on purpose: an argument can be won by moving whichever constant is convenient, so
the count of constants is the count of ways to win an argument.

Sections 1-4 cover the **WBS side** — the product model, the crossing, the sizing, the table, the
assembly. Section 5 covers the **reference class**, which draws on a different kind of data and
therefore carries its own parameters. Comparison against a documented outcome is a separate act with
its own inputs and is not covered here.

---

## 1. The unit

> **Effort is working time spent solving the task.** One person-day = **8 net hours**, 40 to the week.
>
> **Not included, and not parameters of this method:** annual leave · public holidays · sickness ·
> bench time · non-project duties · the effective hours an assigned working day actually delivers ·
> working days per month · anything else describing how an organisation behaves.

A company may give its engineers four hours a day and a hundred and sixty days of leave. That is a
true and important fact about that company, and it is **not a fact about the work**. A rate row of
external norms — *"a one-operation adapter including auth, mapping and error handling: 2 person-days"*
— means an engineer working on it finishes in about sixteen hours. There is nothing organisational
inside it, and nothing organisational may be put inside it.

**Anyone needing days of presence converts, with their own figures:** divide by the effective task
hours their working day delivers — commonly 5 to 6, never 8 — then add their own allowance for leave
and holidays. That conversion is the reader's, and this method deliberately supplies neither number.

*Worth knowing before converting: a nominal 40-hour week delivers roughly 25–30 net task hours, so
**five person-days is not one person-week** — it is closer to one and a half.*

### 1a. Provenance of the 8, stated at its real strength

Three independent gap-blind `Hotyn-K 1.0` runs stated *"1 person-day = 8 net hours"* as their own
convention, unprompted, matching the table's original §2 and §5 text. The **designed numeric test
failed**: the ratio of re-derived hours to table person-days ranges 3.0 to 11.4 within a single run,
dominated by magnitude noise, and is therefore uninformative rather than confirming.

So what stands is **three statements of convention, and no numeric confirmation that the values are
budgeted at 8.** If the role said 8 and budgeted 6, the whole table is a third low in the declared
unit. That is a **calibration** question, not a unit question: it would show up as a systematic bias
across cases, which is exactly what `docs/exit_criterion.md` exists to catch. Recorded here so that
"derived" is not read as stronger than it is.

**Done, 2026-08-25: the table is written in hours and this constant is deleted.** `docs/rate_table.md`
became v0.1-h — 239 cells multiplied by 8, no value's content touched, the person-day original
preserved at `docs/archive/rate_table_v0.1_person_days.md`. Both assembly scripts converted with the
same factor and verified: every total came out exactly ×8 of the recorded figure, and the repeat
spreads are unchanged (BMS ×1.0080, FaxRxTx ×1.0326). An hour has no convention inside it, so the
paragraph above is now history rather than exposure.

---

## 2. The complete list

| # | constant | value | kind | where it lives |
|---|---|---|---|---|
| 1 | ~~unit~~ | ~~1 pd = 8 net task hours~~ | **deleted 2026-08-25** — the table is written in hours | — |
| 2 | **rate table values** | 242 rows × O/M/P | external norm, **uncalibrated** | `docs/rate_table.md` |
| 3 | **size thresholds** | S/M/L/XL bands per element class | instrument scale | `docs/technology_catalogue.md` |
| 4 | **PERT weighting** | `E = (O + 4M + P) / 6` | external standard | assembly scripts |
| 5 | **C3 — integration rate** | **20% of leaf effort at every parent** | **method-declared, free, uncalibrated** | `docs/rate_table.md` §3 |

**Four constants, of which three come from outside and one is ours.**

Everything else that varies between estimates is **read out of the case**, not chosen by the method:
the requirement list, the assumption log, the technology declaration and its parameters (environment
count, cycle counts, staffing of once-scoped stages), and the size classes the sensors count.

---

## 3. One of the four is free, and it is large

Constants 2, 3 and 4 come from outside: industry norms, a pinned catalogue, a standard formula.
Constant 1 no longer exists.

**Constant 5 is the only number this method invented for itself**, and the party that wrote it said
so in the table itself: *"method-declared constant, restated here so the table is the single home of
every number; not an external norm and not calibratable by me."*

Its weight, measured:

| | |
|---|---|
| C3 across all parents, BMS | **2 971 of 10 737 person-hours — 27.7% of the total** |
| of which the root assembly alone | **1 451 h — 13.5% of the total** |
| C3 across all parents, FaxRxTx | 3 070 of 11 203 — **27.4%**, the same share on a different project |
| the diagnosis's own reading (`D1`) | the root assembly alone spans **33–62% of the gap** against the reference class |

**And the declared rate is not the delivered rate.** C3 does not compound — it is never charged on
C3 — but it is charged at *every* parent, so a leaf deep in the tree enters the base of each of its
ancestors. Measured against leaf effort:

| | declared | delivered |
|---|---|---|
| BMS | 20% | **40.9%** (2 971 ÷ 7 257) |
| FaxRxTx | 20% | **44.4%** (3 070 ÷ 6 917) |

The multiplier is roughly **2.0–2.2**, and it is not a rate anyone chose: it is the **average depth of
the tree**, i.e. an output of the product-model step — the step whose two identical runs agree on
what-goes-with-what at Jaccard **0.31 to 0.41**, the least reproducible thing in the chain.

So the honest statement of constant 5 is not "20%". It is **a stipulated 20% multiplied by an
unmeasured structural factor of about two**, together worth more than a quarter of every estimate
the method has ever produced, derived from nothing and calibrated against nothing.

**After the unit is deleted, this is the whole of the method's discretion.** That is the useful
result of counting: there is now exactly one number left worth arguing about, and the argument has a
name and a measured size.

---

## 4. What was removed, and why it is not coming back

Six numbers about time were in circulation on 2026-08-25. Five of them described how an organisation
behaves and were never properties of the work:

| removed | what it was | where it belongs now |
|---|---|---|
| 40 hours to the week | a restatement of 5 × 8 — nothing in the chain counts weeks | the unit statement, as a gloss |
| 5–6 effective hours per assigned day | within-day yield: meetings, coordination, review, interruption | **§4a since 2026-08-27** — pinned at 6 for the comparison layer, still absent from every rate row |
| leave allowance (×1.10 / presence 0.88–0.91) | annual leave, holidays, sickness | **§4a since 2026-08-27** — pinned at ×1.10 for the comparison layer, or an outcome record |
| 21 working days per month | a calendar convention | the reader's conversion |
| `DEM_UNIT = 6/8` | a rescaling applied mid-assembly to eleven case-specific rows | **removed from the script 2026-08-25.** Those eleven rows still hold a *converted* value, not one derived in the operative unit; re-derivation is owed and parked with the outcome-comparison work |

**The rule that keeps them out:** in the WBS part, time appears in exactly one place — the unit
declaration — and nowhere else. Since that is a statement about a finite body of text and code, it is
**mechanically checkable**, and it belongs with the other checkable disciplines in `PIPELINE.md`
rather than with the things everyone promises to remember.

---

## 4a. The presence conversion — pinned by the author, 2026-08-27

**The ruling.** *"We can settle on 6 hours a day + 10% loss to leave. Instead of guessing how the
organisation behaves — use this assumption, now and later."*

| constant | value |
|---|---|
| net task hours delivered by one **present** day | **6** |
| leave, public holidays, sickness | **×1.10** on present days to reach assigned days |
| assigned days per month | **21** |

Together: **1 staffed person-month = 21 ÷ 1.10 × 6 ≈ 114.5 net task hours**, and conversely
1 000 net task hours ≈ 8.73 staffed person-months.

### Why this does not re-open §4

§4 removed these numbers **from the WBS part**, and that stands unchanged: no sensor sees them, no
rate-table row contains them, the table is still denominated in net task hours, and time still appears
in exactly one place inside the method. What §4 did was hand them to "the reader's conversion" — and
the cost of that turned out to be that **the conversion got re-argued every time it was needed, after
the numbers were already on the table.** Run 41 is the demonstration: the same batch scores 9 of 10 on
the corridor under one yield and 5 of 10 under another, and the two candidate instruments swap places
at 6.63.

So this is not a method parameter returning. It is the **comparison layer** — the step that puts an
estimate next to a fact recorded as presence — being given a pinned default instead of an open slot.
It lives here and in the report, never in a rate row.

### Provenance, and why choosing it now is not fitting it to a result

The obvious objection is that 6 was pinned immediately after a table in which 5–6 favours one
instrument. The record must let a later reader check that, so:

1. **The value is not new and was not derived today.** Three gap-blind `Hotyn-K 1.0` runs on
   2026-08-25 put a real working day's yield at **5–6 net task hours**, and §1 of this file has said
   "commonly 5 to 6, never 8" since. Run 41 did not produce it; run 41 only made its absence expensive.
2. **Within that band, 6 is the end least favourable to the chain.** At 5 net hours the chain sits at
   ×0.99 of the FaxRxTx fact; at 6 it sits at ×0.83. Anyone fitting a constant to rescue a result
   would have chosen 5. The author chose the conservative end.

### What it settles, immediately

| | net task hours | against the fact |
|---|---:|---|
| FaxRxTx fact, 120 staffed pm | **13 745** | — |
| Hotyn chain | 11 386 | **×1.21 low** |
| no-method baseline, run 41 mean | 20 244 | **×1.47 high** |

Under the pinned convention the chain is the closer of the two, and the ×1.14 reading that briefly
put the baseline ahead is withdrawn (`examples/FaxRxTx/run41_baseline_no_method.md` §1).

### Standing rule from here

Any figure recorded as **presence** — heads × months, staffed person-months, an outcome from a
timesheet system that counts attendance — converts by this constant and no other, and the conversion
is named wherever it is used. A case whose organisation is known to differ **states its own value in
its case profile before any estimate exists**; absent that statement, this is the value. Changing it
is a dated amendment with a stated reason, never a silent edit, and never an edit made while looking
at a result the change would rescue.

---

## 5. The reference class carries its own parameters

The WBS side prices *work content* from norms that never contained anything organisational. The
reference class does the opposite by construction: it reasons by analogy with **projects as they were
actually recorded**, and such a record is not pure task time.

So the two instruments do not report the same quantity. **The class figure is converted; the WBS
figure is not.**

### 5a. What a recorded project-effort figure actually contains

Checked against the sources the field actually uses, because assuming it was wrong once already.
There are **three levels, not two**:

| source | leave, holidays, sickness | within-day overheads (meetings, coordination, review) |
|---|---|---|
| **COCOMO**, person-month = **152 hours** | **excluded** — Boehm deducts them explicitly | included |
| **ISBSG**, PROMISE sets (China, Kitchenham, Desharnais, Maxwell) — timesheet hours | **excluded** (booked elsewhere) | included |
| *"ten people for about a year"* — a recollection | included | included |
| **this method's rate table** | excluded | **excluded** |

The sharpest datum is COCOMO's **152 person-hours to the month**. A nominal month at 8 h/day is
about 168; 152/168 = **0.905**. Boehm's own deduction for leave is therefore ~10% — the same figure
the author declared independently — **but it is already applied in the published numbers.**

*Confidence: the 152 is certain. That ISBSG and the PROMISE sets are timesheet-based, hence
leave-free and overhead-inclusive, holds for the typical case; what exactly each contributing
organisation booked varies, and that inconsistency is a documented weakness of the data, not a
detail. ISBSG's "resource level" field exists because of it.*

### 5b. Declared, 2026-08-25

> **Effective time: 6 net task hours per recorded day.**
>
> ```
> NET_EFFECTIVE_DAYS = TOTAL_DAYS / 8 * 6      factor 0.75
> ```
>
> Equivalently, and more simply: **each recorded project day contributes 6 hours of task work.**
> Leave is *not* deducted here, because the sources the class reasons from have already deducted it.
> What remains to remove is the within-day overhead, which they have not.

**An earlier version of this declaration also divided by 1.1 for leave. It is withdrawn** — that was
a second deduction of something already absent, worth ×1.10 against the class. The correction was
found by checking what the field's datasets record rather than by assuming.

### 5c. Applied to the BMS readings (`Lytin-R 1.0`, n=2)

| | floor | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|---:|
| RC26-1, as reported (recorded days) | 500 | 650 | 1050 | 1600 | 2050 |
| RC26-1, **net effective days** | 375 | 488 | **788** | 1200 | 1538 |
| RC26-1, **net task hours** | 3 000 | 3 900 | **6 300** | 9 600 | 12 300 |
| RC26-2, as reported (recorded days) | 350 | 420 | 800 | 1250 | 1650 |
| RC26-2, **net effective days** | 262 | 315 | **600** | 938 | 1238 |
| RC26-2, **net task hours** | 2 100 | 2 520 | **4 800** | 7 500 | 9 900 |

### 5d. The divergence, both sides now in one unit

| | raw table-priced (10 737 h) | calibrated centre (15 248 h) |
|---|---|---|
| against class P50 | **×1.70 – ×2.24** | ×2.42 – ×3.18 |
| where it sits in RC26-1 | ~P84 | above P90 |
| where it sits in RC26-2 | **above P90** | above P90 |

And read the other way round, which is the more telling direction:

| | RC26-1 | RC26-2 |
|---|---|---|
| the class's **median** as a percentile of the bottom-up | ~P0.7 | ~P0.05 |
| share of the bottom-up's distribution above the class's **P90** | 19% | 68% |
| the bottom-up's **P10** — its own best case — in the class | ~P69 | ~P84 |

**Each instrument places the other's centre in its own extreme tail.** The bottom-up's most
optimistic tenth percentile is already a bad year by class standards.

Three things follow:

1. The two distributions **overlap only in their tails**. This is not a calibration nuance; the
   instruments disagree about magnitude.
2. **`C3` cannot carry it.** Deleting the integration constant altogether — all 2 971 h — leaves the
   raw figure at 7 766 h, still **×1.23 – ×1.62** above the class median. The method's one free
   constant explains under half of the divergence.
3. The disagreement lands **above the class's P90**, in the one region the class never described: no
   P95, no P99, no tail shape was ever produced. **It cannot be resolved with the published quantiles
   at all.** The cheapest next measurement is therefore a gap-blind `Lytin-R` run asked for the tail.

### 5e. The two things still assumed

**The conversion models what the class sensor's data contains; the sensor never said.** It stops
being an assumption the moment `Lytin-R 1.1` is required to state, in every reading, what its
quantiles are counted in and what is inside them. Existing readings stay attached to `Lytin-R 1.0`
and are converted under this declared model, with the model named.

**And the bottom-up's width rests on a declared correlation.** Every rate cell carries O, M and P;
the assembly has always collapsed each to `E` before summing, which is why the chain reported a
centre and no corridor. Restoring them, with equicorrelated items at **ρ = 0.5** — declared on the
reasoning that the truth is certainly neither 0 nor 1 and far from both — gives P10–P90 of
**8 434 – 13 040 h**. The choice matters less than it appears: across ρ from 0.25 to 0.75 the band
edges move about ±20%, while the divergence with the class is a matter of multiples.

*Known direction of error: the normal approximation understates the right tail, because the cells are
right-skewed and correlated sums keep skew. The true upper tail is fatter, which moves the bottom-up
further from the class, not closer.*

### 5f. The unit of `RC26-1` and `RC26-2`, closed 2026-08-25 from their own transcripts

The two runs were given assumption A7 v2, *"1 pd = 8 hours of net work"*. **Neither honoured it, and
both said so in writing.** The question needed no new run; it needed reading what they wrote.

| run | what its transcript states |
|---|---|
| `RC26-1` | *"A7's unit is load-bearing — anchors are built on **assigned working days**; under a strict '8 productive hours' reading every quantile **×≈0.8**."* Its team×duration anchor: *"~6 effective FTE × **~18 net pd/person-month**"* — 18 charged days of 21, i.e. net of leave, gross of within-day overhead. |
| `RC26-2` | Labels itself *"person-days of net effort (A7)"*, then immediately: *"A7 used as a unit conversion with the **net-vs-booked mismatch flagged**"*, and in its own risk list: *"unit-definition risk (net vs booked effort, **±15–25%**, all quantiles somewhat high if 'net' is strict)"*. Its anchors are duration-derived (*"6–8 FTE × 6–7 months"*, *"QSM SLIM, team 5–8, 8–14 months"*), which are booked days by construction. |
| `RC36-1` | Declares it unprompted: *"one person-day = one **recorded, assigned working day**… the focused task content is realistically **4.5 to 6 hours** — call it 5."* Leave outside. |

**All three sensors reason in assigned working days.** Every one of them flagged the mismatch with the
label it was given, and two of them quantified it. Their own stated conversions to strict 8-hour
task-days: `RC26-1` ×0.8 · `RC26-2` ×0.75–0.85 · `RC36-1` ×0.56–0.75 (centre 0.625).

**The declared house factor of 0.75 (6 productive hours) is applied to all three.** It sits inside the
range `RC26-1` and `RC26-2` state for themselves and at the top edge of the range `RC36-1` states —
which is `RC36-1`'s most favourable end, and is recorded as such.

### 5g. Three class runs on one basis — and the class now disagrees with itself more than with the chain

| run | P50, net task hours | gap to the chain's 10 737 | the chain's centre sits at |
|---|---:|---|---|
| `RC26-2` | 4 800 | ×2.24 | above P90 |
| `RC26-1` | 6 300 | ×1.70 | ~P84 |
| `RC36-1` | 10 200 | **×1.05** | **~P53** |

| | |
|---|---|
| **class-to-class spread on P50** | **×2.12** |
| class-to-chain gap | ×1.05 – ×2.24 |

**The reference-class sensor's run-to-run variation is now the largest single quantity in the
comparison** — larger than its disagreement with the bottom-up. Before any unit conversion the raw
medians are 800 / 1050 / 1700 recorded days, a spread of ×2.1, so the conversion did not create it.

*Not a clean n=3.* `RC36-1` ran on a modified input — A7 withheld, the tail question added — so part of
the spread may be input difference rather than sensor variance, and n=1 on the new input cannot
separate them. What is not in doubt is that the spread exists and dominates.

*And the earlier reading of this section was right for the wrong reason.* The ×0.75 was first applied
as a model of what the class's sources probably contain. The transcripts show it is what the sensors
themselves said to do — which is a stronger warrant, arrived at by reading rather than by assuming.
