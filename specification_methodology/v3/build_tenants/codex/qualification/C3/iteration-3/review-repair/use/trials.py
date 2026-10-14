"""Frozen, instruction-confined task acquisition; no host-context fit claim."""
import argparse
from contextlib import redirect_stdout
from datetime import datetime, timezone
import fcntl
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[4]
REPO = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
PREFIX = str(TENANT.relative_to(REPO)) + '/successor/'
ORACLE = HERE / 'oracle'
SELECTIONS = {
    'T1': ('EVALUATION_CONJUNCTION', ['FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'REFERENCE_FRAME_METHOD']),
    'T2': ('CONSTITUTIONAL_DERIVATION', ['FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'SPEC_METHOD', 'DESIGN_MODULE_METHOD', 'REFERENCE_FRAME_METHOD']),
    'T3': ('CONSTITUTIONAL_DERIVATION', ['FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'SPEC_METHOD', 'DESIGN_MODULE_METHOD', 'REFERENCE_FRAME_METHOD']),
    'T4': ('RELEASE_ADOPTION', ['FOUNDATIONS', 'RELEASE_METHOD', 'SPEC_METHOD', 'REFERENCE_FRAME_METHOD']),
    'T5': ('WORK_RECOVERY', ['FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'SPEC_METHOD', 'TICKET_METHOD', 'REFERENCE_FRAME_METHOD']),
    'T6': ('TRIAGE_CARRIER', ['FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'SPEC_METHOD', 'TICKET_METHOD', 'REFERENCE_FRAME_METHOD']),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def git_data(commit, name):
    return subprocess.check_output(['git', 'show', commit + ':' + PREFIX + name], cwd=REPO)


def prepare(commit, evaluation_projection):
    if subprocess.check_output(['git', 'rev-parse', commit + '^{commit}'], cwd=REPO, text=True).strip() != commit:
        raise ValueError('Require full immutable source commit')
    if (HERE / 'runs').exists():
        raise ValueError('Existing runs are immutable evidence; select a successor before retry')
    # Verify the independently frozen oracle assets before selecting any task.
    for line in (ORACLE / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        if sha((ORACLE / name).read_bytes()) != digest:
            raise ValueError('Oracle drift: ' + name)
    root = Path(tempfile.mkdtemp(prefix='stdo-i3-repair-use-')).resolve()
    for task, (frame_name, owners) in SELECTIONS.items():
        actor = root / task
        actor.mkdir()
        routes = {}
        def add(route, data):
            name = str(len(routes)) + '.txt'
            (actor / name).write_bytes(data)
            (actor / name).chmod(0o444)
            routes[route] = {'file': name, 'bytes': len(data), 'sha256': sha(data)}
        add('task', (ORACLE / 'actor/shared-wrapper.txt').read_bytes() + b'\n' + (ORACLE / ('actor/tasks/' + task + '.txt')).read_bytes())
        frame_path = 'standards/frames/' + frame_name + '.md'
        if task == 'T1':
            if not evaluation_projection:
                raise ValueError('Bind the frozen native Evaluate/Conjoin projection for T1')
            frame = subprocess.check_output(['git', 'show', commit + ':' + evaluation_projection], cwd=REPO)
            frame_path = evaluation_projection
        else:
            frame = git_data(commit, frame_path)
        add('run://' + task + '/frame', frame)
        for owner in owners:
            name = 'standards/' + owner + '.md'
            add('run://' + task + '/method/' + name, git_data(commit, name))
        if task == 'T5':
            for name in ['workspace-current', 'source-current', 'submission-observation']:
                add('case://T5/' + name, (ORACLE / ('case-resources/T5/' + name + '.txt')).read_bytes())
        # Limits cover the selected frame plus three equal-size source acquisitions
        # and task/route overhead. Host-retained context is explicitly unmeasured.
        cap = max(262144, 4 * len(frame) + 32768)
        manifest = {'task': task, 'source_commit': commit, 'selected_frame': frame_path,
                    'routes': routes, 'maximum_acquired_bytes': cap, 'wall_seconds': 600,
                    'limit_basis': 'Selected frame plus up to three equal-size dependency reads and 32 KiB task/routing margin; at least 256 KiB. Ten minutes bounds one synthetic task, not method work.',
                    'started_utc': None, 'started_monotonic': None,
                    'actor_identity': None,
                    'context_boundary': 'Fresh native nonauthor activation; actor message, reader output measured separately; host/tool schemas and active retained context unknown.',
                    'authority': 'Response/in-memory task effects only; parent-owned reader instrumentation appends acquisition evidence. No external paid calls, filesystem task effects or publication.',
                    'source_boundary': 'Frozen candidate assessment only; no installed-v3 or adoption claim. Read only listed routes through this reader. Common sources, other candidates, reviews and withheld oracle are excluded.',
                    'independence': 'Fresh same-family nonauthor task actor; no cross-family acceptance claim.'}
        write(actor / 'manifest.json', manifest)
        out = HERE / 'runs' / task
        out.mkdir(parents=True)
        write(out / 'PREPARATION.json', dict(manifest, actor_root=str(actor), reader_sha256=sha(Path(__file__).read_bytes())))
    write(HERE / 'PREPARATION.json', {'source_commit': commit, 'actor_root': str(root), 'tasks': list(SELECTIONS),
                                    'oracle_commit': '17f981e4ad7e35c663cd936e535c15a59809dfa6',
                                    'oracle_manifest_sha256': sha((ORACLE / 'artifact-manifest.json').read_bytes()),
                                    'frozen_domain_binding_frame': 'Not selected: its continuation/projection/Markov scope does not match T3 mass typing. T3 uses the declared typed-construction frame and source routes.'})
    print(root)


def acquire(root, route, section, start, end):
    # This local POSIX harness can receive concurrent reader processes. Keep
    # first-read timing, cumulative admission and event append one transaction.
    # OS ownership releases the lock on process exit; the empty file is no lease.
    with (root / '.reader.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return acquire_locked(root, route, section, start, end)


def acquire_locked(root, route, section, start, end):
    manifest = json.loads((root / 'manifest.json').read_text())
    log = root / 'acquisition.jsonl'
    prior = [json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
    begun = manifest['started_monotonic']
    if begun is None:
        begun = time.monotonic()
        manifest.update(started_monotonic=begun, started_utc=datetime.now(timezone.utc).isoformat())
        write(root / 'manifest.json', manifest)
    if time.monotonic() - begun > manifest['wall_seconds']:
        raise ValueError('Admitted task time exceeded; return current result')
    scanned_bytes = 0
    if route == 'measurements':
        content = json.dumps({'cumulative_acquired_bytes_before_this_report': sum(x['emitted_bytes'] for x in prior),
                              'elapsed_seconds': time.monotonic() - begun,
                              'maximum_acquired_bytes': manifest['maximum_acquired_bytes'],
                              'wall_seconds': manifest['wall_seconds'],
                              'host_and_active_retained_context': 'unknown',
                              'native_spend': 'unknown', 'additional_paid_calls': 0}, indent=2)
    elif route == 'catalog':
        content = json.dumps({k: {'bytes': v['bytes'], 'sha256': v['sha256']} for k, v in manifest['routes'].items()}, indent=2)
    else:
        if route not in manifest['routes']:
            raise ValueError('Undeclared route')
        row = manifest['routes'][route]
        path = (root / row['file']).resolve()
        path.relative_to(root.resolve())
        data = path.read_bytes()
        scanned_bytes = len(data)
        if sha(data) != row['sha256']:
            raise ValueError('Source drift')
        content = data.decode()
        if section:
            if start or end:
                raise ValueError('Select a section or lines, not both')
            parser_file = HERE.parents[1] / 'use-r2/harness/acquire.py'
            spec = importlib.util.spec_from_file_location('prior_section_parser', parser_file)
            parser = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(parser)
            content, _, _ = parser.section(content, section)
        elif start or end:
            content = ''.join(content.splitlines(keepends=True)[(start or 1)-1:end])
    emitted = content.encode()
    total = sum(x['emitted_bytes'] for x in prior) + len(emitted)
    if total > manifest['maximum_acquired_bytes']:
        raise ValueError('Admitted acquisition allowance exceeded; return current result')
    event = {'route': route, 'section': section, 'start': start, 'end': end,
             'emitted_bytes': len(emitted), 'source_bytes_scanned_by_reader': scanned_bytes,
             'sha256': sha(emitted), 'cumulative_bytes': total,
             'elapsed_seconds': time.monotonic() - begun, 'utc': datetime.now(timezone.utc).isoformat()}
    with log.open('a') as stream:
        stream.write(json.dumps(event) + '\n')
    print(content, end='')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='operation', required=True)
    p = sub.add_parser('prepare'); p.add_argument('--source-commit', required=True)
    p.add_argument('--evaluation-projection', required=True)
    r = sub.add_parser('read'); r.add_argument('root', type=Path); r.add_argument('route')
    r.add_argument('--section'); r.add_argument('--start', type=int); r.add_argument('--end', type=int)
    sub.add_parser('self-check')
    args = parser.parse_args()
    if args.operation == 'prepare':
        prepare(args.source_commit, args.evaluation_projection)
    elif args.operation == 'read':
        acquire(args.root, args.route, args.section, args.start, args.end)
    else:
        checks = {}
        with tempfile.TemporaryDirectory(prefix='stdo-i3-reader-control-') as folder:
            root = Path(folder)
            data = b'# Subject\nExact task material.\n'
            (root / '0.txt').write_bytes(data)
            manifest = {'routes': {'run://control/frame': {'file': '0.txt', 'sha256': sha(data), 'bytes': len(data)}},
                        'started_monotonic': None, 'started_utc': None, 'maximum_acquired_bytes': 512, 'wall_seconds': 600}
            write(root / 'manifest.json', manifest)
            with redirect_stdout(io.StringIO()) as captured:
                acquire(root, 'run://control/frame', None, None, None)
            logged = json.loads((root / 'acquisition.jsonl').read_text())
            checks['exact_material_and_emission_measurement'] = captured.getvalue().encode() == data and logged['emitted_bytes'] == len(data) and logged['sha256'] == sha(data)
            def refused(route):
                previous = (root / 'acquisition.jsonl').read_bytes()
                try:
                    with redirect_stdout(io.StringIO()):
                        acquire(root, route, None, None, None)
                except ValueError:
                    return (root / 'acquisition.jsonl').read_bytes() == previous
                return False
            checks['undeclared_route_refused_without_material'] = refused('oracle')
            (root / '0.txt').write_bytes(data + b'changed')
            checks['changed_source_refused_without_material'] = refused('run://control/frame')
            (root / '0.txt').write_bytes(data)
            current = json.loads((root / 'manifest.json').read_text())
            current['maximum_acquired_bytes'] = len(data)
            write(root / 'manifest.json', current)
            checks['cumulative_allowance_refused_before_emission'] = refused('run://control/frame')
            current.update(maximum_acquired_bytes=512, started_monotonic=time.monotonic()-601)
            write(root / 'manifest.json', current)
            checks['expired_trial_refused_before_emission'] = refused('run://control/frame')
        report = {'valid': all(checks.values()), 'checks': checks, 'reader_sha256': sha(Path(__file__).read_bytes()),
                  'limit': 'Reader behavior only; instruction confinement is not a filesystem security boundary or host-context measurement.'}
        write(HERE / 'READER_CHECK.json', report)
        print(json.dumps(report, indent=2))
        if not report['valid']:
            raise SystemExit(1)


if __name__ == '__main__':
    main()
