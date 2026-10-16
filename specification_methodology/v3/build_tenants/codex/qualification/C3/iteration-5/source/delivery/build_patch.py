"""Author-selected I5 delivery bindings; mechanics only locate their source.

The changes below are the Writer's interpretation, not a semantic inference
from a digest. Independent fidelity assessment remains separate.
"""
import copy
import difflib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
from account_protocol import PROTOCOL, heading_units
from context import INPUTS, PACKAGE, REPO, sha, write

PREIMAGE = INPUTS['starting_tenant']
COMMON = INPUTS['common_input']
F = 'FOUNDATIONS.'
CHANGES = {
    'SPEC_METHOD.universal-intake-triage': (
        'Bind current subject, required outcome, observations and predictive model to the shared feedback/diagnosis relation; distinguish realisation, requirement/design, prediction and observation causes. Preserve unresolved alternatives and acquire evidence before unjustified repair. Severity and priority do not change verdict or authority; a bug list projects existing work.',
        ['bounded-construction']),
    'SPEC_METHOD.transition-evidence-and-proof-cadence': (
        'Select focused proof from material assertion/execution impact and risk, including supported exclusions, new obligations and mandatory gates. Support the intended claim rather than a weaker cheap falsifier; retain justified evidence on its original subject and compare selection plus reassessment costs. Whole-candidate qualification remains at its boundary or where risk, unknown impact or a gate requires it.',
        ['change-impact-and-evidence-retention', 'risk-and-assurance-selection', 'assertions-and-observations']),
    'SPEC_METHOD.evidence-rules': (
        'Construction assurance owns obligation/assertion/observation/conclusion relations; Contract application binds the operation and Faithful projection its views. Existing proof-target, separation and exposure policies retain their triggers.',
        ['construction-assurance']),
    'SPEC_METHOD.proof-target-identity-and-adequacy-stdo-up-001': (
        'Bind supported necessary/sufficient or conjunctive assertion relations and distinguishing observations to the intended proof target; interpretive fidelity and actual checker behaviour remain separate obligations.',
        ['assertions-and-observations']),
    'SPEC_METHOD.testing-strategy-taxonomy': (
        'Bind each lane expectation to owning source and justified interpretation, separately from actual subject/checker/environment/observations. Labels alone establish neither fidelity nor independent failure causes. Implementation-derived regression stays local unless upstream justification is established; shared derivations may serve test families in existing carriers.',
        ['parallel-assurance-and-provenance']),
    'TICKET_METHOD.condition-based-closure-and-reuse': (
        'Closure combines applicable retained evidence with actual reassessment under current material assertion, execution and validity dependencies. Selection is not performance; preserve original subjects, failures, unknown impact, new obligations and mandatory gates, without imposing ticket/file boundaries on impact.',
        ['change-impact-and-evidence-retention']),
    'TICKET_METHOD.test-case-authority': (
        'The expectation authority path needs a justified interpreted predicate and derivation; separate execution provenance binds checker, actual subject, environment, observations and result. Existing carriers and shared derivations suffice without per-test tickets or duplicate ledgers.',
        ['parallel-assurance-and-provenance']),
    'REFERENCE_FRAME_METHOD.evidence': (
        'Bind shared construction assurance to the frame predicate, acquired observations and consuming decision. Assertion and execution provenance remain separate; small context or authenticated observation alone supplies no sound complete decision.',
        ['construction-assurance']),
    'REFERENCE_FRAME_METHOD.independently-activated-co-evaluation': (
        'A mutual-assurance claim accounts for material shared causes under the shared provenance relation. Separate activations and authorship independence alone neither establish statistical independence nor validate a shared expectation.',
        ['parallel-assurance-and-provenance']),
    'DESIGN_MODULE_METHOD.6b-module-derived-unit-test-rule': (
        'Bind assertion sources to accepted module obligations and execution to the actual module realisation. Ownership trace does not establish predicate or observation adequacy; implementation-discovered tests need justified re-expression against the module obligation before module closure. Preserve existing proof carriers and optional profile conditions.',
        ['parallel-assurance-and-provenance', 'assertions-and-observations']),
    'RELEASE_METHOD.qualification-and-recovery': (
        'Reused exact-subject qualification needs supported claim/dependency/observation applicability. Required release gates survive narrower selection, and unchanged content qualification does not establish the separately observed remote publication relation.',
        ['change-impact-and-evidence-retention']),
    'WORLD_MODEL_METHOD.4-assure': (
        'Bind the interpreted model-claim predicate and actual observations to its declared purpose. Prediction accuracy does not establish a required construction outcome, and prediction error alone does not establish outcome failure; correction respects the distinct accounts.',
        ['assertions-and-observations', 'bounded-construction']),
}


def prior_bytes(path):
    return subprocess.check_output(['git', 'show', PREIMAGE + ':' + str(PACKAGE.relative_to(REPO) / path)], cwd=REPO)


