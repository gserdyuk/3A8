# Run 52 — the SAS outside view, `Lytin-R 1.1`, n = 2 — regression of the plugin entry point against run 46

**2026-09-14.** A regression run, not a new estimate step: the `/3a8:estimate-reference-class` entry point launched
the plugin subagent `3a8:estimator-reference-class` twice on claude-opus-5 (the harness's `opus` alias, the run 46
coordinate), `tool_uses: 0` in both. Input: run 46's conditions as its head describes them. The RFP §1–2 verbatim,
and the assumption log v1 with run-history narration, the obligation counts and the unit convention (A19) withheld,
A3 carrying the case profile's team line. Run 46's own prompt was not kept. The text was rebuilt from
`run49_raw/prompt_baseline_sas.txt` lines 23–701, which that run's manifest identifies as the sanitised form the class
sensors saw; the md5 is unchanged since run 49. Framing and whitespace differences are declared in
`run52_raw/MANIFEST.md`. **Not given:** the product model, the work model, the rate table, any total, any prior sensor
output, run 46's readings. Raw: `run52_raw/RC52-1.md`, `RC52-2.md`.

---

## 1. The readings, as declared

| | RC52-1 | RC52-2 |
|---|---|---|
| unit | staffed person-month = **≈18.7 recorded days ≈ 150 recorded hours** | FTE-month = **≈19 recorded days ≈ 152 recorded hours** |
| leave, holidays, sickness | **inside** (≈14% losses; ×0.86 to remove) | **inside** (≈11–12% losses; ÷0.885 to remove) |
| roles | every vendor role charged, incl. BA, UX, DevOps, migration, PM, tech writing; client staff, pen-test firms, bid effort outside | every vendor delivery role charged, same list; client staff, third-party audits, bid effort outside |
| own conversion to task hours | 5–6.5 h per recorded 8-h day (×0.63–0.81), not applied | **none given** |
| sources' disagreement | ±20% between absolute families after conversion; overrun sources ×2.4 apart | 10–20% on unit/role conventions; actuals vs bid-derived families 25–35% at the centre |
| scope | first release, A1's included list; W-4 and NFR-5 carried, not priced; edges named (hypercare, HA/DR build, decommissioning, rule definition) | same; edges named (hypercare, help content writing, client data cleansing, IdM wait) |
| **P10 / P50 / P80 / P90** | **130 / 240 / 360 / 470 PM** | **170 / 300 / 430 / 540 FTE-months** |
| recorded hours at P50 | ~36 000 | ~46 000 (as printed) |
| class confidence / neighbours | 55% · modernisation/data-platform programme (+ ×1.5–2.5, 20%) · mid-size LOB portal (− ×0.5–0.7, 15%) · configure-a-platform (− ×0.6–0.8, 10%) | 60% · data-platform/MDM modernisation (+ ×1.5–2, 20%) · portal refresh (− ×0.5–0.6, 15%) · PIM package + portal (− ×0.7, tail up, 5%) |
| skew | P90/P50 1.96, P50/P10 1.85 | P90/P50 1.80, P50/P10 1.76 |

Both built an eight-branch class at the RFP stage before discovery. The branches: several modules on a shared model,
an external identity provider, a public API behind API management, a separate read store, multi-legacy migration, an
enterprise NFR envelope, a multi-environment path with cutover, and requirements or business rules defined inside the
project. Both drew the same size regime (≈1 000–3 000 FP, as a class judgement) and the same relative anchors: the
cone of uncertainty, Moløkken & Jørgensen, Flyvbjerg & Budzier's 1-in-6 tail, McKinsey–Oxford, the winner's curse and
Standish with its critique. Both reach the centre by two routes, repository actuals and bids × overrun.
**They differ in how far the bid route is lifted.** RC52-1 takes a bid median of ~190 × 1.2–1.3 and finds the routes
agree within 20% at 240. RC52-2 takes bids of 230–250 × 1.3–1.5, finds the families 25–35% apart, and leans the median
toward the bid route at 300.

**Sources named.** RC52-1: ISBSG (new development, 2000s–2010s) · QSM SLIM (Putnam & Myers 2003; Almanac 2014) · Capers
Jones (2008, 2011) · practitioner consensus on bids (2015–2019) and on budgets · McConnell 2006 after Boehm ·
Moløkken-Østvold & Jørgensen 2003 · Flyvbjerg & Budzier 2011 · Bloch, Blumberg & Laartz 2012 · Standish CHAOS 2015 with
Eveleens & Verhoef 2010 · Jørgensen & Grimstad. RC52-2: practitioner consensus on bids (2015–2020) and on elapsed time ·
ISBSG (2010s) · Capers Jones · Boehm 1981 and McConnell 2006 · Moløkken & Jørgensen 2003 · Flyvbjerg & Budzier 2011 ·
Bloch, Blumberg & Laartz 2012 · Little 2006 and DeMarco · Jørgensen & Grimstad · Standish with Eveleens & Verhoef ·
Herbsleb & Mockus 2003 (the distributed-team sensitivity only).

## 2. One unit, by the declared conversion

