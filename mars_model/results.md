# mars_model — checking the §11.3–11.4 hypotheses on open datasets (2026-07-17)

## Setup

A data check of two claims from findings §11.3–11.4:
(Q1) the exponent in Effort ~ Size^b is greater than 1 (diseconomy of scale);
(Q2) breaks exist — boundaries of size regimes;
(Q3) the overrun multiplier (actual/estimate) grows with size.

The method is deliberately simple (the §11.5 precaution): "MARS-lite" — a single
hinge max(0, x−t) in log-log axes, a grid search over the knot, a comparison with a
straight line by AICc, knot stability by bootstrap (500 resamples), slope CIs by
bootstrap (2000). A full MARS (R `earth`) is a possible second pass;
for a single covariate our fit is equivalent to MARS with one knot.

Data (a PROMISE mirror, the danrodgar/DASE repository): China (n=499, AFP→
person-hours), Kitchenham (n=145, AFP→person-hours, has First.estimate), Desharnais
(n=81), Maxwell (n=63). Script: fit_piecewise.py; figure: loglog_fits.png.

## Q1. The exponent: the "b>1" hypothesis was NOT confirmed

| Dataset | b | 95% CI | R² |
|---|---|---|---|
| China | 0.768 | 0.701–0.833 | 0.46 |
| Desharnais | 0.984 | 0.734–1.235 | 0.44 |
| Kitchenham | 0.672 | 0.528–0.801 | 0.53 |
| Maxwell | 0.862 | 0.715–0.982 | 0.63 |

