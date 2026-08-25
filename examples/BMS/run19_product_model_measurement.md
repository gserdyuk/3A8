# BMS — Run 19: `Hotyn-M 1.1` on the repaired inputs — one cell, n=2

Date: 2026-08-20. **Registered before the runs returned.** Everything above the results line was
written while the two agents were still working.

## Design

One cell: **Opus 5 × order A × n = 2.** Deliberately narrow. Run 18 was 2 models × 2 orders × n=1,
which measured everything and separated nothing: with a single run per cell the order effect could not
be told apart from ordinary run-to-run variance. This run buys the missing quantity first — **how much
two runs of the same model on the same input differ** — and buys it for two runs instead of eight.

Sonnet is not run. The model gap is already measured (run 18: ×1.036 anchored, ×4.56 derived); what is
not measured is the floor beneath it.

## What changed since run 18, and why the numbers do not carry across

| | run 18 | run 19 |
|---|---|---|
| engine | `Hotyn-M 1.0` | **`Hotyn-M 1.1`** |
| requirement list | `requirements.md`, N=73, product and work mixed | `requirements_product.md`, **N=68**, md5 `0c2dea478b993e4451a66f9468633f1e` |
| assumptions | `assumptions.md` v1 — contradicted the list on R03 | `assumptions_product.md` v1, md5 `8c622930655540d5fceb0d58d7482f8d` |
| R13, R14 | ambiguous, each run guessed | readings declared (P3, P4) |
| sensor | general-purpose agent, rules pasted | the real definition, `tools: Glob` |

`Hotyn-M 1.1` differs from 1.0 in M2 and in what closure checks:

- partial coverage is coverage at the node, and **a debt at the requirement** — no requirement may
  leave closure partially covered;
- **coverage is declared where the obligation is realised**, never at the node that presides over it;
  a parent's total coverage is computed, not declared;
- closure asserts, per requirement, **whole or residue**.

Node counts from run 18 (anchored 82–87 at N=73) are not comparable. Scaled by list length the same
density would give about 79 anchored nodes at N=68, and that is an arithmetic expectation, not a
prediction.

## Registered expectations

Scored only after the outputs are read.

1. **Executability first.** Both runs produce all nine output sections, with a parent for every node,
   own coverage sets, and a per-requirement whole/residue verdict. **This is the primary reading of
   this run.** If 1.1's rules cannot be executed as written, nothing else here means anything.
2. **Anchored total (skeleton + accretion) agrees between the two repeats within ±5%.** Run 18 put the
   anchored total at CV 2.5% across four runs that differed in model *and* order; two runs differing
   in nothing should not do worse. Above ±10% would mean the anchor is looser than run 18 suggested
   and that its stability was luck.
3. **The derived count differs by more than the anchored count does.** Completion is the unbounded
   phase and run 18 measured ×4.56 between models on it. Between two repeats of one model, expect a
   spread that is visible — up to ×2 — while the anchored part holds.
4. **Prediction 6, in its easiest case.** Between two runs of the same model on the same order, the
   co-location relations come within **×2 in size** and agree at **Jaccard above 0.5**. This is the
   floor case: same engine, same input, no order effect, no model gap. If the rule does not bind
   here, it does not bind anywhere, and the low agreement of run 18 was never about declaration depth.
5. **Fewer than 5 requirements of 68 close with a residue**, and every residue is named. A high count
   means either the list demands what the model cannot express, or the completeness check is being
   answered honestly for the first time — and the two are distinguished by reading which requirements.
6. **Fewer than 20% of skeleton nodes end empty**, and those that do are judged infrastructure. Held
   in run 18; carried forward unchanged.
7. **No requirement is silently absent.** Every id of the 68 appears in the completeness table. A
   failure here is an exception under A0, not a finding.

## Isolation

Both runs went through the `model-builder` definition (`tools: Glob`), which enforces the prohibition
on reading repository files by the absence of tools rather than by instruction. Identical prompts, no
shared context, launched together, neither told of the other.

---

# Results

Both runs returned with `tool_uses: 0`. Raw in `run19_raw/HM19-OA1.md` and `HM19-OA2.md`; the
comparison is `run19_raw/coverage_run19.py`.

## 1. Readings

| reading | OA1 | OA2 | ratio |
|---|---:|---:|---:|
| skeleton | 68 | 21 | ×3.24 |
| accretion | 9 | 99 | ×11.0 |
| **anchored (skeleton + accretion)** | **77** | **120** | **×1.56** |
| completion (derived) | 10 | 11 | ×1.10 |
| nodes before normalisation | 87 | 131 | ×1.51 |
| nodes after normalisation | 78 | 129 | ×1.65 |
| collapsed at closure | 9 | 2 | |
| coverage assignments (requirement, node) | 96 | 136 | ×1.42 |
| nodes per requirement, mean | 1.41 | 2.00 | ×1.42 |
| co-located requirement pairs | 44 | 41 | **×1.07** |
| requirements whole at closure | 68/68 | 68/68 | — |
| deferrals | 0 | 0 | — |
| ambiguity flags | 16 | 17 | — |

