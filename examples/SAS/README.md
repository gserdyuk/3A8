# SAS — case record

**The document.** `Graduate_Work_-_RFP.pdf` — a Request for Proposal for a "Member Application
Solution", 18 pages, dated 2018-09-12, with an EPAM Systems header ("EPAM response to XXX – YYY RFP",
confidential). The client is anonymised as "X-Customer": a standards organisation serving 200 000+
member companies, licensing numeric prefixes from which members build product identifiers (GIN) and
location identifiers (LN). The system to be built is a B2B web application in three modules —
Product, Location, Access Data — with migration off the current applications. The folder name `SAS`
is the author's. Text extracted with pypdf to `rfp_text_raw.txt`.

**Case number: 3** in the project's sequence (BMS, FaxRxTx, SAS). It is the first case prepared
under the `docs/case_profile.md` rule — profile pinned before any estimate exists — and the first
to declare `G-MIGRATE`.

---

## What the orchestrator saw, declared

The orchestrator read the whole RFP. Before pinning, the text was scanned for anything a sensor is
forbidden to see: **the RFP contains no effort, cost, duration, deadline, budget or team-size
figure.** The only numbers in it are data volumes and user counts (NFR-2, NFR-7), the response-time
targets (NFR-14), a 120-day proposal validity period (§3, a commercial term about the bid, not the
work), and the phrase "at no cost to X-Customer" in NFR-5. The `syn` lesson — an RFP carrying a
timeline the estimating group also saw — does not apply here: **there is no timeline in this RFP.**
Nothing was struck.

The orchestrator has seen no estimate, bid, outcome or proposal for this RFP. The author states
that no outcome is known (`case_profile.md` §5).

## Order of pinning (per `docs/case_profile.md`)

| # | artefact | state 2026-09-08 |
|---|---|---|
| 1 | `case_profile.md` | **approved 2026-09-08** — team middle/senior, one site, first domain, 6 h/day + ×1.10, no outcome; overhead detail fields `unknown` |
| 2 | `requirements_pinned.md` (N = 153) · `requirements_split.md` · `requirements_product.md` (N = 146) · `requirements_work.md` (N = 7) | **pinned 2026-09-08**, md5 in `requirements.pin.txt` |
| 2 | `assumptions.md` v1 · `assumptions_product.md` · `open_questions.md` | **approved 2026-09-08** — 21 assumptions and 22 questions, one reading each |
| 2 | `technology_declaration.md` | **approved 2026-09-08** — `D-TEAM` confirmed by the profile; `SA-PENTEST`, test = M, cycles 2/2/2 |
| 3 | sensor runs | **run 44** product model n = 2 (`run44_product_model_measurement.md`) · **run 45** crossing, seven batches (`run45_work_model.md`) · **run 46** reference class n = 2 (`run46_reference_class.md`) · **run 47** size classes n = 2 and the assembly (`run47_sizing_and_assembly.md`) · **run 48** Step C rates, gap-blind, and Steps B–D (`run48_steps_BD.md`) |
| 4 | the deliverable | **`estimate_SAS_2026-09-08.md`** and `reports/` (built from `report_data.json`) — written 2026-09-08 knowing no outcome will open |
| 5 | `FACT.md` | will not exist: no known outcome (author, 2026-09-08). Gate test 3 cannot be scored on this case |

## File map

| file | what |
|---|---|
| `Graduate_Work_-_RFP.pdf`, `rfp_text_raw.txt` | the source and its extraction |
| `requirements_pinned.md` | the anchor: every obligation under the RFP's own id, plus `I-` and `W-` for prose-only obligations; five RFP rows not carried, with reasons |
| `requirements_split.md` | product versus work, rules S1–S5 of BMS |
| `requirements_product.md`, `requirements_work.md` | the two halves, ids unchanged |
| `requirements.pin.txt` | md5 of the three lists and the projection, LF form |
| `assumptions.md` | the log, A0–A21 |
| `assumptions_product.md` | the projection the product-model sensor sees |
| `open_questions.md` | the register, Q1–Q22 |
| `technology_declaration.md` | one choice per catalogue dimension, parameters, W6 outcome |
| `case_profile.md` | the case conditions, pinned before any number |
| `run44_product_model_measurement.md` … `run48_steps_BD.md` | one record per run; raw sensor output verbatim under `run*_raw/` |
| `estimate_SAS_2026-09-08.md` | the deliverable: centre, corridor, reserve, what is not in any number, what moves the answer |
| `report_data.json`, `reports/` | the report's data file and the built HTML, one file per build, never overwritten |
