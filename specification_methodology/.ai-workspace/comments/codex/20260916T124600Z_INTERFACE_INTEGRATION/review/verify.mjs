import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
const review=path.dirname(fileURLToPath(import.meta.url)), task=path.dirname(review);
const source='/Users/jim/src/apps/specification_methodology/specification_methodology';
const abi='/Users/jim/src/apps/abiogenesis', worker=path.join(task,'source-worker');
const local=path.join(abi,'.ai-workspace/comments/codex/20260916_ABG5_INTERFACE_INTEGRATION_FRAME/worker');
const sha=b=>crypto.createHash('sha256').update(b).digest('hex'),hash=p=>sha(fs.readFileSync(p)),json=p=>JSON.parse(fs.readFileSync(p)),text=p=>fs.readFileSync(p,'utf8');
const bindings=[];
function bind(p,expected){const actual=hash(p);if(expected)assert.equal(actual,expected,p);const s=fs.statSync(p);bindings.push({path:p,sha256:actual,bytes:s.size,device:s.dev,inode:s.ino});return actual;}
bind(path.join(worker,'freeze.json'),'5a86eca7e202af8c99310555f99c645c13c6327e5eba6668df67a0c964428625');
bind(path.join(worker,'manifest.json'),'a1cd65d95afedce1857ecc43ced0e91b4e4780116680b607ae21e12c35947e0f');
bind(path.join(local,'freeze.json'),'79ea5c50a208830d4ea1b30dc2314372403e21f438382b5aaa03e013564a0f41');
bind(path.join(local,'manifest.json'),'d0b3f73d1e068c685a865a690815a8c51ed121a7e50a84822f46962de30a387c');
bind(path.join(local,'worker-return.md'),'818391d7dfb75a578095d9587de8dd6b058f581e60ba2780fb93cc6f4410c64b');
const sourceManifest=json(path.join(worker,'manifest.json')),localManifest=json(path.join(local,'manifest.json'));
for(const [root,rows] of [[worker,sourceManifest],[local,localManifest.rows]])for(const row of rows){bind(path.join(root,row.path),row.sha256);assert.equal(fs.statSync(path.join(root,row.path)).size,row.bytes);}
const freeze=json(path.join(worker,'freeze.json'));
for(const row of freeze.canonical){bind(path.join(worker,'candidate',row.path),row.sha256);bind(path.join(source,row.path),row.sha256);if(row.preimageSha256)bind(path.join(worker,'preimages',row.path),row.preimageSha256);}
const target=localManifest.canonical[0];
bind(path.join(local,'subject/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md'),target.sha256);bind(path.join(abi,target.path),target.sha256);bind(path.join(local,'preimage/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md'),target.preimageSha256);
const profilePath='specification/standards/STDO_REFERENCE_FRAME_BASELINE.md';
const before=text(path.join(worker,'preimages',profilePath)),after=text(path.join(worker,'candidate',profilePath));
let prefix=0,suffix=0;while(before[prefix]===after[prefix]&&prefix<before.length)prefix++;
while(before[before.length-1-suffix]===after[after.length-1-suffix]&&suffix<before.length-prefix)suffix++;
assert.equal(before.slice(prefix,before.length-suffix),'');
const added=after.slice(prefix,after.length-suffix);
// Longest common prefix can include the common Markdown heading marker.
assert.ok(added.includes('Derived End-To-End Interface Integration Frame'));
assert.equal(added.split('\n').length-1,141);
const frame=after.split('## Derived End-To-End Interface Integration Frame')[1].split('\n## ')[0];
for(const forbidden of ['ABIogenesis','ABG','HoG','GTL','predecessorStatementRefs'])assert.ok(!frame.includes(forbidden));
for(const row of json(path.join(worker,'conservation.json')).protectedRows)bind(path.join(source,row.path),row.sha256);
const localBefore=text(path.join(local,'preimage/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md')),localAfter=text(path.join(local,'subject/ABI5_PROJECT_REFERENCE_FRAME_BASIS.md'));
const localAdded=localAfter.slice(localAfter.indexOf('## Local Extension: End-To-End Interface Integration'),localAfter.indexOf('## Activation And Return'));
const coverage='| selected entry-to-outcome interface/context seam and its four distinct claims | [`F-END-TO-END-INTERFACE-INTEGRATION`](#f-end-to-end-interface-integration), with applicable existing specialist/testing results |\n';
assert.equal(localAfter.replace(localAdded,'').replace(coverage,''),localBefore);
assert.ok(!localAdded.includes('stdo://releases/v2.5.0-rc.4/'));
assert.ok(localAdded.includes('not adoption of mutable methodology source'));
const sourceDefinition=json(path.join(source,'stdo_default.json')),abiDefinition=json(path.join(abi,'stdo_abiogenesis.json'));
assert.equal(sourceDefinition.constitution.stdo.basis.uri,'stdo://releases/v2.5.0-rc.4/');
assert.equal(abiDefinition.constitution.stdo.basis.uri,'stdo://releases/v2.5.0-rc.7/');
bind(path.join(abi,'stdo_abiogenesis.json'));
const basis=json(path.join(local,'basis.json'));
bind(path.join(abi,basis.definition.path),basis.definition.sha256);
let installedMembers=0;
for(const control of basis.controls.filter(c=>c.root.includes('/Library/Application Support/'))){for(const row of control.rows){if(row.symlink)assert.equal(fs.readlinkSync(path.join(control.root,row.path)),row.symlink);else bind(path.join(control.root,row.path),row.sha256);installedMembers++;}}
const rep='/Users/jim/Library/Application Support/STDO Representation/releases/v2.5.0-rc.7';
const programPath=path.join(rep,'build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7/axiomatic-program.json');
const mapPath=path.join(rep,'build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.7/logical-constraint-map.json');
bind(programPath,basis.representation.programBytesSha256);bind(mapPath,basis.representation.mapBytesSha256);
const map=json(mapPath);assert.equal(map.program_uri,basis.representation.programUri);assert.equal(map.program_sha256,basis.representation.canonicalProgramSha256);
const reviewerUri='stdo://releases/v2.5.0-rc.7/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame';
assert.ok(JSON.stringify(map.frame_refs).includes(reviewerUri));
assert.ok(!JSON.stringify(map.frame_refs).includes('end-to-end-interface-integration'));
const caseEvidence=json(path.join(local,'case-evidence.json'));
for(const row of caseEvidence.paths)bind(row.path,row.sha256);
assert.deepEqual(caseEvidence.inputAssets,[]);
assert.equal(caseEvidence.candidateLinks.reduce((n,s)=>n+s.predecessorStatementRefs.length,0),7);
assert.deepEqual(caseEvidence.timeline.map(r=>r.ordinal),[196,198,200,202,204]);
const priorReview=path.join(abi,'.ai-workspace/comments/codex/20260916_ABG5_RC7_PREDECESSOR_CONTEXT/review/freeze.json');
bind(priorReview,'19cc41e00e9de869b780c08fb3152e9dec37dd721feb25b8de3a568a41dc062f');
const commands=[];
function run(command,args){const start=new Date().toISOString(),result=spawnSync(command,args,{cwd:source,encoding:'utf8',env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}});commands.push({command,args,startedAt:start,endedAt:new Date().toISOString(),status:result.status,stdout:result.stdout,stderr:result.stderr});assert.equal(result.status,0,result.stderr||result.stdout);return JSON.parse(result.stdout);}
const rc4=run('stdo',['verify','v2.5.0-rc.4','--manifest-sha256',sourceDefinition.constitution.stdo.basis.manifest_sha256]);assert.equal(rc4.valid,true);
const rc7=run('stdo',['verify','v2.5.0-rc.7','--manifest-sha256',abiDefinition.constitution.stdo.basis.manifest_sha256]);assert.equal(rc7.valid,true);
bind(path.join(source,'tests/test_compressions.py'));
const tests=run('python3',['-B',path.join(review,'run-source-tests.py')]);
assert.equal(tests.testsRun,30);assert.equal(tests.successful,true);
for(const row of bindings){assert.equal(hash(row.path),row.sha256,row.path);const s=fs.statSync(row.path);assert.equal(s.dev,row.device);assert.equal(s.ino,row.inode);}
fs.writeFileSync(path.join(review,'commands.json'),JSON.stringify(commands,null,2)+'\n',{flag:'wx'});
const result={checkedAt:new Date().toISOString(),sourceManifestMembers:sourceManifest.length,abiManifestMembers:localManifest.rows.length,sourceCanonicalPaths:freeze.canonical.length,abiCanonicalPaths:localManifest.canonical.length,baselineInsertionOnly:true,baselineInsertedLines:141,abiInsertionsOnly:true,genericDomainSpecificLeak:false,installedCohortMembersRebound:installedMembers,sourceOperativeBasis:rc4.uri,sourceBasisValid:rc4.valid,abiOperativeBasis:rc7.uri,abiBasisValid:rc7.valid,selectedReviewerFrame:reviewerUri,newFrameNotClaimedByReleasedMap:true,retainedCasePaths:caseEvidence.paths.length,retainedCandidateSameResponseLinks:7,mechanicalTests:tests.testsRun,mechanicalTestsPassed:tests.successful,mechanicalSourceChecksAreNotSemanticOrNativeProof:true,bindings};
fs.writeFileSync(path.join(review,'checks.json'),JSON.stringify(result,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({...result,bindings:bindings.length},null,2));
