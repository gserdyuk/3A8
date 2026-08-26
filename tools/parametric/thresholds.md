# Complexity thresholds — pinned from run 38

**Pinned 2026-08-26** from two independent gap-blind `Hotyn-N 1.0` runs with exact agreement on
every boundary value (`tools/parametric/run38_raw/`). Standard stated by both runs: **IFPUG CPM
4.x / ISO/IEC 20926, unadjusted**. This file and `weights.tsv` are the numeric half of
`docs/fp_counting_rules.md`; `Hotyn-P` receives these matrices and never the weights.

**ILF and EIF** (shared matrix; record types × data elements):

| RETs \ DETs | 1–19 | 20–50 | 51+ |
|---|---|---|---|
| 1 | Low | Low | Average |
| 2–5 | Low | Average | High |
| 6+ | Average | High | High |

**EI** (files referenced × data elements):

| FTRs \ DETs | 1–4 | 5–15 | 16+ |
|---|---|---|---|
| 0–1 | Low | Low | Average |
| 2 | Low | Average | High |
| 3+ | Average | High | High |

**EO and EQ** (shared matrix; files referenced × data elements):

| FTRs \ DETs | 1–5 | 6–19 | 20+ |
|---|---|---|---|
| 0–1 | Low | Low | Average |
| 2–3 | Low | Average | High |
| 4+ | Average | High | High |

Rule both runs flagged as the commonly-misremembered point, stated deliberately by each: **EQ is
graded on the EO/EQ matrix over its combined input and output sides, and takes the EI weight row
(3/4/6), not the EO row.**

Provenance stamp: `first approximation from the published standard, v0.1 — pinned on cross-run
agreement, run 38, n=2, exact`.
