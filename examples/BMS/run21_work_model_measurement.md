# BMS — Run 21: two crossings of one product model, `Hotyn-W 1.1`

Date: 2026-08-20. **Registered before the runs returned.**

## What this run measures, and why it is not the same question as run 20

Run 20 asked whether the crossing is executable and how big it gets. This one asks the question the
whole chain needs: **how far apart do two runs of the same step land, given identical input?**

Both crossings take **the same product model** — HM19-OA1, the 78-element tree — so unlike a
comparison between two different trees, the elements are shared and the two work models can be
compared item by item.

**Batch A: 25 elements of 78** — the subtrees N02 Platform Foundation, N09 Configuration Subsystem,
N13 Identity & Access, N26 Booking Domain Core. Chosen to carry every class the model has except
`surface`: properties, stores, behaviours, one interface, and four elements that cover no obligation
at all. Batches B and C follow only if this pair is worth extending.

Engine `Hotyn-W 1.1`: catalogue 1.1's **per parent** scope, and every refusal labelled `filter` or
`judgement` (W9). Run 20 was 1.0 on both counts, so its 94 items are not comparable with these.

## The similarity measure for step 2, stated before the numbers exist

Step 1 is compared on requirement co-location — which requirements share a node — scored by Jaccard.
The analogue here is direct, because a work item **is** a pair (element, activity):

| # | measure | what it says |
|---|---|---|
| 1 | **Jaccard over the set of (element, activity) pairs** | how much of the work the two runs agree exists. The primary number |
| 2 | **class agreement** — same class for the same element | where the disagreement comes from, if there is any. Run 20 found the whole judgement space of this step sits here |
| 3 | **judgement refusals** — how many, and on which elements | the only place a run may decline something the rules allowed |
| 4 | **items per requirement** — the projection onto the 68-obligation anchor | the frame that will still work at step 3, and the only one that survives a change of tree |

Measure 4 matters beyond this run. Two chains built on different trees cannot be compared item by
item, but both trace to the same requirement list, so **work per requirement** and later **effort per
requirement** are comparable across any structural difference. That is the common frame for all three
steps.

## Registered expectations

1. **Jaccard over (element, activity) pairs above 0.85.** The crossing is supposed to be nearly
   mechanical once classes are fixed: same tree, same declaration, same parameters. Below 0.7 would
   mean the step has a freedom nobody has identified, and the class log says where.
2. **Class agreement on at least 20 of 25 elements.** Run 20's classification made judgement calls on
   exactly the elements this batch contains — N69 mixing a property with a mechanism, N77 whose name
   reads like a policy and whose content is a doing, N28 and N74 which carry coverage and children at
   once. If agreement is below 16 of 25, the classification is the free parameter of this step and W7
   needs constraining rather than merely logging.
3. **Total item counts within ±10%.**
4. **Judgement refusals land in the same place**: run 20's fifteen were all one question — does this
   store need seed data — asked of five stores. Four of those five stores are in this batch. If the
   two runs answer it differently, that single question is worth a rule of its own.
5. **Per-parent items appear on N28 and N74.** They have children and carry coverage; under 1.0 they
   drew no aggregate work at all, which is the defect run 20 found and 1.1 fixes. This is the check
   that the fix took.
6. **No element untouched, no demanded item lost, no once-scoped item generated.** The imperative and
   the partial-run rule, same as run 20.

## Isolation

Both runs went through the real `work-crosser` definition (`tools: Glob`), which enforces the
prohibition on reading repository files by the absence of tools rather than by instruction. Identical
prompts, no shared context, launched together, neither told of the other. This is stronger than run
20, which had to paste the rules into a general-purpose agent.

---

# Results

Both runs returned with `tool_uses: 0`, through the real sensor definition. Raw in
`run21_raw/HW21-A1.md` and `HW21-A2.md`; the comparison is `run21_raw/compare_run21.py`.

## 1. The measure

| measure | value | registered | outcome |
|---|---:|---|---|
| **Jaccard over (element, activity) pairs** | **0.956** | above 0.85 | **CONFIRMED** |
| class agreement | **24 of 25** | at least 20 of 25 | **CONFIRMED** |
| total items | 154 vs 157, **+1.9%** | within ±10% | **CONFIRMED** |
| judgement refusals | 13 vs 16 | same place | **CONFIRMED** — same activities, same elements |
| per-parent items on N28 and N74 | present in both | present | **CONFIRMED** — the catalogue 1.1 fix took |
| element untouched · demanded item lost · once-scoped item generated | 0 · 0 · 0 | 0 · 0 · 0 | **CONFIRMED** |

