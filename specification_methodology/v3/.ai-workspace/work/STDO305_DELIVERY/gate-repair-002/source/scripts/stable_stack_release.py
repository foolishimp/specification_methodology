#!/usr/bin/env python3
"""Stable complete-cohort profile; shared primitives stay in check_stack_release.

This module reads evidence. It neither runs untrusted qualification commands nor
performs Git writes. Successful structural checks do not manufacture a review.
"""
from __future__ import annotations

import json
import io
from pathlib import PurePosixPath
import re
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
import stdo_source_freeze as source_freeze

PROFILE = 'stable-five-product-v1'
PRODUCTS = {'specification_methodology', 'stdo_representation', 'a_c', 'axiom_indexer', 'stdo_skills'}
COMPONENTS = {
    'native_plugin': ('specification_methodology', {'installed_native_workflow'}),
    'manager': ('specification_methodology', {'installed_manager'}),
    'documentation': ('specification_methodology', {'installed_documentation'}),
    'proof_reader': ('specification_methodology', {'current_proof_reader'}),
    'representation': ('stdo_representation', {'source_current_model', 'source_current_map', 'independent_semantic_review'}),
    'unified_explorer': ('stdo_representation', {'current_3d_2d_layered', 'source_files_navigation'}),
    'graphify': ('a_c', {'installed_graphify'}),
    'lean': ('a_c', {'installed_lean', 'exact_candidate_lean_result'}),
    'axiom_indexer': ('axiom_indexer', {'current_index_validation'}),
    'codex_skills': ('stdo_skills', {'current_codex_skills'}),
    'claude_skills': ('stdo_skills', {'current_claude_skills'}),
}
EDGES = {
    ('stdo_representation', 'specification_methodology', 'exact_semantic_source'),
    ('stdo_representation', 'axiom_indexer', 'exact_validation_mechanics'),
    ('stdo_representation', 'a_c', 'exact_projection_and_formal_tools'),
    ('a_c', 'specification_methodology', 'exact_semantic_profile'),
    ('stdo_skills', 'specification_methodology', 'exact_native_workflow'),
    ('stdo_skills', 'stdo_representation', 'exact_current_representation'),
    ('stdo_skills', 'a_c', 'exact_tool_routes'),
}
STABLE = re.compile(r'(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\Z')
HEX = re.compile(r'[0-9a-f]{64}\Z')
OBJECT = re.compile(r'[0-9a-f]{40}\Z')
ACCEPTED = {'passed', 'verified', 'valid', 'checked', 'satisfied'}
ASSESSMENTS = {'independent_semantic_review', 'independent_release_review'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def path(value):
    require(isinstance(value, str) and value and not value.startswith('/') and '\\' not in value, 'invalid relative path')
    require(all(p not in ('', '.', '..') for p in value.split('/')) and ':' not in value, 'unsafe relative path: ' + value)
    require(not any(ord(c) < 32 for c in value), 'control character in path')
    return value


def digest(value):
    require(isinstance(value, str) and HEX.fullmatch(value), 'invalid SHA-256')
    return value


def regular_member(view, name):
    require(view.member_kind(name) == 'file', 'artifact must be a regular contained file: ' + name)
    if view.revision is None:
        root = view.root.absolute()
        member = root / name
        for parent in (member, *member.parents):
            require(not parent.is_symlink(), 'release path redirects through a parent: ' + name)
            if parent == root:
                break


def pinned(view, ref, api, *, as_json=True):
    require(isinstance(ref, dict), 'missing pinned artifact')
    name = path(ref['path'])
    regular_member(view, name)
    raw = view.read_bytes(name)
    require(api.sha256(raw) == digest(ref['sha256']), 'artifact bytes differ: ' + name)
    if 'bytes' in ref:
        require(ref['bytes'] == len(raw), 'artifact size differs: ' + name)
    return json.loads(raw) if as_json else raw


def collect_subject(view, scopes, api):
    require(isinstance(scopes, list) and scopes and scopes == sorted(set(scopes)), 'subject scopes must be nonempty, unique and sorted')
    names = set()
    for scope in scopes:
        scope = path(scope)
        if view.member_kind(scope) is not None:
            found = [scope]
        else:
            found = view.files(scope)
        require(found, 'empty or missing subject scope: ' + scope)
        names.update(found)
    rows = []
    for name in sorted(names):
        regular_member(view, name)
        raw = view.read_bytes(name)
        rows.append({'path': name, 'bytes': len(raw), 'sha256': api.sha256(raw)})
    return {'scope': scopes, 'member_count': len(rows), 'members': rows, 'sha256': api.canonical_value_sha256(rows)}


def subject(view, value, api):
    require(isinstance(value, dict), 'missing exact subject inventory')
    actual = collect_subject(view, value['scope'], api)
    require(actual == value, 'subject inventory differs (missing, extra, stale or tampered member)')
    return actual


def source(view, manifest, api):
    value = pinned(view, manifest['source'], api)
    require(value.get('kind') == source_freeze.KIND and value.get('version') == manifest['cohort']['version'], 'wrong source freeze profile/version')
    root = path(value['source_root'])
    members, contracts = [], []
    for name in view.files(root):
        relative = name.removeprefix(root + '/')
        standard = relative.startswith('standards/') and not relative.startswith(source_freeze.EXCLUDED)
        contract = any(relative.startswith(p) if p.endswith('/') else relative == p for p in source_freeze.NATIVE_CONTRACTS)
        if standard or contract:
            regular_member(view, name)
            raw = view.read_bytes(name)
            row = {'path': relative, 'bytes': len(raw), 'sha256': api.sha256(raw)}
            (members if standard else contracts).append(row)
    require(members == value['members'] and contracts == value['native_contracts'], 'source freeze closure or bytes differ')
    identity = {k: value[k] for k in ('version', 'basis_uri', 'members', 'native_contracts')}
    require(api.sha256(source_freeze.encoded(identity)) == value['source_identity_sha256'] == manifest['source']['source_identity_sha256'], 'semantic source identity differs')
    require(value['basis_uri'] == 'stdo://releases/' + manifest['cohort']['cut'] + '/', 'source cut URI differs')
    require(len(members) == value['member_count'] and source_freeze.member_digest(members) == value['member_set_sha256'], 'source standards inventory digest differs')
    require(len(contracts) == value['native_contract_count'] and source_freeze.member_digest(contracts) == value['native_contract_set_sha256'], 'native contract inventory digest differs')
    return value


def evidence(view, ref, claim, manifest, api):
    required_claims = {c for _, claims in COMPONENTS.values() for c in claims} | {'complete_installed_cohort', 'independent_release_review'}
    require(claim in required_claims, 'unknown required qualification claim')
    record = pinned(view, ref, api)
    require(record.get('kind') == 'stdo.cohort-evidence/1' and record.get('claim') == claim, 'wrong qualification evidence kind/claim')
    require(record.get('status') == 'passed', 'required claim has not passed: ' + claim)
    require(record.get('source_identity_sha256') == manifest['source']['source_identity_sha256'], 'qualification covers stale semantic source: ' + claim)
    bound = record.get('subjects')
    expected = {k: p['subject']['sha256'] for k, p in manifest['products'].items()}
    require(isinstance(bound, dict) and bound and set(bound) <= PRODUCTS, 'qualification has no actual Product subject binding')
    require(all(expected[k] == value for k, value in bound.items()), 'qualification Product subject differs: ' + claim)
    owners = {owner for owner, claims in COMPONENTS.values() if claim in claims}
    if claim in ('complete_installed_cohort', 'independent_release_review'):
        owners = PRODUCTS
    if claim in ('source_current_model', 'source_current_map', 'independent_semantic_review', 'current_3d_2d_layered',
                 'source_files_navigation', 'current_proof_reader', 'installed_lean', 'exact_candidate_lean_result'):
        owners = owners | {'stdo_representation'}
    require(owners <= set(bound), 'qualification omits a required current Product subject: ' + claim)
    require(record.get('limits') is not None, 'qualification limits missing')
    if claim in ASSESSMENTS:
        require(record.get('category') == 'independent_assessment', 'independent assessment required: ' + claim)
        require(record.get('assessor') and record.get('assessor') not in record.get('authors', []), 'assessment is not independent of stated authorship')
        require(record.get('authors') and record.get('conclusion') == 'satisfied' and record.get('open_required_findings') == [], 'independent assessment incomplete')
        pinned(view, record['report'], api, as_json=False)
        require(record.get('executive_disposition') == 'accepted_for_release_scope', 'required review disposition missing')
        return record
    # Claim semantics belong to fixed owner adapters, never caller-provided
    # JSON-pointer observations or arbitrary success/status labels.
    import stable_release_evidence
    stable_release_evidence.verify(view, record, claim, manifest, api)

    return record


def check_shape(manifest):
    require(manifest.get('kind') == 'specification-stack.release-matched-cohort' and manifest.get('schema_version') == 2 and manifest.get('profile') == PROFILE, 'unknown stable cohort profile')
    cohort = manifest['cohort']; version = cohort.get('version')
    require(isinstance(version, str) and STABLE.fullmatch(version), 'stable exact semantic version required')
    require(cohort.get('cut') == 'v' + version and cohort.get('status') == 'candidate', 'complete candidate status/cut required; assembling is not ready')
    require(cohort.get('publication_mode') == 'atomic' and cohort.get('carrier_ref') == 'refs/heads/main', 'unsupported publication mode/carrier')
    require(set(manifest.get('products', {})) == PRODUCTS, 'cohort must declare exactly five Products')
    require(set(manifest.get('components', {})) == set(COMPONENTS), 'required component set differs')
    for name, product in manifest['products'].items():
        require(product.get('namespace') == name and product.get('version') == version, 'Product namespace/version mismatch: ' + name)
        require(product.get('release_ref') == f'refs/tags/{name}/v{version}', 'wrong immutable Product ref: ' + name)
        require(product.get('release_branch') in (None, f'refs/heads/release/{name}/{version}'), 'wrong optional stable release branch: ' + name)
    for name, (owner, claims) in COMPONENTS.items():
        component = manifest['components'][name]
        require(component.get('owner') == owner and component.get('version') == version and set(component.get('required_claims', [])) == claims, 'component owner/version/claim mismatch: ' + name)
    edges = manifest.get('dependency_edges', [])
    require(len(edges) == len(EDGES) and {(e['consumer'], e['provider'], e['relation']) for e in edges} == EDGES, 'dependency closure differs')
    require(set(manifest['qualification']['required_claims']) == {'independent_release_review', 'complete_installed_cohort'}, 'whole-cohort qualification set differs')
    dependencies = manifest.get('third_party_dependencies', [])
    require(dependencies and len({row['name'] for row in dependencies}) == len(dependencies), 'exact third-party dependency pins missing/duplicated')
    for dependency in dependencies:
        require(dependency.get('version') and dependency.get('provenance') and (OBJECT.fullmatch(str(dependency.get('commit', ''))) or HEX.fullmatch(str(dependency.get('sha256', '')))), 'third-party dependency lacks exact independent pin')


def native(view, manifest, semantic, api):
    selected = manifest['native']; require(isinstance(selected, dict), 'complete native binding missing')
    installed = pinned(view, selected['manifest'], api)
    require(installed.get('kind') == 'stdo.installed-release-manifest', 'wrong native installed manifest')
    release = installed['release']; version = manifest['cohort']['version']
    require(release['cut'] == 'v' + version and release.get('profile') == 'stable-v1' and release['qualified_ref'] == manifest['products']['specification_methodology']['release_ref'], 'native cut/profile differs')
    tag = api.annotated_ref(view.root, release['qualified_ref'], failures := [])
    require(not failures and tag == (release['tag_object'], release['commit']), 'native annotated tag identity differs')
    tagged = api.View(view.root, release['commit'])
    prefix = release['project_subtree_root']
    require(prefix == 'specification_methodology/v3' and release['project_release_namespace'] == 'specification_methodology', 'native Product root/namespace differs')
    for field, expression in (('tree', release['commit'] + '^{tree}'), ('project_subtree_tree', release['commit'] + ':' + prefix),
                              ('standards_tree', release['commit'] + ':' + prefix + '/standards')):
        require(api.git(view.root, 'rev-parse', expression).stdout.strip() == release[field], 'native Git tree differs: ' + field)
    predecessor = manifest['native_preparation']['predecessor_native_commit']
    require(api.git(view.root, 'show', '-s', '--format=%P', release['commit']).stdout.strip().split() == [predecessor], 'native predecessor lineage differs')
    annotation = api.git(view.root, 'cat-file', '-p', release['qualified_ref']).stdout
    require('STDO-Release-Profile: stable-v1' in annotation.splitlines(), 'native annotated tag lacks stable profile')
    provenance = pinned(view, selected['source_selection'], api)
    require(provenance['native']['commit'] == release['commit'] and provenance['native']['manifest_sha256'] == selected['manifest']['sha256'], 'native source selection differs')
    source_candidate = provenance['source_candidate']
    require(source_candidate['package_path'] == semantic['source_root'], 'native source producer path differs')
    require(api.git(view.root, 'rev-parse', source_candidate['commit'] + ':' + source_candidate['package_path']).stdout.strip() == source_candidate['package_tree'], 'native source producer tree differs')
    expected = {}
    for row in installed['standards']['members']:
        expected['standards/' + path(row['path'])] = digest(row['sha256'])
    for row in installed['auxiliary']['plugin']['members']:
        expected['plugins/spec/' + path(row['path'])] = digest(row['sha256'])
    standards = installed['standards']; plugin = installed['auxiliary']['plugin']
    require(standards['member_count'] == len(standards['members']) == len({r['path'] for r in standards['members']}), 'native standards count/uniqueness differs')
    require(plugin['member_count'] == len(plugin['members']) == len({r['path'] for r in plugin['members']}), 'native plugin count/uniqueness differs')
    require(standards['member_set_sha256'] == api.member_stream(('specification/standards/' + r['path'], r['sha256']) for r in standards['members']), 'native standards member digest differs')
    expected['LICENSE'] = installed['auxiliary']['license']['sha256']
    note = installed['auxiliary']['release_note']; expected[note['installed_path']] = note['sha256']
    actual = {name.removeprefix(prefix + '/'): api.sha256(tagged.read_bytes(name)) for name in tagged.files(prefix)}
    require(actual == expected, 'native installed inventory differs from tagged payload')
    require({r['path']: r['sha256'] for r in provenance['files']} == expected, 'native provenance inventory differs')
    producer = api.View(view.root, source_candidate['commit'])
    original = {name.removeprefix(source_candidate['package_path'] + '/'): api.sha256(producer.read_bytes(name)) for name in producer.files(source_candidate['package_path'])}
    require(original == expected, 'native producer source bytes differ')
    require(all(tagged.member_kind(prefix + '/' + name) == 'file' for name in actual), 'native payload contains redirect')
    package_root = semantic['source_root']
    candidate = {name.removeprefix(package_root + '/'): api.sha256(view.read_bytes(name)) for name in view.files(package_root)}
    require(candidate == expected, 'native cut does not match complete current candidate payload')
    for row in semantic['members'] + semantic['native_contracts']:
        require(expected.get(row['path']) == row['sha256'], 'native does not contain selected semantic member: ' + row['path'])
    for host in ('.codex-plugin', '.claude-plugin'):
        plugin = json.loads(tagged.read_bytes(prefix + '/plugins/spec/' + host + '/plugin.json'))
        require(plugin['version'] == version, 'native plugin version differs')
    require(set(p for p in expected if p.startswith('standards/documentation/')) and set(p for p in expected if p.startswith('standards/tooling/')), 'native current documentation/tooling missing')
    return release


def content(view, manifest, api):
    check_shape(manifest)
    semantic = source(view, manifest, api)
    for name, product in manifest['products'].items():
        subject(view, product['subject'], api)
        if name != 'specification_methodology':
            marker = name + '/VERSION'
            require(marker in {row['path'] for row in product['subject']['members']}, 'Product version marker is not in its release inventory: ' + name)
            regular_member(view, marker)
            require(view.read_bytes(marker).decode().strip() == manifest['cohort']['version'], 'delivered Product version differs: ' + name)
    for edge in manifest['dependency_edges']:
        expected = manifest['products'][edge['provider']]['subject']['sha256']
        require(edge.get('provider_subject_sha256') == expected, 'dependency binds a different Product subject')
    for name, component in manifest['components'].items():
        component_subject = subject(view, component['subject'], api)
        owner_rows = {r['path']: r for r in manifest['products'][component['owner']]['subject']['members']}
        require(all(owner_rows.get(r['path']) == r for r in component_subject['members']), 'component is not within exact owning Product subject: ' + name)
        refs = component['evidence']
        require(set(refs) == set(component['required_claims']), 'required component evidence missing/extra: ' + name)
        for claim, ref in refs.items():
            observed = evidence(view, ref, claim, manifest, api)
            require(component['owner'] in observed['subjects'], 'component evidence omits its actual owner subject: ' + name)
            if name in ('representation', 'unified_explorer', 'proof_reader', 'lean'):
                require('stdo_representation' in observed['subjects'], 'derived evidence omits current representation subject: ' + name)
    refs = manifest['qualification']['evidence']
    require(set(refs) == set(manifest['qualification']['required_claims']), 'whole-cohort evidence missing/extra')
    for claim, ref in refs.items():
        observed = evidence(view, ref, claim, manifest, api)
        require(set(observed['subjects']) == PRODUCTS, 'whole-cohort evidence does not bind all five Products')
    facts = manifest['components']['representation'].get('facts', {})
    require(facts.get('source_identity_sha256') == semantic['source_identity_sha256'], 'representation is not source current')
    for key in ('model', 'program', 'map', 'source_corpus'):
        value = pinned(view, facts[key], api)
        require(isinstance(value, dict), 'invalid representation asset: ' + key)
    import stable_release_evidence
    stable_release_evidence.model_facts(view, manifest, api)
    manager(view, manifest, api)
    return native(view, manifest, semantic, api)


def manager(view, manifest, api):
    facts = manifest['components']['manager']['facts']
    raw = pinned(view, facts['wheel'], api, as_json=False)
    version = manifest['cohort']['version']
    require(facts['wheel']['path'].endswith(f'/stdo_toolchain-{version}-py3-none-any.whl'), 'manager wheel name/version differs')
    root = path(facts['source_root'])
    expected = {}
    for name in view.files(root):
        if name.endswith('.py'):
            regular_member(view, name)
            expected['stdo_toolchain/' + name.removeprefix(root + '/')] = view.read_bytes(name)
    require(expected, 'manager source inventory missing')
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), 'manager wheel has duplicate members')
        actual = {name: archive.read(name) for name in names if name.startswith('stdo_toolchain/')}
        require(actual == expected, 'manager wheel does not match exact selected source')
        metadata = archive.read(f'stdo_toolchain-{version}.dist-info/METADATA').decode()
        require(f'Version: {version}' in metadata.splitlines() and 'Name: stdo-toolchain' in metadata.splitlines(), 'manager wheel metadata differs')
    require(f'__version__ = "{version}"' in expected['stdo_toolchain/__init__.py'].decode().splitlines(), 'manager runtime version differs')


