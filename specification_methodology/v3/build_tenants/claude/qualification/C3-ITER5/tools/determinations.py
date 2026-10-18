"""Build qualification/C3-ITER5/determinations/DETERMINATIONS.json (I5-04, port D1 adapted from the
Codex iteration 5 record at 28d87ee): one record per determination this candidate owns, with its
owner locus and digest, the rule sentence, the premises it rests on, the pillars, the consumers the
owning member's consumers paragraph names (each resolved to a locus), and, for the a_c clauses, the
clause id. Sources: every Foundation to law family table (its rows) and consumers paragraph, and
a_c/i3/axiomatic-program.json. The record is a derived index: it decides nothing and is regenerated
from the members. Run from the tenant root with python3 -I.
"""
import glob, hashlib, json, os, re
def slug(h): return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
def sections(path):
    out, seen, cur, buf, code, lines = {}, {}, None, [], False, {}
    for n, line in enumerate(open(path, encoding='utf-8'), 1):
        if line.startswith('```'): code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if cur is not None: out[cur] = ''.join(buf); lines[cur] = (lines[cur][0], n - 1)
            s = slug(m.group(2)); k = seen.get(s, 0); seen[s] = k + 1
            cur = s if k == 0 else f'{s}-{k}'; buf = []; lines[cur] = (n, None)
        else: buf.append(line)
    if cur is not None: out[cur] = ''.join(buf); lines[cur] = (lines[cur][0], n)
    return out, lines
members = {os.path.basename(f): sections(f) for f in glob.glob('standards/*.md')}
def digest(member, anchor):
    secs, _ = members[member]; return hashlib.sha256(secs[anchor].encode('utf-8')).hexdigest() if anchor in secs else None
LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
records, families = [], []
for member, (secs, lines) in sorted(members.items()):
    text = open('standards/' + member, encoding='utf-8').read().split('\n')
    # locate each family table: header row, its rows, the section anchor it sits in, and its consumers paragraph
    i = 0
    while i < len(text):
        if text[i].startswith('| Premises, with standing |'):
            # the heading above
            h = next(j for j in range(i, -1, -1) if re.match(r'^#{1,6}\s', text[j]))
            fam_anchor = [a for a, (s, e) in lines.items() if s == h + 1][0]
            rows = []; j = i + 2
            while j < len(text) and text[j].startswith('| '):
                cells = [c.strip() for c in text[j].strip().strip('|').split(' | ')]
                if len(cells) >= 5: rows.append((j + 1, cells))
                j += 1
            if not rows:  # a header shown as a format statement, not a family table (FOUNDATIONS §3 Foundation to law)
                i = j; continue
            # the consumers paragraph after the table
            k = j; items = {}
            while k < len(text) and not text[k].startswith('Consumers of these rows'): k += 1
            if k < len(text):
                k += 1
                while k < len(text) and not text[k].startswith('Each consumer applies'):
                    m = re.match(r'^- Row (\d+), ([^:]+): (.*)$', text[k])
                    if m: items[int(m.group(1))] = (m.group(2), m.group(3))
                    k += 1
            families.append({'member': member, 'anchor': fam_anchor, 'rows': len(rows), 'consumer_items': len(items)})
            for n, (ln, cells) in enumerate(rows, 1):
                premises, consequence, rule, owner, pillar = cells[0], cells[1], cells[2], cells[3], cells[4] if len(cells) > 4 else ''
                loci = [{'text': t, 'target': u} for t, u in LINK.findall(rule)]
                own = loci[0]['target'] if loci else ''
                own_member, _, own_anchor = own.partition('#')
                own_member = own_member or member
                consumers = []
                name, body = items.get(n, ('', ''))
                for t, u in LINK.findall(body):
                    cm, _, ca = u.partition('#'); consumers.append({'text': t, 'member': cm or member, 'anchor': ca})
                records.append({
                    'id': f'{member[:-3]}.{fam_anchor}.row-{n}',
                    'kind': 'family-row',
                    'owner': {'member': member, 'anchor': own_anchor or fam_anchor, 'family_anchor': fam_anchor, 'table_line': ln,
                              'section_sha256': digest(own_member, own_anchor) if own_anchor else digest(member, fam_anchor)},
                    'rule_loci': loci,
                    'premises': premises,
                    'determination': consequence,
                    'owner_decisions': owner,
                    'pillars': pillar,
                    'consumers': consumers,
                    'consumers_name': name,
                    'consumer_absence_stated': ('no separate consumer applies' in body) or ('no consumer applies' in body),
                })
            i = j
        else: i += 1
prog = json.load(open('a_c/i3/axiomatic-program.json'))
cons = json.load(open('a_c/i3/consumers.json'))
cons_by = {}
units = cons.get('units') or cons.get('clauses') or []
for u in units if isinstance(units, list) else []:
    cons_by[u.get('clause') or u.get('uri')] = u.get('consumers') or u.get('bindings') or []
for c in prog['clauses']:
    src = c['source_refs'][0].rsplit('/', 1)[-1]; m, _, a = src.partition('#')
    records.append({'id': c['uri'].rsplit(':', 1)[-1], 'kind': 'clause', 'owner': {'member': m, 'anchor': a, 'section_sha256': digest(m, a)},
                    'determination': c['statement'], 'operator': c['operator'].rsplit(':', 1)[-1],
                    'consumers': cons_by.get(c['uri'], []) if isinstance(cons_by.get(c['uri']), list) else []})
out = {'kind': 'claude-determinations-record', 'schema_version': 1, 'generated_from': 'standards/*.md family tables and consumers paragraphs; a_c/i3/axiomatic-program.json; a_c/i3/consumers.json',
       'families': families, 'counts': {'family_rows': sum(1 for r in records if r['kind'] == 'family-row'), 'clauses': sum(1 for r in records if r['kind'] == 'clause'),
       'rows_without_consumer': sum(1 for r in records if r['kind'] == 'family-row' and not r['consumers']),
       'rows_with_absence_stated': sum(1 for r in records if r['kind'] == 'family-row' and not r['consumers'] and r['consumer_absence_stated'])},
       'records': records}
json.dump(out, open('qualification/C3-ITER5/determinations/DETERMINATIONS.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out['counts'])); print(len(families), 'families:', [(f['member'], f['rows'], f['consumer_items']) for f in families])
