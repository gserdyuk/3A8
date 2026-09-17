<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-8 -->

Transcription only — no figure changed. Lines marked "implied" were arithmetic I stated as a multiplier or as a rounding, never as a number.

## Round-2 decomposition, in full (person-months, A9 convention)

| # | Line | pm | Note |
|---|---|---|---|
| 1 | Domain immersion + architecture/technology selection (DHT etc.), ~1.5 calendar months across most of the team | 9 | whole-team line — excluded from the QA/PM uplift below |
| 2 | Rendering workers: driver-based render framework (3) + 8–10 formats × ~1 each | 12 | |
| 3 | OCR workers on a third-party library: integration, searchable-PDF assembly, throughput tuning | 4 | |
| 4 | Cluster core: watchdogs + tokens, unordered status store, per-fax state machine, idempotency, retry, recovery, back-pressure | 18 | round 1: 16; +2 in round 2 (P-7's duplicate-fax correctness bar) |
| 5 | Cluster management tool (queue depths, node lifecycle, deployment/agents) | 4 | |
| 6 | NOC: telemetry from 10–20 remote PoPs + cluster + queues, alerting, operator UI | 6 | |
| 7 | User portal: accounts, per-user delivery configuration, fax history/search/retrieval, admin | 8 | |
| 8 | Inbound e-mail parser / Tx entry: SMTP ingest, MIME and attachment extraction, sender authentication, number extraction, bounce and error paths | 5 | |
| 9 | CDR capture and billing-data hand-off | 3 | |
| 10 | Integration surfaces: PoP protocol, ready least-cost routing, Lustre, DB schema and the inter-component API | 6 | |
| 11 | Integration tests on the real stream: shadow harness, load generation, result comparison against the old system | 10 | round 1: 7; +3 in round 2. whole-team line — excluded from the QA/PM uplift below |
| 12 | Rollout, coexistence with v1 during transition, production hardening | 5 | |
| 13 | Rx delivery path: PoP intake, per-user TIFF-per-page vs PDF assembly, outbound email composition and deliverability | 5 | added in round 2 — the omission P-3/P-4/P-5/P-6 exposed |
| | **Subtotal** | **95** | stated in round 2 |
| 14 | QA/PM uplift, +25% applied to lines 2–10 and 12–13 only (76 pm × 0.25) | **+19.0** | *implied* — stated as "76 × 1.25 + 19 ≈ 114" |
| | **Subtotal after uplift** | **114.0** | stated in round 2 |
| 15 | Glue / cross-component-defect factor, ×1.12 (114 × 0.12) | **+13.7** | *implied* — stated as the ×1.12 factor giving ≈128 |
| | **Computed total** | **127.7** | stated as "≈ 128" |
| 16 | Rounding down, carried figure | **−2.7** | *implied* — stated as "carried as 125" |
| | **TOTAL** | **125** | |

Cross-check on the uplift base: lines 2–10 and 12–13 sum to 76 (95 − 9 − 10), which is the figure the +25% was taken on.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
