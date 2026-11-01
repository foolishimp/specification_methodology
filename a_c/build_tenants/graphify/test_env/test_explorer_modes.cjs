// The real shared reader and layered adapter; force rendering is a stateful
// transport stub. Verifies mode-state conservation, not browser WebGL output.
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM}=require('jsdom');
const assets=path.join(__dirname,'../code/viewer');
const grounding={path:'specification/PRODUCT.md',start_line:1,end_line:1,quote:'source'};
const fixture={title:'Modes',focus:'A',model:{id:'model'},basis:{subject:{id:'subject'},calculus:{}},
 nodes:[{id:'A',family:'constraints',label:'Alpha',record:{predicate:{statement:'Alpha',grounding:[grounding]}}},
 {id:'B',family:'constraints',label:'Beta',record:{predicate:{statement:'Beta',grounding:[grounding]}}},
 {id:'C',family:'residuals',label:'Caveat',record:{uncertainty:{statement:'Open',grounding:[grounding]}}}],
 links:[{id:'AB',source:'A',target:'B',layer:'relation',label:'requires'},
 {id:'BC',source:'B',target:'C',layer:'required',label:'Requires retention'}],
 sources:{'specification/PRODUCT.md':{text:'source',sha256:'test'}},counts:{records:3,external:0}};
const tokens={TITLE:'Modes',LAYOUT:'unified',CSS:'',DATA:JSON.stringify(fixture),
 VENDOR:fs.readFileSync(path.join(assets,'layered.js'),'utf8'),APP:fs.readFileSync(path.join(assets,'explorer.js'),'utf8'),CREDITS:'',LICENSE:''};
const fixtureHTML=fs.readFileSync(path.join(assets,'explorer.html'),'utf8').replace(/@@([A-Z]+)@@/g,(_,key)=>tokens[key]);
function boot(html, fail=false){
 const dom=new JSDOM(html,{runScripts:'outside-only',pretendToBeVisual:true,url:'file:///offline/index.html'}),w=dom.window,d=w.document;
 const $=id=>d.getElementById(id),frames=new Map();let nextFrame=0;
 w.matchMedia=q=>({matches:q.includes('min-width: 1301')});w.HTMLElement.prototype.scrollIntoView=function(){};
 w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};w.HTMLDialogElement.prototype.close=function(){this.open=false;};
 w.requestAnimationFrame=fn=>{frames.set(++nextFrame,fn);return nextFrame;};w.cancelAnimationFrame=id=>frames.delete(id);
 w.ResizeObserver=class{constructor(fn){this.fn=fn;}observe(){this.fn();}};
 Object.defineProperties($('graph'),{clientWidth:{value:900},clientHeight:{value:700}});
 const forbidden=()=>{throw Error('network/service use');};w.fetch=w.XMLHttpRequest=w.WebSocket=w.Worker=forbidden;
 assert.equal(d.querySelectorAll('script[src],link[rel=stylesheet],iframe').length,0);
 w.eval([...d.scripts].at(-2).textContent);
 const engine={instances:0,paused:false,resumes:0,dimensions:3,data:{nodes:[],links:[]},handlers:{}};
 w.ForceGraph3D=function(host){
  engine.instances++;if(fail)throw Error('WebGL unavailable');
  assert.equal(host.id,'force-graph');
  const api=new Proxy({}, {get(_,method){
   if(method==='d3Force')return()=>({strength(){}});
   if(method==='graphData')return value=>{
    engine.data=value;const byId=new Map(value.nodes.map(n=>[n.id,n]));
    value.nodes.forEach((n,i)=>{n.x=i;n.y=i;if(engine.dimensions===2)delete n.z;else n.z=17;});
    value.links.forEach(l=>{l.source=byId.get(l.source);l.target=byId.get(l.target);});return api;};
   if(method==='numDimensions')return value=>{engine.dimensions=value;engine.data.nodes.forEach(n=>{if(value===2)delete n.z;else n.z=17;});return api;};
   if(method==='pauseAnimation')return()=>{engine.paused=true;return api;};
   if(method==='resumeAnimation')return()=>{engine.paused=false;engine.resumes++;return api;};
   if(method.startsWith('on'))return fn=>{engine.handlers[method]=fn;return api;};
   if(method==='graph2ScreenCoords')return(x,y,z)=>({x:200+x,y:200+y});
   return()=>api;
  }});return api;
 };
 w.eval([...d.scripts].at(-1).textContent);
 return{dom,w,d,$,engine,frames};
}
function info(t){return {hash:t.w.location.hash,reader:t.$('details').innerHTML,trail:t.$('trail').innerHTML,
 count:t.$('map-count').textContent,query:t.$('query').value,family:t.$('family').value,
 file:t.$('file-scope').innerHTML,origin:t.$('source-origin').innerHTML,results:t.$('results').innerHTML,
 layers:['required','relation','reference'].map(k=>t.$(k+'-layer').checked),data:t.$('explorer-data').textContent};}
