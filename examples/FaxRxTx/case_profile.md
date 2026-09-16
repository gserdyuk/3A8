# FaxRxTx — case profile (form `docs/case_profile.md` v1.0)

**Pinned 2026-09-16, before any number of the run-61 estimate exists.** Written by the orchestrator from
`SYSTEM.md` and `assumptions.md` only; no run file, report file or `FACT.md` was opened to write it.
Unknowns are written as `unknown`. A correction is a new dated section below, never an edit in place.

**Not committed.** The form asks for a commit before the first sensor run; the run-61 session was told to
run no git command that changes state. The file's md5 is recorded in `run61_raw/MANIFEST.md` before the
first sensor launch, and that is the pin this run can offer instead. Writing into `examples/FaxRxTx/` was
refused by the harness ("sensitive file"), so this file lives in the session scratchpad at the same
relative path.

**Standing disclosure.** Case 1 was admitted on conventions supplied after its earlier estimate existed
(`docs/case_profile.md`, header). This profile is written for the run-61 re-estimate; the orchestrator has
read `docs/instrument.md` §5, which states that an earlier estimate on this case landed at ×1.21 against the
outcome. The outcome's number is not known to the orchestrator; the existence of that ratio is.

---

### 1. Team

| field | value |
|---|---|
| grade mix | **unknown.** SYSTEM §6 / A3: a blended team including QA and PM, not only developers. No grade is stated |
| domain experience | **first system in this domain.** A3: the domain (fax protocols, telecom, distributed delivery) was new; ~1–2 months of immersion and technology selection. Mitigation: a working v1 is a live reference of requirements |
| presence fraction actually experienced | **unknown** |

### 2. Overheads

| field | value |
|---|---|
| net task hours a present day delivers | **unknown → the default 6** (`docs/constants.md` §4a) |
| what a booked day contains | **unknown.** Process is scrum after a planning phase (A8), so scrum ceremonies are inside the booked day |
| leave, holidays, sickness factor | **unknown → the default ×1.10** |
| what is booked to the project and what elsewhere | **unknown.** Out of scope by A1: PoP software, routing, billing, post-launch operation, v1 development |

### 3. Process

| field | value |
|---|---|
| stages actually run | a planning / immersion phase (F48, ~1–2 months calendar), then scrum development; integration tests on the real message stream compared with the old system (F49, F50); rollout to production (F51); the old version decommissionable (F52). No client acceptance stage — an internal rework in a product company (A8) |
| cycle counts and environment count | from `technology_declaration.md` §2: environments dev, stage, prod (3, a scope decision); test execution cycles 2 (policy); UAT cycles 0 |
| visible scope decisions | `C-DIRECT` vs `C-UAT` · `E-DSP` vs `E-SINGLE` · `G-SEED` vs `G-MIGRATE` · `U-OPS-USER` vs `U-NONE` (`technology_declaration.md` §1, §5); `SA-NONE` vs `SA-PENTEST` recorded as a sensitivity |
| organisation | product company (Venali, Miami), internal rework by management decision, no hard deadline but pressure; internal approvals (A8) |
| era | 2007–2009, C#/.NET ~3.x, own Windows cluster, no cloud, no ready orchestrator, no message queue (A5). The rate table is modern; the era transfer is not pre-adjusted (`technology_declaration.md` §4(i)) |

### 4. Staffing of every separately-priced stage

| stage | headcount | duration share, if known |
|---|---|---|
| F48 — domain immersion and architecture/technology selection | **unknown.** SYSTEM §6 says the team went through it; A3 removes headcount from the assumptions deliberately. Any row that scales with headcount must refuse to price until it is declared | calendar ~1–2 months (SYSTEM §6, A1) |
| F49 / F50 — parallel-stream integration testing and comparison | **unknown** | unknown |
| F51 / F52 — cutover and decommissioning | **unknown** | unknown |

### 5. The outcome's unit and provenance — without the number

| field | value |
|---|---|
| unit | **person-months of the whole team**, derived from a team size and a duration (SYSTEM §8 names exactly these three quantities as what `FACT.md` records). A9 states 1 pm ≈ 21 pd ≈ 168 h as the case's own convention |
| what it contains | whole team including QA and PM and the architecture-selection phase (A9). Leave: **unknown** — a team-size × duration figure is a staffed figure and would contain leave and within-day overheads unless the record says otherwise |
| how it is known | a project participant's **memory**, recorded 2026-07-17 (SYSTEM, source line) |
| stated uncertainty | the source hedges its own dating ("2007–2008" and "2008–2009"); no uncertainty band for the outcome is known to the orchestrator |
