# STDO Representation Project Reference-Frame Basis

Status: source-project basis, revision 12; acceptance is external and
digest-bound.

## Project frame basis

```text
frame_set_uri =
  "urn:stdo-representation:reference-frame-basis:source-project:12"
governed_workspace = "repo://stdo-representation/"
governed_subject = "urn:stdo-representation:bounded-context:product"
governed_outcome =
  "qualify STDO Representation 2.5.0 as compression and index of STDO 2.5.0"
frame_set_authority =
  "urn:stdo-representation:authority:product-owner"
reference_frame_method =
  "stdo://releases/v2.5.0-rc.1/standards/REFERENCE_FRAME_METHOD.md"
reference_frame_method_sha256 =
  "sha256:90b5ea5e486c1c0e75883db5a15fba3f524cc5d5718c42108a548279e725d51f"
release_method =
  "stdo://releases/v2.5.0-rc.1/standards/RELEASE_METHOD.md"
release_method_sha256 =
  "sha256:c690228adf680dc4ef0a391073a5d60e515fbd4b0150b778b6adb4723e3fa9a0"
stdo_manifest_sha256 =
  "sha256:3cd24c3196d8334fd9e87fe353e0c8039dbce9f15305cfc8474c7fd71d79d338"
```

This basis governs project construction and release evaluation. It is not a
consumer prompt, generated frame overlay, GTL composition, or grant of
operation authority.

Every activation binds the exact live WHAT inventory and digest, Product member
bytes, dependency coordinates, actor and configuration, evidence boundary, and
activation time. Pre-publication activation binds a deterministic candidate
inventory and claim bytes; it does not require an RC tag. Post-publication
exact-cut activation additionally binds the annotated tag object, peeled
commit, tree, and remote refs.

## Exact dependency basis

```text
Source STDO = v2.5.0-rc.1
Source STDO member set =
  sha256:87dca989f2200e91406524b6b2a3e85b230bf201581425614b57a7e0469be1e5
Axiom Indexer tag object =
  e7afc8a42a7123aebe91cb7582cb037b1aae612d
Axiom Indexer commit =
  dc3e00998da36dae6ac7b76b340431a85096c83c
Axiom Indexer tree =
  8c9ad5f5e99a60c18fb8c1802471753afb226272
Axiom Indexer member inventory =
  sha256:7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
Representation semantic version = 2.5.0
Represented STDO semantic version = 2.5.0
```

## Human authority

- The Product owner declares and accepts the frame set and disposes the release
  candidate.
- Source STDO owns STDO meaning and role definitions.
- Axiom Indexer owns its released mechanical contracts.
- An explicitly assigned evaluator may perform one read-only activation.
- Construction, file mutation, publication, tag movement, and remote mutation
  require separate authority.
- An agent may propose or evaluate this basis. It may not accept it merely by
  authorship, visibility, validation, or use.

Acceptance must bind this file's exact SHA-256 in a durable decision record.

## Shared coordinate, evidence, and result law

Semantic coordinates compare by URI, owner, scope, selected basis, and exact
content identity. Candidate coordinates compare by complete Product member
inventory, dependency identities, claims, evidence, and qualification basis.
Exact-cut coordinates add tag object, peeled commit, tree, and remote refs.
Names, paths, counts, or matching prose do not establish equality.

Admissible evidence is exact source or immutable reacquisition evidence,
URI-addressed claims and counterexamples, Axiom Indexer reports and maps,
native-agent inputs and outputs, joined request bytes, Git objects, and
independent judgments where required. A passing schema, hash, or test proves
only its declared mechanical property.

Each evaluation returns exactly one of:

- `satisfied`;
- `falsified` with a material counterexample;
- `indeterminate` with missing evidence;
- `out_of_frame` with the required additional relation; or
- `invalid_basis` with the unresolved subject, source, identity, or authority.

Every result names its frame, exact activation basis, actor, evidence, verdict,
residuals, and invalidation conditions.

## Selected frames

### F-PRODUCT-BOUNDARY

- Evaluation: is `2.5.0` exactly the semantic compression, constraint index,
  and native-instructions Product with no local engine or hidden
  heavy-prototype dependency?
