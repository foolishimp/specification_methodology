import json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
command,job=sys.argv[1:]
if command not in {'status','send'} or job!='JOB-17': raise SystemExit(2)
p=root/'events.jsonl'
if command=='send':
 with p.open('a') as stream: stream.write(json.dumps({'job':job,'state':'delivered'})+'\n')
rows=[json.loads(x) for x in p.read_text().splitlines() if x]
print(json.dumps({'job':job,'delivery_count':sum(x['job']==job and x['state']=='delivered' for x in rows),'observation_owner':'dispatch-service-v1'}))
