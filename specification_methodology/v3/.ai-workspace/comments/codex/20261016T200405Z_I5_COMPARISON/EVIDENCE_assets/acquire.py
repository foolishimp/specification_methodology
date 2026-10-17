#!/usr/bin/env python3
"""Read frozen Git source and record exactly how many output bytes were presented."""
import argparse
import datetime
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path('/Users/jim/src/apps/specification_methodology')
ASSETS = pathlib.Path(__file__).resolve().parent

def record(label, text, source=None):
    data = text.encode('utf-8')
    with (ASSETS / 'acquisition.jsonl').open('a') as handle:
        handle.write(json.dumps({'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'label': label, 'source': source, 'presented_bytes': len(data)}) + '\n')
    sys.stdout.write(text)

def blob(sha, path):
    return subprocess.check_output(['git', 'show', f'{sha}:{path}'], cwd=REPO).decode('utf-8')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['read','match','tree','account'])
    parser.add_argument('sha', nargs='?')
    parser.add_argument('path', nargs='?')
    parser.add_argument('--lines')
    parser.add_argument('--pattern')
    parser.add_argument('--context', type=int, default=0)
    args=parser.parse_args()
    if args.mode == 'account':
        rows=[json.loads(line) for line in (ASSETS/'acquisition.jsonl').read_text().splitlines()]
        print(json.dumps({'presented_bytes_measured':sum(row['presented_bytes'] for row in rows),'bootstrap_allowance_bytes':32768,'total_upper_account':32768+sum(row['presented_bytes'] for row in rows),'records':len(rows)},indent=2))
        return
    if args.mode == 'tree':
        text=subprocess.check_output(['git','ls-tree','-rl',args.sha,args.path],cwd=REPO).decode()
        record('git tree metadata',text,f'{args.sha}:{args.path}')
        return
    source=blob(args.sha,args.path)
    lines=source.splitlines()
    selected=set(range(len(lines)))
    if args.lines:
        selected=set()
        for group in args.lines.split(','):
            bounds=group.split('-'); start=int(bounds[0]); end=int(bounds[-1])
            selected.update(range(start-1,min(end,len(lines))))
    if args.mode == 'match':
        selected=set()
        for i,line in enumerate(lines):
            if re.search(args.pattern,line,re.I):
                selected.update(range(max(0,i-args.context),min(len(lines),i+args.context+1)))
    output=f'SOURCE {args.sha}:{args.path}\n'+''.join(f'{i+1}: {lines[i]}\n' for i in sorted(selected))
    record(args.mode,output,f'{args.sha}:{args.path}')

if __name__=='__main__':
    main()
