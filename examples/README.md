# examples/ — the cases

One folder per case the instrument has been run on. A case folder holds the pinned inputs (the
obligation list, the split, the assumption log, the technology declaration), one raw folder per run
(`run<N>_raw/`, prompts and sensor replies verbatim), one record per run (`run<N>_*.md`), the built
reports (`reports/`) and, where the case was taken to a deliverable, the estimate document
(`estimate_<case>_<date>.md`). Run numbers are global across cases: a run belongs to the case it was
made on, and the sequence never restarts.

To add a case, follow `docs/case_profile.md` (the profile is pinned before any number exists) and
Step 0 of `skills/estimate-product/SKILL.md`.

## Published here

| case | source document | outcome | what is there |
|---|---|---|---|
| `BMS/` | a training RFP of 2016 — a booking management system for a company's own travel; the issuer is anonymised as "the issuer", and the document itself is not included, only the obligation list derived from it | none | case 1: the Lytin generation's runs (1–15), the first Hotyn chain (16–28), the outside view and the parametric reading (36, 40), the estimate of 2026-08-22 and its reports |
| `FaxRxTx/` | the author's own requirements document for a real service (`REQUIREMENTS.md`, `SYSTEM.md`) | **known** — `FACT.md`, opened only after each estimate is fixed | case 2, the one case scored against an outcome: the Lytin runs (1–5), the Hotyn chain (29–35), the parametric reading (39), the no-method baseline (41–43), the assembly (run 31) and the fact comparisons (runs 4, 32) |

## Not published — `examples/ignored/`

`examples/ignored/` is in `.gitignore` and exists on the author's machine only. Whatever lives there
is not in the repository, so the question "is this example published or not" is answered by this
list alone.

| folder | what it is |
|---|---|
| `ignored/SAS/` | case 3, the fullest case on record: runs 44–60, the estimates of 2026-09-08 (the 1.1 chain) and 2026-09-16 (the first through the plugin), the reports with the density chart, every prompt and raw reply of the plugin regression (runs 52–60). Its source document is a third party's and is not ours to publish |
| `ignored/syn/` | a 2026 RFP and a group's consensus figure that is not an outcome; see `BACKLOG.md`, "examples/syn — what is actually in it" |
| `ignored/BMS_source/` | the BMS source document and its extraction, not ours to publish |

Historical records elsewhere in the repository — session notes, findings, proposals — cite SAS files by
the path they had at the time, `examples/SAS/…`; read it as `examples/ignored/SAS/…`. Living documents
say `examples/ignored/SAS` outright.
