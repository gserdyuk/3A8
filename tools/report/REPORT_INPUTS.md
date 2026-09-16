# The report's two input files — what the orchestrator writes at the end of a run

`tools/report/make_report_data.py examples/<case>` turns these two files, plus the case's pinned files, into
`report_data.json`; `tools/report/build_report.py examples/<case>/report_data.json` turns that into the HTML
report. The orchestrator writes the two files as the last step of `/3a8:estimate`; nothing in them may be a
number that is not in a sensor's output, the assembly's output or the diagnosis.

## `report_numbers.json` — every figure, in net task hours, with its source run

```json
{
  "hours_per_pd": 8,
  "dates_line": "chain assembled <b>15–16 Sep</b> · outside view read <b>8 Sep</b> · diagnosed <b>16 Sep</b>",
  "counts": {"elements": 211, "leaves": 187, "items": 1396, "class_agreement_pct": 77, "repeat_spread": 1.093},
  "chain": {"raw_centre_h": 33444, "raw_lo_h": 31954, "raw_hi_h": 34933, "sd_rho05_h": 5288, "source": "run 59 assembly"},
  "calibration": {"centre_lo_h": 48483, "centre_hi_h": 52608, "corridor_lo_h": 39837, "corridor_hi_h": 72031,
                  "factor_central": 1.51, "source": "run 60 RG60 §6"},
  "outside": [
    {"id": "RC46-1", "dash": "", "unit_note": "380 person-months at 168 recorded h",
     "quantiles_h": {"0.1": 22680, "0.5": 47880, "0.8": 80640, "0.9": 107100}, "source": "run 46"},
    {"id": "RC46-2", "dash": "6 4", "unit_note": "215 person-months at 152 charged h",
     "quantiles_h": {"0.1": 14250, "0.5": 24510, "0.8": 37620, "0.9": 50160}, "source": "run 46"}
  ],
  "nomethod_curves_file": "run49_raw/curves_pd.json",
  "parametric": null,
  "fact": null,
  "bottom_up_alt": null,
  "raw_marks": null,
  "engines": {"model": "Claude Opus 5",
              "chain": "Hotyn-M 2.1 / Hotyn-W 1.2 / Hotyn-D 2.0 × rate table v0.1-h",
              "outside": "Lytin-R 1.1 ×2", "rates": "Lytin-K 1.1", "diagnosis": "Lytin-G 1.1"},
  "provenance": [
    {"idx": "1", "title": "Product model · n = 2 · Hotyn-M 2.1", "text": "146 obligations → 211 elements …"},
    {"idx": "2", "title": "Work model · Hotyn-W 1.2", "text": "…"}
  ]
}
```

- `calibration` is `null` when Steps C, B, D did not run: the chart then draws the raw chain as the bell, unlabelled
  "calibrated", and no calibration spread.
- `outside[].quantiles_h` are **in net task hours after the conversion the diagnosis applied**; `unit_note` says what
  the sensor declared. A reading that gave a lognormal fit instead of quantiles supplies `"lognormal": {"median_h",
  "sigma"}`; `"tail_drawn": true` draws the quantiles beyond P90; `"beyond_label"` labels an off-scale quantile.
- `fact`, only when the case has an outcome and it has been opened: `{"value_h", "label", "legend", "note"}`.
- `bottom_up_alt`, only for a second reading of the same instrument on the same case (another engine version or
  repeat): `[{"id", "centre_h", "sd_h", "dash"}]`. Never for another method.
- `raw_marks`: extra ticks on the axis, `[{"value_h", "label", "lo_h", "hi_h"}]`.
- `parametric`: `[{"id", "median_h" | "median_pd", "sigma", "dash"}]` for the function-point instrument; leave it `null` where the instrument prices the functional shell only and says nothing about the case (the author dropped it from the FaxRxTx report, 2026-09-16).
- `nomethod_curves_file`: a JSON list `[{id, median, sigma}]` or a dict `{id: {median, sigma}}`, medians in person-days of the report unit, one entry per bare run; both forms the project has produced are read.
- `axis_max_pd` overrides the computed axis end.

## `report_text.json` — the prose, written by the orchestrator from the run records

```json
{
  "subject": "Case <name> · <what the system is> · <stage> · <b>outcome known / no outcome</b>",
  "standfirst": "Two or three sentences: what was estimated, by which chain, what the reader is looking at.",
  "hint": "The paragraph under the chart. Say what each curve's width is (docs/sensors/README.md, the table of widths), never let a curve claim more than its sensor declared.",
  "chain_legend_note": "optional, appended to the bottom-up legend line",
  "centre_note": "optional tile text; the default states hours, the raw sum and the factor",
  "calibration_note": "optional", "repeat_note": "optional", "nomethod_note": "optional", "outside_note": "optional",
  "reserve_value": "Unresolved", "reserve_note": "the raw class tail, both readings, and where the centre sits against them",
  "extra_tiles": [],
  "divergence": {"count": "×0.65 – ×1.50", "lead": "one sentence",
                 "rows": [{"idx": "units first", "title": "…", "chip": "50–77%", "chip_cls": "blue", "text": "…"}],
                 "stepc_bullets": ["<b>G1 ×1.18</b> — …"], "false_convergence": "…",
                 "src": "examples/<case>/run<N>_steps_BD.md"},
  "outcome": {"count": "×1.17 · ~P85", "lead": "…", "rows": [], "extra": "", "src": ""},
  "findings": {"rows": [{"idx": "I-7", "title": "…", "chip": "…", "chip_cls": "red", "text": "…"}], "src": ""},
  "gaps": {"rows": [{"idx": "1", "title": "…", "chip": "awaiting a parameter", "chip_cls": "caution", "text": "…"}], "src": ""},
  "provenance_extra": "optional HTML appended to the provenance section",
  "footer_fine": ["optional", "two paragraphs"],
  "tiles": null,
  "meta": null
}
```

- Rows are HTML strings; entities (`&mdash;`, `&times;`) as in the existing reports. Keep `chip` to a few words.
- `outcome` only when `fact` exists in the numbers file.
- Anything left `null` or absent gets the generic default from `make_report_data.py`.

## The generated parts (no input needed)

- **Obligations** from `requirements_product.md` and `requirements_work.md` — the first table whose header starts
  with `id`; columns id | obligation | source.
- **Variant readings** from `open_questions.md`, if present — a table id | ids | question | reading taken (or
  id | question | reading).
- **Defaults** from `assumptions.md` — one row per `## A<n>. <title>` section, its first paragraph.
- **How to read the chart** and **Methodology** from `tools/report/fragments/`.
