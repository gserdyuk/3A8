# Rate table v0.1 — approved 2026-08-22; unit adjudicated

> **Unit, fixed by the author 2026-08-25.** One person-day = **8 net hours of work on the task**.
> That is what §2 and §5 below have said since the table was written, and what three independent
> `Hotyn-K` runs state as their own convention. **No value changes.**
>
> **The relabelling of 2026-08-22 — "one person-day = one assigned working day" — is withdrawn.** It
> was a change of label with no value re-derived, and it silently cut every row by a third. The party
> that wrote the values declined to certify it ("accepted-on-statement, not as checked"). Separately
> measured and *not* part of this unit: a real working day of this team grade yields **5–6 net task
> hours**; converting the table's effort into calendar or into staffed headcount uses that figure, and
> it belongs to the estimator, never to a row.
>
> **Status: this table is a fixed set of constants.** It is one sample from `Hotyn-K 1.0` × Fable 5,
> 2026-08-21, and repeat sampling of that role has since been measured at ×1.38–×1.50 — that figure is
> **provenance, not uncertainty of any estimate made from these constants**, because a constant does
> not vary between runs. The table is not re-sampled. It changes only by calibration against
> documented outcomes, producing v0.2 with the evidence recorded beside each changed value.
>
> Kept deliberately un-averaged: every priced run so far (BMS 23–25, FaxRxTx 29–31) used these
> constants, and replacing them with an averaged table would make all of it incomparable.

**Produced 2026-08-21 by `Hotyn-K 1.0` × Fable 5** (`.claude/agents/rate-table-author.md`; the
model half of the stamp is orchestrator-recorded — the launch carried no model override, so the role
inherited the session model, Fable 5; noted 2026-08-22 after the author caught the missing stamp).
Gap-blind by construction: its input was a sanitized extract of catalogue 1.2 — activities, classes,
sizing thresholds, scopes — with **no run references, no project names, no declared/not-declared
marks** — plus one line of team grade. `tool_uses: 0`; contamination check clean. Transcribed
verbatim from the agent's reply (the harness does not persist subagent output; this file is the
durable record). Per the σ_model discipline, any future recalibration or re-draft states its model;
values here are external norms mediated by one model and the stamp is what makes that auditable.

**Status: draft.** On the author's approval this becomes the pinned input of `Hotyn-D 2.0`
(`docs/proposal_rate_card.md`). Known holes at transcription: **three refused XL cells** (catalogue
split needed) and **four driver findings** — §4 below. Calibration rule: a value change produces
v0.2 with its evidence recorded beside it, never an in-place edit, and never while looking at a gap
the edit would explain.

---

**Engine: `Hotyn-K 1.0`** — rate table author. Deliverable follows; no files read, no files written.

## 1. Contamination check

Input contained catalogue structure (v1.2), size-class definitions, and the assumed team grade only
— no effort figure from any run or estimate, no project total, no ΣE, no budget, no duration.
**Clean; proceeding.**

## 2. The table

Units: person-days (pd), 1 pd = 8 h net. Team assumed throughout: competent engineers, senior/middle
mix, enterprise delivery. **Every row carries the stamp: `external norm, uncalibrated v0.1`.** Rows
marked `× cycles` price exactly one cycle. Aggregates never receive per-element rows.

### Dimension 1 — construction

