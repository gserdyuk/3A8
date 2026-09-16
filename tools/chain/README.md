# tools/chain — the deterministic parts of the bottom-up chain

Four scripts and a shared reader. They generate the sensors' prompts from pinned inputs, consolidate the
sensors' replies, and do the one piece of arithmetic in the chain. None of them judges anything; every
figure they print traces to a sensor's reply, the pinned model, the declaration or the rate table. The
orchestrator (the skill `/3a8:estimate-product`) launches the sensors; these scripts sit between the launches.

| step | script | reads | writes |
|---|---|---|---|
| 2, prompts | `make_crossing_prompts.py <case> --model <HM file> --run N` | `chain_config.json`, the model's §6 TSV, `docs/technology_catalogue.md`, `requirements_work.md`, `technology_declaration.md` §W6 | `run<N>_raw/prompt_<batch>.md`, `batches.json` |
| 2, consolidation | `consolidate_crossing.py <case> --run N` | `run<N>_raw/batches.json`, `HW<N>-<batch>1.md` | `classes.tsv`, `work_model.tsv`, `crossing_summary.json` |
| 3, prompts | `make_sizing_prompts.py <case> --crossing-run N --run K` | the consolidation, the model, `requirements_*.md`, `fragments/sizing_rules.md` | `run<K>_raw/prompt_size_<batch>.md`, `sizing_batches.json` |
| 4, arithmetic | `assemble.py <case> --crossing-run N --sizing-run K` | the consolidation, `HD<K>-<batch><repeat>.md`, `chain_config.json`, the catalogue, `docs/rate_table.md` | `run<K>_raw/assembly_summary.json`; the assembly on stdout (redirect to `assembly_output.txt`) |

All paths are relative to the repository root; run them with `PYTHONUTF8=1 py …` on Windows.

## `examples/<case>/chain_config.json` — written at Step 0, with the technology declaration

```json
{
  "case_label": "FaxRxTx, declared 2026-08-22",
  "declared": ["K-BESPOKE", "A-TB", "C-DIRECT", "D-TEAM", "E-DSP", "G-SEED", "U-OPS-USER", "SA-NONE"],
  "parameters": {"environments": ["dev", "stage", "prod"], "test_cycles": 2, "uat_cycles": 0, "migration_rehearsal_cycles": 0},
  "batches": null
}
```

- `declared` — one catalogue code per dimension, exactly the §1 table of `technology_declaration.md`. The
  crossing prompt's INPUT 2 is built from the catalogue's activity tables for these codes — tables only, no
  prose, so that no pricing vocabulary reaches the sensor.
- `parameters` — the declaration's §2: environment names (sized dev = S, test/stage = M, prod = L at
  assembly), cycle counts. A parameter that is not declared is 0 and produces no items.
- `batches` — `null` groups the root's children in model order into batches of at most 36 elements (the
  size runs 45 and 58 used); or fix them: `{"A": ["N02"], "B": ["N06", "N07", "N10"], …}`.

## What the assembly computes, and from where

Rooted subtrees; C3 = 20% of the leaf-item effort at every parent including the root; E = (O + 4M + P) / 6;
position-derived classes by catalogue §3a (per parent by leaves in the subtree, A8 by stores and interfaces,
U1–U3 and O1 by surfaces, D4 by covered ids; once items by the model bracket, E3/E7 by the environment
count, S2/S3 by surfaces plus interfaces, O4 and U1d single; E1 per environment); the root's per-parent items
added here because the root is outside every batch; unsizeable elements and unassigned special counts listed
as named holes and priced at nothing; the corridor at the declared ρ = 0.5. Demanded-work branches the
crossing left standing have no table row and are carried, not priced; a gap-blind rate addendum is the
instrument for them (`docs/rate_table.md` A1 is the precedent).

## Regression

On the SAS case (outside the public tree) the four scripts reproduce run 58's consolidation (1 396 items, 0
row mismatches) and run 59's assembly (34 933 / 31 954 net task hours, 42 / 47 holes, 13 / 3 XL, class
agreement 77.3%) from the pinned model and the raw replies, 2026-09-16.
