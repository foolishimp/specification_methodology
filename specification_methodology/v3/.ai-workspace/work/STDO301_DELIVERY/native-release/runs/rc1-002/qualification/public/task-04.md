# Installed-route task 04: useful preservation and formal claims

**Subject:** the installed root `…/local-store/releases/v3.0.1-rc.1` at cut `v3.0.1-rc.1`. I read files only at that path.

**What I did not check:**
- I did not check any digests or the manifest against the bytes. The manifest SHA, payload inventory and installed-byte proof come from the root, not from me.
- I did not run `examples/deterministic_contracts.py`, because I had no shell.
- Everything below is me applying the installed clauses. It is not acceptance.

## Routes actually used

1. `standards/README.md`. Line 20 routes interpretation and projection questions to AXIOMATIC_CALCULUS and then EVALUATION §2. Line 66 says the examples carry "no generic law or acceptance authority".
2. `standards/FOUNDATIONS.md` §4:
   - Reference versus body: 655–660
   - Formal fragment: 673–728
   - Preservation through construction: 1108–1159
   - Assertions and observation: 1161–1267
   - Quantified assurance: 1326–1374
   - Change impact: 1439–1459
   - Formal representation: 1461–1496
3. `standards/EVALUATION.md`:
   - §2 Separation: 128–175
   - §6 Conformance, including the ladder and representation-benefit experiments: 380–469
   - The F7 family table: 510–524
4. `standards/AXIOMATIC_CALCULUS.md`:
   - AC-011: 670–695
   - §5 intro: 919–958
   - AC-015 and AC-016: 1063–1115
   - §6 with AC-017 to AC-019: 1117–1189
   - Constraint surfaces: 1380–1463
5. `standards/examples/DETERMINISTIC_CONTRACTS.md`, lines 1–15 and 155–209. FOUNDATIONS:715 links this. It contains this exact fixture. I treated it as non-deciding (README:66; example 7–15) and checked its claims myself rather than relying on them.
6. `standards/ACTIVATION.md` §6 Cost and proportionality, lines 1519–1625. EVALUATION:444 and FOUNDATIONS:1444 route cost to it.
7. Grep over those files for headings and terms.

**Deliberately not acquired:** CONFORMANCE (cases AR-01 to AR-04, discriminators 20 and 51), so that I would not use expected distinctions as an oracle. I also did not acquire EVALUATION §3 and §5 (independent assessment and acceptance) or the FOUNDATIONS Results section. The resulting gaps are listed at the end.

---

## Case 1 — Decision factorization: **holds on every input, within a narrow scope**

The claim is `j = h ∘ view` on H. Checked pointwise:

| x∈X | build(x) | view(build(x)) | j(build(x)) | h(view(build(x))) | equal |
|---|---|---|---|---|---|
| S | hS | vS | advance | advance | ✓ |
| F | hF | vF | block_falsified | block_falsified | ✓ |
| I | hI | vI | block_indeterminate | block_indeterminate | ✓ |

- **On H:** `j = h ∘ view`, since all three of hS, hF and hI agree.
- **On X:** composing with build also gives `j ∘ build = h ∘ view ∘ build`.

This is the decision-preservation form in FOUNDATIONS:1243–1248: `delta(s,u) = delta_hat(alpha(s),u)`, with `delta = j`, `alpha = view`, `delta_hat = h`, and u fixed or absent for one subject and basis. The check is a finite argument that covers every input. It is not a mechanical check I ran (FOUNDATIONS:1468–1471 separates these kinds of support). It matches the example (DETERMINISTIC_CONTRACTS:167).

**Exact scope.** It holds only for:
- this one subject and basis Γ;
- the three admissible reports;
- these four finite functions;
- pointwise function equality with ordinary identities and composition.

**What it does not establish:**
- **Transition preservation.** No T or T_hat is declared, and FOUNDATIONS:1248–1253 requires a separate demonstration plus a horizon.
- **Other consumers, policies or report domains.** FOUNDATIONS:1236–1241.
- **That a real checker conforms.** FOUNDATIONS:1205–1207 says a restricted deterministic model keeps its scope, and an actual checker needs its own conformance account.
- **Any compression, minimality or cost claim.** view is a bijection, so every function on H factors through it trivially. The factorization witnesses that no distinction was lost, not that anything was reduced. Compare FOUNDATIONS:1262–1267: a sufficiency witness is not a proof of compression, and representation size is not total cost.
- **A categorical or functor claim.** FOUNDATIONS:702–704; example 172–173.
- **Semantic acceptance.** EVALUATION:162–166; AC:1144–1148.

