<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-5 -->

**Transcription only — no figures changed.** The round-2 total held the round-1 decomposition unchanged: the two round-2 corrections (P-7's soak-testing argument pushing the orchestrator line up, P-9's double-counting objection pushing the QA uplift down) were judged to cancel, so neither was booked into an individual line. They appear below as one explicit net-zero line rather than being silently absorbed. Values marked "implied" were not stated as person-months in round 1 — round 1 gave a percentage or a rounding instruction — and are the figures my total requires.

| # | Line | pm | Note |
|---|---|---|---|
| 1 | Rendering worker framework + 8–10 formats | 9 | stated |
| 2 | OCR workers | 3 | stated |
| 3 | Cluster orchestration: watchdogs, tokens, unordered status store, resume | 18 | stated |
| 4 | Cluster management tool (queues, node state) | 3 | stated |
| 5 | NOC | 8 | stated |
| 6 | User portal | 10 | stated |
| 7 | Inbound email parser (Tx intake) | 5 | stated |
| 8 | Rx path: PoP→DC transfer, page-wise TIFF, email composition and send | 6 | stated |
| 9 | CDR capture / billing data | 3 | stated |
| 10 | Storage (Lustre) + DB schema + inter-component API | 6 | stated |
| 11 | Integration with old system + transition coexistence | 4 | stated |
| 12 | Integration tests on real stream, comparison against old system, rollout | 8 | stated |
| | **Dev subtotal (lines 1–12)** | **83** | stated |
| 13 | QA uplift, +35% of the dev subtotal | 29 | **implied** (round 1 gave the rate, not the pm: 0.35 × 83 = 29.05) |
| 14 | PM / coordination uplift, +10% of the dev subtotal | 8 | **implied** (0.10 × 83 = 8.30) |
| | **Subtotal after uplifts** | **120** | stated as "83 × 1.45 ≈ 120" (83 + 29 + 8 = 120.35) |
| 15 | Domain immersion, architecture and technology selection (~1.5 months, whole team) | 10 | stated; added after the uplifts, not uplifted again |
| | **Sum before rounding** | **130** | stated |
| 16 | Adjustment for v1 as an executable specification (removes specification churn, A3) | −5 | **implied** (round 1 stated "round down to 125") |
| 17 | Round-2 net revision: orchestrator line up (P-7) offset by QA-uplift double-counting down (P-9) | 0 | **implied**; the two were judged equal and opposite, so no line moved |
| | **TOTAL** | **125** | |

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
