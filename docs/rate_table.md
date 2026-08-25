# Rate table v0.1-h — the same values, expressed in person-hours

> **Unit: person-hours of work on the task.** Every O/M/P value below is net hours an engineer spends
> solving that task.
>
> **This is a re-expression, not a revision.** Each cell is the v0.1 person-day value × 8. No value's
> content was reviewed, re-derived, re-sampled or calibrated; 239 cells were multiplied and nothing
> else changed. The person-day version is preserved verbatim at
> `docs/archive/rate_table_v0.1_person_days.md` — divide any figure here by 8 to read what the runs of
> 2026-08-21…25 recorded.
>
> **Why hours.** The person-day carried a convention inside it, and that convention cost this project
> three days and one ×1.33 error in its own favour. An hour has no convention inside it, so the
> method's last free unit disappears. Full reasoning and the resulting constant count:
> `docs/constants.md`.
>
> **Not in these values, and not parameters of this method:** annual leave · public holidays ·
> sickness · bench time · non-project duties · the effective hours an assigned working day actually
> delivers · working days per month. Anyone needing days of presence converts with their own
> organisation's figures; this table deliberately supplies none of them.
>
> **Status: a fixed set of constants.** One sample from `Hotyn-K 1.0` × Fable 5, 2026-08-21; repeat
> sampling of that role has since been measured at ×1.38–×1.50 — that figure is **provenance, not the
> dispersion of any estimate made from these constants**, because a constant does not vary between
> runs. The table is not re-sampled. It changes only by calibration against documented outcomes, with
> the evidence recorded beside each changed value.
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

Units: **person-hours of work on the task** (v0.1-h re-expression: v0.1 person-days x 8). Team assumed throughout: competent engineers, senior/middle
mix, enterprise delivery. **Every row carries the stamp: `external norm, uncalibrated v0.1`.** Rows
marked `× cycles` price exactly one cycle. Aggregates never receive per-element rows.

### Dimension 1 — construction

#### K-BESPOKE — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K1 | behaviour, surface, store | S | 2 | 4 | 8 | single-unit design note plus neighbour contract; sub-day norm for a senior profile |
| K1 | behaviour, surface, store | M | 4 | 8 | 16 | 2–3-unit design fits one coherent sketch and contract |
| K1 | behaviour, surface, store | L | 8 | 16 | 28 | multi-unit design with state and flow decisions |
| K1 | behaviour, surface, store | XL | 16 | 28 | 48 | 7+-unit design: flows, states, error paths need working through |
| K1 | interface | S | 4 | 8 | 16 | one-operation contract where an external party's semantics must be pinned |
| K1 | interface | M | 8 | 16 | 32 | 2–4 operations incl. a protocol/auth concern |
| K1 | interface | L | 16 | 28 | 48 | 5–8 operations; error and versioning semantics dominate |
| K1 | interface | XL | 24 | 40 | 72 | ≥9 operations; negotiation and versioning decisions with the outside party |
| K2 | behaviour, surface | S | 4 | 8 | 16 | one action or one screen on a mainstream stack with plumbing in place |
| K2 | behaviour, surface | M | 8 | 20 | 40 | roughly a day per action/task with shared plumbing |
| K2 | behaviour, surface | L | 20 | 40 | 72 | 4–6 units at the same per-unit norm |
| K2 | behaviour, surface | XL | 40 | 64 | 112 | 7+ units; first unit dear, the rest near a day each |
| K2 | interface | S | 8 | 16 | 32 | one-operation adapter incl. auth, mapping, error handling |
| K2 | interface | M | 16 | 28 | 56 | 2–4 operations on a shared adapter core |
| K2 | interface | L | 24 | 48 | 80 | 5–8 operations; external-system quirks surface here |
| K2 | interface | XL | 40 | 72 | 120 | ≥9 operations; sub-day per op after the adapter core stands |
| K2 | store | S | 4 | 8 | 16 | one entity: schema, persistence, access layer at ORM norm |
| K2 | store | M | 8 | 16 | 28 | 2–3 entities with relations |
| K2 | store | L | 16 | 32 | 56 | 4–6 entities; lifecycle and constraint logic grows |
| K2 | store | XL | 28 | 52 | 88 | ≥7 entities; sub-day per entity on scaffolding |
| K3 | statement-compliance | S | 2 | 4 | 12 | one configuration decision enforced on one component, evidence captured |
| K3 | statement-compliance | M | 4 | 12 | 24 | same decision swept across 2–4 components |
| K3 | statement-compliance | L | 8 | 20 | 40 | 5–8 components plus a consolidated evidence pack |
| K3 | statement-compliance | XL | 16 | 32 | 64 | ≥9 components; sweep and evidence, no run-time mechanics |
| K3 | statement-behavioural | S | 8 | 16 | 32 | run-time mechanism in one component plus demonstration it holds |
| K3 | statement-behavioural | M | 16 | 32 | 64 | mechanism coordinated across 2–4 components |
| K3 | statement-behavioural | L | 24 | 48 | 96 | 5–8 components; failure-path work dominates |
| K3 | statement-behavioural | XL | — | — | — | **refused — see findings (M > 80 h)** |

