#!/usr/bin/env python3
"""Run 74 — forty secret sizings of one fixed list: transcribe, tabulate, compare groups.

    py -X utf8 secret.py extract     # replies verbatim under an orchestrator header, ledger.jsonl, lines.tsv
    py -X utf8 secret.py stats       # per-line medians and spreads, the four registered groups, random partitions

One round, no sheet, no exchange: a participant sees the prompt and nothing else. The registered groups are fixed by
launch label before any reply exists: G1 = P-1..P-10, G2 = P-11..P-20, G3 = P-21..P-30, G4 = P-31..P-40. A group's
estimate is the sum over the seventeen lines of the group's median for the line. The random partitions (seeded) show
what any such grouping would give, for groups of 5, 10 and 20. The actual is used here only, never shown to anyone.
"""
import hashlib, json, os, random, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run69_raw'))
_argv, sys.argv = sys.argv, [sys.argv[0], HERE]
import delphi   # noqa: E402  transcript(), segments(), closing(); it reads this folder's participants.json
sys.argv = _argv

N_LINES = 17
ROW = re.compile(r'^\s*\|\s*\**\s*(L\d{1,2})\b[^|]*\|\s*\**\s*~?\s*(\d+(?:\.\d+)?)\s*\**\s*\|?\s*$')


def table(reply):
    got = {}
    for line in reply.split('\n'):
        m = ROW.match(line)
        if m:
            got[m.group(1)] = float(m.group(2))
    return got


def extract():
    ledger, rows = [], []
    for p, agent in delphi.PARTICIPANTS.items():
        segs = delphi.segments(delphi.transcript(agent))
        s = segs[0]
        reply = s['texts'][-1]
        total, lo, hi = delphi.closing(reply)
        t = table(reply)
        missing = [k for k in ('L%d' % i for i in range(1, N_LINES + 1)) if k not in t]
        head = ('<!-- orchestrator header, not part of the reply: run 74, single secret round, participant %s; general agent, no sensor\n'
                'definition; instruction md5 %s; segments %d; turns %s; tool uses %s -->\n\n'
                % (p, hashlib.md5(s['instruction'].encode('utf-8')).hexdigest(), len(segs),
                   json.dumps(list(s['turns'].values())), json.dumps(s['tools'])))
        open(os.path.join(HERE, 'R1_%s.md' % p), 'w', encoding='utf-8', newline='\n').write(head + reply + '\n')
        ledger.append({'participant': p, 'agent': agent, 'total': total, 'low': lo, 'high': hi, 'lines': t,
                       'sum_of_lines': sum(t.values()), 'missing': missing,
                       'turns': list(s['turns'].values()), 'tools': s['tools'], 'reply_chars': len(reply)})
        print(p, 'TOTAL', total, 'sum of lines', sum(t.values()), 'RANGE', lo, hi, '| missing:', missing, '| tools:', s['tools'])
        for k, v in t.items():
            rows.append('%s\t%s\t%s' % (p, k, v))
    with open(os.path.join(HERE, 'ledger.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for r in ledger:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    open(os.path.join(HERE, 'lines.tsv'), 'w', encoding='utf-8', newline='\n').write('participant\tline\tpm\n' + '\n'.join(rows) + '\n')


def group_estimate(members, how=statistics.median):
    return sum(how([m['lines'][k] for m in members]) for k in KEYS)


def stats():
    global KEYS
    KEYS = ['L%d' % i for i in range(1, N_LINES + 1)]
    L = [json.loads(l) for l in open(os.path.join(HERE, 'ledger.jsonl'), encoding='utf-8')]
    L = [r for r in L if not r['missing']]
    n = len(L)
    print('participants with a complete table: %d' % n)
    tot = [r['sum_of_lines'] for r in L]
    print('own totals (sum of own lines): mean %.1f  median %.1f  CV %.1f%%  min %.0f  max %.0f  max/min x%.2f'
          % (statistics.mean(tot), statistics.median(tot), 100 * statistics.stdev(tot) / statistics.mean(tot), min(tot), max(tot), max(tot) / min(tot)))
    print('stated TOTAL differs from the sum of lines by more than 1 pm: %d' % sum(1 for r in L if r['total'] is None or abs(r['total'] - r['sum_of_lines']) > 1))
    print('\nline   median   mean    p10    p90   p90/p10  max/min   distinct values')
    for k in KEYS:
        v = sorted(r['lines'][k] for r in L)
        p10, p90 = v[int(0.1 * (n - 1))], v[int(round(0.9 * (n - 1)))]
        print('%-5s %7.1f %6.1f %6.1f %6.1f   x%.2f    x%.2f    %d' % (k, statistics.median(v), statistics.mean(v), p10, p90, p90 / p10, v[-1] / v[0], len(set(v))))
    print('\nall %d: sum of line medians %.1f | sum of line means %.1f | against the actual %.1f: x%.2f / x%.2f'
          % (n, group_estimate(L), group_estimate(L, statistics.mean), delphi.ACTUAL_PM,
             group_estimate(L) / delphi.ACTUAL_PM, group_estimate(L, statistics.mean) / delphi.ACTUAL_PM))

    def num(r):
        return int(r['participant'].split('-')[1])
    print('\n=== the registered groups (by launch label) ===')
    for size in (10, 20):
        gs = [[r for r in L if (num(r) - 1) // size == g] for g in range(40 // size)]
        for how, name in ((statistics.median, 'line medians'), (statistics.mean, 'line means')):
            e = [group_estimate(g, how) for g in gs if g]
            print('groups of %2d, sum of %-12s: %s   max/min x%.3f' % (size, name, ' '.join('%6.1f' % x for x in e), max(e) / min(e)))
        if size == 10:
            print('   per line, max/min of the four group medians: ' + ' '.join(
                '%s x%.2f' % (k, max(statistics.median([m['lines'][k] for m in g]) for g in gs) / min(statistics.median([m['lines'][k] for m in g]) for g in gs)) for k in KEYS))
    print('\n=== 2000 random partitions (seed 74): max/min of the group estimates (sum of line medians) ===')
    rnd = random.Random(74)
    for size in (5, 10, 20):
        ratios = []
        for _ in range(2000):
            sh = L[:]
            rnd.shuffle(sh)
            e = [group_estimate(sh[i:i + size]) for i in range(0, n - size + 1, size)]
            ratios.append(max(e) / min(e))
        ratios.sort()
        print('groups of %2d (%d groups): median x%.3f   90th percentile x%.3f' % (size, n // size, ratios[1000], ratios[1800]))
    print('\n=== two random groups of ten, the comparison with two debating panels (x1.10-1.17) ===')
    ratios = []
    for _ in range(2000):
        sh = L[:]
        rnd.shuffle(sh)
        a, b = group_estimate(sh[:10]), group_estimate(sh[10:20])
        ratios.append(max(a, b) / min(a, b))
    ratios.sort()
    print('pair of groups of 10: median x%.3f   90th percentile x%.3f   share above x1.10: %.0f%%'
          % (ratios[1000], ratios[1800], 100 * sum(1 for x in ratios if x > 1.10) / 2000))


if __name__ == '__main__':
    extract() if sys.argv[1] == 'extract' else stats()
