# BMS — Run 10: C5 measurement, aborted (pilot data, n=2)

Date: 2026-08-06. Engine `Lytin-D 2.0` (C5 present, activity-branch scope **not yet** stated).
Prompt `prompt_decomposition_BMS.txt`, md5 `c33affd709792dfe60531daa3cb42d65`.

## What happened

Ten runs launched simultaneously. **Eight failed on the session token limit**; two completed.

**This is not a measurement and must not be treated as one.** n=2 cannot measure spread, and the two
completed runs cannot be pooled with a later batch: run9 showed that a session-to-session level difference
of roughly 10% may be real, so mixing two runs from this session with eight from another would inflate the
apparent spread by an amount indistinguishable from the effect under test. The full ten must be re-run in
one session.

## Pilot data

| Run | ΣE | Modules | Leaves | Σ leaf E | Integration | Int. share | Nodes | Fallback | M in >10 | Stamp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| V-1 | 1404.5 | 21 | 133 | 920.5 | 484.0 | 34.5% | 29 | 0 | 0 | Lytin-D 2.0 |
| V-2 | 1666.8 | 25 | 148 | 1060.3 | 606.5 | 36.4% | 34 | 0 | 0 | Lytin-D 2.0 |

Node counts are **not comparable to earlier runs**: under C5 a node exists per derived module plus per
branch plus the top-level assembly, so the count is now largely a function of module count rather than a
free choice. Whether that removes the old free parameter or merely renames it is exactly what the aborted
measurement was meant to answer.

## The one finding worth keeping

**Both runs independently identified the activity-branch gap in C5, and described it the same way.**

- V-1 logged it as exception E1: branches 1, 7, 8, 9, 10 are activity-shaped, their content is "documents,
  environments, test cycles and cutover steps, not modules", C5 derives modules from *functions*, and these
  branches "serve all functions rather than implementing any". Kept flat, split by artefact/cycle/environment.
- V-2 logged it as "a C5 note, not a C5 exception", with the same reasoning and the same treatment.

Neither run saw the other, and neither saw the project discussion in which the same gap had been named the
previous day (the "constant work" category: work that exists regardless of which functions the system has).
Three independent derivations of the same defect.

**Acted on:** C5 now states its own scope — it applies to the functional branches (2–6) only; branches 1, 7,
8, 9 and 10 carry no modules and are split by C1 directly. Version bumped to `Lytin-D 2.1`. This is a minor
change by the method's own convention: it codifies what both runs already did, so it should not move the
level.

## Status

- `Lytin-D 2.1` is on disk and will load at the next session start.
- The C5 measurement is still owed: ten runs, one session, canonical prompt, after the token limit resets.
- Baselines for that comparison: run9 (`Lytin-D 1.0`, cross-session, mean 1410, CV 10.0%) and run7
  (`Lytin-D 1.0`, within-session, mean 1284, CV 8.9%). The session confound is unresolved and bounds any
  conclusion about level to effects larger than ~10%; the node and module readings are the primary readout.