Integration deliberately absent as an activity — carried as constant C3, restated in section 3.

#### K-PACKAGE-CONFIG — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K1p | behaviour, surface, store | S | 0.8 | 2 | 6 | capability-matrix check for one unit against a known package |
| K1p | behaviour, surface, store | M | 2 | 4 | 8 | 2–3 units assessed in one sitting |
| K1p | behaviour, surface, store | L | 4 | 8 | 16 | multi-unit fit/gap decision with write-up |
| K1p | behaviour, surface, store | XL | 8 | 12 | 24 | 7+ units; gaps need structured disposition |
| K2p | behaviour, surface, store (assessed configure) | S | 2 | 4 | 12 | declared package configuration, no code; quirks inflate P |
| K2p | behaviour, surface, store (assessed configure) | M | 4 | 12 | 24 | 2–3 units of vendor-pattern configuration |
| K2p | behaviour, surface, store (assessed configure) | L | 8 | 24 | 48 | 4–6 units; configuration interactions appear |
| K2p | behaviour, surface, store (assessed configure) | XL | 16 | 40 | 72 | 7+ units; still cheaper than build, dearer to untangle |
| K3p | behaviour, surface, store (assessed extend) | S | 8 | 16 | 32 | custom code inside the package framework, upgrade-safe norm |
| K3p | behaviour, surface, store (assessed extend) | M | 16 | 32 | 64 | 2–3 units; framework constraints tax each unit |
| K3p | behaviour, surface, store (assessed extend) | L | 32 | 56 | 96 | 4–6 units at ~12 h per unit |
| K3p | behaviour, surface, store (assessed extend) | XL | — | — | — | **refused — see findings (M > 80 h)** |
| K5p | statement-compliance | S | 2 | 4 | 12 | vendor compliance switch set and evidenced |
| K5p | statement-compliance | M | 4 | 12 | 24 | 2–4 components via vendor settings |
| K5p | statement-compliance | L | 8 | 20 | 40 | 5–8 components, consolidated evidence |
| K5p | statement-compliance | XL | 12 | 28 | 56 | ≥9 components; vendor tooling caps the sweep cost |
| K5p | statement-behavioural | S | 4 | 12 | 24 | vendor mechanism configured and demonstrated on one component |
| K5p | statement-behavioural | M | 12 | 24 | 48 | 2–4 components on vendor HA/performance features |
| K5p | statement-behavioural | L | 20 | 40 | 80 | 5–8 components; vendor features carry the mechanics |
| K5p | statement-behavioural | XL | 32 | 64 | 112 | ≥9 components; product-provided mechanism keeps M under bespoke |

#### K-PACKAGE-CONFIG — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| K4p | once (model bracket) | S | 16 | 32 | 64 | enterprise package install plus baseline, small scope |
| K4p | once (model bracket) | M | 24 | 48 | 96 | mid-size baseline: modules, roles, base parameters |
| K4p | once (model bracket) | L | 40 | 72 | 128 | large baseline across many modules |

