"""
3A8 / mars_model - checking the section 11.3-11.4 hypotheses (findings.md) on open datasets.

Questions:
  Q1. The exponent b in Effort ~ a * Size^b : is b > 1 ? (diseconomy of scale)
  Q2. Is there a break (a size-regime boundary)? A piecewise-linear fit in log-log
      with one knot against a straight line; knot stability by bootstrap.
  Q3. (Kitchenham) Does the overrun multiplier Actual/FirstEstimate grow with size?

The method is deliberately simple (the findings section 11.5 precaution): one hinge
max(0, x-t), a grid search over t, a comparison with a straight line by AICc, bootstrap.
This is MARS-lite with full transparency; a full MARS is a second pass.
"""

import re
import numpy as np

rng = np.random.default_rng(38)
DATA = "data"
N_BOOT = 2000


def read_arff(path):
    """Minimal ARFF parser: numeric columns -> dict name->np.array (NaN for '?')."""
    attrs, rows, in_data = [], [], False
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("%"):
                continue
            low = line.lower()
            if low.startswith("@attribute"):
                m = re.match(r"@attribute\s+('?[^\s']+'?)\s+(.*)", line, re.I)
                attrs.append((m.group(1).strip("'"), m.group(2).strip().lower()))
            elif low.startswith("@data"):
                in_data = True
            elif in_data:
                rows.append([v.strip() for v in line.split(",")])
    cols = {}
    for j, (name, typ) in enumerate(attrs):
        vals = []
        for r in rows:
            v = r[j] if j < len(r) else "?"
            if typ == "numeric":
                vals.append(float(v) if v not in ("?", "") else np.nan)
            else:
                vals.append(np.nan)  # categorical columns are not needed here
        cols[name] = np.array(vals)
    return cols


def ols(x, y):
    """Straight line y = b0 + b1 x; returns (b0, b1, sse)."""
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    return beta[0], beta[1], float(resid @ resid)


def hinge_fit(x, y):
    """y = b0 + b1 x + b2 max(0, x-t); grid search over t on the inner quantiles.
    Returns (t, beta(3), sse). Requires >=10 points on each side of the knot."""
    best = None
    for t in np.quantile(x, np.linspace(0.10, 0.90, 81)):
        h = np.maximum(0.0, x - t)
        if (x <= t).sum() < 10 or (x > t).sum() < 10:
            continue
        X = np.column_stack([np.ones_like(x), x, h])
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        resid = y - X @ beta
        sse = float(resid @ resid)
        if best is None or sse < best[2]:
            best = (float(t), beta, sse)
    return best


def aicc(n, k, sse):
    if n - k - 1 <= 0:
        return np.inf
    return n * np.log(sse / n) + 2 * k + 2 * k * (k + 1) / (n - k - 1)