#### K-BESPOKE — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K1 | behaviour, surface, store | S | 0.25 | 0.5 | 1 | single-unit design note plus neighbour contract; sub-day norm for a senior profile |
| K1 | behaviour, surface, store | M | 0.5 | 1 | 2 | 2–3-unit design fits one coherent sketch and contract |
| K1 | behaviour, surface, store | L | 1 | 2 | 3.5 | multi-unit design with state and flow decisions |
| K1 | behaviour, surface, store | XL | 2 | 3.5 | 6 | 7+-unit design: flows, states, error paths need working through |
| K1 | interface | S | 0.5 | 1 | 2 | one-operation contract where an external party's semantics must be pinned |
| K1 | interface | M | 1 | 2 | 4 | 2–4 operations incl. a protocol/auth concern |
| K1 | interface | L | 2 | 3.5 | 6 | 5–8 operations; error and versioning semantics dominate |
| K1 | interface | XL | 3 | 5 | 9 | ≥9 operations; negotiation and versioning decisions with the outside party |
| K2 | behaviour, surface | S | 0.5 | 1 | 2 | one action or one screen on a mainstream stack with plumbing in place |
| K2 | behaviour, surface | M | 1 | 2.5 | 5 | roughly a day per action/task with shared plumbing |
| K2 | behaviour, surface | L | 2.5 | 5 | 9 | 4–6 units at the same per-unit norm |
| K2 | behaviour, surface | XL | 5 | 8 | 14 | 7+ units; first unit dear, the rest near a day each |
| K2 | interface | S | 1 | 2 | 4 | one-operation adapter incl. auth, mapping, error handling |
| K2 | interface | M | 2 | 3.5 | 7 | 2–4 operations on a shared adapter core |
| K2 | interface | L | 3 | 6 | 10 | 5–8 operations; external-system quirks surface here |
| K2 | interface | XL | 5 | 9 | 15 | ≥9 operations; sub-day per op after the adapter core stands |
| K2 | store | S | 0.5 | 1 | 2 | one entity: schema, persistence, access layer at ORM norm |
| K2 | store | M | 1 | 2 | 3.5 | 2–3 entities with relations |
| K2 | store | L | 2 | 4 | 7 | 4–6 entities; lifecycle and constraint logic grows |
| K2 | store | XL | 3.5 | 6.5 | 11 | ≥7 entities; sub-day per entity on scaffolding |
| K3 | statement-compliance | S | 0.25 | 0.5 | 1.5 | one configuration decision enforced on one component, evidence captured |
| K3 | statement-compliance | M | 0.5 | 1.5 | 3 | same decision swept across 2–4 components |
| K3 | statement-compliance | L | 1 | 2.5 | 5 | 5–8 components plus a consolidated evidence pack |
| K3 | statement-compliance | XL | 2 | 4 | 8 | ≥9 components; sweep and evidence, no run-time mechanics |
| K3 | statement-behavioural | S | 1 | 2 | 4 | run-time mechanism in one component plus demonstration it holds |
| K3 | statement-behavioural | M | 2 | 4 | 8 | mechanism coordinated across 2–4 components |
| K3 | statement-behavioural | L | 3 | 6 | 12 | 5–8 components; failure-path work dominates |
| K3 | statement-behavioural | XL | — | — | — | **refused — see findings (M > 10)** |

Integration deliberately absent as an activity — carried as constant C3, restated in section 3.

#### K-PACKAGE-CONFIG — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K1p | behaviour, surface, store | S | 0.1 | 0.25 | 0.75 | capability-matrix check for one unit against a known package |
| K1p | behaviour, surface, store | M | 0.25 | 0.5 | 1 | 2–3 units assessed in one sitting |
| K1p | behaviour, surface, store | L | 0.5 | 1 | 2 | multi-unit fit/gap decision with write-up |
| K1p | behaviour, surface, store | XL | 1 | 1.5 | 3 | 7+ units; gaps need structured disposition |
| K2p | behaviour, surface, store (assessed configure) | S | 0.25 | 0.5 | 1.5 | declared package configuration, no code; quirks inflate P |
| K2p | behaviour, surface, store (assessed configure) | M | 0.5 | 1.5 | 3 | 2–3 units of vendor-pattern configuration |
| K2p | behaviour, surface, store (assessed configure) | L | 1 | 3 | 6 | 4–6 units; configuration interactions appear |
| K2p | behaviour, surface, store (assessed configure) | XL | 2 | 5 | 9 | 7+ units; still cheaper than build, dearer to untangle |
| K3p | behaviour, surface, store (assessed extend) | S | 1 | 2 | 4 | custom code inside the package framework, upgrade-safe norm |
| K3p | behaviour, surface, store (assessed extend) | M | 2 | 4 | 8 | 2–3 units; framework constraints tax each unit |
| K3p | behaviour, surface, store (assessed extend) | L | 4 | 7 | 12 | 4–6 units at ~1.5 pd per unit |
| K3p | behaviour, surface, store (assessed extend) | XL | — | — | — | **refused — see findings (M > 10)** |
| K5p | statement-compliance | S | 0.25 | 0.5 | 1.5 | vendor compliance switch set and evidenced |
| K5p | statement-compliance | M | 0.5 | 1.5 | 3 | 2–4 components via vendor settings |
| K5p | statement-compliance | L | 1 | 2.5 | 5 | 5–8 components, consolidated evidence |
| K5p | statement-compliance | XL | 1.5 | 3.5 | 7 | ≥9 components; vendor tooling caps the sweep cost |
| K5p | statement-behavioural | S | 0.5 | 1.5 | 3 | vendor mechanism configured and demonstrated on one component |
| K5p | statement-behavioural | M | 1.5 | 3 | 6 | 2–4 components on vendor HA/performance features |
| K5p | statement-behavioural | L | 2.5 | 5 | 10 | 5–8 components; vendor features carry the mechanics |
| K5p | statement-behavioural | XL | 4 | 8 | 14 | ≥9 components; product-provided mechanism keeps M under bespoke |

