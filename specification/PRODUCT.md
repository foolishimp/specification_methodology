# Axiom Indexer Product

Status: active source definition; no released Axiom Indexer Product or accepted
target index artifact exists.

## Product Terms

Within `urn:axiom-indexer:bounded-context:product`:

- **Axiom Indexer Source Project** is this mutable workspace while it defines
  and builds candidate Products.
- **Target Corpus** is one exact, finite, authority-bound document population.
- **Corpus Basis** identifies the target corpus, ordered members, exact member
  bytes, governing authorities, and acquisition boundary.
- **Axiomatic Calculus Basis** identifies the exact external calculus under
  which a corpus may be interpreted as an axiomatic program.
- **Target Profile** declares corpus-specific population, semantic-address,
  source-reentry, required-closure, and refusal rules without changing the
  common algebra.
- **Semantic Compilation** is a bounded probabilistic traversal that proposes
  a typed axiomatic interpretation of one exact corpus. It grants no semantic
  or acceptance authority.
- **Semantic Compilation Candidate** is the immutable proposed program,
  source-selection rows, and explicit residual uncertainty returned by semantic
  compilation.
- **Axiomatic Program** is the exact candidate content accepted by an
  authorized semantic-selection judgment under one corpus, calculus, and target
  profile basis.
- **Axiom Indexer** is the reusable Product capability that compiles candidate
  programs, exposes them to structural inspection and externally authorized
  semantic selection, encodes accepted programs, exposes encoded artifacts to
  carrier admission, projects accepted programs, and exposes each encoded
  projection to carrier admission while preserving those authority boundaries.
- **Axiom Index** is one immutable, carrier-native, content-addressed artifact
  encoding an Axiomatic Program whose exact program and ledger identities are
  bound by an accepting Semantic Selection Judgment. A target Product may
  separately accept and release that artifact under its own authority.
- **Carrier Tenant** is one independent HOW realization that encodes the common
  algebra in a selected carrier.
- **Carrier Profile** is a versioned, exact mapping from the common algebra into
  one carrier basis.
- **Structural Inspection** evaluates declared form, basis, identity, and
  closure properties without selecting semantic content.
- **Semantic Selection Judgment** is an external exact-subject decision that
  accepts, reworks, or rejects candidate semantic content under declared
  authority and evidence. It binds the unchanged compilation candidate and
  structural judgment to the exact resulting program and selection-ledger
  identities when accepted.
- **Carrier Admission Judgment** decides whether unchanged carrier bytes
  satisfy their exact profile and carrier law.
- **Projection Assignment** binds one exact accepted relation `(P_X, S_X,
  J_X)`, selected carrier basis and profile, purpose, seed set, frames, actor
  capability, required evidence, and context budget.
- **Context Projection** is the exact least declared closure of an assignment's
  seeds under the common projection law.
- **Context Packet** is an invocation-input bundle containing an assignment,
  carrier-native projection, manifest, required evidence, stop states,
  residuals, and source-reentry routes. It is not a new Product or authority.

## Product statement

Axiom Indexer converts an exact governed corpus into a reviewable candidate
axiomatic program, preserves the distinction between proposal and acceptance,
and produces one or more carrier-native Axiom Index artifacts from the accepted
program. The accepted program is reusable across downstream assignments and
can be projected into bounded contexts before each projection is independently
encoded and structurally admitted.

The Product is target-neutral and carrier-neutral at its common boundary. A
target profile binds what corpus is being interpreted. A carrier tenant binds
how accepted meaning is encoded. Neither extension axis may redefine the other
or the common Product.

## Core relation

```text
X_B = (B, M_B, D_B)
B   = exact Corpus Basis
M_B = duplicate-free ordered member inventory
D_B = exact member bytes addressed by M_B
A   = exact Axiomatic Calculus Basis
T   = exact Target Profile
H_X = exact semantic-selection activation binding actor, authority, grant and evidence boundary

Compile(X_B, A, T, I_C, R_C, K_C)
  -> Q_X* = (P_X*, S_X*, U_X*) | hold | gap | refusal

Inspect(Q_X*, A, T)
  -> D_Q = eligible | refuse

Select(Q_X*, X_B, D_Q = eligible, H_X)
  -> J_X = accepted(P_X, S_X) | rework | rejected

Encode_C(P_X, S_X, J_X, Profile_C, Basis_C)
  -> G_X,C

Admit_C(G_X,C, Profile_C, Basis_C)
  -> D_G = admitted | refuse
```