def remote_refs(root, url, api):
    raw = api.git(root, 'ls-remote', url).stdout
    return dict((line.split('\t', 1)[1], line.split('\t', 1)[0]) for line in raw.splitlines())


def push_sources(root, manifest, revision, api):
    carrier = api.git(root, 'rev-parse', revision + '^{commit}').stdout.strip()
    sources = {manifest['cohort']['carrier_ref']: carrier}
    installed = pinned(api.View(root, revision), manifest['native']['manifest'], api)
    native_commit = installed['release']['commit']
    for name, product in manifest['products'].items():
        target = native_commit if name == 'specification_methodology' else carrier
        failures = []
        identity = api.annotated_ref(root, product['release_ref'], failures)
        require(not failures and identity and identity[1] == target, 'local Product tag must be annotated at exact subject: ' + name)
        sources[product['release_ref']] = identity[0]
        if product.get('release_branch') is not None:
            require(api.direct_ref_oid(root, product['release_branch']) == target, 'local release branch differs: ' + name)
            sources[product['release_branch']] = target
    require(api.direct_ref_oid(root, manifest['cohort']['carrier_ref']) == carrier, 'local carrier differs from frozen candidate')
    return sources


def ref_graph(root, manifest, revision, phase, remote, api):
    require(revision, 'frozen --revision required at publication gates')
    publication = manifest['publication']; url = publication['repository_url']
    failures = []; api.validate_remote_endpoint(root, remote, url, failures)
    require(not failures, '; '.join(failures))
    sources = push_sources(root, manifest, revision, api)
    expectations = publication['expected_remote']
    require(set(expectations) == set(sources), 'remote expectation set must equal exact complete push set')
    observed = remote_refs(root, url, api)
    preserved = publication['preserved_immutable_refs']
    require(preserved and all(observed.get(ref) == oid for ref, oid in preserved.items()), 'preserved immutable publication changed or missing')
    historical = {ref for ref in observed if re.fullmatch(r'refs/tags/(?:(?:specification_methodology|stdo_representation|axiom_indexer|a_c|stdo_skills)/)?v[0-9]+\.[0-9]+\.[0-9]+(?:-rc\.[1-9][0-9]*)?(?:\^\{\})?', ref)
                  and ref.removesuffix('^{}') not in sources}
    require(set(preserved) == historical, 'preserved immutable snapshot omits or adds a release ref')
    version = manifest['cohort']['version']
    require(not any(ref.startswith(f'refs/tags/{name}/v{version}-rc.') for ref in observed for name in PRODUCTS)
            and not any(ref.startswith(f'refs/tags/v{version}-rc.') for ref in observed)
            and not any(ref in observed for ref in (f'refs/tags/v{version}', f'refs/tags/v{version}^{{}}')), 'stable version collides with an existing RC or historical bare cut')
    for ref in sources:
        if ref.startswith('refs/tags/'):
            require(expectations[ref] is None, 'immutable tag must have create-only expectation')
        else:
            require(expectations[ref] is None or OBJECT.fullmatch(expectations[ref]), 'invalid mutable remote expectation')
        require(observed.get(ref) == (expectations[ref] if phase == 'refs' else sources[ref]), 'remote ref absent, unexpected or drifted: ' + ref)
    for name, product in manifest['products'].items():
        ref = product['release_ref']
        if phase != 'refs':
            expected_commit = api.annotated_ref(root, ref, failures := [])[1]
            require(not failures and observed.get(ref + '^{}') == expected_commit, 'remote Product tag is lightweight or has wrong peel: ' + name)
    refspecs = [f'{sources[ref]}:{ref}' for ref in sorted(sources)]
    plan = {'revision': sources[manifest['cohort']['carrier_ref']], 'repository_url': url,
            'expected_remote': expectations, 'preserved_immutable_refs': preserved, 'refspecs': refspecs}
    return {'repository_url': url, 'qualified_push_sha256': api.canonical_value_sha256(plan),
            'remote_expectations_sha256': api.canonical_value_sha256(expectations),
            'push_argv': ['git', 'push', '--atomic', *(f'--force-with-lease={r}:{expectations[r] or ""}' for r in sorted(sources)), url, *refspecs]}


