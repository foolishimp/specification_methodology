"""Pin this authored core repair; never edits source, generated assets or Git."""
from __future__ import annotations

import copy
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
PACKAGE = TENANT / 'successor'
TOOLS = TENANT / 'qualification/C3/iteration-5/tools'
sys.path.insert(0, str(TOOLS))
from account_protocol import heading_units, make_owner

sha = lambda data: hashlib.sha256(data).hexdigest()
PREIMAGE = '73443dbc6e7c74b3a80e4375727b768ed2ba54d0'
COMMON = '4c340f7adec9f3c893e3e267b23e4cadeb357854'
PRIOR_PATH = TENANT / 'qualification/C3/rc1/end-repair/integration/DETERMINATIONS.json'
prior = json.loads(PRIOR_PATH.read_text())
old = {r['id']: r for r in prior['determinations']}
preimages = json.loads((HERE / 'SOURCE_PREIMAGE.json').read_text())
source = {m['path']: (PACKAGE / m['path']).read_bytes() for m in preimages['members']}
units = {p: heading_units(raw) for p, raw in source.items()}
for m in preimages['members']:
    inventory = next(x for x in prior['source_members'] if x['path'] == m['path'])
    assert inventory['sha256'] == m['sha256'], ('preimage account drift', m['path'])


def dependency(row, identifier, binding, when='within the declared applicability'):
    if identifier not in row.setdefault('dependencies', []):
        row['dependencies'].append(identifier)
    relations = row.setdefault('dependency_relations', [])
    relation = {'id': identifier, 'kind': 'contract_application', 'binding': binding,
                'required_when': when}
    relations[:] = [x for x in relations if x.get('id') != identifier]
    relations.append(relation)


def pointer(row, path):
    v = row
    for part in path.strip('/').split('/'):
        v = v[int(part)] if isinstance(v, list) else v[part]
    return v


def old_plan(row):
    return [(m['source_roles'], m['represented_at']) for m in row.get('source_clause_roles', [])]


def plan(roles, *refs):
    return (roles.split(), [{'role': role, 'pointer': ptr} for role, ptr in refs])


def blocks(row, mappings):
    unit = units[row['owner']['path']][row['owner']['anchor']]
    spans = list(re.finditer(rb'\S[^\n]*(?:\n(?!\n)[^\n]*)*', unit['body']))[1:]
    assert len(spans) == len(mappings), (row['id'], len(spans), len(mappings))
    clauses, roles = [], []
    for n, (span, (tags, targets)) in enumerate(zip(spans, mappings), 1):
        for target in targets:
            pointer(row, target['pointer'])
        start, end = unit['byte_start'] + span.start(), unit['byte_start'] + span.end()
        digest = sha(source[row['owner']['path']][start:end])
        key = 'c' + str(n)
        clauses.append({'id': key, 'sha256': digest, 'byte_start': start, 'byte_end': end, 'roles': tags})
        roles.append({'source_clause_id': row['id'] + '#' + key, 'source_block_id': key,
                      'source_block_sha256': digest, 'source_byte_start': start, 'source_byte_end': end,
                      'source_roles': tags, 'represented_at': targets,
                      'standing': 'author_source_to_representation_mapping_not_fidelity_verdict'})
    row['source_clauses'] = clauses
    row['source_clause_roles'] = roles
    row['source_clause_ids'] = [x['source_clause_id'] for x in roles]


def source_families():
    path = 'standards/FOUNDATIONS.md'
    u = units[path]['core-contract-derivations']
    rows = []
    scope = 'Only when assessing this family argument, its applicability, consequence, conservation, coverage or fidelity against this consumer; no unconditional operational dependency.'
    for number, line in enumerate(source[path].splitlines(keepends=True), 1):
        text = line.decode().strip()
        if not u['start_line'] <= number <= u['end_line'] or not text.startswith('| ') or text.startswith('| Deciding'):
            continue
        cells = [c.strip() for c in text.split('|')[1:-1]]
        assert len(cells) == 4
        rows.append({'family': cells[0], 'declared_consumer_scope': cells[0],
                     'premises': sorted(set(re.findall(r'F[1-6]', cells[1]))),
                     'premise_and_pillar_argument': cells[1], 'conditional_consequence': cells[2],
                     'additional_policy_and_owner': cells[3],
                     'source_row': {'path': path, 'anchor': u['anchor'], 'line': number,
                                    'sha256': sha(line), 'hash_boundary': 'Exact Markdown row including terminal newline.'},
                     'source_refs': [{'path': path, 'anchor': u['anchor'], 'role': 'provenance', 'required_when': scope}],
                     'required_when': scope})
    return rows


