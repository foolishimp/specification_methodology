# CR3 Critical Review: Codex v3 Candidate

Status: this is commentary, not specification or design. It is a closed, read-only logical review that repairs nothing.

| Coordinate | Binding |
|---|---|
| Reviewer | Claude context (cross-family) |
| Author of the subject | Codex |
| Subject | `subject/specification_methodology/v3/build_tenants/codex/` frozen at `9bc8962`. Members: `successor/standards/`. Design: `design/` |
| Evidence | `evidence/.../codex/qualification/` at `3ad1fca`. `C3/synthesis/RETURN.md` is treated as claims to test |
| Common basis | `common/.../v3/specification/`: PRODUCT, INTENT, requirements/README (R), conformance/README (C, 31 rows) |
| Predecessor | installed `v2.5.1-rc.2/standards/`, read only for inherited-versus-introduced checks |
| Oracle | `tenant/claude/c3-synthesis:.../C3-SYNTHESIS/EXPECTATIONS.md`, items 2, 3, 6, 7 and Amendment 1 |
| Not read | any Claude candidate member |

Path abbreviations, all under `successor/standards/` unless stated:

| Abbreviation | File |
|---|---|
| F | FOUNDATIONS.md |
| RF | REFERENCE_FRAME_METHOD.md |
| SPEC | SPEC_METHOD.md |
| TL | TRANSFORMATION_LIBRARY.md |
| BL | STDO_REFERENCE_FRAME_BASELINE.md |
| TKT | TICKET_METHOD.md |
| REL | RELEASE_METHOD.md |
| DMM | DESIGN_MODULE_METHOD.md |
| AC | AXIOMATIC_CALCULUS.md |
| UX | UX_METHOD.md |
| DES | `design/DESIGN.md` |

## 1. Bounded Transitions And Reference Frames (R items 1–5)

### Item 1: state, destination, transitions and completion. Satisfied (E-2-1).

- F:586–593: "A describes current material state and what is justified about it. Z is the selected set of constraints and acceptance conditions … A transition binds its preconditions, permitted effects, result predicate and outer obligations. Where finite context or attention prevents one adequate activation, refine the task into supported transitions."
- F:611–616: "Useful discovery can enlarge the known frontier; counts alone are no distance metric. Stopping can be lawful without completion. Completion needs the required evidence and acceptance conditions … Changing Z follows its owner and cannot establish that the old destination was reached."
- F:412–416: a stop reports "the actual destination or task predicate … with its reason, observed effects and outstanding obligations."

### Item 2: frame sufficiency and capacity pressure. Satisfied (E-2-2).

- RF-002/003/004 at RF:349–370 bound fit, material sufficiency ("appears in the frame or enters through a declared authoritative input") and irrelevance exclusion.
- F:546–549 makes acquisition include "known material dependencies directly or through declared available inputs".
- F:189–199: "If a coupled required relation does not fit, the actor reports the misfit … The actor acts on an already authorized response, requests the owning decision, or stops with an explicit unresolved result … Never replace a difficult required relation with an easier claim."
- RF-014 at RF:476–481 adds: "The actor may not silently omit material relations to fit context." TL:155–157 adds: "Capacity does not license omission."

### Item 3: context fit separate from adequate attention. Satisfied in meaning; tier-location finding F-3.

- TL:154–155: "Measure context where the execution binding selects it, and assess actual adequacy separately."
- SPEC:853–857: "Context, time, memory, communication, human effort and spend state their units and are measured at the boundary declared by that binding where they are material. Attention adequacy is evaluated through actual-use evidence; no universal attention unit or score is required."
- F:186–188: "No universal numeric budget, resource ledger or measurement gate follows."
- RF:580–584 rules out any universal "resource ledger, benchmark, budget or measurement gate".
- The defect: F, the tier that owns "finite context and attention", never states the distinction "context = what an activation holds, attention = what it uses". F also does not own the separation rule. RF-002 (RF:349–354), titled "Finite Attention", decides only fit. The separation is decided twice, at TL and at SPEC, and neither refers to the other.
- Universal measurement gate: none found. The common builder rule "bytes measured before reading" did not leak into the package. A grep of `standards/` and `plugins/` for before-reading, byte-limit and token-budget phrasing found only WRITING_GUIDE:106, which disclaims byte limits.

