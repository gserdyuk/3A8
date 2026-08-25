# The instrument — the current estimation chain, end to end

`METHODOLOGY.md` is the **frame**: several sensors with structurally different blind spots, a
diagnosed divergence, mechanical calibration, a range with an explained residual. It does not change.

This file is the **current implementation** of that frame — what actually runs today, in what order,
on what inputs, with what pinned at each step. `PIPELINE.md` states who is allowed to see what and how
that isolation is enforced; this file states what happens.

Generation: **`Hotyn`** (product model → work model → size classes → table prices), in force since
2026-08-19. Its predecessor `Lytin` (one sensor decomposing an RFP straight into priced work) is a
closed generation; its record is kept, its outputs do not cross the boundary without a measured
conversion.

---

## 0. The unit

> **Effort is working time spent solving the task, stated in person-hours.** One person-day, where
> one is used for readability, is 8 such hours; a week is 40.
>
> **Leave, public holidays, sickness, bench time and non-project duties are not included, and are
> not parameters of this method.** Neither is the effective yield of an assigned working day, nor
> working days per month. How an organisation behaves is a true and important fact about that
> organisation and not a fact about the work.
>
> **If you need days of presence, convert with your own figures:** divide by the effective task hours
> your working day delivers — commonly 5 to 6, never 8 — then add your own allowance for leave.

In the WBS part, time appears **in this declaration and nowhere else**. That is a statement about a
finite body of text and code, so it is mechanically checkable. The method's full constant list, and
what was removed to get to it, is `docs/constants.md`.

## 1. The design principle, in one sentence

**Numbers come from a table; the model only chooses rows.**

Six weeks of measurement established why (`docs/review_2026-08-21_running_in_circles.md`): rules that
constrain the *form* of an estimate — leaf size, coverage, item provenance — bind exactly what they
name, and the magnitude then relocates into whichever variable was left free. The floor of that
programme was measured directly: a baseline with **no method at all** gave CV 8.55%, and no version of
the method ever significantly beat it. The magnitude has to leave the model or it is sampled afresh
every run.

So the chain is built as three sensors that produce **no effort figures of any kind**, one pinned
table of constants they never see, and a script that joins them.

| where a number comes from | measured repeat-run agreement |
|---|---|
| a script | exact |
| a pinned table | exact |
| classification against pinned rules | ×1.03 |
| structure read out of a document | ×1.02 – ×1.56, depending on the input's density |
| **a magnitude sampled by a model** | **×1.3 – ×2** |

---

## 2. Inputs, all pinned before anything runs

| input | what it is | example |
|---|---|---|
| **requirement list** | stable ids, md5-pinned, never reshaped by any sensor | `examples/FaxRxTx/requirements_pinned.md` |
| **the split** | the list divided into **product obligations** (what the thing must be) and **demanded work** (work the client explicitly requires: migration, parallel run, decommissioning) | `requirements_split.md` → `requirements_product.md` + `requirements_work.md` |
| **assumption log** | every reading the documents leave open, adjudicated once for everybody. This is where the team's tacit knowledge enters, and it stays a human decision | `assumptions.md` |
| **technology declaration** | one entry per dimension of `docs/technology_catalogue.md`, each naming the activities it mandates, plus parameters: environment count, cycle counts, staffing of once-scoped stages | `technology_declaration.md` |
| **rate table** | O/M/P per (activity × element class × size class), external norms, gap-blind, **stated in person-hours** | `docs/rate_table.md` |
| **case profile** *(required from case 2 onward)* | the conditions the work was or will be done under: team grade and domain experience, declared overheads, the presence fraction, the process, the staffing of every separately-priced stage | not yet formalised — `BACKLOG.md` |
| **`FACT.md`** | the outcome, if one exists. **Sealed.** Opened only after the estimate is written and closed | `examples/FaxRxTx/FACT.md` |

**A case whose conditions arrive after its number can be learned from; it cannot score.** That rule
cost three days and one validation case to arrive at.

---

## 3. The steps

### Step 0 — pin, split, declare

The orchestrator's work, not a sensor's: fix the requirement list and its md5, split it, write the
assumption log, write the technology declaration with its parameters and its **visible scope
decisions** (each a named fork, e.g. direct client acceptance vs staged UAT, seeded data vs migrated
data). Scope decisions are declared, never inferred, and each one is separately priceable afterwards.

### Step 1 — the product model · `Hotyn-M 1.1`

**In:** the pinned product obligations, a declared processing order, the assumption log.
**Out:** a tree of the thing to be built — one root, elements with id, name, parent, and the set of
obligation ids each **realises**. No numbers of any kind beyond counts.

Binding rules: the requirement list is the anchor and may not be reshaped (an entry that holds two
obligations is *flagged ambiguous*, not split); a node's identity is the set of requirements it
covers, never its name; at closure every obligation must be placed or explicitly reported unplaced.

**Measured:** two identical runs place the same obligations but disagree on **what goes with what** —
Jaccard 0.31 (BMS) / 0.41 (FaxRxTx) — and on structure size by ×1.56 (BMS) / ×1.02 (FaxRxTx). **This
is the chain's least stable step**, and how unstable depends on how densely the source describes
structure. Whether that spread is instrument defect or the honest multiplicity of designs over an
under-determined document is **not settled**: no human control has ever been run.

### Step 2 — the work model · `Hotyn-W 1.1`

**In:** the closed product model, the technology declaration and its parameters, the demanded-work
list.
**Out:** the structure of the *doing* — one item per (element × mandated activity), plus branches for
demanded work no dimension absorbs. Still no numbers.

Binding rules: **no activity may be invented** — activities belong to the declaration, and work the
product plainly needs but no declared activity covers is reported as a **finding**, never created as
an item; the product model may not be reshaped. Every refusal is labelled **filter** (the rules
exclude it) or **judgement** (the crosser declined).

