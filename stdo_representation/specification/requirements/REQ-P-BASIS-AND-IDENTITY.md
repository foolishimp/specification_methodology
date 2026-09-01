# REQ-P-BASIS-AND-IDENTITY — Thin Product Coordinates

Family: `REQ-P-BASIS-*`
Status: Active
Category: Constraint / Guarantee

Derives from: `../PRODUCT.md#exact-dependency-bases` and
`../PRODUCT.md#identity-and-provenance`

## Purpose

Bind the STDO compression, logical constraint index, native skill, and joined requests to exact Source
STDO and Axiom Indexer coordinates without turning physical paths, counts, or
runtime observations into semantic identity.

## Selected bases

```text
Source STDO release:
  stdo://releases/v2.5.0-rc.4/
Source STDO qualified ref:
  refs/tags/specification_methodology/v2.5.0-rc.4
Source STDO annotated tag object:
  032dac0c833111547f7dd4b290c5316ed9b70f97
Source STDO peeled commit:
  7a25668a8fecfd26f895759af3bec4708727964a
Source STDO installed manifest SHA-256:
  4fa2556d0127bebce8f7184cc4a3cb708a175b2e40552c55cb211f2426d5049e
Source STDO member-set SHA-256:
  504db879867f60e46ed4dea60509d12056d10cdd8c3460dc94abf7bc56542656
Axiomatic Calculus SHA-256:
  cbe2edb928d3e75e23446f6d525baea664966e8d5920e6fa389cbaa4af8f1f8d

Axiom Indexer exact version:
  v2.5.0-rc.4
Axiom Indexer qualified ref:
  refs/tags/axiom_indexer/v2.5.0-rc.4
Axiom Indexer annotated tag object:
  4750e09639c118f1097d4ea046fe23d26713f96b
Axiom Indexer peeled commit:
  a953ad4634fbfaefb8bdffaccdf4eff651a1e3a2
Axiom Indexer repository tree:
  093302db57bfb2e7beeed7f02dfc6d7090921a15
Axiom Indexer Project Subtree tree:
  3f71c3c2df99008b9521e338a7837c553f87173a
Axiom Indexer Product member inventory SHA-256:
  7df380d5c41be4482f06668c5fe1043cd08643daa9f40d83be3c0ff40a8ff7e6
Axiom Indexer executable SHA-256:
  dfb4d7f1e6b06b9c215154a00b689ce82d7cd36e1ec80ee8f93da9c20798b672
Axiom Indexer program schema SHA-256:
  61c9d26fabb1d844f643712632f6a6551a1c6f7f8ddfef604673e57b7c6b3b7b
Axiom Indexer output contract SHA-256:
  fd0996009b890e464399863e1f16bb9b9ca7820cb5aa04e95244618849983694
```

The Axiom coordinates above identify the published immutable dependency from
the atomic coordinated cohort. Historical accepted Axiom Indexer
`v0.1.0-rc.1` remains predecessor evidence and shall not substitute for the
same-version dependency. Mutable sibling bytes remain prepublication
construction evidence only.

## Identity law

- Program and logical-map identities use the exact released Axiom Indexer
  canonicalization and digest law.
- Representation exact version, including prerelease ordinal, equals the exact
  represented STDO version; equal version text does not equate their Products,
  cuts, member identities, review, or acceptance.
- Skill identity binds its exact regular-file inventory and symlink target
  strings.
- Joined-request identity is SHA-256 over exact UTF-8 output bytes.
- Logical source, calculus, frame, symbol, clause, residual, operator, and role
  identities are absolute URIs.
- Physical paths occur only in invocation-local Binding Sets or evidence.
- Line numbers, array positions, filenames, path counts, token counts, and
  lexical similarity do not create semantic identity.

## Requirements

**REQ-P-BASIS-001**: Every released program and map shall bind exact Source STDO
and Axiom Indexer coordinates above. A branch, mutable selector, compatible
local checkout, or unverified cache shall not substitute.

**REQ-P-BASIS-002**: The selected Product artifact paths shall be:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.4/
  axiomatic-program.json
  logical-constraint-map.json
