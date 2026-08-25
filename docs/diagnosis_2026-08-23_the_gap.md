# The ×1.735 — irreducible spread, or removable error?

**2026-08-23.** The question the author asked after run 32: *are we inside a systematic spread we
cannot fight — the freedom of design variants — or is this an error?* And the reading offered with it:
*at RFP maturity a ×0.5–2 cone is normal, and ×0.57 of nominal is inside it.*

This document answers both, in that order, and then lists the causes with what each is worth and how
each is tested. **Nothing here changes a number.** Everything here is a hypothesis with a test, and §6
says why that distinction is load-bearing on this particular document.

---

## 1. The RFP-cone reading is correct, and three things follow from it that are not the same thing

The reading is legitimate and it is conceded without argument: at RFP-stage maturity, published
practice puts the achievable band at ×0.5–2, and 69.2 against 120 sits at ×0.58 — inside it, near the
low edge. As a **range** statement the chain did not do anything unusual.

Three consequences follow, and they must be kept apart.

**(a) The chain did not declare a range. It declared a centre.** A centre is a claim that the outcome
is about as likely above as below. Attach an RFP-maturity band to 69.2 and you get 34.6–138.4; the fact
lands at ~0.87 of the way up that band, not in its middle. So the chain is not "inside the cone" in the
sense that matters — it is near one wall of it.

**(b) A centre is what gets committed.** Bid 69, deliver 120, and that is a 74% overrun. The cone
excuses the estimator; it does not excuse the bid. That is the whole reason `docs/exit_criterion.md`
scores the **calibrated P50** and not the width of anything.

**(c) The project's own claim is precisely that calibration buys the difference.** `exit_criterion.md`
§"Why these numbers" says it in as many words: *"×1.3 is deliberately tighter than uncalibrated
RFP-stage practice (×1.5–2, the cone of uncertainty at that maturity). The instrument's claim is
exactly that calibration buys the difference; this gate is where the claim is tested."* Accepting
×0.57 as acceptable **is** retiring that claim. That may be the right decision — but it is a decision
about what the project is for, not a reading of this result.

**And the sharpest form of the point.** The two repeats agreed to **×1.032** and the centre missed by
**×1.735**. The instrument is *fifty times more precise than it is accurate*. That is not what the cone
looks like. The cone is uncertainty in the world showing through a document; what we have is an
instrument reporting a number confidently that the document does not determine. **False precision is a
diagnosable state, not an irreducible one** — and it is diagnosable exactly because precision and
accuracy came out so far apart.

---

## 2. Design-variant freedom is already measured, and it is an order of magnitude too small

This is the author's own candidate — *"как свобода вариантов проектирования"* — and it is the one
candidate the runs already answer with a number rather than an argument.

Run 29 built **two** product models from the identical pinned list, with the identical instrument and
the identical projection: `HM29-OA1` at 97 nodes and `HM29-OA2` at 87. Those two models *are* two
design variants — different subsystem boundaries, F47 as a parity node in one and as aggregate residue
in the other, identity as a subsystem in one and as two leaves in the other.

| | |
|---|---|
| measured design-variant freedom (OA1 vs OA2 node count) | **×1.115** |
| the gap to be explained | **×1.735** |
| share of the gap it can carry, in log terms | ln 1.115 ÷ ln 1.735 = **20%** |

So: **no.** We are not sitting inside irreducible design freedom. Design freedom, as this instrument
actually exhibits it on this project, is worth about a fifth of the gap at the very most — and that is
an upper bound, because it assumes the total tracks node count perfectly (R8) and that OA2 is a fair
sample of how far variants spread.

---

## 3. The signature test: does the sign correlate with something we control?

Irreducible spread has a signature — the sign of the error is random with respect to everything the
estimator controls. Removable error has the opposite signature: the sign tracks a knob.

Four numbers on **one unchanged project, one unchanged obligation set, one unchanged fact**:

| generation | centre | against 120 | the free parameter that generation is known to have had |
|---|---:|---|---|
| 2026-07-17 manual | 111.6 pm | ×0.93 | judgement pricing, one careful pass |
| 2026-08-05 agent pipeline | 237.8 pm | ×1.98 | judgement pricing at scale — leaf count free |
| 2026-08-05 calibrated | 503 pm | ×4.19 | a ×1.72 multiplier stack on top of the above |
| 2026-08-22 Hotyn chain | 69.2 pm | ×0.58 | element count free; price per element pinned |

The sign is not random. Each number is what that generation's known free parameter predicts. **That is
the signature of error, not of spread.**

---

## 4. The causes, each with a size and a test

Six candidates. The sizes are computed from the pinned table and the run outputs, not guessed; the
arithmetic is in `examples/FaxRxTx/run31_raw/assemble_faxrxtx.py` and reproduced inline.

### (a) The unit of the fact — the largest single lever, and the cheapest to test