- Evidence: exact WHAT, member inventory, dependency basis, exclusions, and
  realization routing.
- Invariants: eight Product members; Axiom Indexer owns all deterministic code;
  retained prototypes remain history.
- Actor envelope: `K-PRODUCT`.
- Exclusions: repository presence, prior tests, or GTL terminology cannot widen
  the Product.

### F-VERSION-ALIGNMENT

- Evaluation: does the Representation semantic version equal the represented
  STDO semantic version while preserving distinct Product, RC, member, and Git
  identities?
- Evidence: exact Source STDO cut and selector, Product version law, historical
  bootstrap release, project-qualified release plan, and dependency identities.
- Invariants: `representation_version = represented_stdo_version = 2.5.0`;
  Source STDO, STDO Representation, and Axiom Indexer remain different
  Products; historical refs never move.
- Actor envelope: `K-PRODUCT`.
- Exclusions: equal version text cannot substitute one Product, cut, install,
  subtree, or release ref for another.

### F-MAP-ESSENCE

- Evaluation: does `a_c.STDO` compress essential constraints and uncertainty,
  and does the index expose that unchanged logic with usable Source STDO routes
  rather than restate prose?
- Evidence: exact compression and index, the closed `F-MECHANICAL-BOUNDARY` result,
  source routes, residuals, and source-grounded counterexamples.
- Invariants: exact compression-to-index identity, URI identity, explicit
  residuals, bounded source re-entry, and no complete-`M_b` or unique-truth
  claim.
- Actor envelope: `K-MAP`.
- Exclusions: size, polish, source-member count, or structural validity alone
  does not prove semantic usefulness.

### F-MECHANICAL-BOUNDARY

- Evaluation: does exact Axiom Indexer validate, instantiate, and join without
  selecting, repairing, or interpreting meaning?
- Evidence: dependency objects, exact inputs and outputs, diagnostics,
  refusal cases, and byte comparison.
- Invariants: no local validator fork; unchanged program bytes; caller-owned
  frame selection and join rows.
- Actor envelope: `K-MECHANICAL`.
- Exclusions: success does not prove truth, completeness, frame applicability,
  role independence, or authority.

### F-NATIVE-USE

- Evaluation: can fresh Codex and Claude agents discover the canonical skill,
  select visible frames, use bounded source re-entry, and preserve role return
  relations?
- Evidence: exact skill inventory, discovery routes, target references, native
  requests and results, selected frame details, and source openings.
- Invariants: common semantic instructions; material target differences only;
  LLM-owned selection; no hidden packet engine.
- Actor envelope: `K-NATIVE`.
- Exclusions: fixture pickup or one target cannot establish the other target's
  usability.

### F-DOGFOOD-USEFULNESS

- Evaluation: is map-first native use non-inferior to direct Source STDO prose
  on material constraints and source recovery, and useful enough to retain?
- Evidence: frozen comparable tasks, exact direct-prose and map-first inputs and
  results, exact Source STDO, source-re-entry observations, regressions,
  residuals, and joined requests.
- Invariants: same task and evidence boundary; no favorable-example selection;
  source remains available.
- Actor envelope: `K-DOGFOOD`.
- Exclusions: token reduction, green validation, or preference without evidence
  cannot satisfy usefulness.
- Result: this separately activated frame produces the independent source
  comparison required by `REQ-P-DOGFOOD-008` and its usefulness verdict; it
  does not consume that comparison as prerequisite evidence.

### F-CANDIDATE-READINESS

- Evaluation: is one frozen eight-member candidate ready for immutable RC
  publication under exact dependencies, claims, evidence, and exclusions?
- Evidence: deterministic member inventory, release record, closed Product
  frame results, dependency verification, explicit predecessor or genesis
  disposition, publication plan, and remote namespace observation.
- Invariants: no RC tag is required before publication; a satisfied result
  grants no publication authority.
- Actor envelope: `K-CANDIDATE`.
- Exclusions: branch state, intended paths, test count, or intended tag name is
  not candidate identity.

### F-EXACT-CUT

- Evaluation: does the published immutable RC exactly carry the ready candidate
  and satisfy exact-cut qualification and acceptance prerequisites?
