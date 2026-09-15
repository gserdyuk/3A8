# SAS — Run 60: Steps C, B and D on the 2.1 chain's reading — the calibrated figures of two chain versions, side by side

**2026-09-16.** The last stage of the regression of the chain through the plugin entry point. Run 48 (2026-09-08)
calibrated and diagnosed the 1.1 chain's reading of SAS (run 47: 38 118 net task hours). Run 60 does the same for the
2.1 chain's reading (runs 57–59: 33 444 h, band 31 954–34 933), against the **same** two reference-class readings
(run 46), so that the two versions can be compared after calibration and not only before it. Two parts, two child
processes, each through `/3a8:estimate`, each one sensor:

- **Part 1, Step C.** `3a8:rates-step-c` (`Lytin-K 1.1`), Opus 5, gap-blind: project brief and assumption log as run
  48's Step C prompt had them, verbatim; INPUT 3 and INPUT 4 rewritten from the run 59 assembly and the fourteen sizing
  readings. No class figure, no target, no other estimate. Prompt `run60_raw/prompt_step_c.md`, md5
  `b19256233b0b691416d5093290156746`; reply `run60_raw/RK60.md`; one turn, `end_turn`, 38 112 output tokens.
- **Part 2, Steps B and D.** `3a8:diagnostician` (`Lytin-G 1.1`), Opus 5: run 48's prompt with INPUT 1, INPUT 2 and
  INPUT 4 (both RC46 readings) verbatim, INPUT 3 the run 59 assembly output verbatim, INPUT 5 RK60 verbatim, and the
  precomputed bases of §1 below; told that no outcome exists; the house unit conversion withheld, as in run 48. Prompt
  `run60_raw/prompt_steps_bd.md`, built by `run60_raw/make_prompt_bd60.py`, md5 `65c93ae92a28432ec0d97d4ce2a82724`;
  reply `run60_raw/RG60.md`; one turn, `end_turn`, 23 950 output tokens, **in English** (run 48's came back in Russian).

Run 48's prompts were not saved at the time; both were recovered from the harness transcripts and are now in
`run48_raw/prompt_step_c.md` and `run48_raw/prompt_steps_bd.md` with a provenance header. Every prompt of run 60 was
pinned with its md5 before launch; both manifests are in `run60_raw/MANIFEST.md`. Neither sensor's prompt names run 47,
run 48 or any of their figures; the one reference in the assembly output (a tree-depth aside) was struck before use.

---

## 1. What Step C returned, and why the orchestrator had to price it

`Lytin-K 1.1` returned a different **shape** of parameters from run 48's. Run 48 gave three targeted multipliers on
the element layer (declared holes +2.5%, closure violations +9%, XL coarseness ×1.30 on three leaves) and five flat
additions (load test, failover and DR rehearsal, WCAG, browser matrix, help content). Run 60 refused the generic omission
rate on the same ground — "this estimate carries every activity category" — and instead **triaged every named hole
and closure violation against the assumption log**, closed about half by assumption (A4 puts credentials in the IdM, so
no password-reset surfaces; A6 excludes QuickBooks/SAP connectors; the module-level record stores the sizing sensors
asked for are the shared domain data model at platform level), and returned the survivors as **counted fills to be
priced with the estimate's own rate table**: H, the genuine holes (the Access Data REST API's six items; migration of
the stores that match an A16 entity kind; the backup and DR statements in repeat 2), and C, the genuine missing work
(surfaces for screenless behaviours, other surfaces, behaviours, interfaces, stores, NFR verification targets, go-live
initial load), each with a count low / central / high and a parent to hang it under. Then a residual on level-of-effort
work priced once (T2, 6 / 8 / 11% on estimate + H + C), and the same two globals as run 48 in kind: G1 requirements
growth ×1.09 / 1.18 / 1.30, G2 domain inexperience ×1.05 / 1.10 / 1.22.

The diagnostician does not see the rate table, so the orchestrator priced the fills as **bases**, by RK60's own fill
rule — each fill is the Hotyn-W 1.2 element-attached item set of its class at size S / M / L, D4 at S, NFR targets at
the carried response-time element's A9 cell (class L, 46.7 h), integration at 20% per ancestor along the real path for
holes and under the named subsystem (×1.4) or its matching child node (×1.6) for closure fills — in
`run60_raw/price_fills60.py`, which wrote `bases60.md` (given to the sensor) and `orchestrator_recomputation.md` (not
given: the orchestrator's own application of RK60's order, made before the diagnostician returned, so its arithmetic
could be checked rather than trusted). The mapping of RK60's fill lists to parents and counts is the script's reading
of RK60 and is printed so it can be disputed.

