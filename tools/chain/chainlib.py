"""Shared readers for the chain tools: the 2.x product model (fenced TSV in section 6 of a Hotyn-M reply), the
technology catalogue (activity tables per declared entry), the case's chain configuration, the rate table.

Nothing here judges anything. Every function reads a pinned file and returns what it says.
"""
import json
import os
import re
from collections import OrderedDict

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
REQ_ID = re.compile(r'\b(?:[A-Z]{1,3}|NFR)-\d+(?:\.\d+)?\b|\b[A-Z]\d{2,3}\b')   # SAS-style I-2 / NFR-14, FaxRxTx-style F01


# ---------------------------------------------------------------- the product model (Hotyn-M 2.x)
class Model:
    """id -> row(parent, origin, coverage, name); order; kids; leaves; root."""

    def __init__(self, path):
        txt = open(path, encoding='utf-8').read()
        sec6 = txt[txt.index('\n## 6. '):txt.index('\n## 7. ')]
        blk = sec6[sec6.index('```tsv') + 6:sec6.rindex('```')]
        lines = [l for l in blk.strip('\n').split('\n') if l.strip()]
        hdr = lines[0].split('\t')
        assert hdr == ['id', 'parent', 'origin', 'coverage', 'name'], hdr
        self.rows, self.order = OrderedDict(), []
        for l in lines[1:]:
            c = l.split('\t')
            self.rows[c[0]] = dict(parent=c[1], origin=c[2], coverage=c[3].strip(), name=c[4])
            self.order.append(c[0])
        self.kids = OrderedDict()
        for k, r in self.rows.items():
            if r['parent'] in self.rows:
                self.kids.setdefault(r['parent'], []).append(k)
        roots = [k for k, r in self.rows.items() if r['parent'] not in self.rows]
        assert len(roots) == 1, roots
        self.root = roots[0]
        self.path = path
        m = re.search(r'reading: (\S+)', txt[:3000])
        self.id = m.group(1) if m else os.path.splitext(os.path.basename(path))[0]
        m = re.search(r"engine \(sensor's own stamp\): (Hotyn-M \d\.\d)", txt[:3000]) or re.search(r'Hotyn-M \d\.\d', txt)
        self.engine = m.group(1) if m and m.groups() else (m.group(0) if m else 'Hotyn-M')

    def subtree(self, k):
        out = [k]
        for c in self.kids.get(k, []):
            out += self.subtree(c)
        return out

    def is_leaf(self, k):
        return k not in self.kids

    def leaves(self):
        return [k for k in self.order if self.is_leaf(k)]

    def parents(self):
        return [k for k in self.order if not self.is_leaf(k)]

    def coverage_ids(self, k):
        cov = self.rows[k]['coverage']
        if cov.lower().startswith('trigger'):
            return []
        return [x for x in re.split(r'[,\s]+', cov) if x]

    def depth(self, k):
        d = 0
        while self.rows[k]['parent'] in self.rows:
            k = self.rows[k]['parent']
            d += 1
        return d

    def auto_batches(self, target=36):
        """Group the root's children, in model order, into batches of at most `target` elements; a single
        subtree larger than the target is a batch of its own. Letters A, B, C …"""
        batches, cur, n = OrderedDict(), [], 0
        letters = iter('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for top in self.kids[self.root]:
            size = len(self.subtree(top))
            if cur and n + size > target:
                batches[next(letters)] = cur
                cur, n = [], 0
            cur.append(top)
            n += size
        if cur:
            batches[next(letters)] = cur
        return batches


# ---------------------------------------------------------------- the case configuration
def load_config(case):
    """examples/<case>/chain_config.json — the declared technology codes and the declaration's parameters."""
    p = os.path.join(case, 'chain_config.json')
    cfg = json.load(open(p, encoding='utf-8'))
    cfg.setdefault('parameters', {})
    cfg['parameters'].setdefault('test_cycles', 1)
    cfg['parameters'].setdefault('uat_cycles', 0)
    cfg['parameters'].setdefault('migration_rehearsal_cycles', 0)
    cfg['parameters'].setdefault('environments', [])
    return cfg


# ---------------------------------------------------------------- the technology catalogue
def catalogue_text():
    return open(os.path.join(REPO, 'docs', 'technology_catalogue.md'), encoding='utf-8').read()


def catalogue_version():
    m = re.search(r'\*\*Version (\d\.\d)', catalogue_text())      # the change log lists the newest first
    return m.group(1) if m else '1.x'


def entry_table(code):
    """(heading title, dimension title, rows) for a declared code: the activity table under '### `CODE` — …'.
    Rows are dicts id, activity, scope, applies, note. Notes are kept verbatim except case-alien absorption
    marks, which are stripped; a code with no table (SA-NONE, U-NONE) returns an empty list."""
    txt = catalogue_text()
    m = re.search(r'^### `%s`[^\n]*$' % re.escape(code), txt, re.M)
    if not m:
        raise KeyError('catalogue has no entry `%s`' % code)
    title = re.sub(r'\s*\*\(.*?\)\*\s*$', '', m.group(0)[4:]).strip()
    dim = re.findall(r'^## \d+\. Dimension \d+ — (.+)$', txt[:m.start()], re.M)[-1].strip()
    rest = txt[m.end():]
    m2 = re.search(r'^##+ ', rest, re.M)
    body = rest[:m2.start()] if m2 else rest
    rows = []
    for line in body.split('\n'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 3 or c[0] == 'id' or set(c[0]) <= set('-'):
            continue
        note = c[4] if len(c) > 4 else ''
        note = re.sub(r'\*\*absorbs demanded work [^*]*\*\*', '', note).strip(' ;')
        applies = c[3] if len(c) > 3 else ''
        note, applies = (re.sub(r'\s*\*\((?:condition added in [\d.]+)\)\*', '', x).strip() for x in (note, applies))
        rows.append(dict(id=c[0], activity=c[1], scope=c[2], applies=applies, note=note))
    return title, dim, rows


def declared_activities(cfg):
    """All activity rows of the declared codes, in catalogue order, with the dimension and entry they come from."""
    out = []
    for code in cfg['declared']:
        title, dim, rows = entry_table(code)
        for r in rows:
            r = dict(r)
            r['code'], r['dimension'], r['entry'] = code, dim, title
            out.append(r)
    return out


def scope_kind(scope):
    """once | per_element | per_parent | per_environment, and whether × cycles."""
    s = scope.lower()
    cycles = '×' in s or 'x cycles' in s or 'cycles' in s
    if s.startswith('once'):
        return 'once', cycles
    if 'per environment' in s:
        return 'per_environment', cycles
    if 'per parent' in s or 'per aggregate' in s:
        return 'per_parent', cycles
    if 'per element' in s:
        return 'per_element', cycles
    if s.startswith('×') or s.startswith('x '):
        return 'once', True
    return s, cycles


def declaration_input(cfg):
    """INPUT 2 of the crossing prompt: the declared entries' activity tables verbatim from the catalogue, the scope
    legend, the parameters. No pricing vocabulary: the catalogue's prose notes are not carried, only its tables."""
    ver = catalogue_version()
    out = ['# INPUT 2 — the technology declaration (%s), as the crossing must see it' % cfg.get('case_label', 'this case'), '',
           'One entry per dimension of catalogue %s. **The activity list is the declaration\'s, not yours**: an' % ver,
           'activity absent here does not exist for this run. Scopes: `once` = one item for the whole model ·',
           '`per element` = one per element of the applicable classes · `per parent` = one per element that has',
           'children (a position, not a class) · `per environment` = one per environment named in the parameters',
           '· `× cycles` = multiplied by the cycle count named in the parameters.', '']
    for code in cfg['declared']:
        title, dim, rows = entry_table(code)
        out.append('## %s — %s' % (dim.capitalize(), title))
        if not rows:
            out.append('')
            out.append('No activities: this dimension is declared as none.')
            out.append('')
            continue
        out.append('| id | activity | scope | applies to | note |')
        out.append('|---|---|---|---|---|')
        for r in rows:
            out.append('| %s | %s | %s | %s | %s |' % (r['id'], r['activity'], r['scope'], r['applies'], r['note']))
        if code.startswith('K-'):
            out.append('')
            out.append('No assembly or integration activity, deliberately: integration is accounted for downstream at every aggregation node, and an activity here would be the same work twice.')
        out.append('')
    P = cfg['parameters']
    out.append('## Parameters')
    out.append('| parameter | value |')
    out.append('|---|---|')
    if P['environments']:
        out.append('| environments | %d: %s |' % (len(P['environments']), ', '.join(P['environments'])))
    out.append('| test execution cycles | %s |' % P['test_cycles'])
    if P['uat_cycles']:
        out.append('| UAT cycles | %s |' % P['uat_cycles'])
    if P['migration_rehearsal_cycles']:
        out.append('| migration rehearsal cycles | %s |' % P['migration_rehearsal_cycles'])
    return '\n'.join(out) + '\n'


def demanded_input(case):
    """INPUT 3 of the crossing prompt: the demanded-work list with the absorption the declaration records.
    Obligation texts from requirements_work.md; absorption from the W6 table of technology_declaration.md."""
    work = []
    for line in open(os.path.join(case, 'requirements_work.md'), encoding='utf-8'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) >= 2 and c[0] != 'id' and not set(c[0]) <= set('-'):
            work.append((c[0], c[1]))
    absorb = {}
    txt = open(os.path.join(case, 'technology_declaration.md'), encoding='utf-8').read()
    m = re.search(r'^## .*(W6|demanded).*$', txt, re.M | re.I)
    if m:
        body = txt[m.end():]
        m2 = re.search(r'^## ', body, re.M)
        body = body[:m2.start()] if m2 else body
        for line in body.split('\n'):
            if not line.startswith('| '):
                continue
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(c) >= 4 and c[0] != 'id' and not set(c[0]) <= set('-'):
                absorb[c[0]] = '%s — %s' % (c[3], c[2]) if c[2] not in ('—', '-', '') else c[3]
    out = ['# INPUT 3 — the demanded-work list (`requirements_work.md`, N = %d), with the absorption the declaration records' % len(work), '',
           '| id | obligation | declaration\'s absorption |', '|---|---|---|']
    for i, t in work:
        out.append('| %s | %s | %s |' % (i, t, absorb.get(i, 'not stated by the declaration')))
    out += ['', 'The absorptions are the declaration\'s claims; W6 asks you to record each demanded id **once** — at the absorbing item where one exists in your scope, otherwise as *accounted for at* an activity that is once-scoped and therefore deferred from this partial run, or as its own branch if you find no declared activity absorbs it. Say which.']
    return '\n'.join(out) + '\n', [i for i, _ in work]


# ---------------------------------------------------------------- the rate table
def load_rates():
    """(activity, classkey, size) -> (O, M, P); first occurrence wins where the table repeats an activity."""
    RATES = {}
    for line in open(os.path.join(REPO, 'docs', 'rate_table.md'), encoding='utf-8'):
        if not line.startswith('| '):
            continue
        c = [x.strip() for x in line.strip().strip('|').split('|')]
        if len(c) < 6 or not re.fullmatch(r'[A-Z]\d{1,2}[a-z]?d?', c[0]):
            continue
        try:
            cell = (float(c[3]), float(c[4]), float(c[5]))
        except ValueError:
            continue
        act, cls, sz = c[0], c[1], c[2]
        m = re.match(r'(?:\w+ = )?(S|M|L|XL)\b', sz)
        size = m.group(1) if m else sz
        if act == 'E1' and '=' in sz:
            size = sz.split('=')[1].strip()
        RATES.setdefault((act, cls, size), cell)
        RATES.setdefault((act, '*', size), cell)
    return RATES


def make_rate_lookup(RATES):
    K1CLS = {'interface': 'interface'}
    K2CLS = {'interface': 'interface', 'store': 'store'}

    def rate(act, size, cls='*'):
        return RATES.get((act, cls, size)) or RATES.get((act, '*', size))

    def cell_for(act, elcls, size, kind=None):
        if act == 'K1':
            return rate('K1', size, K1CLS.get(elcls, 'behaviour, surface, store'))
        if act == 'K2':
            return rate('K2', size, K2CLS.get(elcls, 'behaviour, surface'))
        if act == 'K3':
            return rate('K3', size, 'statement-' + (kind or 'compliance'))
        return rate(act, size)
    return rate, cell_for


def E(cell):
    o, m, p = cell
    return (o + 4 * m + p) / 6.0


def band(n, cuts):
    """cuts = (S_max, M_max, L_max); above L_max is XL."""
    return 'S' if n <= cuts[0] else 'M' if n <= cuts[1] else 'L' if n <= cuts[2] else 'XL'


def md_section(t, n):
    """Text of the numbered markdown section 'n.' ('## n. …' or '### n. …') up to the next numbered section
    heading. Sub-headings inside the section (e.g. '### Subtree N06') do not end it."""
    m = re.search(r'^#{1,3} *%s\. .*$' % re.escape(str(n)), t, re.M)
    if not m:
        return ''
    rest = t[m.end():]
    m2 = re.search(r'^#{1,3} *\d+[a-z]?\. ', rest, re.M)
    return rest[:m2.start()] if m2 else rest
