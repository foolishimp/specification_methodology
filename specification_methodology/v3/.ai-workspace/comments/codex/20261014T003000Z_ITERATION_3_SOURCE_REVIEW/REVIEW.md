# STDO v3 Iteration 3: Bounded Source-Conservation Review (3ad1fca → b99ca785)

All material was supplied inline, so no tool calls were needed.

## Overall bounded verdict

**Conservation is not established. Repair is needed before acceptance.**

- **What holds:** Most consumer rewrites conserve their clauses. They do so by referencing a complete shared owner (Contract application, Faithful projection, Workspace and context, the core result and conjunction laws) together with a concrete domain binding.
- **No inventions found:** No change invents authority, manufactures success, turns unknown into freedom, or imposes universal atomicity.
- **Defects found:** Six findings show material inconsistency. They are lost domain triggers, circular refinement ownership, and new unconditional obligations. Four lower-severity findings follow.
- **No acceptance granted:** This review grants no actor or release acceptance.

## Findings

### 1. Medium: UP-021 trust-boundary revalidation is folded into a change-based rule

**Location:** `SPEC_METHOD.md`, Complete Enclosing-Relation Admission.

**What was removed:**
- "an actual trust boundary trigger[s] the applicable validation before reliance or effect"
- "an unsupported assertion of prior success is not such a fact"
- "Caller or owner assertions … do not establish truth"

**What replaced it:** "Apply Currentness to established facts, including … actual trust boundaries."

**Why this does not conserve the clause:**
- The shared Currentness condition is change-based. It says "a previously satisfied check can be reused on supported unchanged premises."
- Crossing a trust boundary is a position, not a change. Currentness has no trust-boundary trigger, so the reference does not carry the old duty.
- Conjunction authentication against the producer is not content revalidation.

**Counterexample:** An untrusted caller passes a fact saying "enclosing relation validated" to the admission owner. Nothing has changed since it was produced. Currentness permits reuse. The old text required validation at that boundary before effect.

**Minimal repair:** Restore this sentence as a domain trigger: "Material mutation, rollback, changed authority or basis, expired validity, and crossing an actual trust boundary each require the applicable validation before reliance or effect; an unsupported assertion of prior success is not an established fact."

### 2. Medium: Domain refinement maps were deleted and deferred to the core, but the core assigns the map back to the domain

**Locations:**
- `TICKET_METHOD.md`, execution-contract admission
- `AXIOMATIC_CALCULUS.md` AC-007
- `RELEASE_METHOD.md`, qualification items (a lesser instance)

**What the shared law requires:** Under Foundations Result algebra, a domain refinement must supply "a total, reason-sensitive map" with "a declared reason domain". The library's Foundational contract says "the instance owns … their total refinement."

**What the consumers now do:**
- **TICKET** removed the admitted, rejected, missing-evidence, missing-scope and unusable-coordinate mapping. It now says "the core law decides verdict." That is circular: the core sends the decision back to the domain, and the domain sends it to the core.
- **AC-007** deleted its five-row constraint-outcome table. The text now says "Finer outcomes use the following reason-sensitive mapping…". In the supplied context, what follows is the outcome-shorthand paragraph, not a mapping. The reference dangles unless a later table exists, which I could not see.

**Counterexample:** A ticket admission returns `rejected(reason="criteria not met by draft")`. Under the old text this mapped to `falsified` as a demonstrated violation. The new text declares no reason domain, so a consumer must guess between `falsified` and `indeterminate`. The core forbids exactly that guess.

**Minimal repair:** Restore each domain's reason domain and its total map. One line per case is enough, citing the core legal pairs.

### 3. Medium: AC-017 now requires latitude to be retained unconditionally, which contradicts admitted loss

**Location:** `AXIOMATIC_CALCULUS.md` AC-017, new final paragraph.

**The new rule:** "Where the source permits distinct implementations, the model must retain that latitude."

**What it conflicts with:**
- AC-017's own permitted `omitted` disposition with recorded basis and authority
- Foundations, where the governing contract "selects admissible loss"
- Faithful projection's admitted approximation

**Counterexample:** A deployment-specific interpretation lawfully records the alternative implementations as `omitted` under authority. The new paragraph fails its fidelity relation anyway.

