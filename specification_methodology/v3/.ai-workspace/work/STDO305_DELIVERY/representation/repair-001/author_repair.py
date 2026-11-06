"""Bounded LLM-authored repair, producing an answer for the public submit path.

This is not a model builder. The index choices and replacements below are
explicit semantic judgments over the retained lexical screen, not a rule that
deletes every uncertainty containing a keyword. Original authoring stays intact.
"""
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
ROOT = WORK
while not (ROOT / 'stdo_representation').is_dir():
    ROOT = ROOT.parent
BASE = ROOT / 'stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5'
A = json.loads((HERE / 'predecessor' / WORK.relative_to(ROOT) / 'authoring/answer-current.json').read_text())
BEFORE = copy.deepcopy(A)
ROWS = {r['key']: r for f in ['concepts', 'relations', 'constraints', 'latitude', 'residuals'] for r in A[f]}
SCREEN = json.loads((HERE / 'absence-scan-candidates.json').read_text())['candidates']
SEGMENTS = json.loads((BASE / 'run-coherent-003/generation/chunks.json').read_text())[0]['segments']
SOURCE = json.loads((BASE / 'source-freeze.json').read_text())
SOURCES = {r['path']: r for r in SOURCE['members'] + SOURCE['native_contracts']}
IDS = json.loads((WORK / 'authoring/record-ids.json').read_text())
DECISIONS = []

def write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def section(path, ending):
    found = [s for s in SEGMENTS if s['path'].endswith('/source/' + path) and
             (s['heading'] == ending or s['heading'].endswith('/' + ending))]
    assert len(found) == 1, (path, ending, len(found))
    return found[0]

def ground(path, ending):
    s = section(path, ending)
    text = s['text'].rstrip('\n')
    return {'section_id': s['id'], 'start_line': s['start_line'],
            'end_line': s['start_line'] + text.count('\n'), 'quote': text}

def change(key, field, after, group, reason, owner_paths):
    row = ROWS[key]
    prior = copy.deepcopy(row[field])
    assert prior != after, (key, field)
    row[field] = after
    DECISIONS.append({'key': key, 'record_id': IDS[key], 'field': field,
                      'before': prior, 'after': after, 'group': group,
                      'reason': reason, 'source_files': [SOURCES[p] for p in owner_paths]})

change('claude_host_boundary', 'statement',
       "The Product supplies the required acquisition boundary and grant. Use already-selected Product tools when they sufficiently realize that boundary; the host adapters are optional in that case and do not justify installing a competing mechanism. For a selected strict tool-acquisition boundary that uses the Claude adapter, bind its explicit session tool policy and hook, actual allowed control/read commands, roots and output behavior. Disable or constrain alternate tools and channels that bypass that selected policy; validate the actual policy/hook/session result rather than infer isolation from a subagent label or ordinary permission prompt. A direct admitted Claude task whose selected Product tools suffice and whose boundary is not strict does not require this adapter. The adapter covers hooked calls, not inherited or previously acquired context, arbitrary information-flow noninterference or semantic independence.",
       'S3-host-applicability',
       'HOST_BINDING opening makes adapters optional when sufficient selected Product tools exist; COORDINATED_HANDOFF Host Binding scopes strict-boundary use. Preserve the conditional adapter mechanism and its limits.',
       ['plugins/spec/references/HOST_BINDING.md', 'plugins/spec/references/COORDINATED_HANDOFF.md'])
change('claude_host_boundary', 'grounding',
       ROWS['claude_host_boundary']['grounding'] + [
           ground('plugins/spec/references/HOST_BINDING.md', 'Bind The Actual Host'),
           ground('plugins/spec/references/COORDINATED_HANDOFF.md', 'Host Binding')],
       'S3-host-applicability', 'Add deciding applicability owners after the unchanged first ground, preserving the record identity.',
       ['plugins/spec/references/HOST_BINDING.md', 'plugins/spec/references/COORDINATED_HANDOFF.md'])

