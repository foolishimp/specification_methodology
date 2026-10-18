"""Render the explicitly authored RC4 intake account and source coordinates.

The meanings below are the Intake Writer's decisions, not extracted semantics.
The existing heading protocol supplies coordinates; old records are read-only.
"""
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[3]
REPO = TENANT.parents[3]
PREFIX = 'specification_methodology/v3/build_tenants/codex/'
SOURCE_PREIMAGE = '736e5e9283ac1f2a06ed6099aef503711e1f00a1'
ACCOUNT_COMMIT = 'e2e40fbc02484d99c8a84f1a844c36aead2dfd46'
CONSERVATION_COMMIT = 'f45fa26a573665d3e78d2df25d8b13ede83607e1'
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
ACCOUNT_PATH = 'qualification/C3/rc1/content-repair/integration/DETERMINATIONS.json'
sys.path.insert(0, str(TENANT / 'qualification/C3/iteration-5/tools'))
from account_protocol import heading_units


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def frozen(commit, relative):
    return subprocess.check_output(['git', 'show', commit + ':' + PREFIX + relative], cwd=REPO)


def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


prior = json.loads(frozen(ACCOUNT_COMMIT, ACCOUNT_PATH))
rows = {r['id']: r for r in prior['determinations']}
paths = ['standards/SPEC_METHOD.md', 'standards/DESIGN_MODULE_METHOD.md']
old = {p: frozen(SOURCE_PREIMAGE, 'successor/' + p) for p in paths}
new = {p: (TENANT / 'successor' / p).read_bytes() for p in paths}
old_units = {p: heading_units(raw) for p, raw in old.items()}
new_units = {p: heading_units(raw) for p, raw in new.items()}
updates = {}


def edit(identifier, **fields):
    item = updates.setdefault(identifier, {'id': identifier, 'semantic_fields': {}})
    item['semantic_fields'].update(copy.deepcopy(fields))


def dependency(identifier):
    row = rows[identifier]
    deps = list(row.get('dependencies', []))
    dep = 'SPEC_METHOD.universal-intake-triage'
    if dep not in deps:
        deps.append(dep)
    relations = copy.deepcopy(row.get('dependency_relations', []))
    if not any(r['id'] == dep for r in relations):
        relations.append({'id': dep, 'kind': 'contract_application'})
    edit(identifier, dependencies=deps, dependency_relations=relations)


edit('SPEC_METHOD.spec-driven-homeostatic-methodology', predicate='Spec contracts consume foundational premises through contract application and bounded construction; workspace/context governs current state and acquisition, Universal Intake Triage owns classification and re-entry, and UP-020 keeps construction, assessment and disposition predicates and authority separate.')
dependency('SPEC_METHOD.spec-driven-homeostatic-methodology')

identifier = 'SPEC_METHOD.spec-drivenness-litmus'
edit(identifier, obligations=rows[identifier]['obligations'] + ['Apply supported drift correction through Universal Intake Triage; reprice the governing source when its meaning needs change, not merely because realization violates sufficient law.'])
dependency(identifier)

identifier = 'SPEC_METHOD.constitutional-chain'
definition = copy.deepcopy(rows[identifier]['definition'])
definition['chain'][-1] = 'Intake-selected re-entry or observation'
definition['roles']['Repricing'] = 'Universal Intake Triage selects the owning change class and affected downstream span; constitutional insufficiency alone does not require Goals or Intent, and unresolved cause may require observation.'
edit(identifier, definition=definition)
dependency(identifier)

identifier = 'SPEC_METHOD.verification-layers'
edit(identifier, obligations=[
    'Scenarios test concrete operational behavior across the intent-to-realization chain; comparing specification words alone does not supply operational evidence.',
    'Without an adequate scenario the scenario layer has not demonstrated the capability; that absence alone does not establish absence of capability.',
    'A failed scenario enters Universal Intake Triage. Its symptom alone does not distinguish realization defect, inadequate governing meaning, inaccurate prediction or inadequate scenario, oracle or observation.'
])
dependency(identifier)

identifier = 'SPEC_METHOD.renewal-path'
edit(identifier,
     predicate='Concrete use-case feedback follows Universal Intake Triage: supported cause selects the owning-layer change and affected downstream span; insufficient evidence retains unresolved alternatives and may select further authorized observation without justifying dependent repair.',
     obligations=[
         'Apply intake diagnosis to actual observations, current model and required outcome; retain the supported cause and unresolved alternatives.',
         'Reconcile the affected downstream span from the selected owning layer without repricing sufficient upstream meaning.',
         'Goals or Intent change only when the selected class establishes their work-wave, direction or scope change, with a concrete gap and owning decision; implementation pressure supplies neither.',
         'A requirement gap with stable direction and Product meaning may re-enter Requirements; sufficient governing law permits repair of its defective realization.',
         'Maintain directional authority during cumulative refinement and re-derivation.'
     ],
     source_excerpt='Real use supplies feedback to the constitutional chain. Its renewal route uses\nthe classification and re-entry owned by\n[Universal Intake Triage](#universal-intake-triage):')