`FACT.md` states *"Team: ~10 people (±). Duration: about 1 year. Total: ~120 person-months."* The 120
is a **headcount × calendar product** — staffed months, not worked months. Our rates are in *assigned
working days*, the convention the author adjudicated on 2026-08-22.

A person staffed on a project for a year does not deliver 12 × 21 assigned project days: annual leave
and public holidays alone are 11–13% of the working year, and sickness, training and other duties add
more. Project-effective utilisation of 75–85% is the ordinary range.

| utilisation assumed | the fact in our unit | the gap becomes |
|---|---:|---|
| 100% (as stated) | 120 pm | ×1.735 |
| 85% | 102 pm | **×1.475** |
| 80% | 96 pm | **×1.388** |
| 75% | 90 pm | **×1.301** |

**Test: one question to the participant** — *were those ten people full-time on this project for the
whole year, or is ten the headcount that was staffed to it?* Free, and it moves more than anything else
on this list. Note the shape of it: this is the same class of question as A7 v3 (person-day = assigned
working day), which the author has already had to adjudicate once, on the estimate's side. It has never
been adjudicated on the fact's side.

### (b) Coverage holes — the model does not contain parts of the system

Not granularity. **Absence.** And the sensors named it themselves, unprompted, before any fact was
opened:

- **5 unsizeable elements**, 27 items unpriced — `HM1-61` (a database that names no entity kind),
  `HM1-83` (*"what happens when there is no delivery"*), `HM1-78` (*"Integration with the old system"*,
  no direction, no payload), `HM1-84` (core parity, no function named), `HM1-63`'s seed count.
- **13 closure violations** in repeat 1, 11 in repeat 2 — work the sizing sensors judged necessary and
  refused to invent: no element receives the send outcome back from a point of presence · nothing
  determines an unattributable inbound fax's fate · no portal user authentication (only recovery) ·
  nothing ends the transition · no alerting on bad state · no CDR/billing egress · no user directory ·
  no node departure and claim release · nothing establishes the agreed clock.

| | pd |
|---|---:|
| 27 unpriced items at the model's own ~1.45 pd/item, with C3 | +47 |
| 13 closure violations at one M bundle (8.625 pd) each, with C3 | +135 |
| **together** | **+182 → ×1.125** |

**Test: adjudicate them on their own merits, blind to the total.** The list exists; it needs a ruling
per line, not a number. This is A0 discipline applied to a case where the sensors did their job and the
orchestrator has not yet done his.

### (c) Granularity — and the table does *not* conserve the sum under splitting

The author's own insight of 2026-08-19 was that a correct decomposition divides complexity and the sum
should be conserved. **Measured against the pinned table, it is not.** Full per-element bundle for a
covered behaviour (K1, K2, A2, A3, A4, D4):

| size | bundle |
|---|---:|
| S | 4.06 pd |
| M | 8.63 pd |
| L | 16.33 pd |

| split | before → after | ratio |
|---|---|---|
| one L (4–6 actions) → 5 × S | 16.33 → 20.29 | **×1.24** |
| one L → 2 × M | 16.33 → 17.25 | ×1.06 |
| one M (2–3 actions) → 3 × S | 8.63 → 12.17 | **×1.41** |
| one M → 2 × S | 8.63 → 8.12 | ×0.94 |

So splitting inflates wherever the split is real, and the inflation is not small. To reach the fact by
granularity alone, the leaf layer would have to be **×1.81**, i.e. **~133 sized elements against
today's 74**.

**Test: the granularity experiment** — one `Hotyn-M` run instructed to ~160–170 nodes on the same
pinned list, crossed, sized and priced with no rate changed. It is the only test that separates a
modelling artefact from a level error, and it must be run **after** (a), (b) and (d), because those
three move the target it is aimed at.

### (d) The four visible scope decisions

Computed exactly, not estimated:

| switch | pd |
|---|---:|
| `C-DIRECT` → `C-UAT` (U1/U2/U3 on 5 parents with surfaces, U4, minus U1d), with C3 | +102 |
| `SA-NONE` → `SA-PENTEST` (S1, S2, S3, once-layer) | +16 |
| `G-SEED` → `G-MIGRATE` (G1m, G2m/G3m/G4m on two stores, G5m ×2), with C3 | +33 |
| **all four** | **+151 → ×1.104** |

**Test: none needed — it is arithmetic.** What is needed is a *ruling* on which declaration is right,
and `U-OPS-USER` is the fourth, already declared the more expensive way. Note that `G-SEED` was flagged
in the declaration itself as the decision with the thinnest ground.

### (e) A team that did not know the domain — not modelled at all

`assumptions.md` A3 states it flatly: the team did not know fax protocols, telecom or distributed
delivery. The rate table's assumed grade is *"competent engineers, predominantly senior/middle,
enterprise delivery context"* — an **experienced** team.

