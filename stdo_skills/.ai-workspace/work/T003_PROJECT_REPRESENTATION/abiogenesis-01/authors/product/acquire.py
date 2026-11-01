import json
from pathlib import Path
import subprocess
import sys
from author_helpers import HERE, WORK, PROVIDER

index=int(sys.argv[1])
chunks=json.loads((WORK/'run/generation/chunks.json').read_text())
path=HERE/f'task-{index:02d}.json'
if not path.exists():
    command=[sys.executable,'-B',str(PROVIDER/'ac_project.py'),'task','--run',str(WORK/'run'),'--chunk',chunks[index]['id']]
    result=subprocess.run(command,capture_output=True,text=True)
    (HERE/f'task-{index:02d}-call.json').write_text(json.dumps({'command':command,'exit':result.returncode,'stderr':result.stderr},indent=2)+'\n')
    if result.returncode: raise RuntimeError(result.stdout+result.stderr)
    path.write_text(result.stdout)
task=json.loads(path.read_text())
source=json.loads(task['prompt'].split('\nSOURCE_DATA_JSON:\n',1)[1])
assert len(source)==len(chunks[index]['segments'])
for actual, frozen in zip(source,chunks[index]['segments']):
    assert all(actual[k]==v for k,v in frozen.items() if k!='text')
    assert ''.join(line['text'] for line in actual['lines'])==frozen['text']
print(task['status'],task['chunk'],task['task_sha256'])
for i,section in enumerate(source):
    print('\nSECTION',i,'LINES',section['start_line'],section['end_line'],section['heading'])
    print(''.join(line['text'] for line in section['lines']))
