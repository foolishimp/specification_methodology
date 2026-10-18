"""Build the disposition-reading packet for the loan evaluation from exact Git objects.

Run: python3 -I build_loan_packets.py <repo> <out_dir> <sealed_dir> <crosstab.json>
"""
import hashlib, json, os, re, secrets, shutil, subprocess, sys

REPO, OUT, SEALED, CROSSTAB = sys.argv[1:5]
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
RC2 = ('c45a6c6739c72c47974d7435424d3db2dc2662a9', 'specification_methodology/specification/standards')
CLAUDE = ('c2cfa9b908d1722ae3f26c32fa4ece691083bdc3', 'specification_methodology/v3/build_tenants/claude')
CODEX = ('c46e9f965d5e2c44d2b1c0ec0a8a5cbd0c0b1d1e', 'specification_methodology/v3/build_tenants/codex')
CLAUDE_RECORD = 'frontier/REVIEW.json'
CODEX_RECORD = 'qualification/C3/rc5/integration/CONSERVATION.json'


def git(*a, text=False):
    return subprocess.check_output(['git', '-C', REPO, *a], text=text)


def resolve(commit):
    return git('rev-parse', commit + '^{commit}', text=True).strip()


CODEX = (resolve('c46e9f96'), CODEX[1])

SCRUB = [
    (re.compile(r'build_tenants/(claude|codex)'), 'build_tenants/[tenant]'),
    (re.compile(r'urn:stdo-3:(claude|codex):'), 'urn:stdo-3:[tenant]:'),
    (re.compile(r'\b(Claude|Codex|codex|CLAUDE|CODEX)\b(?!\.md|_TEMPLATE)'), '[tenant]'),
    (re.compile(r'(?<![A-Z_/.])claude\b(?![.\-_]md|_TEMPLATE|-plugin|-skills)'), '[tenant]'),
]


def scrub(text):
    for pat, rep in SCRUB:
        text = pat.sub(rep, text)
    return text


def slug(h):
    return re.sub(r'[^\w\- ]', '', h.strip().lower().replace('`', '')).replace(' ', '-')


def headings(text):
    """(line index, level, anchor) for each heading outside code fences, with GitHub duplicate suffixes."""
    out, seen, code = [], {}, False
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('```'):
            code = not code
        m = None if code else re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            s = slug(m.group(2)); n = seen.get(s, 0); seen[s] = n + 1
            out.append((i, len(m.group(1)), s if n == 0 else f'{s}-{n}'))
    return lines, out


def section(text, anchor, children):
    lines, hs = headings(text)
    for k, (i, lvl, a) in enumerate(hs):
        if a == anchor:
            end = len(lines)
            for j, l2, _ in hs[k + 1:]:
                if not children or l2 <= lvl:
                    end = j; break
            return '\n'.join(lines[i:end]).rstrip() + '\n', i + 1, end
    return None, None, None


cache = {}
def member_text(commit, path):
    key = (commit, path)
    if key not in cache:
        cache[key] = git('show', f'{commit}:{path}').decode('utf-8')
    return cache[key]


def put(path, raw):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(raw)


ct = json.load(open(CROSSTAB))
claude_rows = {r['id']: r for r in json.loads(git('show', f'{CLAUDE[0]}:{CLAUDE[1]}/{CLAUDE_RECORD}'))['rows']}
codex_rows = {r['id']: r for r in json.loads(git('show', f'{CODEX[0]}:{CODEX[1]}/{CODEX_RECORD}'))['rows']}

codex_is_a = secrets.randbits(1) == 1
salt = secrets.token_hex(16)
key = {'A': 'codex' if codex_is_a else 'claude', 'B': 'claude' if codex_is_a else 'codex', 'salt': salt}
os.makedirs(SEALED, exist_ok=True)
put(os.path.join(SEALED, 'KEY.json'), json.dumps(key, indent=1))
seal = hashlib.sha256(f"A={key['A']};B={key['B']};salt={salt}".encode()).hexdigest()
label = {'codex': 'A' if codex_is_a else 'B', 'claude': 'B' if codex_is_a else 'A'}

shutil.rmtree(OUT, ignore_errors=True)
for src in ['PRODUCT.md', 'requirements/README.md', 'requirements/ASSURANCE.md']:
    put(os.path.join(OUT, 'common', os.path.basename(src)), member_text(COMMON, 'specification_methodology/v3/specification/' + src))

unresolved, sections_written, rows_out = [], {}, []
def copy_tree(line, commit, root):
    for f in git('ls-tree', '-r', '--name-only', commit, '--', f'{root}/standards', text=True).split():
        rel = f'{label[line]}/' + f[len(root) + 1:]
        if rel.endswith('.md'):
            put(os.path.join(OUT, rel), scrub(member_text(commit, f)))
            sections_written[rel] = len(member_text(commit, f).encode())
copy_tree('claude', CLAUDE[0], CLAUDE[1])
copy_tree('codex', CODEX[0], f'{CODEX[1]}/successor')
for f in git('ls-tree', '-r', '--name-only', RC2[0], '--', RC2[1], text=True).split():
    if f.endswith('.md'):
        put(os.path.join(OUT, 'rc2', 'standards', os.path.basename(f)), member_text(RC2[0], f))

