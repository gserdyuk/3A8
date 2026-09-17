<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-9 -->

Transcription only — no tool use, no figure changed.

## Decomposition behind the round-2 total of 125 pm

| # | Line | pm | Source |
|---|---|---|---|
| 1 | Domain immersion + architecture/technology selection (~1.5 mo, partial team) | 12 | stated round 1, unchanged |
| 2 | Rendering workers: framework + 8–10 formats, each integrated and stabilized | 14 | stated round 1, unchanged |
| 3 | OCR workers on third-party library (TIFF→searchable PDF, tuning, throughput) | 5 | stated round 1, unchanged |
| 4 | Cluster + delivery control: watchdogs, tokens, state store, resume, distribution | 22 | **revised in round 2** (was 28; P-3/P-8 argument that the expected hardening round belongs in the range, not the point) |
| 5 | Cluster management tool (queues, node health, dispatch) | 5 | stated round 1, unchanged |
| 6 | NOC: state of remote PoPs, cluster, queues | 10 | stated round 1, unchanged |
| 7 | User portal (accounts, configuration, fax history) | 12 | stated round 1, unchanged; held in round 2 |
| 8 | Inbound-email parser / Tx intake (MIME, number extraction, attachments, error paths) | 7 | stated round 1, unchanged |
| 9 | CDR and billing-data capture (billing itself excluded) | 4 | stated round 1, unchanged |
| 10 | DB/API plumbing + integration and coexistence with the old system | 8 | stated round 1, unchanged |
| 11 | Integration tests on the real stream with old-system comparison; load/burst testing | 12 | stated round 1, unchanged |
| 12 | Rollout to prod, cutover, stabilization to the A2 bar | 8 | stated round 1, unchanged |
| | **Subtotal, lines 1–12** | **119** | **implied** (round-1 subtotal 125 less the 6 pm taken off line 4) |
| 13 | PM / coordination uplift, ~10% of the subtotal | 12 | **implied** (round 1 stated 13 on a 125 base; the same ~10% on the 119 base) |
| | **Arithmetic sum** | **131** | **implied** |
| 14 | Judgement cut carried to the point estimate | −6 | **implied** (round 1 applied −8 on the grounds that the component lines absorb their own QA; P-1's dedicated-QA argument removed part of that justification, so the cut shrinks rather than a QA line being added) |
| | **Total** | **125** | as given |

Two notes on where the roles sit, so the table is not misread: dedicated QA is not a separate line — it lives inside the component lines 1–12 plus the whole of line 11, and P-1's argument acted on line 14 rather than adding a thirteenth component. Lines 1 and 11 were sized as whole-team from the outset and are therefore not subject to the line-13 uplift, which round 1 nonetheless applied across the full subtotal; I have left that as it was rather than re-deriving it, since this is a transcription.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
