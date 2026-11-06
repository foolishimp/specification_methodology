"""Claim-specific consumers for the stable cohort. No caller-defined predicates.

Execution transcripts are retained observations, not attestations of process
origin. Their adequacy is independently reviewed. This consumer additionally
checks prescribed argv, current input bytes, owner output schemas and installed
bytes; a status label or arbitrary JSON pointer cannot establish a capability.
"""
from __future__ import annotations

import json
from pathlib import Path
import stat
import subprocess
import sys

COMMON = 'specification_methodology/v3/build_tenants/common-tools/'
FORMAL = 'a_c/build_tenants/lean/scripts/formal_gate.py'
GRAPH = 'a_c/build_tenants/graphify/code/ac_graph.py'
PROJECT = 'a_c/build_tenants/graphify/code/ac_project.py'
INDEX = 'axiom_indexer/build_tenants/core/code/ac.py'
SKILLS = 'stdo_skills/scripts/manage_skills.py'
INSTALLED = {'installed_native_workflow', 'installed_manager', 'installed_documentation',
             'current_proof_reader', 'installed_graphify', 'installed_lean',
             'current_codex_skills', 'current_claude_skills'}
BROWSER = {'current_3d_2d_layered', 'source_files_navigation'}


def gate():
    import stable_stack_release
    return stable_stack_release


def local_file(name, expected=None, *, root=None, api):
    s = gate(); p = Path(name)
    s.require(p.is_absolute() and '..' not in p.parts, 'installed path must be absolute and contained')
    if root is not None:
        s.require(p.is_relative_to(root), 'installed artifact is outside its qualification workspace')
    for parent in (p, *p.parents):
        s.require(not parent.is_symlink(), 'installed payload redirects: ' + str(p))
    s.require(stat.S_ISREG(p.stat().st_mode), 'installed artifact is not a regular file: ' + str(p))
    raw = p.read_bytes()
    if expected is not None:
        s.require(api.sha256(raw) == expected, 'actual installed artifact differs: ' + str(p))
    return raw


def python_identity(value, api):
    """Keep the selected venv invocation distinct from its physical executable."""
    s = gate(); invocation = Path(value['invocation']); physical = Path(value['executable_realpath'])
    s.require(invocation.is_absolute() and physical.is_absolute() and invocation.resolve(strict=True) == physical,
              'Python invocation/physical executable differs')
    local_file(str(physical), s.digest(value['sha256']), api=api)
    s.require(isinstance(value.get('version'), str) and value['version'].startswith('3.'), 'Python runtime version missing')
    return str(invocation)


def artifact_location(view, ref, api, installation=None):
    s = gate(); s.pinned(view, ref, api, as_json=False)
    if installation is not None:
        mapped = installation['files'].get(ref['path'])
        s.require(mapped is not None, 'current input/producer is not in installed Product inventory: ' + ref['path'])
        local_file(mapped, ref['sha256'], root=Path(installation['workspace']), api=api)
        return mapped
    actual = str(view.root.absolute() / ref['path'])
    local_file(actual, ref['sha256'], api=api)
    return actual


def execution(view, record, api, producer, arguments, *, installation=None, flags=('-B',), inputs=(), stdout_json=True):
    """Check a prescribed command and its exact producer, inputs and output."""
    s = gate(); selected = record['producer']
    s.require(selected['path'] == producer, 'claim requires its prescribed owner producer: ' + producer)
    executable = artifact_location(view, selected, api, installation)
    run = record['execution']; env = run['environment']
    python = python_identity(env['python'], api)
    s.require(run.get('argv') == [python, *flags, executable, *arguments], 'executed argv differs from prescribed current operation')
    s.require(run.get('returncode') == 0, 'required operation did not exit successfully')
    s.require(Path(run['cwd']).is_absolute(), 'execution working directory missing')
    actual_inputs = {(r['path'], r['sha256']) for r in run['inputs']}
    s.require(all((r['path'], r['sha256']) in actual_inputs for r in inputs), 'execution input closure omits a prescribed current input')
    for ref in [*run['inputs'], *run['outputs']]:
        s.pinned(view, ref, api, as_json=False)
    result_ref = record['result']
    s.require((result_ref['path'], result_ref['sha256']) in {(r['path'], r['sha256']) for r in run['outputs']},
              'result is not a retained executed output')
    result = s.pinned(view, result_ref, api)
    stdout = s.pinned(view, run['stdout'], api, as_json=False)
    s.pinned(view, run['stderr'], api, as_json=False)
    if stdout_json:
        s.require(json.loads(stdout) == result, 'actual command stdout differs from retained result')
    return result


