"""Build release/manifest.json for the commit named, from git, and validate it against the installed-release
manifest schema (I5-10, after the RC1 manifest admitted only the top-level members). The standards member set
is every file under standards/ at that commit; the plugin member set every file under plugins/spec/.
Usage, from the tenant root: python3 -I release/build_manifest.py <commit> <tag object>
"""
import hashlib, json, subprocess, sys
commit, tag = sys.argv[1], sys.argv[2]
T = 'specification_methodology/v3/build_tenants/claude'
git = lambda *a: subprocess.check_output(['git', *a], text=True).strip()
blob = lambda path: subprocess.check_output(['git', 'show', f'{commit}:{T}/{path}'])
def files(root):
    out = git('ls-tree', '-r', '--name-only', '--full-tree', commit, f'{T}/{root}').split('\n')
    return sorted(p[len(T) + len(root) + 2:] for p in out if p)
sha = lambda b: hashlib.sha256(b).hexdigest()
std = [{'path': p, 'sha256': sha(blob('standards/' + p))} for p in files('standards')]
plug = [{'path': p, 'sha256': sha(blob('plugins/spec/' + p))} for p in files('plugins/spec')]
member_set = sha(''.join(f"{m['sha256']}  {m['path']}\n" for m in std).encode())
m = {'kind': 'stdo.installed-release-manifest', 'schema_version': 1,
     'release': {'cut': 'v3.0.0-rc.4', 'tag_object': tag, 'commit': commit, 'tree': git('rev-parse', f'{commit}^{{tree}}'),
                 'standards_tree': git('rev-parse', f'{commit}:{T}/standards'),
                 'project_release_namespace': 'specification_methodology-claude',
                 'qualified_ref': 'refs/tags/specification_methodology-claude/v3.0.0-rc.4',
                 'project_subtree_root': T, 'project_subtree_tree': git('rev-parse', f'{commit}:{T}')},
     'standards': {'installed_root': 'standards', 'source_root': 'specification/standards', 'member_count': len(std),
                   'member_set_sha256': member_set, 'members': std},
     'auxiliary': {'plugin': {'installed_root': 'plugins/spec', 'source_root': 'plugins/spec', 'member_count': len(plug), 'members': plug},
                   'license': {'path': 'LICENSE', 'sha256': sha(blob('LICENSE'))},
                   'release_note': {'source_path': 'releases/v3.0.0.md', 'installed_path': 'release/release-note.md', 'sha256': sha(blob('release/release-note.md'))}}}
import jsonschema
schema = json.loads(blob('standards/schemas/installed-release-manifest.schema.json'))
V = getattr(jsonschema, 'Draft202012Validator', jsonschema.Draft7Validator)
errs = list(V(schema).iter_errors(m))
for e in errs: print('SCHEMA:', list(e.path), e.message[:160])
if errs: raise SystemExit('refusal: manifest does not validate')
if not std or not plug: raise SystemExit('refusal: empty member set')
json.dump(m, open('release/manifest.json', 'w'), indent=1); open('release/manifest.json', 'a').write('\n')
print(f'manifest: {len(std)} standards files, {len(plug)} plugin files; validates against the schema')
