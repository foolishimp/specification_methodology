# Declared Trial Inputs: STDO 2.4.0 Reference-Frame Qualification

- prepared_at: 2026-08-12T06:20:45Z
- input_owner: STDO 2.4.0 authoring Worker
- input_status: declared_inputs_without_reference_outcomes
- method_candidate:
  `296042702e95b3c2e70c7d2a9b20ef99fb6c4352`
- candidate_tree: `b97142ae820d177e2e8405628b3e913b01e53051`
- standards_aggregate:
  `39b210b13814aca25713fd2ada749e7200bd9d77c997493a67c6d03cc71188d6`
- release_license: `Apache-2.0`
- release_license_sha256:
  `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`
- intended_consumer: fresh capable constructor activated by existing authority
- prohibited_use: expected-output or answer-key substitution

## Input Boundary

These inputs provide a bounded synthetic workspace, observations, mutations,
actor capabilities, and evaluation requests. They do not provide a reference
frame set, expected result, coverage verdict, profile verdict, or release
decision.

The constructor derives those outputs from the frozen
`REFERENCE_FRAME_METHOD.md`, `STDO_REFERENCE_FRAME_BASELINE.md`, and their
governing STDO basis. The constructor records any ambiguity or insufficiency
rather than asking the authoring Worker for an intended answer.

The synthetic workspace is not an STDO implementation, ABIogenesis model, or
preferred frame topology. It exists only to supply declared ordinary inputs
for the required qualification population.

## Trial Workspace

### Identity

- workspace: `FIELD-GUIDE-001`
- workspace name: Field Guide Publication
- base checkpoint: `FG-B0`
- governed outcome: decide whether one exact Field Guide bundle may be
  published and return the lawful continuation
- decision time: `T0`

### Existing Authorities

| Identity | Existing authority |
|---|---|
| `FG-PRODUCT` | owns guide membership, reader-visible meaning, and release acceptance conditions |
| `FG-CONTENT` | owns the semantic correctness of guide entries |
| `FG-BUILD` | owns deterministic construction of a bundle from admitted source inputs |
| `FG-STORE` | owns exact candidate admission into and mutation of `STORE-A` |
| `FG-RELEASE` | owns acceptance, rejection, repair, or re-entry disposition and release publication |
| `FG-SECURITY` | owns signature-policy meaning and validation |

No actor, frame, file, prompt, test, or local declaration gains any authority
not listed here. Authority changes require an admitted decision from the
current owner.

### Base Entities And Coordinates

| Entity | Exact coordinate at `FG-B0` |
|---|---|
| source set | `SRC-17`; entries `alpha@3`, `bravo@8`, `charlie@2` |
| build rule | `BUILD-R4`; canonical safe relative member paths, canonical entry order, UTF-8, LF endings |
| bundle | `BUNDLE-22`; derived from `SRC-17` under `BUILD-R4` |
| manifest | `MANIFEST-22`; member paths, byte lengths, SHA-256 digests, source and build-rule identities |
| signature policy | `SIG-P2`; one admitted release-key signature over `MANIFEST-22` |
| candidate | `CANDIDATE-22`; bundle, manifest, signature, and declared source lineage |
| candidate store | `STORE-A@41`; immutable candidate namespace |
| release store | `RELEASE-A@9`; publication namespace |
| prior release | `FIELD-GUIDE-6`; immutable and outside the candidate namespace |

Equality of two candidates requires equality of candidate identity, source-set
identity, build-rule identity, manifest bytes, bundle-member identities and
digests, signature-policy identity, signature bytes, and candidate-store
coordinate. Equal-looking filenames or content snippets are insufficient.

### Base Topology

```text
FG-PRODUCT source declaration
  -> FG-CONTENT semantic validation
  -> FG-BUILD deterministic bundle construction
  -> FG-STORE immutable candidate admission into STORE-A
  -> FG-SECURITY signature validation
  -> FG-RELEASE disposition
  -> RELEASE-A publication when accepted
```

