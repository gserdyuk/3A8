#!/usr/bin/env python3
"""Run 69 — each participant's declared TOTAL and RANGE as a lognormal, per round, on the report's axis.

    py -X utf8 curves.py        # writes curves_R1_pd.json, curves_R2_pd.json; prints the check against run 43's rule

The rule is the one the chart's earlier no-method family was drawn with (run 43, `run43_raw/curves_pd.json`), so that
today's curves sit on the same frame: the declared TOTAL is the mode, the declared low … high is read as a span of five
sigma in log space (about ±2.5 sigma), median = mode × exp(sigma²). Checked below against run 43's stored curves.
Unit: person-days of 8 net task hours; 1 person-month of the prompt's convention = 168 h = 21 such days.
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
PD_PER_PM = 21


def fit(total, lo, hi):
    sigma = math.log(hi / lo) / 5.0
    return {'median': round(total * PD_PER_PM * math.exp(sigma * sigma)), 'sigma': round(sigma, 3)}


rows = [json.loads(l) for l in open(os.path.join(HERE, 'ledger.jsonl'), encoding='utf-8')]
for rnd in (1, 2):
    curves = [{'id': 'R%d %s' % (rnd, r['participant']), **fit(r['total'], r['low'], r['high'])} for r in rows if r['round'] == rnd]
    json.dump(curves, open(os.path.join(HERE, 'curves_R%d_pd.json' % rnd), 'w', encoding='utf-8'), indent=1)
    print('round', rnd, [(c['median'], c['sigma']) for c in curves])

# the check: the same rule applied to run 43's declared ranges against run 43's stored curves
ranges = json.load(open(os.path.join(HERE, '..', 'run43_raw', 'ranges.json'), encoding='utf-8'))
stored = json.load(open(os.path.join(HERE, '..', 'run43_raw', 'curves_pd.json'), encoding='utf-8'))
worst_m, worst_s = 0, 0
for batch in ranges.values():
    for rid, (lo, mode, hi) in batch.items():
        f, s = fit(mode, lo, hi), stored[rid]
        worst_m = max(worst_m, abs(f['median'] / s['median'] - 1))
        worst_s = max(worst_s, abs(f['sigma'] - s['sigma']))
print('rule against run 43 stored curves, 20 runs: worst median deviation %.2f%%, worst sigma deviation %.3f' % (100 * worst_m, worst_s))