dependency(identifier)

identifier = 'SPEC_METHOD.drift-signals'
definition = copy.deepcopy(rows[identifier]['definition'])
definition['persistent observed delta'] = 'Universal Intake Triage establishes the cause; persistence alone decides neither a wrong relation nor observation sufficiency.'
definition['real gap inexpressible in requirements'] = 'Intake selects the owning layer whose meaning needs change; missing requirement meaning does not establish a direction or scope change.'
edit(identifier, definition=definition)
dependency(identifier)

identifier = 'SPEC_METHOD.method'
obligations = list(rows[identifier]['obligations'])
obligations[3] = 'Use-case gap enters intake first, then a scenario makes the pressure concrete. Gap analysis uses the intake diagnosis, retaining unresolved alternatives and needed observations; a failed scenario alone does not decide the cause.'
obligations[7] = 'A constitutional gap uses the selected owning change class and reconciles the affected downstream span; Goals/Intent change only under their work-wave/direction/scope triggers. Sufficient requirements/design permit implementation repair within the grant and affected recheck. A newly discovered need to change governing meaning returns to intake before that change.'
edit(identifier, obligations=obligations)

identifier = 'DESIGN_MODULE_METHOD.proportional-design-sequencing'
obligations = list(rows[identifier]['obligations'])
obligations[3] = 'Repeated/cross-cutting material surprises enter Universal Intake Triage. A supported underconstrained-design diagnosis with sufficient governing requirements requires one bounded design_reframe, retaining affected code provisionally until acceptance. A surprise alone establishes no design cause; preserve unresolved alternatives and any required upstream change or further observation.'
edit(identifier, obligations=obligations)
dependency(identifier)

# The family policy was explicitly revised at its source owner. Every account
# copy of that exact row consumes this same revised policy; no new family or
# speculative dependency is inferred.
old_policy = 'Spec owns computed classification, the upward re-entry route and downstream trace closure. Its ADR fields and layout are conventions for carrying decisions. Ticket owns continuity of recorded judgments and rulings; each semantic owner decides its own repricing.'
new_policy = 'Computed treatment owns whether the candidate or governing relation needs correction; Universal Intake Triage owns the resulting change class and re-entry. Renewal and trace closure consume those decisions. ADR fields and layout carry decisions; Ticket owns continuity of judgments and rulings, and each semantic owner decides its own repricing.'
old_line_sha = '9e80b0c4fd724fd1e7e4cdf9ec561e4a6ac2a5b612b215bc3b791efd3257f199'
family_line = next(line for line in new['standards/SPEC_METHOD.md'].splitlines(keepends=True) if line.startswith(b'| [Computed Classification And Treatment]'))
new_line_sha = sha(family_line)


def family_copy(value):
    if isinstance(value, list):
        return [family_copy(child) for child in value]
    if isinstance(value, dict):
        return {key: family_copy(child) for key, child in value.items()}
    if value == old_policy:
        return new_policy
    if value == old_line_sha:
        return new_line_sha
    return value


for identifier, row in rows.items():
    if row['owner']['path'] not in paths:
        continue
    for field in ('argument', 'definition'):
        if field in row:
            revised = family_copy(row[field])
            if revised != row[field]:
                edit(identifier, **{field: revised})

# Source-block pins retain all immediate-section prose in paragraph-sized
# blocks; they do not claim a mechanically inferred clause-to-predicate proof.
# A current semantic mapping is authored above; independent fidelity is open.
for identifier, row in rows.items():
    path = row['owner']['path']
    if path not in paths:
        continue
    anchor = row['owner']['anchor']
    before, after = old_units[path][anchor], new_units[path][anchor]
    if before['body'] != after['body']:
        if identifier not in updates:
            raise RuntimeError('Changed source lacks authored meaning: ' + identifier)
        blocks = []
        for index, match in enumerate(re.finditer(rb'\S(?:.*?\S)?(?=\n\s*\n|\Z)', after['body'], re.S), 1):
            raw = match.group()
            blocks.append({'id': f'rc4-p{index:02d}', 'byte_start': after['byte_start'] + match.start(),
                           'byte_end': after['byte_start'] + match.end(), 'sha256': sha(raw)})
        edit(identifier, source_clauses=blocks,
             source_clause_ids=[identifier + '#' + block['id'] for block in blocks],
             source_clause_roles=[])