## Case 2 — Constant subject-only projection: **no factorization exists**

Let `c: H → {σ}` be constant. If any `h'` satisfied `j = h' ∘ c`, then `j(hS) = h'(σ) = j(hI)`. That gives `advance = block_indeterminate`, a contradiction. Mathematically, anything that factors through a constant map is constant, and j takes three distinct values, so this fails for every candidate `h'`, not only the given h. If c instead lands at one fixed point of V, then `h ∘ c` is constant and is wrong on at least two inputs.

What the method says about this:
- **Observation sufficiency fails.** `c(hS) = c(hI)` while the required decisions differ (FOUNDATIONS:1216–1226). The same holds for every pair of inputs.
- **The sufficiency claim is falsified.** "Two cases with the same representation but incompatible required decisions … falsify the sufficiency claim" (FOUNDATIONS:1238–1240).
- **The lost distinction is a residual, not success.** The projection drops a required member, which it may not do to fit a carrier or budget (FOUNDATIONS:655–660; AC-011, AC:683–687).
- **The permitted responses** are further evidence, a justified narrower scope, or an indeterminate judgment (FOUNDATIONS:1225–1226).
- The example reaches the same result (DETERMINISTIC_CONTRACTS:169–170) and calls this kind of representation the "insufficient candidate pointer" (line 204).

**Open point:** how an indeterminate judgment about the view maps to a policy value in D is for the policy owner to decide. The clauses I read do not settle it.

## Case 3 — Functor laws for a terminal-category functor: **a structural claim only; nothing follows about the policy distinction**

**What the proof does establish.** Every category has exactly one map to the terminal category 1: every object goes to `*` and every arrow to `id_*`. Identity and composition are preserved trivially. So the author's proof establishes only the stated structural claim, and only if the source category is stated in full (objects, arrows, arrow equality, identities, associative composition) and the map is bound to it (FOUNDATIONS:677–682, 713–714). If the proof is a generic lemma, it "applies only after its source and target objects, arrows, equality and actual maps are bound to the subject" (FOUNDATIONS:713–714).

**What it says about the policy distinction.** Nothing positive, and in fact it is a counterexample:
- 1 has one object and one arrow, so all three readouts collapse to `id_*`. No delta_hat on the image can recover j. This is case 2 in categorical form (example 178–183).
- "Category and functor laws establish their stated structural claim; they do not alone establish that the chosen interpretation or projection is sufficient for the intended use" (FOUNDATIONS:710–713).
- Preserving identities and composition is "a further claim distinct from every rung" of the equivalence ladder (EVALUATION:408–409).
- It is not a categorical equivalence. That would need a quasi-inverse and natural isomorphisms on a stated domain (EVALUATION:413–416).
- It does not discharge H1, which stays unresolved (FOUNDATIONS:719–728; example 184–186).
- The traversal "functor kinds" F_D, F_P and F_H (AC:946–952; AC-015) are a different concept. The same word does not import it.

**Additional adequacy evidence needed:**
1. Name the consumer (the policy j and h). Name its required observations and distinctions (the three readouts), the input and policy scope, and the horizon (FOUNDATIONS:709–710, 1233–1237).
2. Define delta, alpha and delta_hat, and demonstrate `delta = delta_hat ∘ alpha` on the declared domain. If transitions are claimed, also show `alpha(T(s,u)) ≈ T_hat(alpha(s),u)` with a declared adequacy relation and readout preservation over the horizon (FOUNDATIONS:1243–1253).
3. Keep standing, currentness and invalidation, producer and authority distinctions. Keep authority and hold distinctions exact where their contracts require it. Any approximation needs explicit latitude and a horizon bound (FOUNDATIONS:1237–1238, 1255–1258).
4. For any categorical claim, meet the full Formal fragment: the a_c representation that separates premises, consequences and choices, plus the named evidence kinds and scope (FOUNDATIONS:683–694).
5. Get a semantic fidelity judgment that is separate from the structural check (EVALUATION:162–166; AC-018 at AC:1159–1168). Where the representation is used as a task surface, show sufficiency by actual use (AC:1445–1449).

