"""Verify immutable carry, derivative routes and installable member namespaces.

Mechanical conservation and a hypothetical schema instance are not semantic
acceptance or publication. This checker writes only its own qualification return.
"""
from pathlib import Path
import ast
import copy
import difflib
import hashlib
import json
import re
import subprocess
import sys
import time
import unicodedata

base = Path(__file__).resolve().parents[2]
root = base / 'successor'
installed = Path('/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2')
started = time.monotonic()
failures = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

pins = json.loads((base/'qualification/C3/PREDECESSOR_VERIFICATION.json').read_text())['pins']
for pin in pins:
    if sha(installed/pin['path']) != pin['sha256']:
        failures.append('changed predecessor ' + pin['path'])

carry = []
for source in sorted((installed/'standards').glob('*.md')):
    if source.name == 'README.md':
        continue
    before = [line for line in source.read_text().splitlines() if line.strip()]
    after = [line for line in (root/'standards'/source.name).read_text().splitlines() if line.strip()]
    removed = [(tag, before[i:j]) for tag, i, j, _, _ in
               difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes()
               if tag in {'delete', 'replace'}]
    if removed:
        failures.append('source-owned line changed/removed in ' + source.name)
    carry.append({'member': source.name, 'source_operative_lines': len(before),
                  'every_source_nonblank_line_retained_in_order': not removed,
                  'limits': 'Introduced binding semantics need independent comparison; README is separately restated.'})

compression_pins = 0
for path in (root/'standards/authority_compressions').glob('*.md'):
    text = path.read_text()
    if not text.startswith('---\n'):
        continue
    front = text[4:].split('---', 1)[0]
    one = re.search(r'^source_ref: (.+)$', front, re.M)
    if one:
        expected = re.search(r'^source_digest: ([0-9a-f]{64})$', front, re.M)
        if not expected or sha((path.parent/one[1]).resolve()) != expected[1]:
            failures.append('stale compression ' + path.name)
        compression_pins += 1
    for match in re.finditer(r'^  ([\w/.-]+): ([0-9a-f]{64})$', front, re.M):
        if sha(root/'standards'/match[1]) != match[2]:
            failures.append('stale watched source ' + path.name + ':' + match[1])
        compression_pins += 1

view_index = json.loads((base/'qualification/C3/FRAME_INPUTS.json').read_text())
views = view_index['frames'] + view_index.get('source_linked_summaries', [])
exact_excerpt_sections = 0

def heading_slug(value):
    value = re.sub(r'<[^>]*>', '', value).replace('`', '').lower()
    value = unicodedata.normalize('NFC', value)
    return re.sub(r'\s', '-', re.sub(r'[^\w\-\s]', '', value))

def restore_source_link(match):
    target = match[2]
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
        return match[0]
    if not target.startswith('../'):
        raise ValueError('excerpt link lacks its one-level relocation')
    return match[1] + target[3:] + match[3]

for view in views:
    if sha(root/view['path']) != view['sha256']:
        failures.append('view pin mismatch ' + view['path'])
    for route in view['routes']:
        if sha(root/route['owner']) != route['owner_sha256']:
            failures.append('view owner changed ' + route['owner'])
    if view in view_index['frames']:
        chunks = (root/view['path']).read_text().split('\nSource:')[1:]
        if len(chunks) != len(view['routes']):
            failures.append('excerpt count differs ' + view['path'])
            continue
        for route, chunk in zip(view['routes'], chunks):
            owner_text = (root/route['owner']).read_text()
            headings = list(re.finditer(r'^(#{2,6}) (.+)$', owner_text, re.M))
            selected = [(i,h) for i,h in enumerate(headings) if heading_slug(h[2]) == route['anchor']]
            if len(selected) != 1:
                failures.append('ambiguous excerpt source ' + route['anchor'])
                continue
            i,h = selected[0]
            end = next((n.start() for n in headings[i+1:] if len(n[1]) <= len(h[1])), len(owner_text))
            original = owner_text[h.start():end].rstrip() + '\n'
            if hashlib.sha256(original.encode()).hexdigest() != route['section_sha256']:
                failures.append('section digest differs ' + route['anchor'])
            try:
                displayed = chunk.split('\n\n',1)[1].rstrip() + '\n'
                restored = re.sub(r'(\[[^\]]*\]\()([^\n]+?)(\))', restore_source_link, displayed)
            except (ValueError, IndexError) as error:
                failures.append('invalid excerpt ' + view['path'] + ': ' + str(error))
                continue
            if restored != original:
                failures.append('excerpt differs from source ' + route['anchor'])
            else:
                exact_excerpt_sections += 1

# Literal references are checked as references, not accepted semantic imports.
authority = (root/'standards/REFERENCE_FRAME_METHOD.md').read_text().split('### Authority\n',1)[1].split('### Disjointness',1)[0]
literal_rows = []
for match in re.finditer(r'^- \*\*([^*]+)\*\*: (.*?)(?=\n- \*\*|\n\nThese relations)', authority, re.M|re.S):
    meaning = re.sub(r';(?: and)?$', '', ' '.join(match[2].split()))
    literal_rows.append('| '+match[1]+' | urn:stdo:bounded-context:reference-frame-evaluation | [Frame authority](REFERENCE_FRAME_METHOD.md#authority): '+meaning+' |')
authority_literal_rows = 0
if len(literal_rows) != 6:
    failures.append('authority reference source lacks six relations')
for member in ['FOUNDATIONS.md','TRANSFORMATION_LIBRARY.md']:
    text = (root/'standards'/member).read_text()
    for row in literal_rows:
        if text.count(row) != 1:
            failures.append('authority literal reference differs ' + member)
        else:
            authority_literal_rows += 1

