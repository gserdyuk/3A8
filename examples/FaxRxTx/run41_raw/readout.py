# run 41 - FaxRxTx no-method baseline, n=10, claude-opus-5, tool_uses=0 in every run
# Two independent readouts per run:
#   (1) TOTAL in the A9 person-month convention (1 pm = 21 pd = 168 net hours)
#   (2) the run's own stated TEAM x DURATION -> staffed person-months, the unit FACT.md uses
import statistics as st, math

RUNS = [  # id, A9 pm, low, high, team, calendar months
 ("B-1",130, 90,190, 9,18), ("B-2", 90, 60,140, 7,13), ("B-3",120, 85,175, 7,19),
 ("B-4",120, 85,180, 8,15), ("B-5",120, 80,190, 8,17), ("B-6",105, 70,160, 7,18),
 ("B-7",155,110,225, 8,22), ("B-8",120, 85,175, 8,18), ("B-9",125, 80,200, 8,18),
 ("B-10",120, 80,190, 7,19),
]
FACT = 120.0          # staffed person-months: ~10 heads x ~12 months, participant's memory, +-20%
CHAIN = 99.4          # run 31/32 centre, staffed pm
A9_TO_STAFFED = 168/6*1.10/21   # 168 net h -> present days at 6 net h -> +10% leave -> /21

def stats(xs, label):
    m, sd = st.mean(xs), st.stdev(xs)
    print(f"{label:24s} n={len(xs)}  mean={m:7.1f}  median={st.median(xs):7.1f}  sd={sd:6.1f}"
          f"  CV={100*sd/m:5.2f}%  min={min(xs):6.1f}  max={max(xs):6.1f}  max/min={max(xs)/min(xs):.3f}")
    return m

print("=== readout 1: TOTAL as stated, A9 person-months ===")
a9 = [r[1] for r in RUNS]; stats(a9, "A9 pm")
print("\n=== readout 2: the runs' own TEAM x DURATION, staffed person-months ===")
sp = [r[4]*r[5] for r in RUNS]; m_sp = stats(sp, "staffed pm")
print("\n=== readout 3: A9 totals converted by the project's own constant ===")
cvs = [r[1]*A9_TO_STAFFED for r in RUNS]; m_cv = stats(cvs, "staffed pm (converted)")
print(f"    conversion factor: 1 A9 pm = {A9_TO_STAFFED:.4f} staffed pm")

print(f"\n=== against the fact, {FACT:.0f} staffed person-months ===")
for name, val in (("baseline, by stated team x duration", m_sp),
                  ("baseline, by unit conversion", m_cv),
                  ("Hotyn chain (run 31/32)", CHAIN)):
    r = val/FACT
    print(f"  {name:38s} {val:7.1f}  ratio {r:5.2f}  |log10| {abs(math.log10(r)):.4f}")

tgt = FACT/A9_TO_STAFFED
inside = sum(1 for r in RUNS if r[2] <= tgt <= r[3])
print(f"\n  runs whose declared RANGE covers the fact ({tgt:.1f} A9 pm): {inside}/10")
print("\n=== comparison with run 14, the BMS no-method baseline ===")
print("  BMS      n=10  CV 8.55%  max/min 1.263   (a structured RFP)")
print(f"  FaxRxTx  n=10  CV {100*st.stdev(a9)/st.mean(a9):.2f}%  max/min {max(a9)/min(a9):.3f}"
      "   (one participant's hedged recollection)")