**Secondary issue:** "acquires the actual material subject … under the Frame Method" makes Frame Method a dependency of every a_c consumer. Frame Method has its own separate applicability.

**Minimal repair:**
- Qualify the rule: "…latitude material to the declared use, unless the interpretation contract records an admitted loss with basis and authority."
- Change the secondary clause to "under the applicable acquisition owner."

### 4. Medium (depends on unsupplied §3/§4 body): Design policies hardened from conditional or preferred into unconditional

**Location:** `DESIGN_MODULE_METHOD.md`, the new paragraph before §4A, plus §8 and §14A.

**What changed:**
- Several items were moved out of the 14A checklist. Under the old text, that checklist applied only "when a project claims functional bias…". The moved items are:
  - purity
  - placing time, UUID minting, environment, filesystem and network reads, and global registries at ingress or effect boundaries
  - ratified defaults
  - dependency direction
  - layering
- They now sit in indicative, unconditional §4 text.
- §9 and §11 "should" and "preferred" are now stated as fact.
- §8 changed "should avoid" to "violate that policy."
- §14A still says a claim "selects the realization policies in section 14", but the policies have moved out of §14.

**Counterexample:** A boundary that makes no functional-realization claim reads configuration inside a semantic helper.
- **Old text:** at most a §9 "should" applied.
- **New text:** it is a policy violation and blocks a design-conformance claim, through the §14 rule that a missing answer blocks the claim.

**Minimal repair:** Restore the conditional "where a functional-realization claim is made" on the moved paragraph, and keep the original modal strength. Alternatively, cite the §4 text showing these were already unconditional.

### 5. Medium: The Consistency Gate's universal scope was narrowed

**Location:** `SPEC_METHOD.md` Consistency Gate Rule.

**What changed:** The old text said "No gate may close while the affected active surfaces are internally inconsistent." The new text says "Closure of a declared change span…". No shared owner restores the universal rule.

**Counterexample:** A promotion or slice-acceptance gate that is not change-span closure closes over contradictory upstream and downstream surfaces. The old text forbade this. The new text is silent.

**Minimal repair:** Re-add the universal sentence ahead of the change-span binding.

### 6. Low–Medium: RF-017 was repurposed from compressing declarations to projecting views

**Location:** `REFERENCE_FRAME_METHOD.md` RF-017.

**What changed:**
- The old lawfulness criterion governed compressing accumulated practice into a frame *declaration*. It required preserving distinctions and failure detections for the whole evaluation *family*.
- The new text governs a *view* of the declaration for a single `Q`. The declaration is now the authoritative source, so its own compression is unchecked.
- The retained paragraph ("Compression does not require a unique smallest frame…") still talks about frames, so its referent has no criterion.

**Counterexample:** A rewritten declaration drops a failure detection needed by a sibling evaluation in the family. RF-017 no longer catches it. RF-003 catches it only if the detection is a "material relation".

**Minimal repair:** Restore the declaration-level sentence alongside the view binding.

### 7. Low: RF-004's anti-expansion safeguard was lost

**Location:** `REFERENCE_FRAME_METHOD.md` RF-004.

**What was dropped:** "A frame does not expand merely because adjacent workspace material exists."

**What changed:** The exclusion predicate moved from "cannot affect" to "established irrelevant". Read together with the Support condition's "inspect through an affected seam…", this invites loading adjacent material until irrelevance is proven.

**Repair:** Restore the dropped sentence.

### 8. Low: The Baseline real-path rule that a snapshot does not replace the current subject was dropped

**Location:** `STDO_REFERENCE_FRAME_BASELINE.md`, the real-path list, item 4.

**The problem:** Workspace and context explicitly admits "frozen snapshots where selected." The real-path domain restriction was stricter and is now gone.

**Counterexample:** A harness binds a pre-step snapshot as op-3's subject and still claims the ordinary path.

**Repair:** Restore the sentence.

### 9. Low: ODD A4a lost its "only" restriction on `evaluate_action`

**Location:** `ODD_METHOD.md`, A4a and the function table.

**The gap:**
- The new failure rule covers only operations "reserved to another row".
- Admitting a ConstructionIntent belongs to ABG, not to any row.
- The `evaluate_action` row, unlike the other three rows, carries no "does not admit construction intent or invoke work" prohibition.

