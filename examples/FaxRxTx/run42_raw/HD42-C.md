# Run 42 — `Hotyn-D 2.0` × Opus 5 — sizing of HM29-OA2, batch C (17 elements)

`tool_uses: 0`. Clean; harness injection quarantined. **Eleventh independent catch.**

## Sizes

| class | n | elements |
|---|---:|---|
| S | 8 | HM2-38, 39, 65, 67, 68, 69, 75, 76 |
| M | 6 | HM2-14, 64, 70, 71, 77, 78 |
| L / XL | 0 | — |
| **unsizeable (M10)** | **3** | **HM2-83, HM2-84, HM2-91** |

**Statement kind:** HM2-78 **behavioural** — *"which faxes and users each system serves during the
transition"* entails run-time routing while both systems run, not a policy setting.

**Seed-entity count, HM2-14: 3 → M.** All three of the store's entity kinds need pre-loading, each
with its reason: **point of presence** (the 10–20 PoPs are produced by no run of the system; nothing
can be routed or delivered until the set exists), **PoP endpoint** (F38 requires them "known and
addressable"; an endpoint is a fact about external infrastructure the system cannot discover), and
**served region / reach** (F01 fixes the reach; arguable as derived from the loaded PoP set — 2 and 3
both give M, so the class is stable).

## The unsizeable three — a structural defect, not a batch artefact

HM2-83 (portal authentication and session), HM2-84 (NOC operator authentication and roles), HM2-91
(portal credential recovery). All three are `derived`, all three have **no own coverage**, and **no
obligation anywhere in the list names authentication, session, role or credential recovery** — while a
customer portal (F35) and an internal control centre (F31) both exist and both presuppose identity.

The run refused to guess: *"To enumerate distinct actions the declared content names I would have to
supply the actions myself."* It also named the consequence — because D4 sits only on elements with
coverage, **no work item anywhere in the model produces the declaration whose absence makes them
unsizeable.** The gap closes on itself.

## Two doubts that cross a threshold

- **HM2-78 sized M on 4 constrained components** (new system, old system, PoPs, archive). A shared
  user directory read as a fifth component gives **L**. The run counted 4 because the content names
  users as *subjects of the split*, not as a component.
- **HM2-38 sized S on 1 operation.** If F38's fan-out ("delivered to **each** served PoP") is a
  distribution operation distinct from F16's single-archive send ("to *a* point of presence"), it is M.

**Contradiction named and not resolved:** F16 sends one archive to *the one* PoP chosen by least-cost
routing; the F38 part on the same element has archives "delivered to each served PoP". Different
obligations. Sized once, on each obligation's stated reading.

## Closure violations: 3

1. **Requirement acquisition for the three authentication behaviours** — no work item in the model
   produces the declaration they lack.
2. **Handling of a failed PoP handoff** — F16/F38 declare delivery only; nothing covers a delivery
   that does not succeed, nor how the operator learns of it.
3. **Termination of the coexistence arrangement** — F43 binds coexistence "for the duration of the
   transition"; nothing covers ending it and releasing the shared PoP and archive access.

**Model-level finding:** F35 is *"User portal — the users' website"*, with no functional detail given
anywhere, yet three surfaces rest on it and each declares a specific part. Those parts are **not
derivable from the obligation's text** — the enumerations rest on the model's declaration alone.
Sized as declared, and recorded here that the obligation does not carry it.