```

Their content digests shall be recorded only after exact bytes exist and shall
not be inferred from the path.

**REQ-P-BASIS-003**: Every program item shall have an absolute identity and at
least one logical Source STDO route. Residuals shall have explicit re-entry
routes. A physical binding shall not enter the program as meaning.

**REQ-P-BASIS-004**: An invocation Binding Set shall resolve every required
logical prefix unambiguously and remain external to the portable Product member
set. Missing, escaped, ambiguous, or mismatched bindings shall refuse.

**REQ-P-BASIS-005**: The logical constraint index shall bind the unchanged
valid compression URI and canonical digest, resolved-source evidence, and
intrinsic map digest emitted by the exact Axiom Indexer dependency. An index
from different compression or dependency bytes is a different subject.

**REQ-P-BASIS-006**: The canonical skill shall be exposed through exactly these
relative symlink targets:

```text
.agents/skills/stdo-representation -> ../../skills/stdo-representation
.claude/skills/stdo-representation -> ../../skills/stdo-representation
```

**REQ-P-BASIS-007**: A joined request shall bind the exact ordered input array
and output bytes. Reordering, relabelling, or changing one string creates a new
request identity.

**REQ-P-BASIS-008**: Dogfood observations may bind model, configuration, time,
inputs, outputs, usage, and evidence boundary. They remain observations and do
not enter program, map, skill, or joined-request identity.

**REQ-P-BASIS-009**: Release qualification shall bind the frozen eight-member
Product inventory, dependency bases, claim bytes, evidence, annotated immutable
RC tag object, peeled commit, and tree. Publication or validation alone shall
not imply Product acceptance.

**REQ-P-BASIS-010**: A release-matched STDO Representation cut shall carry the
exact represented STDO version, including prerelease ordinal. Its locally
qualified RC ordinal shall equal the represented STDO RC ordinal while its
Product identity, member inventory, review, acceptance, and Git object
identities remain independent of Source STDO and Axiom Indexer.

**REQ-P-BASIS-011**: The Product-owned Shared-Source Release Profile shall
specialize only alternate Git spelling permitted by the installed Release
Method. Its source-subtree root and tree are additional reacquisition evidence,
not Product identity or authority imported from mutable method source.

**REQ-P-BASIS-012**: Every release-matched source refresh shall carry one
machine-readable `source-corpus.json` that binds the exact matched version,
immutable Source STDO cut, installed-manifest digest, standards member-set
digest, and every standards member path and digest. It is reproducibility
evidence rather than a Product member. A changed Source STDO member shall be
semantically re-evaluated by an LLM before the compression is accepted;
byte-identical members and unaffected compression entries shall be conserved.

**REQ-P-BASIS-013**: A release-matched Representation cut shall bind the same
exact version of its Axiom Indexer Development Product. A mutable sibling
candidate may supply construction evidence before a coordinated cohort is
published, but it is not the immutable dependency and cannot satisfy release
qualification or released use. The published relation requires the exact
qualified Axiom Indexer cut, tag object, peeled commit, repository and Project
Subtree trees, member inventory, executable digest, and imported contract
identities.

**REQ-P-BASIS-014**: The release-matched cohort shall close over exact Source
STDO and its plugin, same-version Axiom Indexer mechanics, the eight-member
Representation Product, the released program and map, and all 52 Source STDO
member paths and digests. A missing, stale, differently versioned, or
source-digest-incongruent member shall block the cohort.

**REQ-P-BASIS-015**: Coordinated construction shall freeze Source STDO and its
plugin in commit A, create and verify its annotated local tag and Install,
derive and freeze the child Products and source closure in commit B, and then
publish the complete qualified Product ref set in one atomic transaction.
Pre-push qualification shall bind every local tag object, peel, target, push
ref, and fetched expected remote object ID or required absence. Immutable tags
are create-only; mutable refs require explicit per-ref compare-and-swap leases;
unsupported atomic transport, remote drift, lease mismatch, or a partial set
shall refuse without sequential or force fallback.
