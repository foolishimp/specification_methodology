// Offline DOM regression checks. Install jsdom@26.1.0 in a separate test
// environment and supply its node_modules through NODE_PATH. No browser, network,
// force renderer or subject implementation is executed. A supplied layered
// export executes its local adapter, without browser visual qualification.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const viewer = path.join(__dirname, '../code/viewer');
const template = fs.readFileSync(path.join(viewer, 'explorer.html'), 'utf8');
const app = fs.readFileSync(path.join(viewer, 'explorer.js'), 'utf8');
const g = (p, line = 1) => ({path:p, start_line:line, end_line:line, quote:'source'});
const hostile = 'docs/<img onerror=boom()>.md';
const fixture = {
  nodes:[
    {id:'A',family:'objects',label:'Alpha',record:{value:{label:'Alpha',grounding:[g('docs/a.md'),g('docs/a.md'),g('docs/sub/b.md',2)]}}},
    {id:'B',family:'constraints',label:'Beta',record:{predicate:{statement:'Beta',grounding:[g('docs/sub/b.md')]}}},
    {id:'C',family:'residuals',label:'Missing source',record:{uncertainty:{statement:'Missing source',grounding:[g('missing/absent.md')]}}},
    {id:'D',family:'objects',label:'Literal path',record:{value:{label:'Literal path',grounding:[g(hostile)]}}}
  ],
  links:[{id:'A-B',source:'A',target:'B',layer:'relation',label:'requires'}],
  sources:{'docs/a.md':{text:'source',sha256:'a'},'docs/sub/b.md':{text:'source\nsource',sha256:'b'},'docs/empty.md':{text:'No represented record',sha256:'e'},[hostile]:{text:'<script>boom()</script>',sha256:'x'}},
  basis:{subject:{id:'test:subject'},calculus:{}},model:{id:'test:model'},focus:'A',
  counts:{records:4,external:0,required:0,relations:1,references:0}
};
function boot(data = fixture, width = 1500, artifact = null) {
  const dom = new JSDOM(artifact || template, {runScripts:'outside-only',url:'https://offline.invalid/'});
  const w = dom.window, d = w.document;
  w.matchMedia = query => ({matches:query.includes('max-width: 1300') ? width <= 1300 : query.includes('min-width: 1301') ? width >= 1301 : false});
  w.requestAnimationFrame = () => 0;
  w.HTMLElement.prototype.scrollIntoView = function(){};
  w.HTMLDialogElement.prototype.showModal = function(){this.open = true;};
  w.HTMLDialogElement.prototype.close = function(){this.open = false;};
  if (!artifact) d.getElementById('explorer-data').textContent = JSON.stringify(data);
  if (artifact && ['layered','unified'].includes(d.body.dataset.renderer)) w.eval([...d.scripts].at(-2).textContent);
  w.eval(artifact ? [...d.scripts].at(-1).textContent : app);
  return {dom,w,d,$:id=>d.getElementById(id),click:text=>{
    const element=[...d.querySelectorAll('button')].find(b=>b.textContent===text);
    assert.ok(element,'button missing: '+text); assert.ok(!element.disabled,'button disabled: '+text); element.click();
  }};
}
function entry(t, p) { return [...t.$('file-tree').querySelectorAll('button')].find(b=>b.dataset.path===p); }
function results(t) { return [...t.$('results').querySelectorAll('button')].map(b=>b.dataset.id); }
const checks=[];
function check(name, fn) { fn(); checks.push(name); }

