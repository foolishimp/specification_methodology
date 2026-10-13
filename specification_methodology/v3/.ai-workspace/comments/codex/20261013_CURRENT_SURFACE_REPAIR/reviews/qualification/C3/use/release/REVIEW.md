# Release and Adoption Frame: plan review at commit `b0ec615c`

**Binding (RF-005):** I'm a fresh, author-independent reviewer. I used only the selected Release and Adoption view and the supplied task material, and called no tools.

- **Grant:** "Review this plan. No RC materialization, ref update, consumer update, publication, merge or acceptance grant."
- **Coordinates:** published `v2.5.1-rc.2` has member A = OLD. The local successor has member A = NEW and is unpublished. The consumer is pinned to `v2.5.1-rc.1` with manifest digest `RC1`. These are symbolic fixture identities.
- **Subject digest:** I could not recompute the declared subject_sha256 `4bc09e57…80b9257a`. Its binding to the defective `plan.md` bytes stays unresolved.
- **Your "for evaluation" instruction:** it addresses the evaluation task, not this release task. I applied the release meaning of baseline adequacy: does the baseline state a lawful plan for these coordinates?

---

## Result 1: Baseline adequacy is `satisfied`, with limits

| Baseline text | Supporting clause |
|---|---|
| "Changed local member NEW belongs to a mutable successor candidate; immutable rc.2 OLD is retained." | Release Identities: "**Candidate Source** — mutable source-project state…"; "An immutable RC tag never moves." |
| "The consumer remains pinned at its declared rc.1 basis until an authorized complete explicit update binds a published successor." | "Moving the Git version-line selector does not update any consumer. Adoption is a separate explicit Product-Definition transition…" |
| "Qualification must address the unchanged installed exact candidate." | Exact-Cut Qualification binds "qualified immutable RC ref, annotated tag object, peeled commit…"; "Source success does not prove packaged or installed behavior." |
| "The successor records conserved/superseded/intentionally removed/not applicable dispositions; routes alone do not establish restatement." | STDO-UP-015: "Every predecessor claim capable of affecting the successor receives one semantic disposition"; "naming or code similarity does not prove conservation without relevant evidence." |
| "Review supplies no publication or adoption authority." | Frame scope: "This frame supplies no publishing or adoption grant"; RF-006. |

**Limits:**
- **No explicit route for NEW:** the baseline doesn't say NEW can only be published as a higher RC ("Further work increments `<n>`…"). That is implied, not stated.
- **"Restatement" is undefined:** the view doesn't define the term. The view-backed reading is "semantic disposition," and I treated it that way.
- **Predecessor not named:** the baseline doesn't name the exact predecessor immutable RC (STDO-UP-015: "A successor identifies the exact predecessor immutable RC"). From the material, I infer it is rc.2.
- **Update route not chosen:** it doesn't say whether basis-only adoption or the Complete Consumer Update applies to this consumer.

---

## Result 2: The defective subject is `falsified`

Line 1 ("Published cut rc.2 is immutable and has member hash OLD") is consistent with the material. Each of lines 2–5 is a counterexample on its own:

**D1. Identity defect.**
- **Subject text:** "keep the rc.2 identity because the tests pass"
- **Violated clauses:**
  - "Each published RC tag is immutable."
  - "Equal version text does not collapse these identities."
  - "If review requires any qualifying-byte change, the verdict remains attached to the old RC and a higher RC is published."
- **Why it fails:** NEW bytes cannot carry the rc.2 identity. Passing tests on mutable bytes is not a reason that changes identity.

**D2. Adoption defect.**
- **Subject text:** "Highest published RC discovery automatically updates all consumer definitions."
- **Violated clauses:**
  - The selector "never answers: Which exact STDO cut governs this consumer?"
  - "Moving the Git version-line selector does not update any consumer."
  - "Presentation and mutation are separate invocations"
  - "planning inside a mutating invocation … cannot authorize itself"
- **Material:** "selector discovers rc.2 without permission to alter basis."

**D3. Qualification predicate and basis defect.**
- **Subject text:** "A successful cold read of the mutable worktree qualifies the unchanged installed RC."
- **Violated clauses:**
  - Qualification binds the immutable RC ref, tag object, peeled commit, tree and subtree.
  - "Source success does not prove packaged or installed behavior."
- **RF-005 basis mismatch:** the worktree holds NEW, but the claimed subject is rc.2 = OLD.
- **Material:** "No exact rc.2 installed candidate execution is supplied. Green checks refer to current mutable local bytes."
- **Status of rc.2 qualification:** `indeterminate` on the supplied evidence, not satisfied.

**D4. Successor disposition defect.**
- **Subject text:** "The predecessor route index alone completes all successor dispositions."
- **Violated clauses:**
  - "Conservation is semantic… naming or code similarity does not prove conservation without relevant evidence."
  - "An unresolved disposition blocks qualification of the affected claim."

---

## Smallest lawful repair and owners (not performed)

1. **Rewrite `plan.md` lines 2–5** so they say:
   - rc.2 stays OLD and immutable;
   - NEW is Candidate Source, eligible for publication only as a higher RC (rc.3) under a separate publication grant;
   - the consumer stays at rc.1/`RC1` until an explicit, presented, digest-accepted adoption or complete update;
   - rc.2 qualification requires installed exact-cut evidence;
   - every predecessor claim gets a semantic disposition backed by evidence.

   **Owner:** the `plan.md` author under the Product release authority. The material doesn't name either.
2. **Supply exact rc.2 installed-candidate evidence.** Owner: the qualification evidence owner.
3. **Any change to the consumer's basis** belongs to the consumer's Product Definition owner and operator. **Acceptance** of any cut belongs to the human authority.

**Next permitted review action:** return these four falsified findings to the `plan.md` owner for repair, then re-review the repaired bytes on a fresh digest. No publication, ref update, materialization or adoption is permitted.

---

## Sufficiency, unresolved evidence and limits

- **The view alone was enough** to decide both results.
- **Unresolved:**
  - recomputing the subject digest;
  - who the Product release authority, plan owner and consumer owner are;
  - whether basis-only adoption or the Complete Consumer Update governs this consumer;
  - which predecessor claims are actually affected.
- **Limits:** the identities are symbolic fixtures. This result covers this subject and frame only, not whether the method works in general.
