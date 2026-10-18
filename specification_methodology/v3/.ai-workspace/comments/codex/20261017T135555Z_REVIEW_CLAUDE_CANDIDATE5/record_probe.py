"""Read-only checks of the frozen candidate's affected conservation records.

Run with Python 3 from any directory. No candidate verification script is used.
This checks record identity and standing, not semantic conservation.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import subprocess

REPO = Path('/Users/jim/src/apps/specification_methodology')
PREFIX = 'specification_methodology/v3/build_tenants/claude/'
PACKAGE = 'a85f9ec98e43b942048a6c151aafd9662d2def90'
SOURCE = '4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec'
PREDECESSOR = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards')


def git_bytes(path, ref=PACKAGE):
    return subprocess.check_output(['git', 'show', ref + ':' + PREFIX + path], cwd=REPO)


def sections(raw):
    """The frontier declares one row per heading, excluding child sections."""
    result, counts, current, body = {}, Counter(), None, []
    fenced = False
    for line in raw.decode().splitlines(keepends=True):
        if line.startswith('```'):
            fenced = not fenced
        heading = re.match(r'^(#{1,6})\s+(.*)', line) if not fenced else None
        if heading:
            if current is not None:
                result[current] = ''.join(body).encode()
            base = re.sub(r'[^\w\- ]', '', heading[2].strip().lower().replace('`', '')).replace(' ', '-')
            suffix = counts[base]
            counts[base] += 1
            current = base if suffix == 0 else base + '-' + str(suffix)
            body = []
        else:
            body.append(line)
    if current is not None:
        result[current] = ''.join(body).encode()
    return result


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    record = json.loads(git_bytes('frontier/REVIEW.json'))
    rows = record['rows']
    counts = json.loads(git_bytes('qualification/C3-ITER5/COUNTS.json'))
    dispositions = Counter(row['disposition'] for row in rows)
    readings = Counter(row['semantic_review']['result'] for row in rows if row['disposition'] == 'conserved')
    assert len(rows) == record['row_count'] == counts['frontier_rows'] == 650
    assert dict(dispositions) == counts['by_disposition']
    assert dict(readings) == counts['conserved_by_review_result']
    assert readings['indeterminate'] == counts['conserved_unread'] == 423
    assert sum(n for k, n in readings.items() if k != 'indeterminate') == counts['conserved_read'] == 184
    assert sum(row['proposed_replacement'] for row in rows) == counts['proposed_replacements'] == 24
    targets = {
        'SPEC_METHOD.md#constitutional-chain',
        'SPEC_METHOD.md#renewal-path',
        'SPEC_METHOD.md#drift-signals',
        'SPEC_METHOD.md#method',
        'ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop',
    }
    checked = []
    for row in rows:
        if row['id'] not in targets:
            continue
        pred = sections((PREDECESSOR / row['source_member']).read_bytes())
        assert sha(pred[row['source_anchor'][1:]]) == row['predecessor_sha256'], row['id']
        for item in row['successor_loci']:
            member, anchor = item['locus'].split('#', 1)
            raw = git_bytes('standards/' + member, SOURCE)
            assert raw == git_bytes('standards/' + member), member
            assert sha(sections(raw)[anchor]) == item['sha256'], item['locus']
        assert row['semantic_review']['result'] == 'indeterminate', row['id']
        assert row['acceptance'] == 'ticket_decision_pending', row['id']
        if row['id'].startswith('SPEC_METHOD'):
            assert row['disposition'] == 'superseded' and row['proposed_replacement'], row['id']
        checked.append({'id': row['id'], 'disposition': row['disposition'],
                        'review': row['semantic_review']['result'],
                        'acceptance': row['acceptance'], 'successor_loci_checked': len(row['successor_loci'])})
    assert len(checked) == len(targets)
    return {'kind': 'independent-affected-record-check', 'source_commit': SOURCE,
            'package_commit': PACKAGE, 'passed': True, 'rows': len(rows),
            'dispositions': dict(dispositions), 'conserved_review_results': dict(readings),
            'affected_records': checked,
            'limits': 'Checks hashes, counts and recorded standing for five affected rows. Semantic conservation and owner acceptance are separate.'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2) + '\n', end='')
