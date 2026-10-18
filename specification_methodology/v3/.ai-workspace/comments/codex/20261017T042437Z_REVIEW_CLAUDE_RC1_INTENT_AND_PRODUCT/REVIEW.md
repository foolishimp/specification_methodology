# Independent content review of Claude's STDO v3 RC1

## Judgment

**Claude substantially implements the Intent, but the declared Product is not met.** The core now supplies real deciding rules for construction from A toward Z, bounded context, recovery, evidence, authority and assurance. These relationships operate in downstream procedures; they are more than explanatory headings. I would retain that design.

Six material defects prevent an unqualified conformance conclusion. One prevents the declared installed package from supplying its own fresh-project bootstrap. Four alter or omit distinctions at consumers of otherwise sound shared laws. One makes the published conformance member depend on an external construction specification while promising independence. There is also one low-severity stale interpretation-entry description.

The repairs should be one bounded batch, followed by an affected readback. The findings do not justify another foundational rewrite or repetition of every historical test. This review grants neither acceptance nor a release disposition.

## Exact subject and independence

- **S — candidate:** `af3b8b7107c92a216cc53d629ddeefecd7f77fca`, under `specification_methodology/v3/build_tenants/claude/`.
- **W — common WHAT:** ratified C3-I5-06, `4c340f7adec9f3c893e3e267b23e4cadeb357854`, under `specification_methodology/v3/specification/`.
- **M — later release declaration:** `b7e8f73d6b9908ecb0f6cc1609aa99ed94ce81f7`, under the candidate's tenant root. Its manifest identifies S. The standards, plugin and a_c source are unchanged between S and M.

Candidate citations below are relative to S's `standards/` unless otherwise stated. Common citations use W. These are immutable Git coordinates, not line claims against a mutable worktree. For example, acquire a finding's subject with `git show af3b8b7107c92a216cc53d629ddeefecd7f77fca:specification_methodology/v3/build_tenants/claude/standards/ASSURANCE.md`.

The owner explicitly selected baseline STDO v3, deferring complete a_c coverage, remaining actual-use expectation sets and authority compressions/projections. That direction is recorded at main commit `c5209f002eca6af7d7918c41b96eec9eb18850a3`, in `comments/claude/20261017T025819Z_RC1_CANDIDATE_CLAUDE_LINE.md` under the v3 workspace. Those deferred obligations are not relabelled here as new baseline defects. They still limit any assertion that the complete written Product is delivered.

Expectations were fixed from the common specification before candidate reading. Four fresh nonauthor contexts read all 23 published Markdown members in full, partitioned by responsibility, plus material consumers, ordinary entry, templates and delivery declarations. The parent checked the material counterexamples against their actual source. Claude's test passes, grading, frontiers and return verdicts supplied no correctness credit. Embedded author claims were treated as claims. No author test suite was run.

The parent has authored the competing Codex line and portions of the common specification. That interest is disclosed. Fresh nonauthor readings reduce direct authorship dependence; they do not make the shared specification an independently validated model of the world. Coordinated findings are not counted as statistically independent votes. This is a content review, not a matched actual-use trial or acceptance-bearing review of every predecessor disposition.

## What the implementation delivers

The important distinction is between a rule being present and that rule actually deciding a case. The following judgments use concrete cases fixed independently of the implementation's tests.