def manager_operation(view, operation, installation, manifest, api, command):
    s = gate(); run = operation['execution']; cut = manifest['cohort']['cut']
    manager = installation['manager']; executable = manager['executable']
    local_file(executable['path'], s.digest(executable['sha256']), root=Path(installation['workspace']), api=api)
    expected = [executable['path'], '--store', installation['store'], command, cut]
    if command == 'install':
        expected += ['--repository', manifest['publication']['repository_url']]
    expected += ['--manifest-sha256', manifest['native']['manifest']['sha256']]
    s.require(run.get('argv') == expected and run.get('returncode') == 0, 'manager did not execute the prescribed current ' + command)
    result = s.pinned(view, operation['result'], api)
    s.require(json.loads(s.pinned(view, run['stdout'], api, as_json=False)) == result, 'manager stdout/result differs')
    s.pinned(view, run['stderr'], api, as_json=False)
    expected_root = installation['native_root']
    s.require(result.get('cut') == cut and result.get('uri') == 'stdo://releases/' + cut + '/'
              and result.get('path') == expected_root and result.get('manifest_sha256') == manifest['native']['manifest']['sha256'],
              'actual manager result names a different cut, store or native manifest')
    native = s.pinned(view, manifest['native']['manifest'], api)
    if command == 'install':
        s.require(result.get('status') == 'installed' and result.get('release') == native['release'],
                  'fresh current native installation was not performed')
    else:
        s.require(result.get('valid') is True and result.get('failures') == [] and result.get('manifest') == native,
                  'actual manager did not verify the complete current native manifest')
    return result


def installation(view, ref, manifest, api):
    """Read back all selected Product bytes and the native manifest in one store."""
    s = gate(); value = s.pinned(view, ref, api)
    s.require(value.get('kind') == 'stdo.installed-cohort/1' and value.get('version') == manifest['cohort']['version'],
              'current installed cohort record required')
    expected_subjects = {p: row['subject']['sha256'] for p, row in manifest['products'].items()}
    s.require(value.get('subjects') == expected_subjects and value.get('source_identity_sha256') == manifest['source']['source_identity_sha256'],
              'actual installed cohort must bind current S and all five Product subjects')
    workspace = Path(value['workspace']); store = Path(value['store']); native_root = Path(value['native_root'])
    s.require(workspace.is_absolute() and workspace == workspace.resolve(strict=True) and not workspace.is_relative_to(view.root.absolute()),
              'qualification workspace must be a separate real directory')
    s.require(store.is_relative_to(workspace) and native_root == store / 'releases' / manifest['cohort']['cut'],
              'installed native root does not belong to the declared fresh store')
    expected_files = {row['path']: row for product in manifest['products'].values() for row in product['subject']['members']}
    s.require(value.get('files') and set(value['files']) == set(expected_files), 'installed Product member closure differs')
    for source, destination in value['files'].items():
        raw = local_file(destination, expected_files[source]['sha256'], root=workspace, api=api)
        s.require(len(raw) == expected_files[source]['bytes'], 'installed member length differs')
    native_raw = s.pinned(view, manifest['native']['manifest'], api, as_json=False)
    s.require(local_file(str(native_root / 'manifest.json'), api=api) == native_raw, 'actual installed native manifest differs')
    native = json.loads(native_raw)
    expected = {'standards/' + row['path']: row['sha256'] for row in native['standards']['members']}
    auxiliary = native.get('auxiliary', {})
    s.require(set(auxiliary) <= {'plugin', 'license', 'release_note'}, 'unsupported native auxiliary contract')
    if 'plugin' in auxiliary:
        unit = auxiliary['plugin']
        expected.update({s.path(unit['installed_root']).rstrip('/') + '/' + s.path(row['path']): s.digest(row['sha256']) for row in unit['members']})
    if 'license' in auxiliary:
        unit = auxiliary['license']; expected[s.path(unit['path'])] = s.digest(unit['sha256'])
    if 'release_note' in auxiliary:
        unit = auxiliary['release_note']; expected[s.path(unit['installed_path'])] = s.digest(unit['sha256'])
    actual = {p.relative_to(native_root).as_posix() for p in native_root.rglob('*') if p.is_file() or p.is_symlink()}
    s.require(actual == set(expected) | {'manifest.json'}, 'actual native installed population differs')
    for member, sha in expected.items():
        local_file(str(native_root / member), sha, root=workspace, api=api)
    semantic = s.pinned(view, manifest['source'], api)
    for row in semantic['members'] + semantic['native_contracts']:
        s.require(expected.get(row['path']) == row['sha256'], 'installed native is not the selected semantic source')
    s.require(value['manager'].get('version') == manifest['cohort']['version'], 'installed manager version differs')
    # The wheel/source check in the content gate establishes what must be installed.
    manager_files = manifest['components']['manager']['facts']['source_root'].rstrip('/') + '/'
    source_rows = [row for name, row in expected_files.items() if name.startswith(manager_files) and name.endswith('.py')]
    s.require(source_rows, 'installed manager has no selected source member provenance')
    interpreter = python_identity(value['manager']['python'], api)
    probe = subprocess.run([interpreter, '-I', '-B', '-c',
        'import json,stdo_toolchain;print(json.dumps({"version":stdo_toolchain.__version__,"file":stdo_toolchain.__file__}))'],
        capture_output=True, timeout=30)
    loaded = json.loads(probe.stdout)
    init = manager_files + '__init__.py'
    s.require(probe.returncode == 0 and loaded == {'version': manifest['cohort']['version'], 'file': value['files'][init]},
              'actual installed manager runtime does not load the selected current source')
    fresh_verify = subprocess.run([interpreter, '-I', '-B', '-m', 'stdo_toolchain.cli', '--store', value['store'],
        'verify', manifest['cohort']['cut'], '--manifest-sha256', manifest['native']['manifest']['sha256']],
        capture_output=True, timeout=60)
    s.require(fresh_verify.returncode == 0 and json.loads(fresh_verify.stdout) == s.pinned(view, value['verify']['result'], api),
              'actual installed manager verification differs from retained evidence')
    manager_operation(view, value['install'], value, manifest, api, 'install')
    manager_operation(view, value['verify'], value, manifest, api, 'verify')
    return value


