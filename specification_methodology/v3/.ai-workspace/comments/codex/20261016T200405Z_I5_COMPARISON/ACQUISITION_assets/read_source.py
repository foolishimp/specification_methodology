#!/usr/bin/env python3
"""Bounded, logged Git-object source presentation for EC-I5-COMP-01 cone 3."""
import datetime, hashlib, json, re, subprocess, sys
from pathlib import Path

REPO = Path('/Users/jim/src/apps/specification_methodology')
LEDGER = Path(__file__).with_name('acquisition_ledger.json')
LIMIT = 512 * 1024

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {'source_limit_bytes': LIMIT, 'unique_presented_source_bytes': 0, 'seen_lines': {}, 'reads': []}
for req in json.load(sys.stdin):
    commit, path = req['commit'], req['path']
    data = git('show', f'{commit}:{path}')
    blob = git('rev-parse', f'{commit}:{path}').decode().strip()
    if 'json_rows' in req:
        selection = req['json_rows']
        source = json.loads(data)
        projected, pointers = [], []
        for index, row in enumerate(source[selection['array']]):
            if row[selection.get('key', 'id')] not in selection['ids']:
                continue
            projected.append({key: row[key] for key in selection['fields'] if key in row})
            pointers.append('/' + selection['array'] + '/' + str(index))
        body = json.dumps(projected, indent=2, ensure_ascii=False) + '\n'
        signature = hashlib.sha256((blob + body).encode()).hexdigest()
        seen = ledger.setdefault('seen_fragments', [])
        added = 0 if signature in seen else len(body.encode())
        if ledger['unique_presented_source_bytes'] + added > LIMIT:
            raise SystemExit('Presentation would exceed source acquisition allowance')
        ledger['unique_presented_source_bytes'] += added
        if signature not in seen:
            seen.append(signature)
        ledger['reads'].append({'time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'commit': commit, 'path': path, 'blob': blob, 'sha256': hashlib.sha256(data).hexdigest(), 'whole_blob_bytes_read_by_tool': len(data), 'json_pointer_rows': pointers, 'fields': selection['fields'], 'newly_presented_source_bytes': added, 'cumulative_unique_presented_source_bytes': ledger['unique_presented_source_bytes']})
        LEDGER.write_text(json.dumps(ledger, indent=2) + '\n')
        print(f'\nSOURCE JSON PROJECTION {commit}:{path} rows={pointers} newly_presented={added} cumulative={ledger["unique_presented_source_bytes"]}')
        print(body)
        continue
    lines = data.decode().splitlines(keepends=True)
    picked = set()
    if 'lines' in req:
        for a, b in req['lines']:
            picked.update(range(max(a, 1), min(b, len(lines)) + 1))
    elif 'match' in req:
        pattern, context = re.compile(req['match']), req.get('context', 0)
        for i, line in enumerate(lines, 1):
            if pattern.search(line):
                picked.update(range(max(i-context, 1), min(i+context, len(lines)) + 1))
    elif req.get('headings'):
        picked = {i for i, line in enumerate(lines, 1) if re.match(r'^#{1,6} ', line)}
    else:
        picked = set(range(1, len(lines) + 1))
    seen = set(ledger['seen_lines'].get(blob, []))
    added = sum(len(lines[i-1].encode()) for i in picked-seen)
    if ledger['unique_presented_source_bytes'] + added > LIMIT:
        raise SystemExit('Presentation would exceed source acquisition allowance')
    ledger['unique_presented_source_bytes'] += added
    ledger['seen_lines'][blob] = sorted(seen | picked)
    row = {'time_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'commit': commit, 'path': path, 'blob': blob, 'sha256': hashlib.sha256(data).hexdigest(), 'whole_blob_bytes_read_by_tool': len(data), 'presented_line_numbers': sorted(picked), 'newly_presented_source_bytes': added, 'cumulative_unique_presented_source_bytes': ledger['unique_presented_source_bytes']}
    ledger['reads'].append(row)
    print(f'\nSOURCE {commit}:{path} blob={blob} whole={len(data)} newly_presented={added} cumulative={ledger["unique_presented_source_bytes"]}')
    for i in sorted(picked):
        print(f'{i}: {lines[i-1]}', end='' if lines[i-1].endswith('\n') else '\n')
    LEDGER.write_text(json.dumps(ledger, indent=2) + '\n')
