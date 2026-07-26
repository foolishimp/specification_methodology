# Independent Exact-Cut Review: STDO `v2.2.1-rc.1`

- reviewed_at: 2026-07-26T15:07:37Z
- reviewer: codex, fresh independent review context
- review_mode: read_only_exact_tag
- tag: `v2.2.1-rc.1`
- tag_object: `f272efc9a3a23304e51d653a67af22b8f9f6eb9e`
- peeled_commit: `b9033adb5047a959121d19879ee02cff54054a83`
- tree: `e1aa816e4fd6827fff6f88d31aace2dbbcb330ad`
- predecessor_tag: `v2.2.0`
- predecessor_commit:
  `5326562f075d60052806d0d2c79d3db49671a8ea`
- standards_aggregate:
  `485d22a73d85b43131287e7d76d0c7baf33e09094ea950ee1b9f276d7a372da2`
- verdict: REQUEST_CHANGES

## Scope

The review reconstructed the immutable tagged subject from Git objects. It did
not substitute moving `main`, earlier candidate reviews, untracked files, or
conversation summaries.

Reviewed authority and projection surfaces:

- `specification/PRODUCT.md`;
- `specification/GOALS.md`;
- T-003;
- `releases/v2.2.1.md`;
- `SPEC_METHOD.md`;
- `DESIGN_MODULE_METHOD.md`;
- `TICKET_METHOD.md`;
- `RELEASE_METHOD.md`;
- affected authority compressions; and
- agent templates.

The review tested exact identity, predecessor conservation, proportional
sequencing, decision completeness, Prime semantic atoms, derived projection
fidelity, review durability, and publication ordering.

## Findings

### P1: Non-Adopters Receive An Unintended Prior-Design Gate

`SPEC_METHOD.md` permits co-evolution when `DESIGN_MODULE_METHOD.md` applies and
the network has no unresolved relation, then uses an unqualified `Otherwise`
to require prior design acceptance.

That fallback also reaches boundaries where `DESIGN_MODULE_METHOD.md` does not
apply. It conflicts with optional adoption and the explicit exclusion of a
blanket design-first sequence.

The fallback must be scoped to adopted boundaries with an unresolved or
unsatisfied decision network.

### P1: Co-Evolution Admissibility Is Weaker Than Decision Completeness

The exact predicate is:

```text
U(B) = unresolved(M(B))
co_evolution_admissible(B) iff U(B) = empty
```

It omits the joint-satisfiability condition required by the surrounding
decision-complete law. A completely assigned but contradictory network can
therefore satisfy the written admissibility equation.

The declared complete `M(B)` also omits `entities`, `invariants`, and
`higher-order composition`, although the same standard makes them governed
Ontology elements. Unresolved relations in those families can remain outside
`U(B)`.

### P1: Prime Semantic-Atom Supersession Is Incomplete

The new source correctly makes Prime a semantic-design relation and realization
units projections. Residual deciding language still:

- limits whole-family review to the candidate function and carrier family;
- repeats that limited closure test;
- names a capitalized `Prime carrier`;
- requires `prime carriers` and the `<<prime>>` realization stereotype; and
- retains the function/carrier-family limitation in the design compression.

The complete semantic-atom family must be the deciding contraction boundary.
Carrier vocabulary must express Prime-conformance, not Prime identity.

### P1: Proportionality Expansion Has No Exact Predecessor Disposition

The candidate adds rival authority, failure classes, evidence uncertainty, and
downstream implementation/runtime/test/review/reconciliation space to the
proportional calculus while classifying the change only as clarification.

The successor must either bind those factors explicitly as evidence or
measurement of the already-governed ambiguity contraction, or disposition a
bounded supersession of the proportional predicate.

### P1: T-003 Reverses Final-Delta Proof And Human Acceptance

T-003 evaluation criterion 9 lists direct human acceptance before exact
final-delta proof. Release law requires the final-delta relation to be proven
before the human accepts that relation.

### P2: Prime Domain Declaration Lacks A Deciding Proof Hook

The source requires every accepted Prime atom to declare its admitted domain,
but Ontology evidence, Prime evidence, and closure review do not require that
domain declaration to be present and reviewable.

### P2: RC Qualification Evidence Is Weakly Anchored

The RC tag annotation cites only the short textual prefix `faf6d4f`. The
qualification commit is a child of the tagged subject and is available through
the continuing evidence branch, but it is not reachable from the tag and the
annotation does not carry its full object identity.

A successor RC must cite the complete evidence commit and preserve it through a
durable remote evidence ref.

## Mechanical Evidence

All declared mechanical claims reproduce:

| Check | Result |
|---|---|
| Predecessor ancestry | exact |
| Standards members | 41 / 41 |
| Member-path delta | empty |
| Changed / byte-conserved members | 9 / 32 |
| Recorded changed-member hashes | 9/9 |
| Compression source bindings | 13/13 |
| Standards aggregate | `485d22a73d85b43131287e7d76d0c7baf33e09094ea950ee1b9f276d7a372da2` |
| Predecessor aggregate | `ca6dc3d5094fc5473380df45d76da3c52263c5c21c52a3af62f542c97db2f86c` |
| Normative lines | 9,934 versus 9,792 |
| Normative delta | +142 / 1.45% |
| `git diff --check` | pass |
| Added, removed, renamed, or mode-changed standards | none |

The rejected executable-overstep and overcorrected-normative branches are not
ancestors of the tagged subject.

## Verified Sound

- The repaired release delta now classifies the retained-co-evolution change as
  a bounded supersession.
- Design/implementation feedback is evidence-only.
- Material surprise re-enters the smallest affected design scope.
- Semantic review reconstruction rejects headings, artifacts, hashes, and
  aggregate-green labels as substitutes for governed meaning.
- Durable exact-review law is coherent.
- The restored `competing or ambiguous authority` qualifier is conserved.
- The release note remains free of mutable review, acceptance, branch, and
  tag-existence status.
- No runtime, executable governance, schema, fixed model/worker procedure,
  candidate threshold, or mandatory new artifact entered the Product.

## Release Consequence

`v2.2.1-rc.1` must remain immutable and must not advance to final acceptance.
The normative repairs require a new exact subject and immutable
`v2.2.1-rc.2`.

The next RC must:

1. repair and reconcile source, compressions, templates, release delta, ticket,
   hashes, aggregate, and line count;
2. record qualification evidence with a full durable identity;
3. receive a fresh independent exact-tag review;
4. prove the proposed final carrier relation;
5. receive direct human acceptance; and
6. publish final refs without moving either immutable RC tag.

## Final Verdict

**REQUEST CHANGES**
