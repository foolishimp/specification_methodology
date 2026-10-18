# T-007 Executive lifecycle tooling specification

- id: T-007
- title: Specify deterministic a_c support tools for F_P development actors
- type: feature
- ticket_category: ordinary
- status: completed
- goal: Define F_D support tooling used by F_P Executives, Workers and Reviewers under STDO3.0-owned contracts.
- change_intent: Extend the a_c Product realization with deterministic acquisition, assembly, checking, transport and evidence operations derived from the selected method, without duplicating its lifecycle.
- change_class: product_reprice
- re_entry_point: Product
- triaged_at: 2026-10-18T16:19:18Z
- created_at: 2026-10-18T16:19:18Z
- updated_at: 2026-10-18T16:41:40Z
- affected_boundary: a_c common WHAT and project frame basis
- dependencies: Exact installed STDO v2.5.1-rc.2; existing core a_c requirements

## Owner instruction

Jim requested: “this is additional a_c tooling i want you to write up the a_c
product definition and requirements for this tooling to support the life cycle”.
Jim subsequently clarified: “to be clear this is a set of F_D tooling to support
the F_P Executive, workders & reviwers - STDO3.0 sets the methodology and hence
the toolset needed, don't duplicate”. This clarification controls the scope.
STDO3.0 owns method/lifecycle, role duties, frame and activation semantics,
applicability, admission, result algebra, review/independence and acceptance.
a_c specifies tool inputs, deterministic outputs/checks, observable transport
and evidence boundaries supporting those existing contracts. It does not
author another lifecycle or take over F_P coordination, meaning or decisions.
This instruction authorizes specification authoring only; no implementation,
commits, publication, acceptance or release is requested.

## Basis and intake

