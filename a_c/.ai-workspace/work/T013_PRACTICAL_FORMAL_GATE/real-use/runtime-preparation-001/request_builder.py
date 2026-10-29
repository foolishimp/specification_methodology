#!/usr/bin/env python3
"""Construct one public request from actual prior responses; never execute it."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import prepare_runtime as prep


def artifact(path, operation):
    response = prep.read(path)
    if response.get('schema') != 'a_c.fd-support.response/1' or response.get('operation') != operation or response.get('status') != 'ok':
        raise ValueError('Expected successful actual public ' + operation + ' response')
    reference = response['result']['artifact']
    prep.core.validate_content(reference, 'ArtifactRef')
    return reference, response['result']['value']


def build(runtime, arm, operation, context=None, preflight=None, attempt=None,
          captured=None, stdout_ref=None, after=0, source_ref=None):
    manifest = prep.read(runtime / 'MANIFEST.json')
    if manifest.get('template_only') is not False:
        raise ValueError('Preparation templates cannot create dependent execution requests')
    row = manifest['arms'][arm]
    actor = row['actor_id']
    folder = runtime / arm
    if prep.sha(folder / 'policy.json') != row['policy_sha256']:
        raise ValueError('Selected policy changed')
    if operation == 'context.assemble':
        value = prep.read(folder / 'context.request.json')
        if prep.sha(folder / 'context.request.json') != row['context_request_sha256']:
            raise ValueError('Selected Context request changed')
        return value
    if operation == 'source.read':
        source = prep.read(source_ref)
        prep.core.validate_content(source, 'SourceRef')
        declared = prep.read(folder / 'context.request.json')['arguments']
        refs = [*declared['sources'], *prep.core._all_source_refs(declared['packet']),
                *[m['model']['source'] for m in declared['models']]]
        if source not in refs:
            raise ValueError('Source is not an exact declared Context/model input')
        args = {'source': source, 'encoding': 'utf8'}
    elif operation == 'contract.preflight':
        ctx, _ = artifact(context, 'context.assemble')
        args = {'context': ctx, 'grant_id': 'task', 'executor_id': 'actor',
                'result_key': actor + ':result', 'observations': []}
    elif operation == 'dispatch.start':
        receipt, value = artifact(preflight, 'contract.preflight')
        if value.get('decision') != 'admitted' or value.get('contract_state') != 'admitted':
            raise ValueError('Actual preflight did not admit this call')
        args = {'preflight': receipt}
    elif operation == 'dispatch.observe':
        ref, _ = artifact(attempt, 'dispatch.start')
        args = {'attempt': ref, 'after_event': after}
    elif operation == 'return.capture':
        ref, _ = artifact(attempt, 'dispatch.start')
        payload = prep.read(stdout_ref)
        prep.core.validate_content(payload, 'ArtifactRef')
        contract_ref = prep.read(folder / 'packet.json')['evidence_relations']['return_contract']
        args = {'attempt': ref, 'payload': payload, 'return_contract': contract_ref}
    elif operation == 'return.check':
        ref, _ = artifact(captured, 'return.capture')
        ctx, _ = artifact(context, 'context.assemble')
        args = {'return': ref, 'context': ctx, 'consumer': '/root', 'observations': [], 'predicates': []}
    else:
        raise ValueError('Operation is outside the fixed trial route')
    # Stable input-derived id preserves idempotence; it does not authorize retry.
    identity = actor + ':' + operation + ':' + prep.core.digest(args)[:20]
    return prep.request(identity, operation, args)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime', type=Path, required=True)
    parser.add_argument('--arm', choices=prep.ARMS, required=True)
    parser.add_argument('--operation', required=True)
    for name in ('context', 'preflight', 'attempt', 'captured', 'stdout-ref', 'source-ref'):
        parser.add_argument('--' + name, type=Path)
    parser.add_argument('--after', type=int, default=0)
    args = parser.parse_args()
    value = build(args.runtime, args.arm, args.operation, args.context, args.preflight,
                  args.attempt, args.captured, args.stdout_ref, args.after, args.source_ref)
    sys.stdout.buffer.write(prep.core.canonical(value) + b'\n')


if __name__ == '__main__':
    main()
