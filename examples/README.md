# examples/ — the cases

One folder per case the instrument has been run on. Each case folder holds the pinned inputs (the
obligation list, the split, the assumption log, the technology declaration), one raw folder per run
(`run<N>_raw/`, prompts and sensor replies verbatim), one record per run (`run<N>_*.md`), the estimate
document (`estimate_<case>_<date>.md`) and the built reports (`reports/`).

## Published here

| case | source document | outcome | note |
|---|---|---|---|
| `BMS/` | a training RFP (`BMS_updated.docx`) | none | case 1; the estimate of 2026-08-22 |
| `FaxRxTx/` | an internal system's requirements (`REQUIREMENTS.md`, `SYSTEM.md`) | **known** (`FACT.md`, opened only after each estimate) | case 2; the exit criterion's only scored case |

## Kept outside the public repository — `examples/ignored/`

`examples/ignored/` is in `.gitignore`. It exists on the author's machine only, and nothing under it
is ever committed, so that "is this example in the repository or not" never has to be guessed: if a
case is listed here, it is not.

| case | why | what is there |
|---|---|---|
| `ignored/SAS/` | the source is an EPAM RFP response document (2018) marked confidential; the client is anonymised, the document is not ours to publish | case 3, the fullest case on record: runs 44–60, the estimates of 2026-09-08 (v1, the 1.1 chain) and 2026-09-16 (v2, through the plugin), the reports with the density chart, every prompt and raw reply of the plugin regression (runs 52–60) |
| `ignored/syn/` | a client RFP (2026) and a Delphi figure that is not an outcome; see `BACKLOG.md`, "examples/syn — what is actually in it" | the RFP, the extracted text, `fact.md` (a group consensus, deliberately misnamed, see `docs/case_profile.md` §5) |

The SAS case was tracked in this repository from 2026-09-08 to 2026-09-16 (commits 73357e9 … 6316d35)
and is still in the git history of that period. Removing it from the history is a separate, destructive
operation (`git filter-repo` and a forced push to both remotes) and is done, if at all, deliberately.

Documents elsewhere in the repository that cite SAS runs or files (`BACKLOG.md`, `docs/sensors/`,
`docs/review_2026-09-15_sensor_texts.md`, the skills) say so with the path `examples/ignored/SAS`; the
facts they cite stand, the files are simply not in the public tree.
