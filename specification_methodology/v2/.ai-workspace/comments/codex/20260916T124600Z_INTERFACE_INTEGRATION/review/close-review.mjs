import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';

const review=path.dirname(fileURLToPath(import.meta.url));
const sha=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
const hash=p=>sha(fs.readFileSync(p));
const json=p=>JSON.parse(fs.readFileSync(p));
const put=(name,data)=>fs.writeFileSync(path.join(review,name),JSON.stringify(data,null,2)+'\n',{flag:'wx'});
const checks=json(path.join(review,'checks.json'));
assert.equal(checks.mechanicalTests,30);
assert.equal(checks.mechanicalTestsPassed,true);
for(const row of checks.bindings){
  assert.equal(hash(row.path),row.sha256,row.path);
  const stat=fs.statSync(row.path);
  assert.equal(stat.size,row.bytes,row.path);
  assert.equal(stat.dev,row.device,row.path);
  assert.equal(stat.ino,row.inode,row.path);
}
const abiWorker='/Users/jim/src/apps/abiogenesis/.ai-workspace/comments/codex/20260916_ABG5_INTERFACE_INTEGRATION_FRAME/worker';
const basis=json(path.join(abiWorker,'basis.json'));
let symlinks=0;
for(const control of basis.controls.filter(c=>c.root.includes('/Library/Application Support/'))){
  for(const row of control.rows){
    if(row.symlink){assert.equal(fs.readlinkSync(path.join(control.root,row.path)),row.symlink);symlinks++;}
  }
}
const retained=json(path.join(review,'retained-case-checks.json'));
assert.equal(retained.sameResponseLinks,7);
assert.equal(retained.events,204);
assert.equal(retained.actualActorInvocations,1);
const now=new Date().toISOString();
const closure={
  completedAt:now,
  command:['node',path.join(review,'close-review.mjs')],
  readOnlyBindingsRechecked:checks.bindings.length,
  sameSha256ByteLengthDeviceAndInode:true,
  installedSymlinksRechecked:symlinks,
  independentSourceGuardsPassed:30,
  retainedFailureContentReextracted:true,
  subjectsUnchangedSinceIndependentChecks:true,
  representativeSemanticCases:11,
  casesAreNotExecutedProductOrNativeTrials:true,
  sourceCanonicalMutations:0,
  nativeOrPublicRuns:0,
  result:'satisfied',
  resultScope:'exact source/document composition and faithful retained-case application',
  newNativeUserAnd1BOutcome:'unknown',
  supportedNewFindings:[],
  priorRetainedFinding:'S2 predecessor field-context gap, reused only at its prior exact subject',
  effects:'new review evidence only in this directory'
};
put('closure-checks.json',closure);
const names=fs.readdirSync(review).sort();
assert.ok(!names.includes('manifest.json'));
assert.ok(!names.includes('freeze.json'));
const members=names.map(name=>{
  const p=path.join(review,name),stat=fs.lstatSync(p);
  assert.ok(stat.isFile(),name);
  return {path:name,bytes:stat.size,sha256:hash(p)};
});
put('manifest.json',members);
const freeze={
  activation:'STDO_ABG_E2E_INTERFACE_FRAME_REVIEW_01',
  actor:'/root/rc7_waste_review',
  consumer:'/root',
  startedAt:'2026-09-16T13:06:00Z',
  closedAt:now,
  elapsedMinutesFromRecordedStart:(Date.parse(now)-Date.parse('2026-09-16T13:06:00Z'))/60000,
  manifest:{path:'manifest.json',sha256:hash(path.join(review,'manifest.json')),members:members.length},
  sourceSubject:{freezeSha256:'5a86eca7e202af8c99310555f99c645c13c6327e5eba6668df67a0c964428625',manifestSha256:'a1cd65d95afedce1857ecc43ced0e91b4e4780116680b607ae21e12c35947e0f'},
  abiSubject:{freezeSha256:'79ea5c50a208830d4ea1b30dc2314372403e21f438382b5aaa03e013564a0f41',manifestSha256:'d0b3f73d1e068c685a865a690815a8c51ed121a7e50a84822f46962de30a387c'},
  verdicts:{genericSourceFrame:'satisfied',sourceCompressions:'satisfied',abiLocalDerivation:'satisfied',retainedCaseApplication:'satisfied',newNativeOrLLMUAT:'unknown',predecessorImplementationAcceptance:'unknown',oneBClosure:'unknown'},
  report:{path:'review.md',sha256:hash(path.join(review,'review.md'))},
  findings:[],
  nonclaims:['acceptance','runtime implementation qualification','new native execution','live LLM usability','1B closure','release/install promotion'],
  stopped:true
};
put('freeze.json',freeze);
for(const row of members)assert.equal(hash(path.join(review,row.path)),row.sha256);
console.log(JSON.stringify({closedAt:now,freezeSha256:hash(path.join(review,'freeze.json')),manifestSha256:freeze.manifest.sha256,members:members.length,verdicts:freeze.verdicts},null,2));
