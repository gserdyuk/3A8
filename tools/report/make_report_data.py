#!/usr/bin/env python3
"""
Assemble a case's report_data.json from two small files the orchestrator writes at the end of a run,
plus the case's own pinned files.

    python tools/report/make_report_data.py examples/<case>

Reads, in examples/<case>/:
  report_numbers.json   every number on the chart and in the tiles, in net task hours, each with the run it
                        came from (schema: tools/report/REPORT_INPUTS.md)
  report_text.json      the prose slots: standfirst, subject, the divergence rows, findings, gaps, footer
  requirements_product.md, requirements_work.md   -> the obligations table (id | obligation | source)
  open_questions.md     (optional) -> the variant-readings table
  assumptions.md        -> the defaults list (one row per "## A<n>. <title>" section, first paragraph)
  run<N>_raw/curves_pd.json (optional, named in the numbers file) -> the no-method family

Writes examples/<case>/report_data.json and prints where. Then:

    python tools/report/build_report.py examples/<case>/report_data.json

Nothing about a particular case lives in this file. The numbers are the sensors' and the assembly's; the prose is
the orchestrator's; the tables are the case files'. This script only converts hours to person-days, lays the
pieces into the report's slots and refuses to invent a figure that is not in report_numbers.json.
"""
import json, os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    """HTML-escape a plain string; strings that already carry entities or tags are passed through by the caller."""
    return html.escape(str(s), quote=False)


def md_table_rows(path):
    """Rows of the first markdown table in a file whose header starts with 'id'. Returns list of cell lists."""
    if not os.path.exists(path):
        return []
    rows, in_table, header = [], False, None
    for line in open(path, encoding='utf-8'):
        if not line.startswith('|'):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if header is None:
            if cells and cells[0].lower() == 'id':
                header = cells
                in_table = True
            continue
        if set(''.join(cells)) <= set('-: '):
            continue
        if in_table and len(cells) >= 2:
            rows.append(cells)
    return rows


def md_inline(s):
    """Minimal markdown inline -> HTML: **bold**, *italic*, `code`."""
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s


def obligations_html(case):
    prod = md_table_rows(os.path.join(case, 'requirements_product.md'))
    work = md_table_rows(os.path.join(case, 'requirements_work.md'))
    out = ['<div class="tbl-scroll tbl-tall"><table><thead><tr><th>id</th><th>obligation</th><th>kind</th></tr></thead><tbody>']
    for kind, rows in (('product', prod), ('work', work)):
        for c in rows:
            out.append('<tr><td class="tag">%s</td><td>%s</td><td class="q">%s</td></tr>' % (esc(c[0]), md_inline(c[1]), kind))
    out.append('</tbody></table></div>')
    return '\n'.join(out), len(prod), len(work)


def questions_html(case):
    """open_questions.md: a table whose header starts with 'id' or '#'; columns id | ids | question | reading."""
    p = os.path.join(case, 'open_questions.md')
    if not os.path.exists(p):
        return None, 0
    rows, header = [], None
    for line in open(p, encoding='utf-8'):
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if header is None:
            if cells and cells[0].lower() in ('id', '#', 'q', 'question'):
                header = cells
            continue
        if set(''.join(cells)) <= set('-: '):
            continue
        rows.append(cells)
    if not rows:
        return None, 0
    ncol = max(len(r) for r in rows)
    out = ['<div class="tbl-scroll"><table><thead><tr><th>#</th><th>ids</th><th>the question</th><th>reading taken</th></tr></thead><tbody>']
    for c in rows:
        c = c + [''] * (4 - len(c))
        if ncol == 3:   # id | question | reading
            c = [c[0], '', c[1], c[2]]
        out.append('<tr><td class="tag">%s</td><td class="tag">%s</td><td>%s</td><td class="q">%s</td></tr>'
                   % (esc(c[0]), esc(c[1]), md_inline(c[2]), md_inline(c[3])))
    out.append('</tbody></table></div>')
    return '\n'.join(out), len(rows)