| Intent or Product obligation | Actual deciding path | Content judgment |
| --- | --- | --- |
| Manage construction from A to Z under finite resources | `ACTIVATION:198–353`; `SPEC_METHOD:668–755,1626–1697` | Current state, required constraints, predictive model, strategy and evidence are distinct. An invariant-preserving no-op can be lawful without establishing progress. Resource exhaustion produces a stated unresolved stop, not completion. |
| Use feedback to repair the right thing | `ACTIVATION:278–317`; `SPEC_METHOD:815–899,967–1005` | Bugs and new features enter the same process. Diagnosis can distinguish realisation, requirement/design, prediction and observation. An intake label determines neither priority nor permission to alter the specification. Adequate existing law permits local repair. |
| Treat workspace reality as the continuing basis | `ACTIVATION:1377–1514`; ordinary `stdo-status` entry | A fresh actor can discard stale belief, retain valid edits and re-observe current state. Missing memory does not establish that an external effect did not happen. Recovery requires sufficient reconciliation before dependent action, without a universal reset or complete-history replay. |
| Derive configurations from bounded work rather than impose a hierarchy | `ACTIVATION:510–706`; `EXECUTIVE_BASELINE:3–15,155–193`; `SPEC_METHOD:1772–1911` | Direct, peer, hierarchical and adaptive arrangements are permitted under their conditions. Human and mixed execution can use adequate current records and direct observation. A fixed Executive/Worker/Reviewer sequence, software code and an event store are not universal prerequisites. |
| Preserve judgments through one result system | `FOUNDATIONS:790–1129`; `REFERENCE_FRAME:574–632`; `EXECUTIVE_BASELINE:1078–1092,1271–1286` | A known failure for A survives when B was not performed. Availability, fitness and acceptance remain distinct predicates. Unknown effects are not converted into no effect. R5 identifies one material domain exception to this otherwise substantive integration. |
| Make assurance part of transformation | `FOUNDATIONS:1177–1407`; `ASSURANCE:236–251,639–702` | Local preservation needs the composition premises; approximate local tolerances do not establish an end-to-end bound. A test's assertion provenance and observation binding matter. Agreement does not validate a shared incorrect model, and probability claims require their conditional assumptions. The core observation law is correct; R2 finds a faulty consumer. |
| Reassess affected claims after change | `FOUNDATIONS:1409–1492`; `ACTIVATION:1692–1758`; `REFERENCE_FRAME:910–963` | Unchanged artifact bytes do not preserve evidence invalidated by a changed environment or governing basis. Unaffected evidence can remain applicable. A new actor or conversation alone does not force wholesale repetition. Completeness of a particular impact analysis still needs support. |
| Make algebraic, categorical and model claims precise | `FOUNDATIONS:740–788,1177–1228`; `AXIOMATIC_CALCULUS:988–1114`; `WORLD_MODEL:379–509`; `IDENTITY:148–169` | Operation kind, actor and mechanism stay separate. Category and functor claims carry obligations rather than gaining standing from their names. A bounded interface does not establish a statistical Markov property; the stronger promotion gate remains explicit. |
| Reduce repeated interpretation through shared ownership | Shared effect law consumed by Product Definition and Executive; shared conjunction consumed by frame and ticket integration | There is concrete local consolidation. The required comparative reduction across ordinary paths is not established by this review. Shared references alone, document size and author test counts receive no reduction credit. |

