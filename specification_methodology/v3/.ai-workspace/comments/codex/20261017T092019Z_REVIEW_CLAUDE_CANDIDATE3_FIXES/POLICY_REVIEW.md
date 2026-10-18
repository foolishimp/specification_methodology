# R3/R4 affected policy review

Closed bounded evaluation, 2026-10-17. Reviewer: fresh nonauthor delegated
context. Independent expectations are in `POLICY_EXPECTATIONS.md`, written
before candidate bodies were opened.

**Result: `falsified` for the full affected policy-and-family-binding
predicate.** R3's exception repair and R4's actual recurrence decisions are
`satisfied` in the cases below. One low-severity family-account defect remains:
the Design family now consumes generic ticket recurrence policy but omits the
required F13 import from its argument. This is not a finding that the generic
third-rebuild stop is unlawful or that it produces the wrong outcome.

No candidate acceptance, complete conservation, complete reduction,
qualification, release or owner disposition follows from this result.

## Exact subjects and reference convention

- Common WHAT C3-I5-06: `4c340f7adec9f3c893e3e267b23e4cadeb357854`.
- Candidate source A: `9e901690e9f9b66917cafd917fff9ad755efa2a6`.
- Final records B: `7b40bdb65056967efa8cdcc682ab33af9ded32a2`.
- Old candidate: `af3b8b7107c92a216cc53d629ddeefecd7f77fca`.
- Candidate paths below are relative to
  `specification_methodology/v3/build_tenants/claude/` and refer to A unless
  marked B. Common paths are relative to
  `specification_methodology/v3/specification/` at C3-I5-06.
- Predecessor paths are relative to the installed read-only
  `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards/`.
  The selected manifest is
  `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`;
  the parent reverified the install. This reviewer read its owning sources.

The governing comparison is common `requirements/README.md:32-36`: compare
required, permitted and prohibited decisions under the same scope, triggers
and authority, preserving preferences and exceptions. The family/consumer
obligations are `:44-51,63-67,137-151`. In particular a generic obligation must
remain available without adopting an optional profile (`:151`).

## R3: necessary mutation exception is repaired

The predecessor's `DESIGN_MODULE_METHOD.md:255-277` binds the preference and
avoidance lists. Its owning immutable-carrier rule at `:1861-1878` expressly
permits materially necessary mutation, requires justification for the named
performance, host-runtime/framework and stateful-boundary cases, and excludes
convenience as sufficient justification.

The old candidate's `standards/DESIGN_MODULE.md:396-401` said that the lists
admitted no exception beyond the item saying “where practical”. That excluded
the separate owning mutation exception.

Candidate A `standards/DESIGN_MODULE.md:396-406` now makes departures depend on
permission and justification from the owning rule and explicitly names
materially necessary mutable carrier state under §10. The owner at
`:1790-1800` retains the predecessor's conditions. The preferred discipline at
`:134-142`, the two lists at `:380-394`, and the explicit effect-edge treatment
at `:1821-1832` remain available together.

| Independently fixed case | Supported source decision |
|---|---|
| The host requires a mutable carrier; necessity is supported; transitions and effect/authority boundaries are explicit. | The §10 exception remains usable. §4 no longer declares this departure nonconformant merely because it uses mutation. |
| Mutable state is selected for convenience alone. | The exception is not established; `:1800` and `:404` reject convenience as sufficient justification. |
| Necessity is asserted but unsupported. | Permission has not been established. This review supplies no positive exception judgment. |
| Mutation hides semantic authority, shared coupling or effects. | Necessity does not erase the separate avoidance and boundary obligations. No blanket exception to every avoided shape has been added. |
| An ordinary supported immutable/functional design is available. | The functional preference remains binding at its existing force. The repair does not turn it into unqualified freedom. |

The family argument at `:200,213,255-256` still identifies the preference,
mutation justification and necessary consumers. The design-review question
at `:2098` asks whether mutation is justified, bounded and local. The
checklists (`:2237-2242,2293-2295,2358-2375`) retain their earlier checklist
shapes; this review found no new counterexample that makes them revoke the
explicit owning exception. It does not certify every checklist case or a UX
refinement. The original R3 absolute-summary defect is closed on this source.

## R4: the predecessor already owns generic ticket recurrence policy

