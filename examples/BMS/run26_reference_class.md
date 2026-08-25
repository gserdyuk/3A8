# BMS — Run 26: reference class, first run of the Hotyn era — n=2

Date: 2026-08-22. **Registered before the runs returned.** Этап 2 of the course-correction plan
(`docs/review_2026-08-21_running_in_circles.md` §7.3): the second sensor returns after 18 idle days,
and for the first time ever alongside a table-priced bottom-up centre.

## Design

`estimator-reference-class` (**`Lytin-R 1.0`**, unchanged — the sensor is generation-agnostic by
construction: it never sees the chain, so no Hotyn port is needed; its stamp is recorded and travels
into the diagnosis). Two repeats, identical prompts, Opus 5 by explicit override, launched together.
This is also the **first repeatability measurement of the reference-class sensor** — every prior RC
run (run 2, run 5) was n=1.

## Inputs, and their hygiene

- `examples/BMS/BMS_extracted.md` — the RFP digest, verbatim. Contains product facts only (5000
  rooms / 1000 taxis a year are load volumes, not effort).
- `examples/BMS/assumptions.md` v2 — pasted with the run-history narration elided (sentences citing
  prior runs by number; activity-id pointers kept, they are labels). No number of effort, no budget,
  no deadline anywhere in the paste.
- **Not given, by design:** the requirement lists' split, the product model, the work model, the
  rate table, the assembly, any total, any prior sensor output. The sensor's contamination rule is
  the enforcement; the paste is the discipline.

## Registered expectations

1. **Cleanliness and role-keeping**: contamination check clean; no decomposition performed (the
   sensor's own hard prohibition — reasoning from parts would void the run).
2. **Repeatability, first reading**: the two P50s within **×1.5** of each other. No prior
   measurement exists; whatever lands is the baseline of this sensor's own spread.
3. **Right skew**: P90/P50 exceeds P50/P10 in both runs — a symmetric class range would itself be a
   finding against the run.
4. **Method metadata verbatim**: the seven-item static blind-spot list reported as given, and the
   misclassification split (confidence across the stated class and neighbours) stated.
5. **No level prediction is registered.** July's run 2 (P50 950, P90 1800, typical RFP bids 400–700,
   n=1, assumptions v1) is on the record and will be compared *after* the runs — registering a band
   now would be anchoring the analysis, and the class level is precisely what the diagnosis consumes
   fresh.

## What run 26 is not

No comparison with the bottom-up centre happens here — that is the diagnostician's step (B), with
the gap-blind rates in between. The RC output goes into the этап-2 deliverable as the corridor's
outside view and the **owner of the tail**.

---

# Results

Raw: `run26_raw/RC26-1.md`, `RC26-2.md`. Both `tool_uses: 0` — and both runs **spontaneously
declined to read the repository whose path they could see**, each naming anchoring as the reason.
Both stamped `Lytin-R 1.0`, Opus 5.

## 1. The readings

| quantile | RC26-1 | RC26-2 | ratio |
|---|---:|---:|---:|
| P10 | 650 | 420 | ×1.55 |
| **P50** | **1050** | **800** | **×1.31** |
| P80 | 1600 | 1250 | ×1.28 |
| P90 | 2050 | 1650 | ×1.24 |

Both right-skewed with a floor-clipped left tail; both class definitions materially identical
(custom multi-portal enterprise build, vendor-hosted, **RFP stage as part of the class**); both
report the seven-item blind-spot list verbatim and a misclassification split (0.65/0.60 on the
stated class) whose **up-neighbours outweigh the down-neighbour** — RC26-1 states it outright: "if
the class weights are wrong at all, the error is more likely to be upward."

## 2. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | clean, no decomposition | **CONFIRMED** — both; borderline inputs (A3, A7) declared with how they were used |
| 2 | P50s within ×1.5 | **CONFIRMED: ×1.31.** First-ever repeatability reading of this sensor; the spread **narrows toward the tail** (×1.55 → ×1.24), i.e. the runs agree more about the bad years than about the good ones |
| 3 | right skew in both | **CONFIRMED** — RC26-1: P90−P50 = 2.5 × (P50−P10); RC26-2: P90/P50 2.06 vs P50/P10 1.9 |
| 4 | metadata verbatim + misclassification split | **CONFIRMED** — both |
| 5 | post-hoc July comparison | July run 2 (n=1, assumptions v1): P50 950, P90 1800 — **inside the new pair's band on every quantile**. Three RC readings across two eras and two assumption-log versions span ×1.31 on P50 |

## 3. Readings for the diagnosis (not conclusions)

- The two runs disagree mostly about the **low half** (P10 ×1.55) and converge on the tail — the
  opposite arrangement from the bottom-up chain, whose spread was a level.
- Both runs flag the same two cross-sensor issues before ever seeing the other sensor: the
  **net-vs-booked person-day convention** (±15–25%, and the rate table uses the same "net 8 h"
  wording — the diagnostician must decide whether the conventions actually match), and **where
  divergence is informative**: RC26-1 states that upper-quantile divergence against a bottom-up is
  expected by construction (A6 lives only here), while **P50 divergence is the signal**.
- Both runs' misclassification tables put more weight above than below — the class's own reading of
  which way it errs.