def model_facts(view, manifest, api):
    s = gate(); facts = manifest['components']['representation']['facts']
    raw = s.pinned(view, facts['model'], api, as_json=False); model = json.loads(raw)
    canonical = api.canonical_value_sha256(model)
    s.require(facts['model_sha256'] == api.sha256(raw) and facts['model_canonical_sha256'] == canonical,
              'selected model raw/canonical identities differ')
    return facts, {'id': model['id'], 'sha256': canonical, 'profile': model['profile']}


def skills(view, record, claim, manifest, api, installed):
    s = gate(); host = 'codex' if claim == 'current_codex_skills' else 'claude'
    facts = manifest['components'][host + '_skills']['facts']; runtime = s.pinned(view, record['runtime'], api)
    receipt_raw = s.pinned(view, record['receipt'], api, as_json=False); receipt = json.loads(receipt_raw)
    workspace = record['host_workspace']; config_path = record['configuration_path']
    s.require(receipt.get('kind') == 'stdo-skills.installation/1' and receipt.get('version') == manifest['cohort']['version'] and receipt.get('host') == host,
              'host receipt names a different package/version/host')
    s.require(receipt.get('package_sha256') == facts['package_manifest']['sha256'], 'installed host package differs')
    s.pinned(view, facts['package_manifest'], api)
    base = Path(workspace) / ('.agents' if host == 'codex' else '.claude')
    s.require(base.is_relative_to(installed['workspace']) and receipt['files'], 'host installed file inventory missing/outside workspace')
    for name, sha in receipt['files'].items():
        local_file(str(base / s.path(name)), s.digest(sha), root=Path(installed['workspace']), api=api)
    value = execution(view, record, api, SKILLS,
        ['verify', '--workspace', workspace, '--host', host, '--receipt-sha256', record['receipt']['sha256']],
        installation=installed, inputs=[record['receipt']])
    s.require(value == {'status': 'verified', 'host': host, 'files': len(receipt['files'])}, 'host owner verify output differs')
    config = runtime.get('configuration', {})
    s.require(runtime.get('status') == 'verified' and config.get('kind') == 'stdo-skills.runtime/1'
              and config.get('version') == manifest['cohort']['version'] and config.get('host') == host
              and config.get('method_selection_scope') == 'runtime-installation-anchor-only'
              and config.get('basis') == {'uri': 'stdo://releases/' + manifest['cohort']['cut'] + '/', 'manifest_sha256': manifest['native']['manifest']['sha256']}
              and config.get('method_root') == installed['native_root'], 'host runtime names a stale or different native installation')
    config_raw = s.pinned(view, record['configuration'], api, as_json=False)
    s.require(local_file(config_path, root=Path(installed['workspace']), api=api) == config_raw and json.loads(config_raw) == config, 'actual installed host configuration differs')
    runtime_record = record['runtime_execution']
    checked = execution(view, runtime_record, api, SKILLS, ['check-runtime', '--configuration', config_path],
                        installation=installed, inputs=[record['configuration']])
    s.require(checked == runtime, 'host runtime execution result differs')
    for relative, sha in config['provider_pins'].items():
        source = 'a_c/' + s.path(relative)
        s.require(source in installed['files'], 'host provider is absent from selected installed inventory')
        local_file(str(Path(config['ac_root']) / relative), sha, root=Path(installed['workspace']), api=api)
        s.require(str(Path(config['ac_root']) / relative) == installed['files'][source], 'host provider points to a different installation')


def verify(view, record, claim, manifest, api):
    s = gate()
    if claim == 'complete_installed_cohort':
        s.require(record.get('category') == 'installed_aggregate', 'whole cohort requires concrete installed component results')
        installed = installation(view, record['installation'], manifest, api)
        required = {c for _, claims in s.COMPONENTS.values() for c in claims if c not in s.ASSESSMENTS}
        s.require(set(record.get('component_evidence', {})) == required, 'installed cohort is missing required current component results')
        for name, ref in record['component_evidence'].items():
            current = s.evidence(view, ref, name, manifest, api)
            s.require(current.get('installation') == record['installation'], 'component was qualified against another store')
        return installed
    if claim in BROWSER:
        return browser(view, record, claim, manifest, api)
    category = 'installed_native_binding' if claim == 'installed_native_workflow' else 'execution'
    s.require(record.get('category') == category, 'required evidence category differs: ' + claim)
    installed = installation(view, record['installation'], manifest, api) if claim in INSTALLED else None
    if claim == 'exact_candidate_lean_result':
        return formal(view, record, manifest, api)
    if claim == 'installed_lean':
        return installed_formal(view, record, manifest, api, installed)
    if claim in ('current_codex_skills', 'current_claude_skills'):
        return skills(view, record, claim, manifest, api, installed)
    if claim == 'installed_manager':
        s.require(record.get('result') == installed['verify']['result'] and record.get('execution') == installed['verify']['execution'],
                  'manager capability is not its actual installed verification')
        return
    if claim == 'installed_native_workflow':
        s.require(set(record.get('host_evidence', {})) == {'codex', 'claude'}, 'native workflow requires both actual host discovery/runtime results')
        for host, ref in record['host_evidence'].items():
            child = s.evidence(view, ref, 'current_' + host + '_skills', manifest, api)
            s.require(child.get('installation') == record['installation'], 'native workflow host uses another installation')
        return
    if claim == 'installed_graphify':
        return graphify(view, record, manifest, api, installed)
    if claim in ('installed_documentation', 'current_proof_reader'):
        name = 'documentation' if claim == 'installed_documentation' else 'proof_reader'
        directory = installed['native_root'] if name == 'documentation' else installed['native_root'] + '/standards/documentation/proofs'
        result = execution(view, record, api, COMMON + name + '.py', ['check', directory], inputs=[])
        expected_kind = 'stdo.installed-documentation/2' if name == 'documentation' else 'stdo.current-proof-reader/1'
        facts, identity = model_facts(view, manifest, api)
        s.require(result.get('kind') == expected_kind and result.get('status') == 'checked'
                  and result.get('version') == manifest['cohort']['version']
                  and result.get('source_identity_sha256') == manifest['source']['source_identity_sha256']
                  and result.get('model') == identity, 'current installed documentation/proof-reader owner result differs')
        return
    if claim in ('source_current_model', 'source_current_map', 'current_index_validation'):
        return representation(view, record, claim, manifest, api)
    raise ValueError('no qualified owner evidence adapter for claim: ' + claim)


