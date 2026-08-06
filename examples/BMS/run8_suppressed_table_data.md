# BMS — Run 8: what happens when the leaf table is not printed (raw data)

Date: 2026-08-05. Ten runs of `estimator-decomposition`, engine `Lytin-D 1.0`, definition file **not modified**
before, during or after the batch. All ten launched simultaneously so that no edit could fall between the first
and the last run — the discipline that run7 broke.

**Input:** `prompt_decomposition_BMS.txt`, md5 `c33affd709792dfe60531daa3cb42d65` — byte-identical to the prompt
used for run6 (unpinned baseline) and run7 (pinned baseline), plus one appended block:

> The method is unchanged. Build the full tree, split to the C1 leaf size, estimate every leaf with PERT, price
> every node's seams at the C3 rates. Only the reporting changes: replace output §2 and §3 (the WBS tree and the
> table of leaves) with per-branch subtotals. §1, §4–§8 unchanged; §6 must carry the exact leaf count and the
> full M-distribution.

**Pre-registered prediction, recorded before launch:** the level would go **down**, on the reasoning that the
unpacking effect (Tversky & Koehler) runs in both directions and less enumeration should mean a smaller total.
Magnitude not predicted.

## Raw data

| Run | ΣE | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback nodes | M in >10 | Stamp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S-1 | 1777.7 | 175 | 1223.7 | 554.0 | 31.2% | 22 | 0 | 0 | Lytin-D 1.0 |
| S-2 | 1762.0 | 167 | 1197.5 | 564.5 | 32.0% | 25 | 0 | 0 | Lytin-D 1.0 |
| S-3 | 1741.5 | 169 | 1194.5 | 547.0 | 31.4% | 18 | 0 | 0 | Lytin-D 1.0 |
| S-4 | 1908.5 | 166 | 1209.5 | 699.0 | 36.6% | 43 | 0 | 0 | Lytin-D 1.0 |
| S-5 | 1790.4 | 165 | 1206.9 | 583.5 | 32.6% | 35 | 0 | 0 | Lytin-D 1.0 |
| S-6 | 1484.9 | 157 | 1127.9 | 357.0 | 24.0% | 11 | 0 | 0 | Lytin-D 1.0 |
| S-7 | 1684.7 | 146 | 1014.7 | 670.0 | 39.8% | 31 | 0 | 0 | Lytin-D 1.0 |
| S-8 | 1745.5 | 171 | 1269.5 | 476.0 | 27.3% | 18 | 0 | 0 | Lytin-D 1.0 |
| S-9 | 1480.7 | 143 | 1023.7 | 457.0 | 30.9% | 14 | 0 | 0 | Lytin-D 1.0 |
| S-10 | 1771.7 | 180 | 1280.2 | 491.5 | 27.7% | 20 | 0 | 0 | Lytin-D 1.0 |

## Result

| Quantity | Lytin-D 1.0, table printed (run7) | Lytin-D 1.0, table suppressed (run8) |
|---|---:|---:|
| Mean ΣE | 1284 | **1715** |
| Standard deviation | 114 | 135 |
| **Coefficient of variation** | **8.9%** | **7.8%** |
| Min … max | 1125 … 1436 | 1481 … 1909 |
| max / min | 1.28 | 1.29 |
| Leaf count (mean) | 125 | **164** |
| Price per leaf (mean, CV) | 6.8 pd (8.0%) | 7.17 pd (**2.0%**) |
| Integration share | 34.0% | 31.4% |
| Aggregation nodes (mean, CV) | 19.0 (36.7%) | 23.7 (42.0%) |

**The prediction was wrong, and not marginally.** The level rose by **+430 pd, +33.5%**, which is **7.7 standard
errors** of the difference. Direction predicted: down. Direction observed: up. The unpacking argument was applied
to the wrong variable — it assumed the printed table *is* the enumeration, when the printed table is a *cost on*
the enumeration.

**The spread did not improve.** CV fell from 8.9% to 7.8%, but that is arithmetic: the standard deviation actually
grew (114 → 135) and the ratio only fell because the mean grew faster. max/min is 1.29 against 1.28 — unchanged.
Suppression bought nothing in repeatability.

## Where the level went

The rise is almost entirely on the **leaf side**, which is the opposite of run7, where it was entirely on the seam side.

