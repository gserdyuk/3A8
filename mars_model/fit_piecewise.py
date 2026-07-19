"""
3A8 / mars_model — проверка гипотез §11.3–11.4 (findings.md) на открытых датасетах.

Вопросы:
  Q1. Показатель степени b в Effort ~ a * Size^b : b > 1 ? (diseconomy of scale)
  Q2. Есть ли излом (граница размерного режима)? Кусочно-линейный фит в log-log
      с одним узлом против прямой; стабильность узла — бутстрепом.
  Q3. (Kitchenham) Растёт ли множитель перерасхода Actual/FirstEstimate с размером?

Метод — намеренно простой (предосторожность findings §11.5): один хинж
max(0, x-t), перебор t по сетке, сравнение с прямой по AICc, бутстреп.
Это MARS-лайт с полной прозрачностью; полноценный MARS — второй заход.
"""

import re
import numpy as np

rng = np.random.default_rng(38)
DATA = "data"
N_BOOT = 2000


def read_arff(path):
    """Минимальный ARFF-парсер: numeric-колонки -> dict имя->np.array (NaN для '?')."""
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
                vals.append(np.nan)  # категориальные здесь не нужны
        cols[name] = np.array(vals)
    return cols


def ols(x, y):
    """Прямая y = b0 + b1 x; возвращает (b0, b1, sse)."""
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    return beta[0], beta[1], float(resid @ resid)


def hinge_fit(x, y):
    """y = b0 + b1 x + b2 max(0, x-t); перебор t по внутренним квантилям.
    Возвращает (t, beta(3), sse). Требует >=10 точек с каждой стороны узла."""
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

    # бутстреп CI показателя степени
    slopes = np.empty(N_BOOT)
    for i in range(N_BOOT):
        idx = rng.integers(0, n, n)
        slopes[i] = ols(x[idx], y[idx])[1]
    lo, hi = np.percentile(slopes, [2.5, 97.5])

    print(f"\n=== {name} (n={n}) ===")
    print(f"Q1 показатель степени b = {b1:.3f}  [95% CI {lo:.3f} .. {hi:.3f}]"
          f"  -> {'b>1 подтверждается' if lo > 1 else ('b<1!' if hi < 1 else 'CI накрывает 1')}")

    hf = hinge_fit(x, y)
    if hf is None:
        print("Q2: слишком мало точек для узла")
        return
    t, beta, sse_h = hf
    a_lin, a_h = aicc(n, 2, sse_lin), aicc(n, 4, sse_h)
    s1, s2 = beta[1], beta[1] + beta[2]
    verdict = "излом ОПРАВДАН по AICc" if a_h + 2 < a_lin else "излом НЕ оправдан (прямой достаточно)"
    print(f"Q2 узел t=10^{t:.2f} = {10**t:,.0f} ед. размера; наклоны {s1:.2f} -> {s2:.2f}; "
          f"AICc: прямая {a_lin:.1f} vs хинж {a_h:.1f} -> {verdict}")

    # стабильность узла и знака перелома
    knots, dslope = [], []
    for i in range(N_BOOT // 4):  # бутстреп фита с перебором дороже; 500 хватает
        idx = rng.integers(0, n, n)
        h = hinge_fit(x[idx], y[idx])
        if h:
            knots.append(h[0])
            dslope.append(h[1][2])
    knots, dslope = np.array(knots), np.array(dslope)
    k_lo, k_med, k_hi = np.percentile(knots, [10, 50, 90])
    frac_up = (dslope > 0).mean()
    print(f"   бутстреп узла: медиана 10^{k_med:.2f}={10**k_med:,.0f}, "
          f"[P10 {10**k_lo:,.0f} .. P90 {10**k_hi:,.0f}]; "
          f"доля выборок с УВЕЛИЧЕНИЕМ наклона после узла: {frac_up:.0%}")
    return dict(n=n, b=b1, b_ci=(lo, hi), knot=10**t, s1=s1, s2=s2,
                hinge_better=a_h + 2 < a_lin, frac_up=frac_up)


def main():
    china = read_arff(f"{DATA}/china.arff")
    desh = read_arff(f"{DATA}/desharnais.arff")
    kitch = read_arff(f"{DATA}/kitchenham.arff")
    maxw = read_arff(f"{DATA}/maxwell.arff")

    results = {}
    results["China"] = analyze("China (AFP -> Effort, чел-часы)", china["AFP"], china["Effort"])
    results["Desharnais"] = analyze("Desharnais (PointsAdjust -> Effort)",
                                    desh["PointsAdjust"], desh["Effort"])
    results["Kitchenham"] = analyze("Kitchenham (AFP -> Actual.effort)",
                                    kitch["Adjusted.function.points"], kitch["Actual.effort"])
    # у Maxwell размер называется size_D, усилие — ищем по имени
    eff_name = next(k for k in maxw if "effort" in k.lower())
    results["Maxwell"] = analyze(f"Maxwell (size_D -> {eff_name})", maxw["size_D"], maxw[eff_name])

    # Q3: множитель перерасхода против размера (только Kitchenham)
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
    print(f"\n=== Q3. Kitchenham: множитель перерасхода Actual/FirstEstimate (n={n}) ===")
    print(f"медиана множителя: {np.median(ratio):.2f}; P90: {np.quantile(ratio, .9):.2f}")
    print(f"наклон log(ratio)~log(size): {slope:.3f} [95% CI {lo:.3f} .. {hi:.3f}]"
          f" -> {'растёт с размером' if lo > 0 else ('падает!' if hi < 0 else 'зависимость не доказана')}")
    for j in range(3):
        mm = (x >= q[j]) & (x <= q[j + 1])
        print(f"   терциль размера {j+1} (FP {10**q[j]:,.0f}..{10**q[j+1]:,.0f}): "
              f"медиана {np.median(ratio[mm]):.2f}, P90 {np.quantile(ratio[mm], .9):.2f}")

    # график
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
        ax.plot(xs, b0 + b1 * xs, "r-", lw=1.5, label=f"прямая, b={b1:.2f}")
        hf = hinge_fit(x, y)
        if hf:
            t, beta, _ = hf
            ax.plot(xs, beta[0] + beta[1] * xs + beta[2] * np.maximum(0, xs - t),
                    "g--", lw=1.5, label=f"хинж, узел={10**t:,.0f}")
            ax.axvline(t, color="g", alpha=0.3)
        ax.set_title(nm)
        ax.set_xlabel("log10(size)")
        ax.set_ylabel("log10(effort)")
        ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig("loglog_fits.png", dpi=120)
    print("\nграфик: mars_model/loglog_fits.png")


if __name__ == "__main__":
    main()