### Item 4: configuration, distinct relations, naming and independence. Satisfied (E-2-4 to E-2-7, E-2-9). Inherited residue: F-7, F-8.

- F:620–628: "A configuration allocates operations and information to capable actors … Its existing design or frame record explains the allocation against operations, dependencies, capabilities, assurance, resource limits and failure assumptions … They do not uniquely derive a hierarchy or a fixed inventory of roles. An adequate configuration can use one actor, peers, a hierarchy or supported adaptive allocation."
- F:630–634: "Required independent review retains its authorship and evidence conditions; a new context alone does not supply it. Roles acquire authority from their grants, never from their names. Functional decomposition, communication, authority and evaluation dependency are distinct."
- F:638–641: "Every allocation and reconfiguration, fixed or adaptive, preserves material dependencies, outstanding obligations, observed and uncertain effects, admitted authority and required independence. A claim that one arrangement is optimal names its objective, constraints, comparison scope and evidence."
- RF-009 at RF:403–405: "Roles label selected responsibilities; they are not an exhaustive primitive inventory or a prerequisite for every task."
- RF:218–222: "Declaring, selecting, activating, or executing a frame does not grant semantic, operation, or decision authority." RF-006 at RF:381–384 says the same.
- RF:299–301 makes each activation bind evaluation, subject, basis, actor and evidence boundary.
- Shared sources for independent reviewers are allowed at RF:235–237 and RF:697–700.
- The Executive/Worker/Reviewer arrangement is an optional profile: BL:25–32, BL:89–133, BL:1642–1643 ("need not preserve the labels Executive, Worker, and Reviewer"), and F:636–638. DES:39 scopes it to "This construction's selected coordination; no universal role inventory".
- Predecessor text carried with a role label still in generic members:
  - SPEC:1661–1664 and SPEC:1677 ("Writer", "Executive mutation restrictions remain applicable") and TKT:933–936 are verbatim from rc.2 (SPEC:1577–1591 and TKT:880–881 there). They only permit; they prescribe no inventory. See F-7.
  - RF:207–208 defines frame-set authority as "the human authority", and RF-014 assigns the misfit response to "human authority". Both are inherited (rc.2 RF:187–188 and RF:430–435). A proxy is permitted at RF:224–226. See F-8.
- No carried text prescribes a fixed role inventory as generic law.

### Item 5: workspace, context, the current-state and basis rule, and resumption. Satisfied (E-2-8, E-2-10 to E-2-12).

- F:534–537: "The workspace is the continuing material state … The actor's context is a bounded account acquired from these sources. It is fallible and disposable."
- The current-state and basis rule:
  - F:538–541: "Acquisition observes the subject and basis the activation actually binds, including frozen snapshots where selected. Admissible contrary current evidence reopens affected claims through their drift and re-entry rules; it does not silently select a different basis."
  - F:541–543: observations "do not grant permission to change a requirement to match the implementation".
  - F:551–553: "Absence from a partial projection, sparse checkout or empty local record is not evidence of absence in the bound subject; acquire its authoritative source or retain indeterminacy."
  - F:535–536: "Material external state is observed through its owning interface."
- Reconciliation:
  - F:550–551: "A summary without supported freshness cannot override its owner."
  - RF:142: "Observed state can defeat a stale summary; the summary cannot change the state."
- Resumption:
  - F:564–567: "resumption reconstructs sufficient context from the continuing workspace … It neither erases progress nor requires a transcript of every earlier activation."
  - F:575–582: unknown effects are observed or reconciled before a dependent repeat, and an event log "is not universally the work state or a compulsory recovery algorithm".
  - F:374: "An empty local log or discarded context does not establish no effect."
  - SPEC:1032–1037: "Discarding that context does not rewind A … it cannot silently change Z or create permission." SPEC:1756–1764 applies the same.
- Handoff: RF:693–700 lets a closed result carry the handoff without transferring private context, keeping its validity and independence conditions.

## 2. Build-Tenant Binding (R items 1–6)

The owner is SPEC §WHAT, HOW, And Work Carriers (SPEC:826–859). It is in the Spec Method tier and owns the bounded context `urn:stdo:bounded-context:build-tenancy` (E-3-1 satisfied). This text is introduced; the rc.2 SPEC has no "computational calculus" or "operation kind" text.

