// Independent finite probe of the actual generated/installed proof page.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const {JSDOM, ResourceLoader} = require('jsdom');
const file=path.resolve(process.argv[2]), raw=fs.readFileSync(file);
class Deny extends ResourceLoader { fetch(url){throw Error('external resource '+url);} }
const dom=new JSDOM(raw.toString(), {url:pathToFileURL(file).href,runScripts:'outside-only',resources:new Deny()});
const w=dom.window,d=w.document,$=id=>d.getElementById(id);
for(const key of ['fetch','XMLHttpRequest','WebSocket','Worker'])w[key]=()=>{throw Error('unselected execution '+key);};
w.HTMLElement.prototype.scrollIntoView=function(){};
w.HTMLDialogElement.prototype.showModal=function(){this.open=true;};
w.HTMLDialogElement.prototype.close=function(){this.open=false;};
assert.equal(d.querySelectorAll('script[src],iframe,img,link[rel=stylesheet]').length,0);
const scripts=[...d.querySelectorAll('script')];assert.equal(scripts.length,2);
const data=JSON.parse($('proof-data').textContent),catalog=data.catalog,byId=new Map(catalog.declarations.map(x=>[x.id,x]));
w.eval(scripts[1].textContent);
const opened=[];
for(const claim of catalog.claims){
 d.querySelector(`[data-claim="${claim.id}"]`).click();
 assert.equal($('reader').dataset.view,'claim');
 assert.ok($('reader').textContent.includes(claim.condition));
 for(const id of claim.declarations){
  $('reader').querySelector(`[data-target="${id}"]`).click();
  const decl=byId.get(id);assert.equal($('reader').dataset.declaration,id);
  assert.equal($('reader').querySelector('.statement').textContent,decl.statement);
  assert.equal($('reader').querySelector('details pre').textContent,data.sources[decl.file].split('\n').slice(decl.start_line-1,decl.end_line).join('\n'));
  assert.match($('reader').textContent,/not Lean elaborator or kernel proof-dependency edges/);
  assert.match($('reader').textContent,/no separate verdict is assigned/);
  $('reader').querySelector('[data-source]').click();
  assert.equal($('reader').dataset.view,'file');
  assert.equal(Number(d.querySelector('.source-row.selected').dataset.line),decl.start_line);
  assert.equal([...$('full-source').querySelectorAll('.source-text')].map(x=>x.textContent).join('\n'),data.sources[decl.file]);
  $('back').click();assert.equal($('reader').dataset.declaration,id);
  const ref=$('reader').querySelector('[data-target]');
  if(ref){const target=ref.dataset.target;ref.click();assert.equal($('reader').dataset.declaration,target);$('back').click();assert.equal($('reader').dataset.declaration,id);}
  $('back').click();assert.equal($('reader').dataset.view,'claim');
  opened.push(id);
 }
}
for(const [name,start,end,kind] of [['AC.Closed',19,20,'Definition'],['AC.Witness',30,32,'Definition'],['AC.witnessDecidable',34,41,'Instance'],['AC.CertificateValid',45,47,'Definition']]){
 $('query').value=name;$('query').dispatchEvent(new w.Event('input'));
 const button=[...$('results').querySelectorAll('button')].find(x=>x.dataset.declaration===name);assert.ok(button);button.click();
 assert.equal($('reader').dataset.declaration,name);assert.equal(byId.get(name).kind,kind);
 assert.deepEqual([byId.get(name).start_line,byId.get(name).end_line],[start,end]);
 assert.match($('reader').querySelector('.kind').textContent,new RegExp(`${start}–${end}`));
}
$('query').value='';$('query').dispatchEvent(new w.Event('input'));
for(const kind of new Set(catalog.declarations.map(x=>x.kind))){
 $('kind').value=kind;$('kind').dispatchEvent(new w.Event('change'));
 while(!$('more').hidden)$('more').click();
 assert.equal($('results').querySelectorAll('button').length,catalog.declarations.filter(x=>x.kind===kind).length);
 for(const b of $('results').querySelectorAll('button'))assert.equal(byId.get(b.dataset.declaration).kind,kind);
}
for(const source of catalog.sources){
 $('kind').value='';$('module').value=source.file;$('module').dispatchEvent(new w.Event('change'));
 while(!$('more').hidden)$('more').click();
 assert.equal($('results').querySelectorAll('button').length,catalog.declarations.filter(x=>x.file===source.file).length);
 const b=[...$('modules').querySelectorAll('button')].find(x=>x.dataset.file===source.file);b.click();
 assert.equal([...$('full-source').querySelectorAll('.source-text')].map(x=>x.textContent).join('\n'),data.sources[source.file]);
 assert.equal(crypto.createHash('sha256').update(data.sources[source.file]).digest('hex'),source.sha256);
}
$('evidence-open').click();assert.equal($('evidence').open,true);
assert.ok([...$('evidence-body').querySelectorAll('pre')].some(x=>x.textContent===data.report_text));
assert.equal(crypto.createHash('sha256').update(data.report_text).digest('hex'),catalog.report.sha256);
for(const text of ['Retained historical','not a fresh proof execution','not requalified','204 audited declaration contracts','not that many independent mathematical results','Classical.choice','Quot.sound','propext','32-record','14-record','not the later 1,987-record'])assert.ok($('evidence-body').textContent.includes(text),text);
$('evidence-close').click();assert.equal($('evidence').open,false);
const firstTrail=$('trail').querySelector('button');firstTrail.click();assert.equal($('reader').dataset.view,'claim');assert.equal($('back').disabled,true);
const links=[...d.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'));
for(const href of links)assert.ok(fs.existsSync(path.resolve(path.dirname(file),href)),href);
console.log(JSON.stringify({status:'passed',page_sha256:crypto.createHash('sha256').update(raw).digest('hex'),claims:catalog.claims.length,claim_declarations:opened.length,declarations:catalog.declarations.length,source_files:catalog.sources.length,local_links:links.length,network_requests:0,limits:'jsdom source/navigation check; no actual browser rendering or Lean execution'},null,2));
dom.window.close();
