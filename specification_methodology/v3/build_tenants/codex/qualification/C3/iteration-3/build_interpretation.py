"""Compile the current determination account into a relocatable a_c.text draft.

Freeze the documentary subject before generating these derived package members.
Compilation preserves authored logic and omissions; it does not decide fidelity.
The separately owned RC2 checker remains unchanged.
"""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

HERE = Path(__file__).resolve().parent
TENANT = HERE.parents[2]
PACKAGE = TENANT / "successor"
OUTPUT = PACKAGE / "interpretation"
ACCOUNT = HERE / "DETERMINATIONS.json"
INSTALL = TENANT / "a_c/install/axiom_indexer-v2.5.1-rc.2"
TOOL = INSTALL / "build_tenants/core/code/ac.py"
COMMON_INPUT = "355aa8655cca9c6ba6cf5c414f9bea3032ae89fd"
THEORY_URI = "stdo://releases/v2.5.1-rc.2/"
MANIFEST_SHA = "3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782"
THEORY_SHA = "cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d"
TOOL_SHA = "5a2e0cb503cf598bbaea215270373b87a0928222be272f33d951550b0d16e6c8"
URI = "repo://codex-v3/successor/"
NS = "urn:codex-stdo3:iteration-3-r2:"
VOCAB = URI + "interpretation/SIGNATURE.md#"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text())


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def text(value):
    return value if isinstance(value, str) else json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def slug(value):
    value = unicodedata.normalize("NFC", re.sub(r"<[^>]*>", "", value).replace("`", "").lower())
    return re.sub(r"\s", "-", re.sub(r"[^\w\-\s]", "", value))


def original_source_uri(source):
    path = source["path"]
    if Path(path).is_absolute() or ".." in Path(path).parts or path.startswith("interpretation/"):
        raise ValueError("Source account must bind a documentary package member: " + path)
    anchor = source.get("anchor", "").lstrip("#")
    return URI + path + ("#" + anchor if anchor else "")


def native_slug(title):
    """The exact fragment rule of the separately pinned RC2 checker."""
    base = re.sub(r"[^\w\- ]", "", title.strip().lower(), flags=re.UNICODE)
    return re.sub(r"[\s\-]+", "-", base).strip("-")


def native_source_anchor(source, raw):
    """Bind a carrier route to the same exact original heading and body.

    Semantic/source identities are unchanged. The old checker collapses runs
    of hyphens; the source account uses its normal Markdown owner coordinate.
    Any alias collision or nonmatching coordinate refuses the adapter.
    """
    anchor = source.get('anchor', '').lstrip('#')
    if not anchor:
        return ''
    lines = raw.decode('utf-8').splitlines(keepends=True)
    headings, github_counts, native_counts = [], {}, {}
    fenced = None
    for lineno, line in enumerate(lines, 1):
        fence = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        in_fence = fenced is not None
        if fence:
            mark = fence.group(1)
            if fenced is None:
                fenced = (mark[0], len(mark))
            elif mark[0] == fenced[0] and len(mark) >= fenced[1]:
                fenced = None
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        title = match.group(1)
        native_base = native_slug(title)
        n = native_counts.get(native_base, 0)
        native_counts[native_base] = n + 1
        native = native_base if n == 0 else native_base + '-' + str(n)
        original = None
        if not in_fence:
            original_base = slug(title)
            g = github_counts.get(original_base, 0)
            github_counts[original_base] = g + 1
            original = original_base if g == 0 else original_base + '-' + str(g)
        headings.append({'line': lineno, 'original': original, 'native': native})
    candidates = [h for h in headings if h['original'] == anchor]
    if len(candidates) != 1:
        raise ValueError('Ambiguous or nonmatching original source anchor: ' + source['path'] + '#' + anchor)
    heading = candidates[0]
    if source.get('start_line') and source['start_line'] != heading['line']:
        raise ValueError('Source anchor and exact heading coordinate disagree: ' + source['path'] + '#' + anchor)
    if sum(h['native'] == heading['native'] for h in headings) != 1:
        raise ValueError('Ambiguous native source fragment: ' + source['path'] + '#' + heading['native'])
    if source.get('body_sha256') and 'start_line' in source and 'end_line' in source:
        body = ''.join(lines[source['start_line']-1:source['end_line']]).encode()
        if sha(body) != source['body_sha256']:
            raise ValueError('Source adapter body pin differs: ' + source['path'] + '#' + anchor)
    return heading['native']


def source_uri(source):
    original_source_uri(source)  # Validate the original documentary route.
    anchor = native_source_anchor(source, (PACKAGE / source['path']).read_bytes())
    return URI + source['path'] + ('#' + anchor if anchor else '')


def unit_frame(identifier):
    heading = 'Unit ' + native_slug(identifier) + ' ' + sha(identifier.encode())[:12]
    return heading, URI + 'interpretation/FRAMES.md#' + native_slug(heading)


def sources(row):
    return sorted({source_uri(s) for s in [row["owner"], *row.get("supporting_sources", [])]})


def clause_id(identifier):
    return NS + "clause:" + identifier


def literal(role, value):
    return {"role": VOCAB + role, "literal": value if value is None or isinstance(value, (str, int, float, bool)) else text(value)}