`P_X*` is the candidate axiomatic program, `S_X*` the proposed source-selection
rows, and `U_X*` explicit residual uncertainty. `D_Q` is deterministic
structural evidence and grants no semantic-selection authority. `J_X` is the
external semantic-selection judgment. An accepting `J_X` binds the unchanged
`Q_X*` and `D_Q` to exact accepted program content `P_X` and its exact selection
ledger `S_X`. `G_X,C` is an immutable carrier produced only from that accepted
relation and before admission. `D_G` is a separate deterministic judgment over
its unchanged identity and bytes; it cannot stand in for `J_X`.

`D_Q = eligible` is a necessary but insufficient precondition for an accepting
`J_X`. `D_Q = refuse` prohibits acceptance and returns the candidate to rework
or rejection without constructing `Accepted_X`.

The accepted semantic subject is the relation:

```text
Accepted_X = (P_X, S_X, J_X)
```

`J_X` points to the identities of `P_X` and `S_X` but remains outside both
identity preimages. Rework or rejection produces no `Accepted_X`.

Selection conserves the complete typed candidate population:

```text
Pop(Q_X*) = ids(P_X*) + ids(S_X*) + ids(U_X*)
domain(disposition(S_X)) = Pop(Q_X*)

accepted(J_X) only if:
  every candidate identity has exactly one lawful disposition;
  every retained or uncertain identity maps to an accepted model or residual;
  every reworked identity maps to exact source-preserving replacement lineage;
  every omitted or rejected identity retains its source route and rationale;
  every accepted model identity has candidate or rework lineage.
```

This is typed lineage conservation, not cardinality equality. A selected Target
Profile may permit declared splits or merges, but missing, duplicate,
conflicting, unresolved, or profile-forbidden dispositions prohibit an
accepting `J_X`.

The accepted carrier-neutral Axiomatic Program has the minimum common envelope:

```text
P_X = (B, A, T, M_X, R_X)

B   = exact Corpus Basis
A   = exact Axiomatic Calculus Basis
T   = exact Target Profile
M_X = accepted finite model conforming to A and T
R_X = duplicate-free bindings from M_X identities to exact source routes
```

The selected calculus—not Axiom Indexer—owns the record families, coordinates,
relations, constraints, latitude, residuals, judgments, and compatible-extension
law inside `M_X`. Axiom Indexer requires those laws to close and binds every
accepted model identity to exact source evidence through `R_X`. Unknown kinds,
unresolved references, cross-context collisions, missing required coordinates,
or unresolved source bindings refuse.

## Identity

The Product uses content-first identities. At minimum, distinct immutable
identities bind:

1. the exact Corpus Basis and member inventory;
2. the exact Axiomatic Calculus Basis;
3. the exact Target Profile;
4. the complete Semantic Compilation Candidate;
5. the structural inspection judgment;
6. the accepted Axiomatic Program content;
7. the accepted source-selection ledger;
8. the semantic-selection judgment;
9. the exact Carrier Basis and Carrier Profile;
10. the canonical Axiom Index bytes; and
11. each Projection Assignment, semantic closure, projection envelope, and
    manifest.

Acceptance, admission, release, invocation, and observation records point to
those immutable subjects. They do not enter or retroactively change subject
identity. A carrier cannot embed its final content identity in the bytes from
which that identity is derived.

## Projection relation

For accepted relation `(P_X, S_X, J_X)` and assignment `A_P`:

```text
Z(A_P) = mandatory frame refs + target refs + explicit seed refs
P_A    = least_closure(P_X, Z(A_P), L_projection)
S_A    = exact applicable rows projected from unchanged S_X
R_A    = exact judgment, evidence and source-reacquisition relations
V_A    = (P_A, S_A, ref(J_X), R_A)

EncodeProjection_C(V_A, A_P.carrier_profile, A_P.carrier_basis)
  -> G_A,C

Admit_C(G_A,C, A_P.carrier_profile, A_P.carrier_basis)
  -> D_A = admitted | refuse

Contextualize(P_X, S_X, J_X, A_P)
  -> ContextPacket(V_A, G_A,C, D_A)
   | capability_mismatch | budget_exceeded | invalid_basis | refuse
```

