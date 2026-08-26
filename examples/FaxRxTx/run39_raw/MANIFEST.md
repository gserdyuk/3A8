# Run 39 — `Hotyn-P 1.0` on FaxRxTx, n=2 — raw transcripts

**2026-08-26.** The parametric instrument's counting half, first ever runs. Two independent
launches, identical prompts, model **`claude-fable-5`** (session model, recorded by the
orchestrator; the definition carries no override).

Registered question, written before launch: *what is the data-function inventory and the
transaction inventory of the pinned FaxRxTx obligation list — each item classified with its
complexity class justified by enumeration — and which obligations lie outside the instrument's
scope?*

## Inputs

- `requirements_pinned.md`, N = 52, md5 `473d9789f000da3cbf563c4f008fd9d5`, pasted verbatim.
- Assumption log **A1–A8**, pasted verbatim. **A9 (units) withheld by the orchestrator** — the
  sensor counts and classifies, it does not price; precedent run 37.
- The pinned component definitions and threshold matrices from `tools/parametric/thresholds.md`
  (run 38). **The weight table was not in the prompt** and never is.
- Quarantine declared in the prompt, three items: the harness `gitStatus` block; the source's own
  duration phrase ("~1–2 months of immersion") in F48/A1/A3, declared a residue so the run
  quarantines it instead of stopping; the A9 withholding stated.

Both runs reported all three quarantine items and proceeded clean. `tool_uses: 0` both.

## Result, in two lines

Both runs: **6 internal data functions + 2 external, same six identities on the internal side;
8–9 transactions over the same two fax flows and the same operational views; everything at the
enumeration floor** — the source names almost no fields, and both runs said so unprompted in
nearly the same words.

| | HP39-1 | HP39-2 |
|---|---|---|
| items classified | 16 | 17 |
| outside scope | 27 of 52 | 23 of 52 |
| under-enumerated | 14 | 16 |
| doubts | 13 | 12 |

Differences, all three named by the runs themselves as their own arguable points: HP39-2 adds a
"maintain user configuration" EI (read out of F05/F35 where HP39-1 left F35 unclassifiable);
HP39-2's submit transaction is Average where HP39-1's is Low (5 boundary DETs counted vs 4); one
EIF identity differs (HP39-1: PoP state; HP39-2: old-system interface — each run put the other's
item elsewhere legitimately).

Agreement, measured after pricing by the script (the sensors saw no weights): see
`../run39_parametric_count.md` if written, else the session record. Item-identity Jaccard
**15/18 = 0.833**; class agreement on matched items **14/15**; UFP 78 vs 82 = **×1.051**.

| file | holds |
|---|---|
| `HP39-1.md` | first launch, verbatim |
| `HP39-2.md` | second launch, verbatim |
| `HP39-1_components.tsv` | readout of run 1 for the script: id · component · complexity |
| `HP39-2_components.tsv` | readout of run 2, same form |
| `parametric_readout.txt` | `tools/parametric/parametric.py` output on both counts, verbatim |
