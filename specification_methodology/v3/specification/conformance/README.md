# Common Conformance Questions

A discriminator is a case that separates a correct candidate from a defective one. These discriminators are acceptance criterion 5 of the [C3 Construction Contract](../PRODUCT.md#c3-construction-contract).

Both tenants are evaluated against the same independently specified expectations. The reviewer takes in these expectations and the actual source before inspecting the candidate. No passing result is recorded here.

| Discriminator | Expected distinction |
|---|---|
| A derivation or independence argument is claimed | Each claimed derivation shows its premises. Claimed independence is argued, not assumed. |
| Information and its representation differ | Agreement in structure cannot establish identical meaning or semantic fidelity. |
| Identity is unchanged while content changes | The current state, and whether an earlier observation still applies, are considered separately. |
| Typed producers and consumers disagree | The incompatible domain or precondition is made explicit. Fields of the same shape do not make a valid join. |
| Required assessment A ran and failed, and required assessment B was never covered | A's failure and its citations survive, and B stays unresolved. Every planned assessment slot is authenticated. B is recorded as required coverage that is missing, not as a planned judgement that was omitted. |
| The context a task needs cannot be split and does not fit one actor | Lawful refinement, another capable actor or a truthful stop keeps the material obligations. |
| The basis or evidence changes | Whether affected work still applies is checked again, and unchanged supported work is kept. |
| An interruption leaves work partly written | Recovery uses the current workspace and the applicable work state. It does not erase progress or invent a completed assessment. |
| A parse or map succeeds | The claim stays mechanical until independently sufficient semantic and practical evidence exists. |
| A change to work carriers or process is proposed as new law | The claimed obligation is justified by its purpose and material relation, or identified as unsupported overhead. |
| Two loci in one candidate decide the same question | One is the [owning locus](../requirements/README.md#single-ownership-requirement). The other refers to it, or refines it with a mapping back to it. A frame's copy names its owner. No rule of precedence between loci substitutes for an owner. |
| A member or profile defines its own result values | Each value maps to exactly one core result. Failure, undecidability, non-performance and unknown effect completion never map to a higher standing. The evaluated predicate and the domain outcome travel with the core value ([requirement](../requirements/README.md#single-result-algebra-requirement)). |
| A frame's task returns a result | The frame carries the core result algebra or its profile's mapping into it. |
| A functor or categorical join is claimed | Before the claim, objects, arrows, arrow equality, identity and composition are given and the functor laws are shown. Otherwise the claim is a hypothesis ([standard](../requirements/README.md#categorical-demonstration-standard)). |
| A rewrite or refinement step is applied | The law that permits it is declared for the subject. An exact step preserves meaning. An approximate step states its adequacy relation and an end-to-end bound. |

Logical review is a reviewer's reasoned reading. It finds counterexamples and contradictions without running anything. Actual-use cases do real construction, observe genuine defects, keep the uncertainty of effects, and re-enter the method at the right stage.

The token-transfer test in [A_C_DEPENDENCY](../requirements/A_C_DEPENDENCY.md#proof-claims) tests a_c separately from the method's interpretation fidelity. Source comparison independent of the author, mechanical checks, formal derivations and practical adequacy remain different kinds of evidence.