`L_projection` computes the semantic closure `P_A`. The projection envelope
`V_A` preserves every applicable identity, authority, basis, dependency,
constraint, latitude, residual, evidence, exclusion, refusal, invalidation,
selection-ledger, semantic-selection-judgment, and source-reentry relation
required by the assignment. `S_A` is an immutable view of exact rows from
`S_X`; it cannot rewrite the parent ledger. `R_A` carries exact evidence where
selected and immutable reacquisition routes otherwise. A budget may cause a
hold; it cannot trim mandatory closure. A projection is bounded by its exact
assignment and grants no authority outside it. `P_A` is the semantic closure;
`V_A` has its own immutable identity binding that closure and its external
acceptance relations. `EncodeProjection_C` verifies the exact envelope and
encodes only its unchanged `P_A`; it cannot accept an unbound substitute
closure. `G_A,C` is that closure's carrier-native encoding, and `D_A` judges the
unchanged encoded bytes. A Context Packet is issued only when `J_X` accepts the
exact parent program and ledger, `V_A` closes, and `D_A = admitted`.

## Authority

- Corpus owners own source meaning and the authority to define the corpus.
- The selected calculus owns its algebraic kinds and laws.
- A target profile owns only target-specific population and interpretation
  boundaries.
- A semantic compiler may propose content and expose uncertainty; it cannot
  accept its proposal.
- Semantic-selection authority accepts, reworks, or rejects one exact
  candidate under an explicit grant and evidence boundary.
- A carrier tenant owns only encoding, canonicalization, and structural
  carrier law.
- Carrier admission judges unchanged carrier bytes and cannot select semantics.
- A consuming Product owns invocation, workspace, runtime, effects, events,
  evaluation, continuation, decisions, and closure.

No generated record, carrier, projection, token reduction, model response, or
structural success mints source, semantic, operation, decision, acceptance,
release, or runtime authority.

### Source-project Product authority

```text
actor_identity = "https://github.com/foolishimp"
authority_identity = "urn:axiom-indexer:authority:product-owner"
grant_identity = "urn:axiom-indexer:grant:product-owner:1"
grant_scope = "Establish and accept source-project Goals, Intent, Product, requirements, project frame basis and routing; excludes selecting a calculus, target profile, carrier tenant, implementation, target artifact, release or downstream migration."
```

Every decision under this grant still binds its exact subject and basis. The
grant creates no semantic-selection, carrier-admission, runtime, independent
review, or target-Product authority.

## Product contents

An Axiom Indexer Product contains the target-neutral capabilities and public
contracts required to:

- acquire and verify exact corpus, calculus and target-profile bases;
- produce immutable Semantic Compilation Candidates;
- expose candidates to structural inspection and external semantic selection;
- verify the accepted `(P_X, S_X, J_X)` relation, receive selected carrier
  profiles, and construct canonical index artifacts;
- expose unchanged artifacts to Carrier Admission; and
- derive, encode and admit assignment-bound context projections.

It also contains the identity, refusal, source-reentry and extension boundaries
that keep target profiles and carrier tenants independent. It does not contain
or silently select a particular target profile, carrier tenant, target artifact
or consuming runtime.

## Output artifact boundary

An Axiom Index artifact contains only:

- canonical carrier-native axiomatic-program records;
- minimal exact basis and identity coordinates needed to interpret them; and
- embedded source addresses or exact source-reacquisition routes.

Qualification and release materials may accompany the artifact: source
inventory, compilation candidate, structural receipt, semantic-selection
judgment and ledger, carrier receipt, measurements, and bounded usefulness
observations. They do not enter every invocation payload unless explicitly
selected. The exact accepting judgment remains a required external relation for
encoding and projection even when its full evidence payload is reacquired by
identity. A target Product decides whether to accept and release an exact
artifact.

The Product does not contain a source workspace, target workspace, prompt,
model configuration, response, execution plan, runtime engine, event stream,
continuation state, or downstream decision.

## Extension boundary

Target profiles and carrier tenants are independently selected:

```text
                    target profile T1
                   /
common Product ---- target profile T2
                   \
                    target profile Tn

                    carrier tenant C1
                   /
accepted P_X ------ carrier tenant C2
                   \
                    carrier tenant Cn
```

A target profile may not select a carrier. A carrier profile may not influence
semantic compilation or request omission of accepted meaning. A carrier unable
to represent accepted `P_X` returns a profile gap or refusal.

## Current boundary

This source project has no selected Axiomatic Calculus Product, Target Profile,
Carrier Tenant, Semantic Compilation Candidate, accepted Axiomatic Program,
Axiom Index candidate, released Axiom Indexer Product, target-accepted artifact,
or release. The constitutional extraction authorizes no implementation or
downstream migration.