function geometry(t){return t.d.body.dataset.renderer==='layered'
 ?{nodes:[...t.d.querySelectorAll('.tracks-node')].map(n=>n.dataset.id).sort(),links:[...t.d.querySelectorAll('.tracks-link')].map(e=>e.dataset.link).sort()}
 :{nodes:Array.from(t.engine.data.nodes,n=>n.id).sort(),links:Array.from(t.engine.data.links,e=>e.id).sort()};}
function roundtrip(t){
 const before=info(t),shape=geometry(t),reader=t.$('details').firstChild;
 for(const id of ['mode3','mode2','mode-layered','mode2','mode3','mode-layered']){
  t.$(id).focus();t.$(id).click();assert.equal(t.d.activeElement.id,id);
  assert.deepEqual(info(t),before,'mode change must preserve all reading/navigation state');
  assert.deepEqual(geometry(t),shape,'same displayed nodes and exact link identities in every mode');
  assert.equal(t.$('details').firstChild,reader,'reader DOM is retained, not recreated');
  assert.equal(t.$(id).getAttribute('aria-pressed'),'true');
  assert.equal([...t.frames.values()].filter(fn=>fn.name==='positionLabels').length,id==='mode-layered'?0:1,
    'one owned label loop only for a visible force view; bundled library initialization has its own callbacks');
  assert.equal(t.engine.paused,id==='mode-layered');
 }
 assert.equal(t.engine.instances,1,'reuse the force engine across switches');
 const resumes=t.engine.resumes;t.d.dispatchEvent(new t.w.Event('visibilitychange'));
 assert.equal(t.engine.resumes,resumes,'visibility event cannot resume a hidden force engine');
}
const checks=[];function check(name,fn){fn();checks.push(name);}
check('three modes preserve selected piece, file scope, filters, expansion and reading trail',()=>{
 const t=boot(fixtureHTML);assert.equal(t.engine.instances,0,'layered is lazy and needs no WebGL');
 t.$('file-tree').querySelector('button').click();roundtrip(t);
 t.$('query').value='Alpha';t.$('query').oninput();t.$('results').querySelector('button').click();
 t.$('details').querySelector('button[data-link="AB"]').click();t.$('expand').click();roundtrip(t);
 t.$('required-layer').checked=false;t.$('required-layer').onchange();roundtrip(t);
 t.$('overview').click();roundtrip(t);
 t.$('back').click();assert.equal(t.$('details').querySelector('h2').textContent,'Alpha');t.dom.window.close();
});
check('WebGL failure preserves the same information and leaves the layered reader usable',()=>{
 const t=boot(fixtureHTML,true);const before=info(t),shape=geometry(t);
 t.$('mode3').click();assert.deepEqual(info(t),before);assert.deepEqual(geometry(t),shape);
 assert.equal(t.$('mode-layered').getAttribute('aria-pressed'),'true');assert.equal(t.$('fit').disabled,false);
 assert.ok(t.$('mode3').disabled && t.$('mode2').disabled);
 assert.equal([...t.frames.values()].filter(fn=>fn.name==='positionLabels').length,0);
 assert.match(t.$('renderer-status').textContent,/layered view remains available/);t.dom.window.close();
});
if(process.argv[2])check('actual ABI file and R10 to R9 remain the same information in all three modes',()=>{
 const t=boot(fs.readFileSync(process.argv[2],'utf8'));
 [...t.$('file-tree').querySelectorAll('button')].find(n=>n.dataset.path==='specification/PRODUCT.md').click();roundtrip(t);
 t.$('query').value='R10';t.$('query').oninput();
 [...t.$('results').querySelectorAll('button')].find(n=>n.textContent.startsWith('R10 Replay and CLI agree')).click();
 [...t.$('details').querySelectorAll('.connection')].find(n=>n.textContent.includes('R9 ABG admitted causal')).click();
 roundtrip(t);assert.equal(t.$('trail').children.length,2);
 t.$('source-origin').querySelector('button').click();roundtrip(t);t.dom.window.close();
});
console.log(JSON.stringify({status:'passed',checks,limits:'Actual shared reader and layered adapter; force rendering is stubbed. Browser WebGL, visual layout and camera behavior not qualified.'},null,2));
