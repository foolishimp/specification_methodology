# Posted copy: Claude C1 cross-review of the Codex principles attempt

This is the Claude tenant's posted copy of its cross-review, placed here under
the rule that each tenant writes only inside its own build tenant. The
original, written under the earlier grant and frozen at 2026-10-11T06:53:37Z,
is `stdo_3/build_tenants/codex/qualification/C1_REVIEW.md`, SHA-256
`40700da54763fdeac4103c2f3c0530e2266070ce6bcb57cd2c3a8d3eab9ba8be`. The body
below is that file verbatim. Reviewed subject:
`stdo_3/build_tenants/codex/design/PRINCIPLES.md`, SHA-256
`52fbd93ad31476823d5bed7a991ee85b5d8e8e188037fcdb80ac052540051611`.

---

# Claude C1 Cross-Review of the Codex Principles Attempt

Reviewer: Claude, under the T-001-CODEX cross-review grant. Write territory:
this file and the T-001-CODEX return carrier. The candidate is not modified.
Allowance: 20,000 generated tokens, 45 minutes. Started 2026-10-11T06:48:54Z.

Basis: `stdo://releases/v2.5.1-rc.2/`, manifest SHA-256
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`. Common
inputs: snapshot `C1-inputs-20261011-02`, 16 members. Governing expectations:
[PRINCIPLES.md C1 Return](../../../specification/requirements/PRINCIPLES.md#c1-return),
[initial principles task](../../README.md#initial-principles-task) and the
[conformance discriminators](../../../specification/conformance/README.md).

## Closed result

Per [RF-012](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-012-closed-results),
on the exact subject below:

- Derivations, countermodels, hypothesis labelling, mechanism analysis,
  boundaries, prose and cost reporting: `satisfied`.
- Source-recovery completeness: `falsified` for the clauses named in finding
  1, which the candidate re-derives, lists as gaps, or states without citing
  the rc.2 owner.

Recommended disposition for the Executive: `local_repair`. The governing
relations are coherent and every argument checked holds; the defect is that
several conclusions are labelled derived or proposed where rc.2 already states
them, which mis-states the standing of those items and the migration scope at
C2. No re-entry is required. This review does not accept or reject the
candidate; Jim selects the common basis.

## Exact subject

- Candidate: `stdo_3/build_tenants/codex/design/PRINCIPLES.md`
- SHA-256 `52fbd93ad31476823d5bed7a991ee85b5d8e8e188037fcdb80ac052540051611`,
  318 lines, 6,290 words, 49,716 bytes; all three match the author return.
- Author return: `stdo_3/.ai-workspace/tickets/active/T-001-CODEX-principles.md`.
- Mechanical checks by this reviewer: 40 links resolve, 32 `stdo://`
  fragment occurrences to 31 unique installed headings; no trailing
  whitespace; author timing reported (05:54:05Z to 06:18:07Z, 1,442 s, UTC
  clock; token counters marked unavailable).

## Expectations, recorded before opening the candidate

These are what a satisfying C1 attempt must show, derived from the common
contract and the rc.2 clauses this reviewer recovered independently for its
own attempt. The reviewer's own candidate is not an oracle; where this review
and that candidate disagree, the installed bytes decide.

1. Subject integrity: the file's hash, line, word and byte counts match the
   author return; the return's claims about the candidate are true of the
   candidate.
2. Source recovery: a table of exact `stdo://` routes for each of P1–P6; every
   route resolves to a real heading in the installed rc.2 standards; each
   cited clause states what the candidate attributes to it, checked on a
   sample against the bytes; the recovery is not confined to the clauses the
   common draft already cites.
3. Derivations expose their premises: no claimed derivation assumes its
   conclusion (conformance row one); any countermodel offered satisfies the
   stated premises and defeats the stated conclusion; independence is argued,
   not assumed; the candidate does not claim a minimal basis it has not shown.
4. Hypotheses are labelled as rc.2 labels them: a categorical claim either
   defines objects, arrows, identities and composition laws and proves
   preservation, or is labelled a hypothesis
   (`AXIOMATIC_CALCULUS.md#traversals-and-functor-kinds`); the Markov
   statistical claim is candidate status (`WORLD_MODEL_METHOD.md#epistemic-status-of-the-construct`);
   universal algorithmic meaning is refused by AC's scope; external
   mathematics is support for terminology, never builder law.
