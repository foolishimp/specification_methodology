#!/usr/bin/env python3
"""Render the root history as a self-contained, offline HTML document.

Build dependency: python -m pip install Markdown==3.10.2
Run from any directory: python scripts/build_history.py
The generated page requires no server, package installation, fonts or CDN.
"""

import hashlib
import html
import re
import textwrap
from pathlib import Path

try:
    import markdown
except ImportError as exc:
    raise SystemExit("Install the build dependency: python -m pip install Markdown==3.10.2") from exc

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "history.md"
TEMPLATE = Path(__file__).with_name("history_template.html")
OUTPUT = ROOT / "history.html"
# This source cut retains every local release note cited by the history.
RELEASE_SOURCE = "https://github.com/foolishimp/specification_methodology/blob/225284646a5f975c2c4a3aec6e8ef70a97000d3d/"

CHAPTERS = [
    ("Reading the lineage", "lineage", "Across the projects", "The lineage", "Relationships between the implementations and the ideas."),
    ("2024:", "beginnings", "Mid-2024", "The first applications", "State, relationships and a history of change."),
    ("Late 2024-2025:", "intent", "Late 2024–2025", "Preserving intent", "C4H makes work orders, context and transformation lineage explicit."),
    ("August 2025-January 2026:", "method", "August 2025–January 2026", "A reusable method", "Development practices become a subject of development in their own right."),
    ("January-February 2026:", "foundations", "January–February 2026", "Constraints & emergence", "A parallel inquiry into persistence, boundaries and meaning."),
    ("February-March 2026:", "construction", "February–March 2026", "The asset graph", "Construction and evaluation become a shared operation across artifacts."),
    ("March-June 2026:", "boundaries", "March–June 2026", "Separating responsibilities", "Engine, software lifecycle and general lifecycle acquire distinct owners."),
    ("March-April 2026:", "authority", "March–April 2026", "An independent method", "Shared standards acquire their own source and release identity."),
    ("April-June 2026:", "lifecycle", "April–June 2026", "The complete lifecycle", "The product remains answerable to its conditions after construction."),
    ("July-September 2026:", "evidence", "July–September 2026", "The boundaries of evidence", "Every result needs a subject, a basis and a stated limit."),
    ("October-November 2026:", "context", "October–November 2026", "Finite context, explicit ownership", "STDO 3 separates product responsibilities and strengthens continuation."),
    ("The contribution", "contribution", "What accumulated", "The contribution", "Preservation, evaluation, authority and correction across generations."),
    ("Sources and", "sources", "The record", "Sources & limits", "Check-ins, releases, contemporary publications and the remaining gaps."),
]

LAYOUTS = [
    {
        "title": "Project and conceptual lineage",
        "description": "The application and agent line feeds into Genesis, the execution and lifecycle projects, and STDO. The ontology supplies a parallel conceptual contribution.",
        "size": (830, 1510),
        "positions": {"B": (30, 20), "T": (30, 140), "R": (30, 260), "C": (30, 380), "I": (30, 525), "A": (30, 670), "O": (500, 525), "G": (265, 815), "E": (30, 960), "S": (500, 960), "D": (30, 1105), "L": (30, 1250), "M": (500, 1105), "V": (500, 1250), "W": (500, 1395)},
        "research": {"O"},
        "method": {"I", "A", "M", "V", "W"},
        "outer": {("O", "V")},
    },
    {
        "title": "Engineering and the foundational inquiry",
        "description": "Application work informs reasoning and semantic models. The ontology informs Genesis and STDO. Counterexamples feed back into both the theory and the method.",
        "size": (830, 890),
        "positions": {"P": (265, 20), "R": (30, 170), "S": (500, 170), "O": (265, 325), "G": (265, 475), "M": (265, 625), "E": (500, 780)},
        "research": {"R", "S", "O", "E"},
        "method": {"M"},
        "outer": {("O", "E"), ("E", "O"), ("E", "M")},
    },
    {
        "title": "Authority, evaluation and correction",
        "description": "Intent and requirements govern design and realization. Evaluation informs judgment. A material discrepancy returns work to the layer that owns it.",
        "size": (830, 790),
        "positions": {"I": (30, 20), "R": (30, 150), "D": (30, 280), "C": (30, 410), "E": (30, 540), "J": (30, 670), "Q": (500, 410)},
        "research": {"E", "J"},
        "method": {"I", "R", "Q"},
        "outer": set(),
    },
]


def escape(text):
    return html.escape(text, quote=True)


