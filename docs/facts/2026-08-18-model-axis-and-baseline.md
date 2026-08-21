# Facts pack — 2026-08-18 — baseline, σ_model, C6 scored, projection axes

Covers: run14, run15, run16, the C6 prediction scoring, and the first half of run17.
Repository state at close: `3e9c5d0`.

---

# 1. MEASURED

Every batch of the decomposition sensor on BMS that is on record, oldest first. All figures are
person-days; CV is the sample coefficient of variation of ΣE across the batch.

| batch | engine | model | axis | n | mean ΣE | CV | leaves | Σ leaf E | integ. share | multiplier |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| July manual | `D 0.1` | **not recorded** | mixed | 1 | 486 | — | 26 | — | — | — |
| run6 | `D 0.9` | **not recorded** | mixed | 10 | 1147 | 17.4% | — | — | — | — |
| run7 | `D 1.0` | **not recorded** | mixed | 10 | 1284 | 8.9% | 125 | — | 34.0% | — |
| run9 | `D 1.0` | **not recorded** | mixed | 10 | 1410 | 10.0% | 133 | — | 30.6% | — |
| run11 | `D 2.0` | **not recorded** | mixed | 10 | 1518 | 10.8% | 139.8 | — | 32.3% | — |
| run12 | `D 2.3` | **not recorded** | mixed | 10 | 1668 | 9.85% | 148.7 | — | 33.3% | — |
| run13 | `D 3.0` | **not recorded** | mixed | 10 | 1673.8 | 10.86% | 152.4 | — | 34.5% | 1.527 |
| run14 | **none** | Opus 5 | — | 10 | 1074.0 | 8.55% | 10–19 items | — | — | — |
| run15 | **none** | Sonnet 5 | — | 10 | 762.5 | 20.92% | 10–21 items | — | — | — |
| run16 | `D 4.0` | Opus 5 | mixed | 10 | 1625.5 | 9.25% | 157.3 | 1062.7 | 34.65% | 1.530 |
| run16 | `D 4.0` | Sonnet 5 | mixed | 10 | 804.2 | 11.56% | 79.9 | 532.2 | 33.78% | 1.510 |
| run17 | `D 5.0` | Opus 5 | **S** | 5 | 1458.7 | 6.23% | 132.6 | 937.2 | 35.74% | 1.556 |
| run17 | `D 5.0` | Sonnet 5 | **S** | 5 | 710.0 | 17.54% | 70.8 | 469.9 | 33.63% | 1.507 |
| run17 | `D 5.0` | Opus 5 | **P** | — | *outstanding* | | | | | |
| run17 | `D 5.0` | Sonnet 5 | **P** | — | *outstanding* | | | | | |

**Model not recorded is itself a measurement.** Seven batches and roughly seventy runs predate the
decision to stamp the model, and the coordinate cannot be recovered.

Per-run raw data: run13 §Raw data, run14 §Raw data, run15 §Raw data, run17 §Raw data. run16 per-run
figures exist only in the scratchpad of a closed session and are **not** in the repository; the batch
means above are.

## 1.1 Split-check (C6) discrepancy, by batch

| batch | mean signed discrepancy |
|---|---:|
| `4.0` × Opus | +28.9% |
| `4.0` × Sonnet | +24.6% |
| `5.0` S × Opus | +15.6% |
| `5.0` S × Sonnet | +4.6% |

## 1.2 Contamination and tool discipline

- All 20 baseline runs (run14, run15): `tool_uses: 0`.
- `4.0` × Opus, 10 runs: **0** tool calls. `4.0` × Sonnet, 10 runs: **2 runs made calls** (1 and 3), Glob only.
- Version probe answered `Lytin-F 4.0` before run16 and `Lytin-F 5.0` before run17, on both models.
- `.claude/agents/estimator-decomposition.md:131` named `examples/BMS/run12_seam_readout.md`. One Opus run
  reported declining to open it. Removed in `298eefd`.
- `calibration-rates` was **not** registered as an available agent in the run16 session although the file
  exists on disk. The other four were. Not investigated.

---

# 2. DERIVED

Arithmetic on §1, shown so it can be rechecked.

## 2.1 Model effect

| comparison | ratio | test |
|---|---:|---|
| baseline: Opus ÷ Sonnet (1074.0 ÷ 762.5) | **1.409** | t = 5.35, n = 10+10 |
| `D 4.0` mixed axis (1625.5 ÷ 804.2) | **2.021** | t = 14.70 |
| `D 5.0` axis S (1458.7 ÷ 710.0) | **2.055** | n = 5+5 |
| `D 5.0` axis S, on leaf E (937.2 ÷ 469.9) | **1.994** | |

