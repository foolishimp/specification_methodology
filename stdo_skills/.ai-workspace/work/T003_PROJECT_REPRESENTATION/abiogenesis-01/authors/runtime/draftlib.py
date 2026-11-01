import json, pathlib, sys, traceback, hashlib
BASE=pathlib.Path(__file__).parent
RUN=BASE.parent.parent/'run'
PROVIDER=pathlib.Path('/Users/jim/src/apps/specification_methodology/a_c/build_tenants/graphify/code')
sys.path.insert(0,str(PROVIDER))
import ac_generate
class Draft:
 def __init__(self,n):
  self.n=n; self.task=json.loads((BASE/f'{n:02}.task.json').read_text()); self.s=json.loads(self.task['prompt'].split('SOURCE_DATA_JSON:\n',1)[1]); self.a={k:[] for k in ('concepts','relations','constraints','latitude','residuals','dispositions','limitations')}; self.ds={}
 def g(self,s,l=None,e=None):
  z=self.s[s]; l=z['start_line'] if l is None else l; e=z['end_line'] if e is None else e
  quote=''.join(x['text'] for x in z['lines'] if l<=x['number']<=e)
  assert quote.strip(); return {'section_id':z['id'],'start_line':l,'end_line':e,'quote':quote}
 def add(self,f,k,s,l,e,**x):
  z={'key':k,'grounding':[self.g(s,l,e)],**x}; self.a[f].append(z);return k
 def c(self,k,s,l,e,label,definition,conditions=(),exceptions=()):
  return self.add('concepts',k,s,l,e,label=label,definition=definition,conditions=list(conditions),exceptions=list(exceptions))
 def q(self,k,s,l,e,targets,statement,conditions=(),exceptions=(),uncertainty=''):
  return self.add('constraints',k,s,l,e,applies_to_keys=targets.split(),statement=statement,uncertainty=uncertainty,conditions=list(conditions),exceptions=list(exceptions))
 def r(self,k,s,l,e,source,target,kind,meaning,governing=False,conditions=(),exceptions=()):
  return self.add('relations',k,s,l,e,source_key=source,target_key=target,kind=kind,meaning=meaning,governing=governing,conditions=list(conditions),exceptions=list(exceptions))
 def v(self,k,s,l,e,targets,allowed=(),forbidden=()):
  return self.add('latitude',k,s,l,e,applies_to_keys=targets.split(),allowed=list(allowed),forbidden=list(forbidden))
 def u(self,k,s,l,e,subject,uncertainty,consequence):
  return self.add('residuals',k,s,l,e,subject_key=subject,uncertainty=uncertainty,consequence=consequence)
 def disposition(self,s,decision,reason): self.ds[s]=(decision,reason)
 def finish(self,observations=()):
  records=[r for f in ('concepts','relations','constraints','latitude','residuals') for r in self.a[f]]
  for i,s in enumerate(self.s):
   keys=[r['key'] for r in records if any(g['section_id']==s['id'] for g in r['grounding'])]
   decision,reason=self.ds.get(i,('retained','The selected local records retain the material meaning of this supplied section; this disposition is not a completeness claim.'))
   assert keys or decision in ('omitted','inapplicable','refused'),(i,s['heading'])
   self.a['dispositions'].append({'section_id':s['id'],'decision':decision,'keys':keys,'reason':reason})
  self.a['limitations'] += list(observations)
  self.a['limitations'] += ['This local source interpretation does not resolve identities across chunks or execute the represented runtime. Section processing and exact grounding do not prove semantic completeness, implementation conformity, acceptance, qualification, or release.']
  p=BASE/f'{self.n:02}.draft.json';p.write_text(json.dumps(self.a,indent=2,ensure_ascii=False)+'\n')
  chunk=next(x for x in json.loads((RUN/'generation/chunks.json').read_text()) if x['id']==self.task['chunk'])
  report={'chunk_id':self.task['chunk'],'task_sha256':self.task['task_sha256'],'draft_path':str(p),'author':'codex-runtime-frame','counts':{k:len(v) for k,v in self.a.items()},'observations':list(observations)}
  try: ac_generate.author_check(self.a,chunk);report['author_check']='passed'
  except Exception as ex: report['author_check']='failed';report['diagnostic']=str(ex)
  (BASE/f'{self.n:02}.check.json').write_text(json.dumps(report,indent=2)+'\n')
  print(json.dumps(report))
  return report
