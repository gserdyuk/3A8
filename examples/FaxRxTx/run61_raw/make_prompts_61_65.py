#!/usr/bin/env python3
"""Orchestrator helper: copy the pinned inputs of FaxRxTx into the scratch case folder (byte for byte) and build
the two hand-assembled prompts of this estimate from them — the product-model prompt (run 61) and the
outside-view prompt (run 65). Prints every md5. Nothing is paraphrased: inputs are pasted verbatim; the only
edit is the struck lines of the project description, listed in STRUCK and in the run 65 manifest.
"""
import hashlib, os, shutil

REPO = r'C:\home\OhmNova\3A8'
SRC = os.path.join(REPO, 'examples', 'FaxRxTx')
CASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINNED = ['requirements_pinned.md', 'requirements.pin.txt', 'requirements_split.md', 'requirements_product.md',
          'requirements_work.md', 'assumptions.md', 'assumptions_product.md', 'technology_declaration.md',
          'chain_config.json', 'SYSTEM.md', 'REQUIREMENTS.md']


def md5b(b):
    return hashlib.md5(b).hexdigest()


def md5_lf(p):
    return md5b(open(p, 'rb').read().replace(b'\r', b''))


QUARANTINE = ("**Quarantine instruction.** Your context may carry ambient repository information prepended by the harness — "
              "a git status, recent commit subjects, directory names. None of it is your input. Do not read it, do not act on it, "
              "do not treat it as contamination that stops the run: report in your contamination check that it was present and "
              "that you quarantined it, and proceed on the pasted input alone.")

def read(name):
    return open(os.path.join(SRC, name), encoding='utf-8').read().replace('\r\n', '\n')


def description():
    """SYSTEM.md with the lines that carry duration, dates of the work, money, or the outcome's location struck."""
    t = read('SYSTEM.md')
    cuts = [
        # §6 process: the calendar span of the work
        ('There was no hard deadline, but there was pressure. The team included\nQA/PM, not just developers. The work period — roughly 2007–2009\n(the participant named both "2007–2008" and "2008–2009").',
         'There was no hard deadline, but there was pressure. The team included\nQA/PM, not just developers. [struck by the orchestrator: the calendar period of the work]'),
        # §7: money and the dating inference
        ('- Acquired by j2 Global in September 2010 for ~$17M; revenue ~$10M over\n  the preceding 12 months. Since 2006 there was a patent lawsuit by Venali against j2,\n  closed by the deal.\n- A cluster on Windows 7 (released in October 2009) + the sale of the company in 2010\n  constrain the dating of the development described to roughly 2005–2010;\n  the exact period — to be clarified with the participant.',
         '- [struck by the orchestrator: the company\'s later acquisition, its price and revenue, and a dating inference for the development period]'),
        # §8: the pointer to the outcome
        ('The project\'s actual outcome (team size, duration, final\nperson-months) is recorded separately in **FACT.md** and must not enter\nthe context of the estimator agents. The check against fact — only at the final\nStep D of the pipeline.',
         '[struck by the orchestrator: a note on where the outcome is kept]'),
    ]
    for old, new in cuts:
        assert old in t, old[:60]
        t = t.replace(old, new)
    # the closing note on REQUIREMENTS.md is about another document, not this system
    i = t.index('## A note on REQUIREMENTS.md')
    t = t[:i] + '[struck by the orchestrator: a closing note about an unrelated draft document]\n'
    return t, cuts


def main():
    os.makedirs(CASE, exist_ok=True)
    print('pinned inputs (md5 of bytes · md5 with CR stripped):')
    for n in PINNED + ['FACT.md']:
        p = os.path.join(SRC, n)
        if n == 'FACT.md':
            print('  FACT.md exists: %s (not opened, not copied)' % os.path.exists(p))
            continue
        shutil.copyfile(p, os.path.join(CASE, n))
        print('  %-28s %s · %s' % (n, md5b(open(p, 'rb').read()), md5_lf(p)))
    print('  %-28s %s' % ('case_profile.md (scratch)', md5b(open(os.path.join(CASE, 'case_profile.md'), 'rb').read())))

    # ---- run 61, product model
    rp = read('requirements_product.md')
    ap = read('assumptions_product.md')
    m = ('Build the product model of the system whose obligations are listed below. Everything you need is in this message; read no files.\n\n'
         + QUARANTINE + '\n\n'
         '**Declared processing order: Order A** — the order of INPUT 1 as given, F01 first, F47 last.\n\n'
         '**Output.** Emit the complete deliverable in one reply, beginning at section 1 and ending at section 9, with every section your engine definition requires.\n\n'
         '---\n\n# INPUT 1 — the pinned product obligation list (`requirements_product.md`, N = 47), verbatim\n\n' + rp +
         '\n---\n\n# INPUT 2 — the assumption log a product-model run may see (`assumptions_product.md`), verbatim\n\n' + ap)
    d61 = os.path.join(CASE, 'run61_raw')
    os.makedirs(d61, exist_ok=True)
    p = os.path.join(d61, 'prompt_M.md')
    open(p, 'w', encoding='utf-8', newline='\n').write(m)
    print('run61 prompt_M.md  %6d chars md5 %s' % (len(m), md5b(open(p, 'rb').read())))

    # ---- run 65, outside view
    desc, cuts = description()
    al = read('assumptions.md')
    r = ('Forecast the effort of the project described below from the outside view. Everything you need is in this message; read no files.\n\n'
         + QUARANTINE + '\n\n'
         '**Output.** Emit the complete deliverable in one reply, every section your engine definition requires, the declaration first.\n\n'
         '---\n\n# INPUT 1 — the project description (`SYSTEM.md`, with the struck lines marked in place)\n\n' + desc +
         '\n---\n\n# INPUT 2 — the assumption log (`assumptions.md`), verbatim\n\n' + al)
    d65 = os.path.join(CASE, 'run65_raw')
    os.makedirs(d65, exist_ok=True)
    p = os.path.join(d65, 'prompt_R.md')
    open(p, 'w', encoding='utf-8', newline='\n').write(r)
    print('run65 prompt_R.md  %6d chars md5 %s' % (len(r), md5b(open(p, 'rb').read())))
    print('struck from SYSTEM.md: %d passages + the closing note' % len(cuts))


if __name__ == '__main__':
    main()
