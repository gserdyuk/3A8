# FaxRxTx — technology declaration (`Hotyn-W` input)

One choice per dimension, drawn from `docs/technology_catalogue.md` **1.4**. A run chooses nothing
and invents nothing: this file and the catalogue together fix which activities exist before the
crossing in W3 begins.

Every choice is justified from a **pinned input** — `requirements_pinned.md` (F-ids) or `assumptions.md`
(A-ids) — or is marked as a **scope decision made here, visibly**. There are four of those, more than
BMS's two, and the reason is stated in §4: this input is a recollection of a system, not a statement
of what a supplier owed.

---

## 1. The declaration

| dimension | choice | drawn from |
|---|---|---|
| construction | **`K-BESPOKE`** — bespoke application on a mainstream stack | F30 the language is C# · A4 no first-version code is reused, no package is named anywhere · A5 the era's stack is C#/.NET 3.x on own hardware. Nothing in the source names a product to configure |
| assurance | **`A-TB`** — test-based | A1 includes testing in scope; A2 makes passing integration tests part of done. Nothing asks for formal methods |
| acceptance | **`C-DIRECT`** — direct to production, no acceptance stage | **Scope decision, visible.** A2's definition of done is *production traffic + tests agreeing with the old system + the old version decommissionable* — it names no sign-off, no accepting party and no acceptance cycles. A8 states the organisation is a product company doing an internal rework: there is no client to accept. Declaring `C-UAT` here would invent a stage the source does not contain. The sensitivity is priced in §5 |
| delivery process | **`D-TEAM`** — one team with planning and reporting ceremonies | §6 names one team, "scrum after waterfall", QA and PM inside it, one site (Miami). `D-DISTRIBUTED` would need a second site the source never mentions |
| environments | **`E-DSP`** — dev, stage, production | **Scope decision, visible.** The source names no environment. `E-DSP` is chosen because two pinned obligations require the structure: F49 runs integration tests on the real message stream, which needs somewhere that is not production to run them, and F51 requires a promotion into production. `E-SINGLE` would leave F51 with nothing to absorb it |
| data | **`G-SEED`** — reference and master data seeded, no legacy migration | **Scope decision, visible.** A predecessor system exists (F42, F43, F47, F52) — but **no obligation names a data migration**, and A4 declares the storage infrastructure (Lustre) and the DB **reused as technologies**, which is what a shared archive looks like. If the new system's stores had in fact to be loaded from the old one's, `G-MIGRATE` is the correct choice and this declaration is wrong. The sensitivity is priced in §5 |
| documentation | **`U-OPS-USER`** — operational and user documentation | **Scope decision, visible.** Unlike BMS's A2, this assumption log demands no documentation. It is declared anyway, from three pinned entries: F31–F34 name a NOC — an operations function that must be handed something to operate; F35 names a user-facing portal; F52 requires the old version to be decommissionable, which means the operating organisation must be able to run the new one instead. `U-NONE` removes exactly four items |
| security & compliance assurance | **`SA-NONE`** | No obligation in the list names security, encryption, personal data or a compliance regime — the contrast with BMS R72/R73 is total. §7 of the source records that Venali's customers were healthcare and finance, which makes `SA-PENTEST` arguable; but §7 is public context gathered in 2026, not an obligation the project carried, and declaring from it would be estimating from hindsight. Recorded as a sensitivity in §5, not as scope |

## 2. Parameters

| parameter | value | kind |
|---|---:|---|
| environments | dev, stage, prod | **3**, from the `E-DSP` scope decision above |
| test execution cycles | 2 | policy choice: one pass plus a regression pass after fixes — **identical to the BMS declaration**, deliberately, so the two cases differ in their models and not in this parameter |
| UAT cycles | — | not applicable: `C-DIRECT` mandates no acceptance cycles |

---

## 3. W6 — demanded work under this declaration

`requirements_work.md` carries five demanded items. The prediction registered there, before this file
was written, was: F51 absorbed · F49 and F50 contested · F48 and F52 not absorbed.