change('fd_migration_dispositions', 'statement',
       "If totality, dependency closure and declared outcomes are established, migrate to common F_D while retaining the operation purpose, unchanged-subject evaluation profile where applicable, and exact grants. If new-kind eligibility is unestablished and the owner has identified the evidence gap/remediation or selected a separately declared bounded successor and its remediation obligation, retain pending-identified migration. Either alternative suffices; an identified termination-proof gap/remediation does not require selecting a bounded successor. When neither supported remediation nor successor classification has been selected, retain unresolved classification; do not relabel automatically as F_P or claim common F_D. A bounded successor has its own identity, contract, exhaustion outcomes and preservation obligations and does not retrospectively prove the legacy operation total. Old evidence remains valid only for its exact legacy basis/claims until the required preservation relation is established; patch naming does not promise semantic compatibility.",
       'S4-migration-alternatives',
       'RELEASE Deterministic-kind migration rows 2 and 3 and their explanation distinguish identified evidence-gap/remediation OR selected bounded successor from no supported disposition.',
       ['standards/RELEASE.md'])

# Each row selects the actual supplied owner(s) for this field's absence claim.
# Multiple equivalent rows share the same presence-only judgment. This establishes
# availability, not faithfulness, proof, implementation or an actual instance.
ALIASES = dict(F='FOUNDATIONS', A='ACTIVATION', AC='AXIOMATIC_CALCULUS',
               D='DESIGN_MODULE', E='EVALUATION', RF='REFERENCE_FRAME',
               R='RELEASE', SM='SPEC_METHOD', T='TICKETS', AS='ASSURANCE',
               W='WORLD_MODEL', UX='UX', PD='PRODUCT_DEFINITION', C='CONFORMANCE',
               P='PROFILES', I='IDENTITY', G='GLOSSARY', O='ODD', X='EXECUTIVE_BASELINE',
               PG='POSTING_GUIDE')
ROUTES = '''
4 F
5 SM
9 F A
10 A
12 RF A
13 A E RF
14 AC
15 A
16 RF A D O UX T
17 PD A
18 F A
20 SM A
21 F AC O P A
22 F A
23 AS D
24 A AS
25 AS RF
26 F AS
27 A RF F
28 AS
29 F
31 D A
32 AC
33 F
34 E
35 SM
36 AC R
37 F A
38 AC
39 A E F
40 A E SM O F
41 A
42 A E SM O F
43 A F
44 RF A
48 F A E I SM AS T R O UX
49 D A F
50 F A E I SM AS T R
51 D A E I SM AS T R
52 D
53 E
54 A D
56 AS D
57 F
58 SM T
59 T D
60 A
61 SM
62 A D
63 AS D
64 O UX R
65 SM
66 E T
67 F E
68 I F
69 R
70 F
71 E F
72 SM R
73 C A
74 RF F A E T D AS PD I R
75 F X
76 X RF F
77 E
78 A
80 RF
81 A
82 A E
83 RF AS E A T
84 F RF
85 A
86 E
87 E
88 RF A E
89 E
90 PD A
91 RF
93 T
94 I F
96 F PD P RF
97 F
98 F A E AS R
100 AC C E
101 PD
102 F PD P RF
103 RF F W
104 AC O
105 RF
106 A
107 O AS
108 F PD
112 A E
113 F
114 A
115 RF
116 F E
117 A AC
118 A RF
119 SM PD A E T
120 SM
121 SM A F
122 F
123 R
124 AS F
125 T
127 T AS
128 T
129 D
130 A E
131 E AS T
132 E I
133 T
134 PG
135 A
136 PD
137 SM T UX
138 F T
139 A
140 SM
141 PD
142 SM
143 D
144 E A
146 AS
147 AC A F T
148 T
149 T
151 AC
152 AC
153 UX
154 UX A
155 T W
156 UX D
157 T SM
158 UX
159 UX A
160 A
161 F A E I SM PD R T P
162 W O UX F C P G
163 D
164 SM R T
165 SM R
166 A
167 A
168 RF A
169 A
170 PD
171 SM
'''
routes = {int(parts[0]): ['standards/' + ALIASES[x] + '.md' for x in parts[1:]]
          for line in ROUTES.strip().splitlines() if (parts := line.split())}
