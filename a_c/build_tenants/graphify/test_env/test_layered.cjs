// Geometry checks require only Node. Offline interaction checks use jsdom@26.1.0
// from NODE_PATH. Optional argument: the actual generated standalone HTML.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {JSDOM} = require('jsdom');
const assets = path.join(__dirname, '../code/viewer');
const source = fs.readFileSync(path.join(assets, 'layered.js'), 'utf8');
const context = vm.createContext({}); vm.runInContext(source, context);
const layout = (nodes, edges) => JSON.parse(JSON.stringify(context.ACTracks.layout(nodes, edges)));
const nodes = ['a','b','c','d','isolated'].map(id => ({id, label:id, family:'constraints', record:{predicate:{statement:id}}}));
const edge = (id, a, b) => ({id, source:a, target:b, layer:'relation', label:'requires'});
const edges = [edge('a-b','a','b'), edge('a-b-2','a','b'), edge('b-c','b','c'), edge('c-d','c','d'), edge('self','d','d')];
const checks = [];
function check(name, fn) { fn(); checks.push(name); }

check('directed ranks retain isolated nodes, parallel edges and self-relations without mutation', () => {
  const before = JSON.stringify({nodes,edges});
  const result = layout(nodes, edges), pos = new Map(result.nodes.map(n => [n.node.id,n]));
  assert.ok(pos.get('a').x < pos.get('b').x && pos.get('b').x < pos.get('c').x);
  assert.deepEqual(new Set(result.nodes.map(n => n.node.id)), new Set(nodes.map(n=>n.id)));
  assert.deepEqual(result.edges.map(e=>e.link),edges);
  assert.equal(new Set(result.edges.map(e=>e.path)).size,edges.length);
  assert.equal(pos.get('isolated').cycle,false); assert.equal(pos.get('d').cycle,true);
  assert.equal(JSON.stringify({nodes,edges}),before);
  for(const n of result.nodes) assert.ok([n.x,n.y,n.width,n.height].every(Number.isFinite));
});
check('cycle condensation preserves reciprocal links and stable placement under input reordering', () => {
  const cyclic = [...edges,edge('c-b','c','b')];
  const result = layout(nodes,cyclic), reversed = layout([...nodes].reverse(),[...cyclic].reverse());
  assert.deepEqual(result.nodes,reversed.nodes);
  const pathMap = r => Object.fromEntries(r.edges.map(e=>[e.link.id,e.path]).sort(([a],[b])=>a.localeCompare(b)));
  assert.deepEqual(pathMap(result),pathMap(reversed));
  const positions = new Map(result.nodes.map(n=>[n.node.id,n]));
  assert.ok(positions.get('b').cycle && positions.get('c').cycle);
  assert.equal(result.edges.length,cyclic.length);
});
check('deep chains use iterative traversal and empty input stays finite', () => {
  const chain = Array.from({length:6000},(_,i)=>({id:String(i),label:String(i),family:'objects'}));
  const links = chain.slice(1).map((n,i)=>edge(String(i),String(i),n.id));
  assert.equal(layout(chain,links).nodes.length,chain.length);
  const empty = layout([],[]);assert.ok(Number.isFinite(empty.width) && Number.isFinite(empty.height));
});

const fixture = {title:'Offline tracks',nodes,links:edges,sources:{},focus:'a',
  counts:{records:nodes.length,external:0},basis:{subject:{id:'test'},calculus:{}},model:{id:'fixture'}};
const template = fs.readFileSync(path.join(assets,'explorer.html'),'utf8');
const tokens = {TITLE:'Offline tracks',LAYOUT:'layered',CSS:'',DATA:JSON.stringify(fixture),VENDOR:source,
  APP:fs.readFileSync(path.join(assets,'explorer.js'),'utf8'),CREDITS:'Local',LICENSE:''};
