"""Generate current documentary derivatives from explicit inputs.

Conservation is an independently authored input. This module never writes it.
Source freezing, interpretation construction and full inventory are separate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / 'successor'
PREVIOUS = HERE.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# These source parsing functions have no output effects or selected-path globals.
PARSE = load_module('artifact_source_parsing', PREVIOUS / 'synthesis/check_artifacts.py')


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_path(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def write(name, value):
    write_path(HERE / name, value)


def exact_commit(value):
    resolved = subprocess.check_output(['git', 'rev-parse', value + '^{commit}'], cwd=TENANT, text=True).strip()
    if value != resolved:
        raise ValueError('Use the full immutable commit, not a branch or abbreviation')
    return resolved


def verify_common(value):
    exact_commit(value)
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
    common = TENANT.parents[1] / 'specification'
    # Work-state records may advance independently. Constitutional inputs may not.
    paths = [common / n for n in ['INTENT.md', 'PRODUCT.md', 'REFERENCE_FRAME_BASIS.md']]
    paths += sorted((common / 'requirements').rglob('*.md'))
    paths += sorted((common / 'conformance').rglob('*.md'))
    for path in paths:
        frozen = subprocess.check_output(['git', 'show', value + ':' + str(path.relative_to(repo))], cwd=repo)
        if frozen != path.read_bytes():
            raise ValueError('Common constitutional input drift: ' + str(path.relative_to(repo)))
    return value


def protected_pins(support=HERE):
    return {name: sha(support / name) for name in ['CONSERVATION.json', 'FRONTIER.json']}


def compression_body(path):
    text = path.read_text()
    if not text.startswith('---\n'):
        return None
    front, body = text[4:].split('---', 1)
    return front, body


def compression_owners(path, package=PACKAGE):
    path, package = path.resolve(), package.resolve()
    pair = compression_body(path)
    if pair is None:
        return {}
    front, _ = pair
    owners = {}
    single = re.search(r'^source_ref: (.+)$', front, re.M)
    if single:
        owner = (path.parent / single[1]).resolve()
        owner.relative_to(package.resolve())
        owners[str(owner.relative_to(package.resolve()))] = sha(owner)
    for match in re.finditer(r'^  ([\w/.-]+): ([0-9a-f]{64})$', front, re.M):
        owner = PARSE.confined(package / 'standards', match[1])
        owners[str(owner.relative_to(package))] = sha(owner)
    return owners


def render_views(package, support, common_input):
    """Prepare all changes before writing; declarations select the task routes."""
    package, support = package.resolve(), support.resolve()
    index = read(support / 'FRAME_INPUTS.json')
    changes = {}
    reviews = index.get('compression_body_reviews', {})
    for path in sorted((package / 'standards/authority_compressions').glob('*.md')):
        pair = compression_body(path)
        if pair is None:
            continue
        front, body = pair
        name = str(path.relative_to(package))
        review = reviews.get(name, {})
        owners = compression_owners(path, package)
        if (review.get('body_sha256') != hashlib.sha256(body.encode()).hexdigest()
                or review.get('owner_pins') != owners):
            raise ValueError('Compression body/source reconciliation not recorded: ' + name)
        single = re.search(r'^source_ref: (.+)$', front, re.M)
        if single:
            front = re.sub(r'^source_digest: [0-9a-f]{64}$',
                           'source_digest: ' + sha((path.parent / single[1]).resolve()), front, flags=re.M)
        front = re.sub(r'^(  ([\w/.-]+): )([0-9a-f]{64})$',
                       lambda m: m[1] + sha(package / 'standards' / m[2]), front, flags=re.M)
        changes[path] = '---\n' + front + '---' + body
    for frame in index['frames']:
        path = PARSE.confined(package, frame['path'])
        routes = frame['routes']
        if len({(r['owner'], r['anchor']) for r in routes}) != len(routes):
            raise ValueError('Duplicate frame route: ' + frame['path'])
        parts = [path.read_text().split('\nSource:', 1)[0].rstrip()]
        for route in routes:
            owner = PARSE.confined(package, route['owner'])
            heading, raw = PARSE.section(owner.read_text(), route['anchor'])
            def relocate(match):
                target = match[2]
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    return match[0]
                return match[1] + '../' + (owner.name if target.startswith('#') else '') + target + match[3]
            rendered = re.sub(r'(\[[^\]]*\]\()([^\n]+?)(\))', relocate, raw)
            link = '../' + str(Path(route['owner']).relative_to('standards')) + '#' + route['anchor']
            parts.append('\nSource: [' + owner.name + ' — ' + heading['heading'] + '](' + link + '); '
                         + 'SHA256 `' + sha(owner) + '`.\n\n' + rendered)
            route.update(owner_sha256=sha(owner), section_sha256=hashlib.sha256(raw.encode()).hexdigest())
        value = '\n'.join(parts).rstrip() + '\n'
        changes[path] = value
        frame.update(sha256=hashlib.sha256(value.encode()).hexdigest(), bytes=len(value.encode()))
    if index.get('source_linked_summaries'):
        raise ValueError('No current source-linked summary renderer is selected')
    index.update(input_commit=common_input, standing='Exact current excerpts and author-reconciled summaries; semantic fidelity and task sufficiency require separate proof.')
    return changes, index


def refresh_views(common_input, package=PACKAGE, support=HERE):
    protected = protected_pins(support)
    changes, index = render_views(package, support, common_input)
    for path, value in changes.items():
        path.write_text(value)
    write_path(support / 'FRAME_INPUTS.json', index)
    if protected != protected_pins(support):
        raise ValueError('Conservation input changed during generation; derived subject is invalid')
    return len(index['frames'])


def inventory(source_commit, common_input, document_source_commit):
    source_commit, document_source_commit = map(exact_commit, [source_commit, document_source_commit])
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=TENANT, text=True).strip())
    prefix = str(PACKAGE.relative_to(repo))
    current = PARSE.tree_pins(PACKAGE)
    frozen = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', source_commit, '--', prefix], cwd=repo, text=True).splitlines()
    if {p[len(prefix) + 1:] for p in frozen} != set(current):
        raise ValueError('Frozen package membership differs from working package')
    rows = []
    for name, pin in current.items():
        raw = subprocess.check_output(['git', 'show', source_commit + ':' + prefix + '/' + name], cwd=repo)
        if hashlib.sha256(raw).hexdigest() != pin['sha256'] or len(raw) != pin['bytes']:
            raise ValueError('Package differs from frozen source: ' + name)
        if not name.startswith('interpretation/'):
            document = subprocess.check_output(['git', 'show', document_source_commit + ':' + prefix + '/' + name], cwd=repo)
            if document != raw:
                raise ValueError('Document changed after interpretation source freeze: ' + name)
        row = dict(path=name, **pin)
        if name == 'README.md':
            row['role'] = 'package entry'
        elif name.startswith('interpretation/'):
            row.update(role='source-package interpretation', installation_mapping='not selected by this source construction')
        else:
            row.update(role='Product member', expected_installed_path=name)
        rows.append(row)
    previous = read(HERE / 'CANDIDATE.json')
    previous.update(members=rows, source_input_commit=common_input,
                    candidate_body_input_commit=source_commit, inventory_input_commit=source_commit,
                    document_source_input_commit=document_source_commit,
                    standing='Codex I3 source candidate; independent member acceptance and installed qualification remain open.',
                    snapshot_order='Document source precedes interpretation; complete source precedes this inventory recording.')
    write('CANDIDATE.json', previous)
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--common-input', required=True)
    parser.add_argument('--expect-conservation-sha256', required=True)
    parser.add_argument('--source-commit')
    parser.add_argument('--document-source-commit')
    parser.add_argument('--views', action='store_true')
    parser.add_argument('--verification-material', action='store_true')
    args = parser.parse_args()
    common = verify_common(args.common_input)
    protected = protected_pins()
    if protected['CONSERVATION.json'] != args.expect_conservation_sha256:
        raise ValueError('Conservation preimage changed; reacquire the owning Writer return')
    if not (args.views or args.verification_material or args.source_commit):
        parser.error('Select views, verification material, or frozen inventory')
    if bool(args.source_commit) != bool(args.document_source_commit):
        parser.error('Full inventory requires both source and document-source commits')
    report = {}
    try:
        if args.views:
            report['frames'] = refresh_views(common)
        if args.verification_material:
            helper = load_module('current_derivation_material', PREVIOUS / 'synthesis/derivation_material.py')
            result = helper.build(PACKAGE, PARSE.INSTALLED)
            report['derivation_members'] = len(result['members'])
        if args.source_commit:
            report['members'] = inventory(args.source_commit, common, args.document_source_commit)
    finally:
        if protected != protected_pins():
            raise ValueError('Conservation changed during generation; discard derived outputs')
    report['conservation_preserved'] = protected
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
