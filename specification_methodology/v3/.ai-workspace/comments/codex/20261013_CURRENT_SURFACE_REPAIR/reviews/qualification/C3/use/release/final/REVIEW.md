# Release/Adoption review: `plan.md` (actual baseline vs. actual defective subject)

**Bindings:** subject commit `427a0deb39b7cd8e298b3b2ebc126c052f056d8a`; subject `plan.md`, sha256 `4bc09e57…1980` (supplied, not recomputed); frame RELEASE_ADOPTION. I used only the method text in the view (`RELEASE_METHOD.md` `c061ad3d…`, `SPEC_METHOD.md` `61262847…`, `REFERENCE_FRAME_METHOD.md` `b2fe9139…`). I used no tools, and the grant is review only.

## 1. Baseline adequacy: **adequate** (with unresolved items listed in section 3)

| Baseline statement | Rule it meets | Result |
|---|---|---|
| "Changed local member NEW belongs to a mutable successor candidate; immutable rc.2 OLD is retained" | Release Identities: "An immutable RC tag never moves". Immutable RC Publication: "Further work increments `<n>`" | satisfied |
| "consumer remains pinned at its declared rc.1 basis until an authorized complete explicit update binds a published successor" | Selector And Consumer Adoption: "Moving the Git version-line selector does not update any consumer. Adoption is a separate explicit Product-Definition transition". Explicit Complete Consumer Update | satisfied |
| "Qualification must address the unchanged installed exact candidate" | Exact-Cut Qualification: "Source success does not prove packaged or installed behavior" | satisfied |
| Four-way successor dispositions; "routes alone do not establish restatement" | STDO-UP-015: "naming or code similarity does not prove conservation without relevant evidence" | satisfied as a requirement. "Restatement" is not a term in this view, so I accept that phrase only as a restriction. |
| "Review supplies no publication or adoption authority" | RF-006; the grant | satisfied |

**The overall outcome stays not green, and the baseline says so truthfully.** It claims no qualification:
- **rc.2 qualification is `indeterminate`.** No exact installed rc.2 run is supplied, and the green checks refer to mutable local bytes (RF-012).
- **Successor (NEW) qualification is `invalid_basis`.** No published immutable cut exists to qualify (RF-005).

## 2. Defective-subject adequacy: **inadequate**

**F1: Line 2, "keep the rc.2 identity because the tests pass." Result: `falsified`.**
- Immutable RC Publication: "Each published RC tag is immutable. Further work increments `<n>`".
- Exact-Cut Qualification: "If review requires any qualifying-byte change, the verdict remains attached to the old RC and a higher RC is published".
- Release Identities: "Equal version text does not collapse these identities".
- Passing tests on NEW bytes say nothing about the identity of rc.2 (OLD), which is a basis mismatch under RF-005.
- **Smallest repair:** say that rc.2 stays OLD, that NEW is a mutable candidate for a higher-ordinal RC on the same line (e.g. rc.3), and that it is unpublished.
- **Owner:** the plan text belongs to the fixture Writer. Any actual publication belongs to the Product release authority under a publication grant, which nobody here holds.

**F2: Line 3, "Highest published RC discovery automatically updates all consumer definitions." Result: `falsified`.**
- Selector And Consumer Adoption: the selector "never answers: Which exact STDO cut governs this consumer?" It also says "Moving the Git version-line selector does not update any consumer", and that mutation requires an operator-accepted plan digest that is re-derived before any change.
- Counterexample in the material: the consumer is pinned to rc.1 at digest RC1, and the selector discovers rc.2 "without permission to alter basis".
- RF-006 applies too: the existence of a selector is not adoption authority.
- **Smallest repair:** keep the consumer at rc.1/RC1 until an explicit adoption plan or a complete consumer update is presented, accepted by digest, and re-derived.
- **Owner:** the consumer Product Definition owner or operator.

**F3: Line 4, "A successful cold read of the mutable worktree qualifies the unchanged installed RC." Result: `falsified`.**
- Exact-Cut Qualification binds the immutable RC ref, the annotated tag object, the peeled commit, the tree and subtree, and the member set. It also says "Source success does not prove packaged or installed behavior."
- The worktree holds NEW, not OLD, so it is not even rc.2's bytes. Used as rc.2 evidence, that is `invalid_basis` (RF-005).
- rc.2 qualification itself remains `indeterminate`.
- **Smallest repair:** require evidence from the exact installed rc.2. Then the human authority decides acceptance.
- **Owner:** the release qualification reviewer for the evidence, and the human release authority for acceptance.
- "Cold read" is not defined in this view. The finding does not depend on what it means.

**F4: Line 5, "The predecessor route index alone completes all successor dispositions." Result: `falsified` for the sufficiency claim; the dispositions themselves stay `indeterminate`.**
- STDO-UP-015 requires one semantic disposition per affected predecessor claim, backed by relevant evidence. It also says "An unresolved disposition blocks qualification."
- The plan's own line 1 shows a byte change from OLD to NEW. An index of routes cannot by itself establish conservation of that semantics.
- Whether some route index *could* contain real dispositions is undetermined here, because "route index" is not defined in the view. I have kept that question open rather than widening the frame.
- The predecessor is also not identified, and the material leaves it ambiguous between rc.1 and rc.2.
- **Smallest repair:** name the exact predecessor immutable RC, and record a disposition with evidence for each affected claim.
- **Owner:** the successor candidate's author.

Line 1 ("rc.2 is immutable, OLD") is correct.

## 3. Scope, unresolved evidence and limits

**Scope:** the view is sufficient to decide F1–F3 and the sufficiency claim in F4. These relations remain `out_of_frame` or underdetermined:
- the Project Release Namespace and project-qualified tag form (only the unqualified `v2.5.1-rc.2` is supplied);
- whether the selector is annotated and its peeled commit;
- the subtree root and tree;
- the identity of the predecessor;
- the meaning of "route index", "cold read" and "restatement";
- the general rule that an evaluation baseline must keep a falsified outcome. This task is a release task, so I checked the baseline only for truthful non-green status.

**Measurement limits:**
- OLD, NEW and RC1 are symbolic fixture identities.
- I could not reacquire or recompute `subject_sha256`, Git membership or the subject commit. Those checks belong to the host Writer before dispatch.
- My results cover only the supplied bytes.

## 4. Next permitted review action

Report findings F1–F4 to the Codex C3 Executive. That Executive may accept or repair this bounded fixture proof only. Any change to the `plan.md` text is a fixture-Writer repair within the tenant-only grant.

The grant does not permit any of the following, and I did none of them:
- materialising an RC or updating refs;
- publication;
- qualification acceptance;
- consumer adoption or update;
- merge, or upstream or common acceptance.