# TRAVERSAL_OCCURRENCE, not the TICKETS shorthand T, owns these local domains.
routes[147].append('standards/TRAVERSAL_OCCURRENCE.md')
routes[148] = routes[149] = ['standards/TRAVERSAL_OCCURRENCE.md']

# Mixed claims retain their independent uncertainty. The remaining selected
# uncertainty fields assert only a historical acquisition gap and become empty.
MIXED = {
    9: "The source's claimed derivation standing is represented without an independent proof. Its cited common owners and consumer loci are supplied in the current corpus.",
    22: "The supplied foundation and consumer text records the claimed derivation standing; this interpretation does not independently prove that standing.",
    23: "The introduction and taxonomy phrase module-law ownership differently. Both current clauses and referenced owners are supplied; the distinction between law location and profile-object binding remains a source-reading question, not a new ownership ruling by this model.",
    26: "The source's derivation standings and trace claims are represented as assertions, not independently established proofs of those derivations or complete coverage.",
    42: "The cases describe expected behaviour; their operational owners are supplied, but no executed workflow or actual result is established by the case catalogue.",
    63: "ASSURANCE §15 and the adoption law are supplied. A concrete boundary's selected closure evaluators, implementation and execution evidence still require its own declared binding.",
    65: "SPEC_METHOD §2 supplies the realisation-shape law. The adopting Product's selected composition/effect algebra and concrete implementation remain its own choices and evidence obligations.",
    75: "The source's claimed derivation standings and overview coverage are represented as document assertions, not independently validated completeness.",
    97: "Index entries identify trace locations rather than rule bodies or verified coverage. The named common owner texts are supplied separately; the index does not establish their conformance.",
    101: "PRODUCT_DEFINITION §5 is supplied. Verification of a particular consuming occurrence's exact immutable installed basis remains instance evidence, not established by this glossary.",
    108: "Current foundation and referenced owner clauses are supplied; the model records their claimed standings without independently proving the derivations or the conformance of a concrete Product binding.",
    136: "PRODUCT_DEFINITION §§1 and 4 are supplied. A particular project's selected installed basis and its verification remain concrete binding evidence, not established by this generic layout.",
    137: "The current method's escrow and closure owners are supplied. Whether an actual sprint has selected a lawful deferral and satisfies its limits remains an instance-specific decision and evidence obligation.",
    138: "The table's derivation and ownership claims are represented, not independently proved. The common foundation and owner clauses are supplied; their presence establishes no concrete work-carrier conformance.",
    162: "The cited common owner and consumer texts are supplied. Concrete adopting-builder applications, tool executions and consumer evidence are not instantiated by this profile representation.",
    170: "PRODUCT_DEFINITION §9 is supplied; this template interpretation does not perform or establish conformance.",
    171: "SPEC_METHOD §11 is supplied. Concrete tenant execution bindings, their capabilities and conformance evidence are not instantiated by this template.",
}

RETAIN_REASONS = {
    1: 'Local glossary locator limitation: an index entry does not supply a definition; no claim that the corpus lacks SPEC_METHOD.',
    2: 'Local glossary locator limitation: these entries are locators, not full definitions; their owner texts remain separate.',
    3: 'Premises are not derivable from commitments; this is a logical standing distinction, not an acquisition gap.',
    6: 'Instance premises are not supplied by commitments as logical consequences; not an absent-source claim.',
    7: 'Explicitly scoped to the sort section, which lists the values while other profile clauses own mappings; preserve local excerpt boundary.',
    19: 'A particular step\'s applicable ambiguity policy/risk appetite needs its selected Product and grant; generic source availability does not instantiate it.',
    46: 'Actual formal proofs, observation models and independence evidence are not provided by a catalogue of required discriminators.',
    47: 'Actual quantitative models, impact covers and evidence remain instance-specific; supplied laws do not execute them.',
    172: 'Concrete runtime implementation, override merge semantics and installed qualification remain outside the generic template corpus.',
    174: 'Genuine source reconciliation question about accessibility force and exemptions, not missing owner acquisition; retain the residual unchanged.',
}

