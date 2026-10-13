# Integration review: 875a56e vs. preimage 5b4aebb (consumer changes against the Foundations core)

**Coverage.** I read COMMON, then the CORE sections provided (Result algebra, Result conjunction, Workspace and context, Bounded construction, Configuration, Core contract derivations), then the six changed files with their 15-line boundary context. I did not see the following, so nothing about them is asserted: FOUNDATIONS outside those sections (including the F1–F6 statements), TRANSFORMATION_LIBRARY, the frame files, SPEC_METHOD, the predecessor claims table, or the rest of each changed file. This is a source check only. It is not member acceptance and not approval of the port-review policy.

**Core as producer.** As far as I checked, the provided core sections meet Single Result Algebra items 3–6: the effect join is total over disjoint parts, the verdict precedence never raises standing, and performance stays separate from verdict. I found no core defect. All findings below are at consumer joins.

## Findings

### 1. Result handoffs drop record coordinates (wrong result map, recovery defect)

**a. `plugins/spec/skills/stdo-work/SKILL.md`**, the paragraph added before `## Classify From The Available Evidence` (its owning heading is outside the context provided):

> "use the original domain outcome with the core result, performance, effect observations and unresolved coverage"

- Because performance is listed separately, "core result" reads as the verdict alone.
- The list leaves out the predicate, the exact subject and basis, the evidence, and the reason qualifying the original outcome.
- The core requires these. Result algebra says: "Every result projection preserves these coordinates and the original predicate." It also says "A refined value is the pair of original domain outcome and cause…", and "a consumer cannot guess from a word such as `refused`".

**Counterexample.** A worker returns `refused` / falsified / performed / not_started, with no reason given.
- The handoff cannot show whether the falsified predicate is the admission predicate or the bound predicate P. The core forbids silently substituting one for the other.
- The handoff also cannot show that the reason is missing. A missing reason requires indeterminate.

**Repair.** Replace the clause with: "carry the complete core result record: predicate, exact subject and basis, verdict, performance, original domain outcome with its reason or explicit missing reason, evidence, effect observations and unresolved coverage."

**b. `standards/POSTING_GUIDE.md` § Boundary:**

> "report any judgment through the core result, with its predicate, evidence and limits"

This omits subject and basis, performance, and effect observations, yet the rule applies to a "handoff" post.

**Counterexample.** A deploy's acknowledgment is lost. The handoff post reports "deployment applied: indeterminate" with evidence but no effect coordinate. The receiving actor cannot see `unknown` and retries a non-idempotent deploy. Workspace and context requires reconciling uncertain effects before repeating an operation.

**Repair.** Replace "with its predicate, evidence and limits" with "as the complete core record, including its subject and basis, performance and effect observations."

### 2. "Current" acquisition can rebind the basis (authority/basis defect)

**`SKILL.md`, same paragraph:**

> "Acquire the current workspace and authoritative inputs before relying on a retained summary."

This sits a few lines after "Select only available material in the verified basis … a mutable candidate is no fallback." The core says acquisition observes "the subject and basis the activation actually binds, including frozen snapshots where selected … does not silently select a different basis."

**Counterexample.** An activation is bound to a published cut, while the working tree holds a later mutable candidate. The new sentence directs the actor to acquire the mutable candidate, which contradicts the preceding rule.

**Repair.** "Acquire the bound subject and basis, from the workspace, its selected snapshot and authoritative inputs, before relying on a retained summary."

**`POSTING_GUIDE.md` § Boundary** has the same issue in milder form: "to its current subject". A review of a fixed commit (such as this candidate) that is posted after the branch moves would re-observe HEAD. **Repair:** replace with "its bound subject and basis".

### 3. Glossary route resolution: a second answer on ambiguity, and an unmapped refinement

**a. Contradiction with `## Index Contract`.** The new `## Acquisition use` section says:

> "A stale or ambiguous route leaves the term unresolved."

The Index Contract says repeated spellings are intentional and that "Resolution follows `SPEC_METHOD.md#bounded-context-semantic-resolution`".

