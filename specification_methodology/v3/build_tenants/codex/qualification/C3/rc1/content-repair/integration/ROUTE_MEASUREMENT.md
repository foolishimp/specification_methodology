# Selected route measurement

Every frozen before total in the entry plan reproduces exactly. The same
selected routes all grow after repair. The new direct S5 route avoids the seven
frame-selection prefaces and is smaller even after charging its newly shared
authority owner; the direct S3 route remains larger than its before route.

Subjects: reviewed successor `d1b33480b46f45bb46198a2f63ca197e84e40e55` and
documentary successor `3dca37d72b992f15e058159fe9087312d753ac02`. Every measured
method byte came from these Git objects, under
`specification_methodology/v3/build_tenants/codex/successor/`.

The [JSON](ROUTE_MEASUREMENT.json) carries every ordered selector, source-block
disambiguator, segment byte count and SHA-256, frozen input blob pin and result.
Its parser is the existing pure `synthesis/check_artifacts.py:section`, SHA-256
`6e94013a2f48f8b828370e7473aebbdec77e999967271d0df205f99796de0d00`, verified
equal to its reviewed-commit bytes. Its main was not run.

## Same selected routes

The boundary is the entry plan's boundary: both complete READMEs once, then each
listed section subtree and selected preface once. Source sections use
`rstrip() + '\n'`. Frame excerpts are first isolated at the next `^Source: `
delimiter; provenance lines are outside counted section bodies. A preface is
the bytes before the first `\nSource:`. The Foundations block supplies result
conjunction where the frame contains more than one similarly named section.
These segment counts are not semantic hop counts. Actor rereads, off-route
probes, actual Product inputs and retained context are outside this boundary.

| Scenario | Before bytes | After bytes | Change | Segments |
|---|---:|---:|---:|---:|
| S1: unknown-cause bug | 41,548 | 47,549 | +6,001 | 10 |
| S2: stale-summary resumption and uncertain effect | 53,744 | 57,420 | +3,676 | 13 |
| S3: lawful steps, failed outcome | 48,494 | 52,218 | +3,724 | 16 |
| S4: relaxed threshold and retained failure | 48,767 | 54,781 | +6,014 | 11 |
| S5: changed requirement and evidence reuse | 44,591 | 47,977 | +3,386 | 19 |

Both entry documents together grow from 9,802 to 12,123 bytes (+2,321).
S1/S4 also acquire the expanded authority owner, including its conditional
independence subtree. Other increases include explicit construction conditions,
retained-failure meaning and revised consumer routes. The fixed selector
comparison does not pretend that a newly introduced owner reference supplies
its body without acquisition.

## Direct routes actually offered

The new standards README explicitly offers S3 through “Assess whether lawful
work meets the required outcome” and S5 through “Reuse evidence after a subject,
requirement or basis change”. These are the only direct routes measured here.

Each direct reconstruction retains **every previously selected law section**
through its actual owner, including S3's four calculus sections and S5's RF-012
and applicability sections. Only discovery prefaces are removed. Bind and
Evaluate now delegate generic grant determination to `Judgment and authority`;
its 4,510-byte subtree, including conditional independent assessment, is added
to both compared current envelopes. Its cost is not hidden behind the new link.

| Current reconstruction | S3 bytes | S5 bytes |
|---|---:|---:|
| Same selected route plus that shared owner | 56,728 | 52,487 |
| Direct owner route, preserving the same selected law | 55,128 | 41,757 |
| Direct route change against comparable current envelope | −1,600 | −10,730 |
| Direct route change against frozen before route | **+6,634** | **−2,834** |

S3 avoids one current 1,470-byte evaluation preface. S5 avoids all seven current
prefaces, totaling 10,571 bytes. The remaining savings, 130 and 159 bytes,
respectively, are relative-link relocation overhead in projected excerpts;
they are not removed determinations. No governing law was removed to achieve
these savings. The JSON retains the complete old-selection-to-owner mapping.

