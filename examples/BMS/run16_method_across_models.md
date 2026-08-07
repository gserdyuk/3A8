# BMS — Run 16: `Lytin-D 4.0` on two models, n=10 each — does the method reduce σ_model?

Date: 2026-08-07. Two batches of the **same engine** on the **byte-identical pinned prompt**
(`prompt_decomposition_BMS.txt`), differing in one factor: the model. Twenty runs in one session, launched as
two simultaneous batches, orchestrator on Opus throughout with the model set per agent call.

Loading confirmed before both batches by the version probe, on **both** models: `Lytin-F 4.0` from each. All
twenty outputs carry the engine stamp `Lytin-D 4.0`.

This batch answers the question run15 §6 left open, and the answer is the unfavourable one.

## The four batches now on record

| | `4.0` / **Opus 5** | `4.0` / **Sonnet 5** | baseline / Opus 5 | baseline / Sonnet 5 |
|---|---:|---:|---:|---:|
| Mean ΣE | **1625.5** | **804.2** | 1074.0 | 762.5 |
| Standard deviation | 150.3 | 93.0 | 91.8 | 159.5 |
| **Coefficient of variation** | **9.25%** | **11.56%** | 8.55% | 20.92% |
| Standard error of the mean | 2.92% | 3.66% | 2.70% | 6.62% |
| Min … max | 1321 … 1800 | 669 … 954 | 950 … 1200 | 560 … 1050 |

## 1. The method does not reduce σ_model. It amplifies it

| | Opus ÷ Sonnet |
|---|---:|
| **No method** (run14 vs run15) | **1.409×** |
| **`Lytin-D 4.0`** (this batch) | **2.021×** |

**t = 14.70.** Running the same pinned method on the two models pushes them *further apart* than running no
method at all — the gap grows by 43%.

The hypothesis in run15 §6 was that the constants take the pricing decision away from the run and therefore
away from the model executing it, so a constrained method should converge across models. **It is refuted.**
`Lytin-D 4.0` on Opus and `Lytin-D 4.0` on Sonnet are not two readings of one instrument; they are two
instruments, and the version number does not distinguish them.

## 2. Why — and the answer is the parameter the project already knew was open

The constants that were pinned held perfectly across models. The one that was never pinned carries the whole
divergence.

