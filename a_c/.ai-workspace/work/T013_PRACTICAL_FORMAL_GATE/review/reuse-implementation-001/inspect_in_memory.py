"""Independent source/in-memory controls. No gate, origin, proof or actor run.

Only selected function definitions are compiled from the pinned source. Origin
envelopes and bytes are synthetic dictionaries in memory, not verification.
Filesystem probes inspect ordinary existing ancestors of this review directory;
their hypothetical protected subtree does not exist. No source module imports.
"""
import ast
from copy import deepcopy
import hashlib
import hmac
import json
from pathlib import Path, PurePosixPath
import re
import stat
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
WORK = HERE.parents[1]
SUBJECT = WORK / 'reuse/implementation-001'
CANDIDATE = SUBJECT / 'candidate/a_c'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def definitions(path, names, namespace):
    tree = ast.parse(path.read_bytes())
    chosen = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
    assert {n.name for n in chosen} == set(names)
    exec(compile(ast.Module(body=chosen, type_ignores=[]), str(path), 'exec'), namespace)
    return namespace


results = []
def record(name, predicate):
    assert predicate, name
    results.append({'discriminator': name, 'outcome': 'passed'})


closed = json.loads((SUBJECT / 'CLOSED.json').read_bytes())
pins = json.loads((SUBJECT / 'SOURCE-PINS.json').read_bytes())
record('exact activation closure', sha((SUBJECT / 'CLOSED.json').read_bytes()) == '2cdcd1cebc7a91cdc0a4a54062a9d81676389b20e720042d22012cfd702afe45')
record('exact source pin manifest', sha((SUBJECT / 'SOURCE-PINS.json').read_bytes()) == '9f69e8559f33b4048071ea55541dd16de0dc34218d87e294ee9e0ba39cda2789')
record('exact candidate patch', sha((SUBJECT / 'candidate.patch').read_bytes()) == 'cdccf9fdd55ac558f1b248c8139ac7e7372fd9e2133feaa74d81f0c1299aebc6')
record('all 41 staged source pins', len(pins['candidate_sources']) == 41 and all(sha((CANDIDATE / n).read_bytes()) == h for n, h in pins['candidate_sources'].items()))
baseline = json.loads((SUBJECT / 'BASELINE.json').read_bytes())['copied_files']
refresh = json.loads((SUBJECT / 'BASELINE-REFRESH.json').read_bytes())
baseline[refresh['file']] = refresh['current_live_sha256']
record('all 38 refreshed before-source pins', len(baseline) == 38 and all(sha((SUBJECT / 'before/a_c' / n).read_bytes()) == h for n, h in baseline.items()))
record('exact eight modified and three new source members', sum(sha((CANDIDATE / n).read_bytes()) != h for n, h in baseline.items()) == 8 and len(set(pins['candidate_sources']) - set(baseline)) == 3)
record('declared math generator and support unchanged', all(sha((CANDIDATE / n).read_bytes()) == h for n, h in closed['conservation']['generator_and_support'].items()))
record('three author test logs pinned, not rerun', all(sha((SUBJECT / n).read_bytes()) == v['sha256'] for n, v in closed['validation']['tests'].items()))

source = CANDIDATE / 'build_tenants/lean/scripts/formal_reuse.py'
ns = {'hashlib': hashlib, 'hmac': hmac, 'json': json, 'Path': Path, 'stat': stat, 're': re,
      'ROOT': HERE, 'STORE_RELATIVE': '.cache/formal-origin-v1',
      'ORIGIN_SELECTION_PIN': '.cache/formal-origin-v1/selection.json',
      'ENTRY': 'a_c.formal-gate.local-entry/1', 'HINT': 'a_c.formal-gate.local-hint/1',
      'DOMAIN': b'independent-in-memory-discriminator-only\0',
      'METADATA': ('result.json', 'manifest.json', 'request.json', 'replay-request.json')}
for node in ast.parse(source.read_bytes()).body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        name = node.targets[0].id
        if name in ('STORE_RELATIVE', 'ORIGIN_SELECTION_PIN', 'ENTRY', 'HINT', 'DOMAIN', 'METADATA'):
            exec(compile(ast.Module(body=[node], type_ignores=[]), str(source), 'exec'), ns)
names = ('OriginError', 'canonical', 'sha', 'decode', '_hex', 'compatible',
         'member_name', 'origin_name', 'binding', 'lookup', '_unalias', '_contains', 'guard')