def defaults_html(case):
    """assumptions.md: one row per '## A<n>. <title>' section, the first paragraph as the text."""
    p = os.path.join(case, 'assumptions.md')
    if not os.path.exists(p):
        return None, 0
    txt = open(p, encoding='utf-8').read()
    secs = re.split(r'^## +', txt, flags=re.M)[1:]
    rows = []
    for s in secs:
        head, _, body = s.partition('\n')
        m = re.match(r'(A\d+[a-z]?)\.?\s+(.*)', head.strip())
        if not m:
            continue
        paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
        first = re.sub(r'\s+', ' ', paras[0]) if paras else ''
        if len(first) > 600:
            first = first[:597].rsplit(' ', 1)[0] + '…'
        rows.append('<div class="row"><span class="idx">%s</span><div class="body"><div class="t">%s</div><div class="x">%s</div></div></div>'
                    % (esc(m.group(1)), md_inline(m.group(2)), md_inline(first)))
    if not rows:
        return None, 0
    return '<div class="stack">\n' + '\n'.join(rows) + '\n</div>', len(rows)


def rows_html(rows):
    """Generic stack of rows from report_text: [{idx, title, chip, chip_cls, text}]."""
    out = ['<div class="stack">']
    for r in rows:
        chip = ''
        if r.get('chip'):
            chip = ' <span class="chip %s">%s</span>' % (r.get('chip_cls', ''), r['chip'])
        out.append('  <div class="row"><span class="idx">%s</span><div class="body">\n    <div class="t">%s%s</div>\n    <div class="x">%s</div>\n  </div></div>'
                   % (r.get('idx', ''), r['title'], chip, r['text']))
    out.append('</div>')
    return '\n'.join(out)


def fmt(n):
    """Thin-space thousands, as the reports print numbers."""
    return format(int(round(n)), ',').replace(',', ' ')


