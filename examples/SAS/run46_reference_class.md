# Run 46 — the SAS outside view, `Lytin-R 1.1`, n = 2

**2026-09-08.** Case 3, step 5, run in parallel with and in ignorance of the chain. Two identical
launches of `estimator-reference-class` on Claude Opus 5 (the harness's `opus` alias), `tool_uses: 0`
in both, both quarantining the git status. Input: the RFP §1–2 verbatim (the proposal-guideline,
response-structure and evaluation sections dropped as commercial boilerplate) and the assumption log
v1 with run-history narration, the obligation counts and the unit convention (A19) withheld — the
sensor is required to declare its own unit, and RC36 showed that handing it ours is worse than
handing it none. **Not given:** the product model, the work model, the rate table, any total, any
prior sensor output. The RC prompt carried the case profile's team line (middle/senior, one site,
first domain) as A3. Raw: `run46_raw/RC46-1.md`, `RC46-2.md`.

This is the first `Lytin-R 1.1` pair on record: both readings open with the four-field declaration
the `.1` engines require, and the two declarations differ — which is the point of requiring them.

---

## 1. The readings, as declared

| | RC46-1 | RC46-2 |
|---|---|---|
| unit | person-month of a full-time assigned member = **21 recorded days = 168 recorded hours** | staffed person-month = **19 attended days = 152 charged hours** |
| leave, holidays, sickness | **outside** the effort figures (inside calendar) | **inside** the PM (21.7 nominal days less 2.7 absence = 19 attended) |
| roles | every vendor role charged, incl. PM, BA, UX, DevOps, migration, tech writing | every charged role, same list |
| own conversion to task hours | ×0.65–0.75 | ×0.70–0.80 |
| sources' disagreement | 30–40% at the point of contact, converted, ±15% residual | 22–35% between repository and vendor-bid families, +25% uplift applied |
| scope | first release, A1's included list; component 4 excluded; edges named | same; edges named |
| **P10 / P50 / P80 / P90** | **180 / 380 / 640 / 850 PM** | **125 / 215 / 330 / 440 PM** |
| recorded hours at P50 | ~64 000 | ~32 700 |
| class confidence / neighbours | 60% · programme (+, 20%) · mid-size product (−, 15%) · COTS (−, 5%) | 60% · data-intensive (+, 15%) · CRUD suite (−, 20%) · programme (+, 5%) |
| skew | P90/P50 2.24, P50/P10 2.11 | P90/P50 2.05, P50/P10 1.72 |

Both built the same eight-branch class (multi-module transactional application with a cross-cutting
sharing model, bulk interchange, a read store, migration from several incumbents, an unchosen identity
integration, a contractual NFR envelope, a fixed pre-discovery requirement set) and both excluded the
same neighbours. Both used the same relative anchors (cone of uncertainty, Jørgensen's overrun surveys,
Flyvbjerg's 1-in-6 tail, the winner's curse). **Their absolute anchors are where they differ**: RC46-1
staffs the class at 15–30 FTE over 14–24 months from practitioner patterns for a tier-1 vendor and
adds back a requirements phase to COCOMO; RC46-2 sizes 1 200–3 000 functional units against ISBSG
delivery rates and staffs at 12–20 FTE over 10–16 months. Same shape, different level — the reading
`docs/constants.md` §5g already records for BMS, on a third case.

## 2. One unit, by the declared conversion

Per `docs/constants.md` §5b: recorded or charged hours contribute **6 net task hours per 8**, i.e.
×0.75; leave is not deducted again because both sensors' hours are already attended/charged hours.
Both declarations put their own conversion in a band containing 0.75 (RC46-1: 0.65–0.75, RC46-2:
0.70–0.80), so the house factor is inside what each sensor said of itself.

| net task hours | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|
| RC46-1 (×168 ×0.75) | 22 680 | **47 880** | 80 640 | 107 100 |
| RC46-2 (×152 ×0.75) | 14 250 | **24 510** | 37 620 | 50 160 |
| class-to-class ratio | ×1.59 | **×1.95** | ×2.14 | ×2.14 |

**The class disagrees with itself by ×1.95 at the median** — BMS run 26 gave ×1.31 on a pair and
×2.12 across three readings. The unit conversion did not create it: the raw medians are ×1.77 apart
before any factor. This is the reference-class sensor's known property (`docs/status_2026-08-27.md`
§4d, `constants.md` §5g), reproduced.

## 3. Placed beside the chain, for the diagnosis to interpret

The chain's centre (run 47) is **38 118 net task hours**. In the class readings' own terms it sits at
**×0.80 of RC46-1's median (about P35 of that reading)** and **×1.56 of RC46-2's (about P80 of that
reading)**. For the first time in the project the bottom-up lands *between* two class medians rather
than above both (BMS) or below the one reading (FaxRxTx). Whether that is the chain, the class, or the
case is Step B's question, not this record's; the numbers are stated here in one unit so that Step B
has no conversion left to do.

## 4. Protocol facts

- Both sensors quarantined the ambient git status and named the numeric commit subject in it without
  using it (RC46-1: "one of which contained a numeric result from another run").
- Both declared the era mismatch (2018 RFP, 2013–2022 base rates) as blind spot 5's concrete face and
  refused to adjust for it.
- Both named the carried post-production period as a boundary risk for whoever joins their figure to
  a rate-per-time instrument — the seam the diagnosis must keep visible.
- Both transcripts were re-typed from the delivered reply; the harness transcript files were empty.
