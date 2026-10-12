import assert from 'node:assert/strict';
import {readFile,writeFile,copyFile,mkdir,readdir,lstat} from 'node:fs/promises';
import {join,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';
const evidence=dirname(fileURLToPath(import.meta.url)),root='/Users/jim/src/apps/specification_methodology/specification_methodology';
const sha=b=>createHash('sha256').update(b).digest('hex');
const pre=JSON.parse(await readFile(join(evidence,'preimages.json'))),canonical=[];
const head=spawnSync('git',['rev-parse','HEAD'],{cwd:root,encoding:'utf8'});assert.equal(head.status,0);assert.equal(head.stdout.trim(),'3251990630aced3be29c128e8d0fe17bb6df0b92');
for(const row of pre.protectedRows)assert.equal(sha(await readFile(join(root,row.path))),row.sha256,row.path);
assert.equal(sha(await readFile(join(root,pre.proposal))),pre.proposalSha256,'original proposal unchanged');
let patch='';
for(const path of [...pre.canonical.map(row=>row.path),pre.newPath]){
  const bytes=await readFile(join(root,path)),old=pre.canonical.find(row=>row.path===path);
  if(old){const recorded=await readFile(join(evidence,'preimages',path));assert.equal(sha(recorded),old.sha256);const historical=spawnSync('git',['show','HEAD:specification_methodology/'+path],{cwd:root});assert.equal(historical.status,0);assert.deepEqual(historical.stdout,recorded,'preimage equals exact base '+path)}
  await mkdir(dirname(join(evidence,'candidate',path)),{recursive:true});await copyFile(join(root,path),join(evidence,'candidate',path));
  canonical.push({path,preimageSha256:old?.sha256??null,sha256:sha(bytes),bytes:bytes.length});
  const delta=spawnSync('diff',['-u','--label',old?'a/'+path:'/dev/null','--label','b/'+path,old?join(evidence,'preimages',path):'/dev/null',join(root,path)],{encoding:'utf8'});assert.equal(delta.status,1,path);patch+=delta.stdout;
}
const baselinePath='specification/standards/STDO_REFERENCE_FRAME_BASELINE.md',current=await readFile(join(root,baselinePath),'utf8'),before=await readFile(join(evidence,'preimages',baselinePath),'utf8');
const start=current.indexOf('## Derived End-To-End Interface Integration Frame\n'),end=current.indexOf('## Complete Engagement Transition\n',start);
assert.ok(start>=0&&end>start);assert.equal(current.slice(0,start)+current.slice(end),before,'all preexisting baseline bytes conserved');
const newSection=current.slice(start,end);assert.equal(newSection.split('\n').length-1,141);
const projectionResults=[];
for(const name of ['stdo_compressed.md','stdo_bootstrap.md']){
  const path='specification/standards/authority_compressions/'+name,old=await readFile(join(evidence,'preimages',path),'utf8'),now=await readFile(join(root,path),'utf8');
  let restored=now.replace(/^  STDO_REFERENCE_FRAME_BASELINE\.md: [0-9a-f]{64}$/m,'  STDO_REFERENCE_FRAME_BASELINE.md: '+pre.canonical.find(row=>row.path===baselinePath).sha256).replace('generated_at: 2026-09-16','generated_at: 2026-09-15');
  if(name==='stdo_compressed.md')restored=restored.replace(/^- For material cross-interface outcomes,[\s\S]*?(?=^- Every coded module)/m,'');
  else restored=restored.replace(/^   When the selected evaluation needs the cross-interface refinement, acquire\n[\s\S]*?(?=^8\. Reuse)/m,'');
  assert.equal(restored,old,'projection delta only '+name);projectionResults.push({path,onlyAffectedDigestDateAndRoute:true});
}
await writeFile(join(evidence,'candidate.patch'),patch);
const commands=JSON.parse(await readFile(join(evidence,'proof-final/commands.json')));assert.ok(commands.every(row=>row.code===0&&row.signal===null));
const processStates=commands.map(row=>{let active=false;try{process.kill(row.pid,0);active=true}catch(error){if(error.code!=='ESRCH')throw error}return{pid:row.pid,name:row.name,active,recordedExit:row.code}});assert.ok(processStates.every(row=>!row.active));
const installed='/Users/jim/Library/Application Support/STDO/releases/v2.5.0-rc.4/standards';
const acquired=[];for(const [path,expected]of [['STDO_REFERENCE_FRAME_BASELINE.md','6013e42693066127d729580ac3d01d31c2a82f00adea9d0fb1af3494b4ad9c3e'],['REFERENCE_FRAME_METHOD.md','c7f7abfa620d73e209463605517075ac375d8e79e0273d3f435c4e36155de5d8']]){const digest=sha(await readFile(join(installed,path)));assert.equal(digest,expected);acquired.push({path,sha256:digest})}
await writeFile(join(evidence,'conservation.json'),JSON.stringify({checkedAt:new Date().toISOString(),head:head.stdout.trim(),canonical,allPreexistingBaselineBytesConserved:true,newSectionLines:141,projectionResults,protectedRows:pre.protectedRows,proposalUnchanged:true,installedAuthorityMembers:acquired,processStates,trackedRootWorkExcluded:['specification/GOALS.md','.ai-workspace/tickets/','.ai-workspace/comments/codex/20260916T124600Z_INTERFACE_INTEGRATION/activation.md'],noReleaseOrAdoption:true},null,2)+'\n');
async function inventory(prefix=''){
  const rows=[];for(const name of (await readdir(join(evidence,prefix))).sort()){
    if(prefix===''&&['freeze.json','manifest.json'].includes(name))continue;
    const path=join(prefix,name),info=await lstat(join(evidence,path));
    if(info.isDirectory())rows.push(...await inventory(path));else if(info.isFile()){const bytes=await readFile(join(evidence,path));rows.push({path,bytes:bytes.length,sha256:sha(bytes)})}else throw Error('unexpected entry '+path);
  }return rows;
}
const rows=await inventory(),manifest=JSON.stringify(rows,null,2)+'\n';await writeFile(join(evidence,'manifest.json'),manifest);
const frozenAt=new Date().toISOString(),freeze={kind:'source_frame_candidate_freeze',activation:'STDO_E2E_INTERFACE_FRAME_SOURCE_01',workerResult:'candidate_ready',frameResult:'satisfied',resultScope:'authorized source construction and bounded self-check only',frozenAt,baseHead:head.stdout.trim(),operativeBasis:'stdo://releases/v2.5.0-rc.4/',operativeManifestSha256:'4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e',proposalSha256:pre.proposalSha256,canonical,manifestSha256:sha(manifest),manifestRows:rows.length,mechanicalTestsPassed:30,diffCheckPassed:true,semanticIndependentReview:false,liveLLMUAT:false,released:false,consumerAdoption:false,representationUpdated:false,deadline:'2026-09-16T13:15:00Z',elapsedFromWindowStartSeconds:(Date.now()-Date.parse('2026-09-16T12:46:18Z'))/1000};
const bytes=JSON.stringify(freeze,null,2)+'\n';await writeFile(join(evidence,'freeze.json'),bytes);console.log(JSON.stringify({frozenAt,freezeSha256:sha(bytes),manifestSha256:freeze.manifestSha256,canonical},null,2));
