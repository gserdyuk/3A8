#!/usr/bin/env python3
"""Runs 72-73 — the moderator's helper for the rule-bound Delphi. Builds on run69_raw/delphi.py.

    py -X utf8 delphi_rules.py <run_raw dir> extract <round>   # replies verbatim, ledger, next sheet in two parts
    py -X utf8 delphi_rules.py <run_raw dir> stats

The next round's sheet is written as two files so that each fits one read (run 70's single sheet was cut at ~60k
characters): part 1 holds P-1 ... P-5, part 2 holds P-6 ... P-10 and, from round 2 on, the list of CONTESTED ADDITIONS.
That list is compiled mechanically: every block a participant wrote under the heading "ADDED" is copied verbatim
under the participant's label. The moderator writes nothing else into a sheet.
"""
import hashlib, json, os, re, sys

HERE = os.path.abspath(sys.argv[1])
CASE = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(CASE, 'run69_raw'))
_argv, sys.argv = sys.argv, [sys.argv[0], HERE]
import delphi   # noqa: E402
sys.argv = _argv

ADDED = re.compile(r'^\W*ADDED\b.*?$(.*?)(?=^\W*(?:VOTES?|CONTESTED|FINAL|TOTAL:|```|#{1,3} )|\Z)', re.S | re.M)


def added_block(reply):
    m = ADDED.search(reply)
    return m.group(0).strip() if m else None


def extract(rnd):
    parts = delphi.PARTICIPANTS
    blocks, contested, ledger = [], [], []
    for p, agent in parts.items():
        s = delphi.segments(delphi.transcript(agent))[rnd - 1]
        reply = s['texts'][-1]
        total, lo, hi = delphi.closing(reply)
        head = ('<!-- orchestrator header, not part of the reply: run %s, round %d, participant %s; general agent, no sensor\n'
                'definition; instruction md5 %s; turns %s; tool uses %s -->\n\n'
                % (os.path.basename(HERE).replace('_raw', '').replace('run', ''), rnd, p,
                   hashlib.md5(s['instruction'].encode('utf-8')).hexdigest(), json.dumps(list(s['turns'].values())), json.dumps(s['tools'])))
        open(os.path.join(HERE, 'R%d_%s.md' % (rnd, p)), 'w', encoding='utf-8', newline='\n').write(head + reply + '\n')
        ledger.append({'round': rnd, 'participant': p, 'agent': agent, 'total': total, 'low': lo, 'high': hi,
                       'turns': list(s['turns'].values()), 'tools': s['tools'], 'reply_chars': len(reply)})
        blocks.append('=' * 100 + '\n## %s — reply of round %d, verbatim\n\n%s\n' % (p, rnd, reply))
        a = added_block(reply)
        if a and rnd >= 2:
            contested.append('### from %s\n\n%s\n' % (p, a))
        print(p, 'TOTAL', total, 'RANGE', lo, hi, '| tools:', len(s['tools']), '| chars', len(reply), '| ADDED block:', bool(a))
    with open(os.path.join(HERE, 'ledger.jsonl'), 'a', encoding='utf-8', newline='\n') as f:
        for r in ledger:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    intro = '# Replies of round %d — anonymous and verbatim, part %d of 2\n\nNothing below was written, shortened or commented by the moderator.\n\n'
    p1 = intro % (rnd, 1) + '\n'.join(blocks[:5])
    p2 = intro % (rnd, 2) + '\n'.join(blocks[5:])
    if rnd >= 2:
        p2 += ('\n' + '=' * 100 + '\n## CONTESTED ADDITIONS — every "ADDED" block of round %d, copied verbatim under its author\'s label\n\n' % rnd
               + ('\n'.join(contested) if contested else '(no participant listed an addition)\n'))
    for i, text in ((1, p1), (2, p2)):
        fn = os.path.join(HERE, 'sheet_R%d_part%d.md' % (rnd + 1, i))
        open(fn, 'w', encoding='utf-8', newline='\n').write(text)
        print('sheet part %d: %d chars, %d lines, md5 %s' % (i, len(text), text.count('\n'), hashlib.md5(text.encode('utf-8')).hexdigest()))


if __name__ == '__main__':
    if sys.argv[2] == 'extract':
        extract(int(sys.argv[3]))
    else:
        delphi.stats()
