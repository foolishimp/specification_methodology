"""Wrap actual closed current source operations, preserving original receipts."""
from pathlib import Path
import hashlib
import json

R = Path('/Users/jim/src/apps/specification_methodology')
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W = Q / 'release-tools'
HERE = Path(__file__).resolve().parent
O = HERE / 'source-claims'


def read(p):
    return json.loads(p.read_bytes())


def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}


def save(name, value):
    p = O / name
    with p.open('x') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')
    return ref(p)


def main():
    assert not O.exists()
    O.mkdir()
    b = read(HERE / 'CANDIDATE.json')
    subjects = {k: v['subject']['sha256'] for k, v in b['products'].items()}
    records = {}
    for claim, phase in [('source_current_map', 'map'), ('current_index_validation', 'index')]:
        path = HERE / 'axiom-008' / phase / 'execution.json'
        value = read(path)
        assert value['execution']['returncode'] == 0
        assert value['execution']['inputs'] == [b['components']['representation']['facts'][k] for k in ('program', 'bindings', 'source_corpus')]
        value.update({'kind': 'stdo.cohort-evidence/1', 'category': 'execution', 'claim': claim, 'status': 'passed',
                      'source_identity_sha256': b['source']['source_identity_sha256'],
                      'subjects': {k: subjects[k] for k in ('axiom_indexer', 'stdo_representation')},
                      'original_execution': ref(path),
                      'limits': ['Actual source-side operation with program, bindings and qualification inventory captured before/after. Original execution fields are unchanged.',
                                 'The owner resolves source files via bindings; source-corpus is an explicitly captured qualification inventory, not a direct command argument.',
                                 'Same-byte map emission and its actual mtime effect are retained separately from read-only validation. No installed execution or semantic verdict is inferred.']})
        records[claim] = save(claim + '.json', value)
    path = W / 'rebind-adapter-001/source_current_model.json'
    value = read(path)
    value.update({'subjects': {'stdo_representation': subjects['stdo_representation']}, 'original_source_wrapper': ref(path),
                  'limits': ['Actual finite coordinate rebind of the pinned published predecessor with typed inverse equality and preserved non-coordinate content; not new semantic authoring.',
                             'Original source-side execution remains unchanged. Installation correspondence is added separately and does not relocate that execution.']})
    records['source_current_model'] = save('source_current_model.json', value)
    old = read(R / 'scripts/fixtures/stack_release-v3.0.5.json')
    records['independent_semantic_review'] = save('independent_semantic_review.json', {
        'kind': 'stdo.cohort-evidence/1', 'category': 'independent_assessment', 'claim': 'independent_semantic_review',
        'status': 'passed', 'conclusion': 'satisfied', 'open_required_findings': [],
        'assessor': '/root/stdo305_integration_review', 'authors': ['/root/stdo305_representation', '/root/stdo305_tools_skills'],
        'executive_disposition': 'accepted_for_release_scope',
        'disposition_basis': 'Writer transcription: Root accepted independent rebind review d76ac480 and the current source handoff for the bounded preserved-content scope; this is not a new signed review or remote-publication decision.',
        'source_identity_sha256': b['source']['source_identity_sha256'],
        'subjects': {'stdo_representation': subjects['stdo_representation']},
        'report': ref(W / 'review-custody-001/original/REBIND_REVIEW_004_005.json'),
        'predecessor_assessment': old['components']['representation']['evidence']['independent_semantic_review'],
        'coordinate_rebind': b['components']['representation']['facts']['rebind'],
        'metadata_correction_review': ref(W / 'review-custody-006/REVIEW.json'),
        'limits': ['The predecessor assessment covers its targeted three findings, 42 fields and five cones; original conversation/transcription attribution remains unchanged.',
                   'Independent current review establishes preservation through the closed coordinate transform. It does not establish whole-model or whole-method semantic adequacy.',
                   'Original authoring/calculus provenance and residuals remain historical. Current structural proof, fixed host interfaces, public installation and release qualification have separate actual records.'],
    })
    print(json.dumps(save('INDEX.json', {'kind': 'stdo.closed-source-claim-bindings/1', 'candidate': ref(HERE / 'CANDIDATE.json'),
                                       'claims': records, 'installation_correspondence': 'pending actual complete installed cohort'}), sort_keys=True))


if __name__ == '__main__':
    main()