families = source_families()
changed = {}
plans = {}


def edit(identifier):
    row = copy.deepcopy(old[identifier]); changed[identifier] = row
    plans[identifier] = old_plan(row)
    return row


r = edit('FOUNDATIONS.stdo-foundations')
r['predicate'] = 'Domain methods apply shared result, current-state, bounded-work, authority-conservation, required-independent-assessment and assurance owners with their own predicates, types, policies and grants.'
r['obligations'][1] = 'Use the Transformation Library operations and Foundations shared owners for results, current state, bounded work, authority conservation, required independent assessment and construction assurance; domain specialization supplies no parallel law or actual grant.'
for dep in ['FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.independent-assessment']:
    dependency(r, dep, 'Apply the shared owner while preserving the domain binding.')

r = edit('FOUNDATIONS.finite-capacity-and-total-handling')
r['obligations'] += [
    'Apply Bounded construction within the selected control domain; Design retains the scope and preferred force of its totality policy, with core results unchanged.',
    'Resume from Workspace and context with Spec Product predicates, Ticket carrier use and adopted runtime history/replay duties kept distinct; private context is not continuing work state.']
plans[r['id']] = [plan('obligation latitude scope', ('O', '/obligations/0'), ('P', '/permissions_exceptions/0')),
                  plan('scope obligation', ('O', '/obligations/1')),
                  plan('scope obligation', ('O', '/obligations/2'))]

r = edit('FOUNDATIONS.judgment-and-authority')
r['predicate'] = 'Authority is conserved under actual owner-issued grants, and evidence, assessment, operation and disposition retain their distinct standing.'
r['obligations'] = [
    'This shared owner conserves authority using the unchanged imported authority meanings. Bind actual owner-issued grants to subject, operation/decision, permitted effects and scope; delegation or transfer requires the governing owner permission.',
    'Actor/role/frame identity, document presence, capability, machinery, reachability, evidence shape or a successful judgment cannot mint, widen, transfer or reconstruct authority. Missing/ambiguous authority withholds the dependent act and produces its explicit result or owner re-entry; current existing grants remain usable.',
    'Bind judgment to predicate, subject, basis, evidence, assessor and required independence. Production, assessment and disposition remain separate; supported evidence supplies no operation or decision mandate. Dispose applies the existing decision mandate.',
    'Apply RF-006, AC-014 and adopted Baseline or ODD bindings within their domains; the shared rule appoints no actor or optional profile.',
    'Keep unknown applicability, missing context, incompatible basis and failed predicates observable. Severity, priority, disposition, selected action and promotion are distinct; Spec owns its proportional-disposition conditions.',
    'Bind Construction assurance before a reported pass/failure supports a broader claim; no supported judgment supplies an operation or decision mandate.']
r['permissions_exceptions'] = ['One actor may lawfully hold several distinct authority relations; profile roles and duties require their actual adoption and activation. Existing grants remain usable under their current conditions.']
for dep in ['FOUNDATIONS.reference-only-semantic-imports', 'TRANSFORMATION_LIBRARY.dispose']:
    dependency(r, dep, 'Bind the source meanings or actual disposition operation without granting authority through a reference.')
plans[r['id']] = [plan('obligation scope', ('O', f'/obligations/{i}')) for i in range(6)]
plans[r['id']][0][1].append({'role':'P','pointer':'/permissions_exceptions/0'})
r['argument']['source_family_arguments'] = [x for x in families if '(#judgment-and-authority)' in x['family']]
r['argument']['conditional_consequence'] = 'Evidence or capability cannot supply an owner-issued grant; actual grants retain their scope through delegation and distinct responsibilities.'