| base, net task hours | repeat 1 low / central / high | repeat 2 low / central / high |
|---|---|---|
| H, hole fills, integration included | 138 / 373 / 787 | 152 / 409 / 847 |
| C, closure fills, integration included | 731 / 2 222 / 5 196 | 731 / 2 222 / 5 196 |
| B_T2 = estimate total + H + C | 35 802 / 37 528 / 40 916 | 32 837 / 34 585 / 37 997 |

## 2. Registered before the diagnostician returned

1. Stamps on everything; the declarations reconciled before attribution; no averaging; the chain applied mechanically
   in RK60's fixed order with running totals; the answer in three parts — as run 48 registered.
2. **The orchestrator's recomputation** (`orchestrator_recomputation.md`): calibrated centre **52 609 (r1) / 48 483
   (r2)**, ×1.51 of the raw total; low chain 43 434 / 39 837; high chain 72 031 / 66 892.
3. The reply in the language of the prompt.

## 3. Results

### Scoring

| # | expectation | outcome |
|---|---|---|
| 1 | stamps, reconciliation first, no averaging, three-part answer | **CONFIRMED** — §1a reconciles the three declarations through each reading's own hour column and its own touch-time factor (0.65–0.75 and 0.70–0.80, disputed between them, so both shown); repeats and readings carried as bands to the end |
| 2 | chain mechanical, recomputable | **CONFIRMED to the hour** — 52 608.3 / 48 482.6 central, 43 433.9 / 39 836.9 low, 72 031.0 / 66 892.2 high against the recomputation's 52 609 / 48 483, 43 434 / 39 837, 72 031 / 66 892; no rate touched; three uncovered spots answered by naming |
| 3 | language | **CONFIRMED** — English, 0 Cyrillic characters; run 48's drift did not recur |

### The final answer, `Lytin-G 1.1`, verbatim in substance

- **Centre: 48 483 … 52 608 net task hours** (repeat 2 … repeat 1, central chain).
- **Corridor: 39 837 … 72 031 net task hours**, the low-with-low / high-with-high envelope of the calibration — "not a
  P10–P90 and carries no probability label"; the structure's own ρ = 0.5 band (×0.80 / ×1.20) kept separate.
- **Reserve:** the raw class tails, both readings, converted by each reading's own factor: RC46-1 P80 69 888–80 640,
  P90 92 820–107 100; RC46-2 P80 35 112–40 128, P90 46 816–53 504. **RC46-2's P90 is at or below the calibrated centre;
  RC46-1's P90 lies 40–59 k h above it.** "The two readings do not agree on whether a reserve exists, and I do not
  choose between them."
- **Explained share:** against RC46-1 the chain accounts for 104–269% of the centre gap at RC46-1's own factor range
  (86–269% across the disputed range), the counted additions alone 34–85%, the crossing always at G1 or G2; against
  RC46-2 the corrections **widen** the gap, the calibrated centre sitting ×1.85–2.30 above its P50.
- **Residual, not closed:** 22.3–29.7 k h below the centre (RC46-2) through −11.1 to +2.6 k h (RC46-1), "dominated by
  the ×1.95 disagreement between the two class readings, which no rate touches", plus the unsized terms: scope
  narrowing by the log, era, the conversion seam, the component-4 seam in RC46-1.

In the comparison-layer convention (`docs/constants.md` §4a): the centre band's midpoint, 50 546 h, is ≈ **441 staffed
person-months** (run 48: 503).

### Findings

1. **Units first, again.** Converting the class readings' attended hours to net task hours explains 50–77% of the naive
   gap to RC46-1 and **manufactures** the naive convergence with RC46-2 (×0.94–1.02 as printed becomes ×0.65–0.82 after
   conversion): "units do not explain a gap; they hide one". The same lesson as run 48, on the same readings.
