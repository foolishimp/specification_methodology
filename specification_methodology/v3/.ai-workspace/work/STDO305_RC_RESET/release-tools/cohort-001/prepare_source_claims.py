"""Bind closed source operations without changing their raw observations."""
from pathlib import Path
import copy
import hashlib
import json

R = Path('/Users/jim/src/apps/specification_methodology')
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W = Q / 'release-tools'
O = W / 'cohort-001/source-claims'


def read(path):
    return json.loads(path.read_bytes())


def ref(path):
    raw = path.read_bytes()
    return {'path': path.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(name, value):
    p = O / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')
    return ref(p)


def normalize(value):
    if isinstance(value, dict):
        result = {k: normalize(v) for k, v in value.items()}
        if {'path', 'sha256'} <= set(result):
            p = Path(result['path'])
            if p.is_absolute():
                result['path'] = p.relative_to(R).as_posix()
        return result
    if isinstance(value, list):
        return [normalize(v) for v in value]
    return value


def main():
    assert not O.exists()
    O.mkdir()
    candidate = read(W / 'cohort-001/CANDIDATE.json')
    subjects = {k: v['subject']['sha256'] for k, v in candidate['products'].items()}
    facts = candidate['components']['representation']['facts']
    semantic = read(R / candidate['source']['path'])
    corpus = read(R / facts['source_corpus']['path'])
    prefix = 'stdo_representation/' + facts['source_copy_prefix'].rstrip('/') + '/'
    current = {prefix + row['path']: row for row in semantic['members'] + semantic['native_contracts']}
    uri = semantic['basis_uri']
    expected = {uri + row['path']: row['sha256'] for row in current.values()}
    assert {row['uri']: row['sha256'] for row in corpus['source_files']} == expected
    observed = read(Q / 'tools-skills/model-rebind-006/map/stdout.json')
    resolved = {}
    for row in observed['resolved_sources']:
        key = row['uri'].split('#', 1)[0]
        sha = row['sha256'].removeprefix('sha256:')
        assert key not in resolved or resolved[key] == sha
        resolved[key] = sha
    assert resolved == expected
    inventory_refs = [{'path': path, 'sha256': row['sha256'], 'bytes': row['bytes']} for path, row in sorted(current.items())]
    closure = save('AXIOM_INPUT_CLOSURE.json', {
        'kind': 'stdo.derived-execution-input-closure/1',
        'basis': 'The original recorder directly pins program and bindings. The owner validation stdout independently lists the resolved source URIs and digests. This derivative joins those 68 exact sources to their selected qualification inventory; it does not assert that ac.py opened source-corpus.json.',
        'original_map_execution': ref(Q / 'tools-skills/model-rebind-006/map/execution.json'),
        'original_index_execution': ref(Q / 'tools-skills/model-rebind-006/index/execution.json'),
        'actual_validation_stdout': ref(Q / 'tools-skills/model-rebind-006/map/stdout.json'),
        'owner': ref(R / 'axiom_indexer/build_tenants/core/code/ac.py'),
        'owner_routes': ['Resolver:136-187', 'validate_program:262', 'main:965-994'],
        'qualification_inventory': facts['source_corpus'],
        'semantic_source': candidate['source'],
        'resolved_source_count': len(resolved),
        'resolved_sources': inventory_refs,
        'limitations': ['No syscall trace or new execution is claimed.', 'The qualification inventory is a derived dependency description, not a directly recorded owner argument.'],
    })
    refs = {}
    for name, directory in [('source_current_map', 'map'), ('current_index_validation', 'index')]:
        path = Q / 'tools-skills/model-rebind-006' / directory / 'execution.json'
        raw = read(path)
        value = normalize(copy.deepcopy(raw))
        assert value['execution']['returncode'] == 0
        assert value['execution']['argv'] == raw['execution']['argv']
        assert value['execution']['environment'] == raw['execution']['environment']
        recorded = copy.deepcopy(value['execution']['inputs'])
        value['execution']['inputs'] += [facts['source_corpus'], *inventory_refs]
        value.update({
            'kind': 'stdo.cohort-evidence/1', 'category': 'execution', 'claim': name, 'status': 'passed',
            'source_identity_sha256': candidate['source']['source_identity_sha256'],
            'subjects': {k: subjects[k] for k in ['axiom_indexer', 'stdo_representation']},
            'provenance': {'original_execution': ref(path), 'original_direct_inputs': recorded, 'derived_input_closure': closure,
                           'derivation': 'Retained artifact references are repository-relative. Exact argv, interpreter, stdout, stderr, result and operation timings remain the original observations; the separately identified qualification inventory and resolved-source closure are derived above.'},
            'limits': ['Actual source-side current program validation; no execution inside the installed runtime is claimed.',
                       'Map emission is separately recorded from read-only validation. Semantic assessment and installation correspondence remain separate.'],
        })
        refs[name] = save(name + '.json', value)
    original = W / 'rebind-adapter-001/source_current_model.json'
    value = read(original)
    value.update({'subjects': {'stdo_representation': subjects['stdo_representation']},
                  'original_source_wrapper': ref(original),
                  'limits': ['Actual deterministic coordinate rebind of the pinned predecessor, with typed inverse equality and preserved non-coordinate content; not new semantic authoring.',
                             'This operation ran against source files. Later installation joins establish correspondence only and do not relocate the original execution.']})
    refs['source_current_model'] = save('source_current_model.json', value)
    old = read(R / 'stack_release.json')
    previous = old['components']['representation']['evidence']['independent_semantic_review']
    report = W / 'review-custody-001/original/REBIND_REVIEW_004_005.json'
    value = {
        'kind': 'stdo.cohort-evidence/1', 'category': 'independent_assessment', 'claim': 'independent_semantic_review',
        'status': 'passed', 'conclusion': 'satisfied', 'open_required_findings': [],
        'assessor': '/root/stdo305_integration_review',
        'authors': ['/root/stdo305_representation', '/root/stdo305_tools_skills'],
        'executive_disposition': 'accepted_for_release_scope',
        'disposition_basis': 'Executive conversation disposition accepts the exact bounded producer/content-preservation review d76ac480 and current source handoff; this is a Writer transcription of that disposition, not a new signed review or remote-release decision.',
        'source_identity_sha256': candidate['source']['source_identity_sha256'],
        'subjects': {'stdo_representation': subjects['stdo_representation']},
        'report': ref(report), 'predecessor_assessment': previous,
        'current_rebind': facts['rebind'],
        'limits': ['The predecessor assessment is limited to its targeted three findings, 42 fields and five cones. Its original conversation/transcription attribution remains unchanged.',
                   'The independent current review establishes preservation of that assessed content through the finite coordinate transformation. It does not establish whole-model or whole-method semantic adequacy.',
                   'Original authoring/calculus provenance and residual qualifications remain historical; current structural proof and installed/public claims have separate actual evidence.'],
    }
    refs['independent_semantic_review'] = save('independent_semantic_review.json', value)
    result = save('INDEX.json', {'kind': 'stdo.closed-source-claim-bindings/1', 'candidate': ref(W / 'cohort-001/CANDIDATE.json'),
                                'claims': refs, 'input_closure': closure, 'installed_binding': 'pending actual runtime completion; not claimed by these source executions'})
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