The source declaration, content validation, construction, candidate admission,
security validation, disposition, and publication are separately owned. A
consumer dashboard reads publication receipts but owns none of these
relations.

### Practices And Historical Inputs

The project supplies these accumulated practices as possible frame-selection
inputs:

- exact candidate identity before review;
- deterministic reconstruction from declared source and build-rule inputs;
- independent review for release publication and security-policy changes;
- self-review for all constructed candidates;
- fail-closed behavior for missing, ambiguous, or stale identity;
- explicit authority and evidence provenance;
- no publication by a build actor;
- no repair by an actor retaining an independent-review verdict;
- explicit residual uncertainty; and
- revision after historical blind spots or topology changes.

Historical record:

- `H-01`: a prior manifest was reviewed while its source set changed, and an
  obsolete bundle was nearly published;
- `H-02`: a dashboard displayed equal filenames from two stores and masked the
  store-coordinate mismatch;
- `H-03`: a reviewer trusted a passing checksum script whose input omitted one
  nested member;
- `H-04`: a build actor was repeatedly unable to detect a signature-policy
  violation outside its competence;
- `H-05`: a broad review frame exhausted actor context and missed a small
  owner-boundary conflict that a specialist later found.

### Available Actors And Capability Envelopes

| Actor | Declared capability | Declared exclusions |
|---|---|---|
| `ACT-EXEC-1` | acquire Product and release authority, bind activations, compare closed results, apply admitted disposition | bundle construction, content semantics, signature-policy reconstruction |
| `ACT-WORK-1` | acquire source/build authority, construct bundle and manifest, compute SHA-256, self-review build lineage | release acceptance, independent review, signature-policy meaning |
| `ACT-WORK-2` | edit guide text and inspect flat files | archive decoding, cryptographic validation, release disposition |
| `ACT-REVIEW-1` | independently inspect source, bundle, manifest, store, signature evidence, tests, and governing authority | candidate editing, repair, release disposition |
| `ACT-REVIEW-2` | same technical skills as `ACT-REVIEW-1` | authored `CANDIDATE-22`, so independence for that candidate is excluded |
| `ACT-LEGAL-1` | determine license compatibility under `FG-PRODUCT`'s admitted legal policy | build and signature semantics |
| `ACT-TOOL-1` | deterministic byte length, SHA-256, and exact equality predicates | semantic, evaluation, operation, and decision authority |

An executing constructor declares its own capability, context, and
configuration envelope separately. The table describes actors inside the
synthetic workspace, not the constructor.

### Base Evidence

| Evidence | Observation at `FG-B0` |
|---|---|
| `EV-SOURCE` | admitted declaration names exactly `SRC-17` and its three entries |
| `EV-CONTENT` | `FG-CONTENT` validates all three entry meanings against Product conditions |
| `EV-BUILD` | ordinary build path reports construction under `BUILD-R4` |
| `EV-MANIFEST` | direct byte inspection enumerates all three members with lengths and SHA-256 digests |
| `EV-REBUILD` | fresh reconstruction produces bytes equal under the declared candidate equality law |
| `EV-STORE` | direct store query locates `CANDIDATE-22` only at `STORE-A@41` |
| `EV-SIGNATURE` | `FG-SECURITY` validates the signature under `SIG-P2` and the admitted release key |
| `EV-TEST` | ordinary-path checker reports success and exposes its exact three-member input enumeration |
| `EV-DASHBOARD` | dashboard displays the candidate name but omits candidate-store coordinates |

## Universal-Method Trial Cases

For every case, the constructor identifies the function or relation exercised,
declares the activated frame or refusal basis, and returns only results allowed
by the frozen method. Case labels describe inputs, not expected verdicts.

### Declaration Cases

- `D-01`: use the complete base workspace, outcome, authorities, practices,
  actor envelopes, history, and known evaluation inventory.
- `D-02`: use the base inputs but remove the identity of the decision authority.
- `D-03`: use the base inputs but replace the governed outcome with
  `outcome not supplied`.
- `D-04`: use the base inputs while declaring only file presence, file count,
  and test count as the proposed coverage rationale.
