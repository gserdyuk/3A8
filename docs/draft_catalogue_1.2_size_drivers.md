# DRAFT — catalogue 1.2: size-class drivers — APPLIED

Status: **applied 2026-08-21** as `docs/technology_catalogue.md` §3a (W10), after the author's
review. Historical; the catalogue is authoritative. The author's four §10 decisions, recorded there:
(1) thresholds approved, **XL added** as a fourth size class (an XL element is priced as XL and
reported as a probable M10 coarseness finding); (2) `U4` bracket-sized; (3) `D2`/`D3` stay
bracket-sized, the rate-row alternative stays an open note on the delivery dimension; (4) `statement`
gains a **sizing subclass** — compliance vs behavioural — with W7's element classes unchanged.
Russian translation used for the review: `draft_catalogue_1.2_size_drivers.ru.md`.

Design goal: reduce the size judgement to **counting named things**, so that two runs disagree
visibly — on an enumeration — or not at all.

---

## 1. The rules

**R1 — one size class per element, assigned once, reused everywhere.** The size class `S / M / L` is
a property of the **element**, derived from its declared content and own coverage at closure. Every
per-element activity on that element uses the element's class by default. Activities whose cost
scales differently override with their own driver (§4) — the exception, not the rule.

Why: it collapses the judgement surface. A 25-element batch needs ~25 counts, not ~150 per-item
guesses, and construction, test design, test implementation and review of one element can never
disagree about how big the element is.

**R2 — count by naming.** A size justification is not a number but an **enumeration**: "M — 3
actions: rank offers, re-rank on requirement change, explain ranking." The count is the length of
the list. Two runs that disagree will disagree on a visible, arguable list — the same audit form as
the coverage matrix.

**R3 — an uncountable driver is a defect report, not a guess.** If the declared content does not
support counting (a bare name, an empty declaration), the run reports the element as
*unsizeable — model defect (M10)* and assigns no class. Silence and impressionistic sizing are both
illegal.

**R4 — position-derived sizes are computed, never judged** (§5). Per-parent and once-scoped
activities take their class from tree arithmetic — subtree counts, model brackets, environment
mapping. Zero judgement, zero spread.

**R5 — thresholds live here, not in runs.** All thresholds in §3 are part of the pinned catalogue.
Changing one is a version bump.

**R6 — drivers count scope, never effort.** No driver may reference difficulty, risk, novelty or
time. Those belong to the rate table's O–P width and to the reference class — not to classification.

---

## 2. The element size class (R1)

Counted from the element's declared content plus own coverage, per element class:

| element class | what is enumerated | S | M | L |
|---|---|---|---|---|
| behaviour | distinct actions (verb on object) the declared content names | 1 | 2–3 | ≥4 |
| interface | operations consumed or exposed, plus a named protocol/auth concern counts as one | 1 | 2–4 | ≥5 |
| surface | distinct user tasks the surface serves (view X, enter Y, approve Z) | 1 | 2–3 | ≥4 |
| store | entity kinds the store is responsible for | 1 | 2–3 | ≥4 |
| statement | systems or components the property constrains | 1 | 2–4 | ≥5 |
| aggregate | — never sized: an aggregate draws no per-element construction; its work is position-derived (§5) | | | |

## 3. Default use of the element class

These activities use the element's class **as is** — no driver of their own:

- `K1` element design · `K2` implementation · `K3` statement realisation
- `A2` test design · `A3` unit/component test implementation · `A4` code review
- `F1` formal specification · `F2` proof obligations · `F3` proof construction · `F4` specification
  review · `F6` surface inspection *(the A-FV dimension is drafted too, because the falsification
  test — prediction 2 — swaps it in and must be priceable)*

## 4. Activity-specific overrides (the exceptions, each with its reason)

