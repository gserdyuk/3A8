# Run 27 — `Lytin-G 1.0`, Steps B and D — transcribed verbatim

`tool_uses: 2` — **Glob only, filenames only**: the run listed artifact paths for its inventory,
opened none, and explicitly declined to open the pre-existing `run27_steps_BD.md` ("a prior occupant
of this slot would contaminate the diagnosis"). This is the documented Glob-residual behaviour, same
as the Lytin-era rate agent's. Model: Opus 5 (orchestrator-recorded).

---

**Engine:** `Lytin-G 1.0`
**Inputs by engine stamp:** product model `Hotyn-M 1.1` (68 obligations → 78 elements) · work model
`Hotyn-W 1.1` · size classification `Hotyn-D 2.0` (repeat agreement ×1.016–×1.000) · pinned external
uncalibrated rate table (O/M/P, PERT E) · reference class `Lytin-R 1.0` × 2 independent repeats ·
Step C rates `Lytin-K 1.0` (gap-blind).

## 1. Input inventory

Received: the project description and declared narrowings · the assumption log · method 1 as a
two-point branch **B ∈ {1342.13, 1352.92} pd** with composition, three named unpriced holes, the
carried service, and the precomputed T1 base (85.76 pd own items → **102.9 pd**) · method 2 as two
`Lytin-R 1.0` repeats with quantiles and three method notes · the five Step C rates in fixed order
with constraints and the deliberately-uncorrected list.

**The project's actual outcome was not among the input. It does not exist** — a training RFP; the
pipeline terminates at Step D here, and the orchestrator should record that no fact-comparison step
is possible downstream.

By role: no quantity derived, no rate changed/added/dropped, the 1342/1353 branch and the unit
convention not adjudicated (a frame is stated; no factor applied), nothing averaged — not the two RC
repeats, not the two methods. Artifact paths listed, **no artifact contents read**.

## 2. Step B.1 — raw divergence

**Unit-convention decision, stated before comparing.** As *declared*, the conventions match (both
say "net 8 h"). As *sourced*, neither is verified: RC anchors are acknowledged assigned-day records;
the rate table is an external norms table of unverified provenance whose calibration sign
`Lytin-K 1.0` declared unknown. The doubt is symmetric and unresolved, and applying ×0.8 to one side
while looking at the gap is precisely the forbidden move. **Decision: compare at declared face
value; carry both ×0.8 forks as stated sensitivities; apply neither.**

| metric | method 1 (bottom-up, uncalibrated) | method 2 (class band, 2 repeats) | gap |
|---|---:|---:|---|
| **centre** (face value) | 1342.13 / 1352.92 (branch) | P50 = 800 … 1050 | **+292 to +553 pd; ×1.28 to ×1.69** |
| centre, fork (a-i): RC strictly net (×0.8) | 1342.13 / 1352.92 | 640 … 840 | +502 to +713; ×1.60 to ×2.11 |
| centre, fork (a-ii): rate table as assigned days (×0.8) | 1073.70 / 1082.34 | 800 … 1050 | +24 to +282; ×1.02 to ×1.35 |
| lower tail P10 | **none — no distribution exists** | 420 … 650 (floor ≈350–500) | not comparable |
| upper tail P80 | none | 1250 … 1600 | not comparable |
| upper tail P90 | none | 1650 … 2050 | not comparable |
| within-method-2 reproducibility | — | P10 ×1.55 · P50 ×1.31 · P80 ×1.28 · P90 ×1.24 | — |
| branch width inside method 1 | 10.79 pd (0.80%) | — | — |

Two facts fixed before any diagnosis:

- **The sign is inverted from the pipeline's usual case.** The bottom-up sits *above* the class
  median — at ≈P66 of repeat 1 and ≈P82 of repeat 2 before any correction. Every supplied correction
  is upward, so the corrections cannot be gap-closers here; they are blind-spot fills that widen the
  divergence. This is the headline.
- **The within-method-2 spread is of the same order as the between-method gap** (250 pd at P50
  against a 292–553 pd gap): 45–86% of the gap being diagnosed is inside method 2. Any "method 1
  exceeds the class by X" is meaningful only to ±250 pd.

Method 1 has no tail row and never will: a bottom-up structure produces a point (here a branch), and
its post-calibration low/high are naive band ends that `Lytin-K 1.0` declared not percentiles. The
empty tail cells are structural, not missing data.

## 3. Step B.2 — blind spots already covered (restated from the rate agent's check)

Already inside method 1, so deliberately not corrected: integration at 20% at all 18 parents incl.
root (≈371–374 pd, ≈181 at root) — T1 never touches it · PERT-P in the table — T1 is the residual
beyond it · mobilisation set-up — A-RAMP prices only the forming deficit · vendor-internal
coordination — G2 prices only the cross-company residual · the ≈64 pd once-scoped layer · the
declared assurance/UAT/environment/docs/pentest technology · the 68-obligation discipline (G1
reduced on that account) · sizing noise measured at ×1.016–×1.000 (no correction owed).

Handed over deliberately uncorrected: the four refused-reading step events (tail material, not
multipliers) · the rate-table calibration status (sign unknown — spread, not correction) · the
effort→calendar conversion · the carried service (blocked on "the term") · the 1342/1353 branch
(adjudication debt) · three coverage flags returned for verification (DPA/privacy work · responsive
baseline of the table · legacy-migration absence).

## 4. Step B.3 — the gap decomposed into named items

**Directional attribution only** — no person-days assigned to any spot: no supplied rate covers
them, and a number invented here is exactly the failure the pipeline exists to prevent.

Items placing method 1 high: **D1 — the recursive assembly convention** (structural): 20% at all 18
parents including the root is a modelling rule; the ≈181 pd of root assembly is a line no class
project reports separately, and it alone is **33–62% of the face-value centre gap** (arithmetic on
given figures). The largest single candidate for the sign inversion; a model-construction question,
not a rate question. **D2 — rate-table level, sign unknown** (spread; live in either direction).
**D3 — the narrowings run the other way**: all four push method 1 *down*; it is high despite them,
strengthening D1 and D2.

Items placing method 2 low: **D4 — class misclassification, the RC engine's own flag**: stated-class
weight 0.60–0.65, up-neighbours outweigh; at the mildest up-neighbour factor (×1.3) repeat 1's P50
moves 1050 → 1365 and **brackets the raw base** — the RC's self-declared most-likely error mode
accounts for the sign and roughly the span of the whole face-value gap. Not applied: it is the RC's
uncertainty statement, not a rate. **D5 — RC reproducibility** ×1.31 at P50: an instrument-noise
floor bounding how sharply anything can be stated.

Frame items: **D6 — unit provenance**: a ×1.25 lever on the whole comparison, direction unresolved;
larger in effect than any single correction in the chain. **D7 — scope parity confirmed**: the
carried service is outside both sides; no correction owed.

Reaching neither number: **D8 — the four refused-reading step events**: a step event is not an item,
no multiplier reaches it; implicitly inside the class's upper quantiles, explicitly absent from the
structure — and per Step D, currently **unreserved**. **D9 — the 1342/1353 branch is immaterial**
(≤0.9% everywhere): explicitly ranked so no effort is spent resolving it in the hope of moving the
answer.

**Blind spots NOT covered by the supplied rates — request for a further gap-blind round, holes named
and not filled:** **U1** risk correlation across the six counterparties (nothing in the chain is a
joint-slip term; would have to arrive targeted/additive under the two-global cap) · **U2/U3/U4** the
three coverage flags (absent DPA work → an H4 of the H-species; desktop-only table baseline → a
targeted item on the three portals; a hidden migration → a **missing element**, back to `Hotyn-M`,
not to rates) · **U5** the step events are unreserved (see Step D) — either a gap-blind step-event
sizing round or an explicit tail-less bid stated on its face · **U6** unit provenance blocks the
comparison itself — a frame hole, not a rate hole.

## 5. Step C — the calibration chain (mechanical, fixed order, recomputable)

| # | correction | low | central | high |
|---|---|---:|---:|---:|
| 0 | base B (branch) | 1342.13 / 1352.92 | 1342.13 / 1352.92 | 1342.13 / 1352.92 |
| 1 | T1 on 102.9 pd only — ΔT1 | +20.58 → 1362.71 / 1373.50 | +41.16 → 1383.29 / 1394.08 | +77.18 → 1419.31 / 1430.10 |
| 2 | +H1+H2+H3 | +27 → 1389.71 / 1400.50 | +56 → 1439.29 / 1450.08 | +119 → 1538.31 / 1549.10 |
| 3 | ×G1 | ×1.08 → 1500.89 / 1512.54 | ×1.15 → 1655.18 / 1667.59 | ×1.28 → 1969.03 / 1982.84 |
| 4 | ×G2 | ×1.06 → 1590.94 / 1603.29 | ×1.12 → 1853.81 / 1867.70 | ×1.22 → 2402.22 / 2419.07 |
| 5 | +A-RAMP (outside globals) | +20 → **1610.94 / 1623.29** | +45 → **1898.81 / 1912.70** | +85 → **2487.22 / 2504.07** |
| | implied factor on base | ×1.200 | ×1.415 / ×1.414 | ×1.853 / ×1.851 |

T1 was applied to 102.9 pd and nothing else; the ≈371 pd integration line untouched. Branch width
never exceeds 0.9% of the running total. The low/central/high columns are a **naive band, not
percentiles** (the rate agent's constraint, restated).

## 6. Step D — the final answer

**Centre — 1899–1913 pd** (branch legs 1898.81 / 1912.70; ×1.41 on base).

**Corridor — 1611–2504 pd** (spread of the supplied rates; no P-value on either end). Against the
class band, for reading only: naive low ≈ P80 (rep. 1) / ≈ P89 (rep. 2) · **centre ≈ P86–87 (rep. 1)
/ above P90 (rep. 2)** · naive high ×1.21 / ×1.51 above the P90s. **The whole calibrated corridor
sits at or above the class P80 on both repeats.** Nothing in either method supports a number near
the class floor.

**Reserve — the raw class tail as it stands: P90 = 1650–2050 pd; P80 = 1250–1600.** Uncalibrated,
untouched, correctly so. **And this is where the answer is honestly uncomfortable, stated rather
than smoothed: the calibrated centre sits above repeat 2's P90 and inside repeat 1's P80–P90. The
raw class tail provides no headroom above the calibrated centre. There is no reserve to draw.** The
four refused-reading step events are consequently **unreserved by this pipeline** — sized by
nothing, covered by nothing. The bid either carries a gap-blind step-event round, or goes out
tail-less with that stated on its face.

**Explained share: 0%.** Every correction is upward; they move method 1 away from the class median.
Post-calibration centre gap: ×1.81–1.82 vs repeat 1's P50, ×2.37–2.39 vs repeat 2's.
**Unexplained residual: 100% of the face-value gap, plus the calibration's own +557/+560 stacked on
top.** Not a failure of the run: the corrections were commissioned gap-blind to fill named holes in
method 1, and they did exactly that; they were never gap-closers. The gap is attributed
directionally and unquantified to **D1 + D4 + D6**, none of which any supplied rate addresses.

**Interpretive note that must travel with the centre:** A6 lives only in the class's upper quantiles
(repeat 1's own statement); G2 injects exactly that residual into method 1; comparing the post-G2
centre against the class **P50** is therefore a category error — the calibrated number contains an
upper-quantile phenomenon and lands near P85–P90 **by construction**. Its position there is
expected, and is not by itself evidence of over-correction.

**False-convergence check, three frames, no convergence declared in any:** (1) raw base vs P50 —
×1.28/×1.68, nothing to check. (2) calibrated centre inside repeat 1's P80–P90 — **false
convergence, refused on two counts**: objects of different kinds (a centre vs a quantile), and
construct overlap (G2's construct is the same phenomenon that defines those quantiles — partial loss
of independence, though not a forced fit, since `Lytin-K` never saw the class numbers); repeat 2
settles it regardless (1899 > its 1650 P90). (3) fork (a-ii): BU×0.8 = 1074/1082 against repeat 1's
1050 — agreement within 2.3–3.1%, **the most suspicious number in the exercise, flagged rather than
banked**: the 0.8 came from the RC's own blind method note (in its favour), but a round 0.8 landing
within 3% of a class median is exactly what a unit artefact looks like when it masquerades as
convergence, and repeat 2 refuses it flatly (×1.34). **The methods have not converged. That is the
correct outcome of this step, not a defect in it.**

## 7. What would change this diagnosis

Ranked; both are single questions to a single source; neither requires more estimating.

1. **The unit provenance of the pinned rate table** — net productive hours, or assigned/timesheet
   days? A ×1.25 lever on the entire base (≈±475 pd on the centre), comparable to the whole
   calibration chain and larger than any item in it; the only fact that could collapse the
   face-value gap to near zero (fork a-ii) or nearly double it (fork a-i).
2. **The class assignment weight** — stated class at 0.60–0.65, or an up-neighbour? At even the
   mildest up-neighbour factor the class P50 brackets the raw base and the gap disappears from the
   reference-class side without touching method 1. A classification adjudication, not an estimate.

Explicitly not worth pursuing for the diagnosis: the 1342/1353 branch (≤0.9%) and the three coverage
flags (they move the level, not the gap). To be pursued for the bid though it moves no diagnosis:
**the missing term** — until it exists, hosting, support and periodic upgrades remain outside every
number above, on both sides, correctly and by parity.
