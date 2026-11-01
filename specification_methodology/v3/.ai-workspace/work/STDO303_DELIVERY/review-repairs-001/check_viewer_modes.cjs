'use strict';
// Reuse the exact a_c shared-reader harness, changing only its subject-specific
// exercise. This is DOM/state evidence; force rendering remains a transport stub.
const fs = require('node:fs'), path = require('node:path'), Module = require('node:module');
const artifact = path.resolve(process.argv[2]);
const harness = path.resolve(process.argv[3]);
const source = fs.readFileSync(harness, 'utf8');
const marker = "if(process.argv[2])check('actual ABI file";
if (source.indexOf(marker) < 0) throw Error('selected shared-reader harness changed');
const exercise = `
check('installed STDO artifact conserves selection, source scope and trail across all modes',()=>{
 const t=boot(fs.readFileSync(${JSON.stringify(artifact)},'utf8'));
 assert.equal(t.$('file-count').textContent,'58 files');
 roundtrip(t);
 const file=[...t.$('file-tree').querySelectorAll('button')]
  .filter(n=>Number(n.querySelector('small').textContent)>0)
  .sort((a,b)=>Number(a.querySelector('small').textContent)-Number(b.querySelector('small').textContent))[0];
 assert.ok(file);file.click();roundtrip(t);
 const record=t.$('results').querySelector('button');assert.ok(record);record.click();
 roundtrip(t);
 const connection=t.$('details').querySelector('.connection');assert.ok(connection);connection.click();
 roundtrip(t);assert.equal(t.$('trail').children.length,2);
 t.$('back').click();assert.equal(t.$('trail').children.length,1);
 t.$('source-origin').querySelector('button').click();roundtrip(t);
 t.dom.window.close();
});
console.log(JSON.stringify({status:'passed',checks,
 limits:'Actual installed HTML, shared reader and Layered adapter. Force/WebGL, camera and visual layout are not qualified.'},null,2));
`;
const runner = new Module(harness, module);
runner.filename = harness;
runner.paths = Module._nodeModulePaths(path.dirname(harness));
runner._compile(source.slice(0, source.indexOf(marker)) + exercise, harness);
