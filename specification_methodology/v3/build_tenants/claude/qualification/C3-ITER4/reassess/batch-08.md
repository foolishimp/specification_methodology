# I4-04 reading batch 08

Rows: 12. Members: ['UX_METHOD.md', 'WORLD_MODEL_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `UX_METHOD.md#3a-ux-projection-and-constructive-carrier-boundary` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#3a-ux-projection-and-constructive-carrier-boundary` at rc.2:

```text
UX surfaces are projection and control surfaces. They render admitted truth and
emit typed messages.

A UX-local `Msg` may govern view-local concerns such as expansion state, sort
order, filter text, focus movement, or draft input.

A UX `Msg` that changes product truth is not merely a UX concern. Product-truth
changes include:

- writing, creating, moving, or deleting assets
- changing Context, selection authority, pinning, or global product state
- spawning, attaching, or resuming sessions
- dispatching agents, jobs, workorders, graph calls, or runtime commands
- changing closure, approval, continuation, lineage, provenance, or evidence
- publishing, accepting, rejecting, or superseding product records

Such a message must map to one admitted product carrier:

- an `AssetSurface` action
- a published graph function or lawful graph-function composition
- a workorder, job, or runtime command admitted by the product's design
- an ABG event or command boundary where ABG is the runtime authority
- another typed product contract named by the design module

The UX layer must not become the hidden constructive carrier. If no admitted
carrier exists for a product-truth-changing message, the UX surface is blocked
until the carrier is authored or the requirement is repriced.

---
```

Successor, `UX.md#3-product-truth-and-admitted-carriers`:

```text
UX surfaces are projection and control surfaces: they render admitted
truth and emit typed messages (P6, P0;
rc.2 #3a-ux-projection-and-constructive-carrier-boundary). A UX-local Msg
may govern view-local concerns such as expansion state, sort order,
filter text, focus movement or draft input. A Msg that changes product
truth is not merely a UX concern. Product-truth changes include:

- writing, creating, moving or deleting assets;
- changing Context, selection authority, pinning or global product state;
- spawning, attaching or resuming sessions;
- dispatching agents, jobs, workorders, graph calls or runtime commands;
- changing closure, approval, continuation, lineage, provenance or
  evidence;
- publishing, accepting, rejecting or superseding product records.

Such a message maps to one admitted product carrier (P6, P4a):

- an AssetSurface action;
- a published graph function or lawful graph-function composition;
- a workorder, job or runtime command admitted by the product's design;
- an ABG event or command boundary where ABG is the runtime authority;
- another typed product contract named by the design module.

The UX layer does not become the hidden constructive carrier. If no
admitted carrier exists for a product-truth-changing message, the UX
surface is blocked until the carrier is authored or the requirement is
repriced (P6, P5; §15 states the result).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#8a-msg-replay-proof-requirement` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#8a-msg-replay-proof-requirement` at rc.2:

```text
Every product UX surface must carry at least one executable Msg-replay proof for
each product-meaningful interaction family before claiming method closure.

A replay proof includes:

- an initial `State` fixture
- an ordered `Msg` log
- the expected final `State`
- the expected ordered `Cmd` values
- the success and failure `Msg` values returned by interpreted `Cmd`s
- injected deterministic values for time, randomness, generated ids, and
  external payloads

The proof fails if correctness depends on:

- DOM state not represented in `State`
- mutable refs, module variables, closures, timers, or effect-handler memory
- network or file results that bypass typed `Msg`
- view-local state that changes product behavior after unmount or replay

For a pure projection-only surface, the replay proof may be a no-effect proof:
`Msg` log plus final `State` and empty `Cmd` sequence.

---
```

Successor, `UX.md#msg-replay-proof`:

```text
Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
Purpose and material relation: the Msg log is the surface's recorded work
state, and replay is resumption from it
([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
A surface whose behaviour cannot be reproduced from its log holds state
that no later actor or session can recover or check, so the proof is the
evidence that the view owns no hidden continuation (P0, P4b). A
replay proof includes:

- an initial State fixture;
- an ordered Msg log;
- the expected final State;
- the expected ordered Cmd values;
- the success and failure Msg values returned by interpreted Cmds;
- injected deterministic values for time, randomness, generated ids and
  external payloads.

The proof fails if correctness depends on (P5, P4b):

- DOM state not represented in State;
- mutable refs, module variables, closures, timers or effect-handler
  memory;
- network or file results that bypass typed Msg;
- view-local state that changes product behaviour after unmount or
  replay.

For a pure projection-only surface, the replay proof may be a no-effect
proof: a Msg log plus the final State and an empty Cmd sequence (P2).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `WORLD_MODEL_METHOD.md#3-verification-by-treatment` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#3-verification-by-treatment` at rc.2:

```text
A candidate identity direction is accepted only if projection along
it preserves object identity under held-out treatments. The builder
must record at least one acceptable verification:

- α-sweep: apply `x − α · d` on held-out contexts, show expected
  identity shift and its saturation behaviour
- transplant: apply `x + α · d` to null-peer instances, show
  identity acquisition
- boundary test: overwrite attributes outside the projection support
  and show identity survives (this is what discriminates geometric
  blanket from set-membership blanket)

A direction that has no acceptable verification is a candidate, not an
accepted overlay. Publishing an unverified direction is a violation of
the Representation Law. The underlying entity cut remains lawful and
publishable without the overlay.

The empirical program that motivates these treatments reports that the
strongest of them — direction-native conditional independence — has been
tested and does not close. Passing this battery establishes that a
direction is verified for publication under this method; it does not
establish a formally closed Markov blanket. See *Epistemic Status Of The
Construct*.
```

Successor, `WORLD_MODEL.md#verification-by-treatment`:

```text
A candidate identity direction is accepted only if projection along it
preserves object identity under held-out treatments. The builder records
at least one acceptable verification (P6, P3;
rc.2 #3-verification-by-treatment):

- α-sweep: apply `x − α · d` on held-out contexts, and show the expected
  identity shift and its saturation behaviour;
- transplant: apply `x + α · d` to null-peer instances, and show identity
  acquisition;
- boundary test: overwrite attributes outside the projection support and
  show identity survives (this is what discriminates a geometric blanket
  from a set-membership blanket).

A direction that has no acceptable verification is a candidate, not an
accepted overlay. Publishing an unverified direction violates the
Representation law (§8). The underlying entity cut remains lawful and
publishable without the overlay (P6, P3). The empirical program that
motivates these treatments reports that the strongest of them,
direction-native conditional independence, has been tested and does not
close. Passing this battery establishes that a direction is verified for
publication under this profile; it does not establish a formally closed
Markov blanket (§4 Epistemic status) (P6).
```

Successor, `WORLD_MODEL.md#14-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide publication of entity
cuts and overlays and enter conjunctions with the results of other
members, which combine only in the core, so an inadmissible cut, an
unverified direction or a failed gate run is never read as publishable
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| cut admissibility | is the entity cut admissible (§9 Admissibility) | the entity cut's eight surfaces are explicit, traceable and discriminated from plausible alternatives at evidence altitude proportional to its claim |
| direction acceptance | is a candidate identity direction accepted (§10 Identity-direction extraction, Verification by treatment) | the identity direction is built by an admissible extraction, projection along it preserves object identity under held-out treatments, and at least one acceptable verification is recorded |
| overlay publication | does a published overlay rest on an accepted direction (§8 Representation law, §10 Verification by treatment) | the published overlay's direction has a recorded acceptable verification |
| overlay storage | does the stored overlay keep its package (§10 Storage shape) | the stored overlay retains the six surfaces of §10 Storage shape |
| null-peer discrimination | is the candidate a lawful Markov object by null-peer comparison (§10 Null-peer discrimination) | the candidate passes the uniqueness test and the transfer test |
| promotion gate | does a run of the promotion gate meet its predicate (§4 Epistemic status) | this run of the direction-native conditional-independence test meets its predicate |
| saturation | is the attribute ledger sufficiently saturated for publication (§11 Saturation law) | materially important attributes have traceable support, the remaining gaps are explicit ambiguities, and the resulting cut is stable enough to publish |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| cut admissibility | `cut_admissible` | satisfied | each surface is a stated value, a stated absence or a stated non-applicability with its reason, is traced, and is discriminated at the stated altitude; a stated bound on evidence altitude with its residual ambiguity declared meets the test (sparse first publication) |
| cut admissibility | `cut_inadmissible` | falsified | a surface is neither a stated value, a stated absence nor a stated non-applicability, or is untraceable, or the admissible evidence shows the boundary undiscriminated from a plausible alternative; that surface or alternative is the counterexample |
| cut admissibility | `discrimination_undecided` | indeterminate | no counterexample of `cut_inadmissible` is found, and the admissible evidence cannot decide the discrimination the cut itself claims at its stated altitude; the value names the evidence that would decide |
| direction acceptance | `direction_verified` | satisfied | the direction is built by an admissible extraction in its declared representation space, at least one acceptable verification is recorded with identity preserved under held-out treatment, and no recorded verification shows identity lost |
| direction acceptance | `extraction_inadmissible` | falsified | the direction is built by a principal-component or maximum-variance construction, which is not admissible as an identity direction, whatever its verification shows; that construction is the counterexample |
| direction acceptance | `verification_failed` | falsified | the extraction is admissible, and a recorded verification shows identity not preserved under held-out treatment; that verification is the counterexample |
| direction acceptance | `verification_inconclusive` | indeterminate | the extraction is admissible in a declared representation space, no recorded verification establishes an acceptable preservation or shows identity lost, and a recorded verification ran without establishing either; the value names the held-out treatment or verification that would decide |
| direction acceptance | `representation_space_invalid` | invalid_basis | no counterexample of `extraction_inadmissible` or `verification_failed` is found, and the overlay declares no representation space, or its direction is composed with directions computed in another space; that basis cannot support the evaluation (§10) |
| overlay publication | `published_verified` | satisfied | the published direction has a recorded acceptable verification |
| overlay publication | `published_unverified` | falsified | a direction with no acceptable verification is published, which violates §8 Representation law (§10 Verification by treatment); that publication is the counterexample |
| overlay storage | `storage_retained` | satisfied | the stored package retains the declared representation space and its version, the geometric object, the distributed evidence, the verification trace, the provenance and authority record, and the supersession record |
| overlay storage | `storage_lossy` | falsified | the stored layout loses one of those surfaces; the lost surface is the counterexample |
| null-peer discrimination | `null_peer_discriminated` | satisfied | the identity-loaded attributes in the candidate's core are unique to it among its null peers, and its identity direction transfers more cleanly than a random diagonal |
| null-peer discrimination | `not_yet_lawful` | falsified | the uniqueness test or the transfer test fails, so the cluster is not yet a lawful Markov object; the failing test is the counterexample |
| promotion gate | `gate_met` | satisfied | the run meets the test's predicate |
| promotion gate | `gate_not_met` | falsified | the run does not meet the test's predicate; it is the counterexample for that run only, and the construct's standing is unchanged |
| saturation | `saturated` | satisfied | the three conditions hold; the explicit gaps are carried as residuals |
| saturation | `not_saturated` | falsified | a condition fails, as where an attribute exists without traceable support (silent unsupported attribute creation) or a gap is a silent miss; that attribute or gap is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `representation_space_invalid` (P5).

A verification not run. Where no ground of `extraction_inadmissible` or
`representation_space_invalid` holds, a candidate direction whose
verification has not been run has no result for direction acceptance:
the verification is the evaluation of that predicate, and it was not
performed, so it has no
closed result and is never mapped to
`indeterminate` or to any other core value
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). The
direction stays a candidate (§10 Verification by treatment). In every
conjunction over its acceptance, the unrun verification is a planned
assessment without a closed result
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps) where the verification was planned; where none was planned, the
obligation it would have discharged is uncovered coverage. A step whose output needed that verification and that stopped
without it ends `incomplete`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps for the predicate "a candidate is available", never to
`indeterminate`; the step's work state carries the unrun verification as
a residual ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)).
Publishing the unverified direction is `published_unverified` (P5, P6).

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.
```


### Row `WORLD_MODEL_METHOD.md#6-overlay-publication` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#6-overlay-publication` at rc.2:

```text
A published Markov-object overlay must make visible, at minimum:

- **representation space**: the declared space and attribute basis the
  direction is expressed in, versioned so a later re-fit is detectable
- **identity direction**: the projection (representation-space
  vector or equivalent geometric description)
- **attribute evidence**: core + coat, traced to ledger entries
- **verification record**: treatments used, outcomes observed,
  held-out contexts evaluated
- **boundary characterization**: projection support on which identity
  was preserved under treatment
- **null-peer comparison**: what similar things were tested, what
  was accepted, what was rejected
- **effective coordinate**: α along direction for this instance,
  where applicable

An overlay is an immutable projection. Revising the identity direction —
because new contexts, new evidence, or a re-fitted representation space
became available — produces a new overlay that supersedes the prior one.
A change of representation space changes every direction expressed in it
and is therefore a supersession even when no ledger entry changed. Prior
overlays are never mutated in place (see Publication Law).
```

Successor, `WORLD_MODEL.md#overlay-publication`:

```text
A published Markov-object overlay makes visible, at minimum (P6, P3;
rc.2 #6-overlay-publication):

- representation space: the declared space and attribute basis the
  direction is expressed in, versioned so a later re-fit is detectable;
- identity direction: the projection (a representation-space vector or
  equivalent geometric description);
- attribute evidence: core and coat, traced to ledger entries;
- verification record: treatments used, outcomes observed, held-out
  contexts evaluated;
- boundary characterisation: the projection support on which identity was
  preserved under treatment;
- null-peer comparison: what similar things were tested, what was
  accepted, what was rejected;
- effective coordinate: α along the direction for this instance, where
  applicable.

An overlay is an immutable projection. Revising the identity direction,
because new contexts, new evidence or a re-fitted representation space
became available, produces a new overlay that supersedes the prior one.
A change of representation space changes every direction expressed in it
and is therefore a supersession even when no ledger entry changed. Prior
overlays are never mutated in place (§8 Publication law) (P4b, P3).
```


### Row `WORLD_MODEL_METHOD.md#admissibility` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#admissibility` at rc.2:

```text
An entity cut is admissible when its identity, boundary, authority, state,
evidence, treatment, covariance, and ambiguity are explicit, traceable, and
discriminated from plausible alternatives at evidence altitude proportional to
the claim.

That is the whole constitutional test. It binds what must be true of a
published cut. It does not prescribe how a builder establishes it.

"Explicit" admits three lawful values on every surface: a stated value, stated
absence, or stated non-applicability with its reason. A cut whose entity has no
adjacent-domain treatment says so; it does not manufacture one. This keeps the
predicate whole without adding evidence machinery.

Sparse first publication remains lawful. A unique, historical, single-context,
inaccessible, or regulated entity is publishable when the above holds and its
residual ambiguity is declared. Absence of a comparison population, of repeated
contexts, or of permission to intervene is a bound on evidence altitude to be
stated, not a bar to publication.
```

Successor, `WORLD_MODEL.md#admissibility`:

```text
An entity cut is admissible when its identity, boundary, authority,
state, evidence, treatment, covariance and ambiguity are explicit,
traceable, and discriminated from plausible alternatives at evidence
altitude proportional to the claim (P3, P6; rc.2 #admissibility). That is
the whole constitutional test. It binds what is true of a published cut;
it does not prescribe how a builder establishes it (P0).

"Explicit" admits three lawful values on every surface: a stated value,
stated absence, or stated non-applicability with its reason. A cut whose
entity has no adjacent-domain treatment says so; it does not manufacture
one. This keeps the predicate whole without adding evidence machinery
(P5).

Sparse first publication remains lawful. A unique, historical,
single-context, inaccessible or regulated entity is publishable when the
test above holds and its residual ambiguity is declared. Absence of a
comparison population, of repeated contexts, or of permission to
intervene is a bound on evidence altitude to be stated, not a bar to
publication (P5, P2).
```

Successor, `WORLD_MODEL.md#14-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide publication of entity
cuts and overlays and enter conjunctions with the results of other
members, which combine only in the core, so an inadmissible cut, an
unverified direction or a failed gate run is never read as publishable
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| cut admissibility | is the entity cut admissible (§9 Admissibility) | the entity cut's eight surfaces are explicit, traceable and discriminated from plausible alternatives at evidence altitude proportional to its claim |
| direction acceptance | is a candidate identity direction accepted (§10 Identity-direction extraction, Verification by treatment) | the identity direction is built by an admissible extraction, projection along it preserves object identity under held-out treatments, and at least one acceptable verification is recorded |
| overlay publication | does a published overlay rest on an accepted direction (§8 Representation law, §10 Verification by treatment) | the published overlay's direction has a recorded acceptable verification |
| overlay storage | does the stored overlay keep its package (§10 Storage shape) | the stored overlay retains the six surfaces of §10 Storage shape |
| null-peer discrimination | is the candidate a lawful Markov object by null-peer comparison (§10 Null-peer discrimination) | the candidate passes the uniqueness test and the transfer test |
| promotion gate | does a run of the promotion gate meet its predicate (§4 Epistemic status) | this run of the direction-native conditional-independence test meets its predicate |
| saturation | is the attribute ledger sufficiently saturated for publication (§11 Saturation law) | materially important attributes have traceable support, the remaining gaps are explicit ambiguities, and the resulting cut is stable enough to publish |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| cut admissibility | `cut_admissible` | satisfied | each surface is a stated value, a stated absence or a stated non-applicability with its reason, is traced, and is discriminated at the stated altitude; a stated bound on evidence altitude with its residual ambiguity declared meets the test (sparse first publication) |
| cut admissibility | `cut_inadmissible` | falsified | a surface is neither a stated value, a stated absence nor a stated non-applicability, or is untraceable, or the admissible evidence shows the boundary undiscriminated from a plausible alternative; that surface or alternative is the counterexample |
| cut admissibility | `discrimination_undecided` | indeterminate | no counterexample of `cut_inadmissible` is found, and the admissible evidence cannot decide the discrimination the cut itself claims at its stated altitude; the value names the evidence that would decide |
| direction acceptance | `direction_verified` | satisfied | the direction is built by an admissible extraction in its declared representation space, at least one acceptable verification is recorded with identity preserved under held-out treatment, and no recorded verification shows identity lost |
| direction acceptance | `extraction_inadmissible` | falsified | the direction is built by a principal-component or maximum-variance construction, which is not admissible as an identity direction, whatever its verification shows; that construction is the counterexample |
| direction acceptance | `verification_failed` | falsified | the extraction is admissible, and a recorded verification shows identity not preserved under held-out treatment; that verification is the counterexample |
| direction acceptance | `verification_inconclusive` | indeterminate | the extraction is admissible in a declared representation space, no recorded verification establishes an acceptable preservation or shows identity lost, and a recorded verification ran without establishing either; the value names the held-out treatment or verification that would decide |
| direction acceptance | `representation_space_invalid` | invalid_basis | no counterexample of `extraction_inadmissible` or `verification_failed` is found, and the overlay declares no representation space, or its direction is composed with directions computed in another space; that basis cannot support the evaluation (§10) |
| overlay publication | `published_verified` | satisfied | the published direction has a recorded acceptable verification |
| overlay publication | `published_unverified` | falsified | a direction with no acceptable verification is published, which violates §8 Representation law (§10 Verification by treatment); that publication is the counterexample |
| overlay storage | `storage_retained` | satisfied | the stored package retains the declared representation space and its version, the geometric object, the distributed evidence, the verification trace, the provenance and authority record, and the supersession record |
| overlay storage | `storage_lossy` | falsified | the stored layout loses one of those surfaces; the lost surface is the counterexample |
| null-peer discrimination | `null_peer_discriminated` | satisfied | the identity-loaded attributes in the candidate's core are unique to it among its null peers, and its identity direction transfers more cleanly than a random diagonal |
| null-peer discrimination | `not_yet_lawful` | falsified | the uniqueness test or the transfer test fails, so the cluster is not yet a lawful Markov object; the failing test is the counterexample |
| promotion gate | `gate_met` | satisfied | the run meets the test's predicate |
| promotion gate | `gate_not_met` | falsified | the run does not meet the test's predicate; it is the counterexample for that run only, and the construct's standing is unchanged |
| saturation | `saturated` | satisfied | the three conditions hold; the explicit gaps are carried as residuals |
| saturation | `not_saturated` | falsified | a condition fails, as where an attribute exists without traceable support (silent unsupported attribute creation) or a gap is a silent miss; that attribute or gap is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `representation_space_invalid` (P5).

A verification not run. Where no ground of `extraction_inadmissible` or
`representation_space_invalid` holds, a candidate direction whose
verification has not been run has no result for direction acceptance:
the verification is the evaluation of that predicate, and it was not
performed, so it has no
closed result and is never mapped to
`indeterminate` or to any other core value
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). The
direction stays a candidate (§10 Verification by treatment). In every
conjunction over its acceptance, the unrun verification is a planned
assessment without a closed result
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps) where the verification was planned; where none was planned, the
obligation it would have discharged is uncovered coverage. A step whose output needed that verification and that stopped
without it ends `incomplete`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps for the predicate "a candidate is available", never to
`indeterminate`; the step's work state carries the unrun verification as
a residual ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)).
Publishing the unverified direction is `published_unverified` (P5, P6).

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.
```


### Row `WORLD_MODEL_METHOD.md#builder-project` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#builder-project` at rc.2:

```text
A **Builder Project** has concept identity
`urn:stdo:concept:world-model:builder-project`.

A configured project instance of the builder with its own source inputs,
settings, and publication lane.

Its relation to `Source Project` is the explicit directional specialization in
*Builder-Project Specialization Relation*; this local clause must not be read as
an unchanged import or general equivalence.
```

Successor, `WORLD_MODEL.md#6-units`:

```text
The profile's units (P3; rc.2 #app, #builder-project and the sibling
unit anchors named in §15):

| Unit | Definition | Requires |
|---|---|---|
| App | a world-model builder application | P3 |
| Builder Project | concept identity `urn:stdo:concept:world-model:builder-project`; a configured project instance of the builder with its own source inputs, settings and publication lane; its relation to Source Project is the directional specialisation of §2 Builder Project specialisation, and this clause is not read as an unchanged import or general equivalence | P3, P1 |
| Published Domain Artifact | a published immutable world-model output built by a builder project | P3, P4b |
| Fragment | a bounded published slice inside a published domain artifact | P3 |
| World Model Object | a generic shorthand for something treated as real in the institutional operating model; intentionally weaker than Markov Object; useful during observation, extraction, review and discussion; not the preferred name for the primary published semantic unit once the builder has constructed a governed identity-bearing cut | P3, P1 |
| Assurance | the governed basis on which a traced source observation is accepted as a qualified semantic claim; it answers why a claim is lawful world-model truth rather than merely a raw observation | P6 |
| Attribute Ledger | an append-only ordered record of qualified attribute claims over a stable object identity; entries may carry observed values, derived values, interpreted meanings, rule or constraint claims, topology or relation claims, provenance and authority claims, and effective, observed and publication coordinates | P4b, P3 |
| Markov Object | below | P3 |
| Entity Cut | below | P3, P6 |
| Markov-Object Overlay | an optional geometric overlay on an entity cut, admissible only where a declared representation space exists; it adds an identity direction, projection support and effective coordinate, constructed and verified under §10; the overlay strengthens an entity cut, and its absence does not weaken one | P3, P6 |
| Treatment Surface | a semantic reinterpretation from one domain into another | P1 |
| Covariance Edge | a declared relation showing how changes in one object correspond to changes in another | P1, P3 |
| Adjoint Mapping | the interpret-back contract for a treatment | P1 |
| Temporal Reference Artifact | a changing value list, code set or classification set whose semantics matter for object interpretation | P3, P1 |
| Composed World Model | a higher-order world model built by referencing and stitching published domain artifacts while preserving their identity, version and local authority | P4a, P6 |
| Projection | a user-facing or downstream-facing artifact derived from the semantic kernel | P1 |
| Query Plane | an optional downstream serving surface that makes published domain artifacts or composed world models queryable or traversable without becoming the constitutional publication authority | P6 |

Markov Object. A stable self-bounding world-model object whose internal
state can be reasoned about through its effective blanket (§4). The
published Markov object is an immutable object cut projected from the
attribute ledger, not an in-place mutable record; the cut is an identity
direction together with the distributed attribute evidence that supports
it, not an enumeration of member columns (P3, P4b; rc.2 #markov-object).
The Markov object is the theoretical account of why a discovered boundary
is a real object rather than an arbitrary cluster. It is not a claim that
the builder invents the object: institutional entities are already
committed by people, implicitly in code paths, records and workflows or
explicitly in schemas and policy, and the profile's practical work is to
trawl existing systems and recover them. A recovered entity is published
as an Entity Cut; where the builder additionally operates over a
representation space in which identity is a geometric direction, the
entity cut may carry a Markov-object overlay. The theory is §4, the
discovery obligations §9, and the representation-substrate obligations
§10 (P3, P6).

Entity Cut. The primary published semantic unit: an identity-bearing,
bounded, evidence-backed cut of a recovered entity, projected from the
attribute ledger (P3, P6; rc.2 #entity-cut). An entity cut is lawful
without an identity direction. It publishes identity, boundary,
authority, state, evidence, treatment, covariance and ambiguity, each
traced to ledger entries and their assurance basis. Builder projects may
begin with looser object candidates; world-model publication converges
them into entity cuts, or explicitly leaves them as non-object artifacts
such as treatment surfaces, covariance edges or temporal reference
artifacts (P3, P5).
```


### Row `WORLD_MODEL_METHOD.md#composition-law` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#composition-law` at rc.2:

```text
Do not build one central monolith first.

Build local published domain artifacts and their entity cuts, then
stitch them.

Composition must preserve:

- fragment authority
- bounded-context meaning
- treatment semantics
- declared loss
- ambiguity

Higher-order models are composed from published domain artifacts. They do not
erase them.

The preferred end-state is a federated world-model mesh rather than a single
flattened enterprise model.

Detailed mesh topology may remain product-local while the line is still being
developed. Method-level mesh law should be ratified only once the reusable node
and edge model is stable.

---
```

Successor, `WORLD_MODEL.md#composition-law`:

```text
Do not build one central monolith first. Build local published domain
artifacts and their entity cuts, then stitch them (P4a, P6;
rc.2 #composition-law). Composition preserves fragment authority,
bounded-context meaning, treatment semantics, declared loss and
ambiguity. Higher-order models are composed from published domain
artifacts; they do not erase them (P4a, P4b). The preferred end state is
a federated world-model mesh rather than a single flattened enterprise
model. Detailed mesh topology may remain product-local while the line is
still being developed; profile-level mesh law should be ratified only
once the reusable node and edge model is stable (P2, P6).
```


### Row `WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct` at rc.2:

```text
The method commits to the Markov-object construct as load-bearing
working vocabulary. The empirical program that sharpens it is at
candidate status: it reports evidence consistent with the
geometric-blanket reading but does not close the
conditional-independence condition that would formally establish a
Markov object in the statistical sense.

Adopting this method does not require that the empirical program be
complete. Method commitments that depend on a formally established
conditional-independence object — for example, claims that a
published Markov-object overlay *is* the blanket rather than a
candidate for it — must be read as working commitments, open to
revision when the companion program produces a conditional-independence
result.

Promotion gate. The experimental result that would promote the
construct from candidate to established is a direction-native
conditional-independence test: given the identity projection,
residual variation along remaining components should be independent
of the target under plausible treatments. That test has been run and
did not meet its predicate, and its multi-layer successor did not
either. The gate stands where it is; it has not been met and must not
be relocated to accommodate the negative result.

This status attaches to the Markov-object construct and to overlays
built on it. A published Markov-object overlay is a candidate-class
overlay of a candidate construct, not a certified blanket of a
formally-established object.

It does not attach to entity cuts. An entity cut is lawful published
truth on its own admissibility test and does not inherit the
construct's candidate status. A candidate entity that has not met
that test is a candidate; a published entity cut is not.

This epistemic status is inherited downstream. Tooling that
materializes Markov-object overlays under this method should default to a
candidate-class publication kind and reserve any formally-closed
publication kind for cuts backed by a real promotion-gate result.
```

Successor, `WORLD_MODEL.md#epistemic-status`:

```text
The profile commits to the Markov-object construct as load-bearing
working vocabulary. The empirical program that sharpens it is at
candidate status: it reports evidence consistent with the
geometric-blanket reading but does not close the conditional-independence
condition that would formally establish a Markov object in the
statistical sense, which FOUNDATIONS §5 carries as a hypothesis (P6;
rc.2 #epistemic-status-of-the-construct). Adopting this profile does not
require that the empirical program be complete. Commitments that depend on
a formally established conditional-independence object, for example
claims that a published Markov-object overlay is the blanket rather than
a candidate for it, are read as working commitments, open to revision
when the companion program produces a conditional-independence result
(P6, P5).

Promotion gate. The experimental result that would promote the construct
from candidate to established is a direction-native
conditional-independence test: given the identity projection, residual
variation along remaining components should be independent of the target
under plausible treatments. That test has been run and did not meet its
predicate, and its multi-layer successor did not either. The gate stands
where it is; it has not been met and is not relocated to accommodate the
negative result (P6).

This status attaches to the construct and to overlays built on it. A
published Markov-object overlay is a candidate-class overlay of a
candidate construct, not a certified blanket of a formally established
object. It does not attach to entity cuts: an entity cut is lawful
published truth on its own admissibility test (§9) and does not inherit
the construct's candidate status. A candidate entity that has not met
that test is a candidate; a published entity cut is not (P3, P6). The
status is inherited downstream: tooling that materialises Markov-object
overlays under this profile should default to a candidate-class
publication kind and reserve any formally closed publication kind for
cuts backed by a real promotion-gate result (P6).
```

Successor, `WORLD_MODEL.md#14-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide publication of entity
cuts and overlays and enter conjunctions with the results of other
members, which combine only in the core, so an inadmissible cut, an
unverified direction or a failed gate run is never read as publishable
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| cut admissibility | is the entity cut admissible (§9 Admissibility) | the entity cut's eight surfaces are explicit, traceable and discriminated from plausible alternatives at evidence altitude proportional to its claim |
| direction acceptance | is a candidate identity direction accepted (§10 Identity-direction extraction, Verification by treatment) | the identity direction is built by an admissible extraction, projection along it preserves object identity under held-out treatments, and at least one acceptable verification is recorded |
| overlay publication | does a published overlay rest on an accepted direction (§8 Representation law, §10 Verification by treatment) | the published overlay's direction has a recorded acceptable verification |
| overlay storage | does the stored overlay keep its package (§10 Storage shape) | the stored overlay retains the six surfaces of §10 Storage shape |
| null-peer discrimination | is the candidate a lawful Markov object by null-peer comparison (§10 Null-peer discrimination) | the candidate passes the uniqueness test and the transfer test |
| promotion gate | does a run of the promotion gate meet its predicate (§4 Epistemic status) | this run of the direction-native conditional-independence test meets its predicate |
| saturation | is the attribute ledger sufficiently saturated for publication (§11 Saturation law) | materially important attributes have traceable support, the remaining gaps are explicit ambiguities, and the resulting cut is stable enough to publish |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| cut admissibility | `cut_admissible` | satisfied | each surface is a stated value, a stated absence or a stated non-applicability with its reason, is traced, and is discriminated at the stated altitude; a stated bound on evidence altitude with its residual ambiguity declared meets the test (sparse first publication) |
| cut admissibility | `cut_inadmissible` | falsified | a surface is neither a stated value, a stated absence nor a stated non-applicability, or is untraceable, or the admissible evidence shows the boundary undiscriminated from a plausible alternative; that surface or alternative is the counterexample |
| cut admissibility | `discrimination_undecided` | indeterminate | no counterexample of `cut_inadmissible` is found, and the admissible evidence cannot decide the discrimination the cut itself claims at its stated altitude; the value names the evidence that would decide |
| direction acceptance | `direction_verified` | satisfied | the direction is built by an admissible extraction in its declared representation space, at least one acceptable verification is recorded with identity preserved under held-out treatment, and no recorded verification shows identity lost |
| direction acceptance | `extraction_inadmissible` | falsified | the direction is built by a principal-component or maximum-variance construction, which is not admissible as an identity direction, whatever its verification shows; that construction is the counterexample |
| direction acceptance | `verification_failed` | falsified | the extraction is admissible, and a recorded verification shows identity not preserved under held-out treatment; that verification is the counterexample |
| direction acceptance | `verification_inconclusive` | indeterminate | the extraction is admissible in a declared representation space, no recorded verification establishes an acceptable preservation or shows identity lost, and a recorded verification ran without establishing either; the value names the held-out treatment or verification that would decide |
| direction acceptance | `representation_space_invalid` | invalid_basis | no counterexample of `extraction_inadmissible` or `verification_failed` is found, and the overlay declares no representation space, or its direction is composed with directions computed in another space; that basis cannot support the evaluation (§10) |
| overlay publication | `published_verified` | satisfied | the published direction has a recorded acceptable verification |
| overlay publication | `published_unverified` | falsified | a direction with no acceptable verification is published, which violates §8 Representation law (§10 Verification by treatment); that publication is the counterexample |
| overlay storage | `storage_retained` | satisfied | the stored package retains the declared representation space and its version, the geometric object, the distributed evidence, the verification trace, the provenance and authority record, and the supersession record |
| overlay storage | `storage_lossy` | falsified | the stored layout loses one of those surfaces; the lost surface is the counterexample |
| null-peer discrimination | `null_peer_discriminated` | satisfied | the identity-loaded attributes in the candidate's core are unique to it among its null peers, and its identity direction transfers more cleanly than a random diagonal |
| null-peer discrimination | `not_yet_lawful` | falsified | the uniqueness test or the transfer test fails, so the cluster is not yet a lawful Markov object; the failing test is the counterexample |
| promotion gate | `gate_met` | satisfied | the run meets the test's predicate |
| promotion gate | `gate_not_met` | falsified | the run does not meet the test's predicate; it is the counterexample for that run only, and the construct's standing is unchanged |
| saturation | `saturated` | satisfied | the three conditions hold; the explicit gaps are carried as residuals |
| saturation | `not_saturated` | falsified | a condition fails, as where an attribute exists without traceable support (silent unsupported attribute creation) or a gap is a silent miss; that attribute or gap is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `representation_space_invalid` (P5).

A verification not run. Where no ground of `extraction_inadmissible` or
`representation_space_invalid` holds, a candidate direction whose
verification has not been run has no result for direction acceptance:
the verification is the evaluation of that predicate, and it was not
performed, so it has no
closed result and is never mapped to
`indeterminate` or to any other core value
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed). The
direction stays a candidate (§10 Verification by treatment). In every
conjunction over its acceptance, the unrun verification is a planned
assessment without a closed result
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Gaps) where the verification was planned; where none was planned, the
obligation it would have discharged is uncovered coverage. A step whose output needed that verification and that stopped
without it ends `incomplete`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps for the predicate "a candidate is available", never to
`indeterminate`; the step's work state carries the unrun verification as
a residual ([ACTIVATION §5](ACTIVATION.md#5-work-state-and-restart)).
Publishing the unverified direction is `published_unverified` (P5, P6).

Two readings keep the mapping total without coercion (P5, P1). A stated
absence or stated non-applicability on an admissibility surface is a
lawful surface value, not a non-satisfied result. Candidate-class and
established are standings of the construct, the first being FOUNDATIONS
§5's hypothesis standing, and candidate-class and formally closed are
publication kinds; none of them is a result, and a gate run that fails
does not falsify the construct.
```


### Row `WORLD_MODEL_METHOD.md#four-working-refinements-indicated-by-the-empirical-program` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#four-working-refinements-indicated-by-the-empirical-program` at rc.2:

```text
Four findings from the empirical program constrain how the method
treats Markov objects. They are working refinements: the program has
produced candidate evidence for them, not a formal closure. The
method adopts them as the best current reading of the construct.

They are stated here in the order and sense carried by the pinned
companion surface, each with the experiment that grounds it, so the two
can be checked against each other. Where the companion later re-cuts
them, the pin in *Companion Surfaces* fixes which reading this method
adopted.

1. **Effective blanket is geometric, not set-theoretic** (exp 17). A
   boundary stated as attribute-column membership leaks under bypass.
   The load-bearing structure is the identity axis, and a set-valued
   boundary over columns is an epistemic convenience rather than the
   object. Read the Representation Law this way: the test is whether
   identity survives treatment, not which attributes are in the
   member set.

2. **Attribute schemas sense and fragment; they do not isolate.** Any
   fixed attribute basis partially aligns with a given object's
   identity and partially distributes it. Where a Markov-object
   overlay is published, it must expose the identity axis, not only
   the attribute profile. Schemas are evidence, not ontology.

3. **Core identity, not core size, is the discriminator of
   objecthood** (exps 15, 16). A sparse invariant with semantically
   loaded content is a lawful object; a rich attribute cluster with
   nothing invariant under context variation is not. More columns do
   not buy more objecthood. This is why sparse first publication
   remains lawful under the Saturation Law.

4. **Identity is a DC shift, not a principal-variance axis** (exp 18).
   Object identity appears as a mean offset in representation space,
   not as the dominant-variance direction. Characterization by "the
   biggest source of variance in the attribute set" systematically
   misses identity; characterize by typical-offset-from-a-null-peer
   instead. This is the basis for excluding principal-component and
   maximum-variance constructions as identity directions.

These refinements do not weaken the Markov-object construct. They
sharpen it into a construct that can be operationally validated and
reproduced in published overlays.

They constrain the Markov-object construct and overlays built on it.
They are not admissibility conditions for entity cuts, which are
governed by *Entity Cut Construction Law*.
```

Successor, `WORLD_MODEL.md#four-working-refinements`:

```text
Four findings from the empirical program constrain how the profile treats
Markov objects. They are working refinements: the program has produced
candidate evidence for them, not a formal closure, and the profile adopts
them as the best current reading of the construct (P3, P6;
rc.2 #four-working-refinements-indicated-by-the-empirical-program). They
are stated in the order and sense the pinned companion surface carries
(§13 Companion surfaces), each with the experiment that grounds it, so the
two can be checked against each other; where the companion later re-cuts
them, the pin fixes which reading this profile adopted (P6, P3).

1. Effective blanket is geometric, not set-theoretic (exp 17). A boundary
   stated as attribute-column membership leaks under bypass. The
   load-bearing structure is the identity axis, and a set-valued boundary
   over columns is an epistemic convenience rather than the object. The
   Representation law (§8) is read this way: the test is whether identity
   survives treatment, not which attributes are in the member set.
2. Attribute schemas sense and fragment; they do not isolate. Any fixed
   attribute basis partially aligns with a given object's identity and
   partially distributes it. Where a Markov-object overlay is published,
   it exposes the identity axis, not only the attribute profile. Schemas
   are evidence, not ontology.
3. Core identity, not core size, is the discriminator of objecthood (exps
   15, 16). A sparse invariant with semantically loaded content is a
   lawful object; a rich attribute cluster with nothing invariant under
   context variation is not. More columns do not buy more objecthood.
   This is why sparse first publication remains lawful under the
   Saturation law (§11).
4. Identity is a DC shift, not a principal-variance axis (exp 18). Object
   identity appears as a mean offset in representation space, not as the
   dominant-variance direction. Characterisation by "the biggest source of
   variance in the attribute set" systematically misses identity;
   characterise by typical offset from a null peer instead. This is the
   basis for excluding principal-component and maximum-variance
   constructions as identity directions (§10).

These refinements do not weaken the construct; they sharpen it into one
that can be operationally validated and reproduced in published overlays.
They constrain the construct and overlays built on it. They are not
admissibility conditions for entity cuts, which §9 governs (P3, P6).
```


### Row `WORLD_MODEL_METHOD.md#mappings-are-semantic-treatments` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#mappings-are-semantic-treatments` at rc.2:

```text
Cross-domain transformation is not plain structural rewrite.

Every treatment must declare preserved structure, changed meaning, loss,
surplus, and ambiguity.
```

Successor, `WORLD_MODEL.md#5-core-claims`:

```text
Source systems remain sovereign. Operational truth remains with the
systems that enact it. The world model is a derived semantic layer over
those systems, not a replacement operational source (P6;
rc.2 #source-systems-remain-sovereign).

Domains are functional surfaces. A domain is defined by coherent
function: what enters, what changes, what is owned, what is guaranteed,
what leaves, and what adjacent domains can rely on (P3;
rc.2 #domains-are-functional-surfaces).

Data is evidence, not meaning by itself. Data is a trace of constrained
function execution; it is invalid in isolation from context (P1, P6;
rc.2 #data-is-evidence-not-meaning-by-itself).

World models externalise expert cognition. The world model is the
inspectable form of the domain understanding that experts already carry
implicitly (P6; rc.2 #world-models-externalize-expert-cognition).

Mappings are semantic treatments. Cross-domain transformation is not
plain structural rewrite. Every treatment declares preserved structure,
changed meaning, loss, surplus and ambiguity (P1, P4b;
rc.2 #mappings-are-semantic-treatments). A treatment is a refinement or
rewrite step of
[ACTIVATION §4 Refinement](ACTIVATION.md#refinement): what it preserves
and its licensing law are that section's, and a treatment that changes
meaning is an approximate step with its adequacy relation. The five
declared fields are this profile's domain fields for that statement;
preserved structure is what the step preserves, and changed meaning,
loss, surplus and ambiguity state where and how it is not exact.

Fully qualified naming is mandatory. Many cross-domain failures are
preventable naming collisions. Fully qualified naming removes aliasing,
so the remaining hard work is real semantic transformation; IDENTITY §2
states the scoped identity it applies (P3, P1;
rc.2 #fully-qualified-naming-is-mandatory).

Value lists are domain artifacts too. Changing code sets,
classifications and value lists are governed temporal reference
artifacts, not static enum decorations (P3;
rc.2 #value-lists-are-domain-artifacts-too).

The world model sits above APIs and schemas. API contracts and schema
contracts are projections over the world model. They are useful because
they publish structure and function; they are not the highest semantic
authority (P6, P1; rc.2 #the-world-model-sits-above-apis-and-schemas).

Probability belongs in the epistemic overlay. The canonical published
entity cut should remain semantic and bounded. Probability belongs in
uncertainty, ranking, anomaly and alignment overlays, not in the
ontological identity of the published object itself (P3, P6;
rc.2 #probability-belongs-in-the-epistemic-overlay). That overlay may
include correspondence candidates; confidence and ranking; ambiguity
registers; anomaly and surprise signals; and candidate mappings or
treatment suggestions. The overlay is useful because it lets
probabilistic reasoning operate over a governed semantic substrate rather
than over detached strings, schemas or raw tables. But the overlay is not
the same thing as published semantic truth: accepted semantic treatments,
published domain artifacts and compiled deterministic execution artifacts
remain distinct from probabilistic overlays (P6, P0).
```


### Row `WORLD_MODEL_METHOD.md#markov-object-construction-law` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#markov-object-construction-law` at rc.2:

```text
This law is the representation-substrate specialization of *Entity Cut
Construction Law*. It applies only where the builder operates over a declared
representation space in which identity is a geometric direction — a learned
representation, an embedding over ledger claims, or an equivalent metric
space. It is not required for ordinary institutional recovery.

Where it applies, a builder project constructs the Markov-object overlay by a
directional, interventional procedure. The framework below is both how the
overlay is *built* and the minimum structure that must be *stored* when it is
published.

The declared representation space is part of the overlay. An identity
direction is uninterpretable without the space it lives in, and directions
computed in different spaces do not compose.
```

Successor, `WORLD_MODEL.md#10-markov-object-overlay-construction`:

```text
This law is the representation-substrate specialisation of §9. It
applies only where the builder operates over a declared representation
space in which identity is a geometric direction (a learned
representation, an embedding over ledger claims, or an equivalent metric
space); it is not required for ordinary institutional recovery (P3, P2;
rc.2 #markov-object-construction-law). Where it applies, a builder
project constructs the overlay by a directional, interventional
procedure. The steps below are both how the overlay is built and the
minimum structure that is stored when it is published. The declared
representation space is part of the overlay: an identity direction is
uninterpretable without the space it lives in, and directions computed in
different spaces do not compose (P3, P1).
```


### Row `WORLD_MODEL_METHOD.md#representation-law` (modal; disposition `conserved`)

Predecessor, `WORLD_MODEL_METHOD.md#representation-law` at rc.2:

```text
Every published entity cut must be prompt-sufficient for reasoning.

At minimum, the cut should make visible:

- identity
- boundary
- authority
- state
- evidence
- treatment
- covariance
- ambiguity

"Make the effective blanket explicit" means: state the boundary at which the
entity's identity survives reinterpretation, not enumerate a set of member
attribute columns. Attribute schemas are evidence for identity, not identity
itself.

The boundary is interventional, not structural. The test is "does this
identity survive treatment across its adjacent domains?", never "which
attributes are in the member set?"

Where a declared representation space exists, that boundary takes its
geometric form: the low-rank projection along which identity is preserved
under treatment. A Markov-object overlay should then expose both the
distributed attribute evidence and the projection that recovers identity from
it. Outside such a space the same law is discharged semantically, under
*Entity Cut Construction Law*.

---
```

Successor, `WORLD_MODEL.md#representation-law`:

```text
Every published entity cut is prompt-sufficient for reasoning (P3, P1;
rc.2 #representation-law). At minimum, the cut should make visible
identity, boundary, authority, state, evidence, treatment, covariance and
ambiguity. "Make the effective blanket explicit" means: state the
boundary at which the entity's identity survives reinterpretation, not
enumerate a set of member attribute columns. Attribute schemas are
evidence for identity, not identity itself. The boundary is
interventional, not structural: the test is "does this identity survive
treatment across its adjacent domains?", never "which attributes are in
the member set?" (P3). Where a declared representation space exists, that
boundary takes its geometric form, the low-rank projection along which
identity is preserved under treatment, and a Markov-object overlay should
then expose both the distributed attribute evidence and the projection
that recovers identity from it. Outside such a space the same law is
discharged semantically under §9 (P3, P1).
```
