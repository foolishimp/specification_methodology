# Independent assessment of the frozen STDO 3.1.0-rc.2 W35 repair subject

**Verdict.** The repair holds. W35 now applies at `product_acceptance` and is still selected at `qualification` and `release`. Its source-owned successor condition stays in the rule text, and no fact was added or redefined. Release-only duties are not imported at acceptance. All six constructed queries are **supported** for their exact subjects, with the residuals listed below. The three unknown-boundary queries are **refused correctly**. That is a fail-closed outcome, not semantic coverage. I found **no material counterexample** and no required owner re-entry for this bounded release.

## 0. Standing and limits

- **Identity.** I am a Claude-family actor; the environment reports `claude-opus-5-5`, and the CLI metadata is the authoritative identity. I authored no candidate. The Writers are Codex-family, so this judgment is cross-family. I am the same family as both source-first actors and the RC1 assessors, so confirmation bias is possible.
- **Tools.** I used none. An `advisor` tool was exposed in this session; I did not call it, because you prohibited tools. I recomputed no hashes. Every digest, byte equality and test result below is an operator or Writer observation.
- **Order of reading.** Sources and candidate arrived in one packet, so source-first order was not enforced in this session. Only the two fixed expectation reports predate exposure to the candidate.
- **What I read.** The full RC2 SDLC index and all six delivered bodies. Each deciding owner section: EVALUATION §5, RELEASE §8/§9, FOUNDATIONS Conjunction, ACTIVATION Applicability. The catalog and runtime code, and the native patch.
- **Python index.** For its 113 rules I relied on reported zero rule change and owner byte-equality, plus targeted re-reading. I did not re-derive every clause.
- **Hidden host context.** Not measured.

## 1. Conclusions by claim

### W35 repair (SDLC canonical index `39f2432c…`)

- **Scope of change (operator).** Only W35's `when` changed. Text, dependencies and source references are unchanged. The family guard and purpose facts are equal to RC1; only the purpose description changed.
- **Obligations carried at acceptance (my reading).** The rule carries, in substance, these obligations from my source-first report:
  - O1/O2: identify the exact immutable predecessor.
  - O3: four disposition values, including removal "by Product authority".
  - O4: an unresolved disposition "blocks … and has no performed result".
  - O5: comparing wording or digests alone is not conservation.
  - O7: reuse prior evidence without copying the old judgment.
- **Successor condition.** It stays textual ("For a successor qualification/acceptance claim"). It is not made universal and not turned into a fact.
- **Unestablished successor status.** It is withheld by W23 ("Unknown mandatory applicability … withholds the dependent claim"), not read as "not a successor".
- **Authority boundary.** The general acceptance and authority boundaries are carried by W02, W04, W06, W23 and W24. W25 states that a gate exists only by explicit declaration. The delivered body says "unassessed / experimental-candidate" and implies no acceptance.
- **Residuals.** These are compressions, not inversions (R1–R3 below):
  - the step from "blocks qualification" to "cannot be accepted" is left implicit;
  - the rule that a pre-test "conserved" disposition is unresolved is not stated;
  - "a disposition is a claim, not a result" is not stated;
  - the modal-strength and counterexample detail of RELEASE §9 ¶3 is not stated;
  - the support-line paragraph and deterministic-kind migration are reachable only through the source reference (RELEASE 735–849).

  O6 and K3 are partly covered by W06 and W29: a stale held result is a missing result, and a changed basis invalidates reliance.

### Guard and dependency behaviour, per delivered body

| Query | W35 | W26 (release criteria) | Other notes |
|---|---|---|---|
| acceptance | true | false, shown | W28 true (reuse true); W25, W27–W31 and W14–W16 true; no release-only import |
| qualification | true | false | same behaviour as RC1 |
| release | true | true | |
| work | absent | absent | W25 absent; W14 shown false as a dependency of W29 |
| sdlc (boundary none) | absent | absent | |

- False dependencies are visible (W09/W10 under W12, W26, W14), and none of them hides a W35 obligation (falsifier X3 clear).
- None of falsifiers F1–F9 from my addendum is triggered.

### Unknown-boundary expectation revised

