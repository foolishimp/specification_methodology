"""Serialize only explicit, exact-subject judgments returned by the actual actor."""
from pathlib import Path
import hashlib
import json
import re
import sys

BASE = Path(__file__).resolve().parent
stage = BASE / (sys.argv[1] if len(sys.argv) > 1 else 'semantic-01')
assert stage.resolve().is_relative_to(BASE)
report_path = stage / 'ASSESSMENT.md'
report = report_path.read_text()
execution = json.loads((stage / 'EXECUTION.json').read_text())
assert execution['invocation']['exit_code'] == 0 and execution['result']['subtype'] == 'success'
assert not execution['observed_tool_uses'], 'Review actual tool use before admitting the output.'
assert hashlib.sha256(report_path.read_bytes()).hexdigest() == execution['report_sha256']
objects = []
for fragment in re.findall(r'```json\s*(.*?)```', report, flags=re.S):
    try:
        value = json.loads(fragment)
    except ValueError:
        continue
    if isinstance(value, dict) and isinstance(value.get('subjects'), list):
        objects.append(value)
assert len(objects) == 1, 'Require one unambiguous actor-supplied subject verdict object.'
verdict = objects[0]
freeze = json.loads((BASE.parent / 'context/SEMANTIC_FREEZE.json').read_text())
query_map = {row['name']: row for row in freeze['identities']['queries']}
index_map = {}
for row in freeze['identities']['indexes']:
    purpose = json.loads((Path(row['index_path']).parent / 'PURPOSE.json').read_text())
    index_map[purpose['id']] = row
subjects = {row['name']: row for row in verdict['subjects']}
assert len(subjects) == len(verdict['subjects']), 'Duplicate query judgments.'
assert set(subjects) == set(query_map), 'Every requested exact query needs its explicit returned status.'
for name, row in subjects.items():
    query = query_map[name]
    index = index_map[query['purpose_id']]
    assert row['index_sha256'] == index['canonical_index_sha256'], (name, 'index')
    assert row['corpus_sha256'] == index['corpus_sha256'], (name, 'corpus')
    assert row['query_sha256'] == query['canonical_query_sha256'], (name, 'query')
    assert row['status'] in {'supported', 'falsified', 'unknown'}, name
    assert isinstance(row['evaluator'], str) and row['evaluator'].strip()
    assert isinstance(row['evidence'], list) and row['evidence'] and all(isinstance(x, str) and x.strip() for x in row['evidence'])
    assert isinstance(row['scope'], str) and row['scope'].strip()
    if name.endswith('-boundary'):
        assert row['status'] != 'supported', 'No delivered context exists for an unknown-family refusal.'

destination = stage / 'assessments'
destination.mkdir(exist_ok=False)
keys = ['index_sha256', 'corpus_sha256', 'query_sha256', 'status', 'evaluator', 'evidence']
serialized, withheld, references = [], [], []
for name, row in subjects.items():
    if row['status'] != 'supported':
        withheld.append({'name': name, 'status': row['status'], 'scope': row['scope']})
        continue
    envelope = {key: row[key] for key in keys}
    if envelope['evaluator'] == 'as above':
        # Resolve the actor's explicit unambiguous backward reference. The raw
        # report and parsed verdict retain the original wording unchanged.
        first = verdict['subjects'][0]['evaluator']
        assert first != 'as above'
        envelope['evaluator'] = first
        references.append({'name': name, 'field': 'evaluator', 'original': 'as above',
                           'resolved_from': 'subjects[0].evaluator', 'value': first})
    path = destination / (name + '.json')
    path.write_text(json.dumps(envelope, indent=2) + '\n')
    serialized.append({'name': name, 'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                       'scope': row['scope'], 'source_status': row['status']})
(stage / 'VERDICT.json').write_text(json.dumps(verdict, indent=2) + '\n')
record = {'kind': 'stdo.rc2.actual-assessor-envelope-serialization/1',
          'report': str(report_path), 'report_sha256': execution['report_sha256'],
          'actual_actor_session': execution['init']['session_id'], 'actual_actor_model': execution['init']['model'],
          'source_packet_sha256': execution['invocation']['stdin_sha256'],
          'serialized_supported': serialized, 'withheld': withheld,
          'explicit_reference_resolutions': references,
          'operation': 'Extraction of the six runtime fields from explicit actual Claude same-subject supported verdicts; evaluator as-above references are expanded to their exact first-item text and recorded. No operator status invention, evidence addition or scope strengthening.'}
(stage / 'SERIALIZATION.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'supported': [x['name'] for x in serialized], 'withheld': withheld,
                  'verdict': str(stage / 'VERDICT.json')}))
