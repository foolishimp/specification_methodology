"""Record emitted acquisition for one frozen matched-use arm.

Instruction-confined trial tooling; not a security sandbox or a host-token meter.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import time

HERE = Path(__file__).resolve().parent
ARMS = HERE.parent / 'arms'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def confined(root, name):
    path = (root / name).resolve()
    path.relative_to(root.resolve())
    return path


def section(content, anchor):
    lines, headings, seen, fence = content.splitlines(keepends=True), [], {}, None
    for index, line in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            char = marker[1][0]
            if fence is None:
                fence = char
            elif fence == char:
                fence = None
            continue
        if fence:
            continue
        match = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        slug = re.sub(r'[^\w\-\s]', '', match[2].lower()).strip().replace(' ', '-')
        suffix = seen.get(slug, 0)
        seen[slug] = suffix + 1
        slug += '-' + str(suffix) if suffix else ''
        headings.append((index, len(match[1]), slug))
    for offset, (start, level, slug) in enumerate(headings):
        if slug == anchor:
            end = next((i for i, depth, _ in headings[offset + 1:] if depth <= level), len(lines))
            return ''.join(lines[start:end]), start + 1, end
    raise ValueError('No source heading: ' + anchor)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--arm', choices=['A', 'B', 'C'], required=True)
    sub = parser.add_subparsers(dest='operation', required=True)
    sub.add_parser('info')
    task = sub.add_parser('task'); task.add_argument('task_id', nargs='?', default='all')
    listing = sub.add_parser('list'); listing.add_argument('--prefix', default='')
    reading = sub.add_parser('read'); reading.add_argument('path'); reading.add_argument('--section'); reading.add_argument('--start', type=int); reading.add_argument('--end', type=int)
    search = sub.add_parser('search'); search.add_argument('pattern'); search.add_argument('--prefix', default=''); search.add_argument('--glob', default='*.md')
    args = parser.parse_args()
    arm = ARMS / args.arm
    activation = read_json(arm / 'ACTIVATION.json')
    inventory = {r['path']: r for r in activation['source']['members']}
    root = Path(activation['source']['materialized_root'])
    started = time.monotonic()
    scans = []

    def source(name):
        if name not in inventory:
            raise ValueError('Not a selected source member: ' + name)
        path = confined(root, name)
        if path.is_symlink():
            raise ValueError('Source symlink is not admitted')
        data = path.read_bytes()
        if sha(data) != inventory[name]['sha256']:
            raise ValueError('Source drift: ' + name)
        scans.append({'path': name, 'bytes': len(data), 'sha256': sha(data)})
        return data.decode()

    if args.operation == 'info':
        payload = {'arm': args.arm, 'ordinary_entry': activation['ordinary_entry'], 'subject': activation['source']['identity'],
                   'assessment_boundary': activation['assessment_boundary'], 'source_members': len(inventory),
                   'task_sha256': activation['task_sha256'], 'result_territory': str(arm / 'result')}
    elif args.operation == 'task':
        data = (arm / 'ACTOR_TASKS.json').read_bytes()
        if sha(data) != activation['task_sha256']:
            raise ValueError('Task input drift')
        packet = json.loads(data)
        selected = packet['tasks'] if args.task_id == 'all' else [t for t in packet['tasks'] if t['task_id'] == args.task_id]
        if not selected:
            raise ValueError('Unknown task')
        payload = dict(packet, tasks=selected)
    elif args.operation == 'list':
        payload = {'members': [r for k,r in sorted(inventory.items()) if k.startswith(args.prefix)]}
    elif args.operation == 'search':
        regex = re.compile(args.pattern, re.I)
        matches = []
        for name in sorted(inventory):
            if not name.startswith(args.prefix) or not Path(name).match(args.glob):
                continue
            for number, line in enumerate(source(name).splitlines(), 1):
                if regex.search(line):
                    matches.append({'path': name, 'line': number, 'text': line})
        payload = {'matches': matches}
    else:
        content = source(args.path)
        if args.section and (args.start or args.end):
            raise ValueError('Select a section or lines, not both')
        if args.section:
            content, start, end = section(content, args.section)
        else:
            lines = content.splitlines(keepends=True)
            start, end = args.start or 1, args.end or len(lines)
            if not 1 <= start <= end <= len(lines):
                raise ValueError('Invalid source interval')
            content = ''.join(lines[start - 1:end])
        payload = {'path': args.path, 'source_sha256': inventory[args.path]['sha256'], 'start_line': start, 'end_line': end,
                   'content_sha256': sha(content.encode()), 'content_bytes': len(content.encode()), 'content': content}
    emitted = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    event = {'utc': datetime.now(timezone.utc).isoformat(), 'operation': args.operation, 'arguments': vars(args),
             'emitted_bytes': len(emitted.encode()), 'emitted_sha256': sha(emitted.encode()), 'content_bytes': payload.get('content_bytes'),
             'source_reads': scans, 'source_io_bytes': sum(x['bytes'] for x in scans), 'tool_elapsed_seconds': time.monotonic() - started,
             'measurement_boundary': 'bytes emitted by this logger; delivery truncation, retained context, model tokens and reasoning are not measured'}
    with (arm / 'ACQUISITION.jsonl').open('a') as out:
        out.write(json.dumps(event, ensure_ascii=False) + '\n')
    sys.stdout.write(emitted)


if __name__ == '__main__':
    main()