def reference(role, value):
    return {"role": VOCAB + role, "ref": value}


def verify_dependencies(theory):
    """Verify the exact selected copies before invoking their mechanics."""
    if sha((theory / "manifest.json").read_bytes()) != MANIFEST_SHA or sha((theory / "standards/AXIOMATIC_CALCULUS.md").read_bytes()) != THEORY_SHA:
        raise ValueError("Fixed encoding theory verification failed")
    receipt = read(TENANT / "a_c/INSTALL_RECEIPT.json")
    expected_identity = {"tag_object": "9bff233c3f0e7d80f63307fa3b12800dd3db681c",
        "commit": "9a9c479776ffd974fbcafcf48341980918209aef", "tree": "3a553ceb8db2e8de4ac779abdc2a2ceae5708c7d",
        "subtree": "6dae168d0a258ca506f4d6b9d5cd0a0c835fb546"}
    if receipt["identity"] != expected_identity:
        raise ValueError("Checker receipt is not the selected immutable identity")
    expected = {m["path"] for m in receipt["members"]}
    actual = {str(p.relative_to(INSTALL)) for p in INSTALL.rglob("*") if p.is_file() or p.is_symlink()}
    if actual != expected or len(expected) != 7:
        raise ValueError("Installed checker membership has drifted")
    for member in receipt["members"]:
        path = INSTALL / member["path"]
        data = os.readlink(path).encode() if path.is_symlink() else path.read_bytes()
        frozen = subprocess.check_output(["git", "show", expected_identity["commit"] + ":axiom_indexer/" + member["path"]], cwd=TENANT)
        if path.is_symlink() != (member["type"] == "symlink") or sha(data) != member["sha256"] or data != frozen:
            raise ValueError("Installed checker member differs: " + member["path"])
    stream = "".join(m["sha256"] + "  " + m["type"] + "  " + m["path"] + "\n" for m in sorted(receipt["members"], key=lambda r: r["path"]))
    if sha(stream.encode()) != "55a2061bd55ca29e349318a2869bc13518374ef2fa764a73b1688e76d35a63c1" or sha(TOOL.read_bytes()) != TOOL_SHA:
        raise ValueError("Checker aggregate or executable differs")
    return {"install_root": str(INSTALL), "member_count": len(expected), "identity": expected_identity,
            "inventory_sha256": sha(stream.encode()), "executable_sha256": TOOL_SHA,
            "theory_root": str(theory.resolve()), "theory_manifest_sha256": MANIFEST_SHA, "theory_member_sha256": THEORY_SHA}


def documentary_inventory(commit, package=PACKAGE):
    repo = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=TENANT, text=True).strip())
    exact = subprocess.check_output(["git", "rev-parse", commit + "^{commit}"], cwd=repo, text=True).strip()
    prefix = str(package.relative_to(repo))
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", exact, "--", prefix], cwd=repo, text=True).splitlines()
    frozen = {n[len(prefix) + 1:]: n for n in names if not n[len(prefix) + 1:].startswith("interpretation/")}
    actual = {str(p.relative_to(package)): p for p in package.rglob("*") if p.is_file() and not str(p.relative_to(package)).startswith("interpretation/")}
    if set(frozen) != set(actual):
        raise ValueError("Documentary subject membership differs from source freeze")
    members = []
    for name in sorted(frozen):
        data = actual[name].read_bytes()
        if actual[name].is_symlink() or data != subprocess.check_output(["git", "show", exact + ":" + frozen[name]], cwd=repo):
            raise ValueError("Documentary member differs from source freeze: " + name)
        members.append({"path": name, "sha256": sha(data), "bytes": len(data)})
    return exact, members


# These are the current semantic fields. Qualification history is not a second
# constitutional surface. An unclassified field is an error, never silent loss.
SEMANTIC_FIELDS = {
    'id', 'family', 'representation_kind', 'owner', 'supporting_sources',
    'predicate', 'definition', 'applicability', 'obligations',
    'permissions_exceptions', 'dependencies', 'dependency_relations',
    'result_mapping', 'argument', 'inputs', 'source_references', 'scope_refs',
    'source_clause_ids', 'source_clauses', 'semantic_roles', 'source_clause_roles',
    'signature_components', 'population_map', 'fields', 'closed_fields', 'tuple',
    'states', 'concept_identities', 'contract_bindings', 'imported_concepts',
    'translation', 'locator_meaning', 'state_classifier', 'decision_rule',
    'function_contracts', 'causal_equation', 'compute_predicates', 'semantic_cut',
    'effect_predicates',
}
EVIDENCE_FIELDS = {
    'coverage_standing', 'interpretation_standing', 'proof_standing_ref',
    'prior_standing', 'reduction', 'remaining_work_ref', 'source_excerpt',
    'unrepresented_scope', 'consumers', 'family_ref', 'applicability_ref',
    'unit_kind', 'owner_body_sha256', 'source_member_sha256',
    'bounded_discriminator_projection', 'ready_row_repair',
}
# Exact metadata values only: modal standing such as external_required remains.
CONSTRUCTION_STANDING = {
    'author conditional argument; no independent entailment proof',
    'author_semantic_mapping_not_independently_qualified',
    'authored bounded definition binding', 'authored conditional support, not independent entailment proof',
    'authored_bounded_definition_argument', 'authored_conditional_argument_account_not_independent_proof',
    'authored_conditional_argument_not_independent_proof', 'conditional_source_argument_not_independent_proof',
    'source_mapping_bound_not_independently_qualified',
    'author_source_to_representation_mapping_not_fidelity_verdict',
    'Author conditional argument; source-specific specialization and policy are explicit; independent entailment/fidelity judgment remains separate.',
    'authored_conditional_argument_not_independent_entailment_proof',
}
LOCAL_REF_KEYS = {'value_ref', 'local_predicate_ref', 'local_binding_ref'}
SHARED_REF_KEYS = {'contract_ref', 'scope_ref', 'input_ref'}