2. **The conversion seam, newly named.** The class readings' touch-time factor strips reviews, coordination and status
   time; the bottom-up prices some of exactly that as items (C3 ≈ 46% of element work, code review, status reporting).
   So the converted class figures may be too low by an unknown amount. Nothing in the inputs sizes it. This is the
   diagnostician's first "what would change this diagnosis" item: the house constant plus a declaration by the bottom-up
   of which in-day activities it prices.
3. **The calibrated centre lands where run 48's did relative to the class: above both medians at the readings' own
   factors** (×1.05–1.27 of RC46-1's P50, ×1.85–2.30 of RC46-2's), straddling RC46-1 only at the disputed factor edge
   0.80 — read as "coincidence at one point of a disputed conversion, not confirmation".
4. **Three spots the rates leave uncovered, requested as another gap-blind round:** UX / visual design (in both class
   readings' role lists, not visible in the carried activity categories); knowledge transfer for "maintainable by
   X-Customer resources" (only the 33-hour handover pack carries it); the rate table's row statistic and the XL class.
   The third is run 48's open request, restated.
5. **The tail hand-off landed in the class scenarios except one:** IE9 compatibility blowing up is owned by no
   instrument.
6. **Instrument debt from run 48 still open:** the assembly output declares no roles; the diagnostician again inferred
   them from the activity set and flagged the inference.

## 4. The two chain versions after calibration — the comparison this run exists for

| | run 48 on the 1.1 chain | run 60 on the 2.1 chain | ratio |
|---|---:|---:|---:|
| raw chain total, centre of the repeat band | 38 118 | 33 444 | **×0.877** |
| Step C shape | T1 +2.5% · T2 +9% · T3 ×1.30 on 3 XL · A-1…A-5 flat +970 h · G2 ×1.15 · G1 ×1.18 | H +373 / +409 · C +2 222 · T2 +8% · G1 ×1.18 · G2 ×1.10 | |
| overall calibration factor, central | ×1.50 / ×1.52 | ×1.506 / ×1.517 | |
| **calibrated centre, band** | **57 423 – 57 791** | **48 483 – 52 608** | **×0.877 on the midpoints** |
| corridor (calibration spread) | 48 092 – 74 123 | 39 837 – 72 031 | |
| staffed person-months, §4a | 503 | 441 | ×0.877 |
| centre against RC46-1's P50 (own factor) | ×1.21 | ×1.05 – 1.27 | |
| centre against RC46-2's P50 (own factor) | ×2.35 | ×1.85 – 2.30 | |

**The ratio survived calibration unchanged: ×0.877 raw, ×0.877 calibrated.** Not by construction — the two rate sets
have different shapes, run 48's targeted multipliers and flat additions against run 60's counted fills and level-of-effort
residual — but because both gap-blind rounds read the same coverage report in the same way (thorough estimate, no
generic omission rate, two modest globals) and arrived at the same overall factor, ×1.51, on both structures. The
whole difference between the two chain versions is therefore the skeleton's price (run 59 §2a: C3 at 46% of leaf
effort against 54%, per-parent items ×0.49), carried through calibration one to one.

What is **not** the same: the corridor's lower edge (39 837 against 48 092, because the 2.1 repeats span ×1.09 where
the 1.1 repeats spanned ×1.003 — the shared-obligation question of run 59 §3 reaches the final figure as a wider band),
and the position against the class, where the 2.1 centre sits closer to RC46-1's median and no longer clears its P50
at every factor.

**On the regression question, closed.** The chain through the plugin entry point, on a 2.1 model, produces a
calibrated estimate that differs from the estimate of record by the measured price of the 2.x skeleton and by nothing
else traceable. Every stage ran in one turn under the raised cap, every prompt was pinned before launch, every raw
reply came from the transcript. The SAS estimate of record remains `estimate_SAS_2026-09-08.md` (the 1.1 chain,
57 600 h); run 60's figure is the 2.1 chain's reading of the same case, drawn on the report beside it, not replacing it.

## 5. What run 60 opens

- The shared-obligation rule for sizing (BACKLOG 2026-09-16): its ×1.09 reaches the calibrated band.
- The conversion seam: a roles-and-in-day-activities declaration in the assembly output (the run 48 roles debt, now
  with a second reason).
- The gap-blind rounds requested twice: rate-table row statistic and XL class; UX design and knowledge transfer
  coverage.
- A counted functional size for SAS (`Hotyn-P 1.0` exists), which both diagnoses name as the one fact that would pin
  the class centre.