**Counterexample.** A spelling is indexed under two bounded contexts, and the occurrence's governed scope selects one under SPEC_METHOD.
- The new sentence stops at "unresolved".
- The Index Contract resolves it.

Two loci now answer the same question, which Single Ownership item 7 forbids.

**Repair.** "A stale route, or an ambiguity that `SPEC_METHOD.md#bounded-context-semantic-resolution` leaves unresolved for the occurrence, leaves the term unresolved."

**b. Refinement with no map.** "retaining the original locator outcome" declares a domain refinement, but supplies no total map. The core requires "a total, reason-sensitive map" (Common SRA item 2). The Index Contract's "invalid" and the new "stale", "ambiguous" and "unresolved" have no mapped verdicts.

**Counterexample.** An owner anchor is not found in a sparse checkout. The reader maps "not found" to falsified. The core says absence from a partial projection is not evidence of absence, so the verdict must be indeterminate.

**Repair** (one sentence), for the route-resolution predicate:

| Locator outcome | Verdict |
|---|---|
| Resolved in the selected complete basis | `satisfied` |
| Owner or context established absent in the complete bound basis (the row is invalid) | `falsified` |
| Undecided, including partial acquisition or unresolved ambiguity | `indeterminate` |
| Basis unselected or unverified | `invalid_basis` |

### 4. Writing guide permits deletion without a UP-015 disposition (lost predecessor obligation)

**`standards/WRITING_GUIDE.md` § Practical Layer Checks.** The new paragraph says "F2 and F4 require preserved interpretation and obligations". Three lines later the existing text still says:

> "If any answer is wrong, rewrite or delete."

The preceding section also says "remove stale law" and "cut it".

**Counterexample.** During successor restatement, a writer judges a predecessor determination non-derivable and deletes it. No disposition row exists, and no Product authority gave a reason. This violates the Successor Disposition Requirement and Standalone Successor relationship 3.

The deletion text is pre-existing context, but the change created the join and left it unreconciled.

**Repair.** Append: "Deleting a predecessor or conserved determination requires its recorded STDO-UP-015 disposition under its owning authority."

### 5. Glossary choice attributed to an owner that owns nothing (ownership)

**`GLOSSARY_GUIDE.md` § Acquisition use:**

> "The index supplies routes as a packaging choice."

Single Ownership item 2 says guides own glossary conventions and packaging owns no method determination. Foundation-to-law item 1 requires choices to be listed with their owners, so this sentence names the wrong owner. The Writing guide gets this right ("its own conventions").

**Repair.** "as this guide's glossary convention."

## Not established by the provided material (check before relying on it)

- **Frame carriage claim.** `SKILL.md` asserts that the work/recovery and triage frames "carry the workspace/context contract and core result algebra". The frames are not in the diff, and the preimage README phrase "own … result algebras" suggests the frames were written before unification.
  - If the frame copies do not name `FOUNDATIONS.md#result-algebra` and `#workspace-and-context` as owners and match them, the sentence is false and SRA item 7 fails.
  - The constitutional-derivation route, which handles typed handoffs that return results, is not covered by the claim.
- **Dual ownership of Conjoin and Acquire.** The standards README now says Foundations owns result conjunction and workspace-derived context, while the Transformation Library "supplies … Acquire … Conjoin". SRA item 6 and SO item 7 require the library's families to refer to or refine the Foundations sections, not to state their own aggregation or acquisition rules. Not visible here.
- **Removed category.** The standards README dropped "explanatory account". If a member still fits only that category, it is now unclassified. Not visible here.
- **F-numbers.** The F-numbers in the guides (F1 purpose, F2 interpretation/evidence, F3 identity/basis, F4 relations, F5 bounds, F6 authority) match the core derivations table. FOUNDATIONS' own numbering was not provided.

## No defect found

- Root `README.md`: "refinements of the single result algebra".
- `standards/README.md` ownership sentence: its anchors match the core headings.
- Glossary capitalization fix.
- Writing guide's byte-limit sentence: consistent with Bounded Transitions item 3.
- SKILL's three-predicate separation of availability, fitness and acceptance.
