# FaxRxTx — Run 1: Classic Decomposition (bottom-up WBS + PERT)

**Method:** decomposition of the §6 scope of SYSTEM.md into leaf tasks, triple
estimates O/M/P in person-months, PERT: E = (O + 4M + P)/6, σ = (P − O)/6.
**Input:** SYSTEM.md + assumptions.md (A1–A9). Nothing else was read.
**Units:** person-months (A9), a blended team including QA/PM.
**Run date:** 2026-07-17.

Decomposition principles:
- Scope strictly per A1 (included / not included), DoD per A2 (production traffic,
  comparison with the old system, v1 can be switched off).
- Era A5: orchestration (watchdogs + tokens) is written by hand, MQ and ready
  orchestrators are unavailable/excluded — this is a noticeable share of the core.
- Rendering formats per A7 — each format is a separate piece of integration
  and stabilization work, including a reserve for 1–3 forgotten ones.
- Scale per A6: nominal ~30/s, burst ~300/s, resilience to failures and
  delivery control of each fax are mandatory properties, built into the
  estimates of the core and load testing, without external multipliers.

---

## WBS and estimates (person-months)

### 1. The immersion and architecture-selection phase (A1, A3)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 1.1 | Domain immersion: fax protocols, telecom, analysis of v1's behavior as a live requirements reference | 2.0 | 4.0 | 7.0 | 4.17 | 0.83 |
| 1.2 | Technology evaluation and prototypes (DHT and other distributed storage/coordination mechanisms) | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 1.3 | Architecture of the target system + a coexistence/transition plan with v1 | 2.0 | 4.0 | 8.0 | 4.33 | 1.00 |
| 1.4 | Planning phase ("waterfall before scrum"): backlog, specs, process setup | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |

### 2. Core: the cluster and the delivery-control mechanism (watchdogs + tokens)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 2.1 | Fax status and token model: an unordered status store, the job lifecycle | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 2.2 | Watchdogs: detecting hung/lost jobs, resuming processing after failures | 2.0 | 4.0 | 8.0 | 4.33 | 1.00 |
| 2.3 | Job dispatch across cluster nodes without MQ (pull/lease logic over the DB and the store) | 2.0 | 4.0 | 8.0 | 4.33 | 1.00 |
| 2.4 | Delivery semantics: idempotency, protection against duplicates/losses under node and network failures | 2.0 | 4.0 | 9.0 | 4.50 | 1.17 |
| 2.5 | Cluster management tool: queue lengths, node state, worker management | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 2.6 | Deployment and configuration of the cluster nodes (~16–20), a private network, install scripts | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 2.7 | Load testing of the core: nominal ~30/s, burst up to ~300/s, degradation and recovery | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |

### 3. The Rx path (fax reception)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 3.1 | Reception of TIFF from PoP into the data center: integration with the existing PoP software, registration of the fax in the core | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 3.2 | Worker composing the email with per-page TIFF attachments (per user configuration) | 0.75 | 1.5 | 3.0 | 1.63 | 0.38 |
| 3.3 | Worker converting TIFF → PDF | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 3.4 | OCR worker: integration of a third-party OCR library, embedding into the PDF pipeline, stabilization | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 3.5 | Email-sending worker: SMTP, retries, handling non-delivery | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |

### 4. The Tx path (fax transmission)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 4.1 | Inbound-email parser: addressing, extracting the fax number, attachments, validation, errors to the user | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 4.2 | Rendering framework via a printer driver (Black Ice-class): process isolation, timeouts, hung applications | 2.0 | 3.5 | 7.0 | 3.83 | 0.83 |
| 4.3 | Office-format renderers DOC/XLS/PPT: integration and stabilization (the most capricious) | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 4.4 | PDF and TXT renderers | 0.75 | 1.5 | 3.0 | 1.63 | 0.38 |
| 4.5 | Graphics-format renderers GIF/TIFF | 0.5 | 1.0 | 2.0 | 1.08 | 0.25 |
| 4.6 | Reserve A7: 1–3 forgotten formats (integration + stabilization of each) | 0.5 | 1.5 | 3.5 | 1.67 | 0.50 |
| 4.7 | Transmission of TIFF archives to the PoP: packaging, transport, integration with the ready routing program | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 4.8 | Sending statuses: delivery confirmations/reports, retries, notifications to the sender | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |

### 5. NOC

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 5.1 | Telemetry collection: agents/polling of the remote PoPs (10–20), cluster nodes, queues | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 5.2 | NOC UI: state dashboards, alerts, incident history | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |

### 6. User portal

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 6.1 | Portal — backend/API: accounts, delivery configuration (TIFF/PDF, OCR), numbers, fax history | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 6.2 | Portal — web UI (ASP.NET of era A5) | 1.0 | 2.5 | 5.0 | 2.67 | 0.67 |

### 7. Data and storage

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 7.1 | DB schema and the API for inter-component interaction (components communicate through the DB and an API) | 1.5 | 3.0 | 6.0 | 3.25 | 0.75 |
| 7.2 | CDR and billing data: event capture, reliable storage, export to billing (billing itself is out of scope) | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |
| 7.3 | Integration with Lustre: layout of the archive and working files, access from the nodes, cleanup/retention | 0.75 | 1.5 | 3.0 | 1.63 | 0.38 |

