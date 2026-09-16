#!/usr/bin/env python3
"""Orchestrator helper, run 61 onward: transcribe a subagent's reply verbatim from the harness transcript.

    py -X utf8 extract_reply.py --agent <agentId> --out <run_raw>/<ID>.md --reading <ID> --run <N> --prompt <run_raw>/<prompt file>

The harness does not persist subagent output in the case folder; it does keep the subagent's transcript
(~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl). This script copies the assistant text
blocks out of that transcript, in order, unchanged, under an orchestrator header, and records per turn the
model, stop reason and output tokens, every user-side message after the prompt (a harness continuation
message would appear there), and whether the prompt the sensor received is byte-identical to the saved one.
It appends the same facts as one JSON line to <run_raw>/turns.jsonl. It judges nothing.
"""
import argparse, glob, hashlib, json, os, re, sys

PROJ = os.path.expanduser(r'~/.claude/projects/C--home-OhmNova-3A8')


def find(agent):
    hits = glob.glob(os.path.join(PROJ, '*', 'subagents', 'agent-%s.jsonl' % agent))
    if len(hits) != 1:
        sys.exit('transcript for %s: %r' % (agent, hits))
    return hits[0]


def text_of(content):
    if isinstance(content, str):
        return content
    return ''.join(b.get('text', '') for b in content if b.get('type') == 'text')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--agent', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--reading', required=True)
    ap.add_argument('--run', required=True)
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--note', default='')
    a = ap.parse_args()
    path = find(a.agent)
    meta = json.load(open(path.replace('.jsonl', '.meta.json'), encoding='utf-8'))
    rows = [json.loads(l) for l in open(path, encoding='utf-8')]
    first_user, later_user, turns, texts, tool_uses, attach, versions = None, [], {}, [], 0, [], set()
    for d in rows:
        if d.get('version'):
            versions.add(d['version'])
        t = d.get('type')
        if t == 'attachment':
            att = d.get('attachment') or {}
            attach.append(att.get('type', '?'))
            continue
        m = d.get('message') or {}
        if t == 'user':
            c = m.get('content')
            if first_user is None:
                first_user = text_of(c)
                continue
            if isinstance(c, list) and all(b.get('type') == 'tool_result' for b in c):
                continue
            later_user.append(text_of(c))
        elif t == 'assistant':
            mid = m.get('id') or d.get('requestId')
            u = m.get('usage') or {}
            tr = turns.setdefault(mid, {'model': m.get('model'), 'stop_reason': None, 'output_tokens': 0})
            if m.get('stop_reason'):
                tr['stop_reason'] = m['stop_reason']
            tr['output_tokens'] = max(tr['output_tokens'], u.get('output_tokens', 0))
            for b in m.get('content') or []:
                if b.get('type') == 'text':
                    texts.append(b['text'])
                elif b.get('type') == 'tool_use':
                    tool_uses += 1
    reply = '\n\n'.join(texts)
    pbytes = open(a.prompt, 'rb').read()
    pmd5 = hashlib.md5(pbytes).hexdigest()
    tmd5 = hashlib.md5((first_user or '').encode('utf-8')).hexdigest()
    stamp = re.search(r'(Hotyn-[A-Z]|Lytin-[A-Z]) \d+\.\d+', reply)
    tl = list(turns.values())
    header = [
        '<!-- orchestrator header — written by the orchestrator, not by the sensor',
        'reading: %s' % a.reading,
        "engine (sensor's own stamp): %s" % (stamp.group(0) if stamp else 'NOT FOUND in reply'),
        'run: %s' % a.run,
        'subagent: %s · agent id %s · launched with model alias `%s`' % (meta.get('agentType'), a.agent, meta.get('model')),
        'model per turn (from the transcript): %s' % ', '.join(sorted({str(x['model']) for x in tl})),
        'harness version(s): %s' % ', '.join(sorted(versions)),
        'prompt: %s · md5 %s · md5 of the message the sensor received %s · identical: %s' % (os.path.basename(a.prompt), pmd5, tmd5, 'yes' if pmd5 == tmd5 else 'NO'),
        'turns: %d · stop reasons: %s · output tokens per turn: %s' % (len(tl), ', '.join(str(x['stop_reason']) for x in tl), ', '.join(str(x['output_tokens']) for x in tl)),
        'user-side messages after the prompt (continuations): %s' % (json.dumps(later_user, ensure_ascii=False) if later_user else 'none'),
        'tool uses: %d · harness attachments: %s' % (tool_uses, ', '.join(attach) or 'none'),
        'the reply below is verbatim: the assistant text blocks of the transcript, in order, joined by one blank line',
    ]
    if a.note:
        header.append('note: %s' % a.note)
    header.append('-->')
    with open(a.out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(header) + '\n\n' + reply + ('\n' if not reply.endswith('\n') else ''))
    rec = {'reading': a.reading, 'agent': a.agent, 'agent_type': meta.get('agentType'), 'alias': meta.get('model'),
           'turns': tl, 'continuations': later_user, 'tool_uses': tool_uses, 'prompt': os.path.basename(a.prompt),
           'prompt_md5': pmd5, 'received_md5': tmd5, 'identical': pmd5 == tmd5, 'engine': stamp.group(0) if stamp else None,
           'reply_chars': len(reply), 'harness': sorted(versions)}
    with open(os.path.join(os.path.dirname(a.out), 'turns.jsonl'), 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(json.dumps(rec, ensure_ascii=False))


if __name__ == '__main__':
    main()
