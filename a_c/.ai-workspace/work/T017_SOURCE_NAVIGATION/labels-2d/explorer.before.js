'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const el = (tag, text, className) => {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  };
  // Preserve integer JSON values beyond Number.MAX_SAFE_INTEGER in the reader.
  function parseExact(text) {
    let pos = 0;
    const token = /\s*("(?:\\.|[^"\\])*"|true|false|null|-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[{}\[\],:])/y;
    function take() {
      token.lastIndex = pos;
      const match = token.exec(text);
      if (!match) throw new Error('Invalid embedded JSON at ' + pos);
      pos = token.lastIndex;
      return match[1];
    }
    function value(t = take()) {
      if (t === '{') {
        const result = Object.create(null);
        let key = take();
        if (key === '}') return result;
        while (true) {
          if (key[0] !== '"' || take() !== ':') throw new Error('Invalid object');
          result[JSON.parse(key)] = value();
          const sep = take();
          if (sep === '}') return result;
          if (sep !== ',') throw new Error('Invalid object separator');
          key = take();
        }
      }
      if (t === '[') {
        const result = [];
        let next = take();
        if (next === ']') return result;
        while (true) {
          result.push(value(next));
          const sep = take();
          if (sep === ']') return result;
          if (sep !== ',') throw new Error('Invalid array separator');
          next = take();
        }
      }
      if (t[0] === '"') return JSON.parse(t);
      if (t === 'true') return true;
      if (t === 'false') return false;
      if (t === 'null') return null;
      if (!/^-?\d+$/.test(t)) throw new Error('Only integer semantic values are supported');
      const n = BigInt(t);
      return n <= BigInt(Number.MAX_SAFE_INTEGER) && n >= BigInt(Number.MIN_SAFE_INTEGER) ? Number(n) : n;
    }
    const result = value();
    if (text.slice(pos).trim()) throw new Error('Trailing embedded JSON');
    return result;
  }
  function exactJSON(value, depth = 0) {
    if (typeof value === 'bigint') return String(value);
    if (value === null || typeof value !== 'object') return JSON.stringify(value);
    const pad = '  '.repeat(depth), inner = pad + '  ';
    const entries = Array.isArray(value)
      ? value.map(v => exactJSON(v, depth + 1))
      : Object.entries(value).map(([k, v]) => JSON.stringify(k) + ': ' + exactJSON(v, depth + 1));
    const [open, close] = Array.isArray(value) ? ['[', ']'] : ['{', '}'];
    return entries.length ? open + '\n' + inner + entries.join(',\n' + inner) + '\n' + pad + close : open + close;
  }
  const data = parseExact($('explorer-data').textContent);
  const nodes = new Map(data.nodes.map(n => [n.id, n]));
  const colors = {constraints: '#e7bd84', objects: '#8dc9dc', relations: '#bba4e6', residuals: '#e2949c', latitude: '#a9ce8b', traversals: '#70c8b2', transformations: '#dfbdde', judgments: '#91ace9', external: '#718290'};
  const names = {constraints: 'Constraint', objects: 'Concept', relations: 'Relation', residuals: 'Caveat', latitude: 'Latitude', traversals: 'Traversal', transformations: 'Transformation', judgments: 'Judgment', external: 'External reference'};
  const short = (s, n = 100) => s.length > n ? s.slice(0, n - 1) + '…' : s;
  const prettyKey = s => s.replace(/_/g, ' ').replace(/^./, c => c.toUpperCase());
  const neighbours = new Map(data.nodes.map(n => [n.id, []]));
  for (const link of data.links) {
    neighbours.get(link.source)?.push(link);
    if (link.target !== link.source) neighbours.get(link.target)?.push(link);
  }
  let selected = null, trail = [], visible = new Set(), graph = null, limit = 50, overview = false;
  let dimensions = 3, autoFit = false;
  let labels = [];
  let activeFile = null, fileMapView = null;
  const sourceFiles = new Map(Object.keys(data.sources).map(path => [path, new Map()]));
  const recordFiles = new Map(), expandedFolders = new Set();
  for (const node of data.nodes) {
    const files = new Map();
    for (const g of getGroundings(node.record)) {
      if (!sourceFiles.has(g.path)) sourceFiles.set(g.path, new Map());
      const firstLine = files.get(g.path);
      files.set(g.path, firstLine === undefined ? g.start_line : Math.min(firstLine, g.start_line));
    }
    recordFiles.set(node.id, files);
    for (const [path, line] of files) sourceFiles.get(path).set(node.id, line);
  }
  const graphNodes = new Map(data.nodes.map(n => [n.id, {id: n.id, family: n.family, label: n.label}]));
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function enabled(link) { return $(link.layer + '-layer').checked; }
  function other(link, id) { return link.source === id ? link.target : link.source; }
  function connected(id) { return (neighbours.get(id) || []).filter(enabled); }

  function refreshSearch() {
    const q = $('query').value.toLocaleLowerCase().trim();
    const family = $('family').value;
    const matches = data.nodes.filter(n => (!activeFile || sourceFiles.get(activeFile).has(n.id)) &&
      (!family || n.family === family) && n.search.includes(q));
    if (activeFile) matches.sort((a, b) => sourceFiles.get(activeFile).get(a.id) - sourceFiles.get(activeFile).get(b.id));
    $('matches').textContent = matches.length + ' matches · showing ' + Math.min(limit, matches.length);
    $('results').replaceChildren();
    for (const node of matches.slice(0, limit)) {
      const button = el('button');
      button.dataset.id = node.id;
      button.style.setProperty('--family', colors[node.family]);
      button.setAttribute('aria-current', String(node.id === selected));
      button.append(el('span', node.label, 'result-label'), el('small', names[node.family]));
      button.onclick = () => select(node.id);
      $('results').append(button);
    }
    $('more').hidden = matches.length <= limit;
    if (!matches.length) $('results').append(el('p', activeFile
      ? 'No records match this file and the current filters. Try All records or clear the search.'
      : 'No records match the current filters.', 'muted'));
  }
  for (const node of data.nodes) node.search = exactJSON(node.record).toLocaleLowerCase();
  $('total').textContent = data.nodes.filter(n => n.family === 'constraints').length;
  for (const family of Object.keys(colors)) {
    if (family !== 'constraints' && data.nodes.some(n => n.family === family)) {
      const option = el('option', family === 'external' ? 'External references' : prettyKey(family));
      option.value = family;
      $('family').append(option);
    }
    if (data.nodes.some(n => n.family === family)) {
      const label = el('span'), dot = el('span', '', 'dot');
      dot.style.background = colors[family];
      label.append(dot, document.createTextNode(names[family]));
      $('legend').append(label);
    }
  }
  $('query').oninput = $('family').onchange = () => { limit = 50; refreshSearch(); };
  $('more').onclick = () => { limit += 50; refreshSearch(); };

  function toggleFiles(open) {
    $('files-pane').hidden = !open;
    $('files-toggle').setAttribute('aria-expanded', String(open));
  }
  function expandParents(path) {
    const parts = path.split('/');
    for (let i = 1; i < parts.length; i++) expandedFolders.add(parts.slice(0, i).join('/'));
  }
  function renderFiles(reveal = false) {
    const query = $('file-query').value.trim().toLocaleLowerCase();
    const paths = [...sourceFiles.keys()].sort((a, b) => a.localeCompare(b));
    const matches = paths.filter(path => path.toLocaleLowerCase().includes(query));
    $('file-count').textContent = (query ? matches.length + ' of ' : '') + paths.length + ' files';
    const tree = {folders: new Map(), files: []};
    for (const path of matches) {
      const parts = path.split('/');
      let branch = tree;
      parts.slice(0, -1).forEach((name, index) => {
        if (!branch.folders.has(name)) branch.folders.set(name, {path: parts.slice(0, index + 1).join('/'), folders: new Map(), files: []});
        branch = branch.folders.get(name);
      });
      branch.files.push({path, name: parts[parts.length - 1]});
    }
    function appendTree(branch, target) {
      for (const [name, folder] of branch.folders) {
        const details = el('details'), summary = el('summary'), children = el('div', undefined, 'folder-children');
        summary.append(el('span', name, 'folder-name'));
        details.open = !!query || expandedFolders.has(folder.path);
        details.dataset.folder = folder.path;
        details.ontoggle = () => {
          if (!query) details.open ? expandedFolders.add(folder.path) : expandedFolders.delete(folder.path);
        };
        appendTree(folder, children); details.append(summary, children); target.append(details);
      }
      for (const {path, name} of branch.files) {
        const button = el('button', undefined, 'file-entry');
        const count = sourceFiles.get(path).size;
        button.dataset.path = path; button.title = path + (data.sources[path] ? '' : ' · source not embedded');
        button.setAttribute('aria-current', String(path === activeFile));
        button.append(el('span', name, 'file-name'), el('small', String(count)));
        button.setAttribute('aria-label', path + ' · ' + count + ' records' + (data.sources[path] ? '' : ' · source not embedded'));
        button.onclick = () => chooseFile(path);
        target.append(button);
      }
    }
    $('file-tree').replaceChildren(); appendTree(tree, $('file-tree'));
    if (!matches.length) $('file-tree').append(el('p', 'No files match this path.', 'muted'));
    if (reveal) $('file-tree').querySelector('[aria-current="true"]')?.scrollIntoView({block: 'nearest'});
  }
  function renderFileScope() {
    const scope = $('file-scope'), origin = $('source-origin');
    scope.hidden = origin.hidden = !activeFile;
    scope.replaceChildren(); origin.replaceChildren();
    $('library-title').textContent = activeFile ? 'Records in this file' : 'Find a constraint';
    $('total').textContent = activeFile ? sourceFiles.get(activeFile).size : data.nodes.filter(n => n.family === 'constraints').length;
    if (!activeFile) return;
    const count = sourceFiles.get(activeFile).size;
    scope.append(el('p', activeFile, 'file-path'), el('p', count + ' grounded records across all families', 'muted'));
    const actions = el('div', undefined, 'file-scope-actions');
    const read = el('button', 'Read file');
    read.disabled = !data.sources[activeFile];
    read.onclick = () => openSource({path: activeFile});
    const map = el('button', 'File map'); map.disabled = !count;
    map.onclick = () => showFileMap(activeFile);
    const clear = el('button', 'All files'); clear.onclick = clearFile;
    actions.append(read, map, clear); scope.append(actions);
    if (!data.sources[activeFile]) scope.append(el('p', 'Full source is not embedded. Recorded quotations remain available.', 'muted'));
    origin.append(el('span', 'Document navigation', 'origin-label'));
    const back = el('button', 'Back to file · ' + activeFile);
    back.onclick = () => chooseFile(activeFile);
    origin.append(back);
  }
  function chooseFile(path, revealOnly = false) {
    if (!sourceFiles.has(path)) return;
    activeFile = path; limit = 50;
    $('query').value = ''; $('family').value = ''; $('file-query').value = '';
    if (revealOnly) toggleFiles(true);
    expandParents(path); renderFileScope(); refreshSearch(); renderFiles(true);
    if (!revealOnly) {
      showFileMap(path);
      // On a narrow screen the flyout overlays the record list: expose that list.
      if (matchMedia('(max-width: 1300px)').matches) toggleFiles(false);
      $('query').focus();
    }
  }
  function clearFile() {
    activeFile = null; fileMapView = null; limit = 50;
    renderFileScope(); refreshSearch(); renderFiles();
    if (selected) { overview = false; focusGraph(); }
  }
  function showFileMap(path) {
    fileMapView = path; overview = false;
    visible = new Set(sourceFiles.get(path).keys()); drawGraph();
  }
  $('files-toggle').onclick = () => toggleFiles($('files-pane').hidden);
  $('files-close').onclick = () => { toggleFiles(false); $('files-toggle').focus(); };
  $('file-query').oninput = () => renderFiles();
  $('folders-collapse').onclick = () => { expandedFolders.clear(); $('file-query').value = ''; renderFiles(); };
  $('files-pane').onkeydown = event => {
    if (event.key === 'Escape') { toggleFiles(false); $('files-toggle').focus(); }
  };
  for (const path of sourceFiles.keys()) {
    if (path.includes('/')) expandedFolders.add(path.split('/')[0]);
  }
  renderFiles();
  toggleFiles(matchMedia('(min-width: 1301px)').matches);

  function edgeDescription(link, from) {
    const dir = link.source === from ? '→ ' : '← ';
    if (link.layer === 'required') return dir + (link.source === from ? 'Requires retention' : 'Required by');
    return dir + (link.layer === 'relation' ? 'Authored: ' : 'Reference: ') + link.label;
  }
  function select(id, via = null) {
    if (!nodes.has(id)) return;
    if (id !== selected || via) {
      if (!via) trail = [];
      trail.push({id, via});
    }
    selected = id;
    fileMapView = null;
    location.hash = encodeURIComponent(id);
    overview = false;
    focusGraph();
    renderReader(); renderTrail(); refreshSearch();
    document.querySelector('.reading-pane').scrollTop = 0;
  }
  function follow(link) {
    select(other(link, selected), {label: edgeDescription(link, selected), edge_id: link.id,
      from: selected, to: other(link, selected)});
  }
  function renderTrail() {
    $('trail').replaceChildren();
    trail.forEach((step, index) => {
      const button = el('button');
      button.append(el('span', (index + 1) + '. ' + short(nodes.get(step.id).label, 65)));
      if (step.via) {
        button.append(el('span', typeof step.via === 'string' ? step.via : step.via.label, 'trail-link'));
        if (step.via.edge_id) {
          button.dataset.edgeId = step.via.edge_id;
          button.title = exactJSON(step.via);
          button.append(el('span', short(step.via.edge_id, 80), 'trail-link'));
        }
      }
      button.onclick = () => {
        trail = trail.slice(0, index + 1); selected = step.id;
        location.hash = encodeURIComponent(selected); overview = false; fileMapView = null;
        focusGraph(); renderReader(); renderTrail(); refreshSearch();
      };
      $('trail').append(button);
    });
    $('back').disabled = trail.length < 2;
  }
  $('back').onclick = () => { if (trail.length > 1) $('trail').children[trail.length - 2].click(); };

  function renderValue(value, path = []) {
    if (value === null) return el('span', 'None', 'muted');
    if (Array.isArray(value)) {
      if (!value.length) return el('span', 'None declared', 'muted');
      const list = el('ul');
      value.forEach((v, index) => { const li = el('li'); li.append(renderValue(v, [...path, String(index)])); list.append(li); });
      return list;
    }
    if (typeof value === 'object') {
      const box = el('div', undefined, 'record-field');
      const first = ['label', 'statement', 'definition', 'meaning', 'conditions', 'exceptions', 'uncertainty'];
      const keys = [...first.filter(k => Object.hasOwn(value, k)), ...Object.keys(value).filter(k => !first.includes(k))];
      for (const key of keys) {
        const val = value[key];
        if (key === 'grounding') continue;
        box.append(el('h4', prettyKey(key)), renderValue(val, [...path, key]));
      }
      return box;
    }
    const reference = typeof value === 'string' && (neighbours.get(selected) || []).find(l =>
      l.layer === 'reference' && l.source === selected && l.target === value &&
      l.path.length === path.length && l.path.every((p, i) => p === path[i]));
    if (reference && nodes.has(value)) {
      const button = el('button', nodes.get(value).label, 'identity-button');
      button.title = value;
      button.onclick = () => follow(reference);
      return button;
    }
    return el('div', value === '' ? 'None declared' : String(value), 'statement');
  }
  function getGroundings(value, out = []) {
    if (!value || typeof value !== 'object') return out;
    if (typeof value.path === 'string' && typeof value.quote === 'string' && Number.isInteger(value.start_line) && Number.isInteger(value.end_line)) out.push(value);
    Object.values(value).forEach(v => getGroundings(v, out));
    return out;
  }
  function openSource(g) {
    const source = data.sources[g.path];
    if (!source) return;
    $('source-title').textContent = g.path + (g.start_line ? ':' + g.start_line + '–' + g.end_line : '');
    $('source-digest').textContent = 'Embedded file SHA-256: ' + source.sha256;
    $('source-text').replaceChildren();
    source.text.split('\n').forEach((line, i) => {
      const row = el('span', String(i + 1).padStart(4, ' ') + '  ' + line);
      if (i + 1 >= g.start_line && i + 1 <= g.end_line) row.className = 'selected-line';
      $('source-text').append(row);
    });
    $('source-dialog').showModal();
    $('source-text').scrollTop = 0;
    $('source-text').querySelector('.selected-line')?.scrollIntoView({block: 'center'});
  }
  function addConnections(parent, title, links) {
    if (!links.length) return;
    const section = el('section', undefined, 'connection-group');
    section.append(el('h3', title + ' · ' + links.length));
    for (const link of links) {
      const target = nodes.get(other(link, selected));
      if (!target) continue;
      const button = el('button', undefined, 'connection');
      button.dataset.link = link.id;
      button.append(el('small', edgeDescription(link, selected)), el('span', target.label, 'target-label'));
      if (link.reasons) button.append(el('span', link.reasons.map(r => r.label + (r.path ? ' · ' + r.path.join('/') : '')).join('; '), 'edge-detail'));
      button.onclick = () => follow(link);
      section.append(button);
      if (link.record_id) {
        const inspect = el('button', 'Read relation and qualifications', 'source-link');
        inspect.onclick = () => select(link.record_id, 'Inspect authored relation record');
        section.append(inspect);
      }
    }
    parent.append(section);
  }
  function renderReader() {
    const node = nodes.get(selected), record = node.record, pane = $('details');
    pane.replaceChildren();
    const badge = el('span', names[node.family], 'badge');
    badge.style.setProperty('--family', colors[node.family]);
    pane.append(badge, el('h2', short(node.label, 105)));
    const files = recordFiles.get(node.id);
    if (files.size) {
      const sources = el('section', undefined, 'record-sources');
      sources.append(el('h3', 'Source documents'));
      for (const [path, line] of files) {
        const row = el('div', undefined, 'record-source');
        const reveal = el('button', 'Show in files');
        reveal.setAttribute('aria-label', 'Show in files · ' + path);
        reveal.onclick = () => chooseFile(path, true);
        row.append(el('span', path + ':' + line, 'source-path'), reveal); sources.append(row);
      }
      pane.append(sources);
    }
    const contentKeys = {
      constraints: ['predicate', 'applies_to', 'latitude_ref', 'refusal'], objects: ['value'],
      relations: ['kind', 'source', 'target', 'qualifiers'],
      residuals: ['uncertainty', 'consequence', 'subject', 're_entry', 'invalidation'],
      latitude: ['applies_to', 'allowed_variation', 'forbidden_variation', 'invalidation']
    }[node.family] || Object.keys(record).filter(k => !['id', 'context', 'owner', 'scope', 'basis'].includes(k));
    for (const key of contentKeys) {
      if (record[key] === undefined) continue;
      const section = el('section', undefined, 'record-field');
      section.append(el('h3', key === 'predicate' ? 'Constraint' : prettyKey(key)), renderValue(record[key], [key]));
      pane.append(section);
    }
    const links = neighbours.get(selected) || [];
    addConnections(pane, 'Authored relationships', links.filter(l => l.layer === 'relation'));
    addConnections(pane, 'Must retain with this record', links.filter(l => l.layer === 'required' && l.source === selected));
    addConnections(pane, 'Required by', links.filter(l => l.layer === 'required' && l.target === selected && l.source !== selected));
    const refs = el('details');
    refs.append(el('summary', 'Other typed reference occurrences'));
    addConnections(refs, 'References', links.filter(l => l.layer === 'reference'));
    pane.append(refs);
    const gs = getGroundings(record), seen = new Set();
    pane.append(el('h3', 'Recorded source quotations'));
    if (!gs.length) pane.append(el('p', 'No inline grounding quotation is recorded for this record. Follow its references or inspect the exact payload.', 'muted'));
    for (const g of gs) {
      const key = exactJSON(g);
      if (seen.has(key)) continue;
      seen.add(key);
      const box = el('section', undefined, 'grounding');
      const source = data.sources[g.path];
      if (source) {
        const button = el('button', g.path + ':' + g.start_line + '–' + g.end_line, 'source-link');
        button.onclick = () => openSource(g); box.append(button);
        const span = source.text.split('\n').slice(g.start_line - 1, g.end_line).join('\n');
        const matches = span.replace(/\r/g, '').includes(g.quote.replace(/\r/g, '').trim());
        box.append(el('p', matches ? 'Recorded excerpt occurs in the supplied source lines.' : 'Recorded excerpt does not occur verbatim in these source lines. Open the source to compare.', matches ? 'source-status' : 'source-status warning'));
      } else box.append(el('p', g.path + ':' + g.start_line + '–' + g.end_line + ' · full source not embedded', 'muted'));
      box.append(el('blockquote', g.quote)); pane.append(box);
    }
    const raw = el('details');
    raw.append(el('summary', 'Exact record · identity, owner, scope and all fields'), el('pre', exactJSON(record)));
    pane.append(raw);
  }

  function focusGraph() {
    visible = new Set([selected]);
    for (const link of connected(selected)) visible.add(other(link, selected));
    const firstHop = [...visible];
    for (const id of firstHop) for (const link of connected(id)) visible.add(other(link, id));
    drawGraph();
  }
  function drawGraph() {
    const links = data.links.filter(l => enabled(l) && visible.has(l.source) && visible.has(l.target));
    $('map-count').textContent = (fileMapView ? 'File map · ' + fileMapView + ' · ' : '') + visible.size + ' visible nodes · ' + links.length + ' visible links · ' + data.counts.records + ' local records available';
    if (!graph) return;
    const parallel = new Map();
    const renderedLinks = links.map(link => {
      const key = [link.source, link.target].sort().join('\n');
      const index = parallel.get(key) || 0; parallel.set(key, index + 1);
      return {...link, curve: link.source === link.target ? 0.8 : index ? Math.min(0.15 * index, 0.7) : 0};
    });
    autoFit = true;
    graph.graphData({nodes: [...visible].filter(id => graphNodes.has(id)).map(id => graphNodes.get(id)), links: renderedLinks});
    graph.nodeColor(n => n.id === selected ? '#f4ffe9' : colors[n.family]);
    $('node-labels').replaceChildren();
    labels = [...visible].filter(id => visible.size <= 25 || id === selected).map(id => {
      const label = el('span', short(nodes.get(id).label, 55), 'map-label');
      if (id === selected) label.classList.add('selected');
      $('node-labels').append(label);
      return {id, label};
    });
  }
  function initializeGraph() {
    try {
      graph = new ForceGraph3D($('graph'), {controlType: 'orbit'})
        .enableNodeDrag(false)
        .backgroundColor('#10171e').showNavInfo(false).nodeRelSize(3).nodeOpacity(0.95)
        .nodeVal(n => n.id === selected ? 3 : n.family === 'constraints' ? 1.5 : 1)
        .nodeLabel(n => el('div', names[n.family] + ' · ' + short(n.label, 350), 'graph-tooltip'))
        .linkLabel(l => el('div', (l.layer === 'required' ? 'Retention dependency' : l.layer === 'relation' ? 'Authored relation' : 'Typed reference') + ': ' + l.label, 'graph-tooltip'))
        .linkColor(l => l.layer === 'relation' ? '#b8a0e0' : l.layer === 'required' ? '#779a9c' : '#455669')
        .linkOpacity(0.65).linkWidth(l => l.layer === 'relation' ? 1.3 : 0.6)
        .linkCurvature('curve').linkDirectionalArrowLength(3).linkDirectionalArrowRelPos(0.8)
        .cooldownTicks(80).d3VelocityDecay(0.35)
        .onNodeClick(n => {
          const links = connected(selected).filter(l => other(l, selected) === n.id);
          if (links.length === 1) follow(links[0]); else select(n.id);
        })
        .onLinkClick(link => {
          if (link.record_id) select(link.record_id, 'Inspect authored relation record');
          else if (link.source.id === selected || link.target.id === selected) {
            follow(data.links.find(l => l.id === link.id));
          }
        })
        .onEngineStop(() => { if (autoFit) { autoFit = false; graph.zoomToFit(reducedMotion ? 0 : 350, 85); } });
      graph.d3Force('charge').strength(-130);
      const resize = () => graph.width($('graph').clientWidth).height($('graph').clientHeight);
      new ResizeObserver(resize).observe($('graph')); resize();
      const fallback = $('graph-fallback'); if (fallback) fallback.remove();
    } catch (error) {
      graph = null;
      $('graph').replaceChildren(el('p', '3D rendering is unavailable in this browser. Search, constraint reading, sources and the navigation trail remain available.', 'muted'));
      $('graph').style.padding = '140px 24px';
      for (const id of ['mode2', 'mode3', 'fit']) $(id).disabled = true;
    }
  }
  function mode(n) {
    dimensions = n;
    $('mode3').setAttribute('aria-pressed', String(n === 3));
    $('mode2').setAttribute('aria-pressed', String(n === 2));
    if (graph) { graph.numDimensions(n); autoFit = true; }
  }
  $('mode3').onclick = () => mode(3); $('mode2').onclick = () => mode(2);
  $('focus').onclick = () => { overview = false; fileMapView = null; focusGraph(); };
  $('expand').onclick = () => {
    fileMapView = null;
    const next = new Set(visible);
    for (const id of visible) for (const link of connected(id)) next.add(other(link, id));
    visible = next; drawGraph();
  };
  function showOverview() {
    visible = new Set(data.nodes.filter(n => n.family !== 'external' || $('reference-layer').checked).map(n => n.id));
    // Authored relations may have an external endpoint even with reference links hidden.
    for (const link of data.links.filter(enabled)) { visible.add(link.source); visible.add(link.target); }
    drawGraph();
  }
  $('overview').onclick = () => { overview = true; fileMapView = null; showOverview(); };
  $('fit').onclick = () => graph?.zoomToFit(reducedMotion ? 0 : 350, 85);
  for (const id of ['required-layer', 'relation-layer', 'reference-layer']) $(id).onchange = () => fileMapView ? showFileMap(fileMapView) : overview ? showOverview() : focusGraph();
  $('source-close').onclick = () => $('source-dialog').close();
  $('about-close').onclick = () => $('about-dialog').close();
  $('about-button').onclick = () => $('about-dialog').showModal();
  $('subject-basis').textContent = 'Subject: ' + data.basis.subject.id;
  $('subject-basis').title = data.basis.subject.id;
  $('model-info').textContent = exactJSON({model: data.model, calculus: data.basis.calculus,
    subject: {id: data.basis.subject.id, sha256: data.basis.subject.sha256}, counts: data.counts});
  window.addEventListener('hashchange', () => {
    let id; try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    if (nodes.has(id) && id !== selected) select(id);
  });
  document.addEventListener('visibilitychange', () => {
    if (graph) document.hidden ? graph.pauseAnimation() : graph.resumeAnimation();
  });
  initializeGraph();
  let lastLabelFrame = 0;
  function positionLabels(time) {
    if (graph && !document.hidden && time - lastLabelFrame > 60) {
      lastLabelFrame = time;
      for (const {id, label} of labels) {
        const n = graphNodes.get(id);
        if (![n.x, n.y, n.z].every(Number.isFinite)) { label.hidden = true; continue; }
        const p = graph.graph2ScreenCoords(n.x, n.y, n.z);
        label.hidden = p.x < 10 || p.x > $('graph').clientWidth - 10 || p.y < 100 || p.y > $('graph').clientHeight - 130;
        label.style.transform = `translate(${p.x}px,${p.y + 12}px) translateX(-50%)`;
      }
    }
    requestAnimationFrame(positionLabels);
  }
  requestAnimationFrame(positionLabels);
  let initial; try { initial = decodeURIComponent(location.hash.slice(1)); } catch (_) {}
  select(nodes.has(initial) ? initial : data.focus);
})();
