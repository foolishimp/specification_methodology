# Codex Documentary Implementation

This is the Codex documentary implementation of the selected STDO 3 work scope.
Jim's “continue” accepts the proposed C2 scope at tenant commit 65fd45b for this
build and starts the first actual-use thread. The shared main registry is not
edited by this tenant. Installed STDO 2.5.1 RC2 remains the construction basis;
these documents are an implementation candidate, not an installed release.

Document names, grouping and reader routes are tenant HOW unless an accepted common publication boundary constrains them. The expressed method semantics must satisfy the common contract; they do not replace construction specifications.

## Start A Bounded Task

1. Recover the selected outcome, exact current bounded job, subject/basis and
   permitted effects under [W-01](WORK_METHOD.md#w-01-bind-the-selected-work).
2. Obtain sufficient current context using [W-02/W-03](WORK_METHOD.md#w-02-acquire-sufficient-context).
   Missing or unfit material has a truthful disposition, not a hidden default.
3. Perform and observe the bound work under [W-04](WORK_METHOD.md#w-04-transform-and-observe).
4. Apply the required [evaluation](EVIDENCE_METHOD.md#e-03-assess-the-exact-material)
   and [conjunction](EVIDENCE_METHOD.md#e-04-conjoin-without-losing-findings).
5. Select only the next authorized action under [W-05](WORK_METHOD.md#w-05-select-the-next-authorized-action).
   A new actor resumes from current workspace under [W-06](WORK_METHOD.md#w-06-re-enter-current-persistent-work).

This entry routes an ordinary task; it does not prescribe all tasks as five
stages. It supplies no operation or acceptance grant. Import additional source
only when material relations require it.

## Canonical Owners In This Slice

| Document | Owned meaning |
|---|---|
| [Foundations](FOUNDATIONS.md) | Purpose, interpretation, scoped objects, typed composition, conservation and supported formal claims. |
| [Work](WORK_METHOD.md) | Bind/acquire/transform/dispose, finite context, current-state recovery, effects, progress and churn. |
| [Evidence](EVIDENCE_METHOD.md) | Evaluate/conjoin, exact claim, judgment algebra, independent assessment and conserved findings. |

The six library families are shared definitions bound to particular
responsibilities. Instance count, physical interfaces and publication views do
not determine the number of semantic primitives. Different assessments and
decision owners remain distinct where required.

The [build plan](../design/BUILD_PLAN.md) reserves later Spec/Qualification
documents and optional domain profiles for their dependency-ready threads. This
slice is being tested by actual construction, defect detection, repair and
fresh-actor continuation in [T1](../qualification/T1/RETURN.md). It does not claim
whole-method, full successor, a_c, release or adoption qualification.