My addendum said an unknown `boundary_kind` should make W35's own guard unknown, not make the family incomplete. That was conditional on not seeing the catalog. The actual catalog `family_guard` (identical in RC1 and RC2) includes `any` over all six boundary values, so `boundary_kind` is a family fact. PC-R03 therefore requires family `incomplete`. The three actual refusals match this exactly:

- status `incomplete`, `covered:false`, no delivered body;
- all eight family predicates recorded (each `boundary_kind` clause `unknown`);
- the reason given is "do not invent or coerce caller facts";
- integer `3` is treated as unknown, not coerced.

Neither default (ordinary work, or acceptance) occurs. I revise my expectation to match the source.

Two related notes:
- The Writer's unknown-boundary unit test calls `compile_context` directly. It shows W35 as `unknown` with a gap on the core path; that test does not exercise the installed catalog route. Both paths fail closed.
- **G1 (by code reading only):** a misspelled value such as `"acceptance"` gives family `false` through the catalog route, which returns `refused`. It does not silently drop W35. A direct core caller bypassing the catalog would drop W35 (A1, adjacent). Neither was observed.

### The six constructed queries (my new exact-subject judgments)

- **acceptance — supported.** The full O1–O10 population is present or contained, and there is no import of release-only duties. Residuals R1–R4.
- **qualification — supported.** W35 is conserved. It does not carry the exact-cut binding list of RELEASE §3 (R6, adjacent; unchanged from RC1).
- **release — supported.** W26 and W35 are present. Ref and publication mechanics are correctly excluded; W34 routes acquisition of owner policy.
- **work — supported.** The ordinary-work exclusion is correct and the reuse and staleness law is delivered. Residuals: RC1 F1 (W11 is gated on `repair_planned`), and A2 (integration-time support-line dispositions are not selected at boundary none; pre-existing).
- **sdlc — supported.** The delivered set equals RC1's 20 rules, and the only rule change (W35) is not selected here. RC1 residuals F1, F2 and F5 carry forward. RC1's F6 does not recur, because facts are equal RC1→RC2.
- **python — supported.** Zero rule changes, 16 owners byte-equal, facts and guard equal. 94 rules selected and 19 excluded (ODD and UX), no gaps. RC1 residuals F3, F4 and F7 carry forward:
  - F3: C10's measurement trigger is weaker than the capacity-declared trigger in ACTIVATION §2.
  - F4: `language_version` 3.12 is still not grounded in any RC2 fixture input.
  - F7: C04 omits the explicit sentence on the ticket's work-state authority.

These are new verdicts on new canonical subjects. The RC1 verdicts are cited as evidence only, under `retain_applicable`. The RC1 W35 counterexample does not invalidate them, because both RC1 supported queries used boundary none, where W35 is excluded in both releases.

### Native conservation

- **Unchanged (operator).** The constitutional owners, SDLC_DEFAULTS, frames, and the stdo-work, review and ticket skill contracts are byte-equal to RC1. A's parent is RC1, and the tag peel matches.
- **The four changed members.**
  - GETTING_STARTED and the documentation README and index: rc.1→rc.2 and rc1→rc2 substitutions only. The acquisition binding is superseded by the RC2 identity, and the procedure and checks are conserved.
  - The release note is rewritten. Its statements about W35 and about owner conservation match the evidence.
- **Condition C1.** The release note in immutable A makes prospective claims about the contents of the cohort record, independent assessment, public acquisition and one guarded atomic 25-ref publication. These must be true at publication.
- **Not verifiable from this packet.** The claim of "unchanged manager behaviour and dependency bytes". The 52 frame tests passing is an operator observation (exit 0).

### Visual evidence reuse

The RC1 independent fidelity and recheck judgment (model `784aa60f…`) applies to the RC2 records (model `c16f1203…`) for these claims:
- the 24 annotation meanings;
- the 93-section navigation and residual dispositions;
- relation direction;
- scope honesty and the 67 unselected members (I counted 67 in SOURCE_BINDING).

The basis, as Writer-supplied evidence:
- the three visual source members and the calculus member are byte-equal;
- the recipe changed only the source cut;
- the 306 records are equal under an explicit identity bijection plus a source-path normalisation.