def diagram(source, index):
    """Render the three documented Mermaid graphs as static accessible SVGs.

    Node text and every edge come from history.md. Layout coordinates are
    presentation data. Reject a changed graph inventory instead of omitting it.
    """
    if index >= len(LAYOUTS):
        raise ValueError("A new history diagram needs a layout")
    layout = LAYOUTS[index]
    nodes = dict(re.findall(r'^\s*(\w+)\["(.*?)"\]\s*$', source, re.M))
    if set(nodes) != set(layout["positions"]):
        raise ValueError("History diagram nodes changed; update the layout")
    edges = []
    for line in source.splitlines():
        line = line.strip()
        if not line or line.startswith("flowchart") or '["' in line:
            continue
        chain = re.fullmatch(r'(\w+)((?:\s*-->\s*\w+)+)', line)
        if chain:
            names = re.split(r'\s*-->\s*', line)
            edges.extend((a, b, "solid", "") for a, b in zip(names, names[1:]))
            continue
        edge = re.fullmatch(r'(\w+)\s*(-->|-\.->)(?:\|([^|]*)\|)?\s*(\w+)', line)
        if not edge:
            raise ValueError("Unsupported history graph line: " + line)
        a, style, label, b = edge.groups()
        if a not in nodes or b not in nodes:
            raise ValueError("An edge refers to an unknown history node")
        edges.append((a, b, "dotted" if style == "-.->" else "solid", label or ""))

    node_lines = {}
    node_heights = {}
    for key, label in nodes.items():
        wrapped = []
        for j, line in enumerate(re.split(r'<br\s*/?>', label)):
            wrapped.extend((part, j == 0) for part in textwrap.wrap(line, width=26 if j == 0 else 32, break_long_words=False, break_on_hyphens=False))
        node_lines[key] = wrapped
        node_heights[key] = max(90, len(wrapped) * 20 + 22)
    width, height = layout["size"]
    height = max(height, max(y + node_heights[key] + 20 for key, (_, y) in layout["positions"].items()))
    uid = "lineage-" + str(index)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{uid}-title {uid}-desc" class="history-diagram">',
           f'<title id="{uid}-title">{escape(layout["title"])}</title>',
           f'<desc id="{uid}-desc">{escape(layout["description"])}</desc>',
           f'<defs><marker id="{uid}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#71849a"/></marker></defs>']
    for a, b, style, label in edges:
        ax, ay = layout["positions"][a]
        bx, by = layout["positions"][b]
        if (a, b) in layout["outer"]:
            x1, y1, x2, y2 = ax + 250, ay + node_heights[a] / 2, bx + 250, by + node_heights[b] / 2
            offset = 18 if (a, b) == ("E", "O") else 0
            path = f'M {x1} {y1} C {805 + offset} {y1}, {805 + offset} {y2}, {x2} {y2}'
        elif index == 2 and a == "Q":
            x1, y1, x2, y2 = ax, ay + 45, bx + 250, by + 45
            path = f'M {x1} {y1} C 415 {y1}, 415 {y2}, {x2} {y2}'
        elif index == 2 and b == "Q":
            path = f'M {ax + 250} {ay + 45} C 415 {ay + 45}, 415 {by + 45}, {bx} {by + 45}'
        else:
            x1, y1, x2, y2 = ax + 125, ay + node_heights[a], bx + 125, by
            mid = (y1 + y2) / 2
            path = f'M {x1} {y1} C {x1} {mid}, {x2} {mid}, {x2} {y2}'
        dash = ' stroke-dasharray="5 6"' if style == "dotted" else ""
        svg.append(f'<path d="{path}" fill="none" stroke="#71849a" stroke-width="1.7"{dash} marker-end="url(#{uid}-arrow)"/>')
    for key, label in nodes.items():
        x, y = layout["positions"][key]
        colour = "#9b5234" if key in layout["research"] else "#2858a4" if key in layout["method"] else "#22786e"
        lines = node_lines[key]
        box_height = node_heights[key]
        first_y = y + (box_height - len(lines) * 20) / 2 + 16
        svg.append(f'<g><rect x="{x}" y="{y}" width="250" height="{box_height}" rx="8" fill="white" stroke="#cbd4df"/><rect x="{x}" y="{y + 16}" width="3" height="{box_height - 32}" rx="1" fill="{colour}"/>')
        for j, (text, is_title) in enumerate(lines):
            size, weight, fill = (16, 600, "#142b42") if is_title else (14, 400, "#465b70")
            svg.append(f'<text x="{x + 125}" y="{first_y + j * 20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(text)}</text>')
        svg.append('</g>')
    svg.append('</svg>')
    connections = []
    for a, b, style, label in edges:
        first = lambda key: re.split(r'<br\s*/?>', nodes[key])[0]
        explanation = label or ("conceptual influence or precursor relationship" if style == "dotted" else "documented relationship")
        connections.append(f'<li><strong>{escape(first(a))}</strong> to <strong>{escape(first(b))}</strong><span>{escape(explanation)}</span></li>')
    return ('<figure class="diagram-figure"><figcaption>' + escape(layout["title"]) +
            '</figcaption><div class="diagram-scroll" tabindex="0" aria-label="' + escape(layout["title"]) +
            '; scroll horizontally on a narrow screen">' + ''.join(svg) + '</div>' +
            '<p class="diagram-key"><span class="key-line"></span> Documented relationship <span class="key-line dotted"></span> Conceptual influence</p>' +
            '<details class="diagram-text"><summary>Read the diagram connections</summary><ul>' + ''.join(connections) + '</ul></details></figure>')


