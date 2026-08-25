# Run 34 — person-hours, and the double count settled

**2026-08-24.** The author's ruling, and what it does. Supersedes `run33_unit_of_the_fact.md` §§2–6;
`run32_fact_comparison.md` §§1–4 stand as the record of what was measured against the fact as stated.

---

## 1. The ruling

> **Move to person-hours — then there is nothing to manipulate.**
> **"Two person-days for an adapter" in the norm means two days an engineer is present. Not 16 hours —
> 12 hours. Sixteen hours would be "almost three" person-days.**

So: **one table person-day = 6 person-hours.** The table's day is an *assigned working day* of a real
engineer, with the stand-ups and the training inside it. Meaning (i) of `run33` §10.1 is confirmed and
meaning (ii) is dead.

## 2. The double count, now shown rather than argued — in hours, where it cannot hide

| | |
|---|---|
| **estimate** | 1452.5 table-days × 6 h = **8 715 person-hours** |
| **fact** | 2520 nominal staffed days × `L` × 6 h |
| **ratio** | 15120·`L` ÷ 8715 = **1.735 × `L`** |

**The 6 h/day multiplies both sides and cancels.** It appears once in the estimate, because the table's
day is 6 hours; it appears once in the fact, because a present staffed day delivers 6 hours. It is not
a conversion between the two sides at all.

**Therefore the 0.75 must not be applied to the fact**, and `run33` §§3–5 — which did apply it, and
reported the fact as 90 pm and the miss as ×1.30 — **are withdrawn.** That was the double count, and it
was worth ×1.33 in the estimate's favour.

This is the reading `run33` §10.1 argued for against its own interest. It is now settled by the owner
of both conventions, which is the only way it could have been settled.

## 3. The only real conversion is presence, and the verdict does not turn on it

`L` = days actually present ÷ nominal working days. Leave, public holidays and sickness are *on top of*
the 6 h/day, per the author, and no rate-table norm contains any of them.

| `L` | days present per year | fact, person-hours | chain as it stands | + the two pending adjudications |
|---:|---:|---:|---|---|
| 0.833 | 210 | 12 600 | ×1.446 **fail** | ×1.176 **PASS** |
| 0.861 | 217 | 13 020 | ×1.494 **fail** | ×1.215 **PASS** |
| 0.885 | 223 | 13 380 | ×1.535 **fail** | ×1.249 **PASS** |
| 0.913 | 230 | 13 800 | ×1.583 **fail** | ×1.288 **PASS** |
| 1.000 | 252 | 15 120 | ×1.735 fail | ×1.411 fail |

**Across every plausible `L` the chain as it stands fails and the corrected chain passes.** The verdict
is robust to a parameter nobody has fixed, which is the best kind of result to have on an undecided
input. `L` is still wanted for the record — the author's standing number, not a guess — but no
conclusion in this document waits on it. Figures below use `L` = 0.88 (13 306 h, gate 10 235 … 17 297).

## 4. The score

| | person-hours | against fact | gate |
|---|---:|---|---|
| **chain as it stands** | 8 715 | ×0.655 — the fact is **×1.53 higher** | **fail** |
| **chain + the two pending adjudications** | 10 713 | ×0.805 — the fact is ×1.24 higher | **PASS** |

The two adjudications are the ones already sitting on the desk and needing no run: the **5 unsizeable
elements and 13 closure violations** the sizing sensors named themselves before any fact was opened
(+182 pd), and the **four scope decisions** of the declaration (+151 pd). They have to be ruled on
their merits. But they are now the whole of what separates a fail from a pass, and that is a much
better place to be than needing a level factor.

## 5. The project's outcome history in one unit, at last

Old-generation person-months read as 21 assigned working days = 126 h, the same convention as the
table.

| run | person-hours | against fact | gate |
|---|---:|---|---|
| **2026-07-17 manual, raw** | **14 062** | **×1.057** | **PASS** |
| 2026-07-17 manual, calibrated | 19 530 | ×1.468 | fail |
| 2026-08-05 pipeline, raw | 29 963 | ×2.252 | fail |
| 2026-08-05 pipeline, calibrated | 63 378 | ×4.763 | fail |
| 2026-07-17 reference class P50 | 20 160 | ×1.515 | fail |
| 2026-08-05 reference class P50 | 17 010 | ×1.278 | PASS |
| 2026-08-22 Hotyn chain | 8 715 | ×0.655 | fail |
| 2026-08-22 Hotyn + adjudications | 10 713 | ×0.805 | PASS |

**The best single reading this project has ever produced is its first one, made by hand in July 2026,
at ×1.057.**

