"""Static checks of the sealed actual artifact; no browser or server."""
from __future__ import annotations
import base64
from collections import Counter
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

BASE = Path('/Users/jim/src/apps/specification_methodology/a_c')
APP = BASE / 'applications/stdo-v3-common-35fb4824'
PROOF = BASE / '.ai-workspace/qualification/t010/packaging/final-001'
state = json.loads((PROOF / 'extraction-and-stdlib-command.json').read_text())
BUNDLE = Path(state['bundle'])
WORK = Path(tempfile.mkdtemp(prefix='ac-common-release-final-static-'))


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.scripts = []
        self.ids = []
        self.in_script = False
        self.script = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            self.ids.append(values['id'])
        for key in ('href', 'src'):
            if key in values:
                self.links.append((tag, key, values[key]))
        if tag == 'script':
            self.in_script = True
            self.script = {'attrs': values, 'text': ''}

    def handle_data(self, data):
        if self.in_script:
            self.script['text'] += data

    def handle_endtag(self, tag):
        if tag == 'script':
            self.in_script = False
            self.scripts.append(self.script)


sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
model = json.loads((BUNDLE / 'model.json').read_text())
scope = json.loads((BUNDLE / 'view-scope.json').read_text())
records = json.loads((BUNDLE / 'records.json').read_text())
record_graph = json.loads((BUNDLE / 'records-graph.json').read_text())
families = Counter({name: len(rows) for name, rows in model['populations'].items() if rows})
all_ids = {row['id'] for rows in model['populations'].values() for row in rows}
assert len(all_ids) == 1987 and set(scope['included']) == all_ids and scope['omitted'] == [] and scope['aggregated_nodes'] == 0
graph_html = (BUNDLE / 'graph.html').read_text()
raw_nodes = json.loads(re.search(r'const RAW_NODES = (\[.*?\]);\nconst RAW_EDGES', graph_html, re.S).group(1))
raw_edges = json.loads(re.search(r'const RAW_EDGES = (\[.*?\]);\nconst LEGEND', graph_html, re.S).group(1))
legend = json.loads(re.search(r'const LEGEND = (\[.*?\]);\n', graph_html, re.S).group(1))
assert {row['id'] for row in raw_nodes} == all_ids
assert len(raw_edges) == scope['displayed_reference_pairs'] == scope['full_reference_pairs']
assert {(row['from'], row['to']) for row in raw_edges} == {(row['source'], row['target']) for row in record_graph['links']}
assert sum(len(row['occurrences']) for row in record_graph['links']) == scope['local_reference_occurrences']
assert {row['label'].removeprefix('Record family: '): row['count'] for row in legend} == dict(families)
assert graph_html.count(scope['banner_html']) == 1 and 'no algorithmic communities or semantic acceptance' in scope['banner_html']

html_documents = {}
local_links = []
inline_scripts = []
for name in ('index.html', 'graph.html', 'records.html'):
    parser = Document()
    parser.feed((BUNDLE / name).read_text())
    assert len(parser.ids) == len(set(parser.ids)), name
    html_documents[name] = parser
    for tag, key, value in parser.links:
        url = urlsplit(value)
        assert not url.scheme and not url.netloc, (name, value)
        target = BUNDLE / unquote(url.path)
        assert target.exists(), (name, value)
        local_links.append({'document': name, 'target': value})
    for i, script in enumerate(parser.scripts):
        attrs = script['attrs']
        if attrs.get('type') == 'application/json':
            assert attrs.get('id') == 'record-data' and json.loads(script['text']) == records
        elif 'src' in attrs:
            assert attrs['src'] == 'release_tools/vendor/vis-network-9.1.6.min.js'
            assert attrs['integrity'] == 'sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1'
        else:
            path = WORK / (name + f'.inline-{i}.js')
            path.write_text(script['text'])
            inline_scripts.append(path)
asset = BUNDLE / 'release_tools/vendor/vis-network-9.1.6.min.js'
assert sha(asset) == '576bb887733eb01bb52ee75b90ef46d818454de5fddb5b616fb8a298d307ca12'
assert 'sha384-' + base64.b64encode(hashlib.sha384(asset.read_bytes()).digest()).decode() == 'sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1'
node = shutil.which('node')
assert node, 'existing Node executable unavailable for static syntax checks'
for path in inline_scripts + [asset]:
    result = subprocess.run([node, '--check', str(path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

page_anchors = {}
source_members = json.loads((BUNDLE / 'package-custody.json').read_text())['members']
for row in source_members:
    page = BUNDLE / 'source-view' / (row['path'] + '.html')
    parser = Document()
    parser.feed(page.read_text())
    expected = {f'L{i}' for i in range(1, len((BUNDLE / 'source' / row['path']).read_text().splitlines()) + 1)}
    assert set(parser.ids) == expected and len(parser.ids) == len(expected)
    assert row['sha256'] in page.read_text()
    page_anchors[row['path']] = expected
groundings = []


def walk(value):
    if isinstance(value, list):
        for child in value:
            walk(child)
    elif isinstance(value, dict):
        if {'path', 'section', 'start_line', 'end_line', 'quote'} <= value.keys():
            assert f"L{value['start_line']}" in page_anchors[value['path']]
            assert f"L{value['end_line']}" in page_anchors[value['path']]
            groundings.append(value)
        for child in value.values():
            walk(child)


for row in records['records']:
    walk(row['record'])
assert len(groundings) == 2491
release = json.loads((BUNDLE / 'RELEASE.json').read_text())
md_files = [BUNDLE / 'SOURCE-READINESS.md']
for receipt in release['review_receipts']:
    md_files += [BUNDLE / row['path'] for row in receipt['reports']]
markdown_links = []
for path in md_files:
    for value in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text()):
        url = urlsplit(value)
        assert not url.scheme and not url.netloc, (path, value)
        target = (path.parent / unquote(url.path)).resolve()
        assert target.is_relative_to(BUNDLE.resolve()) and target.exists(), (path, value)
        markdown_links.append({'document': path.relative_to(BUNDLE).as_posix(), 'target': value})
source_ready = (BUNDLE / 'SOURCE-READINESS.md').read_text()
assert '114a4580a344daa1cf32bcbc19246ab189c26b3f50b58d47c105ae7a2b54bd1d' in source_ready
assert '```sh\npython3 -B freeze_sources.py' not in source_ready
assert '```sh\npython3 -B release_tools/bundle_check.py .\n```' in source_ready
result = {'status': 'passed', 'scope': 'Static actual-artifact display/source/link/dependency checks only; no browser/runtime UI verification',
          'displayed_records': len(raw_nodes), 'omitted_records': len(scope['omitted']), 'aggregated_nodes': 0,
          'displayed_reference_pairs': len(raw_edges), 'local_reference_occurrences': scope['local_reference_occurrences'],
          'omitted_external_reference_occurrences': scope['omitted_external_reference_occurrences'], 'family_groups': dict(families),
          'source_pages': len(page_anchors), 'grounding_occurrences_with_valid_source_line_anchors': len(groundings),
          'exact_records_embedded': len(records['records']), 'local_html_links': local_links, 'local_markdown_links': markdown_links,
          'javascript_files_syntax_checked': len(inline_scripts) + 1, 'offline_asset_sha256': sha(asset),
          'browser_or_server_started': False, 'interactive_behavior': 'UNVERIFIED'}
(PROOF / 'static-controls.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({key: value for key, value in result.items() if key not in ('local_html_links', 'local_markdown_links')}, indent=2))