# The unchanged testing taxonomy contains the same literal block twice. Its
# containing section is byte-identical, so its relative offsets identify the
# original clauses without guessing from content search or changing meaning.
identifier = 'SPEC_METHOD.testing-strategy-taxonomy'
row = rows[identifier]
path, anchor = row['owner']['path'], row['owner']['anchor']
before, after = old_units[path][anchor], new_units[path][anchor]
assert before['body'] == after['body']
shift = after['byte_start'] - before['byte_start']
blocks = copy.deepcopy(row['source_clauses'])
for block in blocks:
    assert before['byte_start'] <= block['byte_start'] <= block['byte_end'] <= before['byte_end']
    block['byte_start'] += shift
    block['byte_end'] += shift
    assert sha(new[path][block['byte_start']:block['byte_end']]) == block['sha256']
edit(identifier, source_clauses=blocks)

for identifier, item in updates.items():
    row = rows[identifier]
    path, anchor = row['owner']['path'], row['owner']['anchor']
    item['preimage_body_sha256'] = sha(old_units[path][anchor]['body'])
    item['candidate_body_sha256'] = sha(new_units[path][anchor]['body'])
    assert item['preimage_body_sha256'] == row['owner']['body_sha256'], identifier

write('ACCOUNT_PATCH.json', {
    'schema_version': 'stdo.i5.authored-account-patch/v1',
    'common_input': COMMON, 'source_preimage': SOURCE_PREIMAGE,
    'producer': 'RC4-INTAKE-WRITER', 'owner_paths': paths,
    'updates': [updates[k] for k in sorted(updates)], 'new_rows': []
})
write('SOURCE_MEMBERS.json', {
    'source_preimage': SOURCE_PREIMAGE,
    'members': [{'path': path, 'before_sha256': sha(old[path]), 'sha256': sha(new[path]), 'bytes': len(new[path])} for path in paths],
    'changed_immediate_sections': [r['id'] for r in rows.values() if r['owner']['path'] in paths and old_units[r['owner']['path']][r['owner']['anchor']]['body'] != new_units[r['owner']['path']][r['owner']['anchor']]['body']],
    'patched_determinations': sorted(updates),
    'standing': 'authored source and account coordinates; no independent semantic acceptance'
})
print(json.dumps({'patched_rows': len(updates), 'changed_sections': len(json.loads((HERE / 'SOURCE_MEMBERS.json').read_text())['changed_immediate_sections'])}))

