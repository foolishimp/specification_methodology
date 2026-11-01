import pathlib,json,subprocess,sys
b=pathlib.Path(__file__).parent;n=int(sys.argv[1]);run=b.parent.parent/'run'
c=json.loads((run/'generation/chunks.json').read_text())[n]['id']
p='/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code/ac_project.py'
r=subprocess.run(['python3','-B',p,'task','--run',str(run),'--chunk',c],capture_output=True,text=True)
(b/f'{n:02}.task.json').write_text(r.stdout);(b/f'{n:02}.task.stderr.txt').write_text(r.stderr)
print('EXIT',r.returncode,'STDERR',r.stderr);a=json.loads(r.stdout);print('STATUS',a['status'],'CHUNK',c,'TASK',a.get('task_sha256'))
ref=json.loads((b/'07.task.json').read_text());pre=a['prompt'].split('SOURCE_DATA_JSON:\n',1)[0]
if pre==ref['prompt'].split('SOURCE_DATA_JSON:\n',1)[0]:print('Full prompt prelude exactly matches already-read 07 task.')
else:print(pre)
if a['schema']==ref['schema']: print('Full schema exactly matches already-read 07 task.')
else:print(json.dumps(a['schema']))
for i,s in enumerate(json.loads(a['prompt'].split('SOURCE_DATA_JSON:\n',1)[1])):
 print('\nSECTION',i,s['path'],s['heading'],s['start_line'],s['end_line'])
 for l in s['lines']:print(str(l['number'])+': '+l['text'],end='')