def translated_blocks(row, before, after):
    """Retain block IDs while pinning exact surviving/replaced source spans."""
    old_unit = heading_units(before)[row['owner']['anchor']]
    new_unit = heading_units(after)[row['owner']['anchor']]
    old, new = old_unit['body'], new_unit['body']
    operations = difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes()

    def boundary(index, ending=False):
        if index == len(old):
            return len(new)
        for tag, a, b, c, d in operations:
            if a <= index < b:
                return c + index - a if tag == 'equal' else (d if ending else c)
            if index == b and ending:
                return d
        raise ValueError('Unmapped block boundary')

    blocks = copy.deepcopy(row.get('source_clauses', []))
    for block in blocks:
        start, end = block['byte_start'], block['byte_end']
        fragment = before[start:end]
        if not fragment or sha(fragment) != block['sha256']:
            raise ValueError('Unpinned preimage ' + row['id'])
        if new.count(fragment) == 1:
            start = new_unit['byte_start'] + new.index(fragment)
            end = start + len(fragment)
        elif start == old_unit['byte_start'] and end == old_unit['byte_end']:
            start, end = new_unit['byte_start'], new_unit['byte_end']
        else:
            if not old_unit['byte_start'] <= start < end <= old_unit['byte_end']:
                raise ValueError('Changed cross-section block requires separate authoring: ' + row['id'])
            start = new_unit['byte_start'] + boundary(start - old_unit['byte_start'])
            end = new_unit['byte_start'] + boundary(end - old_unit['byte_start'], True)
        block.update(byte_start=start, byte_end=end, sha256=sha(after[start:end]))
    if not any(b['byte_start'] == new_unit['byte_start'] and b['byte_end'] == new_unit['byte_end'] for b in blocks):
        blocks.append({'id': 'i5-binding', 'byte_start': new_unit['byte_start'], 'byte_end': new_unit['byte_end'],
                       'sha256': sha(new), 'roles': ['source_owned_body']})
    return blocks


def main():
    prior = json.loads((ROOT.parent / 'iteration-4/DETERMINATIONS.json').read_bytes())
    rows = {r['id']: r for r in prior['determinations']}
    patches = []
    territory = set()
    for identifier, (obligation, owners) in CHANGES.items():
        row = rows[identifier]
        path, anchor = row['owner']['path'], row['owner']['anchor']
        territory.add(path)
        before, after = prior_bytes(path), (PACKAGE / path).read_bytes()
        old_unit, new_unit = heading_units(before)[anchor], heading_units(after)[anchor]
        assert old_unit['body'] != new_unit['body'], identifier
        obligations = copy.deepcopy(row.get('obligations', []))
        if identifier == 'SPEC_METHOD.transition-evidence-and-proof-cadence':
            obligations.remove('Use cheapest focused proof able to falsify active relation.')
        obligations.append(obligation)
        deps = copy.deepcopy(row.get('dependencies', []))
        relations = copy.deepcopy(row.get('dependency_relations', []))
        references = copy.deepcopy(row.get('source_references', []))
        for owner in owners:
            target = F + owner
            if target not in deps:
                deps.append(target)
            if target not in references:
                references.append(target)
            if not any(r.get('id') == target and r.get('kind') == 'contract_application' for r in relations):
                relations.append({'id': target, 'kind': 'contract_application', 'binding': obligation})
        blocks = translated_blocks(row, before, after)
        fields = {'obligations': obligations, 'dependencies': deps, 'dependency_relations': relations,
                  'source_references': references, 'source_clauses': blocks,
                  'source_clause_ids': [identifier + '#' + block['id'] for block in blocks]}
        if identifier == 'SPEC_METHOD.transition-evidence-and-proof-cadence':
            fields['permissions_exceptions'] = ['Consumer chooses representation; whole-candidate qualification is at its declared boundary or where affected risk, uncertain impact or a mandatory gate requires it.']
        if row.get('source_excerpt') and row['source_excerpt'].encode() not in new_unit['body']:
            fields['source_excerpt'] = new_unit['body'].decode().split('\n\n', 2)[1]
        patches.append({'id': identifier, 'preimage_body_sha256': sha(old_unit['body']),
                        'candidate_body_sha256': sha(new_unit['body']), 'semantic_fields': fields})
    result = {'schema_version': PROTOCOL, 'producer': 'I5-WRITE-DELIVERY', 'common_input': COMMON,
              'source_preimage': PREIMAGE, 'owner_paths': sorted(territory), 'updates': patches, 'new_rows': []}
    write(Path(__file__).parent / 'ACCOUNT_PATCH.json', result)
    print(json.dumps({'updates': len(patches), 'paths': sorted(territory), 'sha256': sha((Path(__file__).parent / 'ACCOUNT_PATCH.json').read_bytes())}))


if __name__ == '__main__':
    main()