### Dimension 2 — assurance

#### A-TB — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| A2 | behaviour, surface, interface, store | S | 2 | 4 | 8 | case design incl. negatives for one unit |
| A2 | behaviour, surface, interface, store | M | 4 | 8 | 16 | case set for 2–4 units, shared fixtures |
| A2 | behaviour, surface, interface, store | L | 8 | 16 | 28 | multi-unit case matrix |
| A2 | behaviour, surface, interface, store | XL | 12 | 24 | 40 | 7+ units; combinatorics pruned by judgement |
| A3 | behaviour, surface, interface, store | S | 4 | 8 | 16 | typically under a day per case, a handful of cases per unit |
| A3 | behaviour, surface, interface, store | M | 8 | 16 | 32 | same norm over 2–4 units |
| A3 | behaviour, surface, interface, store | L | 16 | 28 | 48 | shared harness amortises across units |
| A3 | behaviour, surface, interface, store | XL | 24 | 44 | 72 | 7+ units on a standing harness |
| A4 | behaviour, surface, interface, store | S | 0.8 | 2 | 4 | review of a single-unit change incl. one rework loop — **at 0.25 floor** |
| A4 | behaviour, surface, interface, store | M | 2 | 4 | 8 | half-day review norm for a small element |
| A4 | behaviour, surface, interface, store | L | 4 | 8 | 16 | larger diff, two passes |
| A4 | behaviour, surface, interface, store | XL | 6 | 12 | 24 | big element reviewed in instalments |
| A9 | statement-behavioural (measurable targets) | S | 8 | 16 | 32 | script, load run, analysis for one measurable target |
| A9 | statement-behavioural (measurable targets) | M | 16 | 28 | 56 | 2–3 targets sharing a test rig |
| A9 | statement-behavioural (measurable targets) | L | 24 | 44 | 80 | 4–6 targets; tuning loops likely |
| A9 | statement-behavioural (measurable targets) | XL | 32 | 64 | 112 | ≥7 targets; rig plus repeated runs |
| A10 | interface | S | 4 | 8 | 20 | contract tests against a stand-in; stand-in set-up dominates |
| A10 | interface | M | 8 | 16 | 32 | 2–4 operations on one stand-in |
| A10 | interface | L | 16 | 28 | 56 | 5–8 operations; external party availability is the risk |
| A10 | interface | XL | 24 | 40 | 80 | ≥9 operations; negotiation of test windows inflates P |

#### A-TB — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| A1 | once (model bracket) | S | 8 | 16 | 32 | strategy note for a small model |
| A1 | once (model bracket) | M | 16 | 28 | 48 | strategy incl. environments, data, automation stance |
| A1 | once (model bracket) | L | 24 | 40 | 72 | large-model strategy with per-area treatment |
| A5 | per parent, × cycles | S | 4 | 8 | 16 | one execution pass over a ≤3-leaf subtree |
| A5 | per parent, × cycles | M | 8 | 16 | 32 | one pass, 4–8 leaves |
| A5 | per parent, × cycles | L | 16 | 28 | 48 | one pass, 9–14 leaves |
| A5 | per parent, × cycles | XL | 24 | 40 | 72 | one pass, ≥15 leaves |
| A6 | per parent, × cycles | S | 4 | 12 | 32 | fix-and-retest of one pass's findings; defect count is the tail |
| A6 | per parent, × cycles | M | 8 | 24 | 56 | typical defect load of a mid subtree pass |
| A6 | per parent, × cycles | L | 16 | 40 | 80 | larger subtree, one pass's load |
| A6 | per parent, × cycles | XL | 24 | 56 | 112 | ≥15 leaves; P carries the bad-pass case |
| A7 | per parent | S | 8 | 16 | 32 | automated regression over core paths of a small subtree |
| A7 | per parent | M | 16 | 32 | 56 | suite over 4–8 leaves incl. CI wiring |
| A7 | per parent | L | 24 | 48 | 80 | 9–14 leaves; suite maintenance seed included |
| A7 | per parent | XL | 32 | 64 | 112 | ≥15 leaves; selective depth, judgement-pruned |
| A8 | per parent (store+interface in subtree) | S | 2 | 4 | 12 | data for at most one store/interface |
| A8 | per parent (store+interface in subtree) | M | 4 | 12 | 24 | 2–3 data-bearing elements |
| A8 | per parent (store+interface in subtree) | L | 8 | 20 | 40 | 4–6 data-bearing elements, cross-consistent sets |
| A8 | per parent (store+interface in subtree) | XL | 16 | 32 | 64 | ≥7 data-bearing elements |

