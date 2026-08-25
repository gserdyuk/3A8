# BMS — technology declaration (`Hotyn-W` input)

One choice per dimension, drawn from `docs/technology_catalogue.md` **1.1** (run 20 was performed under 1.0; the only difference is the `per parent` scope). A run chooses nothing and
invents nothing: this file and the catalogue together fix which activities exist before the crossing
in W3 begins.

Every choice is justified from a **pinned input** — the requirement list or `assumptions.md` — or is
marked as a scope decision made here, visibly.

---

## 1. The declaration

| dimension | choice | drawn from |
|---|---|---|
| construction | **`K-BESPOKE`** — bespoke web application on a mainstream stack | R61 modern web technologies · R63 structured database platform · A4 (integrations are APIs, not a package's connectors). No requirement names a product to configure |
| assurance | **`A-TB`** — test-based | A1 includes testing in scope; A2 makes "UAT has passed" part of done. Nothing in the RFP asks for formal methods |
| acceptance | **`C-UAT`** — staged user acceptance with sign-off | A1 includes UAT support; A2 requires UAT passed |
| delivery process | **`D-TEAM`** — one team with planning and reporting ceremonies | A3 names the team: 1 PM/BA, part-time architect, 3–4 developers, 1 QA, part-time DevOps |
| environments | **`E-DSP`** — dev, stage, production | A1 includes "hosting / DevOps / environment setup (dev/stage/prod)" verbatim |
| data | **`G-SEED`** — reference and master data seeded, no legacy migration | No requirement names a predecessor system to migrate from. R21 and R41 load data **from CTC at run time** — that is product behaviour (an interface), not migration. **Scope decision, visible:** if a legacy booking dataset exists, `G-MIGRATE` is the correct choice and this declaration is wrong |
| documentation | **`U-OPS-USER`** — operational and user documentation | A2: "basic documentation (operational + user) exists" |
| security & compliance assurance | **`SA-PENTEST`** — external penetration test and remediation | R72 TLS on authenticated traffic · R73 personal data under the Data Protection Act. **Scope decision, visible:** the inputs neither demand nor exclude it; `SA-NONE` removes exactly three items |

## 2. Parameters

| parameter | value | kind |
|---|---:|---|
| environments | dev, stage, prod | **3**, from A1 |
| test execution cycles | 2 | policy choice: one pass plus a regression pass after fixes |
| UAT cycles | 2 | policy choice, same shape |

Both cycle counts are policy parameters, not estimates: they say how the work is organised, not how
long it takes. Their effect is linear — A5, A6, U2 and U3 are the only activities they multiply.

---

## 3. W6 — demanded work absorbed by the declaration

`requirements_work.md` carries five demanded items. Under this declaration:

| id | demanded | absorbed by | status |
|---|---|---|---|
| R02 | The Supplier hosts the system | **E7** hosting set-up (tenancy, capacity, runtime) | *partially* — E7 covers making the hosted service exist. Running it is **carried, not priced** (A0/A1 v2): missing parameter, the term |
| R03 | The Supplier supports the system | **O3** support handover pack | *partially* — same shape: the hand-over is priced, operating the desk is carried, not priced |
| R64 | Keep technologies up to date; reviews and planned upgrades | — | **not absorbed.** No dimension mandates a currency programme. One demanded item prices agreeing the policy; performing the reviews is carried, not priced |
| R69 | Configuration management and version control | **E4** configuration management set-up | absorbed |
| R70 | Robust release and patch promotion procedures | **E3** promotion procedure, defined and rehearsed | absorbed |

**Registered expectation versus outcome.** `requirements_work.md` predicted, before the catalogue was
written, that three of five would be absorbed and warned that absorbing none would mean the catalogue
was missing dimensions. Outcome: **two absorbed outright, two partially, one not at all.**

The one that resisted is the informative one. **R64 is a demanded obligation that no way of building
implies** — it is a commitment about the years after delivery, and none of the eight dimensions has
anything to say about them. It therefore stays a demanded branch of the work model with one item, and
it is the only work in the whole model that traces to a requirement and to no activity.

The two partial absorptions are the A1 dispute in another form, and it is **settled as of 2026-08-20**
by `assumptions.md` v2 A0: an obligation the client stated cannot be struck out, only bounded, and the
remainder must name its instrument or its missing parameter. So `E7` and `O3` price the hand-over
residue of R02 and R03, and the continuing service is **carried, not priced**, with the term named as
the missing parameter. No operations dimension is declared, and none is invented — if the client
answers with a term, one has to be written into the catalogue first.

---

## 4. The falsification variant

Prediction 2 in `docs/proposal_product_model.md` requires a second run identical to this one except
in a single dimension.

**`BMS-FV`** — every line of §1 unchanged, except:

| dimension | choice |
|---|---|
| assurance | **`A-FV`** — formal verification |

Parameters unchanged, except that **test execution cycles do not apply** — `A-FV` mandates no
execution cycles, so the parameter has no activity to multiply.

The estimate must move by more than ×1.3. If it does not, the instrument is measuring the document
and not the project, and that is a verdict on the three-step design rather than on one constant.

Note what the swap does structurally, since that is what makes the prediction testable: it removes
A5, A6, A7 and A8 — four activities, two of them multiplied by cycles across every aggregate — and
adds F1, F2 and F3 across every behaviour, interface and store element, replacing A4 with F4 and A2/A3
with nothing. The item count moves in both directions at once, which is why the prediction is about
the estimate and not about the count.

---

## 5. Pins

```
input                             md5
requirements_product.md           0c2dea478b993e4451a66f9468633f1e   (N = 68)
requirements_work.md              330826122b607088df3499e3e71cd103   (N = 5)
docs/technology_catalogue.md      version 1.1, 2026-08-20
```

Declared 2026-08-20. Changing any line above is a new declaration and a new run — not an amendment to
this one.
