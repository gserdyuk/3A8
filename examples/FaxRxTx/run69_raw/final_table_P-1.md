<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-1 -->

## Round-2 decomposition, transcribed in full

No figure changed. Lines 1 and 7 carry the round-2 revisions (immersion 12 → 9, portal 12 → 10); all other block figures are as in round 1. The two uplift lines and the rounding line were stated in round 2 as a calculation rather than as a table, so their arithmetic values are marked "implied".

| # | Line | pm | Whole-team already? |
|---|---|---|---|
| 1 | Domain immersion, architecture and technology selection | 9.0 | yes |
| 2 | Cluster core: watchdogs, tokens, unordered status store, resume-on-failure, orchestration of ~16–20 nodes | 21.0 | no |
| 3 | Cluster management tool (queue depths, node lifecycle) | 5.0 | no |
| 4 | Rendering workers: framework + 8–10 formats | 11.0 | no |
| 5 | OCR workers, PDF assembly, per-user TIFF-vs-PDF policy | 5.0 | no |
| 6 | NOC: state of 10–20 remote PoPs, cluster, queues | 9.0 | no |
| 7 | User portal | 10.0 | no |
| 8 | Inbound email parser (Tx entry) | 6.0 | no |
| 9 | CDR / billing data capture | 3.5 | no |
| 10 | Integration surface: DB + API, Lustre, coexistence with the old system | 7.0 | no |
| 11 | Integration tests on the real stream vs v1, plus load/burst testing | 12.0 | yes |
| 12 | Production rollout, cutover, stabilisation to the A2 Done | 6.0 | yes |
| | **Subtotal** | **104.5** | |
| | *of which already whole-team (lines 1, 11, 12)* | *27.0* | |
| | *of which dev-side, eligible for the QA uplift (lines 2–10)* | *77.5* | |
| 13 | QA uplift, 25% of the 77.5 dev-side only (lines 1, 11, 12 excluded — this is the round-1 double-count P-3 caught) | **19.4** *(implied)* | |
| | *Running total after QA* | *123.9 (implied)* | |
| 14 | PM / scrum master / cross-cutting coordination, 10% of the running total 123.9 | **12.4** *(implied)* | |
| | *Arithmetic total* | *136.3 (implied)* | |
| 15 | Rounding down to the figure carried | **−1.3** *(implied)* | |
| | **TOTAL** | **135.0** | |

Two notes on what is *not* a line, unchanged from round 2: the decomposition-omission factor (P-8's ~1.2) and the continuing cost of domain ignorance after the immersion phase closes (P-2) are carried as upward skew in the range, deliberately not as additions to the point estimate.

---

TOTAL: 135 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