#### A-FV — per element

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| F1 | behaviour, interface, store | S | 4 | 8 | 20 | formalising one unit's pre/post-conditions and invariants |
| F1 | behaviour, interface, store | M | 8 | 20 | 40 | 2–4 units in one specification module |
| F1 | behaviour, interface, store | L | 16 | 36 | 64 | multi-unit specification with interaction invariants |
| F1 | behaviour, interface, store | XL | 28 | 56 | 96 | 7+/9+ units; state space needs structuring first |
| F2 | behaviour, interface, store | S | 2 | 6 | 12 | obligation derivation, semi-mechanical with tooling |
| F2 | behaviour, interface, store | M | 4 | 12 | 24 | obligations across 2–4 units |
| F2 | behaviour, interface, store | L | 8 | 20 | 40 | larger obligation set, manual triage |
| F2 | behaviour, interface, store | XL | 12 | 32 | 56 | XL element's obligation set with pruning |
| F3 | behaviour, interface, store | S | 8 | 16 | 40 | interactive proof plus checker run for one unit |
| F3 | behaviour, interface, store | M | 16 | 32 | 72 | ~16 h per proven unit, some obligations resist |
| F3 | behaviour, interface, store | L | 28 | 60 | 112 | 4–6/5–8 units; a stuck proof carries the P |
| F3 | behaviour, interface, store | XL | — | — | — | **refused — see findings (M > 80 h)** |
| F4 | behaviour, interface, store, surface | S | 2 | 4 | 8 | peer review of a one-unit specification |
| F4 | behaviour, interface, store, surface | M | 4 | 8 | 16 | review of a 2–4-unit specification |
| F4 | behaviour, interface, store, surface | L | 8 | 12 | 24 | larger spec, two reviewers' passes folded in |
| F4 | behaviour, interface, store, surface | XL | 12 | 20 | 32 | XL spec reviewed in instalments |
| F6 | surface | S | 2 | 4 | 8 | structured inspection of a one-task surface |
| F6 | surface | M | 4 | 8 | 16 | inspection across 2–3 tasks |
| F6 | surface | L | 8 | 16 | 28 | 4–6 tasks with checklist evidence |
| F6 | surface | XL | 12 | 24 | 40 | ≥7 tasks |

#### A-FV — position-derived

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| F5 | once (model bracket) | S | 8 | 16 | 32 | verification report over a small model |
| F5 | once (model bracket) | M | 16 | 28 | 48 | consolidation of mid-size proof results |
| F5 | once (model bracket) | L | 24 | 40 | 64 | large-model report with residual-risk register |

### Dimension 3 — acceptance

