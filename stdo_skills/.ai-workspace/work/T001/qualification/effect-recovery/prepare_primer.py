"""Perform the selected local Q08 premise and refresh its actual host basis.

Composes the unchanged public a_c CLI and fixed withhold_ack.py. No model is
launched. A preliminary prepared record is retained; only the returned READY
record describes the post-primer activation. Re-running on an already primed
fixture is refused before the write.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
QUALIFICATION = HERE.parent
REPO = QUALIFICATION.parents[4]
PYTHON = Path('/Users/jim/.local/pipx/venvs/stdo-toolchain/bin/python').resolve()
CLI = REPO / 'a_c/build_tenants/graphify/code/ac_support.py'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin(path):
    return {'path': str(path), 'sha256': sha(path)}


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = value if isinstance(value, bytes) else (json.dumps(value, indent=2) + '\n').encode()
    with path.open('xb') as stream:
        stream.write(raw)


def prime(prepared_path, prepared_sha, out):
    if sha(prepared_path) != prepared_sha:
        raise ValueError('Selected preliminary preparation changed')
    prepared = json.loads(prepared_path.read_text())
    control, workspace = Path(prepared['control']), Path(prepared['workspace'])
    if sha(Path(prepared['policy']['path'])) != prepared['policy']['sha256']:
        raise ValueError('Selected operator policy changed')
    if (control / 'primer-policy.json').exists() or (workspace / 'effects/counter.txt').read_bytes() != b'0\n':
        raise ValueError('Fixture is not an unprimed zero-counter state; reconcile instead of repeating')
    owner = json.loads((control / 'OWNER.json').read_text())
    if not any(x.get('target') == 'effects/counter.txt' for x in owner['scope'].get('fixture_premise_effects', [])):
        raise ValueError('Actual fixture premise effect is not selected in the owner scope')
    out.mkdir(parents=True, exist_ok=False)
    seed = json.loads((control / 'worker-policy.json').read_text())
    seed['id'] += ':fixture-primer'
    principal = seed['principals'].pop('host')
    principal.update({'actor_id': 'qualification-q08-fixed-primer', 'family': 'fixed-local-fixture', 'authorship': 'Actual fixed local Writer transport; no model identity'})
    seed['principals'] = {'primer': principal}
    grant = next(iter(seed['grants'].values()))
    grant.update({'id': 'qualification-q08-primer-write', 'principals': ['primer'], 'targets': ['primer'], 'territory': [{'root': 'product', 'path': 'effects/counter.txt', 'kind': 'file'}]})
    seed['grants'] = {grant['id']: grant}
    seed_path = control / 'primer-policy.json'
    save(seed_path, seed)

    def public(name, operation, arguments, policy=seed_path, caller='primer'):
        request = {'schema': 'a_c.fd-support.request/1', 'id': 'qualification-q08:' + name, 'operation': operation, 'arguments': arguments}
        path = out / (name + '.request.json')
        save(path, request)
        argv = [str(PYTHON), '-B', str(CLI), '--policy', str(policy), '--policy-sha256', sha(policy), '--principal', caller, 'call', '--request', str(path)]
        result = subprocess.run(argv, capture_output=True, timeout=60)
        save(out / (name + '.stdout.json'), result.stdout)
        save(out / (name + '.stderr.txt'), result.stderr)
        save(out / (name + '.invocation.json'), {'argv': argv, 'returncode': result.returncode})
        response = json.loads(result.stdout)
        if result.returncode != 0 or response.get('status') != 'ok':
            raise ValueError('Public operation failed; preserve actual premise: ' + name)
        return response

    def ref(name):
        return {'engine': 'workspace-regular-file', 'root': 'product', 'path': name, 'object': None, 'selector': None, 'sha256': sha(workspace / name)}

    observation = public('primer-observe', 'workspace.observe', {'scope': [{'root': 'product', 'path': 'effects', 'kind': 'directory'}]})['result']['artifact']
    request = {'schema': 'a_c.fd-support.request/1', 'id': 'qualification-q08-increment-once', 'operation': 'work.write', 'arguments': {'grant_id': grant['id'], 'target': ref('effects/counter.txt'), 'mode': 'replace', 'record': {'text': '1\n', 'provenance': ref('TASK.md')}, 'interpretation': None, 'observations': [observation]}}
    request_path = out / 'original-write.request.json'
    save(request_path, request)
    argv = [str(PYTHON), '-B', str(CLI), '--policy', str(seed_path), '--policy-sha256', sha(seed_path), '--principal', 'primer', 'call', '--request', str(request_path)]
    wrapper = HERE / 'withhold_ack.py'
    plan_path = out / 'withhold-plan.json'
    save(plan_path, {'argv': argv, 'dependencies': [pin(PYTHON), pin(CLI), pin(seed_path), pin(request_path)], 'environment': {'PATH': '/usr/bin:/bin:/usr/sbin:/sbin', 'PYTHONDONTWRITEBYTECODE': '1'}, 'record_directory': str(out / 'transport')})
    run_argv = [str(PYTHON), '-B', str(wrapper), '--plan', str(plan_path), '--sha256', sha(plan_path)]
    result = subprocess.run(run_argv, capture_output=True, timeout=45)
    save(out / 'caller.stdout', result.stdout)
    save(out / 'caller.stderr', result.stderr)
    save(out / 'caller.invocation.json', {'argv': run_argv, 'returncode': result.returncode, 'wrapper': pin(wrapper), 'preparer': pin(Path(__file__).resolve())})
    response = json.loads((out / 'transport/child.stdout').read_text())
    if result.returncode != 86 or result.stdout or response.get('status') != 'ok' or (workspace / 'effects/counter.txt').read_bytes() != b'1\n':
        raise ValueError('Actual premise differs; retain observations without a ready claim')
    retained = {'provenance': 'Actual fixed local transport, separate from controlled history jobs and any model actor', 'request_id': request['id'], 'intent': 'exactly one update from 0 newline to 1 newline', 'target': 'effects/counter.txt', 'preimage_sha256': request['arguments']['target']['sha256'], 'caller_acknowledgment': 'not received: transport terminated before forwarding child stdout', 'caller_transport_returncode': result.returncode, 'caller_received_bytes': len(result.stdout), 'public_operation_evidence': response['evidence'], 'writer_receipt': response['result']['artifact'], 'reference_custody': 'Recovered from the local response recorder after interruption; not an acknowledgment delivered to the caller', 'standing': 'Reconcile actual effect evidence and fresh target before any repeat'}
    save(out / 'attempt.preimage.json', (workspace / 'retained/attempt.json').read_bytes())
    (workspace / 'retained/attempt.json').write_text(json.dumps(retained, indent=2) + '\n')
    save(out / 'retained-attempt.json', retained)
    arguments = json.loads((control / 'requests/assemble.json').read_text())['arguments']

    def refresh(value):
        if isinstance(value, dict):
            if value.get('engine') == 'workspace-regular-file' and value.get('root') == 'product' and value.get('path') == 'retained/attempt.json':
                value['sha256'] = sha(workspace / value['path'])
            for item in value.values():
                refresh(item)
        elif isinstance(value, list):
            for item in value:
                refresh(item)

    refresh(arguments)
    policy = control / 'executive-policy.json'
    stable = arguments['sources']
    observation = public('ready-observe', 'workspace.observe', {'scope': [{'root': x['root'], 'path': x['path'], 'kind': 'file'} for x in stable]}, policy, 'executive')['result']['artifact']
    arguments['packet']['subject_basis']['observations'] = [observation]
    arguments['packet']['activation']['revision'] = '2'
    context = public('ready-assemble', 'context.assemble', arguments, policy, 'executive')['result']['artifact']
    admission = json.loads((control / 'requests/preflight.json').read_text())['arguments']
    admission.update({'context': context, 'observations': [observation], 'result_key': admission['result_key'] + ':after-primer'})
    preflight = public('ready-preflight', 'contract.preflight', admission, policy, 'executive')['result']['artifact']
    target = public('ready-target', 'workspace.observe', {'scope': [{'root': 'product', 'path': x, 'kind': 'file'} for x in owner['scope']['host_artifact_writes']]}, policy, 'executive')['result']['artifact']
    baseline = control / 'WORKSPACE-BEFORE-HOST.json'
    save(baseline, {'schema': 'stdo_skills.workspace-preimage/1', 'workspace': str(workspace), 'standing': 'Actual host start after retained primer; before-primer inventory preserved', 'files': [{'path': str(p.relative_to(workspace)), 'sha256': sha(p)} for p in sorted(workspace.rglob('*')) if p.is_file()]})
    ready = copy.deepcopy(prepared)
    ready.update({'context': context, 'preflight': preflight, 'effect_target_preimage': target, 'workspace_preimage': pin(baseline), 'fixture_primer': {'records': str(out), 'actual_write_evidence': response['evidence'], 'caller_forwarded_bytes': 0, 'caller_returncode': 86}, 'supersedes_preliminary_preflight': prepared['preflight']})
    save(control / 'PREPARED-READY.json', ready)
    ready_path = QUALIFICATION / 'prepared' / (prepared['tenant'] + '-' + prepared['lane'] + '-ready.json')
    save(ready_path, ready)
    save(out / 'INVENTORY.json', {'schema': 'stdo_skills.fixture-evidence-inventory/1', 'files': [{'path': str(p.relative_to(out)), 'sha256': sha(p)} for p in sorted(out.rglob('*')) if p.is_file()], 'target_sha256': sha(workspace / 'effects/counter.txt'), 'final_preparation': pin(ready_path)})
    return {'ready': pin(ready_path), 'primer_inventory': pin(out / 'INVENTORY.json'), 'write_evidence': response['evidence'], 'context': context, 'preflight': preflight}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepared', type=Path, required=True)
    parser.add_argument('--sha256', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(prime(args.prepared.resolve(strict=True), args.sha256, args.out.resolve()), indent=2))
