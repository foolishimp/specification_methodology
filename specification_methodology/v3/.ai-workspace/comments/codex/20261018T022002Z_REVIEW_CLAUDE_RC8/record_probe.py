"""Independent record checks over immutable Git objects; no author checker runs.

These checks establish coordinates, counts and recorded standing, not semantic
conservation. Run with Python 3; the repository and installed basis are inputs.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import re
import subprocess

REPO = Path('/Users/jim/src/apps/specification_methodology')
PREFIX = 'specification_methodology/v3/build_tenants/claude/'
SOURCE = '9aee01ffa76cfbde1a6b8f1153a25bd6d71c216e'
PACKAGE = '1db13bfeb0675fc95de04aceccb214f5b76873fc'
BASELINE = '4a63c9293ddaa568803b81f1ed5dcc1d3dc19cec'
PREDECESSOR = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards')


@lru_cache(None)
def git_bytes(path, ref=SOURCE):
    return subprocess.check_output(['git', 'show', ref + ':' + PREFIX + path], cwd=REPO)


def sections(raw):
    """Heading bodies, excluding child headings, as declared by the records."""
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


@lru_cache(None)
def source_sections(member, ref=SOURCE):
    return sections(git_bytes('standards/' + member, ref))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    path = 'frontier/REVIEW.json'
    old = {r['id']: r for r in json.loads(git_bytes(path, BASELINE))['rows']}
    record = json.loads(git_bytes(path))
    rows = record['rows']
    assert set(old) == {r['id'] for r in rows}
    changed = [r for r in rows if r != old[r['id']]]
    counts = json.loads(git_bytes('qualification/C3-ITER5/COUNTS.json'))
    dispositions = Counter(r['disposition'] for r in rows)
    readings = Counter(r['semantic_review']['result'] for r in rows if r['disposition'] == 'conserved')
    assert len(rows) == record['row_count'] == counts['frontier_rows'] == 650
    assert dict(dispositions) == counts['by_disposition']
    assert dict(readings) == counts['conserved_by_review_result']
    assert readings['indeterminate'] == counts['conserved_unread'] == 419
    assert sum(n for k, n in readings.items() if k != 'indeterminate') == counts['conserved_read'] == 184
    assert sum(r['proposed_replacement'] for r in rows) == counts['proposed_replacements'] == 28
    assert len(changed) == 9
    checked = []
    for row in changed:
        predecessor = sections((PREDECESSOR / row['source_member']).read_bytes())
        assert sha(predecessor[row['source_anchor'][1:]]) == row['predecessor_sha256'], row['id']
        for item in row['successor_loci']:
            member, anchor = item['locus'].split('#', 1)
            assert git_bytes('standards/' + member) == git_bytes('standards/' + member, PACKAGE), member
            assert sha(source_sections(member)[anchor]) == item['sha256'], item['locus']
        assert row['acceptance'] == 'ticket_decision_pending', row['id']
        checked.append({'id': row['id'], 'disposition': row['disposition'],
                        'semantic_review': row['semantic_review']['result'],
                        'acceptance': row['acceptance'], 'loci_checked': len(row['successor_loci'])})

    # These two older assessments cover paragraphs that were not changed even
    # though their shared containing section has a changed drift paragraph.
    def paragraph(ref, start, end):
        text = source_sections('SPEC_METHOD.md', ref)['trace-closure-and-anti-drift'].decode()
        return text.split(start, 1)[1].split(end, 1)[0]
    for start, end in [('Ownership:', 'Downstream closure:'), ('Downstream closure:', 'Drift signals')]:
        assert paragraph(BASELINE, start, end) == paragraph(SOURCE, start, end), start

    path = 'qualification/C3-ITER5/determinations/DETERMINATIONS.json'
    determinants = json.loads(git_bytes(path))
    previous = {r['id']: r for r in json.loads(git_bytes(path, BASELINE))['records']}
    assert set(previous) == {r['id'] for r in determinants['records']}
    changed_determinants = [r for r in determinants['records'] if r != previous[r['id']]]
    consumer_checks = 0
    for row in changed_determinants:
        owner = row['owner']
        assert sha(source_sections(owner['member'])[owner['anchor']]) == owner['section_sha256'], row['id']
        for consumer in row['consumers']:
            if 'locus' in consumer:
                member, anchor = consumer['locus'].split('#', 1)
            else:
                member, anchor = consumer['member'], consumer['anchor']
            assert anchor in source_sections(member), (row['id'], member, anchor)
            consumer_checks += 1
    return {
        'kind': 'independent-rc8-record-probe', 'source': SOURCE, 'package': PACKAGE,
        'baseline': BASELINE, 'passed': True, 'frontier_rows': len(rows),
        'dispositions': dict(dispositions), 'conserved_review_results': dict(readings),
        'changed_frontier_records': checked,
        'unchanged_assessed_paragraphs': ['ownership', 'downstream closure'],
        'determination_records': len(determinants['records']),
        'changed_determination_records_checked': len(changed_determinants),
        'consumer_coordinates_checked': consumer_checks,
        'limits': 'Coordinates, counts, affected pins and stated review standing only. Resolved links do not prove consumer meaning. Historical semantic assessments retain their recorded scope. No member acceptance or whole-corpus semantic conservation is established.'
    }


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
