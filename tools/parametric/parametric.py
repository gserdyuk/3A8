"""
3A8 / the parametric instrument - the arithmetic half. Deterministic; no model involved.

What it does, per docs/fp_counting_rules.md:
  1. Takes a function-point count: either --ufp N directly, or --components <tsv>
     (one row per classified item from a pinned Hotyn-P transcript) joined to the
     pinned weight table tools/parametric/weights.tsv (from Hotyn-N; script refuses
     to run components without it).
  2. Refits the two curves from mars_model/data/ at every run - the constants are
     never carried by this script, so their provenance is the data, not a copy.
       China:      Effort ~ a * AFP^b   (n=499, recorded person-hours)
       Kitchenham: Effort ~ a * AFP^b   (n=145, recorded person-hours)
  3. The corridor: empirical P10/P50/P90 of the fit residuals in log space,
     applied multiplicatively around the curve. Width from the scatter of real
     projects, not from a declared correlation.
  4. Prints every figure in four units with every conversion factor named.

Declared constants (docs/fp_counting_rules.md section 5):
  VAF = 1.0                      the adjustment factor is out of scope by ruling
  RECORDED_TO_NET = 0.75         a recorded timesheet hour -> net task hours
                                 (same factor and provenance as the class conversion,
                                 docs/constants.md section 5b)
  NET_H_PER_PRESENT_DAY = 6      the settled ladder, docs/status_2026-08-25.md section 3a
  LEAVE = 1.10
  STAFFED_DAYS_PER_MONTH = 21
  NET_H_PER_TABLE_PD = 8         the operative unit, docs/constants.md section 1
"""

import argparse
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "mars_model" / "data"
WEIGHTS = Path(__file__).resolve().parent / "weights.tsv"

VAF = 1.0
RECORDED_TO_NET = 0.75
NET_H_PER_PRESENT_DAY = 6.0
LEAVE = 1.10
STAFFED_DAYS_PER_MONTH = 21.0
NET_H_PER_TABLE_PD = 8.0

# the recorded fits (mars_model/results.md), printed as a cross-check only - never used
RECORDED = {"China": (27.1, 0.768), "Kitchenham": (37.1, 0.672)}

QUANTS = (0.10, 0.50, 0.90)


def read_arff(path):
    """Minimal ARFF parser (same shape as mars_model/fit_piecewise.py)."""
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
                vals.append(np.nan)
        cols[name] = np.array(vals)
    return cols


def fit_loglog(size, effort):
    """OLS in log-log; returns a, b, R^2, residuals (log space), n."""
    ok = np.isfinite(size) & np.isfinite(effort) & (size > 0) & (effort > 0)
    x, y = np.log(size[ok]), np.log(effort[ok])
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    r2 = 1.0 - float(resid @ resid) / float(((y - y.mean()) ** 2).sum())
    return float(np.exp(beta[0])), float(beta[1]), r2, resid, int(ok.sum())


def load_weights():
    if not WEIGHTS.exists():
        sys.exit(
            "weights.tsv is not pinned yet. It is written from Hotyn-N 1.0 first-approximation "
            "runs (docs/fp_counting_rules.md section 4), never by hand here. "
            "Until then only --ufp is available."
        )
    table = {}
    for ln in WEIGHTS.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        comp, cx, pts = ln.split("\t")
        table[(comp.strip(), cx.strip())] = float(pts)
    return table


def count_ufp(components_path):
    """One row per classified item: id <tab> component <tab> complexity."""
    weights = load_weights()
    ufp, per_comp, missing = 0.0, {}, []
    for ln in Path(components_path).read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        item, comp, cx = [v.strip() for v in ln.split("\t")]
        key = (comp, cx)
        if key not in weights:
            missing.append((item, comp, cx))
            continue
        ufp += weights[key]
        per_comp[key] = per_comp.get(key, 0) + 1
    if missing:
        for m in missing:
            print(f"NO WEIGHT for {m} - the row is not counted", file=sys.stderr)
        sys.exit("unpriceable rows; fix the components file or the weight table")
    return ufp, per_comp


