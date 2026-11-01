// Shared reader and actual layered adapter; force transport is stubbed.
// NODE_PATH selects the existing jsdom. Optional argument: generated overlay HTML.
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path');
const {JSDOM} = require('jsdom');
const assets = path.join(__dirname, '../code/viewer');
const grounding = (path, quote = 'source') => ({path, start_line: 1, end_line: 1, quote});
const requirementLabel = ('Preserve exact amounts and their unresolved rounding conditions throughout the complete export pipeline. ').repeat(6).trim();
const native = {
  title: 'Code overlay', focus: 'R', model: {id: 'base:model', sha256: 'base-digest'},
  basis: {subject: {id: 'base:source', sha256: 'source-digest'}, calculus: {id: 'calculus'}},
  nodes: [
    {id: 'R', family: 'constraints', label: requirementLabel, record: {predicate: {statement: requirementLabel, grounding: [grounding('specification/PRODUCT.md')]}}},
    {id: 'D', family: 'objects', label: 'Exact codec', record: {value: {label: 'Exact codec'}}},
    {id: 'Q', family: 'residuals', label: 'Rounding unresolved', record: {uncertainty: {statement: 'Rounding unresolved'}}}
  ],
  links: [
    {id: 'native-relation', source: 'R', target: 'D', layer: 'relation', label: 'uses'},
    {id: 'native-retention', source: 'R', target: 'Q', layer: 'required', label: 'Requires retention'}
  ],
  sources: {'specification/PRODUCT.md': {text: 'source', sha256: 'p'}},
  counts: {records: 3, external: 0, relations: 1, required: 1, references: 0}
};
const fixture = JSON.parse(JSON.stringify(native));
const hostile = '<img src=x onerror=boom()>', codePath = 'src/' + hostile + '.py';
const codeRecord = (kind, p) => ({category: 'Graphify structural observation', symbol_kind: kind,
  provenance: {upstream_commit: 'pinned', raw_occurrence: 0},
  grounding: [grounding(p)], raw_extraction_json: '{"confidence":0.125,"label":"' + hostile + '"}'});
fixture.nodes.push(
  {id: 'C', family: 'code', label: 'format_amount', record: codeRecord('function', codePath)},
  {id: 'T', family: 'test', label: 'test_amount', record: codeRecord('function', 'tests/test_amount.py')},
  {id: 'U', family: 'code', label: 'unmapped_helper', record: codeRecord('function', 'src/unmapped.py')},
  {id: 'X', family: 'code_external', label: 'Ambiguous helper', record: {
    category: 'Unresolved Graphify endpoint', reason: 'ambiguous endpoint', alternatives: ['raw:one', 'raw:two']}}
);
const structure = id => ({id, source: 'C', target: 'X', layer: 'structure', label: 'calls', governing: false,
  detail: {standing: 'Graphify observation; fallible', raw_extraction_json: '{"confidence":0.125}', grounding: [grounding(codePath)]}});
const trace = (id, source, target, label) => ({id, source, target, layer: 'trace', label, governing: false,
  detail: {standing: 'Caller-attributed proposal', author: hostile, rationale: 'Proposed correspondence',
    conditions: ['Exact selected source'], limitations: ['Not an executed test'], grounding: [grounding(codePath)]}});
fixture.links.push(structure('call-1'), structure('call-2'), {...structure('call-self'), target: 'C'},
  trace('realization', 'R', 'C', 'Proposed realization'), trace('test-source', 'C', 'T', 'Test source for'));
