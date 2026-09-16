# Run 64 — the demanded-work addendum, `Hotyn-K 1.1` × Claude Opus 5, one reading (FaxRxTx, 2026-09-16)

The instrument `technology_declaration.md` §3 names for the four branches the crossing left standing: a gap-blind
rate author given the activity as worded, the sizing rule and the team-grade line. Prompt `prompt_K.md`
(`4e77ebdc…`), hand-written, no figure; it also carried the case profile's staffing rule (headcount of these stages
undeclared → a row that scales with headcount or a period must refuse). Reading HK64-1: engine `Hotyn-K 1.1`,
end_turn, 6 106 output tokens, no tool use. Raw reply: `run64_raw/HK64-1.md`.

## Rows

| row | kind (as declared by the sensor) | O / M / P, net task hours | E |
|---|---|---|---:|
| W-F48 domain immersion and technology selection | scales with headcount and period | **refused** — headcount and stage length undeclared; asks for an output-bounded restatement | — |
| W-F49 integration tests on the real message stream | bounded (one pass) | 24 / 56 / 128 | **62.7** |
| W-F50 comparison with the old system until outputs agree | scales with the parallel-run period; honest M > 10 pd | **refused** — asks for a catalogue split (comparator · per discrepancy class · per week of monitoring) | — |
| W-F52 establishing the old version can be decommissioned | bounded | 16 / 32 / 80 | **37.3** |

Declaration: net task hours (sources natively engineer-days × 8); losses outside; delivery-team hours; **the day
convention of its sources is loose — if they meant assigned days, the rows are overstated ×1.23–1.45** (declared,
not adjusted).

## The chain with the addendum (`price_addendum_64.py` → `addendum_summary.json`)

Once-scoped layer, no C3; sd of the layer 24.5 h at ρ = 0.5, added to the assembly's sd linearly.

| | repeat 1 | repeat 2 |
|---|---:|---:|
| assembly (run 63) | 10 094 | 9 747 |
| + addendum | 100 | 100 |
| **raw chain total, net task hours** | **10 194** | **9 846** |
| sd · P10 · P90 (ρ = 0.5) | 1 672 · 8 050 · 12 337 | 1 625 · 7 764 · 11 929 |

**Raw chain: 10 020 net task hours, repeat band 9 846–10 194 (×1.035), sd ≈ 1 649.**

## Findings

- **W-F48 and W-F50 are carried, not priced** — the profile left their parameters unknown, and the rate author
  refused exactly as the profile's rule requires. Step C (run 66) prices them as phase shares (T3, T4) instead.
- W-F49 prices one pass, not a soak window (F-3); whether C3 should apply to once rows is left to the method (F-4).
- `docs/rate_table.md` was not amended; if the author adopts these rows, they become addendum A2 there.
