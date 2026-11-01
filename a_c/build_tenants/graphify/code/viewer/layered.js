'use strict';
// Standalone presentation adapter. The component-ranking strategy follows
// odd_manager/visual-graph/layout.ts; no manager/runtime dependency is imported.
// Input records and links are never changed, and layout adds no semantic edges.
globalThis.ACTracks = (() => {
  const width = 240, height = 112, columnGap = 146, rowGap = 70;
  const compare = (a, b) => a < b ? -1 : a > b ? 1 : 0;

  function layout(nodes, links) {
    const byId = new Map(nodes.map(node => [node.id, node]));
    const order = (a, b) => compare(byId.get(a).family, byId.get(b).family)
      || compare(byId.get(a).label, byId.get(b).label) || compare(a, b);
    const ids = [...byId.keys()].sort(order);
    const edges = links.filter(link => byId.has(link.source) && byId.has(link.target));
    const outgoing = new Map(ids.map(id => [id, new Set()]));
    const incoming = new Map(ids.map(id => [id, new Set()]));
    const parallel = new Map();
    for (const link of edges) {
      outgoing.get(link.source).add(link.target);
      incoming.get(link.target).add(link.source);
      const key = JSON.stringify([link.source, link.target]);
      if (!parallel.has(key)) parallel.set(key, []);
      parallel.get(key).push(link.id);
    }
    for (const group of parallel.values()) group.sort(compare);
    const padding = 72 + Math.max(1, ...[...parallel.values()].map(group => group.length)) * 14;

    // Iterative Kosaraju: exact SCCs, without a recursion-depth dependency.
    const visited = new Set(), finish = [];
    for (const id of ids) {
      if (visited.has(id)) continue;
      const stack = [[id, false]];
      while (stack.length) {
        const [current, exiting] = stack.pop();
        if (exiting) { finish.push(current); continue; }
        if (visited.has(current)) continue;
        visited.add(current); stack.push([current, true]);
        for (const target of [...outgoing.get(current)].sort(order).reverse()) {
          if (!visited.has(target)) stack.push([target, false]);
        }
      }
    }
    const components = [], componentOf = new Map();
    for (const id of finish.reverse()) {
      if (componentOf.has(id)) continue;
      const index = components.length, members = [], stack = [id];
      componentOf.set(id, index);
      while (stack.length) {
        const current = stack.pop(); members.push(current);
        for (const source of incoming.get(current)) {
          if (!componentOf.has(source)) { componentOf.set(source, index); stack.push(source); }
        }
      }
      components.push(members.sort(order));
    }
    const spans = components.map(group => Math.ceil(Math.sqrt(group.length)));
    const depth = components.map(() => 0), indegree = components.map(() => 0);
    const next = components.map(() => new Set());
    for (const edge of edges) {
      const a = componentOf.get(edge.source), b = componentOf.get(edge.target);
      if (a !== b && !next[a].has(b)) { next[a].add(b); indegree[b]++; }
    }
    const componentOrder = (a, b) => order(components[a][0], components[b][0]);
    const queue = components.map((_, i) => i).filter(i => !indegree[i]).sort(componentOrder);
    while (queue.length) {
      const current = queue.shift();
      for (const target of [...next[current]].sort(componentOrder)) {
        depth[target] = Math.max(depth[target], depth[current] + spans[current]);
        if (--indegree[target] === 0) { queue.push(target); queue.sort(componentOrder); }
      }
    }
    const columns = new Map();
    components.forEach((members, component) => members.forEach((id, offset) => {
      const column = depth[component] + offset % spans[component];
      if (!columns.has(column)) columns.set(column, []);
      columns.get(column).push(id);
    }));
    const positioned = [];
    for (const [column, members] of [...columns].sort(([a], [b]) => a - b)) {
      members.sort(order).forEach((id, row) => positioned.push({
        node: byId.get(id), column, row, width, height,
        x: padding + column * (width + columnGap), y: padding + row * (height + rowGap),
        cycle: components[componentOf.get(id)].length > 1 || outgoing.get(id).has(id)
      }));
    }
    const positions = new Map(positioned.map(item => [item.node.id, item]));
    const routed = edges.map(link => {
      const source = positions.get(link.source), target = positions.get(link.target);
      const group = parallel.get(JSON.stringify([link.source, link.target]));
      const index = group.indexOf(link.id);
      const sx = source.x + width, sy = source.y + height / 2;
      const tx = target.x, ty = target.y + height / 2;
      let path, labelX, labelY;
      if (link.source === link.target) {
        const reach = 48 + index * 18;
        path = `M ${sx} ${sy - 24} C ${sx + reach} ${sy - 64}, ${sx + reach} ${sy + 64}, ${sx} ${sy + 24}`;
        labelX = sx + reach * 0.75; labelY = sy;
      } else if (tx <= sx) {
        const rail = Math.min(source.y, target.y) - 28 - index * 14;
        path = `M ${sx} ${sy} C ${sx + 32} ${sy}, ${sx + 32} ${rail}, ${sx} ${rail} L ${tx} ${rail} C ${tx - 32} ${rail}, ${tx - 32} ${ty}, ${tx} ${ty}`;
        labelX = (sx + tx) / 2; labelY = rail - 6;
      } else {
        const control = Math.max(40, (tx - sx) * 0.42);
        const offset = (index - (group.length - 1) / 2) * 22;
        path = `M ${sx} ${sy} C ${sx + control} ${sy + offset}, ${tx - control} ${ty + offset}, ${tx} ${ty}`;
        labelX = (sx + tx) / 2; labelY = (sy + ty) / 2 + offset * 0.75 - 7;
      }
      return {link, path, labelX, labelY};
    });
    return {nodes: positioned, edges: routed,
      width: Math.max(0, ...positioned.map(n => n.x + width)) + padding,
      height: Math.max(0, ...positioned.map(n => n.y + height)) + padding};
  }

  function create(container, {colors, names, onNode, onLink, onZoom}) {
    const html = (tag, text, cls) => {
      const node = document.createElement(tag);
      if (text !== undefined) node.textContent = text;
      if (cls) node.className = cls;
      return node;
    };
    const svg = (tag, attrs = {}) => {
      const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
      for (const [name, value] of Object.entries(attrs)) node.setAttribute(name, value);
      return node;
    };
    const viewport = html('div', undefined, 'tracks-viewport');
    viewport.tabIndex = 0; viewport.setAttribute('aria-label', 'Scrollable layered graph');
    const extent = html('div', undefined, 'tracks-extent'), canvas = html('div', undefined, 'tracks-canvas');
    extent.append(canvas); viewport.append(extent); container.replaceChildren(viewport);
    let current = null, zoom = 1;
    function scale(value) {
      if (!Number.isFinite(value) || value <= 0) return;
      zoom = Math.min(2, value);
      canvas.style.transform = `scale(${zoom})`;
      extent.style.width = (current?.width || 0) * zoom + 'px';
      extent.style.height = (current?.height || 0) * zoom + 'px';
      onZoom(zoom);
    }
    function center(id) {
      const position = current?.nodes.find(n => n.node.id === id);
      if (!position) { viewport.scrollTop = viewport.scrollLeft = 0; return; }
      viewport.scrollLeft = Math.max(0, (position.x + width / 2) * zoom - viewport.clientWidth / 2);
      viewport.scrollTop = Math.max(0, (position.y + height / 2) * zoom - viewport.clientHeight / 2);
    }
    function draw(nodes, links, selected) {
      const restoreFocus = canvas.contains(document.activeElement);
      current = layout(nodes, links); canvas.replaceChildren();
      canvas.style.width = current.width + 'px'; canvas.style.height = current.height + 'px';
      const edges = svg('svg', {width: current.width, height: current.height, class: 'tracks-edges'});
      const defs = svg('defs'); edges.append(defs);
      const edgeColors = {required: '#83afb0', relation: '#bea4eb', reference: '#8697ab', structure: '#6fb8e3', trace: '#e6be79'};
      for (const [layer, color] of Object.entries(edgeColors)) {
        const marker = svg('marker', {id: 'tracks-arrow-' + layer, viewBox: '0 0 10 10', refX: 9, refY: 5, markerWidth: 6, markerHeight: 6, orient: 'auto'});
        marker.append(svg('path', {d: 'M 0 0 L 10 5 L 0 10 z', fill: color})); defs.append(marker);
      }
      for (const {link, path, labelX, labelY} of current.edges) {
        const description = (link.layer === 'structure' ? 'Code observation: ' : link.layer === 'trace' ? 'Proposed trace: ' : link.layer === 'relation' ? 'Authored: ' : link.layer === 'required' ? 'Retention: ' : 'Reference: ')
          + link.label + ' · ' + link.source + ' → ' + link.target;
        const actionable = !!link.record_id || link.source === selected || link.target === selected;
        const group = svg('g', {'data-link': link.id, 'data-layer': link.layer,
          class: 'tracks-link', tabindex: actionable ? 0 : -1, role: actionable ? 'button' : 'img', 'aria-label': description});
        const title = svg('title'); title.textContent = description; group.append(title);
        group.append(svg('path', {d: path, class: 'tracks-hit'}));
        group.append(svg('path', {d: path, class: 'tracks-line', stroke: edgeColors[link.layer], 'marker-end': `url(#tracks-arrow-${link.layer})`}));
        if (current.edges.length <= 80 || link.source === selected || link.target === selected) {
          const label = svg('text', {x: labelX, y: labelY, 'text-anchor': 'middle', class: 'tracks-edge-label'});
          label.textContent = link.layer === 'required' ? 'retain' : link.label.length > 32 ? link.label.slice(0, 31) + '…' : link.label;
          group.append(label);
        }
        if (actionable) {
          group.onclick = () => onLink(link);
          group.onkeydown = event => {
            if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); onLink(link); }
          };
        }
        edges.append(group);
      }
      canvas.append(edges);
      for (const item of current.nodes) {
        const {node, x, y, cycle} = item;
        const button = html('button', undefined, 'tracks-node');
        button.dataset.id = node.id; button.dataset.cycle = String(cycle);
        button.setAttribute('aria-pressed', String(node.id === selected));
        button.title = node.label + '\n' + node.id;
        Object.assign(button.style, {left: x + 'px', top: y + 'px', width: width + 'px', height: height + 'px'});
        button.style.setProperty('--family', colors[node.family]);
        button.append(html('small', names[node.family] + (cycle ? ' · cycle' : '')), html('strong', node.label));
        button.onclick = () => onNode(node.id);
        button.onkeydown = event => {
          if (!['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) return;
          event.preventDefault();
          const horizontal = event.key === 'ArrowLeft' || event.key === 'ArrowRight';
          const sign = event.key === 'ArrowLeft' || event.key === 'ArrowUp' ? -1 : 1;
          const candidates = current.nodes.filter(n => horizontal ? (n.column - item.column) * sign > 0
            : n.column === item.column && (n.row - item.row) * sign > 0);
          candidates.sort((a, b) => Math.abs(a.column - item.column) - Math.abs(b.column - item.column)
            || Math.abs(a.row - item.row) - Math.abs(b.row - item.row));
          if (candidates[0]) [...canvas.querySelectorAll('.tracks-node')].find(n => n.dataset.id === candidates[0].node.id)?.focus();
        };
        canvas.append(button);
      }
      if (!nodes.length) canvas.append(html('p', 'No records in this view.', 'tracks-empty'));
      scale(zoom); center(selected);
      if (restoreFocus) {
        const target = [...canvas.querySelectorAll('.tracks-node')].find(n => n.dataset.id === selected);
        (target || viewport).focus({preventScroll: true});
      }
    }
    return {draw, zoomBy: multiplier => scale(zoom * multiplier), reset: () => scale(1),
      fit: () => {
        if (!current || !viewport.clientWidth || !viewport.clientHeight) return;
        scale(Math.min(1, viewport.clientWidth / current.width, viewport.clientHeight / current.height));
        viewport.scrollTop = viewport.scrollLeft = 0;
      }};
  }
  return {layout, create};
})();
