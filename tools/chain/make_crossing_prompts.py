#!/usr/bin/env python3
"""Step 2, the prompts: one work-crosser prompt per batch of a closed 2.x product model.

    python tools/chain/make_crossing_prompts.py examples/<case> --model examples/<case>/run<M>_raw/HM<M>-1.md --run <N>

Reads examples/<case>/chain_config.json (the declared technology codes, the parameters, optional batches),
the model's section 6 TSV, docs/technology_catalogue.md (the declared entries' activity tables), and the case's
requirements_work.md and technology_declaration.md (the demanded-work list and its absorption). Writes
examples/<case>/run<N>_raw/prompt_<batch>.md and batches.json, and prints each prompt's size and md5.

INPUT 1 is the batch's subtrees from the model; INPUT 2 is the declaration as the crosser must see it — the
catalogue's tables verbatim, no prose, no pricing vocabulary; INPUT 3 rides with the last batch only. The header
is the one runs 45 and 58 used. Batches default to the root's children grouped in model order to at most
--batch-size elements; chain_config.json may fix them instead ("batches": {"A": ["N02"], ...}).
"""
import argparse, hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chainlib import Model, load_config, declaration_input, demanded_input

HEADER = """Cross the product model subtrees named below with the declared technology. Everything you need is in this message; read no files.

**Partial run.** Scope: the subtrees rooted at **{roots}** of the closed product model `{model_id}` — **{n} elements**, listed in INPUT 1 with their parents and coverage. The model root `{root}` and every other subtree are outside this batch: do not cross them and do not speculate about them. Per the partial-run rule, once-scoped and per-environment activities are **deferred**, not generated, and per-parent activities apply only to parents inside the batch.

**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, do not treat it as contamination that stops the run: report in your contamination check that it was present and that you quarantined it, and proceed on the pasted input alone.

**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section the engine definition requires. **Compact §4 at the orchestrator's instruction: one row per activity — activity id, scope, the element ids receiving an item, the count — with item ids of the form `ACTIVITY@ELEMENT`.** The classification log (§3) and the `no` log (§5) are not compacted: every element with its class, every refusal with its kind and reason.

---

# INPUT 1 — the product model subtrees in scope (from `{model_id}`, `{engine}`, closed and normalised)

This model keeps coverage in leaves only. **A node (an element with children) has an empty coverage column by rule; its content is its children.** A leaf's declared content is its name together with the obligations it covers. A derived leaf has no requirement coverage: its column holds `trigger: <ids>`, the elements whose existence called for it, and its content is its name read with that trigger.{derived_nodes} Every element listed here has its parent listed here, except the batch roots whose parent is `{root}`. Origin values: posited (skeleton), accreted (added at a requirement), derived (added at completion).

| id | name | parent | origin | coverage |
|---|---|---|---|---|
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('case')
    ap.add_argument('--model', required=True)
    ap.add_argument('--run', required=True, type=int)
    ap.add_argument('--batch-size', type=int, default=36)
    a = ap.parse_args()
    case = a.case.rstrip('/\\')
    cfg = load_config(case)
    model = Model(a.model)
    batches = cfg.get('batches') or model.auto_batches(a.batch_size)
    out_dir = os.path.join(case, 'run%d_raw' % a.run)
    os.makedirs(out_dir, exist_ok=True)
    decl = declaration_input(cfg)
    dem, dem_ids = demanded_input(case)
    derived_nodes = [k for k in model.parents() if model.rows[k]['coverage'].lower().startswith('trigger')]
    dn = (' Derived node%s (%s) carr%s a trigger in the column as well; %s node%s — the content is the children — and the trigger is not coverage.'
          % ('s' if len(derived_nodes) > 1 else '', ', '.join('`%s`' % k for k in derived_nodes), 'y' if len(derived_nodes) > 1 else 'ies',
             'they are' if len(derived_nodes) > 1 else 'it is a', 's' if len(derived_nodes) > 1 else '')) if derived_nodes else ''
    record = {'model': os.path.relpath(a.model, case).replace('\\', '/'), 'model_id': model.id, 'engine': model.engine, 'root': model.root,
              'batches': {}, 'prompts': {}, 'demanded_ids': dem_ids, 'declared': cfg['declared'], 'parameters': cfg['parameters']}
    last = list(batches)[-1]
    covered = set()
    for b, roots in batches.items():
        ids = []
        for r in roots:
            ids += model.subtree(r)
        covered |= set(ids)
        rows = ''.join('| %s | %s | %s | %s | %s |\n' % (k, model.rows[k]['name'], model.rows[k]['parent'], model.rows[k]['origin'], model.rows[k]['coverage'] or '—')
                       for k in model.order if k in ids)
        body = HEADER.format(roots=', '.join(roots), model_id=model.id, engine=model.engine, n=len(ids), root=model.root, derived_nodes=dn) + rows + '\n---\n\n' + decl
        if b == last:
            body += '\n---\n\n' + dem
        p = os.path.join(out_dir, 'prompt_%s.md' % b)
        open(p, 'w', encoding='utf-8', newline='\n').write(body)
        md5 = hashlib.md5(open(p, 'rb').read()).hexdigest()
        record['batches'][b] = roots
        record['prompts'][b] = {'file': 'prompt_%s.md' % b, 'elements': len(ids), 'chars': len(body), 'md5': md5}
        print('%s %-24s %3d elements %6d chars md5 %s' % (b, ','.join(roots), len(ids), len(body), md5))
    missing = [k for k in model.order if k not in covered and k != model.root]
    assert not missing, ('elements in no batch', missing)
    json.dump(record, open(os.path.join(out_dir, 'batches.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('all %d non-root elements batched; root %s outside every batch; demanded ids %s ride with batch %s' % (len(covered), model.root, dem_ids, last))


if __name__ == '__main__':
    main()