#### C-UAT — position-derived (sizing: surface count in subtree)

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| U1 | per parent (surfaces in subtree) | S | 4 | 8 | 16 | client workshop plus scenario write-up, one surface |
| U1 | per parent (surfaces in subtree) | M | 8 | 16 | 32 | scenarios across 2–3 surfaces |
| U1 | per parent (surfaces in subtree) | L | 16 | 28 | 48 | 4–6 surfaces; client iteration rounds |
| U1 | per parent (surfaces in subtree) | XL | 24 | 40 | 72 | ≥7 surfaces |
| U2 | per parent, × cycles | S | 4 | 8 | 20 | supplier side of one client-run cycle, one surface |
| U2 | per parent, × cycles | M | 8 | 16 | 32 | one cycle, 2–3 surfaces |
| U2 | per parent, × cycles | L | 12 | 24 | 48 | one cycle, 4–6 surfaces |
| U2 | per parent, × cycles | XL | 20 | 36 | 64 | one cycle, ≥7 surfaces |
| U3 | per parent, × cycles | S | 4 | 12 | 32 | triage and fix of one cycle's findings; volume is the tail |
| U3 | per parent, × cycles | M | 8 | 20 | 48 | one cycle's findings over 2–3 surfaces |
| U3 | per parent, × cycles | L | 12 | 32 | 64 | one cycle's findings over 4–6 surfaces |
| U3 | per parent, × cycles | XL | 20 | 48 | 96 | one cycle's findings over ≥7 surfaces |
| U4 | once (model bracket) | S | 4 | 8 | 16 | record assembly and sign-off shepherding |
| U4 | once (model bracket) | M | 8 | 12 | 24 | more parties on the record |
| U4 | once (model bracket) | L | 8 | 16 | 32 | large model, multi-stakeholder sign-off |

#### C-DIRECT — single-size

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| U1d | once | single | 4 | 8 | 16 | production verification checklist written and run once |

### Dimension 4 — delivery process

#### D-TEAM

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| D1 | once (model bracket) | S | 8 | 16 | 32 | team, tooling, working-agreement stand-up |
| D1 | once (model bracket) | M | 16 | 32 | 56 | mid-size engagement mobilisation |
| D1 | once (model bracket) | L | 24 | 48 | 80 | large engagement, more roles to seat |
| D2 | per parent (subtree leaves) | S | 4 | 8 | 16 | subsystem plan and its upkeep across the build |
| D2 | per parent (subtree leaves) | M | 8 | 16 | 32 | 4–8 leaves tracked to done |
| D2 | per parent (subtree leaves) | L | 16 | 28 | 48 | 9–14 leaves, replanning included |
| D2 | per parent (subtree leaves) | XL | 24 | 40 | 64 | ≥15 leaves |
| D3 | once (model bracket) | S | 8 | 16 | 32 | cadence reporting over a short engagement |
| D3 | once (model bracket) | M | 16 | 32 | 64 | bracket proxies duration — see driver finding |
| D3 | once (model bracket) | L | 32 | 64 | 112 | long engagement's reporting stream, proxy driver |
| D4 | per covering element (requirement ids) | S | 2 | 4 | 8 | clarification loop for one requirement id |
| D4 | per covering element (requirement ids) | M | 4 | 8 | 16 | 2–3 ids elaborated together |
| D4 | per covering element (requirement ids) | L | 8 | 16 | 32 | 4–6 ids; conflicts need resolving |
| D4 | per covering element (requirement ids) | XL | 12 | 24 | 48 | ≥7 ids on one element |
| D6 | once (model bracket) | S | 4 | 8 | 16 | register upkeep and escalations, small engagement |
| D6 | once (model bracket) | M | 8 | 20 | 40 | bracket proxies duration — see driver finding |
| D6 | once (model bracket) | L | 16 | 32 | 64 | long engagement's risk stream, proxy driver |

