# Run 60 — the orchestrator's own application of RK60, made before the diagnostician returned

Net task hours. Fills priced by `price_fills60.py` from rate table v0.1-h under RK60 §3's fill rules; this file is not given to the diagnostician.

## Repeat 1

| step | low | central | high |
|---|---:|---:|---:|
| estimate total | 34933 | 34933 | 34933 |
| + H | 138 | 373 | 787 |
| + C | 731 | 2222 | 5196 |
| B_T2 | 35802 | 37528 | 40916 |
| + T2 (6 / 8 / 11%) | 2148 | 3002 | 4501 |
| subtotal | 37950 | 40531 | 45417 |
| x G1 (1.09 / 1.18 / 1.30) | 41366 | 47826 | 59042 |
| **x G2 (1.05 / 1.10 / 1.22) = calibrated** | **43434** | **52609** | **72031** |
| ratio to the raw total | x1.24 | x1.51 | x2.06 |

<details><summary>low, repeat 1: the fills</summary>

- 80.7 h — A140 Access Data REST API, 6 items (interface S), x1.6
- 57.6 h — A089 migration items G2m/G3m/G4m (store S), x1.6
- 207.8 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 4 fills (surface S)
- 90.9 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 2 fills (surface S)
- 90.9 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 2 fills (behaviour S)
- 76.7 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 1 fills (interface S)
- 90.9 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 2 fills (store S)
- 130.7 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 2 x A9 L cell 46.7 h, x1.4
- 42.7 h — go-live initial load: read-store population, (central) search-index build — 1 x (G3m + G4m store S) 26.7 h, x1.6

</details>

<details><summary>central, repeat 1: the fills</summary>

- 153.1 h — A140 Access Data REST API, 6 items (interface M), x1.6
- 117.3 h — A089 migration items G2m/G3m/G4m (store M), x1.6
- 102.7 h — A018 migration items G2m/G3m/G4m (store M), x1.4
- 569.1 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 6 fills (surface M)
- 452.7 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 5 fills (surface M)
- 362.1 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 4 fills (behaviour M)
- 140.0 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 1 fills (interface M)
- 336.0 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 4 fills (store M)
- 196.0 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 3 x A9 L cell 46.7 h, x1.4
- 166.4 h — go-live initial load: read-store population, (central) search-index build — 2 x (G3m + G4m store M) 52.0 h, x1.6

</details>

<details><summary>high, repeat 1: the fills</summary>

- 262.4 h — A140 Access Data REST API, 6 items (interface L), x1.6
- 190.9 h — A089 migration items G2m/G3m/G4m (store L), x1.6
- 167.1 h — A018 migration items G2m/G3m/G4m (store L), x1.4
- 167.1 h — C01 migration items G2m/G3m/G4m (store L), x1.4
- 1364.9 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 8 fills (surface L)
- 988.4 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 6 fills (surface L)
- 988.4 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 6 fills (behaviour L)
- 471.3 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 2 fills (interface L)
- 915.6 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 6 fills (store L)
- 196.0 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 3 x A9 L cell 46.7 h, x1.4
- 270.9 h — go-live initial load: read-store population, (central) search-index build — 2 x (G3m + G4m store L) 84.7 h, x1.6

</details>

## Repeat 2

| step | low | central | high |
|---|---:|---:|---:|
| estimate total | 31954 | 31954 | 31954 |
| + H | 152 | 409 | 847 |
| + C | 731 | 2222 | 5196 |
| B_T2 | 32837 | 34585 | 37997 |
| + T2 (6 / 8 / 11%) | 1970 | 2767 | 4180 |
| subtotal | 34807 | 37352 | 42177 |
| x G1 (1.09 / 1.18 / 1.30) | 37940 | 44075 | 54830 |
| **x G2 (1.05 / 1.10 / 1.22) = calibrated** | **39837** | **48483** | **66892** |
| ratio to the raw total | x1.25 | x1.52 | x2.09 |

<details><summary>low, repeat 2: the fills</summary>

- 80.7 h — A140 Access Data REST API, 6 items (interface S), x1.6
- 57.6 h — A089 migration items G2m/G3m/G4m (store S), x1.6
- 7.0 h — A158 K3 (statement-compliance S), x1.4
- 7.0 h — A159 K3 (statement-compliance S), x1.4
- 207.8 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 4 fills (surface S)
- 90.9 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 2 fills (surface S)
- 90.9 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 2 fills (behaviour S)
- 76.7 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 1 fills (interface S)
- 90.9 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 2 fills (store S)
- 130.7 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 2 x A9 L cell 46.7 h, x1.4
- 42.7 h — go-live initial load: read-store population, (central) search-index build — 1 x (G3m + G4m store S) 26.7 h, x1.6

</details>

<details><summary>central, repeat 2: the fills</summary>

- 153.1 h — A140 Access Data REST API, 6 items (interface M), x1.6
- 117.3 h — A089 migration items G2m/G3m/G4m (store M), x1.6
- 102.7 h — A018 migration items G2m/G3m/G4m (store M), x1.4
- 17.7 h — A158 K3 (statement-compliance M), x1.4
- 17.7 h — A159 K3 (statement-compliance M), x1.4
- 569.1 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 6 fills (surface M)
- 452.7 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 5 fills (surface M)
- 362.1 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 4 fills (behaviour M)
- 140.0 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 1 fills (interface M)
- 336.0 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 4 fills (store M)
- 196.0 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 3 x A9 L cell 46.7 h, x1.4
- 166.4 h — go-live initial load: read-store population, (central) search-index build — 2 x (G3m + G4m store M) 52.0 h, x1.6

</details>

<details><summary>high, repeat 2: the fills</summary>

- 262.4 h — A140 Access Data REST API, 6 items (interface L), x1.6
- 190.9 h — A089 migration items G2m/G3m/G4m (store L), x1.6
- 167.1 h — A018 migration items G2m/G3m/G4m (store L), x1.4
- 167.1 h — C01 migration items G2m/G3m/G4m (store L), x1.4
- 29.9 h — A158 K3 (statement-compliance L), x1.4
- 29.9 h — A159 K3 (statement-compliance L), x1.4
- 1364.9 h — surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) — 8 fills (surface L)
- 988.4 h — other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) — 6 fills (surface L)
- 988.4 h — behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) — 6 fills (behaviour L)
- 471.3 h — interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) — 2 fills (interface L)
- 915.6 h — stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high — 6 fills (store L)
- 196.0 h — NFR verification targets: capacity/volume, availability/failover, (central) latency — 3 x A9 L cell 46.7 h, x1.4
- 270.9 h — go-live initial load: read-store population, (central) search-index build — 2 x (G3m + G4m store L) 84.7 h, x1.6

</details>

