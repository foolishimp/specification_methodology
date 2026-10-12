# Affected-relation confirmation: C3 candidate at source `0ff2ed70c55d0fcb13efeef1d57b9dd3359463f1`

**Overall result: `falsified` for claims 1, 3, 4 and 5, and `satisfied` for claim 2.** Each failure has a narrow, literal counterexample below. None of them reopens an unchanged owner.

**What I checked against.** I reviewed only the text pasted into the prompt. The frozen candidates came with no digests, so I can't confirm they match the commit's bytes. I didn't use any tools or check the repository. These clauses were cited but not supplied, so anything that depends on them is `out_of_frame`: UP-013, UP-014, UP-017, UP-020, the Design Module Method body, the Baseline, AC-013, AC-016, the Ticket Method, the Traversal profile, and the ODD body outside §11.5D.

## (1) Explanatory direction versus an unproved universal entailment or derivation

**Main statement: `satisfied`.** FOUNDATIONS says it "abstracts recurring relations … creates no normative hierarchy, derivation provenance or constitutional specialization relation" and is "not an entailment proof or replacement derivation basis." The candidate AXIOMATIC_CALCULUS keeps STDO principles and its listed clauses as its only derivation provenance. Its new paragraph does not make FOUNDATIONS a derivation source.

**Sub-claims that fail:**
- **1a. Method claims and interpreted subjects (FOUNDATIONS, opening): `falsified`.** The candidate says "A method claim is scoped to a purpose, interpreted subject, governing basis, actor and evidence." Counterexample: the candidate README lists `a_c` under "Method owners", yet AC Position says its definitions "do not depend on … a selected subject interpretation, … a model provider, a runtime." AC-014 is a calculus claim tied to no interpreted subject and no actor. *Limit:* if "method claim" excludes calculus-level claims, this goes away, but the text doesn't say so.
- **1b. Conjoin rule (TRANSFORMATION_LIBRARY): `falsified`.** The candidate says "Satisfaction requires every applicable material predicate … unknown applicability prevents a wider satisfied claim." RF-010 lets closed results go to "one declared conjunction *or decision rule*." Counterexample: under a declared disjunctive rule, one `satisfied` input settles the result even when another input's applicability is unknown. The library's universal rule overrides the owner's choice of rule. *Limit:* this is avoided only if "applicable" is read as "required by the declared rule", and the text doesn't say that.
- **1c. Reference-frame results (Library, Evaluate): `falsified` (low severity).** The candidate says "For a reference-frame evaluation, return satisfied, falsified, indeterminate, out_of_frame or invalid_basis." RF-012 lets an externally owned compatible extension refine that set. Counterexample: an RF evaluation under such an extension returns a refined result that isn't one of the five. The summary contradicts its owner.
- **1d. FOUNDATIONS imperatives: `indeterminate`.** "Before acting, establish …" and "Never replace a difficult required relation with an easier claim merely to report success" go beyond RF-014, which is limited to silently omitting relations *to fit context*. They are new obligations only if FOUNDATIONS is deciding text, and README doesn't settle that (see 3c).
- **1e. "Loss or abstraction is admissible only when … and the required consumer distinctions remain recoverable": `indeterminate`.** The second condition is a universal rule with no owner cited. It is harmless only if a permitted loss can never touch a "required" distinction.

## (2) AC-014/017 scope and other role and authority owners

**Result: `satisfied`, with limits.**
- **AC-014:** "Within a_c, AC-014 owns its calculus judgment separation" is scoped correctly. The library's line "A judgment supplies no … acceptance authority" sits in its Evaluate section. It might seem to clash with AC-014's "admission or acceptance judgment", which carries `authority` and `decision` fields. The library's preamble, "The calculus and domain members retain their own … judgment laws", resolves this. *Limit:* the library declares no bounded context of its own, unlike FOUNDATIONS, whose context covers only its own member. So the library's terms "judgment", "decision owner" and "assessor" resolve only through that preamble and their inline owner scoping.
- **AC-017:** "Within an adopted a_c interpretation" is acceptable. *Limit:* AC-017 also governs subject declarations that are evaluated *before* adoption, so "adopted" must not be read as narrowing it.
- **RF-014:** FOUNDATIONS says "human or delegated configuration authority … under RF-014." RF-014 names only "human authority", so the delegated branch is `indeterminate`. "Existing" keeps it from creating new authority, but RF-014 itself does not supply a delegated grant. Whether one exists depends on the Baseline, which wasn't supplied.
- **Roles:** "Reviewer judges / decision owner disposes", "the explanation appoints none" and the Baseline scoping all agree with RF-006 and RF-007.