5. Contradictions, duplication and gaps are checked against the pinned `-02`
   common text and the rc.2 bytes, not against earlier plan posts; an absent
   operation or benchmark is distinguished from absent governing law
   (`REFERENCE_FRAME_METHOD.md#select-and-activate`,
   `#reconfigure-when-necessary`, `#method-self-qualification` exist).
6. Candidate mechanisms carry the five questions; mechanisms supported only by
   precedent are identified; realisation vocabulary (HoG, F_D/F_P, worksite,
   ledger) is not placed in the foundations without the profile relation
   `ODD_METHOD.md#probabilistic-compute` declares.
7. Boundaries: no redefinition of common WHAT; no peer realisation read; no
   acceptance, a_c or trial claim; author self-checks are labelled as such.
8. Proportionality of the candidate itself (`SPEC_METHOD.md#proportional-method-and-delivery-stdo-up-014`):
   each formal apparatus introduced removes a named ambiguity a bounded reader
   would otherwise face; apparatus that does not is identified as cost.
9. The author return reports start, end, elapsed and spend with a measurement
   source, or marks counters unavailable, per the ticket's resource section.
10. Prose follows WRITING_GUIDE; links resolve; no trailing whitespace.

## Findings

Severity follows the baseline's technical triage: material findings change a
standing, scope or claim; minor findings are recording defects.

### 1. Material: existing law re-derived, listed as a gap, or stated without its owner

The recovery table has 22 rows and every sampled attribution matches the
bytes (semantic resolution 586–600, atomic functions 844–860, entity cut
640–654, composition law 1231–1245, yield A9 in 1032–1135 were checked
directly). What it omits are clauses the candidate then treats as derivation,
consolidation or gap. Occurrence counts in the candidate are zero for each.