def semantic_projection(account):
    """Separate current meaning from construction evidence, without grading it."""
    if account.get('schema_version') != 'stdo.determinations.v1.4':
        raise ValueError('A frozen consolidated v1.4 account is required')
    exclusions = []

    def clean(value, path):
        if isinstance(value, list):
            return [clean(v, path + '/' + str(i)) for i, v in enumerate(value)]
        if not isinstance(value, dict):
            return value
        out = {}
        for key, item in value.items():
            location = path + '/' + key
            if key == 'standing' and isinstance(item, str) and item in CONSTRUCTION_STANDING:
                exclusions.append({'path': location, 'value': item, 'reason': 'construction qualification metadata'})
            elif key == 'nonclaims' and item == 'Author construction only: no evidence that a real consumer instance satisfies these predicates.':
                exclusions.append({'path': location, 'value': item, 'reason': 'construction qualification metadata'})
            elif key == 'standing' and item == 'source-declared research pin only; companion not acquired or independently revalidated in this activation; later research changes do not amend this source':
                out[key] = 'source-declared research pin only; later research changes do not amend this source'
                exclusions.append({'path': location, 'value': item,
                    'removed_text': 'companion not acquired or independently revalidated in this activation',
                    'retained_value': out[key], 'reason': 'activation-specific acquisition record; required input and source policy retained'})
            else:
                out[key] = clean(item, location)
        return out

    rows = []
    for row in account['determinations']:
        extra = set(row) - SEMANTIC_FIELDS - EVIDENCE_FIELDS
        if extra:
            raise ValueError(row['id'] + ': unclassified account fields ' + ', '.join(sorted(extra)))
        if row.get('unrepresented_scope') or row.get('remaining_work_ref'):
            raise ValueError(row['id'] + ': unfinished construction cannot become a source residual')
        current = {k: v for k, v in row.items() if k in SEMANTIC_FIELDS}
        rows.append(clean(current, '/determinations/' + row['id']))
    contracts = clean(account.get('semantic_contracts', {}), '/semantic_contracts')
    return {'kind': 'stdo.current-semantic-account', 'schema_version': 1,
            'determinations': sorted(rows, key=lambda r: r['id']),
            'semantic_contracts': dict(sorted(contracts.items()))}, exclusions


def local_value(row, path):
    value = row
    for component in path.split('.'):
        if not isinstance(value, dict) or component not in value:
            raise ValueError(row['id'] + ': unresolved local semantic field ' + path)
        value = value[component]
    return value


def semantic_edges(value, ids, contracts, row=None):
    """Resolve declared exact references; prose resemblance supplies no edge."""
    edges = []

    def walk(item, path=()):
        if isinstance(item, dict):
            for key, child in item.items():
                walk(child, path + (key,))
        elif isinstance(item, list):
            for i, child in enumerate(item):
                walk(child, path + (str(i),))
        elif isinstance(item, str):
            key = next((p for p in reversed(path) if not p.isdigit()), '')
            pointer = '/' + '/'.join(p.replace('~', '~0').replace('/', '~1') for p in path)
            if key in LOCAL_REF_KEYS:
                if row is None:
                    raise ValueError('Local field reference outside a determination: ' + item)
                local_value(row, item)
                return
            if key in SHARED_REF_KEYS:
                if item not in contracts:
                    raise ValueError('Unresolved semantic contract: ' + item)
                edges.append({'pointer': pointer, 'relation': 'shared-contract', 'target': contract_id(item)})
            elif item in ids:
                if path == ('id',):
                    return
                relation = 'semantic-reference'
                if 'dependency_relations' in path:
                    relation = 'declared-dependency-relation'
                elif path and path[0] == 'dependencies':
                    relation = 'declared-dependency'
                elif path and path[0] == 'scope_refs':
                    relation = 'scope-reference'
                elif 'argument' in path or 'premises' in path:
                    relation = 'argument-reference'
                elif any(p in {'source_refs', 'source_references'} for p in path):
                    relation = 'source-reference'
                elif key in {'owner', 'owners', 'owner_refs', 'effect_owner', 'composition_owner', 'premise_owner'}:
                    relation = 'governing-owner'
                edges.append({'pointer': pointer, 'relation': relation, 'target': clause_id(item)})
            elif re.fullmatch(r'F[1-6]', item) and ('argument' in path or 'premises' in path):
                target = 'FOUNDATIONS.foundational-commitments'
                if target not in ids:
                    raise ValueError('Foundational premise owner absent')
                edges.append({'pointer': pointer, 'relation': 'foundation-premise-owner', 'target': clause_id(target)})
            elif path and path[0] == 'dependencies':
                raise ValueError('Unresolved determination dependency: ' + item)
            elif 'dependency_relations' in path and key in {'id', 'target', 'target_id'}:
                raise ValueError('Unresolved typed dependency relation: ' + item)
            elif key in {'owner_refs', 'source_references', 'source_refs', 'scope_refs', 'owner', 'owners', 'effect_owner', 'composition_owner', 'premise_owner', 'contract', 'id'} and re.match(r'^[A-Z][A-Z_]+\.', item):
                raise ValueError('Unresolved owned semantic reference: ' + item)
    walk(value)
    return sorted(edges, key=lambda r: (r['pointer'], r['relation'], r['target']))