| id | demanded | absorbed by | status |
|---|---|---|---|
| F51 | rollout to production; the new system takes production traffic | **E6** production cutover | **absorbed.** `E-DSP` mandates exactly this act, once, for the whole model |
| F48 | domain immersion and architecture/technology selection, ~1–2 months | — | **not absorbed.** No dimension of catalogue 1.4 mandates a learning or technology-selection stage. `D1` mobilisation stands the team and its tooling up; it does not study a domain. Enters as its own branch |
| F49 | integration tests on the real message stream | — | **not absorbed.** `A-TB` mandates test design, execution, defect resolution, regression and test data — none of them says *against live traffic through a running predecessor*. `A8` prepares test **data**; a real stream is not prepared data. Enters as its own branch |
| F50 | integration-test results compared with the old system and agreeing | — | **not absorbed**, same ground. A comparison harness against a predecessor's output is not an activity any declared dimension contains |
| F52 | the old version can be decommissioned | — | **not absorbed.** Catalogue 1.4 §13 names this exact absence — *"transition off the manual process — parallel running, decommissioning … If that work is to appear, it must enter as a requirement"*. It has entered as one. Enters as its own branch |

**Outcome: one of five absorbed, four standing alone** — against BMS's two absorbed outright, two
partially, one not at all. The registered prediction scores four of five correct: F49 and F50, called
"contested", came down on the not-absorbed side.

**What this costs, and who pays it.** Four standing branches have no rows in `docs/rate_table.md`
v0.1 + A1: the table was written against catalogue activities, and these are not catalogue
activities. Under the rate-card design they must be priced the same way `W-R64` was — by a
**gap-blind `Hotyn-K` addendum**, given the activity as worded plus the team-grade line and nothing
else. That act comes after the crossing, when the standing items are known exactly, and before the
assembly. No orchestrator judgement enters a price.

**A0 is not exercised on this case.** No assumption strikes out a demanded item, so nothing is
"carried, not priced" here and no missing-parameter clause is needed — with one exception recorded
in §4.

---

## 4. The two things this declaration cannot settle, recorded before the runs

**(i) The vintage question.** `docs/rate_table.md` v0.1 is compiled from **modern** external norms;
this project ran in **2007–2009** on C#/.NET 3.x, own hardware, no clouds, no ready orchestrators
(A5). The era-transfer is **not pre-adjusted** — the whole point of the FaxRxTx replay is to measure
what the transfer costs, and adjusting for it in advance would destroy the measurement. Whatever the
comparison against fact shows, the era is one of the named candidate explanations and it is named
here, before the number exists. Session record `sessions/2026-08-22_…` §8(b) requires exactly this.

**(ii) F48's missing parameter is headcount, and A3 removes it deliberately.** The obligation states a
**calendar** duration (~1–2 months) for a stage the whole team worked through; converting that to
effort needs the team's size, which A3 excludes from the assumptions on purpose ("the volume of work
is estimated, not the calendar"). The gap-blind rate row for F48 must therefore state its own
headcount assumption in its basis, and that assumption becomes a **declared sensitivity of the
estimate**, not a hidden constant.

---

## 5. Declared sensitivities — what a different declaration would do

Not variants to be run, but the visible price of the four scope decisions. Each is a **one-line edit**
to §1, which is the property the three-step design exists to have.

| change | effect on the work model |
|---|---|
| `C-DIRECT` → `C-UAT` | adds `U1` per parent with a surface in its subtree, `U2` and `U3` per that parent × UAT cycles, and `U4` once; removes `U1d`. On a model with few surfaces this is a small structural change; on a portal-heavy model it is large |
| `G-SEED` → `G-MIGRATE` | replaces three per-store activities with four, adds `G1m` once and `G5m` × rehearsal cycles. This is the largest of the four in effect, and the one whose ground is thinnest — see §1 |
| `U-OPS-USER` → `U-NONE` | removes `O1` (per parent with a surface), `O2`, `O3`, `O4` — four item kinds |
| `SA-NONE` → `SA-PENTEST` | adds exactly three once-scoped items: `S1`, `S2`, `S3` |

---

## 6. Pins

```
input                             md5 / version
requirements_product.md           306046dc6cab35147040224e7a4e9662   (N = 47)
requirements_work.md              b25463f3a0a56d227e3348b76e35d26c   (N =  5)
requirements_pinned.md   (parent)        473d9789f000da3cbf563c4f008fd9d5   (N = 52)
docs/technology_catalogue.md      version 1.4, 2026-08-22
docs/rate_table.md                v0.1 + addendum A1  (consumed at assembly, never by a sensor)
```

Declared 2026-08-22. Changing any line of §1 or §2 is a new declaration and a new run — not an
amendment to this one.

**Pin note.** The parent list was renamed from `requirements.md` to `requirements_pinned.md`
after the runs, because the former collides case-insensitively with the pre-existing
`REQUIREMENTS.md`. The md5s quoted above are the values the sensors were launched against; the
post-rename values are in `requirements.pin.txt`, which records both and states that only a header
reference line differs. No obligation row moved.
