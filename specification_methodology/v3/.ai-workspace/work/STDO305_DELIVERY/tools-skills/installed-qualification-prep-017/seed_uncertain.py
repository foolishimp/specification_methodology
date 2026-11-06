"""Seed one real bounded local attempt for a later native-host retry case.

No model call or formal proof is launched. The prior attempt and its uncertainty
must be actually observed; this script never manufactures a reconciliation.
"""
from pathlib import Path
import argparse
import json
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path, required=True)
    args = parser.parse_args()
    case = args.case.absolute(); selected = json.loads(case.read_text())
    if selected['label'] != 'uncertain': raise ValueError('Select only the prepared uncertain case')
    directory = case.parent / 'operator-seed'; directory.mkdir()
    recorder = Path(__file__).with_name('record_public_call.py')
    sequence = 0
    def invoke(operation, arguments=None, existing=None):
        nonlocal sequence
        sequence += 1; label = str(sequence).zfill(3) + '-' + operation
        request_path = existing or directory / (label + '.request.json')
        if existing is None:
            request_path.write_text(json.dumps({'schema': 'a_c.fd-support.request/1', 'id': 'operator-seed-' + str(sequence),
                                               'operation': operation, 'arguments': arguments}) + '\n')
        output = directory / label
        run = subprocess.run([sys.executable, '-B', str(recorder), '--case', str(case), '--request', str(request_path), '--output', str(output)], capture_output=True)
        (directory / (label + '.recorder-stdout')).write_bytes(run.stdout)
        (directory / (label + '.recorder-stderr')).write_bytes(run.stderr)
        response = json.loads((output / 'stdout.json').read_bytes())
        if run.returncode or response['status'] != 'ok': raise ValueError('Actual controlled setup refused; retain ' + str(output))
        return response
    context = invoke('context.assemble', existing=case.parent / 'context-request.json')['result']['artifact']
    admitted = invoke('contract.preflight', {'context': context, 'grant_id': 'work', 'executor_id': 'registered', 'result_key': 'uncertain-seed', 'observations': []})
    if admitted['result']['value']['decision'] != 'admitted': raise ValueError('Controlled attempt was not admitted')
    preflight = admitted['result']['artifact']
    attempt = invoke('dispatch.start', {'preflight': preflight})['result']['artifact']
    deadline = time.monotonic() + 30
    while True:
        observed = invoke('dispatch.observe', {'attempt': attempt, 'after_event': 0})['result']['value']
        if observed['process_end'] is not None and any(e['kind'] == 'effect_observation' for e in observed['events']): break
        if time.monotonic() >= deadline: raise ValueError('Process/effect observation remains incomplete; preserve original attempt')
        time.sleep(0.2)
    if observed['effect']['value'] != 'completion_unknown': raise ValueError('No actually observed uncertainty; do not relabel another outcome')
    count = Path(selected['cwd']) / 'outputs/count'
    if count.read_text() != '1': raise ValueError('Expected exactly one actual bounded receipt effect')
    retry = {'schema': 'a_c.fd-support.request/1', 'id': 'host-selected-single-retry-probe', 'operation': 'dispatch.start',
             'arguments': {'preflight': preflight, 'retry_of': attempt}}
    (case.parent / 'retry-request.json').write_text(json.dumps(retry, indent=2) + '\n')
    (case.parent / 'PRIOR_ATTEMPT.json').write_text(json.dumps({'schema': 'stdo305.actual-uncertain-prior/1', 'attempt': attempt,
        'context': context, 'preflight': preflight, 'observation': observed, 'count': 1,
        'standing': 'Actual controlled process receipt with unknown generic effect completion; no semantic completion or reconciliation asserted.'}, indent=2) + '\n')
    print(json.dumps({'status': 'actual_uncertainty_retained', 'attempt': attempt, 'retry_request': str(case.parent / 'retry-request.json')}))


if __name__ == '__main__': main()
