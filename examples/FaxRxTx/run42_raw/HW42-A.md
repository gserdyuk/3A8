# Run 42 — `Hotyn-W 1.1` × Opus 5 — FaxRxTx crossing of **HM29-OA2**, batch A

**Purpose of run 42.** The second product model of the run-29 pair (`HM29-OA2`, 87 nodes) has never
been crossed or sized; `HM29-OA1` (97 nodes) was carried all the way to 1423.2 table pd. Crossing and
pricing OA2 with **no rate changed** yields the chain's first **end-to-end** repeatability figure.
Registered as action 1 of `docs/status_2026-08-27.md` §7.

**Record status.** Instrument readings, class roster, item counts and findings are verbatim; the
per-element justification prose of §3 is distilled. `tool_uses: 0`.

**Quarantine.** Reported unprompted: branch name, repository status, commit subjects naming prior runs
of this pipeline including a `Hotyn-P` engine and "paired figures presented as counts of a prior sizing
method". Treated as data, entered nothing. **Seventh independent catch.**

## Scope

Subtrees HM2-02 (14), HM2-03 (5), HM2-04 (13) = **32 elements**. Once-scoped and per-environment
items deferred to batch C by instruction.

## Class roster — what the assembly consumes

| class | n | elements |
|---|---:|---|
| behaviour | 24 | HM2-17, 18, 20, 21, 22, 23, 24, 26, 27, 29, 30, 33, 34, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49 |
| interface | 4 | HM2-15, 16, 28, 31 |
| statement | 2 | HM2-02, HM2-03 |
| aggregate | 2 | HM2-04, HM2-40 |
| surface | 0 | — |
| store | 0 | — |

**Parents in scope (7):** HM2-02, 03, 04, 18, 26, 27, 40.

> **Structural difference from the OA1 crossing, and it must not be normalised away.** In the OA1
> assembly every node with children was forced to `aggregate`. Here the crosser ruled explicitly that
> **HM2-18, HM2-26 and HM2-27 have own coverage and are therefore priced elements *and* parents** —
> they draw K1/K2/A2/A3/A4/D4 *and* A5/A6/A7/A8/D2. Likewise HM2-02 and HM2-03 are `statement`
> parents drawing K3 plus the per-parent set. This is a genuine difference between the two models'
> crossings and is carried into the assembly as it stands.

## Item sets

- **K1, K2, A2, A3, A4** on the 28 non-aggregate, non-statement elements (24 behaviour + 4 interface).
- **K3** on HM2-02, HM2-03.
- **A10** on the 4 interfaces.
- **D4** on 30 elements — the 28 plus HM2-02 and HM2-03 (everything with own coverage).
- **per parent** on all 7: A5×2, A6×2, A7, A8, D2. **No O1** — no `surface` anywhere in these subtrees.

## Instrument readings

| reading | value |
|---|---|
| total work items | **225** |
| by activity | K1 28 · K2 28 · K3 2 · A2 28 · A3 28 · A4 28 · A5 14 · A6 14 · A7 7 · A8 7 · A9 0 · A10 4 · D2 7 · D4 30 |
| by scope | per element 176 · per parent 21 · per parent × cycles 28 |
| items per element | mean 7.03 · min 6 · max 13 (HM2-18, 26, 27) |
| `no` answers | **11 — filter 11, judgement 0** (plus 22 class-gate exclusions on the two aggregates) |
| elements untouched | 0 |
| activities eligible but unused | 5 — A9, G1, G2, G3, O1 (all scope artefacts: no store, no surface, no measurable target in these subtrees) |

## Findings (W5), carried to the assembly

- **F1 — the largest classification lever in the batch.** HM2-02 and HM2-03 carry a *parity claim*
  (F47) as own coverage while the behaviour it names lives in their children, so they classify
  `statement` and draw K3 rather than K1/K2/A2/A3/A4. A run reading them as `behaviour` gains 10 items
  and loses 2.
- **F2 — the model treats boundary integrations inconsistently.** HM2-28 declares an *adapter*
  (→ interface, A10 applies); HM2-36 declares the *production of the fax image* through a named
  third-party driver (→ behaviour, no A10); HM2-31 declares delivery into the user's mailbox
  (→ interface). Three integrations of comparable external risk, three declared contents.
- **F3 — HM2-48 declares two things in one element**, a registry (held data) and an extension point.
  Chosen `behaviour`; as two elements one would plausibly be a `store` and draw G1/G2/G3.
- **F4 — HM2-49 is one element standing for a per-format fixture across nine sibling renderers** — a
  granularity mismatch with HM2-41…47, which are enumerated one per format.
- **F5 — the PoP boundary splits across batches:** inbound HM2-15 here, outbound HM2-38 under HM2-08
  in batch C. F16 and F38 must be recombined at assembly.
- **F6 — id gaps** HM2-19, 32, 35, 50, 63 are absent by normalisation; 92 − 5 = 87 matches. Recorded so
  the assembly does not read the gaps as loss.
- **A9 open question:** F47 is a parity requirement with no stated target, so nothing pins how "the
  core function is present" would be demonstrated. Reported, not repaired.

**Where a disagreeing run would disagree:** §3 classification, and specifically the six lines the run
marked *Judgement*. Applicability produced zero judgement refusals — every pair that passed class and
condition received an item.