| id | activity | driver enumerated | S | M | L | why the default is wrong |
|---|---|---|---|---:|---:|---|
| A8 | test data preparation | store + interface elements in the parent's subtree | ≤1 | 2–3 | ≥4 | data volume follows stores and feeds, not the parent's own content |
| A9 | performance/availability testing | measurable targets the statement names (thresholds, SLOs) | 1 | 2–3 | ≥4 | one property may carry several distinct measurements |
| A10 | interface contract testing | uses the interface element's class | — | — | — | same count, listed for completeness |
| D4 | requirement elaboration | requirement ids in the element's own coverage | 1 | 2–3 | ≥4 | elaboration scales with obligations, not with implementation size |
| G1–G3 | seed specification / preparation / reconciliation | entity kinds in the store needing pre-load (a subset of the store's entities) | 1 | 2–3 | ≥4 | only seeded entities cost; run-time-filled ones do not |
| U1–U3 | UAT preparation / support / triage | surface elements in the parent's subtree | 1 | 2–3 | ≥4 | UAT scales with screens under acceptance, not with leaves |
| O1 | user documentation | surface elements in the parent's subtree | 1 | 2–3 | ≥4 | same |
| S2–S3 | penetration test / remediation | surface + interface elements in the crossed model | ≤5 | 6–12 | ≥13 | attack surface, not model size |

## 5. Position-derived classes — computed, no judgement (R4)

| scope | class comes from | S | M | L |
|---|---|---|---:|---:|
| per parent (`A5`, `A6`, `A7`, `D2`) | leaf elements in the parent's subtree | ≤3 | 4–8 | ≥9 |
| once (`A1`, `D1`, `D3`, `D6`, `E2`, `E4`, `E6`, `F5`, `O2`, `O3`, `S1`, `U4`) | elements in the crossed scope — the model bracket | ≤30 | 31–90 | ≥91 |
| per environment (`E1`) | fixed mapping: dev = S, stage = M, prod = L | | | |
| `E3` promotion, `E7` hosting | number of environments in the declaration | 1 | 2 | ≥3 |

Note the model bracket against run 19: HM19-OA1 (78 elements) prices its once-items at M, HM19-OA2
(129) at L — the structure spread propagates into the once-layer *by arithmetic*, which is the
intended behaviour, not a leak.

## 6. Single-size activities

Some activities do not scale with anything countable and get **one row** in the table, no classes:
`O4` release notes · `U1d` production verification checklist · `U4` acceptance record *(moved here
from the bracket if the author prefers; flagged as a decision)*.

## 7. Cycles

Unchanged: cycle counts are declaration parameters. A driver sizes **one cycle**; `× cycles`
multiplies items, never the class.

## 8. What remains judgement after this draft, stated honestly

1. **The enumeration itself** — what counts as one action / operation / entity. R2 makes it visible
   and arguable; it does not make it mechanical. This is the residual freedom of step 4, and P1's
   ≥90% identity is the registered test of whether it is small.
2. **The element classification** (behaviour vs statement etc.) — inherited from `Hotyn-W`, already
   measured at 74/77 with three consequential boundaries.
3. Nothing else. Prices are the table's; counts of parents, subtrees, environments are arithmetic.

## 9. Contamination note

Drivers and thresholds here were written with knowledge of run-22 outputs. The thresholds are counts
of scope, not efforts, so the anchoring surface is small — but the check is cheap and should be
used: **the rate-table author (gap-blind) sees this file and may object to any threshold as
un-priceable before writing values.** An objection is a finding about the drivers, not about the
table.

## 10. Questions for the author before this is applied

1. Are the S/M/L cut-points acceptable as pinned, or do any need moving before anything is priced?
2. `U4` — bracket-sized or single-size?
3. `D3` status reporting is bracket-sized here, and the catalogue already flags the delivery
   dimension as rate-like. Accept the bracket for v1.2, or move `D2`/`D3` to an explicit rate row in
   the table (percent of subtree effort, like C3) now?
4. Does `statement` need a fourth class for pure-compliance statements (TLS version) versus
   behavioural properties (high availability with degraded mode) — or does the A9 override cover it?