## 2.2 What holds across models and what does not (`D 4.0`, n = 10 each)

| parameter | Opus | Sonnet | ratio | test |
|---|---:|---:|---:|---|
| price per leaf (Σ leaf E ÷ leaves) | 6.763 | 6.661 | 1.015 | **t = 0.51** |
| integration share | 34.65% | 33.78% | 1.026 | |
| implied multiplier | 1.530 | 1.510 | 1.013 | |
| module count | 24.8 | 19.6 | 1.265 | |
| **leaf count** | **157.3** | **79.9** | **1.969** | **t = 18.07** |

Decomposition of the ×1.97: 1.265 (modules) × 1.534 (leaves per module) = 1.941.

## 2.3 Arithmetic on granularity

For Sonnet to carry the Opus 1062.66 leaf-pd in 79.9 leaves, the mean leaf must be **13.30 pd**.
C1 caps M at 10; E rarely exceeds 11; every Sonnet run reported `>10: 0`.

## 2.4 Method effect, by model (`D 4.0` against baseline)

| | Opus | Sonnet |
|---|---:|---:|
| baseline → `4.0`, level | ×1.513 | ×1.055 |
| baseline → `4.0`, CV | 8.55% → 9.25% | 20.92% → 11.56% |

## 2.5 C2 removal (`4.0` → `5.0` axis S)

| | Opus | Sonnet |
|---|---:|---:|
| level | −10.3% | −11.7% |
| CV | 9.25% → **6.23%** | 11.56% → **17.54%** |

6.23% is the lowest CV recorded for any batch of this instrument, and is below the methodless
baseline of 8.55%.

## 2.6 Spread comparisons that clear significance

Variance ratios against F(9,9), two-tailed 5% critical value **4.03**:

| comparison | ratio | verdict |
|---|---:|---|
| baseline Sonnet ÷ baseline Opus (20.92 ÷ 8.55)² | 5.99 | **significant** |
| `4.0` Sonnet ÷ `4.0` Opus (11.56 ÷ 9.25)² | 1.56 | not significant |
| `4.0` Opus ÷ baseline Opus (9.25 ÷ 8.55)² | 1.17 | not significant |
| baseline Sonnet ÷ `4.0` Sonnet (20.92 ÷ 11.56)² | 3.28 | not significant |
| `3.0` ÷ `4.0` Opus (10.86 ÷ 9.25)² | 1.38 | not significant |

**One spread difference in the whole history of the project clears significance, and it is a model
difference.**

## 2.7 Standard error of a batch mean

| batch | SEM |
|---|---:|
| baseline Opus | 2.70% |
| baseline Sonnet | 6.62% |
| `4.0` Opus | 2.92% |
| `4.0` Sonnet | 3.66% |

n needed on baseline Sonnet to reach the Opus baseline 2.70%: **60**. To reach 3.44%: **37**.

## 2.8 Declared uncertainty versus measured spread (baseline runs)

Mean self-declared range = **43% of the point estimate** (about ±21%), against a measured between-run
p10–p90 of about ±11%.

## 2.9 C6 discrepancy against splitting depth

| set | leaves per module | Pearson r | Spearman |
|---|---:|---:|---:|
| `4.0` Opus | 6.38 | −0.285 (t = −0.84) | −0.285 |
| `4.0` Sonnet | 4.16 | −0.304 (t = −0.90) | −0.297 |
| **pooled, n = 20** | 3.09 … 7.55 | **−0.035** (t = −0.15) | +0.014 |

---

# 3. PREDICTIONS

Registration is verifiable in the history: in each case the predictions were committed **before** the
commit carrying the result.

## 3.1 C6 — registered `5f82cdb`, scored `21071a0`

| # | prediction | outcome |
|---|---|---|
| 1 | mean discrepancy positive, +5…+20% | **partial** — sign right beyond doubt, magnitude +28.9%, 8 of 10 runs above the band on each model |
| 2 | **discrepancy grows with splitting depth** | **failed** — r = −0.035 pooled over n = 20 |
| 3 | level does not move from `3.0` | **confirmed** — −2.9%, t = −0.65 |
| 4 | spread does not narrow | **confirmed** — 9.25% against 10.86% |

Prediction 2 was named in the proposal as the prediction that matters.

## 3.2 C7 — registered `5afe9df`, **not run**

Six predictions. The one named as decisive: cross-model ratio below ×1.4, from 2.021; at ×1.7 or above the
rule is to be reverted rather than tuned.

## 3.3 Projection axes — registered `0f2cec0`, half scored in `3e9c5d0`