function boot(html) {
  const dom = new JSDOM(html,{runScripts:'outside-only',url:'file:///offline/layered.html'});
  const w=dom.window,d=w.document;
  const forbidden=()=>{throw Error('Unexpected service, network, WebGL or animation dependency');};
  w.fetch=w.XMLHttpRequest=w.WebSocket=w.Worker=w.EventSource=w.ForceGraph3D=w.requestAnimationFrame=forbidden;
  w.matchMedia=q=>({matches:q.includes('min-width: 1301')});
  w.HTMLElement.prototype.scrollIntoView=function(){};
  w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};
  w.HTMLDialogElement.prototype.close=function(){this.open=false;};
  assert.equal(d.querySelectorAll('script[src],link[rel=stylesheet],iframe').length,0);
  for(const script of d.scripts) if(script.type!=='application/json')w.eval(script.textContent);
  return {dom,w,d,$:id=>d.getElementById(id)};
}
const fixtureHTML = template.replace(/@@([A-Z]+)@@/g,(_,key)=>tokens[key]);
check('standalone DOM renders every visible node/edge, labels, zoom and keyboard navigation',()=>{
  const t=boot(fixtureHTML);t.$('overview').click();
  assert.equal(t.d.querySelectorAll('.tracks-node').length,nodes.length);
  assert.equal(t.d.querySelectorAll('.tracks-link').length,edges.length);
  assert.equal(t.d.querySelectorAll('.tracks-node strong').length,nodes.length);
  assert.equal(t.$('force-controls').hidden,true);assert.equal(t.$('layered-controls').hidden,false);
  t.$('zoom-in').click();assert.equal(t.$('zoom-reset').textContent,'125%');
  t.$('zoom-reset').click();assert.equal(t.$('zoom-reset').textContent,'100%');
  const a=[...t.d.querySelectorAll('.tracks-node')].find(n=>n.dataset.id==='a');
  a.focus();a.dispatchEvent(new t.w.KeyboardEvent('keydown',{key:'ArrowRight',bubbles:true}));
  assert.equal(t.d.activeElement.dataset.id,'b');
  const connection=[...t.d.querySelectorAll('.tracks-link')].find(n=>n.dataset.link==='a-b');
  connection.focus();
  connection.dispatchEvent(new t.w.KeyboardEvent('keydown',{key:'Enter',bubbles:true}));
  assert.equal(t.$('details').querySelector('h2').textContent,'b');
  assert.equal(t.$('trail').children.length,2);
  assert.equal(t.d.activeElement.dataset.id,'b','link activation keeps keyboard focus on the opened record');
  const c=[...t.d.querySelectorAll('.tracks-node')].find(n=>n.dataset.id==='c');
  c.focus();c.click();assert.equal(t.d.activeElement.dataset.id,'c','card activation retains keyboard focus');
  t.$('required-layer').focus();t.$('required-layer').onchange();
  assert.equal(t.d.activeElement.id,'required-layer','external controls retain their focus');
  t.dom.window.close();
});
check('untrusted card and edge labels remain literal text',()=>{
  const bad=JSON.parse(JSON.stringify(fixture));bad.nodes[0].label='<img src=x onerror=boom()>';
  bad.links[0].label='<script>boom()</script>';
  const html=template.replace(/@@([A-Z]+)@@/g,(_,key)=>key==='DATA'?JSON.stringify(bad).replace(/</g,'\\u003c'):tokens[key]);
  const t=boot(html);assert.equal(t.$('graph').querySelectorAll('img,script').length,0);
  assert.match(t.$('graph').textContent,/<img src=x/);t.dom.window.close();
});
if(process.argv[2])check('actual ABI export operates from file URL with all network and WebGL entry points forbidden',()=>{
  const t=boot(fs.readFileSync(process.argv[2],'utf8'));
  assert.equal(t.$('file-count').textContent,'86 files');
  const file=[...t.$('file-tree').querySelectorAll('button')].find(n=>n.dataset.path==='specification/PRODUCT.md');
  file.click();const count=t.d.querySelectorAll('.tracks-node').length;assert.ok(count>200);
  t.$('query').value='R10';t.$('query').oninput();
  const r10=[...t.$('results').querySelectorAll('button')].find(b=>b.textContent.startsWith('R10 Replay and CLI agree'));
  assert.ok(r10);r10.click();
  const r9=[...t.$('details').querySelectorAll('.connection')].find(b=>b.textContent.includes('R9 ABG admitted causal'));
  assert.ok(r9);r9.click();assert.equal(t.$('trail').children.length,2);
  assert.match(t.$('details').querySelector('h2').textContent,/R9 ABG admitted/);
  t.$('source-origin').querySelector('button').click();assert.equal(t.d.querySelectorAll('.tracks-node').length,count);
  const read=[...t.$('file-scope').querySelectorAll('button')].find(b=>b.textContent==='Read file');read.click();
  assert.equal(t.$('source-dialog').open,true);
  const data=JSON.parse(t.$('explorer-data').textContent);
  assert.deepEqual([...t.$('source-text').children].map((row,i)=>row.textContent.slice(String(i+1).padStart(4,' ').length+2)),
    data.sources['specification/PRODUCT.md'].text.split('\n'));
  t.$('source-close').click();t.$('overview').click();
  const viewport=t.d.querySelector('.tracks-viewport'),extent=t.d.querySelector('.tracks-extent');
  Object.defineProperties(viewport,{clientWidth:{value:640},clientHeight:{value:600}});
  t.$('fit').click();
  assert.ok(parseFloat(extent.style.width)<=640.00001 && parseFloat(extent.style.height)<=600.00001,
    'Fit contains the entire actual ABI graph at 640 by 600, including scales below 10%');
  assert.notEqual(t.$('zoom-reset').textContent,'0%');
  t.dom.window.close();
});
console.log(JSON.stringify({status:'passed',checks,limits:'Finite geometry and offline DOM checks; no browser visual-layout qualification.'},null,2));