| R item | Result | Owning text |
|---|---|---|
| 1. Calculus bound to an environment, carried in design and realisation | Satisfied | SPEC:834–839: "A tenant's design supplies its computational calculus and concrete binding: which operations realise those requirements, how they compose, which actors or mechanisms perform them, what effects they permit, the operational assumptions and how their outcomes are observed." |
| 2. Stack, human process or mix, within the requirements; author, actor and operation kind distinct | Satisfied, with one sub-clause missing at the owner | SPEC:839–841 ("software, hardware, people, organisations or a mixture"). SPEC:845–848: "Author identity, actor identity and operation kind remain distinct … A person performing a procedure is not thereby making a human adjudication." The sub-clause "including any required human decision" is absent here; it appears only at SPEC:1659–1660 under UP-020. See F-4. |
| 3. Operations, laws, effects, measures with units and boundaries | Satisfied | SPEC:836–839 and SPEC:853–855 |
| 4. Evidence covers meaning and constraints, including authority, independence, failure and recovery; no weakening for convenience; categorical claims meet the standard | Partially at the owner | SPEC:851–853 requires "the evidence capable of defeating the claimed realisation". SPEC:857–859: "A requirement-to-operation route alone does not discharge preservation … A tenant cannot repair an inconvenient requirement by silently changing the common WHAT." The owner does not list authority, independence, failure and recovery, and has no link to the categorical standard. Those parts are spread across DMM:1649–1652 (authority, refusal and recovery for human operations), F:638–640, TL:274–275 and F:257–268. See F-4. |
| 5. Calculus reuse | Satisfied | SPEC:843–845 |
| 6. a_c does not select the executor or prove conformance | Satisfied | SPEC:848–849 |

Applied at the point of use (E-3-2(a) satisfied): DMM:1643–1655 (UP-019) applies the owner: "A machine stack, a human procedure and a mixed process each state their operations, composition, effect locations, authority and material resource measures, with their units and observation boundaries … a role title is not its implementation." SPEC:1018–1019 makes Realisation "the tenant's concrete environment … a performed human procedure is another case".

The tenant's own binding (A1(b)) is present, with gaps (F-5). DES:5–15 declares:

- operations: "document construction, source comparison, frame projection, predicate evaluation and authorised disposition";
- composition laws: sequential preservation, and concurrency "only within disjoint write territories and compatible inputs";
- effects;
- the environment: "a mixed process: Codex construction, separate review activations, Git worktrees, Python checkers, the pinned Axiom Indexer and the product owner's decisions";
- the measures: "Byte counts measure selected inputs; wall time and CLI spend measure the declared process boundary. Unmeasured parent-session overhead remains unknown."

The gaps:

- Wall time and spend have no units.
- The "declared process boundary" is not declared in the design.
- The review actors are not named. The evidence shows they are `claude … --model opus` (`run_actor.py:10`; every `runs/*/MEASUREMENT.json` argv), so author (Codex) and actor (Claude) are distinct coordinates, but only the evidence says so.
- The per-call limits are not in the design: 120,000 input bytes, 900 s, USD 2, and the USD 30 aggregate. They are in MEASUREMENT.json and COSTS.json.
- Failure assumptions are not stated. For example, RETURN:64–68 records that a reviewer claimed tool use it did not have.
- The design does not state whether human effort and communication are material.

The builder's Executive/Worker/Reviewer allocation is common-owned (PRODUCT:156–182), so the tenant is not charged with re-explaining it.

## 3. Categorical Demonstration

- The standard is stated in F §Orthogonal descriptions. At F:245–247: "To assert a category, specify its domain, objects, typed arrows, arrow equality, identities and associative composition. To assert a functor, define its action on objects and arrows and show identity and composition preservation."
- F:248–255 distinguishes the claims: A, I and C_H "name categories only after the required objects, arrows and laws have been supplied … conformance to Sigma_contract, semantic equivalence and computational equivalence remain different claims. Categorical equivalence additionally requires the appropriate quasi-inverse and natural isomorphisms".
- F:257–268 covers per-layer preservation, an adequacy relation with an end-to-end bound, licensing laws, a_c separation, evidence classes, and the worked join required for the capability: "an unproved categorical account remains a hypothesis".
- No categorical claim is presented as established anywhere in the members or the design:
  - AC:812–815: "`Functor Kind` … does not by itself assert a category-theoretic functor."
  - TL:236–239 asserts no "universal category theorem".
  - ODD:48 and DES:77–79 ("Categorical hypotheses remain hypotheses").
  - F:270–273 handles Markov categories and monads.
  - World Model's Markov object is labelled "candidate-class" at WORLD_MODEL_METHOD:338–342.