definitions(source, names, ns)
canonical = ns['canonical']
OriginError = ns['OriginError']

def refuses(function, *args, error_type=OriginError, **kwargs):
    try:
        function(*args, **kwargs)
    except error_type:
        return True
    return False


def identity(origin=None):
    p = {'scripts/formal_gate.py': '1' * 64, 'scripts/formal_reuse.py': '2' * 64,
         'profiles/proof-support-v1.json': '3' * 64}
    if origin is not None:
        p[ns['ORIGIN_SELECTION_PIN']] = origin
    return {'pins': p, 'sha256': sha(canonical(p))}


record('foreign and absent origin alone preserve cold compatibility', ns['compatible'](identity('a' * 64), identity('b' * 64)) and ns['compatible'](identity('a' * 64), identity()))
changed = identity('a' * 64)
changed['pins']['scripts/formal_reuse.py'] = '4' * 64
changed['sha256'] = sha(canonical(changed['pins']))
record('changed deciding helper refuses compatibility', not ns['compatible'](identity('a' * 64), changed))
changed = identity()
changed['pins']['caller-labelled-origin.json'] = '5' * 64
changed['sha256'] = sha(canonical(changed['pins']))
record('no caller-defined origin exception', not ns['compatible'](identity(), changed))
changed['sha256'] = '0' * 64
record('aggregate identity cannot be refreshed incorrectly', refuses(ns['compatible'], identity(), changed))
record('canonical request preserves boolean/integer distinction', canonical({'flag': True}) != canonical({'flag': 1}))
record('duplicate keys and nonfinite numbers refuse', all(refuses(ns['decode'], x) for x in (b'{"a":1,"a":2}', b'{"a":NaN}', b'{"a":1e999}')))

# Directly exercise actual lookup and binding functions over memory-only bytes.
memory = {}
class MemoryPath(PurePosixPath):
    def exists(self):
        return str(self) in memory
    def is_symlink(self):
        return False


def read(path, **kwargs):
    try:
        return memory[str(path)]
    except KeyError:
        raise FileNotFoundError(str(path)) from None


directory = MemoryPath('/synthetic-public-bundle')
root = MemoryPath('/synthetic-checker')
selected = {'origin_id': 'a' * 32}
selection_sha = 'b' * 64
synthetic_key = b'IN-MEMORY-DISCRIMINATOR-ONLY-KEY!!'
request = {'schema': 'synthetic-only', 'input': 'exact synthetic bytes', 'context_binding': {'flag': True}}
replay = deepcopy(request)
manifest = {'schema': 'a_c.formal-gate.bundle/1', 'members': {'request.json': sha(canonical(request)), 'replay-request.json': sha(canonical(replay)), 'actual-runtime.log': sha(b'NOT A FORMAL RESULT')}}
value = {'status': 'verified', 'requested_claims': ['synthetic-only'], 'checked_claims': ['synthetic-only'],
         'evidence': {'manifest_sha256': sha(canonical(manifest)), 'members': manifest['members']},
         'request_sha256': sha(canonical(request)), 'model': {'synthetic': True}, 'inputs': {'synthetic': True},
         'runtime_identity': identity('c' * 64),
         'observations': {'limits': {'timeout_seconds': 90}, 'support': {'synthetic': True},
                          'proof_modules': ['SYNTHETIC'], 'theorem_audit': {'not_a_theorem': []}}}
for name, raw in {'request.json': canonical(request), 'replay-request.json': canonical(replay),
                  'actual-runtime.log': b'NOT A FORMAL RESULT', 'manifest.json': canonical(manifest),
                  'result.json': canonical(value)}.items():
    memory[str(directory / name)] = raw
ns.update(ROOT=root, read=read, _read_regular=read, _unalias=lambda p: p,
          _origin=lambda: ((selected, selection_sha, synthetic_key), None))
body = ns['binding'](directory, 'cold', selected, selection_sha)
entry_id = sha(canonical(body))
entry = {'schema': ns['ENTRY'], 'body': body,
         'hmac_sha256': hmac.new(synthetic_key, ns['DOMAIN'] + canonical(body), hashlib.sha256).hexdigest()}
