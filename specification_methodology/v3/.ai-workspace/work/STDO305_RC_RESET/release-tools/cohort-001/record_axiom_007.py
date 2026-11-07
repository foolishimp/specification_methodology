"""Actual prescribed Axiom pair with predeclared qualification input closure."""
from pathlib import Path
import hashlib
import json
import resource
import subprocess
import sys
import time

R = Path('/Users/jim/src/apps/specification_methodology')
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
HERE = Path(__file__).resolve().parent
O = HERE / 'axiom-007'


def ref(p):
    p = Path(p).absolute()
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(p, value):
    with p.open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')


def main():
    b = json.loads((HERE / 'CANDIDATE.json').read_bytes())
    facts = b['components']['representation']['facts']
    prior = Q / 'tools-skills/model-rebind-006/map/execution.json'
    raw = json.loads(prior.read_bytes())
    argv = raw['execution']['argv']
    python = raw['execution']['environment']['python']
    physical = Path(python['executable_realpath'])
    assert Path(sys.executable).samefile(physical)
    assert hashlib.sha256(physical.read_bytes()).hexdigest() == python['sha256']
    assert sys.version == python['version']
    producer = Path(argv[2])
    program, bindings, corpus, mapped = [R / facts[k]['path'] for k in ('program', 'bindings', 'source_corpus', 'map')]
    assert argv == [python['invocation'], '-B', str(producer), 'validate', '--program', str(program), '--bindings', str(bindings), '--emit-map', str(mapped)]
    expected_inputs = [facts[k] for k in ('program', 'bindings', 'source_corpus')]
    assert [ref(p) for p in (program, bindings, corpus)] == expected_inputs
    assert ref(mapped) == facts['map']
    assert ref(producer)['sha256'] == raw['producer']['sha256']
    assert not O.exists()
    O.mkdir()
    plan = {'kind': 'stdo.exact-owner-pair-plan/1', 'predecessor_execution': ref(prior),
            'producer': ref(producer), 'inputs': expected_inputs, 'map_preimage': facts['map'],
            'input_roles': {'direct_owner_argv': [facts['program'], facts['bindings']],
                            'qualification_inventory': facts['source_corpus'],
                            'qualification_inventory_scope': 'Captured and hashed by this recorder before and after each invocation. The owner resolves actual source files via bindings; no assertion that ac.py directly opens source-corpus.json.'},
            'commands': {'map': argv, 'index': argv[:-2]}, 'timeout_seconds': 180,
            'environment': {'python': python}, 'limits': ['Same current owner/program/model/map; no new semantic or installed execution claim.']}
    save(O / 'PLAN.json', plan)
    before = mapped.read_bytes()
    (O / 'logical-constraint-map.preimage.json').write_bytes(before)
    original_stat = mapped.stat()
    for phase in ('map', 'index'):
        out = O / phase
        out.mkdir()
        actual = plan['commands'][phase]
        inputs = [ref(p) for p in (program, bindings, corpus)]
        assert inputs == expected_inputs
        save(out / 'INVOCATION.json', {'plan': ref(O / 'PLAN.json'), 'argv': actual, 'cwd': str(R), 'inputs': inputs,
                                      'input_roles': plan['input_roles'], 'environment': {'python': python}})
        started = time.time_ns()
        usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        with (out / 'stdout.json').open('xb') as stdout, (out / 'stderr.log').open('xb') as stderr:
            process = subprocess.run(actual, cwd=R, stdout=stdout, stderr=stderr, timeout=180)
        ended = time.time_ns()
        after_usage = resource.getrusage(resource.RUSAGE_CHILDREN)
        outputs = [out / 'stdout.json', out / 'stderr.log'] + ([mapped] if phase == 'map' else [])
        observation = {'schema': 'stdo.execution-observation/1', 'producer': ref(producer), 'result': ref(out / 'stdout.json'),
                       'qualification_input_roles': plan['input_roles'],
                       'execution': {'argv': actual, 'cwd': str(R), 'returncode': process.returncode,
                                     'environment': {'python': python}, 'inputs': inputs, 'outputs': [ref(p) for p in outputs],
                                     'stdout': ref(out / 'stdout.json'), 'stderr': ref(out / 'stderr.log'),
                                     'started_ns': started, 'ended_ns': ended, 'elapsed_seconds': (ended-started)/1e9,
                                     'user_seconds': after_usage.ru_utime-usage.ru_utime,
                                     'system_seconds': after_usage.ru_stime-usage.ru_stime}}
        save(out / 'execution.json', observation)
        after_inputs = [ref(p) for p in (program, bindings, corpus)]
        save(out / 'POST_INPUTS.json', {'inputs': after_inputs, 'unchanged': after_inputs == inputs, 'map': ref(mapped)})
        assert process.returncode == 0
        assert after_inputs == inputs and mapped.read_bytes() == before
        result = json.loads((out / 'stdout.json').read_bytes())
        assert result['kind'] == 'axiom-indexer.validation-report' and result['status'] == 'valid' and result['diagnostics'] == []
    end_stat = mapped.stat()
    save(O / 'COMPLETION.json', {'kind': 'stdo.actual-owner-pair-completion/1', 'status': 'passed', 'plan': ref(O / 'PLAN.json'),
                               'map_execution': ref(O / 'map/execution.json'), 'index_execution': ref(O / 'index/execution.json'),
                               'preimage': ref(O / 'logical-constraint-map.preimage.json'), 'map': ref(mapped),
                               'same_bytes': True, 'same_mode': original_stat.st_mode == end_stat.st_mode,
                               'before_mtime_ns': original_stat.st_mtime_ns, 'after_mtime_ns': end_stat.st_mtime_ns,
                               'scope': 'Actual map emission may change mtime. The emitted bytes exactly match the retained preimage; read-only validation is separately recorded. Original006 records are unchanged.'})
    print(json.dumps(ref(O / 'COMPLETION.json'), sort_keys=True))


if __name__ == '__main__':
    main()