#### D-DISTRIBUTED (two sites, formal hand-offs; cross-site load lives in D7)

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| D1 | once (model bracket) | S | 12 | 24 | 40 | two sites mobilised plus hand-off protocol defined |
| D1 | once (model bracket) | M | 24 | 44 | 72 | mid engagement, two-site set-up |
| D1 | once (model bracket) | L | 32 | 64 | 104 | large engagement, two-site set-up |
| D2 | per parent (subtree leaves) | S | 4 | 8 | 16 | as one-team planning; cross-site load carried by D7 |
| D2 | per parent (subtree leaves) | M | 8 | 16 | 32 | as one-team planning |
| D2 | per parent (subtree leaves) | L | 16 | 28 | 48 | as one-team planning |
| D2 | per parent (subtree leaves) | XL | 24 | 40 | 64 | as one-team planning |
| D3 | once (model bracket) | S | 8 | 16 | 32 | client-facing stream is site-independent |
| D3 | once (model bracket) | M | 16 | 32 | 64 | as one-team; proxy driver, see finding |
| D3 | once (model bracket) | L | 32 | 64 | 112 | as one-team; proxy driver |
| D4 | per covering element (requirement ids) | S | 2 | 4 | 8 | elaboration is site-independent |
| D4 | per covering element (requirement ids) | M | 4 | 8 | 16 | as one-team |
| D4 | per covering element (requirement ids) | L | 8 | 16 | 32 | as one-team |
| D4 | per covering element (requirement ids) | XL | 12 | 24 | 48 | as one-team |
| D6 | once (model bracket) | S | 4 | 8 | 16 | cross-site dependency load carried by D7 |
| D6 | once (model bracket) | M | 8 | 20 | 40 | as one-team |
| D6 | once (model bracket) | L | 16 | 32 | 64 | as one-team |
| D7 | per parent (subtree leaves) | S | 4 | 8 | 20 | hand-off preparation and joint sessions for a small subtree |
| D7 | per parent (subtree leaves) | M | 8 | 20 | 40 | seam rework is the recurring cost |
| D7 | per parent (subtree leaves) | L | 16 | 32 | 64 | 9–14 leaves crossing the seam |
| D7 | per parent (subtree leaves) | XL | 24 | 48 | 88 | ≥15 leaves; misunderstandings scale with hand-offs |

### Dimension 5 — environments

#### E-DSP

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| E1 | per environment | dev = S | 4 | 8 | 20 | scripted provisioning, dev-grade |
| E1 | per environment | stage = M | 8 | 16 | 32 | prod-like configuration, test hooks |
| E1 | per environment | prod = L | 16 | 28 | 56 | hardening, access control, monitoring hooks |
| E2 | once (model bracket) | S | 8 | 16 | 32 | CI/CD across three targets, small system |
| E2 | once (model bracket) | M | 16 | 28 | 56 | more build artefacts, same pipeline pattern |
| E2 | once (model bracket) | L | 24 | 44 | 80 | many components through one pipeline family |
| E3 | once (environment count) | S (1 env) | 0.8 | 2 | 4 | collapses to a release checklist — **at floor; degenerate, see findings** |
| E3 | once (environment count) | M (2 envs) | 4 | 8 | 16 | one promotion boundary defined and rehearsed |
| E3 | once (environment count) | L (≥3 envs) | 8 | 16 | 32 | full path incl. rollback rehearsed |
| E4 | once (model bracket) | S | 4 | 8 | 16 | repos, branching, config store conventions |
| E4 | once (model bracket) | M | 8 | 12 | 24 | multiple repos/config surfaces |
| E4 | once (model bracket) | L | 12 | 20 | 40 | large component set under management |
| E6 | once (model bracket) | S | 8 | 16 | 32 | cutover plan plus the event itself, small system |
| E6 | once (model bracket) | M | 16 | 28 | 56 | coordinated cutover with fallback |
| E6 | once (model bracket) | L | 24 | 40 | 80 | large-system cutover; the long night sits in P |
| E7 | once (model bracket) | S | 8 | 16 | 32 | tenancy, capacity, runtime services, small footprint |
| E7 | once (model bracket) | M | 16 | 28 | 56 | mid footprint with capacity sizing |
| E7 | once (model bracket) | L | 24 | 44 | 80 | large footprint, enterprise hosting process |

#### E-SINGLE

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| E1 | once | S (fixed) | 4 | 8 | 20 | one dev-grade environment |
| E2 | once (model bracket) | S | 4 | 12 | 24 | single-target pipeline, small system |
| E2 | once (model bracket) | M | 8 | 20 | 40 | single target, more artefacts |
| E2 | once (model bracket) | L | 16 | 32 | 56 | single target, many components |

### Dimension 6 — data

#### G-SEED — per store element (entity kinds needing pre-load)