def contract_id(identifier):
    return NS + 'contract:' + identifier


def validate_account(current, package=PACKAGE):
    rows = current.get('determinations')
    if not isinstance(rows, list) or not rows:
        raise ValueError('The current semantic account is absent or empty')
    ids = {r['id'] for r in rows}
    contracts = current.get('semantic_contracts', {})
    if len(ids) != len(rows) or any(not re.fullmatch(r'[A-Za-z0-9_.:-]+', i) for i in ids):
        raise ValueError('Duplicate or non-URI-safe determination identity')
    if len({slug(i) for i in ids}) != len(ids):
        raise ValueError('Determination names produce ambiguous frame anchors')
    for row in rows:
        kind = row['representation_kind']
        if kind not in {'constraint', 'definition_data', 'consumer_binding', 'non_deciding_locator'}:
            raise ValueError(row['id'] + ': unknown representation kind')
        if kind == 'constraint' and not row.get('predicate'):
            raise ValueError(row['id'] + ': constraint has no predicate')
        if kind == 'definition_data' and not (row.get('definition') or row.get('predicate')):
            raise ValueError(row['id'] + ': definition has no meaning')
        if kind == 'consumer_binding' and not row.get('predicate') and not (row.get('definition') and row.get('dependencies')):
            raise ValueError(row['id'] + ': consumer lacks predicate or defined dependency relation')
        if kind == 'non_deciding_locator' and row.get('predicate'):
            raise ValueError(row['id'] + ': locator asserts a deciding predicate')
        if kind != 'non_deciding_locator':
            for field in ('applicability', 'argument', 'result_mapping'):
                if not row.get(field):
                    raise ValueError(row['id'] + ': missing ' + field)
        for source in [row['owner'], *row.get('supporting_sources', [])]:
            source_uri(source)
            path = package / source['path']
            if not path.is_file() or path.is_symlink():
                raise ValueError('Missing independent source member: ' + source['path'])
            raw = path.read_bytes()
            digest = source.get('member_sha256') or source.get('sha256')
            if digest and sha(raw) != digest:
                raise ValueError('Stale source member: ' + source['path'])
            if source.get('unit_scope') == 'whole_member':
                body = raw
            elif 'start_line' in source and 'end_line' in source:
                body = b''.join(raw.splitlines(keepends=True)[source['start_line']-1:source['end_line']])
            else:
                body = None
            if body is not None and source.get('body_sha256') and sha(body) != source['body_sha256']:
                raise ValueError('Stale source body: ' + row['id'])
        raw = (package / row['owner']['path']).read_bytes()
        block_ids = set()
        for block in row.get('source_clauses', []):
            if block['id'] in block_ids or sha(raw[block['byte_start']:block['byte_end']]) != block['sha256']:
                raise ValueError('Stale or duplicate source block: ' + row['id'] + '#' + block['id'])
            block_ids.add(block['id'])
        for block_id in row.get('source_clause_ids', []):
            local_block = block_id.removeprefix(row['id'] + '#')
            if local_block not in block_ids:
                raise ValueError('Unresolved source block: ' + row['id'] + '#' + block_id)
        block_pins = {b['id']: b for b in row.get('source_clauses', [])}
        for relation in row.get('source_clause_roles', []):
            block = block_pins.get(relation['source_block_id'])
            if not block or relation['source_clause_id'] != row['id'] + '#' + block['id'] or any(
                relation[source_field] != block[pin_field]
                for source_field, pin_field in [('source_block_sha256', 'sha256'), ('source_byte_start', 'byte_start'), ('source_byte_end', 'byte_end')]
            ):
                raise ValueError('Source-clause relation has stale or ambiguous coordinates: ' + row['id'])
            for binding in relation['represented_at']:
                pointer = binding['pointer']
                if not isinstance(pointer, str) or not pointer.startswith('/'):
                    raise ValueError('Invalid local representation pointer: ' + row['id'])
                value = row
                try:
                    for part in pointer[1:].split('/'):
                        part = part.replace('~1', '/').replace('~0', '~')
                        value = value[int(part)] if isinstance(value, list) else value[part]
                except (KeyError, IndexError, TypeError, ValueError):
                    raise ValueError('Unresolved local representation pointer: ' + row['id'] + pointer)
        semantic_edges(row, ids, contracts, row)
    for key, contract in contracts.items():
        if not re.fullmatch(r'[A-Za-z0-9_.:-]+', key):
            raise ValueError('Invalid shared semantic identity: ' + key)
        semantic_edges(contract, ids, contracts)
    return rows