**Measured:** Jaccard **0.969** over 77 elements and 553 pairs; every difference traced to three
classification calls. This step is very nearly a function.

### Step 3 — size classes · `Hotyn-D 2.0`

**In:** the work model and the pinned sizing rules — what is enumerated per element class, the
S/M/L/XL thresholds, the statement kinds, the special counts.
**Out:** a size class per element, each justified by an **enumeration** ("3 actions: rank offers,
re-rank on change, explain ranking"). **No person-days, no units, ever** — it must stop and report
contamination if it is shown any rate, price, budget or prior estimate.

Element classes: `interface` · `behaviour` · `store` · `statement` · `surface`; aggregates are never
sized. An element the rules cannot size is a **named hole**, reported, never guessed.

**Measured:** two repeats sized 74 of 79 elements each and disagreed on 10 element classes of 79
(87.3% agreement) — which after pricing is **×1.03 on the total**.

### Step 4 — the arithmetic · a script, no model involved

Joins classes to the rate table. `E = (O + 4M + P) / 6` per cell. Integration is priced as **C3: 20%
of the rooted subtree's leaf effort at every parent, including the root**, never compounding;
once-scoped, per-environment and demanded items attach to the work model and enter no C3 base.

Output: the total in **net person-hours**, the layer breakdown, and the list of named holes. Determinism
is the point: the same inputs give the same number, and any difference is a bug.

### Step 5 — the outside view · `Lytin-R 1.0`

Runs in parallel and in ignorance: it sees the project description and the assumption log, never the
model, the work items, the table or any total. Produces P10 / P50 / P80 / P90 for a named class, the
class's membership test, and its own static blind-spot list. It is generation-agnostic by construction
— it never sees the chain, so it needs no port to a new generation.

**Measured:** first repeatability reading, P50s ×1.31 apart, the spread **narrowing toward the tail**
(×1.55 at P10 → ×1.24 at P90).

### Step 6 — diagnosis, calibration, final range · `Lytin-K 1.0` + `Lytin-G 1.0`

Step B interprets the divergence through each method's known blind spot rather than averaging it.
Step C takes named corrections from a **gap-blind** rate source — one that never sees the reference
class result or the size of the gap. Step D reports the range with its explained and unexplained
residual, and **full convergence is not a success criterion**: methods that answer structurally
different questions and land on one point have either coincided or lost their independence.

---

## 4. What the chain does not have

- **A corridor.** It declares no P10–P90. `ΣO…ΣP` assumes perfect correlation across ~580 items and
  spans ×4.3; leaf independence gives an absurdly narrow band both earlier generations flagged as an
  artefact. Neither is an 80% interval, and the correlation between them has never been measured.
  Consequence: **one of the exit criterion's three tests cannot be scored at all.**
- **A calibrated table.** The rates are external norms, fixed as constants by decision, calibrated
  against no outcome yet.
- **A brake on over-counting.** The design only adds — accretion and completion add, the crossing
  multiplies, splitting inflates, the floor rounds up, nothing may be removed — and the instrument
  that would check the other direction (the reverse audit) is designed and has never been run.
- **Knowledge of the team.** Team capability spans ×2–3 between grade bands; the table declares the
  grade it assumes and nothing downstream reads it.

---

## 5. Standing, and what would change it

`docs/exit_criterion.md` v1.0 is the definition of done: over **≥ 4 cases with documented outcomes**,
none used for fitting — calibrated P50 within ×1.3 on at least 3, declared P10–P90 covering the actual
on at least 3, and no parameter fitted on the case it is scored against.

**Today: 1 of ≥ 4 cases · 1 of 1 passing on the centre.** FaxRxTx, ×1.21 against a remembered
outcome, both classification repeats inside the gate, nothing fitted on the case. Case 1 was admitted
on conventions supplied after the estimate existed and therefore sets the **floor, not the standard**:
for cases 2–4 the case profile is pinned before any estimate exists.

Current state of every claim, and what stale documents say instead:
`docs/status_2026-08-25.md`.

---

## 6. Reproduction

```bash
python examples/FaxRxTx/run31_raw/assemble_faxrxtx.py
```

```bash
python examples/BMS/run25_raw/assemble.py
```

Each prints the total, the layer breakdown, the named holes and the repeat spread. Every sensor run
behind those numbers is transcribed verbatim under `examples/*/run*_raw/` — the harness does not
persist subagent output, so those files are the durable record.

---

## 7. Version stamps

Every sensor states its own engine name and version in every reading; the orchestrator records the
model it was launched on. **An estimate is a property of the triple (project × engine × model)** — the
model coordinate outweighs the entire version history, measured at ×2.02 (t = 14.70) against version
steps of +0.4% to +30%. A batch on a different model is a different instrument, not a replication.

| role | engine | definition |
|---|---|---|
| product model | **`Hotyn-M 1.1`** | `.claude/agents/model-builder.md` |
| work model | **`Hotyn-W 1.1`** | `.claude/agents/work-crosser.md` |
| size classes | **`Hotyn-D 2.0`** | `.claude/agents/work-estimator.md` |
| rate table | **`Hotyn-K 1.0`** | `.claude/agents/rate-table-author.md` |
| outside view | **`Lytin-R 1.0`** | `.claude/agents/estimator-reference-class.md` |
| Step C rates | **`Lytin-K 1.0`** | `.claude/agents/rates-step-c.md` |
| Steps B, D | **`Lytin-G 1.0`** | `.claude/agents/diagnostician.md` |
| version probe | **`Lytin-F 5.0`** | `.claude/agents/version-probe.md` |

The probe is run before the first batch of a session: an edited definition is loaded at session start,
so a sensor can otherwise run under a version nobody intended.