def required_public_assets(view, manifest, api):
    """The native payload carries all components; its exact manifest and manager
    wheel are mandatory assets, plus any explicitly selected component assets.
    Required component membership is independently checked in native/installed
    inventories, not inferred from these asset names.
    """
    pub = manifest['publication']; version = manifest['cohort']['version']
    expected = {'stdo-v' + version + '-manifest.json': manifest['native']['manifest'],
                'stdo_toolchain-' + version + '-py3-none-any.whl': manifest['components']['manager']['facts']['wheel']}
    for component in manifest['components'].values():
        for ref in component.get('public_assets', []):
            require(ref['name'] not in expected, 'duplicate selected public component asset')
            expected[ref['name']] = ref
    assets = pub['assets']
    require(isinstance(assets, list) and len(assets) == len(expected) and {row['name'] for row in assets} == set(expected),
            'required public native/manager/component asset closure differs')
    release_url = pub['repository_url'].removesuffix('.git') + '/releases/download/specification_methodology%2Fv' + version + '/'
    for asset in assets:
        ref = expected[asset['name']]; raw = pinned(view, ref, api, as_json=False)
        require(asset['path'] == ref['path'] and asset['sha256'] == ref['sha256'] and asset['bytes'] == len(raw)
                and asset['url'] == release_url + asset['name'], 'public asset differs from required exact current artifact')
    require(pub['external_manifest_asset']['url'] == release_url + 'stack-release-v' + version + '.json', 'external manifest release URL differs')
    return assets


