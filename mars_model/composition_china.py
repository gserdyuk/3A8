"""
3A8 / mars_model — пилот идеи «состав WBS как параметры» (продолжение results.md).

China раскладывает размер на элементы FP: Input, Output, Enquiry, File,
Interface. Считаем доли элементов «вектором состава работ» и спрашиваем:
объясняет ли состав что-то СВЕРХ общего размера?

  Шаг 1. Базовая модель: log(Effort) ~ log(AFP) -> остатки r.
  Шаг 2. r ~ доли состава (OLS), бутстреп-CI коэффициентов.
         Особый интерес: доля Interface (прокси интеграционных рёбер, §11.4).
  Шаг 3. Прирост R² от добавления состава к размеру.

Дисциплина §11.5: только OLS и доли, никакого отбора признаков.
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

# Шаг 1: базовая модель
b0, b1, sse0 = ols(x, y)
r = y - (b0 + b1 * x)
r2_size = 1 - sse0 / (np.var(y) * n)
print(f"n={n}; базовая модель log(E)={b0:.2f}+{b1:.2f}·log(AFP), R²={r2_size:.3f}")

# Шаг 2-3: остатки ~ доли (без Input — она базовая категория, доли сводятся в 1)
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

print(f"прирост R² от состава сверх размера: +{r2_gain:.3f}")
print("коэффициенты (эффект доли на log10-остаток; + = дороже при том же AFP):")
for j, nm in enumerate(names):
    sig = "*" if lo[j] > 0 or hi[j] < 0 else " "
    print(f"  {nm:16s} {beta[j]:+.3f}  [{lo[j]:+.3f} .. {hi[j]:+.3f}] {sig}")

# перевод в разы для значимых долей: эффект +0.10 доли
print("\nинтерпретация: изменение затрат при +10 п.п. доли элемента (при том же AFP):")
for j, nm in enumerate(names[1:], start=1):
    print(f"  {nm:16s} ×{10 ** (beta[j] * 0.10):.3f}")
