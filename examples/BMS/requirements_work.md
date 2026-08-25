# BMS — demanded-work list (`Hotyn-W` input)

Derived from `requirements.md` (md5 `554ea3608dd0602f0ddf2f7e7b82178c`, N=73) by the split recorded in
`requirements_split.md`. These are the obligations the client places on **the work**, not on the
product. **Ids are unchanged.** The complementary list is `requirements_product.md` (N=68).

Per `docs/proposal_product_model.md` W6, these items do **not** pass through `Hotyn-M`. They enter the
work model directly, as their own branches, each carrying the requirement id that demands it.

**A run may not add, remove, split or merge entries**, exactly as for the product list.

---

## The list

| id | obligation on the work | what it obliges the Supplier to do | source section |
|---|---|---|---|
| R02 | The Supplier hosts the system | run the system on infrastructure the Supplier provides | Project Overview |
| R03 | The Supplier supports the system | operate a support function for the system in service | Project Overview |
| R64 | Keep technologies up to date; periodic reviews and planned upgrades | review the stack periodically and plan and perform upgrades | NFR / Architectural |
| R69 | Configuration management and version control across all environments and documents | maintain configuration management and version control | NFR / Configuration Management |
| R70 | Robust release and patch promotion procedures minimising business impact | define and operate release and patch promotion procedures | NFR / Deployability |

**N = 5.**

---

## W6 pointers — resolved by the declaration, 2026-08-20

An item that is **both** demanded here and mandated by the declared technology is recorded **once**,
in the technology-derived branch, and its entry here is marked *accounted for*. It then produces no
branch of its own. Counting it twice would double the work; keeping it on this side would scatter
technology work across two branches according to whether the client happened to write it down.

Against `technology_declaration.md` (catalogue 1.0):

| id | absorbed by | status |
|---|---|---|
| R02 | `E7` hosting set-up — tenancy, capacity, runtime | **partial.** The hand-over residue is priced; running the service is carried, not priced (A1) |
| R03 | `O3` support handover pack | **partial**, same shape |
| R64 | — | **not absorbed.** No dimension mandates a technology-currency programme. Stays a demanded branch with one item: *agree and record the currency and upgrade policy*. The periodic reviews themselves are carried, not priced (A1) |
| R69 | `E4` configuration management and version control set-up | **absorbed** |
| R70 | `E3` promotion procedure, defined and rehearsed | **absorbed** |

**Registered expectation versus outcome.** Before the catalogue was written, this file predicted that
three of five would be absorbed and warned that absorbing none would mean the catalogue was missing
dimensions. Outcome: **two absorbed outright, two partially, one not at all.**

R64 is the informative one. **It is a demanded obligation that no way of building implies** — a
commitment about the years after delivery, and none of the eight dimensions has anything to say about
them. It is the only work in the model that traces to a requirement and to no activity.

---

## The A1 dispute — resolved 2026-08-20, and how

`assumptions.md` v1 said "not included: subsequent operation (hosting & support), user training, the
warranty period", which struck out exactly what R02, R03 and R64 demand. Run 18 (HM-OA) caught it on
R03; the split showed it was systematic.

**The resolution is not a scope decision but a rule.** `assumptions.md` v2 A0: *an obligation the
client stated cannot be removed by an assumption.* A log may bound what a number prices, and must then
name either the instrument that prices the rest or the parameter that is missing. If an id appears
neither in the priced work nor on the carried list, **the run raises an exception and emits no
estimate.**

Under that rule the three entries resolve without anybody deciding to shrink the project:

| | priced by this estimate | carried, not priced |
|---|---|---|
| R02 | `E7` — the hosted service exists at hand-over | running it. Missing parameter: **the term** |
| R03 | `O3` — support is possible at hand-over | operating the support desk. Missing parameter: **the term** |
| R64 | the policy is agreed and recorded | performing the reviews and upgrades. Missing parameter: **the term** |

**The question that goes back to the client:** over what period do R02, R03 and R64 run? Until it is
answered, no effort figure for them exists — a continuing obligation is priced by a rate per unit
time, which is a different instrument from this one.
