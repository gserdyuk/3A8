#!/usr/bin/env python3
"""Step 3, the prompts: one work-estimator prompt per crossing batch.

    python tools/chain/make_sizing_prompts.py examples/<case> --crossing-run <N> --run <K>

Reads run<N>_raw/batches.json, classes.tsv and work_model.tsv (the consolidated crossing), the model the crossing
was made on, and requirements_product.md (the obligation texts). INPUT 2, the sizing rules, is
tools/chain/fragments/sizing_rules.md (catalogue §3a as the sensor has received it since run 47). Writes
run<K>_raw/prompt_size_<batch>.md and sizing_batches.json; prints each prompt's size and md5. Contains no rate,
price, effort or duration. Both repeats of a batch receive the same file.
"""
import argparse, csv, hashlib, json, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chainlib import Model

HEADER = """Size the elements of the work model batch below by classifying, not pricing. Everything you need is in this message; read no files.

**Scope: the subtrees rooted at {roots} of the product model `{model_id}`, as classified and crossed by `{crosser}`** — {n} sized elements (aggregates are listed for context and are never sized). Other subtrees and the model root are outside this batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, sections 1 to 7 as your engine definition requires. In the sizing table quote the enumeration verbatim, one row per sized element, grouped by subtree. Every number you output is a count of named things; nothing else.

---

# INPUT 1 — the work model batch: elements with class, parent, declared content, covered obligations (with their texts) and the activities crossed onto them

In this model coverage lives in leaves only: an aggregate's content is its children. A derived leaf has no covered obligation; its declared content is its name read with the trigger that called for it (the elements named after `trigger:`).

"""


def obligation_texts(case):
    req = {}
    for fn in ('requirements_product.md', 'requirements_work.md'):
        p = os.path.join(case, fn)
        if not os.path.exists(p):
            continue
        header = None
        for line in open(p, encoding='utf-8'):
            if not line.startswith('|'):
                continue
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if header is None:
                if c and c[0].lower() == 'id':
                    header = c
                continue
            if set(''.join(c)) <= set('-: ') or len(c) < 2:
                continue
            req.setdefault(c[0], c[1])
    return req


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('case')
    ap.add_argument('--crossing-run', required=True, type=int)
    ap.add_argument('--run', required=True, type=int)
    a = ap.parse_args()
    case = a.case.rstrip('/\\')
    cdir = os.path.join(case, 'run%d_raw' % a.crossing_run)
    rec = json.load(open(os.path.join(cdir, 'batches.json'), encoding='utf-8'))
    model = Model(os.path.join(case, rec['model']))
    crosser = rec.get('crosser_engine') or 'Hotyn-W'
    req = obligation_texts(case)
    classes = {r['element']: r['class'] for r in csv.DictReader(open(os.path.join(cdir, 'classes.tsv'), encoding='utf-8'), delimiter='\t')}
    acts = defaultdict(set)
    for r in csv.DictReader(open(os.path.join(cdir, 'work_model.tsv'), encoding='utf-8'), delimiter='\t'):
        acts[r['element']].add(r['activity'])
    rules = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fragments', 'sizing_rules.md'), encoding='utf-8').read()
    out_dir = os.path.join(case, 'run%d_raw' % a.run)
    os.makedirs(out_dir, exist_ok=True)
    record = {'crossing_run': a.crossing_run, 'model': rec['model'], 'model_id': model.id, 'batches': rec['batches'], 'prompts': {}}
    for b, roots in rec['batches'].items():
        ids = []
        for r in roots:
            ids += model.subtree(r)
        rows, sized = [], 0
        for e in model.order:
            if e not in ids:
                continue
            n = model.rows[e]
            cls = classes.get(e, '?')
            if cls == 'aggregate':
                rows.append('\n**%s — %s** · aggregate (not sized) · parent %s\n' % (e, n['name'], n['parent']))
                continue
            sized += 1
            cov_ids = model.coverage_ids(e)
            if cov_ids:
                cov = '; '.join('%s: %s' % (r, req.get(r, '?')) for r in cov_ids)
            else:
                cov = '— (derived element, no covered obligation; %s)' % (n['coverage'] or 'no trigger recorded')
            al = ', '.join(sorted(acts.get(e, []), key=lambda x: (x[0], len(x), x)))
            rows.append('- **%s — %s** · class **%s** · parent %s\n  - covered obligations: %s\n  - activities crossed onto it: %s\n' % (e, n['name'], cls, n['parent'], cov, al))
        body = HEADER.format(roots=', '.join(roots), model_id=model.id, crosser=crosser, n=sized) + ''.join(rows) + '\n---\n\n' + rules
        p = os.path.join(out_dir, 'prompt_size_%s.md' % b)
        open(p, 'w', encoding='utf-8', newline='\n').write(body)
        md5 = hashlib.md5(open(p, 'rb').read()).hexdigest()
        record['prompts'][b] = {'file': 'prompt_size_%s.md' % b, 'sized': sized, 'chars': len(body), 'md5': md5}
        print('%s %-24s sized %3d %6d chars md5 %s' % (b, ','.join(roots), sized, len(body), md5))
    json.dump(record, open(os.path.join(out_dir, 'sizing_batches.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
