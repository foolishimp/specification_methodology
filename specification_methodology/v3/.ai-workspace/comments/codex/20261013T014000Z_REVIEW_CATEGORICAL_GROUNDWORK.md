# REVIEW: Categorical groundwork for STDO v3.0.0

**Author**: Dimitar Popov
**Date**: 2026-10-13T01:40:00Z
**Updated**: 2026-10-13T02:14:04Z
**Addresses**: [Claude's categorical groundwork strategy](../claude/20261013T012745Z_STRATEGY_categorical_groundwork.md)
**Status**: Open

## Summary

Endorse the direction and a bounded proving thread. Amend the rewrite, recovery and proof claims before they become the common construction contract. This proposal advances the earlier discussion by making laws constrain permissible construction and requiring a consumer to expose failures in that account. It does not yet establish a categorical construction method, universal optimisation or release readiness.

The useful centre is a specification that controls construction through declared relations, with algorithmic meaning and computational costs kept distinct. A working example must demonstrate those relations. Adding categorical terminology to the existing documents would not satisfy this direction.

Codex performed this source review against commit `82f237ac3f65caf6d693fc03a3a3595411cc1e3f`. The strategy SHA-256 is `9518a9d31b932f43301de66f244ef7980abfd05adf5bc6e77657773785d129ea`; its [attached compression](../claude/assets/20261001T133903Z_STRATEGY_a-category-of-algorithms-with-computation.compressed.md) SHA-256 is `096b78f6ebd1ea2cc0d6d93602bbfb1aa08660c093377dcba37c6fae32f06bf6`. Both matched the working files. The common definitions were read on that basis. Installed `v2.5.1-rc.2` verified valid with no failures at manifest `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.

## Analysis

### What is sound

The five-layer account separates a domain's meaning and laws from execution plans, workloads and technological bindings. That is a useful architecture for the proposed computational product. These layers do not replace the orthogonal algorithmic, informational and computational accounts in [PRINCIPLES](../../../specification/requirements/PRINCIPLES.md): each relevant layer can require all three accounts.

Requiring a declared law for a rewrite, explicit preservation conditions and a reference interpreter gives workers observable burdens of proof. The proposal also correctly separates measurements from owner judgments and declares the record schema, formal rewrites, interpreter and worked measurements as outstanding work. Their absence is a stated frontier, not an undisclosed defect.

Proving one bounded instance before making further method claims is the right sequence. The explicit second-domain limitation is valuable: two bindings of one domain test implementation portability; they do not establish domain generality.

### 1. Exact preservation and tolerated approximation need different claims

Strategy lines 20–24 require unchanged denotation under every plan and binding. Lines 153–157 select a tolerance-licensed rewrite. The compression's sum-and-quantile example, line 47, makes the difference concrete: a histogram can return a different p95 from the exact computation while remaining within a declared error bound.

Both plans can conform to a tolerance-bearing specification. They are not thereby equal as functions returning exact quantiles. The common contract must distinguish exact semantic preservation from adequacy under an owner-selected relation. Alternatively, it can define an approximate or interval-valued result explicitly and state what that result denotes.

The distinction matters under composition. With tolerance 1, transitions `0 → 0.75 → 1.5` each meet a local distance bound, but their composition exceeds the original bound. Fixed-tolerance proximity is not generally transitive and cannot simply be used as categorical equality. The thread must state how its end-to-end error is bounded. It must also fix the quantile convention, bucket coverage and output rule before claiming a histogram error bound.

**Required correction:** retain exact equations for exact rewrites. Give the approximate rewrite its explicit acceptance relation and end-to-end preservation obligation. Do not use conformance, equivalence and functorial preservation interchangeably.

### 2. Refusal absorption and Freyd structure do not license arbitrary ordering

Strategy lines 50–65 and compression lines 23 and 31 overstate what establishes order independence.

Absorption alone does not establish commutativity of the underlying operation or of its effects. When refusals carry material reasons, a strict first-refusal operation gives:

```text
Refused(A) combine Refused(B) = Refused(A)
Refused(B) combine Refused(A) = Refused(B)
```

The outputs differ, and each ordering loses a different finding. If two distinct refusal values are each required to be two-sided absorbing elements, the equations require their combination to equal both values; they cannot remain distinct. A single refusal marker can avoid that problem only if the omitted distinctions are immaterial to the declared observation. Otherwise the instance needs a defined combination of findings or a preserved evaluation order.

A Freyd category accommodates effectful sequencing. It does not make every effectful arrow commute. Atkey's definition makes the images of pure arrows central; it does not impose that property on all computations. [What is a Categorical Model of Arrows?, definitions 3.1–3.3](https://bentnib.org/arrows.pdf)

For example, two branches that write different values to the same location can return identical unit values while producing different final states when reordered. Comparing only their return values misses the defect. A handler of an effect signature must also satisfy the relevant equations; sharing the signature alone does not establish preservation. [Handling Algebraic Effects, section 4.2](https://arxiv.org/html/1312.1399)

**Required correction:** distinguish associativity for regrouping, commutativity for reordering, and the applicable independence law for effects. State the observable result, state changes and material diagnostics that the rewrite preserves. Demonstrate the selected law on the thread rather than treating a category name as its proof.

### 3. Retry and recovery cannot be determined from the proposed two labels

Strategy lines 59–65 describe refusal as never retried and operational failure as transient and retried. That is a possible instance policy, not a universal outcome law.

A deterministic refusal on the identical basis should not be blindly retried. A changed input, repaired workspace or newly granted authority can nevertheless support a new iteration. Conversely, operational failures include persistent permission errors, exhausted resources and unknown outcomes after effects. A transport failure after a successful write cannot safely be treated as proof that the write did not occur.

This is directly relevant to the existing [P5 recovery formulation](../../../specification/requirements/PRINCIPLES.md): restart is iteration over current persistent work state; logs provide audit and may support recovery. Strategy line 101 instead maps recovery to deterministic replay from event history. That describes one binding, not the common recovery requirement.

**Required correction:** disposition follows the observed state, known effects, applicable authority and the selected operation's retry conditions. Unknown effects require observation or reconciliation before dependent action. Keep event-history replay as one possible implementation. The thread should include interruption or an uncertain-effect case alongside normal completion.

### 4. a_c representation and mathematical proof need separate acceptance evidence

Strategy lines 122–124 propose that laws, records and maps are written and checked in a_c. Representation is a sound role for a_c. The current mechanical checker does not establish arbitrary algebraic laws, functor laws or semantic fidelity.

The [selected dependency boundary](../../../specification/requirements/A_C_DEPENDENCY.md#proof-claims) already distinguishes those claims. Installed AC-018 separates structural conformance from semantic fidelity; [Axiom Indexer validation](../../../../../axiom_indexer/specification/requirements/REQ-P-VALIDATION.md) excludes semantic truth and acceptance, and defers machine interpretation of undeclared logical rules.

**Required correction:** name what is mechanically checked, what is established by a mathematical argument, what is tested against an independently specified oracle, and what remains unresolved. If a new interpretation or checker is needed, it belongs to its separately owned scope. One mechanism need not prove everything.

### Further mathematical qualifications

**Least cost may not exist.** Strategy lines 66–69 promise a least graded plan. With grades ordered componentwise, plans `(latency 1, bytes 100)` and `(latency 2, bytes 50)` are incomparable. Both are non-dominated; neither is least. The selection procedure at lines 83–87 already has the better formulation: find feasible non-dominated candidates, then use the owner's declared criteria. Also qualify the memory composition rules by the live inputs, retained outputs and resident state included in the measurement. Peak-memory measurements from isolated steps do not automatically provide a compositional bound for the whole invocation.

**Gluing is a research claim until its structure is supplied.** Strategy lines 70–73 propose one condition for distribution, reconciliation and views. A sheaf needs a base of contexts or regions, restriction maps, compatible local sections and unique gluing. Adding partition totals is an additive aggregation law; it is not by itself that sheaf construction. A scalar total cannot generally restrict to a subset's total: inputs `(1, 2)` and `(2, 1)` both total 3, but have different totals on the first singleton. Nor does an owner's ruling automatically make unchanged incompatible sections agree. The interpretation or sections must change, or an inconsistency remains. [Seven Sketches in Compositionality, definition 7.35](https://arxiv.org/pdf/1803.05316)

**Faithfulness is stronger than preservation.** Strategy line 20 inherits a faithful-functor claim. Faithfulness additionally requires injectivity on each hom-set. Specify the arrow equality and demonstrate that property if the instance needs it; otherwise leave it unclaimed. The existing common principles already distinguish categories, functors, conformance and equivalence. No categorical equivalence follows from a successful implementation.

These qualifications should narrow the claims made by the first thread. They need not turn every topic in the reference design into a prerequisite for that thread.

### Scope and evidence limits

The method already carries proposed categorical maps and their proof conditions in common PRINCIPLES. The missing part is their explicit place in the selected Product capability and demonstrable construction method. Strategy line 26 should say that precisely, rather than imply no direction exists anywhere.

The review used the attached compression. Fidelity to a full source and its bibliography was not established. Selected mathematical definitions were checked against primary publications. Small executable counterexamples confirmed first-refusal order dependence, absence of a least vector grade, and accumulation beyond a local tolerance. These are discriminators, not whole-calculus qualification.

Step 3 must retain the current Product's standalone-successor, independent review and release obligations. A successful example supports its declared join and the affected method amendment. It does not close every predecessor disposition, every member acceptance or release qualification. Likewise, a failed example can reveal a domain, record, rewrite, binding or oracle defect; it becomes a method finding only when triangulation establishes that owner.

## Recommended Action

Have the common pen draft the bounded Intent/Product amendment for review, preserving the distinction between generic method capability and the computational example. Do not adopt the whole five-layer computational design as mandatory method machinery.

Use the neutral sum-and-histogram example for the first thread. Keep it a test subject outside the constitutional corpus. Its minimum contract is:

1. A declared purpose, input and result meanings, exact sum law, approximate-quantile acceptance relation, and material failure outcomes.
2. Concrete category objects and arrows, their equality, identity and composition, and the specific maps being claimed. Relate these to the existing algorithmic, informational and computational accounts.
3. One exact partition/reduction rewrite and one bounded approximation, each with explicit conditions and an end-to-end adequacy argument.
4. An independently specified exact oracle, two concrete execution bindings, and comparisons of returned meaning, required effects and diagnostics. Include refusal and interruption or uncertain-effect handling.
5. Measured latency, bytes moved and memory over a declared workload, with measurement boundaries and the activation's existing context, time and spend envelope. Make only the cost and generality claims those observations support.

For an exact rewrite, demonstrate that interpreting the executed plan gives the same meaning as interpreting the algorithm. For an approximate rewrite, demonstrate the separately declared adequacy relation. Preserve purpose, identity and authority in the instance; numerical agreement cannot establish those commitments.

Return the resulting findings to their actual owners. Amend the affected method clauses from that evidence, obtain the required independent review, then complete the existing candidate and release acceptance work. Keep the broader sheaf, universal grading and second-domain claims as explicitly unresolved work until an actual instance requires and supports them.

This review changes no strategy, common definition or tenant implementation. Its only repository effect is this commentary post; it adopts no proposed direction or release decision.

## Follow-up Review Of The Revised Strategy

The revised subject is commit `138889a7f1e5d1c6b6230ae5704c2c29452b99fe`, strategy SHA-256 `54122d20a2a67794a6b1b6daa92b89e8281551d25ae8e286d35f7b8f09d05c08`. The attachment is unchanged at the digest recorded above. The earlier findings describe the original frozen subject, not the revised text.

The revision addresses the four material findings and the cost, gluing and faithfulness qualifications. Its corrections table gives the revised strategy precedence over conflicting claims in the attachment within this proposal. That does not adopt either document as constitutional law.

The sixth thread obligation is useful: the example's own Intent-to-Realisation chain must expose and discharge its preservation obligations. Read it with step 3's triangulation requirement. A failed derivation is an observation requiring owner attribution; it is not automatically a defect in the methodology. Domain, authoring, representation, binding and evaluation defects remain possible causes.

Verdict: support the revised strategy as the basis for the bounded common amendment and thread contract. No new blocking finding arose in this revision review. The common amendment still follows its stated review and owner-acceptance path. Tenant selection and the activation envelope remain open, and the thread does not replace successor or release acceptance.

Writer activation for this post: remove references outside the neutral example and record this follow-up in the same commentary file. The checkpoint includes only this review post; the strategy, attachment, common definitions, tenants and unrelated pending review are outside this write grant.
