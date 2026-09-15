"""Correct only the observed pre-exposure newline transcription; no native retry."""
from pathlib import Path
import hashlib
import json
import re
import shutil
from prepare_native import snapshot

HERE = Path(__file__).resolve().parent
PROOF = HERE.parent
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def put(path, value): path.write_text(json.dumps(value, indent=2) + '\n')

selection = json.loads((HERE / 'coverage-selection.json').read_text())
task = (PROOF / 'native-task.md').read_text()
c1, c2 = re.findall(r'```markdown\n(.*?)```', task, re.S)
assert sha(PROOF / 'native-task.md') == selection['task_sha256']
records = []
for case in selection['contexts']:
    dest, work = Path(case['directory']), Path(case['worksite'])
    assert not (dest / 'command.json').exists(), 'Native exposure forbids fixture correction'
    archive = HERE / 'pre-exposure-correction' / case['name']
    archive.mkdir(parents=True)
    for root, label in [(work, 'worksite'), (dest / 'input', 'input')]:
        for relative in ['fixtures/C1/current.md', 'fixtures/C2/current.md', 'draft/current.md', 'evidence.json']:
            source, target = root / relative, archive / label / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        (root / 'fixtures/C1/current.md').write_text(c1)
        (root / 'fixtures/C2/current.md').write_text(c2)
        (root / 'draft/current.md').write_text(c2)
        evidence = json.loads((root / 'evidence.json').read_text())
        evidence['C1']['sha256'] = sha(root / 'fixtures/C1/current.md')
        evidence['C2']['sha256'] = sha(root / 'fixtures/C2/current.md')
        put(root / 'evidence.json', evidence)
    for name in ['snapshot-before.json', 'confinement-preflight.json']:
        shutil.copy2(dest / name, archive / name)
    put(dest / 'snapshot-before.json', snapshot(work))
    records.append({'context': case['name'], 'exposed': False, 'C1_sha256': sha(work / 'fixtures/C1/current.md'), 'C2_sha256': sha(work / 'fixtures/C2/current.md'), 'snapshot_sha256': sha(dest / 'snapshot-before.json')})
selection['prepare_sha256'] = sha(HERE / 'prepare_native.py')
put(HERE / 'coverage-selection.json', selection)
put(HERE / 'pre-exposure-correction.json', {'scope': 'Correct literal backslash-n transport transcription to exact frozen task UTF-8/LF snippets; select explicitly granted Codex xhigh before exposure. No native invocation occurred.', 'contexts': records})
print(json.dumps({'corrected_unexposed_contexts': len(records)}))