### 8. Integration testing and transition (A2)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 8.1 | Integration-test framework on the real stream: traffic duplication, comparison of results with the old system | 2.0 | 4.0 | 8.0 | 4.33 | 1.00 |
| 8.2 | Comparison runs, analysis of discrepancies, stabilization to convergence with v1 | 2.0 | 4.0 | 9.0 | 4.50 | 1.17 |
| 8.3 | Coexistence with v1 and phased switchover of production traffic | 1.0 | 2.5 | 5.0 | 2.67 | 0.67 |
| 8.4 | Rollout to production: prod configuration, runbook, launch-period on-call to DoD | 1.0 | 2.0 | 4.0 | 2.17 | 0.50 |

### 9. Cross-cutting work (QA/PM are included in the estimate per A9)

| ID | Work | O | M | P | E | σ |
|----|--------|---:|---:|---:|---:|---:|
| 9.1 | QA throughout development: test plans, functional regression of components (beyond the integration tests of §8) | 3.0 | 6.0 | 10.0 | 6.17 | 1.17 |
| 9.2 | PM/scrum process: backlog management, coordination, reporting | 2.0 | 4.0 | 6.0 | 4.00 | 0.67 |

---

## Totals

37 leaves.

| Metric | Value |
|---|---|
| Σ O (sum of optimistic) | **51.25 pm** |
| Σ M (sum of most-likely) | **103.5 pm** |
| Σ P (sum of pessimistic) | **204.5 pm** |
| **Σ E (PERT)** | **≈ 111.6 pm** |
| Σ σ² (variance of the sum) | ≈ 19.66 |
| **σ of the sum (under leaf independence)** | **≈ 4.4 pm** |
| **E ± 2σ** | **≈ 102.8 … 120.5 pm** |
| **Honest range (ΣO … ΣP)** | **51 … 205 pm** |

Intermediate E sums by section: immersion phase 13.9; core/cluster 24.0;
Rx 11.4; Tx 19.0; NOC 6.5; portal 5.9; data 7.0; integration
tests/transition 13.7; QA/PM cross-cutting 10.2.

**An explicit caveat about σ.** The total σ ≈ 4.4 pm is obtained under the assumption
of **leaf independence** (σ² add, σ grows as the square root). This is a
known artifact of the method: real task risks are correlated (the same
team, one technology base, a shared core), so the range
E ± 2σ (≈ 103–120 pm) is **artificially narrow** and reflects not the project's real
uncertainty but the mathematics of summing independent quantities.
The honest range from the sums of the extreme scenarios (51–205 pm) more honestly describes the
edges, though all tasks hitting O simultaneously or all hitting P is also
unlikely. A reasonable reading of the result: center ≈ 110 pm, the real
uncertainty is noticeably wider than ±2σ and narrower than ΣO…ΣP.

---

## What the method does not see by construction

Listed without corrections — bottom-up decomposition is by construction blind
to these effects; accounting for them is the job of the other methods of the pipeline.

1. **Correlation of risk across tasks.** Summing variances as independent underestimates
   the spread: if "watchdogs + tokens" turned out harder than
   expected, then with high probability dispatch, delivery semantics,
   and integration stabilization will also be harder — a shared team,
   a shared architecture, shared technology surprises (.NET 3.x, Lustre,
   the absence of MQ). The method adds σ² and pretends the tails
   cancel.
2. **Integration of the parts — edges, not nodes.** The WBS estimates nodes (components),
   while a significant share of the effort lives on the edges: joining the workers to
   the core, the core to the DB/Lustre, the Tx path to the ready routing and PoP
   software, coexistence with v1. Some edges here are broken out into leaves (3.1, 4.7, 8.x),
   but the combinatorics of interactions of N components is always wider than any
   finite list of leaves — the "missing edges" are absent from the estimate.
3. **Organizational overhead.** Communication within the team, onboarding,
   changes of priority by management, context switches, idle time waiting
   for decisions, "pressure without a deadline" (A8) — decomposition sees
   only the pure work on the leaves. The blended composition is partly accounted for
   by leaves 9.1–9.2, but the systemic organizational tax is not.
4. **Scope creep.** The list of work fixed today is estimated.
   A real project to "redo what management did not like" almost
   guaranteedly accreted new wishes, formats, requirements for the NOC
   and portal along the way — the method estimates a snapshot of the scope, not its
   trajectory.
5. **Unknown unknowns of the domain.** The team did not know the domain (A3);
   the leaves describe work that is *visible in advance*. Tasks whose existence
   you only learn about inside the telecom/fax domain (protocol quirks,
   fax-machine compatibility, line quality) do not get into the WBS at
   all.
6. **The stabilization tail in production.** The DoD (A2) requires convergence with the old
   system on the real stream; leaves 8.2–8.4 estimate the foreseeable part
   of this work, but the length of the "last 10%" tail on live traffic is a classic
   zone of bottom-up underestimation.

No correction coefficients for points 1–6 **were applied** —
by the run protocol this is the responsibility of the reference-class method.