- Leaf count: 125 → 164 (**+31%**)
- Price per leaf: 6.8 → 7.17 pd (+5%)
- Integration share: 34.0% → 31.4% (down)

The most plausible mechanism: **printing 160 rows is expensive, and that expense was silently braking the
splitting rule.** With the table suppressed, the marginal cost of one more leaf falls to nearly zero, and the tree
grows to what C1 actually implies. If that reading is right, then run7's 125 leaves were not the tree C1 specifies —
they were the tree C1 specifies minus whatever the reporting burden suppressed. The output format was doing part of
the estimating.

## Where the residual spread now sits

Exact log-variance decomposition on the identity **total = leaf count × price per leaf × (1 + integration/leaf sum)**
(verified to zero error in log space):

| Factor | sd in log space | Share of Var(log total) |
|---|---|---|
| Leaf count | 0.075 | **62.2%** |
| Integration factor | 0.067 | **33.9%** |
| Price per leaf | 0.020 | 3.9% |

Compare run7: price per leaf 61.5%, leaf count 30.7%, integration 7.8%. **The dominant term changed completely.**

Price per leaf — the thing C1 was written to control — is now essentially controlled: its own spread fell 15.9% →
8.0% → **2.0%** across the three specifications. The variance did not disappear; it moved to the two parameters
that were never pinned.

## The unpinned parameter this run exposed: node count

C3 fixes the *price* of a seam. Nothing in the method fixes **how many aggregation nodes a tree has**, and that turns
out to be the widest-swinging quantity in the instrument:

- Node count ranges **11 … 43**, CV **42.0%** — wider than any other reading.
- corr(nodes, Σ integration) = **0.90**
- corr(nodes, integration share) = 0.77
- corr(nodes, total) = 0.75

More nodes means more seams to count means more integration. Two runs on identical input built 11 and 43 nodes over
the same project. This is a free parameter of the same kind as the leaf ceiling was before C1, and it is now the
second-largest contributor to the spread.

## Compliance — the part that did hold

Across all ten runs, without exception:

- No leaf with M > 10; the `>10` bucket empty in every run; no C1 exception claimed.
- No leaf below 1 pd; no merging.
- **Zero** of the ~237 node items fell back to the 15% rule — all priced from enumerated seams.
- All ten branches filled in all ten runs, including branch 9.
- All ten stamped `Lytin-D 1.0`.
- All ten independently reported the `Kosiv 1.0` / `Lytin-D 1.0` defect in output §6 and stated they treated the
  identity section as authoritative.

The rule-following half of the instrument is solid. The quantitative half is not, and the two should not be
confused: perfect compliance with C1–C4 still permits a 33% level shift from a change to the output format alone.

## Conclusions

1. **The leaf table cannot be switched off to make regression runs cheaper.** Not because of cost — cost barely
   moves — but because the resulting readings are from a different instrument, off by 33% in level.
2. **A version number must cover the output format.** Suppressed-table mode is not `Lytin-D 1.0` with less printing;
   it is a different major version, and comparing its numbers with run7's would be an error of exactly the kind the
   stamp convention exists to prevent.
3. **Two free parameters remain and now carry 96% of the variance**: how many leaves the tree has (62%) and how many
   aggregation nodes it has (34%, via the integration factor). Pinning the price of a leaf was necessary but has
   turned out not to be sufficient.
4. **A finding about run7 itself**: its level is partly an artifact of the reporting burden, not purely of C1–C4.
   That does not invalidate its CV of 8.9%, which is a repeatability measure at a fixed configuration, but it does
   mean the number 1284 belongs to the configuration and not to the method.

## Retraction carried over from run7

The `Kosiv 1.0` stamps in run7 batch B were **not** evidence that a modified agent definition is picked up
mid-session. Line 101 of the definition instructs §6 to open with `(Kosiv 1.0)` while line 15 assigns
`Lytin-D 1.0`; batch B agents were obeying §6. The run7 conclusion about mid-session definition loading is withdrawn
as unsupported. The rule it produced — never edit an instrument between the first and last run of a measurement —
stands on its own merits and was honoured in this run.

The §6 defect is still present in the definition file and must be fixed as a minor version (`Lytin-D 1.1`) after
this measurement, not during it.
