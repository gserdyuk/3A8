Cross the product model subtrees named below with the declared technology. Everything you need is in this message; read no files.

**Partial run.** Scope: the subtrees rooted at **N02** of the closed product model `HM57-1` — **35 elements**, listed in INPUT 1 with their parents and coverage. The model root `N01` and every other subtree are outside this batch: do not cross them and do not speculate about them. Per the partial-run rule, once-scoped and per-environment activities are **deferred**, not generated, and per-parent activities apply only to parents inside the batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. **Compact §4 at the orchestrator's instruction: one row per activity — activity id, scope, the element ids receiving an item, the count — with item ids of the form `ACTIVITY@ELEMENT`.** The classification log (§3) and the `no` log (§5) are not compacted: every element with its class, every refusal with its kind and reason.

---

# INPUT 1 — the product model subtrees in scope (from `HM57-1`, `Hotyn-M 2.1`, closed and normalised)

This model keeps coverage in leaves only. **A node (an element with children) has an empty coverage column by rule; its content is its children.** A leaf's declared content is its name together with the obligations it covers. A derived leaf has no requirement coverage: its column holds `trigger: <ids>`, the elements whose existence called for it, and its content is its name read with that trigger. One derived node (`CN01`) carries a trigger in its column as well; it is a node — its content is its children — and the trigger is not coverage. Every element listed here has its parent listed here, except the batch roots whose parent is `N01`. Origin values: posited (skeleton), accreted (added at a requirement), derived (added at completion).

| id | name | parent | origin | coverage |
|---|---|---|---|---|
| N02 | Platform architecture | N01 | posited | — |
| N03 | Data stores | N02 | posited | — |
| N04 | Service and API layer | N02 | posited | — |
| N05 | Web client | N02 | posited | — |
| CN01 | Background processing | N02 | derived | trigger:A032,A045,A051,A133 |
| A001 | Shared domain data model (companies, users, prefixes, records, identifiers) | N03 | accreted | I-2,I-6,NFR-2,I-1 |
| A002 | Unified application shell with Product, Location, Access Data areas | N05 | accreted | I-2,I-6,D-7,NFR-7,I-1 |
| A005 | Architecture design: enterprise alignment, maintainability, growth scalability | N02 | accreted | I-4 |
| A006 | Future-expansion design provisions (further data types, field-level sharing) | N02 | accreted | I-5 |
| A012 | X-Customer reference data set (prefix registry, controlled groups) | N03 | accreted | I-11,I-1 |
| A019 | Role-driven UI composition | N05 | accreted | G-2 |
| A034 | 3scale analytics API client | N04 | accreted | G-7.2 |
| A059 | Record import and export API | N04 | accreted | G-12.1,P-19,L-15,NFR-4 |
| A076 | Industry configuration store | N03 | accreted | P-1,L-1 |
| A089 | Binary asset store for images | N03 | accreted | P-6 |
| A140 | Access Data REST API | N04 | accreted | D-7,NFR-4 |
| A141 | Member API registration in 3scale | N04 | accreted | D-7,NFR-4 |
| A143 | Non-transactional read store | N03 | accreted | NFR-2 |
| A144 | Near-real-time feed to read store | N03 | accreted | NFR-2 |
| A145 | Data volume scalability design | N02 | accreted | NFR-2 |
| A148 | Internal REST service layer | N04 | accreted | NFR-4 |
| A149 | Technical standards conformance design | N02 | accreted | NFR-5 |
| A150 | Standards deviation impact analysis procedure | N02 | accreted | NFR-5 |
| A151 | Cloud-readiness design provisions | N02 | accreted | NFR-6 |
| A152 | Standard web framework foundation (no client install) | N05 | accreted | NFR-7,NFR-13,NFR-21 |
| A153 | User volume and concurrency capacity design | N02 | accreted | NFR-7 |
| A163 | Cross-browser compatibility | N05 | accreted | NFR-13 |
| A171 | WCAG 2.0 Level A conformance | N05 | accreted | NFR-21 |
| C05 | Background job scheduler | CN01 | derived | trigger:A032,A045,A104 |
| C08 | Asynchronous import job queue with progress status | CN01 | derived | trigger:A051,A145 |
| C10 | Industry configuration maintenance screens | N03 | derived | trigger:A076 |
| C12 | Search index maintenance from read-store feed | CN01 | derived | trigger:A133,A144 |
| C13 | User-facing error handling | N05 | derived | trigger:A002 |
| C14 | API caller identity mapping from 3scale credentials | N04 | derived | trigger:A140,A059,A007 |
| C16 | Job run log and retry | CN01 | derived | trigger:C05,C08 |

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
