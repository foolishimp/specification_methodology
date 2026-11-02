"""Bind a successor candidate to unchanged business fixture grants."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
FREEZE_SHA = '68320109c3379df967a475a3f9db799b618241f6160189a5adb9321da065e0e0'
PYTHON = str(Path(sys.executable).resolve())
MANAGER = '/Users/jim/.local/bin/stdo'


def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value, str) else json.dumps(value, indent=2) + '\n')


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    if (HERE / 'FIXTURES.json').exists(): raise SystemExit('preserve prepared fixture')
    freeze_path = PRIOR.parent / 'SOURCE_FREEZE.json'
    raw = freeze_path.read_bytes()
    assert sha(raw) == FREEZE_SHA
    freeze = json.loads(raw)
    for row in freeze['payload'] + freeze['support']:
        data = (REPO / row['path']).read_bytes()
        assert len(data) == row['bytes'] and sha(data) == row['sha256'], row['path']
    save(HERE / 'SOURCE_FREEZE.json', raw.decode())
    base = module('original_fixture', PRIOR / 'prepare_fixtures.py')
    base.HERE = HERE
    shutil.copyfile(PRIOR / 'EXPECTATIONS.md', HERE / 'EXPECTATIONS.md')
    base.main()
    meta = json.loads((HERE / 'FIXTURES.json').read_text())
    suite = Path(meta['suite'])
    candidate = suite / 'candidate'
    shutil.copytree(REPO / freeze['candidate_root'], candidate)
    plugin = candidate / 'plugins/spec'
    reader = plugin / 'scripts/read_basis.py'
    gate = plugin / 'scripts/claude_tool_gate.py'
    reader_module = module('reader_for_policy', reader)
    (suite / 'standards').symlink_to(candidate / 'standards', target_is_directory=True)
    controls = suite / 'controls'
    controls.mkdir()
    save(controls / 'empty-mcp.json', {'mcpServers': {}})
    pin_paths = [Path(PYTHON), Path(MANAGER), Path(MANAGER).resolve(), reader, gate]
    # Pin the installed manager implementation and interpreter, not only its launcher.
    manager_venv = Path(MANAGER).resolve().parents[1]
    pin_paths.extend(p for p in (manager_venv / 'lib').glob('python*/site-packages/stdo_toolchain/**/*.py') if p.is_file())
    pin_paths.append((manager_venv / 'bin/python').resolve())
    roles = {'direct': 'direct', 'issuer': 'coordinated', 'receiver': 'coordinated', 'negative': 'review'}
    contracts = {'direct': 'direct', 'issuer': 'issuer', 'receiver': 'worker', 'negative': 'bad-review'}
    policies = {}
    for name, root_string in meta['projects'].items():
        root = Path(root_string)
        (root / '.agents').mkdir()
        for leaf in ('skills', 'references', 'scripts'):
            (root / '.agents' / leaf).symlink_to(plugin / leaf, target_is_directory=True)
        # These are operational host bindings. Business source, effect and exclusion grants are unchanged.
        notice = f'''\n## Selected session binding\nThe existing fixture owner selects the candidate plugin at {plugin}.\nThe selected Python executable is {PYTHON}; use that absolute route.\nThe selected immutable method store is {suite / 'store'}.\nThe current host invocation has no resumed conversation. Managed/system context\nis not fully measured; no clean-room or universal read-isolation claim is selected.\nFor Claude, the session uses the shipped claude_tool_gate.py, exact per-role\npolicy, Read/Skill/Bash roster, restricted mode, memory disabled, strict empty\nMCP configuration and configured claude-fable-5-1. For Codex direct work, the\nconfigured model is retained and memories disabled for this invocation; exact\nshell confinement is not established. Observe the existing grant.\nA role's SESSION-<role>.md is operational metadata admitted by the fixture owner.\nThe harness is the authorized final-return recorder and dispatch transport;\nonly completed non-timeout final results are relayed to contract-named surfaces.\nA Claude actor need not write the result file itself. The issuer's final packet\nwill be delivered unchanged to a separate new receiver session by this transport.\n'''
        with (root / 'AGENTS.md').open('a') as stream: stream.write(notice)
        shutil.copyfile(root / 'AGENTS.md', root / 'CLAUDE.md')
    for case, project in roles.items():
        root = Path(meta['projects'][project])
        contract_name = contracts[case]
        contract = json.loads((root / f'contracts/{contract_name}.json').read_text())
        admission = f'{PYTHON} {root / "admission.py"} {contract_name}'
        base_args = ['--stdo', MANAGER, '--store', str(suite / 'store'), '--definition', str(root / 'stdo_fixture.json')]
        check = shlex.join([PYTHON, '-B', str(reader), 'check'] + base_args)
        source_commands = []
        catalog_commands = []
        operator_paths = []
        # Closed exact catalog: only installed source owner headings, never candidate programs.
        if case != 'negative':
            for owner in ('ACTIVATION.md', 'REFERENCE_FRAME.md', 'EXECUTIVE_BASELINE.md', 'SPEC_METHOD.md', 'TICKETS.md', 'EVALUATION.md', 'frames/bootstrap.md'):
                catalog = shlex.join([PYTHON, '-B', str(reader), 'read'] + base_args + ['--member', 'standards/' + owner, '--list-headings'])
                catalog_commands.append(catalog)
                source_commands.append(catalog)
                literal_commands = [catalog]
                source = suite / 'store/releases/v3.0.3/standards' / owner
                for _, _, heading in reader_module.headings(source.read_text()):
                    if heading:
                        literal = shlex.join([PYTHON, '-B', str(reader), 'read'] + base_args + ['--member', 'standards/' + owner]) + " --heading '" + heading.replace("'", "'\"'\"'") + "'"
                        source_commands.append(literal)
                        literal_commands.append(literal)
                operator_path = root / 'operators' / case / (owner.replace('/', '_') + '.json')
                save(operator_path, {'source_member': 'standards/' + owner, 'commands': literal_commands})
                operator_paths.append(operator_path)
        commands = [admission]
        if case != 'negative': commands += [check] + source_commands
        if case == 'issuer': commands.append(f'{PYTHON} {root / "admission.py"} worker')
        if case == 'receiver':
            commands += [f'{PYTHON} {root / "subject/service.py"} {op} JOB-17' for op in ('status', 'send')]
        session = root / f'SESSION-{case}.md'
        session_text = f'''# Selected {case} host binding\n\nThis is fixture-owner operational metadata for contracts/{contract_name}.json.\nIt changes no business source, effect, admission or exclusion grant. The\ncontract remains the authority for whether an exposed operation may be used.\n\nNative Skill calls use their selected name without extra arguments. The\nrequest and exact contract supply the invocation input. Tools are Read, Skill\nand Bash; a shipped digest-pinned PreToolUse policy gates exact direct calls.\nAllowed reads are the contract's listed exact files, selected plugin resources\nand this binding. Ordinary directory discovery is absent. The hook does not\ncover bootstrap/system context, native file mentions or commands' internal\nreads/effects. No @ file mentions or inherited conversation are supplied.\n\nExact admission command:\n`{admission}`\n'''
        if case != 'negative':
            session_text += f'''\nExact verified basis command:\n`{check}`\n\nSource reads use the literal approved commands in the operational command
catalogs named below. Copy a complete command exactly; quotes and spacing are
part of the closed policy. There is no separate command-construction recipe.
The catalogs are projections of already-admitted method routes and grant no
work, effect or additional source authority.
'''
        if operator_paths:
            session_text += '\nLiteral source-command catalogs (admitted operational metadata):\n' + '\n'.join(str(path) for path in operator_paths) + '\n'
        if case == 'issuer': session_text += f'\nWorker admission command: `{commands[-1]}`\n'
        if case == 'receiver': session_text += '\nDeclared service commands:\n' + '\n'.join('`' + c + '`' for c in commands[-2:]) + '\nThe command implementation is immutable; its status output and conditional send remain governed by the contract.\n'
        save(session, session_text)
        if case == 'direct': continue
        reads = []
        for entry in contract['permitted_inputs']:
            path = root / entry
            if path.is_file(): reads.append(str(path.resolve()))
        # Packet does not exist until actual issuer returns. Policy generated later for receiver.
        if case == 'receiver': reads.append(str(root / 'incoming/issuer-return.md'))
        reads += [str(session), str(root / 'CLAUDE.md')] + [str(path) for path in operator_paths]
        # Candidate resources are already admitted; route their canonical immutable files.
        reads += [str(p.resolve()) for p in plugin.rglob('*') if p.is_file()]
        policy = {'kind': 'stdo.claude-tool-policy', 'schema_version': 1,
                  'policy_id': 'urn:fixture:successor:' + case,
                  'authority_ref': str(root / f'contracts/{contract_name}.json') + '#existing-grant',
                  'cwd': str(root), 'read_paths': sorted(set(reads)),
                  'bash_commands': sorted(set(commands)),
                  'skills': ['spec:stdo-review'] if case == 'negative' else ['spec:stdo-work']}
        policy_path = controls / (case + '-policy.json')
        save(policy_path, policy)
        policy_sha = sha(policy_path.read_bytes())
        audit = controls / (case + '-audit.jsonl')
        settings = {'autoMemoryEnabled': False,
                    'claudeMdExcludes': ['/Users/jim/**/CLAUDE.md', '/Users/jim/**/.claude/rules/**', '/private/tmp/CLAUDE.md', '/private/CLAUDE.md'],
                    'hooks': {'PreToolUse': [{'matcher': '.*', 'hooks': [{'type': 'command', 'command': PYTHON, 'args': [str(gate), '--policy', str(policy_path), '--policy-sha256', policy_sha, '--audit', str(audit)], 'timeout': 10, 'onFailure': 'block'}]}]}}
        settings_path = controls / (case + '-settings.json')
        save(settings_path, settings)
        policies[case] = {'policy': str(policy_path), 'policy_sha256': policy_sha, 'settings': str(settings_path), 'settings_sha256': sha(settings_path.read_bytes()), 'audit': str(audit), 'session': str(session), 'operator_catalogs': [str(path) for path in operator_paths]}
        pin_paths += [policy_path, settings_path, session] + operator_paths
    direct = Path(meta['projects']['direct'])
    with (direct / 'PROMPT.txt').open('a') as stream: stream.write('The selected operational binding is SESSION-direct.md.\n')
    coordinated = Path(meta['projects']['coordinated'])
    with (coordinated / 'PROMPT-ISSUER.txt').open('a') as stream: stream.write('The selected operational binding is SESSION-issuer.md.\n')
    save(coordinated / 'PROMPT-RECEIVER.txt', "Use the candidate spec plugin's stdo-work as recipient of incoming/issuer-return.md. Perform its selected bounded task and return through its declared result relation. The selected operational binding is SESSION-receiver.md.\n")
    review = Path(meta['projects']['review'])
    save(review / 'PROMPT-NEGATIVE.txt', "Use the candidate spec plugin's stdo-review as recipient of inbox/bad-packet.md. Return through its declared result relation. The selected operational binding is SESSION-negative.md.\n")
    for root_string in meta['projects'].values():
        root = Path(root_string)
        pin_paths += [root / 'admission.py']
        if (root / 'subject/service.py').exists(): pin_paths.append(root / 'subject/service.py')
        shutil.copytree(root, HERE / 'fixtures/initial' / root.name, symlinks=True)
    meta.update(candidate=str(candidate), candidate_loaded=True, source_freeze_sha256=FREEZE_SHA, python=PYTHON, manager=MANAGER, controls=str(controls), policies=policies)
    save(HERE / 'FIXTURES.json', meta)
    save(HERE / 'RUNTIME_PINS.json', {str(p): {'sha256': sha(p.read_bytes()), 'bytes': p.stat().st_size} for p in sorted(set(pin_paths))})
    save(HERE / 'PLAN.json', {'scope': 'final issuer and dependent receiver only; earlier native outcomes retained' , 'sessions': {'issuer': {'host': 'claude', 'seconds': 300}, 'receiver': {'host': 'claude', 'seconds': 240, 'depends': 'actual valid completed issuer packet'}}, 'oracle': {'sha256': sha((HERE / 'EXPECTATIONS.md').read_bytes()), 'not_supplied_to_actor': True}, 'business_grants': 'original contract bytes preserved', 'host_control_limit': 'direct tool calls only; trusted frozen helper and bootstrap/context limits separate', 'new_metadata': 'session settings, policies, command catalog, hook audit and final relay selected by fixture owner'})
    print(json.dumps({'suite': str(suite), 'freeze': FREEZE_SHA, 'policies': {k: v['policy_sha256'] for k, v in policies.items()}}, indent=2))


if __name__ == '__main__': main()