#### K-PACKAGE-CONFIG — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K4p | once (model bracket) | S | 2 | 4 | 8 | enterprise package install plus baseline, small scope |
| K4p | once (model bracket) | M | 3 | 6 | 12 | mid-size baseline: modules, roles, base parameters |
| K4p | once (model bracket) | L | 5 | 9 | 16 | large baseline across many modules |

### Dimension 2 — assurance

#### A-TB — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| A2 | behaviour, surface, interface, store | S | 0.25 | 0.5 | 1 | case design incl. negatives for one unit |
| A2 | behaviour, surface, interface, store | M | 0.5 | 1 | 2 | case set for 2–4 units, shared fixtures |
| A2 | behaviour, surface, interface, store | L | 1 | 2 | 3.5 | multi-unit case matrix |
| A2 | behaviour, surface, interface, store | XL | 1.5 | 3 | 5 | 7+ units; combinatorics pruned by judgement |
| A3 | behaviour, surface, interface, store | S | 0.5 | 1 | 2 | typically under a day per case, a handful of cases per unit |
| A3 | behaviour, surface, interface, store | M | 1 | 2 | 4 | same norm over 2–4 units |
| A3 | behaviour, surface, interface, store | L | 2 | 3.5 | 6 | shared harness amortises across units |
| A3 | behaviour, surface, interface, store | XL | 3 | 5.5 | 9 | 7+ units on a standing harness |
| A4 | behaviour, surface, interface, store | S | 0.1 | 0.25 | 0.5 | review of a single-unit change incl. one rework loop — **at 0.25 floor** |
| A4 | behaviour, surface, interface, store | M | 0.25 | 0.5 | 1 | half-day review norm for a small element |
| A4 | behaviour, surface, interface, store | L | 0.5 | 1 | 2 | larger diff, two passes |
| A4 | behaviour, surface, interface, store | XL | 0.75 | 1.5 | 3 | big element reviewed in instalments |
| A9 | statement-behavioural (measurable targets) | S | 1 | 2 | 4 | script, load run, analysis for one measurable target |
| A9 | statement-behavioural (measurable targets) | M | 2 | 3.5 | 7 | 2–3 targets sharing a test rig |
| A9 | statement-behavioural (measurable targets) | L | 3 | 5.5 | 10 | 4–6 targets; tuning loops likely |
| A9 | statement-behavioural (measurable targets) | XL | 4 | 8 | 14 | ≥7 targets; rig plus repeated runs |
| A10 | interface | S | 0.5 | 1 | 2.5 | contract tests against a stand-in; stand-in set-up dominates |
| A10 | interface | M | 1 | 2 | 4 | 2–4 operations on one stand-in |
| A10 | interface | L | 2 | 3.5 | 7 | 5–8 operations; external party availability is the risk |
| A10 | interface | XL | 3 | 5 | 10 | ≥9 operations; negotiation of test windows inflates P |

#### A-TB — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| A1 | once (model bracket) | S | 1 | 2 | 4 | strategy note for a small model |
| A1 | once (model bracket) | M | 2 | 3.5 | 6 | strategy incl. environments, data, automation stance |
| A1 | once (model bracket) | L | 3 | 5 | 9 | large-model strategy with per-area treatment |
| A5 | per parent, × cycles | S | 0.5 | 1 | 2 | one execution pass over a ≤3-leaf subtree |
| A5 | per parent, × cycles | M | 1 | 2 | 4 | one pass, 4–8 leaves |
| A5 | per parent, × cycles | L | 2 | 3.5 | 6 | one pass, 9–14 leaves |
| A5 | per parent, × cycles | XL | 3 | 5 | 9 | one pass, ≥15 leaves |
| A6 | per parent, × cycles | S | 0.5 | 1.5 | 4 | fix-and-retest of one pass's findings; defect count is the tail |
| A6 | per parent, × cycles | M | 1 | 3 | 7 | typical defect load of a mid subtree pass |
| A6 | per parent, × cycles | L | 2 | 5 | 10 | larger subtree, one pass's load |
| A6 | per parent, × cycles | XL | 3 | 7 | 14 | ≥15 leaves; P carries the bad-pass case |
| A7 | per parent | S | 1 | 2 | 4 | automated regression over core paths of a small subtree |
| A7 | per parent | M | 2 | 4 | 7 | suite over 4–8 leaves incl. CI wiring |
| A7 | per parent | L | 3 | 6 | 10 | 9–14 leaves; suite maintenance seed included |
| A7 | per parent | XL | 4 | 8 | 14 | ≥15 leaves; selective depth, judgement-pruned |
| A8 | per parent (store+interface in subtree) | S | 0.25 | 0.5 | 1.5 | data for at most one store/interface |
| A8 | per parent (store+interface in subtree) | M | 0.5 | 1.5 | 3 | 2–3 data-bearing elements |
| A8 | per parent (store+interface in subtree) | L | 1 | 2.5 | 5 | 4–6 data-bearing elements, cross-consistent sets |
| A8 | per parent (store+interface in subtree) | XL | 2 | 4 | 8 | ≥7 data-bearing elements |