def graphify(view, record, manifest, api, installed):
    s = gate(); facts, identity = model_facts(view, manifest, api)
    producer = 'a_c/build_tenants/graphify/code/ac_upstream.py'
    model_path = artifact_location(view, facts['model'], api, installed)
    carrier_path = artifact_location(view, facts['carrier'], api, installed)
    selections_ref = manifest['components']['lean']['facts']['selections']
    selections = s.pinned(view, selections_ref, api)
    selection_path = artifact_location(view, selections_ref, api)
    runtime = s.pinned(view, record['runtime'], api)
    runtime_path = record['runtime_path']; output = record['output_directory']
    local_file(runtime_path, record['runtime']['sha256'], root=Path(installed['workspace']), api=api)
    s.require(Path(output).is_relative_to(installed['workspace']), 'Graphify output is outside installed qualification workspace')
    result = execution(view, record, api, producer, ['--model', model_path, '--carrier', carrier_path,
            '--selections', selection_path, '--upstream', runtime['upstream'], '--runtime', runtime_path, '--output', output],
            installation=installed, inputs=[facts['model'], facts['carrier'], selections_ref, record['runtime']])
    expected_model = {'id': identity['id'], 'raw_sha256': facts['model']['sha256'], 'canonical_sha256': identity['sha256']}
    s.require(result.get('schema') == 'a_c.graphify.current-roundtrip/1' and result.get('status') == 'verified'
              and result.get('version') == manifest['cohort']['version'] and result.get('model') == expected_model
              and result.get('carrier_raw_sha256') == facts['carrier']['sha256'] and result.get('selections') == selections,
              'Graphify current-model roundtrip did not verify')
    trial = result['upstream_trial']
    pin = next(row for row in manifest['third_party_dependencies'] if row['name'] == 'graphify')
    s.require(trial.get('commit') == pin['commit'] and trial.get('decoded_model_sha256') == identity['sha256']
              and type(trial.get('nodes')) is int and trial['nodes'] > 0 and type(trial.get('edges')) is int and trial['edges'] >= 0,
              'Graphify actual upstream result differs from selected current model/runtime')
    observed = result['runtime']; python = record['execution']['environment']['python']
    s.require(runtime.get('version') == manifest['cohort']['version'] and runtime.get('status') == 'installed'
              and runtime.get('python') == python['invocation'] and runtime.get('upstream_commit') == pin['commit']
              and observed.get('receipt_sha256') == record['runtime']['sha256'] and observed.get('receipt_path') == runtime_path
              and observed.get('python_invocation') == python['invocation'] and observed.get('python_physical') == python['executable_realpath']
              and observed.get('python_sha256') == python['sha256'] and observed.get('prefix') != observed.get('base_prefix'),
              'Graphify actual private runtime differs from the selected installation')
    s.require(api.git(Path(runtime['upstream']), 'rev-parse', 'HEAD').stdout.strip() == pin['commit'],
              'actual Graphify checkout commit differs from selected dependency')
    expected_packages = {}
    required_files = {'test_env/requirements-qualification.txt', 'code/generation/requirements.txt', 'code/code-requirements.txt'}
    s.require(set(runtime.get('requirements', {})) == required_files, 'Graphify dependency requirement population differs')
    for name, sha in runtime['requirements'].items():
        source = 'a_c/build_tenants/graphify/' + name
        raw = local_file(installed['files'][source], sha, root=Path(installed['workspace']), api=api)
        for line in raw.decode().splitlines():
            line = line.strip()
            if line and not line.startswith('#'):
                package, version = line.split('=='); expected_packages[package] = version
    s.require(observed.get('required_packages') == expected_packages and observed.get('package_probe') == {
              'argv': [python['invocation'], '-m', 'pip', 'freeze', '--all'], 'returncode': 0, 'stdout_sha256': runtime['packages_sha256']},
              'actual Graphify package result differs from exact dependency pins')
    packages = subprocess.run([python['invocation'], '-m', 'pip', 'freeze', '--all'], capture_output=True, timeout=60)
    s.require(packages.returncode == 0 and api.sha256(packages.stdout) == runtime['packages_sha256'], 'actual installed Graphify package population changed')
    required_modules = {'graphify.build', 'graphify.export', 'graphify.paths', 'ac_graph', 'ac_generate'}
    s.require(required_modules <= set(observed['loaded_modules']), 'Graphify actual loaded implementation modules missing')
    for name, row in observed['loaded_modules'].items():
        local_file(row['path'], s.digest(row['sha256']), api=api)
        if name.startswith('graphify.'):
            s.require(Path(row['path']).is_relative_to(runtime['upstream']), 'Graphify loaded module is outside selected upstream')
            relative = Path(row['path']).relative_to(runtime['upstream']).as_posix()
            s.require(api.sha256(api.git_bytes(Path(runtime['upstream']), pin['commit'] + ':' + relative)) == row['sha256'], 'loaded Graphify source differs from pinned upstream commit')
    for name in ('ac_upstream.py', 'ac_graph.py', 'ac_generate.py'):
        source = 'a_c/build_tenants/graphify/code/' + name
        local_file(installed['files'][source], s.digest(observed['source_pins'][name]), root=Path(installed['workspace']), api=api)
    members = result['artifacts']; retained = record['artifacts']
    s.require(set(members) == set(retained) == {'model.json', 'carrier.json', 'selections.json', 'runtime.json', 'graph.json', 'views.json'},
              'Graphify executed artifact closure differs')
    for name, sha in members.items():
        s.require(retained[name]['sha256'] == sha, 'retained Graphify artifact binding differs')
        s.pinned(view, retained[name], api, as_json=False)
        local_file(str(Path(output) / name), sha, root=Path(installed['workspace']), api=api)
    s.require(members['model.json'] == facts['model']['sha256'] and members['carrier.json'] == facts['carrier']['sha256']
              and members['runtime.json'] == record['runtime']['sha256'] and members['views.json'] == result['views_sha256'],
              'Graphify actual retained inputs/views differ')
    views = manifest['components']['lean']['facts']['supplied_views']
    s.require(s.pinned(view, retained['views.json'], api) == s.pinned(view, views, api), 'Graphify actual projections differ from selected Lean views')