def contract_sources(current):
    """Ground a shared meaning in declared owners and its bound source users."""
    rows = {r['id']: r for r in current['determinations']}
    contracts = current['semantic_contracts']
    refs = {key: set() for key in contracts}
    users = {key: set() for key in contracts}
    shared_links = {key: set() for key in contracts}
    for row in rows.values():
        for edge in semantic_edges(row, set(rows), contracts, row):
            if edge['target'].startswith(NS + 'contract:'):
                users[edge['target'].removeprefix(NS + 'contract:')].update(sources(row))
    for key, value in contracts.items():
        for edge in semantic_edges(value, set(rows), contracts):
            target = edge['target']
            if target.startswith(NS + 'clause:'):
                refs[key].update(sources(rows[target.removeprefix(NS + 'clause:')]))
            else:
                shared_links[key].add(target.removeprefix(NS + 'contract:'))
        # Declared source owners suffice; otherwise retain source-bound users.
        # Do not enumerate every consumer again when the owner is explicit.
        if not any(edge['relation'] == 'governing-owner' for edge in semantic_edges(value, set(rows), contracts)):
            refs[key].update(users[key])
    changed = True
    while changed:
        changed = False
        for key, linked in shared_links.items():
            for target in linked:
                before = len(refs[target])
                refs[target].update(refs[key])
                changed = changed or len(refs[target]) != before
    for key, value in refs.items():
        if not value:
            raise ValueError('Shared contract has no declared owner or source-bound user: ' + key)
    return {key: sorted(value) for key, value in refs.items()}


def family_mappings(current):
    groups = {}
    for row in current['determinations']:
        groups.setdefault(row['family'], []).append(row['id'])
    return [{'family': family,
             'index': NS + 'index:family:' + slug(family) + '-' + sha(family.encode())[:12],
             'source_frame': URI + 'interpretation/FRAMES.md#' + native_slug('Family ' + native_slug(family) + ' ' + sha(family.encode())[:12]),
             'source_unit_ids': sorted(roots)}
            for family, roots in sorted(groups.items()) if len(roots) > 1]


def build_program(current):
    """Encode authored meanings and typed references without evaluating them."""
    rows = current['determinations']
    ids = {r['id'] for r in rows}
    contracts = current['semantic_contracts']
    shared_sources = contract_sources(current)
    program = {'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
        'uri': NS + 'program:method-determinations', 'calculus_ref': THEORY_URI + 'standards/AXIOMATIC_CALCULUS.md',
        'source_basis': URI, 'frame_refs': [], 'vocabulary_refs': [], 'symbols': [], 'clauses': [], 'residuals': [], 'frame_indexes': []}
    mapping, families = [], {}
    frame_sections = ['# Interpretation Acquisition Frames\n\nSelect an index explicitly for the task. The checker follows declared references; it does not evaluate their predicates or supply task inputs. These optional selectors impose no per-row evaluation, actor or execution partition. A family label is source-account grouping data, not an owner, transformation or complete activation contract.\n']

    def arguments(value, row=None):
        # One exact object literal keeps structure, order and local field refs.
        # Paired pointer/ref arguments expose actual links to native closure.
        args = [literal('semantic-record', value)]
        for edge in semantic_edges(value, ids, contracts, row):
            args.extend([literal('reference-location', edge['pointer']), reference(edge['relation'], edge['target'])])
        return args

    for key, contract in sorted(contracts.items()):
        program['clauses'].append({'uri': contract_id(key), 'clause_type': 'relation',
            'operator': VOCAB + 'shared-contract', 'arguments': arguments(contract),
            'statement': 'Shared semantic contract ' + key, 'source_refs': shared_sources[key]})
    for row in sorted(rows, key=lambda r: r['id']):
        identifier, refs = row['id'], sources(row)
        kind = row['representation_kind']
        target = clause_id(identifier)
        frame_heading, frame = unit_frame(identifier)
        index = NS + 'index:' + identifier
        is_constraint = kind == 'constraint' or (kind == 'consumer_binding' and bool(row.get('predicate')))
        operator = 'requires' if is_constraint else ('locates' if kind == 'non_deciding_locator' else 'defines')
        # Owner coordinates remain native source routes. Exact block pins stay
        # with the semantic row so a local cN reference is usable after projection;
        # source bodies remain only at their owners.
        semantic = {k: v for k, v in row.items() if k not in {'owner', 'supporting_sources', 'family'}}
        program['clauses'].append({'uri': target, 'clause_type': 'constraint' if is_constraint else 'relation',
            'operator': VOCAB + operator, 'arguments': arguments(semantic, row),
            'statement': ('Constraint ' if is_constraint else 'Relation ') + identifier, 'source_refs': refs})
        families.setdefault(row['family'], []).append(target)
        program['frame_refs'].append(frame)
        program['frame_indexes'].append({'uri': index, 'frame_ref': frame,
            'scope': 'Apply the source-bound ' + kind.replace('_', ' ') + ' ' + identifier + ' with its declared conditions, references and task inputs.',
            'clause_refs': [target], 'residual_refs': [], 'source_refs': sorted(set(refs + [frame]))})
        original_refs = sorted({original_source_uri(v) for v in [row['owner'], *row.get('supporting_sources', [])]})
        frame_sections.append('## ' + frame_heading + '\n\nIndex: `' + index + '`.\n\n' + '\n'.join('- [' + ref.removeprefix(URI) + '](' + ref.replace(URI, '../') + ')' for ref in original_refs) + '\n')
        mapping.append({'id': identifier, 'owner': row['owner'], 'source': original_source_uri(row['owner']),
                        'native_source': source_uri(row['owner']), 'representation_kind': kind,
                        'clause': target, 'index': index})
    for family, roots in sorted(families.items()):
        if len(roots) < 2:
            continue  # The individual index already selects this exact root.
        identity = slug(family) + '-' + sha(family.encode())[:12]
        heading = 'Family ' + native_slug(family) + ' ' + sha(family.encode())[:12]
        frame, index = URI + 'interpretation/FRAMES.md#' + native_slug(heading), NS + 'index:family:' + identity
        program['frame_refs'].append(frame)
        program['frame_indexes'].append({'uri': index, 'frame_ref': frame,
            'scope': 'Acquire the declared ' + family + ' relations and their typed references for a separately bound task.',
            'clause_refs': sorted(roots), 'residual_refs': [], 'source_refs': [frame]})
        frame_sections.append('## ' + heading + '\n\nIndex: `' + index + '`. Select only when this family is material to the task.\n')
    program['vocabulary_refs'] = sorted({a['role'] for c in program['clauses'] for a in c['arguments']} | {c['operator'] for c in program['clauses']})
    program['frame_refs'] = sorted(set(program['frame_refs']))
    for key in ('symbols', 'clauses', 'residuals', 'frame_indexes'):
        program[key] = sorted(program[key], key=lambda r: r['uri'])
        if len({r['uri'] for r in program[key]}) != len(program[key]):
            raise ValueError('Duplicate generated ' + key + ' identity')
    return program, mapping, '\n'.join(frame_sections)


