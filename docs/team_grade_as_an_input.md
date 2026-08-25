# Team grade is an input to an outcome comparison, and it has never been declared

**2026-08-24.** Prompted by the author's question: *how much can the speeds of different teams — or of
people from different teams — differ? And in that sense, whose person is the 6 person-hours?*

The second question turns out to answer the first, and together they expose a required input the
project has been missing for as long as the unit was missing.

---

## 1. The 6 hours is not "for a person" at all

Two different quantities are riding in the same sentence and must be separated:

| | what it is | what it depends on | where it lives in this method |
|---|---|---|---|
| **6 h in an 8-h day** | how much of a working day is *available* to the task | the **organisation**: stand-ups, reviews of others' work, email, training, context switching | the **unit** — `1 person-day = 6 person-hours`, declared once |
| **what gets done in those 6 hours** | how much *work* a person delivers per available hour | the **person and the team** | the **values** — "adapter M = 3.5 pd" |

The 6 is roughly the same for a brilliant engineer and a mediocre one **in the same organisation** —
they both attend the same stand-up. It is a property of the working day, not of the worker. The worker
enters through the table's numbers.

So the answer to *whose 6 hours* is: **anybody's, in an organisation that runs its days this way.** And
the answer to *whose 3.5 days* is stamped on every row of `docs/rate_table.md`:

> *"Team grade assumed in every value: competent engineers, predominantly senior/middle profile,
> enterprise delivery context."*

**Every number this chain produces is conditional on that grade**, and the conditionality is stated on
the row and then never used again anywhere downstream.

## 2. How much do speeds actually differ

Figures below are **from memory and approximate**; they are the right order of magnitude and should be
checked against the sources before being quoted outside this repository. They are given because the
order of magnitude is what the argument needs.

**Individual, same task, professional programmers.** The folkloric figure is 10:1, sometimes 28:1, from
Sackman, Erikson and Grant (1968). That study is not sound for this purpose — it mixed batch against
time-sharing conditions, had few subjects, and folded debugging time in. Prechelt's re-analyses in the
late 1990s put the honest figure at roughly **2:1 to 4:1** in work time among professionals doing the
same task. That is still large, and it is the *individual* spread.

**Team against team.** Teams average their members, so team-level spread is **narrower than individual
spread** — call it ×1.5–2 between two teams of the same organisation and grade band, wider across
organisations.

**COCOMO II's personnel effort multipliers** are the estimating world's codification of the same thing.
Each spans roughly ×1.4 to ×2.0 from its worst rating to its best:

- **ACAP** analyst capability · **PCAP** programmer capability — raw capability, ~×1.8–2.0 each
- **APEX** applications (domain) experience · **PLEX** platform experience · **LTEX** language and tool
  experience — ~×1.4–1.5 each
- **PCON** personnel continuity — ~×1.6

Multiplying every extreme gives something absurd (×15 or more) that nobody has ever observed, because
no real team is at every extreme at once. **A realistic best-team-to-mediocre-team ratio on personnel
factors is ×2–3.**

**The consequence, stated bluntly.** If team capability spans ×2–3 and an instrument does not know
which team, then **that instrument cannot be accurate to ×1.3.** No amount of decomposition, case law
or rate-card discipline gets around it. The only two ways out are the ones every serious method uses:
declare the grade the numbers assume, and record the grade of the team that produced any outcome you
score against.

**This method does the first.** It has never done the second.

## 3. What that means for the FaxRxTx comparison

`docs/exit_criterion.md` scores the calibrated centre against a documented outcome. The comparison is
only defined if both sides are at the same grade — otherwise it measures the difference between two
teams and reports it as instrument error.

**The two sides are not at the same grade, and the input says so in as many words.**

- **Table's assumption:** *"competent engineers, predominantly senior/middle profile, enterprise
  delivery context."* Silent on domain experience, which for an enterprise delivery team is normally
  taken as nominal — you have done this kind of system before.
- **The actual team,** `assumptions.md` A3: *"The team **did not know the domain** — immersion in the
  subject area, discussions, and technology selection took ~1–2 months… the domain (fax protocols,
  telecom, distributed delivery) is new to the team."*

That is precisely an **APEX and PLEX** mismatch — applications experience and platform experience —
each one to two ratings below nominal. On the COCOMO scale that is worth roughly **×1.2–1.4**.

**And the residue after the two pending adjudications is ×1.24** (`run34_person_hours.md` §4).

The sizes match. That is worth stating and it is **not** worth acting on, for a reason the last two days
have made vivid: a factor that happens to be the size of your remaining gap is exactly what motivated
reasoning produces. What makes this candidate different from an invented one is that **A3 declared the
mismatch before any estimate existed** — it is in the pinned input, not in the diagnosis. That earns it
the right to be registered as a prediction. It does not earn it the right to be applied.

## 4. Registered prediction — scoreable, and not on FaxRxTx

> **P-G1.** On a second documented outcome case whose team **did** know the domain, and after the same
> two adjudications (unsizeable elements and closure violations; scope decisions), the chain's centre
> will land within **×1.15** of the fact — materially tighter than FaxRxTx's ×1.24.
>
> *Refuted by:* a same-grade case landing no closer than FaxRxTx did, which would say the residue is
> something else — most likely the vintage, or R8's element-count dependence.
>
> **Provenance:** registered 2026-08-24, before any second case exists. May never be evaluated on
> FaxRxTx.

## 5. The rules this produces

**G1 — the rate table declares its grade, and the declaration is an input, not a footnote.** It already
does; what is missing is that nothing downstream reads it. The estimate should carry the grade forward
to its own front page: *this is what a team of grade X would take.*

**G2 — an outcome is usable for calibration only if its team's grade is recorded.** `FACT.md` records
headcount and duration and nothing about who the ten people were. It is the same defect as the unit:
an outcome is an input and inputs are pinned and interrogated. A fact without a grade can score a
gross-error gate and cannot calibrate anything finer.

**G3 — the exit criterion's ×1.3 is conditional and should say so.** Proposed amendment to
`docs/exit_criterion.md`: *the gate applies to cases whose team grade is at, or has been adjusted to,
the grade the rate table declares. A case at a different grade is scored with the adjustment declared
and its size recorded, or it is not scored.* Without that clause the criterion promises an accuracy
that team variance alone forbids, and every future miss will be arguable in both directions.

**G4 — and the honest reading of the whole question the author asked.** Team variance is *irreducible*
for an instrument that does not know the team, and *removable* for one that does. Which is the same
answer the unit question got: it looked like noise in the world and it was a missing input. **Two for
two.** Before concluding that a residue is irreducible spread, the cheap move is to ask what else about
the case has never been written down.
