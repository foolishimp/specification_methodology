"""Read the finite omitted identity facts without changing the candidate."""
from pathlib import Path
import datetime
import difflib
import hashlib
import io
import json
import subprocess
import zipfile

BASE=Path(__file__).resolve().parent
WORK=BASE.parent
ROOT=WORK.parents[2]
B='4a7f7cdfcd724d6b2e47b3d790fa88030b70d84a'
OLD='f68e8f47db69425205db313ba72fbc9cad94c2b9'
CHECKPOINT='31e6f40ed81d6c5163c856c16815d89d5a3f5728'
NATIVE='21a9d4b93c5adef1e84a369360a99176b98793c5'


def sha(x):return hashlib.sha256(x).hexdigest()
def load(p):return json.loads(p.read_bytes())
def git(*args):return subprocess.check_output(['git','-C',str(ROOT),*args],stderr=subprocess.PIPE)
def show(commit,path):return git('show',commit+':'+path)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()


out=BASE/'identity-01/MECHANICAL_GAP_READBACK.json'
assert not out.exists()
r={'kind':'stdo.rc2.identity-finite-gap-readback/1','performed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'subject':{'native':NATIVE,'source_B':B,'predecessor_source':OLD},
   'standing':'Codex assessment operator mechanical evidence; no new independent semantic verdict, acceptance or publication authority. Original Claude report and limits remain unchanged.'}
subprocess.run(['git','-C',str(ROOT),'merge-base','--is-ancestor',CHECKPOINT,B],check=True)
source_path='specification_methodology/v3/build_tenants/common'
tree=git('rev-parse',B+':'+source_path).decode().strip()
assert tree==git('rev-parse',CHECKPOINT+':'+source_path).decode().strip()
assert tree==git('rev-parse',NATIVE+':specification_methodology/v3').decode().strip()
r['G1']={'checkpoint':CHECKPOINT,'checkpoint_is_ancestor_of_B':True,'source_path':source_path,'B_source_tree':tree,
         'checkpoint_source_tree':tree,'native_A_product_tree':tree,'source_freeze_byte_identity_preserved':True}

catpath='purpose_context/skills/stdo-context/indexes/CATALOG.json'
source=json.loads(show(B,catpath));package=load(WORK/'packaged-products'/catpath)
prior=load(WORK/'context/final-packages-01'/catpath)
entries=[]
for entry in package['entries']:
    a=next(x for x in source['entries'] if x['id']==entry['id'])
    old=next(x for x in prior['entries'] if x['id']==entry['id'])
    assert entry==a
    assert old['family_guard']==entry['family_guard']
    changes=sorted(k for k in set(old)|set(entry) if old.get(k)!=entry.get(k))
    assert set(changes)<= {'artifacts','view_sha256'}
    entries.append({'id':entry['id'],'source_B_entry_equal_portable':True,
                    'prior_semantic_package_family_guard_equal':True,'family_guard':entry['family_guard'],
                    'prior_to_final_entry_changed_fields':changes})
unknown=[]
freeze=load(WORK/'context/SEMANTIC_FREEZE.json')
for x in freeze['contexts']:
    if x['context'] is not None:continue
    oldpath=Path(x['selection']);old=load(oldpath)
    for host in ['codex','claude']:
        newpath=WORK/'assessed-packaged/operations'/(host+'-'+x['case']+'-boundary-refused.stdout')
        new=load(newpath)
        changes=sorted(k for k in set(old)|set(new) if old.get(k)!=new.get(k))
        assert set(changes)=={'catalog_sha256','index_path','public_manifest_sha256'}
        assert new['status']=='incomplete' and new['covered'] is False and new['selected'] is None
        unknown.append({'case':x['case'],'host':host,'before_sha256':sha(oldpath.read_bytes()),
                        'after_sha256':sha(newpath.read_bytes()),'changed_fields':changes,
                        'same_guard_predicates_decision_query_index_and_sources':True,'delivered_body':False})
r['G2']={'catalog_source_sha256':sha(show(B,catpath)),'catalog_portable_sha256':sha((WORK/'packaged-products'/catpath).read_bytes()),
         'entries':entries,'unknown_refusals':unknown,'standing':'Only projection/provenance pins and physical index location change; unknown family decisions and supplied facts are equal.'}