check('exact file mapping deduplicates records, preserves multiple sources and distinguishes paths',()=>{
  const t=boot();
  assert.equal(t.$('file-count').textContent,'5 files');
  assert.equal(entry(t,'docs/a.md').querySelector('small').textContent,'1');
  assert.equal(entry(t,'docs/sub/b.md').querySelector('small').textContent,'2');
  entry(t,'docs/sub/b.md').click();
  assert.deepEqual(results(t),['B','A']);
  assert.equal(t.$('total').textContent,'2');
  assert.equal(t.$('family').value,'');
  assert.match(t.$('map-count').textContent,/File map.*2 visible nodes/);
  t.dom.window.close();
});
check('file to logical traversal and return keeps exact reading trail',()=>{
  const t=boot(); entry(t,'docs/a.md').click(); t.$('results').querySelector('button').click();
  t.$('details').querySelector('button[data-link="A-B"]').click();
  assert.equal(t.$('trail').children.length,2);
  assert.equal(t.$('details').querySelector('h2').textContent,'Beta');
  assert.match(t.$('source-origin').textContent,/docs\/a.md/);
  assert.deepEqual(results(t),['A']);
  t.$('source-origin').querySelector('button').click();
  assert.equal(t.$('trail').children.length,2);
  assert.match(t.$('map-count').textContent,/File map.*docs\/a.md/);
  const reveal=t.$('details').querySelector('button[aria-label="Show in files · docs/sub/b.md"]');
  reveal.click();
  assert.equal(t.$('trail').children.length,2);
  assert.equal(t.$('details').querySelector('h2').textContent,'Beta');
  assert.equal(entry(t,'docs/sub/b.md').getAttribute('aria-current'),'true');
  assert.equal([...t.$('file-tree').querySelectorAll('details')].find(e=>e.dataset.folder==='docs/sub').open,true);
  t.$('back').click(); assert.equal(t.$('details').querySelector('h2').textContent,'Alpha');
  assert.equal(t.$('trail').children.length,1); t.dom.window.close();
});
check('empty embedded file and missing full source are distinct and readable honestly',()=>{
  const t=boot(); entry(t,'docs/empty.md').click(); assert.deepEqual(results(t),[]);
  t.click('Read file'); assert.equal(t.$('source-dialog').open,true);
  assert.match(t.$('source-text').textContent,/No represented record/); t.click('Close');
  entry(t,'missing/absent.md').click(); assert.deepEqual(results(t),['C']);
  assert.equal([...t.$('file-scope').querySelectorAll('button')].find(b=>b.textContent==='Read file').disabled,true);
  assert.match(t.$('file-scope').textContent,/not embedded/); t.dom.window.close();
});
check('file filter, family filter and global reset remain independent',()=>{
  const t=boot(); t.$('file-query').value='sub/b'; t.$('file-query').oninput();
  assert.equal(t.$('file-tree').querySelectorAll('button').length,1);
  entry(t,'docs/sub/b.md').click(); t.$('family').value='constraints'; t.$('family').onchange();
  assert.deepEqual(results(t),['B']); t.$('query').value='not found';t.$('query').oninput();assert.deepEqual(results(t),[]);
  t.click('All files'); assert.deepEqual(results(t),[]);assert.equal(t.$('file-scope').hidden,true);
  assert.equal(t.$('total').textContent,'1');
  t.$('query').value='';t.$('query').oninput();assert.deepEqual(results(t),['B']);t.dom.window.close();
});
check('source labels and content remain text, including hostile strings',()=>{
  const t=boot(); entry(t,hostile).click();t.click('Read file');
  assert.equal(t.$('source-title').textContent,hostile);
  assert.match(t.$('source-text').textContent,/<script>boom\(\)<\/script>/);
  assert.equal(t.$('source-text').querySelectorAll('script').length,0);
  assert.equal(t.$('file-tree').querySelectorAll('img').length,0);t.dom.window.close();
});
check('narrow flyout exposes file results and closing preserves state',()=>{
  const t=boot(fixture,800);assert.equal(t.$('files-pane').hidden,true);
  t.$('files-toggle').click();assert.equal(t.$('files-pane').hidden,false);
  entry(t,'docs/a.md').click();assert.equal(t.$('files-pane').hidden,true);
  assert.deepEqual(results(t),['A']);t.$('files-toggle').click();t.$('files-close').click();
  assert.deepEqual(results(t),['A']);t.dom.window.close();
});

if (process.argv[2]) check('actual ABI artifact maps all source paths and follows R10 to R9',()=>{
  const t=boot(null,1500,fs.readFileSync(process.argv[2],'utf8'));
  assert.equal(t.$('file-count').textContent,'86 files');
  const d=JSON.parse(t.$('explorer-data').textContent);
  const paths=new Map(Object.keys(d.sources).map(p=>[p,new Set()]));
  function visit(v,id){ if (!v || typeof v!=='object') return;
    if(typeof v.path==='string' && typeof v.quote==='string' && Number.isInteger(v.start_line) && Number.isInteger(v.end_line)){
      if(!paths.has(v.path)) paths.set(v.path,new Set());paths.get(v.path).add(id);
    } Object.values(v).forEach(c=>visit(c,id)); }
  d.nodes.forEach(n=>visit(n.record,n.id));
  for(const [p,ids] of paths){entry(t,p).click();while(!t.$('more').hidden)t.$('more').click();assert.deepEqual(new Set(results(t)),ids,p);}
  entry(t,'specification/PRODUCT.md').click();t.$('query').value='R10';t.$('query').oninput();
  const r10=[...t.$('results').querySelectorAll('button')].find(b=>b.textContent.startsWith('R10 Replay and CLI agree on typed terminal outcome'));
  assert.ok(r10);r10.click();
  const r9=[...t.$('details').querySelectorAll('.connection')].find(b=>b.textContent.includes('R9 ABG admitted causal result and closure events'));
  assert.ok(r9);r9.click();assert.equal(t.$('trail').children.length,2);
  assert.equal(t.$('details').querySelector('h2').textContent,'R9 ABG admitted causal result and closure events');
  t.click('specification/PRODUCT.md:1541–1541');
  assert.match(t.$('source-text').querySelector('.selected-line').textContent,/R9 ABG admitted/);
  t.dom.window.close();
});
console.log(JSON.stringify({status:'passed',checks,limits:'Offline DOM behavior; force renderer unavailable deliberately, layered adapter runs when supplied. No visual browser/layout/3D interaction qualification.'},null,2));
