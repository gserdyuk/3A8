# Run 61 — the product model, `Hotyn-M 2.1` × Claude Opus 5, n = 2 (FaxRxTx, end-to-end estimate of 2026-09-16)

First step of a fresh end-to-end estimate of FaxRxTx through `/3a8:estimate`. Nothing from runs 1–43 or any earlier
report was read or used. `FACT.md` stays sealed until the estimate document is written. Raw replies, prompts and
the per-turn ledger: `run61_raw/` (`MANIFEST.md`).

## Step 0, as this run found it

- Pinned inputs used as they are: `requirements_pinned.md` (N = 52, md5 CR-stripped `473d9789…`, matches the
  declaration's pin), its split into `requirements_product.md` (N = 47) and `requirements_work.md` (N = 5),
  `assumptions.md`, `assumptions_product.md`, `technology_declaration.md`, `chain_config.json`. `REQUIREMENTS.md` is a
  draft of a different task and is not a source (`requirements_pinned.md`, exclusion rule 4).
  `requirements_product.md` hashes CR-stripped to `abaa0717…`, not to the declaration's `306046dc…`; the declaration's
  pin note says its md5s are the pre-rename values and `requirements.pin.txt` holds the post-rename ones — recorded,
  not investigated further.
- **`case_profile.md` written first**, before any sensor ran, from `SYSTEM.md` and `assumptions.md`
  (form `docs/case_profile.md` v1.0). Not committed (no state-changing git command in this session); its md5, printed by
  `make_prompts_61_65.py` before the first sensor launch, is `30d83b0977934aefbced23e3aa60d38f`.
- Struck from the product-model input: nothing in the pinned lists; one duration figure quoted inside
  `assumptions_product.md`'s "Removed here" paragraph, after both first launches stopped on it (below).

## Launches

| reading | prompt | outcome |
|---|---|---|
| HM61-x1, HM61-x2 | `prompt_M.md` (`b7eb5e73…`) | **both stopped at §1 for contamination** — the pinned projection quotes "the ~1–2 month figure attached to the immersion stage" while saying it was removed. Correct refusals; not readings |
| **HM61-1, HM61-2** | `prompt_M2.md` (`84906781…`) — the same text with that figure struck in place | both clean, Order A, complete §1–§9, `end_turn`, 20 412 / 23 537 output tokens, no continuation |

Engine stamp as printed: `Hotyn-M 2.1` (all four). Model as launched: `opus` → `claude-opus-5` in every turn.

## Readings

| | HM61-1 | HM61-2 |
|---|---:|---:|
| elements after closure | 84 | 91 |
| leaves (accreted / derived) | 68 (56 / 12) | 75 (62 / 13) |
| parents · root children | 16 · 11 | 16 · 11 |
| mean leaf depth | 2.49 | 2.29 |
| derived share of leaves | 17.6% | 17.3% |
| accretion verdicts, pass 1 (covered / partial / not / deferred) | 7 / 10 / 30 / 0 | 8 / 19 / 19 / 1 |
| passes (accretion · completion) | 2 · 3 | 2 · 3 |
| closure: deleted childless · lifted | 0 · 1 | 0 · 0 |
| ambiguity flags | 8 | 10 |
| requirements whole at closure | **47 / 47** | **46 / 47** — F19 residue reported as a defect (the 1–3 unnamed formats) |

Between the repeats (`compare_models.py`): leaves ×1.103, elements ×1.083; distinct accreted coverage sets 44 / 48,
31 shared, **Jaccard 0.508**; as multisets 42 of 76, **Jaccard 0.553**. The skeletons agree on the subsystem cut
(inbound, outbound, orchestration, cluster, storage, NOC, portal, old-system, system-wide properties) and differ in
where the workers and the external exchanges sit and in how finely F05, F35 and F46 are split.

## Closure — the orchestrator's decision

**`HM61-1` is the model the chain continues on**: the only repeat that closed with every requirement whole and no
defect report. `HM61-2`'s F19 treatment (a registration leaf plus a standing residue) and `HM61-1`'s (a placeholder
leaf for the unnamed formats) are the same fact read two ways; the sizing sensors later found the placeholder
unsizeable (run 63), which is where the defect resurfaces on the chosen model.

## Findings

1. **A pinned projection contaminated its own consumer.** `assumptions_product.md` names the figure it says it
   removed. Both sensors refused, as designed. The pinned file needs a new version without the figure; this run did
   not edit it (no existing file may be modified) and struck it in the prompt instead.
2. **Structure spread ×1.10 on leaves** — inside the ×1.02–×1.56 band `docs/instrument.md` §3 records for this step,
   and it is the step's own freedom (Jaccard ~0.5), not carried into any number of this estimate (only `HM61-1` was
   crossed and sized). The diagnosis lists it as unpriced step-1 variance.