## Case 4 — Comparing representations on operating cost

EVALUATION:453–469 makes this comparison an *optional* design.

**Arms:**
- the new representation;
- the existing contract;
- the simplest adequate, qualified plain-text fix, which must itself keep the required distinctions so it is not a strawman (EVALUATION:456–457).

The example also suggests the complete plain-text record, an equivalent qualified reference, and the insufficient pointer as a negative control (DETERMINISTIC_CONTRACTS:203–205).

**Controlled factors:**
- Hold substantive information and access fixed across arms when the claim is a representation benefit.
- Vary separately whether relevant counterexamples are retained, absent, or stale and out of scope (EVALUATION:454–455; example 205–206).

**Outcome oracles:**
- Fix them independently in advance, for example: does the actor's decision equal j on each case, and do unresolved obligations stay visible.
- Compare after freeze against the governing basis. A reference outcome is non-authoritative (EVALUATION:441–451, 465–466).

**Costs:**
- Declare units and boundaries for acquisition, rendering, reasoning, repair and assurance cost (EVALUATION:457–458).
- Measure under the selected execution binding, or record a cost as unmeasured. Declare the allowance up front (ACTIVATION:1578–1581).
- Keep components separate so one cannot hide another, and count context sent to every delegated actor (ACTIVATION:1583–1590).
- Keep anticipated costs separate from measured ones (FOUNDATIONS:1442–1444).
- Reasoning cost means effective reasoning complexity, not raw size (ACTIVATION:1527–1531). Representation size is not total operating cost (FOUNDATIONS:1265–1267).

**Interpreting the results (EVALUATION:462–464):**
- **Information-equivalent benefit** (arms differ only in representation) can support an architecture decision.
- **Retention benefit** (gains that come from keeping counterexamples rather than leaving them out) supports a context-selection policy, not the representation. If the new representation only wins because it carries counterexamples the baseline lacks, that is a retention benefit wrongly reported as a representation benefit.
- **Stale-material failure** points to provenance and invalidation, not to the representation.

**If there is no benefit, or higher total cost:** that supports keeping the existing construction. Outcome correctness and unresolved obligations stay visible either way (EVALUATION:464–466). A cheaper plan never waives required safety, authority or acceptance conditions (FOUNDATIONS:1373–1374). The evidence only informs the decision; the decision authority makes it (EVALUATION:142–143).

**Trial count and architecture:** the method imposes neither.
- Trials scale to the claim, risk and resources, and the guidance "prescribes no universal trial count or new review cycle" (EVALUATION:458–460).
- Propose–Probe–Compose is one possible strategy, "not a dependency or acceptance oracle" (EVALUATION:466–467).
- The method states "No universal quota, ticket count, actor count or accounting carrier" (ACTIVATION:1590–1591).
- The equations impose "no universal functional model" (FOUNDATIONS:1255). The examples "select no runtime or mandatory representation" (example 7).
- A test count does not stand in for a risk and dependence account (FOUNDATIONS:1331–1332).

---

## Gaps and preserved uncertainty

- **Integrity not verified by me.** Manifest, payload and installed-byte claims are the root's.
- **Example program not run.** Its executable claims (example 9–15, 181–183) are unverified by me. Cases 1 and 2 rest on my own hand check of three-element functions.
- **Author's proof not supplied.** Whether its source category is bound to this subject is unknown, so even its structural claim is conditional (FOUNDATIONS:713–714).
- **CONFORMANCE not acquired.** I did not read CONFORMANCE, so any added expected distinctions there are unconsulted.
- **Acceptance and assessment not acquired.** I did not read EVALUATION §3 and §5, so the independent-assessment and acceptance standing of the author's proof or any experiment is undecided here.
- **No formal core values assigned.** I did not acquire FOUNDATIONS Results, so the case decisions above are stated in plain terms, not as core result values.
- **Policy value in case 2 unsettled.** Which value in D follows from an indeterminate judgment about the constant view is not settled by the clauses I read.
- **H1 stays unresolved** (FOUNDATIONS:719–728).