SIGNATURE = '''# Method Interpretation Vocabulary

The interpretation preserves source-owned meanings and their explicit relations.
Structured semantic records use canonical JSON string literals because the a_c.text
carrier accepts scalar literals. The record retains field names, list order,
conditions, exceptions, local field references and result mappings. The native
checker follows explicit references; it does not execute these meanings.

## Requires

The bound predicate has the declared applicability, obligations, permitted
choices and exceptions, inputs and result relation together. A constraint is not
a satisfied instance or a grant. Definitions embedded in it retain their type.

## Defines

The record declares data or a consumer-to-owner relation. A definition is not a
Boolean verdict. Embedded obligations retain their declared scope; any assertion
of conformance requires its own bound predicate and admissible evidence.

## Locates

The record names a non-deciding source location. A locator adds no requirement,
permission, unknown task outcome or unfinished-construction obligation.

## Shared contract

The record defines a meaning reused through an exact contract identity. Each use
retains its local binding and conditions. Reuse does not merge distinct owners.

## Semantic record

The literal is the exact current semantic object. Fields such as applicability,
predicate, definition, argument, input contracts and result mapping keep their
own meanings. Row-local source-block names resolve through the row's exact byte-range and
digest pins against its source owner. Local field references select fields in
the same row.
Required future inputs are conditional contracts, not claims that the source is
missing or that an actual task has an unknown result.

## Reference location

This JSON Pointer identifies the occurrence in the preceding semantic record.
The next argument supplies its typed native target. The pointer/ref pair preserves
the distinction between an occurrence, its target identity and its relation.

## Declared dependency

The source account declares this dependency. Its typed dependency relation and
local conditions determine why it is relevant; the link alone is not a premise.

## Declared dependency relation

The target belongs to the exact relation record at the referenced pointer.
Its kind, scope and qualifications remain in that record. Governing conditions,
refinements and provenance are not interchangeable relations.

## Scope reference

The target supplies the source-owned scope qualification attached to this row.
Its actual applicability must be established for the task; following the link
never establishes adoption or universal applicability.

## Argument reference

The target participates in the declared argument, with the premise kind,
conditional consequence and additional policy retained. An argument reference
neither proves entailment nor supplies instance evidence.

## Source reference

The target supplies source correspondence or provenance under the declared
relation. Provenance does not confer governing authority or imply entailment.

## Governing owner

The named owner supplies only the meaning assigned to it by the local binding.
A result owner does not supply task truth, disposition authority or performance.

## Foundation premise owner

The target owns the exact F1–F6 premise named at the pointer. The premise name and
conditional argument remain in the record; finite capacity does not establish
purpose, identity, composition or authority without their stated premises.

## Semantic reference

The exact target participates in the named local semantic relation. The record,
not reference closure, determines its meaning and whether it governs an action.
'''