## 6. Corrections to my own readings of the last two days

Yesterday's amendments were computed on the 90 pm figure that §2 has just withdrawn. Three of them do
not survive.

**R11 — my amendment is withdrawn; the original stands.** On 2026-08-22 R11 read: *"every generation
removed a degree of freedom; agreement improved and accuracy did not."* Yesterday I amended it to say
accuracy did improve. **It did not.** In one unit the error runs ×1.06 → ×2.25 → ×0.66 across the three
generations: it got much worse, then partly recovered, and never returned to where the first hand-made
run stood. Agreement improved to ×1.032 and accuracy did not. **The original R11 was right and my
amendment of it was an artefact of the double count.**

**R10 — does not survive as I stated it yesterday, in either direction.** I first wrote that the
reference class had been closest twice; yesterday I wrote that it *"overshoots ×1.50 and ×1.78 and
fails on both readings"*. Neither is correct. In one unit the class is **×1.515 (fail) and ×1.278
(pass)** — one of two — and the closest instrument in the project's history is not the class but
July's manual bottom-up. What survives is weaker and still worth keeping: **the class has never been
badly wrong, and the bottom-up has been badly wrong three times out of four.**

**R12 — narrowed.** *"Every calibration this project has ever applied moved the answer away from the
fact, and all three moved it up."* Two of them did: July 111.6 → 155 pm took ×1.06 to ×1.47, and August
237.8 → 503 took ×2.25 to ×4.76. The third, `L-1`, was never applied and would have moved *closer* —
to ×1.136. **But that is arithmetic, not merit:** `L-1` was fitted to make the estimate equal the fact
*as stated*, so applying it necessarily lands at exactly 1/`L` = 1/0.88 = ×1.136 of the corrected fact.
A factor fitted to a wrongly-united number landing near the rightly-united one is a coincidence of the
unit error's size, and it is a warning about `L-1`, not a rehabilitation of it.

**The durable form: both calibrations this project has actually performed moved the estimate away from
its only documented outcome, and both moved it up.** The mechanism named in July 2026 still fits —
calibration pulls towards the ensemble P50, and the class sits ×1.28–1.52 above the fact.

## 7. What the ruling changes in the method

The author's instruction — *move to person-hours, then there is nothing to manipulate* — is a
convention change and should be written down as one, not applied case by case.

**Proposed, for the author's approval:**

- **`docs/rate_table.md`, unit declaration.** *One person-day = one assigned working day = **6
  person-hours**. Values unchanged.* This supersedes A7 v3's wording, which named the assigned working
  day without giving its hour content and thereby left exactly the ambiguity this case ran into. Both
  the table and every future comparison state hours.
- **`A9` in each case's assumption log** currently reads *"1 pm ≈ 21 pd ≈ 168 hours"* and conflates two
  different things — 21 nominal staffed days, and 168 hours that assume an 8-hour day. **Split it:**
  a nominal staffed month is 21 calendar working days; the work it delivers is `21 × L × 6` hours.
- **`A13`, restated in its correct form.** An outcome recorded as *headcount × calendar* is **nominal
  staffed time**. It converts to delivered work by the **presence fraction alone**. The hours-per-day
  figure appears on both sides and **must never be applied to one of them** — that is precisely the
  double count this case produced and caught.

## 8. What is left

Unchanged in order, sharper in consequence.

1. **Adjudicate the 5 unsizeable elements and the 13 closure violations, gap-blind.** No longer one
   correction among several: together with item 2 it is the entire difference between fail and pass.
2. **Rule on the four scope decisions.**
3. **Declare `L`** — the organisation's standing presence fraction. Wanted for the record; changes no
   verdict.
4. **Write the unit declaration into the rate table** (§7), so that no future comparison can repeat
   this.
5. **A corridor instrument.** Unchanged, and now the only structural gap left in the chain.
6. **A second documented outcome.** `L-1` stays withdrawn, so FaxRxTx remains unspent.

## 9. The finding this case has produced, twice over

`run33` §9 said it once: *an outcome is an input, and inputs are pinned and interrogated.* Two days of
argument have now shown the second half of it. The first correction — staffed headcount, not full-time
— was real and worth ×1.14. The second — applying 6/8 to one side — was **an error of mine, in my own
favour, arrived at within an hour of learning what answer would help**, and it took the author's own
norm to kill it.

The safeguard that actually worked was not a rule. It was **stating the unfavourable reading, in full,
in the document, at the moment the favourable one was most attractive.** That is worth making standing
practice: when a correction moves a result towards a threshold, the document records the argument
against it before it records the result.