#### A-FV — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| F1 | behaviour, interface, store | S | 0.5 | 1 | 2.5 | formalising one unit's pre/post-conditions and invariants |
| F1 | behaviour, interface, store | M | 1 | 2.5 | 5 | 2–4 units in one specification module |
| F1 | behaviour, interface, store | L | 2 | 4.5 | 8 | multi-unit specification with interaction invariants |
| F1 | behaviour, interface, store | XL | 3.5 | 7 | 12 | 7+/9+ units; state space needs structuring first |
| F2 | behaviour, interface, store | S | 0.25 | 0.75 | 1.5 | obligation derivation, semi-mechanical with tooling |
| F2 | behaviour, interface, store | M | 0.5 | 1.5 | 3 | obligations across 2–4 units |
| F2 | behaviour, interface, store | L | 1 | 2.5 | 5 | larger obligation set, manual triage |
| F2 | behaviour, interface, store | XL | 1.5 | 4 | 7 | XL element's obligation set with pruning |
| F3 | behaviour, interface, store | S | 1 | 2 | 5 | interactive proof plus checker run for one unit |
| F3 | behaviour, interface, store | M | 2 | 4 | 9 | ~2 pd per proven unit, some obligations resist |
| F3 | behaviour, interface, store | L | 3.5 | 7.5 | 14 | 4–6/5–8 units; a stuck proof carries the P |
| F3 | behaviour, interface, store | XL | — | — | — | **refused — see findings (M > 10)** |
| F4 | behaviour, interface, store, surface | S | 0.25 | 0.5 | 1 | peer review of a one-unit specification |
| F4 | behaviour, interface, store, surface | M | 0.5 | 1 | 2 | review of a 2–4-unit specification |
| F4 | behaviour, interface, store, surface | L | 1 | 1.5 | 3 | larger spec, two reviewers' passes folded in |
| F4 | behaviour, interface, store, surface | XL | 1.5 | 2.5 | 4 | XL spec reviewed in instalments |
| F6 | surface | S | 0.25 | 0.5 | 1 | structured inspection of a one-task surface |
| F6 | surface | M | 0.5 | 1 | 2 | inspection across 2–3 tasks |
| F6 | surface | L | 1 | 2 | 3.5 | 4–6 tasks with checklist evidence |
| F6 | surface | XL | 1.5 | 3 | 5 | ≥7 tasks |

#### A-FV — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| F5 | once (model bracket) | S | 1 | 2 | 4 | verification report over a small model |
| F5 | once (model bracket) | M | 2 | 3.5 | 6 | consolidation of mid-size proof results |
| F5 | once (model bracket) | L | 3 | 5 | 8 | large-model report with residual-risk register |

### Dimension 3 — acceptance

#### C-UAT — position-derived (sizing: surface count in subtree)

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| U1 | per parent (surfaces in subtree) | S | 0.5 | 1 | 2 | client workshop plus scenario write-up, one surface |
| U1 | per parent (surfaces in subtree) | M | 1 | 2 | 4 | scenarios across 2–3 surfaces |
| U1 | per parent (surfaces in subtree) | L | 2 | 3.5 | 6 | 4–6 surfaces; client iteration rounds |
| U1 | per parent (surfaces in subtree) | XL | 3 | 5 | 9 | ≥7 surfaces |
| U2 | per parent, × cycles | S | 0.5 | 1 | 2.5 | supplier side of one client-run cycle, one surface |
| U2 | per parent, × cycles | M | 1 | 2 | 4 | one cycle, 2–3 surfaces |
| U2 | per parent, × cycles | L | 1.5 | 3 | 6 | one cycle, 4–6 surfaces |
| U2 | per parent, × cycles | XL | 2.5 | 4.5 | 8 | one cycle, ≥7 surfaces |
| U3 | per parent, × cycles | S | 0.5 | 1.5 | 4 | triage and fix of one cycle's findings; volume is the tail |
| U3 | per parent, × cycles | M | 1 | 2.5 | 6 | one cycle's findings over 2–3 surfaces |
| U3 | per parent, × cycles | L | 1.5 | 4 | 8 | one cycle's findings over 4–6 surfaces |
| U3 | per parent, × cycles | XL | 2.5 | 6 | 12 | one cycle's findings over ≥7 surfaces |
| U4 | once (model bracket) | S | 0.5 | 1 | 2 | record assembly and sign-off shepherding |
| U4 | once (model bracket) | M | 1 | 1.5 | 3 | more parties on the record |
| U4 | once (model bracket) | L | 1 | 2 | 4 | large model, multi-stakeholder sign-off |

