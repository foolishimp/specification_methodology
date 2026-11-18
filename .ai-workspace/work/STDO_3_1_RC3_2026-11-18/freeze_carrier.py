from pathlib import Path
import json,hashlib,subprocess
w=Path(__file__).resolve().parent;r=w.parents[2]
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(r),*args])
f=read(w/'context/FINAL_RESULT.json');assert f['status']=='passed-for-eight-declared-exact-queries';assert f['assessed_packaged_operations']==100
assert read(w/'ref-tests-02/RESULT.json')['passed'];assert read(w/'manager-checks/RESULT.json')['status']=='passed'
text='''# RC3 prepublication scope

The owner approved release 3.1.0-rc.3. This records finite prepublication
qualification of the actual native A and companion packages. Ref-object
qualification, atomic publication and public installation are separate later
gates; none is claimed by this file.

The method is self-contained across core and profiles. Required tracking,
needed facts and reconciliation to authoritative workspace truth remain;
the generic register is an optional example and equivalent mechanisms are
permitted. Runtime ledger/replay/API design is not imposed. Product specifies
the intended end state; Goals carry current epics. Native authority audit
and F_P judgment guards and purpose-specific UX replay remain.

| Obligation | Observed evidence and limit |
|---|---|
| R31-01 source custody/conservation | Approved source snapshot and explicit 36 native and 12 companion dispositions; isolated published RC2 base; original main remains outside effects. |
| R31-02 method delivery | Native inventory 95 files, 24 standards, 13 regenerated frames; 52 frame tests, package/link closure; no downstream names in native standards/plugin. |
| R31-03 actual cut/dependencies | NATIVE_BINDING and FINAL_NATIVE_IDENTITY bind actual annotated A/private install; both indexes and bounded visual bind its actual manifest. This commit freezes the source companion carrier B. |
| R31-04 distribution identity | Five constructed assets and exact 226-member companion archive; final external cohort asset binds B and qualified refs after this freeze. |
| R31-05 independent/use checks | Native-02 closes native findings; semantic-03 closes the exact eight query subjects and reuses unchanged bounded visual support explicitly. 100 operations consume actual extracted final packages on Codex/Claude paths with supported exact assessments and removal. No automatic host pickup claim. |
| R31-06 ref transaction | Eight real disposable Git-remote controls passed. Actual annotated objects, subtree identities, leases and full 25-ref graph must pass the separate frozen identity gate before atomic publication. |
| R31-07 public readback | Required after publication; unperformed at this prepublication freeze. |

The Context engine's 28 preserved controls and seven successor-boundary controls
passed; the source amendment's actual positive control and three refusals passed.
Final regeneration is current. Unknown boundary/family, wrong purpose/pin, old
assessment, changed owned member, collision and byte-budget cases refuse their
dependent operations. Every final supported context corresponds to an actual
external assessment of its exact index/corpus/query; no support is synthesized.

The manager was installed offline from 21 locked wheels on macOS arm64 CPython
3.13; its 20 third-party wheels and runtime implementation are conserved apart
from owned version metadata. Native manifest verification passed. No other
platform is qualified here. Visual scope is source section navigation and 24
selected annotations with explicit residuals: nine artifact checks and twelve
offline browser checks passed; semantic-01 support applies to unchanged final
artifact bytes and is reused explicitly by later bounded reviews.

Original failures remain: native-01 F1-F4; the initial O04 source coverage mapping
refusal; semantic-01 A1-A3; triage with repair_planned=false failing to exercise
W11; semantic-02 F1 missing no-drift proof. Their repairs and successful bounded
rechecks are retained. No failed report was rewritten into a pass.

Independent judgments are actual Claude CLI read-only returns, independent of
Codex construction but not earlier Claude-family architectural direction. Their
source/applicability reading and mechanical binding limits remain explicit.
Whole-method qualification, arbitrary-query coverage, automatic host discovery,
wider effectiveness, human exact-cut acceptance and consumer adoption are not
claimed. Construction remains on installed STDO 3.0.4. Global installs and
historical immutable tags/assets remain outside effects.
'''
(w/'PREPUBLICATION.md').write_text(text)
# Preserve exact semantic input and extracted package identities at the last pre-carrier gate.
freeze=read(w/'assessment/semantic-03/FREEZE.json')
for row in freeze['files']:assert sha(Path(row['path']))==row['sha256'],row['path']
freeze['files'] += [{'path':str(w/p),'sha256':sha(w/p)} for p in ['context/FINAL_RESULT.json','assessed-packaged/RESULT.json','PRODUCT_EXTRACTION_03.json','assessment/semantic-03/ASSESSMENT.md','assessment/semantic-03/TRANSCRIPTION.json']]
(w/'context/FINAL_FREEZE.json').write_text(json.dumps(freeze,indent=2)+'\n')
# Stage only the release worktree's selected source and durable evidence. Exclude
# installers, virtual environments, release asset binaries and redundant extracted copies.
paths=[Path(x.decode()) for x in git('ls-files','-m','-o','--exclude-standard','-z').split(b'\0') if x]
selected=[];excluded=[]
for p in paths:
 if w.relative_to(r) in p.parents:
  rel=p.relative_to(w.relative_to(r));parts=rel.parts
  omit=parts[0] in ['manager','manager-source','native-store','assets','assets-02','assets-03','attempts','packaged-products','packaged-products-02','packaged-products-03'] or '__pycache__' in parts or '.git' in parts or p.suffix=='.pyc'
  if omit:excluded.append(str(p));continue
 selected.append(str(p))
assert not any('STDO_3_1_RC2_2026-11-15' in p for p in selected)
for start in range(0,len(selected),180):subprocess.run(['git','-C',str(r),'add','--',*selected[start:start+180]],check=True)
# Retained exact package/context snapshots can carry inherited whitespace; do not
# rewrite their bytes to cosmetically alter evidence.
check=subprocess.run(['git','-C',str(r),'diff','--cached','--check'],capture_output=True);(w/'STAGING_WHITESPACE.stdout').write_bytes(check.stdout)
stat={'kind':'stdo.release-carrier-staging/1','selected_paths':len(selected),'excluded_local_artifacts':len(excluded),'staged_names_sha256':hashlib.sha256(git('diff','--cached','--name-only','-z')).hexdigest(),'whitespace_check_exit':check.returncode,'evidence_whitespace_policy':'Preserve original evidence and exact snapshots; active authored source checked separately.'};(w/'STAGING_CHECK.json').write_text(json.dumps(stat,indent=2)+'\n');subprocess.run(['git','-C',str(r),'add','--',str((w/'STAGING_CHECK.json').relative_to(r)),str((w/'STAGING_WHITESPACE.stdout').relative_to(r))],check=True)
p=subprocess.run(['git','-C',str(r),'commit','-m','Freeze STDO 3.1 RC3 companion packages and qualification evidence'],capture_output=True);(w/'SOURCE_COMMIT.stdout').write_bytes(p.stdout);(w/'SOURCE_COMMIT.stderr').write_bytes(p.stderr);p.check_returncode();carrier=git('rev-parse','HEAD').decode().strip();b=read(w/'NATIVE_BINDING.json');record={'carrier':carrier,'native':b['native']['native_commit'],'base':'2c95df2fe4656f1bbe6c4eb2d9f4be6e28446e0d','standing':'Frozen companion source; not published.'};(w/'SOURCE_CARRIER.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