README = '''# Current Method Interpretation

[program.json](program.json) expresses the current source-bound meanings in the
[a_c.text vocabulary](SIGNATURE.md). Its [map](map.json) supports explicit
[acquisition indexes](FRAMES.md). The [current semantic account](source-account.json)
preserves source-body and block pins with the typed meanings; [MAPPING.json](MAPPING.json)
connects each source unit and optional multi-root group to its index. The indexes
are acquisition selectors, not required evaluations, actors or execution
partitions. Family labels add no semantic owner or transformation. The mapping
retains original owner coordinates separately from native checker routes; a
carrier fragment must resolve uniquely to that same heading and body. These
representations refer to
the owning standards; they create no second authority for method law.

Select an index for the actual task. Bind the subject, governing basis and
applicability; acquire required observations, grants and source-owned conditions
before dependent action. Definitions remain data, constraints require evidence,
and a locator creates no deciding rule. A reference-only or materialized view
preserves authored references without evaluating their truth or granting work.

## Representation coordinates

[SOURCE_INVENTORY.json](SOURCE_INVENTORY.json) binds four distinct coordinates:

- The encoding theory is the exact STDO v2.5.1-rc.2 Axiomatic Calculus member.
- The subject interpretation is this program over the named documentary source.
- The carrier is the a_c.text JSON structure and its vocabulary.
- The checker is the separately verified Axiom Indexer RC2 implementation.

The successor's AXIOMATIC_CALCULUS is part of the interpreted subject. It does not
silently replace the encoding theory. The documentary inventory excludes this
derived interpretation to avoid self-reference. Complete-package identity is
bound by the package's external inventory.

## Mechanical use

Run from this package root with separately verified theory and checker installs:

```sh
python3 -B interpretation/bindings.py --theory-root /absolute/verified/rc2 > /absolute/work/bindings.json
python3 -B /absolute/verified/axiom-indexer/build_tenants/core/code/ac.py project \\
  --program interpretation/program.json --map interpretation/map.json \\
  --bindings /absolute/work/bindings.json --frame-index '<index from FRAMES.md>' \\
  --mode materialized --output /absolute/work/projection.json
```

Keep invocation outputs outside the package. The binding procedure verifies the
exact theory and documentary pins. Map or source drift refuses projection;
changed meaning requires source-owned repair and affected review.

Validation establishes structure, reference closure and exact source observations.
It does not execute predicates, prove completeness or fidelity, authenticate task
inputs, grant an operation, accept a member or qualify a release.
'''

