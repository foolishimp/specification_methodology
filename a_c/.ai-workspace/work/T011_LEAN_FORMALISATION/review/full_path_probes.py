"""Review-only source/runtime comparison and isolated generator tamper controls."""
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

ROOT = Path('/Users/jim/src/apps/specification_methodology')
TENANT = ROOT / 'a_c/build_tenants/lean'
REVIEW = Path(__file__).resolve().parent
FAMILIES = ('objects', 'relations', 'constraints', 'latitude', 'residuals', 'traversals', 'transformations', 'judgments')
results = []


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def record(name, detail):
    results.append({'probe': name, 'result': 'passed', 'detail': detail})


def record_value(index, family, original):
    return {'key': index, 'identity': original['id'], 'family': family,
            'context': original['context'], 'owner': original['owner'],
            'scope': canonical(original['scope']), 'basis': original['basis'],
            'payload': canonical(original)}


actual = json.loads((REVIEW / 'full-path-001/actual-lean-output.log').read_text())
for fixture, label in [('stdo-3.0.2', 'stdo302'), ('toy', 'toy')]:
    raw = (TENANT / 'fixtures' / fixture / 'MODEL.json').read_bytes()
    source = json.loads(raw)
    records = [(family, original) for family in FAMILIES for original in source['populations'][family]]
    envelope = {key: value for key, value in source.items() if key != 'populations'}
    assert len(actual[label]) == len(records)
    all_selected = set()
    for seed, entry in enumerate(actual[label]):
        projection = entry['projection']
        included = projection['included']
        assert projection['seeds'] == [seed]
        assert included == sorted(set(included)) and seed in included
        assert entry['budget'] == len(included)
        assert projection['excluded'] == sorted(set(range(len(records))) - set(included))
        assert projection['parentIdentity'] == source['id']
        assert projection['parentRawSha256'] == hashlib.sha256(raw).hexdigest()
        assert projection['parentCanonicalSha256'] == hashlib.sha256(canonical(source).encode()).hexdigest()
        assert projection['parentEnvelope'] == canonical(envelope)
        assert projection['invalidation'] == canonical(source['interpretation']['invalidation'])
        assert projection['records'] == [record_value(i, *records[i]) for i in included]
        assert projection['unresolved'] == [record_value(i, family, original) for i, (family, original) in enumerate(records)
                                            if family == 'residuals' and i in included]
        assert projection['excludedResiduals'] == [record_value(i, family, original) for i, (family, original) in enumerate(records)
                                                 if family == 'residuals' and i not in included]
        assert entry['underbudgetRefusal'] == 'insufficient record budget; required closure is not truncated'
        all_selected.update(included)
    assert all_selected == set(range(len(records)))
    record(fixture + ': independent actual Lean output-to-raw-source comparison',
           {'projections': len(actual[label]), 'complete_records_exercised': len(all_selected)})

mirror = REVIEW / 'isolated-generator'
assert not mirror.exists(), 'Use a fresh review mirror'
(mirror / 'scripts').mkdir(parents=True)
(mirror / 'AC').mkdir()
for name in ('generate_fixture.py', 'import_fixture.py'):
    shutil.copyfile(TENANT / 'scripts' / name, mirror / 'scripts' / name)
for name in ('Fixture.lean', 'Toy.lean'):
    shutil.copyfile(TENANT / 'AC' / name, mirror / 'AC' / name)
shutil.copytree(TENANT / 'fixtures', mirror / 'fixtures')
env = os.environ | {'PYTHONDONTWRITEBYTECODE': '1'}


def generation(name, expected_exit, expected_text):
    proc = subprocess.run([sys.executable, '-B', str(mirror / 'scripts/generate_fixture.py'), '--check'],
                          cwd=mirror, env=env, text=True, capture_output=True)
    text = proc.stdout + proc.stderr
    (REVIEW / (name + '.log')).write_text(text)
    assert proc.returncode == expected_exit and expected_text in text, text
    record(name, {'exit': proc.returncode, 'matched_message': expected_text})


generation('generator-control', 0, 'source-bound-import-checked')
generated = mirror / 'AC/Fixture.lean'
original_text = generated.read_text()
assert 'Recursive Product boundary' in original_text
generated.write_text(original_text.replace('Recursive Product boundary', 'Changed Product boundary', 1))
generation('generated-payload-tamper', 1, 'Generated Lean Fixture differs from exact checked source import')
generated.write_text(original_text)
raw_model = mirror / 'fixtures/stdo-3.0.2/MODEL.json'
raw_model.write_bytes(raw_model.read_bytes() + b'\n')
generation('raw-fixture-tamper', 1, 'raw fixture digest mismatch: MODEL.json')

lock = json.loads((TENANT / 'toolchain-lock.json').read_text())
archive = lock['lean']['archives'][f'{platform.system()}-{platform.machine()}']['name']
prefix = TENANT / '.toolchain' / archive.removesuffix('.tar.zst')
env['PATH'] = str(prefix / 'bin') + os.pathsep + env.get('PATH', '')
for filename, code, message in [('KernelControls.lean', 0, 'depends on axioms'),
                                ('RejectedDisconnectedCycle.lean', 1, 'is false')]:
    proc = subprocess.run([str(prefix / 'bin/lake'), 'env', 'lean', str(REVIEW / filename)],
                          cwd=TENANT, env=env, text=True, capture_output=True, timeout=60)
    output = proc.stdout + proc.stderr
    (REVIEW / (filename + '.log')).write_text(output)
    assert proc.returncode == code and message in output, output
    assert 'sorryAx' not in output and 'ofReduceBoolCompiler' not in output
    record(filename, {'exit': proc.returncode, 'matched_message': message})

manifest = json.loads((ROOT / 'a_c/.ai-workspace/work/T011_LEAN_FORMALISATION/implementation/SOURCE_MANIFEST.json').read_text())
assert all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest for name, digest in manifest['files'].items())
record('frozen tenant source unchanged', {'files': len(manifest['files'])})
report = {'scope': 'Independent bounded full-path probes; no candidate mutation', 'results': results}
(REVIEW / 'full_path_probe_results.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
