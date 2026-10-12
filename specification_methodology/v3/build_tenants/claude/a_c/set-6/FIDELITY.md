# Fidelity pass over the set-5 program (W27 Writer self-check)

Status: a self-check by the Writer activation that derived set-6, run
with six reviewer contexts the Writer started under one rubric. It is not
an author-independent fidelity judgment, nothing here is accepted, and
the reviewer contexts saw only packets the Writer built. Its findings are
the input to [set-6](README.md); the corrections are in that program.

## Subject and baseline

- Program checked: `a_c/set-5/axiomatic-program.json`, canonical digest
  `sha256:b12b31216456f375c2a2e24aefbd16c897d92c1a7b469b50c52ee89b450e4a42`,
  417 clauses.
- Member text: the standards at `4425993`, except TRAVERSAL_OCCURRENCE,
  whose mapping section was re-read at `188bc81` (W28, landed during this
  pass); the two TRAVERSAL mapping clauses were judged against that commit.
  ACTIVATION section 3's indeterminate case changed at `9be9f57` after the
  reviewers finished; `missing-capability-is-out-of-frame` was re-encoded
  by the Writer from that commit (README, "ACTIVATION section 3").
- Baseline for (c), locus changed: the span under each clause's cited
  heading at `3824752` (set-5's subject) against `4425993`. The set-5
  README records 193 older records under headings swept between `978d324`
  and `3824752` that were never re-derived; (c) does not count their
  staleness, but (a) and (b) compare every clause with the current text,
  so a stale older row shows there.

## Method

1. Mechanical pre-pass (script, no judgment): for each clause, the text of
   every cited heading span at both commits; whether the span changed;
   each sentence of the statement and literals tagged verbatim at the
   locus (V), verbatim elsewhere in the member (F) or not verbatim (N),
   with the best-matching member sentences for N; the qualification tags
   (P-, UP-, AC-, RF-, OP-) checked against the cited span.
2. Judged reading: the clauses were split by member into six packets (g1
   ACTIVATION; g2 REFERENCE_FRAME; g3 FOUNDATIONS, CONFORMANCE, README,
   ASSURANCE, GLOSSARY; g4 SPEC_METHOD, EVALUATION, PROFILES; g5
   AXIOMATIC_CALCULUS, EXECUTIVE_BASELINE, TICKETS, PRODUCT_DEFINITION,
   RELEASE, IDENTITY; g6 TRAVERSAL_OCCURRENCE, DESIGN_MODULE, UX,
   WORLD_MODEL, ODD), each with the changed-span diffs appended. One
   reviewer context per packet judged every clause under the rubric
   below and returned a corrected statement and literals built from member
   sentences, or a removal. `traversal-stops-and-decisions-map-to-core` was
   held out of g6 and judged by the Writer at `188bc81`.
3. Rubric. (a) claim not in member: an added restriction or exclusivity,
   invented condition, consequence or definition, an inference merged from
   two places presented as one rule, a cross-reference the member does not
   make. (b) modal or quantifier change against the member sentence
   (should, may, must, can, recommended, typical, prefer, minimum, at
   least, one or more, several, all, every, each, any, only, never,
   exactly, default; "is" or "has" for "should be"; a dropped
   unless, where, except or at-least qualifier). (c) the clause carries
   text that the change between `3824752` and `4425993` altered or removed,
   or the change added text that qualifies or contradicts it.
   Paraphrase that keeps content and force is not a defect.

| Packet | Clauses judged | Flagged | Packet SHA-256 (first 12) | Reviewer reads beyond the packet |
|---|---|---|---|---|
| g1 | 77 | 18 | `2efad9400387` | about 36 KB |
| g2 | 66 | 13 | `381259a40f80` | about 26 KB |
| g3 | 67 | 14 | `eaf1eabecd93` | about 34 KB |
| g4 | 74 | 25 | `a9ccda3a91fa` | about 19 KB |
| g5 | 83 | 23 | `e0facc575a11` | about 75 KB |
| g6 | 49 | 14 | `b8a820a623a1` | about 31 KB |
| Writer | 1 | 1 | | |
| total | 417 | 108 | | about 221 KB |

## Counts

Clauses, a clause with two kinds counted under each:

| Finding | Clauses |
|---|---|
| (a) claim the member text does not contain | 40 |
| (b) modal or quantifier strengthening or weakening | 69 |
| (c) locus text changed under the clause (judged) | 11 |
| (c) mechanical: cited span changed between `3824752` and `4425993` | 78 |
| flagged clauses, distinct | 108 |
| corrected to the member text | 106 |
| removed (the member no longer states it) | 2 |

The 78 mechanically changed spans are mostly broad headings (ACTIVATION
section 3, FOUNDATIONS section 2 and section 3, ODD section 11.5D, WORLD_MODEL
section 14); the judged (c) count is the 11 whose own content the change
touched. Of the 106 corrections, the three set-5 bootstrap clauses and the
two TRAVERSAL mapping clauses and `missing-capability-is-out-of-frame` were rewritten by the Writer rather than
taken from the reviewer fix (README, "Bootstrap" and "TRAVERSAL").

Self-check of the corrections (script, on the committed program): a
literal sentence counts as verbatim only when it occurs at the cited locus
and ends where a member sentence or clause ends (a dropped trailing
citation in parentheses is allowed). Of the literal sentences in the 105
reviewer-corrected clauses, 243 are verbatim, 7 match only part of a
member sentence (table cells and one definition row) and 98 are not
verbatim (field lists, tables and code-block lines recast as prose). The
14 clauses the Writer wrote itself (ten bootstrap clauses, the ODD
binding, the two TRAVERSAL clauses and `missing-capability-is-out-of-frame`)
were put through the same rubric by the Writer after a first version of
them spliced a SPEC_METHOD sentence onto PRODUCT_DEFINITION text, cut the
marker-span sentence short and dropped qualifiers from four statements;
those were fixed. Their literal sentences: 48 verbatim, 5 partial (the
abridged README route rows) and 8 not verbatim (the joined
PRODUCT_DEFINITION command bullets, the ACTIVATION three-case bullets and
TRAVERSAL sentences with their mid-sentence section links dropped). Three clauses had a literal sentence
verbatim only outside their cited heading; the containing heading was
added to their `source_refs`:
`binding-fields-resolve-through-stable-identities` (REFERENCE_FRAME
`#stop-and-change`), `design-decision-complete-is-the-gate-criterion`
(DESIGN_MODULE `#proportional-design-sequencing`) and
`minimal-evaluation-result-fields` (REFERENCE_FRAME
`#frame-evaluation-result`). Five symbol labels were rewritten:
`bootstrap-route` (now the member's "owning sources") and four that carried
a corrected strengthening or a stale count: `formal-fragment` (now a
hypothesis, not established), `minimal-evaluation-result` (no field
count), `scoped-identity-kind` ("should not be collapsed") and
`coverage-ledger` ("at least").

## Flagged clauses

| Clause | Locus (set-5) | Kinds | Finding | Disposition |
|---|---|---|---|---|
| `a-name-tool-or-family-triggers-no-activation` | ACTIVATION#applicability | b | Statement drops 'by itself', turning a denial of sufficiency into an absolute denial of activation. | corrected |
| `ac-013-preservation-relation-is-exact-typed-equality` | AXIOMATIC_CALCULUS#ac-013-transformation | b | Statement turns the permission 'may relate' into the assertion 'equivalence relates removed to introduced'. | corrected |
| `acceptance-binds-one-checkpoint` | ACTIVATION#5-work-state-and-restart; SPEC_METHOD#8-bounded-execution-in-this-method | a | Merges the proxy-delegation ceremony condition and its human-acceptance proviso (Roles section) into the checkpoint rule as a condition the checkpoint text does not state. | corrected |
| `acceptance-exhausts-instance-and-interval` | SPEC_METHOD#3-outcome-conservation | b | Drops 'only' (and 'declared') from the exhaustion limit and 'bounded' from the named prerequisite. | corrected |
| `attribute-ledger-is-the-immediate-source-of-a-cut` | WORLD_MODEL#attribute-ledger-law | b | Statement turns 'should be a fully qualified claim' into 'has ... fully qualified claim record'; literal turns 'one or more' into 'several'. | corrected |
| `authority-coverage-closes-only-with-owners-named` | REFERENCE_FRAME#authority-coverage | b | Statement drops 'material' twice, obliging every evaluation and every operation rather than every material one. | corrected |
| `authority-for-growth-derives-from-outcome` | SPEC_METHOD#3-outcome-conservation | b | Drops the 'Within a product-outcome-bearing work wave' scope; attaches 'exhaustion condition' to every source, member says the admitted basis states exhaustion or falsification. | corrected |
| `authority-kinds-coincide-lawfully-and-never-collapse-by-default` | FOUNDATIONS#authority-kinds | b | Statement drops 'explicitly' and the 'where the governing identity and authority law permits it' condition on acting through a proxy. | corrected |
| `baseline-roles-are-relations` | SPEC_METHOD#12-source-dispositions; SPEC_METHOD#8-bounded-execution-in-this-method | a | SPEC_METHOD never mentions UP-020; the labels name roles ACTIVATION §1 defines, catalogued in EXECUTIVE_BASELINE, not UP-020's roles. | corrected |
| `binding-fields-resolve-through-stable-identities` | REFERENCE_FRAME#minimal-activation-binding | b | 'aid navigation only' adds exclusivity, drops 'may' and 'diagnostics'; member says they may aid navigation or diagnostics but do not substitute. | corrected |
| `bootstrap-basis` | PRODUCT_DEFINITION#12-bootstrap; PRODUCT_DEFINITION#4-shared-installed-release-basis-and-toolchain-manager | a | 'Only adopt changes it' is invented: the 'only' bounds what adopt changes; cohort-update also changes the basis, and bootstrap step 5 binds it. | corrected |
| `bootstrap-discovery` | PRODUCT_DEFINITION#9-recursive-discovery-and-explicit-composition | a, c | Changed span adds exactly-one selection and fail-closed zero/several, which the clause omits; §4 pruning is stated for fleet discovery, §9 never invokes it. | corrected |
| `bootstrap-routes` | PRODUCT_DEFINITION#4-shared-installed-release-basis-and-toolchain-manager; README#routes | a | Route sequence stitches three purpose-keyed README Routes rows into one bootstrap order no member states; 'owning members' narrows 'owning sources'. | corrected |
| `carrier-is-an-admission-candidate-never-truth` | TICKETS#execution-contract-admission | b | 'should treat ... as' strengthened to 'is'. | corrected |
| `carrier-is-selected-by-proportionality` | SPEC_METHOD#carriers | a | Adds the identification '(the rc.2 run-scoped execution contract)', which the member does not make. | corrected |
| `carriers-never-widen-authority` | IDENTITY#6-authority-identity-and-conservation-stdo-up-004 | b | Statement drops 'silently' (explicit elevation is lawful by decision) and over-quantifies the listed changes as 'every change of authority'. | corrected |
| `case-names-subject-mechanism-expectation-status` | CONFORMANCE#conformance | a, b | Clause says status is recorded only by a non-author run; member says status names what exists (fixture, runs, assessment) and a run is not a pass. | corrected |
| `case-passes-without-coerced-success` | CONFORMANCE#conformance | b | Statement turns the member's sufficient condition 'passes when' into an exclusive 'passes only with'. | corrected |
| `chain-layers-narrow-ambiguity` | SPEC_METHOD#5-ambiguity-governance-and-lifecycle | a | The chain listing with 'Requirements (WHAT)', 'Design and realisation (HOW, per tenant)', 'Code or documents' is not member text. | corrected |
| `changed-inputs-invalidate-before-reliance` | ACTIVATION#7-closed-result-and-reuse | a, b | Literal preserves 'the predecessor' instead of the predecessor/successor relation; statement drops 'demonstrably' from independent surviving results. | corrected |
| `claim-scope-cannot-exceed-evidence` | EVALUATION#1-claims | b | Drops 'governing evidence' from the conjunctive requirement for generalisation, weakening it. | corrected |
| `clause-standing-is-disposed` | FOUNDATIONS#1-vocabulary-of-standing | b | Literal's 'not applicable (bounded reason)' drops the condition that the claim has no successor effect, weakening when not applicable is lawful. | corrected |
| `closed-result-reused-after-applicability-check` | ACTIVATION#7-closed-result-and-reuse | b | Requirement literal drops 'exact' from the applicability check, weakening the reuse condition. | corrected |
| `composition-is-declared-only-where-the-evaluation-requires-it` | REFERENCE_FRAME#material-composition | b | Statement drops the 'where material' qualifier on effect or decision order, making order declaration unconditional. | corrected |
| `conservation-is-semantic` | SPEC_METHOD#6-lineage-and-release | a | SPEC_METHOD §6 has no sentence on patch absence or naming/code similarity; it points successor conservation to RELEASE §9. | removed |
| `core-names-no-runtime-carrier-executor` | PROFILES#1-the-boundary | a | Lists traversal, F_D, F_P, F_H and module as excluded terms; member says they are tier-1 or generic and unrestricted; drops IACS and Prime. | corrected |
| `core-statement-names-the-method` | README#stdo-3-standards-claude-tenant-realisation | a | Member gives the core statement as the method's statement; it does not call it a reader route or map it to FOUNDATIONS/SPEC_METHOD/ACTIVATION sections. | corrected |
| `cost-categories-are-separated` | ACTIVATION#6-cost-and-proportionality | b | Drops the 'material' qualifier, widening the separation duty from material costs to all such costs. | corrected |
| `counterevidence-invalidates-dependents` | EVALUATION#1-claims | b | Narrows the end of invalidation to requalification only; drops superseded or withdrawn. | corrected |
| `coverage-dimensions-are-lenses-not-frames` | REFERENCE_FRAME#coverage-dimensions | b | Literal folds the 'Typical' dimension list into the definition of the lenses the audit applies, dropping 'Typical'. | corrected |
| `coverage-ledger-fields` | REFERENCE_FRAME#coverage-ledger | b | Statement drops 'at least', presenting the minimum field list as the complete row. | corrected |
| `design-gate-verdicts-accepted-before-promotion` | DESIGN_MODULE#gate-and-retrospective-work | b | Statement drops 'applicable' ('any failed axiom'), widening the blocking set. | corrected |
| `design-hidden-ambiguity-switches-to-gated-sequencing` | DESIGN_MODULE#proportional-design-sequencing | b | Statement says 'repeated surprises', dropping 'material' (widens the design_reframe trigger) and 'cross-cutting'. | corrected |
| `design-prime-contracts-the-whole-family-and-conserves-the-root` | DESIGN_MODULE#recursive-prime-and-root-conservation-up-003 | a | 'Prime holds only over the whole atom family' adds exclusivity; member applies contraction to each atom and then to the family. | corrected |
| `design-sequencing-mode-is-selected-by-proportionality` | DESIGN_MODULE#proportional-design-sequencing | b | 'warranted when' becomes 'warranted only where', and the reasoning-load condition is dropped. | corrected |
| `direct-entry-unless-coordination-needed` | ACTIVATION#roles-and-delegation | a, b | 'may enter' becomes 'enters'; adds exclusive 'only when'; drops capability from coordination triggers and operation grant from the entry condition. | corrected |
| `engine-and-domain-own-different-identities` | IDENTITY#5-authority-split; IDENTITY#domain-owned-identity; IDENTITY#engine-owned-identity | b, a | should optimise -> optimised; should not -> must not; should not invent -> does not; 'only transports' adds exclusivity. | corrected |
| `entity-cut-carries-its-own-discrimination` | WORLD_MODEL#discrimination | b | Statement says a cut 'says' its evidence kind (member: 'should say', scoped to where a builder can intervene); literal 'is read as such' drops 'should be'. | corrected |
| `evidence-surface-cannot-select-outcome` | SPEC_METHOD#3-outcome-conservation | b | Drops 'explicitly' from the condition under which assurance delivery counts as progress, widening it. | corrected |
| `exact-candidate-is-a-stabilised-subject-identity` | EXECUTIVE_BASELINE#exact-candidate | b | Statement generalises the 'Elsewhere' branch to every candidate and drops the frozen-before-exposure rule where method qualification applies. | corrected |
| `executive-mutates-nothing` | EXECUTIVE_BASELINE#no-mutation-while-executive | a | Statement attaches 'recorded before the effect' to every Worker or Writer relation; member states it only for a same-actor role transition. | corrected |
| `explicit-admits-three-lawful-surface-values` | WORLD_MODEL#14-results-of-this-profile; WORLD_MODEL#admissibility | a | Statement generalises the treatment-specific no-manufacture rule to every surface ('nothing is manufactured to fill it'); member states it only for adjacent-domain treatment. | corrected |
| `faithful-refinement-definition` | ACTIVATION#4-totality-and-refinement | c | The cumulative-input text the clause carries was removed; refinement is now typed composition, with earlier outputs carried only via declared adapter or specialised contract. | corrected |
| `fit-selection-within-grant` | ACTIVATION#2-context-construction-under-an-envelope | b | Statement drops the delegation proviso, making re-entry for actor change or envelope enlargement unconditional. | corrected |
| `formal-fragment-established` | FOUNDATIONS#4-algebra | c | Span now states the fragment as hypothesis H1 ('would be functors'), established by nothing and not law; clause asserts it as established new law. | corrected |
| `four-cross-context-relation-kinds-are-distinct` | PRODUCT_DEFINITION#5-bounded-context-semantic-resolution; PRODUCT_DEFINITION#6-local-constitutional-binding | b | [V] tag is a substring match; dropping 'automatically' turns 'does not by itself prove' into 'never proves'. | corrected |
| `frame-set-selection-meets-the-baseline-coverage-constraint` | REFERENCE_FRAME#frame-set-selection | b | Statement drops the 'where' condition and human authority on non-minimal sets; literal truncates 'reversibility when the set proves inadequate'. | corrected |
| `glossary-locates-and-never-decides` | GLOSSARY#1-index-contract; GLOSSARY#2-locator-law; PRODUCT_DEFINITION#5-bounded-context-semantic-resolution | b | Statement drops the alternative 'or the target context explicitly imports it', narrowing when an indexed concept applies. | corrected |
| `graph-execution-profile-bindings` | PROFILES#2-graph-execution | a, c | Work-state, closure-decision, runtime/product ownership and loop-function bindings are not in §2; changed ODD row now qualifies the graph-functions refinement with §11.8. | corrected |
| `hard-stops-regardless-of-appetite` | ACTIVATION#4-totality-and-refinement | b | Member gives a typical, non-exhaustive list ('typical ... include'); clause states these definitively as the hard stops. | corrected |
| `hypotheses-are-not-law` | FOUNDATIONS#5-hypotheses | a | 'Nothing in the core depends on any of them being established' is not in FOUNDATIONS §5; that sentence exists only in PROFILES about another construct. | corrected |
| `identity-change-is-an-explicit-relation` | IDENTITY#stability | b | 'should remain stable' -> 'stays'; 'should make explicit' -> 'is made explicit' and 'never silently reused'. | corrected |
| `identity-is-authority-kind-value` | IDENTITY#scoped-identity | a, b | 'should be interpretable' -> 'is'; statement drops 'at minimum' and invents 'never a naked string'. | corrected |
| `identity-is-unique-within-its-lawful-scope` | IDENTITY#uniqueness | a | 'not globally unique as a naked string' asserts a property; member only says global naked-string uniqueness is not required. | corrected |
| `identity-kinds-are-not-collapsed` | IDENTITY#type | b | 'should not be collapsed' strengthened to 'are not collapsed' / 'stay distinct'. | corrected |
| `independence-across-families-is-declared` | EVALUATION#3-independent-assessment | a | Substitutes 'actor family' for the member's 'model family' in the independence policy, changing its subject. | corrected |
| `intake-names-its-fields` | ACTIVATION#intake | b | Drops 'bounded' from the affected relation set and omits two listed items: transformation-admission relations and computational or common-library dispositions. | corrected |
| `inventory-is-derived-from-every-material-source-with-provenance` | REFERENCE_FRAME#evaluation-inventory | b | Statement drops 'available' and 'including where applicable', widening derivation to every material source. | corrected |
| `lineage-relation-kinds-are-typed` | TRAVERSAL_OCCURRENCE#closed-relation-families | a | Member says support is not cause by implication; for correction it says only 'does not erase its target', not 'not cause'. | corrected |
| `major-ambiguity-is-recorded-with-disposition` | SPEC_METHOD#5-ambiguity-governance-and-lifecycle | b | Widens 'each major boundary' to 'each boundary'; drops affected-boundary and decision recording. | corrected |
| `member-is-engagement-law-only` | REFERENCE_FRAME#1-the-frame-as-the-engagement-unit | b | Literal drops 'wherever the governing product or method permits them' and turns 'may import or specialise' into an indicative. | corrected |
| `method-execution-is-proportionate` | ACTIVATION#6-cost-and-proportionality | a, b | Drops 'repeated' and 'change' need, swaps activation preparation for 'activation records', drops evidence generation. | corrected |
| `minimal-evaluation-result-fields` | REFERENCE_FRAME#minimal-evaluation-result | a, b | Member shape has thirteen fields incl. out_of_frame residual; clause says twelve, omits it, and pins the result to the ACTIVATION section 3 core algebra, which this section does not state. | corrected |
| `missing-capability-is-out-of-frame` | ACTIVATION#3-result-algebra | c | Diff replaced 'only the first two are members of the algebra', which 'member of neither' restates; third case now may return a result from sufficient evaluation. | corrected |
| `mixed-bases-need-composite-relation` | FOUNDATIONS#2-ontology | a, b | Literal says a step, claim or result binds 'one exact immutable basis'; member allows a moving basis and does not say 'one'. | corrected |
| `odd-closure-decisions-map-to-core` | ODD#115d-constructive-evaluation-and-yield-loop | c | Changed span: repair now maps to falsified or indeterminate (indeterminate when the defect is in the proof); clause still says repair -> falsified. | corrected |
| `one-actor-may-hold-several-roles` | ACTIVATION#roles-and-delegation | b | Drops 'across different claims', widening the permission to several roles on any claim. | corrected |
| `one-declaration-proves-only-declare-and-audit` | EVALUATION#method-self-qualification | b | Drops 'explicitly' from the exception and 'or outcomes'; statement's 'optional comparison only' drops the exception entirely. | corrected |
| `op-005-mutable-reality-conservation` | TRAVERSAL_OCCURRENCE#op-005-mutable-reality-conservation | b | Statement drops the 'under the stable binding when authority is unchanged' condition and turns 'may describe W' into 'Records describe W'. | corrected |
| `p4a-statement` | FOUNDATIONS#3-commitments | c | Changed span added 'exact declared' to the domain the first result must satisfy; clause still carries the old unqualified 'domain'. | corrected |
| `post-exposure-revision-is-new-subject` | EVALUATION#3-independent-assessment | a | Collapses the either/or to 'a new subject'; 'exposure to the assessor' is not member text; drops the no-retroactive-pass rule. | corrected |
| `product-definition-carries-the-required-relations` | PRODUCT_DEFINITION#2-required-definition-relations | b | Drops 'any' (optional shared surfaces read as required) and 'where applicable' on context-qualified term resolution. | corrected |
| `product-definition-locates-and-never-restates-source-truth` | PRODUCT_DEFINITION#2-required-definition-relations; PRODUCT_DEFINITION#6-local-constitutional-binding | a | 'gains authority only from its named owner' adds exclusivity; member says no authority from category or listing, and the entry names its owner. | corrected |
| `product-roles-are-distinct` | SPEC_METHOD#6-lineage-and-release | a, b | 'may build' hardened to 'builds'; parenthetical role definitions are not SPEC_METHOD text (defined in FOUNDATIONS §2); substrate and product definition dropped from the roles. | corrected |
| `product-testing-frame-set-assigns-claims-not-authority` | ASSURANCE#the-set | b | Statement says labels carry no assurance value, dropping 'without the corresponding frame declaration'; also drops 'ordinary' from the four-frame configuration. | corrected |
| `progress-is-accepted-material-movement` | ACTIVATION#5-work-state-and-restart | b | Drops 'new' (not new progress) and 'by themselves' (volume not progress by themselves), strengthening both negations. | corrected |
| `promotion-constraint-projection` | EXECUTIVE_BASELINE#promotion-constraint-projection | b | Statement drops the alternative 'or indeterminate is kept', asserting re-evaluation always follows. | corrected |
| `proportionality-definition` | ACTIVATION#6-cost-and-proportionality | a | Member's subject is a method obligation; clause extends the justification rule to distinctions, carriers and documents, which the member does not state. | corrected |
| `reference-conserves-under-conditions` | FOUNDATIONS#4-algebra | b | Member gives a sufficient condition ('when'); clause makes it exclusive ('only when', 'Only then', 'otherwise') and adds 'as the body'. | corrected |
| `release-cut-binds-its-project-subtree` | RELEASE#project-subtree-release-identity | b | Drops 'Unrelated', extending the carrier-state rule to all sibling bytes. | corrected |
| `release-identities-are-distinct` | RELEASE#2-release-identities | b | Statement turns 'may move' into the assertion 'branches and the selector move'. | corrected |
| `release-mechanics-by-reference` | SPEC_METHOD#6-lineage-and-release | a | Names rc.2 RELEASE_METHOD as the by-reference owner; member assigns release mechanics to RELEASE §2 to §8, with RELEASE_METHOD only as provenance. | corrected |
| `release-rc-publication-creates-one-immutable-subject` | RELEASE#immutable-rc-publication | b | Step 7 drops 'in a shared release source', imposing qualified tags on single-project sources that may keep the unqualified profile. | corrected |
| `release-selector-never-selects-a-consumer-basis` | RELEASE#4-selector-and-consumer-adoption | a | Statement 'changes only by explicit adoption' adds exclusivity RELEASE §4 does not state; cohort-update and bootstrap also set the basis. | corrected |
| `restart-must-be-argued` | ACTIVATION#5-work-state-and-restart | b | Statement turns 'may retain' into 'is preserved'; literal drops 'or unaccepted' and 'exact operation' from the grant. | corrected |
| `review-recommends-not-applies` | EVALUATION#4-review-results | b | 'may recommend' hardened to 'recommends'; drops that the recommendation is evidence only, never a disposition. | corrected |
| `revision-reopens-every-result-bound-to-the-prior-revision` | REFERENCE_FRAME#revision-actions | b | Drops 'material' throughout; member says a non-material revision produces no new coordinate and reopens no result. | corrected |
| `rf-005-every-result-binds-exact-basis-and-coordinates` | REFERENCE_FRAME#rf-005-exact-basis-and-coordinates | b | Statement drops the 'or requires reactivation' alternative, making invalid_basis the only lawful response. | corrected |
| `rf-011-topology-mutation-forces-reevaluation-before-reuse` | REFERENCE_FRAME#rf-011-topology-mutation-and-recharting | b | Statement and literal drop 'material' from the mutation and from frame revision, widening invalidation to non-material changes. | corrected |
| `rf-012-every-evaluation-returns-an-algebra-member` | REFERENCE_FRAME#rf-012-closed-results | b | Clause omits the member's qualifier: an unperformed evaluation owes the step's stop state, not an algebra member. | corrected |
| `saturation-forbids-silent-unsupported-attributes` | WORLD_MODEL#saturation-law | b | Member defines sufficient saturation; statement makes traceable support and explicit gaps unconditional 'need'/'must', though sparse first publication remains lawful. | corrected |
| `silent-omission-is-never-a-fit-option` | ACTIVATION#2-context-construction-under-an-envelope | a | Literal adds 'of required material', narrowing the prohibition the member states for any silent omission to fit. | corrected |
| `software-design-profile-bindings` | PROFILES#3-software-design | a | Member says the derivation-chain cost is decided in DESIGN_MODULE and DESIGN_MODULE_METHOD is restated in full there; not a residual, not conserved by reference. | corrected |
| `step-4-non-candidate-variants-are-not-progress` | EXECUTIVE_BASELINE#4-executive-evaluates-the-work-result | b | Statement drops 'because work occurred', turning a bar on counting effort as progress into an absolute 'never accepted progress'. | corrected |
| `structural-refusal-and-partial-effect-losses` | TRAVERSAL_OCCURRENCE#closed-constraint-judgment-residual-and-stop-kinds | c | Changed span removed 'Falsified for partial and partial_effect ...'; these now map to falsified or indeterminate, and the clause's 'falsified member' wording is stale. | corrected |
| `successor-disposes-every-predecessor-claim` | SPEC_METHOD#6-lineage-and-release | a | SPEC_METHOD §6 states no disposition or blocking rule; it points to RELEASE §9, which owns successor baseline conservation. | removed |
| `tenant-never-patches-what-or-peer` | SPEC_METHOD#11-governance-of-tenants-in-this-source-project | a | States an imported, non-method rule as method law; 'returns to the WHAT's pen' and 'never patches' are not member text; drops 'only'. | corrected |
| `testing-evidence-stays-claim-bound` | ASSURANCE#10-testing-evidence-composition | b | Literal states the four proof responsibilities as absolute; member qualifies them as default proof responsibilities. | corrected |
| `traversal-stops-and-decisions-map-to-core` | TRAVERSAL_OCCURRENCE#closed-constraint-judgment-residual-and-stop-kinds | c, a | Judged by the Writer against 188bc81, not in a packet. The partial_effect and partial rows changed before 4425993 (falsified or indeterminate by the effect evidence) and W28 changed refusal: falsified unless refuse_invalid_basis or an invalid_basis decision; the clause still mapped a structural refusal to invalid_basis. | corrected |
| `undisposed-rc2-obligation-blocks-qualification` | FOUNDATIONS#1-vocabulary-of-standing | a | Member says an unresolved disposition blocks qualification of the affected claim; clause widens the block to qualification of the whole corpus. | corrected |
| `unexercised-declared-capability-yields-no-evaluation-result` | ACTIVATION#3-result-algebra | c | Removed: 'yields no result at all; unresolved, not out of frame and not indeterminate'. Now a result returns where sufficient evaluation exists; unexercised part stays an uncovered obligation. | corrected |
| `ux-msg-replay-proof-before-closure` | UX#msg-replay-proof | b | Statement makes all six parts unconditional, dropping the no-effect proof allowed for projection-only surfaces; 'at least one' becomes 'an'. | corrected |
| `ux-profile-bindings` | PROFILES#4-ux | a | Carries the withdrawn first-pass description; UX_METHOD is restated in full in UX, not conserved by reference. | corrected |
| `weaker-property-is-no-substitute` | EVALUATION#1-claims | b | Drops 'release' from the protected claim kinds, narrowing the rule's scope. | corrected |
| `work-result-variants-map-totally-to-core` | EXECUTIVE_BASELINE#work-result | b | Drops 'or declared result carrier', making the assigning authority the sole return; drops 'after lawful activation' from the totality claim. | corrected |
| `work-wave-names-one-outcome` | SPEC_METHOD#3-outcome-conservation | b | Adds 'only' to how progress is judged and drops 'explicitly selected' and 'product-defined'; regression blocks promotion, not the path generally. | corrected |
| `world-model-profile-bindings` | PROFILES#5-world-model | a | Member restates WORLD_MODEL_METHOD in full in WORLD_MODEL; 'conserved by reference' is not stated. | corrected |
| `world-model-verdicts-map-to-core` | WORLD_MODEL#14-results-of-this-profile | c | Changed span adds the inconclusive-verification verdict (-> indeterminate); the clause's enumerated total mapping omits it. Inserted row cells are verbatim. | corrected |

## Mechanical findings not corrected

Qualification literals naming a tag that the cited span does not contain
("file": the tag occurs elsewhere in the same member; "absent": nowhere in
it). Qualification literals are the encoder's attribution, not member
claims; these are recorded and left for the fidelity judge.

| Clause | Qualification | Tags not in the cited span |
|---|---|---|
| `baseline-roles-are-relations` | UP-020 is conserved; the baseline's Executive, Worker and Reviewer are conserved by reference as labels for UP-020's rol | UP-020 (absent) |
| `binding-fields-resolve-through-stable-identities` | P3 | P3 (file) |
| `closure-conditions-for-operating-under-the-member` | P0 to P6 | P0 (file), P6 (file) |
| `core-statement-names-the-method` | The core statement is the one-sentence route into the method: interpretation (FOUNDATIONS P1), purpose and contract (P2, | P1 (absent), P4a (absent), P4b (absent) |
| `frame-violations-enumerated` | P0 to P6; RF-001, RF-005, RF-006, RF-008 to RF-012, RF-014, RF-016, RF-017 | P6 (file) |
| `intake-triage-makes-six-determinations` | P2, P6, P4b | P4b (file) |
| `minimal-evaluation-result-fields` | P0, P2; RF-016 | P0 (file), P2 (file), RF-016 (file) |
| `minimal-frame-set-declaration-sections` | P0, P2; RF-016 | P0 (file), P2 (file), RF-016 (file) |
| `release-mechanics-by-reference` | Release identities, phases, naming, cohorts and publication follow RELEASE_METHOD by reference and are not restated; lay | AC-020 (file) |

Clauses whose cited span changed between `3824752` and `4425993`
(mechanical, before judgment): `activation-binds-the-declaration-and-loads-the-packet`, `algorithmic-means-structurally-checkable`, `ambiguity-carried-decided-or-escalated`, `ambiguity-outcome-is-policy-over-core`, `bootstrap-discovery`, `closure-is-computed-on-exact-basis`, `composite-reports-by-declared-conjunction`, `composition-exists-only-under-p4a`, `composition-law-only-where-needed`, `compression-preservation-is-a-claim`, `construction-availability-maps-to-core`, `context-fit-is-measured-before-read`, `core-algebra-conserves-rf012-and-ac007`, `coupled-relations-fit-together`, `disposition-consumes-a-core-result`, `dispositions-named-in-advance`, `evaluator-applies-the-frame-and-records-assumptions`, `evidence-and-authority-do-not-mint-each-other`, `explicit-admits-three-lawful-surface-values`, `failure-and-uncovered-obligation-survive-join`, `faithful-refinement-definition`, `fit-selection-within-grant`, `fit-test-against-envelope`, `formal-fragment-established`, `glossary-locates-and-never-decides`, `graph-execution-profile-bindings`, `hard-stops-regardless-of-appetite`, `indeterminate-result-names-the-deciding-evidence`, `inputs-acquired-by-exact-identity`, `latitude-must-be-declared`, `lawful-compression-preserves-distinctions`, `material-means-can-alter`, `missing-capability-is-out-of-frame`, `no-capable-pairing-returns-refusal-or-out-of-frame`, `no-proof-of-no-undiscovered-relation`, `nothing-is-coerced-to-success`, `obligation-without-route-is-unjustified`, `odd-closure-decision-is-a-closed-sum-type`, `odd-closure-decisions-map-to-core`, `odd-yield-is-lawful-iterate-not-failure`, `out-of-frame-result-names-the-missing-declaration`, `outcome-defines-adequacy`, `p0-statement`, `p1-statement`, `p2-statement`, `p3-statement`, `p4a-statement`, `p4b-derivation`, `p5-derivation`, `p6-statement`, `premise-actor-change`, `premise-candidate-until-evaluated`, `premise-open-world`, `premise-selected-outcome`, `profile-closure-declares-mapping`, `profile-imports-core-by-reference`, `projection-cannot-trim-required-member`, `projection-records-boundary`, `reconfiguration-follows-the-cause`, `reference-conserves-under-conditions`, `refinement-generalises-graph-functions`, `refinement-premises-are-not-conclusions`, `refinements-map-totally-to-core`, `result-algebra-has-five-members`, `seam-includes-far-side`, `shared-machinery-is-not-identity`, `silent-omission-is-never-a-fit-option`, `step-produced-facts-are-not-reacquirable`, `structural-refusal-and-partial-effect-losses`, `total-handling-claims-no-omniscience`, `transformation-records-accounting`, `transition-admission-is-one-commit`, `traversal-stop-kinds-and-constraint-results`, `traversal-stops-and-decisions-map-to-core`, `uncovered-coverage-is-r-minus-c`, `undefined-term-is-an-undeclared-material-relation`, `unexercised-declared-capability-yields-no-evaluation-result`, `world-model-verdicts-map-to-core`.

## Inconsistency between members found while encoding

TRAVERSAL_OCCURRENCE's stop `hold` row still maps to indeterminate "while
every relation and capability the judgment requires is declared by this
closed signature and was exercised, which is the second case of ACTIVATION
§3". ACTIVATION at `9be9f57` dropped that precondition from its second
case. `traversal-stops-and-decisions-map-to-core` carries TRAVERSAL's own
wording; the members disagree on what the cited case requires. Not
malformed for encoding; left for the Executive.

## What this pass does not show

It does not show that the 309 clauses no reviewer flagged are faithful:
each reviewer read packets of best-matching sentences, not the whole
member, and a defect in a sentence the matcher did not surface could be
missed. It does not check symbol labels beyond the subjects of corrected
clauses, residual details, or coverage (what the members state that no
clause encodes). Two reviewers stated close calls (g2: `composition-is-declared-only-where-the-evaluation-requires-it`
and `coverage-ledger-fields`; g3: `clause-standing-is-disposed`,
`core-statement-names-the-method`, `glossary-locates-and-never-decides`).
Two corrected clauses keep URIs that no longer describe their content:
`formal-fragment-established` (the member now states a hypothesis) and
`unexercised-declared-capability-yields-no-evaluation-result` (a result is
now returned where a sufficient evaluation exists).
