# <case> — the estimate, v<n> — <date>

<!-- The template of the estimate document, the deliverable of /3a8:estimate. Filled by the orchestrator at the
end of a run, from the run records and the sensors' outputs only. Keep the section order; keep every number
traceable to a run; write it to be read without the conversation behind it. Delete these comments. Worked
examples: examples/BMS/estimate_BMS_2026-08-22.md (the 1.1 chain, no outcome) and, outside the public tree,
the SAS documents of 2026-09-08 and 2026-09-16. -->

**<One paragraph: which case, which chain, what makes this document what it is — first estimate, a re-estimate,
an estimate with an outcome opened after it.>** Written to be read without the conversation behind it.

**Read this box before any number.**
- Every bottom-up figure rests on **rate table v0.1-h — external industry norms in net task hours, uncalibrated
  against any outcome**. The centre is "norms passed through a measured size vector", not a validated cost.
- The bottom-up stands on **one** product model (<id>). <What the pair showed: leaves ×…, anchored ×…>.
- <Outcome: none and why, or known and opened only after the diagnosis was fixed.>
- <Era, or any other standing caveat the sensors refused to adjust for.>

---

## 1. The answer, three parts, not summable

Unit: **net hours of work on the task** — leave, holidays, sickness and presence overhead excluded. In the
comparison-layer convention (`docs/constants.md` §4a) one staffed person-month ≈ 114.5 net task hours.

| part | value (net task hours, A1 scope) | ≈ staffed person-months | what it is |
|---|---|---|---|
| **Centre** | **<lo – hi>** | **≈ <pm>** | the calibrated bottom-up: table-priced assembly <raw band> × the gap-blind Step C chain (×<factor>): <the corrections in one line> |
| **Corridor** | **<lo – hi>** | <pm range> | the spread of the calibration rates — **the rates' band, not percentiles**. It contains <what it contains> and nothing else |
| **Reserve** | **<resolved / unresolved>** | | the raw class tail, uncalibrated, <each reading's P80 and P90 in net hours>; <where the centre sits against them> |

**The outside view, for the same scope** (`Lytin-R 1.1`, <n> launches, each declaring its own unit; converted
by <which factor and why>):

| net task hours | P10 | P50 | P80 | P90 |
|---|---|---|---|---|
| <RC id> (<declared unit>) | | | | |

<Shape and level: P90/P50, the level difference between readings, what each declined to number.>

**The raw chain, for the record:** <raw centre> net task hours (repeat band <lo–hi>, ×<spread>), with its own
O/M/P band at ρ = 0.5 of <lo–hi> — a declared convention, not a measurement.

## 2. What the diagnosis established (run <N>, Steps B–D)

- **Units first.** <How the declarations were reconciled and what share of the gap units explain.>
- <The largest quantity in the comparison and what it is attributed to.>
- <Direction of the calibration; explained share per reading; the residual, not closed.>
- <False convergence, checked and refused, or not found.>
- <How the coverage report moved the rates.>

## 3. What is inside the centre

<Obligations → elements → items → sized leaves, agreement, spread. Then the categories of work the structure
carries, and via the calibration, what the rates added — one dense paragraph, every category named.>

## 4. What is NOT in any number, by name

1. <Carried unpriced, awaiting a parameter.>
2. <The refused readings — the declared narrowings that may reverse.>
3. <The rate table's level.>
4. <Uncovered by any rate.>
5. <The era.>
6. <Tail and failure events — in the class quantiles, in no bottom-up item.>
7. <Effort→calendar, team availability.>

## 5. The decisions and questions that move this answer

**<Two or three facts, in order of leverage — instrument questions.>**

**For the client (from the open-questions register):** <the questions, by id>.

**Known model and catalogue findings:** <converged on by independent instruments>.

## 6. Provenance

<Engine chain with versions and n, the outside view, the rates, the diagnosis; the model coordinate; how the
sensors were launched (plugin, child process, output cap); where every prompt and raw reply is; protocol facts.>

<!-- ## 7. Beside an earlier estimate — only when one exists on the same case: the comparison table, the ratio,
where the difference sits. Two versions of one instrument are shown side by side and never averaged. -->
