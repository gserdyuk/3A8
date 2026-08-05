# Pending notes from a side branch (2026-08-05) — partially merged

Conclusions produced in a forked line of reasoning that ran in parallel with the variance
measurement (`examples/BMS/run6_variance.md`) and the introduction of the method constants.
Written in English to match the merge targets; delete this file once nothing is left unmerged.

Context these notes react to: the first end-to-end wrapper run (`examples/FaxRxTx/run5_agent_pipeline.md`)
overshot the sealed fact by ×4.2, and the n=10 variance study showed ±17% run-to-run spread with a
×2.36 level shift between sensor specifications.

---

## MERGED 2026-08-05 — group 1, before the re-measurement

Merged because each item changes *what is being measured*, so it had to land before the runs.

- **A4 — migration / coexistence / cutover branch.** Now branch 9 of C2 in the decomposition sensor and in PIPELINE.md. Rationale kept: branches 1–8 and 10 describe the product, this one the project; on FaxRxTx the work was ~19% of the estimate and defined the class the other sensor chose. Marked "none, because greenfield" where it does not apply.
- **A1 + A5 — static blind-spot lists as constants.** Now C4. Both sensors carry a fixed list, reported verbatim and kept separate from the project-specific list; the reference-class list is symmetrical to the decomposition one so the diagnostician can attribute a divergence of either sign.
- **B1 — the partition.** A category is a mandatory branch *or* a blind spot, never both and never neither. In `calibration-rates.md` as an explicit check and in PIPELINE.md as discipline 1a.
- **B2 + B3 — completeness report wired into the rate agent.** The decomposition sensor emits it (branch by branch, filled ÷ *applicable*); the rate agent receives it, and must state how it moved the rates. Gap-freeness argument kept verbatim.
- **Added during the merge, not from this document — a cap of two global multipliers.** A fixed catalogue of blind spots invites charging for every entry, which is the ×1.72 stack institutionalised. Globals compound; targeted and additive corrections do not. Everything beyond two whole-project effects must be targeted or additive.
- **D1** — the retracted 0.91 correlation removed from the conclusions of `run6_variance.md`.
- **D2** — the inverted prediction corrected in PIPELINE.md and findings §12c. Splitting conserves the sum, so C1 does not lower the level; with unpacking it plausibly raises it. Recorded together with the methodological point: a prediction registered in advance is worth nothing unless it is also *checked* in advance.

## Modified during the merge

- **A2 — "open, at rate R" was split in two.** The decomposition sensor must not name rates: doing so is Step C work performed while looking at its own tree. The catalogue therefore gets two responses — the sensor answers *covered by branch X / not applicable / open*, and the rate agent answers the same catalogue with *form + rate*. A3 (the catalogue fixes the form, not only the rate) attaches to the second half.
- **B4 — declare a fact, not a label.** As written, handing a project-type declaration to both sensors gives the reference-class sensor part of its own answer and quietly destroys the independence that B5 depends on. The assumption log should state a *fact* ("a predecessor exists and must stay live during the transition"), which is already in the requirements, rather than a *class label* ("this is a rewrite"). The type is not passed to the reference-class sensor at all.

---

## NOT YET MERGED — group 2, after the re-measurement

Deliberately deferred: these are superstructure that does not change what the re-measurement measures, and they will be better informed once the spread of the constrained instrument is known.

- **A2 / A3 — the blind-spot catalogue** in the two-response form above: fixed entries, three admissible answers from the sensor, form-and-rate from the rate agent, free text kept as an addendum so the catalogue is a floor and not a ceiling.
- **B4 / B5 — project type and the branch signature.** The pattern of filled and empty branches is a machine-readable form of the class-membership criterion of §11.4, and gives a cross-check that does not exist today: the class sensor names its class, the tree yields its signature, and a disagreement is visible *before* any numbers are compared.
- **C1–C4 into findings.md**, in particular C1 (the decomposer is judge in its own case: thoroughness grows the tree *and* the hole list, where the two should move in opposite directions — the mechanism behind the ×4.2) and C3 (an estimate is a property of the pair project × instrument).

## NOT YET MERGED — group 3, deferred

- **B6 — catalogue versioning.** One version exists; machinery is premature. Record only the intent: keep versions **nested** (v2 = v1 + new entries with an explicit mapping) so a v2 tree can be projected onto v1 and a version change re-projects history instead of breaking it. Whether two versions are comparable at all is an empirical question with a cheap experiment attached — one case, n runs per version, level shift against the known ±17% scatter.
