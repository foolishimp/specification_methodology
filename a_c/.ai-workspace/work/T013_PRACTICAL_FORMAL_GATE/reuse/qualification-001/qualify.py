"""Bounded T013 qualification launcher; production code is loaded unchanged.

Only Q and the reviewed public init-origin/cold-success path may write. No
private entry body or key is read by this launcher or placed in its evidence.
"""
from pathlib import Path
import copy
import hashlib
import json
import os
import platform
import resource
import sys
import time
import types
from datetime import datetime, timezone

Q = Path(__file__).resolve().parent
BASE = Q.parents[1]
AC = BASE.parents[2]
ROOT = AC / 'build_tenants/lean'
PYTHON = Path('/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12')
PYTHON_SHA = 'a7f5b535d61d1c7326824204ac80f045a97a652abb154421e2c74fcc365a3539'
BASELINE_ID = '07f423004952338c7ce4273e2fe1f17556b0c96803caa4a355859762750e9601'
ORIGIN_PIN = '.cache/formal-origin-v1/selection.json'
SMALL = BASE.parent / 'T012_FORMAL_GATE/runtime/qualification-002/carrier-with-actual-view'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def write(name, value):
    path = Q / name
    with path.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write('\n')


def load_module(name, path):
    module = types.ModuleType(name)
    module.__file__ = str(path)
    module.__package__ = ''
    sys.modules[name] = module
    raw = path.read_bytes()
    exec(compile(raw, str(path), 'exec', dont_inherit=True), module.__dict__)
    return module


def adapter():
    assert Path(sys.executable).resolve() == PYTHON.resolve()
    assert sha(PYTHON) == PYTHON_SHA
    return load_module('qualification_adapter', AC / 'build_tenants/graphify/code/ac_formal_gate.py')


def origin_counts():
    store = ROOT / '.cache/formal-origin-v1'
    if not store.exists():
        return {'present': False, 'entries': [], 'entry_count': 0, 'pending_count': 0}
    # Metadata only. Public entry identifiers are hashes already exposed by hints.
    names = sorted(p.name for p in (store / 'entries').iterdir())
    assert all(len(n) == 69 and n.endswith('.json') and all(c in '0123456789abcdef' for c in n[:-5]) for n in names)
    return {'present': True, 'entries': names, 'entry_count': len(names),
            'pending_count': len(list((store / 'pending').iterdir()))}


