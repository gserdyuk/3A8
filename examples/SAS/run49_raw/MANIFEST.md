# Run 49 — SAS, the no-method baseline, n = 10

**What this is.** The run 41/43 experiment (FaxRxTx) repeated on case 3: ten runs of one pinned
prompt sent to a general agent with **no method definition of any kind**, to place a fast,
unstructured answer on the same axis as the chain and the two class readings. SAS has no outcome,
so the result is a distance, not a score.

## Inputs, pinned before the batch

| input | value |
|---|---|
| prompt | `prompt_baseline_sas.txt`, md5 `9d71b4c7039e5adcd5477c75c7439732` (LF form), 40 286 bytes |
| its content | a bare instruction + the RFP §1–2 verbatim + the assumption log v1 (the sanitised form the class sensors saw) |
| unit imposed | 1 pm = 21 person-days = 168 hours of work on the task, leave outside — the run 41 convention, so the three baselines compare without conversion |
| engine | none — `general-purpose` agent, no sensor definition |
| model | the harness's `opus` alias, i.e. Claude Opus 5 — the same model coordinate as runs 44–48 |
| n | 10, launched simultaneously 2026-09-08 ~12:35, no run seeing another |
| isolation | **deviation from run 41, declared:** the prompt is 40 KB, too long to paste ten times, so each run was told to read exactly this one file and use no other tool. Expected `tool_uses: 1` per run (the one Read); anything above 1 is a protocol fact to record |

## Why the RFP text and not `requirements_pinned.md`

The extraction of the RFP into 153 pinned obligations **is already the first act of the method**.
Handing the baseline that artefact would credit it with work the chain performs. The baseline gets
what a person would get: the document and the assumption log.

## Readout, declared before any reply arrived

Each run's `TOTAL` and `RANGE` (its own P10…P90) are read as stated, in the imposed unit, and each
run's range is fitted as a lognormal (median = TOTAL, sigma from the P10–P90 span) — **ten thin
curves on the report, not one pooled curve**, per the run 43 finding that a single curve asserts a
stability the instrument does not have. Comparators on the same axis, in net task hours: the raw chain
38 118, the calibrated centre 57 600, the class medians 24 510 and 47 880 (house 0.75). Statistics as
run 41: mean, median, sd, CV, max/min, and each run's declared corridor width against the spread of
the ten medians.

A second batch a day later (run 50) is the planned control on the level; a reminder is set.
