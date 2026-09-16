#!/usr/bin/env python3
"""Step 4, the arithmetic: the whole-model assembly. The only thing in the chain that multiplies anything.

    python tools/chain/assemble.py examples/<case> --crossing-run <N> --sizing-run <K> [--repeats 2]

Inputs, all pinned before this script runs:
  product model    the model named in run<N>_raw/batches.json (Hotyn-M 2.x, section 6 TSV)
  work model       run<N>_raw/work_model.tsv, classes.tsv (the consolidated crossing)
  size classes     run<K>_raw/HD<K>-<batch><repeat>.md (one reading per batch per repeat)
  declaration      examples/<case>/chain_config.json: the declared codes and parameters (environments, cycles)
  catalogue        docs/technology_catalogue.md: the declared entries' activities and scopes
  rates            docs/rate_table.md (net person-hours; first row per (activity, class, size) wins)

Conventions, identical to runs 25, 31, 47 and 59:
  subtree = rooted (element + descendants); C3 = 20% of the leaf-item effort of the rooted subtree at every
  parent including the root, never compounding; once-scoped and per-environment items enter no C3 base;
  E = (O + 4M + P) / 6; position-derived classes (per parent, once, per environment) are catalogue §3a arithmetic
  computed here; an element the sensors could not size is a named hole, listed and priced at nothing; the root's
  per-parent items are added here (the root is outside every batch). Each repeat is priced as a variant; their
  ratio is the measurement. The corridor is the O/M/P of every priced item summed at the declared rho = 0.5 —
  a convention, not a measurement.

Writes run<K>_raw/assembly_summary.json and prints the assembly (redirect to assembly_output.txt to keep it).
Demanded-work branches the crossing left standing are listed as carried, not priced: they have no catalogue
activity and therefore no table row; a gap-blind rate addendum is the instrument for them.
"""
import argparse, csv, json, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chainlib import Model, load_config, declared_activities, scope_kind, load_rates, make_rate_lookup, E, band, md_section

C3_RATE = 0.20
PER_PARENT = {'A5', 'A6', 'A7', 'A8', 'D2', 'U1', 'U2', 'U3', 'O1', 'D7'}
SURFACE_PARENT = {'U1', 'U2', 'U3', 'O1'}
SPECIAL = {'A9', 'G2m', 'G3m', 'G4m', 'G1', 'G2', 'G3'}
SIZE_TOKEN = re.compile(r'\*\*(S|M|L|XL)\*\*')
ENV_SIZE = {'dev': 'S', 'development': 'S', 'test': 'M', 'testing': 'M', 'qa': 'M', 'stage': 'M', 'staging': 'M', 'staging/pre-production': 'M', 'pre-production': 'M', 'uat': 'M', 'prod': 'L', 'production': 'L'}