def formal(view, record, manifest, api, installed=None):
    # Implemented against the formal owner's inspect-evidence contract below.
    s = gate(); facts, identity = model_facts(view, manifest, api)
    selected = manifest['components']['lean']['facts']; request_ref = selected['request']
    request = s.pinned(view, request_ref, api)
    selections = s.pinned(view, selected['selections'], api)
    views = s.pinned(view, selected['supplied_views'], api, as_json=False)
    s.require(request.get('input') == {'format': 'model', 'path': artifact_location(view, facts['model'], api), 'raw_sha256': facts['model']['sha256']}
              and request.get('selections') == selections and selections
              and request.get('supplied_views') == {'path': artifact_location(view, selected['supplied_views'], api), 'raw_sha256': api.sha256(views)},
              'formal request differs from externally selected current model, projections or views')
    bundle = s.path(selected['bundle']); bundle_path = str(view.root.absolute() / bundle)
    request_path = artifact_location(view, request_ref, api)
    result = execution(view, record, api, FORMAL, ['verify', '--request', request_path, '--output', bundle_path],
                       installation=installed, flags=('-I', '-S', '-B'), inputs=[facts['model'], request_ref, selected['supplied_views']])
    s.require(record['result']['path'] == bundle + '/result.json' and result.get('schema') == 'a_c.formal-gate.result/1'
              and result.get('status') == 'verified', 'current Lean result bundle did not verify')
    expected_claims = ['imported-model-well-formedness', 'whole-model-source-correspondence',
                       'declared-closure-and-projection', 'record-budget-result', 'supplied-graphify-view-correspondence']
    s.require(request.get('selections') and request.get('supplied_views') and result.get('requested_claims') == expected_claims
              and result.get('checked_claims') == expected_claims, 'current Lean release obligation coverage differs')
    s.require(result.get('model') == {'id': identity['id'], 'sha256': identity['sha256']}
              and result.get('inputs', {}).get('model', {}).get('canonical_sha256') == identity['sha256']
              and result.get('inputs', {}).get('input', {}).get('raw_sha256') == facts['model']['sha256'],
              'Lean result proves a different model')
    bundle_manifest = s.pinned(view, selected['bundle_manifest'], api)
    s.require(selected['bundle_manifest']['path'] == bundle + '/manifest.json' and bundle_manifest.get('schema') == 'a_c.formal-gate.bundle/1'
              and result.get('evidence') == {'manifest_sha256': selected['bundle_manifest']['sha256'], 'members': bundle_manifest['members']},
              'Lean proof bundle inventory/result binding differs')
    required = {'request.json', 'replay-request.json', 'input.json', 'model.json', 'supplied-views.json', 'certificates.json', 'view-comparison.json'}
    modules = ['GateData', 'GateLocalNames', 'GateExternalNames', 'GateIdentities', 'GateBounds', 'GateModel', 'GateViews', 'GateRun']
    required.update(name + '.lean' for name in modules)
    required.update(name + '.olean' for name in modules[:-1])
    s.require(required <= set(bundle_manifest['members']), 'required actual Lean proof artifacts are missing')
    for name, sha in bundle_manifest['members'].items():
        s.require('/' not in name and name not in ('result.json', 'manifest.json'), 'invalid formal artifact member')
        s.pinned(view, {'path': bundle + '/' + s.path(name), 'sha256': s.digest(sha)}, api, as_json=False)
    runtime = result.get('runtime_identity'); expected_runtime = s.pinned(view, selected['runtime_identity'], api)
    s.require(runtime == expected_runtime and runtime.get('sha256') == api.canonical_value_sha256(runtime['pins']), 'Lean selected runtime identity differs')
    root = FORMAL.removesuffix('scripts/formal_gate.py')
    auxiliary = selected.get('runtime_auxiliary', {})
    s.require(set(auxiliary) <= {'.cache/formal-origin-v1/selection.json'}, 'unsupported formal runtime auxiliary input')
    for name, sha in runtime['pins'].items():
        if name == '.cache/formal-origin-v1/selection.json':
            ref = auxiliary[name]
            s.require(ref['sha256'] == sha, 'retained public origin selection differs')
            s.pinned(view, ref, api, as_json=False)
        else:
            s.pinned(view, {'path': root + s.path(name), 'sha256': s.digest(sha)}, api, as_json=False)
    obs = result['observations']
    s.require(obs.get('current_dynamic_proof_invocations') == 7 and obs.get('current_kernel_replay_invocations') == 1
              and obs.get('current_runtime_invocations') == 1, 'required current cold Lean executions did not occur')
    # Inspection rederives owner predicates against the externally selected request.
    # It is a read-only consistency/currentness result, not a fresh kernel verdict.
    inspector = artifact_location(view, record['producer'], api, installed)
    python = python_identity(record['execution']['environment']['python'], api)
    inspection = inspect_formal(view, record, bundle_path, request_ref, result, record['result'], runtime, api, installed)
    if 'installed_verification' in record:
        s.require('replay' not in record, 'select one separate installed verification or same-runtime fresh replay')
        child = s.evidence(view, record['installed_verification'], 'installed_lean', manifest, api)
        replay_result = s.pinned(view, child['result'], api)
        s.require(replay_result['model'] == result['model'] and replay_result['selections'] == result['selections']
                  and replay_result['inputs']['supplied_views']['raw_sha256'] == result['inputs']['supplied_views']['raw_sha256'],
                  'installed verification proves a different current subject')
        return inspection
    replay = record['replay']; replay_path = str(view.root.absolute() / s.path(selected['replay_bundle']))
    replay_result = execution(view, replay, api, FORMAL, ['check-evidence', '--fresh', '--bundle', bundle_path, '--output', replay_path],
        installation=installed, flags=('-I', '-S', '-B'), inputs=[record['result'], selected['bundle_manifest']])
    s.require(replay_result.get('status') == 'verified' and replay_result.get('model') == result['model']
              and replay_result.get('selections') == result['selections'] and replay_result.get('runtime_identity') == runtime
              and replay_result.get('observations', {}).get('current_dynamic_proof_invocations') == 7
              and replay_result.get('observations', {}).get('current_kernel_replay_invocations') == 1
              and replay_result.get('observations', {}).get('current_runtime_invocations') == 1,
              'separate current Lean kernel replay did not verify')
    s.require(replay['result']['path'] == selected['replay_bundle'] + '/result.json', 'fresh replay output is not its selected bundle')
    inspect_formal(view, replay, replay_path, request_ref, replay_result, replay['result'], runtime, api, installed)
    return inspection


