from pathlib import Path
import argparse, hashlib, html, json, os, posixpath, re, subprocess
from urllib.parse import unquote
ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--assets',required=True);args=ap.parse_args()
root=Path(args.repo).resolve();assets=Path(args.assets).resolve();subject=json.loads((assets/'subject.json').read_text());sha=subject['subject'];prefix='specification_methodology/v3/';cache={};anchors_cache={}
def get(path):
 if path not in cache:
  r=subprocess.run(['git','show',sha+':'+path],cwd=root,capture_output=True);cache[path]=r.stdout if r.returncode==0 else None
 return cache[path]
def anchors(data):
 key=hashlib.sha256(data).hexdigest()
 if key in anchors_cache:return anchors_cache[key]
 seen={};out=set();fence=None
 for line in data.decode().splitlines():
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m.group(1)[0]
   elif fence==m.group(1)[0]:fence=None
   continue
  if fence:continue
  m=re.match(r'^#{1,6}\s+(.+?)(?:\s+#+)?$',line)
  if m:
   title=html.unescape(m.group(1));title=re.sub(r'!?\[([^]]+)\]\([^)]*\)',r'\1',title);title=re.sub(r'<[^>]*>','',title)
   a=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-');n=seen.get(a,0);seen[a]=n+1;out.add(a+(f'-{n}' if n else ''))
 out.update(re.findall(r'(?:id|name)=["\']([^"\']+)["\']',data.decode()));anchors_cache[key]=out;return out
errors=[];links=0;skipped=[];pin_errors=[];whitespace=[]
for member in subject['members']:
 path=prefix+member['path'];data=get(path)
 if data is None or len(data)!=member['bytes'] or hashlib.sha256(data).hexdigest()!=member['sha256']:pin_errors.append(path);continue
 for n,line in enumerate(data.decode().splitlines(),1):
  if re.search(r'[\t ]+$',line):whitespace.append({'path':path,'line':n})
 if not path.endswith('.md'):continue
 text=data.decode();fence=None
 for n,line in enumerate(text.splitlines(),1):
  fm=re.match(r'^\s*(`{3,}|~{3,})',line)
  if fm:
   if fence is None:fence=fm.group(1)[0]
   elif fence==fm.group(1)[0]:fence=None
   continue
  if fence:continue
  for m in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)',line):
   target=unquote(m.group(1).strip('<>'));base,_,frag=target.partition('#');linked=None
   if base.startswith('stdo://releases/'):
    p=Path('/Users/jim/Library/Application Support/STDO/releases')/base[len('stdo://releases/'):];linked=p.read_bytes() if p.is_file() else b'' if p.is_dir() else None
   elif re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',base) or base.startswith('/'):
    skipped.append({'source':path,'line':n,'target':target});continue
   else:
    p=posixpath.normpath(posixpath.join(posixpath.dirname(path),base)) if base else path
    if p.startswith('../'):skipped.append({'source':path,'line':n,'target':target});continue
    linked=get(p)
    # git show on a directory yields tree listing; links to directories are valid.
   links+=1
   if linked is None:errors.append({'source':path,'line':n,'target':target,'error':'missing target'});continue
   if frag and base.split(':')[-1].endswith('.md') or frag and not base:
    if frag not in anchors(linked):errors.append({'source':path,'line':n,'target':target,'error':'missing anchor'})
# Verify frozen C3-I5-05 tuple independently of review-subject manifest.
ticket=get(prefix+'.ai-workspace/tickets/active/T-002-c3-successor-construction.md').decode()
section=ticket.split('## C3-I5-05 proposed input snapshot\n',1)[1].split('\n## ',1)[0];B=re.search(r'Input commit B: `([a-f0-9]{40})`',section).group(1);rows=re.findall(r'^\| `([^`]+)` \| (\d+) \| `([a-f0-9]{64})` \|$',section,re.M);input_errors=[]
for path,n,digest in rows:
 b=subprocess.check_output(['git','show',B+':'+prefix+path],cwd=root)
 if len(b)!=int(n) or hashlib.sha256(b).hexdigest()!=digest:input_errors.append(path)
result={'subject':sha,'members':len(subject['members']),'bytes':sum(m['bytes'] for m in subject['members']),'pins_failed':pin_errors,'input':{'id':'C3-I5-05','source':B,'pins':len(rows),'errors':input_errors},'links_checked':links,'link_errors':errors,'skipped_external':skipped,'trailing_whitespace':whitespace}
(assets/'mechanical-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(pin_errors or input_errors or errors))
