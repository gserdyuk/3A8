# BMS — Run 15: σ_model, n=10 — the same baseline on a different model

Date: 2026-08-07. The run14 batch repeated with **exactly one factor changed: the model.** Same pinned
prompt, same wrapper, same agent type, same orchestrating session, launched simultaneously, `tool_uses: 0`
on all ten. No method definition on either side, so no version of `Lytin-D` participates and the model
effect cannot be confused with a method effect.

Opus 5 (run14) is the reference; this batch is Sonnet 5, set per-call rather than by switching the session,
so the orchestrator itself stayed on the same model throughout.

## Raw data — Sonnet 5

| Run | TOTAL | Dev subtotal | Contingency |
|---|---:|---:|---:|
| S-1 | 680 | ~460 | +10% |
| S-2 | 950 | 420 | +12% |
| S-3 | 620 | 269 | +15% |
| S-4 | 900 | 400 | +15% |
| S-5 | 750 | 520 | +5% |
| S-6 | 640 | ~365 | none stated |
| S-7 | 560 | 275 | +10% |
| S-8 | 800 | 370 | +15% |
| S-9 | 675 | 409 | +15% |
| S-10 | 1050 | 587 | +8% |

## The three batches

| | baseline / **Sonnet 5** | baseline / **Opus 5** | `Lytin-D 3.0` / **Opus 5** |
|---|---:|---:|---:|
| Mean ΣE | **762.5** | 1074.0 | 1673.8 |
| Standard deviation | **159.5** | 91.8 | 181.8 |
| **Coefficient of variation** | **20.92%** | **8.55%** | **10.86%** |
| Min … max | 560 … 1050 | 950 … 1200 | 1363 … 1977 |
| max ÷ min | **1.875** | 1.263 | 1.451 |
| Standard error of batch mean | **6.62%** | 2.70% | 3.44% |

## 1. The model moves the level as much as the whole method does

**×1.409 between the two models on identical input** — Opus 5 is +40.9% over Sonnet 5, a difference of
311.5 pd with a standard error of 58.2, i.e. **t = 5.35**. This is not noise by any reading.

Set against the effects the version table has been recording:

| Change | Effect on level |
|---|---:|
| `Lytin-D 2.3` → `3.0` (a rewritten integration rule) | +0.4% |
| `Lytin-D 1.0` → `3.0` (three major versions) | +30% |
| **no method → `Lytin-D 3.0`** (run14) | **+55.8%** |
| **Opus 5 → Sonnet 5, no method at all** (this batch) | **−29.0%** |

**Swapping the model is a larger intervention than any single version of the method, and comparable to
having a method at all.** Nothing in the pipeline records which model produced a number.

## 2. The first significant difference in spread this project has found — and it is not the method's

Sonnet's CV is **20.92%** against Opus's **8.55%**. The variance ratio is **5.99** against a two-tailed 5%
critical value of 4.03 at 9 and 9 degrees of freedom: **significant.** Its widest and narrowest runs differ
by a factor of **1.875**, against 1.263 on Opus.

Five versions of the instrument never produced a significant change in spread (run14 §1). One model swap
did, on the first attempt, with no method involved. Whatever governs the width of the output distribution,
the evidence so far says it is the model and not the procedure.

## 3. The batch-mean threshold was a property of the model, not of the method

Run14 concluded that the unit of output is the batch, since a batch of ten carries a standard error of
2.7–3.4% and a single run carries ±11–14%. That conclusion silently assumed Opus.

On Sonnet a batch of ten carries **6.62%**. To reach run14's 2.70% would take **n = 60**; to reach the
3.44% of `Lytin-D 3.0` would take **n = 37**.

So the rule has to be stated in a form that survives a model change:

> **n is not a constant of the method. It is set by the observed CV and the required standard error:
> n ≥ (CV / target SE)².** Ten runs is what Opus happens to need. Re-measure CV after any model change
> before reusing a batch size.

## 4. Same shapes, cheaper prices

Both models decomposed bottom-up into a comparable number of blocks (Sonnet 10–21, Opus 10–19) and both
added role overheads on top. The difference is not granularity — it is **what a block gets priced at**, plus
a thinner overhead multiplier (≈1.9× against ≈2.2×) and a smaller contingency (≈11% against ≈18%).

This lands on a sore spot. Run6 found that the price attached to a leaf carried most of the *run-to-run*
variance, and C1 was written to control it — but C1 caps how large a leaf may be (M ≤ 10 pd) and says
nothing about what a leaf costs. A model that prices work more cheaply therefore produces a cheaper tree at
the same granularity, and C1 does not stand in the way. The one constant that would bind σ_model is the one
the method deliberately does not have.

The comparison here is between two *unconstrained* batches, so this is an observation and not a controlled
measurement of leaf price. §6 says how to make it one.

## 5. What this does to the version stamp

PIPELINE.md states that "an estimate is a property of the pair (project × engine), so a number without an
engine stamp cannot be compared with anything." This batch says the pair is a triple:

> **(project × engine × model).** `Lytin-D 3.0` is not an instrument. `Lytin-D 3.0 on Opus 5` is.

Every measured batch in this repository — run6 through run14, five versions and roughly fifty runs — was
produced on one model family and none of them records it. The numbers are not wrong, but they are all
readings of an instrument whose largest single parameter was never written down.

The practical edge is sharper than a documentation gap. Models are replaced by their vendor, on the vendor's
schedule. A calibration that shifts 41% on a model change is not a constant of the method; it has a shelf
life. Any rate card, multiplier or level derived from these batches expires when the model does.

## 6. The experiment this makes urgent, and why it could vindicate the method

Everything above measures σ_model **with no method present**. The obvious next question is whether the
method *reduces* it:

> Run `Lytin-D` on Sonnet 5, n=10, same pinned prompt, and compare against the same version on Opus 5.

The two outcomes say opposite things, and both are worth knowing:

- **If the gap stays near 41%** — the method rides on top of whatever the model already thinks, and its
  constants control the shape of the tree while the model sets the price. The version table then measures
  something smaller than the platform it runs on.
- **If the gap collapses** — the method's real product is **model-independence**, and that is a far stronger
  claim than spread reduction ever was. It would mean the constants do exactly what C1–C3 were written to
  do: take the pricing decision away from the run, and therefore away from the model making it.

The second outcome is the one worth hoping for, and it is the first thing this project has had that would
count as evidence the method is doing real work. Neither run14 nor this batch can decide it.

**Answered the same day, in run16, and it is the first outcome — worse.** `Lytin-D 4.0`, n=10 on each
model, widened the gap from **1.41× to 2.02×** (t = 14.70): the method pushes the two models further apart
than no method does. The cause is located precisely — price per leaf is identical across models (6.76 vs
6.66 pd, t = 0.51) while **leaf count differs by ×1.97** (t = 18.07). C1 pinned what a leaf costs and never
pinned how many leaves a module becomes, and that is where the model lives. One consolation did survive:
on Sonnet the method halved the spread (CV 20.9% → 11.6%), which suggests the constants act as a floor on a
weak estimator rather than as a narrower on a strong one.

**Prerequisite:** the comparison needs the *same* version on both sides. The definition on disk is
`Lytin-D 4.0`, which has never been measured on any model — so the batch is two batches, `4.0` on each
model, and the version probe must confirm loading before either.