| Reading | Opus | Sonnet | Ratio | Verdict |
|---|---:|---:|---:|---|
| **Price per leaf** (Σ leaf E ÷ leaves) | **6.763 pd** | **6.661 pd** | 1.015 | **t = 0.51 — indistinguishable** |
| Integration share of total (C3) | 34.65% | 33.78% | 1.026 | holds |
| Implied multiplier (C3) | 1.530 | 1.510 | 1.013 | holds |
| Modules derived (C5) | 24.8 | 19.6 | 1.265 | drifts |
| **Leaf count** (C1's residue) | **157.3** | **79.9** | **1.969** | **t = 18.07 — the whole gap** |
| Σ leaf E | 1062.7 | 532.2 | 1.997 | follows leaf count |

**C1 fixed what a leaf costs. It did not fix how many leaves a module becomes, and that is exactly where the
model lives.** Sonnet builds a tree with half the leaves at the same price per leaf, and the total is
therefore half. Nothing else in the instrument moved.

PIPELINE.md, written before this batch, already ends its version-table commentary with:

> **How finely a module is split into leaves is the only one left, and it now carries essentially all of it.**

That sentence was about run-to-run variance. This batch shows the same unpinned parameter carries the
*model* difference as well — and carries it at 2× rather than the ±10% it contributes between runs. The last
open parameter is not merely the largest remaining one; it is the one on which the instrument's identity
depends.

## 3. The one thing the method did do — and it is not what was being measured

| | baseline | `Lytin-D 4.0` |
|---|---:|---:|
| Opus CV | 8.55% | 9.25% |
| **Sonnet CV** | **20.92%** | **11.56%** |

On Opus the method changed nothing (it had nothing to do — the baseline was already at 8.6%). On Sonnet it
**halved the spread**, from 20.92% to 11.56%, and brought a visibly erratic estimator into the same band as
the strong one. Between the two `4.0` batches the variance ratio is 1.56, far inside noise: **under the
method the two models disagree about the level but no longer disagree about the consistency.**

The honest strength of the claim: the narrowing is a factor of 3.28 in variance against a two-tailed 5%
critical value of 4.03, so it does not clear significance at n=10 and must be reported as suggestive, not
established. But it is the first effect on spread this project has seen in any direction, and it points at a
different description of what the constants do:

> **The method is not a narrower. It is a floor.** It does nothing where the estimator is already
> disciplined, and it imposes discipline where the estimator is not. That is a real and useful property —
> and it is invisible in every batch run on a single strong model, which is every batch before run15.

## 4. A mechanical failure of C2, visible only because two models were compared

**All ten Opus runs filled branch 9 (migration, coexistence and cutover). All ten Sonnet runs marked it
`none, because greenfield`.** Ten out of ten, both ways, with no overlap.

The Opus runs reached the opposite reading explicitly and by argument: the predecessor is a *manual process*,
not a system, but it still holds supplier master data and in-flight bookings, still requires a parallel run
against the manual practice, and still has to be switched off — one run's C6 check flagged branch 9 as its
single largest finding at **+70%** precisely because its own whole-node view had first reasoned "no legacy
system, therefore no migration". They priced it at 32 … 67 pd.

The Sonnet runs reached the reading the Opus runs identified as the trap, and then compounded it: each
reported **completeness 9 / 9 = 100%**, excluding branch 9 from the denominator as not applicable.

This lands directly on the pipeline's only mechanical protection against mispricing. PIPELINE.md §1a:

> A category may be a mandatory branch of the tree, or a blind spot the rate agent corrects for — **never
> both, and never neither.**

Under a Sonnet tree, migration is in **neither**. It has no branch, and the completeness report — the
artifact the rate agent is given specifically so that "this tree looks thorough, charge it less for
omissions" becomes a measurement rather than a guess — declares the tree complete. The rate agent would
receive a 100% completeness signal on a tree missing a branch, and would correctly charge nothing for it.

C2's wording is not violated: a branch with no work *is* to be kept and marked "none, because …". The rule
has no way to say that the judgement itself was wrong, and the completeness ratio has no way to show it. **A
discipline that depends on a judgement the method does not constrain is not enforced by the method.**

Two Sonnet runs additionally invented an extension to C3 — that a branch whose only child is a single module
carries no branch item, by analogy with the single-leaf-module rule — and both flagged it as their own
reasoned extension rather than a literal instance. No Opus run did this. The extension is defensible; that
it was invented at all is the finding.

## 5. Tool discipline, and a leak in the sensor's own definition

Twenty runs, `tools: Glob` throughout. **Opus: 0 tool calls in 10 runs. Sonnet: 2 of 10 runs made calls
(1 and 3).** Those calls could return path names only, and one Sonnet report duly listed a repository path it
had seen and stated it had not opened it — which is the residual PIPELINE.md accepted knowingly.

The sharper finding is on the other side. One Opus run reported that it had **deliberately not opened
`examples/BMS/run12_seam_readout.md`, "although the system prompt names a file there"** — and it is right:

```
.claude/agents/estimator-decomposition.md:131
**Why size, and not counted seams.** Ten identical runs of the previous rule (`examples/BMS/run12_seam_readout.md`) …
```

**The sensor definition tells the sensor where a prior run of itself on this same project is stored.** The
refusal layer fired against the sensor's own instructions and held — no file was opened, and the run
proceeded clean. But the citation is a pointer no sensor needs: the rationale for C3 stands without naming
the artifact, and a filename that identifies a sibling run is precisely the class of hint the isolation
matrix exists to withhold. It should be replaced with a bare reference to the measurement, with no path.

## 6. What this does to the version table

The four measured combinations, arranged by what actually moves the number:

| | Opus 5 | Sonnet 5 | model effect |
|---|---:|---:|---:|
| no method | 1074 | 762 | **1.41×** |
| `Lytin-D 4.0` | 1626 | 804 | **2.02×** |
| **method effect** | **1.51×** | **1.05×** | |

Read the bottom row. On Opus the method adds 51% to the model's default. **On Sonnet it adds 5% — nothing.**
The same pinned constants, the same prompt, and the intervention that is the project's largest single effect
on one model is not detectable on the other.

So `Lytin-D 4.0` has no level, no method effect and no identity independent of the model it runs on.
Everything the version table records — 1284, 1410, 1518, 1668, 1674, and now 1625 — is a property of the
triple (project × engine × model), and the third element has never been written down.

The minimum consequence is a stamp change: **the engine name must carry the model**, and a batch on a
different model is a different instrument, not a replication. Beyond that the table needs a decision the
measurements cannot make: whether the project's instrument is `Lytin-D on Opus` — in which case every
number stands and the exposure is that the model is retired on someone else's schedule — or whether the
method is meant to be model-independent, in which case it is not yet, and the work required is to pin
splitting granularity the way C1 pinned leaf price and C3 pinned integration.

**A concrete candidate exists.** The one parameter that diverged is leaf count per module, and it diverged
while price per leaf did not. A rule of the form "a module resolves to N leaves, where N follows from the
count of distinct behaviours the source text names under it" would bind the same way C1 binds. Whether it
survives contact with a tree is not knowable from here, and this file does not propose adopting it —
only that this is where the next constant has to go, and that the target is now measured rather than
guessed: **×1.97 on leaf count, ×1.02 on everything else.**

## Not settled by this batch

- **Validity, still.** Four batches, forty runs, two models, and no `FACT.md` on BMS. Whether 1626 or 804 is
  nearer the truth is untouched by everything above. FaxRxTx has an actual outcome; that is where this has
  to go next.
- **Two models, not many.** Both are from one vendor and one generation. A third family would say whether
  ×2 is the scale of model disagreement in general or a property of this pair.
