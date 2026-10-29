#!/usr/bin/env python3
"""Prepare exact public-tool inputs; never run a gate, actor, or dispatch.

Template mode writes source-only plans with an inadmissible checker placeholder.
Finalization additionally requires a separately supplied Executive selection,
exact checker/source pins and two existing fresh task workspaces. It stages the
reviewed inputs there. Operator authority is an external premise, not something
this program authenticates by accepting a JSON document.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parent
PREP = BASE.parent
PRODUCT = BASE.parents[4]
CODE = PRODUCT / 'build_tenants/graphify/code'
sys.path.insert(0, str(CODE))
import ac_support_core as core

TASK_SHA = '33e08813021b43a259dc72aa35f904f82b370de25faff64488f29ee4d4495829'
PROTOCOL_SHA = '547a73826a8bd28721661361106d5a8e53844ca3a3a8b2a10dd5b66d7a2ae4f6'
ARMS = ('ungated', 'gated')
TOOLS = ['local-shell-files', 'python3-stdlib']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_bytes())


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        stream.write(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + '\n')


def ref(path, root, base, selector=None):
    path = Path(path)
    return {'engine': 'workspace-regular-file', 'root': root,
            'path': str(path.relative_to(base)), 'object': None,
            'sha256': sha(path), 'selector': selector}


def object_schema(fields):
    return {'type': 'object', 'properties': fields, 'required': list(fields),
            'additionalProperties': False}


def output_schema(fixed, predicate):
    strings = {'type': 'array', 'items': {'type': 'string'}}
    source = object_schema({'engine': {'const': 'workspace-regular-file'},
        'root': {'const': 'task'}, 'path': {'type': 'string'}, 'object': {'type': 'null'},
        'sha256': {'type': 'string', 'pattern': '^[0-9a-f]{64}$'}, 'selector': {'type': 'null'}})
    candidate = copy.deepcopy(source)
    candidate['properties']['path'] = {'const': 'support/candidate.json'}
    evidence = {'type': 'array', 'items': source}
    evaluation = object_schema({'id': {'type': 'string'}, 'predicate': {'const': predicate},
        'domain_outcome': object_schema({'command': {'type': 'string'},
            'exit_code': {'type': 'integer'}, 'observation': {'type': 'string'}}),
        'core_value': {'enum': ['satisfied', 'falsified', 'indeterminate', 'out_of_frame', 'invalid_basis']},
        'evidence': evidence, 'residuals': strings, 'invalidators': strings})
    work = object_schema({'value': {'enum': ['candidate_ready', 'refused', 'incomplete', 're_entry_requested']},
        'cause': {'type': 'string'}, 'candidate': {'anyOf': [candidate, {'type': 'null'}]},
        'evidence': evidence, 'residuals': strings})
    return object_schema({**{key: {'const': value} for key, value in fixed.items()},
        'evaluations': {'type': 'array', 'items': evaluation}, 'not_performed': strings,
        'work_result': {'anyOf': [work, {'type': 'null'}]},
        'residuals': strings, 'invalidators': strings})


def request(identity, operation, arguments):
    value = {'schema': core.REQUEST, 'id': identity, 'operation': operation, 'arguments': arguments}
    core.validate_request(value)
    return value


def prepare(out, workspaces, checker, selection, template):
    out = out.absolute()
    if out.exists() or not out.is_relative_to(BASE):
        raise ValueError('Plan output must be a fresh directory inside this granted runtime preparation')
    if sha(PREP / 'TASK.md') != TASK_SHA or sha(PREP / 'PROTOCOL.md') != PROTOCOL_SHA:
        raise ValueError('Reviewed task/protocol changed')
    receipt = read(BASE / 'owner-binding/RECEIPT.json')
    ticket = PRODUCT / '.ai-workspace/tickets/active/T-013-practical-formal-gate.md'
    definition = PRODUCT / 'stdo_a_c.json'
    if sha(ticket) != receipt['ticket_after_sha256'] or sha(definition) != receipt['definition_sha256']:
        raise ValueError('Selected Product/T013 authority source advanced; re-enter source selection')
    lines = ticket.read_text().splitlines(keepends=True)
    start, end = receipt['selected_owner_lines']
    owner = json.loads(''.join(lines[start - 1:end]))
    selected_path = read(definition)['reference_frame_bases'][0]['authority'][6].split('#')[0]
    if (PRODUCT / selected_path).resolve() != ticket.resolve():
        raise ValueError('Actual Product owner locator does not resolve T013')
    if owner['mechanism']['implementation_sha256'] != sha(CODE / 'ac_support_core.py'):
        raise ValueError('Owner-selected admission implementation advanced')
    cli = read(PREP / 'transport/CLI_INSPECTION.json')
    native = cli['selected_native']
    python = cli['helper_python']
    for selected in (native, python):
        expected = selected.get('sha256', selected.get('raw_sha256'))
        if sha(selected['path']) != expected:
            raise ValueError('Selected native CLI/helper interpreter advanced')
    native_pin = {'path': native['path'], 'sha256': native['raw_sha256']}
    python_pin = {'path': python['path'], 'sha256': python['sha256']}
    code_paths = [CODE / name for name in ('ac_graph.py', 'ac_support.py', 'ac_support_core.py',
                  'ac_support_effects.py', 'ac_support_composition.py', 'ac_formal_gate.py')]
    helper = PRODUCT / 'build_tenants/graphify/examples/fd-support/actor_cli.py'
    current_pins = {str(p): sha(p) for p in [*code_paths, helper]}
    if not template:
        if selection.get('schema') != 'a_c.T013.execution-selection/1' or selection.get('state') != 'selected':
            raise ValueError('A separate exact Executive execution selection is required')
        for key, expected in [('task_sha256', TASK_SHA), ('protocol_sha256', PROTOCOL_SHA),
                              ('ticket_sha256', receipt['ticket_after_sha256']), ('source_pins', current_pins)]:
            if selection.get(key) != expected:
                raise ValueError('Executive selection mismatch: ' + key)
        if selection.get('maximum_invocations_per_arm') != 1 or selection.get('automatic_retry') is not False:
            raise ValueError('Invocation allowance differs')
        if selection.get('checker_config_sha256') != core.digest(checker):
            raise ValueError('Selected checker configuration differs')
        core.ac_formal_gate.validate_config(checker)  # Shape/pins only; never invokes checker.
        if any(not p.is_dir() or p.is_symlink() or any(p.iterdir()) for p in workspaces.values()):
            raise ValueError('Each actual workspace must already exist, be regular and empty')
        if workspaces['ungated'] == workspaces['gated'] or any(p.is_relative_to(PRODUCT) for p in workspaces.values()):
            raise ValueError('Actual workspaces must be distinct and outside protected Product source root')
    out.mkdir(parents=True)
    write(out / 'execution-selection.json', selection)
    delivery = read(PREP / 'transport/DELIVERY_INPUTS.json')['files']
    model_selection = read(PREP / 'shared/MODEL_SELECTION.json')
    model_path = PRODUCT.parent / model_selection['model']['source']
    if sha(model_path) != model_selection['model']['raw_sha256']:
        raise ValueError('Full frozen model bytes changed')
    shared_refs = []
    for item in delivery:
        path = PREP / item['from']
        if sha(path) != item['sha256']:
            raise ValueError('Reviewed delivery input changed: ' + item['from'])
        if not item['render'].startswith('model projection'):
            shared_refs.append(ref(path, 'prepared', PREP))
    profile_path = PRODUCT / 'build_tenants/graphify/design/fd-method-claude-rc9.json'
    method = {'id': core.PROFILE_ID, 'sha256': core.PROFILE_SHA256}
    task_ref = ref(PREP / 'TASK.md', 'prepared', PREP)
    owner_ref = ref(ticket, 'product', PRODUCT, {'lines': [start, end]})
    definition_ref = ref(definition, 'product', PRODUCT)
    selection_ref = ref(out / 'execution-selection.json', 'operator', out)
    manifest = {'schema': 't013.runtime-preparation.manifest/1', 'template_only': template,
                'source_pins': current_pins, 'arms': {}, 'checker_config': checker,
                'execution_selection_sha256': sha(out / 'execution-selection.json')}
    for arm in ARMS:
        folder = out / arm
        folder.mkdir()
        workspace = workspaces[arm]
        if not template:
            for item in delivery:
                target = workspace / item['to']
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open('xb') as stream:
                    stream.write((PREP / item['from']).read_bytes())
            (workspace / 'support').mkdir()
            (workspace / 'scratch').mkdir()
        actor_id = 't013-report-' + arm + '-worker-001'
        territory = [{'root': 'task', 'path': name, 'kind': kind} for name, kind in
            [('gate_report.py', 'file'), ('test_gate_report.py', 'file'), ('README.md', 'file'),
             ('support', 'directory'), ('scratch', 'directory')]]
        arm_source = {'schema': 'a_c.T013.worker-activation/1', 'actor_id': actor_id,
            'role': 'Worker', 'frame': 't013-report-helper-frame', 'revision': '1',
            'workspace': str(workspace), 'territory': territory,
            'task_sha256': TASK_SHA, 'maximum_invocations': 1,
            'tools': TOOLS, 'additional_files': 'Only support/ and scratch/; inputs/ immutable.',
            'stops': ['input/currentness mismatch', 'permission unavailable', 'task timeout',
                      'outside-scope source required', 'attempt already used'],
            'prohibited': ['additional agents/models', 'network acquisition', 'other arm/evaluator read',
                           'tenant private proof/origin read', 'credential read', 'Git or release'],
            'method_boundary': 'Existing selected Claude-RC9 support profile under unchanged STDO 2.5.1 RC2 builder; represented common model is subject data.'}
        write(folder / 'activation.json', arm_source)
        arm_ref = ref(folder / 'activation.json', 'operator', out)
        contract = {'schema': 'a_c.fd-support.return-contract/1', 'id': 't013-report-return-' + arm,
            'authority_source': owner_ref, 'carrier': 'a_c.fd-support.closed-return/1',
            'output_slot': 'final_stdout_object', 'required_evaluations': [], 'role': 'Worker',
            'proof': {'transition_sources': [task_ref, arm_ref], 'predicate_ids': []}}
        core.validate_content(contract, 'ReturnContract')
        write(folder / 'return-contract.json', contract)
        return_ref = ref(folder / 'return-contract.json', 'operator', out)
        subject = {'id': 'urn:a-c:T013:report-helper:001', 'sha256': TASK_SHA}
        packet = {'activation': {'id': actor_id + ':activation', 'revision': '1', 'configuration': arm_ref},
            'frame': {'id': 't013-report-helper-frame', 'revision': '1', 'declaration': task_ref,
                      'evaluation': task_ref, 'result_algebra': return_ref},
            'subject_basis': {'subject': subject, 'method_profile': method,
                'product': {'id': 'urn:stdo:product-definition:a-c-implementations', 'definition': definition_ref},
                'observations': [], 'dependencies': [task_ref, owner_ref, selection_ref],
                'time_basis': 'Exact pinned sources freshly rechecked before each dependent operation.'},
            'attention': {'material_relations': [task_ref], 'invariants': [task_ref],
                'semantic_sources': shared_refs, 'exclusions': ['Hidden evaluator cases and other-arm outputs'],
                'prohibited_assumptions': ['Saved result authenticates itself', 'Proof grants authority',
                                          'Unknown cost is zero', 'Parent model equals child model']},
            'actor_authority': {'actor_id': actor_id, 'role': 'Worker', 'capability': arm_ref,
                'semantic': None, 'evaluation': task_ref, 'operation': owner_ref,
                'decision': None, 'acceptance': None, 'publication': None,
                'territory': territory, 'tools': TOOLS},
            'evidence_relations': {'admissible_evidence': [task_ref], 'acquisition': shared_refs,
                'dependencies': [task_ref], 'conjunction': None, 'translation': None,
                'consumer': '/root', 'return_contract': return_ref},
            'stop_change': {'invalidators': ['Any selected source, policy or activation change'],
                'stop_conditions': arm_source['stops'], 'residuals': ['Semantic acceptance remains external'],
                're_entry': ['Return to Executive on blocked input or authority'], 'reconfiguration': []},
            'profile_additions': {'worker': {'operation_grant_id': 'task',
                'mutation_subject': subject, 'territory': territory}}}
        fixed = {'schema': 'a_c.fd-support.closed-return/1', 'id': actor_id + ':return',
            'frame': {'id': packet['frame']['id'], 'revision': '1'},
            'activation': core.activation_identity(packet), 'subject': subject,
            'basis': {'method_profile': method, 'observations': []},
            'actor': {'id': actor_id, 'family': 'codex-native-default', 'authorship': actor_id},
            'consumer': '/root'}
        write(folder / 'packet.json', packet)
        write(folder / 'return-fixed-fields.json', fixed)
        write(folder / 'return.schema.json', output_schema(fixed, task_ref))
        # Deliver this as an additional declared Context source, avoiding a
        # circular packet/activation hash binding.
        instruction = {'schema': 'a_c.T013.return-instructions/1', 'fixed': fixed,
            'instruction': 'Implement the supplied exact TASK in your own workspace. Return one strict closed-return JSON object with these fixed fields. Report actual local checks only; no independent acceptance. All extra task files belong in support/ or scratch/. Preserve actual test output in support/test-output.txt. Write support/candidate.json listing every deliverable with its raw SHA-256 and byte length, excluding that manifest itself. A candidate_ready return uses a SourceRef to that exact manifest and nonempty evidence SourceRefs to actual local test/output files. SourceRef engine is workspace-regular-file, root is task, path is workspace-relative, object and selector are null, sha256 hashes exact raw file bytes. No extra models/agents/network/outside reads.'}
        write(folder / 'return-instructions.json', instruction)
        instruction_ref = ref(folder / 'return-instructions.json', 'operator', out)
        extra_sources = [*shared_refs, instruction_ref]
        model_ref = {'source': ref(model_path, 'product', PRODUCT), 'format': 'model',
            'model_id': model_selection['model']['id'], 'model_sha256': model_selection['model']['canonical_sha256']}
        context_args = {'packet': packet, 'models': [{'model': model_ref, 'selections': model_selection['selections']}],
            'sources': extra_sources, 'late_acquisition': [],
            'envelope': {'capacity_bytes': None, 'boundary': 'executor-stdin-utf8',
                         'host_context': {'state': 'unknown', 'bytes': None, 'evidence': None}}}
        write(folder / 'context.request.json', request(actor_id + ':context', 'context.assemble', context_args))
        plan = {'schema': 'a_c.fd-support.actor-cli-plan/1', 'id': actor_id + ':native-plan',
            'backend': 'codex', 'executable': native_pin,
            'argv': [native_pin['path'], 'exec', '--ephemeral', '--ignore-user-config', '--json',
                     '--sandbox', 'workspace-write', '--skip-git-repo-check', '--output-schema',
                     str(folder / 'return.schema.json'), '-'],
            'dependencies': [{'path': str(folder / 'return.schema.json'), 'sha256': sha(folder / 'return.schema.json')}],
            'cwd': str(workspace),
            'environment': {'PATH': str(Path(python_pin['path']).parent) + ':/usr/bin:/bin:/opt/homebrew/bin',
                            'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(workspace / 'scratch')},
            'settings': {'selected_model': None, 'selected_effort': None,
                         'defaults': 'native CLI defaults with ignore-user-config; actual identity unknown until reported'},
            'decoder': 'codex-final-jsonl/1',
            'evidence_directory': str(Path(owner['result_surface']['root']).parent / 'actor-transports' / actor_id),
            'limits': {'max_input_bytes': 2097152, 'max_output_bytes': 16777216,
                       'timeout_ms': 900000, 'termination_grace_ms': 2000}}
        write(folder / 'actor-plan.json', plan)
        operator_files = [p for p in out.rglob('*') if p.is_file()
                          and (p.parent == folder or p == out / 'execution-selection.json')]
        dep_paths = [*code_paths, helper, folder / 'actor-plan.json', folder / 'return.schema.json']
        dependencies = [ref(p, 'product', PRODUCT) if p.is_relative_to(PRODUCT) and not p.is_relative_to(out)
                        else ref(p, 'operator', out) for p in dep_paths]
        native_root = Path(native_pin['path']).parent
        dependencies.append({'engine': 'workspace-regular-file', 'root': 'native', 'path': 'codex',
                             'object': None, 'sha256': native_pin['sha256'], 'selector': None})
        executable = {'id': 'actor', 'executable': python_pin,
            'argv': [python_pin['path'], '-B', str(helper), '--plan', str(folder / 'actor-plan.json'),
                     '--plan-sha256', sha(folder / 'actor-plan.json')],
            'dependencies': dependencies, 'cwd': str(workspace), 'environment': plan['environment'],
            'actor_id': actor_id, 'settings': {'timeout_ms': 1000000, 'termination_grace_ms': 2000,
                'execution_selection': selection}, 'tools': TOOLS,
            'effect_scope': {'cooperative': True, 'filesystem': 'local task workspace',
                             'unknowns': ['OS/provider internals and unreported retries']},
            'stdin_mode': 'context-utf8',
            'stdout_decoder': {'format': 'json', 'pointer': None, 'decode_json_string': False},
            'observers': [{'kind': 'process-end'}]}
        roots = {'product': {'path': str(PRODUCT), 'kind': 'workspace', 'writable': False,
                    'read_scope': [{'path': p, 'kind': 'file'} for p in sorted({
                        'stdo_a_c.json', '.ai-workspace/tickets/active/T-013-practical-formal-gate.md',
                        str(profile_path.relative_to(PRODUCT)), owner['mechanism']['source']['path'],
                        str(model_path.relative_to(PRODUCT)), *[str(p.relative_to(PRODUCT)) for p in [*code_paths, helper]]})]},
            'prepared': {'path': str(PREP), 'kind': 'workspace', 'writable': False,
                         'read_scope': [{'path': item['from'], 'kind': 'file'} for item in delivery]},
            'operator': {'path': str(out), 'kind': 'workspace', 'writable': False,
                         'read_scope': [{'path': str(p.relative_to(out)), 'kind': 'file'} for p in operator_files]},
            'native': {'path': str(native_root), 'kind': 'workspace', 'writable': False,
                       'read_scope': [{'path': 'codex', 'kind': 'file'}]},
            'task': {'path': str(workspace), 'kind': 'workspace', 'writable': True,
                     'read_scope': [{'path': name, 'kind': kind} for name, kind in [('inputs', 'directory'),
                         ('gate_report.py', 'file'), ('test_gate_report.py', 'file'), ('README.md', 'file'),
                         ('support', 'directory'), ('scratch', 'directory')]]}}
        operations = ['tools.describe', 'source.read', 'workspace.observe', 'context.assemble',
                      'contract.preflight', 'dispatch.start', 'dispatch.observe', 'dispatch.cancel',
                      'events.wait', 'return.capture', 'return.check']
        principals = {'executive': {'actor_id': '/root', 'role': 'Executive', 'family': 'executive',
                'authorship': '/root', 'operations': operations, 'role_binding': owner_ref, 'role_transition': None},
            'worker': {'actor_id': actor_id, 'role': 'Worker', 'family': 'codex-native-default',
                'authorship': actor_id, 'operations': ['tools.describe', 'source.read'],
                'role_binding': arm_ref, 'role_transition': None}}
        basis = {'method_profile': method, 'observations': []}
        predicate = {'id': 'executive-selected', 'source': selection_ref, 'subject': subject, 'basis': basis,
            'input_names': ['executor'], 'expression': {'op': 'equals', 'args': [
                {'input': 'executor', 'pointer': '/settings/execution_selection/state'}, {'literal': 'selected'}]},
            'limits': ['Exact external selection-state guard; JSON and hashes do not authenticate the Executive.']}
        policy = {'schema': 'a_c.fd-support.policy/1', 'id': actor_id + ':policy',
            'product': {'definition_id': 'urn:stdo:product-definition:a-c-implementations',
                'definition': definition_ref, 'authority_binding': {'definition_locator': receipt['definition_locator'],
                    'owner_record': owner_ref, **{k: owner[k] for k in ('mechanism', 'result_surface', 'scope')}}},
            'method_profile': {**method, 'source': ref(profile_path, 'product', PRODUCT)}, 'sources': roots,
            'principals': principals, 'grants': {'task': {'id': 'task',
                'authority_sources': [owner_ref, selection_ref], 'outcome': {'id': subject['id'], 'source': task_ref},
                'principals': ['executive'], 'targets': ['worker'],
                'operations': ['contract.preflight', 'dispatch.start'], 'tools': TOOLS, 'executors': ['actor'],
                'territory': territory, 'preconditions': [selection_ref],
                'admission': {'mechanism_id': owner['mechanism']['id'], 'mechanism_source': owner['mechanism']['source'],
                    'authority_source': owner_ref, 'required_predicates': ['executive-selected'], 'allowed_override_sources': []},
                'notification_sink': 'events'}}, 'predicates': {'executive-selected': predicate}, 'operators': {},
            'executors': {'actor': executable},
            'event_sinks': {'events': {'kind': 'durable-file-events', 'directory': 'events', 'consumer': '/root',
                                     'authority_source': owner_ref, 'retention': 'indefinite'}},
            'independence_policy': None, 'evidence_root': owner['result_surface']['root'],
            'limits': {'max_message_bytes': 33554432, 'max_files': 4096, 'max_bytes': 33554432,
                       'max_history_records': 20000, 'max_wait_ms': 1000, 'max_output_bytes': 16777216,
                       'max_attempt_ms': 1000000, 'min_poll_ms': 100}, 'authority_sources': [owner_ref],
            'formal_gate': {'checker': checker, 'required_targets': ['worker'] if arm == 'gated' else []}}
        write(folder / 'policy.template.json' if template else folder / 'policy.json', policy)
        # Pure read/schema policy cannot perform admission or launch: no executor
        # registry, no mutating operation grant, and no formal checker selection.
        shape = copy.deepcopy(policy)
        shape.pop('formal_gate')
        shape['id'] += ':shape-only'
        shape['executors'] = {}
        shape['grants'] = {}
        shape['principals']['executive']['operations'] = ['tools.describe', 'source.read']
        write(folder / 'policy.shape-only.json', shape)
        runtime = core.Runtime.from_policy(folder / 'policy.shape-only.json', sha(folder / 'policy.shape-only.json'), 'executive')
        acquired = core.read_source(runtime, owner_ref)
        if acquired['selected_sha256'] != sha(BASE / 'owner-binding/SELECTED.json'):
            raise ValueError('Pure public acquisition did not recover exact selected owner JSON')
        # Public packet/request grammar and return contract checks above do not
        # claim that preflight/dispatch can run with the pending checker.
        manifest['arms'][arm] = {'actor_id': actor_id, 'workspace': str(workspace),
            'packet_sha256': sha(folder / 'packet.json'), 'context_request_sha256': sha(folder / 'context.request.json'),
            'policy_sha256': sha(folder / ('policy.template.json' if template else 'policy.json')),
            'actor_plan_sha256': sha(folder / 'actor-plan.json'), 'return_fixed': fixed,
            'owner_acquisition_sha256': acquired['selected_sha256'],
            'public_shape_policy_loaded': True, 'actual_context_created': False}
    write(out / 'MANIFEST.json', manifest)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    parser.add_argument('--template', action='store_true')
    parser.add_argument('--workspace-ungated', type=Path)
    parser.add_argument('--workspace-gated', type=Path)
    parser.add_argument('--checker-config', type=Path)
    parser.add_argument('--execution-selection', type=Path)
    args = parser.parse_args()
    if args.template:
        checker = None
        selection = {'schema': 'a_c.T013.execution-selection/1', 'state': 'pending',
                     'task_sha256': TASK_SHA, 'protocol_sha256': PROTOCOL_SHA,
                     'maximum_invocations_per_arm': 1, 'automatic_retry': False,
                     'reason': 'Final scale/reuse freeze and exact Executive execution selection absent.'}
        workspaces = {arm: Path('/private/tmp/T013_WORKSPACE_NOT_SELECTED') / arm for arm in ARMS}
    else:
        if not all((args.workspace_ungated, args.workspace_gated, args.checker_config, args.execution_selection)):
            parser.error('Finalization requires two fresh workspaces, checker config and Executive selection')
        checker, selection = read(args.checker_config), read(args.execution_selection)
        workspaces = {'ungated': args.workspace_ungated.resolve(), 'gated': args.workspace_gated.resolve()}
    result = prepare(args.out, workspaces, checker, selection, args.template)
    print(json.dumps({'template_only': result['template_only'], 'output': str(args.out),
                      'actor_calls': 0, 'gate_calls': 0, 'context_calls': 0}))


if __name__ == '__main__':
    main()
