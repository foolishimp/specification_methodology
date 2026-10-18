#!/usr/bin/env python3
"""Bounded Git-object read and presented-source byte receipt for this review."""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = pathlib.Path('/Users/jim/src/apps/specification_methodology')
parser = argparse.ArgumentParser()
parser.add_argument('objects', nargs='*', help='commit:path, or local:absolute-path')
parser.add_argument('--start', type=int, default=1)
parser.add_argument('--stop', type=int)
parser.add_argument('--diff', nargs=2, metavar=('BASE', 'CANDIDATE'))
parser.add_argument('--paths', nargs='*', default=[])
parser.add_argument('--pattern')
parser.add_argument('--context', type=int, default=0)
args = parser.parse_args()
items = []
if args.diff:
    data = subprocess.check_output(['git', 'diff', '--no-ext-diff', '--unified=5',
                                    *args.diff, '--', *args.paths], cwd=REPO)
    items.append(('diff ' + ' '.join(args.diff) + ' ' + ' '.join(args.paths), data))
else:
    for obj in args.objects:
        if obj.startswith('local:'):
            data = pathlib.Path(obj[6:]).read_bytes()
        else:
            data = subprocess.check_output(['git', 'show', obj], cwd=REPO)
        items.append((obj, data))
with (HERE / 'SEMANTIC_ACQUISITION.jsonl').open('a') as log:
    for name, raw in items:
        lines = raw.decode('utf-8').splitlines(keepends=True)
        end = args.stop if args.stop is not None else len(lines)
        indexes = list(range(args.start-1, min(end, len(lines))))
        if args.pattern:
            selected_indexes = set()
            for n in indexes:
                if re.search(args.pattern, lines[n], re.I):
                    selected_indexes.update(range(max(args.start-1,n-args.context), min(end,len(lines),n+args.context+1)))
            indexes = sorted(selected_indexes)
        selected = [lines[n] for n in indexes]
        emitted = ''.join(f'{n+1}: {lines[n]}' for n in indexes)
        if emitted and not emitted.endswith('\n'):
            emitted += '\n'
        print('\nOBJECT ' + name)
        sys.stdout.write(emitted)
        record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  'object': name, 'source_bytes': len(raw),
                  'lines_start': args.start, 'lines_stop': min(end, len(lines)),
                  'selected_source_bytes': len(''.join(selected).encode()),
                  'presented_numbered_bytes': len(emitted.encode())}
        if args.pattern:
            record.update(pattern=args.pattern, context=args.context, selected_line_numbers=[n+1 for n in indexes])
        log.write(json.dumps(record) + '\n')
        print('ACQUISITION ' + json.dumps(record))