`W-F48` prices the immersion **stage**, 43.5 pd. It does not price the drag on every element built
afterwards by people still learning the domain. That drag is real and is a standard estimation
parameter everywhere else — COCOMO II's application experience factor spans roughly ×0.81 to ×1.22
across its range, i.e. about ×1.5 end to end. **Nothing in this chain has a place to put it.**

**Test: needs ≥ 2 further outcome cases** with contrasting team familiarity. Not available now, and it
must not be fitted on this one.

### (f) The vintage — partly modelled, partly not

2007–2009: C#/.NET 3.x, own hardware, no cloud, no orchestrator, and by explicit decision no message
broker. **Part of this is already in the structure** — the hand-built watchdog-and-token mechanism is
ten elements (`HM1-53` … `HM1-58`, `HM1-82`, `HM1-83`, `HM1-85`, `HM1-92`) and is priced. What is *not*
modelled is that every element is dearer in 2007: no library for it, worse tooling, worse diagnostics,
worse build and test infrastructure.

**Test: same as (e)** — a modern case and an old case priced with one table. Cannot be separated from
(e) at n = 1, because both are per-element level effects with the same sign.

---

## 5. The compound, and why it is a hypothesis and not a result

Take the three corrections that need **no new run** — (a) the unit of the fact, (b) the coverage holes
the sensors already named, (d) the scope decisions:

| | pd | pm |
|---|---:|---:|
| the chain's centre as it stands | 1452 | 69.2 |
| + coverage holes (b) | +182 | |
| + all four scope decisions (d) | +151 | |
| **corrected estimate** | **1785** | **85.0** |
| the fact at 80% utilisation (a) | 2016 | 96.0 |
| **remaining gap** | | **×1.13 — inside the ×1.3 gate** |
| the same estimate against the fact at face value | | ×1.41 |

**Read that with the health warning attached, because the warning is the point.** This decomposition
was assembled **after** the gap was known. That is exactly the fitting `exit_criterion.md` §3 and the
rate table's calibration rule forbid, and the fact that it lands so neatly inside ×1.3 is *evidence
that it was constructed to*, not evidence that it is true. Three corrections chosen from six candidates,
each sized with one plausible assumption, landing on the gate — that is what motivated reasoning looks
like from the inside.

So the compound is worth exactly one thing: it shows the gap **does not need an exotic explanation**.
It does not show that these are the right three. Each has to be validated on its own merits, by
someone who is not looking at the total, before any of them is allowed to move a number.

---

## 6. The elimination programme, in cost order

1. **Ask the participant one question** about the ten people — staffed headcount, or full-time on this?
   Free. Largest single lever (×1.735 → ×1.39 at 80%). It is a question about the **fact**, which is why
   nobody has asked it: three generations of this project have interrogated the estimate and taken the
   fact as given.
2. **Adjudicate the 5 unsizeable elements and the 13 closure violations**, gap-blind, on their own
   merits. Re-price. The list exists and cost nothing to produce.
3. **Rule on the four scope decisions.** Pure arithmetic afterwards; +151 pd if all four go the other
   way.
4. **Then re-measure.** Only now is it known what is left to explain.
5. **Then the granularity experiment.** It separates a modelling artefact from a level error — and if
   the total tracks element count, `L-1` must be **withdrawn, not re-fitted**.
6. **Era and team-familiarity factors: not before a second and third outcome case.** They are the two
   candidates that cannot be tested on FaxRxTx at all, and fitting them here would burn the case for
   nothing.

**`L-1` = ×1.735 should not be applied to anything until step 4.** It was recorded as the one act the
stage-3 plan permitted, and it conflates every cause above. Steps 1–3 will move it, and a factor that
moves when you fix an unrelated defect was never a calibration.

---

## 7. What to do with whatever survives

Some of it will. If steps 1–5 leave a residue, that residue **is** the irreducible part, and the
response to irreducible uncertainty is not a better centre — it is a **declared corridor**, which this
chain does not have (`BACKLOG.md`, debt 4). Exit-criterion test 2 could not be applied to run 31 at
all, and that is the same gap seen from the scoring side.

Two facts point the same way and are worth putting next to each other:

- The chain's only band is ΣO…ΣP, which assumes perfect correlation across ~580 items and spans ×4.3.
  The alternative, leaf independence, gives an absurdly narrow interval that both earlier generations
  already flagged as an artefact. **Neither is an 80% interval**, and the truth is in between at a
  correlation nobody has measured.
- The **reference class** produces a corridor natively, and has been the closest instrument to this
  fact twice (×1.33 and ×1.13) while the bottom-up wandered ×0.93 → ×1.98 → ×4.19 → ×0.58 (R10, R9).

Which suggests the division of labour the July 2026 run already proposed and the project never took up:
**the centre from the bottom-up, the corridor from the class.** Today's result is the strongest evidence
so far that the bottom-up's job may be decomposition and coverage — telling you *what the work is* —
rather than telling you how much of it there is.
