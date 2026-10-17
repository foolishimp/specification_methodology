from pathlib import Path
import argparse,subprocess,json,re,hashlib
p=argparse.ArgumentParser();p.add_argument('commit');p.add_argument('path');p.add_argument('--match');p.add_argument('--radius',type=int,default=0);p.add_argument('--span',action='append');a=p.parse_args()
base=Path(__file__).resolve().parent; ledger=base/'acquisition.json';records=json.loads(ledger.read_text())
data=subprocess.check_output(['git','show',a.commit+':'+a.path],cwd='/Users/jim/src/apps/specification_methodology');lines=data.decode().splitlines(keepends=True);ids=set()
if a.match:
 for i,s in enumerate(lines,1):
  if re.search(a.match,s,re.I):ids.update(range(max(1,i-a.radius),min(len(lines),i+a.radius)+1))
if a.span:
 for sp in a.span:
  lo,hi=map(int,sp.split(':'));ids.update(range(lo,min(len(lines),hi)+1))
if not (a.match or a.span):ids=set(range(1,len(lines)+1))
record={'commit':a.commit,'path':a.path,'line_bytes':{str(i):len(lines[i-1].encode()) for i in ids},'sha256':hashlib.sha256(data).hexdigest()}
projected=sum(sum(r['line_bytes'].values()) for r in records)+sum(record['line_bytes'].values())
if projected>65536:raise SystemExit('REFUSED: cumulative source presentations would exceed 64 KiB: '+str(projected))
print('\nSOURCE '+a.commit+':'+a.path)
for i in sorted(ids):print(str(i)+': '+lines[i-1].rstrip('\n'))
records.append(record);ledger.write_text(json.dumps(records,indent=2)+'\n')
print('TRI_PRESENTED_BYTES_CUMULATIVE='+str(projected))
