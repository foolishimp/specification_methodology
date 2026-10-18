"""Bounded source acquisition for RC1-CONSUMERS; no account/source mutations."""
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[8]
BASE = 'specification_methodology/v3/build_tenants/codex/'
ACCOUNT_COMMIT = '57f711d964cd4eac8ed8523460cecc68bcaa63fb'
SOURCE_COMMIT = '5fd3b789ef6e0039f722676cdd0126113c745a11'
ACCOUNT_PATH = BASE + 'qualification/C3/iteration-5/DETERMINATIONS.json'
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / BASE / 'qualification/C3/iteration-5/tools'))
from account_protocol import heading_units


def git_bytes(commit, path):
    return subprocess.check_output(['git', 'show', commit + ':' + path], cwd=ROOT)


def account():
    return json.loads(git_bytes(ACCOUNT_COMMIT, ACCOUNT_PATH))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def sources(rows):
    return {path: git_bytes(SOURCE_COMMIT, BASE + 'successor/' + path)
            for path in sorted({r['owner']['path'] for r in rows})}


def unit(row, raw):
    if row['owner'].get('unit_scope') == 'whole_member':
        return dict(body=raw, byte_start=0, byte_end=len(raw), start_line=1,
                    end_line=len(raw.splitlines()), anchor='')
    return heading_units(raw)[row['owner']['anchor']]


def excerpt(body, limit):
    if not limit or len(body) <= limit:
        return body
    # Exact source prefix ending on a line boundary; never interpret a partial
    # acquisition as the complete law. Large JSON/table blocks stay bounded.
    return body[:limit].rsplit(b'\n', 1)[0]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--kind')
    p.add_argument('--member')
    p.add_argument('--ids', nargs='*')
    p.add_argument('--offset', type=int, default=0)
    p.add_argument('--count', type=int, default=20)
    p.add_argument('--limit', type=int, default=1200)
    a = p.parse_args()
    rows = account()['determinations']
    if a.ids:
        rows = [r for r in rows if r['id'] in a.ids]
    else:
        rows = [r for r in rows if not r.get('consumers')]
    if a.kind:
        rows = [r for r in rows if r['representation_kind'] == a.kind]
    if a.member:
        rows = [r for r in rows if r['owner']['path'] == 'standards/' + a.member + '.md']
    rows = rows[a.offset:a.offset+a.count]
    src = sources(rows)
    log_path = HERE / 'ACQUIRED_SLICES.json'
    log = json.loads(log_path.read_text()) if log_path.exists() else []
    prior = {(e['source_commit'], e['path'], e['byte_start'], e['byte_end']) for e in log}
    total = 0
    for r in rows:
        raw = src[r['owner']['path']]
        u = unit(r, raw)
        b = excerpt(u['body'], a.limit)
        rec = dict(id=r['id'], source_commit=SOURCE_COMMIT, path=r['owner']['path'],
                   anchor=r['owner'].get('anchor',''), byte_start=u['byte_start'],
                   byte_end=u['byte_start']+len(b), sha256=sha(b),
                   immediate_body_sha256=sha(u['body']), immediate_body_bytes=len(u['body']),
                   bytes=len(b), full_immediate_body=len(b)==len(u['body']))
        rec['repeat_exact_slice'] = (SOURCE_COMMIT,rec['path'],rec['byte_start'],rec['byte_end']) in prior
        log.append(rec)
        total += len(b)
        print('\nSOURCE', r['id'], 'KIND', r['representation_kind'],
              'BODY', len(u['body']), 'PRESENTED', len(b), 'LINE', u['start_line'])
        print(b.decode())
    log_path.write_text(json.dumps(log,indent=2)+'\n')
    print('PRESENTED_SOURCE_BYTES',total,'ROWS',len(rows))


if __name__ == '__main__':
    main()
