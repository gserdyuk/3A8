# Comparing the tree back against the text

Status: **design only. Nothing run, nothing implemented.** Predictions registered at the end, before any
measurement, per the pattern that made C6's result readable.

## Two mechanisms, not one

Both are "compare the WBS with the task". They answer different questions and must not be built as one
thing.

| | **A — behaviour inventory** | **B — full reverse audit** |
|---|---|---|
| Question | *Is leaf count derivable from the text?* | *Is this decomposition correct?* |
| Object | many trees, one number each | one tree, many findings |
| Output | a count, and its spread | a list of named defects |
| Aimed at | the next **constant** | the **validity** of a tree |
| Fails if | the count is as unstable as leaf count | it cannot tell two trees apart |

A is a ruler. B is an inspection. A ruler that cannot be read is useless even if inspections are valuable,
and inspections do not produce a constant however many you run. They are sequenced, not merged: **A first**,
because if the count is unstable there is nothing to build a constant on and B remains the only usable form.

## Where this comes from

C6 asked the tree about itself and the tree answered the same way twenty times on two models: the whole-node
figure prices what the source text *says*, the split prices what the work *is*, and the gap is where the
text compresses a mechanism into a phrase — "high configurability", "capabilities for the Travel Manager",
"intelligent search".

If that diagnosis is right, then leaf count should follow **how many distinct things the text names**, which
is a property of the text: fixed, countable once, and — this is the whole point — **the same for every
model**. run16 showed every pinned parameter holds across models to within 3% while leaf count moves ×1.97.
A parameter anchored in the text is the shape of thing that could hold.

## The crux, stated before the measurement rather than after

**The inventory has the same granularity problem, one level up.**

"Count the distinct behaviours" is not obviously more constrained than "split until nothing exceeds 10 pd".
If the inventory agent is free to decide what counts as one behaviour, it will produce whatever number it
likes, and the project will have moved the judgement from the estimator to the inventory rather than
removing it. That is failure disguised as progress, and it would be invisible from a single run.

The only defence is to **measure the ruler before using it**, and to measure it on the axis that actually
failed. Note carefully which axis that is:

- leaf count *within* a model was already fine — CV 6.8% on Opus, 10.4% on Sonnet;
- leaf count *across* models was the failure — **×1.97, t = 18.07**.

So a within-model stability check on the inventory proves almost nothing. **The decisive experiment is
cross-model from the start.** If two models, reading the same fixed text under the same fixed definition,
count materially different numbers of behaviours, the idea is dead and no amount of downstream design saves
it.

## The definition of a behaviour, fixed on record before any run

> A **behaviour** is one distinct thing the system must do, stated by or directly entailed by a verb in the
> source text, and attributable to a named actor, a named external system, or the system itself.
>
> - Count separately whatever the text names separately. Do not merge — this mirrors C5 rule 1.
> - Do not invent. If it is not in the text, it is not a behaviour, however obviously the work would be
>   needed in practice.
> - Non-functional requirements are counted only where they name an action, not where they state a property.
> - Group the result under the source's **own headings**, so the grouping is textual and not a decomposition.

This definition is deliberately textual and deliberately blind to the method: the inventory agent is not
told about C1, C5, modules, leaves, person-days, or that an estimate exists. It never sees a tree.

## What gets compared, and to what

Not behaviours against total leaf count. Branches 1, 7, 8, 9, 10 are activity-shaped — analysis, QA,
infrastructure, migration, documentation — and are not derived from behaviours at all; they come from C2's
fixed branch list. The comparison is **behaviours against functional leaves only** (branches 2–6), and any
result quoted against the full leaf count is a category error.

## Mechanism B — the audit, sketched

For a completed tree, read the whole source text against the whole tree, in both directions, and report
findings rather than a score:

- **coverage:** text requires X, no node covers X → silent omission, the expensive failure;
- **traceability:** node Y traces to nothing in the text → invented work, the failure that inflates a total
  while looking thorough.

Each finding names the passage it came from and the node it lands on, so a reader can check it instead of
believing it. **The estimator never sees the audit.** If the run that built the tree also scores it, the tree
gets adjusted to match, the judgement C1 removed comes back, and C6's own discipline — *no figure was changed
on the strength of this table* — is what gets lost. Same structural argument as keeping `calibration-rates`
blind to the gap it explains.

Two things this makes decidable that nothing else does:

1. **Branch 9.** Whether migration work is present in this RFP is precisely a coverage question, and the two
   models answered it 10–0 in opposite directions (run16 §4). The audit settles it from the text.
2. **Which tree is closer.** run16 left Opus at 157 leaves and Sonnet at 80 on identical input, ×2 apart,
   with no way to say which is nearer the work. Auditing one of each is the cheapest available answer.

## Registered predictions — experiment A, the ruler

To be run n=10 on each of two models, same fixed definition, same source text, inventory agents blind to the
method and to every tree.

1. **Cross-model count ratio lands within ±15% (0.85 … 1.15).** This is the prediction that matters. Leaf
   count came in at 1.97; anything above roughly 1.3 here means the count is a property of the reader rather
   than of the text, the idea fails on its own terms, and mechanism A should be abandoned in favour of B.
2. **Within-model CV below 15%** on both models. A weak precondition, stated so that a miss is visible: leaf
   count already managed 6.8% within-model, so passing this proves little and failing it kills the idea
   outright.
3. **Behaviour count lands between 45 and 90.** A guess, registered so the shape of the miss is legible. If
   it comes back at 150+, the definition is being read as "one behaviour per clause" and needs rewriting
   before anything is concluded.
4. **Functional-leaf count exceeds behaviour count on both models.** A leaf is an implementation piece and a
   behaviour is a requirement; several leaves per behaviour is expected. The interesting quantity is the
   **ratio's stability across models**, not its value. If the ratio is stable while leaf counts differ ×2,
   that is the constant, and it is a multiplier on a textual count.

Prediction 1 and prediction 4 are the pair to watch. 1 says the ruler exists; 4 says the tree is a fixed
multiple of it. Either can hold without the other, and only both together give a constant.