hint = {'schema': ns['HINT'], 'origin_id': selected['origin_id'], 'entry_id': entry_id, 'layout': 'cold'}
memory[str(directory / 'local-origin.json')] = canonical(hint)
entry_path = root / ns['STORE_RELATIVE'] / 'entries' / (entry_id + '.json')
record('manufactured hint with no private final entry does not hit', ns['lookup'](directory, value['runtime_identity'], value['observations']['limits'])[0] is None)
memory[str(entry_path)] = canonical(entry)
record('exact synthetic sealed envelope lookup selects original body', ns['lookup'](directory, value['runtime_identity'], value['observations']['limits'])[0]['body'] == body)
bad_entry = deepcopy(entry); bad_entry['hmac_sha256'] = '0' * 64
memory[str(entry_path)] = canonical(bad_entry)
record('incorrect seal refuses lookup', refuses(ns['lookup'], directory, value['runtime_identity'], value['observations']['limits']))
memory[str(entry_path)] = canonical(entry)
original_result = memory[str(directory / 'result.json')]
changed_result = deepcopy(value); changed_result['observations']['proof_modules'] = ['CALLER-CREATED']
memory[str(directory / 'result.json')] = canonical(changed_result)
record('self-consistent public result cannot replace authenticated body', refuses(ns['lookup'], directory, value['runtime_identity'], value['observations']['limits']))
memory[str(directory / 'result.json')] = original_result
for malformed in (None, [], 1, 'verified'):
    memory[str(directory / 'result.json')] = canonical(malformed)
    record('malformed original result refuses: ' + type(malformed).__name__, refuses(ns['binding'], directory, 'cold', selected, selection_sha))
memory[str(directory / 'result.json')] = original_result
reused = MemoryPath('/synthetic-reuse-bundle')
for name in ('request.json', 'replay-request.json', 'result.json', 'manifest.json'):
    memory[str(reused / ('origin-' + name))] = memory[str(directory / name)]
memory[str(reused / 'actual-runtime.log')] = b'NOT A FORMAL RESULT'
memory[str(reused / 'local-origin.json')] = canonical(dict(hint, layout='reuse'))
record('reuse layout resolves direct original cold body without chain', ns['lookup'](reused, value['runtime_identity'], value['observations']['limits'])[0]['body'] == body)

# Metadata-only path checks at a hypothetical, absent subtree in review territory.
ns.update(ROOT=HERE)
definitions(source, ('_unalias',), ns)
protected = HERE / ns['STORE_RELATIVE']
record('hypothetical review origin remains absent', not protected.exists())
record('absent protected suffix and case variant refuse before acquisition',
       refuses(ns['guard'], protected / 'input', output=True) and
       refuses(ns['guard'], HERE / '.CACHE/FORMAL-ORIGIN-V1/input', output=True))
record('output ancestor of reserved subtree refuses', refuses(ns['guard'], HERE, output=True))
record('broad registered input directory remains eligible', ns['guard'](HERE, directory=True) == HERE)
alias = HERE.with_name(HERE.name.upper())
case_alias_available = alias.exists() and alias.samefile(HERE)
record('host case alias discriminator available', case_alias_available)
record('case-alias output ancestor and protected suffix refuse',
       refuses(ns['guard'], alias, output=True) and
       refuses(ns['guard'], alias / '.CACHE/FORMAL-ORIGIN-V1/input', output=True))

adapter_source = CANDIDATE / 'build_tenants/graphify/code/ac_formal_gate.py'
adapter = {'Path': Path, 'stat': stat, 'Any': object}
definitions(adapter_source, ('GateError', '_unalias', '_contains', 'guard_path'), adapter)
config = {'root': str(HERE)}
record('Graphify guard independently rejects case-alias output and reserved suffix',
       refuses(adapter['guard_path'], config, alias, output=True, error_type=adapter['GateError']) and
       refuses(adapter['guard_path'], config, alias / '.CACHE/FORMAL-ORIGIN-V1/input', output=True, error_type=adapter['GateError']))
record('Graphify broad input root remains eligible', adapter['guard_path'](config, HERE, directory=True) == HERE)

print(json.dumps({'schema': 'a_c.independent-source-discriminators/1', 'scope': 'source hashes and extracted function definitions; in-memory synthetic envelopes and ordinary ancestor metadata only',
                  'candidate_closure_sha256': sha((SUBJECT / 'CLOSED.json').read_bytes()),
                  'results': results, 'count': len(results), 'actual_formal_verification': False,
                  'candidate_or_origin_writes': False, 'compiler_or_actor_runs': False}, indent=2, sort_keys=True))
