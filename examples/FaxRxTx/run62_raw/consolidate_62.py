#!/usr/bin/env python3
"""Run 62: tools/chain/consolidate_crossing.py, unchanged, with one read-time normalisation.

HW62-C1 §4 defines its element groups as '- **PAR7** is the 7 nodes: …' and '- **BUILD27** is the 27 leaves …';
the consolidator recognises a group only in the form '**NAME** = …', so the five PAR7 rows (A5, A6, A7, A8, D2 —
49 items) were dropped with a printed mismatch. The raw reply stays verbatim on disk; this wrapper rewrites
' is the ' to ' = the ' on those two definition lines, in memory, when section 4 is read. Nothing else changes.

    py -X utf8 run62_raw/consolidate_62.py
"""
import os, sys
sys.path.insert(0, r'C:\home\OhmNova\3A8\tools\chain')
import consolidate_crossing as cc

CASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_orig = cc.md_section
FIX = [('- **PAR7** is the 7 nodes:', '- **PAR7** = the 7 nodes:'),
       ('- **BUILD27** is the 27 leaves', '- **BUILD27** = the 27 leaves')]


def patched(t, n):
    s = _orig(t, n)
    if n == 4:
        for a, b in FIX:
            if a in s:
                s = s.replace(a, b)
                print('[run62 wrapper] normalised: %r' % a, file=sys.stderr)
    return s


cc.md_section = patched
sys.argv = ['consolidate_crossing.py', CASE, '--run', '62']
cc.main()