r = edit('FOUNDATIONS.preservation-obligations')
r['obligations'][4] += ' Execution by a person, machine or mixed arrangement does not itself discharge cross-account maps or preservation obligations.'

r = edit('FOUNDATIONS.assertions-and-observations')
r['obligations'][2] = 'Equality is available for a justified declared target, including a narrower regression property. Keep its target and scope; establish the required relation to Q_r before a broader claim. Equality alone cannot reject permitted alternatives or prove the full obligation.'

r = edit('FOUNDATIONS.parallel-assurance-and-provenance')
r['permissions_exceptions'][1] = 'One shared derivation may cover a declared family in existing bindings and evidence without a per-test document; any required authorship independence applies Independent assessment.'
dependency(r, 'FOUNDATIONS.independent-assessment', 'Apply claim-relative independence conditions separately from statistical dependence.', 'the governing contract requires independent assessment')

r = edit('FOUNDATIONS.change-impact-and-evidence-retention')
r['obligations'][4] = 'Retention supports claim/scope applicability, justified assertion/observation bases, any independence required for that claim under Independent assessment, and unchanged dependencies or an established preservation relation. Keep original subjects and a new applicability relation; changed hashes alone prove neither invalidity nor equivalence.'
r['obligations'][5] = 'Reopen affected reliance without altering historical observations. Supported repair, reassessment or authorised obligation change may dispose outstanding status, while the original observation, counterexample, subject and citations remain with the reason applicability changed. Relaxing a requirement cannot turn former failure into success or erase it; assess the changed subject against current obligations.'
dependency(r, 'FOUNDATIONS.independent-assessment', 'Recheck only the independence required for the reused claim.', 'that claim requires independent assessment')

r = edit('FOUNDATIONS.bounded-construction')
r['obligations'][0] += ' Lawfulness alone establishes neither delivery nor optimality.'
r['obligations'][2] = 'Finite capacity motivates acquisition while purpose, identity, compatibility and assurance supply additional premises. Refinement may add detail and construction may change state within permitted variation. Decomposition, delegation, concurrency and recursive application preserve affected outer obligations and joins; local success establishes the outer outcome only with required coverage and preservation.'
r['obligations'][3] += ' Admitted work authority selects strategy; a superiority claim states objectives, comparison and assumptions.'
r['obligations'][6] = 'The selected control model truthfully handles its admitted states, including unavailable input, unknown conditions, failed preconditions, partial effects, exhausted capability/authority and revoked authority, through the core under its actual grant. Deterministic, probabilistic and human operations retain their selected outcome models.'
r['obligations'].append('This section owns the shared construction relation; consumers apply it to delivery, correction and control while domain strategy, actor configuration, execution and additional assurance policy retain their owners.')
r['permissions_exceptions'][0] = 'Applicable granted responses include continuation, repair, recovery, re-entry, refusal, yield or termination. A selected total control contract covers every admitted state, without requiring every operation to be total or guaranteeing a solution or external termination.'
plans[r['id']] = [plan('scope obligation', ('O','/obligations/8'))] + plans[r['id']]
r['argument']['source_family_arguments'] = [x for x in families if '(#bounded-construction)' in x['family']]

r = edit('FOUNDATIONS.configuration')
r['obligations'][1] = 'Producing, checking and accepting remain distinct responsibilities even when one actor may do several. Bind actual grants and required review through Judgment and authority and Independent assessment; functional decomposition, communication, authority and evaluation dependency remain distinct.'
for dep in ['FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.independent-assessment']:
    dependency(r, dep, 'Apply the shared rule to this configuration and its actual grants and review conditions.')

r = edit('FOUNDATIONS.core-contract-derivations')
r['definition']['meaning'] = f'{len(families)} source-bound conditional family arguments connect their actual consumers, applicable premises/pillars, consequences and owner choices; linked bodies own the decisions.'
r['definition']['source_family_arguments'] = families
for dep in ['FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.independent-assessment']:
    dependency(r, dep, 'The family argument explains the linked deciding owner and creates no second rule.', 'assessing this argument and its deciding consumer')