#### C-DIRECT — single-size

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| U1d | once | single | 0.5 | 1 | 2 | production verification checklist written and run once |

### Dimension 4 — delivery process

#### D-TEAM

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| D1 | once (model bracket) | S | 1 | 2 | 4 | team, tooling, working-agreement stand-up |
| D1 | once (model bracket) | M | 2 | 4 | 7 | mid-size engagement mobilisation |
| D1 | once (model bracket) | L | 3 | 6 | 10 | large engagement, more roles to seat |
| D2 | per parent (subtree leaves) | S | 0.5 | 1 | 2 | subsystem plan and its upkeep across the build |
| D2 | per parent (subtree leaves) | M | 1 | 2 | 4 | 4–8 leaves tracked to done |
| D2 | per parent (subtree leaves) | L | 2 | 3.5 | 6 | 9–14 leaves, replanning included |
| D2 | per parent (subtree leaves) | XL | 3 | 5 | 8 | ≥15 leaves |
| D3 | once (model bracket) | S | 1 | 2 | 4 | cadence reporting over a short engagement |
| D3 | once (model bracket) | M | 2 | 4 | 8 | bracket proxies duration — see driver finding |
| D3 | once (model bracket) | L | 4 | 8 | 14 | long engagement's reporting stream, proxy driver |
| D4 | per covering element (requirement ids) | S | 0.25 | 0.5 | 1 | clarification loop for one requirement id |
| D4 | per covering element (requirement ids) | M | 0.5 | 1 | 2 | 2–3 ids elaborated together |
| D4 | per covering element (requirement ids) | L | 1 | 2 | 4 | 4–6 ids; conflicts need resolving |
| D4 | per covering element (requirement ids) | XL | 1.5 | 3 | 6 | ≥7 ids on one element |
| D6 | once (model bracket) | S | 0.5 | 1 | 2 | register upkeep and escalations, small engagement |
| D6 | once (model bracket) | M | 1 | 2.5 | 5 | bracket proxies duration — see driver finding |
| D6 | once (model bracket) | L | 2 | 4 | 8 | long engagement's risk stream, proxy driver |

#### D-DISTRIBUTED (two sites, formal hand-offs; cross-site load lives in D7)

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| D1 | once (model bracket) | S | 1.5 | 3 | 5 | two sites mobilised plus hand-off protocol defined |
| D1 | once (model bracket) | M | 3 | 5.5 | 9 | mid engagement, two-site set-up |
| D1 | once (model bracket) | L | 4 | 8 | 13 | large engagement, two-site set-up |
| D2 | per parent (subtree leaves) | S | 0.5 | 1 | 2 | as one-team planning; cross-site load carried by D7 |
| D2 | per parent (subtree leaves) | M | 1 | 2 | 4 | as one-team planning |
| D2 | per parent (subtree leaves) | L | 2 | 3.5 | 6 | as one-team planning |
| D2 | per parent (subtree leaves) | XL | 3 | 5 | 8 | as one-team planning |
| D3 | once (model bracket) | S | 1 | 2 | 4 | client-facing stream is site-independent |
| D3 | once (model bracket) | M | 2 | 4 | 8 | as one-team; proxy driver, see finding |
| D3 | once (model bracket) | L | 4 | 8 | 14 | as one-team; proxy driver |
| D4 | per covering element (requirement ids) | S | 0.25 | 0.5 | 1 | elaboration is site-independent |
| D4 | per covering element (requirement ids) | M | 0.5 | 1 | 2 | as one-team |
| D4 | per covering element (requirement ids) | L | 1 | 2 | 4 | as one-team |
| D4 | per covering element (requirement ids) | XL | 1.5 | 3 | 6 | as one-team |
| D6 | once (model bracket) | S | 0.5 | 1 | 2 | cross-site dependency load carried by D7 |
| D6 | once (model bracket) | M | 1 | 2.5 | 5 | as one-team |
| D6 | once (model bracket) | L | 2 | 4 | 8 | as one-team |
| D7 | per parent (subtree leaves) | S | 0.5 | 1 | 2.5 | hand-off preparation and joint sessions for a small subtree |
| D7 | per parent (subtree leaves) | M | 1 | 2.5 | 5 | seam rework is the recurring cost |
| D7 | per parent (subtree leaves) | L | 2 | 4 | 8 | 9–14 leaves crossing the seam |
| D7 | per parent (subtree leaves) | XL | 3 | 6 | 11 | ≥15 leaves; misunderstandings scale with hand-offs |