The original classification as an optional Design policy being silently made
generic is not sustained by the predecessor.

Installed `TICKET_METHOD.md:1085-1118` states the rule inside the generic
implementation-migration ticket contract. The second credible recurrence
forces explicit library/commonisation review (`:1095-1098`). When review shows
the same realisation pattern already exists in two boundaries or tickets, a
third local rebuild blocks implementation unless the ticket consumes a
library, extends it, or links an explicit do-not-commonise decision
(`:1100-1106`). This clause has no Design-profile adoption condition. It also
owns the preferred order and preserves the distinction between those hard
stops and merely discovered opportunities (`:1108-1118`).

Separately, installed `DESIGN_MODULE_METHOD.md:2078-2139` supplies the adopted
design-method review obligation and conformance refinement. It expressly
leaves ticket recording and enforcement to TICKET_METHOD (`:2116-2119`).
Its adoption and partial-adoption conditions remain explicit at
`:2546-2595`.

Candidate A `standards/TICKETS.md:858-888` preserves those generic decisions
at the generic owner. Its words “whichever profiles the Product adopts” at
`:866-867` make the existing scope explicit. They introduce no new
third-rebuild prohibition. The conditional Design refinement is named at
`:877-881`. `standards/DESIGN_MODULE.md:1938-1961` uses the ticket owner for
the shared threshold/order and retains its own design-review condition and
necessary design-specific obligations. Adoption and partial scope remain
owned at `:2398-2437`; availability alone is not adoption under
`standards/PRODUCT_DEFINITION.md:689-693`.

| Case | Decision preserved |
|---|---|
| Implementation-migration ticket; no selected Design recurrence family; second credible recurrence. | Explicit library/commonisation review is required by ticket law. |
| Same scope; review establishes two existing instances; third local rebuild; no consume, extend or recorded do-not-commonise decision. | Implementation is blocked. Design nonadoption does not waive this generic obligation. |
| Same case, with one of the three recorded alternatives and its required supporting fields. | This particular stop is discharged; it does not itself establish all implementation or acceptance conditions. Candidate fields at TICKETS `:798-806` preserve the predecessor's `:1005-1018`. |
| A suspected or merely similarly named repeat; the credible/same-pattern premise is not established. | A numeric count alone does not establish the required same-pattern case. No automatic commonisation or identity merger follows. |
| A reusable pattern is discovered outside the recurrence stops and the current claim's applicable hard stops. | It is repricing input; it does not automatically block the claim or admit a follow-up. |
| The work is outside implementation-migration scope and no applicable Design recurrence family is adopted. | This generic ticket clause does not become a universal stop on every kind of work. |
| The Design recurrence family governs the boundary. | Its design-conformance refinement and candidate-identification/design-change obligations apply within that adopted scope. |

The generic owner has an explicit argument: `standards/TICKETS.md:596`
identifies recurrence review and classifies the numerical thresholds as
policy choices of that member. Its consumer binding at `:618` names the
conditional Design refinement. The Design row at `:217`, consumer paragraph
at `:228-229` and detailed binding at `:259` agree on the direction of policy
ownership. This is conservation of the decisions just compared; no accepted
replacement relation is needed merely to locate that policy at its generic
successor owner.

## Remaining finding: F17 omits its required F13 import

**Low severity; family argument/account completeness, not a demonstrated
wrong recurrence outcome.**

Candidate `standards/PROFILES.md:31-43` requires a profile to import the
generic families its rules rest on and name each imported family by ID and
table section in the premise column. `standards/FOUNDATIONS.md:584-587`
confirms that table requirement. Common `requirements/README.md:44-50`
requires the applicable premises, extra policies, rules and consumers to be
bound to each material-family argument.

After the repair, F17's recurrence rule depends on F13's generic ticket
policy. F13 is explicitly identified at `standards/TICKETS.md:572-586` and
owns the policy at `:858-888`. However:

- F17's imported-family declaration, `standards/DESIGN_MODULE.md:160-181`,
  names F1, F2, F3, F4, F6, F8, F10, F12 and F18, but not F13.
- The recurrence row at `:217` still has only P2, P3 and I4 in its premise
  column. Its choice column links the new generic owner; it does not declare
  F13 or link F13's family argument as the import rule requires.

