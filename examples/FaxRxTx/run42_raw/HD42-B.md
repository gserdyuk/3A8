# Run 42 — `Hotyn-D 2.0` × Opus 5 — sizing of HM29-OA2, batch B (27 elements)

`tool_uses: 0`. Clean; harness injection quarantined. **Twelfth independent catch.**

Judged explicitly **not** contamination, and the reasoning recorded: F36, F37 and F39 carry quantities
(daily fax volume, burst multiple, node count). Those are **domain volumes and machine counts** —
properties of the thing built, not of the work of building it. Where such a figure carried a time unit
the run referred to it by name rather than reproducing it, so no time-bearing number entered its output.

## Sizes

| class | n | elements |
|---|---:|---|
| S | 12 | HM2-25, 53, 55, 56, 58, 59, 60, 61, 62, 79, 85, 90 |
| M | 14 | HM2-54, 57, 66, 72, 73, 74, 80, 81, 82, 86, 87, 88, 89, 92 |
| L | 1 | HM2-52 |
| XL | 0 | — |

**Statement kinds — both `compliance`:** HM2-90 ("clock discipline" — a configuration held by machines,
no run-time scenario) · HM2-92 ("version consistency across nodes" — a state of configuration).
Against batch A's two **behavioural** statements, this is the split the rate table prices most sharply:
`K3 compliance` is a fraction of `K3 behavioural` at every size.

**Seed-entity counts:** HM2-74 → **M** (cluster node, private-network topology entry; node role judged
*not* pre-loaded) · HM2-25 → **S** (per-user delivery preference: the first fax to a user has no
decidable format until the row exists) · HM2-88 → **M** (subscriber, fax number) · **HM2-61 →
unsizeable, model defect (M10)**.

## The HM2-61 refusal, and why it matters

The model places G1/G2/G3 on "System database schemas" while F28 states only *"A database is part of
the system (the DBMS is not specified)"* and F29 names only a hand-over mechanism. The run counted the
store itself at 1 entity kind → S, and refused the seed count outright:

> *"The model places G1/G2/G3 on this store while declaring no entity kind that must exist before the
> system is usable. I will not invent reference or configuration tables to fill the gap."*

It also stated its own boundary, so the call is auditable: had F29 not named the hand-over record,
**HM2-61 would have been reported unsizeable outright** — F28 alone supports no entity enumeration.

**The OA1 sizing refused the seed count of its own `HM1-61` on the same ground.** Two independent
model builds, two independent sizers, the same element, the same defect, the same refusal.

## Doubts: 30 — of which 21 class-changing

The largest is **D22, HM2-61**: the name says "schemas" (plural) and the model puts seed work on it,
yet no schema and no DBMS is named anywhere. Counted at what is named (1 → S). *If the element is
intended to carry the system-wide persistent model, the true count runs far past L and the class
changes materially.* Not resolved by the sizer, and it is the single largest unresolved size in OA2.

**Two obligation contradictions named and left standing:**

- **D27** — F22 excludes a job queue and deliberately excludes MSMQ, while F21 and F34 name "queue
  lengths" and "the state of the queues" shown by the NOC. Proceeded on HM2-66's coverage: the figures
  are per-stage backlogs read from the token store.
- **D28** — F21 is annotated *"no further detail given anywhere in the source"*, yet HM2-52's declared
  coverage names four specific control actions. **HM2-52's `L` — the batch's only L — rests entirely on
  detail the obligation says does not exist.** Sized as declared; the conflict is named, not resolved.

## Closure violations: 6

1. **Exclusive claim under contention** — any free node claims the next token with no broker beneath,
   and idempotence is declared only *during recovery*. Nothing declares two nodes claiming one token at
   the same instant.
2. **Private-network partition** — the roster splits, each half believes the other lost; precisely the
   case where a broker-less claim is granted twice.
3. **Retention and purge of the token store** — HM2-86 covers archive and working files only; nothing
   prunes terminal tokens from an unordered store holding one record per fax at the declared volume.
4. **Authorisation and audit of node control actions** — an operator may take a node out, put it back
   and redistribute its work; nothing declares who may, or that it is recorded.
5. **System-level demonstration of the declared volumes** — every test item is element-scoped; nothing
   demonstrates the assembled pipeline carries the nominal volume or the burst multiple.
6. **Delivery retry before non-delivery is declared** — confirmation raises the unconfirmed fax and the
   user is notified, with no attempt-again path between the two.

Items 1, 2 and 3 are the deepest: all three are failure modes of the hand-rolled broker-less
orchestrator, which every one of run 41's ten no-method baseline runs independently named as the
project's largest cost driver.