# Compare the JSON Schema instance in a local, explicitly hypothetical release
# envelope. It chooses no actual cut/ref and performs no installation.
from jsonschema import Draft202012Validator
manifest = copy.deepcopy(json.loads((installed/'manifest.json').read_text()))
manifest['release'] = {'cut':'v0.0.0-rc.1', 'tag_object':'0'*40, 'commit':'0'*40,
                       'tree':'0'*40, 'standards_tree':'0'*40}
for key, folder in [('standards','standards'), ('plugin','plugins/spec')]:
    members = [{'path':str(p.relative_to(root/folder)), 'sha256':sha(p)}
               for p in sorted((root/folder).rglob('*')) if p.is_file()]
    inventory = manifest['standards'] if key == 'standards' else manifest['auxiliary']['plugin']
    inventory['members'] = members
    inventory['member_count'] = len(members)
    if key == 'standards':
        inventory['member_set_sha256'] = hashlib.sha256(json.dumps(members,sort_keys=True,separators=(',',':')).encode()).hexdigest()
manifest['auxiliary']['license']['sha256'] = sha(root/'LICENSE')
manifest['auxiliary']['release_note'] = {'source_path':'releases/v0.0.0.md',
                                       'installed_path':'release/release-note.md',
                                       'sha256':sha(base/'qualification/C3/surface-repair/release-note-fixture.md')}
schema = json.loads((root/'standards/schemas/installed-release-manifest.schema.json').read_text())
validator = Draft202012Validator(schema)
errors = list(validator.iter_errors(manifest))
if errors:
    failures.extend('manifest schema: '+e.message for e in errors)
bad = copy.deepcopy(manifest)
bad['auxiliary']['uncatalogued_history'] = {'path':'provenance/note.md'}
extra_category_refused = bool(list(validator.iter_errors(bad)))
if not extra_category_refused:
    failures.append('undeclared installed auxiliary category passed')
installed_members = ({'standards/'+m['path'] for m in manifest['standards']['members']} |
                     {'plugins/spec/'+m['path'] for m in manifest['auxiliary']['plugin']['members']} |
                     {'LICENSE','release/release-note.md'})
product_files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
                 and (str(p.relative_to(root)).startswith(('standards/','plugins/spec/'))
                      or str(p.relative_to(root)) == 'LICENSE')}
if product_files | {'release/release-note.md'} != installed_members:
    failures.append('hypothetical installer inventory differs from complete Product member set')
for path in ['standards/frames/WORK_RECOVERY.md']:
    if path not in installed_members:
        failures.append('new material not inventory-covered '+path)

# Instantiate the retained template, including a positive definition and two
# ordinary wrong-basis controls; no Product Definition is installed or synced.
template = json.loads((root/'standards/templates/PRODUCT_DEFINITION_TEMPLATE.json').read_text())
raw = json.dumps(template).replace('REPLACE_WITH_IMMUTABLE_CUT','v2.5.1-rc.2').replace(
    'REPLACE_WITH_64_LOWERCASE_HEX_SHA256','3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782').replace('REPLACE_WITH_VERSION_LINE','2.5.1')
positive = json.loads(raw)
def_validator = Draft202012Validator(json.loads((root/'standards/schemas/product-definition.schema.json').read_text()))
definition_errors = list(def_validator.iter_errors(positive))
if definition_errors:
    failures.extend('definition schema: '+e.message for e in definition_errors)
negative_definition_controls = []
for key, value in [('uri','stdo://channels/2.5.1'),('manifest_sha256','1'*63)]:
    bad = copy.deepcopy(positive)
    bad['constitution']['stdo']['basis'][key] = value
    refused = bool(list(def_validator.iter_errors(bad)))
    negative_definition_controls.append({'field':key,'refused':refused})
    if not refused:
        failures.append('wrong definition basis accepted '+key)

for path in [base/'qualification/C3/check_candidate.py', base/'qualification/C3/refresh_views.py',
             base/'qualification/C3/run_review.py', base/'qualification/C3/a_c/finite_check.py']:
    try:
        ast.parse(path.read_text(), feature_version=(3,8))
    except SyntaxError as error:
        failures.append('Python 3.8 syntax: '+str(path)+': '+str(error))

report = {'kind':'standalone_distribution_artifact_check',
          'builder_manifest_sha256':'3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782',
          'predecessor_members_verified':len(pins), 'operative_carry':carry,
          'compression_source_and_index_pins':compression_pins, 'derived_views_checked':len(views),
          'selected_excerpt_sections_exact':exact_excerpt_sections,
          'authority_literal_reference_rows_exact':authority_literal_rows,
          'hypothetical_inventory_members':len(installed_members),
          'product_package_members':len(product_files),
          'release_note_is_hypothetical_fixture':True,
          'manifest_schema_valid':not errors, 'extra_auxiliary_category_refused':extra_category_refused,
          'template_definition_schema_valid':not definition_errors,
          'negative_definition_controls':negative_definition_controls,
          'failures':failures,'valid':not failures,'elapsed_seconds':round(time.monotonic()-started,3),
          'limits':['No semantic fidelity from structural success',
                    'No published cut, native v3 install or plugin-host qualification; actual release note remains an owner-selected publication obligation',
                    'Python 3.8 syntax only, not an executed Python 3.8 compatibility test']}
(base/'qualification/C3/DISTRIBUTION_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='operative_carry'},indent=2))
raise SystemExit(0 if report['valid'] else 1)