## 2. Every difference between the two work models is one classification call

The symmetric difference is seven items and all seven sit on **one element**:

| | repeat 1 | repeat 2 |
|---|---|---|
| **N06 Data Platform** | `statement` | `store` |
| items it drew | K3, A9, D4 | K1, K2, A2, A3, A4, D4 |
| seed activities | not eligible | eligible, and refused by judgement (3 refusals) |
| R63's row in the projection | 3 items | 6 items |

Nothing else differs. Not one other element, not one other activity, not one filter refusal.

**Both runs flagged N06 as contested, in opposite directions, and each stated exactly what the other
reading would change.** Repeat 1: "`store` is defensible; I declined it because the class is *data the
system holds*, and the data is held by N27/N29/N86/N80/N81/N82, not by the platform." Repeat 2:
"classed `store` because calling it a statement would delete design, implementation and test of the
platform."

That is the disagreement stated in full, by both parties, before anyone compared them. The rule that
made it visible is W7's requirement to log the classification and justify it.

## 3. Read against step 1, this is the result that matters

| | step 1 — product model | step 2 — crossing |
|---|---:|---:|
| Jaccard between two identical runs | **0.308** | **0.956** |
| size ratio | ×1.65 (nodes) | ×1.019 (items) |

**The instability of this chain is in step 1 and not in step 2.** Given a tree, two runs produce very
nearly the same work — the crossing behaves like a function of (tree, classification), and the
classification agreed on 24 of 25 elements. Given a requirement list, two runs produce two rather
different trees.

This changes what is worth working on. A rule that binds the crossing further would be polishing
something already at 0.96. The freedom that decides the estimate lives one step earlier, in how finely
an obligation is divided into parts — which run 19 measured at ×1.42 and which no rule addresses.

**And it makes the propagation question sharper rather than answering it.** Two crossings of *one*
tree agree to 0.956. What two crossings of the *two different* trees would give is a separate number,
and by construction it is bounded by how different the trees are — which is the ×1.65 from step 1. The
crossing does not amplify the disagreement it inherits, and this run shows it adds almost none of its
own.

## 4. Two things both runs did that the rules did not require

**Both counted the applicability questions, and counted them differently.** Repeat 1: 525, every
element against every in-scope activity. Repeat 2: 354, splitting per-element questions (25 × 12) from
per-parent questions (6 × 9). Repeat 2 is right — a per-parent activity is not a question you can ask
of a leaf — and the definition should say which convention it wants, because the number is a
registered reading and two conventions make it uncomparable.

**Both named the same three obligations as living on elements that are not surfaces**: R54 "system
configuration for the Travel Manager" on a store, R19 "rules defined by the Travel Manager" on a
behaviour, R37/R47 "suppliers manually upload" on a store. Neither reshaped the model. If the whole
model has no surface elements for these, the acceptance and documentation dimensions generate no work
for them at all — and that is a defect in the product model, not in the crossing.

## 5. What this run does not establish

- **25 elements of 78, and no `surface` among them.** The UAT and documentation activities never
  fired, so the agreement measured above says nothing about them. Batches B and C contain the portals.
- **One pair.** Two runs give a difference, not a spread.
- **The classification agreed 24 of 25 here on a sample with one genuinely ambiguous element.** A
  sample richer in surfaces — where "is this a screen or the data behind it" is asked repeatedly —
  could disagree more.

---

# Batches B and C — the rest of the model

Added 2026-08-20, after the batch-A pair. Batch B: 27 elements (UX foundation, integrations, search and
prioritisation, booking workflow, hotel, transport). Batch C: 25 elements — the portals, reporting and
the support console, where every `surface` in the model lives. With batch A that is **77 of the model's
78 elements**; only the root N01 is uncrossed, and its per-parent items belong to the whole-model layer.

## The measure, all three batches

