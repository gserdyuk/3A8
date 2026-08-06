# BMS — Run 7: variance of the pinned instrument (raw data)

Date: 2026-08-05. Ten runs of `estimator-decomposition` under the pinned constants C1–C4, on
byte-identical prompts — the same prompt used for the unconstrained baseline of run6.
Before the batch, the agent was probed for its constants and reported them correctly (ceiling 10,
ten branches including migration, no merging, C4 list given), so the runs are known to have used
the new definition.

Baseline for comparison (run6, unconstrained): mean 1147, sd 200, CV 17.4%, range 894–1525.

## Batch A (runs 1–5)

| Run | ΣE | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback nodes | M in >10 | Branch 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1375.2 | 123 | 828.7 | 546.5 | 39.7% | 23 | 0 | 0 | 42.5 |
| 2 | 1219.8 | 115 | 838.8 | 381.0 | 31.2% | 18 | 0 | 0 | 40.5 |
| 3 | 1287.0 | 138 | 849.0 | 438.0 | 34.0% | 17 | 0 | 0 | 60.7 |
| 4 | 1125.3 | 119 | 753.3 | 372.0 | 33.1% | 14 | 0 | 0 | 32.5 |
| 5 | 1127.8 | 116 | 717.3 | 410.5 | 36.4% | 14 | 0 | 0 | 29.5 |

## Batch B (runs 6–10)

| Run | ΣE | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback nodes | M in >10 | Engine stamp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 6 | 1397.0 | 127 | 936.0 | 461.0 | 33.0% | 21 | 0 | 0 | Kosiv 1.0 |
| 7 | 1436.0 | 133 | 947.0 | 489.0 | 34.1% | 36 | 0 | 0 | Kosiv 1.0 |
| 8 | 1185.8 | 132 | 803.8 | 382.0 | 32.2% | 16 | 0 | 0 | Kosiv 1.0 |
| 9 | 1377.8 | 123 | 910.3 | 467.5 | 33.9% | 20 | 0 | 0 | Kosiv 1.0 |
| 10 | 1310.9 | 125 | 892.4 | 418.5 | 31.9% | 11 | 0 | 0 | Kosiv 1.0 |

## Results

| Quantity | Lytin-D 0.9 (unpinned) | Lytin-D 1.0 (pinned) |
|---|---:|---:|
| Mean | 1147 | **1284** |
| Median | 1124 | 1299 |
| Standard deviation | 200 | **114** |
| **Coefficient of variation** | **17.4%** | **8.9%** |
| Min … max | 894 … 1525 | 1125 … 1436 |
| max / min | 1.70 | **1.28** |
| Leaf count (CV) | 80 (10.0%) | 125 (6.0%) |
| Price per leaf (CV) | 11.0 pd (15.9%) | 6.8 pd (8.0%) |
| Integration share | 23.1% | 34.0% |

**The spread halved: 17.4% → 8.9%,** and the extremes moved from a factor of 1.70 apart to 1.28. The sd ratio is 0.57 with a relative standard error of about 24% on each sd, so the narrowing is larger than the measurement noise on it.

**The level rose 12%** (1147 → 1284). The pre-registered prediction — after its correction — said the direction was unknown and plausibly upward, and upward is what happened. The mechanism is visible in the components: the leaf ceiling pushed the leaf count from 80 to 125 and the price per leaf from 11.0 down to 6.8, so 125 × 6.8 ≈ 848 against 80 × 11.0 ≈ 880 — the *leaf* sums are almost unchanged, and the whole +137 pd came from the seam side, where the fixed rate card produced 34% of the total against 23% before.

Where the residual spread now sits (exact log-variance decomposition, no ratio artifacts):

| Factor | sd in log space | Share of Var(log total) |
|---|---|---|
| Price per leaf | 0.081 | 61.5% |
| Leaf count | 0.060 | 30.7% |
| Integration factor | 0.039 | 7.8% |

Price per leaf is still the largest contributor but its own spread fell by half (15.9% → 8.0%), which is what a ceiling should do. The integration factor is no longer a damper but a small positive contributor.

## A confound I introduced, and a belief that was wrong

The two batches differ: A gives 1227 ± 107, B gives 1342 ± 98, a difference of +114 pd (1.8 standard errors — suggestive, not conclusive). They should not differ at all, because they were meant to run the same definition.

They did not. Every batch-B run reports the stamp **`Kosiv 1.0`** — a name that existed only between two edits made *after* batch A returned and *before* batch B was launched, and which had already been renamed to `Lytin-D 1.0` in the file by launch time. So agent definitions are **not** simply read once at session start, as was believed after the earlier experiment with a *newly created* agent; a *modified* definition is picked up mid-session, with a lag that put batch B on an intermediate snapshot.

The practical damage is limited — the C1–C4 constants were identical in both snapshots, and only the engine-identity paragraph differed — but the discipline was broken: an instrument was edited during its own measurement, on the strength of a belief about the harness that had been verified for a different case. Both batches are kept above with their stamps, and the pooled n = 10 is reported as the headline because the constants were the same; a reader who wants a clean single-snapshot sample should use batch B alone (mean 1342, CV 7.3%).

**Rule for next time:** no edit to an agent definition — not even a comment — between the first and last run of a measurement.

## Compliance with the constants

Across all ten runs: **no leaf with M > 10**, no leaf below 1 pd, no merging, no C1 exception claimed, and **zero** of the ~200 node items fell back to the 15% rule. All ten runs filled all ten branches, including branch 9, which every run read as a genuine (if thin) migration off a manual predecessor rather than as greenfield.

## Observations recorded as they arrive

- **C1 was obeyed in every run of batch A:** no leaf with M > 10, no leaf under 1 pd, no merging, and
  no C1 exception claimed. The `5–10` bucket holds 78–91% of leaves in every run; the rest sit in
  `3–4`, which the rule permits (naturally small standalone work that may not be merged upward).
- **C3 was obeyed:** all 86 node items across the five runs were priced from counted seams; **zero**
  fell back to the 15% rule.
- **Branch 9 was filled by all five runs, not marked greenfield.** The prediction before the batch was
  the opposite. Every run read the manual booking process as a predecessor carrying real migratable
  content — supplier catalogues, negotiated rates, in-flight bookings — plus a parallel-run period,
  and three of the five explicitly flagged the branch as *thin* because the predecessor is a process
  rather than a system. The branch ranges 29.5–60.7 pd, a factor of 2.1 — the widest relative spread
  of any branch, which is what a newly introduced category looks like before its content settles.
- **Integration share rose sharply**: 31–40% here against 17–29% in the unconstrained baseline. The
  fixed rate card meets a seam-dense domain and produces more than the invented cards did; the top
  assembly node alone is 93–141 pd. This is the single largest structural difference between the two
  instruments and it needs its own diagnosis once the full sample is in.