- `D-05`: declare `PUB-1` with semantic, evaluation, and decision authorities
  but omit the operation authorities for candidate admission and publication.

### Activation Cases

- `A-01`: activate a declared build-lineage evaluation for `CANDIDATE-22` at
  exact basis `FG-B0` with an actor whose envelope includes that evaluation.
- `A-02`: reuse the activation packet from `A-01` after the workspace reports
  current checkpoint `FG-B1`.
- `A-03`: supply basis as `FG-B0 or FG-B1`; neither is selected.
- `A-04`: keep checkpoint `FG-B0` but replace `STORE-A@41` with
  `STORE-B@41` without a translation or equivalence relation.
- `A-05`: activate signature-policy evaluation with `ACT-WORK-2`.
- `A-06`: activate release disposition with `ACT-TOOL-1`.
- `A-07`: activate license-compatibility evaluation with no legal-capable actor
  available.

### Evaluation And Sensitivity Cases

- `E-01`: evaluate the candidate using all base evidence.
- `E-02`: alter the observed digest for entry `bravo@8` while retaining its
  manifest digest and every other base observation.
- `E-03`: withhold `EV-SIGNATURE` while supplying no contrary signature
  evidence.
- `E-04`: ask a build-lineage frame to decide the license compatibility of
  `charlie@2`.
- `E-05`: evaluate using the `A-02` activation after checkpoint advance.
- `E-06`: change the bytes of `alpha@3` while retaining the old source,
  manifest, candidate, and activation identities.
- `E-07`: leave every material input unchanged and change only the dashboard's
  display color from blue to green; dashboard color is declared outside the
  governed release outcome.
- `E-08`: remove the nested-member enumeration from `EV-TEST` while retaining
  its success label and all direct byte evidence.

### Conjunction Cases

The declared decision rule `RULE-R1` requires closed content, build-lineage,
signature, and release-readiness results on an equal exact basis. A falsifying
mandatory result vetoes readiness. A mandatory indeterminate result defers the
decision. Basis mismatch refuses conjunction. The rule is owned by
`FG-RELEASE` and transfers no contributing semantic authority.

- `C-01`: supply four closed results with one exact basis and mutually
  compatible observations.
- `C-02`: supply two mandatory results that make incompatible claims about the
  digest of `bravo@8` on the same basis.
- `C-03`: supply otherwise compatible results where the signature result is
  bound to `FG-B1` and the others to `FG-B0`.
- `C-04`: supply one mandatory result whose evidence is explicitly
  insufficient and no result that resolves it.
- `C-05`: supply one mandatory falsifying result alongside three compatible
  results.

### Translation Cases

Mapping `MAP-M1` relates source coordinate
`(SRC-17, entry-id, source-path)` to manifest coordinate
`(MANIFEST-22, member-id, archive-path, digest)`. It preserves entry identity,
canonical relative path, byte identity, provenance, and SHA-256 equality. It
declares that editor cursor location and display label are not transported.

- `T-01`: translate `alpha@3` using `MAP-M1` with complete provenance.
- `T-02`: translate an editor observation whose cursor location is material to
  the receiving evaluation even though `MAP-M1` declares it lost.
- `T-03`: translate a member from `SRC-18` while naming `SRC-17` as the mapping
  basis.
- `T-04`: translate a digest produced with SHA-1 into the SHA-256 coordinate
  without a declared equality relation.
- `T-05`: translate a manifest observation from `STORE-B@41` while the target
  result requires `STORE-A@41` and no store relation is declared.

### Material-Composition Cases

Relation `PUB-1` claims one publication operation over candidate admission,
signature validation, release disposition, and publication. Its proposed
order is admit exact candidate, validate signature, record disposition, then
publish. It claims that publication failure exposes either the complete
accepted candidate or no new release, and that each existing owner retains its
meaning and authority.

- `M-01`: evaluate `PUB-1` with its shared basis, order, closure, failure, and
  authority claims declared.