| id | element class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| G1 | store | S | 2 | 4 | 8 | which records, sources, ownership for one entity kind |
| G1 | store | M | 4 | 8 | 16 | 2–3 entity kinds specified |
| G1 | store | L | 8 | 16 | 28 | 4–6 kinds; source negotiation |
| G1 | store | XL | 12 | 24 | 40 | ≥7 kinds |
| G2 | store | S | 2 | 4 | 12 | collect, cleanse, load one kind |
| G2 | store | M | 4 | 12 | 24 | 2–3 kinds; cleansing is the variable |
| G2 | store | L | 8 | 20 | 40 | 4–6 kinds |
| G2 | store | XL | 16 | 32 | 56 | ≥7 kinds |
| G3 | store | S | 0.8 | 2 | 4 | counts, spot checks, written note — **at 0.25 floor** |
| G3 | store | M | 2 | 4 | 8 | reconciliation across 2–3 kinds |
| G3 | store | L | 4 | 8 | 16 | 4–6 kinds cross-checked |
| G3 | store | XL | 8 | 12 | 24 | ≥7 kinds |

#### G-MIGRATE

| id | position / class | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| G1m | once (model bracket) | S | 8 | 16 | 32 | profiling the predecessor's actual data quality |
| G1m | once (model bracket) | M | 16 | 32 | 64 | mid-size legacy source, sampling and anomaly log |
| G1m | once (model bracket) | L | 24 | 48 | 96 | large source; surprises live in P |
| G2m | store (entity kinds) | S | 4 | 8 | 20 | field-level mapping for one kind incl. rules for dirt |
| G2m | store (entity kinds) | M | 8 | 20 | 40 | 2–3 kinds mapped |
| G2m | store (entity kinds) | L | 16 | 32 | 64 | 4–6 kinds; transformation rules multiply |
| G2m | store (entity kinds) | XL | 24 | 48 | 88 | ≥7 kinds |
| G3m | store (entity kinds) | S | 8 | 16 | 32 | ETL build for one kind against legacy quirks |
| G3m | store (entity kinds) | M | 16 | 32 | 64 | 2–3 kinds on a shared ETL frame |
| G3m | store (entity kinds) | L | 24 | 52 | 96 | 4–6 kinds; quirk handling dominates |
| G3m | store (entity kinds) | XL | 32 | 72 | 128 | ≥7 kinds; just under a split-worthy load |
| G4m | store (entity kinds) | S | 4 | 8 | 20 | load run plus reconciliation report, one kind |
| G4m | store (entity kinds) | M | 8 | 16 | 32 | 2–3 kinds loaded and reconciled |
| G4m | store (entity kinds) | L | 12 | 28 | 56 | 4–6 kinds |
| G4m | store (entity kinds) | XL | 20 | 40 | 80 | ≥7 kinds |
| G5m | once (model bracket), × cycles | S | 8 | 16 | 32 | one full rehearsal pass, timing, issue log |
| G5m | once (model bracket), × cycles | M | 16 | 28 | 56 | one rehearsal, mid volume |
| G5m | once (model bracket), × cycles | L | 24 | 44 | 80 | one rehearsal, large volume window |

### Dimension 7 — documentation

#### U-OPS-USER

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| O1 | per parent (surfaces in subtree) | S | 4 | 8 | 16 | user guide for one surface |
| O1 | per parent (surfaces in subtree) | M | 8 | 16 | 32 | guide across 2–3 surfaces |
| O1 | per parent (surfaces in subtree) | L | 16 | 28 | 48 | 4–6 surfaces with task flows |
| O1 | per parent (surfaces in subtree) | XL | 24 | 40 | 72 | ≥7 surfaces |
| O2 | once (model bracket) | S | 8 | 16 | 28 | operate/monitor/recover procedures, small system |
| O2 | once (model bracket) | M | 12 | 24 | 40 | mid system runbook |
| O2 | once (model bracket) | L | 20 | 36 | 64 | large system, more failure modes to document |
| O3 | once (model bracket) | S | 4 | 12 | 24 | known errors, contacts, walkthrough for the support org |
| O3 | once (model bracket) | M | 8 | 20 | 36 | mid handover incl. session |
| O3 | once (model bracket) | L | 16 | 32 | 56 | large handover, several sessions |

