#!/usr/bin/env python3
"""Independent source-derived CLI probes. All writes stay in this review directory."""
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
sha=lambda data:hashlib.sha256(data).hexdigest()
def physical(text):
    return re.findall(r"[^\r\n]*(?:\r\n|\r|\n|$)",text)[:-1]
def expected(text, headings):
    lines=physical(text); sections={}
    for index,level,name in headings:
        end=next((n for n,d,_ in headings if n>index and d<=level),len(lines))
        body=''.join(lines[index:end])
        sections[name]={'heading':name,'first_line':index+1,'last_line':end,'sha256':sha(body.encode()),'text':body}
    catalog=[{'heading':name,'level':level,'first_line':index+1,'unique':sum(n==name for _,_,n in headings)==1} for index,level,name in headings]
    return catalog,sections
cases=[]
def add(name,text,headings,selected='One'):
    catalog,sections=expected(text,headings)
    cases.append({'name':name,'text':text,'expected_catalog':catalog,'expected_sections':sections,'selected':selected,'permitted_outcomes':'exact successful projection or explicit whole-projection refusal'})
separators=[('vt','\x0b'),('ff','\x0c'),('fs','\x1c'),('gs','\x1d'),('rs','\x1e'),('nel','\x85'),('ls','\u2028'),('ps','\u2029'),('nbsp','\u00a0')]
for name,char in separators:
    add('paragraph_'+name,'## One\nprefix'+char+'## Invented\ninside\n## Two\ntwo\n',[(0,2,'One'),(3,2,'Two')],'Invented')
for marker in ['```','~~~']:
    for name,char in [('nbsp','\u00a0'),('ls','\u2028'),('nel','\x85'),('vt','\x0b'),('ff','\x0c'),('emspace','\u2003')]:
        add(('backtick_' if marker[0]=='`' else 'tilde_')+'close_'+name,'## One\n'+marker+'\ncode\n'+marker+char+'\n## Invented\ninside\n',[(0,2,'One')],'Invented')
    for name,char in [('none',''),('space',' '),('tab','\t'),('space_tab',' \t ')]:
        add(('backtick_' if marker[0]=='`' else 'tilde_')+'valid_close_'+name,'## One\n'+marker+'\ncode\n'+marker+char+'\n## Two\ntwo\n',[(0,2,'One'),(4,2,'Two')])
for name,closer in [('short','```'),('wrong','~~~~'),('trailing_text','````x')]:
    add('fence_'+name,'## One\n````\ncode\n'+closer+'\n## Invented\ninside\n````\n## Two\ntwo\n',[(0,2,'One'),(7,2,'Two')])
for name,end in [('lf','\n'),('crlf','\r\n'),('cr','\r')]:
    add('line_endings_'+name,end.join(['## One','first','```','## Invented','```','last','## Two','two','']),[(0,2,'One'),(6,2,'Two')])
add('mixed_line_endings','## One\r\nfirst\rsecond\n## Two\rtwo',[(0,2,'One'),(3,2,'Two')])
add('nbsp_after_hash_not_heading','## One\n##\u00a0\ninside\n## Two\ntwo\n',[(0,2,'One'),(3,2,'Two')],'')
add('nbsp_title_preserved','## One\nbody\n## Name\u00a0\ntext\n',[(0,2,'One'),(2,2,'Name\u00a0')],'Name\u00a0')
add('ls_in_heading_text','## One\nbody\n## Name\u2028Part\ntext\n',[(0,2,'One'),(2,2,'Name\u2028Part')],'Name\u2028Part')
add('ascii_empty_heading','## One\nbody\n## \t\ntext\n',[(0,2,'One'),(2,2,'')],'')
add('nbsp_after_closing_hash','## One\nbody\n## Name ###\u00a0\ntext\n',[(0,2,'One'),(2,2,'Name ###\u00a0')],'Name ###\u00a0')
add('nbsp_before_closing_hash','## One\nbody\n## Name\u00a0###\ntext\n',[(0,2,'One'),(2,2,'Name\u00a0###')],'Name\u00a0###')
parser=argparse.ArgumentParser();parser.add_argument('--reader',type=Path);parser.add_argument('--label');parser.add_argument('--freeze-cases',action='store_true');args=parser.parse_args()
if args.freeze_cases:
    (BASE/'PROBE_CASES.json').write_text(json.dumps(cases,ensure_ascii=True,indent=2)+'\n');print(len(cases));sys.exit(0)
