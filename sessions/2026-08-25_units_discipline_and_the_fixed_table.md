# Session record — 2026-08-23…25 — the units, the discipline, and the table fixed

**Written to be read without the conversation.** Continues
`sessions/2026-08-22_faxrxtx_validation.md`, which records the execution of stage 3. This one records
what happened when its result was interrogated: three unit errors, two of them mine, and the changes
to how the work is done.

---

## 1. What this session did, in one paragraph

Stage 3 ended at 69.2 pm against a fact of ~120 pm — a ×1.735 miss. Interrogating it found that the
two sides of the comparison were never in the same unit, in three separate places: the fact was
recorded as **staffed headcount × calendar**, not delivered work; I then **applied the 6/8
effectiveness factor to one side only**, a double count worth ×1.33 in the estimate's favour; and the
rate table's own hour content had been **relabelled without re-derivation**, silently cutting every row
by a third. Each was found, sized and corrected. The table was then **fixed as a set of constants** at
1 pd = 8 net hours, and the eleven addendum rows converted into that unit. The FaxRxTx estimate now
stands at **99.4 staffed person-months against a fact of 120 — ×1.21**, inside the ×1.3 gate. The
session also produced a change in working method, at the author's instruction, and the suspension of
four readings that had rested on comparing numbers whose units were never declared.

## 2. The final numbers

| | |
|---|---|
| chain, repeat 1 / repeat 2 | 1446.0 / 1400.4 table person-days (spread ×1.033) |
| **centre** | **1423.2 table pd = 11 386 net person-hours** |
| **in the fact's unit** (÷ 6 net hours per present day, × 1.10 leave, ÷ 21) | **99.4 staffed person-months**, range 97.8–101.0 |
| **fact** | **120 staffed person-months** (10 staffed heads × ~12 months) |
| **ratio** | **×1.21 low** · gate `[92.3 … 156.0]` → **inside** |

Sensitivities, all still inside the gate:

| variant | staffed pm | vs fact |
|---|---:|---|
| as it stands | 99.4 | ×1.21 low |
| + the two pending adjudications (+333 pd) | 122.6 | ×1.02 high |
| + `W-F48` at the real stage headcount | 116.5 | ×1.03 low |
| + both | 139.7 | ×1.16 high |

**`W-F48` is deliberately *not* corrected in the number above.** The concept stage is still priced at
~2% of the project where the fact puts it at 17%. The chain reaches ×1.21 *despite* a known ×8.5
under-pricing of one stage — which is worth more than the ratio itself.

## 3. The three unit errors, in the order found

| # | where | what it was | worth |
|---|---|---|---|
| 1 | the **fact** | "~120 person-months" is 10 **staffed** heads × 12 calendar months — presence, not delivered work. No rate-table norm contains leave, holidays or sickness; a headcount × calendar product contains all of them | ×1.10 (leave) |
| 2 | **my arithmetic** | applied the 6/8 within-day effectiveness to the fact **only**. In hours it is visible: estimate = pd × h, fact = nominal days × L × h — **the h multiplies both sides and cancels**. Caught by the author | ×1.33, in my favour |
| 3 | the **rate table** | `docs/rate_table.md` §2 and §5 both said "1 pd = 8 hours of net working time", written with the values. The 2026-08-22 banner relabelled it "one assigned working day" **with no value re-derived**. The party that wrote the values declined to certify the relabelling: *"accepted-on-statement, not as checked"* | ×1.33 |

**The method was carrying an unverified unit on both sides of the comparison at once.** Every accuracy
claim made between 22 and 24 August rested on two conventions of which neither had been checked.

## 4. Facts measured this session

- **The re-derivation (2 runs, `Hotyn-K 1.0` × Fable 5, gap-blind, 24 cells priced in person-hours).**
  Both runs stated their own convention unprompted — *"1 person-day = 8 net hours"* — matching the
  table's original text. Both, asked separately and afterwards, put a real working day's yield at
  **5–6 net task hours**, with the remainder to meetings, coordination, review of others' work, admin
  and context switching. **Three independent runs, one answer: the table is denominated at 8 net
  hours, and a working day yields 6.** The two are different quantities and both were needed.
- **And, by accident, the first repeatability measurement of the rate author.** The two runs on an
  identical prompt differ by **×1.38 on the sum of 24 cells, ×1.50 on the median cell**, agreeing
  exactly on 3 of 24. Conventions agreed perfectly; magnitudes did not. **The rate table is one draw
  from a distribution of that width.**
- **A test that failed as designed, recorded so it is not repeated.** The ratio *re-derived hours ÷
  table person-days* was meant to measure the table's hour content. It cannot: within a single run it
  ranges 3.0 to 11.4, because it is dominated by magnitude noise rather than by the unit. The
  question was settled by the runs' **direct statements**, which the noise does not touch.
