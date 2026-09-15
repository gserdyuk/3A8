# Run 54 — the discriminating replay of run 53 stage 1, `Hotyn-M 1.1`, n = 2 — VOID

**2026-09-15.** Intended as run 53 verbatim with one of its three co-moving factors removed: the output-limit
continuation, to be removed by a bounded thinking budget (`MAX_THINKING_TOKENS=16000` in the orchestrating process).
The other two factors were held: the plugin entry point, and run 53's framing (its prompt was recovered from its
transcripts and replayed, identical except the final newline).

Launch record, gate, pins, per-turn audit and deviations: `run54_raw/MANIFEST.md`. No raw replies: neither sensor
emitted any text.

---

## 1. Protocol facts

**No model was produced.** Both sensors were aborted by the harness's stream watchdog ("no progress for 600s"), in
the same millisecond, about five hours after launch. HM54-2 never completed a turn. HM54-1 completed one.

**The manipulation was not in force.** HM54-1's one completed turn was thinking only. It stopped at `max_tokens` with
**64 000** output tokens after 12 min 57 s, and the harness injected the same continuation message as in run 53
("… Break remaining work into smaller pieces."). Run 53's first turns: 64 000 tokens each, 12 min 10 s and 12 min
30 s. With the budget set, the sensor thought exactly as long as without it. Run 54 therefore did not remove factor 3,
even before the transport failure.

---

## 2. The readings, beside run 44 and run 53

| reading | HM54-1 | HM54-2 | HM53-1 | HM53-2 | run 53 ratio | run 44 OA1 | run 44 OA2 | run 44 ratio |
|---|---:|---:|---:|---:|---|---:|---:|---|
| skeleton (posited) | — | — | 64 | 74 | ×1.16 | 72 | 69 | ×1.04 |
| accretion (accreted) | — | — | 43 | 64 | ×1.49 | 160 | 167 | ×1.04 |
| **anchored (posited + accreted)** | **—** | **—** | **107** | **138** | **×1.29** | **232** | **236** | **×1.017** |
| completion (derived) | — | — | 10 | 12 | ×1.20 | 27 | 20 | ×1.35 |
| nodes after normalisation | — | — | 117 | 150 | ×1.28 | 246 | 242 | ×1.017 |
| leaves after normalisation | — | — | 103 | 133 | ×1.29 | 187 | 187 | ×1.00 |
| coverage assignments | — | — | 239 | 281 | ×1.18 | 257 | 279 | ×1.086 |
| obligations placed / unplaced | — | — | 146 / 0 | 146 / 0 | — | 146 / 0 | 146 / 0 | — |
| Jaccard within the pair | — | | 0.569 | | | 0.451 | | |
| Jaccard against run 44 members | — | — | 0.252 / 0.325 | 0.360 / 0.343 | | | | |
| Jaccard against run 53 members | — | — | | | | 0.252 / 0.360 | 0.325 / 0.343 | |
| **first turn: stop · output tokens** | **`max_tokens` · 64 000** | none completed | `max_tokens` · 64 000 | `max_tokens` · 64 000 | | *not audited* | *not audited* | |
| continuation messages injected | 1 (before the stall) | 0 | 1 | 2 | | *not audited* | *not audited* | |

"—" = no reply, nothing to parse. The run 44 and run 53 figures were re-computed with run 53's compare script before
this run failed, and match their records exactly. Cross-run Jaccards are given as "vs OA1 / vs OA2" and
"vs HM53-1 / vs HM53-2".

---

## 3. The reading, and what would overturn it

**R8 — Run 54 decides neither branch. Setting `MAX_THINKING_TOKENS=16000` in the orchestrator's environment does not
bound a `3a8:model-builder` sensor on claude-opus-5: its first turn still thinks to the 64 000-token output limit and
receives the continuation instruction.** So the plugin entry point is neither cleared nor convicted, and run 53's
three factors are still confounded. The pre-registered readings, "≈ 232 at ×1.02 clears the entry point" and "≈ 120
again keeps it", did not become applicable. No structure was built, and the factor they assumed removed was present.

What this run does add is one fact about the lever. HM54-1 shows that the thinking-only first turn reproduces run 53's
exactly in length (64 000 tokens) and in duration (±1 min), under a budget of 16 000. A replay that reaches a reply
through this process would therefore be a third run-53 condition, not a discriminating one. That is why this run was
not relaunched.

*Overturned by:* a transcript of a sensor launched under the same setting whose first turn ends below 16 000 output
tokens, or ends `end_turn` with no continuation message. That would show the budget can take effect and this run's
64 000 was incidental. HM54-2 never completed a turn, so it cannot supply that transcript.

**Before any relaunch of run 54**, establish a lever that demonstrably changes the sensor's first turn. The check is
the audit this manifest already uses: turn 1 not `max_tokens`, no `isMeta` continuation. That costs one sensor's first
turn, about 13 minutes. Only then spend the n = 2 replay.

---

## 4. The model carried forward

None from this run. Run 53's record (§5) still stands as written: `HM53-1` is the model stage 2 would cross, and
whether stage 2 waits for the discriminating relaunch is still the stage 2 launch's decision.

- **Copied into place** 2026-09-15 from the child session scratchpad by the orchestrating session, byte for byte.
