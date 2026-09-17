<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-4 -->

Transcription only — no figures changed, and nothing re-estimated.

## Decomposition behind the round-2 total of 128 pm

| # | Line | pm | Source |
|---|---|---|---|
| 1 | Domain immersion, architecture and technology selection (A1/A3, ~1.5 calendar months of a forming team) | 10 | stated, round 1 |
| 2 | Core orchestration: watchdogs, tokens, per-fax state, resume, backpressure | 20 | stated, round 1 (held in round 2 against P-6/P-9's 28) |
| 3 | Cluster management tool (queue depth, node control, job placement) | 6 | stated, round 1 |
| 4 | Render worker framework + 8–10 formats via print driver | 13 | stated, round 1 |
| 5 | OCR workers on a third-party library, throughput tuning | 5 | stated, round 1 |
| 6 | Rx pipeline: PoP intake, per-user config, TIFF-per-page vs PDF, email composition and deliverability | 8 | stated, round 1 |
| 7 | Tx pipeline: inbound-email parser, MIME and attachment handling, number extraction, sender identification, archive handoff | 8 | stated, round 1 |
| 8 | NOC: remote PoP, cluster and queue state | 8 | stated, round 1 |
| 9 | User portal | 10 | stated, round 1 |
| 10 | Storage and data layer: Lustre layout, DB schema, inter-component API | 6 | stated, round 1 |
| 11 | CDR / billing data capture (billing itself excluded) | 3 | stated, round 1 |
| 12 | Integration with the old system and coexistence through the transition | 6 | stated, round 1 |
| 13 | QA beyond in-block testing: real-stream comparison harness, load testing to ~300/s, regression | 14 | stated, round 1 |
| 14 | Rollout, cutover, production hardening | 5 | stated, round 1 |
| 15 | PM and coordination across the whole period | 12 | stated, round 1 |
| | **Subtotal of lines 1–15** | **134** | arithmetic of the round-1 table |
| 16 | Rounding to the round-1 point estimate (134 table → 135 reported) | +1 | **implied** (round 1 reported 135 against a table summing to 134) |
| | **Round-1 total** | **135** | stated, round 1 |
| 17 | De-duplication of QA and PM against whole-team block sizes (the P-9 catch), net of the retained part of P-8's decomposition-glue uplift | −7 | **implied** — round 2 stated "roughly 6–7 pm" and "128", which fixes the net at exactly −7 |
| | **Round-2 total** | **128** | stated, round 2 |

**Implied split of line 17**, since round 2 named both the QA and the PM line as carrying the overlap but gave no breakdown: −4 against line 13 (QA, 14 → 10) and −3 against line 15 (PM, 12 → 9). Both marked **implied**; only their sum of −7 is fixed by the stated total.

Two notes so the table is not read as more precise than it is. Line 17 is a *net* figure: the gross double-count I identified was larger, and part of it was deliberately not deducted because P-8's argument that component tables systematically under-count cross-component and burst-mode work pushes in the opposite direction. The two were netted in one step rather than shown as separate gross lines, so no gross value for either exists to transcribe.

```
TOTAL: 128 person-months, on the A9 convention (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
```
