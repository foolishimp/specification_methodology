// Label adapter regression with the exact pinned renderer dimension-change
// handler. Projection/graphics are stubbed: this does not claim WebGL rendering.
// Run with jsdom@26.1.0 available through NODE_PATH; optionally pass exported HTML.
'use strict';
const fs = require('node:fs'), path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {JSDOM} = require('jsdom');
const viewer = path.join(__dirname, '../code/viewer');
const vendor = fs.readFileSync(path.join(viewer,'vendor/3d-force-graph-1.80.1.min.js'),'utf8');
const pins = JSON.parse(fs.readFileSync(path.join(viewer,'vendor/manifest.json'),'utf8'));
assert.equal(crypto.createHash('sha256').update(vendor).digest('hex'),pins.files['3d-force-graph-1.80.1.min.js']);
// Exercise the actual dependency's removal of z/vz, rather than assuming its shape.
const match = vendor.match(/numDimensions:\{default:3,onChange\(e,t\)(\{.*?\})\},dagMode:/);
assert.ok(match,'pinned renderer dimension callback not found');
const changeDimensions = new Function('e','t',match[1].slice(1,-1));
const checks=[];
function exercise(html, app, data, name) {
  const dom=new JSDOM(html,{runScripts:'outside-only',pretendToBeVisual:true,url:'https://offline.invalid/'});
  const w=dom.window,d=w.document;
  w.matchMedia=()=>({matches:false});w.HTMLElement.prototype.scrollIntoView=function(){};
  w.ResizeObserver=class {constructor(fn){this.fn=fn;} observe(){this.fn();}};
  Object.defineProperties(d.getElementById('graph'),{clientWidth:{value:1000},clientHeight:{value:800}});
  const frames=[];w.requestAnimationFrame=fn=>{frames.push(fn);return frames.length;};
  let state={nodes:[],links:[]},dims=3;
  const projected=[];
  const rendererState={d3ForceLayout:{force:()=>({strength(){}})},get graphData(){return state;}};
  let graph;
  w.ForceGraph3D=function(){
    graph=new Proxy({}, {get(_,method){
      if(method==='d3Force')return ()=>({strength(){}});
      if(method==='graphData')return value=>{
        if(!value)return state;
        state=value;state.nodes.forEach((n,i)=>{n.x=i;n.y=i;n.z=17;});
        changeDimensions(dims,rendererState);return graph;
      };
      if(method==='numDimensions')return value=>{
        dims=value;changeDimensions(dims,rendererState);
        if(dims===3)state.nodes.forEach(n=>{n.z=17;});return graph;
      };
      if(method==='graph2ScreenCoords')return (x,y,z)=>{projected.push({x,y,z});return {x:200+x,y:200+y};};
      return ()=>graph;
    }});return graph;
  };
  if(data)d.getElementById('explorer-data').textContent=JSON.stringify(data);
  const unified=d.body.dataset.renderer==='unified';
  if(unified) w.eval(fs.readFileSync(path.join(viewer,'layered.js'),'utf8'));
  w.eval(app || [...d.scripts].at(-1).textContent);
  if(unified) d.getElementById('mode3').click();
  const frame=t=>{assert.equal(frames.length,1);frames.shift()(t);};
  const labels=()=>[...d.querySelectorAll('.map-label')];
  frame(100);assert.ok(labels().length);assert.ok(labels().every(l=>!l.hidden),'initial 3D labels visible');
  d.getElementById('mode2').click();
  assert.ok(state.nodes.every(n=>!Object.hasOwn(n,'z')),'actual dependency removes depth in 2D');
  const before=projected.length;frame(200);
  assert.ok(labels().every(l=>!l.hidden),'2D labels remain visible without node.z');
  assert.ok(projected.length>before,'2D labels are projected');
  assert.ok(projected.slice(before).every(p=>p.z===0),'planar labels project at zero depth');
  const first=state.nodes[0];const x=first.x;first.x=NaN;frame(300);
  assert.equal(labels()[0].hidden,true,'invalid planar position is still hidden');first.x=x;
  d.getElementById('mode3').click();frame(400);
  assert.ok(labels().every(l=>!l.hidden),'return to 3D restores labels');
  assert.ok(projected.at(-1).z===17,'3D preserves actual depth');
  delete first.z;frame(500);assert.equal(labels()[0].hidden,true,'missing 3D position remains pending');
  d.getElementById('mode2').click();frame(600);assert.ok(labels().every(l=>!l.hidden),'repeated 2D switch restores labels');
  checks.push(name);w.close();
}
const sample={nodes:[{id:'A',family:'objects',label:'Alpha',record:{value:{label:'Alpha'}}}],links:[],sources:{},focus:'A',basis:{subject:{id:'test'},calculus:{}},model:{id:'test'},counts:{records:1}};
exercise(fs.readFileSync(path.join(viewer,'explorer.html'),'utf8'),fs.readFileSync(path.join(viewer,'explorer.js'),'utf8'),sample,'source viewer: 3D → 2D → 3D → 2D, zero depth and invalid-coordinate controls');
if(process.argv[2])exercise(fs.readFileSync(process.argv[2],'utf8'),null,null,'actual exported viewer: dimension switching preserves labels');
console.log(JSON.stringify({status:'passed',checks,pinned_renderer_handler:true,limits:'Offline DOM and coordinate-adapter checks with exact upstream dimension mutation; projection and WebGL are stubbed.'},null,2));
