<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-3 -->

Transcription only — no figures changed. Lines A–M are my round-1 table carried forward, with the two round-2 revisions marked; the uplifts are recomputed on the revised base exactly as stated in round 2.

| # | Line | pm | Note |
|---|---|---|---|
| A | Domain immersion + architecture/technology selection (~1.5 months, most of the team) | 10 | unchanged from R1 |
| B | Render workers: common harness 3; 8–10 formats at ~0.6–1.2 each | 10 | unchanged |
| C | OCR workers on the third-party library (wrapping, throughput, error paths) | 4 | unchanged |
| D | Cluster core: watchdogs + tokens, unordered status store, fax orchestration, resumption, failure survival | 20 | **revised in R2** (was 16) |
| E | Cluster management tool (queues, node health, job distribution) | 4 | unchanged |
| F | NOC — remote PoP / cluster / queue state, collectors + console | 6 | unchanged |
| G | User portal (archive, per-user TIFF-vs-PDF config, numbers, settings) | 9 | **revised in R2** (was 8) |
| H | Inbound-email parser, Tx path (MIME, addressing, sender auth, bounces, abuse) | 5 | unchanged |
| I | Rx assembly and outbound email (page-by-page TIFF or PDF attachment, send) | 3 | unchanged |
| J | CDR / billing data capture (schema, reliable write, reconciliation) | 3 | unchanged |
| K | Integration: PoP protocol, routing, Lustre, DB+API contracts, coexistence with v1 | 6 | unchanged |
| L | Integration tests on the real stream + comparison harness vs old system + load to nominal/burst | 8 | unchanged |
| M | Rollout, dual-run, cutover readiness (A2 Done) | 4 | unchanged |
| | **Subtotal** | **92** | |
| N | Dedicated QA at 30% of the component base — base is subtotal 92 less the already-whole-team lines A (10) and L (8) = 74; 0.30 × 74 = 22.2 | 22 | uplift; base of 74 is *implied* (arithmetic, not written out in R2) |
| O | PM / lead / coordination at 12% of (92 + 22 = 114) = 13.68 | 14 | uplift |
| | **Arithmetic total** | **128** | stated in R2 |
| P | Carry for cross-component integration drag / rounding, 128 → 130 (the P-8 omission argument, booked as a carry rather than a separate component line) | 2 | **implied** — the carry was stated in R2 as "carried as 130", the +2 line itself was not broken out |
| | **TOTAL** | **130** | |

```
TOTAL: 130 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
```
