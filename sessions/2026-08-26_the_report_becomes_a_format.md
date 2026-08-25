# Session record — 2026-08-25…26 — the constants counted, the report made a format, and the class returns

**Written to be read without the conversation.** Continues
`sessions/2026-08-25_units_discipline_and_the_fixed_table.md`. Facts separated from readings, and the
session's own errors recorded with them, because they are why two of the rule changes below exist.

---

## 1. What this session did, in one paragraph

Counted the method's constants and found six of them were about time and five of those were about how
an organisation behaves rather than about the work; deleted those five by ruling, and deleted the sixth
by re-expressing the rate table in person-hours. Gave the chain a corridor for the first time, at the
price of one declared correlation. Turned the estimate into a **report format** — structure in a
builder, case in a data file, output timestamped and never overwritten — and ran it on both cases. Ran
the reference class on FaxRxTx for the first time in this generation, which produced the only
comparison in the project's history that needs no unit conversion on either side. Then made the thing
that made that possible — the unit declaration — a **required output** of every role that produces a
number. Everything committed and pushed: branch `checkpoint-2026-08-25`, the first time this
repository has held the `Hotyn` generation at all.

## 2. Instrument state

| role | before | after | what changed |
|---|---|---|---|
| `Lytin-R` | 1.0 | **1.1** | required declaration: unit · losses · roles · source disagreement · scope boundary |
| `Hotyn-K` | 1.0 | **1.1** | same, plus: prefer stating values directly in hours |
| `Lytin-K` | 1.0 | **1.1** | same, for every correction stated as an amount rather than a factor |
| `Lytin-G` | 1.0 | **1.1** | the consumer side: reconcile declarations and size the units component of a gap *before* attributing the rest to method |
| `Hotyn-M / W / D` | unchanged | unchanged | they produce no numbers with units |

**All four are minor bumps.** Nothing about how any role estimates changed; a `.0` reading is the same
instrument with a thinner report.

`docs/rate_table.md` → **v0.1-h**: 239 cells multiplied by 8, no value's content reviewed, the
person-day original preserved at `docs/archive/rate_table_v0.1_person_days.md`. Both assembly scripts
converted by the same factor and verified — every total came out exactly ×8 of the recorded figure and
the repeat spreads are unchanged.

## 3. Facts measured

- **The constant count.** Six numbers about time were in circulation; five described organisational
  behaviour and left the method by ruling; the sixth was deleted by writing the table in hours.
  **Four constants remain** — rate-table values, size thresholds, PERT, and `C3`. Three come from
  outside. `docs/constants.md`.
- **`C3`'s real weight.** Declared 20% of leaf effort at every parent; **delivered 40.9% (BMS) and
  44.4% (FaxRxTx)**, because a deep leaf enters every ancestor's base. The multiplier is the tree's
  average depth — an output of the least reproducible step, not a rate anyone chose. It is 27% of
  either total, and deleting it entirely still leaves the chain above the class.
- **The corridor.** Every rate cell carries O/M/P; the assembly collapsed each to `E` before summing.
  Restored under equicorrelated items: independent gives P10–P90 of ×1.04, perfectly correlated ×1.87.
  Across ρ from 0.25 to 0.75 — a threefold range — the band edges move about ±20%.
- **ΣO…ΣP is six sigma, not a percentile band.** It spans ×4.19 and was long quoted as the bottom-up's
  honest band. A P10–P90 is 2.56 sigma. The correlation assumption and the choice of percentile are
  two separate decisions and had been conflated.
- **Run 36** (`Lytin-R 1.0`, BMS, tail asked): P95 = 4600, P99 within-regime = 8500 person-months,
  and a refusal to give an unconditional P99 — beyond a point the project is stopped and restarted and
  effort ceases to be the right unit. Power-law tail, α ≈ 1.2. Its own P50 is **1700 recorded days**
  against the earlier pair's 1050 and 800.
- **Run 37** (`Lytin-R 1.0`, FaxRxTx, first in this generation): **P50 = 140 funded-seat person-months**
  against a documented outcome of **120** — **×1.17 high**, the outcome at about **P39**. Both sides are
  seats × time, so **no conversion enters this comparison at all**. It is the first in the project's
  history of which that is true.
- **The class's shape is stable and its level is not.** Across four independent readings:
  P10/P50 spans 0.50–0.62 (×1.18), P90/P50 spans 1.95–2.07 (×1.06) — while P50 itself spans ×2.12.
  Run 37 derived the same ratios from three sources of different provenance and called the agreement a
  cross-check that passed.
- **The conversion ladder.** From a funded seat to task hours: 365 → 261 (weekends) → 251 (holidays) →
  238 (leave) → 233 (sickness), giving a presence fraction of 0.893 against the sensor's own 0.889 and
  this project's declared 0.88 — three sources, one number. **Only the last rung is open**: net task
  hours in a present day, this project 6 against the sensor's 4.0–5.6, worth ×1.25.

## 4. Method decisions by the author

1. **`h` = 6 net task hours per present day** is the convention, being what every earlier figure used.
2. **The report gives effort, never money.** Converting to money, calendar or headcount is the
   reader's act with the reader's own figures.
3. **Reports are timestamped and never overwritten**, with an index line per run — a report replaced in
   place destroys the comparison with the one before it.
4. **The declaration becomes a requirement**, not something a run happens to mention.
5. **The third instrument is worth building only if its level comes from a table**, not from recall.
   A third instrument that samples its magnitude is a third voice with the same defect and leaves the
   project where it was with three instead of two.