- Evidence: annotated RC and selector objects, peeled commit and tree, remote
  refs, the closed candidate-readiness result, independently reacquired member
  and claim bytes, and the reacquired predecessor or genesis disposition.
- Invariants: immutable RC tags never move; qualifying-byte repair creates a
  higher RC; candidate and cut bytes agree.
- Actor envelope: `K-EXACT-CUT`.
- Exclusions: this frame is not activated before publication and cannot veto a
  candidate whose release subject does not yet exist.
- Result: this separately activated frame produces the independent exact-cut
  review; it does not consume that review as prerequisite evidence.

## Actor capability envelopes

Each activation records actual actor identity, model or tool version,
configuration, context boundary, access, and prior involvement.

| Envelope | Actor and configuration | Context, access, independence, and stop law |
|---|---|---|
| `K-PRODUCT` | Product evaluator competent in recursive Product boundaries, exact dependency identity, and release scope | read-only WHAT, member routes, tenant history, and Git evidence; discloses authorship; stops on missing authority, inventory, or dependency basis |
| `K-MAP` | LLM semantic evaluator competent in `a_c.text`, URI reasoning, residual analysis, and source comparison | exact program, map, sources, and read-only re-entry; no independent-assurance claim when author; stops on missing source, unresolved semantics, or context limit |
| `K-MECHANICAL` | Python/tool evaluator competent in Axiom Indexer validation, joining, canonical identity, and falsifier construction | exact dependency and inputs with temporary output space; does not repair the subject; stops on environment, dependency, input, or output drift |
| `K-NATIVE` | fresh Codex or Claude actor competent in native skill pickup, map traversal, explicit frame selection, and source re-entry | initially bounded skill, map, and task; no expected answer or complete-corpus exposure; stops on unresolved map, frame, source, authority, or role boundary |
| `K-DOGFOOD` | separately activated comparison assessor competent in task equivalence, Source STDO semantic review, evidence control, and regression reporting | activated only after both conditions freeze; did not author or repair the exact program, map, skill, task, or evaluated outputs and saw no expected verdict before evidence acquisition; independently reacquires exact Source STDO and both condition records under recorded actor and model configuration; preserves the same material task, workspace evidence, role, output contract, model capability, and evaluator across arms; does not discard negative results, select favorable cases, repair the subject, or dispose the Product claim; stops on any separation, equality, provenance, or evidence failure |
| `K-CANDIDATE` | release-readiness evaluator competent in STDO release law, inventory, claim matching, and dependency verification | frozen candidate, closed frame results, local Git and read-only remote namespace; no publication authority; stops on incomplete or mutable subject |
| `K-EXACT-CUT` | separately activated assessor competent in remote reacquisition, annotated tags, tree comparison, and claim-to-evidence review | published refs, clean reacquisition, exact release record, and closed candidate result; no authorship or repair of the exact qualifying candidate; independently reacquires the published subject and evidence; stops on any tag, tree, member, claim, or provenance mismatch |

## Coverage ledger