### Dimension 5 — environments

#### E-DSP

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| E1 | per environment | dev = S | 0.5 | 1 | 2.5 | scripted provisioning, dev-grade |
| E1 | per environment | stage = M | 1 | 2 | 4 | prod-like configuration, test hooks |
| E1 | per environment | prod = L | 2 | 3.5 | 7 | hardening, access control, monitoring hooks |
| E2 | once (model bracket) | S | 1 | 2 | 4 | CI/CD across three targets, small system |
| E2 | once (model bracket) | M | 2 | 3.5 | 7 | more build artefacts, same pipeline pattern |
| E2 | once (model bracket) | L | 3 | 5.5 | 10 | many components through one pipeline family |
| E3 | once (environment count) | S (1 env) | 0.1 | 0.25 | 0.5 | collapses to a release checklist — **at floor; degenerate, see findings** |
| E3 | once (environment count) | M (2 envs) | 0.5 | 1 | 2 | one promotion boundary defined and rehearsed |
| E3 | once (environment count) | L (≥3 envs) | 1 | 2 | 4 | full path incl. rollback rehearsed |
| E4 | once (model bracket) | S | 0.5 | 1 | 2 | repos, branching, config store conventions |
| E4 | once (model bracket) | M | 1 | 1.5 | 3 | multiple repos/config surfaces |
| E4 | once (model bracket) | L | 1.5 | 2.5 | 5 | large component set under management |
| E6 | once (model bracket) | S | 1 | 2 | 4 | cutover plan plus the event itself, small system |
| E6 | once (model bracket) | M | 2 | 3.5 | 7 | coordinated cutover with fallback |
| E6 | once (model bracket) | L | 3 | 5 | 10 | large-system cutover; the long night sits in P |
| E7 | once (model bracket) | S | 1 | 2 | 4 | tenancy, capacity, runtime services, small footprint |
| E7 | once (model bracket) | M | 2 | 3.5 | 7 | mid footprint with capacity sizing |
| E7 | once (model bracket) | L | 3 | 5.5 | 10 | large footprint, enterprise hosting process |

#### E-SINGLE

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| E1 | once | S (fixed) | 0.5 | 1 | 2.5 | one dev-grade environment |
| E2 | once (model bracket) | S | 0.5 | 1.5 | 3 | single-target pipeline, small system |
| E2 | once (model bracket) | M | 1 | 2.5 | 5 | single target, more artefacts |
| E2 | once (model bracket) | L | 2 | 4 | 7 | single target, many components |

### Dimension 6 — data

#### G-SEED — per store element (entity kinds needing pre-load)

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| G1 | store | S | 0.25 | 0.5 | 1 | which records, sources, ownership for one entity kind |
| G1 | store | M | 0.5 | 1 | 2 | 2–3 entity kinds specified |
| G1 | store | L | 1 | 2 | 3.5 | 4–6 kinds; source negotiation |
| G1 | store | XL | 1.5 | 3 | 5 | ≥7 kinds |
| G2 | store | S | 0.25 | 0.5 | 1.5 | collect, cleanse, load one kind |
| G2 | store | M | 0.5 | 1.5 | 3 | 2–3 kinds; cleansing is the variable |
| G2 | store | L | 1 | 2.5 | 5 | 4–6 kinds |
| G2 | store | XL | 2 | 4 | 7 | ≥7 kinds |
| G3 | store | S | 0.1 | 0.25 | 0.5 | counts, spot checks, written note — **at 0.25 floor** |
| G3 | store | M | 0.25 | 0.5 | 1 | reconciliation across 2–3 kinds |
| G3 | store | L | 0.5 | 1 | 2 | 4–6 kinds cross-checked |
| G3 | store | XL | 1 | 1.5 | 3 | ≥7 kinds |

#### G-MIGRATE

