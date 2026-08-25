# BMS — Run 28: conditional prices for the four step events — the options table

Date: 2026-08-22. **Registered before the run returned.** Resolves U5 by the author's decision of
2026-08-22: **both halves** — the bid goes out conditional on the pinned readings (tail-less on its
face), *and* carries a priced options table for the four refused readings, so the reserve decision
becomes the client's, with a price on it.

## Design

One gap-blind run through `rates-step-c` (`Lytin-K 1.0`), Opus 5. Input: project description ·
the four events with their taken and refused readings · the base's relevant composition (gap-free) ·
**computed per-item E facts from the pinned rate table** (so conditional arithmetic is table-derived,
not invented). **Not in the input:** class quantiles, the diagnosis, the calibrated centre, any
target. The run prices **conditional magnitudes only — no probabilities**: a step event's likelihood
is the client's information or a separately-sourced act, never part of this table.

Each event's row must state its **netting rule** — what already-priced base work the delta replaces
or subsumes if the event fires — so an option price can never double-count the base.

## Registered expectations

1. **Clean**, and the run confirms what it was not given.
2. **Four rows**, each: trigger (the refused reading, verbatim) · netting rule against the base ·
   conditional delta **low / central / high in pd** · external basis · form (conditional pure
   addition / replacement).
3. **R15's row is a formula, not a point**: the count of direct integrations is genuinely unknown,
   so the honest price is per-integration cost × N, quoted with illustrative N points — not a
   pretended total.
4. **No probabilities anywhere**, stated explicitly.
5. **No event nets below zero** and none of the four is priced by widening a global — each is a
   named conditional object, per the rate agent's own "a multiplier cannot express a step" rule.

---

# Results

Raw: `run28_raw/options.md`, verbatim, with the orchestrator completing the one thing the run
refused to proceed without silently — the base's engine stamp, which the task omitted (a prompt
defect, caught by the sensor and closed in the transcription header).

## Scoring the registered expectations

| # | expectation | outcome |
|---|---|---|
| 1 | clean + confirms what it was not given | **CONFIRMED** — every numeral in the prompt checked and classified; and the run independently caught the `gitStatus` environment leak (second sensor to do so), repeating the strip recommendation |
| 2 | four rows with trigger/netting/bands/basis/form | **CONFIRMED — and exceeded in the spec's own spirit**: a fifth row (X-13, the E-1∧E-3 interaction, priced because its sign is unambiguous) and one **refused** interaction (E-3×E-4 — "I cannot source the sign, so I price nothing and name it") |
| 3 | E-1 as a formula, not a point | **CONFIRMED** — per-integration unit 12.8/23.6/51.6 + programme once-costs 45/124/149; N quoted as a client-supplied axis "never to be read as a central case"; the N≥24 tier effect stated, not baked in |
| 4 | no probabilities | **CONFIRMED**, and promoted to a binding constraint on every later step |
| 5 | no negative nets, no globals | **CONFIRMED** — "no global multipliers are emitted; the two-global budget is untouched" |

## The options table (headline figures, pd)

| event | netting | low | central | high |
|---|---|---:|---:|---:|
| **E-1** direct integrations | aggregator stays (switch) | 12.8/unit + 45 once | 23.6/unit + 124 | 51.6/unit + 149 |
| — illustrative N=10 / 20 / 30 | | 173 / 301 / 429 | 360 / 596 / 832 | 665 / 1181 / 1697 |
| **E-2** own SMS infrastructure | gateway replaced (−18…−20) | 60 | 178 | 239 (+5/10/20 switch: carrier onboarding, zeroable) |
| **E-3** disruption-response capability | none — additive | 112 | 212 | 288 |
| **E-4** configurable process engine | H2 superseded (−5/−15/−40) | 117 | 192 | 252 |
| **X-13** if E-1 **and** E-3 both fire | — | 12 | 22 | 37 |

**U5 is closed** by the author's both-halves decision: the bid goes out conditional on the pinned
readings, with this table attached as pre-priced options — the reserve decision becomes the
client's, with a price on it. Recorded in `estimate_BMS_2026-08-22.md`.
