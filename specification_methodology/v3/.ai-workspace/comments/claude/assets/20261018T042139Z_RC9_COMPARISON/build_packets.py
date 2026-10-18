"""Build the two blind reading packets for the RC9 comparison from exact Git objects.

Run from anywhere: python3 -I build_packets.py <repo> <out_dir> <sealed_dir>
"""
import hashlib, json, os, re, secrets, shutil, subprocess, sys

REPO, OUT, SEALED = sys.argv[1:4]
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
CODEX = ('5592168e26759f37e730aed12c030a6061709ec4', 'specification_methodology/v3/build_tenants/codex/successor')
CLAUDE = ('c2cfa9b908d1722ae3f26c32fa4ece691083bdc3', 'specification_methodology/v3/build_tenants/claude')
I5_REPORT = sys.argv[4]  # extracted I5 test 1 report, for its 65 expectations


def git_bytes(commit, path):
    return subprocess.check_output(['git', '-C', REPO, 'show', f'{commit}:{path}'])


def git_files(commit, prefix):
    out = subprocess.check_output(['git', '-C', REPO, 'ls-tree', '-r', '--name-only', commit, '--', prefix], text=True)
    return [p for p in out.splitlines() if p]


SCRUB = [
    (re.compile(r'build_tenants/(claude|codex)'), 'build_tenants/[tenant]'),
    (re.compile(r'urn:stdo-3:(claude|codex):'), 'urn:stdo-3:[tenant]:'),
    (re.compile(r'\b(Claude|Codex|codex)\b(?!\.md|_TEMPLATE)'), '[tenant]'),
    (re.compile(r'(?<![A-Z_/.])claude\b(?![.\-_]md|_TEMPLATE|-plugin|-skills)'), '[tenant]'),
]


def scrub(raw):
    text = raw.decode('utf-8')
    for pat, rep in SCRUB:
        text = pat.sub(rep, text)
    return text.encode('utf-8')


def put(path, raw):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(raw)


# Blind key, drawn at random and sealed by hash before any reading.
codex_is_a = secrets.randbits(1) == 1
salt = secrets.token_hex(16)
key = {'A': 'codex' if codex_is_a else 'claude', 'B': 'claude' if codex_is_a else 'codex', 'salt': salt}
key_line = f"A={key['A']};B={key['B']};salt={salt}"
os.makedirs(SEALED, exist_ok=True)
put(os.path.join(SEALED, 'KEY.json'), json.dumps(key, indent=1).encode())
seal = hashlib.sha256(key_line.encode()).hexdigest()
label = {'codex': 'A' if codex_is_a else 'B', 'claude': 'B' if codex_is_a else 'A'}

# ---- Read 1: owner-text fidelity, same expectations and locators as the I5 test 1.
r1 = os.path.join(OUT, 'r1')
for src, dst in [('requirements/README.md', 'README.md'), ('PRODUCT.md', 'PRODUCT.md'),
                 ('requirements/ASSURANCE.md', 'ASSURANCE.md'), ('REFERENCE_FRAME_BASIS.md', 'REFERENCE_FRAME_BASIS.md')]:
    put(os.path.join(r1, 'common', dst), git_bytes(COMMON, 'specification_methodology/v3/specification/' + src))
report = open(I5_REPORT, encoding='utf-8').read()
expect = report[report.index('## Expectations'):report.index('## Candidate A')].strip()
put(os.path.join(r1, 'EXPECTATIONS.md'), (
    '# Fixed expectations\n\n'
    'These 65 expectations were fixed earlier by a separate fresh reader from the files now under `common/`, '
    'before that reader opened any candidate. Line references: R = `common/README.md`, P = `common/PRODUCT.md`, '
    'S = `common/ASSURANCE.md`, F = `common/REFERENCE_FRAME_BASIS.md`. Use them as given; if one misstates its '
    'source, say so and judge against the source.\n\n' + expect.replace('## Expectations', '').strip() + '\n').encode())
locator = {
    'codex': ('Owner sections. Construction relation: `FOUNDATIONS.md` `## Construction and use` (to the next `## `) and '
              '`## Bounded construction` (to the next `## `). Assurance relations: `FOUNDATIONS.md` `## Construction assurance` '
              'with its subsections (Preservation obligations, Assertions and observations, Parallel assurance and provenance, '
              'Risk and assurance selection, Change impact and evidence retention), to the next `## `.\n'),
    'claude': ('Owner sections. Construction relation: `ACTIVATION.md` from `### Construction relation` to the next `###` heading, '
               'with `FOUNDATIONS.md` `### Construction synthesis`. Assurance relations: `FOUNDATIONS.md` from `### Assurance relations` '
               'through the end of `### Formal representation` (the family head and six subsections).\n'),
}
for line, (commit, root), members in [('codex', CODEX, ['standards/FOUNDATIONS.md']),
                                      ('claude', CLAUDE, ['standards/ACTIVATION.md', 'standards/FOUNDATIONS.md'])]:
    d = os.path.join(r1, label[line])
    for m in members:
        put(os.path.join(d, os.path.basename(m)), scrub(git_bytes(commit, f'{root}/{m}')))
    put(os.path.join(d, 'LOCATOR.md'), locator[line].encode())

# ---- Read 2: scenario walkthroughs by route, from each candidate's installed standards entry.
r2 = os.path.join(OUT, 'r2')
for line, (commit, root) in [('codex', CODEX), ('claude', CLAUDE)]:
    d = os.path.join(r2, label[line])
    for p in git_files(commit, f'{root}/standards'):
        rel = p[len(root) + 1:]
        if rel.endswith('.md') and (rel.count('/') == 1 or rel.startswith('standards/frames/')):
            put(os.path.join(d, rel), scrub(git_bytes(commit, p)))
    extra = ['README.md', 'interpretation/README.md', 'interpretation/FRAMES.md'] if line == 'codex' else ['a_c/i3/README.md']
    for rel in extra:
        put(os.path.join(d, rel), scrub(git_bytes(commit, f'{root}/{rel}')))

print(json.dumps({'seal_sha256': seal, 'seal_preimage_format': 'A=<line>;B=<line>;salt=<hex>'}, indent=1))
