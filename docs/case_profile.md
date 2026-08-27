# The case profile — pinned before any estimate exists

**Version 1.0, approved by the author 2026-08-26.** Required from case 2 onward. Case 1 (FaxRxTx)
was admitted on conventions supplied after the estimate existed and therefore sets the floor, not
the standard (`docs/status_2026-08-25.md` §5.2). This form is the stricter rule made concrete.

**The rule this form enforces:** *a case whose conditions arrive after its number can be learned
from; it cannot score.* Everything below was, on case 1, asked for after the fact — over three days,
one question at a time — and every one of those questions turned out to be a case condition, not a
requirement. All of it was available on day one.

---

## Order of pinning

1. **This profile** — filled, dated, committed. Unknowns are written as `unknown`, which is an
   answer; a field left out is not.
2. The requirement list with its md5 · the split · the assumption log · the technology declaration
   with its parameters and visible scope decisions.
3. Only then any sensor run or any estimate.
4. `FACT.md` — the outcome itself — stays sealed until the estimate is written and closed. Its
   **unit and provenance** are declared here (§5); its **number** is not.

A correction to a pinned profile is a new dated section, never an edit in place.

---

## The form

### 1. Team

| field | value |
|---|---|
| grade mix (the rate table declares the grade it assumes; state the real one) | |
| domain experience — first system in this domain, or a repeat | |
| presence fraction actually experienced (leave + holidays + sickness), if known | |

### 2. Overheads

| field | value |
|---|---|
| **net task hours a present day delivers — a number, not a description.** Default if not stated: **6** (`docs/constants.md` §4a). Run 41 showed this one figure deciding which of two instruments is closer to a fact, so `unknown` here is expensive | |
| what a booked day contains — meetings, coordination, review; declared share or `unknown` | |
| leave, holidays, sickness as a factor on present days. Default if not stated: **×1.10** | |
| what is booked to the project and what elsewhere — training, support, presale | |

### 3. Process

| field | value |
|---|---|
| the stages the delivery actually runs — concept, build, test cycles, parallel run, acceptance mode | |
| cycle counts and environment count, as the technology declaration will need them | |
| the visible scope decisions, each a named fork | |

### 4. Staffing of every separately-priced stage

One row per stage the method prices as a stage. The `W-F48` lesson: stage headcount is a
**declaration parameter**, like environment count and cycle count — a gap-blind rate author has
nothing to make one from, and any row that scales linearly in a headcount must refuse to price
until it is declared.

| stage | headcount | duration share, if known |
|---|---|---|
| | | |

### 5. The outcome's unit and provenance — without the number

The unit of a comparison is part of the comparison, and it is an input on both sides
(`docs/status_2026-08-25.md` §5.6). All of this is knowable without opening the number:

| field | value |
|---|---|
| the unit the outcome is recorded in — staffed person-months, timesheet hours, invoiced days, … | |
| what it contains — leave in or out · within-day overheads in or out · which roles | |
| how it is known — documents, timesheets, a participant's memory | |
| the stated uncertainty | |

The number itself goes to `FACT.md`, sealed.

---

## What "pinned" means

Committed before the first sensor run on the case. The estimate's report then names this profile by
its commit, so a reader can verify the order held.
