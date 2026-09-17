#!/usr/bin/env python3
"""Run 69 — the moderator's helper for the Delphi among ten bare estimators.

    py -X utf8 delphi.py extract <round>     # transcribe the round's ten replies verbatim, build the next round's sheet
    py -X utf8 delphi.py stats               # the table of totals and ranges per round

The harness keeps each participant's transcript (~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl).
A participant is continued across rounds, so its transcript holds one segment per round: a user message (the round's
instruction) followed by the participant's turns. `extract` copies the assistant text of segment <round> unchanged
under an orchestrator header, records per segment the model, stop reasons, output tokens and every tool use with its
target, and writes sheet_R<round+1>.md: the ten replies verbatim, labelled P-1 … P-10, nothing added. It judges nothing.
The actual outcome appears only in `stats`, never in a sheet.
"""
import glob, hashlib, json, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.expanduser(r'~/.claude/projects/C--home-OhmNova-3A8')
PARTICIPANTS = json.load(open(os.path.join(HERE, 'participants.json'), encoding='utf-8'))   # {"P-1": agentId, ...}
ACTUAL_PM = 13745 / 168.0      # the actual, in the prompt's A9 person-months; used by `stats` only


def transcript(agent):
    hits = glob.glob(os.path.join(PROJ, '*', 'subagents', 'agent-%s.jsonl' % agent))
    assert len(hits) == 1, (agent, hits)
    return [json.loads(l) for l in open(hits[0], encoding='utf-8')]


def text_of(content):
    if isinstance(content, str):
        return content
    return ''.join(b.get('text', '') for b in content if b.get('type') == 'text')


def segments(rows):
    """One segment per user instruction (tool results are not instructions)."""
    segs = []
    for d in rows:
        t, m = d.get('type'), d.get('message') or {}
        if t == 'user':
            c = m.get('content')
            if isinstance(c, list) and all(b.get('type') == 'tool_result' for b in c):
                continue
            segs.append({'instruction': text_of(c), 'texts': [], 'turns': {}, 'tools': []})
        elif t == 'assistant' and segs:
            s = segs[-1]
            mid = m.get('id')
            for b in m.get('content') or []:
                if b.get('type') == 'text' and b.get('text', '').strip():
                    s['texts'].append(b['text'])
                elif b.get('type') == 'tool_use':
                    inp = b.get('input') or {}
                    s['tools'].append('%s %s' % (b.get('name'), inp.get('file_path') or inp.get('command') or inp.get('pattern') or ''))
            u = m.get('usage') or {}
            s['turns'][mid] = {'model': m.get('model'), 'stop_reason': m.get('stop_reason'), 'output_tokens': u.get('output_tokens')}
    return segs


def closing(reply):
    tot = re.search(r'TOTAL:\s*\**\s*~?\s*(\d+(?:\.\d+)?)', reply)
    rng = re.search(r'RANGE:\s*\**\s*~?\s*(\d+(?:\.\d+)?)\s*(?:\.\.\.|…|-|–|to)\s*~?\s*(\d+(?:\.\d+)?)', reply)
    return (float(tot.group(1)) if tot else None, float(rng.group(1)) if rng else None, float(rng.group(2)) if rng else None)


def extract(rnd):
    sheet, ledger = [], []
    for p, agent in PARTICIPANTS.items():
        segs = segments(transcript(agent))
        assert len(segs) >= rnd, (p, 'has %d segments, round %d asked' % (len(segs), rnd))
        s = segs[rnd - 1]
        reply = '\n\n'.join(s['texts'][-1:])          # the final message of the round is the reply
        earlier = s['texts'][:-1]
        total, lo, hi = closing(reply)
        head = ('<!-- orchestrator header, not part of the reply: run 69, round %d, participant %s; general agent, no sensor\n'
                'definition; instruction md5 %s; turns %s; tool uses %s; interim text blocks before the reply: %d -->\n\n'
                % (rnd, p, hashlib.md5(s['instruction'].encode('utf-8')).hexdigest(),
                   json.dumps(list(s['turns'].values())), json.dumps(s['tools']), len(earlier)))
        open(os.path.join(HERE, 'R%d_%s.md' % (rnd, p)), 'w', encoding='utf-8', newline='\n').write(head + reply + '\n')
        ledger.append({'round': rnd, 'participant': p, 'agent': agent, 'total': total, 'low': lo, 'high': hi,
                       'turns': list(s['turns'].values()), 'tools': s['tools'], 'reply_chars': len(reply)})
        sheet.append('=' * 100 + '\n## %s — reply of round %d, verbatim\n\n%s\n' % (p, rnd, reply))
        print(p, 'TOTAL', total, 'RANGE', lo, hi, '| tools:', s['tools'], '| stops:', [t['stop_reason'] for t in s['turns'].values()])
    with open(os.path.join(HERE, 'ledger.jsonl'), 'a', encoding='utf-8', newline='\n') as f:
        for r in ledger:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    text = ('# Round %d — the ten replies, anonymous and verbatim\n\nNothing below was written, shortened or commented by the moderator.\n\n' % rnd
            + '\n'.join(sheet))
    fn = os.path.join(HERE, 'sheet_R%d.md' % (rnd + 1))
    open(fn, 'w', encoding='utf-8', newline='\n').write(text)
    print('sheet:', fn, len(text), 'chars, md5', hashlib.md5(text.encode('utf-8')).hexdigest())


def stats():
    rows = [json.loads(l) for l in open(os.path.join(HERE, 'ledger.jsonl'), encoding='utf-8')]
    import math
    for rnd in sorted({r['round'] for r in rows}):
        rs = [r for r in rows if r['round'] == rnd]
        t = [r['total'] for r in rs]
        ratio = [r['high'] / r['low'] for r in rs]
        inside = sum(1 for r in rs if r['low'] <= ACTUAL_PM <= r['high'])
        mean, med = statistics.mean(t), statistics.median(t)
        print('round %d: n=%d totals %s' % (rnd, len(t), [int(x) if x == int(x) else x for x in t]))
        print('   mean %.1f  median %.1f  sd %.1f  CV %.1f%%  max/min x%.2f' % (mean, med, statistics.stdev(t), 100 * statistics.stdev(t) / mean, max(t) / min(t)))
        print('   against the actual %.1f pm: mean x%.2f (ln %.3f)  median x%.2f (ln %.3f)' % (ACTUAL_PM, mean / ACTUAL_PM, math.log(mean / ACTUAL_PM), med / ACTUAL_PM, math.log(med / ACTUAL_PM)))
        print('   declared high/low, mean x%.2f; ranges containing the actual: %d of %d' % (statistics.mean(ratio), inside, len(rs)))


if __name__ == '__main__':
    if sys.argv[1] == 'extract':
        extract(int(sys.argv[2]))
    else:
        stats()
