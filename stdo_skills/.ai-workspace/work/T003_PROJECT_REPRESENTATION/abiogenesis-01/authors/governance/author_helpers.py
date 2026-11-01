import json,sys,hashlib
from pathlib import Path
HERE=Path(__file__).parent
BASE=HERE.parents[1]
PROVIDER=Path('/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
sys.path.insert(0,str(PROVIDER))
import ac_generate
class Author:
 def __init__(self,index):
  self.index=index;self.task=json.loads((HERE/f'task-{index}.json').read_text())
  self.chunk=json.loads((BASE/'run/generation/chunks.json').read_text())[index]
  assert self.task['chunk']==self.chunk['id']
  supplied=json.loads(self.task['prompt'].split('SOURCE_DATA_JSON:\n',1)[1])
  assert [(s['id'],''.join(l['text'] for l in s['lines'])) for s in supplied]==[(s['id'],s['text']) for s in self.chunk['segments']]
  self.a={k:[] for k in ['concepts','relations','constraints','latitude','residuals','dispositions','limitations']}
 def g(self,sec,start,end=None):
  s=self.chunk['segments'][sec];end=start if end is None else end
  assert s['start_line']<=start<=end<=s['end_line']
  quote=''.join(s['text'].splitlines(keepends=True)[start-s['start_line']:end-s['start_line']+1]).rstrip('\n')
  return {'section_id':s['id'],'start_line':start,'end_line':end,'quote':quote}
 def add(self,f,key,gr,**fields):
  self.a[f].append(dict(key=key,grounding=gr,**fields))
 def c(self,key,label,definition,gr,conditions=[],exceptions=[]):self.add('concepts',key,gr,label=label,definition=definition,conditions=conditions,exceptions=exceptions)
 def q(self,key,targets,statement,gr,conditions=[],exceptions=[],uncertainty=''):self.add('constraints',key,gr,applies_to_keys=targets,statement=statement,uncertainty=uncertainty,conditions=conditions,exceptions=exceptions)
 def r(self,key,kind,source,target,meaning,gr,governing=False,conditions=[],exceptions=[]):self.add('relations',key,gr,kind=kind,source_key=source,target_key=target,meaning=meaning,governing=governing,conditions=conditions,exceptions=exceptions)
 def l(self,key,targets,allowed,forbidden,gr):self.add('latitude',key,gr,applies_to_keys=targets,allowed=allowed,forbidden=forbidden)
 def u(self,key,subject,uncertainty,consequence,gr):self.add('residuals',key,gr,subject_key=subject,uncertainty=uncertainty,consequence=consequence)
 def done(self,ds,limitations):
  records=[r for f in ['concepts','relations','constraints','latitude','residuals'] for r in self.a[f]]
  assert set(ds)==set(range(len(self.chunk['segments'])))
  for i,(decision,reason) in ds.items():
   s=self.chunk['segments'][i];keys=[r['key'] for r in records if any(g['section_id']==s['id'] for g in r['grounding'])]
   self.a['dispositions'].append(dict(section_id=s['id'],decision=decision,keys=keys,reason=reason))
  self.a['limitations']=limitations
  ac_generate.author_check(self.a,self.chunk)
  path=HERE/f'answer-{self.index}.json'
  with path.open('x') as f:json.dump(self.a,f,indent=2,ensure_ascii=False);f.write('\n')
  receipt={'chunk_index':self.index,'chunk_id':self.chunk['id'],'task_sha256':self.task['task_sha256'],'answer':str(path),'answer_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'author':'codex-governance-frame','author_check':'passed','counts':{k:len(v) for k,v in self.a.items()}}
  with (HERE/f'answer-{self.index}.receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
  print(json.dumps(receipt))
