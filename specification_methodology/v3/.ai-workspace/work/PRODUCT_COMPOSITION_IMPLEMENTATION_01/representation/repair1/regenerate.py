"""Repackage the repaired finite authored model using the existing tenant adapter."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import zipfile

REPO = Path(__file__).resolve().parents[7]
BUNDLE = Path(__file__).resolve().parents[1]
CODE = REPO / 'a_c/build_tenants/graphify/code'
sys.path.insert(0, str(CODE))
import ac_generate as adapter

def load(name):
    return json.loads((BUNDLE / name).read_text())

def save(name, value):
    (BUNDLE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

with zipfile.ZipFile(BUNDLE / 'repair1/PRE_REPAIR.zip') as archive:
    def previous(name):
        return json.loads(archive.read(str((BUNDLE/name).relative_to(REPO))))
    prior_model = previous('MODEL.json')
    prior_coverage = previous('COVERAGE.json')

plan, chunk, answer, authoring = [load(name) for name in
    ('PLAN.json', 'SOURCE_SECTIONS.json', 'AUTHOR_ANSWER.json', 'AUTHORING.json')]
assert hashlib.sha256((BUNDLE/'AUTHOR_ANSWER.json').read_bytes()).hexdigest() == authoring['author_answer_sha256']
for path, expected in load('TOOL_PINS.json').items():
    assert hashlib.sha256((REPO/path).read_bytes()).hexdigest() == expected, path
adapter.author_check(answer, chunk)
model, coverage = adapter.model_from_answers(plan, [chunk], {chunk['id']:answer},
    [{'authoring':'AUTHORING.json','sha256':adapter.digest(authoring)}])
# Preserve the original explicit non-CLI producer contract, replacing its authoring pin.
model['id'] = prior_model['id']
model['interpretation'] = prior_model['interpretation']
model['interpretation']['interpreter']['sha256'] = adapter.digest(authoring)
model['interpretation']['provenance'][0]['sha256'] = adapter.digest(authoring)
for key in ('mode', 'interpretation_contract', 'semantic_acceptance', 'authoring', 'whole_method_coverage'):
    coverage[key] = prior_coverage[key]
assert model['interpretation']['contract']['sha256'] == adapter.digest(load('INTERPRETATION_CONTRACT.json'))
save('MODEL.json', model)
save('COVERAGE.json', coverage)
commands=[]
derived = {name:BUNDLE / "repair1" / ("generated-"+name) for name in ("CARRIER.json", "GRAPHIFY_EXTRACTION.json", "RECOVERED.json", "RECOVERED_EXTRACTION.json")}
for args in [
    ['validate', 'MODEL.json'],
    ['materialize', 'MODEL.json', '--out', 'CARRIER.json'],
    ['materialize', 'MODEL.json', '--out', 'GRAPHIFY_EXTRACTION.json', '--extraction'],
    ['decode', 'CARRIER.json', '--out', 'RECOVERED.json'],
    ['decode', 'GRAPHIFY_EXTRACTION.json', '--out', 'RECOVERED_EXTRACTION.json'],
]:
    argv=[sys.executable, '-B', str(CODE/'ac_graph.py')]+[str(derived.get(a, BUNDLE/a)) if a.endswith('.json') else a for a in args]
    done=subprocess.run(argv,text=True,capture_output=True)
    commands.append({'argv':argv,'exit':done.returncode,'stdout':done.stdout,'stderr':done.stderr})
    if done.returncode: raise RuntimeError(done.stderr or done.stdout)
recovered=json.loads(derived['RECOVERED.json'].read_text()); extraction=json.loads(derived['RECOVERED_EXTRACTION.json'].read_text())
assert model == recovered == extraction
for name,path in derived.items(): path.replace(BUNDLE/name)
checks={'author_schema_and_exact_grounding':'passed by existing author_check','declared_sections':len(chunk['segments']),
    'family_counts':{key:len(value) for key,value in model['populations'].items()},
    'outputs_relocated_after_success':'repair1/generated-* replaced the four corresponding current representation artifacts after successful value recovery',
    'recovery_relation':'equal JSON values and canonical model digests; raw serialization-byte equality not claimed',
    'carrier_recovery_equal_json_values':model == recovered,
    'graphify_extraction_recovery_equal_json_values':model == extraction,
    'canonical_model_sha256':adapter.digest(model),'commands':commands,
    'claims':'Bounded source grounding, structural validation and carrier round-trip only; independent semantics and actual upstream Graphify trial separate.'}
save('CHECKS.json', checks)
print(json.dumps({'canonical_model_sha256':adapter.digest(model),'records':sum(checks['family_counts'].values()),'recovered_equal_json_values':True}))