fixture.sources[codePath] = {text: 'source\n<script>boom()</script>', sha256: 'c'};
fixture.sources['tests/test_amount.py'] = {text: 'source', sha256: 't'};
fixture.sources['src/unmapped.py'] = {text: 'source', sha256: 'u'};
fixture.code_overlay = {
  profile: 'a_c.code-overlay/1', id: 'overlay:example', sha256: 'a'.repeat(64), base_model: fixture.model,
  counts: {nodes: 4, structure_links: 3, trace_links: 2, unresolved_nodes: 1, combined_nodes: 7, combined_links: 7},
  standing: {structure: 'Fallible structural observations', trace: 'Caller-attributed proposals', formal: 'Overlay is not Lean checked'},
  coverage: {source_files: 3, unresolved_mappings: 1}, author: {label: hostile, identity: 'caller-declared'}
};
function html(data) {
  const tokens = {TITLE: 'Code overlay', LAYOUT: 'unified', CSS: fs.readFileSync(path.join(assets, 'explorer.css'), 'utf8'),
    DATA: JSON.stringify(data).replace(/[<>&]/g, c => '\\u' + c.charCodeAt(0).toString(16).padStart(4, '0')),
    VENDOR: fs.readFileSync(path.join(assets, 'layered.js'), 'utf8'),
    APP: fs.readFileSync(path.join(assets, 'explorer.js'), 'utf8'), CREDITS: '', LICENSE: ''};
  return fs.readFileSync(path.join(assets, 'explorer.html'), 'utf8').replace(/@@([A-Z]+)@@/g, (_, key) => tokens[key]);
}
function boot(content) {
  const dom = new JSDOM(content, {runScripts: 'outside-only', pretendToBeVisual: true, url: 'file:///offline/explorer.html'});
  const w = dom.window, d = w.document, $ = id => d.getElementById(id);
  const frames = new Map(); let frame = 0;
  w.matchMedia = q => ({matches: q.includes('min-width: 1301')});
  w.HTMLElement.prototype.scrollIntoView = function(){};
  w.HTMLDialogElement.prototype.showModal = function(){this.open = true;};
  w.HTMLDialogElement.prototype.close = function(){this.open = false;};
  w.requestAnimationFrame = fn => {frames.set(++frame, fn); return frame;};
  w.cancelAnimationFrame = id => frames.delete(id);
  w.ResizeObserver = class {constructor(fn){this.fn = fn;} observe(){this.fn();}};
  Object.defineProperties($('graph'), {clientWidth: {value: 900}, clientHeight: {value: 700}});
  const forbidden = () => {throw Error('Unexpected network/service access');};
  w.fetch = w.XMLHttpRequest = w.WebSocket = w.Worker = forbidden;
  assert.equal(d.querySelectorAll('script[src],link[rel=stylesheet],iframe').length, 0);
  w.eval([...d.scripts].at(-2).textContent);
  const engine = {data: {nodes: [], links: []}, dimensions: 3, settings: {}};
  w.ForceGraph3D = function() {
    const api = new Proxy({}, {get(_, method) {
      if (method === 'd3Force') return () => ({strength(){}});
      if (method === 'graphData') return value => {
        engine.data = value;
        const byId = new Map(value.nodes.map(n => [n.id, n]));
        value.nodes.forEach((n, i) => {n.x = i; n.y = i; if (engine.dimensions === 2) delete n.z; else n.z = 17;});
        value.links.forEach(l => {l.source = byId.get(l.source); l.target = byId.get(l.target);}); return api;
      };
      if (method === 'numDimensions') return value => {engine.dimensions = value; return api;};
      if (method === 'graph2ScreenCoords') return (x, y) => ({x: 200 + x, y: 200 + y});
      return value => {engine.settings[method] = value; return api;};
    }}); return api;
  };
  w.eval([...d.scripts].at(-1).textContent);
  return {dom, w, d, $, engine, data: JSON.parse($('explorer-data').textContent)};
}
function shape(t) {
  return t.d.body.dataset.renderer === 'layered'
    ? {nodes: [...t.d.querySelectorAll('.tracks-node')].map(n => n.dataset.id).sort(), links: [...t.d.querySelectorAll('.tracks-link')].map(l => l.dataset.link).sort()}
    : {nodes: Array.from(t.engine.data.nodes, n => n.id).sort(), links: Array.from(t.engine.data.links, l => l.id).sort()};
}
function state(t) {
  return {hash: t.w.location.hash, reader: t.$('details').innerHTML, trail: t.$('trail').innerHTML,
    scope: t.$('file-scope').innerHTML, origin: t.$('source-origin').innerHTML, results: t.$('results').innerHTML,
    query: t.$('query').value, family: t.$('family').value, counts: t.$('map-count').textContent,
    layers: ['required', 'relation', 'reference', 'structure', 'trace'].map(l => t.$(l + '-layer').checked),
    native: t.$('model-info').textContent, overlay: t.$('code-overlay-about').innerHTML};
}
function modes(t) {
  const before = state(t), geometry = shape(t), reader = t.$('details').firstChild;
  for (const id of ['mode3', 'mode2', 'mode-layered']) {
    t.$(id).click(); assert.deepEqual(state(t), before);
    assert.deepEqual(shape(t), geometry, 'every mode retains exact displayed node and link identities');
    assert.equal(t.$('details').firstChild, reader);
  }
}
function file(t, p) {
  const button = [...t.$('file-tree').querySelectorAll('button')].find(b => b.dataset.path === p);
  assert.ok(button, 'source file available: ' + p); button.click();
}
function selectResult(t, id) {
  while (!t.$('more').hidden) t.$('more').click();
  const button = [...t.$('results').querySelectorAll('button')].find(b => b.dataset.id === id);
  assert.ok(button, 'record available: ' + id); button.click();
}
function follow(t, id) {
  const button = [...t.$('details').querySelectorAll('.connection')].find(b => b.dataset.link === id);
  assert.ok(button, 'connection available: ' + id); button.click();
}
function groundings(value, out = []) {
  if (!value || typeof value !== 'object') return out;
  if (typeof value.path === 'string' && typeof value.quote === 'string') out.push(value);
  Object.values(value).forEach(v => groundings(v, out)); return out;
}
function selectedRecord(t, node) {
  assert.equal(decodeURIComponent(t.w.location.hash.slice(1)), node.id, 'exact selected record identity');
  const heading = t.$('details').querySelector('h2').textContent;
  assert.ok(heading === node.label || (heading.endsWith('…') && heading.length > 1 && node.label.startsWith(heading.slice(0, -1))),
    'heading is the label or its ellipsis-marked prefix; it does not define identity');
  const payload = [...t.$('details').children].find(e => e.tagName === 'DETAILS' &&
    e.querySelector('summary')?.textContent === 'Exact record · identity, owner, scope and all fields');
  assert.ok(payload, 'complete record remains inspectable');
  assert.deepEqual(JSON.parse(payload.querySelector('pre').textContent), node.record, 'complete selected record content is preserved');
}
function journey(t, realization, test) {
  const byId = new Map(t.data.nodes.map(n => [n.id, n]));
  const requirement = byId.get(realization.source), code = byId.get(realization.target);
  const testNode = byId.get(test.target), start = groundings(requirement.record)[0];
  assert.ok(start); file(t, start.path); selectResult(t, requirement.id); selectedRecord(t, requirement); modes(t);
  follow(t, realization.id); selectedRecord(t, code); modes(t);
  follow(t, test.id); assert.equal(t.$('details').querySelector('.badge').textContent, 'Test source');
  selectedRecord(t, testNode);
  assert.match(t.$('details').textContent, /no test execution or result/); modes(t);
  const source = groundings(testNode.record)[0]; assert.ok(source);
  const sourceButton = [...t.$('details').querySelectorAll('.grounding button')].find(b => b.textContent.startsWith(source.path + ':'));
  assert.ok(sourceButton); sourceButton.click();
  assert.equal(t.$('source-dialog').open, true); assert.match(t.$('source-title').textContent, new RegExp(source.path.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));
  assert.ok(t.$('source-text').textContent.includes(source.quote)); t.$('source-close').click();
  t.$('back').click(); selectedRecord(t, code); modes(t);
  t.$('back').click(); selectedRecord(t, requirement);
  t.$('source-origin').querySelector('button').click(); assert.match(t.$('map-count').textContent, /File map/); modes(t);
}
const checks = []; function check(name, action) {action(); checks.push(name);}
check('native exports retain native identity, counts, layers and hidden overlay controls', () => {
  const t = boot(html(native));
  for (const id of ['code-overlay-panel', 'code-overlay-about', 'structure-control', 'trace-control']) assert.equal(t.$(id).hidden, true);
  assert.equal([...t.$('family').options].some(o => ['code', 'test', 'code_external'].includes(o.value)), false);
  assert.match(t.$('map-count').textContent, /3 local records available$/);
  assert.deepEqual(JSON.parse(t.$('model-info').textContent).counts, native.counts); modes(t); t.w.close();
});
check('overlay identity, standing and counts stay separate from the exact native model', () => {
  const t = boot(html(fixture));
  assert.deepEqual(JSON.parse(t.$('model-info').textContent), {model: native.model, calculus: native.basis.calculus, subject: native.basis.subject, counts: native.counts});
  assert.deepEqual(JSON.parse(t.$('code-overlay-about').querySelector('pre').textContent), fixture.code_overlay);
  assert.match(t.$('map-count').textContent, /3 native records.*4 overlay nodes.*7 total nodes available/);
  assert.match(t.$('code-overlay-panel').textContent, /3 selected code\/test files.*1 unresolved mappings/);
  assert.match(t.$('code-overlay-panel').textContent, /no Lean verdict/);
  assert.deepEqual(['code', 'test', 'code_external'].map(v => [...t.$('family').options].find(o => o.value === v).textContent), ['Code', 'Test source', 'Unresolved code reference']);
  t.$('code-overlay-panel').querySelector('button').click(); assert.equal(t.$('about-dialog').open, true); t.w.close();
});
check('Files requirement to code to test source and Back preserves every mode and reading state', () => {
  const t = boot(html(fixture)); journey(t, fixture.links.find(l => l.id === 'realization'), fixture.links.find(l => l.id === 'test-source')); t.w.close();
});
check('structural and proposed links have separate filters, connection groups and inspectable evidence', () => {
  const t = boot(html(fixture)); follow(t, 'realization');
  const section = layer => t.$('details').querySelector('.connection-group[data-layer="' + layer + '"]');
  assert.equal(section('relation'), null); assert.equal(section('required'), null);
  assert.equal(section('structure').querySelectorAll('.connection').length, 3);
  assert.equal(section('trace').querySelectorAll('.connection').length, 2);
  assert.match(section('structure').textContent, /Graphify observation; fallible/);
  assert.match(section('trace').textContent, /Caller-attributed proposal.*Proposed correspondence/s);
  const evidence = section('structure').querySelector('.link-evidence'); evidence.open = true;
  evidence.querySelector('.grounding button').click(); assert.ok(t.$('source-text').textContent.includes('<script>boom()</script>'));
  t.$('source-close').click(); t.$('overview').click();
  for (const layer of ['structure', 'trace']) {
    const expected = fixture.links.filter(l => l.layer !== layer && l.layer !== 'reference').map(l => l.id).sort();
    t.$(layer + '-layer').checked = false; t.$(layer + '-layer').onchange();
    assert.deepEqual(shape(t).links, expected); modes(t);
    t.$(layer + '-layer').checked = true; t.$(layer + '-layer').onchange();
  }
  t.w.close();
});
check('unresolved endpoints and parallel/self observations retain their identities and honest gaps', () => {
  const t = boot(html(fixture)); follow(t, 'realization');
  const links = [...t.d.querySelectorAll('.tracks-link[data-layer=structure]')];
  assert.deepEqual(links.map(l => l.dataset.link).sort(), ['call-1', 'call-2', 'call-self']);
  assert.equal(new Set(links.map(l => l.querySelector('.tracks-line').getAttribute('d'))).size, 3);
  links.forEach(l => assert.match(l.getAttribute('aria-label'), /^Code observation:/));
  assert.match(t.d.querySelector('.tracks-link[data-layer=trace]').getAttribute('aria-label'), /^Proposed trace:/);
  follow(t, 'call-1'); assert.match(t.$('details').textContent, /Unresolved code reference.*No unique local endpoint/s);
  assert.match(t.$('details').textContent, /raw:one.*raw:two/s); modes(t);
  file(t, 'src/unmapped.py'); selectResult(t, 'U');
  assert.match(t.$('details').textContent, /No test-source mapping.*does not mean the project has no tests/s); t.w.close();
});
check('source, attribution and float-bearing raw observation strings remain literal text', () => {
  const t = boot(html(fixture)); follow(t, 'realization');
  assert.ok(t.$('details').textContent.includes(hostile));
  assert.ok(t.$('details').textContent.includes('"confidence":0.125'));
  assert.equal(t.$('details').querySelectorAll('img,script').length, 0);
  assert.equal(t.$('file-tree').querySelectorAll('img,script').length, 0);
  t.$('mode3').click();
  const observation = fixture.links.find(l => l.layer === 'structure'), proposal = fixture.links.find(l => l.layer === 'trace');
  assert.match(t.engine.settings.linkLabel(observation).textContent, /^Code observation:/);
  assert.match(t.engine.settings.linkLabel(proposal).textContent, /^Proposed trace:/);
  assert.notEqual(t.engine.settings.linkColor(observation), t.engine.settings.linkColor(proposal)); t.w.close();
});
if (process.argv[2]) check('generated real overlay carries exact identity and traversable requirement/code/test in every mode', () => {
  const t = boot(fs.readFileSync(process.argv[2], 'utf8'));
  const realization = t.data.links.find(l => l.layer === 'trace' && l.label === 'Proposed realization' &&
    t.data.links.some(test => test.layer === 'trace' && test.label === 'Test source for' && test.source === l.target));
  assert.ok(realization, 'generated artifact needs one demonstrated requirement/code/test chain');
  const test = t.data.links.find(l => l.layer === 'trace' && l.label === 'Test source for' && l.source === realization.target);
  assert.deepEqual(JSON.parse(t.$('code-overlay-about').querySelector('pre').textContent), t.data.code_overlay);
  assert.deepEqual(JSON.parse(t.$('model-info').textContent).counts, t.data.counts);
  assert.deepEqual(JSON.parse(t.$('model-info').textContent).model, t.data.model);
  journey(t, realization, test);
  // Native external references are intentionally hidden by the default layer
  // filter. Enable that layer before asking for the complete available graph.
  t.$('reference-layer').checked = true; t.$('reference-layer').onchange(); t.$('overview').click();
  assert.deepEqual(shape(t).nodes, t.data.nodes.map(n => n.id).sort());
  assert.deepEqual(shape(t).links, t.data.links.map(l => l.id).sort());
  modes(t); t.w.close();
});
console.log(JSON.stringify({status: 'passed', checks,
  limits: 'Actual shared reader and layered adapter with a stubbed force transport. No browser/WebGL visual, camera, semantic, code-correctness or test-result qualification.'}, null, 2));
