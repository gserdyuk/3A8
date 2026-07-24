# 3A8 (Triangulate) — estimation you can defend, for the AI-assisted era

**The problem.** Project estimation is chronically wrong — and almost always in one direction, toward underestimation. AI doesn't cure this; it makes it worse: asking an LLM to estimate feels easy, but its answer swings more than a human's would. A single model asked several times gives not independent opinions but well-anchored guesses.

**The idea.** Wideband Delphi rests on the independence of experts — which an LLM cannot supply. 3A8 replaces independence of experts with independence of techniques: different estimation methods have blind spots that are guaranteed by construction, not random. The output is a range with an explained residual, not a single number.

**How it works.** The same project is estimated two independent ways: bottom-up from the WBS (sum of leaves + PERT), and top-down by analogy to a similar past project (reference class). They disagree — and the direction of the disagreement is diagnostic: for example, if the WBS sum is below the analogy, the WBS missed the seams between tasks (the sum of leaves carries no charge for integration). We don't average — we calibrate one method with the other.

**The ask — an opinion.** Does the approach hold up, and could it apply at the company?

*Next: more projects for validation, then automation as isolated agents, one per method.*
