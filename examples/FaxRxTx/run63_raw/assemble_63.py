#!/usr/bin/env python3
"""Run 63: tools/chain/assemble.py, unchanged, with a read-time overlay for special counts the parser missed.

The assembler finds a G1/G2/G3 special class in a sizing reply only in a few phrasings. Four replies state it in
other words; unparsed, the assembler prices those items as holes ("special count not found in reading"), which
would silently drop a class the sensor did assign. Each overlay entry below is (reading, element, class, phrase):
the phrase must occur verbatim in the raw reply or the script stops. Class None means the sensor stated that no
class applies (count 0), which the assembler then reports as 'special count unsizeable' instead of 'not found'.
The raw replies are not edited. Writes assembly_output.txt next to assembly_summary.json.

    py -X utf8 run63_raw/assemble_63.py
"""
import io, os, sys, contextlib
sys.path.insert(0, r'C:\home\OhmNova\3A8\tools\chain')
import assemble as A

HERE = os.path.dirname(os.path.abspath(__file__))
CASE = os.path.dirname(HERE)
OVERLAY = [
    ('HD63-A1.md', 'D01', 'M', '2 entity kinds need pre-loading, so the class is **M**'),
    ('HD63-A2.md', 'D01', 'M', '**Count: 2. Class: M.**'),
    ('HD63-C1.md', 'L01', 'M', '**L01, count 2, M.**'),
    ('HD63-C1.md', 'D03', 'S', '**D03, count 1, S.**'),
    ('HD63-B2.md', 'L32', None, '**Count: 0.** No threshold row matches zero'),
]
_orig = A.parse_reading
applied = []


def patched(fn, leaf_re):
    sizes, kinds, special = _orig(fn, leaf_re)
    base = os.path.basename(fn)
    text = open(fn, encoding='utf-8').read()
    for f, el, cls, phrase in OVERLAY:
        if f != base:
            continue
        assert phrase in text, (f, phrase)
        before = special.get(el, 'not found')
        special[el] = cls
        applied.append('%s %s: parser %s -> %s  (reply: "%s")' % (f, el, before, cls, phrase))
    return sizes, kinds, special


A.parse_reading = patched
sys.argv = ['assemble.py', CASE, '--crossing-run', '62', '--sizing-run', '63']
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    A.main()
    print('=== run 63 read-time overlay (assemble_63.py), %d entries:' % len(applied))
    for a in applied:
        print('     ' + a)
out = buf.getvalue()
open(os.path.join(HERE, 'assembly_output.txt'), 'w', encoding='utf-8', newline='\n').write(out)
print(out)
