# SAS — case profile

**Form:** `docs/case_profile.md` v1.0. **Status: approved by the author 2026-09-08, pinned by the commit that carries it.** Fields the
RFP settles are filled from it; the team, the delivery organisation, the presence convention and the
absence of an outcome were stated by the author on 2026-09-08; the remaining `unknown` fields are
recorded as such. Per the form, `unknown` is an answer and a field left out is not; the defaults of
`docs/constants.md` §4a apply wherever `unknown` stands.

**The rule this file enforces:** a case whose conditions arrive after its number can be learned
from; it cannot score. Nothing below may change after the first sensor run except by a new dated
section.

---

### 1. Team

| field | value |
|---|---|
| grade mix | **middle/senior mix** — stated by the author 2026-09-08. Matches the grade the rate table declares |
| domain experience — first system in this domain, or a repeat | **first system in this domain** — stated by the author 2026-09-08 |
| presence fraction actually experienced | **×1.10 leave**, holidays 0, sickness 0 — confirmed by the author 2026-09-08 (the §4a convention) |

### 2. Overheads

| field | value |
|---|---|
| net task hours a present day delivers | **6** — confirmed by the author 2026-09-08 (the §4a convention) |
| what a booked day contains | **unknown** |
| leave, holidays, sickness as a factor on present days | **×1.10** — confirmed by the author 2026-09-08 |
| what is booked to the project and what elsewhere | **unknown** |

### 3. Process

| field | value |
|---|---|
| the stages the delivery runs | from the RFP §1 Project Structure: **requirements and design · development and testing · implementation** (deployment through four environments, data migration with rehearsals, user acceptance, production cutover) · **post-production support and transition** (term unknown; carried, not priced — `assumptions.md` A1) |
| cycle counts and environment count | environments **4** (NFR-11) · test execution cycles **2** · UAT cycles **2** · migration rehearsal cycles **2** — `technology_declaration.md` §2 |
| the visible scope decisions, each a named fork | `D-TEAM` vs `D-DISTRIBUTED` (declared `D-TEAM`; confirmed by the author: one site) · `SA-PENTEST` vs `SA-NONE` (declared `SA-PENTEST`) · fourth environment `E1` = M vs S (declared M) · NFR-5 impact analysis count 0 vs ≥1 (declared 0) |
| delivery organisation — one site or distributed | **one team, one site** — stated by the author 2026-09-08 |

### 4. Staffing of every separately-priced stage

| stage | headcount | duration share, if known |
|---|---|---|
| mobilisation (`D1`) | unknown | — |
| user acceptance support (`U2`, `U3`) | unknown | — |
| migration rehearsal (`G5m`) | unknown | — |
| production cutover (`E6`) | unknown | — |
| post-production support (W-4) | unknown — carried, not priced | term unknown |

No rate row in v0.1-h scales linearly in a headcount, so no row refuses to price on these unknowns;
they are recorded because the form requires the question to be asked before the number exists.

### 5. The outcome's unit and provenance — without the number

| field | value |
|---|---|
| does a comparison figure exist for this case? | **no** — stated by the author 2026-09-08: no known outcome. `FACT.md` will not exist. The case can score gate tests 1 (repeatability) and, given a human scale, 2 (position); it **cannot** score test 3 (calibratability) |
| the unit it is recorded in | n/a |
| what it contains | n/a |
| how it is known | n/a |
| the stated uncertainty | n/a |

If a figure exists, it goes to `FACT.md`, sealed, and its provenance is declared in this table first
— **a bid or group-consensus estimate is declared as such so that nobody later scores calibration
(gate test 3) on it**; only an outcome can do that.

---

## What "pinned" means

Committed before the first sensor run on the case. The estimate's report then names this profile by
its commit, so a reader can verify the order held.
