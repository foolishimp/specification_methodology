from pathlib import Path
import argparse,subprocess,json,re,hashlib
p=argparse.ArgumentParser();p.add_argument('commit');p.add_argument('paths',nargs='+');p.add_argument('--headings',action='store_true');p.add_argument('--match');p.add_argument('--radius',type=int,default=0);p.add_argument('--span',action='append');a=p.parse_args()
base=Path(__file__).resolve().parent; ledger=base/'acquisition.json'; records=json.loads(ledger.read_text())
for path in a.paths:
 data=subprocess.check_output(['git','show',a.commit+':'+path],cwd='/Users/jim/src/apps/specification_methodology');lines=data.decode().splitlines(keepends=True)
 ids=set()
 if a.headings:
  ids.update(i for i,s in enumerate(lines,1) if re.match(r'^#{1,6} ',s))
 if a.match:
  for i,s in enumerate(lines,1):
   if re.search(a.match,s,re.I):ids.update(range(max(1,i-a.radius),min(len(lines),i+a.radius)+1))
 if a.span:
  for sp in a.span:
   lo,hi=sp.split(':');ids.update(range(int(lo),min(len(lines),int(hi))+1))
 if not (a.headings or a.match or a.span):ids=set(range(1,len(lines)+1))
 print('\nSOURCE '+a.commit+':'+path+'; file_bytes='+str(len(data))+'; lines='+str(len(lines)))
 for i in sorted(ids):print(str(i)+': '+lines[i-1].rstrip('\n'))
 records.append({'commit':a.commit,'path':path,'line_ids':sorted(ids),'line_bytes':{str(i):len(lines[i-1].encode()) for i in ids},'sha256':hashlib.sha256(data).hexdigest()})
seen={}
for r in records:
 for i,n in r['line_bytes'].items():seen[(r['commit'],r['path'],i)]=n
ledger.write_text(json.dumps(records,indent=2)+'\n')
print('\nACQUISITION unique_presented_source_bytes='+str(sum(seen.values()))+'; presentations='+str(len(records)))