## (3) README deciding and non-deciding standing

**Result: `falsified`.**
- **3a. Raw members:** "Raw members retain deciding authority at all times." Counterexample: GLOSSARY_GUIDE is a raw member, not a compression. SPEC says it is "a non-deciding locator index." The frames in `frames/` are also members, and README itself calls them "views".
- **3b. Table header:** the column headed "Deciding text" lists Glossary Guide in the "Non-deciding semantic discovery" row. Read literally, that labels the glossary as deciding text. A later README sentence says the opposite, so the README contradicts itself.
- **3c. Product versus cut:** "A selectable STDO Product is one complete immutable released RC cut." The immutable owner says a cut "is the constitutional member set of the selectable STDO Product." The candidate merges the Product's identity into one cut's member set. *Limit:* this is harmless only if "selectable Product" just means "selectable release".
- **3d. Standing of the explanatory account: `indeterminate`.** README creates a third standing, the "explanatory account", without saying whether it decides anything. That gap is what leaves 1d open.

## (4) Exact ODD function identities, complete listed outputs, closure versus next-action, and admission ownership

**ODD binding: `satisfied`.**
- All four names match exactly.
- All output lists match §11.5D in full: `synthesize_model` → ProductAssetModel; `eval_gap` → ObservationSnapshot + GapPressureRow; `evaluate_action` → EdgeFulfillmentLedger + EdgeClosureDecision; `evaluate_next` → PriorityProjection + NextActionProjection + selected_action, including typed no-action while `post_reprice` is unresolved.
- `evaluate_next` consumes the *admitted* decision, consistent with A1a and A7, and "cannot decide prior closure", consistent with A4a.
- ConstructionIntent is admitted separately by ABG admission and traversal authority, which matches its table row.
- A11 is kept.

*Limit:* "including" does not exhaust the typed no-action cases; A3 and A4 have others. The Transform row's "or lawful composition" must mean a published action under A3 and A14, but the row doesn't say so.

**Two summaries elsewhere fail:**
- **4a. FOUNDATIONS: `falsified`.** "ODD owns RuntimeEventLog as runtime truth and its admitted ledger/evidence relations." A15 says "ABG owns runtime truth, event replay." The §11.5D table assigns RuntimeEventLog to "ABG runtime truth" and AdmittedEvidence to "ABG/product admission." The summary moves ownership from the ABG role to the method.
- **4b. README: `falsified` within ODD scope.** "The frame's result, required independent assessment and owner's disposition determine supported continuation." Counterexample: in a selected ODD scope, the closing paragraph of §11.5D says the next work decision is "derived from that equation … no other path can decide what work happens next." That is `evaluate_next` over `NextActionBasis` and a fresh `eval_gap`, not a disposition. *Limit:* this goes away if "supported continuation" means only evidential support, but the text doesn't say that.

## (5) No new normative hierarchy from the binding introductions

**Result: `falsified`.**
- **5a. WORLD_MODEL binding:** "World-model scoped identity, interpretation and typed composition refine the shared foundation." This states a narrowing, constraint-adding relation from FOUNDATIONS to a deciding member. That is a specialization in substance, and FOUNDATIONS says it creates none. SPEC also says that naming a specialization without its coordinates "establishes nothing."
- **5b. Other bindings: `indeterminate`.** The phrases are: SPEC "Bind is refined here by …", the ODD and UX column headers "ODD refinement" and "UX refinement", UX "realized by", and RF "supply concrete instances." Combined with the library's "An instance is bound by purpose, … actor capability, … permitted effects, … consumer", these can make library contracts binding on owner functions. Concrete case: AC binding says calculus applications express the families "through these exact records." AC-014's `Judgment` record has no actor-capability, permitted-effects, failures or consumer field, and `a_c` is independent of model provider and runtime. Either the library's instance contract imposes a requirement on `a_c`, or `a_c` judgments aren't instances. The text doesn't decide which. The disclaimers "the library does not supersede …" and "these correspondences preserve …" reduce the risk but don't define "refine" or "instance" in a way that rules out a hierarchy.
- **Without the issue:** the RELEASE, GLOSSARY, AC Position and ODD intro bindings ("maps", "realized here … owned by the detailed method members") create no hierarchy.

I have no authority to repair or accept anything. These results are evidence for the decision owner.