def public(view, manifest, manifest_path, receipt_path, receipt_sha256, api):
    pub = manifest['publication']; assets = required_public_assets(view, manifest, api)
    external = pub['external_manifest_asset']
    require(external['name'] == 'stack-release-v' + manifest['cohort']['version'] + '.json', 'external complete cohort manifest release asset missing')
    require(receipt_path and receipt_sha256, 'post-publication receipt and exact digest are required separately from frozen B')
    receipt_view = api.View(view.root)
    receipt = pinned(receipt_view, {'path': receipt_path, 'sha256': receipt_sha256}, api)
    require(receipt.get('kind') == 'stdo.public-cohort-readback/1' and receipt.get('status') == 'verified', 'fresh public readback did not verify')
    require(receipt.get('source_identity_sha256') == manifest['source']['source_identity_sha256'] and receipt.get('unauthenticated') is True, 'public readback provenance/source differs')
    require(receipt.get('assets') == assets and receipt.get('fresh_store') and receipt.get('installed_manifest_sha256') == manifest['native']['manifest']['sha256'], 'public byte inventory or fresh installed native differs')
    require(receipt.get('external_manifest') == {**external, 'sha256': api.sha256(view.read_bytes(manifest_path))}, 'public external manifest differs from exact frozen B')
    external_bytes = view.read_bytes(manifest_path)
    downloads = [*assets, {**external, 'bytes': len(external_bytes), 'sha256': api.sha256(external_bytes)}]
    for asset in downloads:
        require(asset['url'].startswith(pub['repository_url'].removesuffix('.git') + '/releases/download/'), 'asset URL is outside selected repository release')
        if asset['name'] != external['name']:
            pinned(view, asset, api, as_json=False)
        require(type(asset.get('bytes')) is int and 0 < asset['bytes'] <= 256 * 1024 * 1024, 'invalid public asset size')
        # A previous local file or provenance label is not public transport
        # evidence. Reacquire now with no credentials/cookies and exact bound.
        with urllib.request.urlopen(urllib.request.Request(asset['url'], headers={'User-Agent': 'stdo-cohort-verifier'}), timeout=45) as response:
            data = response.read(asset['bytes'] + 1)
        require(len(data) == asset['bytes'] and api.sha256(data) == asset['sha256'], 'fresh anonymous public asset differs: ' + asset['name'])
    observed = pinned(receipt_view, receipt['installed_qualification'], api)
    installed = pinned(receipt_view, observed['installation'], api)
    require(set(observed['subjects']) == PRODUCTS and installed['store'] == receipt['fresh_store'],
            'public installed qualification does not bind all Products in the declared fresh store')
    require(installed['native_root'] == str(__import__('pathlib').Path(receipt['fresh_store']) / 'releases' / manifest['cohort']['cut']),
            'public installed result names a different native root')
    actual_install = pinned(receipt_view, installed['install']['result'], api)
    require(actual_install['manifest_sha256'] == receipt['installed_manifest_sha256'] and actual_install['status'] == 'installed',
            'public fresh installation actual result differs')
    evidence(receipt_view, receipt['installed_qualification'], 'complete_installed_cohort', manifest, api)


def check(root, manifest_path, phase, revision, remote, api, receipt_path=None, receipt_sha256=None):
    try:
        view = api.View(root, revision); manifest = view.read_json(manifest_path)
        content(view, manifest, api)
        if phase in ('refs', 'published', 'public'):
            ref_graph(root, manifest, revision, phase, remote, api)
        if phase == 'public':
            public(view, manifest, manifest_path, receipt_path, receipt_sha256, api)
        return []
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError, IndexError, subprocess.CalledProcessError, subprocess.TimeoutExpired, urllib.error.URLError, zipfile.BadZipFile, StopIteration) as exc:
        return ['stable cohort: ' + str(exc)]
