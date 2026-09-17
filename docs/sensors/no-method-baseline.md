# Sensor note — the no-method baseline (a control, not a sensor)

**Eight sections:** 1 how it was conceived · 2 the question it answers · 3 what its width means ·
4 what it sees and must never see · 5 measured properties · 6 how to read a reading · 7 versions ·
8 what we want to add. Sections 2–7 are what the sensor is; 1 is what it was meant to be; 8 is what
it may become. **This note is expected to disagree with the code** — the disagreement is the record of
what came from the idea, what was added, and what arrived by accident.

Engine: none — that is the point. Run by hand: the pinned prompt of the case, n = 10, sent to a
general agent with no definition. Curve on the panel: a family of thin curves, one per run, never
pooled.

---

## 1. How it was conceived

**The idea.** A control, not a method. By 2026-08-07 every version of the decomposition sensor had
been judged only against earlier versions of itself; nothing had established that the method was
doing the work rather than the pinned prompt and the assumption log (`run14` head). So: the same
words, the same log, the same session, the same model, launched simultaneously — with the method
removed and nothing else changed.

**What it was meant to buy.** A floor for repeatability. Whether pinning constants was buying
anything.

**What arrived unplanned.**
- **The floor was below the method.** CV 8.55% with no method against 9–17% with one; no version
  significantly beat it (`docs/review_2026-08-21_running_in_circles.md` E1–E3). This one number
  closed the constant-pinning programme and is the origin of the chain.
- **It became the level comparator too.** Run on the one case with a fact (run 41), it made the
  question "is the chain closer than a bare prompt?" answerable — and the answer turned on a
  conversion constant: at 5–6 net hours per present day the chain is closer, at ≈7 the baseline is,
  crossover 6.63. The author pinned the conversion the same day (`docs/constants.md` §4a). Under it,
  chain ×1.21 low, baseline ×1.47 high, n = 1 — "not shown to buy accuracy; no longer shown to lose
  to a bare prompt either" (`docs/status_2026-08-27.md` §5).
- **The measurement itself does not reproduce.** The identical prompt a day later moved the level
  ×1.145 with the same CV (run 43). The author had read the three-curve chart and said of this curve
  "I suspect it is volatile"; it was, at batch level rather than run level.
- On SAS it landed ×0.75 *below* the raw chain — the inverse of FaxRxTx — with a ×1.92 spread
  (run 49). The sign of its disagreement with the chain is not stable across cases.

## 2. The question it answers

*What does one capable reader with no method, given only the source and the assumption log, say the
project costs?* It answers what the corpus prior says about this text. It is the thing every method
has to beat, on spread and on level, to be worth its cost.

## 3. What the width of its curve means

**Sampling of the model's prior on the magnitude** — n draws of the same question. Within a batch:
CV 8.5–14% on one model, 21% on another. Between batches on the same day-old prompt: a level shift
of ×1.145 that the within-batch width does not contain. The family is drawn as thin curves and
**never pooled**: a pooled curve would hide both the spread and the batch shift, and the family *is*
the reading. Each run's own declared range is not a corridor of anything.

## 4. What it sees and what it must never see

It sees a bare instruction, the **source description** and the **assumption log**, verbatim. It does
**not** see `requirements_pinned.md`: extracting that list is the method's first act, and handing it
over would credit the baseline with work the chain performs (runs 41, 49). Nothing else is withheld —
there is no method to protect. Unit is imposed by the prompt (run 41's: 1 pm = 21 person-days = 168
task hours, leave outside) so the three baselines on record compare without conversion.

There are no blind spots to list because there is no method to have them. What it cannot see is
whatever the corpus did not see.

## 5. Measured properties

| property | value | run |
|---|---|---|
| BMS, one model, n = 10 | mean 1074 pd, **CV 8.55%** | run 14 |
| BMS, the other model, n = 10 | mean 762, CV 20.92% | run 16 |
| FaxRxTx, n = 10, against a fact | mean 120.5 A9 pm, CV 13.75%, max/min 1.722, mean pairwise ratio 1.168; **×1.47 high** under the pinned conversion; accuracy undecidable before it | run 41 |
| FaxRxTx, same prompt a day later, n = 10 | mean 138.0, CV 13.47%; **level ×1.145 up** with identical injected material in both batches | run 43 |
| SAS, n = 10 | ×0.75 below the raw chain; spread ×1.92 across runs | run 49 |
| FaxRxTx, a third batch, n = 10 | mean 125.0, CV 8.6%, max/min 1.38 — inside the two earlier batches | run 69, round 1 |
| FaxRxTx, the same ten after one Delphi exchange (each reads all ten replies, anonymous and verbatim, and revises or holds) | max/min 1.38 → **1.08**, median 122.5 → 126.5; against the fact ×1.53 → ×1.56; declared ranges containing the fact 4 of 10 → 1 of 10. **Agreement without accuracy:** the family's width is sampling noise and collapses on contact, its level is the model's prior on the text and does not move | run 69 |
| FaxRxTx, a fixed list of seventeen lines (one rule-bound panel's) sized in secret by forty bare agents, no exchange; a group's figure = sum of per-line medians | groups of ten x1.03 apart (random pairs x1.04; debating panels x1.10-1.17); own totals 130-237, one scale factor per estimator (lines correlate 0.80); level 174 pm, **x2.13 of the fact** - above every panel: a list handed over as fixed is sized dearer than by its authors. **Averaging buys stability, not level; the list is the remaining freedom** | run 74 |
| what it is the comparator for | gate v2.0 test 1: the chain's end-to-end ×1.0532 is 3.0× tighter than the baseline's own pairwise agreement | run 42 vs 41 |

## 6. How to read a reading

- Read it as a **band on the same axis**, not as an estimate: where a fast, unstructured answer
  lands, so that every method's claim to have done more can be checked against it.
- The within-batch CV is the model's day; the batch-to-batch shift is the model's week. Neither is
  the project.
- On a case with a fact, read the baseline's miss beside the chain's — they have opposite signs on
  FaxRxTx and SAS, and n is 1 on each. Nothing about accuracy follows from either alone.
- All ten runs on every batch reported `tool_uses: 0` (or exactly the one permitted Read on SAS) and
  quarantined the ambient git status unprompted; that is a property of the harness, not of the
  method, and it is what makes the batch a control.

## 7. Versions

There is no engine and nothing to bump. The pinned prompts are the versions:

| case | prompt | md5 (LF) |
|---|---|---|
| BMS | `prompt_decomposition_BMS.txt` + the no-file, `TOTAL:` wrapper | `c33affd7…` |
| FaxRxTx | `run41_raw/prompt_baseline_faxrxtx.txt` | `c17b874b…` |
| SAS | `run49_raw/prompt_baseline_sas.txt` (40 KB, read via one permitted tool call) | `9d71b4c7…` |

## 8. What we want to add or change

| idea | would move | where it lives |
|---|---|---|
| **Run it on every case, every model, as protocol** — it is the only whole-pipeline repeatability figure the project had until run 42, and the comparator for gate test 1 | measurement | `BACKLOG.md` "Protocol" |
| **A third model family** — ×2 between two models of one vendor may be the general scale of model disagreement or a property of the pair | spread across models | `BACKLOG.md` "Consequences of σ_model" |
| **Keep the batch-shift on the panel** — two batches on one case are two families, not one; the report draws each bare run, the batch identity should be visible too | report only | `tools/report/build_report.py`, no-method family |
