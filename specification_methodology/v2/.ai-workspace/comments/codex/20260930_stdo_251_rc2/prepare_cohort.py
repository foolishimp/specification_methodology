"""Bind the unchanged mechanics and targeted RC2 representation using existing release checks."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
VERSION = '2.5.1-rc.2'
CUT = 'v' + VERSION
spec = importlib.util.spec_from_file_location('rc2_check', ROOT / 'scripts/check_stack_release.py')
check = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = check
spec.loader.exec_module(check)
view = check.View(ROOT)
load = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

def put(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')

prior = json.loads(subprocess.check_output(['git', 'show', '4e83fdc4e31ad2161ab70a9759cecbbae5390b69:stack_release.json'], cwd=ROOT))
assert prior['cohort']['version'] == '2.5.1-rc.1'
payload = json.loads(json.dumps(prior).replace('2.5.1-rc.1', VERSION))
receipt = load(OUT / 'stdo-install.json')
verify = load(OUT / 'stdo-verify.json')
assert verify['valid'] and not verify['failures']
assert verify['manifest_sha256'] == receipt['manifest_sha256']
source_inventory = load(OUT / 'source-inventory.json')
source = payload['products']['specification_methodology']
freeze = {key: receipt['release'][key] for key in ('tag_object', 'commit', 'tree', 'project_subtree_tree', 'standards_tree')}
assert freeze == check.local_tag_identity(ROOT, source['release_ref'], source['subtree'])
freeze.update(installed_manifest_sha256=receipt['manifest_sha256'],
              standards_member_count=receipt['standards']['member_count'],
              standards_member_set_sha256=receipt['standards']['member_set_sha256'],
              plugin_member_count=len(source_inventory['plugin']),
              plugin_member_set_sha256=check.member_stream(('./' + row['path'], row['sha256']) for row in source_inventory['plugin']))
source['freeze'] = freeze
payload['publication'] = load(OUT / 'remote-expectations.json')

for name in ('axiom_indexer', 'stdo_representation'):
    product = payload['products'][name]
    failures = []
    required = check.required_child_members(view, name, product, failures)
    assert not failures, failures
    members = []
    for path, kind in sorted(required.items()):
        full = name + '/' + path
        assert view.member_kind(full) == kind
        content = view.read_member_bytes(full, kind)
        row = {'type': kind, 'path': path, 'sha256': check.sha256(content)}
        if kind == 'symlink': row['target'] = content.decode()
        members.append(row)
    product['subject'] = {'member_count': len(members), 'member_set_sha256': check.product_member_stream(members), 'members': members}
assert payload['products']['axiom_indexer']['subject'] == prior['products']['axiom_indexer']['subject']
assert payload['products']['stdo_representation']['subject']['member_count'] == 9

link = '../../specification_methodology/.ai-workspace/comments/codex/20260930_stdo_251_rc2/README.md'

def note(name, title):
    product = payload['products'][name]
    lines = [f'# {title} 2.5.1 RC2', '', 'Status: coordinated candidate. Exact publication and fresh public acquisition',
             f'are recorded in the [RC2 release record]({link}).', '', '| Coordinate | Value |', '|---|---|']
    lines += product['release_note_markers']
    lines += ['', '## Exact source and Product subject', '',
              f"Source A `{freeze['commit']}`; source tag `{freeze['tag_object']}`; installed",
              f"manifest `{freeze['installed_manifest_sha256']}`; {freeze['standards_member_count']} standards,",
              f"aggregate `{freeze['standards_member_set_sha256']}`.", '',
              f"{product['subject']['member_count']} Product members, aggregate `{product['subject']['member_set_sha256']}`.",
              'Digests cover file bytes or UTF-8 symlink targets; membership remains unchanged.', '',
              '| Type | Member | SHA-256 |', '|---|---|---|']
    for row in product['subject']['members']:
        member = f"`{row['path']}`"
        if row['type'] == 'symlink': member += f" -> `{row['target']}`"
        lines.append(f"| {row['type']} | {member} | `{row['sha256']}` |")
    lines += ['', f"Immutable predecessor: `{name}/v2.5.1-rc.1`. Its exact artifacts and bounded",
              'qualification remain preserved. Continuing-source authoring Definitions/frame bases',
              'retain their existing authority independently of the represented source selection.', '']
    return '\n'.join(lines)

axiom = payload['products']['axiom_indexer']
rep = payload['products']['stdo_representation']
axiom_note = note('axiom_indexer', 'Axiom Indexer') + '''
## Qualification and scope

All seven mechanics members are byte-identical to RC1. Its C01-C03 claims and
valid evidence retain their original scope; C04 advances only the matched-cohort
identity. No new semantic inference, frame selection, executor or API is added.
Existing validation and projection commands reproduce the RC2 program/map and
both views of six indexes. Generic negative-case evidence is reused against the
unchanged executable, schema and output contract. Native interpretation remains
Representation's separately assessed claim.
'''
(ROOT / axiom['release_note']).write_text(axiom_note)
dep = rep['dependencies']['axiom_indexer']
dep['release_record']['sha256'] = sha(ROOT / axiom['release_note'])
artifact_root = ROOT / payload['assets']['stdo_semantic_index']['root']
rep_note = note('stdo_representation', 'STDO Representation') + f'''
## Exact dependency and generated assets

Same-version Axiom: `{axiom['release_ref']}`, seven members,
aggregate `{axiom['subject']['member_set_sha256']}`. External release note
`{dep['release_record']['path']}` SHA-256 `{dep['release_record']['sha256']}`.

| Role | Axiom member | SHA-256 |
|---|---|---|
'''
rep_note += '\n'.join(f"| {m['role']} | `{m['path']}` | `{m['sha256']}` |" for m in dep['mechanics'])
rep_note += '\n\n| Generated artifact / external evidence | SHA-256 |\n|---|---|\n'
rep_note += '\n'.join(f"| `{payload['assets']['stdo_semantic_index']['root']}/{p.name}` | `{sha(p)}` |" for p in sorted(artifact_root.iterdir()) if p.is_file())
rep_note += '''

## Qualification and scope

C01 gains one source-grounded triage clause; all 115 prior clauses and symbols preserve their meaning after exact RC2 source-URI rebinding. One residual replaces a stale RC1 label with source_basis while preserving
its qualification and authority limits. C02 adds that clause to four applicable indexes; all six indexes retain both views.
All 52 exact source members are rebound; changed meaning receives independent
source/program review rather than digest-only acceptance. The map and report
reproduce byte-for-byte using unchanged mechanics.

C03 retains the native interface, with current source/dependency routes and one
fresh Codex context evaluating three bounded triage cases. Independent assessment
of its actual tool use and decisions is retained in companion-review.json. This
is neither repeated-judgment evidence nor a new Claude-host qualification. RC1's
published native reporting limits remain visible in its release record; they
are not retroactively cured by this scope. C04 advances exact cohort identity.

Publication, Product acceptance, source-project authoring adoption and external
consumer migration remain distinct. No generic model reliability or ABG outcome
is claimed. Final closed qualification and publication records supply their own
subjects and results; this release note does not manufacture them.
'''
(ROOT / rep['release_note']).write_text(rep_note)
put(ROOT / 'stack_release.json', payload)
put(OUT / 'cohort-subject.json', {'source_freeze':freeze, 'axiom_subject':axiom['subject'],
                               'representation_subject':rep['subject'],
                               'files':{p:sha(ROOT / p) for p in ['stack_release.json',axiom['release_note'],rep['release_note']]}})
print(json.dumps({'axiom_members':7,'representation_members':9,'version':VERSION}))
