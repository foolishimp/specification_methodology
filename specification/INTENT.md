# Axiom Indexer Intent

## Intent

Transform an exact, finite, authority-bound document corpus into a compact,
source-addressed axiomatic semantic index that software and probabilistic
reasoners can traverse without reconstructing governing relations from textual
similarity.

Semantic compilation proposes a typed axiomatic program under one exact
calculus and target profile. Structural inspection checks the proposal's
declared form. Authorized semantic selection decides what is accepted,
reworked, rejected, or retained as uncertainty. Only the accepted program may
be encoded by a carrier tenant and admitted as an Axiom Index.

The source corpus remains semantic authority. The index makes accepted
identities, relations, constraints, latitude, residuals, and source re-entry
routes machine-addressable; it does not prove that the corpus is true,
complete, consistent, decidable, or uniquely interpretable.

## Desired outcomes

- One reusable indexing capability for any exact corpus satisfying a selected
  target profile.
- A carrier-neutral axiomatic-program algebra independent of every named
  document family and encoding technology.
- Complete separation between target semantics and carrier mechanics.
- Content-first identities for corpus basis, compilation candidate, accepted
  program, encoded index, and projection.
- Explicit uncertainty, omission, refusal, and source re-entry rather than
  silent semantic completion.
- Exact least-closure projections for bounded reasoning contexts.
- Independent target profiles and carrier tenants that cannot redefine the
  common Product.

## Product relation

```text
X_B = exact corpus basis, member population and bytes
A   = exact axiomatic-calculus basis
T   = exact target profile

Compile(X_B, A, T, intent, frames, capability)
  -> Q_X* | hold | gap | refusal

Inspect(Q_X*, A, T)
  -> D_Q = eligible | refuse

Select(Q_X*, X_B, D_Q = eligible, semantic_selection_activation)
  -> J_X = accepted(P_X, S_X) | rework | rejected

Encode(P_X, S_X, J_X, carrier_profile)
  -> G_X,C

Admit(G_X,C, carrier_profile)
  -> admitted | refuse

Project(P_X, S_X, J_X, assignment)
  -> V_A = (P_A, S_A, J_X_ref, R_A) | hold

EncodeProjection(V_A, assignment.carrier_profile)
  -> G_A,C

Admit(G_A,C, assignment.carrier_profile)
  -> admitted | refuse

Packet(assignment, V_A, G_A,C, admission)
  -> ContextPacket | hold
```

`Q_X*` is a proposal and `D_Q` is deterministic structural evidence about that
proposal. `J_X` is the separately authorized semantic-selection judgment that
binds the unchanged candidate and structural judgment to the exact accepted
program `P_X` and selection ledger `S_X`. `J_X` remains outside the identity
preimages of `P_X` and `S_X`; neither structural eligibility nor carrier
admission can substitute for it. A refused `D_Q` prohibits an accepting `J_X`.
`G_X,C` is one carrier-native Axiom Index.
Admission judges the unchanged carrier; it does not construct or semantically
select it. `V_A` is the projection envelope: exact semantic closure `P_A`, the
applicable unchanged selection-ledger rows `S_A`, exact `J_X` identity and
reacquisition relation, and source/evidence re-entry routes `R_A`. Only `P_A`
is carrier-encoded, but encoding is gated by `V_A` and the manifest and packet
preserve its external acceptance relations. `G_A,C` is the separately admitted
carrier encoding. A Context Packet is an invocation input, not a new Product or
authority surface.

## Constitutional boundary

This Product owns the target-neutral compilation contract, common index
algebra, identity law, selection boundary, carrier boundary, and projection
law. A target profile owns corpus-specific population and semantic-address
rules. A carrier tenant owns only its direct encoding and structural
admission rules. A consuming Product owns its workspace, prompt, model,
execution, events, continuation, evaluation, and decisions.

## Non-goals

- Turning arbitrary text into accepted axioms without exact selection.
- Establishing source truth, completeness, consistency, soundness, or one
  uniquely correct interpretation.
- Defining a target ontology or carrier language in the common Product.
- Embedding a mutable workspace, execution engine, workflow, event log,
  continuation mechanism, prompt, model invocation, or response.
- Granting semantic, operation, decision, acceptance, release, or closure
  authority through visibility in an index or projection.
- Using embeddings, similarity, or retrieval rank as identity, dependency,
  authority, or closure truth.