rows=[];patches=[]
for x in freeze['contexts']:
    if x['context'] is None:continue
    oldpath=Path(x['markdown']);old=oldpath.read_text()
    expected=old.replace('Source-semantic coverage: unassessed\n','Source-semantic coverage: supported\n',1).replace('Use: experimental-candidate\n','Use: assessed-context\n',1)
    suffix=x['case']+('-delivery' if x['case'] in ['python','sdlc'] else '-boundary')
    for host in ['codex','claude']:
        newpath=WORK/'assessed-packaged'/(host+'-'+suffix)/'CONTEXT.md';new=newpath.read_text()
        assert new==expected
        rows.append({'case':x['case'],'host':host,'before_sha256':sha(oldpath.read_bytes()),'after_sha256':sha(newpath.read_bytes()),
                     'exactly_two_header_annotations_changed':True,'rule_and_source_text_equal':True})
        patches.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(oldpath),tofile=str(newpath)))
(BASE/'identity-01/MARKDOWN_ANNOTATION_DELTA.patch').write_text(''.join(patches))
r['RM1']={'contexts':rows,'only_replacements':{'Source-semantic coverage: unassessed':'Source-semantic coverage: supported','Use: experimental-candidate':'Use: assessed-context'},'all_other_bytes_equal':True}

manager=load(WORK/'manager-checks/RESULT.json');members=[]
with zipfile.ZipFile(WORK/'assets/stdo_toolchain-3.1.0rc2-py3-none-any.whl') as current:
    for x in manager['members']:
        name='specification_methodology/v2/src/'+x['path']
        old=show(OLD,name);new=show(B,name);wheel=current.read(x['path'])
        assert new==wheel and sha(new)==x['sha256']
        if x['path']=='stdo_toolchain/__init__.py':
            assert old.replace(b'__version__ = "3.1.0rc1"',b'__version__ = "3.1.0rc2"')==new
        else:assert old==new
        members.append({'path':name,'RC1_sha256':sha(old),'RC2_sha256':sha(new),'RC2_source_and_wheel_equal':True,
                        'RC1_to_RC2_change':'__version__ value only' if old!=new else 'none'})
oldzip=Path('/Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/public-readback/assets/stdo-manager-runtime-v3.1.0-rc.1-macos-arm64-cp313.zip')
newzip=WORK/'assets/stdo-manager-runtime-v3.1.0-rc.2-macos-arm64-cp313.zip'
with zipfile.ZipFile(oldzip) as a,zipfile.ZipFile(newzip) as b:
    oldw={Path(n).name:a.read(n) for n in a.namelist() if n.endswith('.whl') and not Path(n).name.startswith('stdo_toolchain-')}
    neww={Path(n).name:b.read(n) for n in b.namelist() if n.endswith('.whl') and not Path(n).name.startswith('stdo_toolchain-')}
    assert oldw==neww and len(oldw)==20
    oldmanager=next(a.read(n) for n in a.namelist() if Path(n).name.startswith('stdo_toolchain-') and n.endswith('.whl'))
    newmanager=next(b.read(n) for n in b.namelist() if Path(n).name.startswith('stdo_toolchain-') and n.endswith('.whl'))
    with zipfile.ZipFile(io.BytesIO(oldmanager)) as wa,zipfile.ZipFile(io.BytesIO(newmanager)) as wb:
        old_code={n:wa.read(n) for n in wa.namelist() if n.startswith('stdo_toolchain/')}
        new_code={n:wb.read(n) for n in wb.namelist() if n.startswith('stdo_toolchain/')}
        assert old_code.keys()==new_code.keys() and len(old_code)==13
        for name,data in old_code.items():
            expected=data.replace(b'__version__ = "3.1.0rc1"',b'__version__ = "3.1.0rc2"') if name=='stdo_toolchain/__init__.py' else data
            assert expected==new_code[name]
        old_meta=next(wa.read(n) for n in wa.namelist() if n.endswith('/METADATA'))
        new_meta=next(wb.read(n) for n in wb.namelist() if n.endswith('/METADATA'))
        assert old_meta.replace(b'Version: 3.1.0rc1\n',b'Version: 3.1.0rc2\n')==new_meta
        for suffix in ['/entry_points.txt','/WHEEL','/top_level.txt']:
            assert next(wa.read(n) for n in wa.namelist() if n.endswith(suffix))==next(wb.read(n) for n in wb.namelist() if n.endswith(suffix))
