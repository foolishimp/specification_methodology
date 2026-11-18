from pathlib import Path
import json,hashlib,re,subprocess
w=Path(__file__).resolve().parent;r=w.parents[2];a=w/'assessment/semantic-03'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
execution=read(a/'EXECUTION.json');assert execution['exit_code']==0
report=(a/'ASSESSMENT.md').read_text();matches=[json.loads(x) for x in re.findall(r'```json\s*(.*?)\s*```',report,re.S)];j=next(x for x in matches if x.get('kind')=='stdo.rc3-semantic-assessment/1');assert j['result']==j['visual_result']=='satisfied'
for row in read(a/'FREEZE.json')['files']:assert sha(Path(row['path']))==row['sha256'],row['path']
subjects={x['name']:x for x in read(a/'SUBJECTS.json')['subjects']};assert set(subjects)=={x['name'] for x in j['assessments']} and len(subjects)==8
out=a/'assessments';out.mkdir()
for row in j['assessments']:
 assert row['status']=='supported';s=subjects[row['name']]
 for k in ['index_sha256','corpus_sha256','query_sha256']:assert row[k]==s[k]
 evidence=row.get('evidence') or row.get('reason');assert evidence
 obj={k:row[k] for k in ['index_sha256','corpus_sha256','query_sha256','status']};obj.update(evaluator='Claude Opus 5.5 independent read-only semantic-03; exact verbatim return '+str(a/'ASSESSMENT.md')+' sha256 '+sha(a/'ASSESSMENT.md'),evidence=[evidence] if isinstance(evidence,str) else evidence)
 (out/(row['name']+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
(a/'TRANSCRIPTION.json').write_text(json.dumps({'report_sha256':sha(a/'ASSESSMENT.md'),'execution_sha256':sha(a/'EXECUTION.json'),'subject_count':8,'status':'transcribed-external-supported-judgments','scope':'No Writer-generated semantic verdict; all identities verified against actual external return and frozen subjects.'},indent=2)+'\n')
b=read(w/'NATIVE_BINDING.json');c=w/'context';old=read(c/'trial-hosts-01/RESULT.json')['negative_predecessor_assessment']
args=['python3','-B',c/'run_distribution_checks.py','--products-root',w/'packaged-products-03','--native-root',b['installed_root'],'--stdo',b['manager'],'--store',b['store'],'--python',w/'manager/bin/python','--fixture-root',c/'final-use-02/fixture','--queries-root',c/'final-use-02/queries','--predecessor-assessment',old,'--out',w/'assessed-packaged','--assessment-python',out/'python.json','--assessment-profile',out/'profile.json','--assessment-sdlc',out/'sdlc.json','--assessment-boundaries',out,'--remove']
p=subprocess.run(list(map(str,args)),capture_output=True);(w/'ASSESSED_PACKAGED.stdout').write_bytes(p.stdout);(w/'ASSESSED_PACKAGED.stderr').write_bytes(p.stderr);(w/'ASSESSED_PACKAGED_COMMAND.json').write_text(json.dumps({'argv':list(map(str,args)),'exit':p.returncode},indent=2)+'\n');print(p.stdout.decode(),flush=True);p.check_returncode()
hosts=read(w/'assessed-packaged/RESULT.json');assert all(x['passed'] for x in hosts['operations'])
for name,h in hosts['hosts'].items():
 assert h['removed'] and all(x['covered'] for x in h['contexts'])
 assert all(x['covered'] for x in h['boundary_controls'] if x['case'] in ['acceptance','qualification','release','work','triage'])
triage=read(c/'trial-hosts-04/codex-triage-boundary/CONTEXT.json')['payload'];assert next(x for x in triage['selected'] if x['rule']['id']=='W11')['applicability']=='true'
(c/'FINAL_RESULT.json').write_text(json.dumps({'status':'passed-for-eight-declared-exact-queries','method':hosts['method'],'portable_context_manifest_sha256':hosts['public_manifest_sha256'],'skills_inventory_sha256':hosts['skills_inventory_sha256'],'source_context_manifest_sha256':sha(r/'purpose_context/PUBLIC_MANIFEST.json'),'independent_report':str(a/'ASSESSMENT.md'),'independent_report_sha256':sha(a/'ASSESSMENT.md'),'assessed_packaged_operations':len(hosts['operations']),'covered_queries_per_host':8,'hosts':list(hosts['hosts']),'repairs':{'A1':'six class identifiers and owning Product/Goals layers retained; proposed-repair triage context selects W11','A2':'RC3 hypothetical scenarios declare RC2 predecessor and actual basis','A3':'source id/path correspondence plus preimage and ground digest refuse mismatch','semantic-02-F1':'W11 explicitly requires no-drift proof, smaller-change assertion and class label is not a satisfied result'},'limits':['Exact declared queries only; unknown facts refuse delivery.','No automatic native host pickup, task correctness or consumer adoption asserted.','Trial-hosts-02 triage did not select W11 because repair_planned was false. That original observation is retained; final-use-02 and trial-hosts-03 explicitly declare a hypothetical proposed repair and select W11.']},indent=2)+'\n')
print('exact assessments and final packaged consumption closed',flush=True)
