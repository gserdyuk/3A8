# Run 47 — SAS size classes, `Hotyn-D 2.0`, n = 2, and the whole-model assembly

**2026-09-08.** Case 3, steps 3 and 4. The work model of run 45 (245 elements, 1 650 items) sized by
`Hotyn-D 2.0` in the same seven batches as the crossing, **two independent repeats per batch** — fourteen
launches, all on Claude Opus 5 (the harness's `opus` alias), all `tool_uses: 0`, all quarantining the git
status. Prompts: `run47_raw/make_sizing_prompts.py` — for every sized element its class, parent, covered
obligations **with their texts**, and the activities crossed onto it; plus catalogue 1.4 §3a verbatim.
Raw: `run47_raw/HD47-A1.md` … `HD47-G2.md` (headers say which were taken from the harness transcript and
which were transcribed from the delivered reply). Assembly: `run47_raw/assemble_sas.py`, which reads the
rate table from `docs/rate_table.md` directly.

```bash
python examples/SAS/run47_raw/assemble_sas.py
```

---

## 1. Sizing readings

| reading | repeat 1 | repeat 2 |
|---|---:|---:|
| elements received (sizeable) | 187 | 187 |
| sized | 183 | 184 |
| **S / M / L / XL** | **52 / 105 / 23 / 3** | **55 / 101 / 25 / 3** |
| unsizeable — model defect (M10) | 4: C-016, A-065, C-020, A-013 | 3: C-005, C-016, C-020 |
| statement kinds (compliance / behavioural), 24 statements | 13 / 10 (+1 unsizeable) | 13 / 10 (+1 unsizeable) |
| special counts, A9 | A-145: S | A-145: S |
| special counts, G2m–G4m (22 stores) | 18 classed, 4 unsizeable (C-011, C-001, A-043, A-159) | 21 classed, 1 unsizeable (C-011) |
| doubts (sum over batches) | 126 | 143 |
| closure violations (sum over batches) | 33 | 28 |
| XL elements (M10 coarseness findings) | A-036, A-049, A-062 | A-036, A-049, A-062 |

**Class agreement between the repeats: 159 of 187 elements — 85.0%** (FaxRxTx run 31: 87.3%). The 28
differences are all one step (S↔M or M↔L) except A-017 (S vs L, "four roles: one kind or four") and the
two elements one repeat refused and the other sized (A-065, A-013, C-005). Statement kinds agree on all
23 assigned. The three XL elements are the same in both repeats and were the crossing's own granularity
findings (run 45 §3.5): the notification engine A-036, the record import service A-049, the
basic-and-full profiles A-062.

**Where the sizing disagrees with itself** is, batch after batch, one question: *are the GIN and LN
twins one object or two?* Both B repeats declared the reading up front (one action over a
parameterised record kind) and said the other reading would double most counts; G's two repeats split
on exactly that for A-049 (8 vs 7 actions, both XL). The assumption projection pinned the *structure*
(P3, shared core plus per-kind residue) but not the *enumeration*, and the sensors said so. A
precedent for the catalogue, not a repair here.

**Holes.** Priced items: repeat 1 skips 31 items on the 4 unsizeable elements and the 4 unsizeable
migration counts; repeat 2 skips 14. Named, never guessed, in the assembly output.

---

## 2. The assembly

Conventions identical to BMS run 25 and FaxRxTx run 31: rooted subtrees, C3 at 20% of leaf-item effort at
every parent including the root, once-scoped and per-environment items outside every C3 base,
E = (O + 4M + P) / 6, the rate table v0.1-h in **net person-hours**. Position-derived classes computed by
the script: 58 parents plus the root; model bracket **L** (246 elements); E3 **L** (4 environments); E1
dev S · test M (declared) · stage M · prod L; G5m twice; S2/S3 **XL** (45 surfaces and interfaces).

| layer | repeat 1 | repeat 2 |
|---|---:|---:|
| element items, incl. the root's per-parent items | 24 163 | 24 221 |
| C3, all 59 parents | 13 065 | 13 106 |
| of which the root alone | 4 833 | 4 844 |
| once + per-environment (23 items) | 840 | 840 |
| **total, net person-hours** | **38 069** | **38 168** |
| in table person-days (8 h) | 4 759 | 4 771 |

**Repeat spread ×1.0026 · centre 38 118 net task hours.** The chain's own corridor, from the O/M/P
of every priced item summed at ρ = 0.5 (`docs/constants.md` §5e, the declared convention): sd ≈ 6 330 h,
**P10 ≈ 30 000 · P90 ≈ 46 200 net task hours (×0.79 / ×1.21 of the centre)** — the same ×1.5 P10–P90
width the earlier cases showed, because the rate table's cells set it, not the case. C3 is 34.3% of the total (BMS 27.7%, FaxRxTx
27.4%); delivered against leaf effort it is 54% — the tree is one level deeper than the earlier cases
(mean depth 2.6 against ~2.0), which is `docs/constants.md` §3's structural factor showing itself.

**In the comparison-layer convention** (`docs/constants.md` §4a: 6 net task hours per present day,
×1.10 leave, 21 days): **38 118 h ≈ 333 staffed person-months**. Stated here once, for the report; no
sensor saw the conversion.

For scale, and nothing more: FaxRxTx priced at 11 386 h, BMS at 10 737 h. SAS is ×3.35 FaxRxTx in the
chain's own terms, from a product list ×3.1 its length and a work model ×2.9 its size — the three
cases scale together, which is the least a bottom-up instrument owes.

---

## 3. What the two repeats show about step 3

The class-agreement number (85%) matches FaxRxTx's (87%) and the total-level agreement is tighter
(×1.003 against ×1.032), because with 187 elements the one-step disagreements cancel. This is the
second case on which **the sizing step's own spread is an order of magnitude below what the reference
class produces on the same input** (run 46: ×1.77 on P50 before any unit conversion). Nothing new
about the instrument; the same reading on a third case.

Two things the repeats did not agree on and the assembly could not settle:

- **Whether a store with no predecessor origin has a migration count at all.** E1 answered "none —
  the pinned driver names loading *from the predecessor*; these stores are written at run time" and
  assigned no class (a driver-level M10 finding); E2 answered "one kind each, the system is unusable
  without it". The rate table's G-migration rows have no zero rung, so E1's reading prices those three
  stores at nothing and E2's at S. The difference is 9 items in the hole list, not in the total
  materially, but it is a catalogue ambiguity the prompt inherited from §3a's two framings of the
  driver ("needing pre-load" against "loaded from the predecessor"). Recorded for the catalogue.
- **A-017, the role catalogue: one entity kind or four** — S against L, the widest single swing, and
  both repeats named it as the arguable item.

---

## 4. Carried forward

`assemble_sas.py` output, both repeats, is the chain's reading for the diagnosis: **38 118 net task
hours, repeat band 38 069 – 38 168**, 23 once-scoped items, 31 and 14 named holes. The demanded branch
is empty (all seven items absorbed or carried per run 45); the carried-not-priced list of
`assumptions.md` A1 (post-production support term, NFR-5 impact analysis at count 0) stands beside the
number, as A0 requires.
