"""Bind closed public001 observations; no owner invocation or large-tree scan."""
import copy
import sys
import hashlib
import json
from pathlib import Path

R = Path.cwd()
Q = R / 'specification_methodology/v3/.ai-workspace/work/STDO305_RC_RESET'
W, T = Q / 'release-tools', Q / 'tools-skills'
C = Path(__file__).resolve().parent
O = Q / 'public-qualification-001/cohort'
TQ = Q / 'public-qualification-001'
sha = lambda b: hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_bytes())
def ref(p):
    raw = p.read_bytes()
    return {'path': p.relative_to(R).as_posix(), 'sha256': sha(raw), 'bytes': len(raw)}
def save(p, value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        assert p.read_bytes() == raw, str(p)
    else:
        with p.open('xb') as f: f.write(raw)
    return ref(p)
def recorded(p):
    value = load(p)
    assert value['execution']['returncode'] == 0
    value['original_execution'] = ref(p)
    return value

candidate = load(R / 'stack_release.json')
handoff = load(TQ / 'HANDOFF.json')
workspace, native = Path(handoff['workspace']), Path(handoff['native_root'])
source_id = candidate['source']['source_identity_sha256']
subjects = {k: v['subject']['sha256'] for k, v in candidate['products'].items()}
expected = {r['path']: r for p in candidate['products'].values() for r in p['subject']['members']}
materialized = load(TQ / 'MATERIALIZATION_CHECK.json')
tool_rows = {r['archive_path']: r for r in materialized['sources']}
source_selection = load(R / handoff['source_selection']['path'])
native_rows = {r['path']: r for r in source_selection['files']}
manager_match = load(TQ / 'manager-operations/external-manager-source-match/stdout.txt')
manager_prefix = candidate['components']['manager']['facts']['source_root'].rstrip('/') + '/'
common_prefix = 'specification_methodology/v3/build_tenants/common/'
files = {}
for name, row in expected.items():
    if name.startswith(common_prefix):
        relative = name[len(common_prefix):]
        assert native_rows[relative]['sha256'] == row['sha256']
        destination = native / relative
    elif name.startswith(manager_prefix):
        relative = 'stdo_toolchain/' + name[len(manager_prefix):]
        assert manager_match['members'][relative] == row['sha256']
        destination = Path(manager_match['site']) / relative
    else:
        assert tool_rows[name]['sha256'] == row['sha256'] and tool_rows[name]['bytes'] == row['bytes']
        destination = workspace / 'source-tools' / name
    files[name] = str(destination)
assert len(files) == 429
def manager_operation(name):
    original = handoff[name]
    raw = load(R / original['path'])
    assert raw['returncode'] == 0
    return {'schema': 'stdo.execution-observation/1', 'original_execution': original,
            'execution': copy.deepcopy(raw), 'result': raw['stdout'],
            'adaptation': 'Original observed invocation, environment selection, return code and streams retained exactly. Result is actual JSON stdout; no new manager execution.'}
installation = {'kind': 'stdo.installed-cohort/1', 'version': candidate['cohort']['version'],
    'source_identity_sha256': source_id, 'subjects': subjects, 'workspace': str(workspace),
    'store': handoff['store'], 'native_root': str(native), 'files': files,
    'manager': {'version': handoff['manager']['version'], 'executable': handoff['manager']['manager'], 'python': handoff['manager']['python']},
    'acquisition': handoff['acquisition'], 'install': manager_operation('install'), 'verify': manager_operation('verify'),
    'runtime_derivation': ref(TQ / 'observed/runtime/bootstrap/derivation.json'),
    'limits': 'Actual corrected public001 install, manager, 243 source materialization and independent fresh support. Mapping joins closed inventories; no runtime or support scan occurs in this metadata assembly. Final live currentness predicates remain required.'}
installed_ref = save(O / 'INSTALLATION.json', installation)
refs = {}
def claim(name, owners, fields, category='execution', limits=None):
    value = dict(fields)
    value.update(kind='stdo.cohort-evidence/1', claim=name, status='passed', category=category,
        source_identity_sha256=source_id, subjects={k: subjects[k] for k in owners}, installation=installed_ref)
    value['limits'] = limits or 'Closed actual public001 observation only. Required final live currentness/ref and public gates remain separate; no adoption or universal host behavior claim.'
    refs[name] = save(O / 'evidence' / (name + '.json'), value)
    return refs[name]

for name in ('source_current_model', 'source_current_map', 'current_index_validation', 'independent_semantic_review'):
    value = load(C / 'source-claims' / (name + '.json'))
    value['installation'] = installed_ref
    value['installation_join_basis'] = 'Same exact selected Product bytes. Original source execution and assessment retain their own subjects; they were not rerun in public001 and are not relabelled installed operations.'
    refs[name] = save(O / 'evidence' / (name + '.json'), value)
claim('installed_manager', ['specification_methodology'], installation['verify'])
hosts = load(TQ / 'HOST_SELECTIONS.json')['hosts']
for host, selected in hosts.items():
    value = recorded(TQ / 'executions' / (host + '-verify') / 'execution.json')
    runtime = recorded(TQ / 'executions' / (host + '-check-runtime') / 'execution.json')
    value.update(configuration=selected['configuration'], receipt=selected['receipt'], runtime=runtime['result'], runtime_execution=runtime,
        configuration_path=runtime['execution']['argv'][-1], host_workspace=str(workspace / 'hosts' / host),
        runtime_anchor=ref(TQ / 'observed/anchors' / host / 'INSTALLATION.json'))
    claim('current_' + host + '_skills', ['stdo_skills'], value,
          limits='Actual setup, owner verify/check-runtime and exact native launcher bindings for this host. No LLM session or blanket instruction-compliance claim.')
mcp = recorded(TQ / 'executions/codex-early-mcp/execution.json')
mcp.update({key: hosts['codex'][key] for key in ('configuration', 'setup', 'policy', 'method_verification', 'stdin')})
claim('installed_native_workflow', ['specification_methodology'],
      {'mcp': mcp, 'host_evidence': {host: refs['current_' + host + '_skills'] for host in hosts}},
      category='installed_native_binding', limits='Both actual installed host interfaces and initialized Codex MCP source.read passed at the corrected exact RC installation. Historical actor/Context trials are not current RC executions; none is claimed here.')
for name in ('installed_documentation', 'current_proof_reader'):
    claim(name, ['specification_methodology', 'stdo_representation'] if name == 'current_proof_reader' else ['specification_methodology'], recorded(TQ / 'installed-owner-checks' / name / 'execution.json'))
graph = recorded(TQ / 'executions/actual-upstream-roundtrip/execution.json')
graph.update(runtime=ref(TQ / 'observed/dependencies/graphify/RUNTIME.json'), runtime_path=str(workspace / 'dependencies/graphify/RUNTIME.json'),
    output_directory=str(workspace / 'graphify/current-roundtrip'))
graph['artifacts'] = {Path(row['path']).name: row for row in graph['execution']['outputs']
    if '/observed/graphify/current-roundtrip/' in row['path'] and Path(row['path']).name != 'result.json'}
assert set(graph['artifacts']) == {'model.json', 'carrier.json', 'graph.json', 'views.json', 'runtime.json', 'selections.json'}
claim('installed_graphify', ['a_c'], graph)

scratch = Path(sys.argv[1])
custody_list = load(scratch / 'CUSTODY_LIST.json')
assert sha((scratch / 'CUSTODY_LIST.json').read_bytes()) == sys.argv[2]
custody_root = TQ / 'original-review'
relocation = {}
for row in custody_list['files'] + [{'path': str(scratch / 'CUSTODY_LIST.json'), 'sha256': sha((scratch / 'CUSTODY_LIST.json').read_bytes()), 'bytes': (scratch / 'CUSTODY_LIST.json').stat().st_size}]:
    original = Path(row['path']); raw = original.read_bytes()
    assert len(raw) == row['bytes'] and sha(raw) == row['sha256'] and not original.is_symlink()
    target = custody_root / 'original' / original.relative_to(scratch)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists(): assert target.read_bytes() == raw
    else:
        with target.open('xb') as f: f.write(raw)
    relocation[str(original)] = ref(target)
custody = save(custody_root / 'CUSTODY.json', {'kind': 'stdo.original-review-custody/1', 'files': relocation, 'excluded': custody_list['excluded'], 'basis': 'Byte-exact original ordinary reports, driver and nine screenshots; no isolated browser profile.'})
observation_path = next(p for p in scratch.rglob('OBSERVATION.json') if 'isolated-profile' not in p.parts)
observation = load(observation_path)
def relocate(value):
    if isinstance(value, dict):
        if value.get('path') in relocation and 'sha256' in value:
            replacement = relocation[value['path']]
            assert replacement['sha256'] == value['sha256']
            return {**value, 'path': replacement['path']}
        return {k: relocate(v) for k, v in value.items()}
    if isinstance(value, list): return [relocate(v) for v in value]
    return value
portable = save(O / 'browser/observation-portable.json', relocate(observation))
save(O / 'browser/RELOCATION.json', {'original': relocation[str(observation_path)], 'derivative': portable,
    'mapping': relocation, 'basis': 'Only retained artifact reference paths relocated; actual installed page paths, observations and assertions remain unchanged.'})
for name in ('current_3d_2d_layered', 'source_files_navigation'):
    claim(name, ['stdo_representation'], {'result': portable, 'report': relocation[str(scratch / sys.argv[3])],
        'original_custody': custody, 'assessor': '/root/stdo305_integration_review',
        'authors': ['/root/stdo305_release_tools', '/root/stdo305_tools_skills', '/root/stdo305_representation']}, category='browser_observation',
        limits='Independent actual corrected public001 file:// observations, one Chromium-family session; nine screenshots and original report preserved. Public installation is independently bound; this observation alone does not establish universal browser behavior.')
result = save(O / 'CLOSED_BINDINGS.json', {'kind': 'stdo.closed-local-binding-frontier/1', 'installation': installed_ref, 'evidence': refs,
    'pending': ['installed_lean', 'exact_candidate_lean_result installed join', 'final independent release review', 'Executive cohort acceptance', 'public gate and Latest']})
print(json.dumps({'installation': installed_ref, 'closed_bindings': result, 'evidence_count': len(refs)}))
