# Run 17 — raw record and manifest

Preserved per the format adopted in `run17_axis_projection.md` §8: keep the sample, not only the
statistics. The analysis lives in `../run17_axis_projection.md`; this directory holds what it was
derived from.

## Coordinates

An estimate is a property of (project × engine × model × axis). All runs below:

- **Project:** Booking Management System, RFP digest June 2016 (`BMS_extracted.md`, `assumptions.md`)
- **Engine:** `Lytin-D 5.0` — sensor definition `.claude/agents/estimator-decomposition.md`
- **Probe:** `Lytin-F 5.0` confirmed on Opus 5, Sonnet 5 and Haiku 4.5 before their batches

| batch | prompt file | md5 (LF form) | model | n | date |
|---|---|---|---|---:|---|
| axis S, first | `prompt_decomposition_BMS_axisS.txt` | `196524bee339e2da35a293652ca9b00f` | Opus 5 / Sonnet 5 | 5 + 5 | 2026-08-18 |
| axis P | `prompt_decomposition_BMS_axisP.txt` | `5de455cf8c165be500dc17bf2a09dac3` | Opus 5 / Sonnet 5 | 5 + 5 | 2026-08-19 |
| axis P, third tier | `prompt_decomposition_BMS_axisP.txt` | `5de455cf8c165be500dc17bf2a09dac3` | Haiku 4.5 | 5 | 2026-08-19 |
| axis S, rerun for structure | `prompt_decomposition_BMS_axisS.txt` | `196524bee339e2da35a293652ca9b00f` | Opus 5 / Sonnet 5 | 5 + 5 | 2026-08-19 |

Each axis prompt is the pinned base (`prompt_decomposition_BMS.txt`, md5
`c33affd709792dfe60531daa3cb42d65`) plus one declaration line and nothing else. All three md5s were
verified at launch. Orchestrator on Opus throughout, model set per agent call. Every run isolated:
the sensor sees the prompt and nothing else, enforced by tool restriction (`tools: Glob`).

## Contents

| file | what it is |
|---|---|
| `axisP_readings.tsv` | instrument readings, 10 axis-P runs |
| `axisP_trees_opus.md` | leaf inventory + placement reports, PO-1…PO-5 |
| `axisP_trees_sonnet.md` | leaf inventory + placement reports, PS-1…PS-5 |
| `axisS_rerun_readings.tsv` | instrument readings, 10 axis-S rerun runs |
| `axisS_rerun_trees_RO4.md` | leaf inventory, RO-4 (written first, kept separate) |
| `axisS_rerun_trees_opus.md` | leaf inventory, RO-1, RO-2, RO-3, RO-5 |
| `axisS_rerun_trees_sonnet.md` | leaf inventory + structural defects, RS-1…RS-5 |
| `haiku_readings.tsv` | instrument readings, 5 Haiku runs, with per-run protocol verdict |
| `haiku_protocol_violations.md` | what each broken Haiku run broke, run by run |
| `prereg_overlap_metric.md` | overlap measurement procedure, pinned before any overlap was computed |
| `prereg_haiku_third_point.md` | Haiku predictions, pinned before results, including a correction of an over-claim |

## Known gaps in this record

- **The ten axis-S runs of 2026-08-18 (SO-1…5, SS-1…5) have no leaf inventory.** Their trees were not
  preserved and are unrecoverable. This is the loss that forced the rerun, and the reason this
  directory exists. Only their instrument readings survive, in `../run17_axis_projection.md` §1.
- These inventories are transcriptions of the sensors' output, not byte-for-byte captures: leaf
  names, module structure, branch structure, placement answers and C6 summaries were carried over;
  per-leaf O/M/P columns were not, except where already summarised in the readings tables.
  The harness does not persist subagent output — the per-task `.output` files were empty — so
  transcription was the only path available.
