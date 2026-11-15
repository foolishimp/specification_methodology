from pathlib import Path
import hashlib,json,subprocess,zipfile
w=Path(__file__).resolve().parent
p=w/'public-readback'
assets=p/'assets'

def run(name,args):
    r=subprocess.run([str(x) for x in args],capture_output=True,text=True)
    (p/(name+'.stdout')).write_text(r.stdout)
    (p/(name+'.stderr')).write_text(r.stderr)
    (p/(name+'.json')).write_text(json.dumps({'argv':[str(x) for x in args],'exit':r.returncode},indent=2)+'\n')
    print(json.dumps({'operation':name,'exit':r.returncode}),flush=True)
    if r.returncode:raise SystemExit(r.returncode)

for archive,dest in [('stdo-manager-runtime-v3.1.0-rc.2-macos-arm64-cp313.zip','runtime'),('stdo-products-v3.1.0-rc.2.zip','products')]:
    root=p/dest;root.mkdir(exist_ok=False)
    with zipfile.ZipFile(assets/archive) as bundle:
        for name in bundle.namelist():
            relative=Path(name)
            assert not relative.is_absolute() and '..' not in relative.parts
        bundle.extractall(root)
products=json.loads((p/'products/PRODUCTS.json').read_text())
for name,product in products['products'].items():
    root=p/'products'/name
    assert {f.relative_to(root).as_posix() for f in root.rglob('*') if f.is_file()}=={r['path'] for r in product['members']}
    for row in product['members']:
        data=(root/row['path']).read_bytes()
        assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
run('venv',['/opt/homebrew/bin/python3.13','-m','venv',p/'manager'])
python=p/'manager/bin/python';stdo=p/'manager/bin/stdo'
run('offline-install',[python,'-m','pip','install','--no-index','--find-links',p/'runtime/wheels','--require-hashes','--no-deps','-r',p/'runtime/requirements-macos-arm64-cp313.txt'])
run('pip-check',[python,'-m','pip','check'])
run('manager-version',[stdo,'--version'])
pin=hashlib.sha256((assets/'stdo-v3.1.0-rc.2-manifest.json').read_bytes()).hexdigest()
assert pin=='b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4'
run('native-install',[stdo,'--store',p/'store','install','v3.1.0-rc.2','--repository','https://github.com/foolishimp/specification_methodology.git','--manifest-sha256',pin])
run('native-verify',[stdo,'--store',p/'store','verify','v3.1.0-rc.2','--manifest-sha256',pin])
assert (p/'store/releases/v3.1.0-rc.2/manifest.json').read_bytes()==(assets/'stdo-v3.1.0-rc.2-manifest.json').read_bytes()
run('context-hosts',[python,'-B',w/'context/run_distribution_checks.py','--products-root',p/'products','--native-root',p/'store/releases/v3.1.0-rc.2','--stdo',stdo,'--store',p/'store','--fixture-root',w/'context/final-use-01/fixture','--queries-root',w/'context/final-use-01/queries','--out',p/'host-checks','--assessment-python',w/'assessment/semantic-01/assessments/python.json','--assessment-sdlc',w/'assessment/semantic-01/assessments/sdlc.json','--assessment-boundaries',w/'assessment/semantic-01/assessments','--remove'])
run('visual-browser',['node',w/'visual/check_browser.cjs',p/'products/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.2/run/generation/proposal/explorer.html','../public-readback/visual-browser'])
readback=json.loads((p/'ASSET_READBACK.json').read_text());hosts=json.loads((p/'host-checks/RESULT.json').read_text())
for host in hosts['hosts'].values():
    assert all(context['covered'] for context in host['contexts'])
    acceptance=next(case for case in host['boundary_controls'] if case['case']=='acceptance')
    assert acceptance['covered'] and acceptance['W35']=='true' and acceptance['W26']=='false'
result={'kind':'stdo.public-installed-readback/1','release_id':readback['release_id'],'url':readback['url'],'native_manifest_sha256':pin,'assets':len(readback['assets']),'product_members':sum(len(x['members']) for x in products['products'].values()),'manager_version':(p/'manager-version.stdout').read_text().strip(),'hosts':{name:[{'purpose':x['purpose'],'covered':x['covered'],'context_sha256':x['context_sha256']} for x in value['contexts']] for name,value in hosts['hosts'].items()},'boundary_controls':{name:value['boundary_controls'] for name,value in hosts['hosts'].items()},'visual_browser_result':str(p/'visual-browser/RESULT.json'),'valid':True}
(p/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