#### U-OPS-USER — single-size

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| O4 | once | single | 2 | 4 | 8 | release notes for one release |

#### U-NONE

No activities — no rows, by declaration.

### Dimension 8 — security and compliance assurance

#### SA-PENTEST

| id | position | size | O | M | P | basis |
|---|---|---|---|---|---|---|
| S1 | once (model bracket) | S | 8 | 16 | 32 | threat-model review of the design, small model |
| S1 | once (model bracket) | M | 16 | 28 | 48 | mid model, workshop plus write-up |
| S1 | once (model bracket) | L | 24 | 40 | 72 | large model, several sessions |
| S2 | once (surface+interface count) | S | 8 | 16 | 32 | supplier side: scoping, access, liaison, receiving report |
| S2 | once (surface+interface count) | M | 16 | 24 | 40 | wider scope, same liaison pattern |
| S2 | once (surface+interface count) | L | 20 | 32 | 56 | 13–25 exposed items to scope and support |
| S2 | once (surface+interface count) | XL | 24 | 40 | 72 | ≥26 items; staged engagement support |
| S3 | once (surface+interface count) | S | 8 | 16 | 48 | remediation; findings count unknowable ex ante, P wide |
| S3 | once (surface+interface count) | M | 16 | 32 | 80 | typical mid-scope findings load |
| S3 | once (surface+interface count) | L | 24 | 48 | 112 | larger attack surface, longer tail |
| S3 | once (surface+interface count) | XL | 32 | 64 | 144 | widest surface; tail risk in P |

#### SA-NONE

No activities — no rows, by declaration.

## 3. Constants carried, restated

| id | constant | scope | value | basis |
|---|---|---|---|---|
| C3 | integration rate | every parent | 20% of the summed leaf effort beneath that parent | method-declared constant, restated here so the table is the single home of every number; not an external norm and not calibratable by me |

## 4. Findings

**Cells refused (honest M > 80 h) — catalogue split needed, rows not written:**

1. **K3 · statement-behavioural · XL** (≥9 constrained components, bespoke). Realising a run-time
   property (HA with degraded mode, latency bound) across nine or more bespoke components is honestly
   96-120 h at M. The catalogue should split realisation from evidence, or introduce a
   per-constrained-component unit.
2. **K3p · behaviour/surface/store · XL** (assessed as extend). Package extension at ≥7 counted units
   runs ~12 h per unit -> honest M 80-112. Needs decomposition into smaller extension units in the
   catalogue.
3. **F3 · behaviour/interface/store · XL**. Proof construction for an XL element (≥7 actions / ≥9
   operations / ≥7 entity kinds) at ~12-16 h per proven unit -> honest M 88-112. Split by
   proof-obligation cluster.

**Cells flagged (M < 2 h):** none strictly below the floor. Four rows sit exactly at 2 h and
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

- **Units:** **person-hours of work on the task.** O <= M <= P holds in every row. Leave, holidays, sickness and any other organisational time are outside these values and are not parameters of this method.
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
- **Sub-floor policy:** no floor applied; rows at 2 h are honest estimates, and the floor decision
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
| W-R64 — agree and record the technology currency and upgrade policy | work model (once) | single | 4 | 12 | 32 | external norm: drafting and agreeing a short governance document (review cadence, upgrade planning approach, decision rights) with client stakeholders, senior/middle profile — a one-to-few-page draft plus one review cycle in the typical case; pessimism covers disputed decision authority and reconciliation with the client's existing IT-governance standards |

All values price the agreement and write-up only; performing any future review or upgrade is out of
scope of the row. Stamp: `external norm, uncalibrated v0.1`.

## Known label defect, recorded for v0.2

`E7`'s rows are labelled *once (model bracket)* while the pinned driver (catalogue §3a) is
**environment count**. The values stand; the label is wrong. Found at the run-25 assembly,
2026-08-22; to be corrected at the next table version, never in place.