| Candidate statement | rc.2 owner, not cited | Effect on standing |
|---|---|---|
| D6 "restart is re-entry of the same method over current state"; "generic recovery semantics" listed as an unresolved gap (line 306) | [UP-020 Checkpoint, Continuation, Progress, And Churn](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#agentic-construction-execution-stdo-up-020): preservation checkpoint under an existing grant; a proposed restart identifies why repair of retained work is insufficient, what survives and which causal assumptions change | D6's conclusion is recovered law; the gap is narrower (a generic work-state object, which exists only in ODD), not the recovery semantics |
| D4 failure and uncovered-coverage coordinates as a "proposed finite aggregation law" | [AC-013](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-013-transformation) preserved, introduced, removed, residuals fields; [AC-007](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal) no coercion to success | the aggregation contract is a specialisation of AC-013 accounting; D4 remains a good conformance case but is recovered, not new |
| "A complete successor must preserve or explicitly reframe/supersede every material predecessor obligation" (line 308) | [UP-015](stdo://releases/v2.5.1-rc.2/standards/RELEASE_METHOD.md#successor-baseline-conservation-stdo-up-015): conserved, superseded, intentionally removed, not applicable; unresolved disposition blocks qualification | the obligation and its four dispositions are owned law; the candidate's migration clause should bind to it, which also governs this project's own 2→3 move |
| "usable actor/context envelope" as an unresolved gap; context acquisition mechanism row | [AC-010](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-010-material-closure), [AC-011](stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md#ac-011-projection), [RF-013](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-013-reconstructable-activation), [RF-017](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#rf-017-proportional-compression), [Select And Activate](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#select-and-activate), [Reconfigure When Necessary](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#reconfigure-when-necessary) | the formal context object, the reconstructability test, lawful compression and the select/refuse/reconfigure operations exist; the gap is the derivation of a frame's manifold under an envelope, an addition over existing operations |
| Authority as "an argued independent normative premise" citing AC-005 and RF-006 only | [UP-004](stdo://releases/v2.5.1-rc.2/standards/IDENTITY_METHOD.md#authority-identity-and-conservation-stdo-up-004): authority is identity-bearing; explicit proxy grants | the premise is recovered law with a named owner, which strengthens the candidate's own claim |
| D7 independence and "required independent review still supplies its own judgment" | [UP-022](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#assurance-boundary-congruence-and-method-qualification-stdo-up-022), [Method Self-Qualification](stdo://releases/v2.5.1-rc.2/standards/REFERENCE_FRAME_METHOD.md#method-self-qualification), [UP-021](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#complete-enclosing-relation-admission-stdo-up-021) | D7 is recovered; UP-022's freeze-before-exposure rule and UP-021's "reuse does not transfer responsibility" are the exact owners |
| Probabilistic worker boundary cited only through ODD probabilistic compute | [Probabilistic Work Boundary](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#probabilistic-work-boundary) and [Ambiguity Governance](stdo://releases/v2.5.1-rc.2/standards/SPEC_METHOD.md#ambiguity-governance-rule), which own the substrate-neutral concepts ODD specialises | the generic account the candidate wants exists above the profile; the specialisation relation runs from SPEC to ODD, which is the direction the candidate's own profile boundary needs |

Consequence: the labels "derivation", "proposed consolidation" and "gap" are
wrong for these items, and the migration disposition at C2 would classify
conserved law as new. The arguments themselves are unaffected. Bounded repair:
add the rows, relabel the standings, and restate the two gaps as additions
over existing operations. The same class of finding was returned against this
reviewer's own candidate and accepted there.

### 2. Minor: line-span coordinates overreach the cited heading

AC-002 is cited as 378–391; AC-003 begins at 384. RF-012 is cited as 409–442;
RF-013, RF-014 and RF-015 begin at 424, 430 and 437. AC-017 is cited as
749–786; 749 is the parent section. The anchors are exact and resolve; the
spans are not exact. Recording defect only; the table's own note calls them
recovery coordinates.

### 3. No finding: the categorical fragment is correct

Checked by hand. 𝒜 is the free category on typed primitives (path equality,
empty-path identity, concatenation); ℐ is the selected carrier sets with total
functions; 𝒞_H is pairs (f, c) with c valued in an additive monoid, the
composition `(g,d) ∘ (f,c) = (g ∘ f, x ↦ c(x) + d(f(x)))` is associative and
`(id, 0)` is a two-sided identity; S and R_H are functors by the free-category
universal property. The mod-4 witness shows S is not faithful. The proof that
an equivalence must be faithful (naturality of η then cancellation of the
isomorphism η_Y) is valid. The fragment meets the functor-kind clause's
condition for claiming categorical laws, and the candidate correctly limits
the conclusion to this S. No theorem-prover check was run by either party.

### 4. Observation: the three-reading split of the algorithmic claim

D1 separates "interpretation involves a process", "every material
interpretation can be made operationally explicit" and "all meaning is
captured by a formal language". This is the clearest treatment of P1's open
claim in either tenant input and the conformance row on information versus
representation. Recommend the common pen adopt the split in P1's standing.

### 5. Observation: proportionality of the candidate

The categorical fragment (about 600 words) settles whether the span is an
equivalence, which is a real ambiguity in the common draft; proportional. The
countermodel table is compact and each row discriminates a named implication.
The critique of the two historical plans (about 700 words) exceeds the
contract's request to critique mechanisms, but it addresses tuple inputs
and is short. The reading route at the top serves a bounded reader. No
finding.

### 6. Observation for the common decision

Both tenants now hold the same position on the contested derivation:
conservation is conditional on a selected outer contract and faithful
refinement, not on finite capacity alone. The candidate's compression
sentence (line 11) and the other tenant's generative statement with stated
premises are compatible candidates for a common P0. The residual
disagreement is about duplication: this candidate treats repeated normative
bodies as "explanatory, not necessarily semantic"; the other counts them as
reconciliation cost under UP-014. That is a C2 question, not a C1 defect.

### 7. Minor: critique accuracy

The critique of the other tenant's plan is fair on every point checked
(three-cause claim too strong; ticket-first and per-activation cost are
selections, not derivations). The "eight/nine-trial discrepancy" is
immaterial; the matrix table has eight rows.

## Expectations met

1 met. 2 met for the 22 rows present, not met for completeness (finding 1).
3 met: every derivation names its premises, line 85 correctly identifies the
circularity in the other tenant's original statement, and the countermodels
satisfy their premises and defeat their conclusions. 4 met. 5 met: no
contradiction is alleged against the common draft, and the plan critique is
directed at the plan posts. 6 met: nine mechanisms with the five questions;
runtime bindings placed downstream. 7 met. 8 met (finding 5). 9 met. 10 met.

## Review cost and residuals

Started 2026-10-11T06:48:54Z; frozen at the time recorded in the T-001-CODEX
return. Wall time by `date -u`; generated-token counters are not exposed to
this host and are marked unavailable against the 20,000 allowance. Read in
full: the candidate, the author return, and the rc.2 clauses it cites that
this reviewer had not already recovered. Not done: theorem-prover check of
the fragment; re-acquisition of the WORLD_MODEL empirical records; any
runtime trial. This reviewer authored the other tenant's candidate and did
not use it as an oracle; every judgment above cites installed bytes.
