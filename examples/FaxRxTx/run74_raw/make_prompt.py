#!/usr/bin/env python3
"""Run 74 — the rules prompt of runs 72-73 with the list of lines fixed; the participant sizes the lines and nothing else.

    py -X utf8 make_prompt.py      # writes prompt_fixed_list.txt beside this file and prints its md5

The list is the one panel D (run 72) ended with after its contest: seventeen lines, every one of them carried by all
ten final tables, worded from those tables with every figure and every staffing hint removed (the PM line's
"0.8 FTE across 18 months" is gone; the scale figures that are the text's own - 8-10 formats, 16-20 nodes, 10-20 PoPs,
~30/s and ~300/s - stay, they are in the source). No number of any participant of any earlier run is in the prompt.
"""
import hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'run72_raw', 'prompt_rules.txt'), 'rb').read().decode('utf-8').replace('\r\n', '\n')

LINES = [
    ('L1', 'Domain immersion, architecture and technology selection (DHT and alternatives studied)', 'S6, A1, A3'),
    ('L2', 'Render worker host: job model, node-side execution, restart and isolation on the Windows cluster, printer-driver harness', 'S3.2, S4, A4'),
    ('L3', 'Format renderers: 8-10 input formats, each integrated and stabilised', 'S3.4, A7'),
    ('L4', 'OCR workers: TIFF to PDF conversion with digitisation on a third-party library', 'S2.3, S6, A4'),
    ('L5', 'Delivery-control core: watchdogs and tokens over an unordered store, per-fax status, resume after failure, no MQ', 'S4, A5, A6'),
    ('L6', 'Cluster management tool: queue lengths, node state, work placement over 16-20 nodes', 'S4, S5'),
    ('L7', 'Data layer: DB schema, the inter-component API the components talk through, Lustre integration for the fax archive and working files', 'S4, S6, A4'),
    ('L8', 'Rx path in the data centre: intake of TIFF from 10-20 PoPs, per-user page-by-page or PDF configuration, email assembly and delivery at volume', 'S2.2-2.4'),
    ('L9', 'Tx path: inbound-email parser, fax-number extraction, attachment handling, archive packaging and hand-off to routing / PoP', 'S3.1-3.2, S6'),
    ('L10', 'NOC internal control centre: state of the remote PoPs, the cluster and the queues', 'S4, S6'),
    ('L11', 'User portal', 'S4, S6'),
    ('L12', 'CDR and billing-data capture (billing itself out of scope)', 'S6, A1'),
    ('L13', 'Integration with the reused PoP software and least-cost routing, and coexistence with v1 through the transition', 'S6, A4'),
    ('L14', 'Integration tests on the real stream and the comparison harness against the old system', 'S6, A1, A2'),
    ('L15', 'Load-generation and failure-injection rig for the burst mode (~300/s), and the end-to-end campaign run on it across the cluster and the PoPs', 'S5, A6'),
    ('L16', 'Rollout to production traffic and readiness to decommission v1', 'A2'),
    ('L17', 'Project management and coordination (the one line on top, rule 3), with the basis you derive it from', 'S6, A3, A8'),
]

OLD_REPORT = ("Report compactly: a decomposition table that obeys the three rules below, at most about 250 words\n"
              "of reasoning outside the table, then a closing block in exactly this shape.\n")
NEW_REPORT = ("The decomposition is already made: the list of lines below is fixed. Your work is to size each line.\n"
              "Report compactly: the table of the seventeen lines with your person-months for each, at most about\n"
              "250 words of reasoning outside the table, then a closing block in exactly this shape.\n")
OLD_TABLE = "The table has three columns: line | source in the text | person-months.\n"
NEW_TABLE = (
    "THE LIST OF LINES IS FIXED. It was agreed beforehand under the three rules. Do not add, remove, merge,\n"
    "split or rename a line; if you believe work is missing or double-counted, say so in your reasoning and\n"
    "size the lines as they stand. Your estimate is secret: no other estimator will see it, and you will see\n"
    "no one else's. Give your own honest figure for every line.\n"
    "\n"
    + ''.join('  %-4s %s  [%s]\n' % (k, name, cite) for k, name, cite in LINES) +
    "\n"
    "Your table has two columns, the label exactly as above and your figure: line | person-months, seventeen\n"
    "rows L1 ... L17, no other rows. TOTAL is the arithmetic sum of the seventeen figures.\n")
assert src.count(OLD_REPORT) == 1 and src.count(OLD_TABLE) == 1
out = src.replace(OLD_REPORT, NEW_REPORT).replace(OLD_TABLE, NEW_TABLE)
open(os.path.join(HERE, 'prompt_fixed_list.txt'), 'w', encoding='utf-8', newline='\n').write(out)
print('prompt_fixed_list.txt', len(out), 'chars, md5', hashlib.md5(out.encode('utf-8')).hexdigest())
print('rules prompt md5 (LF form)', hashlib.md5(src.encode('utf-8')).hexdigest())
