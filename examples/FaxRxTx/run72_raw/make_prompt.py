#!/usr/bin/env python3
"""Runs 72-73 — the pinned prompt of run 41 with three rules added, nothing else changed.

    py -X utf8 make_prompt.py      # writes prompt_rules.txt beside this file and prints its md5

The rules fix what a line is and how lines add up; they say nothing about how large a line is.
"""
import hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'run41_raw', 'prompt_baseline_faxrxtx.txt'), 'rb').read().decode('utf-8').replace('\r\n', '\n')

OLD_REPORT = ("Report compactly: your reasoning in whatever form you find natural, then a closing block in\n"
              "exactly this shape.\n")
NEW_REPORT = ("Report compactly: a decomposition table that obeys the three rules below, at most about 250 words\n"
              "of reasoning outside the table, then a closing block in exactly this shape.\n")
OLD_FREE = "Nothing below tells you how to estimate. Choose your own approach.\n"
NEW_FREE = (
    "THE THREE RULES OF THIS ESTIMATE. They fix what a line is and how lines add up. They say nothing about\n"
    "how large a line is: that is yours to judge, by whatever approach you choose.\n"
    "\n"
    "  RULE 1 - a line includes its testing. Every line of the table is the effort of the whole blended team\n"
    "           on that block: designed, built, tested and stabilised. Add no QA line, no testing uplift and no\n"
    "           percentage of any kind on top of the lines. Work that is itself a deliverable of testing\n"
    "           (for example a comparison harness the text asks for) is a line like any other.\n"
    "  RULE 2 - a line is a thing built or a piece of work done, and it cites the text. Give each line the\n"
    "           place it comes from: a section of the system description (for example S2, S4, S6) or an\n"
    "           assumption (A1 ... A9). A line with nothing to cite is not admissible. There are no lines for\n"
    "           risk, novelty, friction, glue, omissions, discounts, rounding or anything else that is not\n"
    "           itself work: whatever you believe about those goes into RANGE, never into TOTAL.\n"
    "  RULE 3 - one line on top. Project management and coordination may be one line, in person-months, with\n"
    "           the basis you derive it from. TOTAL is the arithmetic sum of the lines, not rounded by more\n"
    "           than one person-month.\n"
    "\n"
    "The table has three columns: line | source in the text | person-months.\n")
assert src.count(OLD_REPORT) == 1 and src.count(OLD_FREE) == 1
out = src.replace(OLD_REPORT, NEW_REPORT).replace(OLD_FREE, NEW_FREE)
open(os.path.join(HERE, 'prompt_rules.txt'), 'w', encoding='utf-8', newline='\n').write(out)
print('prompt_rules.txt', len(out), 'chars, md5', hashlib.md5(out.encode('utf-8')).hexdigest())
print('base prompt md5 (LF form)', hashlib.md5(src.encode('utf-8')).hexdigest())
