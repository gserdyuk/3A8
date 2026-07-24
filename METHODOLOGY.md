# Multi-Method AI-Assisted Estimation Framework

## 1. The problem the framework solves

Classic Wideband Delphi removes anchoring bias through the **independence of experts** — different people with different experience and different information. Trying to carry this over to an LLM reveals that:

- One model across different sessions does not provide genuine independence — its "ceiling of ignorance" is systematic, not random (underestimation of integration and organizational risks, anchoring on the phrasing of the request — see Section 5 in the discussion archive).
- Persona engineering (different "roles" of one model) gives diversity of focus, but not diversity of the *reasoning apparatus* — under the hood the same statistical mechanism is at work.

**The key substitution:** instead of independence of *experts* — independence of *estimation techniques*. Different methods (decomposition, analogy, throughput statistics, parametric models) have structurally different, predictable blind spots — not empirically random ones, but ones guaranteed by the construction of the method. This makes the decorrelation of errors more reliable than in a human panel and, importantly, *explainable in advance*.

## 2. The methods and their constructive blind spots

| Method | What it captures well | What it cannot capture by construction |
|---|---|---|
| **Decomposition (bottom-up + PERT)** | The specifics of individual tasks | Correlation of risk across tasks; systemic/integration risks; organizational overhead |
| **Reference class forecasting** | Systemic risk as a whole, the "outside view" | The specifics of this particular task/team |
| **Throughput Monte Carlo** (from sprint history) | Organizational overhead, time fragmentation, ceremony cost — automatically, empirically | The causes of complexity; does not work without history; assumes future tasks resemble past ones |
| **Parametric (COCOMO-like)** | Independence from subjective judgment altogether | Quality depends on calibration against historical data; models age |
| **ML/regression on historical data** | Semantic patterns of similar tasks | Explainability; new task types outside the training set |

Each method is not a more accurate "competitor" to the others, but a sensor tuned to its own class of signals and blind to the rest.

## 3. The pipeline

### Step A — independent runs
Each method produces a **range** (not a point) + an explicit assumption log: what the method, by construction, did not account for. The log is not a situational diagnosis but static metadata of the method (the Section 2 table).

### Step B — diagnosing the divergence
If the methods diverge, the divergence is not averaged — it is **interpreted** through the known blind spots:
- decomposition < throughput → the difference is probably organizational overhead (ceremony + fragmentation)
- decomposition < reference_class → probably a systemic/integration risk not captured in the WBS
- throughput much wider in spread than decomposition → underestimated correlation of risk across tasks

### Step C — parameter transfer (the analog of Delphi's "round 2")
Convergence here is **mechanical, not epistemic**: the methods do not "change their minds"; one method calibrates a parameter of another.
Example: the focus factor measured from throughput (actual throughput / nominal sum of estimates over N past sprints) is applied as an explicit multiplier to the decomposition estimate.

### Step D — final range + explained residual
The goal is not a single number but a range with an explanation: how much of the spread was removed by parameter transfer, and how much remained unexplained (and that is an honest measure of uncertainty, not noise to be averaged away).

**Important:** full convergence after Step C is not necessarily a success. If the methods answer structurally different questions yet converge to a single point — it is either a coincidence, or one method was forced under another and lost its diagnostic independence.

## 4. Boundaries of applicability

- The framework yields a **range with an explanation of the sources of uncertainty**, not a single number for a contract/budget.
- It requires historical data (throughput, reference projects) — on projects with zero history only decomposition and reference class (from external data) work, and the range will be wider.
- It does not replace the team's local/tacit knowledge (the specifics of particular people, of the organization) — this is the one kind of uncertainty that no method, the LLM included, structurally covers.