**Counterexample:** `evaluate_action` admits a ConstructionIntent while deciding `retry`.

**Repair:** Add that prohibition to the `evaluate_action` row.

### 10. Low: Design 14A applies ODD obligations outside ODD's scope

**Location:** `DESIGN_MODULE_METHOD.md` §14A.

**The problem:** "A graph-native boundary additionally uses ODD's supported real authority-path proof." Graph-native does not mean ODD-adopted. This conflicts with the Governing Relations statement that "ODD alignment … retain[s] [its] declared adoption scopes."

**Repair:** Change the wording to "an ODD-governed boundary."

## Old entry defects

**Whether the three old entry defects are corrected cannot be established from the supplied material.**

- **Missing evidence:** Neither the defect enumeration nor the old entry bodies were supplied. Only the current `a_c/README.md` and `stdo-work/SKILL.md` are present.
- **What the current entries show:**
  - `a_c/README.md` selects iteration 3 as current. It explicitly does not select or regrade iteration 2 or the six-clause construction.
  - `SKILL.md`'s "Acquire The Responsibility Frame" anchor matches the library link. The skill disclaims view sufficiency and mutable-candidate fallback.
  - The authority-compressions README changed Foundations and the library from "non-deciding explanations" to owners of shared deciding contracts, which is consistent with Foundations.
- **Open item:** I found no residual defect in these entries, but I cannot map them to the three defects you named.

## Source expectations evaluated

1. **Consumer decisions use shared law.** Mostly met. Finding 2 is the exception.
2. **Exact domain restrictions and exceptions survive.** Not met. See findings 1 and 5–9.
3. **No invented authority.** Met. No instance found.
4. **No manufactured success.** Met. No instance found.
5. **No unknown turned into freedom.** No instance found. Finding 1 is borderline.
6. **No universal atomicity.** Met. TRAVERSAL_OCCURRENCE_PROFILE and Release still disclaim it.
7. **No new mandatory actor or validation stage.** Not met. See findings 3, 4 and 10.
8. **Reference plus binding, not a bare route.** Not established where the target is unsupplied. See below.

**Observations (not findings):**
- Many routine handoffs now apply Faithful projection, whose text includes "Check fidelity against independently specified source decisions." This could be read as a new validation step on every handoff.
- Several consumers "apply Contract application to" an outcome predicate (UX, Identity), which blurs it with Contract application's admissibility predicate. The Result condition limits the practical impact.

## Unresolved scope (missing dependencies)

**Release Method:**
- The Release identities and Selector and consumer adoption sections are not supplied. Spec's Release Version Boundary depends on them for "the only exact operative identifier", "not part of the live project specification", and "cannot silently change a consumer selection".

**Reference Frame Method:**
- Material relation definition: needed for RF-003's five-fold criterion.
- Reference-frame tuple.
- Minimal-frame activation binding: needed for the Agentic Use packet items.
- Diagnostic order: needed for the Baseline's eight steps.

**Baseline:**
- Derived Worker Frame, Derived Reviewer Frame, Work result and Exact candidate sections. These hold the activation contents, the testing results passed to Reviewer, and the triage fields.

**ODD:**
- The constitutional equation that carries A0's explicit object chain.
- The owner sections cited by §16.
- The cold-start route.

**Traversal Occurrence Profile body:**
- Exclusion of future results from the occurrence seed.
- Resolution of the calculus derivation basis as an admission or refusal condition.
- Source-frontier identity equalities used by OP-002.

**Other members:**
- Design §3, §4 and §7 body text: needed for finding 4 and the shared-mutable-state rule.
- Spec authority chain: needed to verify the compressed flow change "Code → Events" to "Realisation → Observations".
- Spec semantic resolution: needed for the Ticket term-binding narrowing and the dropped "glossary heading / tenant placement" exclusions.
- The world-model "representation spaces / no generic translation exception" rule: its origin is unknown.
- The rest of the `stdo_compressed.md` body: whether its statements of Foundations' standing are consistent.

**General limits:**
- Untouched clauses outside these excerpts were not reviewed.
- This is not an exhaustive whole-member review.
