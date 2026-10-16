"""Exercise measurement integrity and refusal before any live trial."""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('trial_acquisition', HERE / 'acquire.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    checks = []
    old_args = sys.argv
    with tempfile.TemporaryDirectory(prefix='stdo-acquisition-check-') as folder:
        root = Path(folder)
        source = root / 'source'
        source.mkdir()
        data = b'# Root\n\n## Selected\nfirst\n```text\n## False heading\n```\n### Child\nchild\n## Other\nlast\n'
        (source / 'source.md').write_bytes(data)
        (source / 'unselected.md').write_text('not a selected member\n')
        reader.ARMS = root / 'arms'
        arm = reader.ARMS / 'A'
        arm.mkdir(parents=True)
        task = json.dumps({'tasks': [{'task_id': 'T0'}]}).encode()
        (arm / 'ACTOR_TASKS.json').write_bytes(task)
        activation = {'ordinary_entry': 'source.md', 'assessment_boundary': 'fixture', 'task_sha256': sha(task),
                      'source': {'identity': 'fixture', 'materialized_root': str(source), 'members': [{'path': 'source.md', 'sha256': sha(data), 'bytes': len(data)}]}}
        (arm / 'ACTIVATION.json').write_text(json.dumps(activation))

        def invoke(*arguments):
            sys.argv = ['acquire.py', '--arm', 'A', *arguments]
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                reader.main()
            return stream.getvalue()

        first = invoke('read', 'source.md', '--section', 'selected')
        decoded = json.loads(first)
        assert 'False heading' in decoded['content'] and 'child' in decoded['content'] and 'last' not in decoded['content']
        checks.append('section honors fenced headings and includes selected children only')
        second = invoke('read', 'source.md', '--section', 'selected')
        events = [json.loads(line) for line in (arm / 'ACQUISITION.jsonl').read_text().splitlines()]
        assert len(events) == 2 and first == second
        assert sum(e['emitted_bytes'] for e in events) == len(first.encode()) + len(second.encode())
        assert sum(e['source_io_bytes'] for e in events) == 2 * len(data)
        checks.append('repeated acquisition is counted twice at exact emitted and source-I/O boundaries')
        before = (arm / 'ACQUISITION.jsonl').read_bytes()
        for path in ('unselected.md', '../ACTIVATION.json'):
            try:
                invoke('read', path)
                raise AssertionError('unexpected source permission')
            except ValueError:
                pass
        assert (arm / 'ACQUISITION.jsonl').read_bytes() == before
        checks.append('unselected and escaping paths refuse without emitting source')
        (source / 'source.md').write_bytes(data + b'changed\n')
        try:
            invoke('read', 'source.md')
            raise AssertionError('source drift accepted')
        except ValueError:
            pass
        assert (arm / 'ACQUISITION.jsonl').read_bytes() == before
        checks.append('source identity drift refuses before successful acquisition logging')
        (arm / 'ACTOR_TASKS.json').write_bytes(task + b' ')
        try:
            invoke('task', 'all')
            raise AssertionError('task drift accepted')
        except ValueError:
            pass
        checks.append('task byte drift refuses before use')
        sys.argv = old_args
    report = {'valid': True, 'checks': checks, 'scope': 'logger behavior in disposable fixtures; no actor, method correctness, security sandbox or complete host-context proof'}
    (HERE / 'CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