def invoke(a, config, label, args):
    before = origin_counts()
    record = {'schema': 'a_c.T013.public-invocation/1', 'label': label,
              'started_utc': datetime.now(timezone.utc).isoformat(),
              'expected_argv': [str(PYTHON), '-I', '-S', '-B', '-X', 'pycache_prefix=' + os.devnull,
                                str(ROOT / 'scripts/formal_gate.py'), *args],
              'outer_seconds': 600, 'checking_seconds': 90, 'lean_memory_mb': 4096,
              'physical_rss_cap': False, 'origin_before': before,
              'rss_scope': 'Darwin bytes: launcher self peak and cumulative peak over reaped children of this isolated launcher invocation; child peak is not stage-attributed.'}
    started = time.monotonic()
    try:
        process = a._invoke(config, args)
        record['external_invocation_seconds'] = time.monotonic() - started
        record['returncode'] = process.returncode
        (Q / (label + '.stdout')).write_bytes(process.stdout)
        (Q / (label + '.stderr')).write_bytes(process.stderr)
        record['stdout_sha256'] = sha(Q / (label + '.stdout'))
        record['stderr_sha256'] = sha(Q / (label + '.stderr'))
        result = a._json(process.stdout)
        record['returned'] = result
        record['status'] = result.get('status', 'setup-returned')
    except Exception as exc:
        record['external_invocation_seconds'] = time.monotonic() - started
        record['status'] = 'launcher-error'
        record['error'] = type(exc).__name__ + ': ' + str(exc)
        result = None
    record['finished_utc'] = datetime.now(timezone.utc).isoformat()
    record['origin_after'] = origin_counts()
    record['parent_high_water_rss_bytes'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    record['child_high_water_rss_bytes'] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    record['measurement_scope'] = 'From before reviewed adapter validation/launch through complete CLI exit and publication; excludes writing this qualification receipt.'
    write(label + '.external.json', record)
    print(json.dumps({k: record.get(k) for k in ('label', 'status', 'returncode', 'external_invocation_seconds',
                                               'parent_high_water_rss_bytes', 'child_high_water_rss_bytes',
                                               'origin_before', 'origin_after', 'error')}, sort_keys=True))
    return record, result


def baseline():
    a = adapter()
    assert not origin_counts()['present'], 'Unexpected existing production origin; no repair permitted'
    pin_record = json.loads((BASE / 'reuse/integration-001/SOURCE-PINS.json').read_text())
    for group in ('after', 'conserved_source_pins'):
        for name, digest in pin_record[group].items():
            assert sha(AC / name) == digest, name
    config = a.select_checker(ROOT, PYTHON, 600)
    assert config['runtime_identity']['sha256'] == BASELINE_ID
    assert ORIGIN_PIN not in config['runtime_identity']['pins']
    load_module('runtime_process', ROOT / 'scripts/runtime_process.py')
    support = load_module('formal_support', ROOT / 'scripts/formal_support.py')
    started = time.monotonic()
    checked = support.check()
    write('BASELINE.json', {'schema': 'a_c.T013.qualification-baseline/1',
          'recorded_utc': datetime.now(timezone.utc).isoformat(),
          'integration_source_pins_sha256': sha(BASE / 'reuse/integration-001/SOURCE-PINS.json'),
          'all_integrated_and_conserved_pins_match': True,
          'runtime_identity': config['runtime_identity'], 'python': config['python'],
          'support': checked, 'support_check_seconds': time.monotonic() - started,
          'support_established': False, 'origin': origin_counts()})
    write('baseline-checker.json', config)
    print(json.dumps({'baseline': config['runtime_identity']['sha256'], 'support': checked, 'origin': origin_counts()}))


def initialize():
    a = adapter()
    config = json.loads((Q / 'baseline-checker.json').read_text())
    assert not origin_counts()['present'], 'Explicit init is allowed only once, with absent store'
    record, selected = invoke(a, config, 'init-origin', ['init-origin'])
    assert record.get('returncode') == 0 and selected is not None, 'Origin setup failed; stop'
    current = a.select_checker(ROOT, PYTHON, 600)
    public_pins = {k: v for k, v in current['runtime_identity']['pins'].items() if k != ORIGIN_PIN}
    assert public_pins == config['runtime_identity']['pins']
    assert ORIGIN_PIN in current['runtime_identity']['pins']
    assert origin_counts()['entry_count'] == origin_counts()['pending_count'] == 0
    write('checker.json', current)
    write('RUNTIME-IDENTITY.json', current['runtime_identity'])
    write('ORIGIN-SELECTION.json', {'schema': 'a_c.T013.qualification-origin-selection/1',
          'created_only_by': 'reviewed public init-origin', 'public_setup_response': selected,
          'runtime_identity_sha256': current['runtime_identity']['sha256'],
          'origin_selection_pin': current['runtime_identity']['pins'][ORIGIN_PIN],
          'checker_sha256': sha(Q / 'checker.json'),
          'runtime_identity_file_sha256': sha(Q / 'RUNTIME-IDENTITY.json'),
          'private_entry_bodies_or_key_retained': False, 'origin_counts': origin_counts()})
    request = json.loads((SMALL / 'replay-request.json').read_text())
    request['input']['path'] = str(SMALL / 'input.json')
    request['supplied_views']['path'] = str(SMALL / 'supplied-views.json')
    request['context_binding']['activation_identity']['trial_ordinal'] = 1
    assert sha(SMALL / 'input.json') == request['input']['raw_sha256']
    assert sha(SMALL / 'supplied-views.json') == request['supplied_views']['raw_sha256']
    write('small-request.json', request)
    print(json.dumps({'runtime_identity': current['runtime_identity']['sha256'],
                     'checker_sha256': sha(Q / 'checker.json'),
                     'runtime_identity_file_sha256': sha(Q / 'RUNTIME-IDENTITY.json'),
                     'nonsecret_origin_id': selected['origin_id'], 'entry_count': 0}))


def run(label, args):
    a = adapter()
    selection = json.loads((Q / 'ORIGIN-SELECTION.json').read_text())
    config = a.load_config(Q / 'checker.json', selection['checker_sha256'])
    record, result = invoke(a, config, label, args)
    if result is None:
        raise SystemExit(1)
    if '--output' in args:
        directory = Path(args[args.index('--output') + 1])
        if directory.is_dir() and (directory / 'result.json').is_file():
            retained = json.loads((directory / 'result.json').read_text())
            assert retained == result, 'Returned and retained public result differ'
    expected_exit = a.EXITS.get(result.get('status'))
    assert record.get('returncode') == expected_exit, 'Public exit/status mismatch'
    if result.get('status') not in ('verified', 'refused'):
        raise SystemExit(1)


if __name__ == '__main__':
    assert platform.system() == 'Darwin', 'Recorded RSS units require explicit host scope'
    command = sys.argv[1]
    if command == 'baseline':
        baseline()
    elif command == 'initialize':
        initialize()
    elif command == 'run':
        run(sys.argv[2], sys.argv[3:])
    else:
        raise SystemExit('Unknown qualification action')
