# Run 41 — FaxRxTx, the no-method baseline, n = 10

**What this is.** The `run14` experiment (BMS, 2026-08-07) repeated on the one case that has a
documented outcome. Ten runs of one pinned prompt sent to a general agent with **no method
definition of any kind**, to establish what the bare corpus produces on this input — the floor the
whole `Hotyn` chain must beat to be worth its cost.

Registered in `docs/status_2026-08-27.md` §7 as action 2, and in `BACKLOG.md` under TODO 2026-08-27.

## Inputs, pinned before the batch

| input | value |
|---|---|
| prompt | `prompt_baseline_faxrxtx.txt`, md5 `c17b874b1101f32f6d8c1ff7a151e7df` (LF form), 11 744 bytes |
| its content | a bare instruction + `SYSTEM.md` verbatim + `assumptions.md` (A1–A9) verbatim |
| engine | none — a general agent, no sensor definition |
| model | `claude-opus-5`, the same model coordinate as runs 29–31 (the chain this is compared against) |
| n | 10, launched simultaneously, no run seeing another |
| isolation | "use no tool of any kind"; **every run reported `tool_uses: 0`** |

## Why the source text and not `requirements_pinned.md`

The extraction of `SYSTEM.md` into 52 pinned obligations **is already the first act of the method**.
Handing the baseline that artefact would credit it with work the chain performs. The baseline gets
what a person would get: the recollection document and the assumption log.

## What was asked of the output, and why it is not contamination

Each run had to close with `TOTAL` in the A9 person-month convention, a `RANGE`, an implied
`TEAM x DURATION`, and a `DECLARATION` of what the number contains. **None of that says how to
estimate.** The unit declaration is the same requirement every number-producing role in this project
has carried since 2026-08-25; `TEAM x DURATION` exists because the fact is recorded as heads ×
months, and asking for the answer in the fact's own shape removes a conversion from the comparison
rather than adding one.

## Protocol fact — the injection, caught 10 times out of 10

Every run reported, unprompted, that ambient repository material reached it: git branch, status and
**recent commit subjects naming this very case** — "run 40", "Hotyn-P counts FaxRxTx twice",
"UFP 78 vs 82", "the enumeration floor" — plus the memory index and tool listings. Several runs said
outright that these looked like leaked prior results for the object under estimate and quarantined
them explicitly.

**Assessment.** No effort figure appears in those subjects; the leaked numbers are function-point
counts, which cannot anchor a person-month estimate. The batch stands. But this is now the **sixth**
independent catch of the same defect, and the standing backlog item to strip `gitStatus` from sensor
launches is no longer a tidiness matter — a commit subject one word different would have carried a
person-month figure straight into a blind run.
