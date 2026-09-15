Cross the product model subtrees named below with the declared technology. Everything you need is in this message; read no files.

**Partial run.** Scope: the subtrees rooted at **N06, N07, N10** of the closed product model `HM57-1` — **30 elements**, listed in INPUT 1 with their parents and coverage. The model root `N01` and every other subtree are outside this batch: do not cross them and do not speculate about them. Per the partial-run rule, once-scoped and per-environment activities are **deferred**, not generated, and per-parent activities apply only to parents inside the batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. **Compact §4 at the orchestrator's instruction: one row per activity — activity id, scope, the element ids receiving an item, the count — with item ids of the form `ACTIVITY@ELEMENT`.** The classification log (§3) and the `no` log (§5) are not compacted: every element with its class, every refusal with its kind and reason.

---

# INPUT 1 — the product model subtrees in scope (from `HM57-1`, `Hotyn-M 2.1`, closed and normalised)

This model keeps coverage in leaves only. **A node (an element with children) has an empty coverage column by rule; its content is its children.** A leaf's declared content is its name together with the obligations it covers. A derived leaf has no requirement coverage: its column holds `trigger: <ids>`, the elements whose existence called for it, and its content is its name read with that trigger. One derived node (`CN01`) carries a trigger in its column as well; it is a node — its content is its children — and the trigger is not coverage. Every element listed here has its parent listed here, except the batch roots whose parent is `N01`. Origin values: posited (skeleton), accreted (added at a requirement), derived (added at completion).

| id | name | parent | origin | coverage |
|---|---|---|---|---|
| N06 | Identity and access | N01 | posited | — |
| N07 | Record governance | N01 | posited | — |
| N10 | User assistance | N01 | posited | — |
| A007 | Cross-module authorisation service | N06 | accreted | I-6,G-2 |
| A008 | Validation rule engine (entry, import, identifier assignment) | N07 | accreted | I-7,G-12.4,NFR-16 |
| A009 | Validation rule set held as configuration | N07 | accreted | I-7 |
| A013 | User role assignment | N06 | accreted | G-1,G-1.2,G-3.1 |
| A014 | Workflow task assignment (edit and approve responsibilities) | N07 | accreted | G-1,G-1.2,G-3.1 |
| A015 | Company administrator designation per member | N06 | accreted | G-1.1,G-1.2,G-3.1 |
| A016 | Company user administration (add, edit users) | N06 | accreted | G-1.1,NFR-3 |
| A017 | Configurable role catalogue seeded with four roles | N06 | accreted | G-1.3,G-1.4,NFR-3 |
| A018 | Role permission sets (function and data scope per role) | N06 | accreted | G-1.4,G-2 |
| A020 | Record approval workflow engine | N07 | accreted | G-3,G-3.2,P-10.2,L-9.2,NFR-16 |
| A021 | Approval rule configuration per company | N07 | accreted | G-3.1 |
| A023 | Records-awaiting-my-action work list | N07 | accreted | G-3.3 |
| A024 | Password reset initiation (self, company admin, help desk) | N06 | accreted | G-4 |
| A025 | IdM password reset exchange | N06 | accreted | G-4,NFR-3 |
| A026 | Record edit lock | N07 | accreted | G-5 |
| A046 | Application feedback submission to configured address | N10 | accreted | G-9 |
| A047 | Contextual help display | N10 | accreted | G-10,G-10.1 |
| A048 | Industry variants of help content | N10 | accreted | G-10.1 |
| A049 | Help content editor for non-technical staff | N10 | accreted | G-10.2 |
| A050 | Configurable training link set | N10 | accreted | G-11 |
| A146 | Claims-based single sign-on integration | N06 | accreted | NFR-3 |
| A147 | Claims-to-company-user-role mapping | N06 | accreted | NFR-3 |
| A165 | Attribute accuracy verification workflow | N07 | accreted | NFR-16 |
| C01 | X-Customer staff accounts and staff roles | N06 | derived | trigger:A024,A041,A049,A069,A137 |
| C02 | Session management and sign-out | N06 | derived | trigger:A146 |
| C03 | IdM user provisioning and deprovisioning exchange | N06 | derived | trigger:A016,A146 |
| C04 | Record lock expiry and administrative release | N07 | derived | trigger:A026 |