The operative builder basis is installed STDO v2.5.1-rc.2, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`,
selected by [stdo_a_c.json](../../../stdo_a_c.json). The exact installed
`SPEC_METHOD.md`, `REFERENCE_FRAME_METHOD.md`, `TICKET_METHOD.md` and
`AXIOMATIC_CALCULUS.md` govern this work. Mutable sibling v2/v3 source and
represented candidate versions do not replace this basis.

The provisional target-contract derivation reference is common V3 commit
`494451522072ec34381c644f1ccfa2331f2b1e27`, package
`specification_methodology/v3/build_tenants/common/`, tree
`082df4ea2b7b3658aab528bbfbcfe81234ccc810`. Exact member identities and owning
clauses are recorded in the [source-owner map](../../../specification/requirements/fd-source-owner-map.md). This unaccepted,
unreleased, uninstalled candidate is derivation evidence, not the a_c builder
or an adopted consumer constitution. No fabricated v3 release URI, Product
composition, runtime dependency, sibling change or frozen-model regeneration
is selected. Runtime use binds the caller's exact operative method/profile and
reports unsupported contracts rather than substituting this candidate.

The stable Intent direction remains source-faithful, carrier-neutral calculus
realization. Product scope gains deterministic tools supporting all three F_P
actors; Requirements state observable tool obligations linked to their upstream
owners. Intent wording and project navigation are aligned without changing
that direction. Tenant design, code, tests and qualification remain downstream.
New families are Deferred because owning design and realization are pending;
that status does not withdraw the requested Product outcome. Existing
AC-R-001..015 and the separate F_P source-to-model capability remain intact.

## Activations and effects

- Executive `/root` binds scope and basis, delegates this bounded authoring,
  consumes the frozen Writer return and the closed nonauthor assessment
  without mutating while in the Executive role.
- Nonauthor assessor `/root/ac_fd_contract_review` independently assesses the
  exact frozen source under F-TOOL-CONTRACT and returns to Executive `/root`;
  it does not author or repair the assessed candidate.
- Writer `/root/ac_lifecycle_spec_writer` is activated to author only
  `a_c/README.md`, `a_c/stdo_a_c.json` (justified locator/authority updates),
  `a_c/specification/GOALS.md`, `INTENT.md`, `PRODUCT.md`,
  `REFERENCE_FRAME_BASIS.md`, `requirements/README.md`, new lifecycle
  requirement/scenario files under `requirements/`, and this ticket.
- The owner instruction supplies the bounded specification work grant. This
  activation records the delegated operation and territory; neither role name
  nor ticket status creates wider authority. No tenant design/code, frozen
  studies, representations, older tickets, sibling Product or Git effects are
  granted. Preserve unrelated work and concurrent source changes.

The pre-clarification broad lifecycle/governance draft is superseded within
this same uncommitted source increment. The renewed Writer activation narrows
the same territory to this F_D tooling contract and removes duplicated method
law. Dispatch/capture wrappers retain external observations and do not relabel
an invoked F_P worker's semantic result as F_D. Named domain operations remain
distinct from deterministic evaluation/proof traversals `F_D[v]`.

## Evaluation criteria

The resulting Product and requirement families define externally observable
tool operations: supplied inputs, deterministic outputs/checks and explicit
limits, each linked to exact method owners. They support F_P Executive,
Worker and Reviewer use, including independently acquired sources/proof and
candidate comparisons. They do not restate method-owned governance, role
duties, result algebras or workflow states. The common WHAT remains independent
of Graphify, provider, protocol, executor topology and storage choices.

The deciding proof is source review against the exact installed builder method,
the exact provisional STDO3.0 owner clauses and existing a_c boundary,
requirement/scenario trace coverage, local-link and
whitespace checks, and exact Product Definition verification. Unchanged runtime
tests and upstream Graphify trials are not pertinent to this specification-only
change. Nonauthor review assesses the frozen authored files before the bounded
source increment can close.

## Non-closure conditions

- a_c duplicates method/lifecycle law or takes ownership of F_P judgment.
- Governing requirements are replaced by graph reachability or mechanical shape.
- The tool claims new semantic, mutation, admission, acceptance or release authority.
- Current runtime functionality or qualification is asserted for the proposed tooling.
- A universal waterfall, ticket database, actor count, polling supervisor,
  resource quota or routine approval ceremony is imposed.
- Source/derived identity, incomplete coverage, conditional applicability,
  actual acquired evidence or unknown operation effects are silently collapsed.
- Existing core requirements, frozen studies or unrelated work are changed.

## Result and continuation

The Writer candidate is authored for nonauthor source review. It contains the
Product extension, aligned Intent/Goals/navigation/frame-basis locators,
[13 tool-operation requirements](../../../specification/requirements/fd-support-tools.md),
[three qualification obligations and 15 scenarios](../../../specification/requirements/fd-support-verification.md),
and the exact source-owner map. New families are Deferred. The superseded broad
lifecycle/governance draft was replaced within this same source increment.

Proportional checks passed: `git diff --check`; 101 local Markdown file/anchor
links; unique identities and complete scenario/source-owner trace for all 16
new requirements; exact SHA-256 verification of all ten referenced common
members and the pinned package tree; preservation of all 15 existing core rows;
and Product Definition comparison proving that only the T-007 frame-basis
authority locator was added. `stdo status --definition a_c/stdo_a_c.json
--verify` returned valid with no failures for the unchanged installed basis.
No runtime tests, Graphify trials, implementation/design or frozen artifacts
were changed or rerun. The final ticket links are checked with the frozen
per-file subject before return.

The durable source return is this ticket plus the permitted Product/requirement
files. Construction, nonauthor assessment, owner disposition, implementation,
qualification and release remain distinct. Specification authoring and its
bounded nonauthor assessment are complete as recorded below. Tenant design or
implementation requires separately selected work and has not started. No
commit or push is performed.

## Subsequent review and completion record

Recorded at 2026-10-18T16:41:40Z (2026-10-19 Australia/Sydney), after the frozen
candidate's assessment. The reviewed ticket preimage is SHA-256
`14a86e7912f8a88fa0019abb1bb449ec356552f23c0705f45dc883106dec179e`.
The original eleven-file reviewed subject remains identifiable by the exact
pins in the [nonauthor report](../../comments/codex/20261019_AC_FD_TOOLING_REQUIREMENTS_REVIEW.md),
SHA-256 `66039c31575f9a63ca9ea0b091a540095b02dadf10a1676868988cd3c071510b`.
This subsequent recording changes only this ticket, not the reviewed Product,
requirements, source-owner map or report.

Assessor `/root/ac_fd_contract_review` returned no actionable document-contract
defect. Its three source predicates were satisfied: conservation of method
ownership/exact bases/existing a_c obligations; sufficient specification-level
tool obligations for all three F_P actors; and separation of deterministic
support, F_P judgment, owner decisions and pending qualification. The verdict
is bounded to the exact source contract. It establishes no executable tool
behavior, generated-model semantic fidelity, actual-use benefit, operational
qualification, Product acceptance, method adoption or release.

Executive `/root`, the result consumer, consumed that closed return and
independently reproduced the 104 local links/anchors, 16 requirement IDs,
15 scenarios, ten source-member digests/package tree, core-row preservation
and T-007-only overlay locator change. No supported repair was required.
Writer `/root/ac_lifecycle_spec_writer` was then activated solely to record
this result/continuation against the exact ticket preimage above, correcting
the assessor/consumer attribution and checking the recording diff/links.

T-007 is completed for specification authoring and bounded independent source
assessment only. Both new requirement families remain Deferred: owning tenant
design, public implementation and executed qualification are pending.
Reserved owner decisions, Product acceptance and release remain unperformed.
Any subsequent design/implementation is separately selected work; this record
does not authorize or begin it. No code, runtime tests, Git commit or push is
part of this recording operation.

## Owner-requested main checkpoint

2026-10-18T16:49:19Z — Jim subsequently instructed: “commit to main”. Writer
`/root` is activated to record that instruction here and create one local
checkpoint on `main` of the twelve a_c specification and review files produced
by this increment. The scope is the eleven authored files identified above,
including this ticket's subsequent records, plus the nonauthor review report.
The reviewed Product/requirement content remains unchanged. This grant covers
the scoped index and commit effects; it selects no implementation, Product
acceptance, release or remote publication. The commit containing this record
identifies the checkpoint.
