from pathlib import Path
import json
import run_observed as o

p = Path(__file__).absolute().parent
h = json.loads((p / 'SELECTED_HANDOFF.json').read_bytes())
b = Path(h['workspace']); native = Path(h['native_root']); ac = b / 'runtime/a_c'
py = json.loads((b / 'dependencies/graphify/RUNTIME.json').read_bytes())['python']
common = 'specification_methodology/v3/build_tenants/common-tools/'
assert (b / 'runtime/bootstrap/derivation.json').is_file()

def run(*args, **kwargs):
    receipt, result = o.run(*args, **kwargs)
    assert receipt['execution']['returncode'] == 0, receipt
    return receipt, result

run('formal-origin', [py, '-I', '-S', '-B', ac / 'build_tenants/lean/scripts/formal_gate.py', 'init-origin'],
    'a_c/build_tenants/lean/scripts/formal_gate.py',
    output_files=[ac / 'build_tenants/lean/.cache/formal-origin-v1/selection.json'])
run('formal-checker-selection', [py, '-B', ac / 'scripts/ac.py', 'formal-select', '--lean-root', ac / 'build_tenants/lean',
    '--python', py, '--timeout-seconds', '900', '--output', b / 'formal/checker.json'], 'a_c/scripts/ac.py',
    output_files=[b / 'formal/checker.json'])
hosts = {}
for host, hostdir in [('codex', '.agents'), ('claude', '.claude')]:
    workspace = b / 'hosts' / host
    configuration = workspace / hostdir / 'stdo-3.0.5/CONFIG.json'
    receipt, result = run(host + '-host-setup', [py, '-B', native / 'standards/tooling/setup.py', 'host',
        '--tools', b / 'source-tools', '--anchor', b / 'anchors' / host, '--method-root', native,
        '--workspace', workspace, '--store', b / 'store', '--stdo', b / 'manager/bin/stdo', '--python', py,
        '--host', host, '--manifest-sha256', h['native_manifest']['sha256'], '--runtime-ac', ac,
        '--derivation', b / 'runtime/bootstrap/derivation.json', '--derivation-sha256', o.sha(b / 'runtime/bootstrap/derivation.json')],
        common + 'tooling_setup.py', inputs=[b / 'runtime/bootstrap/derivation.json'], output_tree=workspace,
        output_files=[b / 'anchors' / host / 'INSTALLATION.json', b / 'anchors' / host / 'stdo_runtime.json', b / 'anchors' / host / 'stdo'])
    config = json.loads(configuration.read_bytes())
    assert config['python'] == py and config['ac_root'] == str(ac)
    assert config['basis']['manifest_sha256'] == h['native_manifest']['sha256']
    assert config['provider_pins']['build_tenants/graphify/code/ac_support_core.py'] == '8798e1b822a631d0e64991fa5e6caa446accb9ec098e4735b8c0858ad2f46636'
    manager = configuration.parent / 'manage_skills.py'
    install_receipt = Path(result['result']['receipt'])
    run(host + '-skills-verify', [py, '-I', '-B', manager, 'verify', '--workspace', workspace,
        '--host', host, '--receipt-sha256', result['result']['receipt_sha256']],
        'stdo_skills/scripts/manage_skills.py', inputs=[install_receipt])
    checked, observed = run(host + '-check-runtime', [py, '-I', '-B', manager, 'check-runtime', '--configuration', configuration],
        'stdo_skills/scripts/manage_skills.py', inputs=[configuration])
    assert observed['configuration'] == config
    early = workspace / 'early-readonly'
    initialized, setup = run(host + '-early-initializer', [py, '-B', ac / 'build_tenants/graphify/examples/fd-support/prepare_readonly.py',
        '--out', early, '--product-root', Path(config['definition']).parent, '--definition-name', Path(config['definition']).name,
        '--profile', 'stdo-3.0.5', '--method-installation', config['method_root'], '--stdo', config['stdo']],
        'a_c/build_tenants/graphify/examples/fd-support/prepare_readonly.py', inputs=[configuration, Path(config['definition'])], output_tree=early)
    assert setup['policy_sha256'] == o.sha(early / 'policy.json')
    hosts[host] = {'configuration': o.ref(configuration), 'receipt': o.ref(install_receipt),
                   'setup': o.ref(early / 'SETUP.json'), 'policy': o.ref(early / 'policy.json'),
                   'method_verification': o.ref(early / 'method-verification.json'), 'stdin': o.ref(early / 'mcp-session.jsonl')}
    if host == 'codex':
        mcp, replies = run('codex-early-mcp', [py, '-B', ac / 'build_tenants/graphify/code/ac_support.py',
            '--policy', early / 'policy.json', '--policy-sha256', setup['policy_sha256'], '--principal', 'executive', 'mcp'],
            'a_c/build_tenants/graphify/code/ac_support.py', inputs=[early / 'policy.json', early / 'mcp-session.jsonl'],
            stdin=early / 'mcp-session.jsonl', decode='jsonl')
        assert [row['id'] for row in replies] == [1, 2, 3]
        assert replies[0]['result']['serverInfo'] == {'name': 'a_c.graphify.fd-support', 'version': '3.0.5'}
        source_read = replies[2]['result']['structuredContent']
        assert source_read['status'] == 'ok' and source_read['result']['value']['content'] == Path(config['definition']).read_text()
        hosts[host]['mcp_execution'] = o.ref(p / 'executions/codex-early-mcp/execution.json')
(p / 'HOST_SELECTIONS.json').write_bytes(o.encoded({'schema': 'stdo305.actual-host-selections/1', 'hosts': hosts,
    'standing': 'Actual host setup/verify/check-runtime and both initializers succeeded; initialized Codex MCP source read succeeded before full proof. Native LLM sessions have not run.'}))
print(json.dumps({'status': 'actual_hosts_and_early_native_startup_complete', 'hosts': hosts}))
