"""Build the routing, frames and members packet (reader B) from exact Git objects.

R is the receiving line, D the donor. Run: python3 -I build_reader_b_packet.py <repo> <out_dir> <rc9_assets> <frame_quotes.txt>
"""
import hashlib, os, re, shutil, subprocess, sys

REPO, OUT, RC9, FQ = sys.argv[1:5]
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
R = ('c2cfa9b908d1722ae3f26c32fa4ece691083bdc3', 'specification_methodology/v3/build_tenants/claude', 'standards')
D = ('c46e9f96381097245a6714164f03b72ad32116c0', 'specification_methodology/v3/build_tenants/codex', 'successor/standards')
SCRUB = [
    (re.compile(r'build_tenants/(claude|codex)'), 'build_tenants/[tenant]'),
    (re.compile(r'urn:stdo-3:(claude|codex):'), 'urn:stdo-3:[tenant]:'),
    (re.compile(r'\b(Claude|Codex|codex|CLAUDE|CODEX)\b(?!\.md|_TEMPLATE)'), '[tenant]'),
    (re.compile(r'(?<![A-Z_/.])claude\b(?![.\-_]md|_TEMPLATE|-plugin|-skills)'), '[tenant]'),
]


def scrub(t):
    for p, r in SCRUB:
        t = p.sub(r, t)
    return t


def git(*a, text=False):
    return subprocess.check_output(['git', '-C', REPO, *a], text=text)


def put(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(text)


shutil.rmtree(OUT, ignore_errors=True)
for tag, (commit, root, sub) in (('R', R), ('D', D)):
    for f in git('ls-tree', '-r', '--name-only', commit, '--', f'{root}/{sub}', text=True).split():
        rel = f[len(f'{root}/{sub}') + 1:]
        if rel.startswith('templates/') or rel.startswith('schemas/'):
            continue
        if rel.endswith('.md') or rel.endswith('.json'):
            put(os.path.join(OUT, tag, 'standards', rel), scrub(git('show', f'{commit}:{f}').decode('utf-8')))
for src in ['PRODUCT.md', 'requirements/README.md', 'requirements/ASSURANCE.md', 'REFERENCE_FRAME_BASIS.md']:
    put(os.path.join(OUT, 'common', os.path.basename(src)), git('show', f'{COMMON}:specification_methodology/v3/specification/{src}').decode('utf-8'))
header = ('<!-- In this report, candidate A is the receiving line R and candidate B is the donor line D. '
          'The report was written on an earlier blind packet; its file paths name that packet, '
          'and its line numbers match the files under R/ and D/ here. -->\n\n')
for name in ('READ2A_REPORT.md', 'READ2B_REPORT.md'):
    put(os.path.join(OUT, 'rc9', name), header + open(os.path.join(RC9, name), encoding='utf-8').read())
for name in ('SCENARIOS.md', 'EXPECTED.md'):
    put(os.path.join(OUT, 'rc9', name), open(os.path.join(RC9, name), encoding='utf-8').read())
put(os.path.join(OUT, 'R_FRAME_QUOTES.txt'), '# R: frame sizes and which frames copy each owner section\n\n'
    'Frame capacity is 160,000 bytes. A change to an owner section grows every frame that copies it.\n\n' + open(FQ).read())
hashes = []
for dp, _, fs in sorted(os.walk(OUT)):
    for f in sorted(fs):
        p = os.path.join(dp, f)
        hashes.append(f"{hashlib.sha256(open(p, 'rb').read()).hexdigest()}  {os.path.relpath(p, OUT)}")
put(os.path.join(os.path.dirname(OUT.rstrip('/')), 'PACKET_B_SHA256.txt'), '\n'.join(hashes) + '\n')
print(len(hashes), 'files')
