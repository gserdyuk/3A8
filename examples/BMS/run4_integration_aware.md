# BMS — Run #4 (experiment): Integration-aware bottom-up

Date: 2026-07-17. A check of the method correction from findings §9: WBS → a tree with aggregation nodes, and at each node an explicit integration item as a % of the sum of the children's component development. The integration rate, by the author's decision: **15–20%** per node.

**A checkable prediction (fixed before recalculation):** the result is noticeably > 486 pd but < 884 pd (calibrated decomposition), because the correction cures one blind spot (internal seams) without touching the others (external icebergs, scope creep, overhead, correlation).

## WBS tree

```
BMS (system)                                 ← aggregation node (top)
├── A. Platform                     56.5 pd  ← node
│   ├── Setup CI/CD/IaC             15.8
│   ├── SSO + roles                 12.7
│   ├── Data model/DB/audit         15.3
│   └── Notifications (email+SMS)    12.7
├── B. External integrations        84.8 pd  ← node
│   ├── CTC (sync, merge, alerts)   26.7
│   ├── UPSA                         8.7
│   ├── Hotel aggregator            36.7
│   └── Uber                        12.7
├── C. Booking core                 77.9 pd  ← node
│   ├── Search & prioritization     31.7
│   ├── Workflow engine             23.0
│   ├── Manual booking               8.2
│   ├── Hotel change / changes UI    6.3
│   └── Combining transport          8.7
├── D. Portals                      63.7 pd  ← node
│   ├── Employees                   18.7
│   ├── Administration              29.2
│   └── Suppliers                   15.8
└── E. Reporting                    15.8 pd  (a single leaf — no node)
Component development: 298.7 pd
```

Cross-cutting work (outside the component tree, the integration % does not apply to it): discovery 25.8, architecture 15.8, UI/UX 25.8, NFR 14.8, security 8.7, **QA 29.2 (trimmed from 40.8)**, UAT 16.7, deployment 8.2, PM 30.8 → **175.8 pd**.

**Against double counting:** item #23 "QA: system and integration testing" (25/40/60, E=40.8) is trimmed to system regression/E2E (18/28/45, E=29.2) — the integration testing of the seams now lives in the nodes' explicit integration items (−11.6 pd from QA).

## The nodes' integration items

A node's integration = p × (sum of the children's contents), p = 15–20%. The top node is computed from the components + intra-node integration (already-assembled subsystems are joined).

| Node | What the seams are | p=15% | p=20% |
|---|---|---:|---:|
| A internal | notifications↔events, SSO↔all, audit↔all | 8.5 | 11.3 |
| B internal | a common adapter frame, unification of errors/retries | 12.7 | 17.0 |
| C internal | search↔workflow↔data (the densest connectivity) | 11.7 | 15.6 |
| D internal | a common design system, shared portal components | 9.6 | 12.7 |
| **Top: system assembly** | core↔integrations (search across external systems, CTC sync moves the workflow), portals↔core, notifications↔statuses, reporting↔data of all subsystems | 51.2 | 71.1 |
| **Total integration** | | **93.6** | **127.6** |

An honest caveat: a single p per node is crude; it is more correct to derive p from the actual number/type of seams on the diagram (connectivity is lower inside B, higher inside C). Left for the next iteration — the 15–20% range is enough to test the prediction.

## Result

| | pd |
|---|---:|
| Components | 298.7 |
| Cross-cutting (QA trimmed) | 175.8 |
| Integration (15–20%) | 93.6–127.6 |
| **Total** | **568–602** (center ~585) |

## Check against the prediction — it held

- **585 > 486** (+20%): the internal seams got lines and a cost.
- **585 < 884**: the gap with calibrated decomposition remained — 300 pd, and this is exactly the spots the correction did not promise to cure: scope creep (+114 in Step B), coordination/overhead (+189), external icebergs (+61 — the real quality of others' APIs, not our seams), PM/UAT (+34).
- An interesting cross-check with Step B: there the "integration" part of the gap was estimated from above (from reference class) at +61 pd for external icebergs only; integration-aware gives +82…+116 net (93.6–127.6 minus 11.6 from QA) for the internal edges — **these are different items**; in Step B the internal assembly sat inside the coordination multiplier. I.e. the correction does not "catch up" to reference class but moves part of the unexplained multiplier into an explainable structural item — exactly what it was designed for.

## Conclusion for the methodology

Integration-aware bottom-up is accepted as a refinement of the decomposition method: (1) the WBS is a tree, not a list; (2) each aggregation node carries an integration item; (3) the node's rate is a transferable parameter (for now 15–20% from base rates, in Phase 2 — measure on history; the next iteration — derive it from the actual graph of seams instead of a single p); (4) items of the "integration testing" kind must then be trimmed — otherwise double counting.