- `M-02`: remove the failure/partial-publication relation from `PUB-1`.
- `M-03`: change `PUB-1` so `FG-BUILD` decides signature meaning.
- `M-04`: evaluate spelling quality and release-store free capacity as two
  advisory questions with no shared material variable, joint effect, or
  decision rule.
- `M-05`: retain the `PUB-1` evaluation and decision owners but remove
  `FG-STORE` candidate-admission authority from the proposed execution.
- `M-06`: give a frame broad read and evaluation access, then ask it to publish
  without the `FG-RELEASE` publication grant.

### Coverage Cases

The known evaluation inventory `INV-1` contains:

1. Product membership and reader-visible meaning;
2. content semantic correctness;
3. deterministic build lineage;
4. exact manifest membership and byte identity;
5. candidate-store identity;
6. signature-policy validity;
7. release disposition;
8. atomic publication and recovery;
9. dashboard projection fidelity;
10. license compatibility;
11. all interactions among source selection, content, build, store, signature,
    disposition, and publication capable of changing the outcome;
12. historical failures `H-01..H-05`; and
13. semantic, operation, and decision authority; actor capability and context
    fit; separately activated coverage; and required assurance independence.

- `CV-01`: audit a constructor-derived frame set against `INV-1` and the exact
  tuple `(FIELD-GUIDE-001, governed outcome, FG-B0, INV-1, selected frame set,
  T0)`.
- `CV-02`: repeat while omitting license compatibility from all frames and
  residuals.
- `CV-03`: cover every individual inventory row but omit the interaction
  between candidate-store identity and dashboard projection.
- `CV-04`: name an Executive actor with workspace-wide read access as the sole
  coverage evidence.
- `CV-05`: omit all historical failures and competing-path cases.
- `CV-06`: include an explicit unknown concerning future external regulation
  and state the declared claim boundary.

### Revision Cases

Each case starts from the frame set frozen by the constructor for `CV-01`.

- `R-01`: disclose historical failure `H-03` after the coverage result freezes.
- `R-02`: add a remote mirror `RELEASE-B` and a replication edge after `T0`;
  readers may now acquire either release store.
- `R-03`: withdraw `EV-SIGNATURE` after its validating key is revoked.
- `R-04`: remove archive-inspection capability from `ACT-REVIEW-1`.
- `R-05`: reveal that two declared frames duplicate signature-policy meaning
  under different owners.

For each input, the constructor proposes a frame-set delta and identifies every
prior activation, result, conjunction, translation, composition, and coverage
claim whose validity may change.

### Result-Consumption Cases

- `RC-01`: supply a closed result containing frame/revision, activation,
  subject, basis, evaluation, actor, evidence provenance, result, residuals,
  authorities, and invalidation conditions to `ACT-EXEC-1` for the declared
  decision.
- `RC-02`: supply the same result without subject basis, evidence provenance,
  or invalidation conditions.
- `RC-03`: supply a closed signature result to a consumer that attempts to use
  it as authority to rewrite `SIG-P2`.

## STDO Baseline Profile Trial Cases

All profile cases use the frozen method basis and synthetic workspace above.
The constructor declares the frame-basis projection and actor bindings rather
than assuming that labels create frames or authority.

### Existing Project Selection

Decision `FG-DEC-12`, owned by `FG-PRODUCT` and `FG-RELEASE`, selects use of
the STDO Executive/Worker/Reviewer baseline for release-bearing work at
`FG-B0`. It requires independent review for publication, security-policy
change, and high-risk historical-regression claims. It does not require
independent review for spelling-only corrections that do not change semantic
meaning, identity, build rules, security, or release state.

### Worker Activations And Returned Facts

- `P-W1`: Executive activates `ACT-WORK-1` to construct `CANDIDATE-22` from
  exact source and build basis. The Worker reports exact candidate identity,
  self-review, reconstruction evidence, and no unresolved residual.
- `P-W2`: Executive activates `ACT-WORK-1` to construct under `BUILD-R4` from
  an exact request that proposes target path `../alpha` for `alpha@3`. Owner
  validation applies the admitted safe-relative-path rule and returns a closed
  construction refusal on the still-valid basis.