Fresh RC2 browser checks (12, digest-bound, `file://`, source tree) support only the source-tree reading modes.

Not upgraded:
- packaged, installed or public browser modes;
- external Graphify;
- general fidelity;
- structured re-entry (94 empty arrays retained as a disclosed limit);
- the latitude-label display limit.

VIS-RC2-05, which supersedes RC1 coordinates as the current selection, is lawful identity succession.

## 2. Remaining for final identity, package and publication closure (not claimed here)

1. **Package02 equality.** Package02 must be byte-identical to the frozen package01 bytes: indexes `84a4043c…`/`e307802e…`, purposes, sources, and the nine query bytes. The final installed contexts must equal the six frozen bodies on both the Codex and Claude adapters. The Claude-host delivery was not supplied. Any difference voids these statuses for that subject.
2. **Distribution pins.** Public manifest and catalog pins (`312dda…`, `c96390…`) reconciled, along with Skills dependency pins and the COVERAGE-STANDING records. Those records must cite this assessment by canonical index, corpus and query hash.
3. **Release identity.** Source B and the cohort record; remote absence and no higher ordinal; exact previous objects for the mutable refs; one atomic 25-ref push with RC1 unmoved; a normal GitHub release.
4. **Public acquisition.** Public assets downloaded and hash-checked; a fresh isolated install of the manager and native cut; installed context results.
5. **Release-note truth.** Verify the prospective claims in the release note against the actual outcomes (C1).
6. **Human acceptance.** Human exact-cut acceptance stays separate and open.