r = edit('TRANSFORMATION_LIBRARY.contract-application')
r['obligations'][0]['conditions']['Authority'] = 'Apply Foundations Judgment and authority to the actual operation/decision grant for this subject and effect. Bind required assessment through Independent assessment, retaining the domain additional conditions and authority requiring them.'
plans[r['id']].append(plan('scope obligation', ('O','/obligations/2')))
for dep in ['FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.independent-assessment']:
    dependency(r, dep, 'Apply authority and required assessment at the admission decision under domain conditions.')

r = edit('TRANSFORMATION_LIBRARY.bind')
r['obligations'][0] = 'Recover purpose, subject identity, governing specification, role, authority, state and material relations. Return missing/conflicting/stale bindings explicitly; apply Foundations Judgment and authority to the actual grants and distinct relations.'
dependency(r, 'FOUNDATIONS.judgment-and-authority', 'Resolve the actual instance grants under shared authority conservation.')

r = edit('TRANSFORMATION_LIBRARY.evaluate')
r['obligations'][0] = 'Apply core results to exact predicate/subject/basis, retaining original outcome, performance, effects, citations and residual coverage. The domain evidence rule decides its predicate. Apply Independent assessment where required, and Judgment and authority to evaluation/operation/decision grants; a function or adopted Baseline Reviewer retains its actual domain grant.'
for dep in ['FOUNDATIONS.judgment-and-authority', 'FOUNDATIONS.independent-assessment']:
    dependency(r, dep, 'Apply the shared condition before relying on assessment or exercising an admitted mandate.')

r = edit('TRANSFORMATION_LIBRARY.dispose')
r['obligations'].append('Apply Judgment and authority to the current mandate and exact subject; consume closed work/evaluation results and select only a permitted disposition. The decision is separate from its assessment and returns its own predicate-bound core result.')
plans[r['id']] = [plan('obligation result scope', ('O','/obligations/3'))] + plans[r['id']]
dependency(r, 'FOUNDATIONS.judgment-and-authority', 'Apply the actual decision mandate without deriving it from the assessment.')

new_id = 'FOUNDATIONS.independent-assessment'
new = {k: copy.deepcopy(v) for k,v in old['FOUNDATIONS.judgment-and-authority'].items()
       if k in {'inputs','result_mapping','scope_refs','representation_kind'}}
new.update({'id': new_id, 'family': 'Independent assessment',
            'owner': make_owner('standards/FOUNDATIONS.md','independent-assessment',source['standards/FOUNDATIONS.md']),
            'coverage_standing':'bounded_author_binding', 'interpretation_standing':'bounded_semantic_binding',
            'predicate':'An assessment meets the independence conditions required by its governing contract on the exact claim.',
            'applicability':'Only where the governing contract requires independent assessment; the domain retains review boundaries, additional exposure/trace conditions and reserved decisions.',
            'obligations':[
                'Bind whether independent assessment is required and its authorship, evidence, reference-exposure, actor and configuration conditions. Required nonauthor assessment excludes material authorship of the subject or repair. Self-review remains authoring evidence even after human acceptance.',
                'A defect, counterexample or identification of already-required behavior does not itself author a repair and may be rechecked. Adopted material wording/policy/design is authorship: disclose it and do not independently assess that claim; retain unaffected judgment scope. Changed subjects/tests/conditions apply evidence-retention rules.',
                'Shared sources/evidence are allowed only under required conditions. Actor identity, fresh context or model-family difference alone proves no independence. Keep statistical shared-cause assurance, frame disjointness, procedural independence and claim-relative nonauthor assurance distinct.'],
            'permissions_exceptions':['No additional review boundary, reviewer count or model family follows; governing domains retain their particular requirements.'],
            'dependencies':[], 'dependency_relations':[], 'consumers':[],
            'source_references':[],
            'argument':{'premises':[{'id':x,'kind':'foundational_premise','owner':'FOUNDATIONS.foundational-commitments'} for x in ['F2','F6']],
                        'conditional_consequence':'Where independent nonauthor assessment is required, adopted authorship cannot support that independent claim; reporting a counterexample alone need not author its repair.',
                        'policy_choices':['The governing contract selects independent-review boundaries and additional evidence/exposure/configuration conditions.'],
                        'source_refs':[new_id,'FOUNDATIONS.foundational-commitments'],
                        'source_family_arguments':[x for x in families if '(#independent-assessment)' in x['family']],
                        'standing':'authored_conditional_argument_not_independent_entailment_proof'}})