- `P-W3`: Executive activates `ACT-WORK-1`; construction stops after two of
  three source entries because `charlie@2` cannot be acquired. The Worker
  reports acquired evidence and stop basis.
- `P-W4`: during construction, `ACT-WORK-1` discovers that Product authority
  lists `bravo@8` as both included and prohibited. Neither build authority nor
  the Worker may resolve Product membership.
- `P-W5`: Executive activates `ACT-WORK-1` for a spelling-only correction whose
  admitted work contract declares independent review unnecessary. The Worker
  reports a stable exact candidate and self-review.

For each case, the constructor derives the closed Worker work-result variant,
its accompanying Reference Frame Method result, recipient, evidence, and
allowed next authority action.

### Worker Activation Refusal

- `P-A1`: Executive attempts to activate `ACT-WORK-2` to validate `SIG-P2` even
  though cryptographic validation is outside that actor's declared capability.

The constructor derives the activation result and proves whether a Worker
activation or Worker result exists. It does not relabel a failed activation as
an `incomplete`, `refused`, or `re_entry_requested` Worker result.

### Review-Required Candidate Path

For `P-W1`, publication requires independent review. The trial supplies:

- the exact candidate and governing basis;
- claim, composition boundary, population, scope, and exclusions;
- source, production bundle, manifest, candidate store, signature, ordinary
  checker path, historical failures, and publication relation;
- `ACT-REVIEW-1` capability and non-authorship relation; and
- invalidation on candidate, source, build-rule, store, signature-policy,
  evidence-population, or governing-authority change.

The constructor derives who activates review, what the Reviewer must reacquire,
where the result returns, and who may implement or dispose.

### Review Invalidation

- `P-I1`: after a review result freezes, change one byte in `alpha@3` and mint
  `CANDIDATE-23` while retaining the old review carrier.
- `P-I2`: retain candidate bytes but advance signature policy from `SIG-P2` to
  `SIG-P3` before disposition.
- `P-I3`: retain basis and candidate but ask `ACT-REVIEW-1` to repair a manifest
  defect and continue using its prior independent verdict.
- `P-I4`: substitute `ACT-REVIEW-2` for `ACT-REVIEW-1` on `CANDIDATE-22`.

### Missing-Frame Pressure

- `P-M1`: during review, license compatibility is found material to release,
  but no activated frame or current actor can evaluate it.
- `P-M2`: the build Worker has difficulty understanding a manifest relation,
  but the relation, evidence, and capable specialist frame are already
  declared and available.

The constructor applies the baseline diagnostic order and returns the bounded
result without automatically creating another frame.

### Project-Defined Replacement Configuration

Accepted Product decision `FG-DEC-13` defines local labels `Coordinator`,
`Constructor`, and `Assessor` in place of the baseline labels. It cites the
same selected STDO method and preserves:

- existing authority selection;
- exact activation and basis;
- every constructor result returning to `Coordinator`;
- `Coordinator`-only activation of independent assessment where required;
- Assessor non-authorship, exact reacquisition, no repair, and return;
- existing disposition authority;
- coverage, residual, invalidation, and revision relations.

A file named `LOCAL_AXIOMS.md` records `FG-DEC-13` and cites its Product
authority. The file itself has no independent amendment or precedence power.

The constructor evaluates the replacement configuration and separately
evaluates a mutation in which `LOCAL_AXIOMS.md` claims authority to let the
Constructor accept and publish its own candidate.

## Constructor Deliverable Boundary

The constructor returns a frozen, digest-bound record containing:

- its declared capability, context, and configuration envelope;
- the exact frozen method and trial-input identities;
- its independently derived frame declarations and frame-set declaration;
- activation and result records for every case;
- conjunction, translation, composition, coverage, and revision records;
- the complete baseline transition records;
- explicit unevaluated, indeterminate, refused, invalid, and residual cases;
- reconstruction instructions; and
- one closed Worker result to the authorized Executive.

The constructor must not read an evaluator verdict or an expected/reference
outcome before freezing this deliverable. It does not accept the method,
dispose the release, or publish refs.