| # | prediction | status |
|---|---|---|
| 1 | axis effect on ΣE below ×1.4 | **outstanding** — needs axis P |
| 2 | Σ leaf E converges better than ΣE, ratio below ×1.25 | **outstanding** — needs axis P |
| 3 | spread rises with C2 gone, Opus CV into 12…20% | **inverted on Opus (6.23%), confirmed on Sonnet (17.54%)** |
| 4 | level falls 10…30% on Opus | **confirmed at the lower edge** — −10.3% |
| 5 | first level stable within an axis, different between axes | **provisional** — within-axis stability high on both models; the between-axis half is outstanding |
| 6 | testing placed in ≥4/5 runs; transition in <3/5 | **outstanding** |

Prediction 3 was registered **with its opposite named**: a fall in CV would mean C2 was itself a source of
variance, not a control on it.

---

# 4. READINGS

Interpretation, not measurement. Separated deliberately so that a later analysis can discard any of it
without touching §1–§3.

1. **Constraining an output property works; constraining the transformation was never attempted.** Every
   pinned parameter — leaf price, integration rate, multiplier — holds across models to within 3%. The one
   thing never constrained, how requirements become work, carries ×1.97.
   *Basis: §2.2. The causal claim is not tested.*
2. **The ×1.97 is coverage, not granularity.** Splitting conserves the sum, and 13.30 pd per leaf is not
   expressible under C1.
   *Basis: §2.3. Close to a derivation, but rests on the premise that both trees describe the same project,
   which is not independently established.*
3. **The constants act as a floor, not a narrower.** They changed the Opus spread not at all and halved the
   Sonnet one.
   *Basis: §2.4. The Sonnet narrowing does not clear significance — see §2.6.*
4. **C2 was a source of variance on the strong model and a floor on the weak one.**
   *Basis: §2.5. The proposal pre-committed to the first half of this reading; the second half is new and
   unregistered.*
5. **The version table measures something smaller than the platform it runs on.** Version steps span +0.4%
   to +30%; the model spans ×2.02.
   *Basis: §2.1 with §1.*
6. **The instrument estimates at a granularity the input does not support.** Standard presale practice puts
   leaves at 40–120 pd; these leaves are 6.8 pd.
   *Basis: external practice recorded in `decomposition_rules.md`, not a measurement of this project. The
   weakest reading here.*

## 4.1 Readings that were made and then withdrawn

Recorded because a later analysis benefits from knowing which way the errors ran.

- *The ×2 is part coverage, part granularity, and granularity is the harder half.* Withdrawn on §2.3.
  `docs/proposal_reverse_comparison.md` carries the correction inline.
- *C7 as a tree rule.* The relation between requirements and work is many-to-many, so a rule of the form
  "children cover the parent" is a tree rule applied to something that is not a tree. Noted, not yet fixed
  in the C7 document.
- *Opus is the reference and Sonnet is deficient.* Not supported: no outcome exists for either.

---

# 5. OPEN

- **Validity is untouched.** Roughly 110 runs across seven engine versions, two models and two axes, and
  **zero** comparisons against an outcome. BMS has no `FACT.md`. FaxRxTx has one, i.e. n = 1.
- **Axis P**, both models — the half of run17 that makes predictions 1, 2 and 6 readable.
- **The control has not been checked**: leaf-set overlap between axes. Above 90% the axes are not distinct
  and nothing else in run17 is worth reading.
- **Third model family.** Both models measured are one vendor, one generation. Whether ×2 is the scale of
  model disagreement in general or a property of this pair is unknown.
- **Branch 9 and C2 applicability.** With C2 removed the 10–0 disagreement on migration is no longer
  observable at all; the placement report replaces it but has not been read across a full batch.
- **`calibration-rates` did not load** in one session. Unexplained.
- **run16 per-run data is not in the repository** — only batch means. Recoverable only from the scratchpad
  of a closed session.

---

# 6. INSTRUMENT STATE AT CLOSE

`Lytin-D 5.0` with probe `Lytin-F 5.0`.

| constant | status |
|---|---|
| C1 splitting rule (ceiling 10 pd, never merge) | unchanged since `1.0` |
| C2 | **replaced** — was a fixed list of ten branches, now a declared projection axis |
| C3 integration = 20% of leaf E per node | unchanged since `3.0` |
| C4 static blind-spot list | unchanged |
| C5 modules derived from functions | scope restated in terms of node content, not branch number |
| C6 split consistency check | unchanged since `4.0`; diagnostic only |
| C7 coverage at every split | designed, **not implemented** |

Output §8 is a **placement report** — where did testing, transition, documentation and environments end up,
with "nowhere" a permitted answer — replacing the branch-completeness count, which has no meaning without a
fixed list.

A batch is stamped **(project × engine × model × axis)**. The engine half is self-reported by the sensor;
the model and axis halves are recorded by the orchestrator.