def inspect_formal(view, record, directory, request_ref, result, result_ref, runtime, api, installed=None):
    """Invoke the owner's read-only consistency adapter against exact inputs."""
    s = gate(); request = s.pinned(view, request_ref, api)
    inspector = artifact_location(view, record['producer'], api, installed)
    python = python_identity(record['execution']['environment']['python'], api)
    request_path = artifact_location(view, request_ref, api)
    process = subprocess.run([python, '-I', '-S', '-B', inspector, 'inspect-evidence', '--bundle', directory,
                              '--request', request_path], capture_output=True, timeout=180)
    inspection = json.loads(process.stdout)
    s.require(process.returncode == 0 and inspection.get('schema') == 'a_c.formal-gate.inspection/1'
              and inspection.get('status') == 'consistent', 'formal owner retained-evidence inspection refused or is unavailable')
    required_checks = {'complete-member-integrity', 'current-runtime-and-support', 'exact-current-request-inputs',
                       'known-required-obligations', 'regenerated-proof-sources', 'complete-theorem-axiom-audit',
                       'cold-stage-consistency', 'current-runtime-output-correspondence', 'supplied-view-correspondence'}
    required_claims = ['imported-model-well-formedness', 'whole-model-source-correspondence',
                       'declared-closure-and-projection', 'record-budget-result', 'supplied-graphify-view-correspondence']
    s.require(set(inspection.get('checks', [])) == required_checks
              and inspection.get('model') == result['model'] and inspection.get('inputs') == result['inputs']
              and inspection.get('selections') == request['selections'] and inspection.get('context_binding') == request['context_binding']
              and inspection.get('required_claims') == result.get('checked_claims') == result.get('requested_claims') == required_claims
              and inspection.get('selected_request_sha256') == api.canonical_value_sha256(request)
              and inspection.get('evidence') == {'result_sha256': result_ref['sha256'], **result['evidence']},
              'formal inspection does not bind the actual selected evidence and obligations')
    current_pins = {k: v for k, v in inspection['runtime_identity']['pins'].items() if k != '.cache/formal-origin-v1/selection.json'}
    expected_pins = {k: v for k, v in runtime['pins'].items() if k != '.cache/formal-origin-v1/selection.json'}
    s.require(current_pins == expected_pins, 'formal inspector executes a different machinery/profile source')
    return inspection