def to_units(recorded_h):
    net_h = recorded_h * RECORDED_TO_NET
    table_pd = net_h / NET_H_PER_TABLE_PD
    staffed_pm = net_h / NET_H_PER_PRESENT_DAY * LEAVE / STAFFED_DAYS_PER_MONTH
    return recorded_h, net_h, table_pd, staffed_pm


def main():
    ap = argparse.ArgumentParser(description="parametric instrument arithmetic")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--ufp", type=float, help="unadjusted function points, counted elsewhere")
    g.add_argument("--components", help="tsv from a pinned Hotyn-P transcript: id/component/complexity")
    args = ap.parse_args()

    if args.components:
        ufp, per_comp = count_ufp(args.components)
        print(f"UFP = {ufp:.0f} from {sum(per_comp.values())} classified items:")
        for (comp, cx), n in sorted(per_comp.items()):
            print(f"  {comp:4s} {cx:8s} x{n}")
    else:
        ufp = args.ufp
        print(f"UFP = {ufp:.0f} (given directly)")

    afp = ufp * VAF
    print(f"AFP = UFP x VAF = {ufp:.0f} x {VAF} = {afp:.0f}   (VAF declared 1.0 by ruling)")
    print()

    datasets = {
        "China": (lambda c: (c["AFP"], c["Effort"]), DATA / "china.arff"),
        "Kitchenham": (
            lambda c: (c["Adjusted.function.points"], c["Actual.effort"]),
            DATA / "kitchenham.arff",
        ),
    }

    for name, (pick, path) in datasets.items():
        size, effort = pick(read_arff(path))
        a, b, r2, resid, n = fit_loglog(size, effort)
        ra, rb = RECORDED[name]
        drift = "" if abs(a - ra) / ra < 0.02 and abs(b - rb) < 0.005 else "  <-- DRIFT vs results.md"
        print(f"== {name}: Effort ~ {a:.1f} * AFP^{b:.3f}   (n={n}, R2={r2:.2f}; "
              f"recorded {ra} * AFP^{rb}){drift}")
        centre_log = np.log(a) + b * np.log(afp)
        qs = np.quantile(resid, QUANTS)
        print(f"   residual quantile factors (P10/P50/P90): "
              + " / ".join(f"x{np.exp(q):.2f}" for q in qs))
        print(f"   {'':14s}{'recorded p-h':>14s}{'net task h':>14s}{'table pd':>12s}{'staffed pm':>12s}")
        for p, q in zip(("P10", "P50", "P90"), qs):
            rec, net, pd, pm = to_units(float(np.exp(centre_log + q)))
            print(f"   {p:14s}{rec:14.0f}{net:14.0f}{pd:12.1f}{pm:12.1f}")
        print()

    print("Declaration (required of every number-producing role, session 2026-08-25..26):")
    print(f"  unit      : native - recorded timesheet person-hours of the source datasets;")
    print(f"              converted columns as headed, factors: x{RECORDED_TO_NET} recorded->net task h;")
    print(f"              /{NET_H_PER_TABLE_PD:.0f} net h -> table pd; /{NET_H_PER_PRESENT_DAY:.0f} net h per present day,")
    print(f"              x{LEAVE} leave, /{STAFFED_DAYS_PER_MONTH:.0f} -> staffed person-months")
    print("  losses    : leave/holidays/sickness EXCLUDED from recorded hours (booked elsewhere);")
    print("              within-day overheads INCLUDED - hence the 0.75 (docs/constants.md 5a-5b)")
    print("  roles     : whatever the contributing organisations booked; inconsistent across them")
    print("              (a documented weakness of the data - ISBSG resource-level problem)")
    print("  disagree  : China vs Kitchenham levels differ; both rows reported, neither chosen")
    print("  scope     : functional size only - the sensor's outside-scope list bounds the number")


if __name__ == "__main__":
    main()
