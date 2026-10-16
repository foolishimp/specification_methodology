#!/usr/bin/env python3
"""Bounded source-author checks; no semantic fidelity or acceptance judgment."""
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[9]
TENANT = Path(__file__).resolve().parents[5]
STANDARDS = TENANT / 'successor/standards'
PREIMAGE = '199c6d29bc02590a8b7f252043fc43223c09808d'
OWNERS = ('FOUNDATIONS', 'TRANSFORMATION_LIBRARY', 'REFERENCE_FRAME_METHOD',
          'STDO_REFERENCE_FRAME_BASELINE')


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def frozen(path):
    return subprocess.check_output(
        ['git', 'show', f'{PREIMAGE}:{path.relative_to(ROOT)}'],
        cwd=ROOT).decode()


def anchor(text):
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[^\w\- ]', '', text.lower()).replace(' ', '-')


def sections(text):
    lines = text.splitlines(keepends=True)
    points, fenced = [], False
    for index, line in enumerate(lines):
        if line.lstrip().startswith(('```', '~~~')):
            fenced = not fenced
        if not fenced:
            match = re.match(r'^(#{1,6}) (.+?)\s*$', line)
            if match:
                points.append((anchor(match[2]), index, match[2]))
    result = {}
    for i, (key, start, heading) in enumerate(points):
        end = points[i + 1][1] if i + 1 < len(points) else len(lines)
        result[key] = {'heading': heading, 'start_line': start + 1,
                       'end_line': end, 'body': ''.join(lines[start + 1:end])}
    return result


def run():
    failures, members, changed = [], {}, []
    headings_preserved = True
    current, previous = {}, {}
    for name in OWNERS:
        path = STANDARDS / f'{name}.md'
        current[name], previous[name] = path.read_text(), frozen(path)
        old, new = sections(previous[name]), sections(current[name])
        if list(old) != list(new):
            headings_preserved = False
            failures.append(f'{name}: heading identity/order changed')
        changed_ids = []
        for key in old:
            if old[key]['body'] != new[key]['body']:
                identity = f'{name}.{key}'
                changed.append(identity)
                changed_ids.append(identity)
        members[name] = {
            'path': str(path.relative_to(TENANT)),
            'preimage_sha256': digest(previous[name]),
            'candidate_sha256': digest(current[name]),
            'changed_ids': changed_ids,
        }

    preserved = {
        'FOUNDATIONS': ['result-algebra', 'result-conjunction',
                        'workspace-and-context', 'bounded-construction',
                        'configuration', 'orthogonal-descriptions'],
        'REFERENCE_FRAME_METHOD': ['rf-012-closed-results',
                                   'rf-006-authority-conservation',
                                   'rf-009-no-assumed-hierarchy',
                                   'rf-014-capability-fit',
                                   'rf-017-proportional-compression'],
        'STDO_REFERENCE_FRAME_BASELINE': ['work-result',
            'non-hierarchical-frame-configuration',
            '5a-candidate-does-not-require-independent-review',
            '5b-candidate-requires-independent-review',
            'actor-binding-and-independence'],
    }
    protected = []
    for name, keys in preserved.items():
        old, new = sections(previous[name]), sections(current[name])
        for key in keys:
            blocks = [part for part in old[key]['body'].split('\n\n') if part.strip()]
            intact = all(part in new[key]['body'] for part in blocks)
            protected.append({'id': f'{name}.{key}',
                              'all_preimage_paragraphs_retained': intact})
            if not intact:
                failures.append(f'{name}.{key}: changed protected paragraph')

    checked_links = []
    pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
    for name in OWNERS:
        path = STANDARDS / f'{name}.md'
        added = set(pattern.findall(current[name])) - set(pattern.findall(previous[name]))
        for link in sorted(added):
            if re.match(r'[a-zA-Z][\w+.-]*:', link):
                continue
            file_part, _, fragment = link.partition('#')
            target = (path.parent / unquote(file_part)).resolve() if file_part else path
            try:
                if target.parent == STANDARDS and target.stem in OWNERS:
                    text = current[target.stem]
                else:
                    text = frozen(target)
                found = not fragment or unquote(fragment) in sections(text)
                found = found or f'id="{fragment}"' in text or f'name="{fragment}"' in text
            except (ValueError, subprocess.CalledProcessError, UnicodeDecodeError):
                found = False
            checked_links.append({'source': name, 'target': link, 'resolves': found})
            if not found:
                failures.append(f'{name}: unresolved new link {link}')

    patch = json.loads((Path(__file__).parent / 'ACCOUNT_PATCH.json').read_text())
    patch_ids = [row['id'] for row in patch['changes']]
    if sorted(changed) != sorted(patch_ids):
        failures.append('Changed source headings and ACCOUNT_PATCH entries differ')
    account_path = TENANT / 'qualification/C3/iteration-3/DETERMINATIONS.json'
    account = json.loads(frozen(account_path))
    account_ids = {row['id'] for row in account['determinations']}
    for identity in patch_ids:
        if identity not in account_ids:
            failures.append(f'{identity}: absent from frozen account')
    for row in patch['changes']:
        name, key = row['id'].split('.', 1)
        body = sections(current[name])[key]['body']
        if row['candidate_body_sha256'] != digest(body):
            failures.append(f'{row["id"]}: stale candidate body pin')
        if row['result_mapping_change'] != 'none':
            failures.append(f'{row["id"]}: unexpected result mapping mutation')
        if 'consumers' in row.get('append_unique', {}):
            failures.append(f'{row["id"]}: reverse consumers added as active inputs')
        for relation in row.get('append_dependency_relations', []):
            if relation['target'] not in account_ids or not relation.get('required_when'):
                failures.append(f'{row["id"]}: missing conditional dependency binding')
        for reference in row.get('append_source_refs', []):
            if reference.get('acquisition_role') != 'provenance_only':
                failures.append(f'{row["id"]}: consumer route lost provenance standing')

    check = subprocess.run(['git', 'diff', '--check', '--'] + [
        str((STANDARDS / f'{name}.md').relative_to(ROOT)) for name in OWNERS],
        cwd=ROOT, capture_output=True, text=True)
    if check.returncode:
        failures.append('Scoped whitespace check failed: ' + check.stdout)
    return {'standing': 'source-author mechanical check only', 'preimage': PREIMAGE,
            'members': members, 'heading_identities_preserved': headings_preserved,
            'changed_heading_count': len(changed),
            'protected_source_checks': protected, 'new_links': checked_links,
            'account_patch_binding': 'checked against frozen 701-unit account',
            'failures': failures, 'passed': not failures}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)