These are reconstructed selected-source paths. They establish neither a minimum
acquisition route nor complete task sufficiency or dependency closure. Required
actual subject, evidence, grant and additional domain/profile inputs still need
their appropriate acquisition. This accounting isolates the new authority
dependency; it does not silently certify every other dependency.

## Complete frame tradeoff

The evaluation frame now directly includes Bounded construction (6,984 selected
body bytes) and Change impact and evidence retention (3,845). This removes the
two hidden deciding-owner routes identified in the review. Its full serialized
size grows by 12,839 bytes, which also includes refreshed excerpts, provenance
and its scope preface. Keeping complete result and conjunction excerpts is the
declared standalone-frame tradeoff. All refreshed frame sizes increase:

| Complete frame | Before bytes | After bytes | Change |
|---|---:|---:|---:|
| Evaluation/conjunction | 61,541 | 74,380 | +12,839 |
| Constitutional derivation | 80,763 | 82,806 | +2,043 |
| Domain binding | 69,047 | 70,182 | +1,135 |
| Release/adoption | 56,844 | 60,778 | +3,934 |
| Work/recovery | 77,572 | 80,113 | +2,541 |
| Triage/carrier | 96,659 | 99,383 | +2,724 |
| Member construction/assessment | 53,764 | 57,989 | +4,225 |

## Reproduction and limits

Run from the Codex checkout root. This uses the recorded selectors and the
existing parser; it writes nothing and imports with `-B`.

```sh
python3 -B - <<'PY'
import hashlib, importlib.util, json, re, subprocess
from pathlib import Path
base = Path('specification_methodology/v3/build_tenants/codex')
r = json.loads((base / 'qualification/C3/rc1/content-repair/integration/ROUTE_MEASUREMENT.json').read_text())
p = Path(r['parser']['path'])
if hashlib.sha256(p.read_bytes()).hexdigest() != r['parser']['sha256']:
    raise ValueError('Parser drift')
s = importlib.util.spec_from_file_location('route_sections', p)
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
cache = {}
def segment(commit, item):
    path, anchor = item['path'], item['selector']
    key = (commit, path)
    if key not in cache:
        cache[key] = subprocess.check_output(['git', 'show', commit + ':' + r['prefix'] + path]).decode()
    text = cache[key]
    if anchor == '@file': return text.encode()
    if anchor == '@preface': return text.split('\nSource:', 1)[0].encode()
    if '/frames/' not in path: return m.section(text, anchor)[1].encode()
    found = []
    for block in re.split(r'(?m)(?=^Source: )', text)[1:]:
        owner = item.get('source_member')
        if owner and not block.startswith('Source: [' + owner + ' '): continue
        try: found.append(m.section(block, anchor)[1])
        except ValueError: pass
    if len(found) != 1: raise ValueError((path, anchor, len(found)))
    return found[0].encode()
def count(label, run):
    print(label, sum(len(segment(run['commit'], x)) for x in run['segments']), len(run['segments']))
for name, comparison in r['same_selected_routes'].items():
    for stage in ['before', 'after']: count(name + ' ' + stage, comparison[stage])
for name, comparison in r['direct_owner_routes'].items():
    count(name + ' direct', comparison['route'])
    count(name + ' same plus authority', comparison['same_route_with_same_added_owner'])
for name, comparison in r['full_serialized_frames'].items():
    print(name, *[len(segment(r['subjects'][stage], comparison[stage])) for stage in ['before', 'after']])
PY
```

This is a bounded author measurement by the earlier Core Writer, not independent
review or a new cold-reader trial. It makes no rc.2 comparison, complete
criterion-6 conclusion, full Product qualification, acceptance or release claim.
The parser processed 1,472,541 unique frozen input bytes across its calculation
passes; those tool inputs are distinct from counted route bytes and material
delivered into actor context. Exact actor acquisition, repeated reads, native
retained context and native spend remain uninstrumented; no 1 MiB acquisition
compliance or active-context-fit claim follows. No paid call or test suite was
run. Work completed within the first 30-minute reporting interval.
