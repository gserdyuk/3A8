# Run 38 — `Hotyn-N 1.0` first approximations, n=2 — raw transcripts

**2026-08-26.** The norms author for the parametric instrument, launched twice independently with
identical prompts, in parallel, gap-blind: no case, no count, no estimate, no outcome in either
task. Probe before the batch: `Lytin-F 5.0`, correct stamp.

Registered question, written before launch: *what are the published function-point counting
standard's numeric tables — the complexity threshold matrices and the component weight table —
stated from the standard alone, with per-table confidence?*

**Result: exact agreement on every numeric cell.** Both runs state IFPUG CPM 4.x / ISO/IEC 20926;
the three threshold matrices (18 boundary values) and the weight table (15 cells) are identical
between runs. Both independently flagged the same subtlety — EQ shares the EO/EQ complexity matrix
but takes the EI weight row — and both declined the value adjustment factor per the pipeline's
ruling. Neither produced any effort, hours or productivity figure. Both reported and quarantined
the harness-prepended repository-status block.

Pinned from these runs: `tools/parametric/weights.tsv`, `tools/parametric/thresholds.md`;
`docs/fp_counting_rules.md` moves to v0.2.

| file | run |
|---|---|
| `HN38-1.md` | first launch, verbatim |
| `HN38-2.md` | second launch, verbatim |

Model coordinate, recorded by the orchestrator: the session model was switched to
**`claude-fable-5`** (author's `/model` command, 2026-08-26, before the probe and both launches);
the agent definitions carry no model override, so both sensors ran on it. Probe and both runs in
one batch, one model.
