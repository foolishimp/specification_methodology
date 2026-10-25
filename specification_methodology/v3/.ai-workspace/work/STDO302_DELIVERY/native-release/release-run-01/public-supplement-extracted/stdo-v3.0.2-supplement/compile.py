"""Compile already-authored bounded choices with the existing a_c adapter."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

BUNDLE = Path(__file__).resolve().parent
REPO = BUNDLE.parents[5]
CODE = REPO / 'a_c/build_tenants/graphify/code'
sys.path.insert(0, str(CODE))
import ac_generate as adapter

def load(name):
    return json.loads((BUNDLE / name).read_text())

def save(name, value):
    (BUNDLE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for path, expected in load('TOOL_PINS.json').items():
    assert sha(REPO/path) == expected, path
plan, chunk, answer, authoring, contract = [load(name) for name in
    ('PLAN.json', 'SOURCE_SECTIONS.json', 'AUTHOR_ANSWER.json', 'AUTHORING.json', 'INTERPRETATION_CONTRACT.json')]
assert sha(BUNDLE/'AUTHOR_ANSWER.json') == authoring['author_answer_sha256']
assert sha(REPO/authoring['authority_record']) == authoring['authority_record_sha256']
for row in plan['files']:
    assert sha(REPO/row['source_path']) == row['sha256']
    assert sha(BUNDLE/'source'/row['path']) == row['sha256']
for segment in chunk['segments']:
    lines=(BUNDLE/'source'/segment['path']).read_text().splitlines(keepends=True)
    assert ''.join(lines[segment['start_line']-1:segment['end_line']]) == segment['text']
    assert hashlib.sha256(segment['text'].encode()).hexdigest() == segment['sha256']
adapter.author_check(answer, chunk)
model, coverage = adapter.model_from_answers(plan, [chunk], {chunk['id']: answer},
    [{'authoring': 'AUTHORING.json', 'sha256': adapter.digest(authoring)}])
# The adapter packages choices; this real Writer supplied them, not a CLI actor.
model['id'] = 'urn:stdo:3.0.2:composition-release:interpretation:1'
model['interpretation']['contract']['sha256'] = adapter.digest(contract)
model['interpretation']['interpreter'] = {'id': 'urn:stdo:3.0.2:interpreter:current-writer', 'sha256': adapter.digest(authoring)}
model['interpretation']['authority']['sha256'] = authoring['authority_record_sha256']
model['interpretation']['provenance'] = [
    {'id':'urn:stdo:3.0.2:authoring-record','sha256':adapter.digest(authoring)},
    {'id':'urn:stdo:3.0.2:plan','sha256':adapter.digest(plan)}]
coverage.update(mode='manual-bounded-authoring', interpretation_contract='INTERPRETATION_CONTRACT.json',
    semantic_acceptance='pending independent exact-source review', authoring='AUTHORING.json',
    whole_method_coverage='not claimed; prior whole-method interpretation remains incomplete')
save('MODEL.json', model); save('COVERAGE.json', coverage)
commands=[]
for args in [
    ['validate','MODEL.json'],
    ['materialize','MODEL.json','--out','CARRIER.json'],
    ['materialize','MODEL.json','--out','GRAPHIFY_EXTRACTION.json','--extraction'],
    ['decode','CARRIER.json','--out','RECOVERED.json'],
    ['decode','GRAPHIFY_EXTRACTION.json','--out','RECOVERED_EXTRACTION.json']]:
    argv=[sys.executable,'-B',str(CODE/'ac_graph.py')]+[str(BUNDLE/a) if a.endswith('.json') else a for a in args]
    result=subprocess.run(argv,text=True,capture_output=True)
    commands.append({'argv':argv,'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    if result.returncode: raise RuntimeError(result.stderr or result.stdout)
assert model == load('RECOVERED.json') == load('RECOVERED_EXTRACTION.json')
checks={'scope':'Ten selected sections; five active statement families; no operation execution or semantic acceptance',
    'source_sections':len(chunk['segments']),'family_counts':{k:len(v) for k,v in model['populations'].items()},
    'grounding':'actual author_check and complete exact line-span comparison against pinned source files passed',
    'recovery_relation':'equal JSON values and canonical model digest; raw serialization-byte equality not claimed',
    'canonical_model_sha256':adapter.digest(model),'commands':commands}
save('CHECKS.json',checks)
print(json.dumps({'sections':len(chunk['segments']),'records':sum(checks['family_counts'].values()),'canonical_model_sha256':adapter.digest(model),'recovery':True}))