def analyze(name, size, effort):
    m = np.isfinite(size) & np.isfinite(effort) & (size > 0) & (effort > 0)
    x, y = np.log10(size[m]), np.log10(effort[m])
    n = len(x)
    b0, b1, sse_lin = ols(x, y)

    # bootstrap CI of the exponent
    slopes = np.empty(N_BOOT)
    for i in range(N_BOOT):
        idx = rng.integers(0, n, n)
        slopes[i] = ols(x[idx], y[idx])[1]
    lo, hi = np.percentile(slopes, [2.5, 97.5])

    print(f"\n=== {name} (n={n}) ===")
    print(f"Q1 exponent b = {b1:.3f}  [95% CI {lo:.3f} .. {hi:.3f}]"
          f"  -> {'b>1 confirmed' if lo > 1 else ('b<1!' if hi < 1 else 'CI covers 1')}")

    hf = hinge_fit(x, y)
    if hf is None:
        print("Q2: too few points for a knot")
        return
    t, beta, sse_h = hf
    a_lin, a_h = aicc(n, 2, sse_lin), aicc(n, 4, sse_h)
    s1, s2 = beta[1], beta[1] + beta[2]
    verdict = "break JUSTIFIED by AICc" if a_h + 2 < a_lin else "break NOT justified (a straight line suffices)"
    print(f"Q2 knot t=10^{t:.2f} = {10**t:,.0f} size units; slopes {s1:.2f} -> {s2:.2f}; "
          f"AICc: line {a_lin:.1f} vs hinge {a_h:.1f} -> {verdict}")

    # stability of the knot and the sign of the break
    knots, dslope = [], []
    for i in range(N_BOOT // 4):  # bootstrapping a grid-search fit is costlier; 500 is enough
        idx = rng.integers(0, n, n)
        h = hinge_fit(x[idx], y[idx])
        if h:
            knots.append(h[0])
            dslope.append(h[1][2])
    knots, dslope = np.array(knots), np.array(dslope)
    k_lo, k_med, k_hi = np.percentile(knots, [10, 50, 90])
    frac_up = (dslope > 0).mean()
    print(f"   knot bootstrap: median 10^{k_med:.2f}={10**k_med:,.0f}, "
          f"[P10 {10**k_lo:,.0f} .. P90 {10**k_hi:,.0f}]; "
          f"share of samples with an INCREASE of the slope after the knot: {frac_up:.0%}")
    return dict(n=n, b=b1, b_ci=(lo, hi), knot=10**t, s1=s1, s2=s2,
                hinge_better=a_h + 2 < a_lin, frac_up=frac_up)


def main():
    china = read_arff(f"{DATA}/china.arff")
    desh = read_arff(f"{DATA}/desharnais.arff")
    kitch = read_arff(f"{DATA}/kitchenham.arff")
    maxw = read_arff(f"{DATA}/maxwell.arff")

    results = {}
    results["China"] = analyze("China (AFP -> Effort, person-hours)", china["AFP"], china["Effort"])
    results["Desharnais"] = analyze("Desharnais (PointsAdjust -> Effort)",
                                    desh["PointsAdjust"], desh["Effort"])
    results["Kitchenham"] = analyze("Kitchenham (AFP -> Actual.effort)",
                                    kitch["Adjusted.function.points"], kitch["Actual.effort"])
    # in Maxwell the size is called size_D, the effort - look it up by name
    eff_name = next(k for k in maxw if "effort" in k.lower())
    results["Maxwell"] = analyze(f"Maxwell (size_D -> {eff_name})", maxw["size_D"], maxw[eff_name])

    # Q3: the overrun multiplier vs size (Kitchenham only)
    fe, ae, sz = (kitch["First.estimate"], kitch["Actual.effort"],
                  kitch["Adjusted.function.points"])
    m = np.isfinite(fe) & np.isfinite(ae) & np.isfinite(sz) & (fe > 0) & (ae > 0) & (sz > 0)
    ratio = ae[m] / fe[m]
    x, y = np.log10(sz[m]), np.log10(ratio)
    n = len(x)
    _, slope, _ = ols(x, y)
    sl = np.empty(N_BOOT)
    for i in range(N_BOOT):
        idx = rng.integers(0, n, n)
        sl[i] = ols(x[idx], y[idx])[1]
    lo, hi = np.percentile(sl, [2.5, 97.5])
    q = np.quantile(x, [0, 1 / 3, 2 / 3, 1])
    print(f"\n=== Q3. Kitchenham: overrun multiplier Actual/FirstEstimate (n={n}) ===")
    print(f"median multiplier: {np.median(ratio):.2f}; P90: {np.quantile(ratio, .9):.2f}")
    print(f"slope log(ratio)~log(size): {slope:.3f} [95% CI {lo:.3f} .. {hi:.3f}]"
          f" -> {'grows with size' if lo > 0 else ('falls!' if hi < 0 else 'no proven dependence')}")
    for j in range(3):
        mm = (x >= q[j]) & (x <= q[j + 1])
        print(f"   size tercile {j+1} (FP {10**q[j]:,.0f}..{10**q[j+1]:,.0f}): "
              f"median {np.median(ratio[mm]):.2f}, P90 {np.quantile(ratio[mm], .9):.2f}")

    # figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    sets = [("China", china["AFP"], china["Effort"]),
            ("Desharnais", desh["PointsAdjust"], desh["Effort"]),
            ("Kitchenham", kitch["Adjusted.function.points"], kitch["Actual.effort"]),
            ("Maxwell", maxw["size_D"], maxw[eff_name])]
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    for ax, (nm, s, e) in zip(axes.flat, sets):
        m = np.isfinite(s) & np.isfinite(e) & (s > 0) & (e > 0)
        x, y = np.log10(s[m]), np.log10(e[m])
        ax.scatter(x, y, s=12, alpha=0.5)
        b0, b1, _ = ols(x, y)
        xs = np.linspace(x.min(), x.max(), 100)
        ax.plot(xs, b0 + b1 * xs, "r-", lw=1.5, label=f"line, b={b1:.2f}")
        hf = hinge_fit(x, y)
        if hf:
            t, beta, _ = hf
            ax.plot(xs, beta[0] + beta[1] * xs + beta[2] * np.maximum(0, xs - t),
                    "g--", lw=1.5, label=f"hinge, knot={10**t:,.0f}")
            ax.axvline(t, color="g", alpha=0.3)
        ax.set_title(nm)
        ax.set_xlabel("log10(size)")
        ax.set_ylabel("log10(effort)")
        ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig("loglog_fits.png", dpi=120)
    print("\nfigure: mars_model/loglog_fits.png")


if __name__ == "__main__":
    main()