6. **The unit ladder is not to be reopened.** The rungs above `h` are settled by three agreeing
   sources; substituting an alternative convention and reporting the changed number is arithmetic on a
   choice, not a finding.

## 5. Readings

**R13 — the class and the outcome share a unit, and nothing else in this project does.** Both are
funded seats × time, so their ratio is convention-free. Every other comparison the project has made
needed a conversion on one side. *Overturned by:* a case whose outcome is recorded as delivered work
rather than as headcount × calendar.

**R14 — the class's shape survives what its level does not.** Four readings agree on P10/P50 and
P90/P50 to within ×1.18 and ×1.06 while disagreeing ×2.12 on the median. Run 37 says why in its own
words: its shape is triple-sourced and every person-month of its level descends from a single anchor,
team size × duration. *Overturned by:* a reading whose ratios fall outside 0.5–0.62 / 1.95–2.07.

**R15 — the two ×1.17 figures are not one finding.** The class is ×1.17 above the outcome in a
comparison no convention touches. The chain is ×1.17 below it under this project's declared `h`, and
that figure moves with `h`. **They are not symmetric and must not be reported as if they were** — one
is a measurement, the other is a measurement conditional on a convention.

## 6. This session's own errors, recorded because two rules exist to prevent them

- **Compared factorisations.** Took a sensor's illustrative "8 people × 17.5 months", compared its
  factors against the outcome's "10 × 12", and called the differences errors that "partly cancel".
  Effort is a product; 8×17.5 = 10×14 = 12×11.7, and the sensor had already labelled its own
  factorisation *"scenario narrative only, not outputs"*. Only the product means anything.
- **Announced a convention substitution as a contradiction.** Replaced the focus factor and the
  days-per-month figure, found the ratio had moved, and reported it as a conflict with the report. A
  number must move when its multiplier changes; that is the definition of a multiplier.
- **Said the conversion factor "is not measured on this project by anyone".** It is a ladder of five
  rungs, four of them settled and agreed by three sources. Only one was open.
- **Declined to draw the class because its unit differed.** A *declared* unit is convertible; an
  *undeclared* one is not. Conflating them is what the whole session was about.
- **Invented a floor under the class curve** at 0.8 × P10, where the sensor stated none — and drew the
  body by interpolating between quantiles, which flattens P10→P50 and destroys the mode, so the curve
  read as a descending ramp. Now drawn as the lognormal the sensor itself declared.

The first two are why §4.6 exists. The fourth is why the declaration became a requirement rather than a
courtesy.

## 7. What was built

- `docs/constants.md` — the complete constant list, and the five removed with the reason each was never
  a property of the work.
- `docs/instrument.md` — the chain step by step, what is pinned where, what each sensor may not produce.
- `docs/status_2026-08-25.md` — what may be claimed and which documents are stale.
- `tools/report/build_report.py` — the report **format**, holding nothing about any project.
- `examples/<case>/report_data.json` — the case, holding nothing about the layout.
- `examples/<case>/reports/` — timestamped output plus an index line per run.

The report: masthead, a two-panel chart (density above, cumulative below, one shared axis and one
cursor crossing both), five headline numbers, then everything else behind accordion headings written so
the closed state says whether to open. Two cases have now been through it; the second needed exactly two
additions to the format, both generic — a case may declare a documented outcome, and a case may lack an
instrument.

## 8. Debts, cheapest first

1. **Adjudicate the 5 unsizeable elements and 13 closure violations, gap-blind** (+182 pd), and **rule
   on the four scope decisions** (+151 pd). Both lists are written and unruled; both owe nothing to any
   outcome.
2. **`W-F48` and its class of defect.** Stage headcount is a declaration parameter; a gap-blind rate
   author has nothing to make one from.
3. **A case profile pinned with the requirements, before any estimate** — required for cases 2–4 under
   the stricter rule.
4. **A third case.** Named by the author as the next step.
5. **The parametric instrument**, under the author's condition (§4.5).
6. **Re-derive the eleven A2/A3 addendum rows in the operative unit.** They hold a *converted* value,
   not one derived in it — 6.2% of the FaxRxTx total, a provenance defect and possibly not a numeric
   one.
7. **Catalogue defects from run 30**: `A10` cannot reach the system's own internal API; `A9` cannot
   reach an availability obligation carried by a `behaviour`.
8. **Protocol**: strip `gitStatus` from sensor launches — caught and quarantined by every sensor so far,
   which is a workaround and not a mechanism.

## 9. Open cross-session questions

- **Does the corridor's pass count?** ρ = 0.5 was not fitted on FaxRxTx — it was declared while working
  the other case — but it was declared with that outcome already known. Not fitted, and not blind. The
  report says so and counts the pass at less than full weight.
- **Which `h`?** This project declares 6; `Lytin-R` declares 4.0–5.6. It is the only open rung of the
  ladder and it is worth ×1.25 on every comparison between an instrument in funded seats and one in
  task hours.
- **Is the class's level fixable at all?** Its shape is triple-sourced and stable; its level is
  single-sourced and spans ×2.12. If the level cannot be anchored, the honest division of labour is
  shape and tail from the class, level from the chain — which is a design decision nobody has taken.

## 10. Reproduction

```bash
python examples/BMS/run25_raw/assemble.py
python examples/FaxRxTx/run31_raw/assemble_faxrxtx.py
python tools/report/build_report.py examples/BMS/report_data.json
python tools/report/build_report.py examples/FaxRxTx/report_data.json
```

Raw sensor output for this session's runs: `examples/BMS/run36_raw/`, `examples/FaxRxTx/run37_raw/`.