In all four b ≤ 1, in three the CI is entirely below 1: the data show
**economies of scale** in the production function, not a rise in unit cost.
This is not our anomaly — it is a well-known, long-standing dispute in the literature
(Banker & Kemerer 1989, "Scale economies in new software development";
Kitchenham 2002, "The question of scale economies — why cannot researchers
agree?"): FP datasets often give b<1, KLOC calibrations of COCOMO give b>1.

Caveats that prevent reading b<1 literally:
- **survivorship**: the datasets contain only completed projects; the large
  failed ones (that very class tail) are unobservable at all;
- mixing of organizations and eras (except Kitchenham — one company);
- FP as a size metric is itself non-linearly related to the volume of work;
- large projects may get better teams/processes (endogeneity).

## Q2. Breaks: the direction is there, the position is unstable

| Dataset | Knot (best) | Slope before → after | AICc verdict | Bootstrap: share "slope grows" |
|---|---|---|---|---|
| China | ~616 FP | 0.74 → 0.85 | not justified | 77% |
| Desharnais | ~141 | 0.40 → 1.07 | not justified | 62% |
| Kitchenham | ~701 FP | 0.56 → 1.15 | **justified** | **98%** |
| Maxwell | ~1137 | 0.79 → 1.16 | not justified | 47% |

The systematic picture: where a break is visible, the slope after the knot
**increases** (economies of scale weaken or turn into growth on large
projects). A break is formally justified only in Kitchenham
(a homogeneous source — one company; knot ~600–700 FP, 98% of bootstrap
samples agree on the direction). The knot position wanders by an order of
magnitude in the others → **stratification by size is meaningful as an idea, but
stratum boundaries cannot be confidently extracted from these data**. It indirectly
supports §11.4: a homogeneous population (Kitchenham) shows a regime boundary more
clearly than a mix of organizations (China).

## Q3. The overrun multiplier grows with size — CONFIRMED (Kitchenham)

The only dataset with a "first estimate / actual" pair (n=145):

- Median Actual/FirstEstimate = **0.97** — in the median the company estimated
  itself accurately; P90 = 1.34.
- Slope of log(ratio) ~ log(size): **+0.054, 95% CI 0.006–0.097** — the CI does
  not cover zero, the multiplier grows with size.
- By size terciles: median 0.95 / 0.94 / 1.00; **P90: 1.11 / 1.15 / 1.46**.

The key structure of the effect: with size it is not the center of the error that
grows, but its **right tail**. Small projects miss by percentages; large ones —
in P90 already by +46%, at almost the same median.

## Synthesis: a correction to our theory (§11.3)

The data separate two quantities that §11.3 conflated:

1. **The production function** Effort(Size) — may show economies of
   scale (b<1); the claim "exponent >1" in this formulation is not
   supported by the data (with the survivorship/FP caveats above).
2. **The estimation error** (actual/estimate) — grows with size, and in the tail,
   not the center. This is exactly what §11.3 claimed in terms of the "overrun
   multiplier," and this is exactly what is relevant for 3A8: the pipeline calibrates
   estimates, it does not produce projects.

A refinement of the edges argument (n²/2): edges strike not necessarily at the
project's cost itself, but at its **visibility in the WBS** — the underestimation
grows with the number of seams, because seams have no lines. The growth of the P90
multiplier with size at a stable median corresponds exactly to this: large projects
have more invisible items that occasionally fire.

## The obtained models (use only as the shape of a prior, not as a predictor)

- China: Effort ≈ 27.1 · AFP^0.77 (person-hours)
- Kitchenham: Effort ≈ 37.1 · AFP^0.67; after ~700 FP the slope ~1.15
- Desharnais: Effort ≈ 15.3 · FP^0.98
- Maxwell: Effort ≈ 26.2 · Size^0.86

The populations are other people's organizations of the 1990s–2000s, the era of
function points; R² 0.44–0.63 (half the variance is outside size). The legitimate
use in 3A8 (per §11.5): transfer the **shape** (the order of b, the existence of a
break, the growth of the multiplier tail with size), tune the level on one's own history.

## Pilot: work composition as parameters (the author's idea, a continuation of §11.4)

The idea: the MARS approach is multivariate — instead of a single "size," feed a
**vector of WBS composition** (the shares of work types), turning the discrete strata
of §11.4 into continuous coordinates of a class space. There are no open datasets
with real WBSs, but China breaks size down into FP elements
(Input/Output/Enquiry/File/Interface) — a crude proxy for composition. Of particular
interest: the share of **Interface** (external interface files) — an almost literal
proxy for integration edges.

Script: composition_china.py. Model: the residuals of log(E)~log(AFP) are regressed
on the element shares (OLS, bootstrap CIs, no feature selection — §11.5).

Result (n=499):
- The R² gain from composition over size: **+0.017** (modest at the population level).
- Significant shares: **share_Interface +0.43 [CI 0.13..0.76]** and share_Enquiry
  +0.42 [0.12..0.73]; Output and File — zeros.
- Interpretation: +10 pp of the Interface share → **×1.10 to cost at the same AFP**.

The key nuance: AFP already pays for interfaces with **increased** weight (EIF:
5–10 points against 3–6 for inputs; only ILF is more expensive). A significant positive
coefficient on top of AFP means: even when the method deliberately assigns interfaces
a premium, they still cost more — the underestimation of seams survives even an
explicit attempt to pay for them with increased weight. This is a direct empirical
echo of the §11.4/9 thesis about the edges that have no lines.

Pilot limitations: FP elements are a functional, not a work decomposition
(they are not WBS branches); ΔR² is small; the Enquiry effect has no theory — it is
not interpretable. A real check is possible only on one's own history with real
WBS vectors, and there the features must be few and chosen by theory
(Interface-like), not by search — otherwise §11.5.

## Files

- data/ — china.arff, chinaOriginal.arff, desharnais.arff|csv,
  kitchenham.arff|csv, maxwell.arff (a PROMISE / DASE mirror)
- fit_piecewise.py — the main analysis (numpy, matplotlib; run: `py fit_piecewise.py`)
- composition_china.py — the "composition as parameters" pilot on China
- loglog_fits.png — four log-log panels with the straight-line and hinge fits