assert args.reader and args.label
reader=args.reader.resolve();runroot=BASE/'probes'/args.label;runroot.mkdir(parents=True,exist_ok=True)
rows=[]
for case in cases:
    scratch=runroot/case['name'];release=scratch/'release';member=release/'standards'/'OWNER.md';member.parent.mkdir(parents=True,exist_ok=True);member.write_bytes(case['text'].encode())
    manifest={'standards':{'installed_root':'standards','members':[{'path':'OWNER.md','sha256':sha(member.read_bytes())}]}}
    mp=release/'manifest.json';mp.write_text(json.dumps(manifest));uri='stdo://releases/review-unicode/'
    definition=scratch/'definition.json';identity='urn:review:unicode:'+case['name'];basis={'uri':uri,'manifest_sha256':sha(mp.read_bytes())}
    definition.write_text(json.dumps({'product':{'definition_id':identity},'constitution':{'stdo':{'basis':basis}}}))
    status={'installed':True,'valid':True,'failures':[],'definition_id':identity,'definition':str(definition),'basis':uri,'manifest_sha256':basis['manifest_sha256'],'path':str(release)}
    (scratch/'state.json').write_text(json.dumps({'status':status,'manifest':str(mp),'member':str(member)}))
    manager=scratch/'manager';manager.write_text('#!'+sys.executable+'\n'+"import json,sys\nfrom pathlib import Path\ns=json.loads((Path(__file__).parent/'state.json').read_text())\na=sys.argv[1:]\nif a[0]=='status': print(json.dumps(s['status']))\nelif a[0]=='resolve': print(json.dumps({'uri':a[1],'path':s['manifest'] if a[1].endswith('manifest.json') else s['member']}))\nelse: sys.exit(2)\n");manager.chmod(0o700)
    results=[]
    for selection in [['--list-headings'],['--heading',case['selected']],['--heading','One']]:
        argv=[sys.executable,'-I','-B',str(reader),'read','--stdo',str(manager),'--definition',str(definition),'--member','standards/OWNER.md']+selection
        proc=subprocess.run(argv,capture_output=True,text=True,cwd=scratch);response=json.loads(proc.stdout)
        refused=proc.returncode==1 and response.get('status')=='refused' and not any(k in response for k in ['sections','headings'])
        if selection[0]=='--list-headings': expected_result=case['expected_catalog'];actual=response.get('headings')
        else:
            section=case['expected_sections'].get(selection[1]);expected_result=[section] if section else None;actual=response.get('sections')
        exact=proc.returncode==0 and response.get('status')=='checked' and expected_result is not None and actual==expected_result
        results.append({'selection':selection,'command':argv,'exit':proc.returncode,'response':response,'stderr':proc.stderr,'explicit_refusal':refused,'exact_projection':exact,'supported':refused or exact})
    rows.append({'name':case['name'],'member_sha256':sha(member.read_bytes()),'results':results,'all_supported':all(r['supported'] for r in results)})
record={'reader':str(reader),'reader_sha256':sha(reader.read_bytes()),'probe_script_sha256':sha(Path(__file__).read_bytes()),'frozen_case_sha256':sha((BASE/'PROBE_CASES.json').read_bytes()),'scope':'Actual shipped helper CLI, controlled mock manager supplying exact control JSON and member hashes; no real install or native actor qualification.','cases':rows,'case_count':len(rows),'cli_calls':sum(len(r['results']) for r in rows),'unsupported_cases':[r['name'] for r in rows if not r['all_supported']]}
(BASE/(args.label+'_RESULTS.json')).write_text(json.dumps(record,ensure_ascii=True,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['reader_sha256','case_count','cli_calls','unsupported_cases']},indent=2))
