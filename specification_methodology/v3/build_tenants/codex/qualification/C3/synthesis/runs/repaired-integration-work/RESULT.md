# Integration review: candidate 9982ab80 against preimage 875a56e3

## Coverage

- **Read in full:** COMMON, plus the four core sections Result algebra, Result conjunction, Workspace and context, Bounded construction and Configuration, and the derivations table.
- **Read partially:** the consumer members, only through the diff hunks and their roughly 15 lines of context.
- **Not seen:** the rest of each member. That includes any other place where the Build-Tenant Binding items 4 and 6 (authority, independence, failure and recovery evidence, and the categorical demonstration standard) might be carried. Section headings outside the hunks are located by their neighbouring headings.
- **Not covered:** this is not a per-member acceptance and not approval of the source-port policy.

## Findings, by severity

### 1. A lawful reject can satisfy a closure conjunct (TICKET_METHOD.md, `### Condition-Based Closure And Reuse`)

**What changed.** The text now reads "including every required judgment and owner ruling as a required conjunct". The core defines a decision result's predicate as "disposition D … was made under mandate M". It also states that a lawful rejection can satisfy that predicate.

**Counterexample.**
1. Closure requires an owner acceptance ruling.
2. The owner lawfully records `reject`.
3. The ruling's own result is `satisfied`, because the reject was lawfully made.
4. It enters the conjunction as the required conjunct and contributes `satisfied`.
5. The closure conjunction can therefore be `satisfied`, and `completed` (Minimum status model) becomes reachable on a rejection.

The preimage only bound rulings before conjoining. It did not admit their results as conjuncts. This change opened the path.

**Smallest repair.** Add: "…each required owner ruling enters as the predicate that the disposition closure requires was made on this subject and basis under its mandate; a ruling of another disposition does not satisfy that conjunct."

### 2. The admission map is partial, and an override-only `admitted` state has no result (TICKET_METHOD.md, admission section before `### Execution And Verification Authority Separation`)

**What changed.** "`admitted` maps to `satisfied` when the admission evaluation establishes that predicate" now has no "otherwise" branch. The core requires a total, reason-sensitive map. The new override paragraph says the override "leaves the admission evaluation's verdict intact". That wording presupposes an evaluation exists. However, the context line "without deterministic admission **or** explicit human override" allows an override in place of an evaluation.

**Counterexample.**
- A contract is set to `admitted` by override with no evaluation. Frame assembly and closure read `admitted`, but no admission result exists.
- The opposite case also breaks: an override follows a `rejected`/falsified evaluation. A consumer keyed on carrier state still sees `admitted`.

**Smallest repair.** Add: "Otherwise, including an override-only `admitted` state, the admission predicate keeps its evaluated result or, with none, remains an absent slot with its known performance; the override's decision result alone carries the authority."

### 3. The qualification map is partial, and the performance field is binary (RELEASE_METHOD.md, qualification section before `## Monotonic Version-Line Advancement`)

**What changed.**
- "A passed item maps to `satisfied` only with established performance …" excludes skipped or cached-green "passed" items. It does not say where they map, so the map is not total.
- The context line "whether the item was actually performed" offers a binary choice. The core has three performance values, and "Unconfirmed … stays unconfirmed".

**Counterexample.** A CI item reports `passed` from a cache on a different cut.
- It has no mapped verdict.
- Its performance must be recorded either as performed, which invents execution, or as not performed, which invents non-performance.

**Smallest repair.**
- Add: "otherwise a passed label maps to `indeterminate`".
- Change "whether the item was actually performed" to "its performance (`performed`, `not_performed` or `unconfirmed`)".

### 4. The calculus reuse condition is weaker than COMMON (SPEC_METHOD.md, `### WHAT, HOW, And Work Carriers`)

**What changed.** COMMON Build-Tenant item 5 says a calculus may be reused "where the bindings satisfy **its laws**". The candidate says "wherever its bindings satisfy the common obligations". The candidate also drops the item's second sentence: "A different language, tool or team does not by itself require a different calculus."

**Counterexample.** A calculus declares an idempotent-retry law. It is reused on an at-least-once queue binding that happens to meet the common obligations for the current task but violates that law. The candidate permits the reuse, and COMMON does not.

**Smallest repair.** "…reused across tenants and execution environments where its bindings satisfy its laws and the common obligations; a different language, tool or team does not by itself require a different calculus."

### 5. The author ≠ actor distinction is lost (same heading as finding 4)

**What changed.** COMMON item 2 says: "Author identity, actor identity and operation kind remain distinct". The candidate says only that the two identities "do not determine operation kind". It no longer states that author and actor are distinct from each other. That distinction is material to the UP-007 authorship-based independence test.

**Counterexample.** A reviewer executed a procedure that someone else authored. Without the distinction, nothing stops that reviewer being treated as the procedure's author, which would wrongly disqualify the review. The reverse error is also open: a performer could be treated as independent of an author they are.

**Smallest repair.** "Author identity, actor identity and operation kind remain distinct; a person performing a procedure is not thereby making a human adjudication."

### 6. Attention now needs units (same heading, design-admission paragraph)

**What changed.** The words "state their units" now apply to "attention". COMMON Bounded Transitions item 3 treats attention adequacy as an evaluation from actual-use evidence that "establishes no universal attention score". COMMON Build-Tenant item 3's measured list does not include attention.

The verb "measured" was already in the preimage. This change makes it a units obligation.

**Counterexample.** A human-process binding where attention is material must now declare a unit for attention. COMMON does not ask for one.

**Smallest repair.** Remove "attention" from the measured list. Add: "attention adequacy is evaluated by actual-use evidence."

### 7. Low: an incomplete rename leaves the authority direction narrower (SPEC_METHOD.md, `## Renewal Path`)

**What changed.** The chain was renamed to "realisation", but the unchanged context line still says "requirements plus design govern **code**". Under a human-procedure binding, the "full direction of authority" sentence therefore names no governed realisation.

**Smallest repair.** Change "govern code" to "govern realisation".

## Checked, no defect found

- **SPEC_METHOD `### Proportional Disposition`:**
  - The (remedy, cause) → verdict refinement is total once the prose rows and the missing-cause rule are included.
  - Requirement coherence is an admission condition and alignment is an evaluated relation. This matches the core's admission/join roles.
  - Separating a proof defect from an implementation defect does not raise standing.
  - The decision result stays separate from the assessment result.
- **SPEC_METHOD intake events sentence:** it is consistent with the core effect, supersession and empty-log rules.
- **Change-class renames:** they conserve their code coverage under "implementation".
- **TICKET status, withdrawn/deferred retention:** consistent. `completed` remains gated by closure.
- **RELEASE "skipped required item remains visible":** consistent with the core absent-slot rule.