| Evaluation | Provenance | Selected frame | Authority | Evidence and dependencies | Status and residual |
|---|---|---|---|---|---|
| exact frame-set acceptance and overlay binding | Reference Frame Method; Product owner | external acceptance relation | Product owner decides; overlay mutation separately granted | exact file digest, acceptance record, valid Product Definition; prerequisite to activation | separately covered; human acceptance and overlay binding pending |
| compression-and-index Product boundary | Goals; Intent; Product; T-006 | `F-PRODUCT-BOUNDARY` | Product owner | WHAT, member set, dependencies, excluded tenant routes | conditionally covered; requires frozen activation |
| represented-version alignment | Product version relation; T-006; Release Method | `F-VERSION-ALIGNMENT` | Product owner | exact STDO cut and version, Representation candidate, historical bootstrap, project-qualified refs | conditionally covered; mismatch or identity collapse falsifies |
| compression/index essence and source re-entry | Product; map requirement | `F-MAP-ESSENCE` | Source owners own meaning; Product owner disposes usefulness | compression, index, closed mechanical result, sources, residuals, counterexamples | conditionally covered; semantic uncertainty remains |
| imported validator and join boundary | Product; candidate requirement; Axiom release | `F-MECHANICAL-BOUNDARY` | Axiom owns contract; Product owner owns dependency selection | exact dependency, reports, maps, joins, falsifiers | conditionally covered; proves mechanical properties only |
| Codex and Claude frame use | native-use requirement | `F-NATIVE-USE` | Product owns instructions; LLM owns selection within supplied authority | skill inventory, target references, fresh pickups, selected frames | conditionally covered; each target requires observation |
| practical usefulness | dogfood requirement | `F-DOGFOOD-USEFULNESS` | Product owner disposes claim | comparable tasks, outputs, source re-entry, regressions | conditionally covered; unobserved tasks remain residual |
| pre-publication candidate readiness | Release Method candidate phase; release record | `F-CANDIDATE-READINESS` | Product owner disposes candidate; publisher separately granted | closed Product results, frozen inventory, claims, dependencies | conditionally covered; no RC prerequisite |
| immutable RC publication and selector advancement | Release Method Immutable RC Publication and Monotonic Version-Line Advancement | external publication relation | an exact Product-owner grant names the publisher and repository/ref mutation territory; this frame set grants none | frozen candidate result, reconciled release assets, annotated RC and selector objects, atomic-push result where supported, and remote highest-RC verification | separately covered; any partial, lagging, mismatched, or unverified publication blocks exact-cut activation |
| post-publication exact-cut qualification | Release Method exact-cut phase | `F-EXACT-CUT` | Product owner accepts or rejects exact RC | published refs, clean reacquisition, closed candidate result | phase-conditional; not activated before publication |

## Material interactions and conjunction

- `mechanical -> map`: `F-MECHANICAL-BOUNDARY` produces the closed validation
  and map result over the exact program, bindings, and Axiom dependency;
  `F-MAP-ESSENCE` consumes that result and exact map bytes; subject or
  dependency drift returns `invalid_basis`.
- `mechanical + map -> native`: `F-NATIVE-USE` consumes only the exact frozen
  map after `F-MECHANICAL-BOUNDARY` and `F-MAP-ESSENCE` return closed results;
  hidden repair or stale bytes refuse.
- `native -> dogfood`: dogfood consumes exact native inputs, selected frames,
  source openings, and closed results without converting them into truth.
- `Product frames -> candidate`: candidate readiness consumes closed Product,
  map, mechanical, native, and dogfood results over one frozen inventory.
- `candidate -> publication`: the closed `F-CANDIDATE-READINESS` result and
  exact publication plan enter the separately granted Release Method
  publication relation; no frame result grants publication authority.
- `publication -> exact cut`: only publication evidence binding the frozen
  candidate, annotated RC and selector objects, peeled commit and tree, and
  remotely verified highest-RC refs may activate `F-EXACT-CUT`; partial or
  mismatched publication refuses activation.

Only closed results cross frame boundaries. Unclosed working context and ambient
conversation are not evidence.

Before publication, the six Product frames plus `F-CANDIDATE-READINESS` must
return `satisfied` on one frozen candidate after the external acceptance and
overlay prerequisite is satisfied. `F-EXACT-CUT` is not activated and cannot
veto publication. After the separately authorized publication relation
succeeds and remote verification closes, `F-EXACT-CUT` evaluates the immutable
RC; its satisfied result supports but does not perform Product-owner
acceptance.

## Residual uncertainty and revision

- Final Product member digests and the release subject are assigned only after
  exact bytes freeze.
- Native usefulness beyond observed Codex and Claude tasks remains uncertain.
- Semantic fidelity beyond the map's explicit source comparison and residuals
  remains probabilistic.
- GTL, GraphFunctions, automatic frame selection, deterministic packet
  construction, rendering, and ABG are outside this frame-set outcome.

Revise this basis when Product meaning, member or claim sets, dependency bases,
role or native-instruction law, evidence boundary, release line, actor
capability, or known material failure changes.

## Acceptance gate

Revision 12 is accepted only through a Product-owner decision naming its exact
SHA-256, frame-set URI, actor, authority, scope, and time. Only that external
decision allows `stdo_representation.json` to bind this basis.

Editing this file after presentation changes its subject and requires a new
digest and decision.
