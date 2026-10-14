"""Summarize recorded acquisition without inferring retained context or quality."""
from datetime import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
USE = HERE.parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    arms = []
    for arm in ('A', 'B', 'C'):
        root = USE / 'arms' / arm
        activation = json.loads((root / 'ACTIVATION.json').read_text())
        prompt = (root / 'ACTOR_PROMPT.md').read_bytes()
        tasks = (root / 'ACTOR_TASKS.json').read_bytes()
        if sha(prompt) != activation['actor_prompt_sha256'] or sha(tasks) != activation['task_sha256']:
            raise ValueError('Changed actor inputs: ' + arm)
        trace = (root / 'ACQUISITION.jsonl').read_bytes()
        events = [json.loads(line) for line in trace.splitlines() if line.strip()]
        if not events:
            raise ValueError('No recorded acquisition: ' + arm)
        times = [datetime.fromisoformat(e['utc']) for e in events]
        files = {r['path']: r for e in events for r in e['source_reads']}
        reads = [e for e in events if e['operation'] == 'read']
        artifacts = [{'path': str(p.relative_to(root / 'result')), 'bytes': p.stat().st_size,
                      'sha256': sha(p.read_bytes())}
                     for p in sorted((root / 'result').rglob('*')) if p.is_file()]
        if not (root / 'result/answers.json').is_file() or not (root / 'result/RETURN.md').is_file():
            raise ValueError('Actor return is incomplete: ' + arm)
        arms.append({
            'arm': arm, 'source': activation['source']['identity'],
            'task_sha256': activation['task_sha256'], 'explicit_actor_prompt_bytes': len(prompt),
            'task_packet_file_bytes': len(tasks), 'trace_sha256': sha(trace),
            'successful_acquisition_calls': len(events),
            'total_emitted_bytes': sum(e['emitted_bytes'] for e in events),
            'method_navigation_and_content_emitted_bytes': sum(e['emitted_bytes'] for e in events if e['operation'] in ('read', 'search', 'list')),
            'task_emitted_bytes': sum(e['emitted_bytes'] for e in events if e['operation'] == 'task'),
            'metadata_emitted_bytes': sum(e['emitted_bytes'] for e in events if e['operation'] == 'info'),
            'read_content_bytes_including_repeats': sum(e['content_bytes'] for e in reads),
            'source_io_bytes': sum(e['source_io_bytes'] for e in events),
            'unique_source_files_opened': len(files),
            'unique_source_file_bytes': sum(r['bytes'] for r in files.values()),
            'summed_reader_seconds': sum(e['tool_elapsed_seconds'] for e in events),
            'first_acquisition_utc': min(times).isoformat(),
            'last_acquisition_utc': max(times).isoformat(),
            'acquisition_window_seconds': (max(times) - min(times)).total_seconds(),
            'result_artifacts': artifacts,
        })
    if len({a['task_sha256'] for a in arms}) != 1:
        raise ValueError('Arms did not use the same task packet')
    report = {
        'kind': 'stdo.matched-use.acquisition-measurement', 'arms': arms,
        'boundaries': [
            'Successful logger emissions and file reads; delivery truncation and failed commands require actor disclosure.',
            'Navigation, content and repeated reads are included. Full source-file I/O is not loaded model context.',
            'The acquisition window excludes work before the first and after the last reader call; it is not full actor elapsed time.',
            'Inherited host instructions, retained context, attention, model/reasoning tokens and spend are uninstrumented.',
            'This report measures acquisition and pins returns; independent oracle grading owns task correctness.',
            'One actor per arm is a bounded comparison, not a general performance estimate.',
        ],
    }
    (HERE / 'MEASUREMENTS.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps([{'arm': a['arm'], 'emitted_bytes': a['total_emitted_bytes'],
                       'acquisition_window_seconds': a['acquisition_window_seconds']} for a in arms], indent=2))


if __name__ == '__main__':
    main()
