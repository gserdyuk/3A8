<!-- orchestrator header, not part of the reply: run 69, transcription request after round 2 (no re-estimation), participant P-6 -->

Transcription only — no figures changed. Lines not stated explicitly in round 2 are marked "implied"; they are the values my stated round-2 subtotal of ~118 and total of 125 require.

## Decomposition behind the round-2 total

| # | Block | pm | Source |
|---|---|---|---|
| 1 | Domain immersion, architecture and technology selection (DHT etc.), 1–2 calendar months of the whole team | 12 | round 1, unchanged |
| 2 | Rendering workers: worker host plus 8–10 format integrations, each with its own stabilization | 12 | round 1, unchanged |
| 3 | OCR workers and TIFF→PDF: library integration, output quality, throughput | 6 | round 1, unchanged |
| 4 | Cluster with delivery control: watchdogs + tokens, unordered store, per-fax state, resume, distribution, failure survival | 24 | **revised in round 2** (was 28; trimmed on the P-1/P-2/P-3/P-5/P-7/P-8/P-10 cluster-core comparison and the double-count against line 12) |
| 5 | Cluster management: queue depths, node control | 4 | round 1, unchanged |
| 6 | NOC: remote PoP state, cluster and queue state, agents, alerting, UI | 9 | **implied** (was 10; part of the −2 my round-2 subtotal of ~118 requires after the line-4 trim, taken here because my NOC sat at the group's high end) |
| 7 | User portal: accounts, per-user delivery configuration, history and archive access | 11 | **implied** (was 12; the other half of that −2, same reason) |
| 8 | Inbound email parser for Tx: MIME, number extraction, sender authorization, error/confirmation mail | 6 | round 1, unchanged |
| 9 | Outbound email delivery for Rx at volume, attachment assembly, deliverability | 4 | round 1, unchanged |
| 10 | CDR / billing-data capture (feed only) | 3 | round 1, unchanged |
| 11 | Integration surfaces: PoP software, ready routing, Lustre, DB/API contracts, coexistence with the old system | 10 | round 1, unchanged |
| 12 | Integration tests on the real stream with comparison against the old system, plus burst/load harness | 12 | round 1, unchanged |
| 13 | Rollout, migration and production cutover to the A2 definition of done | 5 | round 1, unchanged |
| | **Subtotal** | **118** | stated in round 2 as "~118" |
| 14 | PM / coordination uplift, 10% of the subtotal, not already inside the blocks | 11.8 | round 2, stated as "PM at 10%" |
| | **Before final adjustment** | **129.8** | stated in round 2 as "→ ~130" |
| 15 | Downward adjustment for double-count risk between the block-level stabilization allowances and lines 12 and 14 (P-8's caution) | −4.8 | **implied** — the round-2 total of 125 is the "carried as" figure against ~130 |
| | **Total** | **125.0** | |

Note on QA: there is no separate QA uplift line, and its absence is deliberate rather than an omission. Blocks 1–13 are sized as whole-team effort (build + test + stabilize) with QA inside them, and line 12 carries the dedicated acceptance campaign. This is the structural difference between my table and P-1's, P-3's, P-5's, P-7's and P-8's, which size the blocks dev-side and then add QA at 25–35%.

TOTAL: 125 person-months, on the A9 convention below (1 pm = 21 person-days = 168 hours of work
       on the task, whole team including QA and PM)
