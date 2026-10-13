# Common Conformance Questions

A discriminator is a case that separates a correct candidate from a defective one. These discriminators are acceptance criterion 5 of the [C3 Construction Contract](../PRODUCT.md#c3-construction-contract).

Both tenants are evaluated against the same independently specified expectations. The reviewer takes in these expectations and the actual source before inspecting the candidate. No passing result is recorded here.

| Discriminator | Expected distinction |
|---|---|
| A derivation or independence argument is claimed | Each claimed derivation shows its premises. Claimed independence is argued, not assumed. |
| Information and its representation differ | Agreement in structure cannot establish identical meaning or semantic fidelity. |
| Identity is unchanged while content changes | The current state, and whether an earlier observation still applies, are considered separately. |
| Typed producers and consumers disagree | The incompatible domain or precondition is made explicit. Fields of the same shape do not make a valid join. |
| Assessment A failed and required coverage B is uncovered | A's authenticated failure and its citations survive, and B stays unresolved. Every planned assessment's returned judgement is authenticated against its producer, subject, basis and supporting evidence. B is required coverage outside those assessments, not an omitted planned judgement. |
| A genuinely planned assessment carries a judgement from a different subject | Plan membership does not authenticate the returned judgement. The misbound result cannot satisfy the assessment obligation. |
| The context a task needs is interdependent and does not fit one actor | Narrowing the task lawfully, handing it to another capable actor, or a truthful stop keeps the material obligations. |
| A frame fits its byte limit but irrelevant material obscures a required dependency | Size alone does not establish adequacy. Keep the material dependency, exclude irrelevant material and evaluate actual use under the [frame requirement](../requirements/README.md#bounded-transitions-and-reference-frames). |
| An author opens a fresh context to review its own candidate | A new context does not establish independent authorship or supply missing review authority. Relevant common sources may still be shared by an independent reviewer. |
| A coordination frame omits frontier items from its current attention | Excluded work remains open; a bounded view cannot silently dispose it. The next decision retains its material dependencies. |
| A new observation exposes more obligations, or a destination is revised to make the current candidate pass | Discovery may increase the frontier while improving knowledge. Counts alone do not measure progress. A revised destination requires its owning decision and cannot establish that the original destination was reached. |
| One directly authorised task fits a sufficient frame | The generic method permits the direct activation, subject to any separately required assessment. It imposes no fixed role inventory or actor sequence. |
| A peer configuration has no central Executive, or a task uses responsibilities outside the familiar three roles | Evaluate the configuration against the task, dependencies, actor limits, authority and required assurance. Different labels or topology neither reject nor accept it. The installed configuration selected to build this release retains its own scope. |
| Actors redistribute work during execution, including work with effects of uncertain completion | The permitted reconfiguration retains outstanding obligations and result dependencies, resolves material effect uncertainty before dependent action, and preserves authority and required independence. Self-organisation supplies no exemption from these conditions. |
| An arrangement is called optimal because it is familiar, persistent or self-organised | Adequacy and optimality remain separate claims. An optimality claim needs stated objectives, constraints and comparison scope with supporting evidence. Different models or objectives can favour different configurations. |
| A coordinator receives a compact task result that omits a blocker material to delivery | Small size is insufficient. The coordinator retains the longer-term outcome and acquires the information needed for the next decision through its permitted frame inputs. Missing information cannot be assumed favourable. |
| A material dependency changes or a new observation invalidates an earlier claim | Affected applicability and validity are checked before reuse, including when the candidate's bytes are unchanged. Demonstrably independent supported work is kept. |
| A task packet contains relevant rules but lacks material context or authority | A rule packet alone is insufficient. The activated frame binds the contract, subject, evidence, capability and permitted effects required for the task. |
| An interruption leaves work partly written | Recovery uses the current workspace and the applicable work state. It does not erase progress or invent a completed assessment. |
| A parse or map succeeds | The claim stays mechanical until independently sufficient semantic and practical evidence exists. |
| A change to work carriers or process is proposed as new law | The claimed obligation is justified by its purpose and material relation, or identified as unsupported overhead. |
| The same requirements are realised by software, a human team or a mixed process | Each tenant supplies its computational calculus, concrete execution binding and conformance evidence. Common requirements decide fitness; the kind of executor alone neither rejects nor accepts the realisation ([binding requirement](../requirements/README.md#build-tenant-binding-requirement)). |
| A faster execution plan merges two required independent assessments or substitutes an automated result for a required human decision | Matching outputs or lower cost cannot discharge the lost independence or authority obligation. The binding fails conformance. |
| Two environments use one computational calculus, or one actor performs different kinds of operation | Each binding must satisfy the calculus's laws. Different stacks do not force duplicate calculi; actor identity does not determine operation kind or grant authority. |
| An a_c model of a human process passes structural validation | The representation neither selects an automated executor nor establishes that the human process meets its requirements. Execution conformance needs its own applicable evidence. |
| Two loci in one candidate decide the same question | One is the [owning locus](../requirements/README.md#single-ownership-requirement). The other refers to it, or refines it with a mapping back to it. A frame's copy names its owner. No rule of precedence between loci substitutes for an owner. |
| A member or profile defines its own result values | Each value maps to exactly one core result. Failure, undecidability, non-performance and unknown effect completion never map to a higher standing. The evaluated predicate and the domain outcome travel with the core value ([requirement](../requirements/README.md#single-result-algebra-requirement)). |
| A frame's task returns a result | The frame carries the core result algebra or its profile's mapping into it. |
| A functor or categorical join is claimed | Before the claim, objects, arrows, arrow equality, identity and composition are given and the functor laws are shown. Otherwise the claim is a hypothesis ([standard](../requirements/README.md#categorical-demonstration-standard)). |
| A rewrite or refinement step is applied | The law that permits it is declared for the subject. An exact step preserves meaning. An approximate step states its adequacy relation and an end-to-end bound. |

Logical review is a reviewer's reasoned reading. It finds counterexamples and contradictions without running anything. Actual-use cases do real construction, observe genuine defects, keep the uncertainty of effects, and re-enter the method at the right stage.

The token-transfer test in [A_C_DEPENDENCY](../requirements/A_C_DEPENDENCY.md#proof-claims) tests a_c separately from the method's interpretation fidelity. Source comparison independent of the author, mechanical checks, formal derivations and practical adequacy remain different kinds of evidence.
