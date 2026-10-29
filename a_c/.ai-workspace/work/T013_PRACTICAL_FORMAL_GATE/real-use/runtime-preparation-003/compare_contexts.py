#!/usr/bin/env python3
"""Check actual contexts against selected sources; pure, no proof or actor call."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import prepare_runtime as prep


def compare(runtime_path, paths):
    manifest = prep.read(runtime_path / 'MANIFEST.json')
    if manifest.get('template_only') is not False:
        raise ValueError('Actual comparison requires a finalized selected runtime')
    view = prep.read(prep.PREP / 'shared/model-view.json')
    delivered = {}
    observations = {}
    for arm in prep.ARMS:
        folder = runtime_path / arm
        policy = folder / 'policy.json'
        row = manifest['arms'][arm]
        if prep.sha(policy) != row['policy_sha256']:
            raise ValueError('Policy changed')
        runtime = prep.core.Runtime.from_policy(policy, prep.sha(policy), 'executive')
        request = prep.read(folder / 'context.request.json')
        if prep.sha(folder / 'context.request.json') != row['context_request_sha256']:
            raise ValueError('Context request changed')
        # Existing pure Core regenerates the expected complete rendering. This
        # does not execute effects, retain artifacts, invoke Lean, or admit work.
        outcome = prep.core.execute_read(runtime, request)
        if outcome.get('refusal') is not None:
            raise ValueError('Current pure Context construction refused: ' + str(outcome['refusal']))
        expected = [a['payload'] for a in outcome['artifacts'] if a['kind'] == 'context']
        if len(expected) != 1:
            raise ValueError('Expected one exact pure Context')
        actual = prep.read(paths[arm])
        if actual.get('kind') == 'context':
            actual = actual['payload']
        text = actual['rendered_utf8']
        digest = hashlib.sha256(text.encode()).hexdigest()
        if digest != actual['rendered_sha256'] or text != expected[0]['rendered_utf8']:
            raise ValueError('Actual rendering differs from complete current selected construction')
        if len(actual['projections']) != 1 or actual['projections'][0]['views'] != view:
            raise ValueError('Actual view is not the frozen exact 29-record selection')
        shared = {}
        other = []
        for source in actual['sources']:
            ref = source['source']
            if ref['root'] == 'prepared':
                shared[ref['path']] = (source['selected_sha256'], source['size_bytes'], source['content_base64'])
            else:
                other.append({'source': ref, 'selected_sha256': source['selected_sha256'],
                              'purpose': 'Exact preselected Product/owner/activation/return/selection metadata'})
        delivered[arm] = shared
        observations[arm] = {'rendered_sha256': digest, 'rendered_bytes': len(text.encode()),
                             'exact_selected_construction_matches': True, 'nonshared_sources': other,
                             'formal_required': 'formal_gate' in actual}
    if delivered['ungated'] != delivered['gated']:
        raise ValueError('Substantive source bytes differ between arms')
    if observations['ungated']['formal_required'] or not observations['gated']['formal_required']:
        raise ValueError('Required-gate difference is not the selected experiment')
    return {'schema': 't013.actual-context-comparison/1', 'substantive_sources_equal': True,
            'exact_view_equal': True, 'arms': observations,
            'limits': ['Pure source/current-rendering comparison only; actual helper forwarding must also match these digests.',
                       'Hidden host/provider context and semantic adequacy are not established.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime', type=Path, required=True)
    parser.add_argument('--ungated-context', type=Path, required=True)
    parser.add_argument('--gated-context', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(compare(args.runtime, {'ungated': args.ungated_context, 'gated': args.gated_context}), indent=2))