- Conformance and equivalence are kept distinct. Functorial preservation is defined (F:246–247) but not named as a third claim distinct from conformance. See F-9.
- Associativity claims (F:508–518): "the conjunction precedence is associative, and the effect join over normalized disjoint parts is associative".
  - They are true by inspection. Conjunction precedence is the maximum over a chain: falsified > invalid_basis > out_of_frame > indeterminate > satisfied. The effect join depends only on the set of part values and is a union homomorphism; I checked each case of f(f(A)∪B) = f(A∪B).
  - The member gives neither the argument nor an evidence class, which standard item 5 requires. See F-6.
  - The candidate correctly withholds associativity from arbitrary operators and requires an effect-independence law before reordering (F:512–518).
- Tier: the standard sits in F. This is acceptable under oracle ambiguity A5.

## 4. Discriminators (all 31 rows of C)

Each row has a C line number and an oracle ID (Amendment 1 numbering: row 19 = E-7-31; rows 20–31 = E-7-19 to E-7-30). Tally: **29 satisfied, 2 falsified, 0 indeterminate.**

| # | C line / oracle | Case | Verdict | Deciding text |
|---|---|---|---|---|
| 1 | 9 / E-7-1 | Derivation or independence claimed | Satisfied | F:48–51 (premises "are adopted commitments … not theorems derived from finite capacity alone"); F:81–83 ("A family without that argument remains an unsupported specialisation"); F:645–654 table; RF:243–245 ("The unqualified word `independent` does not establish any of these relations by itself") |
| 2 | 10 / E-7-2 | Information vs representation | Satisfied | F:87–90: "Equal encodings can have different meanings … A parser, structural validator or successful join does not establish interpretation fidelity." |
| 3 | 11 / E-7-3 | Same identity, new content | Satisfied | F:120–122 ("unchanged identity does not establish current content. A digest binds bytes, not all semantic meaning"); F:555–559 (observation binds time or version); RF-011 |
| 4 | 12 / E-7-4 | Typed producer and consumer disagree | Satisfied | F:169–171 (compose only when types, interpretation, identity, lifecycle, preconditions, authority and effects are compatible); RF:181–182 ("Equal names, values, shapes … do not establish coordinate equality"); AC-016 |
| 5 | 13 / E-7-5 | A failed, B uncovered | Satisfied | F:455–461 ("authenticate each contribution against its producer, subject, basis and required plan membership … required coverage outside an authenticated plan remains uncovered. These are separate conditions"); F:465–467 ("Missing or undecidable other coverage remains explicit alongside it") |
| 6 | 14 / E-7-6 | Planned judgment from a different subject | Satisfied | F:456–457 ("An unauthenticated claim cannot discharge an obligation"); RF:652–653 ("bound to another subject/basis … cannot satisfy a dependent conjunction") |
| 7 | 15 / E-7-7 | Interdependent context exceeds one actor | Satisfied | F:192–199; RF-014 (RF:478–481); TL:155–157 |
| 8 | 16 / E-7-8 | Byte-fit frame obscures a dependency | Satisfied (tier-location issue F-3) | RF-003 and RF-004 (RF:358–370); TL:154–155; SPEC:855–857; RF:1044 ("Frame size is optimized for reliable evaluation, not maximum context loading"); RF:1205–1208 sensitivity and irrelevance tests |
| 9 | 17 / E-7-9 | Author reviews in a fresh context | Satisfied | F:631–632 ("a new context alone does not supply it"); TKT:767–773 (UP-007: "the reviewer is not the author … Self-review … cannot be relabeled as independent"); RF:238–241; TL:234; shared sources allowed at RF:697–700 |
| 10 | 18 / E-7-10 | Coordination frame omits frontier items | Satisfied | Generic: F:312 (`out_of_frame` "is not silently omitted from the wider obligation"); F:551–553; RF-015 (RF:485–488); F:638–640 (outstanding obligations kept). Profile specialisation: BL:339–345 ("An omitted obligation remains open in the workspace") |
| 11 | 19 / E-7-11 | Discovery; destination revised to pass | Satisfied | F:611–616; SPEC:1768–1773 ("Discovery of previously hidden distance … is not itself negative implementation progress … commit count, and review count are not Product progress") |
| 12 | 20 / E-7-12 | Direct task fits one frame | Satisfied | SPEC:1661–1670 ("No Executive activation is required solely to appoint that Writer … Direct entry preserves … required assessment and reserved decisions"); TKT:933–936; RF-009 |
| 13 | 21 / E-7-13 | No Executive; unfamiliar roles | Satisfied | Generic: F:625–628; RF-016 (RF:492–495, no "collaboration topology, worker count"); F:633. Builder scope: DES:39. Profile: BL:31–32, BL:1642–1643 |
| 14 | 22 / E-7-14 | Redistribution with uncertain effects | Satisfied | F:638–640 ("fixed or adaptive, preserves … observed and uncertain effects, admitted authority and required independence"); F:575–578 |
| 15 | 23 / E-7-15 | "Optimal" arrangement | Satisfied | F:627–628 (adequacy); F:640–641 (optimality "names its objective, constraints, comparison scope and evidence"); RF:576–578 |
| 16 | 24 / E-7-16 | Compact result omits a blocker | Satisfied | Generic: RF:693–695 (private context is unneeded only "when its closed result and provenance are sufficient for the consuming decision"); F:297–301 (the core record carries "unresolved obligations"); F:470–475 (a missing evaluation gives indeterminate; "An empty list proves nothing"); F:546–549 (acquire through declared inputs). Profile: BL:339–345 |
| 17 | 25 / E-7-17 | A dependency invalidates a claim | Satisfied | F:569–573 ("Changed support reopens the affected dependent claims. Unchanged independent work remains usable … A stored green label is not a validity argument"); F:120–122; SPEC:2203–2207 (UP-008) |
| 18 | 26 / E-7-18 | Rules without context or authority | Satisfied | F:549–550 ("A rule packet without its current subject is insufficient"); RF:1027–1038 minimum activation packet; RF:218–222 |
| 19 | 27 / E-7-31 | Fresh actor; stale summary | Satisfied | F:536–543; F:550–551; RF:142; F:374 (discarded context ≠ no effect); SPEC:1035–1037 (no new permission) |
| 20 | 28 / E-7-19 | Interrupted partial work | Satisfied | F:327–333 ("An interruption does not erase evaluation already undertaken"); F:343–345 (absent slot, "not a fabricated child result"); F:564–567; RF:459–461 ("The work remains `not_performed` until actually undertaken") |
| 21 | 29 / E-7-20 | Parse or map succeeds | Satisfied | F:89–90; AC:747–749; SPEC:931–938; SPEC:2261–2263 ("Digest integrity and index generation establish identity and structure, not semantic fidelity or usability") |
| 22 | 30 / E-7-21 | Carrier or process change made law | Satisfied | SPEC:1527–1530 ("Each constraint must identify the semantic ambiguity it removes"); SPEC:1555–1558 ("disproportionate when it duplicates truth"); SPEC:1560–1566 (applied to the method's own execution); F:622–624 (configuration lives in existing records) |
| 23 | 31 / E-7-22 | Software, human or mixed realisation | Satisfied | SPEC:834–841; DMM:1647–1655 ("not as a demand to disguise every human step as code") |
| 24 | 32 / E-7-23 | Merged assessments; automated human decision | Satisfied | Merging: TL:274–275 ("Contract duplicated meaning and authority only while preserving required distinctions and independent evaluations"); F:638–640. Automation: SPEC:1659–1660 ("does not weaken direct-human acceptance where Product or release law requires it"); AC:838–841 (cannot flatten "probabilistic proposal, deterministic evaluation, and human decision"); RF:224–226 (proxy only where the authority law permits). Backup: RF:583–584 |
| 25 | 33 / E-7-24 | One calculus across environments; one actor, several operation kinds | Satisfied | SPEC:843–848; AC:806–811 ("The actor, executor, domain operation, and functor kind are different coordinates") |
| 26 | 34 / E-7-25 | a_c model of a human process validates | Satisfied | SPEC:848–849 |
| 27 | 35 / E-7-26 | Two loci decide one question | **Falsified (Low, F-3)** | Counterexample: whether attention adequacy is measured and judged separately is decided at TL:154–155 and again at SPEC:855–857. Neither refers to the other, and a third locus is F:649. The loci agree. Frame copies hold: all 89 excerpts in the six `frames/*.md` views name their source and SHA-256 and match it byte for byte, apart from rebased links (checked mechanically) |
| 28 | 36 / E-7-27 | A member defines result values | **Falsified (Medium, F-1, F-2)** | Counterexample: TKT:337–343 defines sprint-close classes (`accepted`, `local_paydown`, `design_reframe`, `requirement_reprice`, `product_reprice`, `remove`) with no core map. TL:205–206 declares Ticket's "sprint/paydown and work-carrier closure classifications" to be core refinements, and F:383–386 then requires "a total, reason-sensitive map". UX:512–520 maps the identical list. REL:561–568 (UP-015 dispositions) has no map although TL:206–207 lists them as refinements. Held elsewhere: AC-007 (AC:427–441), TKT:728–737 admission, BL:513–521, SPEC proportional disposition table, RF-012, REL:250–258, UX, ODD:1195–1201 |
| 29 | 37 / E-7-28 | A frame task returns a result | Satisfied | RF-012 (RF:435–441); each of the six frame views carries `FOUNDATIONS.md — Result algebra` (for example frames/WORK_RECOVERY.md:23–25) |
| 30 | 38 / E-7-29 | Functor or join claimed | Satisfied | No functor or join is claimed. The standard is at F:245–255 and AC:812–815 |
| 31 | 39 / E-7-30 | Rewrite or refinement applied | Satisfied (evidence-class gap F-6) | F:257–261 (exact rewriting preserves meaning, approximation needs an end-to-end bound, licensing laws); F:508–518 (the regrouping law is declared for a fixed domain; reordering needs an effect-independence law) |

## 5. Findings

| ID | Severity | Claim | Evidence | Inherited or introduced | Smallest repair |
|---|---|---|---|---|---|
| F-1 | Medium | Sprint-close classifications are a member result set with no core map, yet the library declares them core refinements. This contradicts R §Single Result Algebra item 2 and RETURN:30–31 ("Consumers refine their own outcomes into it"). The generic decision-result rule at F:405–408 does not repair this. It maps only whether a disposition was lawfully made, whereas `accepted` also asserts "compliant under the sprint authority", an assessment claim. UX:512–520 separates those two predicates; TKT does not. TKT:735–737 ("For every original outcome … apply the core result law") is scoped to admission and does not reach sprint close. | TKT:337–343; TL:205–206; F:383–386; contrast UX:512–520 | Enum inherited (rc.2 TKT:328). Contradiction introduced (TL claim; UX mapped, TKT not) | Add UX:512–520's map to TKT §Sprint Close Review, or make one locus own the shared list and refer the other to it |
| F-2 | Low–Medium | UP-015 dispositions are listed as core refinements with no map. Oracle ambiguity A3 allows them to lie outside the core, but the candidate chose "inside" without supplying the map. The gap is narrower than the full list. `intentionally removed` is an owner decision, covered by F:405–408. `not applicable` is partly covered by F:409–410. The unmapped residue is `conserved` and `superseded`, which are semantic claims about the successor. Row 28 is falsified on F-1 alone. | REL:561–568; TL:206–207 | Introduced (the TL classification) | State the map in REL (for example, the predicate is "claim c has disposition d with its required locus or reason"; unresolved → `indeterminate`), or declare dispositions outside the core and remove them from the TL list |
| F-3 | Low | Fit versus adequate attention is decided at two unlinked loci, below the owning tier. F never defines context versus attention, and RF-002 "Finite Attention" decides only fit. Content is correct. | TL:154–155; SPEC:855–857; F:649; RF:349–354 | Introduced (TL and SPEC text are new) | One owning sentence in F §Workspace and context or §Finite capacity; TL and SPEC refer to it |
| F-4 | Low | The binding owner omits R item 2's "including any required human decision" and item 4's list of evidence conditions (authority, independence, failure, recovery) and its categorical link. Other loci cover them, so the use holds but the owner is incomplete. | SPEC:851–859, compared with SPEC:1659–1660, DMM:1649–1652, TL:274–275 and F:257–268 | Introduced | Add one sentence to SPEC:851–859 naming those conditions and linking F §Orthogonal descriptions |
| F-5 | Low (Medium only under an owner ruling on A1(b)) | The tenant's own binding lacks units for time and spend, a declared process boundary, the review actor identity and family, its limits and its failure assumptions. These exist only in evidence. | DES:5–15; `run_actor.py:10`; `MEASUREMENT.json` argv and limits; COSTS.json; RETURN:64–68 | Introduced | Extend DES §Binding and outcome with the units (bytes, s, USD), the per-call and aggregate limits, `claude --model opus` as cross-family reviewer actor distinct from the Codex author, and known failure modes |
| F-6 | Low | Associativity of conjunction precedence and of the effect join is asserted without argument or evidence class. The claims are true by inspection. | F:508–512; R §Categorical item 5 | Introduced | Add the two-line argument (maximum over a chain; set-union homomorphism) and label it "established by mathematical argument" |
| F-7 | Low | Generic members use the optional profile's labels ("Writer", "Executive mutation restrictions") without owner qualification. They permit only; nothing is prescribed. | SPEC:1661–1664, SPEC:1677; TKT:933–936 | Inherited (rc.2 SPEC:1577–1591; TKT:880–881) | Owner-qualify ("where the Baseline is adopted") or use "constructor" and "coordinator" |
| F-8 | Observation | Frame-set authority is fixed as "the human authority", and the RF-014 misfit response names "human authority". This is a fixed authority placement in generic law, not derived from task or assurance. A proxy is permitted. | RF:207–208; RF:478–481; RF:224–226 | Inherited (rc.2 RF:187–188; RF:430–435) | Record it as a declared choice with its owner in F's derivation table, or say "admitted authority (human or admitted proxy)" |
| F-9 | Observation | Functorial preservation is defined but not named as a third claim distinct from conformance and equivalence. | F:246–255 | Introduced | Add "functorial preservation" to the F:252–253 list |

## 6. What Holds

- The workspace/context and current-state rules (F:532–582) are complete against R item 5. This includes the sparse-checkout rule, no rebinding of the basis, no permission from observation, unknown effects resolved before a dependent repeat, and no universal replay.
- Configuration law (F:618–641) is generic and derives allocation from task, dependency, capability and assurance. The three-role Baseline is explicitly optional and project-replaceable (BL:25–32, BL:1642–1643). No fixed role inventory or universal measurement gate appears as generic law.
- Build-tenant binding is owned by the Spec Method and applied in Design (UP-019), and it covers human and mixed processes without disguising them as code.
- No categorical claim outruns its demonstration. Functor Kind is disclaimed.
- The core result algebra separates verdict, performance and effect (F:296–416), and its conjunction preserves failure, absent slots and uncovered coverage (F:418–530).
- The 89 frame excerpts are exact copies of their owners, apart from rebased links. Each names its source and SHA-256.
- RETURN claims confirmed against the text: the arrangements are task-dependent, there is no six-stage procedure, tenant binding includes human and mixed processes, and no categorical result is inferred.
- RETURN claim falsified in part: "Consumers refine their own outcomes into it" (F-1, F-2).

## 7. Limits

- This was a logical review only. No actual-use activation was run and no evidence run was re-executed.
- FOUNDATIONS, REFERENCE_FRAME_METHOD (lines 1–1300), TRANSFORMATION_LIBRARY, the design, and the SPEC sections on tenancy, the chain, UP-014, UP-020, UP-022 and evidence were read in full.
- The rest was read selectively: BL lines 1–750 and 1584–1682; TKT admission, sprint, UP-007 and closure; the REL header, qualification and UP-015; DMM UP-019; AC position, AC-007 and functor kinds; the UX, ODD and WORLD_MODEL excerpts cited above.
- Other profile members (TRAVERSAL, IDENTITY, the rest of DMM, ODD, UX, WORLD_MODEL) were only grepped. Row 28's sweep is bounded to the members named in its row, so further unmapped value sets may exist.
- The a_c interpretation under the tenant's `a_c/` (R §Categorical item 5) was not evaluated.
- Row 27 was tested by sampling recurring determinations, not by an exhaustive ownership census.
- The entry points `successor/plugins/` skills and `authority_compressions/stdo_bootstrap.md` are outside the member scope and were only grepped or excerpted.
- The frame-copy check script is at `scratchpad/cr3tools/framecheck2.py`. It is the reviewer's own tool, not part of the subject.
- The Claude candidate was not read. The oracle was used for its items 2, 3, 6 and 7 and Amendment 1 only.
