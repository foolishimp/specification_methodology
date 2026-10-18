import sys,random,copy
from pathlib import Path
root=Path('a_c/build_tenants/graphify');sys.path[:0]=[str(root/'code'),str(root/'test_env')]
import ac_graph as ac
from fixture_support import toy_model,seal,uid

def oracle(m,seeds,budget=None):
 c=m.document['dependency_contract'];g=set(c['required_relation_kinds']);inc=set(seeds)
 req={rid:{r.target for r in m.references if r.owner==rid and r.target in m.records and r.schema['governing'] is True} for rid in m.records}
 while True:
  before=set(inc)
  for rid in tuple(inc):inc.update(req[rid])
  for rec in m.records.values():
   f=rec.fields
   if rec.family=='relations' and f['kind'] in g and (rec.identity in inc or f['source'] in inc):
    inc.add(rec.identity);inc.update(v for v in (f['source'],f['target']) if v in m.records)
   if rec.family in ('constraints','latitude','residuals'):
    subjects=[f['subject']] if rec.family=='residuals' else f['applies_to']
    if any(s in inc for s in subjects):inc.add(rec.identity)
  if inc==before:break
 ext=sorted({r.target for r in m.references if r.owner in inc and r.target in m.external})
 crossing=[{'id':r.identity,'kind':r.fields['kind'],'source':r.fields['source'],'target':r.fields['target']} for r in m.records.values() if r.family=='relations' and r.identity not in inc and (r.fields['source'] in inc or r.fields['target'] in inc)]
 return {'profile':'a_c.graphify.projection/1','parent':ac.model_identity(m),'selection':{'seeds':list(seeds),'dependency_contract':c,'budget_records':budget},'included':sorted(inc),'excluded':sorted(set(m.records)-inc),'populations':{f:[r.fields for r in m.records.values() if r.family==f and r.identity in inc] for f in ac.CORE_FIELDS},'boundary':{'external':[m.external[e] for e in ext],'unresolved_residuals':sorted(rid for rid in inc if m.records[rid].family=='residuals'),'crossing_relations':crossing,'non_governing_references':[{'owner':r.owner,'path':list(r.path),'target':r.target,'domain':r.schema['domain']} for r in m.references if r.owner in inc and r.target in m.records and r.target not in inc],'invalidation':m.document['interpretation']['invalidation']},'claim':'view of exact parent; not a replacement complete model or semantic acceptance'}
rng=random.Random(20261015);count=0
for trial in range(100):
 d=toy_model();df=d['signature']['definition'];d['dependency_contract']['required_relation_kinds']=rng.sample(list(df['relation_kinds']),rng.randrange(3))
 for group in ['fields','relation_kinds','constraint_kinds','residual_kinds','judgment_kinds','sorts']:
  def walk(x):
   if isinstance(x,dict):
    if x.get('type')=='ref' and x.get('local_families'):x['governing']=rng.choice([False,True])
    for v in x.values():walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(df[group])
 for relation in d['populations']['relations']:
  relation['source']=uid('object:'+rng.choice('abc'));relation['target']=uid('object:'+rng.choice('abc'));relation['kind']=rng.choice(list(df['relation_kinds']))
 for f in ['constraints','latitude']:
  d['populations'][f][0]['applies_to']=[uid('object:'+s) for s in rng.sample(list('abc'),rng.randrange(1,4))]
 # Vary residual attachments across legal object/relation/constraint targets.
 d['populations']['residuals'][0]['subject']=rng.choice([r['id'] for f in ['objects','relations','constraints'] for r in d['populations'][f]])
 seal(d);m=ac.validate(d)
 selections=[([rid],None) for rid in m.records]+[(rng.sample(list(m.records),rng.randrange(1,8)),None)]
 got=ac.project_many(m,selections)
 for (seeds,budget),actual in zip(selections,got):
  expected=oracle(m,seeds,budget)
  assert actual==expected,(trial,seeds,actual['included'],expected['included'])
  count+=1
print({'differential_cases':count,'randomized_models':100,'status':'passed'})