The concrete failed case is an actor acquiring F17's declared family
dependencies to review its adopted recurrence refinement. The family trace
does not declare F13 as a premise, although the rule now consumes that
family's extra policy. P2/P3/I4 alone do not select the second/third numerical
thresholds. The prose link is usable and produces the right policy outcome;
the claimed family account is incomplete under its own explicit rule.

Smallest correction: declare F13 and its owning family-table section in
F17's import declaration and the recurrence row's premises, then update any
affected derived account. The threshold, adoption scope and ticket result
need no semantic change. Disposition remains the parent's/owner's decision;
this reviewer made no repair.

## Affected procedures, views and record standing

The readback included PROFILES' boundary/import contract, the actual
TICKETS and Design procedures and family tables, partial adoption, the
Design checklist, and ASSURANCE's selected whole-path procedure.
`standards/ASSURANCE.md:889-909` still describes the design-specific
computational/recurrence evaluation. Installed
`STDO_REFERENCE_FRAME_BASELINE.md:1227-1245` contains that same selected
whole-path obligation. No concrete additional recurrence-outcome
contradiction was established here, so this review raises no separate
ASSURANCE ownership finding and does not broaden its scope to that entire
evaluation family.

A read-only in-memory check bound `standards/frames/FRAME_INPUTS.json` and
actual Git-object bytes at A. The recorded frame hash matched for
`dm-task-d`, `stale-summary` and `acceptance-release`; each selected
DESIGN_MODULE/TICKETS route's member hash also matched its current owner
(three, five and two routes respectively). The changed consumer sentence
in `standards/frames/dm-task-d.md:1552-1561` correctly says the recurrence
row refines TICKETS. The route declaration at `:35-44` does not offer this
frame as a complete functional-preference or recurrence-policy task.
These samples establish current subject references and that observed
directional wording only; they do not establish every excerpt's fidelity or
ordinary-use sufficiency. No mutation-capable generation/check script ran.

After the independent source conclusions, final records B were inspected.
They correctly retain proposal/pending acceptance and invalidate the old
satisfied read standing for the changed source:

- `frontier/REVIEW.json:1484-1506`: functional-bias row is an author proposal,
  ticket decision pending, `indeterminate`, with the pre-repair read and
  reread owed explicitly identified.
- `frontier/REVIEW.json:2792-2814` and `:13723-13745`: Design recurrence and
  ticket recurrence have the same appropriately limited standing.
- `frontier/REVIEW_ASSESSMENTS.json:96-102,1373-1379,1802-1808` agrees on
  those three indeterminate records.
- `frontier/REVIEW.json:2590-2609` does not falsely claim independent review
  of the unchanged immutable-carrier row; it remains indeterminate.

The scalar historical `modal_force: preserved` survives only inside a record
whose result and scope explicitly say the current reread is owed. This
readback does not mutate those records or confer ticket acceptance. No
affected false current acceptance claim was found in these sampled rows.

## Evaluation boundaries and acquisition

This is source-first reasoning over frozen Git objects and the selected
installed predecessor, with a read-only digest sample. No candidate or Git
mutation, author test execution, peer-live-worktree read, further delegation
or external paid call occurred. Only the two named commentary files were
written. Author tests and returned reviewer judgments were not used to form
the source conclusions. Consumer discovery did acquire heading/search
excerpts from the author's historical `design/REDUCTION.md` account; those
assertions were not used as correctness evidence. Author-written normative
family arguments were necessarily part of the reviewed source.

A conservative reconstructed acquisition bound charges complete requested
source ranges even when tool-output truncation may have hidden some of them:
386,811 unique source bytes, plus a 20,480-byte reserve for subsequent
rendered record/memory extracts, gives **407,291 bytes** against the
524,288-byte allowance. Requested repeated source presentation was separately
bounded at **91,127 bytes** before that record reserve. Path listings,
command code and digest-result metadata are not source-body acquisition and
are separate from this count. The count is an upper bound on this task's
presented source, not a native active-context or token/cost measurement. No
required excess was omitted; the review completed before the 30-minute
checkpoint.

The closed result supports R3 closure and correction/closure of R4's original
policy classification, with the F17 trace defect retained. Full predecessor
conservation, complete interpretation, ordinary-use trials, all generated
views, integrated reduction and final candidate acceptance remain outside
this delegated predicate.
