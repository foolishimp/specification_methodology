"""Run the selected immutable a_c tool and bounded executable checks.

Structural success is kept separate from independent interpretation fidelity.
No installation, acceptance, real transport or whole-corpus claim follows.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

if not __debug__:
    raise SystemExit('Qualification refuses disabled assertions; run without -O/PYTHONOPTIMIZE.')

root = Path(__file__).resolve().parent
base = root.parents[2]
tool_root = base / 'a_c/install/axiom_indexer-v2.5.1-rc.2'
tool = tool_root / 'build_tenants/core/code/ac.py'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(arguments):
    return subprocess.run([sys.executable, '-B'] + [str(a) for a in arguments],
                          capture_output=True, text=True)


def record(report, operation, result, **fields):
    row = dict(operation=operation, exit=result.returncode, **fields)
    report['operations'].append(row)
    return row


pins = json.loads((root/'INSTALL_VERIFICATION.json').read_text())
for pin in pins['members']:
    path = tool_root / pin['path']
    value = os.readlink(path).encode() if pin['type'] == 'symlink' else path.read_bytes()
    assert hashlib.sha256(value).hexdigest() == pin['sha256'], pin['path']

report = {'operations': [], 'tool_dependency_members_verified': len(pins['members'])}
finite = run([root/'finite_check.py'])
row = record(report, 'finite-token-check', finite)
assert finite.returncode == 0, finite.stderr
data = json.loads(finite.stdout)
row['cases'] = data['cases']
row['label_permission_counterexamples'] = data['unauthorized_mutant_counterexamples']
before = sha(root/'FINITE_RESULT.json')
optimized = subprocess.run([sys.executable, '-B', '-O', str(root/'finite_check.py')],
                           capture_output=True, text=True)
unchanged = before == sha(root/'FINITE_RESULT.json')
row = record(report, 'assertions-disabled', optimized,
             refused=optimized.returncode != 0, old_receipt_unchanged=unchanged)
assert row['refused'] and unchanged
(root/'OPTIMIZATION_REFUSAL.json').write_text(json.dumps({
    **row, 'stderr': optimized.stderr, 'preserved_receipt_sha256': before,
    'standing': 'Refused invocation; preserved receipt is from the normal invocation only'
}, indent=2)+'\n')

for suffix in ['', '-mutant']:
    result = run([tool, 'validate', '--program', root/('program'+suffix+'.json'),
                  '--bindings', root/'bindings.json',
                  '--output', root/('validation'+suffix+'.json'),
                  '--emit-map', root/('map'+suffix+'.json')])
    record(report, 'validate', result, program_suffix=suffix)
    (root/('validation'+suffix+'.stderr.txt')).write_text(result.stderr)
    assert result.returncode == 0, result.stderr

selection = []
for index in json.loads((root/'program.json').read_text())['frame_indexes']:
    selection.extend(['--frame-index', index['uri']])
empty = run([tool, 'project', '--program', root/'program.json', '--map', root/'map.json',
             '--bindings', root/'bindings.json', '--mode', 'reference-only'])
empty_report = json.loads(empty.stdout)
assert empty.returncode != 0 and any(d['code'] == 'empty_selection' for d in empty_report['diagnostics'])
(root/'EMPTY_SELECTION_REFUSAL.json').write_text(empty.stdout)
record(report, 'empty-frame-selection', empty, refused=True)
views = []
for mode in ['reference-only', 'materialized']:
    result = run([tool, 'project', '--program', root/'program.json', '--map', root/'map.json',
                  '--bindings', root/'bindings.json', '--mode', mode,
                  '--output', root/('projection-'+mode+'.json')] + selection)
    record(report, 'project', result, mode=mode)
    assert result.returncode == 0, result.stdout + result.stderr
    (root/('project-'+mode+'.report.json')).write_text(result.stdout)
    views.append(json.loads((root/('projection-'+mode+'.json')).read_text()))
keys = ['closure', 'clause_relations', 'residual_routes', 'source_routes']
assert all(views[0][key] == views[1][key] for key in keys)
assert {c['uri'] for c in views[0]['clause_relations']} == {
    c['uri'] for c in json.loads((root/'program.json').read_text())['clauses']}
report['projection_relations_equal'] = True
report['complete_selected_clause_closure'] = True
report['compared_keys'] = keys

wrong = run([tool, 'project', '--program', root/'program-mutant.json', '--map', root/'map.json',
             '--bindings', root/'bindings.json', '--mode', 'reference-only'] + selection)
record(report, 'wrong-program-old-map', wrong, refused=wrong.returncode != 0)
assert wrong.returncode != 0
(root/'MISMATCH_REFUSAL.json').write_text(json.dumps({
    'exit': wrong.returncode, 'stdout': wrong.stdout, 'stderr': wrong.stderr,
    'normal_program_sha256': sha(root/'program.json'),
    'mutant_program_sha256': sha(root/'program-mutant.json'), 'map_sha256': sha(root/'map.json')
}, indent=2)+'\n')

sections = [
    {'label': 'Selected finite source', 'text': (root/'SOURCE.md').read_text()},
    {'label': 'Selected program view', 'text': (root/'projection-reference-only.json').read_text()},
    {'label': 'Exact scoped request', 'text': 'Assess selected source/model fidelity; structural validity supplies no semantic acceptance or operation grant.'}
]
(root/'sections.json').write_text(json.dumps(sections, indent=2)+'\n')
joined = run([tool, 'join', '--input', root/'sections.json', '--output', root/'REQUEST.txt'])
record(report, 'exact-join', joined)
assert joined.returncode == 0, joined.stderr
expected = '\n\n'.join(s['label']+'\n'+s['text'] for s in sections)
assert (root/'REQUEST.txt').read_text() == expected
report['operations'][-1]['exact'] = True
report['pins'] = {name: sha(root/name) for name in [
    'SOURCE.md', 'ENCODING.md', 'program.json', 'program-mutant.json', 'finite_check.py',
    'FINITE_RESULT.json', 'map.json', 'projection-reference-only.json', 'REQUEST.txt']}
report['limits'] = ['No semantic predicate or fidelity inference from validation/projection/join',
                    'Token executable is a separately reviewed interpretation; ac.py does not execute it']
(root/'MECHANICAL_RESULT.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