```json
{
  "subjects": [
    {"name": "acceptance", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "58ce3e20119f98c411da8f0c04f693342e92a5821527635f51829f8d33f6a63f", "status": "supported", "evaluator": "Claude-family (env claude-opus-5-5; CLI metadata authoritative); cross-family to Codex Writers; same family as source-first and RC1 assessors; no tools; advisor exposed, not called", "evidence": ["delivered context/acceptance 45b4ba3facddf611f9357dc0da9f462dd425dd37012b9f99debbf530ea884f7d", "operator readback 8e9e7595c2cc5aff1d263e52e425037d79f51e9ac639cb6b6e960b530c47db51 (only W35.when changed)", "EVALUATION b856cf04... section 5; RELEASE eea362e1... sections 8-9; FOUNDATIONS 7fe9ecf2... Conjunction", "BOUNDARY_SCENARIOS db8547fc..."], "scope": "Predecision SDLC workflow-constraint sufficiency for a successor product_acceptance decision on native RC2; no acceptance, release or exact-cut criteria (RELEASE section 8 is not imported); exact-cut acceptance should use boundary release"},
    {"name": "qualification", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "0049b6e2e05c603e7c786efa785bfbe98ceaba46337a7cb0c59b723e0c83ecfe", "status": "supported", "evaluator": "as above", "evidence": ["delivered context/qualification 329c66d9a3ad266a06b91cf6698f22712856c669ce36e1af6aca008cffaae93b", "operator readback 8e9e7595..."], "scope": "Workflow constraints and successor conservation at a qualification boundary; excludes the RELEASE section 3 exact-cut binding list (R6)"},
    {"name": "release", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "428f2d98b8628bb2889cc4435773c572cb4d108471ff204a5610208082c4df8b", "status": "supported", "evaluator": "as above", "evidence": ["delivered context/release 15a513924fd91ecbff2716867dbe504034e41ed3bb5e89b6ed591f9a2774c8dd"], "scope": "Workflow-level release criteria (W26) plus successor conservation; ref and publication mechanics are owner re-entry, not covered"},
    {"name": "work", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "650ed9eda70cc471c75ff528aa81d9650576ed71cffb41341ce2c07e0d8d0c1c", "status": "supported", "evaluator": "as above", "evidence": ["delivered context/work a56e6e3855bdfff791a2228958a07f166dfd6ec8db45cac91e6c6d463de7d0c8"], "scope": "Ordinary work with proposed reuse and changed source; correct W35/W25/W26 exclusion; residuals F1 and A2"},
    {"name": "sdlc", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "9e81574d3328ae77260769130ea16045ab84dc9594815aab8449bdb010f769a5", "status": "supported", "evaluator": "as above", "evidence": ["delivered context/sdlc 043f28a9d0662cfc54f81d37b77bb1516661b9472be3731888a6cecedeecce7b", "fixture WORK_CONTRACT 65557c70..., FRAME_BASIS 4c04bc7a...", "RC1 VERDICT a09b8f04... cited only"], "scope": "Executing and recording the admitted bounded refactor via the run carrier, boundary none, no Executive profile"},
    {"name": "python", "index_sha256": "e6a71a11163b84e9906591cd02cc448949f289382814414976bc261aaeb41ecd", "corpus_sha256": "108aa7915a7c236c27934f52531f43d271b94a0ad4366706a2e4fb222f8ca07e", "query_sha256": "84b5d4b993d24b068e0e601f00f4b75cbeab4cd0475482256410b279be60f409", "status": "supported", "evaluator": "as above", "evidence": ["delivered context/python da7fb2666bfa68a694d7387e5ec725bdf52724d3407a6f49a3035603b12e31e9", "operator readback: zero rule changes, 16 owners byte-equal, facts and guard equal", "fixture REQUIREMENTS ab9a26eb..., DESIGN 0a91a535..., FRAME_BASIS 4c04bc7a...", "RC1 python verdict on index 717857ed... cited only"], "scope": "Preconstruction method-constraint sufficiency for the worker / DESIGN_MODULE / pure-local Python 3.12 realization_refactor family; excludes code, typing pass, equivalence and acceptance"},
    {"name": "missing-boundary", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "abe1b7b7a7a45465ae6b23958e3a2b33ca83c4d6f209432b5ec47f17d2f86dcb", "status": "unknown", "refusal_judgment": "correct", "evaluator": "as above", "evidence": ["actual refusal 203f6455bf11a449512a704ce27ebf9ad234bee6b9f0bcf9b8b3be19bca5f9ff (status incomplete, covered false, family unknown)"], "scope": "No delivered context exists, so semantic coverage is not judgeable; the fail-closed family refusal is judged correct under PC-R03"},
    {"name": "null-boundary", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "191ef66060fde1062ca6becc85f63ff77d63256a625dbc98a44f7f51fa386e88", "status": "unknown", "refusal_judgment": "correct", "evaluator": "as above", "evidence": ["actual refusal 74c525401e35afd7691bd06fbe6c561b97184d4555a611affcdde9aa976a92b8"], "scope": "As missing-boundary"},
    {"name": "ill-typed-boundary", "index_sha256": "39f2432c76dd74a2db4c94b773640d2d06edc311d6f850a71a603e1f60d2571c", "corpus_sha256": "f281ac7afbcece39b3febaae0e28bda568d38868ebebb2d72c35b778ff7558eb", "query_sha256": "0acae931ae6d9fc2cbd3ca0555870934f9109eea2b95c47d750c063056046484", "status": "unknown", "refusal_judgment": "correct", "evaluator": "as above", "evidence": ["actual refusal ab30b694863b397d59d7559c7a8bea5682b4246e64f13da268f7de57f853eee6 (integer 3 treated as unknown, not coerced)"], "scope": "As missing-boundary"}
  ],
  "claim_results": [
    {"claim": "W35 selected at product_acceptance with unchanged obligation; qualification and release conserved; ordinary work excluded", "result": "supported", "basis": "Guard delta only; obligations O1-O5, O7 and O9 present; O4/O6/O8 compressed (R1, R2); W23 withholds unestablished successor status"},
    {"claim": "No release-only duty imported at acceptance; dependency guards visible", "result": "supported", "basis": "W26 shown false at acceptance and qualification, true at release; no X3 emptying"},
    {"claim": "No new or redefined purpose fact", "result": "supported", "basis": "purpose_facts_equal true for both indexes; description-only change"},
    {"claim": "Unknown boundary fails closed", "result": "supported_with_revised_expectation", "basis": "boundary_kind is a family fact in the unchanged catalog guard; family incomplete is the correct outcome; the prior conditional expectation is revised"},
    {"claim": "Native constitutional, default, frame and workflow owners conserved; four metadata members bounded", "result": "supported", "basis": "operator byte equality; patch is version rebinding plus a release note whose current claims match the evidence", "condition": "C1"},
    {"claim": "Visual unchanged semantics reuse", "result": "supported_for_declared_claims", "basis": "selected sources byte-equal; 306-record bijection; fresh source-tree browser checks", "not_upgraded": ["packaged/installed/public browser modes", "Graphify", "general fidelity", "structured re-entry"]}
  ],
  "evidence_reuse": [
    {"evidence": "RC1 python and sdlc supported verdicts", "applicability": "cited support only; not invalidated by the W35 counterexample (boundary none excludes W35 in both releases); verdicts not relabelled"},
    {"evidence": "RC1 failing acceptance test (ACCEPTANCE_NEGATIVE 36235df2...)", "applicability": "retained on the RC1 subject as the before-failure"},
    {"evidence": "RC1 visual recheck on model 784aa60f...", "applicability": "applicable to the 24 annotations, navigation, relation direction and scope on RC2 model c16f1203... via Writer-computed equality; the RC2 verdict is this new judgment"},
    {"evidence": "Writer mechanical tests (FINAL_CONTROLS 162ee727..., 28 + 8 tests)", "applicability": "mechanical only; no semantic weight"}
  ],
  "findings": [
    {"id": "R1", "class": "bounded_residual", "subject": "acceptance", "summary": "W35 says an unresolved disposition 'blocks its affected qualification'; the EVALUATION section 5 consequence 'and so cannot be accepted' is implicit via 'qualification/acceptance claim' and W06/W23"},
    {"id": "R2", "class": "bounded_residual", "subject": "acceptance/qualification/release", "summary": "W35 omits: pre-test 'conserved' is unresolved (O6/K3; partly covered by W06/W29); disposition-is-a-claim (O8/K6); modal-strength and counterexample detail of RELEASE section 9 para 3; 'superseded by accepted successor relation'"},
    {"id": "R3", "class": "bounded_residual", "summary": "Deterministic-kind migration and the support-line paragraph are reachable only through W35 source re-entry RELEASE 735-849"},
    {"id": "R4", "class": "bounded_residual", "summary": "Acceptance of an exact immutable cut labelled product_acceptance would not receive W26; the label is the caller's observation"},
    {"id": "R6", "class": "adjacent", "summary": "Qualification context lacks the RELEASE section 3 exact-cut binding list; unchanged from RC1"},
    {"id": "A1", "class": "adjacent", "summary": "A direct compile_context caller bypassing the catalog family guard would silently deselect W35 on a misspelled boundary value; the catalog route refuses (code reading, unobserved)"},
    {"id": "A2", "class": "adjacent", "summary": "RELEASE section 9 integration-time support-line dispositions not selected at boundary none; pre-existing"},
    {"id": "C1", "class": "closure_condition", "summary": "Release note in immutable native A asserts future cohort record, assessment, public-acquisition and atomic-publication outcomes; these must be verified true"},
    {"id": "RC1-F1/F2/F3/F4/F5/F7", "class": "bounded_residual_carried", "summary": "Unchanged RC1 residuals; F4 language_version still ungrounded in the RC2 fixture"}
  ],
  "residuals": ["No material counterexample found", "Confirmation-bias risk: same model family as source-first and RC1 assessors", "No exhaustive clause-by-clause re-derivation of the 113 Python rules", "All hashes and equalities supplied, not recomputed", "Adequate attention and receipt not claimed", "Visual: 94 empty re_entry arrays; latitude label displays its identifier"],
  "unperformed": ["Claude-host adapter delivery and package02 byte comparison", "Queries at landing/work_closure and misspelled-value observations", "Manager behaviour and dependency-byte conservation", "Source B, cohort record, ref graph, atomic push, GitHub release, public acquisition, fresh install", "Packaged/installed/public visual browser modes", "Task correctness, code equivalence, typing pass", "Human exact-cut acceptance", "Whole-method, universal coverage, automatic host pickup"]
}
```