Same rule as run 46 §2 (`docs/constants.md` §5b): recorded hours contribute ×0.75 net task hours. Leave is not deducted
again, because both readings' hours are recorded hours with losses inside. RC52-1's own band (×0.63–0.81) contains
0.75. RC52-2 declared no task-hour band, unlike RC46-2, so the house factor is applied to it without a self-declared
band to check against.

| net task hours | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|
| RC52-1 (×150 ×0.75) | 14 625 | **27 000** | 40 500 | 52 875 |
| RC52-2 (×152 ×0.75) | 19 380 | **34 200** | 49 020 | 61 560 |
| reading-to-reading ratio | ×1.33 | **×1.27** | ×1.21 | ×1.16 |

## 3. The regression: run 52 against run 46

Raw quantiles, each in its declared unit:

| reading | unit | leave | P10 | P50 | P80 | P90 |
|---|---|---|---:|---:|---:|---:|
| RC46-1 | PM = 21 d = 168 h | outside | 180 | 380 | 640 | 850 |
| RC46-2 | PM = 19 d = 152 h | inside | 125 | 215 | 330 | 440 |
| **RC52-1** | PM ≈ 18.7 d ≈ 150 h | inside | **130** | **240** | **360** | **470** |
| **RC52-2** | FTE-month ≈ 19 d ≈ 152 h | inside | **170** | **300** | **430** | **540** |

Repeat spread within each pair, per quantile (max/min, raw):

| pair | P10 | P50 | P80 | P90 |
|---|---:|---:|---:|---:|
| run 46 | ×1.44 | ×1.77 | ×1.94 | ×1.93 |
| **run 52** | **×1.31** | **×1.25** | **×1.19** | **×1.15** |

In net task hours, run 46's pair spread is ×1.59 / ×1.95 / ×2.14 / ×2.14 and run 52's is
×1.33 / ×1.27 / ×1.21 / ×1.16.

**What reproduced:**
- the engine stamp;
- `tool_uses: 0`;
- a four-field declaration ahead of any figure;
- an eight-branch structural class at the RFP stage;
- the same family of relative anchors;
- right skew, not symmetrised;
- component 4 and NFR-5 honoured as carried, not priced;
- the era named, with no adjustment made.

Both run 52 medians (240, 300 raw; 27 000 and 34 200 net) fall **inside the span of run 46's two medians** (215–380
raw; 24 510–47 880 net).

**What did not reproduce:**
- **RC46-1's level.** Neither new reading comes near 380 PM or a P90 of 850. RC46-1 staffed the class at 15–30 FTE and
  had the only tier-1-vendor staffing anchor centred at ~370. Both run 52 readings staff it at 12–22.
- **Leave.** Both run 52 readings put leave inside; run 46 split, one inside and one outside.
- **RC46-2's task-hour band.** RC52-2 gave none.
- **Ambient material.** Neither run 52 reading mentions any, where both run 46 readings reported and quarantined a
  git status.

**Reading of the regression.** Run 52's pair is ×1.25 apart at P50, close to the ×1.31 recorded for BMS run 26. Run 46's
pair was ×1.77 apart. Across all four readings on identical inputs, P50 spans 215–380 raw, ×1.77. That equals run 46's
own pair spread, because run 52 landed inside it.

With n = 2 against n = 2, the entry point's effect cannot be told apart from the sensor's known level scatter, the
×1.31–×2.12 range in `docs/sensors/reference-class.md`. The new entry point therefore shows **no regression detectable
at this n**. It produced the same instrument, with readings inside run 46's corridor. The narrower pair is one draw,
not evidence that the plugin path steadies the level.

The two pairs are not averaged, per the skill; the spread is the reading.

## 4. Beside the chain, for continuity with run 46 §3

The chain's centre (run 47) is **38 118 net task hours**. It sits at ×1.41 of RC52-1's median, between that reading's
P50 and P80 and just below P80 (40 500). It sits at ×1.11 of RC52-2's median, between that reading's P50 and P80.
Run 46 had the chain between its two medians; in run 52 the chain lies **above both medians and below both P80s**.
Interpreting that is Step B's job, and run 52 was not run to feed a diagnosis.

## 5. Protocol facts

- **Contamination checks.** Both passed their own check. Both named the log's content counts (formats, symbologies,
  entity kinds, rehearsals, environment sizes) and said they used none of them. RC52-2 also noted that the log mentions
  a "rate table" and a "bottom-up chain", with no figures.
- **Era.** Both declared their base rates era-matched to the 2018 RFP rather than to today, and applied no transfer (A19).
- **Identifiable client.** Both noticed that the client can be identified (a GS1-type organisation) and said they used
  no knowledge of its real project history.
- **Blind-spot list.** RC52-1 reproduced item 7 of the static list including the definition's instruction sentence;
  RC52-2 reproduced it without that sentence. The other six items are verbatim in both.
- **Transcription.** Both replies were transcribed verbatim from the harness's completion notifications.
- **Where the files are.** Writing into `examples/SAS/` was refused by the permission layer. All run 52 files were
  written to the session scratchpad, to be copied into place (see `run52_raw/MANIFEST.md`).

- **Copied into place** 2026-09-14 from the session scratchpad by the orchestrating session, byte for byte; nothing else in `examples/SAS/` touched.
