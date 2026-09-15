# Precomputed bases for the rate agent's targeted steps (you have no access to the leaf tables or the rate table and may not derive quantities of your own)

RK60 prices its fills H and C with the estimate's own rate table by element class and size, with the method's 20% integration constant along the parent path. The orchestrator has done that arithmetic; the priced amounts below are the bases you apply in RK60's order. Each is stated low / central / high (size S / M / L per RK60's fill rule; D4 at S; NFR targets at the carried response-time element's A9 cell, class L, 46.7 h each; integration x1.4 under a top-level subsystem, x1.6 under its matching child node, and along the real path for holes). Apply low with low, central with central, high with high. Unit: net person-hours of work on the task, integration included where stated.

## Repeat 1 — estimate total 34 933 h

| fill (RK60 §3) | low | central | high |
|---|---:|---:|---:|
| H: A140 Access Data REST API, 6 items | 81 | 153 | 262 |
| H: A089 migration items G2m/G3m/G4m | 58 | 117 | 191 |
| H: A018 migration items G2m/G3m/G4m | — | 103 | 167 |
| H: C01 migration items G2m/G3m/G4m | — | — | 167 |
| **H, hole fills, integration included** | **138** | **373** | **787** |
| C: surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) | 208 | 569 | 1365 |
| C: other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) | 91 | 453 | 988 |
| C: behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) | 91 | 362 | 988 |
| C: interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) | 77 | 140 | 471 |
| C: stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high | 91 | 336 | 916 |
| C: NFR verification targets: capacity/volume, availability/failover, (central) latency | 131 | 196 | 196 |
| C: go-live initial load: read-store population, (central) search-index build | 43 | 166 | 271 |
| **C, closure fills, integration included** | **731** | **2222** | **5196** |
| **B_T2 = estimate total + H + C** | **35802** | **37528** | **40916** |

## Repeat 2 — estimate total 31 954 h

| fill (RK60 §3) | low | central | high |
|---|---:|---:|---:|
| H: A140 Access Data REST API, 6 items | 81 | 153 | 262 |
| H: A089 migration items G2m/G3m/G4m | 58 | 117 | 191 |
| H: A158 K3 | 7 | 18 | 30 |
| H: A159 K3 | 7 | 18 | 30 |
| H: A018 migration items G2m/G3m/G4m | — | 103 | 167 |
| H: C01 migration items G2m/G3m/G4m | — | — | 167 |
| **H, hole fills, integration included** | **152** | **409** | **847** |
| C: surfaces for screenless behaviours: record entry/edit (and cloning at high) and hierarchy editor, Product and Location, under the module (x1.4); duplicate review and status/reuse-date under the shared-record child nodes (x1.6) | 208 | 569 | 1365 |
| C: other surfaces: approval review-and-decision (N07), admin assignment (N06), owner publish/share and consumer request/decision (N12), training links (N10), help-desk reset trigger (N06, high only) | 91 | 453 | 988 |
| C: behaviours: deactivate company user (N06), entitlement check before viewing (N21), export-option enforcement (N11), data-challenge follow-up (N07), edit-lock release (N07, high), role seeding (N06, high) | 91 | 362 | 988 |
| C: interfaces: 3scale usage collection (N09); import/export through the API (N11, high only) | 77 | 140 | 471 |
| C: stores: report definitions and schedules (N09), groups and members (N12), per-user subscriptions and onscreen notifications (N08, central), pending requests (N12) and page-layout templates (N19) at high | 91 | 336 | 916 |
| C: NFR verification targets: capacity/volume, availability/failover, (central) latency | 131 | 196 | 196 |
| C: go-live initial load: read-store population, (central) search-index build | 43 | 166 | 271 |
| **C, closure fills, integration included** | **731** | **2222** | **5196** |
| **B_T2 = estimate total + H + C** | **32837** | **34585** | **37997** |

- C3 layer (the structure's 20% constant, already inside the totals): 10 761 h (r1), 9 765 h (r2); once-scoped layer 840 h both; element-attached layer 23 332 h (r1), 21 349 h (r2).
- The XL leaves' own element-attached effort, should you need it: repeat 1 2 085.0 h over 13 leaves, repeat 2 601.7 h over 3 leaves (RK60 names this base and leaves it uncorrected).