def locus_file(line, commit, root, locus):
    path, _, anchor = locus.partition('#')
    path = path if path.startswith('standards/') else 'standards/' + path
    rel = f'{label[line]}/{path}'
    try:
        text = member_text(commit, f'{root}/{path}')
    except subprocess.CalledProcessError:
        unresolved.append((line, locus, 'no member')); return None
    if not anchor:
        return f'{rel} (whole file, {len(text.splitlines())} lines)'
    body, start, end = section(text, anchor, children=False)
    if body is None:
        unresolved.append((line, locus, 'no anchor')); return None
    _, cs, ce = section(text, anchor, children=True)
    extra = f'; with subsections to line {ce}' if ce != end else ''
    return f'{rel} lines {start}-{end}{extra}'


SHARED = {'I3-R2-R003', 'I3-R2-R012', 'I3-R2-R015'}
for n, it in enumerate(sorted(ct['differ'], key=lambda d: (d['claude'], d['codex'], d['id'])), 1):
    rid = it['id']; c = claude_rows[rid]; x = codex_rows[rid]
    member, _, anchor = rid.partition('#')
    pred, ps, pe = section(member_text(RC2[0], f'{RC2[1]}/{member}'), anchor, children=False)
    split_note = ''
    if pred is None:
        parts_a = anchor.split('-')
        for k in range(len(parts_a) - 1, 0, -1):
            pred, ps, pe = section(member_text(RC2[0], f'{RC2[1]}/{member}'), '-'.join(parts_a[:k]), children=False)
            if pred is not None:
                split_note = (f"This row is a sentence-level split of the section below; the common inventory names it "
                              f"by the anchor `#{anchor}`. Judge only that part.\n\n"); break
        if pred is None:
            unresolved.append(('rc2', rid, 'no anchor')); pred = '(not resolved)\n'
    shared = sorted(set(x.get('shared_replacement_dependencies') or []) & SHARED)
    rec = {}
    disp_c = {'not': 'not applicable'}.get(c['disposition'], c['disposition'])
    rec['claude'] = [f"Disposition: {disp_c}", f"Note: {c.get('disposition_note') or '(none)'}"]
    loci_c = [l['locus'] if isinstance(l, dict) else l for l in c.get('successor_loci', [])]
    rec['codex'] = [f"Disposition: {x['disposition']}", f"Note: {x.get('reason') or x.get('note') or '(none)'}"]
    sr = x.get('successor_relation') or {}
    if sr.get('changed_meaning'):
        rec['codex'].append(f"Changed meaning stated by this line's record: {sr['changed_meaning']}")
    loci_x = list(x.get('successor_loci') or [])
    for l in sr.get('replacement_loci') or []:
        if l not in loci_x: loci_x.append(l)
    files = {'claude': [(l, locus_file('claude', CLAUDE[0], CLAUDE[1], l)) for l in loci_c],
             'codex': [(l, locus_file('codex', CODEX[0], f'{CODEX[1]}/successor', l)) for l in loci_x]}
    parts = [f"# Row {n:02d}: `{rid}`\n",
             f"Shared cause tag: {', '.join(shared) if shared else 'none'}\n",
             f"## Predecessor text\n\n{split_note}rc.2 `{member}` lines {ps}-{pe}, from the heading to the next heading of any level (full member: `rc2/standards/{member}`):\n\n````markdown\n{pred}````\n"]
    for line in sorted(label, key=lambda k: label[k]):
        parts.append(f"## Line {label[line]} record\n\n" + '\n'.join('- ' + scrub(s) for s in rec[line]) + '\n\nSuccessor loci:\n' +
                     '\n'.join(f"- `{scrub(l)}` -> {('`' + f + '`') if f else 'UNRESOLVED'}" for l, f in files[line]) + '\n')
    put(os.path.join(OUT, 'rows', f'{n:02d}.md'), '\n'.join(parts))
    rows_out.append({'n': n, 'id': rid, 'claude': disp_c, 'codex': x['disposition'], 'shared': shared})

# The three shared causes, stated once.
causes = []
for r in codex_rows.values():
    sr = r.get('successor_relation') or {}
    if sr.get('id') in SHARED:
        causes.append(f"## {sr['id']} (tagged in line {label['codex']}'s record at `{r['id']}`)\n\n{scrub(sr['changed_meaning'])}\n\nLoci: " + ', '.join('`' + scrub(l) + '`' for l in sr.get('replacement_loci', [])) + '\n')
put(os.path.join(OUT, 'CAUSES.md'), '# Shared causes\n\nLine ' + label['codex'] + "'s record tags some rows with these shared replacement causes. Judge each once, then check each tagged row only for what goes beyond it.\n\n" + '\n'.join(sorted(causes)))

index = ['# Index of rows', '', '| Row | Claim | Line A | Line B | Shared cause |', '|---|---|---|---|---|']
for r in rows_out:
    index.append(f"| {r['n']:02d} | `{r['id']}` | {r[key['A']]} | {r[key['B']]} | {', '.join(r['shared']) or '-'} |")
put(os.path.join(OUT, 'INDEX.md'), '\n'.join(index) + '\n')

hashes = []
for dp, _, fs in sorted(os.walk(OUT)):
    for f in sorted(fs):
        p = os.path.join(dp, f)
        hashes.append(f"{hashlib.sha256(open(p, 'rb').read()).hexdigest()}  {os.path.relpath(p, OUT)}")
put(os.path.join(os.path.dirname(OUT.rstrip('/')), 'PACKET_SHA256.txt'), '\n'.join(hashes) + '\n')
print(json.dumps({'rows': len(rows_out), 'member_files': len(sections_written), 'member_bytes': sum(sections_written.values()),
                  'unresolved': unresolved, 'seal': seal, 'codex_record_commit': CODEX[0]}, indent=1))
