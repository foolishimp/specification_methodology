"""Independent raw CLI specimens; no native models or source changes.

The manager double supplies exact synthetic fixture identities. This tests the
reader CLI's projection/refusal boundary, not a real STDO installation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'stack_release.json').exists())
COMMIT = '0aa00244602293d8e0fd384b7a280ae443afcd7d'
SOURCE = 'specification_methodology/v3/build_tenants/common/plugins/spec/scripts/read_basis.py'


def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(path, value): path.write_text(json.dumps(value, ensure_ascii=True, indent=2) + '\n')


def specimens():
    cases = []
    def positive(name, text, body, headings, last_line):
        cases.append({'name': name, 'text': text, 'outcome': 'projection',
                      'one_text': body, 'one_last_line': last_line, 'headings': headings})
    # Expected coordinates are manually fixed per specimen, not parsed by the implementation.
    for label, separator in [('VT', '\v'), ('FF', '\f'), ('FS', '\x1c'), ('GS', '\x1d'),
                             ('RS', '\x1e'), ('NEL', '\x85'), ('LS', '\u2028'), ('PS', '\u2029')]:
        body = '## One\nparagraph' + separator + '## Phantom\nkept\n'
        positive('paragraph-' + label, body + '## Two\nexcluded\n', body,
                 [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
                  {'heading': 'Two', 'level': 2, 'first_line': 4, 'unique': True}], 3)
    for label, suffix in [('NBSP', '\u00a0'), ('EM_SPACE', '\u2003'),
                          ('NNBSP', '\u202f'), ('IDEOGRAPHIC_SPACE', '\u3000')]:
        opening = '## One\n```text\ninside\n```' + suffix + '\n## Phantom\nstill code\n'
        cases.append({'name': 'fence-' + label + '-unclosed', 'text': opening, 'outcome': 'refuse'})
        body = opening + '```\n'
        positive('fence-' + label + '-later-close', body + '## Two\nexcluded\n', body,
                 [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
                  {'heading': 'Two', 'level': 2, 'first_line': 8, 'unique': True}], 7)
    for label, ending in [('LF', '\n'), ('CR', '\r'), ('CRLF', '\r\n')]:
        lines = ['## One', 'first', '### Nested', 'kept', '## Two', 'excluded']
        positive('line-ending-' + label, ending.join(lines) + ending,
                 ending.join(lines[:4]) + ending,
                 [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
                  {'heading': 'Nested', 'level': 3, 'first_line': 3, 'unique': True},
                  {'heading': 'Two', 'level': 2, 'first_line': 5, 'unique': True}], 4)
    positive('line-ending-mixed', '## One\r\nfirst\r### Nested\nkept\r\n## Two\nexcluded',
             '## One\r\nfirst\r### Nested\nkept\r\n',
             [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
              {'heading': 'Nested', 'level': 3, 'first_line': 3, 'unique': True},
              {'heading': 'Two', 'level': 2, 'first_line': 5, 'unique': True}], 4)
    for label, closing in [('SPACE', '``` '), ('TAB', '```\t'), ('SPACES_TAB', '  ``` \t')]:
        body = '## One\n```text\n## Phantom\n' + closing + '\n'
        positive('fence-positive-' + label, body + '## Two\nexcluded\n', body,
                 [{'heading': 'One', 'level': 2, 'first_line': 1, 'unique': True},
                  {'heading': 'Two', 'level': 2, 'first_line': 5, 'unique': True}], 4)
    return cases


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--reader', type=Path)
    args = parser.parse_args()
    expectation = HERE / 'EXPECTATIONS.json'
    if not expectation.exists():
        save(expectation, {'basis': 'User counterexamples and predecessor closed-ATX projection contract; CR/LF/CRLF are physical line endings; other Unicode separators are literal paragraph data; fence trailing whitespace is ASCII space/tab only.',
                          'frozen_before_successor_exposure': True, 'specimens': specimens()})
    cases = json.loads(expectation.read_text())['specimens']
    assert cases == specimens(), 'expectation freeze changed'
    out = HERE / args.label
    out.mkdir(exist_ok=False)
    scratch = Path(tempfile.mkdtemp(prefix='stdo304-unicode-' + args.label + '-', dir='/private/tmp'))
    if args.reader is None:
        raw = subprocess.run(['git', 'show', COMMIT + ':' + SOURCE], cwd=REPO, capture_output=True, check=True).stdout
        blob = subprocess.run(['git', 'rev-parse', COMMIT + ':' + SOURCE], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
        reader = scratch / 'read_basis.py'; reader.write_bytes(raw)
        save(out / 'SOURCE.json', {'commit': COMMIT, 'source_path': SOURCE, 'git_blob': blob, 'sha256': sha(raw), 'bytes': len(raw), 'copied_reader': str(reader)})
    else:
        reader = scratch / 'read_basis.py'; reader.write_bytes(args.reader.read_bytes())
        save(out / 'SOURCE.json', {'source_path': str(args.reader), 'sha256': sha(reader.read_bytes()), 'bytes': reader.stat().st_size, 'copied_reader': str(reader)})
    shutil.copyfile(reader, out / 'read_basis.py')
    release = scratch / 'release'; (release / 'standards').mkdir(parents=True)
    member = release / 'standards/OWNER.md'
    definition = scratch / 'definition.json'
    state_path = scratch / 'manager-state.json'
    manager = scratch / 'manager.py'
    manager.write_text('#!' + sys.executable + '\n' + '''import json,pathlib,sys
state=json.loads((pathlib.Path(__file__).parent/'manager-state.json').read_text())
args=sys.argv[1:]
assert args[:2]==['--store',state['store']]
args=args[2:]
if args[0]=='status': print(json.dumps(state['status']))
elif args[0]=='resolve': print(json.dumps({'uri':args[1],'path':state['routes'][args[1]]}))
else: raise SystemExit(3)
''')
    manager.chmod(0o755)
    rows = []
    for case in cases:
        raw = case['text'].encode('utf-8'); member.write_bytes(raw)
        manifest = {'standards': {'installed_root': 'standards', 'members': [{'path': 'OWNER.md', 'sha256': sha(raw)}]}}
        manifest_raw = (json.dumps(manifest) + '\n').encode(); (release / 'manifest.json').write_bytes(manifest_raw)
        uri = 'stdo://releases/v0-unicode-fixture/'
        basis = {'uri': uri, 'manifest_sha256': sha(manifest_raw)}
        definition.write_text(json.dumps({'product': {'definition_id': 'urn:fixture:unicode'}, 'constitution': {'stdo': {'basis': basis}}}))
        save(state_path, {'store': str(scratch / 'store'), 'status': {'definition': str(definition), 'definition_id': 'urn:fixture:unicode', 'basis': uri, 'manifest_sha256': basis['manifest_sha256'], 'path': str(release), 'installed': True, 'valid': True, 'failures': []}, 'routes': {uri + 'manifest.json': str(release / 'manifest.json'), uri + 'standards/OWNER.md': str(member)}})
        for selector in ['One', 'Phantom', 'catalog']:
            command = [sys.executable, '-B', str(reader), 'read', '--stdo', str(manager), '--store', str(scratch / 'store'), '--definition', str(definition), '--member', 'standards/OWNER.md']
            command += ['--list-headings'] if selector == 'catalog' else ['--heading', selector]
            run = subprocess.run(command, capture_output=True, text=True, timeout=10)
            value = json.loads(run.stdout)
            want_refusal = case['outcome'] == 'refuse' or selector == 'Phantom'
            if want_refusal:
                ok = run.returncode == 1 and value.get('status') == 'refused' and 'sections' not in value and 'headings' not in value
            elif selector == 'catalog':
                ok = run.returncode == 0 and value.get('status') == 'checked' and value.get('headings') == case['headings'] and 'sections' not in value
            else:
                body = case['one_text']
                expected = [{'heading': 'One', 'first_line': 1, 'last_line': case['one_last_line'], 'sha256': sha(body.encode()), 'text': body}]
                ok = run.returncode == 0 and value.get('status') == 'checked' and value.get('sections') == expected
            rows.append({'case': case['name'], 'selector': selector, 'raw_source_sha256': sha(raw), 'raw_source_utf8_hex': raw.hex(), 'argv': command, 'exit': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr, 'actual': value, 'expected': 'refusal without projection' if want_refusal else ('exact catalog' if selector == 'catalog' else 'exact raw section, lines and digest'), 'passes': ok and not run.stderr})
    save(out / 'RESULTS.json', rows)
    save(out / 'SUMMARY.json', {'specimens': len(cases), 'cli_calls': len(rows), 'passes': sum(bool(r['passes']) for r in rows), 'failures': [{'case': r['case'], 'selector': r['selector'], 'status': r['actual'].get('status'), 'reason': r['actual'].get('reason')} for r in rows if not r['passes']], 'expectation_sha256': sha(expectation.read_bytes()), 'scratch': str(scratch), 'manager_scope': 'explicit synthetic manager double; projection CLI evidence only', 'reader_sha256': sha(reader.read_bytes())})
    print((out / 'SUMMARY.json').read_text())


if __name__ == '__main__': main()
