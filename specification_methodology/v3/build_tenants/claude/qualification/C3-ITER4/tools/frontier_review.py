"""Build frontier/REVIEW.json from the Markdown frontier (port C3, adapted).

Usage, from the tenant root: python3 -I qualification/C3-ITER4/tools/frontier_review.py
Reads the installed rc.2 standards and this candidate's standards; writes
frontier/REVIEW.json. A section's text, for its hash, runs to the next heading of
any level: the frontier's own granularity rule (one row per heading section, a
parent's row not covering its children), which differs on purpose from the frame
generator's whole-section rule. modal_conversion is raised only for `conserved`
rows with a successor locus: a `superseded` row is decided by its proposed
replacement relation, not by the conservation reading; a row without a locus has
nothing to compare. Fields beyond the donor schema: identifiers, disposition_note,
proposed_replacement, acceptance and the summary counts. Every semantic_review.result is `indeterminate` unless
frontier/REVIEW_ASSESSMENTS.json records a nonauthor assessment for the row.
"""
import hashlib, json, os, re, sys
RC2 = '/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards'
def slug(h):
    return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')
def sections(path):
    """anchor -> text under the heading up to the next heading of any level"""
    out, seen, cur, buf, code = {}, {}, None, [], False
    for line in open(path, encoding='utf-8'):
        if line.startswith('```'): code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if cur is not None: out[cur] = ''.join(buf)
            s = slug(m.group(2)); n = seen.get(s, 0); seen[s] = n + 1
            cur = s if n == 0 else f'{s}-{n}'; buf = []
        else:
            buf.append(line)
    if cur is not None: out[cur] = ''.join(buf)
    return out
assess = {}
if os.path.exists('frontier/REVIEW_ASSESSMENTS.json'):
    assess = {a['id']: a for a in json.load(open('frontier/REVIEW_ASSESSMENTS.json'))['assessments']}
rows, member, base, pred = [], None, None, {}
succ_cache = {}
def succ(locus):
    f, _, a = locus.partition('#')
    if f not in succ_cache:
        p = os.path.join('standards', f)
        succ_cache[f] = sections(p) if os.path.exists(p) else None
    s = succ_cache[f]
    if s is None or a not in s: return None
    return s[a]
unres_pred = unres_succ = 0
for line in open('frontier/PREDECESSOR_CLAIMS.md', encoding='utf-8'):
    if line.startswith('## '):
        member = line[3:].strip(); base = None; pred = {}; continue
    m = re.match(r'Base route: `stdo://releases/v2\.5\.1-rc\.2/standards/([^`]+)`', line)
    if m:
        base = m.group(1); p = os.path.join(RC2, base)
        pred = sections(p) if os.path.exists(p) else {}
        continue
    if not line.startswith('| ') or line.startswith('|---'): continue
    c = [x.strip() for x in line.rstrip('\n').strip('|').split(' | ')]
    if len(c) < 6: continue
    am = re.search(r'`#([^`]+)`', c[1])
    if not am: continue
    anchor = am.group(1); dcell = c[4].strip('`* ')
    dm = re.match(r'(conserved|superseded|removed|rejected)', dcell)
    disp = dm.group(1) if dm else dcell.split(' ')[0]
    proposed = bool(re.search(r'\bproposed\b', dcell)) or disp == 'superseded'
    loci = re.findall(r'`([^`#\s]+\.md#[^`]+)`', c[5])
    ptext = pred.get(anchor)
    if ptext is None: unres_pred += 1
    stexts = [(l, succ(l)) for l in loci]
    for l, t in stexts:
        if t is None: unres_succ += 1
    pmodal = bool(ptext and re.search(r'\b(must|shall)\b', ptext, re.I))
    smodal = any(t and re.search(r'\b(must|shall)\b', t, re.I) for _, t in stexts)
    rid = f'{member}#{anchor}'
    a = assess.get(rid)
    rows.append({
        'id': rid, 'source_member': base, 'source_anchor': '#' + anchor, 'identifiers': c[2],
        'disposition': disp, 'disposition_note': dcell if dcell != disp else '', 'proposed_replacement': proposed, 'disposition_standing': 'author_proposal',
        'acceptance': 'ticket_decision_pending',
        'predecessor_sha256': hashlib.sha256(ptext.encode()).hexdigest() if ptext is not None else None,
        'successor_loci': [{'locus': l, 'sha256': hashlib.sha256(t.encode()).hexdigest() if t is not None else None} for l, t in stexts],
        'modal_conversion': bool(pmodal and loci and not smodal and disp == 'conserved'),
        'semantic_review': a['semantic_review'] if a else {
            'result': 'indeterminate',
            'scope': 'author disposition; no nonauthor assessment recorded for this row',
            'remaining_obligations': ['author-independent comparison of required and permitted decisions, modal force, triggers, scope and exceptions']}
    })
sem = hashlib.sha256(json.dumps([(r['id'], r['disposition'], r['predecessor_sha256'], r['successor_loci']) for r in rows]).encode()).hexdigest()
out = {'kind': 'claude-frontier-review', 'schema_version': 1, 'rows': rows, 'row_count': len(rows), 'semantic_sha256': sem,
       'counts': {'modal_conversion': sum(r['modal_conversion'] for r in rows),
                  'assessed': sum(1 for r in rows if r['semantic_review']['result'] != 'indeterminate'),
                  'unresolved_predecessor_anchor': unres_pred, 'unresolved_successor_locus': unres_succ,
                  'proposed_replacement': sum(r['proposed_replacement'] for r in rows), 'by_disposition': {d: sum(1 for r in rows if r['disposition'] == d) for d in sorted({r['disposition'] for r in rows})}}}
json.dump(out, open('frontier/REVIEW.json', 'w'), indent=1); print(json.dumps(out['counts']), 'rows', len(rows))