new['inputs'] = [{'kind':'authority','description':'The governing contract and exact independence conditions it requires for this claim.','required_when':'independence is claimed or required','standing':'external_required'},
                 {'kind':'observation','description':'Material authorship, exposure and evidence provenance for the exact assessment and subject.','required_when':'needed to establish the selected independence conditions','standing':'external_required'}]
new['result_mapping'] = copy.deepcopy(old['FOUNDATIONS.judgment-and-authority']['result_mapping'])
new['result_mapping']['owner_refs'] = ['FOUNDATIONS.result-algebra', new_id]
for dep,when in [('FOUNDATIONS.change-impact-and-evidence-retention','relying on former evidence after change'),('FOUNDATIONS.parallel-assurance-and-provenance','assessing shared causes or provenance'),('REFERENCE_FRAME_METHOD.disjointness-and-independence','claiming frame disjointness or procedural evaluation independence')]:
    dependency(new,dep,'Apply the distinct owner; do not substitute its relation for required nonauthor assurance.',when)
blocks(new,[plan('obligation scope',('O','/obligations/0')),
            plan('obligation latitude',('O','/obligations/1')),
            plan('obligation latitude scope',('O','/obligations/2'),('P','/permissions_exceptions/0'))])
new['consumers'] = sorted(r['id'] for r in changed.values() if new_id in r.get('dependencies', []))
authority = changed['FOUNDATIONS.judgment-and-authority']
authority['consumers'] = sorted(set(authority.get('consumers', [])) | {
    r['id'] for r in changed.values() if authority['id'] in r.get('dependencies', [])})

updates=[]
for identifier,row in changed.items():
    blocks(row,plans[identifier])
    unit=units[row['owner']['path']][row['owner']['anchor']]
    fields={k:v for k,v in row.items() if k not in {'id','owner'} and v != old[identifier].get(k)}
    updates.append({'id':identifier,'preimage_body_sha256':old[identifier]['owner']['body_sha256'],
                    'candidate_body_sha256':sha(unit['body']),'semantic_fields':fields})

actual={r['id'] for r in old.values() if r['owner']['path'] in source
        and r['owner']['body_sha256'] != sha(units[r['owner']['path']][r['owner']['anchor']]['body'])}
assert actual == set(changed), ('unaccounted changed sections',actual ^ set(changed))
patch={'schema_version':'stdo.i5.authored-account-patch/v1','common_input':COMMON,
       'source_preimage':PREIMAGE,'producer':'RC1-CONTENT-REPAIR-CORE',
       'owner_paths':sorted(source),'updates':updates,'new_rows':[new]}
(HERE/'ACCOUNT_PATCH.json').write_text(json.dumps(patch,indent=2,ensure_ascii=False)+'\n')
checks={'kind':'bounded_author_account_checks','subject':[{ 'path':p,'sha256':sha(b),'bytes':len(b)} for p,b in source.items()],
        'prior_account':str(PRIOR_PATH.relative_to(TENANT)),'prior_account_sha256':sha(PRIOR_PATH.read_bytes()),
        'preimage_members_match_prior_account':True,'changed_immediate_sections_accounted':sorted(actual),
        'new_sections':[new_id],'paragraph_role_pointers_resolved':True,'family_arguments':len(families),
        'limitations':['Authored semantic account, not independent fidelity review.','No generated assets, full account integration, package check or actual-use trial performed.','Integration must preserve prior account fields and establish the reverse consumer projection from the complete merged account.']}
(HERE/'ACCOUNT_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({'updated_sections':len(updates),'new_sections':1,'family_arguments':len(families)}))
