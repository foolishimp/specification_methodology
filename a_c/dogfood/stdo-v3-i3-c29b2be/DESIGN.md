# Frozen Codex V3 I3 transport design

Status: proposed representation of an existing authored interpretation. This
consumer binding does not independently interpret, accept or release v3 and
does not add a Product dependency. This design precedes its implementation.

## Input and exact basis

Use only the self-contained `input/candidate.tar.gz` and `input/manifest.json`.
Check the fixed commit/package/tree coordinates, archive bytes and SHA-256,
unique regular archive members, every member's bytes and SHA-256, the 80-member
documentary inventory, all interpretation pins, and every one of the 701 source
owner body and local block pins. Read archive members in memory; never extract
or execute candidate code. No live v3 checkout, installed candidate, or Axiom
Indexer library participates in this binding.

The exact published STDO 2.5.1-rc.2 calculus remains the generic tenant's basis.
The subject is this candidate's existing `interpretation/program.json`, with
its raw-file identity distinct from canonical JSON/model/carrier identities.
The full source account and all 37 contracts remain in frozen input custody.

## Mapping

Carry all 705 native clauses as `objects`, preserving original URI, ordinal and
complete original payload. Native kind/operator/literal roles remain inert
authored content; a native `constraint` label does not invent a core constraint
instance, an `applies_to` subject, a judgment or an authority grant.

For each exact adjacent reference-location/ref argument pair retain ordinal,
pointer, role and typed governing target. Do not reconstruct a new dependency
relation from prose. The 7,741 such pairs define the transported required
relation. Pointer strings may refer to a preceding inlined contract and later
return to the semantic record, so preserve the original sequence rather than
pretending every pointer addresses the main record.

Retain all 2,076 route literals with exact payload and ordinal. Their typed
target references are non-governing: 2,046 provenance routes remain navigable;
30 conditional routes retain `required_when` and target-index coordinates.
Unknown applicability withholds dependent action. Selecting a current index
alone does not assert applicability or unconditionally select a conditional
target index.

Carry all 725 native selectors as objects with original payload, ordinal and
governing root references. Carry only the two actual native residuals as core
`residuals`, keeping exact native details/routes and their authored clause
subjects. Leave relations, constraints, latitude, traversals, transformations
and judgments explicitly empty and signature-permitted. Nested reference
occurrences preserve ordering and multiplicity without synthesizing thousands
of semantic relation instances.

An envelope object preserves the remaining original program fields. Recovering
the source program reassembles original clause/selector/residual arrays in
their declared order and compares the complete JSON object to frozen input.
The original raw program file remains available separately in the archive.

## Operations and checking

The typed stdlib consumer CLI builds and checks the model through the existing
Graphify tenant codec. It does not duplicate the generic validator, carrier or
projection algorithm. Deterministic gzip JSON keeps exact checked-in artifacts
manageable. An explicit output option emits normal uncompressed node-link JSON
for native Graphify use outside source authority.

`select` accepts a native selector URI, returns the generic complete governing
projection and explains conditional/provenance boundaries. `find` and `inspect`
operate on the recovered exact representation. A record budget refuses when
the complete required closure exceeds it. No generated semantic acceptance
judgment or full-calculus admission is supplied.

For every selector, compare projected clause identities to an independently
computed closure over only the original program's direct native references.
Compare selector residual roots and subject-attached residuals, preserve source
program round trip, and test tampering at custody, owner/block-pin, payload,
route and graph boundaries. Exercise both Release residuals, provenance-only
exclusion, conditional non-promotion, repeated ordered references and budget
refusal. Native Graphify build/export/reload/query qualification uses exact
upstream code separately. Raw sizes and timings are observations; accepted-
result efficiency and v3 semantic acceptance remain open.