def installed_formal(view, record, manifest, api, installed):
    """The installed owner verifies current inputs under its exact actual runtime.

    Same-runtime --fresh replay and a new installed verify after support setup
    are distinct paths. Neither transports a historical proof verdict.
    """
    s = gate(); facts, identity = model_facts(view, manifest, api)
    selected = manifest['components']['lean']['facts']
    native_bundle = Path(installed['native_root']) / s.path(selected['native_bundle'])
    original = s.pinned(view, selected['bundle_manifest'], api)
    local_file(str(native_bundle / 'manifest.json'), selected['bundle_manifest']['sha256'], root=Path(installed['workspace']), api=api)
    s.require(local_file(str(native_bundle / 'result.json'), root=Path(installed['workspace']), api=api) == view.read_bytes(selected['bundle'] + '/result.json'), 'native bundle does not retain the exact original current proof result')
    for name, sha in original['members'].items():
        local_file(str(native_bundle / s.path(name)), s.digest(sha), root=Path(installed['workspace']), api=api)
    request = s.pinned(view, record['current_request'], api)
    s.require(request.get('input') == {'format': 'model', 'path': str(native_bundle / 'input.json'), 'raw_sha256': facts['model']['sha256']}
              and request.get('selections') == s.pinned(view, selected['selections'], api)
              and request.get('supplied_views') == {'path': str(native_bundle / 'supplied-views.json'), 'raw_sha256': selected['supplied_views']['sha256']},
              'installed Lean request differs from exact embedded current model/views')
    output = record['output_directory']
    s.require(Path(output).is_relative_to(installed['workspace']) and not Path(output).is_relative_to(installed['native_root']),
              'installed Lean output overlaps immutable method or leaves workspace')
    mode = record.get('verification_mode')
    s.require(mode in ('fresh_replay', 'verify_current'), 'explicit installed verification path required')
    if mode == 'fresh_replay':
        arguments = ['check-evidence', '--fresh', '--bundle', str(native_bundle), '--output', output]
        inputs = [selected['bundle_manifest']]
    else:
        arguments = ['verify', '--request', artifact_location(view, record['current_request'], api), '--output', output]
        inputs = [record['current_request']]
    result = execution(view, record, api, FORMAL, arguments,
        installation=installed, flags=('-I', '-S', '-B'), inputs=inputs)
    s.require(result.get('schema') == 'a_c.formal-gate.result/1' and result.get('status') == 'verified'
              and result.get('model') == {'id': identity['id'], 'sha256': identity['sha256']}, 'installed Lean did not verify current model')
    local_file(str(Path(output) / 'result.json'), record['result']['sha256'], root=Path(installed['workspace']), api=api)
    bundle = s.pinned(view, record['bundle_manifest'], api)
    s.require(result.get('evidence') == {'manifest_sha256': record['bundle_manifest']['sha256'], 'members': bundle['members']},
              'installed Lean result differs from retained executed bundle')
    local_file(str(Path(output) / 'manifest.json'), record['bundle_manifest']['sha256'], root=Path(installed['workspace']), api=api)
    original_runtime = s.pinned(view, selected['runtime_identity'], api)
    runtime = s.pinned(view, record['runtime_identity'], api)
    s.require(runtime == result.get('runtime_identity') and runtime.get('sha256') == api.canonical_value_sha256(runtime['pins']),
              'installed proof does not bind its own exact actual machinery')
    ignored = {'.cache/formal-origin-v1/selection.json'}
    if mode == 'verify_current':
        # Establishing private compiled support produces this owner-defined
        # runtime profile. It is pinned as a new runtime subject, not treated
        # as equivalent to the construction profile or a reusable old verdict.
        profile = 'profiles/proof-support-v1.json'
        support = s.pinned(view, record['support_profile'], api, as_json=False)
        s.require(api.sha256(support) == runtime['pins'][profile], 'installed support profile artifact differs')
        actual_profile = Path(installed['files'][FORMAL]).parent.parent / profile
        s.require(local_file(str(actual_profile), root=Path(installed['workspace']), api=api) == support,
                  'actual selected installed support profile differs')
        ignored.add(profile)
    s.require({k: v for k, v in runtime['pins'].items() if k not in ignored} ==
              {k: v for k, v in original_runtime['pins'].items() if k not in ignored},
              'installed proof changed selected machinery outside declared support setup')
    return inspect_formal(view, record, output, record['current_request'], result, record['result'], runtime, api, installed)