r['G3']={'manager_source_and_wheel_members':members,'retained_public_RC1_runtime':str(oldzip),'RC1_runtime_sha256':sha(oldzip.read_bytes()),
         'RC2_runtime_sha256':sha(newzip.read_bytes()),'third_party_wheels':[{ 'name':n,'sha256':sha(v)} for n,v in sorted(oldw.items())],
         'twenty_third_party_wheel_bytes_equal':True,'twelve_manager_runtime_members_equal':True,
         'remaining_init_member_only_version_value_changes':True,
         'entry_points_wheel_and_top_level_metadata_equal':True,'METADATA_only_version_changes':True,
         'limit':'Runtime/input byte conservation plus the retained finite fresh RC2 install checks; not an exhaustive behavioral theorem.'}

package_source=show(B,'stdo_skills/scripts/package.py')
assert package_source==(ROOT/'stdo_skills/scripts/package.py').read_bytes()
(BASE/'identity-01/SKILLS_PACKAGE_SOURCE.py').write_bytes(package_source)
paths=git('ls-tree','-r','--name-only',B,'--','stdo_skills').decode().splitlines()
explicit=['README.md','GETTING_STARTED.md','RELEASE.md','AGENTS.md','CLAUDE.md','stdo_skills.json','build_tenants/README.md','build_tenants/codex/README.md','build_tenants/claude/README.md']
bases=['scripts/','specification/','skills/','build_tenants/codex/current/','build_tenants/claude/current/']
selected={p.removeprefix('stdo_skills/') for p in paths if p.removeprefix('stdo_skills/') in explicit or any(p.removeprefix('stdo_skills/').startswith(base) for base in bases)}
inventory=load(WORK/'packaged-products/stdo_skills/INVENTORY.json')
assert selected=={x['path'] for x in inventory['files']}
frozen=load(WORK/'context/FINAL_FREEZE.json')
allskills={x['path'].removeprefix('stdo_skills/') for x in frozen['source_files'] if x['path'].startswith('stdo_skills/')}
omitted=sorted(allskills-selected)
assert omitted==['release/3.0.5-rc.1/README.md','release/3.0.5-rc.1/manifest.json','release/3.0.5/README.md','release/3.0.5/manifest.json']
r['F2']={'package_script_commit':B,'package_script_path':'stdo_skills/scripts/package.py','package_script_sha256':sha(package_source),
         'selected_member_count':len(selected),'generated_inventory_adds_one':True,'selected_members_exactly_match_portable_inventory':True,
         'excluded_from_source_freeze':omitted,'reason':'The committed positive-selection recipe includes named root/current files and scripts/specification/skills/current host subtrees. It does not select release/ history. The four historical artifacts remain in B and have never been declared portable current members.'}
runtime=[]
scopes=['purpose_context/skills/stdo-context/scripts','stdo_skills/skills/stdo-context/scripts','stdo_skills/scripts/manage_skills.py']
for scope in scopes:
    oldpaths=git('ls-tree','-r','--name-only',OLD,'--',scope).decode().splitlines()
    newpaths=git('ls-tree','-r','--name-only',B,'--',scope).decode().splitlines()
    assert oldpaths==newpaths
    for name in newpaths:
        a=show(OLD,name);b=show(B,name);assert a==b
        runtime.append({'path':name,'sha256':sha(b),'RC1_to_RC2_bytes_equal':True})
r['context_runtime_conservation']=runtime
r['retained_attempt']={'script':'assessment/identity-facts-01.py','stderr':'assessment/identity-facts-01.stderr',
    'reason':'The first operator checker incorrectly required the version-bearing __init__.py bytes to be identical. The actual source and wheel change only the declared __version__ value. The checker now verifies that exact single substitution and keeps all executable-mechanics members byte-equal; no Product bytes changed.'}
r['report_count_clarification']={'PC_total':51,'byte_equal_source_members':48,'filtered_catalog':1,'generated_replaced_identity_members':2,
    'note':'The actual actor report says 49 equal plus two, but also identifies the filtered catalog. The original report remains unedited; the exact mechanical partition is 48 + 1 + 2 = 51.'}
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'path':str(out),'sha256':sha(out.read_bytes()),'G1':True,'G2':len(unknown),'RM1':len(rows),'G3_manager_modules':len(members),'G3_third_party':len(oldw),'F2_selected':len(selected),'runtime_members':len(runtime)}))