def main():
    if len(sys.argv) < 2:
        sys.exit('usage: make_report_data.py examples/<case>')
    case = sys.argv[1].rstrip('/\\')
    N = json.load(open(os.path.join(case, 'report_numbers.json'), encoding='utf-8'))
    T = json.load(open(os.path.join(case, 'report_text.json'), encoding='utf-8'))
    H = float(N.get('hours_per_pd', 8))
    pd = lambda h: round(float(h) / H)

    chain, cal = N['chain'], N.get('calibration')
    counts, eng = N.get('counts', {}), N.get('engines', {})

    # ---------------------------------------------------------------- chart
    if cal:
        centre_h = (cal['centre_lo_h'] + cal['centre_hi_h']) / 2
        sd_h = chain['sd_rho05_h'] * (centre_h / chain['raw_centre_h'])
    else:
        centre_h, sd_h = chain['raw_centre_h'], chain['sd_rho05_h']
    chart = {
        'axisMax': N.get('axis_max_pd') or int(round(max(pd(centre_h + 3.6 * sd_h), *[pd(q) for o in N.get('outside', []) for q in o['quantiles_h'].values()], pd(N['fact']['value_h']) if N.get('fact') else 0) * 1.08 / 600.0 + 1) * 600),
        'rawSum': pd(chain['raw_centre_h']) if cal else None,
        'rawSumLabel': ('raw table sum %d' % pd(chain['raw_centre_h'])) + ((' (band %d–%d)' % (pd(chain['raw_lo_h']), pd(chain['raw_hi_h']))) if chain.get('raw_lo_h') else '') if cal else '',
        'calibration': {'lo': pd(cal['corridor_lo_h']), 'hi': pd(cal['corridor_hi_h']),
                        'label': 'calibration spread %d–%d · not percentiles' % (pd(cal['corridor_lo_h']), pd(cal['corridor_hi_h']))} if cal else None,
        'bottomUp': {'mu': pd(centre_h), 'sd': pd(sd_h)},
        'outside': [],
        'axisLabel': 'NET WORKING TIME — PERSON-DAYS OF %d TASK HOURS' % int(H),
        'legend': [],
        'hint': T.get('hint') or '',
    }
    for o in N.get('outside', []):
        q = sorted((float(k), pd(v)) for k, v in o['quantiles_h'].items())
        p50 = dict(q).get(0.5)
        entry = {'id': o['id'], 'dash': o.get('dash', ''), 'q': [[v, k] for k, v in q], 'tailDrawn': bool(o.get('tail_drawn', False))}
        if o.get('lognormal'):
            entry['lognormal'] = {'median': pd(o['lognormal']['median_h']), 'sigma': o['lognormal']['sigma']}
        else:
            p10 = dict(q).get(0.1)
            if p10 and p50:
                entry['floor'] = round(p10 * p10 / p50)
        if o.get('beyond_label'):
            entry['beyondLabel'] = o['beyond_label']
        chart['outside'].append(entry)
        chart['legend'].append({'cls': 'blue' + (' dash' if o.get('dash') else ''),
                                'text': 'Outside view %s &mdash; P50 %d%s' % (o['id'], p50 or 0, (' (%s)' % o['unit_note']) if o.get('unit_note') else '')})
    chart['legend'].append({'cls': 'red', 'text': ('Bottom-up, calibrated &mdash; P50 %d' if cal else 'Bottom-up, table-priced &mdash; P50 %d, &rho; = 0.5') % pd(centre_h)
                            + ((' (%s)' % T['chain_legend_note']) if T.get('chain_legend_note') else '')})
    if N.get('bottom_up_alt'):
        chart['bottomUpAlt'] = [{'id': a['id'], 'mu': pd(a['centre_h']), 'sd': pd(a['sd_h']), 'dash': a.get('dash', '6 4')} for a in N['bottom_up_alt']]
        for a in N['bottom_up_alt']:
            chart['legend'].append({'cls': 'red dash', 'text': '%s &mdash; P50 %d' % (a['id'], pd(a['centre_h']))})
    if N.get('raw_marks'):
        chart['rawMarks'] = [{'x': pd(m['value_h']), 'label': m['label'], **({'lo': pd(m['lo_h']), 'hi': pd(m['hi_h'])} if m.get('lo_h') else {})} for m in N['raw_marks']]
    if N.get('parametric'):
        chart['parametric'] = [{'id': p['id'], 'median': pd(p['median_h']) if p.get('median_h') else p['median_pd'], 'sigma': p['sigma'], 'dash': p.get('dash', '6 3')} for p in N['parametric']]
        chart['legend'].append({'cls': 'teal dash', 'text': T.get('parametric_legend') or 'Parametric &mdash; ' + ', '.join(p['id'] for p in N['parametric'])})
    if N.get('nomethod_curves_file'):
        nm = json.load(open(os.path.join(case, N['nomethod_curves_file']), encoding='utf-8'))
        chart['nomethod'] = nm if isinstance(nm, list) else [{'id': k, **v} for k, v in nm.items()]   # list, or {id: {median, sigma}}
        meds = sorted(c['median'] for c in chart['nomethod'])
        chart['legend'].append({'cls': 'ochre', 'text': T.get('nomethod_legend') or 'No method &mdash; %d bare runs, one thin curve each, medians %s&ndash;%s' % (len(meds), fmt(meds[0]), fmt(meds[-1]))})
    if N.get('fact'):
        chart['fact'] = {'value': pd(N['fact']['value_h']), 'label': N['fact'].get('label') or ('the outcome &mdash; %d' % pd(N['fact']['value_h']))}
        chart['legend'].append({'cls': 'fact', 'text': N['fact'].get('legend') or 'The documented outcome &mdash; %d' % pd(N['fact']['value_h'])})

    # ---------------------------------------------------------------- tiles (generated unless the text file supplies them)
    tiles = T.get('tiles')
    if not tiles:
        tiles = [{'cls': 'red', 'k': 'Centre', 'v': '%d' % pd(centre_h), 'unit': 'pd',
                  'd': T.get('centre_note') or ('%s net task hours%s' % (fmt(centre_h), ((' &mdash; the table-priced assembly %s &times; the gap-blind Step C chain, <b>&times;%.2f</b>' % (fmt(chain['raw_centre_h']), cal['factor_central'])) if cal else ' &mdash; the table-priced assembly, uncalibrated')))},
                 {'cls': 'red', 'k': 'Corridor &middot; P10&ndash;P90', 'v': '%d&ndash;%d' % (pd(centre_h - 1.2816 * sd_h), pd(centre_h + 1.2816 * sd_h)), 'unit': 'pd',
                  'd': 'The drawn band. From the O/M/P in every rate cell, under a declared item correlation of <b>&rho; = 0.5</b>%s. A convention, not a measurement.' % (', scaled by the calibration' if cal else '')}]
        if cal:
            tiles.append({'cls': '', 'k': 'Calibration spread', 'v': '%d&ndash;%d' % (pd(cal['corridor_lo_h']), pd(cal['corridor_hi_h'])), 'unit': 'pd',
                          'd': T.get('calibration_note') or 'A different quantity, and <b>not percentiles</b>: the centre at the low and high ends of the Step C rates. %s &ndash; %s net task hours.' % (fmt(cal['corridor_lo_h']), fmt(cal['corridor_hi_h']))})
        if N.get('fact'):
            tiles.append({'cls': 'none', 'k': 'The outcome', 'v': '%d' % pd(N['fact']['value_h']), 'unit': 'pd', 'd': N['fact'].get('note', '')})
            tiles.append({'cls': 'red', 'k': 'Against the outcome', 'v': '&times;%.2f' % (N['fact']['value_h'] / centre_h), 'unit': '', 'd': T.get('against_outcome_note', 'outcome / centre')})
        if counts.get('repeat_spread'):
            tiles.append({'cls': '', 'k': 'Repeat spread', 'v': '&times;%.3f' % counts['repeat_spread'], 'unit': '',
                          'd': T.get('repeat_note') or ('Two independent size classifications%s, priced from the same table.' % ((', %s%% class agreement' % counts['class_agreement_pct']) if counts.get('class_agreement_pct') else ''))})
        if chart.get('nomethod'):
            meds = sorted(c['median'] for c in chart['nomethod'])
            tiles.append({'cls': 'ochre', 'k': 'No method &middot; %d runs' % len(meds), 'v': '%s&ndash;%s' % (fmt(meds[0]), fmt(meds[-1])), 'unit': 'pd', 'd': T.get('nomethod_note', '')})
        if chart['outside']:
            tiles.append({'cls': 'blue', 'k': 'Outside view &middot; P50', 'v': ' &middot; '.join(str(dict((k, v) for v, k in o['q']).get(0.5, '')) for o in chart['outside']), 'unit': 'pd', 'd': T.get('outside_note', '')})
        if T.get('reserve_note'):
            tiles.append({'cls': 'none', 'k': 'Reserve', 'v': T.get('reserve_value', 'Unresolved'), 'unit': '', 'd': T['reserve_note']})
        if T.get('extra_tiles'):
            tiles += T['extra_tiles']

    # ---------------------------------------------------------------- sections
    obl_html, n_prod, n_work = obligations_html(case)
    q_html, n_q = questions_html(case)
    d_html, n_d = defaults_html(case)
    how = T.get('how_to_read') or open(os.path.join(HERE, 'fragments', 'how_to_read.html'), encoding='utf-8').read()
    method = open(os.path.join(HERE, 'fragments', 'methodology.html'), encoding='utf-8').read()

    prov_rows = []
    for i, r in enumerate(N.get('provenance', []) or []):
        prov_rows.append({'idx': r.get('idx', str(i + 1)), 'title': r['title'], 'chip': r.get('chip'), 'chip_cls': r.get('chip_cls', 'caution'), 'text': r['text']})
    prov_html = rows_html(prov_rows) if prov_rows else ''
    prov_html += ('\n<h4>Two coordinates, not one</h4>\n<p>An estimate is a property of the triple <b>(project &times; engine &times; model)</b>. %s</p>'
                  % (eng.get('model_note') or ('Every sensor on this case ran on %s, so the model coordinate is held fixed.' % eng.get('model', 'one model'))))
    if T.get('provenance_extra'):
        prov_html += '\n' + T['provenance_extra']

    sections = [
        {'id': 'how-to-read', 'title': 'How to read the chart', 'count': 'the method', 'lead': 'Both instruments produce a distribution. Only one of them did so without being asked.', 'html': how, 'src': 'docs/constants.md &middot; docs/instrument.md &middot; docs/sensors/'},
    ]
    if T.get('divergence'):
        dv = T['divergence']
        body = rows_html(dv.get('rows', []))
        if dv.get('stepc_bullets'):
            body += '\n<h4>What Step C adds, and why the rates came out as they did</h4>\n<ul>\n' + '\n'.join('<li>%s</li>' % b for b in dv['stepc_bullets']) + '\n</ul>'
        if dv.get('false_convergence'):
            body += '\n<h4>False convergence, checked</h4>\n<p>%s</p>' % dv['false_convergence']
        sections.append({'id': 'divergence', 'title': dv.get('title', 'Why the methods disagree'), 'count': dv.get('count', ''), 'lead': dv.get('lead', ''), 'html': body, 'src': dv.get('src', '')})
    if T.get('outcome'):
        oc = T['outcome']
        sections.append({'id': 'outcome', 'title': oc.get('title', 'Against the outcome'), 'count': oc.get('count', ''), 'lead': oc.get('lead', ''), 'html': rows_html(oc.get('rows', [])) + ('\n' + oc['extra'] if oc.get('extra') else ''), 'src': oc.get('src', '')})
    sections.append({'id': 'obligations', 'title': 'Obligations', 'count': str(n_prod + n_work), 'lead': 'One entry per obligation <b>as the document words it</b>, under the document\'s own ids. Ids never change, so every artefact downstream still means what it meant. <b>No run may add, remove, split or merge an entry.</b>', 'html': obl_html, 'src': 'requirements_product.md &middot; requirements_work.md'})
    if T.get('findings'):
        f = T['findings']
        sections.append({'id': 'findings', 'title': 'Findings', 'count': str(len(f.get('rows', []))), 'lead': f.get('lead', 'Produced without being asked for, by instruments whose job was something else.'), 'html': rows_html(f.get('rows', [])), 'src': f.get('src', '')})
    if q_html:
        sections.append({'id': 'two-ways', 'title': 'Variant readings', 'count': '%d' % n_q, 'lead': T.get('questions_lead', 'Pinned before any run and consumed by every run. <b>Ask the client; if no answer comes, assume; declare the assumption; and when runs are compared afterwards, exclude the differences the open question causes.</b>'), 'html': q_html, 'src': 'open_questions.md'})
    if d_html:
        sections.append({'id': 'defaults', 'title': 'Defaults', 'count': '%d' % n_d, 'lead': T.get('defaults_lead', 'Each is a fork the document leaves open and the estimate had to close. <b>The reading taken is inside the centre; the reading refused is not.</b> One row per entry of the assumption log, its first paragraph.'), 'html': d_html, 'src': 'assumptions.md &middot; technology_declaration.md'})
    if T.get('gaps'):
        g = T['gaps']
        sections.append({'id': 'not-in-number', 'title': 'Estimate gaps', 'count': str(len(g.get('rows', []))), 'lead': g.get('lead', 'Not oversights. Each is a thing the chain refused to price, with the reason it refused.'), 'html': rows_html(g.get('rows', [])), 'src': g.get('src', '')})
    sections.append({'id': 'provenance', 'title': 'Where every number came from', 'count': '%d roles' % len(prov_rows) if prov_rows else 'the sensors', 'lead': 'Each sensor is an engine with a version, stamped on its own output. They are hired for what they are <b>forbidden to see</b>, not for autonomy.', 'html': prov_html, 'src': 'PIPELINE.md &middot; docs/instrument.md'})
    sections.append({'id': 'methodology', 'title': 'Methodology', 'count': 'the documents', 'lead': 'This report is one output of a method that is written down. Nothing below is specific to this case; every file states what it is for, what it may not do, and what would change it.', 'html': method, 'src': 'the report format: tools/report/build_report.py'})

    meta = T.get('meta') or [
        '<b>%d</b> obligations &mdash; %d product, %d work' % (n_prod + n_work, n_prod, n_work),
        '<b>%s</b> model elements &middot; <b>%s</b> work items' % (fmt(counts.get('elements', 0)), fmt(counts.get('items', 0))),
        N.get('dates_line', ''),
        'unit <b>1 pd = %d net task hours</b> &mdash; leave, holidays and sickness not included' % int(H),
    ]
    data = {
        'title': T.get('title', 'Project estimate'),
        'eyebrow': T.get('eyebrow', '3A8 &middot; TriAngulEight'),
        'headline': T.get('headline', 'Project estimate'),
        'subject': T['subject'],
        'standfirst': T['standfirst'],
        'meta': [m for m in meta if m],
        'chart': chart,
        'tiles': tiles,
        'sections': sections,
        'footer': {'brand': '3A8', 'brandsub': 'TriAngulEight<br>an estimation instrument',
                   'fine': T.get('footer_fine') or [
                       '<b>What this report is not.</b> Not a validated price, and not a price at all &mdash; it is work content in net task hours, shown as person-days of %d such hours. Converting it into money, calendar or headcount is the reader\'s act, using the reader\'s own figures. Every bottom-up number rests on a rate table of external industry norms calibrated against no outcome.' % int(H),
                       '<b>What it is.</b> The estimate, its corridor, the disagreement between two structurally independent methods stated rather than averaged away, and, on the record, the obligations, the findings, the questions and the defaults that the number is standing on.']},
    }
    out = os.path.join(case, 'report_data.json')
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print('written', out, '| centre', pd(centre_h), 'pd, sd', pd(sd_h), '| obligations', n_prod + n_work, '| questions', n_q, '| defaults', n_d, '| sections', len(sections))


if __name__ == '__main__':
    main()