The finite-assurance content is also represented faithfully in one independently inspected current a_c path: the program, map and offered construction/assurance projection preserve the condition that an observed pass remains an observation while oracle fidelity is unestablished. This is one supported binding, not whole-interpretation qualification. Its exact source and artifact identities are in the [domain report](DOMAIN_REVIEW.md#bounded-current-a_c-binding-inspection).

## Material findings

Severity describes the demonstrated consequence. It does not automatically select Product priority or the owner's release decision.

### R1 — Major: the declared installed package cannot supply its required bootstrap

**Source:** `PRODUCT_DEFINITION:85–91,243–248,287–292,944–952,1043–1082`; `RELEASE:490–507`; M `release/manifest.json:15–200` and `release/release-note.md:50–55`.

The method identifies a normative Product Definition schema and a single fill-in template. Its bootstrap requires installing the exact cut, copying that cut's template and validating the resulting definition. The declared manifest contains 23 top-level Markdown members, 17 plugin files, LICENSE and the release note. It contains neither `schemas/product-definition.schema.json` nor `templates/PRODUCT_DEFINITION_TEMPLATE.json`.

Both files exist in the frozen source tree. That does not resolve the defect: the method explicitly distinguishes repository carriers from Product membership, and its verifier rejects entries not derived from the manifest's exact file paths. The release note's statement that schemas and templates are auxiliary members of the same tree supplies no missing manifest admission.

**Independent case:** a fresh project acquires exactly the declared installed member set and follows bootstrap. The required template cannot be copied from that installation; its normative schema is also unavailable. Manually obtaining unmanifested source or a predecessor copy does not satisfy the selected installed-basis contract. The dependent bootstrap must stop.

**Repair:** reconcile the admitted package inventory, its schema and release description with the current bootstrap inputs. Check the one resulting clean, source-blind bootstrap route. This is a source-proven delivery contradiction; no installer was run and no observed installer failure is claimed. Deferring frames or complete a_c work does not defer these directly required schema/template inputs. See [LC-01](LIFE_CYCLE_REVIEW.md#lc-01--major-declared-package-cannot-supply-its-required-bootstrap-template-and-schema).

### R2 — Medium: assurance demands distinguishing subjects when distinguishing predicate truth is sufficient

**Source:** `ASSURANCE:681–686` against its owner `FOUNDATIONS:1285–1300`; W `requirements/ASSURANCE.md:49–56`.

The foundation correctly requires `π(s) = π(s′) ⇒ q(s) = q(s′)`: the same observation must not conceal opposite truth values for the assessed predicate. The assurance consumer instead requires further evidence, narrower scope or an indeterminate result whenever the observation cannot separate two admissible subjects. That is stronger than its owner.

**Independent case:** admissible subjects are 1, 2, 3 and 4; the authenticated observation is parity; the assessed predicate is “even.” The observation cannot distinguish 2 from 4, but both satisfy the predicate. It cannot distinguish 1 from 3, but both falsify it. The observation is sufficient for the task without being injective over all subject identity. The consumer nevertheless demands extra acquisition or an inconclusive judgment.

A constant observation over all four subjects is the negative control: that really is insufficient. The positive case separately assumes a supported observation binding; it does not excuse a faulty instrument.

**Repair:** qualify the consumer by differing predicate truth and use the existing foundation's condition. No new calculus or requirement to observe every detail is needed. This matters directly to task-specific context reduction. See [CORE-F1](CORE_REVIEW.md#core-f1--p2--medium-assurance-acquisition-demands-subject-separation-instead-of-predicate-separation).

### R3 — Medium: a design preference becomes an absolute prohibition and loses an express exception

**Source:** `DESIGN_MODULE:378–401` against `134–142,1787–1795`; W `requirements/README.md:32–34,66`.

The functional-bias list prefers immutable carriers. An added sentence says a realisation forgoing any preferred shape does not conform, with no exception beyond one failure-carrier item saying “where practical.” The immutable-carrier rule in the same member expressly permits materially necessary mutation, including a host/runtime requirement, with justification.

**Independent case:** a selected design profile uses an interface whose host requires a mutable carrier. The design establishes necessity, confines mutation to explicit transitions and preserves effect/authority boundaries. The immutable-carrier owner permits this case; the blanket functional-bias sentence rejects it. The predecessor also carried the necessity exception, so the candidate's claim that it admitted no such exception is incorrect.

**Repair:** retain the binding preference and actual prohibitions while preserving the necessity exception at its owner. An immutable-first policy is not a rule that every mutable carrier is nonconforming. See [B-01](DOMAIN_REVIEW.md#b-01--p2-functional-preference-is-turned-into-an-absolute-rule-contradicting-an-express-permitted-case).

### R4 — Medium: generic migration tickets enforce an optional profile's recurrence policy

**Source:** `TICKETS:425–438,858–883`; `DESIGN_MODULE:3–13,1917–1944,2395–2433`; `PROFILES:31–49`; W `requirements/README.md:139–151`.

The design profile owns the second/third-recurrence policy and is optional, including partial adoption by rule family. Generic migration tickets nevertheless require a library/commonisation declaration and block a third local rebuild unless it consumes or extends a shared implementation or carries a do-not-commonise decision. The operating consumer supplies no adoption condition.

**Independent case:** a Product selects core method law, or adopts only design families that exclude recurrence. Its otherwise lawful migration adds a third authority-neutral local helper. The generic ticket imports the unselected recurrence policy and blocks implementation pending additional design/library work.

**Repair:** condition the ticket's enforcement on adoption of the owned recurrence family. If recurrence is instead intended as universal method policy, that needs an explicit owning decision; it cannot become universal through a ticket consumer. See [U1](USE_REVIEW.md#u1--medium-a-generic-migration-ticket-imports-optional-recurrence-policy).

### R5 — Medium: material no-action determinations are excluded from the core result system

**Source:** `ODD:985–1025`, especially `1019–1025`; `FOUNDATIONS:112,792–816`; `ACTIVATION:945–959,1016–1034`; W `requirements/README.md:162–174`.

The ODD evaluator determines that a desired unpublished action cannot lawfully be selected, and returns typed no-action. It also makes material authority/re-entry determinations. The member explicitly says that selection, including typed no-action, maps to no core value; a preceding closure carries the result “where there is one.”

**Independent case:** a lawfully activated initial selection has an exact outcome and catalogue, but the fresh gap requires action X, which the catalogue does not publish. No prior action or closure exists. The evaluator makes a material no-lawful-action determination, but the declared contract provides no core result for that predicate. Successfully producing the next-action projection proves availability only. No later admission of X occurs to supply the missing judgment.

This does not require every selected action identifier or internal ranking calculation to be an evaluation result. The common requirement expressly distinguishes ordinary data from material compliance, admission, closure and disposition determinations. The latter cannot be exempted by naming their output a selection or state.

**Repair:** keep action data separate while binding the actual predicates and core mappings for material refusal/authority determinations. Preserve their distinct causes and the separate authority of later admission. See [B-02](DOMAIN_REVIEW.md#b-02--p2-material-no-action-determinations-are-excluded-from-the-one-result-system).

### R6 — Medium: the standalone conformance member imports its deciding expectations from outside the delivery

**Source:** `CONFORMANCE:3–11,138–150,154–205`; M's complete manifest inventory; W `requirements/README.md:38–56`.

The member promises that its common discriminators are stated in its own text and that the constructing specification is provenance only. It later says each expected distinction is the one in the common specification's conformance table and expressly does not restate it. That common file is absent from the declared installed Product.

**Independent case:** a source-blind reviewer follows discriminator L-19. The local table names an earlier interpretation marked current and routes to method sections. The external expected distinction also requires checking the actually offered current route against its bound source, signature, program, maps and instructions. The local situation label and routes do not restate that whole expectation. The member delegates the deciding oracle to an unavailable construction source.

This concerns the published candidate-construction/qualification contract, not a requirement that every ordinary adopter run all construction checks. Some expected distinctions can be recovered from other owning members; the finding does not claim that every local oracle is absent.

**Repair:** supply the needed expected distinctions at appropriate published owners, or move construction-only material to its proper qualification surface and correct its standing. Another external link or count correction does not make the stated standalone contract true. See [B-03](DOMAIN_REVIEW.md#b-03--p2-the-conformance-member-promises-standalone-expected-distinctions-but-imports-their-deciding-source).

## Minor finding and challenged concerns

**R7 — Low:** the current `a_c/README.md:11–14,39` still describes an older basis, 64 clauses and four indexes, whereas its current descriptor and inspected artifacts describe the rebound interpretation with 155 clauses and five indexes. That can misdirect acquisition. It is a stale current-entry claim, not proof that the whole interpretation is unfaithful or a demand to complete deferred coverage. Details: [B-04](DOMAIN_REVIEW.md#b-04--p3-the-current-calculus-entry-describes-an-obsolete-basis-and-coverage).

Several apparent tensions were challenged rather than counted. A no-ticket route exists for bounded work and assurance. Generic operations do not force ordinary output data into result values. The failed-derivation rules do not automatically require a law change after every failed attempt. Markov wording does not ban a future supported statistical claim. A traversal observation-ordering passage is awkward, but the optional edge and distinct observation possibilities prevent a demonstrated universal cycle. The component reports preserve those limits.

## Why these findings matter to the intended reduction

The recurring failure is incomplete reconciliation at a consumer. A correct shared condition becomes stronger, narrower or absent when repeated in a domain procedure: subject separation replaces predicate sufficiency; preference loses a necessity exception; optional recurrence becomes generic; a material refusal loses its result mapping. Those are failures of the common Product's ownership-and-use requirement, not evidence that the foundational account should be discarded.

The delivery findings expose a related boundary mistake: construction-source availability is treated as if it supplied an admitted installed dependency. The method itself correctly forbids that substitution. Keeping its own package and qualification consumers within that rule is necessary for standalone use.

Thus the content supports the intended architecture but not complete integration. It also does not establish that actors actually spend less context, time or effort applying it than they did under 2.5.1. Local consolidation is visible; whole-method practical superiority remains a separate evidence question.

## Completion boundary and next action

For the owner-selected baseline, the six material findings are concrete current defects. For the full written Product, complete interpretation/fidelity, the remaining actual-use obligations and comparative reduction cannot be marked satisfied by this review. The owner's deferrals remain visible without being converted into fresh release blockers. The separately selected categorical thread supports its own scope when performed; source reading is no substitute for that demonstration.

The appropriate next increment is to repair R1–R6 together, refresh R7, then freeze one successor. One independent affected readback should cover the exact changed clauses and material consumers, the six counterexamples, and a clean bootstrap against the corrected declared package. Existing applicable evidence can be retained. Broader review is warranted only if those changes alter shared meaning or expose further dependencies.

This review did not independently re-prove every predecessor disposition, execute ordinary actors or an installed v3 method, measure acquisition efficiency, or validate every a_c binding. Complete body reading is not exhaustive proof over every possible use. It is nevertheless enough to refute unqualified Product conformance through the concrete cases above.

No implementation, common requirement, ticket, release state, commit, branch or index was changed by this review. Only the expectations, source inventory, component reports and this consolidation were written in this visible main-checkout commentary directory. Main advanced independently during the review from `a79b2a1db2829668bf155d9e70063d261a2f3471` to `7dc097314b73a7ddd8f3d54df1f49a94bb051d59` by addition of the other line's review-plan post; it did not change these frozen subjects.

## Supporting records

- [Activation and scope](ACTIVATION_AND_EXPECTATIONS.md), [whole-method expectations](WHOLE_METHOD_EXPECTATIONS.md), [source inventory](SOURCE_INVENTORY.txt).
- [Core expectations](CORE_EXPECTATIONS.md) and [core report](CORE_REVIEW.md): construction, results, assurance and Spec Method.
- [Domain expectations](DOMAIN_EXPECTATIONS.md) and [domain report](DOMAIN_REVIEW.md): eight profiles/members, mathematical standing and the bounded a_c inspection.
- [Ordinary-use expectations](USE_EXPECTATIONS.md) and [ordinary-use report](USE_REVIEW.md): activation, frames, tickets and plugin entry.
- [Lifecycle expectations](LIFE_CYCLE_EXPECTATIONS.md) and [lifecycle report](LIFE_CYCLE_REVIEW.md): seven members, templates, identity and declared delivery.

The reports give exact full-body coverage and material slices. Cumulative acquired-source accounting is distinct from active retained context; the latter and native session token cost were not instrumented. No paid external actor call or network service was used. These limits do not supply a context-fit or zero-cost claim.
