Cross the product model subtrees named below with the declared technology. Everything you need is in this message; read no files.

**Partial run.** Scope: the subtrees rooted at **N40, N50, N60, N70, N80, N90** of the closed product model `HM61-1` — **36 elements**, listed in INPUT 1 with their parents and coverage. The model root `N00` and every other subtree are outside this batch: do not cross them and do not speculate about them. Per the partial-run rule, once-scoped and per-environment activities are **deferred**, not generated, and per-parent activities apply only to parents inside the batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. **Compact §4 at the orchestrator's instruction: one row per activity — activity id, scope, the element ids receiving an item, the count — with item ids of the form `ACTIVITY@ELEMENT`.** The classification log (§3) and the `no` log (§5) are not compacted: every element with its class, every refusal with its kind and reason.

---

# INPUT 1 — the product model subtrees in scope (from `HM61-1`, `Hotyn-M 2.1`, closed and normalised)

This model keeps coverage in leaves only. **A node (an element with children) has an empty coverage column by rule; its content is its children.** A leaf's declared content is its name together with the obligations it covers. A derived leaf has no requirement coverage: its column holds `trigger: <ids>`, the elements whose existence called for it, and its content is its name read with that trigger. Every element listed here has its parent listed here, except the batch roots whose parent is `N00`. Origin values: posited (skeleton), accreted (added at a requirement), derived (added at completion).

| id | name | parent | origin | coverage |
|---|---|---|---|---|
| N40 | Processing cluster | N00 | posited | — |
| N41 | Cluster management tool | N40 | accreted | — |
| N50 | Storage and records | N00 | posited | — |
| N60 | NOC | N00 | posited | — |
| N70 | User portal | N00 | posited | — |
| N80 | Old system coexistence | N00 | posited | — |
| N90 | System-wide properties | N00 | posited | — |
| L01 | PoP registry: served PoPs and their reach | N90 | accreted | F01,F38 |
| L28 | Windows cluster node host | N40 | accreted | F20,F39 |
| L29 | Queue-length view | N41 | accreted | F21,F34 |
| L30 | Node state view | N41 | accreted | F21,F33 |
| L31 | Node control: take out, put back, redistribute | N41 | accreted | F21 |
| L36 | Fax archive store on Lustre | N50 | accreted | F26 |
| L37 | Working-file area on Lustre | N50 | accreted | F27 |
| L38 | System database schema | N50 | accreted | F28,F29 |
| L40 | Common C#/.NET codebase and shared libraries | N90 | accreted | F30 |
| L41 | NOC console | N60 | accreted | F31,F33,F34 |
| L42 | PoP state view | N60 | accreted | F32 |
| L43 | Portal site and user sign-in | N70 | accreted | F35 |
| L44 | Delivery configuration page | N70 | accreted | F35 |
| L45 | Fax status and history page | N70 | accreted | F35 |
| L46 | Capacity provision for nominal volume | N90 | accreted | F36 |
| L47 | Burst absorption: backlog and admission control | N90 | accreted | F37 |
| L48 | Cluster membership and private-network addressing | N40 | accreted | F39,F44 |
| L49 | CDR writer and store | N50 | accreted | F40 |
| L50 | Billing data writer and store | N50 | accreted | F41 |
| L51 | Old-system exchange interface | N80 | accreted | F42,F43 |
| L52 | Traffic assignment between old and new system | N80 | accreted | F43 |
| D03 | User account and service settings records | N50 | derived | trigger:L43,L05,D01,D02 |
| D04 | PoP status collector | N60 | derived | trigger:L42 |
| D05 | Node and queue state collector | N41 | derived | trigger:L29,L30 |
| D06 | Archive retrieval index by fax identity | N50 | derived | trigger:L36,L45 |
| D07 | Working-file cleanup | N50 | derived | trigger:L37 |
| D09 | Portal password recovery | N70 | derived | trigger:L43 |
| D11 | System event and alarm log | N60 | derived | trigger:L41,L33 |
| D12 | Account data synchronisation with old system | N80 | derived | trigger:D03,L51 |