BINDINGS_SCRIPT = '''"""Emit invocation-local bindings after verifying supplied source and theory."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--theory-root", type=Path, required=True)
    args = parser.parse_args()
    package, theory = args.package_root.resolve(), args.theory_root.resolve()
    inventory = json.loads((package / "interpretation/SOURCE_INVENTORY.json").read_text())
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    basis = inventory["encoding_theory"]
    if digest(theory / "manifest.json") != basis["manifest_sha256"] or digest(theory / basis["member"]) != basis["member_sha256"]:
        raise SystemExit("The supplied theory does not match the fixed encoding basis")
    for row in inventory["document_members"]:
        relative = Path(row["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise SystemExit("Unsafe documentary source coordinate")
        path = package / relative
        if not path.is_file() or path.is_symlink() or digest(path) != row["sha256"]:
            raise SystemExit("Documentary subject drift: " + row["path"])
    for name, key in (("program.json", "program_file_sha256"), ("source-account.json", "semantic_account_sha256"), ("SIGNATURE.md", "vocabulary_sha256"), ("FRAMES.md", "frames_sha256"), ("MAPPING.json", "mapping_sha256")):
        path = package / "interpretation" / name
        if not path.is_file() or path.is_symlink() or digest(path) != inventory["interpretation"][key]:
            raise SystemExit("Interpretation carrier drift: " + name)
    print(json.dumps({"kind": "axiom-indexer.binding-set", "schema_version": 1,
        "bindings": [{"uri_prefix": "repo://codex-v3/successor/", "path": str(package)},
                     {"uri_prefix": basis["release_uri"], "path": str(theory)}]}, indent=2))


if __name__ == "__main__":
    main()
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-commit', required=True, help='Exact full documentary source freeze')
    parser.add_argument('--account-sha256', required=True, help='Exact frozen consolidated account digest')
    parser.add_argument('--account-commit', required=True, help='Exact commit containing the consolidated input account')
    parser.add_argument('--theory-root', type=Path, default=Path.home() / 'Library/Application Support/STDO/releases/v2.5.1-rc.2')
    args = parser.parse_args()
    if not re.fullmatch(r'[0-9a-f]{40}', args.source_commit) or not re.fullmatch(r'[0-9a-f]{40}', args.account_commit) or not re.fullmatch(r'[0-9a-f]{64}', args.account_sha256):
        raise ValueError('Full source/account commits and account digest are required')
    if sha(ACCOUNT.read_bytes()) != args.account_sha256:
        raise ValueError('Frozen consolidated account digest differs')
    repo = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HERE, text=True).strip())
    frozen_account = subprocess.check_output(['git', 'show', args.account_commit + ':' + str(ACCOUNT.relative_to(repo))], cwd=repo)
    if frozen_account != ACCOUNT.read_bytes():
        raise ValueError('Consolidated account differs from its named freeze')
    account = read(ACCOUNT)
    current, exclusions = semantic_projection(account)
    rows = validate_account(current)
    commit, members = documentary_inventory(args.source_commit)
    if account['subject']['source_commit'] != commit:
        raise ValueError('Account and documentary source freezes differ')
    dependencies = verify_dependencies(args.theory_root)
    program, mapping, frames = build_program(current)
    mapping_record = {'kind': 'stdo.method-interpretation-mapping', 'schema_version': 1,
        'document_source_input_commit': commit, 'rows': mapping, 'optional_family_indexes': family_mappings(current),
        'source_route_rule': 'Original Markdown owner coordinates and semantic IDs are preserved. Native source routes use the pinned RC2 checker fragment convention at the same uniquely resolved heading/body. Alias collisions or nonmatching coordinates refuse.'}
    source_inventory = {'kind': 'stdo.method-interpretation-source', 'schema_version': 1,
        'document_source_input_commit': commit, 'document_members': members,
        'excluded_from_documentary_subject': ['interpretation/'],
        'encoding_theory': {'release_uri': THEORY_URI, 'manifest_sha256': MANIFEST_SHA,
            'member': 'standards/AXIOMATIC_CALCULUS.md', 'member_sha256': THEORY_SHA},
        'checker': {'product': 'urn:stdo:product-definition:axiom-indexer',
            'release_ref': 'refs/tags/axiom_indexer/v2.5.1-rc.2', 'commit': '9a9c479776ffd974fbcafcf48341980918209aef',
            'executable_sha256': TOOL_SHA, 'inventory_sha256': '55a2061bd55ca29e349318a2869bc13518374ef2fa764a73b1688e76d35a63c1'},
        'interpretation': {'program_uri': program['uri'], 'program_file_sha256': sha(json_bytes(program)),
            'semantic_account_sha256': sha(json_bytes(current)), 'vocabulary_sha256': sha(SIGNATURE.encode()),
            'frames_sha256': sha(frames.encode()), 'mapping_sha256': sha(json_bytes(mapping_record))},
        'carrier': {'kind': 'axiom-indexer.axiomatic-program', 'schema_version': 1,
            'schema_sha256': sha((INSTALL / 'skills/axiomatize-corpus/references/program.schema.json').read_bytes())}}
    outputs = {'README.md': README.encode(), 'SIGNATURE.md': SIGNATURE.encode(), 'FRAMES.md': frames.encode(),
        'SOURCE_INVENTORY.json': json_bytes(source_inventory), 'MAPPING.json': json_bytes(mapping_record),
        'source-account.json': json_bytes(current), 'program.json': json_bytes(program), 'bindings.py': BINDINGS_SCRIPT.encode()}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, data in outputs.items():
        (OUTPUT / name).write_bytes(data)
    evidence = HERE / 'a_c/current'
    evidence.mkdir(parents=True, exist_ok=True)
    bindings = {'kind': 'axiom-indexer.binding-set', 'schema_version': 1,
        'bindings': [{'uri_prefix': URI, 'path': str(PACKAGE)}, {'uri_prefix': THEORY_URI, 'path': str(args.theory_root.resolve())}]}
    binding_path = evidence / 'bindings.json'
    binding_path.write_bytes(json_bytes(bindings))
    (evidence / 'DEPENDENCY_VERIFICATION.json').write_bytes(json_bytes(dependencies))
    result = subprocess.run([sys.executable, '-B', str(TOOL), 'validate', '--program', str(OUTPUT / 'program.json'),
        '--bindings', str(binding_path), '--output', str(evidence / 'validation.json'), '--emit-map', str(OUTPUT / 'map.json')], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    report = {'document_source_input_commit': commit, 'common_input_commit': COMMON_INPUT,
        'account_input_commit': args.account_commit, 'account_input_sha256': args.account_sha256, 'semantic_account_sha256': sha(json_bytes(current)),
        'determinations': len(rows), 'shared_contracts': len(current['semantic_contracts']),
        'clauses': len(program['clauses']), 'residuals': len(program['residuals']), 'indexes': len(program['frame_indexes']),
        'excluded_construction_metadata': exclusions,
        'source_route_adaptations': [{'id': r['id'], 'owner': r['owner'], 'original_source': r['source'], 'native_source': r['native_source']} for r in mapping if r['source'] != r['native_source']],
        'native_validation': 'passed',
        'package_members': [{'path': p.name, 'bytes': p.stat().st_size, 'sha256': sha(p.read_bytes())} for p in sorted(OUTPUT.iterdir()) if p.is_file()],
        'limits': ['Mechanical correspondence is not semantic completeness or fidelity.',
            'Conditional task-input contracts do not assert instance evidence or results.',
            'No actual-use, member acceptance, adoption or release conclusion.']}
    (evidence / 'GENERATION.json').write_bytes(json_bytes(report))
    print(json.dumps({k: report[k] for k in ('document_source_input_commit', 'determinations', 'shared_contracts', 'clauses', 'residuals', 'indexes', 'native_validation')}))


if __name__ == '__main__':
    main()