def main():
    source = SOURCE.read_text()
    original = source
    diagram_count = 0

    def replace_diagram(match):
        nonlocal diagram_count
        rendered = diagram(match.group(1), diagram_count)
        diagram_count += 1
        return rendered

    source = re.sub(r'```mermaid\n(.*?)\n```', replace_diagram, source, flags=re.S)
    if diagram_count != len(LAYOUTS):
        raise ValueError("The expected three source diagrams were not found")
    definitions = re.findall(r'^\[([^\]]+)\]:\s*(\S+)\s*$', source, re.M)
    ref_block = '\n\n' + '\n'.join(f'[{name}]: {url}' for name, url in definitions)
    source = re.sub(r'^\[([^\]]+)\]:\s*\S+\s*$', '', source, flags=re.M)

    def render(content):
        result = markdown.markdown(content + ref_block, extensions=['tables', 'fenced_code', 'smarty'])
        # Local release-note references remain useful when the single HTML is shared.
        result = re.sub(r'href="(specification_methodology/[^\"]+)"',
                        lambda m: 'href="' + RELEASE_SOURCE + m.group(1) + '"', result)
        return result.replace('<table>', '<div class="table-scroll" tabindex="0" role="region" aria-label="Historical release table"><table>').replace('</table>', '</table></div>')

    sections = re.split(r'^## (.+)$', source, flags=re.M)
    intro = sections[0]
    intro = re.sub(r'^# .*\n', '', intro, count=1)
    intro = re.sub(r'^\*From AI-assisted.*?\*\s*', '', intro, count=1, flags=re.M)
    intro = re.sub(r'\*\*Historical cut:.*?(?=\nSTDO)', '', intro, count=1, flags=re.S)
    chapters, nav, options = [], [], []
    found = []
    for title, content in zip(sections[1::2], sections[2::2]):
        matches = [c for c in CHAPTERS if title.startswith(c[0])]
        if len(matches) != 1:
            raise ValueError("Unmapped chapter: " + title)
        _, slug, period, short, description = matches[0]
        found.append(slug)
        nav.append(f'<a href="#{slug}" data-chapter-link="{slug}"><span>{escape(period)}</span>{escape(short)}</a>')
        options.append(f'<option value="{slug}">{escape(period)} · {escape(short)}</option>')
        chapters.append(f'<section class="chapter" id="{slug}" aria-labelledby="{slug}-heading" data-period="{escape(period)}">'
                        f'<header class="chapter-heading"><p class="eyebrow">{escape(period)}</p><h2 id="{slug}-heading">{escape(title)}</h2>'
                        f'<p class="chapter-deck">{escape(description)}</p></header><div class="prose">{render(content)}</div></section>')
    if len(found) != len(CHAPTERS) or len(set(found)) != len(found):
        raise ValueError("Missing or repeated history chapter")
    source_links = ''.join(f'<li id="source-{escape(name)}"><a href="{escape(url if url.startswith("https://") else RELEASE_SOURCE + url)}">{escape(name.replace("-", " "))}</a><span>{escape(url.split("/")[2] if url.startswith("https://") else "Repository release record")}</span></li>' for name, url in definitions)
    replacements = {
        '@@INTRO@@': render(intro), '@@NAV@@': ''.join(nav), '@@OPTIONS@@': ''.join(options),
        '@@CHAPTERS@@': '\n'.join(chapters), '@@SOURCES@@': source_links,
        '@@SOURCE_COUNT@@': str(len(definitions)), '@@SOURCE_SHA@@': hashlib.sha256(original.encode()).hexdigest(),
        '@@MARKDOWN@@': original.replace('</', '<\\/'),
    }
    output = TEMPLATE.read_text()
    for marker, value in replacements.items():
        output = output.replace(marker, value)
    if re.search(r'@@[A-Z_]+@@', output):
        raise ValueError("An HTML template marker was not filled")
    OUTPUT.write_text(output)
    print(f"Rendered {len(chapters)} chapters, {diagram_count} diagrams and {len(definitions)} sources to {OUTPUT}")


if __name__ == '__main__':
    main()