| id | position / class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| G1m | once (model bracket) | S | 1 | 2 | 4 | profiling the predecessor's actual data quality |
| G1m | once (model bracket) | M | 2 | 4 | 8 | mid-size legacy source, sampling and anomaly log |
| G1m | once (model bracket) | L | 3 | 6 | 12 | large source; surprises live in P |
| G2m | store (entity kinds) | S | 0.5 | 1 | 2.5 | field-level mapping for one kind incl. rules for dirt |
| G2m | store (entity kinds) | M | 1 | 2.5 | 5 | 2–3 kinds mapped |
| G2m | store (entity kinds) | L | 2 | 4 | 8 | 4–6 kinds; transformation rules multiply |
| G2m | store (entity kinds) | XL | 3 | 6 | 11 | ≥7 kinds |
| G3m | store (entity kinds) | S | 1 | 2 | 4 | ETL build for one kind against legacy quirks |
| G3m | store (entity kinds) | M | 2 | 4 | 8 | 2–3 kinds on a shared ETL frame |
| G3m | store (entity kinds) | L | 3 | 6.5 | 12 | 4–6 kinds; quirk handling dominates |
| G3m | store (entity kinds) | XL | 4 | 9 | 16 | ≥7 kinds; just under a split-worthy load |
| G4m | store (entity kinds) | S | 0.5 | 1 | 2.5 | load run plus reconciliation report, one kind |
| G4m | store (entity kinds) | M | 1 | 2 | 4 | 2–3 kinds loaded and reconciled |
| G4m | store (entity kinds) | L | 1.5 | 3.5 | 7 | 4–6 kinds |
| G4m | store (entity kinds) | XL | 2.5 | 5 | 10 | ≥7 kinds |
| G5m | once (model bracket), × cycles | S | 1 | 2 | 4 | one full rehearsal pass, timing, issue log |
| G5m | once (model bracket), × cycles | M | 2 | 3.5 | 7 | one rehearsal, mid volume |
| G5m | once (model bracket), × cycles | L | 3 | 5.5 | 10 | one rehearsal, large volume window |

### Dimension 7 — documentation

#### U-OPS-USER

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| O1 | per parent (surfaces in subtree) | S | 0.5 | 1 | 2 | user guide for one surface |
| O1 | per parent (surfaces in subtree) | M | 1 | 2 | 4 | guide across 2–3 surfaces |
| O1 | per parent (surfaces in subtree) | L | 2 | 3.5 | 6 | 4–6 surfaces with task flows |
| O1 | per parent (surfaces in subtree) | XL | 3 | 5 | 9 | ≥7 surfaces |
| O2 | once (model bracket) | S | 1 | 2 | 3.5 | operate/monitor/recover procedures, small system |
| O2 | once (model bracket) | M | 1.5 | 3 | 5 | mid system runbook |
| O2 | once (model bracket) | L | 2.5 | 4.5 | 8 | large system, more failure modes to document |
| O3 | once (model bracket) | S | 0.5 | 1.5 | 3 | known errors, contacts, walkthrough for the support org |
| O3 | once (model bracket) | M | 1 | 2.5 | 4.5 | mid handover incl. session |
| O3 | once (model bracket) | L | 2 | 4 | 7 | large handover, several sessions |

#### U-OPS-USER — single-size

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| O4 | once | single | 0.25 | 0.5 | 1 | release notes for one release |

#### U-NONE

No activities — no rows, by declaration.

### Dimension 8 — security and compliance assurance

#### SA-PENTEST

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| S1 | once (model bracket) | S | 1 | 2 | 4 | threat-model review of the design, small model |
| S1 | once (model bracket) | M | 2 | 3.5 | 6 | mid model, workshop plus write-up |
| S1 | once (model bracket) | L | 3 | 5 | 9 | large model, several sessions |
| S2 | once (surface+interface count) | S | 1 | 2 | 4 | supplier side: scoping, access, liaison, receiving report |
| S2 | once (surface+interface count) | M | 2 | 3 | 5 | wider scope, same liaison pattern |
| S2 | once (surface+interface count) | L | 2.5 | 4 | 7 | 13–25 exposed items to scope and support |
| S2 | once (surface+interface count) | XL | 3 | 5 | 9 | ≥26 items; staged engagement support |
| S3 | once (surface+interface count) | S | 1 | 2 | 6 | remediation; findings count unknowable ex ante, P wide |
| S3 | once (surface+interface count) | M | 2 | 4 | 10 | typical mid-scope findings load |
| S3 | once (surface+interface count) | L | 3 | 6 | 14 | larger attack surface, longer tail |
| S3 | once (surface+interface count) | XL | 4 | 8 | 18 | widest surface; tail risk in P |

#### SA-NONE

No activities — no rows, by declaration.

## 3. Constants carried, restated

| id | constant | scope | value | basis |
|---|---|---|---|---|
| C3 | integration rate | every parent | 20% of the summed leaf effort beneath that parent | method-declared constant, restated here so the table is the single home of every number; not an external norm and not calibratable by me |

