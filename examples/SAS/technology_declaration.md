# SAS — technology declaration (`Hotyn-W` input)

**Approved by the author 2026-09-08.** One choice per dimension, drawn from
`docs/technology_catalogue.md` **1.4**. A run chooses nothing and invents nothing: this file and the
catalogue together fix which activities exist before the crossing in W3 begins.

Every choice is justified from a **pinned input** — `requirements_pinned.md` (ids) or
`assumptions.md` (A-ids) — or is marked as a **scope decision made here, visibly**. There are three
of those.

---

## 1. The declaration

| dimension | choice | drawn from |
|---|---|---|
| construction | **`K-BESPOKE`** — bespoke web application on a mainstream stack | NFR-1 no platform constraint · NFR-7 web-based on industry-standard frameworks · NFR-4 service-oriented, REST. Nothing in the RFP names a product to configure |
| assurance | **`A-TB`** — test-based | W-2 "Development and Testing" · NFR-15 performance testing · A2 makes acceptance passed part of done. Nothing asks for formal methods |
| acceptance | **`C-UAT`** — staged user acceptance with sign-off | §1 Introduction: the contract term covers "design, development, testing, and acceptance" · W-3 Implementation · A2 |
| delivery process | **`D-TEAM`** — one team with planning and reporting ceremonies | **Scope decision, visible.** The RFP names no site and no team; the document header names an outsourcing vendor, which makes `D-DISTRIBUTED` arguable. Declared `D-TEAM` for comparability with both earlier cases; the case profile is where the real delivery organisation is stated, and the sensitivity is priced in §5 |
| environments | **`E-DSP`** with **four** environments | NFR-11 names development, test, staging/pre-production, production. The dimension's activities are unchanged; the count is a parameter. The `E1` mapping for the fourth environment is declared in §2 |
| data | **`G-MIGRATE`** — migration from a predecessor system | NFR-12 migration of current application data including users · A16 names the source and the seven entity kinds. **First case in the project to declare this dimension** |
| documentation | **`U-OPS-USER`** — operational and user documentation | NFR-9 backup and recovery procedures · NFR-8 failover process · G-10 help content · W-4 hand-over · A2 |
| security & compliance assurance | **`SA-PENTEST`** — external penetration test and remediation | **Scope decision, visible.** NFR-10 demands a security design and security processes; NFR-3 puts authentication on claims; I-10 opens part of the system to the anonymous public; NFR-7 projects 256 000 users. None of these *names* a penetration test; `SA-NONE` removes exactly three items |

## 2. Parameters

| parameter | value | kind |
|---|---:|---|
| environments | dev, test, stage, prod | **4**, from NFR-11 |
| `E1` class of the fourth environment | **test = M** | **catalogue amendment proposal** (A17): catalogue 1.4 §3a fixes dev = S, stage = M, prod = L and names no fourth; `test` is a shared integration environment and takes the M row. No new table row is needed. Recorded here until the catalogue is bumped to 1.5 |
| test execution cycles | 2 | policy choice: one pass plus a regression pass after fixes — **identical to BMS and FaxRxTx**, deliberately |
| UAT cycles | 2 | policy choice, same shape — identical to BMS |
| migration rehearsal cycles (`G5m`) | 2 | policy choice: one full rehearsal, one repeat after fixes. **First use of this parameter**; A16 |

All cycle counts are policy parameters, not estimates. Their effect is linear — A5, A6, U2, U3 and
G5m are the only activities they multiply.

---

## 3. W6 — demanded work under this declaration

`requirements_work.md` carries seven demanded items and registered, before this file was written:
six absorbed, W-4 partial.

| id | demanded | absorbed by | status |
|---|---|---|---|
| W-1 | Requirements and Design | **D4** requirement elaboration · **K1** element design · **A1** test strategy · **S1** security design review | **absorbed** — the stage is the union of what four dimensions mandate |
| W-2 | Development and Testing | **K2, K3** · **A2–A10** | **absorbed** |
| W-3 | Implementation | **E1** ×4, **E2**, **E3**, **E6** · **G1m–G5m** · **U1–U4** | **absorbed** |
| W-4 | Post-production Support and Transition | **O3** support handover pack · **E6** production cutover | **partially** — the hand-over is priced; the support period is **carried, not priced** (A1): missing parameters, the term and the service level |
| NFR-11 | deployment to four environments with deployment processes | **E1** ×4 · **E2** build and deployment pipeline · **E3** promotion procedure | **absorbed** |
| NFR-12 | migration of current data and users | **G1m–G5m** | **absorbed** |
| NFR-15 | performance testing processes against the response-time targets | **A9** on NFR-14 (five measurable targets) | **absorbed** |

Two clauses on product-side entries are absorbed as pointers (S3): I-7's "business rules … defined
as part of the project" by **D4**; NFR-5's conditional impact analysis is carried at count 0 (A1).

**Outcome: six of seven absorbed, one partial — as registered.** Nothing stands alone. This is the
first case where no demanded item escapes the catalogue, and it is worth saying why it proves little:
the RFP's demanded items are the names of the lifecycle stages, and a catalogue built as a lifecycle
absorbs them by construction. The catalogue is tested by FaxRxTx's four standing items, not by these.

---

## 4. What this declaration cannot settle, recorded before the runs

**(i) The delivery organisation.** `D-TEAM` is declared from nothing in the RFP; the real
organisation is a case condition and belongs in `case_profile.md` §3. If the profile states two
sites, this line changes and `D7` enters per aggregate — a new declaration, not an amendment.

**(ii) The era.** The RFP is from September 2018; the rate table is compiled from modern norms. As on
FaxRxTx, the transfer is not pre-adjusted, and the era is a named candidate explanation of whatever
the comparison later shows. The distance is eight years, not seventeen.

**(iii) Migration volume.** `G2m`–`G4m` are sized per store element by entity kinds; nothing in the
table scales with record counts, and NFR-2's 10 million GIN records enter no rate. If volume turns
out to matter, it is a table finding, named here first.

---

## 5. Declared sensitivities — what a different declaration would do

| change | effect on the work model |
|---|---|
| `D-TEAM` → `D-DISTRIBUTED` | adds `D7` cross-site coordination per aggregate; everything else unchanged |
| `SA-PENTEST` → `SA-NONE` | removes exactly three once-scoped items: `S1`, `S2`, `S3` |
| test environment M → S | one `E1` item moves down one class |
| migration rehearsal cycles 2 → 1 | removes one `G5m` item |

---

## 6. Pins

```
input                             md5 / version
requirements_product.md           see requirements.pin.txt   (N = 146)
requirements_work.md              see requirements.pin.txt   (N =   7)
requirements_pinned.md (parent)   see requirements.pin.txt   (N = 153)
docs/technology_catalogue.md      version 1.4, 2026-08-22 (+ the E1 mapping proposal of §2)
docs/rate_table.md                v0.1-h  (consumed at assembly, never by a sensor)
```

Drafted 2026-09-08. Once approved, changing any line of §1 or §2 is a new declaration and a new
run — not an amendment to this one.