for x in SCREEN:
    i = x['index']
    if i not in routes:
        DECISIONS.append({'screen_index': i, 'key': x['key'], 'record_id': IDS[x['key']],
                          'field': x['field'], 'before': x['before'], 'after': x['before'],
                          'group': 'retained-local-instance-or-semantic-limit' if i in RETAIN_REASONS else 'retained-normative-keyword-match',
                          'reason': RETAIN_REASONS.get(i, 'The matched word is part of a normative condition, exception or consequence, not a claim that the source corpus lacks its owner.')})
        continue
    paths = routes[i]
    if i == 4:
        after = ROWS[x['key']][x['field']].replace('Its full foundational definition is not supplied.', 'The complete owning definition is in the supplied FOUNDATIONS P0.')
    elif i == 5:
        after = ROWS[x['key']][x['field']].replace('the complete source definition is not supplied.', 'the complete owning definition is in the supplied SPEC_METHOD §5.')
    else:
        assert x['field'] == 'uncertainty', (i, x['field'])
        after = MIXED.get(i, '')
    change(x['key'], x['field'], after,
           'supplied-owner-with-retained-independent-limit' if i in MIXED else 'historical-acquisition-gap-resolved',
           'The identified common owner files are exact members of accepted source S and have retained section dispositions in this model. Resolve only the false source-absence assertion. Presence does not establish semantic completeness, independent proof, an instance binding or execution.', paths)
    DECISIONS[-1]['screen_index'] = i
    # Retain a bounded per-file route to every exact included owner section,
    # without manufacturing proof of its interpretation or adding dependencies.
    DECISIONS[-1]['owner_section_ids'] = [s['id'] for s in SEGMENTS if any(s['path'].endswith('/source/' + p) for p in paths)]

assert {x['index'] for x in SCREEN} == {d['screen_index'] for d in DECISIONS if 'screen_index' in d}
assert len(A['residuals']) == len(BEFORE['residuals']) == 42
assert A['residuals'] == BEFORE['residuals'], 'No residual silently discharged by this field-level repair'
assert A['dispositions'] == BEFORE['dispositions']
assert all(ROWS[k]['grounding'][0] == next(r for f in ['concepts','relations','constraints','latitude','residuals'] for r in BEFORE[f] if r['key']==k)['grounding'][0] for k in ROWS)
write(HERE / 'answer-repaired.json', A)
write(HERE / 'field-decisions.json', {'kind': 'stdo305.semantic-field-repair/1',
      'source_identity_sha256': SOURCE['source_identity_sha256'],
      'standing': 'Writer source-fidelity judgments for independent targeted recheck; not acceptance',
      'scope': 'Two source-owned predicates and the repeated historical acquisition-gap class only',
      'screen_candidates': len(SCREEN), 'decisions': DECISIONS,
      'preserved': ['all record keys and first grounds', 'all 896 section dispositions', 'all 42 residual records', 'all record references', 'source S', 'direct-generation machinery']})
print(json.dumps({'answer_sha256': hashlib.sha256((HERE/'answer-repaired.json').read_bytes()).hexdigest(),
                  'changed_fields': sum(d['before'] != d['after'] for d in DECISIONS),
                  'retained_screen_fields': sum(d['before'] == d['after'] for d in DECISIONS),
                  'screen_fields': len(SCREEN)}))
