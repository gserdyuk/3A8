<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-2 -->

Transcription only — no figures changed.

## Decomposition behind the round-2 total of 125 pm

| # | Line | pm | Source |
|---|---|---|---|
| 1 | Domain immersion, architecture and technology selection (DHT etc.), incl. discarded options | 8 | round 1 |
| 2 | Rendering workers: worker framework + 8–10 formats via printer driver, each integrated and stabilized (A7) | 11 | round 1 |
| 3 | OCR workers: third-party library integration, PDF assembly, quality tuning | 5 | round 1 |
| 4 | Cluster + delivery control (watchdogs, tokens, unordered store, per-fax resume) — build and harden | 21 | round 1, held against P-6/P-9's 28 |
| 5 | Cluster management tool (queues, node state, operator control) | 3.5 | round 1 |
| 6 | NOC: remote PoP state, cluster state, queue state | 7 | round 1 |
| 7 | User portal (configuration incl. TIFF-vs-PDF choice, archive, account) | 9 | round 1 |
| 8 | Inbound-email parser on the Tx path (parsing, number extraction, attachments, rejects/bounces) | 4.5 | round 1 |
| 9 | CDR and billing-data capture (billing itself excluded) | 2.5 | round 1 |
| 10 | Integration with the old system, coexistence for the transition | 6 | round 1 |
| 11 | Integration tests on the real stream with old-system comparison; load/burst testing | 9 | round 1 |
| 12 | Rollout to production, migration, cutover | 3.5 | round 1 |
| | *Round-1 subtotal* | *90* | |
| 13 | Rx delivery path: PoP→data-centre transfer, per-user TIFF-page-by-page vs PDF branching, email composition, outbound deliverability at volume | 5 | added in round 2 (P-3/P-4/P-5/P-6) |
| 14 | Database schema and inter-component API (the §4 spine), split out from line 10 | 4 | added in round 2 (P-4/P-5/P-9/P-10) |
| | **Component subtotal** | **99** | |
| 15 | Dedicated QA function, ~22% of the 90 pm of non-QA component work (lines 1–10, 12–14; line 11 already counted as QA) | 20 | round 2 |
| | *Subtotal with QA* | *119* | |
| 16 | PM, scrum lead and cross-cutting coordination, ~10% | 12 | round 2 |
| | *Arithmetic total* | *131* | |
| 17 | Downward adjustment for the mechanical acceptance oracle (outputs must match v1 on the same input, which makes the comparison campaign cheaper to converge than a spec-negotiated acceptance of the same size), and rounding | −6 | **implied** — stated in round 2 only as "I carry 125, a shade below that arithmetic" |
| | **Total** | **125** | |

Line 17 is the only figure I never stated as a number; it is the arithmetic residual between the 131 the uplifts produce and the 125 I carried, and the reasoning for it is quoted above from round 2.

---

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