def representation(view, record, claim, manifest, api):
    s = gate(); facts, identity = model_facts(view, manifest, api)
    if claim == 'source_current_model':
        run = str(view.root.absolute() / s.path(facts['build_run']))
        result = execution(view, record, api, PROJECT, ['build', '--run', run], inputs=[facts['model']])
        binding = s.pinned(view, facts['current_binding'], api)
        s.require(binding.get('source_identity_sha256') == manifest['source']['source_identity_sha256']
                  and binding.get('source_freeze_raw_sha256') == manifest['source']['sha256']
                  and binding.get('model_raw_sha256') == facts['model']['sha256'] and binding.get('model_identity') == identity,
                  'current model owner source binding differs')
        s.require(result.get('profile') == 'a_c.project-build-result/1' and result.get('status') in ('built', 'reused')
                  and result.get('model') == {'id': identity['id'], 'sha256': identity['sha256']}, 'current model producer result differs')
        source_manifest = s.pinned(view, facts['source_manifest'], api)
        semantic = s.pinned(view, manifest['source'], api)
        prefix = s.path(facts['source_copy_prefix']).rstrip('/') + '/'
        expected = sorted([{**row, 'path': prefix + row['path']} for row in semantic['members'] + semantic['native_contracts']], key=lambda r: r['path'])
        s.require(source_manifest.get('files') == expected and result.get('source_manifest_sha256') == facts['source_manifest']['sha256'],
                  'model producer did not consume the complete exact semantic source')
        for row in expected:
            s.pinned(view, {**row, 'path': 'stdo_representation/' + row['path']}, api, as_json=False)
        model = s.pinned(view, facts['model'], api)
        s.require(model['basis']['subject']['sha256'] == api.canonical_value_sha256(expected)
                  and model['basis']['subject']['id'] == source_manifest['subject_id'] == result['subject_id'],
                  'actual model basis does not bind its consumed source inventory')
        return
    program = s.pinned(view, facts['program'], api); program_sha = api.canonical_value_sha256(program)
    args = ['validate', '--program', artifact_location(view, facts['program'], api), '--bindings', artifact_location(view, facts['bindings'], api)]
    if claim == 'source_current_map':
        args += ['--emit-map', artifact_location(view, facts['map'], api)]
    result = execution(view, record, api, INDEX, args, inputs=[facts['program'], facts['bindings'], facts['source_corpus']])
    s.require(result.get('kind') == 'axiom-indexer.validation-report' and result.get('status') == 'valid'
              and result.get('diagnostics') == [] and result.get('program_sha256') == 'sha256:' + program_sha,
              'current Axiom validation output differs')
    semantic = s.pinned(view, manifest['source'], api)
    expected = {(semantic['basis_uri'] + row['path'], 'sha256:' + row['sha256']) for row in semantic['members'] + semantic['native_contracts']}
    s.require(expected <= {(row['uri'], row['sha256']) for row in result['resolved_sources']}, 'current Axiom result omits exact semantic source members')
    if claim == 'source_current_map':
        preservation = s.pinned(view, facts['preservation'], api)
        s.require(preservation.get('kind') == 'axiom-indexer.model-conversion-receipt' and preservation.get('preserved') is True
                  and preservation.get('model_sha256') == preservation.get('restored_model_sha256') == identity['sha256']
                  and preservation.get('program_sha256') == program_sha, 'current model/program preservation differs')
        s.pinned(view, facts['map'], api)
        s.require(any(row['path'] == facts['map']['path'] and row['sha256'] == facts['map']['sha256'] for row in record['execution']['outputs']),
                  'current map is not the actual validator output')
        helper = 'axiom_indexer/build_tenants/core/code/ac_model.py'
        members = {r['path']: r for r in manifest['products']['axiom_indexer']['subject']['members']}
        artifact_location(view, members[helper], api)
        # Use the owning conversion and map functions directly, without copying
        # their semantic rules into this release controller.
        code = ('import sys,json;sys.path.insert(0,sys.argv[1]);import ac,ac_model;'
                'p=ac.load_json(sys.argv[2]);m=ac.load_json(sys.argv[3]);v=ac.load_json(sys.argv[4]);'
                'report=ac.load_json(sys.argv[5]);'
                'print(json.dumps({"restored":ac_model.restore(p)==m,"map":ac.instantiate(p,report)==v}))')
        python = python_identity(record['execution']['environment']['python'], api)
        checked = subprocess.run([python, '-I', '-B', '-c', code, str((view.root / helper).parent.absolute()),
            artifact_location(view, facts['program'], api), artifact_location(view, facts['model'], api),
            artifact_location(view, facts['map'], api), artifact_location(view, record['result'], api)], capture_output=True, timeout=120)
        s.require(checked.returncode == 0 and json.loads(checked.stdout) == {'restored': True, 'map': True},
                  'owning conversion/map functions do not preserve the actual current model/program relation')


def browser(view, record, claim, manifest, api):
    s = gate(); installed = installation(view, record['installation'], manifest, api)
    s.require(record.get('category') == 'browser_observation' and record.get('assessor') and record.get('assessor') not in record.get('authors', []),
              'current browser behavior requires a separately bound observer')
    facts, identity = model_facts(view, manifest, api)
    result = s.pinned(view, record['result'], api)
    page = manifest['components']['unified_explorer']['facts']['page']
    location = artifact_location(view, page, api, installed)
    s.require(result.get('kind') == 'stdo.current-browser-observation/1' and result.get('page') == {'path': location, 'sha256': page['sha256']}
              and result.get('source_identity_sha256') == manifest['source']['source_identity_sha256'] and result.get('model') == identity
              and result.get('errors') == [], 'browser observation is not the current installed view')
    expected = {'3d', '2d', 'layered'} if claim == 'current_3d_2d_layered' else {'source', 'files'}
    observations = result['observations']
    s.require(set(observations) >= expected, 'required browser modes/navigation missing')
    for name in expected:
        row = observations[name]
        s.require(row.get('observed') is True and row.get('action') and row.get('visible_result'), 'browser behavior was not observed')
        s.pinned(view, row['screenshot'], api, as_json=False)
    s.pinned(view, record['report'], api, as_json=False)