- **The concept stage.** All ten people, two months, nothing else — **2 218 net person-hours, 17% of
  the project**, against `W-F48`'s 261 person-hours, 2%. The row is low by **×8.5**. Cause: `Hotyn-K`
  correctly refused to price the stage from the client's stated calendar duration, then had to invent
  a headcount to convert calendar into effort.

## 5. Decisions taken by the author

1. **The rate table is fixed, as a set of constants.** Not averaged over samples, not re-derived. One
   sample from `Hotyn-K 1.0` × Fable 5, 2026-08-21, kept because every priced run to date (BMS 23–25,
   FaxRxTx 29–31) used it and replacing it would make all of that incomparable.
2. **Unit: 1 person-day = 8 net hours of work on the task.** The 2026-08-22 relabelling is withdrawn.
   No value changed.
3. **The eleven A2/A3 addendum rows are converted into that unit** — they were written in assigned
   working days on my instruction, and `Hotyn-K` had warned in A3 that the two sets *"may not be summed
   without a declared conversion"*. 117.33 assigned-days = 704 net person-hours = **88.0 table pd**.
   Same work, larger unit, fewer of them.
4. **Working method, four rules** — §7 below.

**Consequence of decision 1 that is worth stating on its own: the ×1.38–1.50 rate-author spread stops
being an uncertainty of any estimate.** A constant does not vary between runs. The figure moves to
provenance, and my proposal of 24 August to build the chain's missing corridor out of it is
**withdrawn** — it was a by-product promoted to a proposal in the same turn it appeared.

## 6. Readings — four suspended, not overturned

R9 through R12 of the previous session all rested on comparing this project's estimates **across
generations**: 111.6 → 237.8 → 503 → 69.2 person-months, and the reference class at 135 and 160.

**Those numbers are in units that were never declared.** The Lytin-era runs said "person-months"
without stating whether a person-month meant staffed presence, assigned days or net hours — the same
ambiguity that took three days to resolve for one table. Rescoring them, as I did twice on 23 and 24
August, was comparing quantities of unknown dimension.

- **R9** (the bottom-up centre swung ×3.4 across generations) — **suspended**. Part of the swing may be
  unit, and no part of it can be attributed until the old runs' units are recovered, if they can be.
- **R10** (the reference class has been closest to the fact) — **suspended**, having been asserted,
  overturned and partly restored in three days on three different arithmetics. It should never have
  been restated twice.
- **R11** (agreement improved and accuracy did not) — **suspended**, same ground.
- **R12** (every calibration moved away from the fact, upward) — **suspended**, same ground.

**This is the correct disposition and it removes the root of a three-day spiral.** Reinstating any of
them requires first declaring the unit of the run it cites — which is cheap for the two July 2026 runs
and may be impossible for the August pipeline.

Surviving from this session, and it is a small list deliberately:

> **The unit of a comparison is part of the comparison, and it is an input on both sides.** Three
> failures in three days, all the same shape: a convention asserted rather than checked. Two were on
> the estimate's side and one on the fact's; the method held all three simultaneously without noticing.

## 7. Working method — the author's instruction, 2026-08-25

The author named the pattern: a fact is checked, and instead of closing, an incidental observation is
promoted to a finding, written up, and made the basis of the next turn — and it then turns out not to
be what it was called. Four rules, adopted:

1. **One question per run.** Written down before launch: what is asked, and what would answer it. The
   answer comes first in the report.
2. **By-products are parked, not promoted.** One line in a parking list. **A by-product may not change
   a conclusion in the same turn it appeared.** It becomes work only if the author takes it up, or on
   its third recurrence.
3. **No document is written without the author's word.** Exception: raw run transcripts, which are the
   protocol and are cheap.
4. **"Nothing came of it" is a legitimate result.** Treating every run as owing a finding is what
   manufactures the spiral.

And a stance toward variation, so that it stops being reported as news:

| what | expect | measured | what a violation means |
|---|---|---|---|
| script arithmetic | exact | exact | a bug |
| classification against pinned rules (`Hotyn-D`) | ≤ ×1.05 | ×1.03 | a hole in the rules |
| crossing against a declared technology (`Hotyn-W`) | ≤ ×1.05 | n = 1 | — |
| structure from a document (`Hotyn-M`) | ×1.0–1.6 | ×1.02 FaxRxTx · ×1.56 BMS | depends on the input's density |
| **magnitude sampled by a model** | **×1.3–2** | ×1.38–1.50 (`Hotyn-K`) | **expected; not a finding** |
| an outcome remembered by a participant | ±20% stated | — | — |