| batch | elements | repeat 1 | repeat 2 | Jaccard | class agreement |
|---|---:|---:|---:|---:|---|
| A — platform, configuration, identity, domain core | 25 | 154 | 157 | 0.956 | 24 of 25 |
| B — UX, integrations, search, workflow, hotel, transport | 27 | 197 | **197** | **1.000** | **27 of 27** |
| C — portals, reporting, support console | 25 | 195 | 189 | 0.949 | 23 of 25 |
| **all** | **77** | **546** | **543** | **0.969** | **74 of 77** |

Total item counts differ by **0.6%**. Reproduce: `run21_raw/compare_run21_all.py`.

**Batch B is identical, item for item.** Two independent runs of a 27-element subtree set produced the
same 197 items, the same classification of all 27 elements, the same 18 refusals and the same 27
projection rows. Both recorded zero judgement refusals: every `no` was forced by a condition the
declaration states.

## Every difference in 553 items traces to three classification calls, and one of them costs nothing

| element | repeat 1 | repeat 2 | items affected |
|---|---|---|---:|
| **N06 Data Platform** (batch A) | statement | store | 7 |
| **N60 Reporting** (batch C) | surface | statement | 7 |
| **N87 Reporting Read Model** (batch C) | store, seeded | store, seeding declined | 3 |
| N65 Incident Intake (batch C) | surface | behaviour | **0** |

N87 is not a classification difference at all — both runs called it a store. It is the one place in
546 items where the **applicability question** produced a disagreement: does a derived read model need
seed data? Repeat 1 said yes because the declaration's applies-to column says `store`, unqualified;
repeat 2 said no because a projection has nothing to seed. **Both wrote down the disagreement before it
existed**, naming the exact three lines where a second run would differ.

## The surface/behaviour boundary is where the judgement is and where the cost is not

Batch C's repeat 1 stated it outright: six of its seven contested calls sit on the surface/behaviour
boundary, and that boundary **changes nothing** — the two classes draw the same six activities, and a
parent qualifies for the UAT and documentation activities through any surface in its subtree. "A run
that disagrees with me across that boundary will produce the same 195 items."

Only three boundaries carry item consequences, and both repeats identified the same three:

| boundary | effect on one element |
|---|---|
| aggregate vs constructible | ±5 items (the construction and test chain) |
| statement vs constructible | ∓5 / ±2 — K3 and possibly A9 replace K1, K2, A2, A3, A4 |
| store vs not a store | ±3 items (the seed-data chain) |

**That is a usable result.** The classification has six classes, but only three distinctions in it can
move the work model. A rule that constrained W7 would only need to address those three.

## What the surfaces changed

Batch C is the first crossing in which the acceptance and documentation dimensions fired: **U1, U2, U3
and O1 produced 30 of its 195 items**, at the five parents whose subtree holds a screen. Batch B fired
them at three parents of six. Batch A fired them nowhere — it contains no surface at all.

Both C runs also reported the same asymmetry: **N55 Administration Portal and N60 Reporting carry own
coverage *and* children**, so each draws the full construction chain *and* the full per-parent chain —
19 items against a leaf norm of 6. Batch C repeat 1: "the single largest source of item-count asymmetry
in this model; any comparison run must be checked at these two elements first."

## Findings that are about the product model, not about the crossing

Both B runs, independently: **the search, prioritisation and approval-workflow subtrees declare no
surface**, so they generate no UAT and no user documentation at all — while R19 speaks of rules "defined
by the Travel Manager" and R25 of approval stages someone must approve. Either those subtrees genuinely
face no user, or the product model is missing screens.

Both C runs, independently: **R57 is covered twice**, at the Administration Portal and at the
configuration screen inside it. And **N68 Process Transparency, a leaf directly under the root, can
receive no per-parent work at all** — its acceptance and documentation work can only attach at the root,
which no partial run crosses.

Batch B, both runs: **K3 and A9 hang on a single element** (N16) and **G1, G2, G3 hang on a single
element** (N43). Batch C repeat 2: the data dimension produced **nothing at all**. The two dimensions
with the least purchase on this product are the ones whose fate rests on one classification call.

## What still is not crossed

The **whole-model layer**: the 16 once-scoped activities, E1 across three environments, the root's own
per-parent items, and the demanded-work branch. Every partial run deferred them explicitly and none
struck anything out. That layer is arithmetic rather than judgement — one item per once-scoped activity
— with one exception that is not arithmetic: **whether the root's per-parent items exist and reach N68**.