def parse_reading(fn, leaf_re):
    t = open(fn, encoding='utf-8').read()
    sizes, kinds, special = {}, {}, {}
    for line in md_section(t, 2).split('\n'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        eid = re.sub(r'[*`]', '', c[0]).strip()
        if len(c) < 5 or not leaf_re.fullmatch(eid):
            continue
        m = SIZE_TOKEN.search(c[-1]) or SIZE_TOKEN.search(' '.join(c[1:]))
        sizes[eid] = m.group(1) if m else None
        km = re.search(r'statement[^|]*?(compliance|behavioural)', ' '.join(c[1:]))
        if km:
            kinds[eid] = km.group(1)
    s3 = md_section(t, 3)
    anchor = re.compile(r'^[\s|*\-]*(%s)(?![\w.])' % leaf_re.pattern.strip(r'\b'), re.M)
    hits = [(m.start(), m.group(1)) for m in anchor.finditer(s3)]
    for i, (pos, eid) in enumerate(hits):
        end = hits[i + 1][0] if i + 1 < len(hits) else len(s3)
        chunk = s3[pos:end]
        m = (re.search(r'(?:→|->)\s*\**\s*(S|M|L|XL)\b', chunk) or re.search(r'\|\s*\d+\s*\|\s*\*\*(S|M|L|XL)\*\*', chunk)
             or re.search(r'\|\s*\d+\s*\|\s*(S|M|L|XL)\s*\|', chunk) or re.search(r'class\s*\*\*(S|M|L|XL)\*\*', chunk)
             or re.search(r'[Cc]ount and class:\*\*\s*\d+,\s*\*\*(S|M|L|XL)\*\*', chunk) or re.search(r'·\s*\d+ kinds?\s*·\s*\*\*(S|M|L|XL)\*\*', chunk)
             # run 63 phrasings: "so the class is **M**", "**Count: 2. Class: M.**", "**L01, count 2, M.**"
             or re.search(r'\bclass is \*{0,2}(S|M|L|XL)\*{0,2}(?!\w)', chunk) or re.search(r'\b[Cc]lass:\s*\*{0,2}(S|M|L|XL)\*{0,2}(?!\w)', chunk)
             or re.search(r'\bcount\s+\d+,\s*\*{0,2}(S|M|L|XL)\*{0,2}(?!\w)', chunk))
        if m:
            special.setdefault(eid, m.group(1))
        elif re.search(r'unsizeable|none assigned|not assigned|not countable|not determinable|no special[- ]count|no count|nothing can be enumerated'
                       r'|\*\*none\*\*|\|\s*none\s*\||\bno class\b|\bno band\b|below the S threshold|\|\s*0(?: evidenced| kinds)?\s*\||\|\s*—\s*\|\s*—\s*\|'
                       r'|\bcount:?\s*\*{0,2}0\b|no special class|assign no (?:special )?class', chunk, re.I):
            special.setdefault(eid, None)
    return sizes, kinds, special


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('case')
    ap.add_argument('--crossing-run', required=True, type=int)
    ap.add_argument('--sizing-run', required=True, type=int)
    ap.add_argument('--repeats', type=int, default=2)
    a = ap.parse_args()
    case = a.case.rstrip('/\\')
    cdir, sdir = os.path.join(case, 'run%d_raw' % a.crossing_run), os.path.join(case, 'run%d_raw' % a.sizing_run)
    rec = json.load(open(os.path.join(cdir, 'batches.json'), encoding='utf-8'))
    model = Model(os.path.join(case, rec['model']))
    cfg = load_config(case)
    P = cfg['parameters']
    RATES = load_rates()
    rate, cell_for = make_rate_lookup(RATES)
    acts = declared_activities(cfg)
    act_by_id = {r['id']: r for r in acts}

    CLS = {r['element']: r['class'] for r in csv.DictReader(open(os.path.join(cdir, 'classes.tsv'), encoding='utf-8'), delimiter='\t')}
    CLS[model.root] = 'aggregate'
    ITEMS = [(r['activity'], r['element']) for r in csv.DictReader(open(os.path.join(cdir, 'work_model.tsv'), encoding='utf-8'), delimiter='\t')]
    # the root's per-parent items, outside every batch: every declared per-parent activity, × its cycles; the
    # surface-conditioned ones only if the root's subtree holds a surface (it does whenever any surface exists)
    has_surface = any(CLS.get(e) == 'surface' for e in model.order)
    for r in acts:
        kind, cyc = scope_kind(r['scope'])
        if kind != 'per_parent':
            continue
        if r['id'] in SURFACE_PARENT and not has_surface:
            continue
        n = (P['uat_cycles'] if r['id'] in ('U2', 'U3') else P['test_cycles']) if cyc else 1
        ITEMS += [(r['id'], model.root)] * max(1, n)

    leaf_ids = model.leaves()
    leaf_re = re.compile(r'\b(?:%s)\b' % '|'.join(sorted(map(re.escape, leaf_ids), key=len, reverse=True)))
    READINGS = {}
    for rep in range(1, a.repeats + 1):
        S, K, SP = {}, {}, {}
        for b in rec['batches']:
            fn = os.path.join(sdir, 'HD%d-%s%d.md' % (a.sizing_run, b, rep))
            if not os.path.exists(fn):
                print('!! missing', fn)
                continue
            s, k, sp = parse_reading(fn, leaf_re)
            S.update(s); K.update(k); SP.update(sp)
        READINGS[rep] = (S, K, SP)

    n_model = len(model.order)
    bracket = band(n_model, (30, 90, 10**9))
    n_si = sum(1 for e in model.order if CLS.get(e) in ('surface', 'interface'))
    n_env = len(P['environments'])

    def once_layer():
        """Once-scoped and per-environment items of the declared activities, sized by catalogue §3a."""
        out = []
        for r in acts:
            kind, cyc = scope_kind(r['scope'])
            aid = r['id']
            if kind == 'once' or (kind == 'once' and cyc):
                reps = 1
                if cyc:
                    reps = P['migration_rehearsal_cycles'] if aid.startswith('G') else P['test_cycles']
                    if reps == 0:
                        continue
                if aid in ('E3', 'E7'):
                    size, lab = band(n_env, (1, 2, 10**9)), '%d envs' % n_env
                elif aid in ('S2', 'S3'):
                    size, lab = band(n_si, (5, 12, 25)), '%d surf+int' % n_si
                elif rate(aid, 'single'):
                    size, lab = 'single', 'single'
                else:
                    size, lab = bracket, 'bracket'
                for i in range(reps):
                    out.append(('%s %s [%s]%s' % (aid, r['activity'], lab, ' #%d' % (i + 1) if reps > 1 else ''), rate(aid, size), aid))
            elif kind == 'per_environment':
                for env in P['environments']:
                    size = ENV_SIZE.get(env.lower().split(' ')[0], 'M')
                    out.append(('%s environment: %s [%s]' % (aid, env, size), rate(aid, size), aid))
        return out

    ONCE = once_layer()
    missing_rows = [lab for lab, cell, _ in ONCE if cell is None]
    assert not missing_rows, ('no rate row for', missing_rows)

    def assemble(rep):
        sizes, kinds, special = READINGS[rep]
        leafE, byact, sds, holes = defaultdict(float), defaultdict(float), [], []
        for act, el in ITEMS:
            cls = CLS.get(el, '?')
            if act in PER_PARENT:
                st = model.subtree(el)
                if act == 'A8':
                    size = band(sum(1 for x in st if CLS.get(x) in ('store', 'interface')), (1, 3, 6))
                elif act in SURFACE_PARENT:
                    n = sum(1 for x in st if CLS.get(x) == 'surface')
                    if n == 0:
                        holes.append((el, act, 'no surface in subtree (crosser filter should have refused)'))
                        continue
                    size = band(n, (1, 3, 6))
                else:
                    size = band(sum(1 for x in st if model.is_leaf(x)), (3, 8, 14))
                cell = cell_for(act, cls, size)
            elif act == 'D4':
                size = band(len(model.coverage_ids(el)), (1, 3, 6))
                cell = cell_for(act, cls, size)
            elif act in SPECIAL:
                size = special.get(el, 'MISSING')
                if size in (None, 'MISSING'):
                    holes.append((el, act, 'special count unsizeable' if size is None else 'special count not found in reading'))
                    continue
                cell = cell_for(act, cls, size)
            else:
                size = sizes.get(el, 'MISSING')
                if size in (None, 'MISSING'):
                    holes.append((el, act, 'unsizeable (M10)' if size is None else 'no size in reading'))
                    continue
                cell = cell_for(act, cls, size, kinds.get(el))
            if cell is None:
                holes.append((el, act, 'no rate cell for class %s size %s' % (cls, size)))
                continue
            leafE[el] += E(cell)
            byact[act] += E(cell)
            sds.append((cell[2] - cell[0]) / 6.0)
        c3 = {p: C3_RATE * sum(leafE.get(x, 0.0) for x in model.subtree(p)) for p in model.parents()}
        once_total = sum(E(c) for _, c, _ in ONCE)
        tl, tc3 = sum(leafE.values()), sum(c3.values())
        rho = 0.5
        once_sd = [(c[2] - c[0]) / 6.0 for _, c, _ in ONCE]
        var_el = (1 - rho) * sum(x * x for x in sds) + rho * sum(sds) ** 2
        var_once = (1 - rho) * sum(x * x for x in once_sd) + rho * sum(once_sd) ** 2
        sd_total = (var_el ** 0.5) * (1 + tc3 / tl if tl else 1) + var_once ** 0.5
        total = tl + tc3 + once_total
        xl = sorted(e for e, v in sizes.items() if v == 'XL')
        return dict(total=total, leaf_total=tl, c3_total=tc3, root_c3=c3.get(model.root, 0.0), once_total=once_total, sd=sd_total,
                    p10=total - 1.2816 * sd_total, p90=total + 1.2816 * sd_total, holes=holes, byact=dict(byact), leafE=leafE, c3=c3,
                    sized=sum(1 for v in sizes.values() if v), unsizeable=sorted(e for e, v in sizes.items() if v is None),
                    distribution={s: sum(1 for v in sizes.values() if v == s) for s in ('S', 'M', 'L', 'XL')},
                    xl=xl, xl_own_effort=sum(leafE.get(e, 0.0) for e in xl))

    res = {rep: assemble(rep) for rep in READINGS}
    # ---------------------------------------------------------------- print
    print('=== assembly: %s · model %s (%d elements, %d leaves, %d parents) · crossing run %d · sizing run %d · %d repeats'
          % (os.path.basename(case), model.id, n_model, len(leaf_ids), len(model.parents()), a.crossing_run, a.sizing_run, len(res)))
    print('=== declared: %s · environments %s · test cycles %s · UAT cycles %s · migration rehearsals %s · model bracket %s'
          % (', '.join(cfg['declared']), P['environments'], P['test_cycles'], P['uat_cycles'], P['migration_rehearsal_cycles'], bracket))
    for rep, r in res.items():
        print('=== repeat %d: sized %d · distribution %s · unsizeable %s' % (rep, r['sized'], r['distribution'], r['unsizeable']))
        print('  element leaf E (incl. root per-parent items): %.1f h' % r['leaf_total'])
        print('  C3 all parents:                               %.1f h   of which root C3: %.1f' % (r['c3_total'], r['root_c3']))
        print('  once + per-environment layer [%s]:            %.1f h  (%d items)' % (bracket, r['once_total'], len(ONCE)))
        print('  GRAND TOTAL:                                  %.0f net person-hours  (= %.1f pd at 8 h)' % (r['total'], r['total'] / 8))
        print('  corridor, rho = 0.5:  sd %.0f h · P10 %.0f · P90 %.0f  (x%.2f / x%.2f of the centre)' % (r['sd'], r['p10'], r['p90'], r['p10'] / r['total'], r['p90'] / r['total']))
        print('  XL leaves %d, own effort %.1f h: %s' % (len(r['xl']), r['xl_own_effort'], ', '.join(r['xl'])))
        print('  named holes (%d):' % len(r['holes']))
        for h in r['holes']:
            print('     ', h)
    r1 = res[min(res)]
    print('=== composition, repeat %d - per top-level subtree: element items + C3 inside the subtree' % min(res))
    for top in model.kids[model.root]:
        st = model.subtree(top)
        el = sum(r1['leafE'].get(x, 0.0) for x in st)
        c3 = sum(r1['c3'].get(x, 0.0) for x in st if x in r1['c3'])
        print('   %-6s %-40s elements %3d  items %6.0f h  C3 %6.0f h  subtotal %6.0f h' % (top, model.rows[top]['name'][:40], len(st), el, c3, el + c3))
    print('   root own per-parent items %.0f h · root C3 %.0f h · once/per-env %.0f h' % (r1['leafE'].get(model.root, 0.0), r1['root_c3'], r1['once_total']))
    print('=== composition, repeat %d - per activity (element-attached items only, hours)' % min(res))
    for act, v in sorted(r1['byact'].items(), key=lambda kv: -kv[1]):
        print('   %-4s %7.0f  %s' % (act, v, act_by_id.get(act, {}).get('activity', '')))
    print('=== once / per-environment items:')
    for lab, cell, _ in ONCE:
        print('   %-52s E = %5.1f' % (lab, E(cell)))
    dem = rec.get('demanded_ids', [])
    if dem:
        print('=== demanded ids (W6): %s — absorbed or standing per the crossing\'s §6; a standing branch has no table row and is carried, not priced here' % ', '.join(dem))
    if len(res) > 1:
        s1, k1, sp1 = READINGS[1]
        s2, k2, sp2 = READINGS[2]
        common = [e for e in s1 if e in s2]
        diff = [(e, s1[e], s2[e]) for e in common if s1[e] != s2[e]]
        print('=== size-class agreement: %d elements in both, %d differ (%.1f%% agree)' % (len(common), len(diff), 100 * (1 - len(diff) / max(1, len(common)))))
        for d in diff:
            print('     ', d)
        print('=== statement-kind divergences:', [(e, k1.get(e), k2.get(e)) for e in set(k1) | set(k2) if k1.get(e) != k2.get(e)])
        print('=== special-count divergences:', [(e, sp1.get(e, '-'), sp2.get(e, '-')) for e in set(sp1) | set(sp2) if sp1.get(e, '-') != sp2.get(e, '-')])
    lo, hi = min(r['total'] for r in res.values()), max(r['total'] for r in res.values())
    print('=== repeat spread: %.0f .. %.0f net person-hours (x%.4f); centre %.0f h' % (lo, hi, hi / lo, (lo + hi) / 2))
    depth = [model.depth(e) for e in leaf_ids]
    print('=== tree: %d elements, %d leaves, %d parents; mean leaf depth %.2f' % (n_model, len(leaf_ids), len(model.parents()), sum(depth) / len(depth)))
    print('=== unit: net hours of work on the task (docs/instrument.md section 0). Leave, holidays, sickness and presence are NOT included.')
    summary = {'case': os.path.basename(case), 'model': rec['model'], 'model_id': model.id, 'crossing_run': a.crossing_run, 'sizing_run': a.sizing_run,
               'elements': n_model, 'leaves': len(leaf_ids), 'parents': len(model.parents()), 'mean_leaf_depth': round(sum(depth) / len(depth), 2),
               'bracket': bracket, 'declared': cfg['declared'], 'parameters': P, 'once_items': len(ONCE),
               'repeats': {rep: {k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items() if k not in ('leafE', 'c3', 'byact')} for rep, r in res.items()},
               'centre_h': round((lo + hi) / 2), 'lo_h': round(lo), 'hi_h': round(hi), 'spread': round(hi / lo, 4),
               'sd_rho05_h': round(sum(r['sd'] for r in res.values()) / len(res)),
               'class_agreement_pct': round(100 * (1 - len(diff) / max(1, len(common))), 1) if len(res) > 1 else None}
    json.dump(summary, open(os.path.join(sdir, 'assembly_summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)


if __name__ == '__main__':
    main()