The `Hotyn-K` spread belongs in the fifth row and needed one clause, not a document. The only new fact
in it was that it applies to the rate table too — which decision 1 has now made irrelevant.

## 8. Debts, cheapest first

1. **Adjudicate the 5 unsizeable elements and the 13 closure violations**, gap-blind (+182 pd). Owes
   nothing to the fact; the sizing sensors wrote the list themselves before any fact was opened.
2. **Rule on the four scope decisions** (`C-DIRECT`, `E-DSP`, `G-SEED`, `U-OPS-USER`), +151 pd if all
   four go the other way.
3. **`W-F48` and the class of defect it represents.** Stage headcount is a **declaration parameter**,
   like environment count and cycle count — a gap-blind rate author has nothing to make it from. Any
   row that scales linearly in a headcount should refuse to price until it is declared.
4. **A case profile, pinned with the requirements, before any estimate**: team grade and domain
   experience, declared overheads and what is inside them, the presence fraction, the process, and the
   staffing of every stage the method prices separately. Everything asked of the author over three days
   was a case condition, none of it was a requirement, and all of it was obtainable on day one.
5. **A corridor instrument.** Still the only structural gap in the chain; exit-criterion test 2 still
   cannot be applied. The rate-sampling candidate is withdrawn (§5).
6. **A second documented outcome, with its case profile collected first.**
7. **Catalogue defects from run 30**, untouched: `A10` cannot reach the system's own internal API;
   `A9` cannot reach an availability obligation carried by a `behaviour`.
8. **Protocol**, carried: strip `gitStatus` from sensor launches; a subagent reply can arrive truncated
   and is recovered by asking for a verbatim re-emission, never by re-running.

## 9. The question, answered by the author 2026-08-25

**Does a comparison whose unit conventions were supplied by the fact's owner *after* the estimate
existed count as a score?**

> **Yes, we count it. An explanation after the fact is a poor explanation — but it is still an
> explanation.**

So **FaxRxTx is case 1 of the four the exit criterion requires, and it passes on the centre.**

| | |
|---|---|
| case | FaxRxTx / Venali, 2007–2009 |
| estimate | **99.4 staffed person-months**, uncalibrated; repeats 97.8 and 101.0 |
| fact | **120 staffed person-months** (10 staffed heads × ~12 months; ±20% stated on the duration) |
| **test 1 — centre** | **PASS** — ×1.21, gate `[92.3 … 156.0]`; **both repeats also inside** |
| test 2 — corridor | **not scoreable** — the chain declares no P10–P90 |
| **test 3 — provenance** | **PASS** — no parameter is fitted on this case; `L-1` stays withdrawn |
| standing | 1 of ≥ 4 cases; 1 of 1 passing |

**Exactly what the decision covers, stated so it cannot drift.** Two different things arrived late and
only one of them is in the number:

- **Unit conventions** — staffed-versus-delivered, the ×1.10 leave factor, the table's 8 net hours.
  These say what the numbers *mean*. They are in the score, and they are what the author's decision
  admits.
- **The concept-stage headcount** — all ten people, two months. This is the *value* of a declared
  parameter, and it is **not applied**. The 99.4 does not contain it. The chain reaches ×1.21 while
  still pricing that stage at 2% of the project where the fact puts it at 17%.

**One consequence worth carrying, and it is the constructive half of the decision.** A case admitted on
after-the-fact conventions is weaker evidence than one whose conditions were pinned in advance — the
author's own wording says so. So case 1 should set the **floor**, not the standard: **cases 2–4 are held
to the stricter rule**, with the case profile (§8 debt 4) collected before any estimate exists.
Otherwise the gate measures how well conditions can be reconstructed afterwards rather than how well
the instrument estimates.

This supersedes `examples/FaxRxTx/run35_stage_headcount.md` §6, which argued the case could no longer
score. Its reasoning stands as reasoning; the decision is the author's and is against it.

## 10. Reproduction

```bash
python examples/FaxRxTx/run31_raw/assemble_faxrxtx.py
```

Documents of this session, in reading order: `run32_fact_comparison.md` (superseded on the fact's
unit) → `docs/diagnosis_2026-08-23_the_gap.md` → `run33_unit_of_the_fact.md` (§§2–6 withdrawn) →
`run34_person_hours.md` → `docs/team_grade_as_an_input.md` → `run35_stage_headcount.md` →
`docs/the_unit_of_the_rate_table.md` → this record.

**Read them knowing that four of them contain conclusions this record suspends.** They are kept
because the project records rather than edits, and because the sequence of three corrections — two of
them mine, one of them in my own favour — is the most useful thing the episode produced.