---

# INPUT 2 — the technology declaration (FaxRxTx, declared 2026-08-22), as the crossing must see it

One entry per dimension of catalogue 1.4. **The activity list is the declaration's, not yours**: an
activity absent here does not exist for this run. Scopes: `once` = one item for the whole model ·
`per element` = one per element of the applicable classes · `per parent` = one per element that has
children (a position, not a class) · `per environment` = one per environment named in the parameters
· `× cycles` = multiplied by the cycle count named in the parameters.

## Construction — `K-BESPOKE` — bespoke web application on a mainstream stack
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| K1 | element design | per element | behaviour, surface, interface, store | how this element is built and what it promises its neighbours |
| K2 | element implementation | per element | behaviour, surface, interface, store | includes the persistence for a `store` and the adapter for an `interface` |
| K3 | statement realisation and evidence | per element | statement | the decision, the configuration that enforces it, and what shows it holds |

No assembly or integration activity, deliberately: integration is accounted for downstream at every aggregation node, and an activity here would be the same work twice.

## Assurance — `A-TB` — test-based assurance
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| A1 | test strategy | once |  | what is tested, at which levels, against what exit criteria |
| A2 | test design | per element | behaviour, surface, interface, store | the cases, not their execution |
| A3 | unit and component test implementation | per element | behaviour, surface, interface, store |  |
| A4 | code review | per element | behaviour, surface, interface, store | verification by reading; belongs to assurance, not to construction |
| A5 | test execution | per parent × cycles |  |  |
| A6 | defect resolution | per parent × cycles |  | fixing and retesting what execution found |
| A7 | automated regression suite | per parent |  |  |
| A8 | test data preparation | per parent |  |  |
| A9 | performance and availability testing | per element | statement elements whose content is a performance, capacity or availability property **and states at least one measurable target** | this is how an NFR statement gets tested rather than merely asserted; a property with no stated target is a crossing filter refusal and an open question for the client, not a test item |
| A10 | interface contract testing | per element | interface | against the external system or a stand-in for it |

## Acceptance — `C-DIRECT` — direct to production, no acceptance stage
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| U1d | production verification checklist | once |  |  |

## Delivery process — `D-TEAM` — one team, planning and reporting ceremonies
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| D1 | mobilisation and set-up | once |  |  |
| D2 | planning and tracking | per parent |  | the subsystem's plan; the project's plan is D1 and D3 |
| D3 | status reporting and client communication | once |  |  |
| D4 | requirement elaboration | per element | any element covering at least one requirement | the business analysis run 18 found had no home anywhere in the model |
| D6 | risk and dependency management | once |  |  |

## Environments — `E-DSP` — dev, stage and production
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| E1 | environment provisioning | per environment |  |  |
| E2 | build and deployment pipeline | once |  |  |
| E3 | promotion procedure, defined and rehearsed | once |  |  |
| E4 | configuration management and version control set-up | once |  |  |
| E6 | production cutover | once |  | run 18 flagged go-live cutover as work nobody could price |
| E7 | hosting set-up: tenancy, capacity, runtime | once |  | the part of demanded work **R02** that survives A1 |

## Data — `G-SEED` — reference and master data seeded, no legacy migration
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| G1 | seed data set specification | per element | store | what must be in it before the system is usable |
| G2 | seed data preparation and load | per element | store |  |
| G3 | load reconciliation | per element | store |  |

## Documentation — `U-OPS-USER` — operational and user documentation
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| O1 | user documentation | per parent | parents whose subtree contains at least one `surface` element |  |
| O2 | operational runbook | once |  |  |
| O3 | support handover pack | once |  | the part of demanded work **R03** that survives A1 |
| O4 | release notes | once |  |  |

## Security and compliance assurance — `SA-NONE`

No activities: this dimension is declared as none.

## Parameters
| parameter | value |
|---|---|
| environments | 3: dev, stage, prod |
| test execution cycles | 2 |
