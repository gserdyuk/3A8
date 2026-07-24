"""
3A8 / mars_model - pilot for the idea "WBS composition as parameters" (a continuation of results.md).

China breaks size down into FP elements: Input, Output, Enquiry, File,
Interface. We treat the element shares as a "vector of work composition" and ask:
does the composition explain anything OVER AND ABOVE the overall size?

  Step 1. Base model: log(Effort) ~ log(AFP) -> residuals r.
  Step 2. r ~ composition shares (OLS), bootstrap CIs of the coefficients.
          Of particular interest: the Interface share (a proxy for integration edges, section 11.4).
  Step 3. The R^2 gain from adding composition to size.

The section 11.5 discipline: only OLS and shares, no feature selection.
"""

import numpy as np
from fit_piecewise import read_arff, ols

rng = np.random.default_rng(38)
N_BOOT = 2000

c = read_arff("data/china.arff")
ELEMS = ["Input", "Output", "Enquiry", "File", "Interface"]

afp, eff = c["AFP"], c["Effort"]
elem = np.column_stack([c[e] for e in ELEMS])
total = elem.sum(axis=1)
m = np.isfinite(afp) & np.isfinite(eff) & (afp > 0) & (eff > 0) & (total > 0)
x, y, elem, total = np.log10(afp[m]), np.log10(eff[m]), elem[m], total[m]
shares = elem / total[:, None]
n = len(x)

# Step 1: base model
b0, b1, sse0 = ols(x, y)
r = y - (b0 + b1 * x)
r2_size = 1 - sse0 / (np.var(y) * n)
print(f"n={n}; base model log(E)={b0:.2f}+{b1:.2f}*log(AFP), R2={r2_size:.3f}")

# Steps 2-3: residuals ~ shares (without Input - it is the base category, shares sum to 1)
X = np.column_stack([np.ones(n), shares[:, 1:]])
names = ["const"] + [f"share_{e}" for e in ELEMS[1:]]
beta, *_ = np.linalg.lstsq(X, r, rcond=None)
resid = r - X @ beta
sse1 = float(resid @ resid)
r2_gain = (float(r @ r) - sse1) / (np.var(y) * n)

boot = np.empty((N_BOOT, len(beta)))
for i in range(N_BOOT):
    idx = rng.integers(0, n, n)
    boot[i], *_ = np.linalg.lstsq(X[idx], r[idx], rcond=None)
lo, hi = np.percentile(boot, [2.5, 97.5], axis=0)

print(f"R2 gain from composition over size: +{r2_gain:.3f}")
print("coefficients (effect of a share on the log10 residual; + = more expensive at the same AFP):")
for j, nm in enumerate(names):
    sig = "*" if lo[j] > 0 or hi[j] < 0 else " "
    print(f"  {nm:16s} {beta[j]:+.3f}  [{lo[j]:+.3f} .. {hi[j]:+.3f}] {sig}")

# convert to a factor for the significant shares: effect of +0.10 of the share
print("\ninterpretation: change in cost at +10 pp of an element's share (at the same AFP):")
for j, nm in enumerate(names[1:], start=1):
    print(f"  {nm:16s} x{10 ** (beta[j] * 0.10):.3f}")