# Author conservation assessment against the actual installed predecessor.
# No changed decision is labelled conserved merely because intake's owner was
# already sound elsewhere. Earlier proposed changes remain in each relation.
conservation = json.loads(frozen(CONSERVATION_COMMIT, 'qualification/C3/rc1/content-repair/integration/CONSERVATION.json'))
frontier = {r['id']: r for r in conservation['rows']}
installed = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards')
changes = [
 ('SPEC_METHOD.md#spec-drivenness-litmus', None,
  'Replace unconditional constitutional repricing on drift with intake-selected correction. Sufficient governing law permits realization repair without an invented upstream revision.'),
 ('SPEC_METHOD.md#constitutional-chain', None,
  'Replace the constitutional-insufficiency-to-new-Goals/Intent edge with Universal Intake Triage selection at the actual owning layer. Preserve unresolved cause and authorized further observation; genuine Goal/Intent changes retain their own conditions.'),
 ('SPEC_METHOD.md#verification-layers', 'RC4-INTAKE-R001',
  'Separate a capability not demonstrated by the scenario layer from an absent capability. A scenario failure is evidence for diagnosis rather than proof that realization caused it; retain inadequate scenario/oracle/observation and governing-meaning alternatives.'),
 ('SPEC_METHOD.md#renewal-path', None,
  'Replace unconditional top-level renewal for constitutional gaps with intake-owned diagnosis and layer-specific re-entry. Requirement-only repair, sufficient-law realization repair and unresolved diagnosis remain possible; concrete Goal/Intent repricing retains its triggers and owner.'),
 ('SPEC_METHOD.md#drift-signals', 'RC4-INTAKE-R002',
  'Replace the forced code-or-stale-stack diagnosis and required new Intent for gaps absent from current Requirements with the supported cause and owning-layer selection. Persistence and missing requirement meaning do not prove direction change or observation adequacy.'),
 ('SPEC_METHOD.md#method', None,
  'Complete the earlier selected-re-entry repair by retaining unresolved intake, applying its full diagnosis to gap analysis, and preventing an implementation classification from silently authorizing requirement/design changes.'),
 ('DESIGN_MODULE_METHOD.md#proportional-design-sequencing', 'RC4-INTAKE-R003',
  'Condition the repeated-surprise design_reframe trigger on intake establishing an underconstrained affected design cut with sufficient governing requirements. Preserve the existing material architectural-ambiguity design gate; surprise alone does not establish a design cause or make that gate sufficient for an upstream/observation defect.')
]
proposals = []
for claim, new_id, meaning in changes:
    previous = frontier[claim]
    member, anchor = claim.split('#')
    path = 'standards/' + member
    pred_raw = (installed / member).read_bytes()
    pred_unit = heading_units(pred_raw)[anchor]
    successor = new_units[path][anchor]
    relation = copy.deepcopy(previous.get('successor_relation')) or {
        'id': new_id, 'predecessor_claim_id': claim,
        'changed_meaning': '', 'replacement_loci': []}
    assert relation['id']
    relation['changed_meaning'] = (relation['changed_meaning'] + ' ' + meaning).strip()
    for locus in [path + '#' + anchor, 'standards/SPEC_METHOD.md#universal-intake-triage', 'standards/SPEC_METHOD.md#computed-classification-and-treatment']:
        if locus not in relation['replacement_loci']:
            relation['replacement_loci'].append(locus)
    relation.update(standing='proposed_pending_owner_decision', owner_decision=None,
                    remaining_condition='Current independent semantic assessment and the reserved owner decision on the exact replacement remain open.')
    proposals.append({
        'predecessor_claim_id': claim,
        'current_disposition': previous['disposition'],
        'authored_successor_disposition': 'superseded',
        'standing': 'author_proposal_pending_independent_assessment_and_owner_decision',
        'owner_decision': None,
        'affected_successor_loci': relation['replacement_loci'],
        'meaning': meaning,
        'reason': 'The predecessor consumer makes a stronger or differently routed decision than the existing Universal Intake Triage owner permits. Repair changes that consumer meaning; it is not an unchanged-row conservation claim.',
        'existing_relation': previous.get('successor_relation'),
        'proposed_relation': relation,
        'author_comparison': {
            'predecessor_basis': 'v2.5.1-rc.2',
            'predecessor_section_sha256': sha(pred_unit['body']),
            'candidate_section_sha256': sha(successor['body']),
            'predecessor_section_bytes': len(pred_unit['body']),
            'candidate_section_bytes': len(successor['body']),
            'candidate_locus': path + '#' + anchor,
            'candidate_source_preimage': SOURCE_PREIMAGE,
            'candidate_assessed_commit': None,
            'granularity': 'Immediate section plus the named intake/treatment owner and material consumer conditions.',
            'meaning_assessment': meaning,
            'standing': 'bounded_author_assessment_not_independent_acceptance'
        }
    })
write('CONSERVATION_DISPOSITIONS.json', {
    'schema_version': 'stdo.rc4.intake-conservation-dispositions/v1',
    'source_preimage': SOURCE_PREIMAGE,
    'predecessor_basis': 'stdo://releases/v2.5.1-rc.2/',
    'predecessor_manifest_sha256': '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782',
    'prior_account_commit': CONSERVATION_COMMIT,
    'prior_account': 'qualification/C3/rc1/content-repair/integration/CONSERVATION.json',
    'rows': proposals,
    'clarifications_without_new_predecessor_claims': [
        {'locus': 'standards/SPEC_METHOD.md#spec-driven-homeostatic-methodology', 'meaning': 'Route intake and re-entry to the existing actual owner; workspace/context retains only its existing state/acquisition relation.'},
        {'locus': 'standards/SPEC_METHOD.md#method-families', 'meaning': 'Expose intake and computed-treatment ownership without treating Renewal as a competing re-entry owner.'}
    ],
    'limits': ['No independent acceptance is recorded.', 'Null candidate_assessed_commit is intentionally pending the parent source freeze; section hashes bind this author comparison now.', 'Historical dispositions and evidence remain on their original subjects.']
})

write('CONSERVATION_CHANGES.json', {
    'schema_version': 'stdo.rc4.intake-conservation-changes/v1',
    'source_preimage': SOURCE_PREIMAGE,
    'prior_account_commit': CONSERVATION_COMMIT,
    'updates': [{
        'id': p['predecessor_claim_id'],
        'expected_disposition': p['current_disposition'],
        'disposition': p['authored_successor_disposition'],
        'reason': p['proposed_relation']['changed_meaning'],
        'successor_loci': list(dict.fromkeys(frontier[p['predecessor_claim_id']].get('successor_loci', []) + p['affected_successor_loci'])),
        'successor_relation': p['proposed_relation'],
        'question_id': 'Q-' + p['proposed_relation']['id'],
        'author_comparison': p['author_comparison']
    } for p in proposals]
})