## 4. Findings

**Cells refused (honest M > 10 pd) — catalogue split needed, rows not written:**

1. **K3 · statement-behavioural · XL** (≥9 constrained components, bespoke). Realising a run-time
   property (HA with degraded mode, latency bound) across nine or more bespoke components is honestly
   12–15 pd at M. The catalogue should split realisation from evidence, or introduce a
   per-constrained-component unit.
2. **K3p · behaviour/surface/store · XL** (assessed as extend). Package extension at ≥7 counted units
   runs ~1.5 pd per unit → honest M 10–14. Needs decomposition into smaller extension units in the
   catalogue.
3. **F3 · behaviour/interface/store · XL**. Proof construction for an XL element (≥7 actions / ≥9
   operations / ≥7 entity kinds) at ~1.5–2 pd per proven unit → honest M 11–14. Split by
   proof-obligation cluster.

**Cells flagged (M < 0.25 pd):** none strictly below the floor. Four rows sit exactly at 0.25 and
are listed for the method owner's visibility (the floor decision is not mine): K1p·S, A4·S, G3·S,
E3·S.

**Driver findings:**

1. **D3 and D6 (both process alternates): duration-driven once-activities priced against the model
   bracket.** Reporting and risk-management effort follows calendar length and cadence; element count
   reaches effort only through a loose size→duration correlation. Priceable roughly — priced with
   wide P — but the catalogue would do better with a duration-linked driver. Caution, not refusal.
2. **E3 size S (one environment) is degenerate**: with one environment there is nothing to promote
   between, and under E-DSP (fixed dev/stage/prod) the S cell can never occur. The row exists because
   the marked sizing enumerates S = 1; the catalogue should either drop S from E3's sizing or note it
   unreachable.
3. **Coverage observation: K-PACKAGE-CONFIG has no construction activity for interface elements**
   (K1p/K2p/K3p apply to behaviour, surface, store only). A declaration pairing package construction
   with interface elements leaves their construction homeless. Catalogue owner's call; reported, not
   worked around.
4. **S3's true driver is findings count, unknowable ex ante**; surface+interface count is an
   acceptable rough proxy — accepted with deliberately wide P, noted for calibration priority.

## 5. Notes on use

- **Units:** person-days; 1 pd = 8 hours of net working time. O ≤ M ≤ P holds in every row.
- **Team grade assumed in every value:** competent engineers, predominantly senior/middle profile,
  enterprise delivery context.
- **Provenance stamp on every row:** `external norm, uncalibrated v0.1`. Every value derives from
  general industry base rates for the activity kind; no value descends from any run, estimate,
  total, budget or duration of this pipeline, and no specific project was referenced.
- **× cycles rows** (A5, A6, U2, U3, G5m) price one cycle; cycle counts are declaration parameters
  and do not alter rows.
- **Aggregates** never draw per-element rows; they are reached only by per-parent and once positions
  and by constant C3.
- **Compaction** used only where classes honestly share values; every size's O/M/P is written
  explicitly, no formulas.
- **Sub-floor policy:** no floor applied; rows at 0.25 are honest estimates, and the floor decision
  belongs to the method.
- **Calibration rule:** calibration is a later, separate act by someone else, performed against
  documented outcomes only. It never edits a row while looking at a gap the edit would explain; any
  change produces v0.2 with its evidence recorded beside it — never an in-place correction.

---

# Addenda (same provenance discipline, gap-blind `Hotyn-K 1.0`)

## A1 — 2026-08-22 — the demanded-work row W-R64

Produced by a single-purpose gap-blind run (input: the activity definition, the sizing rule, the
team grade — nothing else; contamination clean). Transcribed verbatim:

| activity id | element class | size | O | M | P | basis |
|---|---|---|---:|---:|---:|---|
| W-R64 — agree and record the technology currency and upgrade policy | work model (once) | single | 0.5 | 1.5 | 4.0 | external norm: drafting and agreeing a short governance document (review cadence, upgrade planning approach, decision rights) with client stakeholders, senior/middle profile — a one-to-few-page draft plus one review cycle in the typical case; pessimism covers disputed decision authority and reconciliation with the client's existing IT-governance standards |

All values price the agreement and write-up only; performing any future review or upgrade is out of
scope of the row. Stamp: `external norm, uncalibrated v0.1`.

## Known label defect, recorded for v0.2

`E7`'s rows are labelled *once (model bracket)* while the pinned driver (catalogue §3a) is
**environment count**. The values stand; the label is wrong. Found at the run-25 assembly,
2026-08-22; to be corrected at the next table version, never in place.
