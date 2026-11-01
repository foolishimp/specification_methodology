"""Serialization and exact-source location for Codex-authored semantic records.
No source interpretation is performed by this helper.
"""
import json, hashlib, sys
from pathlib import Path
BASE=Path(__file__).parent
RUN=BASE.parent.parent/'run'
PROVIDER=Path('/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
sys.path.insert(0,str(PROVIDER))
import ac_generate
class Draft:
 def __init__(self,index):
  self.index=index
  self.task=json.loads((BASE/f'task-{index:02d}.json').read_text())
  self.sections=json.loads(self.task['prompt'].split('SOURCE_DATA_JSON:\n',1)[1])
  self.chunk=json.loads((RUN/'generation/chunks.json').read_text())[index]
  self.answer={k:[] for k in ['concepts','relations','constraints','latitude','residuals','dispositions','limitations']}
 def grounds(self,refs):
  result=[]
  for section,start,end in refs:
   s=self.sections[section]
   assert s['start_line']<=start<=end<=s['end_line']
   quote=''.join(l['text'] for l in s['lines'] if start<=l['number']<=end)
   assert quote.strip()
   result.append({'section_id':s['id'],'start_line':start,'end_line':end,'quote':quote})
  return result
 def concept(self,key,label,definition,refs,conditions=(),exceptions=()):
  self.answer['concepts'].append(dict(key=key,label=label,definition=definition,conditions=list(conditions),exceptions=list(exceptions),grounding=self.grounds(refs)))
 def constraint(self,key,targets,statement,refs,conditions=(),exceptions=(),uncertainty=''):
  self.answer['constraints'].append(dict(key=key,applies_to_keys=targets,statement=statement,conditions=list(conditions),exceptions=list(exceptions),uncertainty=uncertainty,grounding=self.grounds(refs)))
 def relation(self,key,kind,source,target,meaning,refs,governing=False,conditions=(),exceptions=()):
  self.answer['relations'].append(dict(key=key,kind=kind,source_key=source,target_key=target,meaning=meaning,governing=governing,conditions=list(conditions),exceptions=list(exceptions),grounding=self.grounds(refs)))
 def latitude(self,key,targets,allowed,forbidden,refs):
  self.answer['latitude'].append(dict(key=key,applies_to_keys=targets,allowed=allowed,forbidden=forbidden,grounding=self.grounds(refs)))
 def residual(self,key,subject,uncertainty,consequence,refs):
  self.answer['residuals'].append(dict(key=key,subject_key=subject,uncertainty=uncertainty,consequence=consequence,grounding=self.grounds(refs)))
 def disposition(self,section,decision,reason,keys=None):
  sid=self.sections[section]['id']
  if keys is None:
   keys=[r['key'] for family in ['concepts','relations','constraints','latitude','residuals'] for r in self.answer[family] if any(g['section_id']==sid for g in r['grounding'])]
  self.answer['dispositions'].append(dict(section_id=sid,decision=decision,keys=keys,reason=reason))
 def finish(self,limitations):
  self.answer['limitations']=limitations
  path=BASE/f'draft-{self.index:02d}.json'
  assert not path.exists()
  path.write_text(json.dumps(self.answer,ensure_ascii=False,indent=2)+'\n')
  ac_generate.author_check(self.answer,self.chunk)
  receipt={'chunk':self.chunk['id'],'index':self.index,'task_sha256':self.task['task_sha256'],'draft':str(path),'answer_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'author':'codex-gtl-frame','author_check':'passed','scope':'schema, exact source grounding, local reference closure and disposition coverage; not semantic acceptance'}
  (BASE/f'check-{self.index:02d}.json').write_text(json.dumps(receipt,indent=2)+'\n')
  ready_path=BASE/'READY.json'
  ready=json.loads(ready_path.read_text()) if ready_path.exists() else {}
  ready[self.chunk['id']]=receipt
  ready_path.write_text(json.dumps(ready,indent=2)+'\n')
  print(json.dumps(receipt))
