"""Run the installed STDO verifier over Claude's RC9 package (Codex addition A3).

Materialises, from git, the members that Claude's RC9 manifest (commit B) admits, in the
installed layout, into a fresh directory; then calls the installed toolchain's
verify_materialization on the manifest as built, with the canonical member-set digest, with
the digest and release coordinates, and with one byte appended to UX.md.
Usage, from the repository root, with the toolchain's own interpreter:
  ~/.local/pipx/venvs/stdo-toolchain/bin/python -I <this file> <empty scratch dir>
"""
import copy, json, os, subprocess, sys
from pathlib import Path
from stdo_toolchain.manifest import standards_member_set_sha256, verify_materialization

B = '3a2097137c3588ba44b98e3ea801ac7f2be1daf0'
T = 'specification_methodology/v3/build_tenants/claude'
R = Path(sys.argv[1])
if R.exists() and any(R.iterdir()):
    raise SystemExit('refusal: scratch dir not empty')
m = json.loads(subprocess.check_output(['git', 'show', f'{B}:{T}/release/manifest.json']))
c = m['release']['commit']

def put(dst, src):
    p = R / dst
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(subprocess.check_output(['git', 'show', f'{c}:{T}/{src}']))

for x in m['standards']['members']: put('standards/' + x['path'], 'standards/' + x['path'])
for x in m['auxiliary']['plugin']['members']: put('plugins/spec/' + x['path'], 'plugins/spec/' + x['path'])
put('LICENSE', 'LICENSE'); put(m['auxiliary']['release_note']['installed_path'], 'release/release-note.md')
(R / 'manifest.json').write_text(json.dumps(m, indent=1))
print('materialised', sum(len(f) for _, _, f in os.walk(R)), 'files; manifest commit B', B, '; members from', c)
print('declared member_set_sha256 ', m['standards']['member_set_sha256'])
print('canonical member_set_sha256', standards_member_set_sha256(m['standards']['members']))

print('1 as built:', verify_materialization(R, m))
m1 = copy.deepcopy(m); m1['standards']['member_set_sha256'] = standards_member_set_sha256(m1['standards']['members'])
print('2 canonical digest only:', verify_materialization(R, m1))
m2 = copy.deepcopy(m1); r = m2['release']
r['project_release_namespace'] = 'specification_methodology'
r['qualified_ref'] = f"refs/tags/specification_methodology/{r['cut']}"
r['project_subtree_root'] = 'specification_methodology/v3'
print('3 canonical digest and release coordinates:', verify_materialization(R, m2))
with open(R / 'standards/UX.md', 'ab') as f: f.write(b' ')
print('4 as 3, one byte appended to UX.md:', verify_materialization(R, m2))
