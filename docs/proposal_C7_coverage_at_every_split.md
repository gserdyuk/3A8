# C7 — coverage at every split

Status: **design only. Not implemented, not run.** Predictions registered at the end, before any
measurement, per the pattern that made C6's result readable.

## What the measurement forced

run16 left a ×1.97 gap in leaf count between two models on identical input, with price per leaf
indistinguishable (6.76 vs 6.66 pd, t = 0.51). Two explanations were on the table: the trees cover different
work, or they cover the same work at different granularity.

**Granularity is arithmetically excluded.** Splitting conserves the sum — a 14-day leaf becomes 7 + 7 — so
covering identical work in half the leaves requires leaves twice as heavy. For Sonnet to carry Opus's
1062.66 leaf-pd in 79.9 leaves, the mean leaf would have to be **13.3 pd**. C1 caps M at 10, E rarely
exceeds 11, and all ten Sonnet runs reported `>10: 0`. A leaf that heavy is not expressible under the
method.

So either C1 was violated — it was not — or the trees cover different amounts of work. **They cover
different amounts of work.** The ×2 is coverage.

A worked instance was checked in the other direction and confirmed the same thing from the opposite side.
Where Sonnet split *finer* than Opus (rules configuration as two leaves against Opus's one), it also priced
**lower in total** — 13.83 against 18.00. Conservation holds; there is no free multiplier hiding in
granularity.

## The mechanism, and why pinning the leaf price did not reach it

C1 is monotone and order-independent — **given a starting judgement.** The judgement itself is free: *is
this node above ten days or not?* Nothing constrains it, and it decides whether splitting happens at all.

From run16, one Sonnet run:

```
M9 Suppliers Portal — single leaf                    10.17
```

The entire suppliers portal as one leaf. Judged at ten days, therefore not split, therefore ten days. The
same portal in an Opus run: **five leaves, 29.33 pd**.

The judgement then feeds back on itself:

- judged small → not split → stays small;
- judged large → split → unpacking adds **+28.9%** (measured by C6) → larger still.

That is why the divergence is multiplicative rather than additive, and why pinning the price of a leaf could
not touch it. The total is *price × count*. C1 fixed the price and left the **entry into splitting** free.

## The rule

> **C7 — coverage at every split.** The children of a node must together account for **everything the node
> names**. When you split, state for each child which part of the parent it covers, and confirm that nothing
> named in the parent is left uncovered; if something is, the split is incomplete and the missing child is
> added.
>
> A node that is **not** split is subject to the same requirement on its own. **If a single leaf cannot
> account for everything its node names, the node is split — regardless of its estimated size.** Coverage is
> a second and independent trigger for splitting, alongside C1's ten-day ceiling.
>
> At the **root**, the ten branches must together account for everything the source text names. This is the
> only place the full source text is read for coverage.

## Why local coverage rather than a global audit

By induction: if every node fully covers its parent, and the root fully covers the source text, the tree
covers the source text. The full text is read **once, at one place**, and every other check is local.

That is not merely elegant, it is the difference between a check that works and one that does not. Asking
"do these six leaves cover *Administration Portal: configuration, visibility of booking statuses,
reporting*" is a question with an answer. Asking "does this tree of 157 leaves cover this RFP" is a question
that invites a confident yes.

It also breaks the feedback loop directly. `M9 Suppliers Portal` as one 10.17 pd leaf cannot account for
supplier registration, availability upload, pricing upload and manual booking confirmation — all four named
in the source. Under C7 the split becomes compulsory instead of optional, and the entry judgement stops
being free.

## Decisions taken, and by whom

- **The rule binds; it does not report.** This is a deliberate departure from C6, which compares and changes
  nothing. C7 changes the tree. The reason for the difference: C6 measures an inconsistency whose correct
  resolution is unknown (parts or whole?), while C7 detects an omission whose correct resolution is not in
  doubt — the missing work is added. Where the answer is known, reporting instead of fixing is just a slower
  way to be wrong.
- **It only adds.** C7 has no power to remove a node that traces to nothing in the source. That direction —
  invented work — belongs to the reverse audit and is explicitly out of scope here.
- **It does not touch pricing.** Coverage says what is in the tree, never what it costs. This is deliberate,
  and defensible on evidence: price per leaf is the one parameter that already agrees across models
  (6.76 vs 6.66), so the sensible move is to constrain the factor that diverges and leave alone the factor
  that does not.
- **Directionally inflationary, knowingly.** Every mechanism in this method that has ever moved the level has
  moved it up: splitting, unpacking, C5, C3. C7 adds a fifth. That is accepted because the alternative is a
  tree that is cheap by omission, but it means the level must be watched and not treated as a validation.

## The design flaw, stated before the measurement rather than after

**"Everything the node names" is itself a judgement, and at internal nodes it is a judgement about a label
the run wrote itself.**

At the root the anchor is external and solid: the source text. One level down, C2's branch list is fixed by
fiat, so "everything branch 5 names" is well defined. But a derived module — `M14 Administration Portal` —
carries a name the run invented under C5. Checking that a module's leaves cover the module's own label is
circular: the run chooses the label, then grades itself against it.

The rule therefore has real force only where a node is traceable to text. Concretely, it should bind hard on
**branches 2–6** (functional, C5-derived from named functions) and be close to **vacuous on branches 1, 7,
8, 9, 10** (analysis, QA, infrastructure, migration, documentation), whose contents the source text does not
name at all.

This is not fatal, because branches 2–6 carry the majority of leaf weight and are where the models actually
diverged. But it means **C7 cannot be reported as "the tree now covers the requirement"** — only as "the
functional part of the tree covers the named functions". A pass on the activity branches means nothing and
must not be counted as one.

Second flaw, smaller: adding leaves to satisfy coverage feeds the unpacking effect, so C7's effect on the
level will be **larger than the coverage gap it closes**. The two cannot be separated from the total alone.

## Why a major version

`Lytin-D 5.0`, not `4.1`. The convention makes major the test of whether a change *can* move the level, and
this one is designed to: a second, independent trigger for splitting adds leaves, and leaves are priced.
Estimates across the boundary are not comparable without a measured conversion, which is exactly what the
next batch has to supply.

## Registered predictions

To be run n=10 on each of two models, same pinned prompt, against the `4.0` batches of run16
(Opus: mean 1625, CV 9.25%, 157.3 leaves · Sonnet: mean 804, CV 11.56%, 79.9 leaves · ratio 2.021).

1. **The cross-model ratio falls below 1.4.** *This is the prediction that matters.* It is the entire claim:
   coverage is the dominant cause, and forcing coverage closes it. If the ratio stays above 1.7, the
   arithmetic argument above is wrong somewhere and C7 should be reverted rather than tuned.
2. **Sonnet's leaf count rises much more than Opus's** — Sonnet +50% or more (79.9 → 120+), Opus +0…20%
   (157 → 157…190). Sonnet is the under-coverer, so the rule should bite there and barely elsewhere. If both
   rise equally the rule is adding leaves indiscriminately, not fixing coverage, and prediction 1 will pass
   for the wrong reason.
3. **Both levels rise; Sonnet's far more** — Opus +5…20%, Sonnet +40…80%. The rule only adds.
4. **Within-model spread does not improve materially.** Opus CV stays in 8…12%. C7 removes no judgement, it
   adds a step. A large narrowing would be surprising and would need explaining before being believed.
5. **The rule binds on branches 2–6 and is near-silent on 1, 7, 8, 9, 10.** Reported as leaves gained per
   branch. If the activity branches gain as much as the functional ones, the circularity flaw in the design
   is real and the result is not what it appears to be.
6. **Price per leaf stays near 6.7 pd on both models.** The parameter that already agrees should be
   untouched. Movement here means something unintended happened and nothing else in the batch is safe to
   read.

Predictions 1 and 2 are the pair to watch, and they work the way C6's 1 and 3 did: 1 can pass for the wrong
reason, and 2 is what distinguishes the right reason from the wrong one.

## What comes after, depending on the result

- **Ratio closes and Sonnet gains most** → coverage was the dominant cause, the parameter is closed, and the
  remaining work is the other direction: invented work, which needs the reverse audit.
- **Ratio closes but both gain equally** → the rule is inflating, not correcting. Level up, gap closed by
  raising the floor rather than by fixing anything. Read as a failure despite the headline number.
- **Ratio does not close** → coverage is not the dominant cause after all. The arithmetic says it must be,
  so a failure here means an assumption in it is wrong — most likely that the two models' leaves are
  comparable units at all — and that is the thing to go after next.