---

# INPUT 2 — the technology declaration (SAS, approved 2026-09-08), as the crossing must see it

One entry per dimension of catalogue 1.4. **The activity list is the declaration's, not yours**: an
activity absent here does not exist for this run. Scopes: `once` = one item for the whole model ·
`per element` = one per element of the applicable classes · `per parent` = one per element that has
children (a position, not a class) · `per environment` = one per environment named in the parameters
· `× cycles` = multiplied by the cycle count named in the parameters.

## Construction — `K-BESPOKE`, bespoke web application on a mainstream stack
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| K1 | element design | per element | behaviour, surface, interface, store | how this element is built and what it promises its neighbours |
| K2 | element implementation | per element | behaviour, surface, interface, store | includes the persistence for a `store` and the adapter for an `interface` |
| K3 | statement realisation and evidence | per element | statement | the decision, the configuration that enforces it, and what shows it holds |

No assembly or integration activity, deliberately: integration is accounted for downstream at every aggregation node, and an activity here would be the same work twice.

## Assurance — `A-TB`, test-based
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| A1 | test strategy | once | | |
| A2 | test design | per element | behaviour, surface, interface, store | the cases, not their execution |
| A3 | unit and component test implementation | per element | behaviour, surface, interface, store | |
| A4 | code review | per element | behaviour, surface, interface, store | verification by reading |
| A5 | test execution | per parent × cycles | | |
| A6 | defect resolution | per parent × cycles | | fixing and retesting what execution found |
| A7 | automated regression suite | per parent | | |
| A8 | test data preparation | per parent | | |
| A9 | performance and availability testing | per element | statement elements whose content is a performance, capacity or availability property **and states at least one measurable target** | a property with no stated target is a filter refusal and an open question for the client, not a test item |
| A10 | interface contract testing | per element | interface | against the external system or a stand-in for it |

## Acceptance — `C-UAT`, staged user acceptance with sign-off
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| U1 | UAT scenario preparation | per parent | parents whose subtree contains at least one `surface` element | |
| U2 | UAT support | per parent × UAT cycles | same | |
| U3 | UAT defect triage and fix | per parent × UAT cycles | same | |
| U4 | acceptance record and sign-off | once | | |

## Delivery process — `D-TEAM`, one team with planning and reporting ceremonies
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| D1 | mobilisation and set-up | once | | |
| D2 | planning and tracking | per parent | | the subsystem's plan |
| D3 | status reporting and client communication | once | | |
| D4 | requirement elaboration | per element | any element covering at least one requirement | |
| D6 | risk and dependency management | once | | |

## Environments — `E-DSP` with four environments
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| E1 | environment provisioning | per environment | | |
| E2 | build and deployment pipeline | once | | |
| E3 | promotion procedure, defined and rehearsed | once | | |
| E4 | configuration management and version control set-up | once | | |
| E6 | production cutover | once | | |
| E7 | hosting set-up: tenancy, capacity, runtime | once | | |

## Data — `G-MIGRATE`, migration from a predecessor system
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| G1m | source profiling | once | | |
| G2m | field mapping specification | per element | store | |
| G3m | extraction and transformation | per element | store | |
| G4m | load and reconciliation | per element | store | |
| G5m | migration rehearsal | once × migration rehearsal cycles | | |

## Documentation — `U-OPS-USER`, operational and user documentation
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| O1 | user documentation | per parent | parents whose subtree contains at least one `surface` element | |
| O2 | operational runbook | once | | |
| O3 | support handover pack | once | | |
| O4 | release notes | once | | |

## Security and compliance assurance — `SA-PENTEST`
| id | activity | scope | applies to | note |
|---|---|---|---|---|
| S1 | security review of the design | once | | |
| S2 | penetration test engagement | once | | |
| S3 | remediation of findings | once | | |

## Parameters
| parameter | value |
|---|---|
| environments | 4: development, test, staging/pre-production, production |
| test execution cycles | 2 |
| UAT cycles | 2 |
| migration rehearsal cycles | 2 |
