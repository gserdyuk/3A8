# run 49 - SAS no-method baseline, n=10, claude-opus-5, tool_uses=1 (the single permitted Read) in every run
# Readout as run 41/43: TOTAL and RANGE (the run's own P10..P90) in the imposed unit,
# 1 pm = 21 pd = 168 net task hours; each run fitted as a lognormal (median = TOTAL, sigma from P10..P90).
import statistics as st, math, json, sys

RUNS = [  # id, TOTAL pm, P10, P90, team, calendar months
 ("B-1",170,120,270,14,14), ("B-2",250,165,390,18,16), ("B-3",150,105,230,12,14),
 ("B-4",185,125,290,13,16), ("B-5",240,165,380,18,16), ("B-6",130, 95,195,12,12),
 ("B-7",147,110,240,13,13), ("B-8",145,105,215,11,14), ("B-9",140, 95,225,11,15),
 ("B-10",135, 95,210,11,14),
]
H = 168.0            # net task hours per imposed pm
Z = 1.2816           # P90 z-score
CHAIN_RAW, CHAIN_CAL = 38118, 57600        # net task hours, runs 47/48
RC1_P50, RC2_P50 = 47880, 24510            # class medians at the house 0.75

def stats(xs, label):
    m, sd = st.mean(xs), st.stdev(xs)
    print(f"{label:22s} n={len(xs)}  mean={m:7.1f}  median={st.median(xs):7.1f}  sd={sd:6.1f}"
          f"  CV={100*sd/m:5.2f}%  min={min(xs):6.1f}  max={max(xs):6.1f}  max/min={max(xs)/min(xs):.3f}")
    return m

print("=== readout 1: TOTAL as stated, imposed pm (168 net h) ===")
tot = [r[1] for r in RUNS]; m = stats(tot, "TOTAL pm")
print("\n=== readout 2: the runs' own TEAM x DURATION, calendar person-months ===")
sp = [r[4]*r[5] for r in RUNS]; stats(sp, "team x months")
print("\n=== readout 3: each run's declared corridor against the spread of the medians ===")
widths = [r[3]/r[2] for r in RUNS]
print(f"  declared P10..P90 width, mean x{st.mean(widths):.2f} (x{min(widths):.2f} .. x{max(widths):.2f})")
print(f"  spread of the ten medians: x{max(tot)/min(tot):.2f}")
pairs = [max(a,b)/min(a,b) for i,a in enumerate(tot) for b in tot[i+1:]]
print(f"  mean pairwise ratio {st.mean(pairs):.3f}, median {st.median(pairs):.3f}")

print("\n=== on the chain's axis, net task hours ===")
mh = m*H
print(f"  baseline mean {mh:,.0f} h  = x{mh/CHAIN_RAW:.2f} of the raw chain ({CHAIN_RAW:,}), x{mh/CHAIN_CAL:.2f} of the calibrated centre ({CHAIN_CAL:,})")
print(f"  = x{mh/RC1_P50:.2f} of RC46-1's median, x{mh/RC2_P50:.2f} of RC46-2's median")
print(f"  runs whose own P10..P90 covers the raw chain ({CHAIN_RAW/H:.0f} pm): {sum(1 for r in RUNS if r[2]*H <= CHAIN_RAW <= r[3]*H)}/10")
print(f"  runs whose own P10..P90 covers the calibrated centre ({CHAIN_CAL/H:.0f} pm): {sum(1 for r in RUNS if r[2]*H <= CHAIN_CAL <= r[3]*H)}/10")

# lognormal fit per run, in person-days of 8 net task hours (the report's axis)
curves = []
for rid, t, lo, hi, k, mo in RUNS:
    sigma = math.log(hi/lo) / (2*Z)
    curves.append({"id": rid, "median": round(t*H/8), "sigma": round(sigma, 3)})
json.dump(curves, open(__file__.replace('readout.py','curves_pd.json'), 'w'), indent=1)
print("\n=== per-run lognormals written to curves_pd.json (median in pd of 8 net h, sigma) ===")
for c in curves: print("  ", c)
print("\n=== comparison with runs 14 / 41 / 43 ===")
print("  BMS run 14      n=10  CV 8.55%   max/min 1.263")
print("  FaxRxTx run 41  n=10  CV 13.75%  max/min 1.722")
print("  FaxRxTx run 43  n=10  CV 13.47%  max/min 1.500")
print(f"  SAS run 49      n=10  CV {100*st.stdev(tot)/st.mean(tot):.2f}%  max/min {max(tot)/min(tot):.3f}")
