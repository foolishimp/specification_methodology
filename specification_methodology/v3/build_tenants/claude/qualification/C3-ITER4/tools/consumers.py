"""Build a_c/i3/consumers.json (port C4, adapted): for each clause, its owner locus
and the sections of this candidate that cite that owner. support is `cites` when
derived from a link; `required`/`conditional` only where a_c/i3/consumer_readings.json
records a reader's judgment. Run from the tenant root with python3 -I.
"""
import glob, hashlib, json, os, re
def slug(h): return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
def sections(path):
    out, seen, cur, buf, code = {}, {}, None, [], False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'): code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if cur is not None: out[cur] = ''.join(buf)
            s = slug(m.group(2)); n = seen.get(s, 0); seen[s] = n + 1
            cur = s if n == 0 else f'{s}-{n}'; buf = []
        else: buf.append(line)
    if cur is not None: out[cur] = ''.join(buf)
    return out
std = {os.path.basename(f): sections(f) for f in glob.glob('standards/*.md')}
readings = {}
if os.path.exists('a_c/i3/consumer_readings.json'):
    readings = {(r['clause'], r['consumer']): r for r in json.load(open('a_c/i3/consumer_readings.json'))['readings']}
lcm = json.load(open('a_c/i3/logical-constraint-map.json'))
units = []
for c in lcm['clauses']:
    owners = []
    for ref in c.get('source_refs', []):
        m = re.match(r'stdo-3://build_tenants/claude/standards/([^#]+)#(.+)$', ref)
        if not m: continue
        f, a = m.group(1), m.group(2)
        text = std.get(f, {}).get(a)
        owners.append({'locus': f'{f}#{a}', 'sha256': hashlib.sha256(text.encode()).hexdigest() if text is not None else None, 'resolves': text is not None})
    consumers = []
    for o in owners:
        f, a = o['locus'].split('#', 1)
        for mf, secs in std.items():
            for sa, t in secs.items():
                if mf == f and sa == a: continue
                if (mf == f and f'(#{a})' in t) or (f'{f}#{a})' in t):
                    r = readings.get((c['uri'], f'{mf}#{sa}'))
                    consumers.append({'locus': f'{mf}#{sa}', 'owner': o['locus'], 'support': r['support'] if r else 'cites', 'basis': r['basis'] if r else 'link-derived; semantics unresolved'})
    units.append({'clause': c['uri'], 'statement': c['statement'][:160], 'owners': owners, 'consumers': consumers})
out = {'kind': 'claude-i3-consumers', 'schema_version': 1, 'units': units,
       'counts': {'clauses': len(units), 'owners_unresolved': sum(1 for u in units for o in u['owners'] if not o['resolves']),
                  'consumer_bindings': sum(len(u['consumers']) for u in units),
                  'clauses_without_consumer': sum(1 for u in units if not u['consumers']),
                  'read_support': sum(1 for u in units for x in u['consumers'] if x['support'] != 'cites')}}
json.dump(out, open('a_c/i3/consumers.json', 'w'), indent=1); print(json.dumps(out['counts']))
