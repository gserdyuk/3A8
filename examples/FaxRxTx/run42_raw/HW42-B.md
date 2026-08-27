# Run 42 — `Hotyn-W 1.1` × Opus 5 — FaxRxTx crossing of **HM29-OA2**, batch B

Subtrees HM2-05 (10), HM2-06 (13), HM2-07 (8) = **31 elements**. Once-scoped and per-environment
deferred to batch C. `tool_uses: 0`. Quarantine reported unprompted (branch, status, commit subjects
including "run 40", "UFP 78 vs 82"); treated as data. **Eighth independent catch.**

Readings and counts verbatim; per-element justification prose distilled.

## Class roster — what the assembly consumes

`HM2-05=aggregate · HM2-54=behaviour · HM2-55=store · HM2-56=behaviour · HM2-57=behaviour ·
HM2-58=behaviour · HM2-73=behaviour · HM2-81=behaviour · HM2-82=behaviour · HM2-85=behaviour ·
HM2-06=aggregate · HM2-51=aggregate · HM2-52=surface · HM2-53=surface · HM2-66=behaviour ·
HM2-72=behaviour · HM2-74=store · HM2-79=behaviour · HM2-80=behaviour · HM2-87=behaviour ·
HM2-89=behaviour · HM2-90=statement · HM2-92=statement · HM2-07=aggregate · HM2-25=store ·
HM2-59=store · HM2-60=store · HM2-61=store · HM2-62=behaviour · HM2-86=behaviour · HM2-88=store`

**Tally:** behaviour 16 · store 7 · aggregate 4 · surface 2 · statement 2 · interface 0.
**Parents in scope (4):** HM2-05, HM2-06, HM2-07, HM2-51.

## Item sets

- **K1, K2, A2, A3, A4** on 25 elements: HM2-54, 55, 56, 57, 58, 73, 81, 82, 85, 52, 53, 66, 72, 74,
  79, 80, 87, 89, 25, 59, 60, 61, 62, 86, 88.
- **K3** on HM2-90, HM2-92 (and nothing else — these two take K3 alone, 1 item each).
- **D4** on 21 elements (those with own coverage): HM2-54, 55, 56, 57, 58, 73, 81, 82, 52, 53, 66, 72,
  74, 79, 80, 89, 25, 59, 60, 61, 62.
- **G1, G2, G3** on 4 stores only: HM2-74, HM2-25, HM2-61, HM2-88.
- **per parent** on all 4: A5×2, A6×2, A7, A8, D2. **O1** on HM2-06 and HM2-51 only (surfaces in subtree).
- **A9 and A10: zero in this batch.**

## Instrument readings

| reading | value |
|---|---|
| total work items | **190** |
| by activity | K1 25 · K2 25 · K3 2 · A2 25 · A3 25 · A4 25 · A5 8 · A6 8 · A7 4 · A8 4 · A9 0 · A10 0 · D2 4 · D4 21 · G1 4 · G2 4 · G3 4 · O1 2 |
| by scope | per element 160 · per parent 14 · per parent × cycles 16 |
| items per element | mean 6.13 · min 1 (HM2-90, HM2-92 — K3 only) · max 9 (HM2-25, 61, 74) |
| `no` answers | **23 — filter 14, judgement 9** |
| elements untouched | 0 |

**The nine judgement refusals are one reading applied three times:** a store whose entire content is
produced at run time takes no seed-data work under `G-SEED`. Applied to HM2-55 (token store), HM2-59
(fax archive), HM2-60 (working files) — each losing G1, G2, G3. Judgement share 39%, against batch A's
**zero**. That asymmetry is itself a reading about where the two batches' freedom sat.

## Findings (W5), carried to the assembly

- **F-2 — the internal API can receive no contract test, and no declared activity would give it one.**
  HM2-62 is the one element whose declared content *is* a contract, but `interface` is defined as an
  exchange with a system **outside** this one, so HM2-62 is `behaviour` and A10 cannot reach it. Either
  the class definition or A10's applicability is too narrow for this product. **No activity invented.**
- **F-3 — the model's principal capacity content produces no performance-test item.** F36/F37 live in
  HM2-72 and HM2-73, both classified `behaviour` because their content describes run-time acts
  (allocating, accepting, holding, draining). A9 is restricted to `statement` and reaches neither. So
  a stated capacity target yields design, build, test-design, unit-test and review items and **no A9**.
  Either A9's applicable class is wrong for a model expressing capacity as mechanisms, or these two
  should have been statements. **For the assembly to adjudicate.**
- **F-4 — HM2-74 bundles a data roster and an infrastructure property** in one element; crossed as it
  stands on the roster reading, so it carries G1/G2/G3 and the topology half is worked only incidentally.
- **F-5 — one item hangs on HM2-85's class.** Read as `behaviour` (the system emits a notification);
  had it been `surface`, HM2-05 would have passed O1's condition and gained a user-documentation item.
- **F-6 — open question:** HM2-90 declares a discipline over cluster clocks and states no measurable
  target. What agreement bound must they hold? Passed up, not answered.
- **F-7 — overlap to confirm at assembly:** HM2-87 (component deployment, an element here) against E2
  (build/deploy pipeline, once-scoped in batch C). Formally distinct traces; confirm they are not the
  same work twice.

**The batch's own most consequential judgements:** HM2-90 and HM2-92 are `derived` elements whose whole
declared content is their name phrase. Read as `statement` they take K3 alone; read as `behaviour` each
would take K1/K2/A2/A3/A4 — **+8 items in the batch.**
