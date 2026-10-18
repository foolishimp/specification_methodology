#!/usr/bin/env python3
"""Reproduce this bounded author's contribution. No source or account mutation."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[8]
BASE = 'specification_methodology/v3/build_tenants/codex/'
SOURCE = 'f2cb3e593757d094d008102551925e871a0204ff'
ACCOUNT_COMMIT = 'fe4fcbe'
ACCOUNT_SHA = 'ae5169eea86204a0d5d27915c6935604bb09d8d9a4feeb6cc403706a0ac42b12'
OWNERS = ('SPEC_METHOD', 'TICKET_METHOD', 'RELEASE_METHOD', 'POSTING_GUIDE', 'WRITING_GUIDE')

def show(commit, path):
    return subprocess.check_output(['git', '-C', str(ROOT), 'show', commit + ':' + path])

account_bytes = show(ACCOUNT_COMMIT, BASE + 'qualification/C3/iteration-3/DETERMINATIONS.json')
assert hashlib.sha256(account_bytes).hexdigest() == ACCOUNT_SHA
account = json.loads(account_bytes)
assert account['schema_version'] == 'stdo.determinations.v1.3'
rows = {r['id']: r for r in account['determinations']}
bindings = []

CORE = ['FOUNDATIONS.result-algebra', 'FOUNDATIONS.workspace-and-context']
ARGUMENTS = {
    'POSTING_GUIDE': (['F2', 'F6'], 'Evidence-bound interpretation and separate authority imply that commentary preserves basis and cannot confer adoption. The carrier, categories, discussion lifecycle and propagation chain are adopted guide policy.'),
    'WRITING_GUIDE': (['F1', 'F2', 'F4', 'F5'], 'Given a writing purpose and an authoritative layer, an adequate revision preserves meaning, material obligations and sufficient relevant context. Style, tense and vocabulary preferences are adopted policy, not consequences of a byte limit.'),
    'RELEASE_METHOD': (['F2', 'F3', 'F4', 'F6'], 'Given an adopted immutable release boundary, qualification and reuse must bind the same subject, preserve its material assets and distinguish evidence from publication authority. Version naming, phase order, cut/cohort transactions and required evidence are release policy.'),
    'TICKET_METHOD': (['F1', 'F2', 'F3', 'F4', 'F6'], 'Given an adopted work contract, scope, evidence, authority and preserved obligations determine lawful execution and closure. Ticket/sprint carriers, workflow labels, admission and migration policies are local method choices, not deductions from finitude.'),
    'SPEC_METHOD': (['F1', 'F2', 'F3', 'F4', 'F5', 'F6'], 'Within adopted purposeful construction, lawful reliance preserves purpose, interpreted subject, state, material composition, uncertainty and authority. Product boundaries, constitutional hierarchy and the named policy gates below are additional method policy; the premises alone do not select them.')
}

def add(owner, anchor, kind, applicability, meaning, obligations, permissions, inputs, deps=(), result=None, policy=None):
    rid = owner + '.' + anchor
    old = rows[rid]
    is_data = kind in ('definition_data', 'non_deciding_locator')
    premises, consequence = ARGUMENTS[owner]
    dependencies = list(dict.fromkeys(list(deps) + old.get('dependencies', [])))
    for dep in dependencies:
        assert dep in rows, (rid, dep)
    binding = {
        'id': rid,
        'owner_body_sha256': old['owner']['body_sha256'],
        'source_member_sha256': next(m['sha256'] for m in account['source_members'] if m['path'] == old['owner']['path']),
        'owner': old['owner'],
        'representation_kind': kind,
        'interpretation_standing': 'bounded_semantic_binding' if kind != 'non_deciding_locator' else 'non_deciding_source_locator',
        'applicability': applicability,
        'predicate': None if is_data else meaning,
        'definition': meaning if is_data else None,
        'obligations': obligations,
        'permissions_exceptions': permissions,
        'dependencies': dependencies,
        'dependency_relations': [{'id': dep, 'kind': 'contract_application'} for dep in dependencies] + [{'id': 'FOUNDATIONS.foundational-commitments', 'kind': 'conditional_foundation_argument'}] + [rel for rel in old.get('dependency_relations', []) if rel['kind'] != 'contract_application' and rel['id'] not in dependencies],
        'inputs': [{'kind': 'external_world_or_authority', 'description': value, 'required_when': applicability, 'standing': 'external_required'} for value in inputs],
        'result_mapping': {
            'kind': 'definition_with_embedded_constraints' if is_data else 'predicate_result',
            'owner_refs': ['FOUNDATIONS.result-algebra', 'FOUNDATIONS.result-conjunction'],
            'conditions': result or ('The definition supplies data and scoped obligations, not a Boolean verdict. Evaluate any asserted compliance, adoption or use claim separately on the named obligations; category/status/name alone proves neither performance nor authority.' if is_data else 'Evaluate this exact scoped predicate using authenticated observations: established failure is falsified; complete admissible support is satisfied; undecided material conditions are indeterminate; an established scope or governing-interpretation defect gives out_of_frame or invalid_basis. Preserve actual performance, effects, unresolved coverage and original domain data. Operation or decision permission is a distinct claim.'),
            'standing': 'author_semantic_mapping_not_independently_qualified'
        },
        'argument': {'premises': premises, 'conditional_consequence': consequence, 'policy_choices': policy or [meaning], 'source_refs': [rid, 'FOUNDATIONS.foundational-commitments'], 'standing': 'authored_conditional_argument_not_independent_proof'},
        'source_clause_ids': [rid + '#' + c['id'] for c in old.get('source_clauses', [])],
        'unrepresented_scope': []
    }
    assert not any(b['id'] == rid for b in bindings), rid
    bindings.append(binding)

# Explicit authored local bindings, grouped by source owner.
P = 'POSTING_GUIDE'
add(P,'posting-guide','definition_data','Repository commentary governed by the Product-bound commentary surface.',
    'A post carries analysis, criticism, proposals, handoff or confidence repricing as working commentary; its influence on specification or design requires a separate owning adoption.',
    ['Preserve observations and proposals as commentary, with the governing source distinguishable.'],
    ['Commentary can inform later specification or design decisions.'], [], ['FOUNDATIONS.judgment-and-authority'])
add(P,'boundary','constraint','Publishing a review, handoff, or other provisional, investigative, comparative or argumentative post.',
    'The post retains its subject and basis and reports any judgment through a sufficient core result; it does not stand in for live requirements, ratified design, active process law or an absent decision.',
    ['Bind subject and basis before publication.', 'Carry judgment evidence, performance, limits and authority distinctly; a concise sufficient reference may carry the record.', 'Put live truth in the bound WHAT or ratified design owner.'],
    ['Use commentary for material not yet ratified.'], ['Actual post, bound subject/basis, judgment evidence and any adoption decision.'], CORE + ['FOUNDATIONS.judgment-and-authority'])
add(P,'location','definition_data','Resolving the commentary carrier of a Product Definition Overlay.',
    'ticketing.comments.root selects the commentary carrier. The default is .ai-workspace/comments/<agent>/; the binding may instead select a directory, repository resource, board, API collection or product query.',
    ['Every bound carrier preserves commentary versus authority; location or visibility supplies no ticket, Product, requirement or design standing.'],
    ['An existing project may select a different carrier.'], ['Selected Product Definition comments binding.'])
add(P,'carrier-identity','definition_data','Naming a post in its selected carrier.',
    'Local files use YYYYMMDDTHHMMSS_CATEGORY_SUBJECT.md. Equivalent non-file identity retains publication time, category, subject, author, discussion state and supersession history.',
    ['Use the stated local-file format; non-file carriers preserve the listed identity coordinates.'],
    ['A short, specific, stable subject is recommended.'], ['Carrier kind and post identity metadata.'])
add(P,'categories','definition_data','Classifying a post.',
    {'REVIEW':'critique of code, spec, design or a post','STRATEGY':'proposed technical or methodological direction','GAP':'precise insufficiency or contradiction','SCHEMA':'data/event/interface/contract shape','HANDOFF':'bounded context or task-state transfer','MATRIX':'explicit option comparison'},
    ['Use a category appropriate to the post subject.'], [], ['Actual post purpose.'])
add(P,'structure','definition_data','Authoring a post; MATRIX selects a decision table.',
    'Base shape: category and subject title; Author, ISO Date, Addresses and Status (initially Draft), optional Updated; Summary, Analysis and Recommended Action.',
    ['For MATRIX, make the central section a decision table.'], ['Updated is optional.'], ['Post type and metadata.'])
add(P,'discussion-state-and-mutability','definition_data','Updating a post according to its discussion state and bounded subject.',
    {'Draft':'author is shaping the post','Open':'published into an active discussion','Closed':'discussion concluded'},
    ['Draft/Open revisions on the same bounded discussion update the same post, including corrections, replies, recommendations, confidence and relevant evidence.', 'Preserve Date as first publication when updating; make discussion state explicit.', 'Closed records remain commentary until content is explicitly adopted.'],
    ['Add/update Updated when useful.', 'Editing Closed is discouraged, not categorically forbidden; prefer a new post for a materially changed conclusion, reopened dispute or new subject.'], ['Discussion status, subject continuity, first publication and materiality of proposed change.'])
add(P,'posting-rules','constraint','Publishing or revising a post.',
    'One bounded subject is stated with labeled current/target claims, separate findings and recommendations, exact claim references and truthful unratified standing; closed history is not covertly rewritten.',
    ['Label whether current reality, target direction or both.', 'Separate findings and recommendations; cite exact file or requirement for claims.', 'Do not claim ratification or stealth-rewrite closed history.'],
    ['Open posts may change in place; closed posts should normally be superseded.'], ['Post text, cited claims and discussion history.'])
add(P,'ratification','constraint','Claiming normative consequence from post content.',
    'Content has governing consequence only through explicit adoption into bound WHAT, ratified design or accepted implementation; without it the post remains commentary.',
    ['Resolve the adopting surface and its owning decision; publication itself is not ratification.'], [], ['Explicit owner adoption and adopted content identity.'], ['FOUNDATIONS.judgment-and-authority'])
add(P,'shared-method-adoption-and-propagation-stdo-up-012','constraint','Propagating a reusable method change or accompanying executable asset.',
    'Evidence reaches consumer realization through shared-method intake, one owning standard, consistency and independent review, human acceptance, one complete released STDO version and explicit consumer selection.',
    ['Keep one law owner; other standards consume the admitted law by reference.', 'Consumers select a complete release and own their realization/evidence.', 'Tool/runtime/carrier-schema/assurance implementations require separate Product authorization.'],
    ['The causal authority chain does not prescribe a particular intake workflow or artifact set.'], ['Incident evidence, review independence, acceptance, exact release and consumer selection; separate asset authorization when relevant.'], ['RELEASE_METHOD.successor-baseline-conservation-stdo-up-015'])

W = 'WRITING_GUIDE'
add(W,'writing-guide','consumer_binding','Writing or compressing method text for an interpreted task context.',
    'The text preserves its governing layer and every material determination needed by the reader; shortening by itself establishes no semantic or operational improvement.',
    ['Judge sufficiency and preservation on the selected task and source meaning.'], [], ['Source meaning, reader task and resulting text.'], ['TRANSFORMATION_LIBRARY.faithful-projection'])
add(W,'core-rule','constraint','Technical prose intended for the guide\'s fluent reader.',
    'The prose states its claim and reason without performative setup, respecting a technically fluent reader with limited time.',
    ['State claim and reason; remove surrounding performance.'], [], ['Actual prose and intended audience.'])
add(W,'style-rules','constraint','Applying the guide\'s writing style to technical text.',
    'Prose uses direct concrete claims, precise vocabulary and useful examples, while removing announced setup and transitions that add only tone.',
    ['Remove section-announcing setup and filler transitions.', 'Use concrete nouns/verbs; examples must reduce ambiguity.'],
    ['Prefer positive statements and precise technical vocabulary; one claim per sentence when possible.'], ['Actual prose, ambiguity and intended technical meaning.'])
add(W,'remove-these-habits','constraint','Editing tone-only habitual phrasing.',
    'Remove generic reassurance, dramatic phrasing and the listed habitual contrast/intensifier/promotional expressions when they add tone rather than information.',
    ['Check not-X-but-Y, simply, just, clearly, obviously, powerful, robust, seamless and game-changing for the guide\'s removal rule.'],
    ['The source says these usually add no information; it does not make every literal occurrence an independent forbidden token.'], ['Phrasing and whether it carries material information.'])
add(W,'good-prose','constraint','Assessing technical prose under this guide.',
    'Prose is factual, bounded, explicit about authority and uncertainty, and open to challenge; a polished sentence with no new constraint or observation is cut.',
    ['Retain evidential and authority limits; cut information-free polished sentences.'], [], ['Sentence meaning and evidence.'])
add(W,'bad-prose','definition_data','Diagnosing prose problems.',
    'Diagnostic defects are ungrounded implied conclusions, repeated claims, unlabeled current/target mixing, basic explanation to expert readers and branding of straightforward instructions.',
    [], [], ['Actual text and reader context.'])
add(W,'method-alignment','consumer_binding','Choosing tone for the governing authority layer.',
    'Method prose is constitutional, requirements normative, design structural and commentary analytical; mismatched tone is rewritten without changing its authority.',
    ['Match the text to its actual layer and rewrite a mismatch.'], [], ['Surface role and actual text.'], ['SPEC_METHOD.constitutional-chain'])
add(W,'specification-artifact-practice','constraint','Writing specification artifacts governed by SPEC_METHOD.',
    'Each sentence states current live truth in its proper layer, preserves only live law and includes design detail only when that detail is constitutional.',
    ['SPEC_METHOD owns layer roles and closure.', 'Cut informative-looking sentences that change no authority, constraint or derivability; remove stale law within authority.'],
    ['Design detail is allowed in a constitutional layer when itself constitutional.'], ['Current owning source, constitutional role and proposed sentence.'], ['SPEC_METHOD.constitutional-chain'])
add(W,'practical-layer-checks','constraint','Revising or reviewing a specification artifact.',
    'Acquire the current owner; the resulting artifact enables downstream derivation, states current truth and keeps each sentence in its rightful layer while preserving predecessor dispositions.',
    ['If a layer/currentness/derivability answer is wrong, rewrite or delete within owning authority.', 'Review the actual preservation/style predicate through the core result; retain required UP-015 authority and disposition.'],
    ['Style choices are conventions; no byte limit entails them and shorter text proves neither preservation nor style.'], ['Current source, proposed revision, downstream derivability and authorized predecessor dispositions.'], CORE + ['RELEASE_METHOD.successor-baseline-conservation-stdo-up-015'])
add(W,'current-surface-writing','constraint','Maintaining active constitutional specification during a change wave.',
    'The active surface states current law in present tense and contains no dead law; removal, supersession or transfer to commentary follows owning authority and applicable recorded UP-015 disposition.',
    ['Use explicit version labels only for immutable release facts, explicit mutable selector bindings or clearly historical material.'],
    ['For change waves prefer active/current/base/live/shared/tenant-local terminology.', 'Authorized deletion, supersession and movement to commentary are alternatives.'], ['Live/dead determination, intended version use and owner authority.'], ['RELEASE_METHOD.successor-baseline-conservation-stdo-up-015'])

def emit():
    selected = [r for r in rows.values() if r['id'].split('.')[0] in OWNERS]
    done = {b['id'] for b in bindings}
    missing = [r['id'] for r in selected if r['id'] not in done]
    out = {'schema_version': 'stdo.semantic-contribution.v1', 'input_account_sha256': ACCOUNT_SHA,
           'source_commit': SOURCE, 'account_commit': ACCOUNT_COMMIT,
           'grant': 'I3-R2-ACCOUNT-COMPLETE-01', 'execution_contract': 'EC-CODEX-I3-02',
           'common_input': '355aa8655cca9c6ba6cf5c414f9bea3032ae89fd',
           'installed_builder_manifest_sha256': '3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782',
           'owner_paths': ['standards/' + o + '.md' for o in OWNERS],
           'bindings': bindings, 'unchanged_ready_ids': [], 'unfinished_source_ids': missing,
           'standing': 'bounded_author_contribution_not_acceptance'}
    payload = json.dumps(out, indent=2, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        assert (HERE / 'bindings.json').read_text() == payload, 'bindings.json is not reproducible from authored bindings'
    else:
        (HERE / 'bindings.json').write_text(payload)
    print(json.dumps({'bindings': len(bindings), 'unfinished': len(missing)}))

if __name__ == '__main__':
    for part in ('release_bindings.py', 'ticket_bindings.py', 'spec_bindings.py', 'spec_change_bindings.py', 'spec_execution_bindings.py', 'spec_final_bindings.py', 'discriminator_models.py'):
        if (HERE / part).exists():
            exec(compile((HERE / part).read_text(), str(HERE / part), 'exec'), globals())
    emit()