## 2. Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | both runs execute 1.1 as written | **CONFIRMED**, and both found defects in the rules — §4 |
| 2 | anchored total agrees within ±5% | **REFUTED**: ×1.56 |
| 3 | derived spread exceeds anchored spread | **REFUTED, and inverted**: derived ×1.10, anchored ×1.56 |
| 4 | relations within ×2 in size **and** Jaccard above 0.5 | **SPLIT**: size ×1.07 — confirmed with room to spare, against ×8.7 in run 18. Jaccard **0.308** — not confirmed |
| 5 | fewer than 5 requirements close with a residue | **CONFIRMED**: zero in both, and zero partial marks standing |
| 6 | fewer than 20% of skeleton nodes end empty | **NOT SCOREABLE** — the test changed meaning under 1.1; see §4 |
| 7 | no requirement silently absent | **CONFIRMED**: 68 of 68 in both |

## 3. The result: the freedom moved, it did not go away

Run 18 measured the freedom in **completion** — derived nodes differed ×4.56 between models while
anchored structure held to ×1.036, and the document concluded that the anchor bounds how much
structure exists. Run 19 finds the opposite arrangement in the same instrument one version later:

- **completion is now the stable part** — 10 nodes against 11, and their content largely agrees:
  both runs derived supplier credential recovery, notification delivery retry, integration failure
  handling and configuration history from structure alone, unprompted and independently;
- **the anchored part is where the two runs diverge** — 77 against 120.

The mechanism is visible in the coverage assignments. M2 v1.1 forces coverage down to the node that
realises the obligation and forbids a partial verdict from surviving closure. A run satisfying both
must enumerate the **parts** of each requirement as nodes — and how many parts an obligation has is a
judgement nothing bounds. OA1 read requirements as mostly single-part (1.41 nodes per requirement);
OA2 read them as compound (2.00). That single ratio, ×1.42, carries almost the whole node-count gap.

**So 1.1 removed the freedom of declaration depth and exposed a partition freedom underneath it.**
This is the third time this project has watched the same thing happen: C1 fixed leaf size and leaf
count went free; closure fixed leaf count and granularity-within-an-element went free; M2 v1.1 fixed
where coverage is declared and the number of parts went free. The freedom is not being removed by
these rules, it is being **relocated to a place where it can be seen and counted** — which is
progress, but should stop being described as binding.

**What 1.1 did bind, and it is not nothing.** The amount of declared co-location came within ×1.07,
against ×8.7 across the four run-18 models. The instrument's readings are now comparable between runs
in a way they demonstrably were not: run 18's Jaccard figures were capped by relation sizes differing
by a factor of nine, and that cap is gone. What replaced it is a real disagreement — at ×1.07 in size,
the two runs share only 20 of 65 co-location statements.

**Jaccard 0.308 in the easiest case available.** Same model, same order, same input to the letter, no
model gap, no order effect. Two runs of one instrument agree on 68 of 68 requirements being wholly
covered, on how much co-location to declare — and on less than a third of what goes with what. That
is the honest state of structural agreement in this generation.

## 4. Two defects in the rules, both found by the runs

**The stale engine stamp.** The output-format section of the sensor definition still said
`Hotyn-M 1.0` while the identity section said 1.1 — an error introduced when M2 was amended. **Both
runs caught it, both stamped 1.1, and both reported the inconsistency rather than honouring the stale
literal.** One of them gave the reason: a 1.0 stamp on 1.1 readings "would make the two instruments
indistinguishable, which is precisely what the versioning exists to prevent." That is the behaviour
the definition asks for, exercised on the definition itself.

**M4's empty-skeleton test broke under M2 v1.1, and both runs said so independently.** Under 1.0 an
aggregate held the coverage of what sat beneath it; under 1.1 it holds none by rule. Applied to *own*
coverage the test reports every aggregate as a finding — 13 in OA1, all 21 in OA2 — which is a false
positive manufactured by the coverage rule. **The test must be applied to total coverage**: a skeleton
node is a finding when nothing in its subtree covers anything. Applied that way OA1 reports zero and
OA2 reports two genuine wrong guesses, both collapsed at closure.

Two related observations, both from OA1:

- **`stated` and `implied` no longer mean what they meant.** With coverage pushed to the realiser, a
  grouping node and a derived node are both `implied`. Provenance must be recorded by **origin** —
  posited, accreted, derived — not by whether the coverage set is empty.
- **The derived fraction is only stable measured before normalisation.** Three collapses in OA1 merged
  stated nodes into completion-derived leaves, so afterwards "derived" and "carries no coverage" are
  different sets.

And one cost of an existing rule, reported rather than repaired, from OA2: after S21 collapsed, the
Feedback Record ended up parented to the root rather than to the booking domain, because M5 forbids
moving a node once added. The run recorded the odd parent instead of quietly fixing it, which is the
rule working — and it is worth knowing that only-adds buys its monotonicity with structural debris.

## 5. What cannot be concluded from two runs

**The ×1.56 cannot be attributed to 1.1 with the data in hand.** Run 18 never measured a within-cell
repeat: every cell was n=1. Either 1.1 introduced this divergence, or it was always there and four
runs landing at 82–87 was luck. The two readings are distinguishable and the experiment is cheap —
**two repeats under 1.0 on the same list** — and until it is run, "1.1 loosened the anchor" is a
hypothesis, not a finding.

What can be said without that experiment: **under 1.1, two identical runs differ by ×1.56 on the part
of the structure the requirement list is supposed to bound.** That is a measurement of the instrument
as it stands today, whatever its history.

**And n=2 gives a difference, not a spread.** Everything above rests on one pair.

