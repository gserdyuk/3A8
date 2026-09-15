"""Run 60, part 2 - assemble the Steps B-D (diagnostician) prompt for the 2.1 chain's reading of SAS.
Built from run 48's diagnostician prompt (run48_raw/prompt_steps_bd.md, recovered from the transcript) so that
everything that is not the bottom-up changes as little as possible: INPUT 1 (project description) and INPUT 2
(assumption log) verbatim; INPUT 4 (the two RC46 readings) verbatim; the framing edited for the 2.1 engine chain;
INPUT 3 replaced by the run 59 assembly output verbatim; INPUT 5 replaced by RK60 (the Step C rates for this
chain) verbatim; the precomputed bases replaced by run 59's. Writes prompt_steps_bd.md next to this file.
Usage: python examples/SAS/run60_raw/make_prompt_bd60.py"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.abspath(os.path.join(HERE, '..'))

src = open(os.path.join(CASE, 'run48_raw', 'prompt_steps_bd.md'), encoding='utf-8').read()
src = src[src.index('-->') + 3:].lstrip('\n')            # drop the recovery header
L = src.split('\n')


def find(prefix, start=0):
    for i in range(start, len(L)):
        if L[i].startswith(prefix):
            return i
    raise KeyError(prefix)


i_in1 = find('# INPUT 1')
i_in3 = find('# INPUT 3')
i_in4 = find('# INPUT 4')
i_in5 = find('# INPUT 5')
i_bases = find('# Precomputed bases')
i_ask = find('# What is asked of you')

framing = '\n'.join(L[:i_in1])
framing = framing.replace(
    "- bottom-up: product model `Hotyn-M 1.1` (n = 2, first reading carried) → work model `Hotyn-W 1.1` (seven batches) → size classes `Hotyn-D 2.0` (n = 2, both repeats priced) × rate table v0.1-h (`Hotyn-K`), assembled by script; all sensors on Claude Opus 5;",
    "- bottom-up: product model `Hotyn-M 2.1` (n = 2, first reading carried; in this generation coverage lives in leaves only and distinct leaves realising the same obligations are kept apart) → work model `Hotyn-W 1.2` (seven batches) → size classes `Hotyn-D 2.0` (n = 2, both repeats priced; the repeats declared opposite rules for obligations shared by several leaves and differ ×1.09 on the total) × rate table v0.1-h (`Hotyn-K`), assembled by script; all sensors on Claude Opus 5;")
assert 'Hotyn-M 2.1' in framing
inputs12 = '\n'.join(L[i_in1:i_in3])
input4 = '\n'.join(L[i_in4:i_in5])
ask = '\n'.join(L[i_ask:])

assembly = open(os.path.join(HERE, 'assembly_run59_output.txt'), encoding='utf-8').read().strip('\n')
input3 = """# INPUT 3 — the bottom-up estimate (run 1): the assembly of the sized work model, both repeats, script output verbatim

Conventions of the assembly: rooted subtrees; every element carries its crossed activities as items; each item is priced from the rate table cell (activity × element class × size class) as E = (O + 4M + P) / 6; C3 (coordination) is 20% of the leaf-item effort at every parent including the root; once-scoped and per-environment items sit outside every C3 base. Holes are items the sizing refused (unsizeable elements, or migration counts for which no entity kind was shown to need loading from a predecessor); they are named, never guessed, and priced at nothing. The corridor line is the O/M/P of every priced item summed at an equicorrelation of ρ = 0.5 — the declared convention, not a measurement. The model's ids: N = node, A = accreted leaf (placed at a requirement), C = derived leaf (added at completion, no requirement of its own), CN = derived node.

Carried-not-priced beside the number, per A1: W-4 (the post-production support period and the transition service — no term, no service level; the crossing entered it as a demanded branch `DW-4` without an activity) and NFR-5 (impact analysis on deviation, read at count 0).

The two repeats of the sizing step declared opposite rules for one question the sizing rules do not settle — whether an obligation shared by several leaves is counted in full on each leaf (repeat 1) or only for the part each leaf's name claims (repeat 2) — and this, not random disagreement, is why repeat 1 sits a class higher across the board (13 XL against 3). Both are legal readings; keep them as a band.

```
""" + assembly + """
```
"""

rk = open(os.path.join(HERE, 'RK60.md'), encoding='utf-8').read()
rk_body = rk[rk.index('-->') + 3:].lstrip('\n') if rk.startswith('<!--') else rk
input5 = "# INPUT 5 — the calibration rates from Step C, gap-blind, verbatim\n\n" + rk_body.rstrip('\n') + "\n"

# bases: RK60's fills priced by price_fills60.py (run it first); the diagnostician gets the priced bases, not the chain's result
bases = open(os.path.join(HERE, 'bases60.md'), encoding='utf-8').read()

out = '\n'.join([framing.rstrip('\n'), '', inputs12.rstrip('\n'), '', input3.rstrip('\n'), '', input4.rstrip('\n'), '', input5.rstrip('\n'), '', bases.rstrip('\n'), '', ask.rstrip('\n'), ''])
dst = os.path.join(HERE, 'prompt_steps_bd.md')
open(dst, 'w', encoding='utf-8', newline='\n').write(out)
print(dst, len(out), 'chars')
for h in re.findall(r'^# .*$', out, re.M):
    print('  ', h[:90])
