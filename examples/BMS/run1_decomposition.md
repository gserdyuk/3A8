# BMS — Run #1: Decomposition (bottom-up + PERT)

Date: 2026-07-17. Input: [BMS_extracted.md](BMS_extracted.md) + [assumptions.md](assumptions.md).
Run rule: the WBS is built **strictly from what the RFP says** — with no corrections for scope creep, "icebergs," or organizational overhead. This is not carelessness but the method's discipline: its blind spots are to be caught by reference class, not by hidden fudge factors inside the WBS.

## WBS + PERT (person-days; O = optimistic, M = mode, P = pessimistic)

| # | WBS item | O | M | P | E | σ |
|---|---|---:|---:|---:|---:|---:|
| 1 | Discovery / requirements detailing | 15 | 25 | 40 | 25.8 | 4.2 |
| 2 | Architecture and technical design | 10 | 15 | 25 | 15.8 | 2.5 |
| 3 | UI/UX design (3 portals, responsive) | 15 | 25 | 40 | 25.8 | 4.2 |
| 4 | Setup: CI/CD, environments, IaC | 10 | 15 | 25 | 15.8 | 2.5 |
| 5 | SSO + role/permission model (5 actor types) | 8 | 12 | 20 | 12.7 | 2.0 |
| 6 | Data model, DB, audit | 10 | 15 | 22 | 15.3 | 2.0 |
| 7 | Notification service (email + SMS gateway) | 8 | 12 | 20 | 12.7 | 2.0 |
| 8 | CTC integration (frequent sync, merge policy, alerts) | 15 | 25 | 45 | 26.7 | 5.0 |
| 9 | UPSA integration | 5 | 8 | 15 | 8.7 | 1.7 |
| 10 | Hotel-aggregator integration (search + booking) | 20 | 35 | 60 | 36.7 | 6.7 |
| 11 | Uber integration | 8 | 12 | 20 | 12.7 | 2.0 |
| 12 | Search & prioritization engine (custom rules) | 20 | 30 | 50 | 31.7 | 5.0 |
| 13 | Booking workflow engine (6+ statuses, extensible) | 15 | 22 | 35 | 23.0 | 3.3 |
| 14 | Manual booking (Travel Manager, web forms) | 5 | 8 | 12 | 8.2 | 1.2 |
| 15 | Manual hotel change / changes UI | 4 | 6 | 10 | 6.3 | 1.0 |
| 16 | Combining transport bookings | 5 | 8 | 15 | 8.7 | 1.7 |
| 17 | Employees Portal (view/confirm/print/feedback) | 12 | 18 | 28 | 18.7 | 2.7 |
| 18 | Administration Portal (config, rules, statuses) | 18 | 28 | 45 | 29.2 | 4.5 |
| 19 | Suppliers Portal (manual upload flows) | 10 | 15 | 25 | 15.8 | 2.5 |
| 20 | Reporting (booking / suppliers / financial) | 10 | 15 | 25 | 15.8 | 2.5 |
| 21 | NFR: performance, HA/DR | 8 | 14 | 25 | 14.8 | 2.8 |
| 22 | Security hardening, TLS, DPA review | 5 | 8 | 15 | 8.7 | 1.7 |
| 23 | QA: system and integration testing | 25 | 40 | 60 | 40.8 | 5.8 |
| 24 | UAT support and bugfix | 10 | 15 | 30 | 16.7 | 3.3 |
| 25 | Production deployment, cutover, documentation | 5 | 8 | 12 | 8.2 | 1.2 |
| 26 | PM/BA support | 20 | 30 | 45 | 30.8 | 4.2 |

## Method result

- **E(total) ≈ 486 person-days** (~97 person-weeks).
- σ under the assumption of item independence ≈ 17 pd → 90% CI ≈ **458–514 pd**.
- Naive bounds (sum of all O / all P): **296–764 pd** — the method's real uncertainty lies closer to this range than to the CI (see below).

⚠️ **A diagnostic artifact expected by the methodology:** the CI ±3.5% is absurdly narrow. It follows from the assumption of error independence across WBS items — and that is exactly blind spot #1 of the method (risk correlation). If the project "slipped" on the CTC integration, it almost certainly slips on the aggregator and on UAT too. The narrowness of the CI is not precision but a consequence of construction. In Step B one must compare with the other methods both the center (486) and the shape of the spread.

## The method's assumption log (static blind spots, per METHODOLOGY.md §2)

Not accounted for **by construction**:
1. **Correlation of risk across items** — summing σ² assumes independence; common causes (unavailability of the client's API, the quality of the CTC documentation, turnover) strike many items at once.
2. **Systemic/integration risks as a whole** — the WBS covers what the RFP says; "icebergs" like the real complexity of "intelligent search" or the undocumented behavior of the CTC API do not exist in the WBS.
3. **Organizational overhead** — ceremony, time fragmentation, approvals with the client, waiting for access. It is not, and cannot be, in the items' pd estimates.
4. **Scope creep** — the content of the RFP dated 2016-06-10 was estimated, not what the project turns out to be by the end.

## What's next

Run #2 — reference class forecasting (the same input, the same assumptions). The methodology's expectation: a higher range center, a wider spread; the divergence is interpreted through points 2–4 above.
