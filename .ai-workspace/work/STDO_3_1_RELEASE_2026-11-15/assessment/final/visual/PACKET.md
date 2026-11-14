# Independent bounded visual/source-fidelity assessment

Assess the final native-A-bound 3.1 visual against the previously source-first expectations below. You are the actual distinct-family Claude assessor; the candidate writer and packet operator are Codex-family. No prior candidate writing by this session. No tools or writes are requested. Host metadata, not a self-label, binds actual model identity. Do not claim total-context isolation.

Exact subject: native A c1e0faaa8437c169031a476343c764614135cd93, annotated tag fca8d5e97cf2e945196aecdc33908bb190efdca5, installed manifest ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa. Visual canonical model 10f810f04d4fcf99424ea99631f461e108ee8030ce8145915eb5b9dbe8d14851, model file bf696c10177ffc393a3ae0279b3717fccb42d06d6092afd626d8efa245bc022f, STDO Representation public manifest f1e132063af09d266c9aef908ea778253d22ede665c1bcf6762d33b4d8e124e8. Child B/ref/asset/publication closure is later; this assessment binds exact content, not future invented identity.

Review population: all 24 authored semantic annotations and the explicit 93-section navigation/residual coverage across complete ACTIVATION, SDLC_DEFAULTS and TICKETS. Every population record's meaning-bearing fields are exactly projected below; omitted formal common owner/context/kind scaffolding is declared, so do not claim independently revalidating it. Existing observed mechanics bind the full model/carrier and provide tested preservation evidence. Assess source fidelity, conditions, exceptions, direction, residuals and lawful nonclaims. The three complete source owners below are the deciding visual subjects. Referenced unselected owners are explicitly residual; no complete governing context is claimed.

Return (1) concrete material findings with source/record coordinates, trigger, harm and finite falsifier; (2) supported/falsified/unknown for the bounded source-fidelity and scope-honesty claim; (3) whether fresh artifact meaning and evidence satisfy the source-first V/G-01 population within the expressly bounded visual claim; (4) mechanical/browser evidence applicability and limits. Do not impose non-STDO usefulness/Graphify/whole-method/formal/automatic-host claims excluded by source. Do not turn a compact-label UX limitation into a full source-fidelity failure unless it loses needed meaning. Do not treat Writer pass counts as your semantic verdict. No release/owner acceptance or publication verdict here.

End with one fenced JSON object having keys subject, status (supported/falsified/unknown), findings, supported_claims, unperformed_or_excluded, evidence_limits.



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/assessment/source-first/CLAUDE_EXPECTATIONS.md
SHA256 67aad938b407a4a6616df679d87efe2dd02287a70d6a082a34d03419ba54e4d2; 33354 bytes

# STDO 3.1.0-rc.1: source-first qualification expectations

**Stage result.** This stage evaluated no candidate predicate, and no candidate was in the packet. Every release predicate below therefore has no result yet. None is `indeterminate` and none is `falsified` (EVALUATION §4). Nothing here authorizes publication, assigns Product priority or gives a release verdict.

---

## 0. Actor, independence and observation limits

| Item | Declaration |
|---|---|
| Actor | A Claude-family model (environment reports `claude-opus-5-5`). The CLI session metadata, not this text, is the authoritative identity. |
| Authorship | Within this session I authored none of the supplied Product sources. Codex authored the packet, the request and the choice of which sources to include. That selection is a shared-source dependency, so my derivation covers only what was supplied (ASSURANCE, mutual assurance). |
| Family independence | I am independent of a Codex author only to the extent that the governing basis declares cross-family independence (EVALUATION §3: "declared, not assumed"). Two source trees have Claude build tenants: `v3/build_tenants/claude` and `stdo_skills/build_tenants/claude`. If any changed release subject was authored by a Claude-family actor, I am not independent for that part by default. An authorship map is needed (§5). |
| Host binding | The intake says all tools are disabled. My environment still exposed one tool, an "advisor" that would forward this whole transcript to another model. **I did not call it**, so this result has a single author. The stated "no tools" property is therefore not fully accurate for this host, and fresh context alone proves neither isolation nor independence (CS-04; COORDINATED_HANDOFF, Host Binding). |
| Supplied but unverified | The Product/basis verification record and the per-source SHA-256 digests came from the operator. I could not recompute them. I rely on them as supplied mechanical facts, not as my own observations. |
| Writes | None. The output is stdout only, for the authorized recorder. |

---

## 1. Minimal release predicates

Abbreviations used below: Act = release activation; R = installed 3.0.4 `RELEASE.md`; EV = `EVALUATION.md`; ACT = `ACTIVATION.md`; TK = `TICKETS.md`. Section numbers refer to the 3.0.4 basis unless stated.

| ID | Predicate (minimal claim) | Source | Observation boundary | Finite falsifier |
|---|---|---|---|---|
| RP-01 Scope | The release subject is exactly the six named Products under explicit Product ownership. There is no seventh Product, no implicit adoption and no global install. | Act ¶2–3; root AGENTS | Cohort record, Product Definitions, member inventories, the user's installed store before and after | A seventh member or an edge inferred from co-location. Any Product Definition `basis` changed. A write into the existing global/default STDO store, or into installed 3.0.4 or 3.0.5 bytes. |
| RP-02 Identity and profile | RC profile. For each Product namespace: an annotated immutable tag `<ns>/v3.1.0-rc.1`, an annotated selector `<ns>/v3.1.0` on the same commit, the RC branch, and an optional release branch. Every embedded asset version reads `3.1.0-rc.1`, with only the documented `3.1.0rc1` wheel spelling. | Act ¶1; R §2, §3, §5, §7 | Local and remote refs: object types, peels, version fields in every package | Lightweight tag. Selector on a different commit from the RC tag. Version suffix mismatch. Unqualified `v3.1.0*` ref. Any `3.0.6` identity. A namespace inferred from a directory name. |
| RP-03 Namespace assignment | Every Product has a release namespace assigned by its release authority. Purpose Context needs a newly assigned one. The namespaces for `a_c` and `stdo_skills` come from the 3.0.5-rc.1 record. | R §2 Project-qualified refs | Cohort record and the authority record | A namespace with no assigning authority recorded, or one that collides with an existing namespace. |
| RP-04 Frozen source | The build runs from an isolated release worktree and branch, starting from the selected current source plus authorized prior work. The dirty main worktree, existing refs, installed releases and unrelated work are unchanged. | Act ¶2, ¶6 | `git status`/diff digests of the main worktree before and after; ref list before and after; store digests | A pre-existing ref moved or deleted. Main worktree bytes changed. The build took its input from mutable main or an empty checkout of old main. |
| RP-05 Two-commit order | Commit A freezes the native STDO corpus, plugin, release record and qualification bytes, and gets a local annotated tag. That local cut is installed into a fresh store and verified. Every derived index and child asset in commit B binds A's installed manifest. | Act ¶5; R §7, two-commit construction | A/B commit trees, A's manifest digest, binding fields in B | A derived index binds a development-candidate identity, the 3.0.5-rc.1 manifest `64c0…` as its target corpus, or a manifest other than A's installed manifest. B content exists before the A install. |
| RP-06 Six-Product graph | The cohort record names, for each Product: namespace, definition ID, version, member inventory, Project Subtree root and tree, and every dependency edge with its relation and pin. It also records migration from the five-Product 3.0.5-rc.1 cohort. | Act ¶2, ¶5; R §6, §7 | The new cohort record compared with Product Definition `composition` fields and package pins | An edge missing or invented. A version or tree mismatch. The historical `stack_release.json` mutated, or used as the current cohort. |
| RP-07 Predecessor conservation | Every 3.0.5-rc.1 claim capable of affecting the successor has exactly one disposition: conserved, superseded, intentionally removed or not applicable. "Intentionally removed" cites owner wording. "Conserved" passes the modal and counterexample test. | R §9; EV §5; Act ¶5 | A per-claim disposition record across the five predecessor Products and the native corpus | Any unresolved row, which blocks the affected claim. A package-wide equivalence statement. Withdrawn-unsatisfied obligations presented as satisfied, or as silently absent. |
| RP-08 Version assessment | The minor-version change names its selected predecessor, the affected consumer mappings and the remaining obligations. | R §9, deterministic-kind migration, last ¶ | Release record | The assessment is missing, or compatibility is asserted from the version label alone. |
| RP-09 Semantic freshness of release-target indexes | Every distributed release-target index binds A's actual source membership, order and bytes, method and purpose. Any `covered: true` rests on an external assessment of that exact index, corpus and query. Older entries stay byte-identical. | Act ¶3; PC-R15, PC-R16, PC-S06–S09, PC-R06 | Catalog, provenance, coverage-standing files, regeneration receipt | A stale member pin. Relabelled coverage. An assessment bound to a predecessor index or corpus cited as the new one's verdict. A preserved P1, 3.0.4 or 3.0.5-rc.1 entry whose bytes changed. |
| RP-10 Retired routes stay retired | Context, registry, formal and Lean routes are not runtime dependencies of any released Product. Visual components remain optional. | Act ¶2; root AGENTS; AC-R-V06; PC README; SK-14; GS-03 | Import and dependency sweep of the packaged bytes; context-only install | A context-only install requires a visual component or Lean. A Purpose Context runtime import of representation, Axiom or Lean. Active `join`, `project-registry` or `axiomatize-corpus` present. |
| RP-11 Independent review | A cross-family independent review covers the exact frozen release subject: the A tag object, B commit, local child tag objects and assets. Its expectations were fixed before the subject was read. It is bound to producer, subject, basis and evidence. Partitions conjoin to cover interactions. | Act ¶4–5; EV §3–4; TK UP-007; stdo-review | Review reports with CLI metadata; subject identities | A self-authored semantic verdict. A review bound to a different identity from the published one. A partitioned review with no interaction coverage. |
| RP-12 Finite actual use | The applicable SDLC, ticket/context and Skills scenarios have retained requests, context identities, outputs and assessments on the released path, or valid reuse is shown (§3). Unperformed cases are named. | Act ¶5; SDLC_DEFAULTS qualification obligations; PC-S12; SK-18, SK-20; SCENARIOS | Per-case evidence records | A pass inferred from word presence or schema. A count of passes hides an unperformed case. Expected answers were written by the author. |
| RP-13 Installed and public path | Install through the real manager into a fresh store, verify and resolve. Package checks pass. Host install and verify works. After publication: public download digests match, a fresh public install succeeds, and readback matches. | Act ¶5; R §3; DOC-06 and TOOL-05 where applicable | Manager output, store digests, asset digests, GitHub readback | A staging-directory check presented as installation. Asset digest mismatch. The public install resolves to different bytes. |
| RP-14 Atomic publication | Before the push, every immutable tag has bound remote absence and every mutable ref has a per-ref lease. One atomic transaction pushes the complete ref set. If atomic push is unsupported, publication refuses, with no sequential fallback. | Act ¶5–6; R §7 | Pre-push fetch record, the push command and its result, remote readback | A non-atomic or partial push. An unguarded force. A tag moved after creation. A ref missing on readback. |
| RP-15 Durable result | `RELEASED.md` and `RESULT.json` bind source, native and derived commits, tags, assets, public install, evidence and residuals. They close only after publication actually completes. They state failures and uncertainty. | Act ¶7 | The two files | A closure claimed before readback. An omitted residual or failed check. |
| RP-16 Acceptance kept separate | "Published", "qualified for declared claims" and "accepted by the owner" are recorded as distinct. Acceptance attaches to the exact immutable identity and is not inferred from the earlier conditional approval or from GitHub "Latest". | R §3, §8; EV §5; Act ¶6 | Release record wording | The record says "accepted" with no owner act on the exact cut. A host flag treated as qualification. |
| RP-17 Release-facing assets match | Release notes, READMEs, GOALS, inventory documents and manifests describe the exact cut. Stale statements such as "no successor release", "unversioned" or wrong rule counts are reconciled before tagging. | R §6, §8 bullet 5 | Diff of release-facing documents at A and B | Contradictory counts, a stale "development" label on released bytes, or a claim of qualification beyond the evidence. |

---

## 2. Semantic, behaviour and migration case matrix

Each case derives its expectation from the cited source. **Rerun** marks evidence that must be fresh on final bytes, by its nature. **Reuse?** marks cases where prior evidence may be retained under §3.

### 2a. Native STDO 3.1.0-rc.1 (Specification Methodology v3)

| Case | Expected behaviour | Source | Evidence class |
|---|---|---|---|
| N-01 Default projection standing | `SDLC_DEFAULTS.md` names its deciding owners. Examples declare their standing. The installed member's standing (guidance or projection, not a second constitution) is explicit. | SDLC-08; v3, PC and Skills frame bases | Source assessment; Reuse? |
| N-02 Frame reproduction | Affected verbatim frames reproduce from current owners at A. `FRAME_INPUTS` matches. An unaffected frame is reused only with unchanged inputs demonstrated. | SDLC-08; PRODUCT_BASIS frame check | Mechanical; Rerun at A |
| N-03 TICKETS §5 clarification | It is presented as an application of TK §1/§2/§5/§7 and ACT §2/§5/§7, with ACTIVATION as the single owner. It needs an R §9 disposition against 3.0.5-rc.1, and the modal test if "conserved" is claimed. | SDLC_DEFAULTS ¶2; R §9 | Source assessment |
| N-04 Native work and review routes | `stdo-work` and `stdo-review` consume the default. Direct Writer entry stays sufficient. No automatic ticket, coordinator or review. Guidance selects no profile and grants no effect. | SDLC-07; CS-01 | Source + actual use |
| N-05 Ordinary test-closed repair | A reproduced repair closes on failing-before and passing-after evidence plus the declared suite, with no invented review or release gate. | SDLC-05; QF-02; Q09 | Actual use |
| N-06 Four causal routes | Defective realization, inadequate requirement or design, inaccurate predictive model and insufficient observation each route through diagnosis. Recurrence alone selects no repair. | SDLC-03; Q10 | Actual use, one case per route |
| N-07 Capability or complexity failure | A recurring failure triggers frame and capability diagnosis in its prescribed order. | SDLC-03 | Actual use |
| N-08 Changed-scope re-entry | A changed outcome, scope or territory needs its owning decision before dependent work. | SDLC-04 | Actual use |
| N-09 Named boundary review | Incremental QA does not satisfy acceptance, qualification or release. | SDLC-02; Q11 | Actual use |
| N-10 Unrelated finding | It is preserved and routed to its owner. The current claim is not widened or blocked by severity alone. | SDLC-04; EV §5; Q12 | Actual use |
| N-11 Incomplete evidence | The dependent result stays unresolved. Unrelated authorized progress continues, with no blanket stop. | SDLC-06; Q13 | Actual use |
| N-12 Required recheck | A recheck happens only on an actual trigger: boundary claim, hard-stop or capture-fidelity repair, absent reproduction, or uncovered scope. | QF-02; SDLC-05; Q14 | Actual use |
| N-13 Valid-support reuse | Evidence for unchanged claims is retained. Only affected claims reopen. A new session alone invalidates nothing. | SDLC-06; ACT §7 | Actual use |
| N-14 Installed references | Native skills and Getting Started resolve inside the installed package, with no working-record dependency. | CS-08; TOOL-03 | Installed; Rerun |
| N-15 Builder and basis unchanged | `stdo_3.json` still binds 3.0.4. No consumer adoption occurs. | Act ¶3; R §4 | Mechanical |
| N-16 Bundled documentation and tools | If the native package carries the explorer, code example, proof reader or tool bundle, then DOC-01–06 and TOOL-01–05 apply on the new manifest, with historical representations labelled historical. If dropped, an R §9 disposition is required. | INSTALLED_DOCUMENTATION; INSTALLED_TOOLING | Installed; Rerun |

### 2b. Ticket and context continuity (one cross-Product family: native, Purpose Context, Skills)

| Case | Expected behaviour | Source |
|---|---|---|
| T-01 Fresh actor from ticket | With no prior conversation, the actor recovers progress, governing inputs and the next authorized action, then records facts and results before return. No mandatory transcript. | PC-S11/S12 row 1; Q15; ACT §5 |
| T-02 Contrary summary | Current state corrects the account. An unresolved conflict stays explicit. Contradicting acceptance evidence withholds closure. | PC-S12 row 2; Q16; TK UP-009 |
| T-03 Changed evidence | Affected support reopens. Independent surviving support keeps its original subject. | PC-S12 row 3; Q14/Q16; ACT §7 |
| T-04 Uncertain effect | Reconcile before repetition. `completion_unknown` is kept apart from `not_effected`. Missing history is not evidence of no effect. | PC-S12 row 4; Q17; ACT §3 Effects |
| T-05 Declared capacity | Size, unit, boundary and comparison are recorded before reading. Unmeasured host context stays outside the claim. No clipping. | PC-S12 row 5; Q18; ACT §2 step 3 |
| T-06 Sufficient non-ticket carrier | A one-run task uses a run contract with no invented durable ticket. | Q18; TK §5 carrier selection |
| T-07 Missing admission or write authority | Treated as a material boundary. Obligations are retained in the named surface. No ticket is created without authority. | SDLC-10; TK §5; stdo-work step 5 |

### 2c. Purpose Context (index and runtime behaviour)

| Case | Expected behaviour | Source |
|---|---|---|
| PC-01 Manifest pin | Changed catalog, index, schema or runtime bytes refuse under the old pin. | PC-R01 |
| PC-02 Rebinding to A | The `sdlc-workflow/1` source closure equals A's installed members by membership, order and bytes. Development-candidate identity is gone from release-target bindings. Rebuilt through the reproducible path. | PC-S06–S08; PC-R16 |
| PC-03 Drift refusal | A changed source, recipe, purpose, query or default projection refuses before reliance. | PC-S07 |
| PC-04 Historical entries | P1 (68 rules), 3.0.4 v2 and 3.0.5-rc.1 v2 stay byte-identical, and no consumer migrates. | PC-R05; PC-S09; PC-R15 |
| PC-05 Python release-target entry | Either a `python-pure-refactor/2` entry over A exists with its own exact binding, or its absence is declared and older consumers keep their exact entries (see G-05). | PC-R15/R16 |
| PC-06 Coverage honesty | `covered: true` only with an external exact assessment and no material unknowns. Otherwise `covered: false` or trial-only. | PC-R06; PC README |
| PC-07 Unknown facts | Missing, null or ill-typed deciding facts return unknown or incomplete. | PC-R03; PC-S05 |
| PC-08 Budget | Over-budget requests produce no partial directory and no truncation. | PC-R07 |
| PC-09 Runtime independence | No model, provider, representation, Axiom or Lean dependency. A non-Python purpose needs no representation runtime. | PC-R08; PC Product |
| PC-10 Workflow content | The index retains PC-S02/S03/S04/S11 duties. No added boolean makes retention or restart optional. The family's meaning is preserved. | SDLC-WORKFLOW body |

### 2d. Skills

| Case | Expected behaviour | Source |
|---|---|---|
| S-01 (Q01) | Context-only fresh install verifies on both Codex and Claude without visual components or Lean. Native frontmatter is bound to the selected method. | SK-01/02/14 |
| S-02 (Q02/Q03) | The installed adapter reaches the pinned Purpose Context, selects and consumes the matching index, and checks it. Mismatch, stale and unknown controls refuse. | SK-05/06 |
| S-03 (Q04) | The receipt removes only roots it owns. No global skill-directory mutation. Historical installs are not migrated. | SK-10/11 |
| S-04 (Q05) | Explicit visual selection exposes the visual path. Without it, context use works fully. | SK-14 |
| S-05 (Q06) | Automatic pickup and explicit invocation are separate claims. If unobserved, they are not claimed. | SK-12 |
| S-06 (Q07) | Native intake, direct Writer, handoff and review, drift continuation, interrupted effects and status are observed, not inferred from wrapper inspection. | SK-03/08 |
| S-07 Package identity | The released Skills package is versioned `3.1.0-rc.1` and pins exactly the final B bytes of Purpose Context and `a_c`. Development builds stay labelled unversioned. SK-10 is reconciled for released bytes. | SK-10; R §7 |
| S-08 Method binding | The installer records which native method it binds (3.1.0-rc.1, or the consumer's selected basis). No adoption on the target's behalf. | Skills PRODUCT, Selected methodology |

### 2e. Visual-only path (Representation Tools, STDO Representation, Axiom Indexer)

| Case | Expected behaviour | Source |
|---|---|---|
| V-01 | The `a_c` public visual package runs without retired modules. `project`, `code` and `explore` work. | AC-R-V06; PU-08 |
| V-02 | Stale inputs refuse reuse, and prior models are preserved. | AC-R-V05; PU-06; CR-06 |
| V-03 | Structural checks are reported with their subject and limits, and no fidelity claim is made from them. | AC-R-V04; PU-04 |
| V-04 | STDO Representation is either a source-matched model of A, or the cohort is explicitly narrowed (G-01). | R §7 item 5; REQ-P-CURRENT-MODEL |
| V-05 | Axiom `convert`/`restore` reproduces the exact model value. The receipt binds its digests. Missing mappings or duplicate IDs refuse. | REQ-P-MODEL-CONVERSION |
| V-06 | Axiom has no active `join`, `project-registry` or authoring skill. Projection stays separate from prompt construction. | Axiom PRODUCT; REQ-P-PROJECTION |
| V-07 | Historical generated artifacts and earlier releases stay byte-identical. | All three Products' AGENTS files |
| V-08 | Any integrated `a_c` qualification claim needs an assessment of the non-STDO visual path. | PU-09 |

### 2f. Cross-Product interactions (these must be assessed across Products, not per Product)

| Case | Expected behaviour |
|---|---|
| X-01 Pin chain order | Final PC bytes → PC `PUBLIC_MANIFEST` → Skills `DEPENDENCIES.json` and composition contracts → Skills package → cohort record. A pin is refreshed only after the upstream public bytes are stable (PC README; PURPOSE-INDEX-CONSUMPTION). Falsifier: a Skills pin that does not equal the released PC manifest digest. |
| X-02 Index → A | Every release-target index binds A's installed manifest (which includes the tag object). A change to A cascades into regeneration of B and an applicability check (R §7). |
| X-03 STDO-v3 → Axiom | The historical mechanical-evaluation pin to `axiom_indexer/v2.5.1-rc.2` (A_C_DEPENDENCY) stays distinct from Axiom 3.1.0-rc.1 being a cohort member. Cohort membership must not rewrite or imply that pin. |
| X-04 Native bundle circularity | Native A cannot contain final B bytes of Skills, PC or `a_c`. If the native distribution keeps a bundled tool or Skills source set (TOOL-01 precedent), it is either historical or development-labelled, or removed with an R §9 disposition. |
| X-05 Default projection across three frame bases | The v3, PC and Skills frame bases all cite projection `a04335…`. If release bytes differ, all three need refreshed identity and adoption applicability (v3 frame basis, Selected SDLC Default). |
| X-06 Root `$stdo-context` route | The root adapter path resolves the released Skills adapter to the released PC canonical skill (root AGENTS). |
| X-07 Visual optionality | Skills → `a_c` is optional. PC has no edge to `a_c` or Axiom. STDO Representation → Axiom and `a_c` (Product Definitions). |
| X-08 Document consistency | v3 README says the workflow index has "35 rules over 12 exact source members". PC and Skills READMEs say "40 rules over 12 source owners". Reconcile before A or B. I do not decide which is right. |

### 2g. Migration (five-Product 3.0.5-rc.1 → six-Product 3.1.0-rc.1)

| Item | Expected declaration |
|---|---|
| M-01 | Product map: STDO v3, STDO Representation, Axiom Indexer and STDO Skills continue. `a_c` Implementations continues as "Representation Tools" under the same definition ID. Purpose Context is new, with no predecessor release; its lineage is the extracted comparison engine. |
| M-02 | Retired claims each get the "intentionally removed" disposition, citing the Nov 12 owner wording: Lean and proof tools, registry, F_D, T-020 C1–C7, PU-05/07, SK-13, axiomatize-corpus, join and project-registry. They are recorded as "withdrawn unsatisfied", not as satisfied. |
| M-03 | Moved responsibility (the context route moved from `a_c`, STDO Representation and the Skills-owned engine to Purpose Context) gets "superseded", naming the replacement locus. |
| M-04 | Consumers: existing installs, the 3.0.5 selectors and Product Definition bases are unchanged. Adoption happens only through the R §4 digest-bound plan. |
| M-05 | The archived five-Product constructor and tests are not used as the current acceptance gate (root AGENTS). |

---

## 3. Prior evidence: when it applies, what must be rerun, what may be reused

**Applicability test.** Prior evidence E may support a release claim C only if all of the following hold (ASSURANCE, change impact; ACT §7; EV §2–3; PC-S09):

1. C's predicate and scope are within E's original claim.
2. Each dependency material to E's assertion and execution is byte-identical in the release subject, or covered by an established preservation argument. A changed hash alone proves neither invalidity nor equivalence.
3. None of the three invalidators has occurred: material input change, changed basis, or a declared revising observation.
4. Actor and host conditions still match where the claim depends on them.
5. The original subject stays named. Reuse is recorded as an applicability relation, not a relabelling.

Any judgment that must be independent cannot be satisfied by reusing an author's judgment. Shared mechanical evidence may be reused.

**Mandatory reruns (bound to final identities, so no prior evidence can apply):**
- R1: A manifest and fresh-store install, verify and resolve; frame reproduction at A.
- R2: Index regeneration and freshness against A; PC manifest-pin controls on released bytes.
- R3: Package, install and remove (Q01, Q04) on the released Skills, PC and `a_c` packages.
- R4: Post-tag, pre-push gate; remote absence and lease binding; atomic push; remote readback.
- R5: Public download digests and fresh public install.
- R6: Independent review bound to the exact local tag objects and B.
- R7: Exact-subject external assessment for any index that claims `covered: true`.
- R8: DOC-06 and TOOL-05 if those assets are shipped.
- R9: Dependency sweep for retired modules on the packaged bytes.

**Reuse that may be allowed, subject to the test above:**
- U1: Source-first semantic assessments of the SDLC default and of the ticket/context placement, if the projection is still `a04335…` and its deciding owners at A are byte-identical to the assessed subject.
- U2: Earlier actual-use trials (the SDLC nine-case trial, continuation observations). These need proof that the skill text and received context material to each decision are unchanged, plus matching actor and host conditions. Otherwise rerun only the affected cases. A new index identity with identical rendered rule content may support retention of behavioural evidence, but cannot carry over a coverage verdict.
- U3: The `python-pure-refactor` assessment over 3.0.5-rc.1, only as cited support for a new exact-binding assessment if the sixteen owners are byte-identical. It is never a transferred verdict.
- U4: Historical 3.0.4 and 3.0.5 release evidence stays on its own subjects and qualifies nothing in 3.1.0-rc.1.

**Explicitly not required:**
- Method self-qualification (EV §7) or a whole-method reliability proof for these bounded claims.
- The C3 six-criteria acceptance or the 2.5.1-rc.2 PREDECESSOR_CLAIMS inventory. Both are historical subjects.
- COMPLETE_RELEASE's Lean, unified explorer and proof components (historical, per its own header).
- A universal review round or full rerun after every repair. Rechecks are triggered only (QF-02).
- An independent review of every local step (TK UP-007).

---

## 4. Gaps and ambiguous obligations that need a declared disposition before final claims

| ID | Issue | Why it matters | Disposition needed (by whom) |
|---|---|---|---|
| **G-01** | R §7 says a "release-matched STDO stack" closed cohort contains Axiom mechanics, STDO Representation, and an "a_c.STDO … map or equivalent semantic index" regenerated whenever any covered source member changes. A stale index "cannot accompany the changed source". The current STDO Representation sources say "This alignment does not regenerate them". | The activation explicitly applies R §7, and the six-Product relation includes the STDO corpus, Axiom and Representation. Regenerating a *visual* source-occurrence model would be consistent with REQ-P-CURRENT-MODEL and would not revive a retired route. | Root or owner. Either (a) build a source-matched model of A in B, validated through Axiom, with its fidelity standing declared; or (b) explicitly narrow the claimed scope under R §8 and record the cohort as not a complete §7 stack. |
| **G-02** | Native-bundled tools and documentation (TOOL-01 Lean, `a_c` and Skills sources; DOC "Lean proofs") versus the activation's "no Lean runtime dependency", plus the A/B circularity (X-04). | Both "runtime dependency" and "shipped historical asset" are possible readings. | Owner. Retain as labelled historical, or remove under R §9 with owner wording. |
| **G-03** | Purpose Context has no release namespace. The namespaces for `a_c` and `stdo_skills` are not in the R §2 list, which names only three. | R §2 requires assignment by release authority. | Release authority record. |
| **G-04** | Acceptance versus publication: R §8 needs human acceptance of the exact immutable identity. The activation gives conditional publication approval but names no acceptance proxy. | Risk of recording "accepted" without an owner act on the exact cut. | State acceptance status explicitly, or name an explicitly admitted bounded proxy. |
| **G-05** | Which release-target indexes must exist at A. `sdlc-workflow/1` clearly must. For `python-pure-refactor/2` over 3.1.0-rc.1, either a new entry is produced or its absence is declared. | PC-R15/R16 and the activation's "release-target indexes bind the actual final cut". | PC owner and Root. |
| **G-06** | Whether GitHub "Latest" and normal-release marking are inside publication scope. "Existing public-release convention" suggests yes. | A host flag is not qualification (R §3). | Declare in the release record as publication scope, not as a claim. |
| **G-07** | The status of `SDLC_DEFAULTS.md` and the TICKETS §5 clarification inside installed standards: normative law, or projection and guide? | It decides the R §9 disposition (conserved or superseded) and how consumers should read the member. | Owner or common pen, with independent review of changed common meaning. |
| **G-08** | Severity scale for my later findings. I assume the 1–5 convention selected in the 3.0.4 review flow (QF-09). Purpose Context adopts no cutoff. | stdo-review requires the scale the Product binds. | Confirm per Product. |
| **G-09** | Re-tagging an unpushed local tag after review. R §3 "published RC immutable" does not strictly cover local tags. The activation forbids force-moving immutable tags. | Any change to A changes the manifest and every binding in B, invalidating the review bound to it. | Declare: invalidate all identity-bound evidence and rerun R1–R7 for the affected parts. |
| **G-10** | Authorship map. Claude-family content may exist in the changed subject (the Claude tenants). | Default: same-family activations are not independent (EV §3). | Declare authorship per changed path, or a family-independence policy for those parts. |
| **G-11** | Host pickup (Q06) and automatic triggering. | Not required unless claimed. | Narrow the claim, or observe it. |

---

## 5. Evidence I need for the later candidate assessment

1. **Missing governing sources**, as exact path and section:
   - The "preceding recommendation" the owner accepted, which sets accumulated scope.
   - The 3.0.4 sections not supplied: R lines 82–143; R §1 header remainder; EV §6; `EXECUTIVE_BASELINE` §5 and §12 (recheck triggers, severity anchors); `REFERENCE_FRAME` §11 and §13; `FOUNDATIONS` §4 (Results, Conjunction, Change impact); `SPEC_METHOD` §2, §4, §6; `PRODUCT_DEFINITION` §4 and §11; TK §4 required fields.
   - `build_tenants/common/standards/SDLC_DEFAULTS.md` (projection `a04335…`) and the changed TICKETS §5 text.
   - `purpose_context/skills/stdo-context/references/method-targets.md` and `sdlc-workflow.md`.
   - `stdo_skills/specification/DESIGN.md`, `composition/PRODUCTS.md`, `DEPENDENCIES.json`.
   - `v3/development/TOOLS.md`; root `DEVELOPMENT.md`.
   - The 3.0.5-rc.1 `RELEASED.md`, its cohort record and its namespaces.
   - The Nov 12 alignment `ACTIVATION.json` (owner wording for removals).
   - The SDLC_DEFAULTS and TICKET_CONTEXT activations, plus their existing review and actual-use records with exact subjects.
2. **Frozen subject identities:**
   - A: commit, local tag object, tree, subtree tree, installed manifest digest, fresh-store path.
   - B: commit, per-Product subtree trees, member inventories, local child tag objects, selectors, branches.
   - The cohort record bytes.
3. The predecessor disposition record, per claim across the native corpus and the five predecessor Products, with modal comparison evidence for "conserved".
4. Index regeneration receipts (inputs, recipe, generator, outputs), catalog diffs, byte-identity proof for historical entries, coverage-standing records and external assessment bindings.
5. Retained actual-use records for every case in §2 that is claimed: request, packet, context identity and bytes, output, effects and assessment. Unperformed cases must be listed.
6. Package, install and remove receipts for both hosts; dependency sweep output; manager verify and resolve output; DOC and TOOL checks if applicable.
7. Pre-push evidence: fetched remote object IDs or absence for every ref, the exact push command and result, and remote readback with types and peels.
8. Public asset digests, GitHub release readback and the fresh public install transcript.
9. Before-and-after state proving RP-04 preservation: main worktree, ref list, installed and global stores.
10. The authorship map (G-10) and producer metadata for every independent review.
11. Final `RELEASED.md` and `RESULT.json`.

**Re-entry.** Gaps G-01 through G-11 go to the Root release coordinator and the owner for the dispositions listed. This return makes no candidate judgment.



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/assessment/ROOT_CONSTRUCTION_DIRECTION.md
SHA256 8f6325797d4801adfdfd96c7ee6f751f23a46cb3774af2b9627eb3a546c2851a; 1480 bytes

# Root construction direction after source-first expectations

Origin: direct Root message to this assessment operator after the recorded Claude source-first return. This is a construction/claim-boundary direction, not evidence that the planned artifacts exist or a candidate review verdict.

Verbatim:

> Source-first G-01 understood and accepted as release construction obligation. Root is preparing a fresh current native-A-bound visual artifact through retained Representation Tools, explicit source inventory, declared visual scope and coverage/residuals; prior3.0.5 model/proof remains history and will not be relabelled. Six-Product package claims current bounded visual documentation plus Purpose Context declared purposes, not universal semantic representation/whole-method qualification. Method Writer is replacing old native docs/tooling with current verified acquisition routes. Keep final review finite against your recorded expectations; awaiting actual final A/B subjects.

Assessment continuation: G-01 is addressed as a planned construction path. Its candidate predicate remains unperformed until the exact A-bound visual asset, inventory, source fidelity standing, declared residuals and package/public evidence are supplied. The historical 3.0.5 model/proof retains its own subject. Native old documentation/tooling disposition is assessed on final bytes and the explicit migration record. No extra whole-method or universal visual-completeness claim is added.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/releases/3.1.0-rc.1/RELEASE.md
SHA256 b4c0c8aece6fb11fbf326d829a15322b3d39a092cf806b6137e2d64028deceea; 5428 bytes

# STDO 3.1.0 release scope

The owner's 2026-11-15 instruction selects this six-Product release-matched
cohort at exact cut `3.1.0-rc.1`, on public version line `3.1.0`. This relation
supersedes the historical five-Product distribution for this successor only.
It preserves each Product's definition, namespace, inventory and qualification
boundary. The root is a coordinating repository, not a seventh Product.

| Product | Release namespace | Current delivered responsibility |
|---|---|---|
| Specification Methodology | `specification_methodology` | Complete native standards and plugin; default SDLC and ticket/context continuity |
| Purpose Context | `purpose_context` | Exact-source purpose indexes, selection, construction and verification of received context |
| STDO Skills | `stdo_skills` | Explicit Codex/Claude bindings and installation over selected Method, Purpose Context and optional visual provider |
| Representation Tools | `a_c` | Source-linked visual generation, model/carrier preservation and offline exploration |
| STDO Representation | `stdo_representation` | Identified visual documentation of the current native source, with declared coverage and residuals |
| Axiom Indexer | `axiom_indexer` | Mechanical validation, reversible conversion and explicit visual projection |

All six use the suffix `3.1.0-rc.1` within this explicitly selected cohort.
Equal version text does not transfer meaning, authority or acceptance between
Products. Their construction definitions continue to select installed STDO
3.0.4; publication does not adopt 3.1 for an existing consumer.

## Release claims

The Method's existing context/restart/reuse rules remain owned by ACTIVATION;
TICKETS explicitly applies them through the selected work carrier. The default
workflow connects work, incremental QA, causal diagnosis, the appropriate
requirements/design/implementation re-entry, affected verification and closure.
Named acceptance/release boundaries retain their own conditions. Context,
handoff and chat are not rival work-state authorities.

Purpose Context ships separately scoped `python-pure-refactor/2` and
`sdlc-workflow/1` entries over the actual native 3.1.0-rc.1 cut. A matching index
does not establish an arbitrary query's semantic coverage: supplied assessments
bind exact subjects and facts, and unknown facts/verdicts remain explicit.
Historical indexes and assessments keep their original bindings.

Skills delivers the canonical Purpose Context route through both supported
local host layouts, preserving native workflow ownership and exact dependency
pins. Explicit invocation, installed-layout behavior and automatic host
discovery are separate claims; only observed modes are qualified.

Visual Products deliver source-linked documentation and mechanics. The current
STDO visual artifact declares its exact source, selected interpretation scope,
coverage, omissions and unresolved meaning. Structural validation, round-trip
equality and source navigation do not establish whole-method semantic
completeness. Historical 3.0.5 model/proof artifacts are not relabelled as 3.1.
Lean, proof execution, registry authority and the retired context-support
runtime are outside the new delivered capability. See [migration](MIGRATION.md).

## Construction and qualification

The exact native predecessor is `specification_methodology/v3.0.5-rc.1`,
commit `b5b00b896d44804e0f5d615a9bc23a02345888b3`. Source construction first
freezes the current native payload. Native commit/tag A and a verified private
installation then supply the manifest used by both purpose indexes and the
current visual source binding. Derived Product inventories and dependencies
are frozen in source carrier B before their annotated tags are created.

The native manifest is produced by the existing manager against the actual
annotated tag, never predicted from a version string. The external cohort
record binds A, B, all Product subtrees/member inventories, public assets and
the complete annotated-ref graph without a self-containing digest.

Qualification applies to these declared capabilities and their changed causal
paths. It includes predecessor conservation/removal dispositions; an actual
independent-family semantic assessment; meaningful existing component controls;
current installed Method/Skills/context/visual checks; exact package identity;
and fresh public acquisition/install/readback. Earlier valid mechanical and
behavior observations may be reused only with their validity conditions and
unqualified modes preserved. A release does not assert universal context fit,
general productivity improvement, new formal proofs or whole-method/C3
qualification.

Before publication every immutable ref requires remote absence and every
mutable destination an exact expected object. One atomic push publishes the
complete declared carrier/ref set; no sequential fallback or moved immutable
tag is permitted. Public assets are read back and installed from their actual
downloaded bytes. A normal GitHub release uses the exact RC identity; a second
stable cut is unnecessary. Exact-cut acceptance and consumer adoption retain
their separate authority and evidence requirements.

The [input descriptor](COHORT_INPUTS.json) is a construction selection, not a
completed qualification receipt. The release's `cohort-release-v3.1.0-rc.1.json`
asset and retained release record carry actual immutable identities and results.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/releases/3.1.0-rc.1/MIGRATION.md
SHA256 b9a21fed317949a294ca79df21a4efc3f0271ada8f43cf1810a00748d17d55d2; 3598 bytes

# Moving from STDO 3.0.5 to 3.1

Install the new release into fresh, explicitly selected locations. Existing
Product Definitions, native installations and receipt-owned Skills remain on
their selected releases until their own migration is performed. Preserve the
old receipt and historical evidence. Never repair an immutable old package in
place or silently reinterpret an old query/model/proof under new sources.

| Previous responsibility or route | 3.1 disposition and consumer action |
|---|---|
| Native STDO law and `stdo-work`, `stdo-ticket`, `stdo-review`, `stdo-status`, `stdo-help` | Conserved with the declared continuity/default improvements. Install the exact new native cut, review its adoption plan and explicitly select its default frame where applicable. |
| Native combined tools/source archive and bundled Lean/proof/documentation views | Superseded by separately inventoried current Products and current installed acquisition guidance. Old views/proofs remain on the exact old release. They are not current 3.1 evidence. |
| a_c-based agent context, task-context/support/formal orchestration | Removed from current Representation Tools. Use the independent Purpose Context Product and its canonical `stdo-context` route through STDO Skills. |
| `stdo-representation` agent skill and registry-based context selection | Removed. STDO Representation now supplies identified visual documentation; context selection belongs to Purpose Context. |
| `axiomatize-corpus`, Axiom `join` and `project-registry` | Removed from current ordinary-agent discovery. Retained Axiom `validate`, `project`, `convert` and `restore` serve explicit mechanical visual operations. |
| a_c model/carrier and visual source navigation | Conserved within the declared visual purpose. Use the current provider and a source-matched artifact; preserve old artifacts as history. |
| Open legacy T-020/formal/context obligations | Withdrawn unsatisfied under the earlier owner-directed scope change. Their removal is not reported as delivery or proof. |
| Python and SDLC purpose indexes | New entries bind the actual 3.1 native manifest. Select the consumer's actual complete method/purpose and facts. Old indexes remain available only for their exact old consumers. |
| Semantic assessments, test evidence and closure | Reuse only when the exact claim's validity conditions hold. A new version/hash does not carry an old query verdict or invent satisfaction. Reassess changed source/subject/query relations. |
| Skills installation | Use the release package mode and its new receipt-owned `stdo-skills` distribution. Development installs retain their separate `stdo-skills-dev` receipt/mode. Use the old receipt's verify/remove procedure before an overlapping replacement. |
| Five-Product `stack_release.json` and old `cohort-update` workflow | Historical contract. The six-Product 3.1 cohort is selected by its own descriptor and assets; the old updater does not migrate this successor implicitly. |

Purpose Context and the visuals serve different consumers. Code-build and
workflow constraints require no visual model or Lean installation. A diagram
adds no constitutional authority; the exact native source remains deciding.

Read the current package's `stdo_skills/scripts/INSTALLATION.md` and
`stdo_skills/GETTING_STARTED.md` for the explicit install and use sequence.
The native installed `plugins/spec/references/GETTING_STARTED.md` gives the
verified acquisition route. Download filenames and hashes are recorded in the
release's exact cohort asset; no mutable local checkout is an installed basis.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/a_c/specification/PRODUCT.md
SHA256 360871cd968cb36fbbe90f10e6b9a497c6b21417f2c7540d1ae06ad89b291d23; 2101 bytes

# Representation Tools Product

## Product boundary

Stable definition `urn:stdo:product-definition:a-c-implementations` owns generic
source-linked visual documentation. The retained Graphify tenant implements
source generation, declared model/carrier preservation, offline exploration,
source navigation and additive code/test-source overlays. STDO Representation
owns its STDO-specific source interpretation; Axiom Indexer owns its separately
selected mechanical conversion/projection. Purpose Context owns purpose indexes.

## Public behavior

The public router is `scripts/ac.py`: `project`, `code`, `explore`, `graph`,
optional `upstream`, and explicit isolated `bootstrap graphify`. A project build
binds its definition, source inventory and hashes, author submissions and
machinery. Reuse refuses changed inputs. A model check verifies declared structure
and references; it does not discover missing meaning or accept source fidelity.
The visual overlay preserves the base and distinguishes observations from
attributed mappings, unknown endpoints and unexecuted test-source links.

## Current source and history

Active runtime no longer imports Lean/formal, support, registry or task-context
implementations. Prior proof-selected runs require their exact archived runtime;
they are not silently reinterpreted as current visual runs. Retired code, tests,
requirements and original dirty source are preserved in the alignment archive.
Existing generated artifacts, installed caches and immutable releases remain.
Version 3.1.0-rc.1 participates in the exact six-Product cohort. Its public
runtime is inventoried by PUBLIC_MANIFEST.json; publication/qualification
follow that cohort's evidence. Existing consumers require explicit adoption.

## Product disposition authority

The owner directs this scope and retirement; Root binds scoped Writer effects.
The current exact construction basis remains STDO 3.0.4. Earlier T-020 C1–C7
context obligations are withdrawn unsatisfied. The completed comparison remains
evidence for the separate context direction, not a visual capability acceptance.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/a_c/specification/requirements/project-use.md
SHA256 ca5fa75d647e7669c12b7864e29f9291e8c6f72bcf9c3e6dee878b8fd21ac6a7; 1225 bytes

# Visual project use

| ID | Current required behavior |
|---|---|
| PU-01 | Bind the caller's Product Definition, exact method/source cut and selected local source; refuse escaping or redirected source. |
| PU-02 | Accept source-grounded authored records with coverage dispositions, assumptions and residuals; discovered code edges do not become normative relations. |
| PU-03 | Produce portable full-record documentation with constraints, conditions, exceptions, source links and 2D/3D navigation; offline reading needs no authoring stack. |
| PU-04 | Report structural validation with its exact subject and limits; no source completeness or proof claim. |
| PU-06 | Refuse stale reuse and preserve previous models and evidence. |
| PU-08 | Supply documented portable visual entrypoints and explicit optional extraction dependencies. |
| PU-09 | Assess the actual non-STDO visual path and source fidelity before integrated qualification claims. |

PU-05 agent-context delivery and PU-07 workflow/recipient composition are
withdrawn from this Product, unsatisfied where previously open. Their original
text remains archived. A public visual path does not grant mutation, access,
semantic acceptance or new release standing.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/a_c/specification/requirements/code-realization.md
SHA256 096c4c0a6f5cbd380f860e78dd031614674a2b9ab4bf176f9fd48b02e52bcff2; 4417 bytes

# Code and realization traces

This capability connects an exact source representation to selected project
code and tests. It refines the [visual requirements](README.md) and [project use](project-use.md). Acquisition remains confined to explicit local source selection; no lifecycle, context delivery or proof capability is introduced.

## Required outcomes

**CR-01 — Exact selection and lawful acquisition.** Bind the nominated Product,
exact base representation and its source basis, and explicitly selected local
code/test files with their content identities. Directory selection records its
member set. Acquire only within the selected scope and existing permissions;
an import, graph edge, nearby folder or common repository creates no implicit
route into another Product. Unsupported acquisition routes refuse.

**CR-02 — Additive representation.** Supply a versioned code-and-trace overlay
bound to that exact base. Preserve the existing native model and carrier bytes,
record identities and declared dependency semantics. An unknown overlay version
or inconsistent base binding refuses. Existing validation and historical evidence
retain their original subject and proof scope; adding an overlay does not extend
them to code or trace assertions.

**CR-03 — Distinct observations and interpretations.** Identify extracted
structural observations separately from caller-attributed F_P mappings such as
`implements`, `supports` and `tests`. Preserve the extractor's supported scope
and each mapping's declared author, origin and meaning. Unknown or ambiguous
endpoints, unsupported files and failed extraction remain inspectable; they
cannot be silently resolved by matching names or presented as an empty successful
extraction. A discovered call/import is not a normative dependency. No structural
observation or trace link establishes implementation correctness, requirement
satisfaction, test execution or result, semantic admission or formal proof.

**CR-04 — Recoverable identities and provenance.** Preserve record and directed
relation identities, distinct parallel/self-relations and repeated occurrences.
Bind code observations and mappings to exact source content, available source
coordinates and producing inputs/tools. Retain unresolved endpoint descriptions
and alternatives without substituting an arbitrary resolved target. Readers can
distinguish observed source, caller assertions and unavailable evidence.

**CR-05 — Readable trace navigation.** The same portable offline reader can
follow a selected requirement to its mapped code and tests, inspect the linked
source and return through the reading trail. Its views distinguish source-model
relations, code observations and F_P mappings, preserving selection when changing
renderers or moving between Files and logical views. Display missing or unresolved
links and extraction coverage honestly. No mapped test means only that no such
link is available in this selected representation, not that the project has no
test. Reading the export needs neither a service nor the extractor installation.

**CR-06 — Currentness and reuse.** Bind reuse to the base model/source, selected
code/test bytes and membership, mapping assertions, overlay profile and relevant
extraction/rendering machinery and options. A material change invalidates the
affected reusable result; report its scope and retain prior evidence as history.
Rechecking identity does not renew a semantic judgment or grant new access.

**CR-07 — Public-path evidence.** Provide documented public construction and
inspection operations using the existing project workflow. Independently assess
the actual supported extractor at an exact pinned version and the generated
reader, including source-to-observation samples and requirement→code→test
navigation. Exercise unresolved/ambiguous endpoints, unsupported/failed extraction,
parallel relations, base preservation and stale-input controls. Report checked
properties, coverage and remaining uncertainty. Semantic fidelity, test outcomes,
whole-project qualification and any quality or cost benefit require their own
evidence under the existing AC-R and PU contracts.

[T-019](../../.ai-workspace/tickets/active/T-019-code-representation.md) selects
the first public CLI/reader slice. Concrete languages, extractor, schema, commands
and storage belong to tenant HOW; this common contract does not mandate Graphify.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/specification/PRODUCT.md
SHA256 80d53d5948b60782b0cd56789535c8ef3ec244f3c35a2a0abf361dd925609e0b; 2493 bytes

# STDO Representation Product

## Product terms

Stable definition `urn:stdo:product-definition:stdo-representation` owns visual
documentation of exact STDO sources: attributed source interpretation, declared
coverage/residuals and identified visual artifacts. Source STDO remains authority.
Counts and valid carriers do not establish complete or faithful interpretation.

## Axiom Indexer Product dependency relation

The separately owned Axiom Indexer supplies model conversion/restoration,
source-bound validation and visual projection. Its exact selected inputs,
configuration and provider bytes accompany an output. It does not resolve a
context registry or select agent instructions for this Product.

## Exact dependency bases

Version 3.1.0-rc.1 uses separately inventoried public providers. Existing
published artifacts retain their original exact provider/release pins. A source
change does not carry old qualification forward or rewrite those pins. The 3.1
cohort binds and assesses its own full provider and artifact inventory.

## a-c provider relation

Representation Tools (`../a_c/stdo_a_c.json`) supplies source generation,
structural model/carrier checks, offline explorer and additive code-source
navigation. No Lean, workflow support or registry/context route is imported.
The STDO-specific model and coverage judgment remain this Product's responsibility.

## Current boundary

The old `skills/stdo-representation` bundle and registry data route are archived
outside active source. Purpose Context is a separate Product; STDO Skills owns
its adapter. Existing visual artifacts and prior release evidence are unchanged.
The current 3.1 artifact is freshly authored from the native cut recorded in
`build_tenants/a_c/representation/stdo-v3.1.0-rc.1/SOURCE_BINDING.json`. It
provides complete source-section navigation for its declared members plus
selected SDLC/work-carrier/context annotations, with explicit unrepresented
meaning. It does not rebind the old models or migrate installed bundles.
The exact artifact and public provider pins are in PUBLIC_MANIFEST.json; the
cohort records publication and independent assessment standing.

## Product disposition authority

The owner selects visual-only direction; scoped Writer changes and exact archive
receipts implement the November 12 retirement. Retired context/registry/formal
obligations are withdrawn unsatisfied where open, including prior T-020 work;
their historical bodies do not remain active Product mandates.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/specification/requirements/REQ-P-CURRENT-MODEL.md
SHA256 107111ce83ec7bfd1a085041fc8d521ded23d329e13d1440e7fced21a1c6dcea; 430 bytes

# REQ-P-CURRENT-MODEL — Visual model and views

Preserve one identified source-occurrence model and reversible carrier for each selected source cut. Derive visual views from that model, preserving complete declared records and source links. An optional Axiom conversion must round-trip the exact model value. The former model-plus-registry successor is withdrawn; no authoritative registry pair remains in the current contract.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/specification/requirements/REQ-P-CANDIDATE-VALIDATION.md
SHA256 80a18d022dced000115d8544ff8f7ad9ebc5fa6e7113dc50fdc4d85a1b114fda; 449 bytes

# REQ-P-CANDIDATE-VALIDATION — Structural validation

Use selected Representation Tools and Axiom public checks for declared schemas, identities, references, source mapping and reversible preservation. Record actual subjects and failures. These checks do not establish semantic completeness, Product acceptance, proof or code correctness.

## Imported validation boundary

Provider checks retain their declared mechanical scope and exact subject.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/axiom_indexer/specification/requirements/REQ-P-MODEL-CONVERSION.md
SHA256 f196a3035f1148d3a9348533bcd65fb8cb358227f894f8af7d334a5853d011d9; 1663 bytes

# REQ-P-MODEL-CONVERSION — Preserve a declared a_c model

Status: current development visual requirement. Axiom remains the generic provider;
source owners retain semantic authoring and frame selection.

1. Accept a caller-supplied, provider-checked source-semantic a_c model and an
   explicit conversion configuration. Require unique record identities, known
   authorable families, exact grounds and a complete explicit source mapping.
   Unsupported operational populations refuse instead of silently disappearing.
2. Derive one Axiom Program preserving every declared record, identity, local
   reference, semantic field, condition, exception, latitude and residual. A
   reversible exact payload carries record/model metadata; visible statements
   expose the same authored text and exact local reference closure.
3. The caller supplies program/source/calculus identities and all frame indexes.
   The converter neither chooses applicability nor invents semantic relations.
4. Reverse conversion shall reproduce the exact input model value. The receipt
   binds model, configuration, program and reconstructed-model digests and the
   exact preservation outcome. This proves declared representation preservation,
   not source fidelity, model admission or method truth.
5. Missing source mapping, duplicate/dangling identities, invalid frame roots,
   unsupported families or altered reverse payload refuse. Successful program
   validation and projection remain separate existing public operations.
6. Preserve inputs and refuse colliding or existing output paths. The operation
   does not repair semantics, invoke models, run Lean or grant acceptance.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/axiom_indexer/specification/requirements/REQ-P-PROJECTION.md
SHA256 8dc8669ed540b79209103b91f45e277d892d506ed6e4f215ba4a5c7fb6b67238; 262 bytes

# REQ-P-PROJECTION — Visual projection

Render explicitly selected program roots and declared closure with readable source links. Preserve provenance and qualifications, refuse unknown roots, and keep visual navigation separate from agent prompt construction.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/README.md
SHA256 f5d720ef015f87606be07e793436b91a7e28a65450b100836fe978b15660ce8a; 3894 bytes

# STDO 3.1 source navigation and selected work/context relations

Open the standalone [explorer](run/generation/proposal/explorer.html). This is a
fresh source-authored visual of three exact native members: ACTIVATION,
SDLC_DEFAULTS and TICKETS. It supplies section navigation and 24 selected
SDLC/work-carrier/context annotations. It does not claim complete method
semantics, a purpose context index, execution authority or formal proof.

## Exact identities

- Represented native cut: `stdo://releases/v3.1.0-rc.1/`.
- Native manifest SHA-256: `ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa`.
- Native commit A: `c1e0faaa8437c169031a476343c764614135cd93`.
- Annotated native tag object: `fca8d5e97cf2e945196aecdc33908bb190efdca5`.
- Model canonical SHA-256: `10f810f04d4fcf99424ea99631f461e108ee8030ce8145915eb5b9dbe8d14851`.
- Model identity: `urn:a-c:generation:c8b565861ea509feddf2ebd4:model:3748671f0539880ef4616730`.

[SOURCE_BINDING.json](SOURCE_BINDING.json) identifies the native members and all
unselected standards. [GENERATION.json](GENERATION.json) binds that exact record,
the model identity and every copied source-to-native member mapping. The exact
native manifest is retained at [source/manifest.json](source/manifest.json).
The distributing Product/cohort identity is separate from the represented source.

Construction uses this Product's installed STDO 3.0.4 definition. The retained
Representation Tools model format declares its own calculus coordinate
`stdo://releases/v2.5.1-rc.2/standards/AXIOMATIC_CALCULUS.md`; this is a format
coordinate, not the represented source or construction basis. The optional
Axiom conversion explicitly locates the represented native 3.1 calculus owner
and preserves that model metadata unchanged. No Lean or formal-gate operation
is performed or needed.

## Reading and coverage

The file pane opens complete embedded source text with line numbers. Select a
record to read its entire statement, conditions, exceptions and grounds.
Authored relations retain direction and a separate “Read relation and
qualifications” action. Residual records identify unrepresented meaning and
required source re-entry. Layered, 2D and 3D views share the reading state.

There are 93 source-section navigation entries, all with explicit residual
dispositions, and 306 complete declared records: 104 concepts, 99 relations,
8 constraints, 1 latitude and 94 residuals. Processing counts establish no
semantic acceptance. [COVERAGE.md](COVERAGE.md) states the actual boundary.

One compact latitude label currently displays its generated identifier in the
graph; its complete allowed/forbidden content remains readable in the record.
The graph may require pan/zoom for connected neighborhoods. These are observed
reading limits, not missing source records.

## Construction and evidence

The existing public project `prepare`, `task`, attributed `submit`, `build`,
`status` and matching `build` reuse produced this artifact. The exact task and
answer are retained in [authoring](authoring/), public command results in
[commands](commands/) and the complete run in [run](run/). No historical 3.0.5
model or semantic verdict was imported or rebound. Producer-local absolute
paths in run receipts are provenance; open the standalone viewer anywhere, or
create a fresh run to use live project status under another producer root.

[Axiom artifacts](axiom/) retain the exact conversion configuration, public
provider pin, program, restored model, validation/map and a selected
materialized projection. Conversion preserved the exact model value.
Public mechanics, stale-source refusal and real offline Chrome reading checks
are retained in the source cohort's `visual/` work record. They are Writer
evidence; the root's distinct-family source-first assessment and cohort
qualification/publication records supply their own exact judgments.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/COVERAGE.md
SHA256 21d2b548a93e517e4340e7c3dabbce1c6f86399ede42a2ad34a535694653eb76; 3613 bytes

# Declared visual scope and residuals

This artifact represents source structure for three complete native members and
only the finite body-meaning annotations in `scripts/visual_31_annotations.json`.
That distinction applies to every count and every processing disposition.
Source STDO remains authority.

| Native member | Visual sections | Exact SHA-256 | Use |
|---|---:|---|---|
| `standards/ACTIVATION.md` | 29 | `56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d` | visual source corpus |
| `standards/SDLC_DEFAULTS.md` | 6 | `a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8` | visual source corpus |
| `standards/TICKETS.md` | 58 | `2e601f701170a7eece65153ba707cc7d857bfb7c3b9ce28c283dad199e919748` | visual source corpus |
| `standards/AXIOMATIC_CALCULUS.md` | 0 | `b39c45fd86b8f9add7d196b2974a8e5f75bf4a327cf796e362716a6b4f5776d5` | Axiom conversion calculus provenance only; not visually interpreted |

The selected visual source is 255,355 bytes across 93 sections: 29 ACTIVATION,
6 SDLC_DEFAULTS and 58 TICKETS sections. Each section has a source-linked
navigation concept, structural containment relation and explicit residual.
All 93 dispositions say `residual`; none asserts complete section meaning.
Exact line ranges and quotations remain inspectable. The pipeline's generated
[coverage.json](run/generation/proposal/coverage.json) is a processing ledger.

The 24 selected annotations comprise eight concepts, six relations, eight
constraints, one latitude and one cross-owner residual. They describe:

- authorized frame-basis selection of SDLC guidance;
- a selected work carrier's links to context acquisition, restart and reuse;
- persistent work state and a disposable actor account;
- conditional context-fit measurement and re-entry for stale derived context;
- ticket durability, retained results, owner rulings and continuation limits;
- affected reuse invalidation, required independence, bounded QA and causal triage.

Source-specific conditions and exceptions are explicit record fields. The six
authored relation kinds are marked governing only for this model's retention
contract. The 93 source-containment relations are non-governing navigation.
Neither marking grants authority or executes the represented law.

Unrepresented meaning includes the rest of the selected sections' bodies,
all 67 unselected native standards members, the semantic content of the one
auxiliary calculus member, and native plugin/tooling meanings outside this
selection. The complete native manifest and SOURCE_BINDING's unselected member
list preserve exact re-entry coordinates. Referenced owners such as FOUNDATIONS,
REFERENCE_FRAME, EVALUATION and SPEC_METHOD are not silently treated as supplied
semantic dependencies. This graph cannot substitute for the context needed by
a governing decision.

Operational transformation, traversal and judgment populations remain empty.
Source-defined operations appear only as inert authored data where selected.
No complete semantics, Product acceptance, execution, code correctness, formal
validity, Lean proof, external Graphify execution or universal UX claim follows.
All prior artifacts and judgments retain their original subjects.

Finite Writer observations cover source-member identity, complete declared
record/carrier preservation, exact grounds, conditional record reading, relation
direction/qualifications, residual visibility, stale-source refusal, Axiom
conversion/restoration/validation/projection and offline browser modes. Required
independent source fidelity and Product/release decisions remain separate.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/SOURCE_BINDING.json
SHA256 d7361b40775a12d8f5b784279fc9332aa67f7b2bdd38840f472e249fb1c2df6b; 13299 bytes

{
  "profile": "stdo-representation.native-visual-binding/1",
  "version": "3.1.0-rc.1",
  "represented_source": {
    "uri": "stdo://releases/v3.1.0-rc.1/",
    "manifest_sha256": "ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa",
    "release": {
      "commit": "c1e0faaa8437c169031a476343c764614135cd93",
      "cut": "v3.1.0-rc.1",
      "project_release_namespace": "specification_methodology",
      "project_subtree_root": "specification_methodology/v3",
      "project_subtree_tree": "31aab3cebc56ec308afb3c7312cd4b6d3315043e",
      "qualified_ref": "refs/tags/specification_methodology/v3.1.0-rc.1",
      "standards_tree": "78f97d798fabacf0b76c2e2e6a19d7257a75198d",
      "tag_object": "fca8d5e97cf2e945196aecdc33908bb190efdca5",
      "tree": "0ceecf8a106dff4c7b616849167757405f819610"
    }
  },
  "construction_basis": {
    "uri": "stdo://releases/v3.0.4/",
    "manifest_sha256": "102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b"
  },
  "provider": {
    "product": "urn:stdo:product-definition:a-c-implementations",
    "version": "3.1.0-rc.1",
    "public_manifest_sha256": "40b6e19214f40ba10ed38d90b11f98f0e62ecad6ef2e9b2ccf758ed9607f74af"
  },
  "recipe_sha256": "f11a9091ef1fd2e726d6634969e52d47adeab25c09b49525a46c8d6f678b019f",
  "generator_sha256": "f9f67e7600d8ef041a79eba60b5e8590d61e3be95ad225acc719c2d2ae6be4ba",
  "selected_native_members": [
    {
      "path": "standards/ACTIVATION.md",
      "sha256": "56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d",
      "bytes": 142205,
      "use": "visual source corpus"
    },
    {
      "path": "standards/SDLC_DEFAULTS.md",
      "sha256": "a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8",
      "bytes": 11713,
      "use": "visual source corpus"
    },
    {
      "path": "standards/TICKETS.md",
      "sha256": "2e601f701170a7eece65153ba707cc7d857bfb7c3b9ce28c283dad199e919748",
      "bytes": 101437,
      "use": "visual source corpus"
    },
    {
      "path": "standards/AXIOMATIC_CALCULUS.md",
      "sha256": "b39c45fd86b8f9add7d196b2974a8e5f75bf4a327cf796e362716a6b4f5776d5",
      "bytes": 92360,
      "use": "Axiom conversion calculus provenance only; not visually interpreted"
    }
  ],
  "unselected_standard_members": [
    {
      "path": "ASSURANCE.md",
      "sha256": "5f6740a39355314ea2a9227a8795ea68cdafb2c4c3e9b25e1d9e626eb43f27ca"
    },
    {
      "path": "CONFORMANCE.md",
      "sha256": "d49e75f64dbdc4ca787062a9044da9d74e16fa0ae7b9321c29d3c1dd4a41ee03"
    },
    {
      "path": "DESIGN_MODULE.md",
      "sha256": "741b798ea2e71797bd884817eb6903ae1a1431c97a989ab5741ffa315a3bd1e2"
    },
    {
      "path": "EVALUATION.md",
      "sha256": "b856cf04e2cf6ea0ba8b5f9de8b455a3a5f95cdb05fe7337f077f1b7547c7485"
    },
    {
      "path": "EXECUTIVE_BASELINE.md",
      "sha256": "ba089c92bee43891a509788e34b92044b0c8b0c0bb0217271724930a846e24ff"
    },
    {
      "path": "FOUNDATIONS.md",
      "sha256": "7fe9ecf257ad9aa725e7ae87ba23e406f6993dbd143c429d53df06284023127e"
    },
    {
      "path": "GLOSSARY.md",
      "sha256": "e1658700fd584ba64fa2620cadd2f44d74b0182de2f8921a6698eb6704d65da1"
    },
    {
      "path": "IDENTITY.md",
      "sha256": "c70399311010a8835b00d2a887a2451f11f66f631d6217d8df4be41751a59c08"
    },
    {
      "path": "ODD.md",
      "sha256": "06fe72e2fe11f0b63464a85fefbf29506ee81230ecc7ff4792d930abe574fbb9"
    },
    {
      "path": "POSTING_GUIDE.md",
      "sha256": "c5930cc1fa7da2324be0baaed970d35450e79f4673b77857f9f84a3fe5611ea0"
    },
    {
      "path": "PRODUCT_DEFINITION.md",
      "sha256": "7ee46438de5e4cb33cd8920814ecc90cfef95fb5eaee269f6f1a4fa389f4e523"
    },
    {
      "path": "PROFILES.md",
      "sha256": "076d5c17a06d372ed1efdc7909f9dc93c3193513ff233c48df2915810ffeffa4"
    },
    {
      "path": "README.md",
      "sha256": "e290c4839a50791d66180cbdd6efa0c28270ee1874ca33c385eb60f27e95b8b2"
    },
    {
      "path": "REFERENCE_FRAME.md",
      "sha256": "4bf3bb18f8590b8096f5ff2de6554787d29a164224be697c76640289d2096d64"
    },
    {
      "path": "RELEASE.md",
      "sha256": "eea362e1fa60fee0ed07d0fd5790f2bb8437cdcee968985c445e59e151eab628"
    },
    {
      "path": "SPEC_METHOD.md",
      "sha256": "06d5e8cbbda67952cd5671a4b01752a1eaaf30be84a790ee7e31b1551a5a787e"
    },
    {
      "path": "TRAVERSAL_OCCURRENCE.md",
      "sha256": "7809ec20f4cf47a299ea3892616b449532a568feeccb50d49d46bbc72be9cba5"
    },
    {
      "path": "UX.md",
      "sha256": "236df084b51620fcc16c042db745448540777f7dab40c92cd946e7375a4815a0"
    },
    {
      "path": "WORLD_MODEL.md",
      "sha256": "86d946ccd015857051727bae0f9cf3340bf8bebe2e166e40c554173d8ac5a931"
    },
    {
      "path": "WRITING_GUIDE.md",
      "sha256": "155cb29aee317c189f78954dd210d206206ec5e854a26086d6560288cd51e249"
    },
    {
      "path": "documentation/README.md",
      "sha256": "308aebc6dfa32783fe3655b77656bf2722cfe9124a8a43115411aeafc6080775"
    },
    {
      "path": "documentation/index.html",
      "sha256": "7168ac72c3758d620d8ced70bdd7035ce09c7c3e174973dd1169ec1b59dd5be1"
    },
    {
      "path": "examples/DETERMINISTIC_CONTRACTS.md",
      "sha256": "1ce623ad76a65b62292c842974811e10a5daa6fda672f836181a220205fbcbcb"
    },
    {
      "path": "examples/PRODUCT_COMPOSITION.md",
      "sha256": "306d197b2b983af43328eda0845776ea367530abbd73523723c3f230921df201"
    },
    {
      "path": "examples/SDLC_DEFAULTS.md",
      "sha256": "0a755316a78b1f53982671618a4172b32cbaafbcfa818b61ad1a77e624e7d606"
    },
    {
      "path": "examples/deterministic_contracts.py",
      "sha256": "5eb612aac53947a7134d941cdc0433c227637e54509c7d33de211f9ab6ad146e"
    },
    {
      "path": "frames/FRAME_INPUTS.json",
      "sha256": "66a2f33cf325de8391d827c883e50dfb4a876e9ef478310d840ab3d0bc792ec5"
    },
    {
      "path": "frames/ac-task-a.md",
      "sha256": "88280e8164b30b855673d17d44ae2f0cc7e3761917dd22703bbcacfec0f133b4"
    },
    {
      "path": "frames/acceptance-release.md",
      "sha256": "ff88a8d4e0c2d331a3d32c79740026256002d18d19e53e2fccdc9c65fe3b3d5e"
    },
    {
      "path": "frames/binding.md",
      "sha256": "3eaf9c87cd37b8c925dfc84ffc2ab6dcd376ea2296197dde831ab80de3ddfc6b"
    },
    {
      "path": "frames/bootstrap.md",
      "sha256": "7f8741bfaeb03aba16e231fac461024b27dd469b6250471690b81c6bc8ee8f65"
    },
    {
      "path": "frames/configuration.md",
      "sha256": "6f6bed1fb115bf5a0ea939a12a6124924a96e4920614b5c6fb3b688b93075d74"
    },
    {
      "path": "frames/dm-task-d.md",
      "sha256": "e53ead1a63da1675f70f4ef2b4897b7a36ee2a7c6e33f92401c735d8404e00e6"
    },
    {
      "path": "frames/eb-task-d.md",
      "sha256": "5bc43ce1c3a75844c4f2b2dac641226ae9c945c1d7a70b2bcab5d6fcfa2fbe67"
    },
    {
      "path": "frames/member-build-assess.md",
      "sha256": "c31871a0ce47f77e723a37a65304579fc95aaf157ed2d5944e267e91424d2dd4"
    },
    {
      "path": "frames/product-composition.md",
      "sha256": "239e7f9e11cd9e3f4a7c75360851901932a8eb3824ccf7a4fea4a5ae696cc73a"
    },
    {
      "path": "frames/rf-task-a.md",
      "sha256": "ed1ab2daa1503c9e3a7ef88fe309d2e91bf1b79a665ce9613e64501788507da1"
    },
    {
      "path": "frames/rf-task-b.md",
      "sha256": "7dfae737281f057b08ce079fc87b33e6f71c6ea57d03cd4dc5e035a9c23e191c"
    },
    {
      "path": "frames/stale-summary.md",
      "sha256": "147096ea768d84c727890445788d5df44f9fab7af42cf29d6c6fdac8dda4b937"
    },
    {
      "path": "frames/traversal-task-f.md",
      "sha256": "8350586b8a6e4c02a04b5064b6fd4eb33bb2625f80f7578f3a5b3090a210ccf9"
    },
    {
      "path": "schemas/installed-release-manifest.schema.json",
      "sha256": "6454ddae1268e3918785c8bf5203648723390288ef3a8d9da51b7c0193f60eab"
    },
    {
      "path": "schemas/product-definition.schema.json",
      "sha256": "fefbfa2a5508c7399968b7ebcde83854a416a07d4e794215bdddc38f5e820f0e"
    },
    {
      "path": "templates/AGENTS_TEMPLATE.md",
      "sha256": "e27610545d3b9648ca8655052a067b64f93941dd096afd8e8b25c8722b1cb20e"
    },
    {
      "path": "templates/CLAUDE_TEMPLATE.md",
      "sha256": "e27610545d3b9648ca8655052a067b64f93941dd096afd8e8b25c8722b1cb20e"
    },
    {
      "path": "templates/GOALS_TEMPLATE.md",
      "sha256": "2dc711293f5e7129389efe0e5c3ea86e111c528569e6b72dad983cdbc2c71c3d"
    },
    {
      "path": "templates/INTENT_TEMPLATE.md",
      "sha256": "85b1e6c83b30d619e9f7f8018315022b6963edaa03f908e7aac38a16d5bdab26"
    },
    {
      "path": "templates/PRODUCT_COMPOSITION_CONTRACT_TEMPLATE.md",
      "sha256": "0f1ec842a316d78b1cf755176a7e97ac6d7ae54d9d520c5f476c1d3d3f8297ef"
    },
    {
      "path": "templates/PRODUCT_DEFINITION_TEMPLATE.json",
      "sha256": "84586b352660ff960188663fc21c2634e74c6fc61cba21e9c1a1e80190f92ef5"
    },
    {
      "path": "templates/PRODUCT_TEMPLATE.md",
      "sha256": "0e5365e4c87faecbaccb20aa8a106364afcd07635ca52dffbbf4a223873256f9"
    },
    {
      "path": "templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md",
      "sha256": "d5afbc7572615e343f3600ed21c0d5edf0cce9116af9d33b7c7817fee3577f35"
    },
    {
      "path": "templates/README.md",
      "sha256": "0cad976e5d9c9b6b272aa5d417f2d4f9626b93980e26b2195ae25f7517d52438"
    },
    {
      "path": "templates/build_tenants/TENANT_REGISTRY_TEMPLATE.md",
      "sha256": "8dd5d925a82f63683c9702a5fe8732eaa4afaead626ddfe49e270fb0a79e08a9"
    },
    {
      "path": "templates/build_tenants/common/README_TEMPLATE.md",
      "sha256": "e88790f0521229ca41cadc82af434908e5d8782748ccc93eb287d0e2fb5efae8"
    },
    {
      "path": "templates/build_tenants/common/design/README_TEMPLATE.md",
      "sha256": "bfe738647de2010be9571b3f330ee249d4a644f679ce2430312fbd57d5c08d33"
    },
    {
      "path": "templates/build_tenants/common/design/adrs/ADR_TEMPLATE.md",
      "sha256": "467c02cebf87d393ee7239cc1c80d66eda9485bb251097ef8e87dc7368e19089"
    },
    {
      "path": "templates/build_tenants/common/design/adrs/README_TEMPLATE.md",
      "sha256": "cb1084ed83594af1f6a6a4103d11b0daa1c13af4c199d2baf95d100db31969e8"
    },
    {
      "path": "templates/build_tenants/variant/README_TEMPLATE.md",
      "sha256": "0236d71e75b917f4b008474478eda7662e62fc7b11cc7409b8299b2e26f3ef96"
    },
    {
      "path": "templates/build_tenants/variant/design/README_TEMPLATE.md",
      "sha256": "64237bb1766e83781e1c6e64f0eecf00e21524e007caae3a5651268cf94f7ec0"
    },
    {
      "path": "templates/build_tenants/variant/design/adrs/ADR_TEMPLATE.md",
      "sha256": "e2f820c3a7b2ed1ae8b97c96706e83ee7cb086e8bef93427813e394cb2ea0929"
    },
    {
      "path": "templates/build_tenants/variant/design/adrs/README_TEMPLATE.md",
      "sha256": "96c415caa86d9e6e5190c97f99f7fd36ae04a075e5c6da51594024728a562aa2"
    },
    {
      "path": "templates/build_tenants/variant/design/fp/INTENT_TEMPLATE.md",
      "sha256": "76e33d7a4a75d77644eec20f6d5d3611894320eab05e36580d29cf90c28a4490"
    },
    {
      "path": "templates/build_tenants/variant/design/fp/README_TEMPLATE.md",
      "sha256": "4542edc7e3a51bfba843530f1ee6b03fd3615f27a65d0f8815ae054225a5594c"
    },
    {
      "path": "templates/build_tenants/variant/design/fp/edge-overrides/EDGE_OVERRIDE_TEMPLATE.json",
      "sha256": "996e1f2cd55090519e7c487ec46333afd2994a546c15190bb11d862e3a0683c4"
    },
    {
      "path": "templates/build_tenants/variant/design/fp/edge-overrides/README_TEMPLATE.md",
      "sha256": "1432362afe35b5816259e6bef0163ffc38db6639557cd4541d2804ff04d02991"
    },
    {
      "path": "templates/docs/README_TEMPLATE.md",
      "sha256": "9c3425ff8b49c2b5573e9b8f0130b7a3e5f7d3ddcc01204aec363327e0872e7f"
    },
    {
      "path": "templates/requirements/README_TEMPLATE.md",
      "sha256": "4eacc1d3604e4859b60fc29c4bc6555fcd5de11d9ca1773258eedfb398e0f4a9"
    },
    {
      "path": "templates/requirements/STARTER_REQUIREMENTS_TEMPLATE.md",
      "sha256": "86165ef6955f5f56e096c23bb4bf07b155c75de76060d3e248fcc48b14218077"
    }
  ],
  "scope": "Complete source-section navigation for ACTIVATION.md, SDLC_DEFAULTS.md and TICKETS.md, plus these selected SDLC/work-carrier/context annotations. Navigation coverage is not semantic coverage.",
  "limits": [
    "All declared sections receive residual dispositions: their structure and source location are represented, while body meaning is not comprehensively modeled.",
    "Only the explicitly listed authored annotations assert selected body meanings. They require independent source-first assessment for their exact subject.",
    "The remaining native members and referenced owners are unrepresented meaning, not missing requirements inferred false or satisfied.",
    "No operational judgments, traversals or transformations are instantiated. No Lean/formal claim, context selection, workflow execution or code-correctness claim is made.",
    "Governing flags on the authored relations describe retention dependencies in this model; they grant no authority to a reader or tool.",
    "Historical 3.0.5 models and semantic verdicts are not reused or rebound."
  ],
  "author": "OpenAI Codex visual Products Writer; host-session source authoring; no isolated actor telemetry",
  "assessment": "Structural checks and Writer observations do not supply independent source-fidelity acceptance."
}



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/GENERATION.json
SHA256 e19512c67035e4531dbe581d91f5568a24e31f4d6dfc13f2d5148f356ccab216; 2271 bytes

{
  "profile": "stdo-representation.bounded-generation/1",
  "represented_source": {
    "uri": "stdo://releases/v3.1.0-rc.1/",
    "manifest_sha256": "ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa",
    "release": {
      "commit": "c1e0faaa8437c169031a476343c764614135cd93",
      "cut": "v3.1.0-rc.1",
      "project_release_namespace": "specification_methodology",
      "project_subtree_root": "specification_methodology/v3",
      "project_subtree_tree": "31aab3cebc56ec308afb3c7312cd4b6d3315043e",
      "qualified_ref": "refs/tags/specification_methodology/v3.1.0-rc.1",
      "standards_tree": "78f97d798fabacf0b76c2e2e6a19d7257a75198d",
      "tag_object": "fca8d5e97cf2e945196aecdc33908bb190efdca5",
      "tree": "0ceecf8a106dff4c7b616849167757405f819610"
    }
  },
  "source_binding_sha256": "d7361b40775a12d8f5b784279fc9332aa67f7b2bdd38840f472e249fb1c2df6b",
  "native_member_mapping": [
    {
      "project_source_path": "build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md",
      "native_member_path": "standards/ACTIVATION.md",
      "sha256": "56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d"
    },
    {
      "project_source_path": "build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md",
      "native_member_path": "standards/SDLC_DEFAULTS.md",
      "sha256": "a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8"
    },
    {
      "project_source_path": "build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md",
      "native_member_path": "standards/TICKETS.md",
      "sha256": "2e601f701170a7eece65153ba707cc7d857bfb7c3b9ce28c283dad199e919748"
    }
  ],
  "sections": 93,
  "annotations": 24,
  "records": {
    "concepts": 104,
    "relations": 99,
    "constraints": 8,
    "latitude": 1,
    "residuals": 94
  },
  "model": {
    "id": "urn:a-c:generation:c8b565861ea509feddf2ebd4:model:3748671f0539880ef4616730",
    "sha256": "10f810f04d4fcf99424ea99631f461e108ee8030ce8145915eb5b9dbe8d14851"
  },
  "source_manifest_sha256": "14a547910aa81f7823afc6827b8e79f37542df41d81df74fdfef5697925a5842",
  "standing": "Fresh source-authored bounded visual; independent source-fidelity assessment is separate."
}



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/assessment/final/visual/MODEL_SEMANTIC_PROJECTION.json
SHA256 1bab7a3772579c1aa0077a4f7d637f376f9d9177870c3b91b6819f478fd425fe; 317053 bytes

{"source_path":"/Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/run/generation/proposal/model.json","source_file_sha256":"bf696c10177ffc393a3ae0279b3717fccb42d06d6092afd626d8efa245bc022f","model_identity":"urn:a-c:generation:c8b565861ea509feddf2ebd4:model:3748671f0539880ef4616730","profile":"a_c.graphify.model/1","coordinates":{"context":"urn:a-c:generation:c8b565861ea509feddf2ebd4:context:source-first-proposal","owner":"urn:a-c:generation:c8b565861ea509feddf2ebd4:actor:f-p-author","scope":["urn:a-c:generation:c8b565861ea509feddf2ebd4:scope:source-corpus"]},"dependency_contract":{"attachment_families":["constraints","latitude","residuals"],"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:dependency-contract:authored-governing-relations","required_relation_kinds":["urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:applies_context_owner","urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:applies_restart_owner","urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:applies_reuse_owner","urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:bounds_continuation","urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:corrects_account","urn:a-c:generation:c8b565861ea509feddf2ebd4:relation-kind:governing:selects_guidance"]},"population_projection":{"objects":[{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","value":{"conditions":[],"definition":"Exact selected native source member. Its complete text is embedded for source re-entry; this node supplies navigation, not a complete interpretation.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"# ACTIVATION","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION","start_line":1}],"label":"ACTIVATION.md"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2f6837ca62ccf92b0d07382360091298","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"# ACTIVATION","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION","start_line":1}],"label":"ACTIVATION.md · ACTIVATION"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:400ef0f69f49a653a381946710819e61","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 1. The step","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step","start_line":27}],"label":"ACTIVATION.md · ACTIVATION/1. The step"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ba646bb3d8f1bbfc5b5422caade3b1a","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":116,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transitions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FTransitions","start_line":116}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Transitions"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:325d2070aa58719f3f446c35ca205379","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":199,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction relation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConstruction%20relation","start_line":199}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Construction relation"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148dfee42423870fdae0c364ddc8ed32","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":353,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Intake","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FIntake","start_line":353}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Intake"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1226632ad2ac42069c057a4bee0a7a71","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":391,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Execution unit","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FExecution%20unit","start_line":391}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Execution unit"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:07423eb066be1627975a960ee421930d","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":402,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FAdmission","start_line":402}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Admission"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ceada1b7bdb7a0cd2a8f54716ab041c3","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":439,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Applicability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FApplicability","start_line":439}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Applicability"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:568bae2370b2aa7dda3f25c93c2abac3","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":489,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Output","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FOutput","start_line":489}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Output"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9d49d7d28b3bef14d7c8e0c41a877cc3","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":497,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Configuration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConfiguration","start_line":497}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Configuration"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cf5901ce38d3a46343cb59a6596f6b13","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":619,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Roles and delegation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FRoles%20and%20delegation","start_line":619}],"label":"ACTIVATION.md · ACTIVATION/1. The step/Roles and delegation"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:222611d49ebb6a3da08e26ea2f6b4d39","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":693,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 2. Context construction under an envelope","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope","start_line":693}],"label":"ACTIVATION.md · ACTIVATION/2. Context construction under an envelope"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:df7b1d64f0812fa86dfd410c806570b1","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":902,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Staleness of derived surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope%2FStaleness%20of%20derived%20surfaces","start_line":902}],"label":"ACTIVATION.md · ACTIVATION/2. Context construction under an envelope/Staleness of derived surfaces"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:489ab6435409e216e3e5962b342a188f","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":938,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 3. Step results and disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition","start_line":938}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1d6224c48fe5d3c554a98c71e9b871a3","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":968,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission and activation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAdmission%20and%20activation","start_line":968}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition/Admission and activation"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d6aae782cb81aa9a98afc37213c1e50","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1002,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction availability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FConstruction%20availability","start_line":1002}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition/Construction availability"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a715f999050fe32cda11f33018b9ae9","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1049,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FDisposition","start_line":1049}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition/Disposition"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f9c599914ff44e8b4d080328ef4cdbbf","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1087,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Ambiguity outcome","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAmbiguity%20outcome","start_line":1087}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition/Ambiguity outcome"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:304e27191e740a14ff1a5360f96c192a","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1114,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Effects","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FEffects","start_line":1114}],"label":"ACTIVATION.md · ACTIVATION/3. Step results and disposition/Effects"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8112c1d9ca80c0f81b6fffbaccaf4058","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1164,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 4. Totality and refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement","start_line":1164}],"label":"ACTIVATION.md · ACTIVATION/4. Totality and refinement"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fe60a4abb04eaaf1ce62331937b96208","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1210,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FRefinement","start_line":1210}],"label":"ACTIVATION.md · ACTIVATION/4. Totality and refinement/Refinement"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6b21eeadc9a4c3f9a3ab684176865732","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1286,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Complete enclosing-relation admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FComplete%20enclosing-relation%20admission","start_line":1286}],"label":"ACTIVATION.md · ACTIVATION/4. Totality and refinement/Complete enclosing-relation admission"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:93395e367024e30ac50a227dc9423045","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Standing structural qualification","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FStanding%20structural%20qualification","start_line":1338}],"label":"ACTIVATION.md · ACTIVATION/4. Totality and refinement/Standing structural qualification"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:22033e571d79ba6f2d722b08ef8f6957","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1370,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 5. Work state and restart","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart","start_line":1370}],"label":"ACTIVATION.md · ACTIVATION/5. Work state and restart"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55444d1e0e6c8fc6ece0f11e82e42ede","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1458,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### The workspace and an actor's account","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1458}],"label":"ACTIVATION.md · ACTIVATION/5. Work state and restart/The workspace and an actor's account"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2348700f1fc9d2f2fcf11b79717c0fe5","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1519,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 6. Cost and proportionality","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality","start_line":1519}],"label":"ACTIVATION.md · ACTIVATION/6. Cost and proportionality"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:198b48795b15017f083879352e8a1a75","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1627,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Resource limits","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality%2FResource%20limits","start_line":1627}],"label":"ACTIVATION.md · ACTIVATION/6. Cost and proportionality/Resource limits"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:aeca5f74aefda27b57ba696aa98bc091","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1681,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 7. Closed result and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse","start_line":1681}],"label":"ACTIVATION.md · ACTIVATION/7. Closed result and reuse"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:779bfa6b7fb6026d7bc35d8d59e9b2d1","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1750,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transition evidence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse%2FTransition%20evidence","start_line":1750}],"label":"ACTIVATION.md · ACTIVATION/7. Closed result and reuse/Transition evidence"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","value":{"conditions":[],"definition":"Exact selected native source member. Its complete text is embedded for source re-entry; this node supplies navigation, not a complete interpretation.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"# SDLC default frame guidance","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":1}],"label":"SDLC_DEFAULTS.md"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d7c084f84be762a7a02d3bca00e74d83","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"# SDLC default frame guidance","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":1}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f1efd93eac82ee04279f0e6c9c430858","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":9,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selection and binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelection%20and%20binding","start_line":9}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance/Selection and binding"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d26d3d787b82b4e52ed39f8aa944bee","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":28,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selected default flow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelected%20default%20flow","start_line":28}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance/Selected default flow"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:353842eaa17aecc389d45c5c780a5bd6","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":66,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Work reference, context and continuation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":66}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance/Work reference, context and continuation"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7eeccb8acfff20281aed92698aaf2968","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":107,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Causal triage","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FCausal%20triage","start_line":107}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance/Causal triage"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1ddaff9ad5cdb350c55adf8d522c16fe","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":139,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Verification and stopping","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FVerification%20and%20stopping","start_line":139}],"label":"SDLC_DEFAULTS.md · SDLC default frame guidance/Verification and stopping"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","value":{"conditions":[],"definition":"Exact selected native source member. Its complete text is embedded for source re-entry; this node supplies navigation, not a complete interpretation.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"# TICKETS","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS","start_line":1}],"label":"TICKETS.md"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:288b2b57cf91788264f06f5158444194","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"# TICKETS","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS","start_line":1}],"label":"TICKETS.md · TICKETS"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:24a8ce280034b1cbdbda9500c1afda5e","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 1. Work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers","start_line":27}],"label":"TICKETS.md · TICKETS/1. Work carriers"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4dda5889dc3b394c373ddbf41f26daba","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":29,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Goals","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FGoals","start_line":29}],"label":"TICKETS.md · TICKETS/1. Work carriers/Goals"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cefab13899a3eec95583c0b70f0769c7","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":37,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Ticket records","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FTicket%20records","start_line":37}],"label":"TICKETS.md · TICKETS/1. Work carriers/Ticket records"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:175be88af46095d15a3581f999210e6a","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":45,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprints","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FSprints","start_line":45}],"label":"TICKETS.md · TICKETS/1. Work carriers/Sprints"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:95059345cc5ba14701f6a2468d18bb93","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":64,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Comments","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FComments","start_line":64}],"label":"TICKETS.md · TICKETS/1. Work carriers/Comments"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ccf76836ad0e8a5b3057591d1f71a51","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":76,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contracts","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FExecution%20contracts","start_line":76}],"label":"TICKETS.md · TICKETS/1. Work carriers/Execution contracts"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1bd4e4631ddf82e966569f02e5ad151f","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":101,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Milestones and phase-scoped truth (UP-006)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FMilestones%20and%20phase-scoped%20truth%20%28UP-006%29","start_line":101}],"label":"TICKETS.md · TICKETS/1. Work carriers/Milestones and phase-scoped truth (UP-006)"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:665dc3d455890527702945184416553b","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":118,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 2. Layout and authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority","start_line":118}],"label":"TICKETS.md · TICKETS/2. Layout and authority"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c2606640e448e13bc04c7dbcd588b03d","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":120,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Default layout","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FDefault%20layout","start_line":120}],"label":"TICKETS.md · TICKETS/2. Layout and authority/Default layout"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a8e3813cac312f0c232760d58fdfd537","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":148,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bindings and projections","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FBindings%20and%20projections","start_line":148}],"label":"TICKETS.md · TICKETS/2. Layout and authority/Bindings and projections"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c535a4b4eadc4143d5d7dd2c96ce3b3c","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":165,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier substitution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FCarrier%20substitution","start_line":165}],"label":"TICKETS.md · TICKETS/2. Layout and authority/Carrier substitution"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148fde93b9c151b85980430227c61d99","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":179,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 3. Sprint rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules","start_line":179}],"label":"TICKETS.md · TICKETS/3. Sprint rules"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2eb65a18805d48be5cbc62aa42167702","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":181,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per sprint","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FOne%20durable%20record%20per%20sprint","start_line":181}],"label":"TICKETS.md · TICKETS/3. Sprint rules/One durable record per sprint"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a4d5bb17a6d2db5e63951e9e18fd599","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":190,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Manifest fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FManifest%20fields","start_line":190}],"label":"TICKETS.md · TICKETS/3. Sprint rules/Manifest fields"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a76468a77fd08ec0ac60a81d60676afe","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":209,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20status","start_line":209}],"label":"TICKETS.md · TICKETS/3. Sprint rules/Sprint status"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ca8be99cfd04580ef9e1e609073e493","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":220,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20admission","start_line":220}],"label":"TICKETS.md · TICKETS/3. Sprint rules/Sprint admission"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:480ad63724075a769d12b25724c756a2","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":234,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Compliance escrow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FCompliance%20escrow","start_line":234}],"label":"TICKETS.md · TICKETS/3. Sprint rules/Compliance escrow"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b70e36657e6d05dacc2f88b6fadce2f7","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":261,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Close review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FClose%20review","start_line":261}],"label":"TICKETS.md · TICKETS/3. Sprint rules/Close review"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b65a4420ec4d34c1e36c3925bba61dc1","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":325,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 4. Ticket rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules","start_line":325}],"label":"TICKETS.md · TICKETS/4. Ticket rules"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7753ee5278b8d8220dd5cbe227a014b4","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":327,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FOne%20durable%20record%20per%20ticket","start_line":327}],"label":"TICKETS.md · TICKETS/4. Ticket rules/One durable record per ticket"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d0e3552799102f530a089d131bcdcf87","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":340,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant independence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FMulti-build-tenant%20independence","start_line":340}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Multi-build-tenant independence"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:57daa5098984b440797b565ccd6da2bf","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":387,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Required fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FRequired%20fields","start_line":387}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Required fields"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:dc6c2e37caf5e28652358376fb9d5a1e","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":408,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Types","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTypes","start_line":408}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Types"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2e92a9c8920c09e452a2e18acc822f85","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":415,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Category","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FCategory","start_line":415}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Category"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7f12dbb95582a2c7f730f9aa6993fc21","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":430,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Inside-out sequencing","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FInside-out%20sequencing","start_line":430}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Inside-out sequencing"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ce81d876d3e689c1707f6e2f692d0128","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":446,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Change class","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FChange%20class","start_line":446}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Change class"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:eae45f030c94c44c47ba075ab6d6d1a1","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":468,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Upward propagation check","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FUpward%20propagation%20check","start_line":468}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Upward propagation check"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2966e4a8fb239c7eb9cc6c308606d25b","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":508,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Triage metadata","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTriage%20metadata","start_line":508}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Triage metadata"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5af0931d446931d7ee2d0303fca5eabc","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":517,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FStatus","start_line":517}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Status"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e4b3efcb2bfc4fd55aa29da4ac397155","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":536,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review findings and bug items","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FReview%20findings%20and%20bug%20items","start_line":536}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Review findings and bug items"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9ff518456b185aaaea39d1657b416a20","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":579,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Lanes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FLanes","start_line":579}],"label":"TICKETS.md · TICKETS/4. Ticket rules/Lanes"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:19b041cb32911e059e86daed2701621d","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":593,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 5. From carrier to execution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution","start_line":593}],"label":"TICKETS.md · TICKETS/5. From carrier to execution"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e7fe483488542c5c34b5581c285fc72c","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":608,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Foundation to law: work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FFoundation%20to%20law%3A%20work%20carriers","start_line":608}],"label":"TICKETS.md · TICKETS/5. From carrier to execution/Foundation to law: work carriers"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55f6126378408d89e2357e9620c29ef1","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":672,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier selection","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":672}],"label":"TICKETS.md · TICKETS/5. From carrier to execution/Carrier selection"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8950d31599ac068a0cc437f10e42839c","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":746,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contract admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FExecution%20contract%20admission","start_line":746}],"label":"TICKETS.md · TICKETS/5. From carrier to execution/Execution contract admission"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9181f717e875d57b8ecd74c2d8c7c233","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":770,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Evaluation criteria and non-closure conditions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FEvaluation%20criteria%20and%20non-closure%20conditions","start_line":770}],"label":"TICKETS.md · TICKETS/5. From carrier to execution/Evaluation criteria and non-closure conditions"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8130ed360ed8e84bb1f918ea5862cbbd","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":792,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bounded-context term binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FBounded-context%20term%20binding","start_line":792}],"label":"TICKETS.md · TICKETS/5. From carrier to execution/Bounded-context term binding"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ff0efb108940b7e239b597dfd6b26bb3","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":811,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 6. Implementation migration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration","start_line":811}],"label":"TICKETS.md · TICKETS/6. Implementation migration"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:77e4bd08d9e699d0e5027985f132c23d","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":813,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Declaration and checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FDeclaration%20and%20checklist","start_line":813}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Declaration and checklist"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:38794e02a2115cbb16b0f87abb76002b","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":868,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Closure of a migration ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FClosure%20of%20a%20migration%20ticket","start_line":868}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Closure of a migration ticket"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5cda870a3222a75847aa34fcb2ec02d4","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":898,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Strategy requirements","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FStrategy%20requirements","start_line":898}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Strategy requirements"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:778ef0f4ebbd594e48708a535e340037","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":918,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recurring realisation and library declaration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FRecurring%20realisation%20and%20library%20declaration","start_line":918}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Recurring realisation and library declaration"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8243a4ecc93f8bf206eaf13fc7a04031","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":949,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMulti-build-tenant%20review","start_line":949}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Multi-build-tenant review"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d3c9998459e383d18220b110e47798f","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":960,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review disambiguation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FReview%20disambiguation","start_line":960}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Review disambiguation"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d468d62446a2674f2c56af24006f011","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1000,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Impacted interface review checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FImpacted%20interface%20review%20checklist","start_line":1000}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Impacted interface review checklist"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f3ccb6274556c15ca20b323d6a7912d0","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1035,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Break order and break-to-closure map","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FBreak%20order%20and%20break-to-closure%20map","start_line":1035}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Break order and break-to-closure map"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f99c383afa81c78c769e56a0385af1ba","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1064,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Mixed-state negative proof","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMixed-state%20negative%20proof","start_line":1064}],"label":"TICKETS.md · TICKETS/6. Implementation migration/Mixed-state negative proof"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f16a036f6e0242fc2a4232012f8a86ff","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1093,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 7. Authority, judgment, closure and state","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state","start_line":1093}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4c0d38b06add273b8262e123dc603c73","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1103,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution and verification authority separation (UP-007)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FExecution%20and%20verification%20authority%20separation%20%28UP-007%29","start_line":1103}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state/Execution and verification authority separation (UP-007)"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a3957b6c5aa85512eaafc5ecc923f804","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1161,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recorded judgment and owner-ruling continuity","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1161}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state/Recorded judgment and owner-ruling continuity"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:25c172e7d5c86c1c87953fa016b63d45","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1249,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Condition-based closure and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FCondition-based%20closure%20and%20reuse","start_line":1249}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state/Condition-based closure and reuse"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:576e967eef5938037bcb9508f64e1394","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1292,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Test case authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FTest%20case%20authority","start_line":1292}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state/Test case authority"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e3789c9e24e88aacee0987a8b0a49e1b","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One-truth state projection and drift refusal (UP-009)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FOne-truth%20state%20projection%20and%20drift%20refusal%20%28UP-009%29","start_line":1338}],"label":"TICKETS.md · TICKETS/7. Authority, judgment, closure and state/One-truth state projection and drift refusal (UP-009)"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0dbef1b28168b242013beeebd2089719","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1352,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 8. Recommended shapes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F8.%20Recommended%20shapes","start_line":1352}],"label":"TICKETS.md · TICKETS/8. Recommended shapes"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:063c155871c928bf0de1871ab8596464","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1507,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 9. Operating mode and relationships","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships","start_line":1507}],"label":"TICKETS.md · TICKETS/9. Operating mode and relationships"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b0a395d11f87040b91bd7249fb10bafc","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1509,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Operating mode","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FOperating%20mode","start_line":1509}],"label":"TICKETS.md · TICKETS/9. Operating mode and relationships/Operating mode"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:11bcfd20a2217bb67a38a7e38ed8c325","value":{"conditions":[],"definition":"Source-section navigation entry. The heading and exact source location are preserved. Body meaning is not comprehensively modeled; inspect the attached residual and original source.","exceptions":[],"grounding":[{"end_line":1523,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Relationship to other surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FRelationship%20to%20other%20surfaces","start_line":1523}],"label":"TICKETS.md · TICKETS/9. Operating mode and relationships/Relationship to other surfaces"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1c1b407b4d3e3b974fa53f8a6a0fce0e","value":{"conditions":[],"definition":"A selectable projection of existing method law for ordinary software work, linking the work reference and bounded context to QA, diagnosis, re-entry, verification and continuation. It creates no new result, actor, workflow engine, permission or mandatory Executive configuration.","exceptions":[],"grounding":[{"end_line":7,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"This is a selectable projection of existing method law for ordinary software\nwork. It connects the current work reference and bounded context to QA,\ndiagnosis, re-entry, verification and durable continuation;\nthe linked sections remain the single deciding owners. It adds no result,\nactor, workflow engine, permission or mandatory Executive configuration.","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":3}],"label":"Selectable SDLC guidance"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2b58bb0f2986e9fbf24900e6af8a0032","value":{"conditions":[],"definition":"The Product-owned basis selects this guidance with its exact source and governing cut while retaining Product policy values, explicit gates and accepted alternatives.","exceptions":[],"grounding":[{"end_line":17,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Select this guidance in the accepted Project Reference-Frame Basis, binding\nits exact source identity and the governing method cut. The\n[basis template](templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#sdlc-default-selection)\nproposes it ready for adoption. An existing Product may select it through its\nown authorized basis change; merely installing or finding it selects nothing.\nKeep the Product's policy values, explicit gates and accepted alternatives.\nNo numeric priority cutoff, review ratio or additional gate is supplied here.","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelection%20and%20binding","start_line":11}],"label":"Accepted Project Reference-Frame Basis"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7","value":{"conditions":[],"definition":"The selected ticket, sprint entry or run contract is the work reference for its current question, exact subject and basis, result/evidence references and surviving obligations. It supplies no new authority by being present.","exceptions":[],"grounding":[{"end_line":744,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":731},{"end_line":701,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"Absence of a durable ticket neither requires nor authorises creating one.\nAn exact product-authorised work instruction may supply the upstream work\nauthority for a one-run contract; a generic request or a model-widened\nscope cannot. A durable ticket is created or updated only when the table\nrequires surviving state and the actor holds ticket-state authority. An\nexplicit instruction from ticket-state authority to create a durable record\nselects that durability; it does not admit an execution contract or widen\nits upstream work authority (P6, P2).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":694}],"label":"Selected work carrier"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e","value":{"conditions":[],"definition":"Acquisition of the deciding owners and current material subject for the next bounded decision. Qualified references must preserve the consuming contract, standing, provenance, active obligations and invalidators; a typed pointer alone proves no sufficiency.","exceptions":[],"grounding":[{"end_line":703,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"Qualified-reference guidance. Under\n[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) and\n[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), a reference can supply\nsufficient context when its accessible target and qualifications preserve\nthe consuming contract. Check the required subject and basis, assessment\nstanding, provenance, active obligation and version, and invalidators, rather\nthan candidate identity alone. A typed annotation supplies no evidence of\nsufficiency by itself. Preserve the required body or a qualified resolvable\nreference; no mandatory carrier or registry follows (P1, P3, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope","start_line":695},{"end_line":85,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":76}],"label":"Bounded context acquisition"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c443889322953a8151234eb2a5a0af7b","value":{"conditions":[],"definition":"The workspace and authoritative inputs persist across activations. Their current material state decides what the work has and has not done.","exceptions":[],"grounding":[{"end_line":1469,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"The workspace and its authoritative inputs persist across activations and\nare the continuing truth surface of the work: the surface whose current\nmaterial state decides what the work has and has not done. An actor's\ncontext is an account of that state. It is bounded, because it is a\nprojection of the state (§2); revisable, because an observation can\ncorrect it; and disposable, because a step records its closed results and\nstep-produced facts before it returns (§1 Admission; P4b). An account is\nnever a second truth surface, and no later activation needs a prior\nactor's context: its intake reconstructs the governing relations without\nit (§1 Intake) (P0, P3, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1460}],"label":"Persistent current work state"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2de0fd46815975a22813945715b29a6f","value":{"conditions":[],"definition":"An actor context is a bounded, revisable and disposable account of work state. It is not a second truth surface and the next activation need not inherit it.","exceptions":[],"grounding":[{"end_line":1469,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"The workspace and its authoritative inputs persist across activations and\nare the continuing truth surface of the work: the surface whose current\nmaterial state decides what the work has and has not done. An actor's\ncontext is an account of that state. It is bounded, because it is a\nprojection of the state (§2); revisable, because an observation can\ncorrect it; and disposable, because a step records its closed results and\nstep-produced facts before it returns (§1 Admission; P4b). An account is\nnever a second truth surface, and no later activation needs a prior\nactor's context: its intake reconstructs the governing relations without\nit (§1 Intake) (P0, P3, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1460}],"label":"Disposable actor account"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4628b52b8251c543094a5bbd0af25c7d","value":{"conditions":[],"definition":"A closed result identifies its frame/activation, subject, basis, evaluation, actor, evidence, verdict, residual uncertainty and invalidation conditions. Handoff sufficiency is relative to the consuming decision.","exceptions":[],"grounding":[{"end_line":1692,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"A closed result identifies the frame and its activation, the subject, the\nbasis, the evaluation, the actor, the evidence, the verdict, the residual\nuncertainty and the invalidation conditions (the minimal shape is\nREFERENCE_FRAME §13). The frame's internal working context need not be\ntransferred when the closed result and its provenance are sufficient for\nthe consuming decision; it may still be attached, for audit or otherwise,\nwithout changing the result. Independent evaluations may share valid\nmechanical evidence under the declared independence conditions of\n[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that\npermission (P4b, P0).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse","start_line":1683}],"label":"Closed result and provenance"}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e877d59b2fd96fab2de168ed3ffee734","value":{"conditions":[],"definition":"An owner ruling retains its original wording, owner, exact subject and basis, permitted scope/effects, conditions and source, separately from agent interpretation.","exceptions":[],"grounding":[{"end_line":1197,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"A direct or lawfully proxied owner ruling is recorded in its original\nwording, with its owner, exact subject and basis, permitted scope and\neffects, conditions and source, separately from agent interpretation. Later\nwork consumes that same ruling while it applies; it neither widens the\nruling nor requests unchanged authority again. New ambiguity or a\nmaterially changed decision returns only the affected question to its\nowner. J is not O, and recording either cannot create admission,\nacceptance, effects or continuation beyond the original grant (P6, P3).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1190}],"label":"Recorded owner ruling"}}],"relations":[{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a272cdeb8e7316a88bc125d8fc85c8cf","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2f6837ca62ccf92b0d07382360091298","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"# ACTIVATION","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION","start_line":1}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a7cff193c9266a9890a368cbfc0eab0a","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:400ef0f69f49a653a381946710819e61","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 1. The step","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step","start_line":27}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:091f5c09359770e090b03e7bff612a45","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ba646bb3d8f1bbfc5b5422caade3b1a","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":116,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transitions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FTransitions","start_line":116}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1108ec8bf0b6117a36abf7769ea7ec81","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:325d2070aa58719f3f446c35ca205379","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":199,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction relation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConstruction%20relation","start_line":199}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:59535c553ef5141600fb1261b90cbe67","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148dfee42423870fdae0c364ddc8ed32","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":353,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Intake","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FIntake","start_line":353}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:eef98bf88e1487a3a9dc301788c2efe4","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1226632ad2ac42069c057a4bee0a7a71","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":391,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Execution unit","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FExecution%20unit","start_line":391}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8550807043415a1db02053dc48948c7b","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:07423eb066be1627975a960ee421930d","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":402,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FAdmission","start_line":402}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2f997e48413b59b4ac0a91ef72f15332","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ceada1b7bdb7a0cd2a8f54716ab041c3","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":439,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Applicability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FApplicability","start_line":439}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5f118b646a77b7514a9f145ce5fb7c6c","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:568bae2370b2aa7dda3f25c93c2abac3","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":489,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Output","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FOutput","start_line":489}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:638cb5eaa3e17c8ff320d4548f383d42","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9d49d7d28b3bef14d7c8e0c41a877cc3","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":497,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Configuration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConfiguration","start_line":497}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:04101d68f65845749d341d20609923de","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cf5901ce38d3a46343cb59a6596f6b13","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":619,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Roles and delegation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FRoles%20and%20delegation","start_line":619}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:343294bf108f91204d46bacd122c22af","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:222611d49ebb6a3da08e26ea2f6b4d39","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":693,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 2. Context construction under an envelope","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope","start_line":693}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4f9aba7253c334eb32516e8e741d494a","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:df7b1d64f0812fa86dfd410c806570b1","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":902,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Staleness of derived surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope%2FStaleness%20of%20derived%20surfaces","start_line":902}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f014511c5f966d61a0299f740830f62b","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:489ab6435409e216e3e5962b342a188f","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":938,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 3. Step results and disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition","start_line":938}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:35050718a13a43d59813c2c915d32fce","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1d6224c48fe5d3c554a98c71e9b871a3","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":968,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission and activation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAdmission%20and%20activation","start_line":968}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9792a478ed098f9adbda904e00aa1c30","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d6aae782cb81aa9a98afc37213c1e50","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1002,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction availability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FConstruction%20availability","start_line":1002}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:85f86cac6ebb2aaed5ece3c0bf86622f","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a715f999050fe32cda11f33018b9ae9","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1049,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FDisposition","start_line":1049}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:896e96b646b8498de3b7f857fc98a0c5","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f9c599914ff44e8b4d080328ef4cdbbf","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1087,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Ambiguity outcome","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAmbiguity%20outcome","start_line":1087}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cc302f0414e6f24d0d0c1f90f1781924","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:304e27191e740a14ff1a5360f96c192a","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1114,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Effects","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FEffects","start_line":1114}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:dcaa55d68b09e2984145fcbf1c63e05b","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8112c1d9ca80c0f81b6fffbaccaf4058","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1164,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 4. Totality and refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement","start_line":1164}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:34fc24245bbe44692baef1a5fe0a48ac","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fe60a4abb04eaaf1ce62331937b96208","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1210,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FRefinement","start_line":1210}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:58576662eee692bd68fd0ccd07121fa8","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6b21eeadc9a4c3f9a3ab684176865732","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1286,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Complete enclosing-relation admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FComplete%20enclosing-relation%20admission","start_line":1286}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2c1996739a19898367f7056a9f49469d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:93395e367024e30ac50a227dc9423045","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Standing structural qualification","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FStanding%20structural%20qualification","start_line":1338}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6982d93f49f0fdef14b14d3dcb557e0d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:22033e571d79ba6f2d722b08ef8f6957","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1370,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 5. Work state and restart","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart","start_line":1370}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0fb14c090b473da4145b29b1c7a17fcb","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55444d1e0e6c8fc6ece0f11e82e42ede","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1458,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### The workspace and an actor's account","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1458}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5333ecf19db990a537e09e928d42a7f0","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2348700f1fc9d2f2fcf11b79717c0fe5","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1519,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 6. Cost and proportionality","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality","start_line":1519}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:89b43423e118b07eec579ff940bd92d8","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:198b48795b15017f083879352e8a1a75","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1627,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Resource limits","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality%2FResource%20limits","start_line":1627}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cee3448dbe15f914fdd54c5fc4ff065c","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:aeca5f74aefda27b57ba696aa98bc091","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1681,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 7. Closed result and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse","start_line":1681}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2737bde297b499417ca287183a4a23dd","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271feea7083c5adee7f2b40b7d36baa0","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:779bfa6b7fb6026d7bc35d8d59e9b2d1","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1750,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transition evidence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse%2FTransition%20evidence","start_line":1750}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:282c529dfd8580cec83314a0f7719876","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d7c084f84be762a7a02d3bca00e74d83","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"# SDLC default frame guidance","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":1}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8b0b64b31fb79d8c1cf27405c255fbcb","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f1efd93eac82ee04279f0e6c9c430858","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":9,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selection and binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelection%20and%20binding","start_line":9}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d71f5b30e8629267a830bffb1781ad75","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d26d3d787b82b4e52ed39f8aa944bee","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":28,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selected default flow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelected%20default%20flow","start_line":28}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5e0e1127ee2cc40eaa97a1d91ed215bf","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:353842eaa17aecc389d45c5c780a5bd6","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":66,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Work reference, context and continuation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":66}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d61e0441455c94a54b6d1ae3988041e1","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7eeccb8acfff20281aed92698aaf2968","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":107,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Causal triage","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FCausal%20triage","start_line":107}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cd389cec85c3a82ee48f9060bdb8b20d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:68be7418757e364979696b4b1107b8d9","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1ddaff9ad5cdb350c55adf8d522c16fe","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":139,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Verification and stopping","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FVerification%20and%20stopping","start_line":139}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ca68955367037662ebb1f3f5417f7fd2","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:288b2b57cf91788264f06f5158444194","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"# TICKETS","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS","start_line":1}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1e31b7ba55aaef84e68277ff51021036","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:24a8ce280034b1cbdbda9500c1afda5e","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 1. Work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers","start_line":27}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c1a8f3520a46e46e8e190127395e6ac4","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4dda5889dc3b394c373ddbf41f26daba","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":29,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Goals","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FGoals","start_line":29}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:77d9573cc511a8d2965aecb41463009c","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cefab13899a3eec95583c0b70f0769c7","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":37,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Ticket records","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FTicket%20records","start_line":37}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:32eaa2d4f89471fb413efbb4e7227515","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:175be88af46095d15a3581f999210e6a","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":45,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprints","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FSprints","start_line":45}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7834a61721d8b8108289bf1c8b197322","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:95059345cc5ba14701f6a2468d18bb93","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":64,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Comments","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FComments","start_line":64}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f4a1088c7bd6f22620461c5051cd4561","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ccf76836ad0e8a5b3057591d1f71a51","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":76,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contracts","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FExecution%20contracts","start_line":76}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b60a664454d69d489b31a9303e9a6814","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1bd4e4631ddf82e966569f02e5ad151f","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":101,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Milestones and phase-scoped truth (UP-006)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FMilestones%20and%20phase-scoped%20truth%20%28UP-006%29","start_line":101}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ebf2fad372a7865893a319dd1c0d48f2","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:665dc3d455890527702945184416553b","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":118,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 2. Layout and authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority","start_line":118}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7e435916abecb1af382ae342fcec0241","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c2606640e448e13bc04c7dbcd588b03d","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":120,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Default layout","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FDefault%20layout","start_line":120}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:81bee278409c429e92dc5ff67b249643","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a8e3813cac312f0c232760d58fdfd537","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":148,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bindings and projections","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FBindings%20and%20projections","start_line":148}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:52f61277b3d7a5cb9b2c1102ad564fc7","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c535a4b4eadc4143d5d7dd2c96ce3b3c","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":165,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier substitution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FCarrier%20substitution","start_line":165}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:81ea8fa37fa000852f49ed299c46d69d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148fde93b9c151b85980430227c61d99","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":179,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 3. Sprint rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules","start_line":179}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:dd6a73d5d4c044918e2a8e58a59d7227","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2eb65a18805d48be5cbc62aa42167702","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":181,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per sprint","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FOne%20durable%20record%20per%20sprint","start_line":181}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2cdd8af6ed4bd8e9c1de89396136847e","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a4d5bb17a6d2db5e63951e9e18fd599","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":190,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Manifest fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FManifest%20fields","start_line":190}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b2cad6cdcf359765adcbee36e3b26f0f","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a76468a77fd08ec0ac60a81d60676afe","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":209,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20status","start_line":209}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:33b878dc01334696d23e7345a29a56ed","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ca8be99cfd04580ef9e1e609073e493","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":220,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20admission","start_line":220}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:64cb16278fdedd899724d63c3c2cfe7f","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:480ad63724075a769d12b25724c756a2","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":234,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Compliance escrow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FCompliance%20escrow","start_line":234}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ced41f30d3b61f44a8d84bdc1d6a866d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b70e36657e6d05dacc2f88b6fadce2f7","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":261,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Close review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FClose%20review","start_line":261}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1af45a6731cc56adc5aaea1cf0d75c97","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b65a4420ec4d34c1e36c3925bba61dc1","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":325,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 4. Ticket rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules","start_line":325}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f71fad3262a53f18c4d31dcf59ad515c","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7753ee5278b8d8220dd5cbe227a014b4","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":327,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FOne%20durable%20record%20per%20ticket","start_line":327}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8e4d99d64b017d2d3242f57237658c89","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d0e3552799102f530a089d131bcdcf87","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":340,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant independence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FMulti-build-tenant%20independence","start_line":340}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e758b6ae5c7fda4685e1dca5f5f28bcd","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:57daa5098984b440797b565ccd6da2bf","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":387,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Required fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FRequired%20fields","start_line":387}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:076fda1f7acef06be65e1fe379a9a066","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:dc6c2e37caf5e28652358376fb9d5a1e","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":408,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Types","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTypes","start_line":408}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1eaf63c37d496c9515a46d4087ce0006","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2e92a9c8920c09e452a2e18acc822f85","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":415,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Category","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FCategory","start_line":415}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:15dc8090355e4dac3a7ee5e49fe7e723","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7f12dbb95582a2c7f730f9aa6993fc21","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":430,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Inside-out sequencing","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FInside-out%20sequencing","start_line":430}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:126d7ac27739a2639edb5e81a1382661","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ce81d876d3e689c1707f6e2f692d0128","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":446,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Change class","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FChange%20class","start_line":446}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8a89c720c0589809effbefee58b4ed11","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:eae45f030c94c44c47ba075ab6d6d1a1","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":468,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Upward propagation check","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FUpward%20propagation%20check","start_line":468}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edfe73a1a31a9dae5d3fca08c7c6cf51","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2966e4a8fb239c7eb9cc6c308606d25b","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":508,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Triage metadata","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTriage%20metadata","start_line":508}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c2b18e4e6b38ddcae0e1caaf87888254","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5af0931d446931d7ee2d0303fca5eabc","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":517,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FStatus","start_line":517}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d2937afbb75455ddf74a4108512cfb1","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e4b3efcb2bfc4fd55aa29da4ac397155","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":536,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review findings and bug items","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FReview%20findings%20and%20bug%20items","start_line":536}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ba371f66bbbf43de61ddf09cb5e04270","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9ff518456b185aaaea39d1657b416a20","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":579,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Lanes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FLanes","start_line":579}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0500ac8f6b0f0943098dec79eaf4ebba","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:19b041cb32911e059e86daed2701621d","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":593,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 5. From carrier to execution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution","start_line":593}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a71dba87d30c5f65b88ac53d878f3005","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e7fe483488542c5c34b5581c285fc72c","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":608,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Foundation to law: work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FFoundation%20to%20law%3A%20work%20carriers","start_line":608}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0f12115f3a92c93bc0d89293eb0d2d5b","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55f6126378408d89e2357e9620c29ef1","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":672,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier selection","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":672}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:78954c0a06b6ab227fa20b0dd2a957b3","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8950d31599ac068a0cc437f10e42839c","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":746,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contract admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FExecution%20contract%20admission","start_line":746}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f922a708499d2d0ff642de3fac4c952a","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9181f717e875d57b8ecd74c2d8c7c233","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":770,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Evaluation criteria and non-closure conditions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FEvaluation%20criteria%20and%20non-closure%20conditions","start_line":770}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e9eb12a4406c0939ea5eef55049fb183","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8130ed360ed8e84bb1f918ea5862cbbd","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":792,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bounded-context term binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FBounded-context%20term%20binding","start_line":792}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:06605e5eeb245e97b39fd6ad5a07c4b0","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ff0efb108940b7e239b597dfd6b26bb3","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":811,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 6. Implementation migration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration","start_line":811}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3da3b32c80aad0120944b1e422df3091","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:77e4bd08d9e699d0e5027985f132c23d","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":813,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Declaration and checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FDeclaration%20and%20checklist","start_line":813}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d744a2f59beb400451c828ce6de70b94","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:38794e02a2115cbb16b0f87abb76002b","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":868,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Closure of a migration ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FClosure%20of%20a%20migration%20ticket","start_line":868}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a10076e385e86d0c6f51be77479d9baf","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5cda870a3222a75847aa34fcb2ec02d4","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":898,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Strategy requirements","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FStrategy%20requirements","start_line":898}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:48c8670ce078157ba6133987fe5c27b5","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:778ef0f4ebbd594e48708a535e340037","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":918,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recurring realisation and library declaration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FRecurring%20realisation%20and%20library%20declaration","start_line":918}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:02ca3ce277aeb0f7d4c7a96de5c545fb","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8243a4ecc93f8bf206eaf13fc7a04031","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":949,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMulti-build-tenant%20review","start_line":949}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c1f33927ff2b7dfdd54a17b94518d4e4","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d3c9998459e383d18220b110e47798f","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":960,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review disambiguation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FReview%20disambiguation","start_line":960}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:48928c8e875c6f050935b253a50c28cc","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d468d62446a2674f2c56af24006f011","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1000,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Impacted interface review checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FImpacted%20interface%20review%20checklist","start_line":1000}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:eb0918341bc5d875d9f5e3345dacefc2","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f3ccb6274556c15ca20b323d6a7912d0","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1035,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Break order and break-to-closure map","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FBreak%20order%20and%20break-to-closure%20map","start_line":1035}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5de96e1c8cda38ffa2fc45cdbd0148b3","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f99c383afa81c78c769e56a0385af1ba","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1064,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Mixed-state negative proof","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMixed-state%20negative%20proof","start_line":1064}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1d396a15bab0e3766f77400629a39c47","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f16a036f6e0242fc2a4232012f8a86ff","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1093,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 7. Authority, judgment, closure and state","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state","start_line":1093}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:94d67b5b8ab5eefc675b0b339d2135d9","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4c0d38b06add273b8262e123dc603c73","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1103,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution and verification authority separation (UP-007)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FExecution%20and%20verification%20authority%20separation%20%28UP-007%29","start_line":1103}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4f84c6a63251c205cfd3648e4e576bdd","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a3957b6c5aa85512eaafc5ecc923f804","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1161,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recorded judgment and owner-ruling continuity","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1161}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:69b08b3a5532da6ef4c7fadf7baf2643","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:25c172e7d5c86c1c87953fa016b63d45","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1249,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Condition-based closure and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FCondition-based%20closure%20and%20reuse","start_line":1249}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:84c3abfe85423e3e3f770dfe2392e2aa","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:576e967eef5938037bcb9508f64e1394","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1292,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Test case authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FTest%20case%20authority","start_line":1292}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8d01a7328befc0daee7eab128ff7d6b4","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e3789c9e24e88aacee0987a8b0a49e1b","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One-truth state projection and drift refusal (UP-009)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FOne-truth%20state%20projection%20and%20drift%20refusal%20%28UP-009%29","start_line":1338}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:90963606d70079a46a0e82a1121a2ba4","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0dbef1b28168b242013beeebd2089719","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1352,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 8. Recommended shapes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F8.%20Recommended%20shapes","start_line":1352}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4185fe0732675c4572a9db4e642b920e","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:063c155871c928bf0de1871ab8596464","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1507,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 9. Operating mode and relationships","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships","start_line":1507}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6a9084159fcea3fdc9a01b95fc719d4a","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b0a395d11f87040b91bd7249fb10bafc","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1509,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Operating mode","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FOperating%20mode","start_line":1509}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e174ed70a16762b46c2d67b9c74d418d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edc0a0731f341ab18e0e85693ad0e4bf","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:11bcfd20a2217bb67a38a7e38ed8c325","qualifiers":{"conditions":[],"exceptions":[],"grounding":[{"end_line":1523,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Relationship to other surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FRelationship%20to%20other%20surfaces","start_line":1523}],"kind":"contains_source_section","meaning":"The selected source member contains this section. This is a structural navigation relation and grants no semantic authority."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9534040fb748d9b2c1dcadc313dfde0d","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2b58bb0f2986e9fbf24900e6af8a0032","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1c1b407b4d3e3b974fa53f8a6a0fce0e","qualifiers":{"conditions":["Selection occurs through the Product's authorized basis change."],"exceptions":["Merely installing or finding guidance selects nothing."],"grounding":[{"end_line":17,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Select this guidance in the accepted Project Reference-Frame Basis, binding\nits exact source identity and the governing method cut. The\n[basis template](templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#sdlc-default-selection)\nproposes it ready for adoption. An existing Product may select it through its\nown authorized basis change; merely installing or finding it selects nothing.\nKeep the Product's policy values, explicit gates and accepted alternatives.\nNo numeric priority cutoff, review ratio or additional gate is supplied here.","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelection%20and%20binding","start_line":11}],"kind":"selects_guidance","meaning":"An accepted Product frame basis selects exact SDLC guidance and governing method cut."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f793354343fab46e7b5121a2222477dd","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e","qualifiers":{"conditions":["Bind current question, subject/basis, result/evidence references and surviving obligations."],"exceptions":["This relation creates no additional carrier requirement and confers no ticket-state authority."],"grounding":[{"end_line":744,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":731}],"kind":"applies_context_owner","meaning":"The selected carrier applies ACTIVATION section 2 to bounded acquisition using its exact current work bindings."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b7e39de592a9a6ca914e39603fd60581","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c443889322953a8151234eb2a5a0af7b","qualifiers":{"conditions":["Resume from current material state and reconcile effects needed by the next dependent action."],"exceptions":["A summary or actor account cannot replace governing sources or current evidence."],"grounding":[{"end_line":744,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":731}],"kind":"applies_restart_owner","meaning":"The selected carrier applies ACTIVATION section 5 to current work state, the disposable actor account and resumption."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e1ef9d999473885a3f7e075f7ed4eee0","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4628b52b8251c543094a5bbd0af25c7d","qualifiers":{"conditions":["Use existing admission and continuity law and check applicability."],"exceptions":["No new ticket-state authority follows."],"grounding":[{"end_line":744,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":731}],"kind":"applies_reuse_owner","meaning":"The selected carrier applies ACTIVATION section 7 to closed results and reuse and retains step-produced facts and owner rulings on the named evidence surface."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cc6fa4f9ae46cebb4d591dcbb2ea0acc","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c443889322953a8151234eb2a5a0af7b","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2de0fd46815975a22813945715b29a6f","qualifiers":{"conditions":["Reconciliation stays within the actor's grant."],"exceptions":["When needed operations, territory or decisions exceed the grant, stop with re_entry_requested(authority) naming the owner."],"grounding":[{"end_line":1483,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"Acquisition ([§2](#2-context-construction-under-an-envelope)) observes the\ncurrent subject and its authoritative inputs. Where they materially\ndisagree with a cached belief, a retained summary or a prior result, the\nactor reconciles the disagreement: current evidence corrects the account,\nand what the evidence cannot decide stays an explicit unknown. A stored\nbelief, a summary or a successful prior result never overrules contrary\ncurrent evidence. A prior result is relied on only after its\napplicability and invalidators are checked against the current subject\nand inputs (§7). The actor corrects its account within its grant; where\nresolving the disagreement needs an operation, a territory or a decision\noutside the grant, the step stops with `re_entry_requested(authority)`,\nnaming the owner of what it needs (§3 Construction availability) (P5,\nP6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1471}],"kind":"corrects_account","meaning":"Current material evidence corrects a contrary cached belief, retained summary or prior result; undecidable facts remain explicit unknowns."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:178e4545739722430f5aaca2f6353df9","source":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e877d59b2fd96fab2de168ed3ffee734","target":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7","qualifiers":{"conditions":["Exact subject, basis, permitted scope/effects and conditions remain applicable."],"exceptions":["New ambiguity or a materially changed decision returns only the affected question to the owner; recording creates no new grant."],"grounding":[{"end_line":1197,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"A direct or lawfully proxied owner ruling is recorded in its original\nwording, with its owner, exact subject and basis, permitted scope and\neffects, conditions and source, separately from agent interpretation. Later\nwork consumes that same ruling while it applies; it neither widens the\nruling nor requests unchanged authority again. New ambiguity or a\nmaterially changed decision returns only the affected question to its\nowner. J is not O, and recording either cannot create admission,\nacceptance, effects or continuation beyond the original grant (P6, P3).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1190}],"kind":"bounds_continuation","meaning":"Later work consumes the original ruling while it applies, without widening it or requesting unchanged authority again."}}],"constraints":[{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f83be18de616594f9748d70b53f1e131","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e"],"predicate":{"conditions":["The selected envelope declares context capacity."],"exceptions":["Where no capacity is declared, no measurement gate is added."],"grounding":[{"end_line":85,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":76}],"statement":"Where the selected envelope declares context capacity, record the required measurement, capacity and comparison before reading. Complete-fit judgment remains unresolved without complete active inputs or a supported upper bound, unless measured excess falsifies it.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0e726b795f3392bfff0420a980f8939b","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e"],"predicate":{"conditions":[],"exceptions":[],"grounding":[{"end_line":85,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":76},{"end_line":744,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":731}],"statement":"A stale or insufficient derived surface requires re-entry to the exact owning sections; a summary or index supplies no work-state authority, governing meaning or current material evidence by itself.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:749801924ad07ba4dc4219f0bc15bdd7","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7"],"predicate":{"conditions":[],"exceptions":[],"grounding":[{"end_line":701,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"Absence of a durable ticket neither requires nor authorises creating one.\nAn exact product-authorised work instruction may supply the upstream work\nauthority for a one-run contract; a generic request or a model-widened\nscope cannot. A durable ticket is created or updated only when the table\nrequires surviving state and the actor holds ticket-state authority. An\nexplicit instruction from ticket-state authority to create a durable record\nselects that durability; it does not admit an execution contract or widen\nits upstream work authority (P6, P2).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":694}],"statement":"Absence of a durable ticket neither requires nor authorizes creating one. Required surviving state and ticket-state authority govern creation/update; selecting durability does not admit an execution contract or widen upstream work authority.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d7916c0e3f840b08b2a72f7df639cf79","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4628b52b8251c543094a5bbd0af25c7d"],"predicate":{"conditions":["The actor holds the necessary Writer effects."],"exceptions":["An actor without those effects returns to the permitted Writer; Executive performs no file or Git mutation in that role. No second state ledger or per-tool log is added."],"grounding":[{"end_line":96,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Before return, a permitted Writer records the closed result, step-produced\nfacts needed later, evidence, unresolved work, original owner rulings and the\nnext authorized action or owner re-entry in the existing named durable\nresult/evidence surface. Keep references with the owning work. This projection\nadds no second state ledger or per-tool logging requirement. An actor without those effects\nreturns to the permitted Writer; Executive still performs no file or Git\nmutation in that role. Sources:\n[ACTIVATION admission](ACTIVATION.md#admission),\n[closed results](ACTIVATION.md#7-closed-result-and-reuse),\n[TICKETS continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":87}],"statement":"Before return, a permitted Writer records the closed result, needed step-produced facts, evidence, unresolved work, original rulings and lawful next action or owner re-entry in the existing named durable result/evidence surface.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a66cf4002c6c4b734e699cfa4ebb2d4e","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4628b52b8251c543094a5bbd0af25c7d"],"predicate":{"conditions":["The change can alter the result, or changes a bound basis coordinate, or is the declared revising observation."],"exceptions":["Role, conversation or resumption change alone invalidates nothing. Changed coordinates alone establish neither claim failure nor success."],"grounding":[{"end_line":1727,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"A closed result is reused by an unchanged consumer that checks exact\napplicability; a role, conversation or resumption change alone invalidates\nnothing. An invalidator invalidates the affected result before reliance,\neven where the subject's own bytes are unchanged, preserving its\npredecessor/successor relation and any demonstrably independent surviving\nresults. Invalidation withdraws the result from direct reliance; whether\nits evidence is retained on the new basis is decided by `retain_applicable`\nof FOUNDATIONS §4 Change impact and evidence reuse, and the changed\ncoordinate alone establishes neither that the claim fails nor that it\nholds. The invalidators are three:\n\n- a material input change: a change to the result's subject or to an\n  input it rests on, including the admissible evidence that bears on its\n  predicate; newly acquired or changed admissible evidence is such a\n  change when it is material to the result as\n  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,\n  when it could change the result's value;\n- a changed basis: a change to any coordinate of the basis the result\n  binds (FOUNDATIONS §2, Basis);\n- a declared revising observation: an observation that the result or\n  judgment itself names as one that would revise it, once it occurs.","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse","start_line":1707}],"statement":"Check exact applicability before reuse. Material input change, changed basis or a declared revising observation invalidates the affected result before reliance; retain its predecessor/successor relation and demonstrably independent surviving results.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8ac7ef58890232a5734d8e6560b07d5f","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4628b52b8251c543094a5bbd0af25c7d"],"predicate":{"conditions":["Independent assessment is required by the actual governing boundary."],"exceptions":["A new role or conversation alone does not invalidate otherwise applicable work."],"grounding":[{"end_line":1188,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"Later roles and resumed runs recover the result and check its\napplicability rather than re-author unchanged judgment. Reuse and\ninvalidation are\n[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): changed material\ninputs, a declared revising observation or a changed basis invalidate\nthe affected result, preserving the original result and its successor\nrelation and keeping only demonstrably independent results, and a new\nrole or conversation alone invalidates nothing. For a recorded judgment\nthe material inputs include its supporting computed facts and evidence,\nand its declared revising observation is the one the record states;\nreassessment covers what the change affects. The result may reference\ncurrent C outputs; reuse cannot silently turn unknown facts into\nestablished premises (P4b, P5). Required independent assessment may consume valid C, but\nits assessor acquires sufficient exact evidence and supplies its own\njudgment under the actual independence condition; reusing the author's J\ncannot satisfy that condition (P6; EVALUATION §3).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1173}],"statement":"Required independent assessment may consume valid computed facts, but its assessor acquires sufficient exact evidence and supplies its own judgment under the actual independence condition. Reusing the author's judgment cannot satisfy it.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b2725b81be15d4c26d0a88ac818425a0","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1c1b407b4d3e3b974fa53f8a6a0fce0e"],"predicate":{"conditions":["Preserve selected gates and mandatory conditions."],"exceptions":[],"grounding":[{"end_line":43,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"2. **Construct and perform incremental QA.** Check the admitted step against\n   its requirement/design and the smallest adequate falsifier. State the\n   observed predicate, subject, oracle, coverage and residuals. A local pass\n   supports that bounded predicate; it supplies no unnamed Product acceptance,\n   qualification or release claim. Preserve selected gates and mandatory\n   conditions. Sources: [ASSURANCE](ASSURANCE.md),\n   [EVALUATION §1](EVALUATION.md#1-claims) and\n   [EVALUATION §5](EVALUATION.md#landing-closure-and-release).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelected%20default%20flow","start_line":36}],"statement":"Incremental QA checks the admitted step against its requirement/design and the smallest adequate falsifier, naming observed predicate, subject, oracle, coverage and residuals. A local pass supports that bounded predicate and no unnamed Product acceptance, qualification or release claim.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c8e46679ae3482755e4d5e5ca697d9f5","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1c1b407b4d3e3b974fa53f8a6a0fce0e"],"predicate":{"conditions":["Use evidence that distinguishes causes over the same exact subject and basis."],"exceptions":["A failed candidate alone does not establish inadequate governing law; insufficient observation keeps indeterminate and withholds the dependent claim."],"grounding":[{"end_line":119,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"| Supported cause | Lawful next action |\n|---|---|\n| Defective realisation under adequate unchanged law | Repair the realised surface within its grant; assert and verify no upstream drift. |\n| Inadequate governing requirement or design | Return to the first inadequate owner; admit its changed truth, then derive affected downstream work and evidence. A failed candidate alone does not establish this cause. |\n| Inaccurate predictive model | Return to the model's owner, identify the failed prediction and supported replacement/intervention, then re-evaluate the dependent claims. Do not relabel an outcome mismatch as a code defect without evidence. |\n| Insufficient observation | Acquire the missing admissible observation through its authorized route, or retain `indeterminate` and withhold the dependent claim. Repetition of the same uninformative check supplies no missing evidence. |","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FCausal%20triage","start_line":114}],"statement":"Causal triage distinguishes defective realization under adequate unchanged law, inadequate requirement/design, inaccurate predictive model and insufficient observation. Their lawful routes remain different; repeated uninformative checks supply no missing evidence.","uncertainty":"Bounded authored annotation; exact source and referenced owners decide applicability."}}],"latitude":[{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:75d9d582dabda9590f75c942498c06c0","applies_to":["urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7"],"allowed_variation":{"grounding":[{"end_line":105,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Resume from current material state, correct a contrary retained account,\ncheck exact applicability and invalidators, and reopen only affected support.\nReconcile uncertain external effects before a retry or dependent action;\nunresolved completion remains unresolved. Handoff needs sufficient closed\nresults and references, not the prior actor's private conversation. Sources:\n[ACTIVATION state and restart](ACTIVATION.md#5-work-state-and-restart),\n[actor account](ACTIVATION.md#the-workspace-and-an-actors-account) and\n[reuse](ACTIVATION.md#7-closed-result-and-reuse).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":98}],"statements":["Resume from current material state, correct a contrary account and reopen only affected support after exact applicability/invalidator checks.","Handoff sufficient closed results and references without the prior actor's private conversation."]},"forbidden_variation":{"grounding":[{"end_line":105,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"Resume from current material state, correct a contrary retained account,\ncheck exact applicability and invalidators, and reopen only affected support.\nReconcile uncertain external effects before a retry or dependent action;\nunresolved completion remains unresolved. Handoff needs sufficient closed\nresults and references, not the prior actor's private conversation. Sources:\n[ACTIVATION state and restart](ACTIVATION.md#5-work-state-and-restart),\n[actor account](ACTIVATION.md#the-workspace-and-an-actors-account) and\n[reuse](ACTIVATION.md#7-closed-result-and-reuse).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":98}],"statements":["Retry or take a dependent action before reconciling uncertain external effects.","Treat unresolved completion as established completion."]}}],"residuals":[{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7c5639dad8921a472bfd555c840e8336","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2f6837ca62ccf92b0d07382360091298","uncertainty":{"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"# ACTIVATION","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION","start_line":1}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:31c26c19a5aad3befbde3cf0e22631b1","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:400ef0f69f49a653a381946710819e61","uncertainty":{"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 1. The step","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step","start_line":27}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:edad610072a3c753098214b403655d84","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ba646bb3d8f1bbfc5b5422caade3b1a","uncertainty":{"grounding":[{"end_line":116,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transitions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FTransitions","start_line":116}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:bef4383955954b3c44743398a3193e14","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:325d2070aa58719f3f446c35ca205379","uncertainty":{"grounding":[{"end_line":199,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction relation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConstruction%20relation","start_line":199}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8e053eead0add0b0204543360f5ba5e3","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148dfee42423870fdae0c364ddc8ed32","uncertainty":{"grounding":[{"end_line":353,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Intake","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FIntake","start_line":353}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:bfd9857417066bf23130ab12f9c041e5","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1226632ad2ac42069c057a4bee0a7a71","uncertainty":{"grounding":[{"end_line":391,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Execution unit","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FExecution%20unit","start_line":391}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:03587aa99a8bd9fe72806ab4478dd0a0","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:07423eb066be1627975a960ee421930d","uncertainty":{"grounding":[{"end_line":402,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FAdmission","start_line":402}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fdffd22723215ea31574617a176bef4e","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ceada1b7bdb7a0cd2a8f54716ab041c3","uncertainty":{"grounding":[{"end_line":439,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Applicability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FApplicability","start_line":439}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:639df2ef08ab526c45ecd0eb19995335","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:568bae2370b2aa7dda3f25c93c2abac3","uncertainty":{"grounding":[{"end_line":489,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Output","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FOutput","start_line":489}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5d5b218c111d0945010522ba1426e943","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9d49d7d28b3bef14d7c8e0c41a877cc3","uncertainty":{"grounding":[{"end_line":497,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Configuration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FConfiguration","start_line":497}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:80b848b2ec48950dff539e5e98568446","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cf5901ce38d3a46343cb59a6596f6b13","uncertainty":{"grounding":[{"end_line":619,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Roles and delegation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F1.%20The%20step%2FRoles%20and%20delegation","start_line":619}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:efc659152de16f4c0232f2b3100f7e37","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:222611d49ebb6a3da08e26ea2f6b4d39","uncertainty":{"grounding":[{"end_line":693,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 2. Context construction under an envelope","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope","start_line":693}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:da8fef67cf51b47382fb8a1b691562e1","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:df7b1d64f0812fa86dfd410c806570b1","uncertainty":{"grounding":[{"end_line":902,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Staleness of derived surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope%2FStaleness%20of%20derived%20surfaces","start_line":902}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:42ccd429a9a9fad2a7678d7d86f88226","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:489ab6435409e216e3e5962b342a188f","uncertainty":{"grounding":[{"end_line":938,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 3. Step results and disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition","start_line":938}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fac7977dfbd744669e99f2d25e9f5fd2","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1d6224c48fe5d3c554a98c71e9b871a3","uncertainty":{"grounding":[{"end_line":968,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Admission and activation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAdmission%20and%20activation","start_line":968}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:71938e34d846ace8ebec2286af5e0be6","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d6aae782cb81aa9a98afc37213c1e50","uncertainty":{"grounding":[{"end_line":1002,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Construction availability","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FConstruction%20availability","start_line":1002}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d6f2b70971d8b000b0bc66856aeecc55","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a715f999050fe32cda11f33018b9ae9","uncertainty":{"grounding":[{"end_line":1049,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Disposition","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FDisposition","start_line":1049}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cc7b323383fcfa2c3f74f776c758a24b","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f9c599914ff44e8b4d080328ef4cdbbf","uncertainty":{"grounding":[{"end_line":1087,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Ambiguity outcome","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FAmbiguity%20outcome","start_line":1087}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:35b3d4a980b99dce5c34ad5fdcaae1c0","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:304e27191e740a14ff1a5360f96c192a","uncertainty":{"grounding":[{"end_line":1114,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Effects","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F3.%20Step%20results%20and%20disposition%2FEffects","start_line":1114}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a97ea958a71ebd496e745184e389845b","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8112c1d9ca80c0f81b6fffbaccaf4058","uncertainty":{"grounding":[{"end_line":1164,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 4. Totality and refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement","start_line":1164}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e4ec35958cbc102030b980c2a9d74d6d","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fe60a4abb04eaaf1ce62331937b96208","uncertainty":{"grounding":[{"end_line":1210,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Refinement","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FRefinement","start_line":1210}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3c81ede712c119f323c1fb5d444e8837","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6b21eeadc9a4c3f9a3ab684176865732","uncertainty":{"grounding":[{"end_line":1286,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Complete enclosing-relation admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FComplete%20enclosing-relation%20admission","start_line":1286}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:563b489e4c0e97958486b668741feda9","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:93395e367024e30ac50a227dc9423045","uncertainty":{"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Standing structural qualification","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F4.%20Totality%20and%20refinement%2FStanding%20structural%20qualification","start_line":1338}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4f28bd6ba116275baac163c757942728","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:22033e571d79ba6f2d722b08ef8f6957","uncertainty":{"grounding":[{"end_line":1370,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 5. Work state and restart","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart","start_line":1370}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e33600dbd87fc86ffb18bffce4afb09b","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55444d1e0e6c8fc6ece0f11e82e42ede","uncertainty":{"grounding":[{"end_line":1458,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### The workspace and an actor's account","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F5.%20Work%20state%20and%20restart%2FThe%20workspace%20and%20an%20actor%27s%20account","start_line":1458}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2822e9c5b080107580e41fd1d77ced60","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2348700f1fc9d2f2fcf11b79717c0fe5","uncertainty":{"grounding":[{"end_line":1519,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 6. Cost and proportionality","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality","start_line":1519}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a4cff738db76def066e72f7ccae23d77","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:198b48795b15017f083879352e8a1a75","uncertainty":{"grounding":[{"end_line":1627,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Resource limits","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F6.%20Cost%20and%20proportionality%2FResource%20limits","start_line":1627}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:31b025d8f085456e13ca528af18e543f","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:aeca5f74aefda27b57ba696aa98bc091","uncertainty":{"grounding":[{"end_line":1681,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"## 7. Closed result and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse","start_line":1681}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c69c6def9d43e311b87cef0066f827f1","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:779bfa6b7fb6026d7bc35d8d59e9b2d1","uncertainty":{"grounding":[{"end_line":1750,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"### Transition evidence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F7.%20Closed%20result%20and%20reuse%2FTransition%20evidence","start_line":1750}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9d591ca04aa80ad1152ec42925efb0c4","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d7c084f84be762a7a02d3bca00e74d83","uncertainty":{"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"# SDLC default frame guidance","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":1}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7a999890839f91bdc485729c9091f6ab","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f1efd93eac82ee04279f0e6c9c430858","uncertainty":{"grounding":[{"end_line":9,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selection and binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelection%20and%20binding","start_line":9}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9ee92631258617e99d5ef13bf50e26ef","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0d26d3d787b82b4e52ed39f8aa944bee","uncertainty":{"grounding":[{"end_line":28,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Selected default flow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FSelected%20default%20flow","start_line":28}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a829b47921ea575e13eb87f7e8d009a9","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:353842eaa17aecc389d45c5c780a5bd6","uncertainty":{"grounding":[{"end_line":66,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Work reference, context and continuation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FWork%20reference%2C%20context%20and%20continuation","start_line":66}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:bf0f098c3242a1757ca8e8c724167695","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7eeccb8acfff20281aed92698aaf2968","uncertainty":{"grounding":[{"end_line":107,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Causal triage","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FCausal%20triage","start_line":107}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ec9bf06cd4b75edc53ca9d828167a251","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1ddaff9ad5cdb350c55adf8d522c16fe","uncertainty":{"grounding":[{"end_line":139,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"## Verification and stopping","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance%2FVerification%20and%20stopping","start_line":139}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:48d4079e361b476c69e58b28f1511821","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:288b2b57cf91788264f06f5158444194","uncertainty":{"grounding":[{"end_line":1,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"# TICKETS","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS","start_line":1}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5610dcd792d406c17ba71877fbc8013a","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:24a8ce280034b1cbdbda9500c1afda5e","uncertainty":{"grounding":[{"end_line":27,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 1. Work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers","start_line":27}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0748e3280673e89315191ad54ee7e3a7","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4dda5889dc3b394c373ddbf41f26daba","uncertainty":{"grounding":[{"end_line":29,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Goals","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FGoals","start_line":29}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4ebe562ec92492c744ffbb2a177ed9ce","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cefab13899a3eec95583c0b70f0769c7","uncertainty":{"grounding":[{"end_line":37,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Ticket records","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FTicket%20records","start_line":37}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:67d65684a52f19a4ba76762f9a6cb495","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:175be88af46095d15a3581f999210e6a","uncertainty":{"grounding":[{"end_line":45,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprints","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FSprints","start_line":45}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9348eb0b17ab51e64d9e6e8724177ce0","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:95059345cc5ba14701f6a2468d18bb93","uncertainty":{"grounding":[{"end_line":64,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Comments","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FComments","start_line":64}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a41cfac622969bf79edb10358d321170","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ccf76836ad0e8a5b3057591d1f71a51","uncertainty":{"grounding":[{"end_line":76,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contracts","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FExecution%20contracts","start_line":76}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:da9055adcef1a6c67e27a5595d1f0c6d","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1bd4e4631ddf82e966569f02e5ad151f","uncertainty":{"grounding":[{"end_line":101,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Milestones and phase-scoped truth (UP-006)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F1.%20Work%20carriers%2FMilestones%20and%20phase-scoped%20truth%20%28UP-006%29","start_line":101}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:12b62382993b201efc15eb433560cef1","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:665dc3d455890527702945184416553b","uncertainty":{"grounding":[{"end_line":118,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 2. Layout and authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority","start_line":118}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fbf7c7f4c58d86a9c61b70144d8ccea5","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c2606640e448e13bc04c7dbcd588b03d","uncertainty":{"grounding":[{"end_line":120,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Default layout","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FDefault%20layout","start_line":120}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e8ef73329d1fab30fd893bed87c1faba","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a8e3813cac312f0c232760d58fdfd537","uncertainty":{"grounding":[{"end_line":148,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bindings and projections","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FBindings%20and%20projections","start_line":148}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3123e6421e79fd77c0368344c9934fe9","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c535a4b4eadc4143d5d7dd2c96ce3b3c","uncertainty":{"grounding":[{"end_line":165,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier substitution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F2.%20Layout%20and%20authority%2FCarrier%20substitution","start_line":165}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:990e8939db016abecd7b4e320ae56cdd","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:148fde93b9c151b85980430227c61d99","uncertainty":{"grounding":[{"end_line":179,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 3. Sprint rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules","start_line":179}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6787adbbe764e74a49f748cfd2457e9f","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2eb65a18805d48be5cbc62aa42167702","uncertainty":{"grounding":[{"end_line":181,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per sprint","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FOne%20durable%20record%20per%20sprint","start_line":181}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8d1c1f93371700a20c465c5783cbced2","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1a4d5bb17a6d2db5e63951e9e18fd599","uncertainty":{"grounding":[{"end_line":190,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Manifest fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FManifest%20fields","start_line":190}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f94066ece6f3892dd4cb028cf8d7b99f","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a76468a77fd08ec0ac60a81d60676afe","uncertainty":{"grounding":[{"end_line":209,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20status","start_line":209}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2a8292c6a027449a7a4f2e763f0789b0","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:3ca8be99cfd04580ef9e1e609073e493","uncertainty":{"grounding":[{"end_line":220,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Sprint admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FSprint%20admission","start_line":220}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0b899feaff96674b0cacd14abb019749","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:480ad63724075a769d12b25724c756a2","uncertainty":{"grounding":[{"end_line":234,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Compliance escrow","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FCompliance%20escrow","start_line":234}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f52f5f85fe7ff6fbdfd62e5c08907cca","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b70e36657e6d05dacc2f88b6fadce2f7","uncertainty":{"grounding":[{"end_line":261,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Close review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F3.%20Sprint%20rules%2FClose%20review","start_line":261}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:c77363fae2643ef86fe6900e56346a63","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b65a4420ec4d34c1e36c3925bba61dc1","uncertainty":{"grounding":[{"end_line":325,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 4. Ticket rules","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules","start_line":325}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:29dff336cb70463c7e34cf71fbb67a11","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7753ee5278b8d8220dd5cbe227a014b4","uncertainty":{"grounding":[{"end_line":327,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One durable record per ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FOne%20durable%20record%20per%20ticket","start_line":327}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0e7d9a78e1ef59744e102d6d4524562a","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d0e3552799102f530a089d131bcdcf87","uncertainty":{"grounding":[{"end_line":340,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant independence","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FMulti-build-tenant%20independence","start_line":340}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:6763e15d984fba2798d4b3966e61ba98","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:57daa5098984b440797b565ccd6da2bf","uncertainty":{"grounding":[{"end_line":387,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Required fields","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FRequired%20fields","start_line":387}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:db402b110fd0ff41f4e01dec453040c0","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:dc6c2e37caf5e28652358376fb9d5a1e","uncertainty":{"grounding":[{"end_line":408,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Types","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTypes","start_line":408}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b1a61798063fe9a89c413e0afe7bf22b","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2e92a9c8920c09e452a2e18acc822f85","uncertainty":{"grounding":[{"end_line":415,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Category","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FCategory","start_line":415}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:00cd0dd6be90affb2b39dcd94138e577","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7f12dbb95582a2c7f730f9aa6993fc21","uncertainty":{"grounding":[{"end_line":430,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Inside-out sequencing","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FInside-out%20sequencing","start_line":430}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:aa753ab85a3ca4196a0f3cf4f046f306","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ce81d876d3e689c1707f6e2f692d0128","uncertainty":{"grounding":[{"end_line":446,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Change class","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FChange%20class","start_line":446}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fa44b8ff4fff35dae99d7aacd1f7c67b","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:eae45f030c94c44c47ba075ab6d6d1a1","uncertainty":{"grounding":[{"end_line":468,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Upward propagation check","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FUpward%20propagation%20check","start_line":468}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:75c67472d8ce9f781d10755d5568798e","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2966e4a8fb239c7eb9cc6c308606d25b","uncertainty":{"grounding":[{"end_line":508,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Triage metadata","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FTriage%20metadata","start_line":508}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e1f65382da7e00d3a4c6186f5a1a4838","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5af0931d446931d7ee2d0303fca5eabc","uncertainty":{"grounding":[{"end_line":517,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Status","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FStatus","start_line":517}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:91d54481da73f4589cffe4373e6fa290","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e4b3efcb2bfc4fd55aa29da4ac397155","uncertainty":{"grounding":[{"end_line":536,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review findings and bug items","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FReview%20findings%20and%20bug%20items","start_line":536}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:fcd2c31f1bf295d288ee1c9f9021f1ca","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9ff518456b185aaaea39d1657b416a20","uncertainty":{"grounding":[{"end_line":579,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Lanes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F4.%20Ticket%20rules%2FLanes","start_line":579}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:128ceb70b4d51b8267ebcd58e6b31bba","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:19b041cb32911e059e86daed2701621d","uncertainty":{"grounding":[{"end_line":593,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 5. From carrier to execution","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution","start_line":593}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:23344ed36f2a4f7ea205aa8614c01b11","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e7fe483488542c5c34b5581c285fc72c","uncertainty":{"grounding":[{"end_line":608,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Foundation to law: work carriers","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FFoundation%20to%20law%3A%20work%20carriers","start_line":608}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:18403f21ee17fea9b89553d5caa61670","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:55f6126378408d89e2357e9620c29ef1","uncertainty":{"grounding":[{"end_line":672,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Carrier selection","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FCarrier%20selection","start_line":672}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:7dedda0551b1acdfa6815941815d90ac","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8950d31599ac068a0cc437f10e42839c","uncertainty":{"grounding":[{"end_line":746,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution contract admission","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FExecution%20contract%20admission","start_line":746}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:85684c39f43515a90458f162509b7c2c","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9181f717e875d57b8ecd74c2d8c7c233","uncertainty":{"grounding":[{"end_line":770,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Evaluation criteria and non-closure conditions","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FEvaluation%20criteria%20and%20non-closure%20conditions","start_line":770}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e384647e5bbaa604954f1b9667843684","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8130ed360ed8e84bb1f918ea5862cbbd","uncertainty":{"grounding":[{"end_line":792,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Bounded-context term binding","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F5.%20From%20carrier%20to%20execution%2FBounded-context%20term%20binding","start_line":792}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ae0adb6d9d7469c3d0f218c959296376","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:ff0efb108940b7e239b597dfd6b26bb3","uncertainty":{"grounding":[{"end_line":811,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 6. Implementation migration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration","start_line":811}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f14c1cab3597890c1b1c84ec28b50639","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:77e4bd08d9e699d0e5027985f132c23d","uncertainty":{"grounding":[{"end_line":813,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Declaration and checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FDeclaration%20and%20checklist","start_line":813}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f35e94ce94a91c1c1347e1a8aa396a8e","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:38794e02a2115cbb16b0f87abb76002b","uncertainty":{"grounding":[{"end_line":868,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Closure of a migration ticket","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FClosure%20of%20a%20migration%20ticket","start_line":868}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:bfe422e1a67fb234f4ab1d0656b5cf0c","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5cda870a3222a75847aa34fcb2ec02d4","uncertainty":{"grounding":[{"end_line":898,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Strategy requirements","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FStrategy%20requirements","start_line":898}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:deb19e352d67b7a6478c91febae15635","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:778ef0f4ebbd594e48708a535e340037","uncertainty":{"grounding":[{"end_line":918,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recurring realisation and library declaration","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FRecurring%20realisation%20and%20library%20declaration","start_line":918}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d1e80c789fa9046996fd8e0eee78c56f","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:8243a4ecc93f8bf206eaf13fc7a04031","uncertainty":{"grounding":[{"end_line":949,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Multi-build-tenant review","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMulti-build-tenant%20review","start_line":949}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:1ccadade1388f9c5a494aed0a6daecd6","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d3c9998459e383d18220b110e47798f","uncertainty":{"grounding":[{"end_line":960,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Review disambiguation","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FReview%20disambiguation","start_line":960}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a92d7ef6fcf7e68ac15d372e73cb55cb","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4d468d62446a2674f2c56af24006f011","uncertainty":{"grounding":[{"end_line":1000,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Impacted interface review checklist","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FImpacted%20interface%20review%20checklist","start_line":1000}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:9eeba2f86d6b498d1757cfc29f35db85","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f3ccb6274556c15ca20b323d6a7912d0","uncertainty":{"grounding":[{"end_line":1035,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Break order and break-to-closure map","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FBreak%20order%20and%20break-to-closure%20map","start_line":1035}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:cf857b66f24a4013665f7f6329c70e40","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f99c383afa81c78c769e56a0385af1ba","uncertainty":{"grounding":[{"end_line":1064,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Mixed-state negative proof","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F6.%20Implementation%20migration%2FMixed-state%20negative%20proof","start_line":1064}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:110659fee9c4e2b8759d7c47c847108e","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f16a036f6e0242fc2a4232012f8a86ff","uncertainty":{"grounding":[{"end_line":1093,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 7. Authority, judgment, closure and state","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state","start_line":1093}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2bdcf291a9040772f48df762fd9a811a","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4c0d38b06add273b8262e123dc603c73","uncertainty":{"grounding":[{"end_line":1103,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Execution and verification authority separation (UP-007)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FExecution%20and%20verification%20authority%20separation%20%28UP-007%29","start_line":1103}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:209ab758ba61329598b1cb011eacc616","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:a3957b6c5aa85512eaafc5ecc923f804","uncertainty":{"grounding":[{"end_line":1161,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Recorded judgment and owner-ruling continuity","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FRecorded%20judgment%20and%20owner-ruling%20continuity","start_line":1161}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:761876cf1b86c68a5ef43c98c52afbf7","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:25c172e7d5c86c1c87953fa016b63d45","uncertainty":{"grounding":[{"end_line":1249,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Condition-based closure and reuse","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FCondition-based%20closure%20and%20reuse","start_line":1249}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:d8f1b576f8b980b1570eeca555b79a7d","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:576e967eef5938037bcb9508f64e1394","uncertainty":{"grounding":[{"end_line":1292,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Test case authority","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FTest%20case%20authority","start_line":1292}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:56b91f980e70b75b1c79d5a8eeee5374","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e3789c9e24e88aacee0987a8b0a49e1b","uncertainty":{"grounding":[{"end_line":1338,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### One-truth state projection and drift refusal (UP-009)","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F7.%20Authority%2C%20judgment%2C%20closure%20and%20state%2FOne-truth%20state%20projection%20and%20drift%20refusal%20%28UP-009%29","start_line":1338}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:2dcb600e8858a2eac9d7dda2afa59f8c","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:0dbef1b28168b242013beeebd2089719","uncertainty":{"grounding":[{"end_line":1352,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 8. Recommended shapes","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F8.%20Recommended%20shapes","start_line":1352}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:271bb05ae54d88b82a192165ef4d396f","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:063c155871c928bf0de1871ab8596464","uncertainty":{"grounding":[{"end_line":1507,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"## 9. Operating mode and relationships","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships","start_line":1507}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:e01338d4ed9c83650759782e5cf92744","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:b0a395d11f87040b91bd7249fb10bafc","uncertainty":{"grounding":[{"end_line":1509,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Operating mode","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FOperating%20mode","start_line":1509}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:5350eac7483ffdb0e7cade948a68e156","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:11bcfd20a2217bb67a38a7e38ed8c325","uncertainty":{"grounding":[{"end_line":1523,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md","quote":"### Relationship to other surfaces","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md#TICKETS%2F9.%20Operating%20mode%20and%20relationships%2FRelationship%20to%20other%20surfaces","start_line":1523}],"statement":"This bounded visual preserves source structure and selected separately attributed annotations. The remainder of this section's body meaning, including requirements, qualifications, examples and cross-source dependencies, is not comprehensively represented."},"consequence":"Re-enter the exact embedded source for any decision depending on unrepresented meaning. A section node or processing disposition does not establish semantic coverage, applicability or acceptance.","re_entry":[]},{"id":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:30ac9621ca49f40c14754e7ac1a4d731","subject":"urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e","uncertainty":{"grounding":[{"end_line":703,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md","quote":"Qualified-reference guidance. Under\n[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) and\n[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), a reference can supply\nsufficient context when its accessible target and qualifications preserve\nthe consuming contract. Check the required subject and basis, assessment\nstanding, provenance, active obligation and version, and invalidators, rather\nthan candidate identity alone. A typed annotation supplies no evidence of\nsufficiency by itself. Preserve the required body or a qualified resolvable\nreference; no mandatory carrier or registry follows (P1, P3, P6).","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md#ACTIVATION%2F2.%20Context%20construction%20under%20an%20envelope","start_line":695},{"end_line":7,"path":"build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md","quote":"This is a selectable projection of existing method law for ordinary software\nwork. It connects the current work reference and bounded context to QA,\ndiagnosis, re-entry, verification and durable continuation;\nthe linked sections remain the single deciding owners. It adds no result,\nactor, workflow engine, permission or mandatory Executive configuration.","section":"urn:a-c:project:77d5569c2ffe57de8004b53fef4cfa650e8bbf11ba59f7bd47ec641183ed6503/source/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md#SDLC%20default%20frame%20guidance","start_line":3}],"statement":"This visual selects three complete native members for navigation and a finite set of annotations. Referenced owners such as FOUNDATIONS, AXIOMATIC_CALCULUS, REFERENCE_FRAME, EVALUATION and SPEC_METHOD are not semantically distilled here. The Axiom calculus copy is conversion provenance only."},"consequence":"Re-enter the exact native cut and applicable owners before making a governing decision; this graph is not a purpose context index or a substitute constitution.","re_entry":[]}],"transformations":[],"traversals":[],"judgments":[]},"field_selection":{"objects":["id","value"],"relations":["id","source","target","qualifiers"],"constraints":["id","applies_to","predicate"],"latitude":["id","applies_to","allowed_variation","forbidden_variation"],"residuals":["id","subject","uncertainty","consequence","re_entry"],"transformations":null,"traversals":null,"judgments":null},"limit":"Exact fields projected from every population record for source-fidelity assessment. Omitted common formal basis/context/owner/scope/kind references and signature remain in full model; structural mechanics are separately observed, not semantically certified by this projection."}



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/scripts/visual_31_annotations.json
SHA256 f11a9091ef1fd2e726d6634969e52d47adeab25c09b49525a46c8d6f678b019f; 39644 bytes

{
  "profile": "stdo-representation.bounded-authored-annotations/1",
  "source_cut": "v3.1.0-rc.1",
  "scope": "Complete source-section navigation for ACTIVATION.md, SDLC_DEFAULTS.md and TICKETS.md, plus these selected SDLC/work-carrier/context annotations. Navigation coverage is not semantic coverage.",
  "limitations": [
    "All declared sections receive residual dispositions: their structure and source location are represented, while body meaning is not comprehensively modeled.",
    "Only the explicitly listed authored annotations assert selected body meanings. They require independent source-first assessment for their exact subject.",
    "The remaining native members and referenced owners are unrepresented meaning, not missing requirements inferred false or satisfied.",
    "No operational judgments, traversals or transformations are instantiated. No Lean/formal claim, context selection, workflow execution or code-correctness claim is made.",
    "Governing flags on the authored relations describe retention dependencies in this model; they grant no authority to a reader or tool.",
    "Historical 3.0.5 models and semantic verdicts are not reused or rebound."
  ],
  "annotations": [
    {
      "family": "concepts",
      "record": {
        "key": "sdlc_guidance",
        "label": "Selectable SDLC guidance",
        "definition": "A selectable projection of existing method law for ordinary software work, linking the work reference and bounded context to QA, diagnosis, re-entry, verification and continuation. It creates no new result, actor, workflow engine, permission or mandatory Executive configuration.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "This is a selectable projection of existing method law for ordinary software\nwork. It connects the current work reference and bounded context to QA,\ndiagnosis, re-entry, verification and durable continuation;\nthe linked sections remain the single deciding owners. It adds no result,\nactor, workflow engine, permission or mandatory Executive configuration."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "selected_frame_basis",
        "label": "Accepted Project Reference-Frame Basis",
        "definition": "The Product-owned basis selects this guidance with its exact source and governing cut while retaining Product policy values, explicit gates and accepted alternatives.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Select this guidance in the accepted Project Reference-Frame Basis, binding\nits exact source identity and the governing method cut. The\n[basis template](templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#sdlc-default-selection)\nproposes it ready for adoption. An existing Product may select it through its\nown authorized basis change; merely installing or finding it selects nothing.\nKeep the Product's policy values, explicit gates and accepted alternatives.\nNo numeric priority cutoff, review ratio or additional gate is supplied here."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "work_reference",
        "label": "Selected work carrier",
        "definition": "The selected ticket, sprint entry or run contract is the work reference for its current question, exact subject and basis, result/evidence references and surviving obligations. It supplies no new authority by being present.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6)."
        },
        {
          "file": "TICKETS.md",
          "quote": "Absence of a durable ticket neither requires nor authorises creating one.\nAn exact product-authorised work instruction may supply the upstream work\nauthority for a one-run contract; a generic request or a model-widened\nscope cannot. A durable ticket is created or updated only when the table\nrequires surviving state and the actor holds ticket-state authority. An\nexplicit instruction from ticket-state authority to create a durable record\nselects that durability; it does not admit an execution contract or widen\nits upstream work authority (P6, P2)."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "bounded_context",
        "label": "Bounded context acquisition",
        "definition": "Acquisition of the deciding owners and current material subject for the next bounded decision. Qualified references must preserve the consuming contract, standing, provenance, active obligations and invalidators; a typed pointer alone proves no sufficiency.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "Qualified-reference guidance. Under\n[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) and\n[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), a reference can supply\nsufficient context when its accessible target and qualifications preserve\nthe consuming contract. Check the required subject and basis, assessment\nstanding, provenance, active obligation and version, and invalidators, rather\nthan candidate identity alone. A typed annotation supplies no evidence of\nsufficiency by itself. Preserve the required body or a qualified resolvable\nreference; no mandatory carrier or registry follows (P1, P3, P6)."
        },
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "work_state",
        "label": "Persistent current work state",
        "definition": "The workspace and authoritative inputs persist across activations. Their current material state decides what the work has and has not done.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "The workspace and its authoritative inputs persist across activations and\nare the continuing truth surface of the work: the surface whose current\nmaterial state decides what the work has and has not done. An actor's\ncontext is an account of that state. It is bounded, because it is a\nprojection of the state (§2); revisable, because an observation can\ncorrect it; and disposable, because a step records its closed results and\nstep-produced facts before it returns (§1 Admission; P4b). An account is\nnever a second truth surface, and no later activation needs a prior\nactor's context: its intake reconstructs the governing relations without\nit (§1 Intake) (P0, P3, P6)."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "actor_account",
        "label": "Disposable actor account",
        "definition": "An actor context is a bounded, revisable and disposable account of work state. It is not a second truth surface and the next activation need not inherit it.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "The workspace and its authoritative inputs persist across activations and\nare the continuing truth surface of the work: the surface whose current\nmaterial state decides what the work has and has not done. An actor's\ncontext is an account of that state. It is bounded, because it is a\nprojection of the state (§2); revisable, because an observation can\ncorrect it; and disposable, because a step records its closed results and\nstep-produced facts before it returns (§1 Admission; P4b). An account is\nnever a second truth surface, and no later activation needs a prior\nactor's context: its intake reconstructs the governing relations without\nit (§1 Intake) (P0, P3, P6)."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "closed_result",
        "label": "Closed result and provenance",
        "definition": "A closed result identifies its frame/activation, subject, basis, evaluation, actor, evidence, verdict, residual uncertainty and invalidation conditions. Handoff sufficiency is relative to the consuming decision.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "A closed result identifies the frame and its activation, the subject, the\nbasis, the evaluation, the actor, the evidence, the verdict, the residual\nuncertainty and the invalidation conditions (the minimal shape is\nREFERENCE_FRAME §13). The frame's internal working context need not be\ntransferred when the closed result and its provenance are sufficient for\nthe consuming decision; it may still be attached, for audit or otherwise,\nwithout changing the result. Independent evaluations may share valid\nmechanical evidence under the declared independence conditions of\n[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that\npermission (P4b, P0)."
        }
      ]
    },
    {
      "family": "concepts",
      "record": {
        "key": "owner_ruling",
        "label": "Recorded owner ruling",
        "definition": "An owner ruling retains its original wording, owner, exact subject and basis, permitted scope/effects, conditions and source, separately from agent interpretation.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "A direct or lawfully proxied owner ruling is recorded in its original\nwording, with its owner, exact subject and basis, permitted scope and\neffects, conditions and source, separately from agent interpretation. Later\nwork consumes that same ruling while it applies; it neither widens the\nruling nor requests unchanged authority again. New ambiguity or a\nmaterially changed decision returns only the affected question to its\nowner. J is not O, and recording either cannot create admission,\nacceptance, effects or continuation beyond the original grant (P6, P3)."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "basis_selects_sdlc",
        "source_key": "selected_frame_basis",
        "target_key": "sdlc_guidance",
        "kind": "selects_guidance",
        "meaning": "An accepted Product frame basis selects exact SDLC guidance and governing method cut.",
        "governing": true,
        "conditions": [
          "Selection occurs through the Product's authorized basis change."
        ],
        "exceptions": [
          "Merely installing or finding guidance selects nothing."
        ]
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Select this guidance in the accepted Project Reference-Frame Basis, binding\nits exact source identity and the governing method cut. The\n[basis template](templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#sdlc-default-selection)\nproposes it ready for adoption. An existing Product may select it through its\nown authorized basis change; merely installing or finding it selects nothing.\nKeep the Product's policy values, explicit gates and accepted alternatives.\nNo numeric priority cutoff, review ratio or additional gate is supplied here."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "carrier_routes_context",
        "source_key": "work_reference",
        "target_key": "bounded_context",
        "kind": "applies_context_owner",
        "meaning": "The selected carrier applies ACTIVATION section 2 to bounded acquisition using its exact current work bindings.",
        "governing": true,
        "conditions": [
          "Bind current question, subject/basis, result/evidence references and surviving obligations."
        ],
        "exceptions": [
          "This relation creates no additional carrier requirement and confers no ticket-state authority."
        ]
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6)."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "carrier_routes_restart",
        "source_key": "work_reference",
        "target_key": "work_state",
        "kind": "applies_restart_owner",
        "meaning": "The selected carrier applies ACTIVATION section 5 to current work state, the disposable actor account and resumption.",
        "governing": true,
        "conditions": [
          "Resume from current material state and reconcile effects needed by the next dependent action."
        ],
        "exceptions": [
          "A summary or actor account cannot replace governing sources or current evidence."
        ]
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6)."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "carrier_routes_reuse",
        "source_key": "work_reference",
        "target_key": "closed_result",
        "kind": "applies_reuse_owner",
        "meaning": "The selected carrier applies ACTIVATION section 7 to closed results and reuse and retains step-produced facts and owner rulings on the named evidence surface.",
        "governing": true,
        "conditions": [
          "Use existing admission and continuity law and check applicability."
        ],
        "exceptions": [
          "No new ticket-state authority follows."
        ]
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6)."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "current_state_corrects_account",
        "source_key": "work_state",
        "target_key": "actor_account",
        "kind": "corrects_account",
        "meaning": "Current material evidence corrects a contrary cached belief, retained summary or prior result; undecidable facts remain explicit unknowns.",
        "governing": true,
        "conditions": [
          "Reconciliation stays within the actor's grant."
        ],
        "exceptions": [
          "When needed operations, territory or decisions exceed the grant, stop with re_entry_requested(authority) naming the owner."
        ]
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "Acquisition ([§2](#2-context-construction-under-an-envelope)) observes the\ncurrent subject and its authoritative inputs. Where they materially\ndisagree with a cached belief, a retained summary or a prior result, the\nactor reconciles the disagreement: current evidence corrects the account,\nand what the evidence cannot decide stays an explicit unknown. A stored\nbelief, a summary or a successful prior result never overrules contrary\ncurrent evidence. A prior result is relied on only after its\napplicability and invalidators are checked against the current subject\nand inputs (§7). The actor corrects its account within its grant; where\nresolving the disagreement needs an operation, a territory or a decision\noutside the grant, the step stops with `re_entry_requested(authority)`,\nnaming the owner of what it needs (§3 Construction availability) (P5,\nP6)."
        }
      ]
    },
    {
      "family": "relations",
      "record": {
        "key": "owner_ruling_bounds_continuation",
        "source_key": "owner_ruling",
        "target_key": "work_reference",
        "kind": "bounds_continuation",
        "meaning": "Later work consumes the original ruling while it applies, without widening it or requesting unchanged authority again.",
        "governing": true,
        "conditions": [
          "Exact subject, basis, permitted scope/effects and conditions remain applicable."
        ],
        "exceptions": [
          "New ambiguity or a materially changed decision returns only the affected question to the owner; recording creates no new grant."
        ]
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "A direct or lawfully proxied owner ruling is recorded in its original\nwording, with its owner, exact subject and basis, permitted scope and\neffects, conditions and source, separately from agent interpretation. Later\nwork consumes that same ruling while it applies; it neither widens the\nruling nor requests unchanged authority again. New ambiguity or a\nmaterially changed decision returns only the affected question to its\nowner. J is not O, and recording either cannot create admission,\nacceptance, effects or continuation beyond the original grant (P6, P3)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "context_fit_is_conditional",
        "applies_to_keys": [
          "bounded_context"
        ],
        "statement": "Where the selected envelope declares context capacity, record the required measurement, capacity and comparison before reading. Complete-fit judgment remains unresolved without complete active inputs or a supported upper bound, unless measured excess falsifies it.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "The selected envelope declares context capacity."
        ],
        "exceptions": [
          "Where no capacity is declared, no measurement gate is added."
        ]
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "context_reenters_stale_source",
        "applies_to_keys": [
          "bounded_context"
        ],
        "statement": "A stale or insufficient derived surface requires re-entry to the exact owning sections; a summary or index supplies no work-state authority, governing meaning or current material evidence by itself.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Acquire the deciding owners and current material subject needed by the next\nbounded decision. An accessible qualified reference must preserve the\nconsumer's subject/basis, assessment standing, provenance, active obligations\nand invalidators. If a derived surface is stale or insufficient, re-enter the\nexact owning sections. Where the selected envelope declares context capacity,\nrecord the required measurement, capacity and comparison before reading.\nWithout complete active inputs or a supported upper bound, complete-fit\njudgment remains unresolved unless a measured excess falsifies it. Where no\ncapacity is declared, no measurement gate is added. Source:\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)."
        },
        {
          "file": "TICKETS.md",
          "quote": "The selected carrier is also the work reference for context construction and\ncontinuation: bind its current question, subject and basis, result and evidence\nreferences, and surviving obligations. Apply\n[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that\nbounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current\nwork state, the disposable actor account and resumption, and\n[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.\nThe ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);\nan actor's account cannot replace the carrier, governing sources or current\nevidence. Preserve results, step-produced facts and owner rulings through\nthe named result and evidence surface under existing admission and\n[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies\nthose owners to the selected carrier; it creates no additional carrier\nrequirement and confers no ticket-state authority (P0, P3, P4b, P6)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "ticket_absence_does_not_authorize_creation",
        "applies_to_keys": [
          "work_reference"
        ],
        "statement": "Absence of a durable ticket neither requires nor authorizes creating one. Required surviving state and ticket-state authority govern creation/update; selecting durability does not admit an execution contract or widen upstream work authority.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "Absence of a durable ticket neither requires nor authorises creating one.\nAn exact product-authorised work instruction may supply the upstream work\nauthority for a one-run contract; a generic request or a model-widened\nscope cannot. A durable ticket is created or updated only when the table\nrequires surviving state and the actor holds ticket-state authority. An\nexplicit instruction from ticket-state authority to create a durable record\nselects that durability; it does not admit an execution contract or widen\nits upstream work authority (P6, P2)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "record_result_before_return",
        "applies_to_keys": [
          "closed_result"
        ],
        "statement": "Before return, a permitted Writer records the closed result, needed step-produced facts, evidence, unresolved work, original rulings and lawful next action or owner re-entry in the existing named durable result/evidence surface.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "The actor holds the necessary Writer effects."
        ],
        "exceptions": [
          "An actor without those effects returns to the permitted Writer; Executive performs no file or Git mutation in that role. No second state ledger or per-tool log is added."
        ]
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Before return, a permitted Writer records the closed result, step-produced\nfacts needed later, evidence, unresolved work, original owner rulings and the\nnext authorized action or owner re-entry in the existing named durable\nresult/evidence surface. Keep references with the owning work. This projection\nadds no second state ledger or per-tool logging requirement. An actor without those effects\nreturns to the permitted Writer; Executive still performs no file or Git\nmutation in that role. Sources:\n[ACTIVATION admission](ACTIVATION.md#admission),\n[closed results](ACTIVATION.md#7-closed-result-and-reuse),\n[TICKETS continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "invalidate_affected_reuse",
        "applies_to_keys": [
          "closed_result"
        ],
        "statement": "Check exact applicability before reuse. Material input change, changed basis or a declared revising observation invalidates the affected result before reliance; retain its predecessor/successor relation and demonstrably independent surviving results.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "The change can alter the result, or changes a bound basis coordinate, or is the declared revising observation."
        ],
        "exceptions": [
          "Role, conversation or resumption change alone invalidates nothing. Changed coordinates alone establish neither claim failure nor success."
        ]
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "A closed result is reused by an unchanged consumer that checks exact\napplicability; a role, conversation or resumption change alone invalidates\nnothing. An invalidator invalidates the affected result before reliance,\neven where the subject's own bytes are unchanged, preserving its\npredecessor/successor relation and any demonstrably independent surviving\nresults. Invalidation withdraws the result from direct reliance; whether\nits evidence is retained on the new basis is decided by `retain_applicable`\nof FOUNDATIONS §4 Change impact and evidence reuse, and the changed\ncoordinate alone establishes neither that the claim fails nor that it\nholds. The invalidators are three:\n\n- a material input change: a change to the result's subject or to an\n  input it rests on, including the admissible evidence that bears on its\n  predicate; newly acquired or changed admissible evidence is such a\n  change when it is material to the result as\n  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,\n  when it could change the result's value;\n- a changed basis: a change to any coordinate of the basis the result\n  binds (FOUNDATIONS §2, Basis);\n- a declared revising observation: an observation that the result or\n  judgment itself names as one that would revise it, once it occurs."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "reuse_preserves_independence",
        "applies_to_keys": [
          "closed_result"
        ],
        "statement": "Required independent assessment may consume valid computed facts, but its assessor acquires sufficient exact evidence and supplies its own judgment under the actual independence condition. Reusing the author's judgment cannot satisfy it.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "Independent assessment is required by the actual governing boundary."
        ],
        "exceptions": [
          "A new role or conversation alone does not invalidate otherwise applicable work."
        ]
      },
      "grounds": [
        {
          "file": "TICKETS.md",
          "quote": "Later roles and resumed runs recover the result and check its\napplicability rather than re-author unchanged judgment. Reuse and\ninvalidation are\n[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): changed material\ninputs, a declared revising observation or a changed basis invalidate\nthe affected result, preserving the original result and its successor\nrelation and keeping only demonstrably independent results, and a new\nrole or conversation alone invalidates nothing. For a recorded judgment\nthe material inputs include its supporting computed facts and evidence,\nand its declared revising observation is the one the record states;\nreassessment covers what the change affects. The result may reference\ncurrent C outputs; reuse cannot silently turn unknown facts into\nestablished premises (P4b, P5). Required independent assessment may consume valid C, but\nits assessor acquires sufficient exact evidence and supplies its own\njudgment under the actual independence condition; reusing the author's J\ncannot satisfy that condition (P6; EVALUATION §3)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "local_qa_has_bounded_claim",
        "applies_to_keys": [
          "sdlc_guidance"
        ],
        "statement": "Incremental QA checks the admitted step against its requirement/design and the smallest adequate falsifier, naming observed predicate, subject, oracle, coverage and residuals. A local pass supports that bounded predicate and no unnamed Product acceptance, qualification or release claim.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "Preserve selected gates and mandatory conditions."
        ],
        "exceptions": []
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "2. **Construct and perform incremental QA.** Check the admitted step against\n   its requirement/design and the smallest adequate falsifier. State the\n   observed predicate, subject, oracle, coverage and residuals. A local pass\n   supports that bounded predicate; it supplies no unnamed Product acceptance,\n   qualification or release claim. Preserve selected gates and mandatory\n   conditions. Sources: [ASSURANCE](ASSURANCE.md),\n   [EVALUATION §1](EVALUATION.md#1-claims) and\n   [EVALUATION §5](EVALUATION.md#landing-closure-and-release)."
        }
      ]
    },
    {
      "family": "constraints",
      "record": {
        "key": "triage_distinguishes_four_causes",
        "applies_to_keys": [
          "sdlc_guidance"
        ],
        "statement": "Causal triage distinguishes defective realization under adequate unchanged law, inadequate requirement/design, inaccurate predictive model and insufficient observation. Their lawful routes remain different; repeated uninformative checks supply no missing evidence.",
        "uncertainty": "Bounded authored annotation; exact source and referenced owners decide applicability.",
        "conditions": [
          "Use evidence that distinguishes causes over the same exact subject and basis."
        ],
        "exceptions": [
          "A failed candidate alone does not establish inadequate governing law; insufficient observation keeps indeterminate and withholds the dependent claim."
        ]
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "| Supported cause | Lawful next action |\n|---|---|\n| Defective realisation under adequate unchanged law | Repair the realised surface within its grant; assert and verify no upstream drift. |\n| Inadequate governing requirement or design | Return to the first inadequate owner; admit its changed truth, then derive affected downstream work and evidence. A failed candidate alone does not establish this cause. |\n| Inaccurate predictive model | Return to the model's owner, identify the failed prediction and supported replacement/intervention, then re-evaluate the dependent claims. Do not relabel an outcome mismatch as a code defect without evidence. |\n| Insufficient observation | Acquire the missing admissible observation through its authorized route, or retain `indeterminate` and withhold the dependent claim. Repetition of the same uninformative check supplies no missing evidence. |"
        }
      ]
    },
    {
      "family": "latitude",
      "record": {
        "key": "resume_preserves_valid_progress",
        "applies_to_keys": [
          "work_reference"
        ],
        "allowed": [
          "Resume from current material state, correct a contrary account and reopen only affected support after exact applicability/invalidator checks.",
          "Handoff sufficient closed results and references without the prior actor's private conversation."
        ],
        "forbidden": [
          "Retry or take a dependent action before reconciling uncertain external effects.",
          "Treat unresolved completion as established completion."
        ]
      },
      "grounds": [
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "Resume from current material state, correct a contrary retained account,\ncheck exact applicability and invalidators, and reopen only affected support.\nReconcile uncertain external effects before a retry or dependent action;\nunresolved completion remains unresolved. Handoff needs sufficient closed\nresults and references, not the prior actor's private conversation. Sources:\n[ACTIVATION state and restart](ACTIVATION.md#5-work-state-and-restart),\n[actor account](ACTIVATION.md#the-workspace-and-an-actors-account) and\n[reuse](ACTIVATION.md#7-closed-result-and-reuse)."
        }
      ]
    },
    {
      "family": "residuals",
      "record": {
        "key": "unmodeled_governing_dependencies",
        "subject_key": "bounded_context",
        "uncertainty": "This visual selects three complete native members for navigation and a finite set of annotations. Referenced owners such as FOUNDATIONS, AXIOMATIC_CALCULUS, REFERENCE_FRAME, EVALUATION and SPEC_METHOD are not semantically distilled here. The Axiom calculus copy is conversion provenance only.",
        "consequence": "Re-enter the exact native cut and applicable owners before making a governing decision; this graph is not a purpose context index or a substitute constitution."
      },
      "grounds": [
        {
          "file": "ACTIVATION.md",
          "quote": "Qualified-reference guidance. Under\n[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) and\n[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), a reference can supply\nsufficient context when its accessible target and qualifications preserve\nthe consuming contract. Check the required subject and basis, assessment\nstanding, provenance, active obligation and version, and invalidators, rather\nthan candidate identity alone. A typed annotation supplies no evidence of\nsufficiency by itself. Preserve the required body or a qualified resolvable\nreference; no mandatory carrier or registry follows (P1, P3, P6)."
        },
        {
          "file": "SDLC_DEFAULTS.md",
          "quote": "This is a selectable projection of existing method law for ordinary software\nwork. It connects the current work reference and bounded context to QA,\ndiagnosis, re-entry, verification and durable continuation;\nthe linked sections remain the single deciding owners. It adds no result,\nactor, workflow engine, permission or mandatory Executive configuration."
        }
      ]
    }
  ]
}



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/ACTIVATION.md
SHA256 56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d; 142205 bytes

# ACTIVATION

Tier 1. Owns how bounded work proceeds: the step (transitions from a
current state to a destination, intake, execution unit, admission,
applicability with exclusion, output, the configuration of
responsibilities over frames and its admission, roles and delegation,
recording a result without review); context construction under an
envelope, with the size measurement and fit test, acquisition, activation,
evaluation and the staleness of derived surfaces; the
refinements of the core for admission and activation and for the step's
results, and disposition; totality and refinement, with the hard stops,
licensing and approximate steps; work state and restart, with the workspace and an
actor's account; cost and proportionality, with the resource-limit law;
the closed result, its invalidators and reuse. It uses
the objects of [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology), the core result
algebra of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), and the frame
object and the outcomes of `activate` of
[REFERENCE_FRAME](REFERENCE_FRAME.md) (§5). It defines the step-level
concepts it introduces, among them the current state, the destination,
the transition, the configuration, the execution unit, acquisition, the
rewrite step, the licensing law, the adequacy relation, the work state,
the actor's account, progress and churn, proportionality and the closed
result, and refines the
core for admission, activation and steps (§3); it redefines nothing those
members own.

## 1. The step

A step is the activation of one reference frame, or one declared active
frame configuration, on an exact subject (REFERENCE_FRAME §1, §11). Its
context is the projection of that activated frame to the actor; the corpus
or the workspace is never the context (P0; RF-002). Intake, admission,
applicability and activation are distinct relations inside the step even
when one invocation performs all of them.

When construction is delegated to a probabilistic or agentic worker, the
method governs the execution relation without prescribing the worker's
model, prompt, tools, internal search, process topology, repository layout
or orchestration runtime (P0; the work boundary of FOUNDATIONS §2). The
normative relation runs: accepted governing basis; bounded affected
relation set; selected computational relations; delegated execution and
decision authority; construction and self-review; independent live-surface
assessment where required; one of accept, local repair, re-enter or reject
(§3); the exact accepted checkpoint; the next already-authorised bounded
action (§5).

Use [Transitions](#transitions), [Intake](#intake), [Admission](#admission),
[Applicability](#applicability), [Configuration](#configuration), and
[Roles and delegation](#roles-and-delegation) for the deciding rules.
The following table traces those owners to their premises.

Foundation to law. This family, transitions, steps and configuration,
covers this section and §4. Its instance premises are: (a) a selected
outcome with its acceptance conditions; (b) work that may exceed one
activation's capacity; (c) actors with declared capability envelopes; (d)
an admitted grant. They are conditions of the work this family governs,
not commitments, and do not follow from finite capacity alone. The
standing of the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P0 (recovered), P2 (independent); instance premises a, b | By P0 an actor's context is bounded, and by P2 work serves a selected destination, so work that exceeds one activation reaches its destination through bounded transitions, each binding the current state, the destination and the obligations it preserves | [Transitions](#transitions); [Intake](#intake); [Execution unit](#execution-unit) | the destination and its acceptance conditions: the owning authority of the selected outcome | 1, 5 |
| P0 (recovered), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); instance premise d | By P0 and P4b an actor cannot recover a governing relation from memory, and by P6 admission is a separate authority, so a step starts only from an intake that reconstructs its governing relations without history, and only after an admission its drafting actor does not certify; its output is a candidate with its step-produced facts | [Intake](#intake); [Admission](#admission); [Output](#output) | the carrier (ticket, sprint entry, run-scoped contract): [TICKETS](TICKETS.md) | 5, 9 |
| P1 (independent), P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P1 a premise's form is not its truth, by P6 applicability is decided on evidence, and by P5 an unresolved premise is undecided, so applicability is decided from basis-bound facts and is itself a result in the core; an unresolved premise withholds the dependent claim and is never read as false; an excluded obligation, after a `falsified` applicability result, has no result and maps to no core value, and a `satisfied` for a disjunction that includes non-application counts toward that disjunction only | [Applicability](#applicability), with Exclusion and the core | which obligations apply to a subject: the owning evaluation and its scope declarations; a predicate declared as a disjunction that includes non-application: the owner of that predicate | 9, 6 |
| P0 (recovered), P2 (independent), P4a (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premises b, c, d | By P4a responsibilities compose through declared operations and dependencies, by P6 a decision belongs to its owner, and by P0 and P5 each frame must fit a finite actor, so responsibilities are allocated to frames from operations, dependencies, capabilities and assurance; no role inventory, hierarchy or actor sequence follows; reconfiguration keeps dependencies, obligations, effects, authority and independence; a configuration is admitted only by the authority that owns the decision it makes, and its admission creates no authority | [Configuration](#configuration), with Admission of a configuration; [Roles and delegation](#roles-and-delegation) | the configuration (frames, topology, coordinator, role names) and its explanation: the design that selects it; which authority owns which decision: the method or profile that applies the rule, [EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration) for the executive configuration; the executive configuration: [EXECUTIVE_BASELINE](EXECUTIVE_BASELINE.md) | 7, 9 |
| P6 (independent), P2 (independent), P0 (recovered); instance premise d | By P6 a record is no assessment or acceptance unless the law requires one, by P2 a step with no route to the outcome is unjustified, and by P0 the record must outlive the actor, so where the applicable law requires no assessment and reserves no acceptance, the grant holder may record the conditions it found satisfied in the existing result surface without adding ceremony, because a step with no route to the outcome is unjustified; the record is no disposition and waives no condition that applies | [Roles and delegation](#roles-and-delegation), Recording a result without review | which conditions require assessment or reserve acceptance: the applicable law and the governing grant; the carrier: [TICKETS](TICKETS.md) | 9, 1 |
| P2 (independent), P6 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P2 completion is measured against the destination, by P6 and P5 only evidence can establish it, and by P4b a stop's cause persists, so completion needs evidence against the applicable destination; a count, an empty list or a revised destination is no such evidence; a stop names its cause and keeps what is owed | [Transitions](#transitions): Completion, Destination change, Stops | accepting a completion claim: the decision owner ([§3 Disposition](#disposition)) | 1, 5, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P2 (independent), P6 (independent); instance premise d | By P5 a non-satisfied result leaves the outcome undecided or failed, by P2 work continues only toward the outcome, and by P6 a hard stop is no policy decision, so every non-satisfied result has a named next move, an explicit unknown class included, and reconfiguration follows the cause; a hard stop holds whatever the risk appetite | [§4](#4-totality-and-refinement), Hard stops and the paragraphs before Refinement | the ambiguity policy and its risk appetite: the project's declared policy ([SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)) | 5 |
| P4a (independent), P1 (independent), P6 (independent); instance premise b | By P4a a step composes only under declared laws, by P1 structural success does not establish meaning, and by P6 preservation needs evidence, so a refinement or rewrite step is admissible only under a law declared for its subject, and each layer discharges what it preserves; a refinement is faithful only when its steps are exact and each output meets the next step's declared domain; a composite with an approximate step is adequate only within its stated adequacy relation and end-to-end bound | [Refinement](#refinement) | the laws declared for a subject: the subject's owner | 3, 4 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P3 (independent), P6 (independent); instance premise d | By P4b a partial commit would leave facts that later steps cannot reconcile, by P3 the relation binds one basis identity, and by P6 admission is the owner's act, so admission of a material transition derives and validates the complete enclosing relation on one basis identity and commits all of it or none; qualification covers every admission owner and supported boundary | [Complete enclosing-relation admission](#complete-enclosing-relation-admission); [Standing structural qualification](#standing-structural-qualification) | the supported boundaries and the operating or threat model: the accepted design | 4, 9 |
| P2 (independent), P3 (independent), P1 (independent), P6 (independent); instance premise a | By P2 the destination is a set of required conditions that several realised states may satisfy, by P3 the current state is the bound subject with its observations and dependencies, by P1 the required conditions, the observations and any predictive model are different accounts, and by P6 lawfulness confers no delivery or acceptance, so construction binds A and Z explicitly, works under the declared calculi, and keeps the three accounts apart | [Construction relation](#construction-relation), Binding A and Z, Three accounts | the governing specification that supplies Z: the owning authority of the selected outcome; the declared calculi: SPEC_METHOD §11 for a build tenant | 1, 5, 6, 8 |
| P0 (recovered), P2 (independent), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premises b, c | By P0 context and attention are finite, and the time, spend and other resources of the selected execution binding are finite (SPEC_METHOD §11), by P2 work is arranged to serve the destination, by P5 exhaustion of those resources leaves the outcome undecided, and by P6 a claim that one arrangement is better states its grounds, so a strategy is selected within the resource envelope with its material rationale recorded, and no preferred strategy is imposed by this relation or its consumers | [Construction relation](#construction-relation), Strategy | the strategy itself: the realisation and the actor exercising the admitted work authority; for this corpus's Executive, EXECUTIVE_BASELINE | 5, 7, 9 |
| P4a (independent), P1 (independent), P6 (independent); instance premise b | By P4a steps compose only through compatible preconditions, effects, results and authority, by P1 a locally successful step says nothing about the composite's meaning, and by P6 end-to-end success is a claim on evidence, so each composition boundary preserves the applicable outer obligations, and local success establishes the outcome only with coverage, compatibility and outcome evidence, the chain obligations being those of FOUNDATIONS §4 Preservation through construction | [Construction relation](#construction-relation), Composition boundaries | the decomposition, order and concurrency: the strategy's owner | 3, 4, 7 |
| P1 (independent), P2 (independent), P6 (independent), P5 (derived from P0 and P6, with P0's open-world premise); instance premise a | By P1 a discrepancy between an observation and the required conditions has candidate causes of different kinds that are not conflated, of which the relation names four, by P2 the response serves the destination, by P6 each repair goes to the owner of its cause, and by P5 an undecided cause stays undecided, so feedback compares observations with the governing conditions, diagnoses among the four causes, preserves unresolved alternatives and routes each supported response to its owner; a bug is one intake category of change work, which SPEC_METHOD §4 applies at intake | [Construction relation](#construction-relation), Feedback and diagnosis | severity and priority policies: the adopting Product's work carriers ([TICKETS](TICKETS.md)) | 5, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P2 (independent), P6 (independent); instance premises a, b | By P5 a step reports only what its context decides, by P2 continuing work needs a route to the destination, and by P6 completion is a claim on evidence against the destination, so preservation, progress, termination and outcome satisfaction are distinct claims, each with its own support, and an exhausted limit or an unresolved attempt proves neither completion nor impossibility | [Construction relation](#construction-relation), Preservation, progress and completion, and Evaluation and completion; [§3](#3-step-results-and-disposition); [§6](#6-cost-and-proportionality) | the completion condition of ongoing work: the owner of its mandate | 5, 7, 9 |

[SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method),
outside this member, binds the step to that member's terms and applies
these rows, except its delivery priority, which family F5 traces at §6.
Its execution relation applies the second and fourth rows; its binding of
the selected outcome to the product outcome, and of the owning relations
and re-entry conditions to the chain's layers and change classes, applies
the first and sixth rows; and its rule that the configuration sets the
frames for construction, assessment and disposition, the consumer of a
step's return and any coordinator applies the fourth row; and its binding
of the step to the construction relation applies the tenth to fourteenth
rows. Two of its
statements apply other sections: the step's results in the core apply
§3, which family F3 traces, and the computational relations, actors and
resource limits of the tenant's binding apply SPEC_METHOD §11, which
family F10 traces. SPEC_METHOD §8 keeps its owner.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, transitions: [§2](#2-context-construction-under-an-envelope), [§4](#4-totality-and-refinement), [§6 Resource limits](#resource-limits), [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method).
- Row 2, intake, admission and output: [TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and its [family table](TICKETS.md#foundation-to-law-work-carriers); [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability), [Attention cycle](EXECUTIVE_BASELINE.md#attention-cycle), [Drift locks](EXECUTIVE_BASELINE.md#drift-locks) and [Work result](EXECUTIVE_BASELINE.md#work-result); the [REFERENCE_FRAME family table](REFERENCE_FRAME.md#foundation-to-law); [AXIOMATIC_CALCULUS AC-007](AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal); [PRODUCT_DEFINITION Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update); [DESIGN_MODULE UP-018](DESIGN_MODULE.md#invariant-reconstruction-sufficiency-up-018); [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion).
- Row 3, applicability: [DESIGN_MODULE Cross-view axiom evaluation](DESIGN_MODULE.md#cross-view-axiom-evaluation) and its [family table](DESIGN_MODULE.md#foundation-to-law).
- Row 4, configuration and delegation: [EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration), [§17](EXECUTIVE_BASELINE.md#17-actor-binding-and-independence), [The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration) and [No mutation while Executive](EXECUTIVE_BASELINE.md#no-mutation-while-executive); [PROFILES §6](PROFILES.md#6-engagement-baseline); [REFERENCE_FRAME RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy); [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method) and [§11](SPEC_METHOD.md#11-build-tenant-binding); the [EVALUATION family table](EVALUATION.md#foundation-to-law-claims-evidence-assessment-and-acceptance); [TICKETS Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse); [ODD §1](ODD.md#1-position) and [§11.7A](ODD.md#117a-conforming-agentic-development).
- Row 5, recording a result without review: [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability), which applies it and adds two bindings; the carrier is [TICKETS Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse).
- Row 6, completion, destination change and stops: [§6 Resource limits](#resource-limits); [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method).
- Row 7, totality and hard stops: [EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion); [EXECUTIVE_BASELINE Technical triage](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect); [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle); [DESIGN_MODULE Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review); the [WORLD_MODEL family table](WORLD_MODEL.md#foundation-to-law).
- Row 8, refinement: [FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction); [REFERENCE_FRAME Evidence or coordinate translation](REFERENCE_FRAME.md#evidence-or-coordinate-translation); [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding); [WORLD_MODEL §5](WORLD_MODEL.md#5-core-claims); [ODD Graph functions](ODD.md#graph-functions).
- Row 9, complete enclosing-relation admission and standing structural qualification: [DESIGN_MODULE Transformation admission completeness](DESIGN_MODULE.md#transformation-admission-completeness-up-016); [ODD §11.5B](ODD.md#115b-execution-authority-audit); [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), which binds both to ACTIVATION §4.
- Row 10, binding A and Z and the three accounts: [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method); [FOUNDATIONS §3 Construction synthesis](FOUNDATIONS.md#construction-synthesis); [FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction).
- Row 11, strategy: [EXECUTIVE_BASELINE Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery); [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method).
- Row 12, composition boundaries: [FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction); [§4 Refinement](#refinement).
- Row 13, feedback and diagnosis: [SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage); [ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop); [FOUNDATIONS §4 Parallel derivation and mutual assurance](FOUNDATIONS.md#parallel-derivation-and-mutual-assurance) and [Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse); [DESIGN_MODULE §5 Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where repeated material surprises are evidence for diagnosis; [EXECUTIVE_BASELINE §20](EXECUTIVE_BASELINE.md#20-failure-classification), whose first row diagnoses a coherent capability that is not the selected Product; [ASSURANCE §1](ASSURANCE.md#1-verification-layers), where no scenario for a capability can be written.
- Row 14, preservation, progress and completion, and evaluation and completion: [EVALUATION §1](EVALUATION.md#1-claims); [§3](#3-step-results-and-disposition); [§6](#6-cost-and-proportionality); [FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation).

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### Transitions

Construction moves work from a current state towards a destination
(P0, P2). The current state is the material state of the workspace and
its authoritative inputs, together with what is justifiably known about
that state, with the unknowns explicit. The work state of §5 records it:
the workspace, the governing basis, and the closed results and judgments
that still apply, with the residuals and the uncertainty over external
effects as the explicit unknowns. An actor's context is an account of the
current state, not the state itself
([§5](#the-workspace-and-an-actors-account)) (P3, P5).

The destination is defined by constraints: the selected outcome with its
acceptance conditions (Outcome U, [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology))
and the governing obligations the work must keep. It names no single
state: its acceptance conditions admit several realised states. Its
owning authority defines it (P2, P6).

A transition is a bounded change from the current state to a next state,
carried out by one step. Where the work exceeds one activation's capacity,
the outer transformation towards the destination is refined into a series
of bounded transitions under §4 Refinement, each carried out by its own
step; work that fits one activation is a single transition. Each
transition binds the obligations it must preserve: the outer obligations
of the destination and of the governing relations it affects, as far as
they apply to it. A step's intake binds the current state, the
destination and the obligations: the governed outcome names the
destination, or the prerequisite towards it, that the step serves; the
exact subject and basis identify the current state it starts from; and
the affected relation set with its governing invariants holds the
obligations it preserves (Intake below; P0, P4a).
Transitions compose only as §4 Refinement permits.

Discovery. Construction, observation and evaluation change the current
state and what is known about it. A new observation may add obligations,
which join the known work, or invalidate a claim, which is re-established
or withdrawn before anything relies on it (§7). Discovery can enlarge the
known work while knowledge improves (P5, P4b).

Open work outside attention. An obligation outside a frame's current
attention stays open. A bounded view disposes of none of the work it
excludes, and the next decision keeps its material dependencies on that
work (P4b, P6).

Destination change. An authorised change may revise the destination. The
change follows its owning authority and re-enters at the owning relation
(§4). A revised destination does not establish that the previous
destination was reached, and a candidate that satisfies the revised
destination is no evidence that it satisfies the previous one (P2, P6).

Completion. Work is complete only when sufficient evidence shows that the
current state satisfies the applicable destination and its acceptance
conditions; accepting that claim is the decision owner's disposition
(§3 Disposition). An empty list of known work, a count of closed or
remaining items, or the absence of a recorded counterexample does not
establish completion (P6;
[RF-015](REFERENCE_FRAME.md#rf-015-residual-uncertainty)).

Stops. Work that cannot continue ends in an explicit stop that names its
cause: a step that cannot deliver its output stops with a value of
construction availability other than `candidate_ready`, and a declared
ambiguity that halts the work or exceeds the step's authority stops it
with `blocked` or `escalated` (§3). A refused admission or activation
stops the work without creating a step (§3 Admission and activation).
The work state (§5) retains the unresolved outcome, the residuals and the
obligations still owed. A stop reaches no destination and discards none
of these (P4b, P5).

Progress. Progress is judged against the selected outcome and the
evidence for it, as §5 defines progress, not by the number of remaining
items alone: discovery
can raise that number while the work moves towards the destination (P2).

Purpose and material relation: finite context and attention (P0) mean
that an outcome beyond one activation is reached through bounded steps.
Binding the destination and the preserved obligations at each transition
keeps the outer contract through that decomposition. Keeping completion,
destination change and stops apart prevents a count, an exhausted list or
a revised destination from standing in for evidence that the applicable
destination is satisfied (P2, P6). The state, the destination and the
obligations are those that the intake and the work state already bind; no
further carrier is required. 

### Construction relation

This subsection states the construction relation for this corpus: how a
selected construction binds its current state and destination, chooses
its work, composes its steps, corrects itself and claims completion. This
section owns that relation. ACTIVATION §2 to §7, EVALUATION §1,
SPEC_METHOD §4 and §8, EXECUTIVE_BASELINE and ODD apply it through their
local bindings; none creates a competing determination (P6).

Binding A and Z. A construction binds A, the current state of Transitions
above with its account, and Z, the destination as a predicate over
realised states that includes the acceptance conditions of the selected
outcome. The account of A describes the material workspace state, the
relevant external observations acquired through the interfaces that own
them, what is justifiably known and the explicit unknowns; an actor's
acquired account can be incomplete or stale, and the workspace, not the
account, is the subject (§5). Several realised states may satisfy Z. The
governing specification, the selected WHAT across the Intent, Product and
Specification of the Product that owns the work, supplies Z; its
descriptions refine Z. The applicable declared requirements and the declared calculi of the
tenant's binding ([SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding))
govern which transformations and compositions are lawful; the calculi
select no outcome. A
lawful construction can remain incomplete or fail to reach Z, and
lawfulness establishes neither delivery nor optimality. A proof about the
outcome that rests on premises retains those premises and its scope. A
selected construction may need to discover its path while performing and
evaluating work (P2, P3, P6).

Three accounts of the subject, distinct from the accounts of a
construction ([FOUNDATIONS §2](FOUNDATIONS.md#accounts-of-a-construction)).
The specification is the internal reference model of the required
conditions. Observations describe what does hold. A causal or
predictive model explains how an action may change the state. These
accounts have different purposes and can be incomplete or wrong in
different ways; a claim about one is never taken for a claim about
another, and the applicability and adequacy of a predictive model are
claims of their own (P1).

Strategy. A strategy arranges admissible construction and assurance to
serve Z within the selected resource envelope. Its material choices
account for context, attention, time, effort, computation, communication
and the other relevant resources, together with feedback delay,
uncertainty, integration exposure and rework; planning, checking and
coordination consume resources too. Measures that justify a choice state
their units, boundaries and composition rules, and keep estimates,
assumptions and observations distinguishable. Several objectives can
leave alternatives incomparable; the owning criteria decide the tradeoff.
Steel thread, phased (waterfall) delivery and iterative delivery are
possible strategies, each with its own costs, feedback delays, integration risks and rework.
The selection belongs to the realisation and to the actor exercising the
admitted work authority; its material rationale is stated in existing
design or work records, and a claim that one strategy is superior states
the objectives, comparison and assumptions it depends on. No exhaustive
optimisation, universal numerical budget, scalar cost measure or preferred
strategy is imposed by this relation or its consumers (P2, P5, P6).
Context bounds what one activation can hold and attention what it can
use; the frame selects the material and the task contract of one step,
and the destination stays Z across the activations that reach it
([§2](#2-context-construction-under-an-envelope)).

Composition boundaries. A composition boundary is the boundary between
successive steps, where one step's output becomes the next step's
starting state. It is distinct from a categorical join, which is a map
between categories ([FOUNDATIONS §4](FOUNDATIONS.md#4-algebra)). Steps
compose through compatible preconditions, effects, results and authority,
and each boundary preserves the applicable outer obligations. Refinement
can add detail and construction can change state within the permitted
variation (§4). Decomposition, delegation, concurrent work and recursive
application retain the affected obligations; independent actions may
proceed concurrently where their dependencies, effects and authority
permit. Local success supplies end-to-end success only when the required
coverage, composition compatibility and outcome evidence hold; the
obligations a chain of steps must discharge are
[FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction).
A categorical claim about a construction meets the demonstration of
FOUNDATIONS §4 (P4a, P1, P6).

Feedback and diagnosis. Feedback observes the current subject, compares
it with the governing conditions, diagnoses a material discrepancy,
selects an authorised response, acts and observes the result. Homeostasis
means correction towards the required conditions as disturbances and new
observations arise; it guarantees neither convergence nor the adequacy of
those conditions. For work management a bug is a category of
feature/change work: an observed or suspected discrepancy handled through
the same intake and delivery mechanism
([SPEC_METHOD §4 Universal intake triage](SPEC_METHOD.md#universal-intake-triage)).
Diagnosis distinguishes four causes: a defective realisation, an
inadequate governing requirement or design, an inaccurate predictive
model, and insufficient observation. A prediction error alone does not
decide whether the required outcome holds. A revised model does not erase
the counterexample or by itself repair the realisation. Diagnosis preserves unresolved
alternatives and routes each supported repair to the owner of its cause;
the intake label supplies no repair class and no permission. Severity
describes consequence; priority orders the response under the selected
outcome, dependencies, resources and authority. A bug list projects
existing work state and creates no separate delivery or authority
mechanism (P1, P2, P5, P6).

Preservation, progress and completion. Recursive and repeated work
distinguish four claims: preservation, that an invariant or obligation is
kept through the steps; progress, that the work moves towards Z on
evidence; termination; and outcome satisfaction. A formal induction or
termination claim supplies its premises and argument; no universal
termination proof is required before bounded work can begin, and where
such a proof is absent the claim stays within the available evidence.
Continuing work has a supported purpose under the selected strategy,
which can include reducing uncertainty or testing a bounded hypothesis.
Discovery may enlarge the known work (Transitions above), and repeated
activity alone establishes no progress. Control handles failure,
unavailable information, uncertain effects and exhausted resources
through the continuation, repair, recovery, re-entry, yield or stop that
§3, §5 and §6 name. Resumption reacquires current reality and retains
valid progress; unknown effects are resolved sufficiently before the next
dependent action (§5). Ongoing maintenance can continue under its mandate; a
delivery claim needs its completion condition. A resource limit can end
an attempt with an unresolved outcome; it establishes neither achievement
nor impossibility (P5, P2, P6).

Evaluation and completion. Evaluation uses the core result algebra
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)), preserving failure,
missing coverage and uncertainty. Formal proof, mechanical checking,
testing and observed use establish their respective claims on their
stated subjects, assumptions and boundaries
([FOUNDATIONS §4 Assertions and observation](FOUNDATIONS.md#assertions-and-observation));
an unavailable proof remains
an explicit obligation where the governing conditions require that proof.
Producing a candidate, proving a property and accepting delivery remain
distinct acts ([EVALUATION §5](EVALUATION.md#5-acceptance)). Completion
requires sufficient evidence against Z, including its acceptance
conditions; exhaustion or an unresolved attempt proves neither completion
nor impossibility (P5, P6). A change to Z follows its owning authority and
the re-entry rules of Transitions (Destination change); it establishes
nothing about whether the former Z was reached, and the original
counterexample stands.

Ownership and limits. This subsection is the one owner of the
construction relation in this corpus. Its consumers apply it where an
actor enters construction, triage, recovery, assurance and release, and
state no second relation. Domain strategy, actor configuration, execution
mechanisms and additional assurance policies retain their owners:
EXECUTIVE_BASELINE for this corpus's Executive, PROFILES for the
profiles, SPEC_METHOD §11 for the tenant's binding. The existing work and
evidence carriers hold the necessary state ([TICKETS](TICKETS.md); the
closed results of §7); the relation adds no independent ledger, required
role sequence or orchestration runtime. It establishes no general solver,
no fixed organisational structure, no guaranteed convergence and no
theorem of categorical universality (P6, P2). Purpose and material
relation: bounded activity can consume resources without delivering the
intended outcome, and isolated checks can conceal a failed composition;
the relation connects purpose, action, observation and correction so that
features and defects alike remain governed by their end-to-end
obligations (P2, P5, P6).

### Intake

A step is activated from an intake sufficient to reconstruct its governing
relations without conversation history, commentary or a prior actor's memory
(P0, actor-change premise). The intake names:

- the governed outcome or decision: the selected outcome, admitted
  prerequisite or experiment it serves (P2);
- the exact workspace subject and basis, and the inputs it may acquire,
  each by identity and hash or by an input commit;
- the evaluation or evaluation family the step performs and its result
  algebra: the core of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results) or
  a refinement mapped into it (§3);
- the bounded affected relation set and the applicable governing
  invariants;
- the accepted transformation-admission relations the step relies on (§4);
- the selected computational or common-library dispositions: which
  shared machinery serves the step and under what binding (FOUNDATIONS §4,
  shared machinery);
- the construction and assessment authority: the applicable frame-set,
  semantic, evaluation, operation where material, and decision authority
  (FOUNDATIONS §2, authority kinds), and the grant: the operations
  permitted, the territory that may change, and the decisions reserved to
  others (P6);
- the available actor capability envelopes;
- the conditions that make the result stale or out of scope, and the
  conditions that require re-entry at an owning relation;
- where the governed question is a cost claim, the allowance and how
  spend will be measured (§6).

Implementation folklore is not an intake source. Where a design profile
applies, its bounded-frame conservation, transformation-admission
completeness, invariant-reconstruction sufficiency and
computational-realisation projection laws supply the affected set, the
admission relations, the invariants and the computational dispositions;
this section consumes those laws and creates no second design package
([DESIGN_MODULE](DESIGN_MODULE.md)).

### Execution unit

The execution unit is the smallest coherent causal dependency cone capable
of delivering working behaviour while preserving every affected governing
relation. It need not coincide with one function, file, module, ticket
field or design document (P0, P4b). A seam whose far side can causally affect,
or be affected by, the action is inside the cone unless the basis
establishes that it cannot participate. Unrelated incompleteness outside
the cone is recorded as repricing input and does not block the bounded
claim. The cone is the seed set Z of §2; the context is its projection.

### Admission

Drafting a step's contract and admitting it are distinct relations, even
inside one invocation that drafts, validates, admits and executes; no
separate turn, carrier or approval ceremony is implied by the distinction.
A contract carries at minimum the states drafted, admitted, rejected and
superseded ([TICKETS §5](TICKETS.md#execution-contract-admission)).
Execution begins only after deterministic admission or an
explicit human override of the exact contract. The drafting actor never
infers admission from its own draft, from the presence of a carrier
(ticket, sprint entry, work contract), from lane placement or from an
`active` label. The admitted result identifies the admission mechanism and
its authority, the exact contract identity or digest, the decision and the
evidence, including any human override; absent those coordinates the
contract stays drafted or rejected, and prose asserting admission is not
admission evidence (P6; the actor cannot self-certify its own execution
basis). Admission validates the contract against its cited outcome,
prerequisite or experiment basis; it does not admit that basis, and
drafting, admitting or retaining a contract creates or renews no authority
its owner has not admitted (P6, P2;
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). Only an admitted contract activates a step: no
result, child completion, tool output, model response, shared actor or
lateral handoff activates another step or authorises continuation by
itself, and a profile that routes results names its instances of this
rule. Purpose and material relation: these admission conditions govern every
configuration, and their generic owner is this section (P6).
The admitted contract names one
durable result and evidence surface; every result, withheld closure and
residual obligation is recorded there before return, a conversation return
alone is not durable evidence, and if no such surface is authorised and
available, admission refuses (P4b). Absent or rejected admission returns
the missing work authority without execution, as `admission_refused` with
its cause ([§3 Admission and activation](#admission-and-activation)).
The selection of the carrier (ticket, sprint entry, run-scoped contract)
is owned by [TICKETS §5](TICKETS.md#5-from-carrier-to-execution).

### Applicability

The owning evaluation and scope declarations determine which frame
obligations apply to the exact subject. Their declared predicates are
evaluated from sufficient basis-bound facts: a true predicate requires the
applicable evaluation and its result; a false predicate excludes only that
obligation, under its cited authority; a missing or ambiguous premise
leaves applicability unresolved, not false. A supported inapplicability
of a conditional obligation is recorded as such, apart from any result
value, and waives no criterion of the member's acceptance (P5, P6). A frame name, an available
tool or a listed family triggers no activation by itself. Where
applicability needs residual semantic judgment, that judgment and its
evidence are retained as a judgment, never represented as a computed fact
(P6, P1). A required result that is absent, stale, bound to another subject
or basis, or incapable of establishing its claim cannot satisfy a dependent
conjunction ([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results));
unresolved applicability withholds the dependent claim until
sufficient evidence or the owning decision resolves it; other applicable
constraints stay in force even if only one evaluation detects them (P4b,
P5). Qualification of an applicability rule distinguishes true, false and
unknown premises, required results that are missing or bound to the wrong
subject, and a sufficient positive result, under a finite declared fixture;
a rule that always skips or always activates cannot satisfy those distinct
expected outcomes (EVALUATION §7).

Exclusion and the core. Deciding applicability is an evaluation of the
predicate "the obligation applies to the exact subject", and its result is
a core value of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results): a true
predicate is `satisfied`; a false predicate is `falsified`, the
basis-bound fact that makes it false being the counterexample; a missing
or ambiguous premise is `indeterminate`, or `out_of_frame` where the
premise needs a relation the frame does not declare, and never
`falsified`. An exclusion is the state of the excluded obligation after a
`falsified` applicability result: it is no result, the obligation's own
evaluation is not performed and maps to no core value, and the obligation
leaves the required coverage of a dependent conjunction under the cited
authority of that applicability result. An obligation whose applicability is
unresolved stays in that required coverage. A predicate that its owner
declares as a disjunction that includes non-application, such as "meets
the axiom or does not apply", may be `satisfied` because the obligation
does not apply; that `satisfied` is for the declared disjunction only and
never counts toward the predicate that the obligation holds
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results),
Predicates travel). Members, profiles and projects refer to this
paragraph for exclusions and do not decide them again (P5, P6, P1).
Purpose and material relation: an exclusion read as a result of the
excluded obligation, or a "does not apply" counted toward that obligation,
would report a skipped obligation as met; an unresolved premise read as an
exclusion would drop an obligation that may apply.

### Output

The step's output is a candidate plus its step-produced facts: judgments with
their evidence, residuals, observations, authority decisions, provenance, and
one stop state, a value of construction availability (§3). The actor's
internal path is not part of the output
and is not governed (FOUNDATIONS §2, work boundary).

### Configuration

A configuration allocates a task's responsibilities and information
exchanges to frames; activation binds an actor to each frame (§2). It
spans the task's work. The active frame configuration of
[FOUNDATIONS §2](FOUNDATIONS.md#frame-objects) is the part of it used for
one evaluation or decision (P0, P6).

Allocation. The allocation is derived from the task's operations, the
dependencies among them, the capabilities of the available actors and the
required assurance. These conditions constrain a configuration without
determining it. One frame or several, fixed or adaptive allocation, a
hierarchy, peer coordination, or an arrangement that changes as actors
allocate work within their contracts may each be adequate. The method
prescribes no role inventory, hierarchy, coordinator or actor sequence
(P0, P2; [RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality)).

Explanation. The design that selects a configuration explains its
allocation, including the material resource limits it assumes, such as
context, attention, time and spend, each declared as §6 Resource limits
states, and its assumptions about failure. The
explanation is recorded in the existing design, frame declarations and
work records; no separate configuration carrier is required. It is
proportional (§6): for a direct entry, the intake states it, its
capability envelopes carrying the resource limits and its stale,
out-of-scope and re-entry conditions the failure assumptions (P2, P6).

Direct entry. A one-frame configuration is lawful. One directly
authorised task that fits a sufficient frame may be entered directly, as
Roles and delegation below states, subject to any separately required
assessment (P0, P2).

Evaluation of a configuration. A configuration is evaluated against the
task, its dependencies, the actors' limits, the authority it applies and
the required assurance. Its labels, its topology, and the presence or
absence of a coordinator or of familiar roles neither accept nor reject
it (P1, P6).

Distinct relations. Within a configuration, the relation structures that
[RF-009](REFERENCE_FRAME.md#rf-009-no-assumed-hierarchy) lists as
distinct stay distinct; RF-009 owns that list and the rule, and this
section adds no structure to it and drops none. Naming or selecting a
frame grants no authority
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority): each activation binds its subject, result algebra,
actor capability and admitted authority through its intake (Intake above)
and its activation (§2).

Admission of a configuration. A configuration is admitted by the smallest
existing authority that owns the material decision the configuration
makes. One configuration may derive from several governing owners; each
keeps its own decision, and admitting the configuration creates no new
authority over them. An explicitly bounded proxy admits a configuration
only inside its existing grant (FOUNDATIONS §2 Authority kinds, Proxy
limit). Which authority owns which decision is a binding of the method or
profile that applies this rule; the executive configuration's binding is
[EXECUTIVE_BASELINE §16](EXECUTIVE_BASELINE.md#existing-authority-selects-the-configuration),
which refers here for the rule (P6, P2).
Purpose and material relation: a configuration allocates authority-bearing
responsibilities, so admitting one by an authority that does not own the
decision would move authority with position in the decomposition; the
rule holds for every configuration, so it is stated here and not only in
an optional profile.

Reconfiguration. The allocation, and every reconfiguration, preserves the
material dependencies, the outstanding obligations, the effects,
including those of uncertain completion, the admitted authority and the
required independence. A reconfiguration is any change of allocation
during the work, including actors redistributing work among themselves
and the changes §4 Reconfiguration selects after a result. An outstanding
obligation and the results that depend on it move with the work. An
effect of uncertain completion is resolved sufficiently for the next
dependent action before that action (§3 Effects, §5). Required
independence keeps its authorship and evidence conditions
([EVALUATION §3](EVALUATION.md#3-independent-assessment)), which a fresh
context alone does not meet. An adaptive or self-organised arrangement is
exempt from none of these conditions (P4b, P5, P6).

Coordination across tasks. Where a configuration separates carrying out a
bounded change from managing delivery across successive tasks, the frame
that manages delivery, a coordinator, keeps the longer-term outcome. It
decides from a sufficient bounded view of the closed results of the task
frames (§7), not from their working context. When a decision needs
information that view lacks, the coordinator acquires it through its
permitted frame inputs or requests a further bounded evaluation. Missing
information is never assumed favourable. A task result never omits a
blocker material to delivery: a compact result keeps every residual and
stop material to delivery, and its size is no evidence that none exists
(P0, P4b, P6).

Optimality. Adequacy and optimality are separate claims. A claim that a
configuration is optimal is relative to stated objectives, constraints and
comparison scope, and rests on evidence for that comparison. Familiarity,
persistence or self-organisation is no such evidence. Different
objectives or actor models can favour different configurations (P2, P6).

Example. The executive configuration, which the
[executive baseline profile](EXECUTIVE_BASELINE.md) defines, is one
configuration, for task-based work in which a bounded change and delivery
across tasks need separate attention. It allocates construction,
assessment and disposition (Roles and delegation below) to three frames: a
Worker frame, specialised as Writer for documents and records, constructs;
a Reviewer frame assesses; an Executive frame keeps the longer-term
outcome, selects the next work and disposes within its decision grant, and
mutates nothing. That profile owns its frames, their grants, limits and
prohibitions, and its explanation; they apply where it is selected. It is
not the method's default. A configuration with other frames, names or
topology is evaluated as Evaluation of a configuration above states.

Purpose and material relation: finite context and attention bound each
responsibility (P0); dependencies between tasks require exchanges and
compatible results (P4a); and fallible actors with incomplete knowledge
require checking and recovery (P5, P6). These conditions constrain a
configuration without determining it, so the method states what every
allocation preserves and leaves the arrangement to the design. A
coordinator that decides from a bounded view relies on what the view
holds, so a blocker missing from a task result would be read as absent
(P4b). The material relation is whether an allocation or a reallocation
can drop an obligation, an effect or a required independence, move
authority with position in a decomposition, or hide a blocker from the
decision that needs it. 

### Roles and delegation

Roles are relations over steps that a configuration allocates
(Configuration above), not kinds of actor and not a fixed inventory.
Where a configuration's operations include construction, assessment or
disposition, this member names the responsibility for each: a
constructor owns the bounded implementation and its self-review; an
assessor evaluates a frozen candidate independently; a decision owner
disposes. A configuration may allocate other responsibilities. Where
independent assessment supports promotion, the assessor evaluates the
exact live subject, its authority paths, proof and installed state, not
the constructor's summary (EVALUATION §3). This preserves the
independent-review relation and prescribes no actor count: one actor may
occupy different roles across different claims when independence for the
assessed claim is preserved; no role name confers an operation
([RF-016](REFERENCE_FRAME.md#rf-016-implementation-neutrality);
P6).

The governing authority relation declares whether a bounded proxy may
accept and advance routine actions. Inside a step, a proxy so declared may
accept preservation, require local repair, reject a violating candidate
and advance to the next already-authorised action; what it cannot change,
and the re-entry such a change requires, is the proxy limit of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), which
this paragraph applies and does not restate. Human ceremony is not
required at every transition when the governing basis, the affected cone,
the decision envelope and the re-entry conditions are already accepted;
this delegation does not weaken direct human acceptance where the
governing product or release law requires it (P6).

When one capable context has sufficient existing work authority, exact
intake and operation grant, it may enter directly as constructor. No
coordinating activation is required solely to appoint that constructor.
The applicable configuration (Configuration above) selects
coordination when material contexts, authority, capability or required
independence need it; a role or frame name alone does not create that
need. Direct entry preserves
execution-contract admission (Admission above), the smallest lawful
carrier, the required assessment and the reserved decisions; it permits
bounded work and condition-based result recording, not self-acceptance at a
boundary owned elsewhere (P0, P6).

Recording a result without review. Where the applicable law requires no
independent assessment and reserves no acceptance, the constructor that
holds the grant may record the satisfied bounded result, with the conditions
it found satisfied and their evidence, in the existing durable result
surface (Admission above), without adding a carrier, coordinating
appointment, review or recreated design view solely to mark completion. The
recording waives no condition that actually applies, states only
conditions that were evaluated, as an actor cannot report an evaluation it
did not perform
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed), and is
no disposition at a boundary owned elsewhere
(§3 Disposition). Where an assessment or a reserved acceptance does apply,
it stays required, and an insufficiency found during the work withholds
the dependent effect and returns the question to its owner. Carriers and
profiles refer to this paragraph and add only their own carrier binding
(P0, P2, P6). Purpose and material relation:
requiring a review or a ceremony that no law requires adds reasoning cost
without removing ambiguity (§6), while recording a satisfied result where
a review or acceptance is required would read construction as acceptance.

One bounded operation grant may cover its declared construction, status and
checkpoint sequence. Actual role transitions are recorded in the existing
work carrier; a status change alone requires neither a new grant nor
rehashing an unchanged subject. A material change to the operation, the
subject, the territory, the authority or the validity conditions requires
the affected binding to be resolved before effect. Where the selected
configuration restricts its coordinating role from mutation, as the
executive configuration (Configuration above) restricts its Executive,
the restriction that the coordinating role mutates nothing remains
applicable; an operation grant covering the sequence does not lift it
(P6, P3).

## 2. Context construction under an envelope

Qualified-reference guidance. Under
[AC-003](AXIOMATIC_CALCULUS.md#ac-003-reference-closure) and
[AC-011](AXIOMATIC_CALCULUS.md#ac-011-projection), a reference can supply
sufficient context when its accessible target and qualifications preserve
the consuming contract. Check the required subject and basis, assessment
standing, provenance, active obligation and version, and invalidators, rather
than candidate identity alone. A typed annotation supplies no evidence of
sufficiency by itself. Preserve the required body or a qualified resolvable
reference; no mandatory carrier or registry follows (P1, P3, P6).

An exact local reference to a complete assessed record can preserve the
consumer-required distinctions. A candidate-only pointer can lose them when
unchanged candidate bytes have satisfied and indeterminate assessments that
require different continuations. A sufficiency claim relying on hash matching
states its collision and access assumptions. Unknown semantic relations retain their owning gap or
result; they do not all become one error class. A declared but unperformed
evaluation has no assessment result; an undeclared required capability is
a different condition. The [qualified-reference example](examples/DETERMINISTIC_CONTRACTS.md#qualified-references)
applies the sufficiency law owned by
[FOUNDATIONS §4](FOUNDATIONS.md#assertions-and-observation).

Given a seed set Z (the subject, outcome and affected relations named in the
intake), a relation family R (the dependency relations whose change can
alter the result, basis validity, evidence sufficiency or authority), and
the actor's envelope B:

1. Compute the material closure of Z under R (AC-010,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure)).
   If Z, R, the required-edge semantics, the basis or the scope is not
   exact, or the closure is not finite and unique on the exact basis,
   activation returns `closure_unresolved` (§3, Admission and activation)
   and no step proceeds; it does not guess.
2. Project the closure to the selected context, recording its boundary: the
   excluded, external, unresolved, translated and invalidation-sensitive
   seams (AC-011,
   [AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-011-projection)).
   If the projection returns a gap or refusal, activation returns
   `closure_unresolved` and no step proceeds.
   Material not in the closure stays out; adjacent material does not enter
   because it exists
   ([RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)).
3. Test fit against B. This step owns the size measurement and the fit
   test for the context dimension. Where B declares a context capacity,
   the size of the selected context is measured before the actor reads it,
   in the unit the capacity is declared in (bytes or tokens) and over the
   boundary that the selected execution binding states for it (§6), and is
   compared with that capacity. The measurement, the capacity and the
   outcome of the comparison are recorded before the read. A fit holds
   only for the measured boundary: context outside it is recorded as not
   measured, and no fit claim covers it. The fit claim for a measured
   boundary and the step's fit judgment are distinct: the judgment is
   established from the recorded complete active inputs, or from a
   supported upper bound that includes any host-supplied context; where
   neither exists it is `indeterminate`, unless a counterexample, such as
   a measured excess, establishes `falsified`. A correct task result keeps
   its own bounded standing and does not satisfy a missing fit judgment
   (P0, P5). The measurement applies wherever B declares a
   context capacity, whatever question the step governs, because without
   it a fit claim against that capacity is an assertion, and a context
   that exceeds it would be cut without record
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)). It applies only
   there, because a resource control applies only through a selected frame
   and its owning scope
   ([REFERENCE_FRAME §4](REFERENCE_FRAME.md#frame-set-selection)), and a
   declared capacity is such a control: the measurement tests that
   capacity, is no budget, and is not a universal measurement gate (P0,
   P2). Where B declares no context capacity, no measurement is
   required, and the other conditions of
   [RF-002](REFERENCE_FRAME.md#rf-002-finite-attention) still apply. The size
   shows fit and nothing else: whether the actor attends adequately to a
   context that fits is decided by actual-use evidence under
   [EVALUATION §7](EVALUATION.md#frame-qualification). The envelope's
   other dimensions are fitted as RF-014 states; time, spend and other
   resource limits follow [§6 Resource limits](#resource-limits), which
   this step refines for the context dimension.
   If the context fits, activate. If it does not, one or more of these, in
   combination: refine the outer contract into steps whose contexts fit
   (§4); sequence activations; apply a lawful compression that preserves the material
   distinctions and failure detections the evaluation needs
   ([RF-017](REFERENCE_FRAME.md#rf-017-proportional-compression));
   select another actor whose envelope fits; or return `out_of_frame`
   ([§3 Admission and activation](#admission-and-activation)). Silent
   omission to fit is never one of them
   ([RF-014](REFERENCE_FRAME.md#rf-014-capability-fit)).
   None of these options silently reduces the required predicate: the
   obligations the step preserves stay bound
   ([§1 Transitions](#transitions)), a narrowing of them is a destination
   change under its owning authority (§1, Destination change), and what
   the selected context leaves undecided stays an explicit unknown.
   Within its grant a step selects refinement, sequencing and compression
   itself; selecting another actor or enlarging the envelope re-enters the
   owner of the grant or envelope, who may delegate that choice in the grant
   (RF-014 vests the selection in human authority; a grant is that authority
   exercised in advance). Whether a compression preserved what the
   evaluation needs is a claim with the standing of any other (EVALUATION
   §1): the compressing step records the compression and its preservation
   argument, and the claim is assessed independently only where the
   promotion it serves needs independent assessment (EVALUATION §3).
4. Acquire declared inputs by their exact identity. A declared input absent
   from the actor's materialised view is neither licence to read elsewhere
   nor evidence that it is absent.

Acquisition. Acquisition is the read-only observation of the material a
step needs (its frame, its subject and its declared inputs) within the
inputs its intake permits it to acquire (§1 Intake). It is not an admission and not a further
actor stage; effectful work still needs its admitted contract (§1
Admission), and acquiring material grants no role, operation or decision
([FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority). A derived surface is material derived from owning
sources by copying, projection or compression, such as a projected frame
for a task; it names its sources and owns no determination. Where a
current interpretation of the subject in `a_c` exists, the constraint
surface it yields for the task is such a derived surface, under the
conditions of
[AXIOMATIC_CALCULUS §9 Constraint surfaces](AXIOMATIC_CALCULUS.md#constraint-surfaces).
Where a derived surface whose sources
are current serves the task, the actor acquires it. For another task, or
where the derived surface is stale ([Staleness of derived surfaces](#staleness-of-derived-surfaces)),
missing or insufficient for a named unresolved question, the actor acquires the deciding owner sections
directly: the owning sections that decide the task's questions, which are
declared inputs of the selected basis. Only material in the exact selected
basis is acquired: where that basis has no derived surface for the task,
its exact owner sections are used, and a candidate source, a version-line
selector or another basis is no substitute for it
([FOUNDATIONS §2 Product lineage objects](FOUNDATIONS.md#product-lineage-objects)).
The actor reads the selected material and the actual subject, and follows
the material source and coupled-obligation references the task needs
(step 2; [RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency));
presence of the corpus is no reason to read it (step 2;
[RF-004](REFERENCE_FRAME.md#rf-004-irrelevance-exclusion)). No frame,
derived surface or acquisition carries a universal sufficiency claim:
sufficiency is decided for the named question against the task's
material relations, never for the corpus or the frame as a whole
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)). Before any dependent action, a missing binding is returned with
its outcome of [§3 Admission and activation](#admission-and-activation),
naming what is missing: where no available frame declares what the
evaluation needs, `out_of_frame`; where the basis the step requires is
absent, or cannot be verified as the exact basis named, the basis cannot
support the step, and the outcome is `admission_refused(basis)` at
admission or `activation_refusal(basis)` at activation. Coupled material that does not fit is handled under
step 3 (P0, P6, P3).

Activation. The actor or the assigning authority selects one frame or one
declared active frame configuration capable of the evaluation. Activation
binds each reusable frame declaration to the exact subject and basis and
loads the declared material relations and evidence sources, never an
undifferentiated workspace dump; what the actor receives is the packet of
REFERENCE_FRAME §11. When no available frame and actor pairing can lawfully
perform the evaluation, activation returns `out_of_frame` where no such
pairing declares a material relation or capability the evaluation needs,
and otherwise the `activation_refusal` whose cause holds
([REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions)); both are
outcomes of §3 Admission and activation. Work does not proceed through
implied context (P0, P5).

Evaluation. The evaluator applies the activated frame's declared
invariants, evidence rules and result algebra. It distinguishes semantic
law, observed evidence, inference and decision, and records every
assumption whose failure could change the result (P6).

Standalone scope. A derived surface or projected frame decides standalone
only the questions that its own source members own. It refuses to close a
question owned by another member, or one that joins the law of several
owners; the evaluation of that question returns `out_of_frame`
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)) naming the owning
members, and
the question is decided from those members at their current digests or
from a derived surface whose declared sources include every owner of it
(P6, P1).

Prompt construction. A prompt is rendered contract over typed authority;
it is not source law. Prompt text must project the current authority
references, obligations, contracts, boundaries, proof expectations and
fallback conditions the step needs. A prompt body must not carry
historical workaround prose unless the current requirement, design,
runtime or test still needs that constraint. Construction starts from the
highest live authority surface the question needs. If the prompt needs an
upstream ambiguity resolved, it names the unresolved authority gap before
fallback context is read. The prompt projects the material that
Acquisition above selects, including the raw owning members where
Acquisition falls back to them (P6, P0, P5). The design, ODD, UX and ticket
specialisations are
[DESIGN_MODULE §11](DESIGN_MODULE.md#11-review),
[ODD §11.5D](ODD.md#115d-constructive-evaluation-and-yield-loop) A5 and
[§11.7A](ODD.md#117a-conforming-agentic-development),
[UX §7](UX.md#7-carrier-binding) and
[TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and
[§7](TICKETS.md#7-authority-judgment-closure-and-state) (P6).

The operation that joins AC-010, AC-011 and RF-002, RF-003, RF-004,
RF-014 and RF-017 into one procedure is stated here (P0); each of
those laws is applied here from its owning section in
[AXIOMATIC_CALCULUS §4](AXIOMATIC_CALCULUS.md#ac-010-material-closure) and
[REFERENCE_FRAME §3](REFERENCE_FRAME.md#3-laws). The method does not require proving
that no undiscovered material relation exists
([RF-003](REFERENCE_FRAME.md#rf-003-material-sufficiency)).
The size measurement of step 3 applies under its stated condition.
Purpose and material relation of that measurement and Acquisition:
finite context makes fit necessary (P0), so a fit against a declared
capacity is measured rather than asserted, while fit and attention stay
separate claims (P6); and an actor without a derived surface for its task
still reaches the sections that decide it, from the exact basis, without
reading the corpus or substituting a stale or mutable copy (P3, P6). The
material relation is whether a context larger than the declared capacity
is read as if it fit, a fit is taken as adequate attention, or a decision
rests on material other than its deciding owners at the selected basis.

### Staleness of derived surfaces

This subsection owns when a derived surface (Acquisition above) is current
and when it is stale, for any method and any carrier (P3, P5, P6):

- A derived surface names the exact identity, such as the path and
  digest, of each source it was derived from and of each source whose
  change can change its content.
- It is current for a selected basis only while every source identity it
  names equals the identity of that source in the selected basis. A change
  to any of them makes it stale.
- A stale derived surface is not used as current for any question. It
  becomes current again only by regeneration from the sources at the
  selected basis, or by an explicit re-acceptance that records the new
  source identities and the finding that its content still matches them;
  until then the actor acquires the deciding owner sections directly
  (Acquisition above).
- Matching source identities establish only that the surface was derived
  from those sources. They establish neither its fidelity to them nor its
  sufficiency for a question; a surface found insufficient for a named
  question is handled as Acquisition above states.
- The owning sections at the selected basis remain the deciding source.
  Whether a current surface is insufficient for a question, or decides
  beyond its own sources, is judged against them (Standalone scope above);
  a derived surface never decides that about itself.

A packaging or installation carrier refines this rule with its own
identities and re-acceptance procedure, and names this subsection as its
owner; [PRODUCT_DEFINITION §11](PRODUCT_DEFINITION.md#11-one-constitutional-surface-and-version-boundary)
does so for the method's released carriers. Purpose and material relation: an actor that relies on a
derived surface after one of its sources has changed decides from material
that no longer matches its owners, and a matching digest read as fidelity
would let a faithful-looking but wrong surface decide; the material
relation is whether a decision rests on a surface whose sources are not
those of the selected basis. This rule applies to derived surfaces under every selected carrier.

## 3. Step results and disposition

A step returns its results in the core algebra of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results): each evaluation it
performed returns one core value with its predicate and domain outcome,
and an evaluation it did not perform has no result. The outcomes of
admitting and activating a step, and the step's own outcomes, answer other
questions than its evaluations do. This section owns them as five
refinements of the core. Each names the question it answers and the
predicate its mapping is for, and maps each of its values to exactly one
core value; the predicate travels with the value, so no refinement's
`satisfied` counts toward another predicate
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)).
Purpose and material relation: admission, work, decisions and effects
stand in the one core (P5, P6), so a consumer that combines them cannot
read a refused activation as a step's stop, availability as fitness or
acceptance, a carried ambiguity as resolved, or an unknown effect as none.

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| admission and activation | may the step begin | the step is lawfully admitted and activated on the exact subject and basis |
| construction availability | did the step yield its output | a candidate is available |
| disposition | what the decision owner does with an assessed candidate | the candidate is accepted at its declared boundary |
| ambiguity outcome | what happened to a declared ambiguity | the declared ambiguity is resolved on the exact basis |
| effects | did an intended external effect occur | the intended effect occurred |

A profile that refines these values for its own units maps each of its
values to exactly one core value under FOUNDATIONS §4 Results and adds no
core value.

### Admission and activation

A step exists only after its contract is admitted (§1, Admission) and its
frame is activated on the exact subject and basis (§2). The outcomes of
admission and of context construction are owned here; each maps for the
predicate "the step is lawfully admitted and activated on the exact
subject and basis", and its cause selects its value (P5, P6; RF-005 for
the basis causes). The outcomes of frame activation are the `activate`
refinement of [REFERENCE_FRAME §5](REFERENCE_FRAME.md#5-method-functions),
which owns their causes, their predicate and their core values. Because
this predicate requires activation, a refused activation decides it with
the value REFERENCE_FRAME §5 gives; the table names those outcomes and
maps none of them again:

| Outcome | Cause | Core value |
|---|---|---|
| `activated` | the contract is admitted with its admission evidence (§1), Z, R, the required-edge semantics, the basis and the scope are exact and the material closure is finite and unique (§2, step 1), its projection returns a selected context (§2, step 2), and activation returns `activated_frame` | satisfied |
| `admission_refused(authority)` | the work authority the step needs is not admitted: no admission mechanism or explicit human override admits the exact contract, or no durable result and evidence surface is authorised and available; the outcome names the missing authority or surface and its owner | out_of_frame |
| `admission_refused(basis)` | the contract's cited outcome, prerequisite or experiment basis, or the exact subject and basis it names, cannot support it; the outcome names that basis | invalid_basis |
| `closure_unresolved` | the seed set Z, the relation family R, the required-edge semantics, the basis or the scope is not exact, or the material closure is not finite and unique on the exact basis (§2, step 1; AC-010), or the projection of the closure returns a gap or refusal (§2, step 2; AC-011); the outcome names the condition that fails and the basis coordinates that leave it open | invalid_basis |
| `out_of_frame` | no available frame and actor pairing declares a material relation or capability the evaluation needs (§2, Activation), or no fit option of §2 step 3 fits the selected context to an actor's envelope | out_of_frame |
| `activation_refusal` with its cause | a cause REFERENCE_FRAME §5 states | the core value REFERENCE_FRAME §5 maps that cause to |

These outcomes are not values of construction availability and are not
results of a step. A refused admission or activation creates no step, no
activation of the step's frame and no work result, the closed output of a
constructing actor to its consumer; the outcome returns to the assigning
authority or the declared result carrier, and no consumer records it as a
step's stop state. [EXECUTIVE_BASELINE §5](EXECUTIVE_BASELINE.md#work-result)
applies this rule to the Worker.
Purpose and material relation: a mismatch known before the step begins is
reported with its cause in the one core, so it is neither mistaken for a
step that stopped nor for one that ran.

### Construction availability

A step's output is a candidate until evaluated (FOUNDATIONS §3, P0): the
constructed subject of a constructing step, or the closed results of an
assessing step. Construction availability records whether that output
exists (P5, P6):

| Value | Core value | Ground |
|---|---|---|
| `candidate_ready` | satisfied | an exact candidate and its transition evidence are available |
| `refused` | falsified | lawful activation occurred, and a governing prohibition or an owner-valid construction refusal defeats the requested construction; the prohibition or refusal is the counterexample |
| `incomplete` | falsified | the lawfully activated step stopped without its output, because an evaluation the output needs was not performed or could not be decided on the admissible evidence, or bounded execution ended first; the stop basis is the counterexample, and it and the residuals name which |
| `re_entry_requested(authority)` | out_of_frame | a material decision the step needs lies outside its grant; the value names the owner of that decision |
| `re_entry_requested(basis)` | invalid_basis | the activated basis can no longer support the work |

The mapping is total and exclusive after lawful activation: the cause of
the stop selects the value, and payload wording, stop timing or actor
preference cannot select another. A mismatch known during admission or
activation is no value of this refinement, because no step exists; it
takes its outcome under Admission and activation above.

`satisfied` here establishes availability only and never counts toward the
candidate's fitness or acceptance (FOUNDATIONS §4 Results).

`incomplete` maps to `falsified` only for "a candidate is available", never
to `indeterminate`. The step's evaluations keep their own results: each
evaluation it performed returns its core value, `indeterminate` where the
admissible evidence could not decide; each evaluation it planned and did
not perform has no result, and its work state (§5) carries it as a
residual with the capability or the execution left unfinished
(FOUNDATIONS §4 Results, the third case of the boundary). An evaluation
not performed thus stays distinct from one whose evidence cannot decide
(P5, P6).

An assessing step that ends `incomplete` leaves each criterion it did not
evaluate not performed: no result, never `falsified`. The `falsified` of its
availability concerns its own output, never the subject under assessment
(P6).

The cause of a re-entry request is part of its value, because a re-entry
request without its cause would map to `out_of_frame` or to
`invalid_basis` according to that cause, and a refined value maps to
exactly one core value (FOUNDATIONS §4 Results, Refinements). A stop
with both causes records both and takes `re_entry_requested(basis)`,
because a decision cannot be taken on a basis that cannot support it (P5,
P3).

### Disposition

The decision owner disposes an assessed candidate with one of four
semantic dispositions (§1, Roles and delegation; P6, P5). An assessor may recommend one; the
recommendation is evidence for the decision owner, never a disposition
([EVALUATION §4](EVALUATION.md#4-review-results)). The disposition is the
acceptance result: it consumes the candidate's availability and assessment
results and stays separate from both (FOUNDATIONS §4 Results). Each maps
to the core for the predicate "the candidate is accepted at its declared
boundary":

| Disposition | Condition | Core value |
|---|---|---|
| `accept` | the candidate closes its declared cone and preserves every affected governing relation | satisfied |
| `local_repair` | implementation or proof is locally defective while the governing relation remains coherent | falsified |
| `re_enter` | the governing outcome, a requirement, an identity, a lifecycle, an authority, a public contract or the accepted design must change | invalid_basis |
| `reject` | the candidate violates a governing relation or leaves an undisposed competing truth path | falsified |

For `local_repair` the local defect, and for `reject` the violated relation
or the competing truth path, is the counterexample to accepting this
candidate; a repaired candidate is a new candidate with its own results.
For `re_enter` the governing basis the candidate was built and assessed on
must change, so that basis cannot support acceptance; the change re-enters
at its owning relation (§4). The core values place
acceptance in the one core, as FOUNDATIONS §4 Results requires, so that a
consumer combining results cannot take availability or assessment as
acceptance (P6).

Global correctness means conserving every global relation affected by the
bounded action; it does not require proving the whole product inside every
local action (P4b). Repeated rejection against one unchanged boundary
requires reassessment of the frame altitude, the causal cone, the common
components, the design-versus-code placement and the authority
sufficiency. The method sets no rejection-count threshold, mandatory
review-round count or review state machine; it prohibits repeating an
unchanged failed construction relation as if iteration alone could close
it (P2).

### Ambiguity outcome

A declared ambiguity is resolved, carried, escalated or blocked, and the
outcome is recorded either way (§4, which also names the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies this to the method's chain of authority surfaces). Each outcome
maps to the core for the predicate "the declared ambiguity is resolved on
the exact basis" (P5, P6):

| Outcome | Core value | Ground |
|---|---|---|
| `resolved` | satisfied | a decision was taken under the policy that permits lawful probabilistic processing, or by human adjudication, and recorded |
| `carried` | falsified | policy permits work to continue with the ambiguity open; the open ambiguity is the counterexample, and it stays a recorded residual that names the evidence or decision that would resolve it |
| `escalated` | out_of_frame | policy or risk appetite reserves the decision to human adjudication, an authority the step does not hold; the value names that authority |
| `blocked` | falsified | the ambiguity stays unresolved, and policy or a hard stop (§4) halts work at it; the open ambiguity is the counterexample, and the value names the halting condition and what would lift it |

An open ambiguity is a known state of the exact basis, so `carried` and
`blocked` decide the predicate false; neither is `indeterminate`, whose
evidence cannot decide the predicate. Each keeps its domain outcome with
the value: `carried` with what would resolve the ambiguity, `blocked` with
the halting condition and what would lift it (FOUNDATIONS §4 Results,
Recording). No outcome other than `resolved` maps to `satisfied`, so a
dependent claim cannot rest on a carried, escalated or blocked ambiguity
as if it were resolved. The mapping places ambiguity outcomes
in the one core, which FOUNDATIONS §4 Results requires of every outcome
(P5, P6).

### Effects

An effectful step's intended external effect has one of three values,
mapped for the predicate "the intended effect occurred", that is, the
declared outcome of the effect is attained. The value turns on what the
admitted evidence establishes about that outcome (P5 with the open-world
premise, P6):

| Value | Core value | Ground |
|---|---|---|
| `completed` | satisfied | evidence about the subject establishes that the intended effect occurred in full and that the effect has ended |
| `not_effected` | falsified | evidence about the subject establishes that the declared outcome is not attained and that no later completion of the effect can attain it, for example where no effect began, the effect ended short, an interval that the declared outcome bounds has closed with part of it not done, or the part already done has itself made the declared outcome unattainable, as when it destroyed what the outcome needed; any part that did occur is named with the value |
| `completion_unknown` | indeterminate | neither of the other values is established: the evidence cannot decide whether the intended effect has occurred or will occur, as for a request whose response was lost with no counterexample observed; or the evidence shows the intended effect in full while the effect may still be acting, and the outcome stays undecided until what the effect leaves on the subject is settled; its residual names the observation that would decide |

`not_effected` requires evidence about the subject. A lost response, an
absent record, or an actor's context that holds no trace of the effect is
not that evidence, and the value stays `completion_unknown`.
`completion_unknown` never maps to `completed` or to `not_effected`.

Whether the effect has ended is a second question beside the predicate
above, and it enters the value only as a conjunct of `completed`. An
effect has ended where evidence about the subject establishes
that it no longer acts on the subject or that it never began. Where an
effect began and the evidence does not establish its end, the end is not
established, and that is recorded beside the value as a residual naming
the observation that would establish it. The end never decides a
`not_effected` value and is never folded into one: when an interval that
the declared outcome bounds has closed with part not done, the value is
`not_effected` while the effect may still be acting. The residual does
not weaken the counterexample, and the counterexample does not resolve
the residual. `completed` alone requires the end established, so a
counterexample stands without proof that the effect has ended, while
success is never claimed for an effect that may still be acting
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Standing).

An effect of uncertain completion is one whose value is
`completion_unknown`, or whose value is `not_effected` with its end not
established. §5 reconciles it, sufficiently for the next dependent
action, before any repetition or dependent action. A `not_effected`
value licenses neither treating the effect as absent nor repeating it
while its end is not established.

The refinement's material relation is whether an action whose
external effect may have occurred is repeated or relied on; §4 names a
lost post-effect response as a case that no added core value solves, and
this refinement records it in the existing core. Keeping the end of the
effect beside the value keeps two facts that one value would merge: a
counterexample already established for the declared outcome, and an
effect that may still be acting.

## 4. Totality and refinement

Next moves after any non-satisfied result are named in advance: continue
within the current contract when supported; refine; recover; yield; re-enter
the owning relation; terminate. Each admitted condition class has a declared
next move, including an explicit unknown class. Total handling does not
claim that every external condition is recognised, that an invoked provider
terminates, or that every request can be completed. A hanging external call,
an unsatisfiable demand and a lost post-effect response are three different
cases and none is solved by adding a value to the algebra.

Claiming the common deterministic kind adds the total-domain and termination
contract of [AXIOMATIC_CALCULUS §5](AXIOMATIC_CALCULUS.md#5-traversals-and-functor-kinds).
This section's total handling does not establish that qualification. Fuel
exhaustion retains the evaluated predicate; candidate absence, an available
indeterminate assessment report and an unperformed assessment take the
different results of [§3](#construction-availability), as the
[finite cases](examples/DETERMINISTIC_CONTRACTS.md#exhaustion) demonstrate.

Which outcome of [§3 Ambiguity outcome](#ambiguity-outcome) a declared
ambiguity takes is decided by the applicable ambiguity policy and its risk
appetite, an added choice; for this method the owner of the default
policy is [SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle),
and this section states none. The outcome is recorded either way.

Hard stops. Some conditions are not optional ambiguity decisions and
remain hard stops regardless of risk appetite. Typical hard-stop classes
include: a violated invariant or guarantee; an absent required authority
surface; a missing declared capability for an executional or operational
stage; an undeclared irreversible side effect; and an explicit policy gate
requiring human approval. A hard stop halts the work at its condition whatever the policy:
for a declared ambiguity, with the §3 Ambiguity outcome `blocked`;
otherwise, as a stop of [§1 Transitions](#transitions), Stops. This
section owns the hard stops;
[SPEC_METHOD §5](SPEC_METHOD.md#5-ambiguity-governance-and-lifecycle)
applies them to the method's chain of authority surfaces (P6, P5).

Reconfiguration. An out_of_frame, invalid_basis, repeated indeterminate or
incompatible result causes one of: supply the missing admissible evidence;
select another actor inside the frame's capability envelope; activate
another existing frame; refine or extend a frame declaration; revise the
frame set (REFERENCE_FRAME §10); change the evaluation; or re-enter the
governing product or method relation. The next move follows the cause; a
difficult evaluation alone does not prove that another frame is required
(P5, P2).

### Refinement

An outer transformation T: A → X with success predicates P₀ … Pₙ
is faithfully refined by steps Tᵢ when each admitted input satisfying Pᵢ
yields an output satisfying Pᵢ₊₁, retains every applicable invariant, exposes
other outcomes without coercion, and each output satisfies the next step's
declared domain and preconditions, as typed composition requires (P4a;
[AXIOMATIC_CALCULUS §5 AC-016](AXIOMATIC_CALCULUS.md#ac-016-typed-composition)).
The step and end-to-end preservation obligations this refinement discharges, and what a completion-only relation leaves unclaimed, are [FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction); this section applies them to refinement. Then a successful composite of exact steps carries P₀ to Pₙ by induction;
a composite that contains an approximate step carries only what its
end-to-end bound states (Exact and approximate steps below). A refinement
carries an earlier output to a later step other than the next only through
a declared adapter, itself a step composed under AC-016, or a declared
specialised contract, in either case one whose declared domain names what
is carried; a specialised contract is declared under its owner's exact
authority, context, basis, scope, preservation, loss, refusal and
invalidation law (P4a, P4b).
Coverage of the outer obligations, correctness of the local
implications and legitimate authority are premises, not conclusions; "each
step passed" is weaker than "the outer contract was conserved". Required
coupled relations must fit together in some step; unrelated obligations stay
outside the selected context. Every seam crossing the affected set includes
its far side or states why it cannot participate
([UP-017](DESIGN_MODULE.md#bounded-frame-conservation-up-017)).
Admission of a material transition is one semantic commit of the complete
transition within its enclosing relation, or none (the law below). The ODD [graph-function binding](ODD.md#graph-functions) refines one
outer vector into an inner workflow; this law also applies to other
realisations. [PROFILES §2](PROFILES.md#2-graph-execution) locates the ODD binding.

Preservation and licensing. A refinement step decomposes a transformation
into steps, as above. A rewrite step replaces a representation, a step or
a composite by another that is claimed to keep its meaning, for example
by partitioning, regrouping, reordering, merging or substituting parts.
Each refinement layer, the steps that refine one transformation, states
what it preserves of the layer above, the transformation it refines, and
discharges that obligation (P4a, P6). A refinement or rewrite step is
admissible only under the laws declared for its subject. Its licensing law is the declared
law that permits it, such as an associativity, commutativity or
equivalence law that the subject's owner declares for the subject. Where
no law is declared for the subject, only universally valid steps are
admissible: steps that hold whatever laws the subject has. A step that
is neither licensed nor universally valid, such as a partition or
regrouping that no declared law permits, is inadmissible, and so is a
refinement or rewrite that relies on it (P4a, P1).

Exact and approximate steps. An exact step preserves meaning: under the
subject's declared interpretation, its output means what the material it
replaces means, and an exact refinement step carries Pᵢ to Pᵢ₊₁ without
approximation (P1). Faithful refinement, defined above, requires exact
steps. An approximate step does not preserve meaning exactly. It
states its adequacy relation, which says how close its output must be to
the exact result to be close enough for the outer contract, and the
composite that contains it states an end-to-end bound, which limits how
far the whole composite may depart from the outer obligation and is
argued for that composite. Such a composite is not faithful; it is
adequate within its end-to-end bound and establishes nothing beyond that
bound. A fixed tolerance at each step does not compose into an
end-to-end bound, because deviations that each stay within the tolerance
can accumulate across steps, so the induction above applies to exact
steps only. A step that is neither exact nor approximate with its
adequacy relation and an end-to-end bound for its composite is
inadmissible: a composite that relies on it is neither faithful nor
adequate within a bound (P4a, P6).

Purpose and material relation: a decomposition or rewrite that changes
meaning, or approximations whose deviations accumulate, would let a
composite whose every step passed violate the outer contract (P4a, P1,
P6). The material relation is whether the composite still meets the outer
obligations. Preservation per layer, licensing laws and the per-step law
for exact and approximate steps, including the inadmissibility of a step
that is neither, are stated here; the obligation to state an
adequacy relation and a composition bound, and the end-to-end obligations
of a composition, are
[FOUNDATIONS §4 Preservation through construction](FOUNDATIONS.md#preservation-through-construction),
which this section applies to refinement steps.

### Complete enclosing-relation admission

For a material transition, each admission owner is independently
responsible for deriving and validating the complete enclosing relation
from authoritative inputs (P4b, P6).
The relation contains every participant and equality join whose identity,
validity, authority, currentness or transition can affect or be affected by
admission; each crossing seam includes its relevant far side or
authoritatively establishes that the far side cannot participate. Caller or
owner assertions of completeness, validity, prior admission or authority do
not establish truth.

An owner may consume established facts when their exact subject, basis,
scope, provenance and validity remain applicable to its relation. Their
production and invalidation are recoverable; an unsupported assertion of
prior success is not such a fact. A function, component, role,
conversation or status boundary alone invalidates none of those coordinates
and requires no repeated derivation. Material mutation, rollback, changed
authority or basis, expired validity and an actual trust boundary trigger
the applicable validation before reliance or effect. Reuse does not
transfer the owner's admission responsibility, omit a participant or
satisfy a separately required independent judgment (§7).

Derivation and validation bind one exact admission-valid authoritative
basis identity through admission. If validity or currentness can advance
after preflight, admission remains conditional on the declared predecessor
and currentness law for that basis, or re-enters derivation and validation
without effect. Participating owners bind an equal basis or a
design-declared coherent composite basis; independently valid mixed-basis
judgments cannot combine (FOUNDATIONS §2, Basis).

Every participant and join is validated before any transition effect.
Internal evaluation order and lawful reuse are implementation-owned, and no
participant subset or nested constituent becomes admitted truth. Admission
is one semantic commit of the complete transition, bound to its exact basis
identity; failure or interruption admits the complete transition or none,
never a subset. No realisation mechanism or participant count is
prescribed. Direct and every supported composite or nested boundary
preserve this law: a partial result cannot substitute for an owner's
derivation and validation, and a competing same-scope path cannot establish
the transition outside the governing admission relation. Fresh
reconstruction and replay over the same basis reproduce the enclosing
relation, the basis identity and the complete outcome or refusal exactly at
semantic altitude (P3, P5).

The law is false if completeness is asserted rather than derived; a
relevant participant, join or seam is omitted; validation and admission use
an unidentified, stale or incoherently mixed basis; currentness can
advance without a commit condition or effect-free re-entry; any effect
precedes complete validation; failure or interruption exposes a subset;
fresh reconstruction differs; or competing same-scope authority remains.

### Standing structural qualification

Qualification of the admission law is instantiated for every admission
owner and supported boundary declared by accepted design (P6). Case applicability
follows the supported input, state and operating or threat model. An
excluded threat alone cannot create an acceptance predicate or require
defensive work; a proposed scope expansion returns to its owning authority.
Supported malformed inputs, stale state and effect boundaries retain their
required checks:

| Form | Required observation |
|---|---|
| direct | the complete direct relation is derived, validated and admitted once |
| supported composite or nested | every supported constituent and owning boundary satisfies the same law; unsupported forms have a design-grounded `not_applicable` disposition and no weaker or competing path |
| forged | forged identity, membership, equality or authority reachable within the supported operating or threat model is refused without effect; exclusion requires its owning authority, not a helper's inability to construct the case |
| ambiguous enclosing relation | unresolved participant, join, seam or relation identity ambiguity is refused without effect |
| stale or advanced basis | stale input is refused, and basis advancement between preflight and admission causes effect-free re-entry rather than mixed-basis admission |
| incoherent multi-owner basis | owner judgments on bases that are neither equal nor joined by a design-declared coherent composite basis cannot combine and are refused without effect |
| competing same-scope admission authority | an undisposed competing same-scope path cannot establish the transition |
| reconstructed or fresh-process | the same basis reconstructs the same relation, basis identity and outcome or refusal |
| exact replay equality | replay over the same basis reproduces exactly the enclosing relation, basis identity and complete outcome or refusal |
| atomic publication failure | after validation succeeds, failure or interruption is observed at every materially distinct commit or publication boundary capable of exposing a subset, followed by fresh reconstruction showing the complete transition or none; named representative observations suffice only under a design-declared dominance or equivalence proof covering the complete partial-failure surface |

For an indivisible commit unit the atomic test establishes that boundary
and observes failure immediately on both sides. Final-participant
validation failure does not substitute for post-validation atomic-failure
evidence. A standing claim is false if an owner or supported boundary is
omitted, a materially distinct partial-failure boundary lacks an
observation or a declared coverage proof, a case uses a weaker helper or a
manufactured refusal, or fresh reconstruction does not compare the complete
semantic result (EVALUATION §1).

## 5. Work state and restart

Work state is the tuple of: the current persistent workspace; the governing
basis; the applicable closed results and judgments with their invalidators;
the residuals; and the known uncertainty over external effects. It is an
object (P3); its carrier (files, an event stream, another admitted owner) is
a profile or realisation choice. Resumption, checkpointing and the
progress account of this section are generic procedures
([SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)): they require
no particular carrier (P1, P6).

Resumption is re-entry of the same method over the current work state,
starting from the current material state, by a possibly different actor.
It recovers applicable progress, re-checks the invalidators of each reused
result (§7), reopens only affected support, and reconciles uncertain
external effects, sufficiently for the next dependent action, before any
repetition or dependent action. Resumption does not imply idempotence: an
action whose external effect may have occurred is not repeated blindly;
the lawful next moves are reconciliation, yield or stop.

Checkpoint. Acceptance binds one exact checkpoint. The next
already-authorised bounded action may begin without renewed human approval;
acceptance does not widen the selected outcome or the affected relation set
(P6, P2). A preservation checkpoint may retain unfinished or unaccepted
work under an existing exact operation grant; it identifies its parent or
predecessor, the included territory, the concurrent-writer disposition and
the durable evidence location, and it is neither acceptance, promotion nor
publication. A proposed restart, which reconstructs from less than the
retained work, identifies why repair of retained work is insufficient,
which obligations and evidence survive, and which causal assumptions
change; reconstructability alone does not select reconstruction. The work state and reconciliation
of uncertain effects preserve the retained progress and unresolved obligations
(P0, P5 with the open-world premise).

Progress is accepted material movement toward the selected outcome;
prerequisite work names the obligation it enables; preservation and
repeated proof are evidence, not new progress; rejected or superseded
construction is churn; discovering previously hidden distance revises the
forecast and is not negative progress. Paperwork, code volume, test count,
commit count and review count are not progress by themselves. These are
semantic categories, not a numeric progress algorithm; a consumer may
derive its own progress and churn projections from them (P2). A member,
profile or project that distinguishes finer categories for its own
outcome states them as a refinement of these, naming this paragraph and
mapping each of its categories to one of progress, prerequisite work,
evidence that is not new progress, churn or forecast revision; a category
it cannot map is a change to this owner, not a parallel category (P2, P6).

The execution protocol of §1, §3 and this section is false if execution
proceeds from unreconstructable context; if a constructor's report
substitutes for required independent live evidence; if a bounded proxy
changes a governing relation outside its delegation; if unrelated
incompleteness blocks a closed causal cone; if a same-process test is used
to prove materially cross-process authority (§7); or if rejected activity
is reported as accepted progress.

Foundation to law. This family, work state, resumption and reuse, covers
this section and §7. Its instance premises are: (a) a workspace that
persists across activations; (b) work that spans activations; (c) actors
that may change between activations; (d) external effects in an open
world. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P3 (independent), P0 (recovered); instance premises a, b | By P3 work state binds an exact basis, and by P0 an actor holds only part of it at a time, so work state is an object: the workspace, the governing basis, the applicable closed results and judgments, the residuals and the uncertainty over external effects | [§5](#5-work-state-and-restart), first paragraph | its carrier (files, an event stream, another admitted owner): the profile or realisation | 2, 5 |
| P0 (recovered), P3 (independent), P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P6 (independent); instance premises a, c | By P0 an actor's context is bounded and disposable, by P3 the workspace binds the exact state, and by P4b recorded facts persist where the context does not, so the workspace is the truth surface and an actor's context a disposable account of it; current evidence corrects the account; discarding the account resets nothing | [The workspace and an actor's account](#the-workspace-and-an-actors-account) | the observations and reconciliations a resumption needs: the recovery contract, which is the resuming step's intake with the work state | 6, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise d | By P5 an effect of uncertain completion is undecided, and by P6 repeating an effect needs evidence that it is safe, so an effect of uncertain completion is reconciled before any repetition or dependent action; resumption does not imply idempotence | [§5](#5-work-state-and-restart) Resumption; [§3 Effects](#effects) | none | 4, 5 |
| P2 (independent), P6 (independent); instance premise b | By P2 progress is movement toward the selected outcome, and by P6 acceptance binds what was evaluated, so acceptance binds one exact checkpoint; a restart states why repair of retained work is insufficient; progress is accepted movement towards the selected outcome, not a count; finer progress categories refine these with a map | [§5](#5-work-state-and-restart) Checkpoint and Progress | progress and churn projections: their consumer | 5 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable), P0 (recovered), P6 (independent); instance premise c | By P4b and P0 private working context does not survive the actor, and by P6 a reused judgment is not a new independent one, so handoff is by closed results without private working context; reuse checks exact applicability and three invalidators, a material input change (newly acquired material evidence included), a changed basis and a declared revising observation, and a domain trigger is an instance of one of them; a reused judgment does not satisfy a required independent judgment | [§7](#7-closed-result-and-reuse) | the revising observation a result declares, and its other invalidation conditions: the producer of that result | 7, 9 |
| P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent); instance premise c | By P5 a transition's outcome is undecided without its evidence, and by P6 a proof establishes only the authority it was produced under, so a reviewable transition names its exact candidate, changes, proof and disposition; a same-process proof does not establish a reconstructable authority claim where the loss of process state is a counterexample | [Transition evidence](#transition-evidence) | the representation of transition evidence: its consumer | 9 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, work state as an object: [§1 Transitions](#transitions), where the current state is the work state this section records; [FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Not performed, and [Assertions and observation](FOUNDATIONS.md#assertions-and-observation), where unresolved work and an unexercised capability are a state of the work, carried as a residual and not a result; [WORLD_MODEL §14](WORLD_MODEL.md#14-results-of-this-profile), where a step's work state carries an unrun verification as a residual; [REFERENCE_FRAME §10 Revision actions](REFERENCE_FRAME.md#revision-actions), where results reopened without a material revision are recorded in the work state; [UX §8 Msg-replay proof](UX.md#msg-replay-proof), whose Msg log is the surface's recorded work state, and the [UX family table](UX.md#foundation-to-law), whose row for continuation and replay imports F4; the [ODD family table](ODD.md#foundation-to-law), whose rows for the immutable ledger and for yield import F4 for a replay-visible work state.
- Row 2, the workspace and an actor's account: [§1 Transitions](#transitions), where an actor's context is an account of the current state and not the state itself; [EXECUTIVE_BASELINE §20](EXECUTIVE_BASELINE.md#20-failure-classification), where a compression, summary or prior result that replaces current source authority is evidence substitution and a retained account never overrules current evidence; [UX §8 Msg-replay proof](UX.md#msg-replay-proof), where replay is resumption from the recorded work state; [CONFORMANCE §4](CONFORMANCE.md#4-cases-for-method-discriminators), case CD-03, and [§5](CONFORMANCE.md#5-discriminator-coverage), discriminators 38 and 39.
- Row 3, resumption and effects of uncertain completion: [§1 Construction relation](#construction-relation), Control, where resumption reacquires current reality and unknown effects are resolved before the next dependent action; [EXECUTIVE_BASELINE §12 step 4](EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result), [§7 The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration), failure assumptions, and [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), whose work result names each intended effect with its value, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the effect field imports F4 for the reconciliation; [PRODUCT_DEFINITION §4 Explicit complete consumer update](PRODUCT_DEFINITION.md#explicit-complete-consumer-update), where an update of uncertain completion is reconciled from the presented preimages before any repetition; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), where a retry waits on that reconciliation; [TRAVERSAL_OCCURRENCE Closed constraint, judgment, residual and stop kinds](TRAVERSAL_OCCURRENCE.md#closed-constraint-judgment-residual-and-stop-kinds) and [Mutable-subject effect relation](TRAVERSAL_OCCURRENCE.md#mutable-subject-effect-relation), where an effect whose end is not established is reconciled before any repetition; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where recovery reacquires current reality and need not erase valid work; [CONFORMANCE §4](CONFORMANCE.md#4-cases-for-method-discriminators), case CD-03, and [§5](CONFORMANCE.md#5-discriminator-coverage), discriminators 38 and 39.
- Row 4, checkpoint and progress: [SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation), whose four kinds of evidence refine the progress categories for a product outcome, and [§8](SPEC_METHOD.md#8-bounded-execution-in-this-method), where construction ends at the exact accepted checkpoint and the next already-authorised bounded action; [EXECUTIVE_BASELINE §14](EXECUTIVE_BASELINE.md#14-coverage-application), where checkpoint and continuation are the Executive's under existing authority; [CONFORMANCE §1](CONFORMANCE.md#1-counterexample-cases), case C-03, where a restart proposal states why repair of retained work is insufficient.
- Row 5, closed result and reuse: [§6](#6-cost-and-proportionality), the method's own execution, where reuse stays subject to exact applicability and invalidation; [REFERENCE_FRAME §5 Method functions](REFERENCE_FRAME.md#5-method-functions), [§8 Coverage basis](REFERENCE_FRAME.md#coverage-basis) and [§10 Revision actions](REFERENCE_FRAME.md#revision-actions), where whether a closed result or a coverage result stays valid is decided by the reuse rule; [EVALUATION §2](EVALUATION.md#2-separation), [§3](EVALUATION.md#3-independent-assessment), where shared mechanical evidence may be reused and judgment may not, and [§6](EVALUATION.md#6-conformance-of-realisations), where an accepted relation is reused after checking applicability and invalidation; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), which applies the rule to computed classification, and [Consistency gate](SPEC_METHOD.md#consistency-gate); [TICKETS §7 Recorded judgment and owner-ruling continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity) and [Condition-based closure and reuse](TICKETS.md#condition-based-closure-and-reuse); [EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability), [§5 Work result](EXECUTIVE_BASELINE.md#work-result), [§6 Attention cycle](EXECUTIVE_BASELINE.md#attention-cycle) and [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), specialist result, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Product chain imports F4 for the repair that invalidates affected results; [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design), [Capability and foundation selection (UP-023)](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), [§7 Gate and retrospective work](DESIGN_MODULE.md#gate-and-retrospective-work) and [§10 Post-ticket design review](DESIGN_MODULE.md#post-ticket-design-review), and the [DESIGN_MODULE family table](DESIGN_MODULE.md#foundation-to-law), whose row for that review imports F4; [ASSURANCE §7 The set](ASSURANCE.md#the-set), whose invalidation rows name instances of this rule's invalidators, and [§13 Obligations](ASSURANCE.md#obligations), item 4; [WORLD_MODEL §2 Builder Project specialisation](WORLD_MODEL.md#builder-project-specialisation), whose invalidation conditions are instances of them; [CONFORMANCE §1](CONFORMANCE.md#1-counterexample-cases), case C-04, and [§5](CONFORMANCE.md#5-discriminator-coverage), discriminators 21 and 36.
- Row 6, transition evidence: [TICKETS §7 Execution and verification authority separation (UP-007)](TICKETS.md#execution-and-verification-authority-separation-up-007), where the reviewable transition is carried by an existing surface and no new ceremony is required; [EXECUTIVE_BASELINE §5 Exact candidate](EXECUTIVE_BASELINE.md#exact-candidate), [§8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), for the proof cadence, [§9](EXECUTIVE_BASELINE.md#9-derived-worker-frame), where `candidate_ready` binds the exact candidate and the transition evidence, [§12 step 5B](EXECUTIVE_BASELINE.md#5b-candidate-requires-independent-review), [§13 Handoff projection](EXECUTIVE_BASELINE.md#13-handoff-projection), work result, and [§14](EXECUTIVE_BASELINE.md#14-coverage-application), where candidate and transition evidence are the Worker's.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### The workspace and an actor's account

The workspace and its authoritative inputs persist across activations and
are the continuing truth surface of the work: the surface whose current
material state decides what the work has and has not done. An actor's
context is an account of that state. It is bounded, because it is a
projection of the state (§2); revisable, because an observation can
correct it; and disposable, because a step records its closed results and
step-produced facts before it returns (§1 Admission; P4b). An account is
never a second truth surface, and no later activation needs a prior
actor's context: its intake reconstructs the governing relations without
it (§1 Intake) (P0, P3, P6).

Acquisition ([§2](#2-context-construction-under-an-envelope)) observes the
current subject and its authoritative inputs. Where they materially
disagree with a cached belief, a retained summary or a prior result, the
actor reconciles the disagreement: current evidence corrects the account,
and what the evidence cannot decide stays an explicit unknown. A stored
belief, a summary or a successful prior result never overrules contrary
current evidence. A prior result is relied on only after its
applicability and invalidators are checked against the current subject
and inputs (§7). The actor corrects its account within its grant; where
resolving the disagreement needs an operation, a territory or a decision
outside the grant, the step stops with `re_entry_requested(authority)`,
naming the owner of what it needs (§3 Construction availability) (P5,
P6).

Discarding an actor's private context resets nothing: the workspace, the
applicable valid work and the outstanding obligations remain as the work
state records them. A missing trace in a context, a memory or a summary is
no evidence about the subject. It shows neither that work was not done
nor that an external effect did not occur, nor that it ended; an effect
of uncertain completion keeps the value `completion_unknown`, or its end
stays not established beside its `not_effected` value, until evidence
about the subject decides it (§3 Effects) (P5).

Work that an interruption left partly written is part of the current
material state from which resumption (above) starts, and is assessed as
it stands; an assessment that was not performed has no result and is
never recorded as performed
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results); §3 Construction
availability). The method imposes no universal reset and no obligation to
replay the complete history. The recovery contract that applies, which is
the resuming step's intake with the work state, determines which
observations and which effect reconciliations the next dependent action
needs. Handoff between actors is by closed results, which carry no private
working context and keep their validity and independence conditions (§7)
(P0, P4b).

Purpose and material relation: finite context (P0) means an actor's
context ends or is replaced while the work continues, and discarding it is
safe only because the step-produced facts the outer contract needs are
recorded (P4b). Treating the account as the truth surface would let a
stale account overrule the workspace; treating a discarded account as a
reset would erase progress or repeat an effect that occurred (P5, P6). The
material relation is whether a decision relies on an account that current
evidence contradicts, or reads a missing record as undone work or an
absent effect.  The workspace, the
work state and the closed results carry it, and no further carrier is
required.

## 6. Cost and proportionality

Proportionality is the relation between semantic ambiguity removed and
effective reasoning complexity introduced. A method obligation is
proportional when its contraction of the admissible interpretation space
justifies the additional concepts, relations, projections and evidence an
actor must hold together to reach a correct decision (P2, P0).

Effective reasoning complexity includes independent concepts and authority
surfaces, cross-document joins, exceptions and branching, states and
transitions, duplicated representations requiring reconciliation, and the
detail required to decide the governed question. It is not raw line count,
artifact count or context-window size. A detailed algebra or semantic
design view may be highly proportional when it eliminates rival
interpretations; a short additional ticket, receipt or summary may be
disproportionate when it creates another truth surface without reducing
uncertainty.

A proportional method deliberately constrains the admissible reasoning and
realisation space. Each constraint identifies the semantic ambiguity it
removes and contracts enough of the admissible interpretation space to
justify the reasoning complexity it introduces. Rival authority,
uncertainty over failure classification and evidence uncertainty count only
where they leave materially distinct admissible semantic, authority,
outcome or acceptance interpretations; they measure or evidence the same
interpretation space removed and are not independent proportional
benefits. The method does not prescribe an internal decomposition, search,
collaboration, tool or synthesis procedure when variation in that procedure
cannot affect a governed semantic, authority, evidence, safety or release
property. Increased actor capability may enlarge the bounded relation an
actor can resolve; it grants no authority, an instance of
[FOUNDATIONS §2 Authority kinds](FOUNDATIONS.md#authority-kinds), What
creates no authority, and it weakens no invariant and waives no
acceptance (P6). The owning law may justify one coherent constraint
family once; no rationale field, receipt or repeated audit is required for
every clause or consumer application.

For symbolic design, materially divergent implementation paths, runtime
states, tests, reviews and reconciliation joins are counterfactual evidence
of the semantic alternatives the design contracts; they are not an
independent numerator. When one bounded symbolic model can resolve those
material alternatives within effective reasoning capacity, resolving it at
design altitude is proportional even when the model is detailed. A prior
design surface that removes no material semantic alternative is
disproportionate. A method addition is disproportionate when it duplicates
truth, increases reconciliation paths or expands the bounded reasoning
surface without materially reducing ambiguity; existing obligations should
absorb new detail where they can without weakening ownership or meaning.

Apply this relation to the method's own execution: repeated source
acquisition, context assembly, hashing, activation preparation, status
recording, review and evidence generation serve an identified change,
decision or assurance need. Reuse stays subject to exact applicability and
invalidation (§7); repetition alone supplies neither validity nor
independence. Where this work materially affects the supported outcome, its
operational assumptions are qualified under UP-019 below. No universal
resource quota or separate accounting carrier follows. The delivery
priority this relation yields for a product outcome is SPEC_METHOD §8.

Cost is selected, not universal. Where a cost claim is the governed
question, the activation declares its allowance and reports its spend,
measured under the selected execution binding or recorded as unmeasured
(P0; Resource limits below). The size of an activation's
context is measured and fitted under §2 step 3, which refines the
resource-limit law below for the context dimension. Separate material startup, framework
processing, external computation, transport and assurance costs so that
one cannot conceal another; declare supported input dimensions and
workloads before qualification
([UP-019](DESIGN_MODULE.md#computational-realisation-projection-up-019)).
Report volume is not model traffic; a cost claim over transferred context
counts the context transferred to every delegated actor, not only to the
coordinator. No universal quota, ticket count, actor count or accounting
carrier follows.

Foundation to law. This family, proportionality and cost, covers this
section, with Resource limits below, and the delivery priority of
SPEC_METHOD §8. Its instance premises
are: (a) a selected outcome; (b) method obligations that each add
reasoning complexity; (c) where one is the governed question, a cost
claim; (d) an activation that consumes bounded resources, such as
context, attention, time or spend. They are conditions of the work this family governs, not
commitments, and do not follow from finite capacity alone. The standing of
the consequences below is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P2 (independent), P0 (recovered); instance premise b | By P2 an obligation is justified only by its route to the outcome, and by P0 reasoning capacity is finite, so a method obligation is proportional only when the ambiguity it removes justifies the reasoning complexity it adds, and that complexity is not raw size | [§6](#6-cost-and-proportionality), first three paragraphs | the justification of a constraint family: its owning law, once for the family | 6, 7 |
| P2 (independent), P0 (recovered), P1 (independent); instance premise b | By P2 and P0 detail is justified where it resolves alternatives the actor can hold, and by P1 a duplicate of truth is a second representation, not more truth, so a detailed symbolic design that resolves material alternatives within reasoning capacity is proportional; an addition that duplicates truth or adds reconciliation paths without reducing ambiguity is not | [§6](#6-cost-and-proportionality), symbolic-design paragraph | none | 4, 6 |
| P2 (independent), P0 (recovered), P6 (independent); instance premise b | By P2 the method's own steps need an identified purpose, and by P6 and P0 repetition adds neither validity nor independence, so the method's own acquisition, hashing, review and evidence serve an identified need; repetition supplies neither validity nor independence | [§6](#6-cost-and-proportionality), method's own execution | none | 7, 9 |
| P0 (recovered), P2 (independent); instance premise c | By P0 and P2 spend is part of what a finite actor's work costs the outcome, so a cost claim declares its allowance and reports spend measured under the selected execution binding, or recorded as unmeasured; costs that could conceal one another are kept apart; no universal quota follows | [§6](#6-cost-and-proportionality), Cost is selected | the allowance: the activation that makes the claim; the measurement units and boundaries of the cost components: the selected execution binding, under [Resource limits](#resource-limits) | 8 |
| P0 (recovered), P5 (derived from P0 and P6, with P0's open-world premise), P6 (independent), P2 (independent); instance premise d | By P0 limits bind only as declared and measured, by P5 an unmeasured consumption supports no claim of fit, and by P6 and P2 staying within a limit establishes no adequacy, so a resource limit binds only where it is declared, with its unit and measurement boundary, and no universal quota follows; consumption outside the measured boundary supports no fit; pressure on a limit never licenses omission, so the activation refines, sequences, reassigns or stops with a named value; staying within limits shows no adequacy and grants no authority | [Resource limits](#resource-limits) | the value of each limit and the units and boundaries the environment can measure: the selected execution binding, for a build tenant [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) | 8, 7 |
| P2 (independent), P0 (recovered); instance premise a | By P2 delivery serves the outcome, and by P0 an actor can pursue only part of it at a time, so delivery for a product outcome is prioritised by this relation over likelihood, impact, reversibility, dependency and delayed feedback; probability waives no hard stop | [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method), outside this member | the default priority, the smallest supported product path first: SPEC_METHOD §8 | 1, 5 |

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the proportionality relation: [§1 Configuration](#configuration), whose explanation of an allocation is proportional, and [Roles and delegation](#roles-and-delegation), where a review or ceremony that no law requires adds reasoning cost without removing ambiguity; [§7 Transition evidence](#transition-evidence), whose proof cadence uses the cheapest focused proof unless the affected risk makes whole-candidate proof necessary; [DESIGN_MODULE §5](DESIGN_MODULE.md#5-ontology-first-design), its opening, and [Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the relation selects between co-evolution and a design gate; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), which applies the relation to Prime contraction; [Capability and foundation selection (UP-023)](DESIGN_MODULE.md#capability-and-foundation-selection-up-023), whose selection pass is applied proportionally; [CONFORMANCE §1](CONFORMANCE.md#1-counterexample-cases), case C-12, and [§5](CONFORMANCE.md#5-discriminator-coverage), discriminator 41.
- Row 2, symbolic design and the disproportion test: [DESIGN_MODULE §5 Proportional design sequencing](DESIGN_MODULE.md#proportional-design-sequencing), where the realisation space a bounded symbolic model removes is counterfactual evidence and a gate that removes no material alternative adds ceremony; [§6 Boundary and governance cost (UP-005)](DESIGN_MODULE.md#boundary-and-governance-cost-up-005), where a contraction that adds authority centres or truth surfaces does not succeed; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 11.
- Row 3, the method's own execution: [EXECUTIVE_BASELINE §6 Event-driven attention](EXECUTIVE_BASELINE.md#event-driven-attention), where repeated polling or repair on an unchanged basis is no reassessment and reduced churn introduces no universal cost gate; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where the selection of checks after a change weighs acquisition, execution and assessment costs against the required assurance.
- Row 4, cost is selected: [§1 Intake](#intake), where an intake whose governed question is a cost claim declares the allowance and how spend will be measured; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where frame selection creates no universal resource ledger and this section is the cost control where a cost claim is the governed question; [FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse), where anticipated costs are distinguished from measurements; [DESIGN_MODULE §7 Computational realisation projection (UP-019)](DESIGN_MODULE.md#computational-realisation-projection-up-019), which takes the separation of startup, framework, external, transport and assurance costs from here; [EVALUATION §7 Method self-qualification](EVALUATION.md#method-self-qualification), where mechanical and operational claims carry the workload and operational assumptions declared here; [CONFORMANCE §1](CONFORMANCE.md#1-counterexample-cases), cases C-01 and C-06.
- Row 5, resource limits: [§1 Configuration](#configuration), where each assumed limit is declared as this subsection states, and [§2](#2-context-construction-under-an-envelope), step 3, which refines the law for the context dimension and measures over the boundary the execution binding states; [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), whose binding sets the values, units and boundaries; [EXECUTIVE_BASELINE §7 The executive configuration](EXECUTIVE_BASELINE.md#the-executive-configuration), whose assumed limits are declared, measured and honoured as this subsection states, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for that configuration imports F5 for them; [EVALUATION §7 Frame qualification](EVALUATION.md#frame-qualification), where time, spend and other limits are the execution binding's under this law and not of the fit test; [REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection), where a resource control applies only through a selected frame; [CONFORMANCE §2](CONFORMANCE.md#2-construction-trials), whose total-work budget is a limit declared under this subsection.
- Row 6, delivery priority: [EXECUTIVE_BASELINE §8 Steel-thread delivery](EXECUTIVE_BASELINE.md#steel-thread-delivery), whose sequencing around the smallest runnable path is this priority as profile law; [ASSURANCE §13 Obligations](ASSURANCE.md#obligations), where an early sunny thread establishes bounded evidence while unexercised claims stay open, the sequencing heuristic of SPEC_METHOD §8.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

### Resource limits

A resource limit bounds a resource that an activation consumes: context,
attention, wall time, spend, human effort, communication or a machine
resource (P0). This subsection owns the law for every such limit. It sets
no value (P0, P2, P5, P6):

- Declaration. A limit applies to an activation only where its intake,
  its actor's capability envelope or the selected execution binding
  declares it, because a resource control applies only through a selected
  frame and its owning scope
  ([REFERENCE_FRAME §4 Frame-set selection](REFERENCE_FRAME.md#frame-set-selection)).
  A declared limit states its unit and the boundary over which it is
  measured: which inputs, actors, processes and repeated reads it counts.
  No universal quota, budget or measurement gate follows.
- Measurement. A declared limit is measured in its unit over its boundary
  where the obligation it serves needs the measurement; consumption
  outside the boundary is recorded as not measured, and no claim against
  the limit covers it. A context limit bounds the material held in active
  context at once, including material acquired during the activation, so
  the bytes supplied at its start, the cumulative bytes it acquires,
  counting repeated reads, and the bound on what it holds at once are
  reported separately; §2 step 3 refines this for the measurement of the
  selected context before it is read. Measures that answer different
  questions, such as the cost components of Cost is selected above, are
  reported separately.
- Exhaustion. Pressure on a declared limit never licenses omitting or
  truncating a material obligation or input. Before a limit would be
  exceeded, the activation refines the task, sequences activations,
  reassigns the work to an actor whose limits fit, or stops with the
  applicable value of §3, naming the limit, such as `incomplete` where
  bounded execution ends first; a stop keeps the unresolved outcome
  ([§1 Transitions](#transitions), Stops). Enlarging a limit re-enters the
  owner of the grant or binding that set it.
- Values. The value of each limit, and the units and boundaries the
  selected environment can measure, are set by the selected execution
  binding, which binds this law; for a build tenant that binding is the
  one [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding) defines.
  A value is stated before the activation it limits.
- Standing. An activation that stays within its limits is not thereby
  adequate, and an actor's larger limits grant no authority and waive no
  invariant (P2, P6).

Purpose and material relation: the configuration (§1), context
construction (§2) and frame qualification
([EVALUATION §7](EVALUATION.md#frame-qualification)) rely on resource
limits, so the law for declaring, measuring and honouring them is stated
once in tier 1, and only their values are left to the execution binding.
The material relation is whether an undeclared, unmeasured or exceeded
limit is read as fitting, or forces a silent omission. The rule applies
RF-014's prohibition of silent omission, REFERENCE_FRAME §4's rule that a
resource control applies only through a selected frame, and UP-014's
selection rule.

## 7. Closed result and reuse

A closed result identifies the frame and its activation, the subject, the
basis, the evaluation, the actor, the evidence, the verdict, the residual
uncertainty and the invalidation conditions (the minimal shape is
REFERENCE_FRAME §13). The frame's internal working context need not be
transferred when the closed result and its provenance are sufficient for
the consuming decision; it may still be attached, for audit or otherwise,
without changing the result. Independent evaluations may share valid
mechanical evidence under the declared independence conditions of
[EVALUATION §3](EVALUATION.md#3-independent-assessment), which owns that
permission (P4b, P0).

The sufficiency of a handed-off result or reference for subsequent decisions
is [FOUNDATIONS §4 Observation sufficiency](FOUNDATIONS.md#assertions-and-observation)'s
consumer-relative claim. Reuse preserves the material standing and
continuation distinctions, including unassessed versus indeterminate; a
role change alone requires no full-history scan or new representation.

The selection of affected results after a change and the conditions for
retaining evidence on a new subject are
[FOUNDATIONS §4 Change impact and evidence reuse](FOUNDATIONS.md#change-impact-and-evidence-reuse);
this section applies them to closed results and handoffs, and the three
invalidators below are kinds of change Δ, and a closed result is affected
when its dependencies `D*(t)` meet the impact cover `I(Δ)` (P3, P6).

A closed result is reused by an unchanged consumer that checks exact
applicability; a role, conversation or resumption change alone invalidates
nothing. An invalidator invalidates the affected result before reliance,
even where the subject's own bytes are unchanged, preserving its
predecessor/successor relation and any demonstrably independent surviving
results. Invalidation withdraws the result from direct reliance; whether
its evidence is retained on the new basis is decided by `retain_applicable`
of FOUNDATIONS §4 Change impact and evidence reuse, and the changed
coordinate alone establishes neither that the claim fails nor that it
holds. The invalidators are three:

- a material input change: a change to the result's subject or to an
  input it rests on, including the admissible evidence that bears on its
  predicate; newly acquired or changed admissible evidence is such a
  change when it is material to the result as
  [FOUNDATIONS §2](FOUNDATIONS.md#2-ontology) defines material, that is,
  when it could change the result's value;
- a changed basis: a change to any coordinate of the basis the result
  binds (FOUNDATIONS §2, Basis);
- a declared revising observation: an observation that the result or
  judgment itself names as one that would revise it, once it occurs.

A changed source, task or actor condition is a changed basis where the
basis binds it, and otherwise a material input change; a role change that
alters a required actor condition is such a change, while a role,
conversation or resumption change that alters none of these invalidates
nothing (P3, P6).

Judgment continuity names the basis and the evidence; Return A Closed
Result names inputs and the observation. A member, profile or project
that names a trigger for its own domain, such as a changed projection,
rule or configuration, names it as an instance of one of these three and
states no parallel list (P3, P4b, P6). A reused judgment does not
satisfy a separately required independent judgment; the independent assessor
acquires its own evidence and supplies its own judgment. [TICKETS §7](TICKETS.md#recorded-judgment-and-owner-ruling-continuity)
uses the same evidence invalidator. Naming these kinds once gives every
consumer the same triggers. The
material relation is whether a result is relied on after a change that
could alter it (P3, P6). Whether a revision of a frame needs a new
revision coordinate is
[REFERENCE_FRAME §10](REFERENCE_FRAME.md#revision-actions)'s question;
whether a result it touches stays valid is this section's.

### Transition evidence

A reviewable transition identifies the exact candidate, the affected
relations, the changed realisation paths, the authority paths added or
removed, the retained and open seams, the focused proof, any required
integration proof, the explicit non-changes, and, where an assessor was
activated, the assessor's recommended disposition, with the decision
owner's disposition beside it once one is made (§3). Consumers
choose the representation. Transition evidence is a read
model; it does not become specification, design or admission authority
(P6, P4b).

Construction uses the cheapest focused proof capable of falsifying the
active relation. Expensive whole-candidate qualification occurs at a
declared candidate boundary rather than after every local edit, unless the
affected risk makes whole-candidate proof necessary (§6). A durable or
reconstructable authority claim is not established solely by a same-process
proof when loss of incidental process state is a material counterexample:
the proof destroys or excludes the incidental authority and compares the
reconstructed semantic outcomes (P5, P6).



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md
SHA256 a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8; 11713 bytes

# SDLC default frame guidance

This is a selectable projection of existing method law for ordinary software
work. It connects the current work reference and bounded context to QA,
diagnosis, re-entry, verification and durable continuation;
the linked sections remain the single deciding owners. It adds no result,
actor, workflow engine, permission or mandatory Executive configuration.

## Selection and binding

Select this guidance in the accepted Project Reference-Frame Basis, binding
its exact source identity and the governing method cut. The
[basis template](templates/PROJECT_REFERENCE_FRAME_BASIS_TEMPLATE.md#sdlc-default-selection)
proposes it ready for adoption. An existing Product may select it through its
own authorized basis change; merely installing or finding it selects nothing.
Keep the Product's policy values, explicit gates and accepted alternatives.
No numeric priority cutoff, review ratio or additional gate is supplied here.

Bind the exact claim, affected subject and basis, existing grant, carrier,
applicable obligations, actors and decision owner, evidence and stop conditions.
Use a sufficient direct Writer where the accepted configuration permits one.
Use coordination only for the material authority, dependency, capability or
attention boundary that requires it; adopt the optional Executive profile
separately. Sources: [ACTIVATION §1](ACTIVATION.md#1-the-step),
[TICKETS §5](TICKETS.md#5-from-carrier-to-execution) and
[EXECUTIVE_BASELINE §3](EXECUTIVE_BASELINE.md#3-engagement-applicability).

## Selected default flow

1. **Recover the work reference and construct bounded context.** Start from
   the exact admitted ticket, sprint entry or run contract. Bind its current
   question, subject/basis, grant, result/evidence routes and surviving
   obligations. Apply [work continuity](#work-reference-context-and-continuation)
   below before relying on a summary or prior result. A new session alone
   neither resets progress nor requires another ticket.
2. **Construct and perform incremental QA.** Check the admitted step against
   its requirement/design and the smallest adequate falsifier. State the
   observed predicate, subject, oracle, coverage and residuals. A local pass
   supports that bounded predicate; it supplies no unnamed Product acceptance,
   qualification or release claim. Preserve selected gates and mandatory
   conditions. Sources: [ASSURANCE](ASSURANCE.md),
   [EVALUATION §1](EVALUATION.md#1-claims) and
   [EVALUATION §5](EVALUATION.md#landing-closure-and-release).
3. **Triage a discrepancy before selecting a repair.** Use the causal routes
   below and retain plausible unresolved causes. Repeated failure, escalating
   repair cost or growing review context calls for bounded diagnosis of the
   frame and capability; it authorizes neither another code patch nor an
   upstream change. Source: [SPEC_METHOD intake](SPEC_METHOD.md#universal-intake-triage).
4. **Re-enter at the owning layer.** Record the change intent/class, affected
   Product boundary, first changed layer, downstream impact and whether release
   scope changes. Reuse the admitted ticket, sprint entry or run intake when
   it still covers the work. A changed requested outcome or territory needs
   owner re-entry and admission before dependent effects. Select `stdo-ticket`
   only when its durable-state need and effect grant hold; an unrelated finding
   does not silently enlarge this work. Sources: [change classes](SPEC_METHOD.md#change-classes),
   [TICKETS carrier selection](TICKETS.md#carrier-selection).
5. **Repair, verify and dispose the bounded result.** Reconcile the affected
   requirement, design, implementation, tests and displaced path; retain
   unaffected valid support. Apply the verification and stopping rules below.
   The authorized decision owner chooses `accept`, `local_repair`, `re_enter`
   or `reject` under [ACTIVATION §3](ACTIVATION.md#disposition). Preserve the
   result and lawful next action through the named durable surface before
   return. A new scope or missing authority returns to that owner before
   continuation.

## Work reference, context and continuation

The selected ticket is the enduring reference for its unit of work, under
[TICKETS records](TICKETS.md#ticket-records) and
[one-truth state](TICKETS.md#one-truth-state-projection-and-drift-refusal-up-009).
Retain a sufficient sprint or run carrier where
[carrier selection](TICKETS.md#carrier-selection) permits it. Work-state
authority, governing meaning and current material evidence remain distinct;
a context summary or index supplies none of them by itself.

Acquire the deciding owners and current material subject needed by the next
bounded decision. An accessible qualified reference must preserve the
consumer's subject/basis, assessment standing, provenance, active obligations
and invalidators. If a derived surface is stale or insufficient, re-enter the
exact owning sections. Where the selected envelope declares context capacity,
record the required measurement, capacity and comparison before reading.
Without complete active inputs or a supported upper bound, complete-fit
judgment remains unresolved unless a measured excess falsifies it. Where no
capacity is declared, no measurement gate is added. Source:
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope).

Before return, a permitted Writer records the closed result, step-produced
facts needed later, evidence, unresolved work, original owner rulings and the
next authorized action or owner re-entry in the existing named durable
result/evidence surface. Keep references with the owning work. This projection
adds no second state ledger or per-tool logging requirement. An actor without those effects
returns to the permitted Writer; Executive still performs no file or Git
mutation in that role. Sources:
[ACTIVATION admission](ACTIVATION.md#admission),
[closed results](ACTIVATION.md#7-closed-result-and-reuse),
[TICKETS continuity](TICKETS.md#recorded-judgment-and-owner-ruling-continuity).

Resume from current material state, correct a contrary retained account,
check exact applicability and invalidators, and reopen only affected support.
Reconcile uncertain external effects before a retry or dependent action;
unresolved completion remains unresolved. Handoff needs sufficient closed
results and references, not the prior actor's private conversation. Sources:
[ACTIVATION state and restart](ACTIVATION.md#5-work-state-and-restart),
[actor account](ACTIVATION.md#the-workspace-and-an-actors-account) and
[reuse](ACTIVATION.md#7-closed-result-and-reuse).

## Causal triage

The four causes are owned by
[ACTIVATION feedback and diagnosis](ACTIVATION.md#construction-relation) and
applied by [SPEC_METHOD intake](SPEC_METHOD.md#universal-intake-triage).
Use evidence that distinguishes causes over the same exact subject and basis:

| Supported cause | Lawful next action |
|---|---|
| Defective realisation under adequate unchanged law | Repair the realised surface within its grant; assert and verify no upstream drift. |
| Inadequate governing requirement or design | Return to the first inadequate owner; admit its changed truth, then derive affected downstream work and evidence. A failed candidate alone does not establish this cause. |
| Inaccurate predictive model | Return to the model's owner, identify the failed prediction and supported replacement/intervention, then re-evaluate the dependent claims. Do not relabel an outcome mismatch as a code defect without evidence. |
| Insufficient observation | Acquire the missing admissible observation through its authorized route, or retain `indeterminate` and withhold the dependent claim. Repetition of the same uninformative check supplies no missing evidence. |

If diagnosis or repair cannot fit the current capability/complexity envelope,
apply [REFERENCE_FRAME diagnostic order](REFERENCE_FRAME.md#diagnostic-order):
check the activated family, exact subject/basis, actor capability and available
evidence before missing variables, joins, families or another frame. Then
revise, decompose or request the capable evaluation through its owner. State
the missing relation/capability, next discriminating evidence and bounded
return condition. This route changes no requirement merely to make work pass.

Keep technical severity and causal confidence separate from Product priority,
promotion effect and disposition. The Reviewer supplies supported triage and
explicit uncertainty; the Product decision owner decides its consequence under
the actual mandate. Under an adopted Executive profile that owner is the
Executive. Use the selected scale and preserve historical grades; severity
does not itself grant or forbid an operation. Sources:
[EVALUATION results](EVALUATION.md#result-and-triage-projection),
[blocking](EVALUATION.md#when-a-finding-blocks-promotion) and
[Executive triage](EXECUTIVE_BASELINE.md#technical-triage-severity-priority-and-boundary-effect).

## Verification and stopping

Bind a review to one exact claim, subject, coverage population, exclusions,
capability and time/attention envelope. A budget cannot shrink a declared
claim or make missing coverage satisfied. Return its finite findings and
residuals; do not keep expanding the review until no possible issue remains.
Sources: [EVALUATION assessment](EVALUATION.md#3-independent-assessment),
[REFERENCE_FRAME closure](REFERENCE_FRAME.md#rf-012-closed-results).

Where the accepted basis selects
[EXECUTIVE_BASELINE QA cadence](EXECUTIVE_BASELINE.md#qa-cadence-and-repair-rechecks),
a mechanically decidable repair may close on a reproduction failing before
and passing after, its declared suite and the other applicable conditions.
Use an independent bounded recheck when the governing boundary requires or
claims independence, the repair concerns a hard stop or material capture
fidelity, there is no reproducing test, or selected review left declared
coverage incomplete. Required independence follows
[EVALUATION §3](EVALUATION.md#3-independent-assessment); another actor name
or a fresh context does not establish it. Other adopted configurations retain
their own recheck conditions. Tests never impersonate required assessment.

Close the repair/work claim when its applicable conjunction is satisfied and
no active non-closure condition remains; otherwise return the precise missing
condition, owner and re-entry. Stop at the activation's return boundary.
Authorized landing, work closure and named acceptance/release keep their
separate conditions. A later material finding is new input to a new bounded
disposition, not standing permission to reopen every repair or broaden review.
An adjacent observation outside the claim is retained for its lawful owner.
Sources: [TICKETS closure](TICKETS.md#condition-based-closure-and-reuse),
[QA cadence](EXECUTIVE_BASELINE.md#qa-cadence-and-repair-rechecks).

Before reuse, check exact question, subject/basis, support and invalidators.
Re-evaluate affected claims after changed material inputs, basis or capability;
retain demonstrably independent valid evidence. Required independent judgment
is not replaced by reused constructor judgment. A material frame revision
reopens every result bound to its old revision until applicability is checked.
Sources: [ACTIVATION reuse](ACTIVATION.md#7-closed-result-and-reuse),
[REFERENCE_FRAME revision](REFERENCE_FRAME.md#revision-actions),
[FOUNDATIONS change impact](FOUNDATIONS.md#change-impact-and-evidence-reuse).

[Worked cases](examples/SDLC_DEFAULTS.md) illustrate these routes. Their
expected outcomes explain the projection; they are not evidence of actual use
or qualification of an actor, host or release.



## Exact file /Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/TICKETS.md
SHA256 2e601f701170a7eece65153ba707cc7d857bfb7c3b9ce28c283dad199e919748; 101437 bytes

# TICKETS

Tier 2. Owns the work carriers of the method: goals, tickets, sprints,
comments and execution contracts as one model; the default layout and the
bindings that locate the carriers; the sprint rules; the ticket rules,
including triage-first intake, the change class the ticket records and the
upward propagation check; the selection of the smallest lawful carrier for
a piece of work and the carrier side of execution-contract admission; the
separation of execution from verification authority; the continuity of
recorded judgment and owner rulings; condition-based closure and reuse;
test case authority; the implementation-migration ticket category with its
declaration, checklist and review rules; one-truth state projection; the
recommended ticket and sprint shape; the operating mode. It is realised
from [FOUNDATIONS](FOUNDATIONS.md), [ACTIVATION](ACTIVATION.md) and
[EVALUATION](EVALUATION.md) and is the T area named by
[SPEC_METHOD §1](SPEC_METHOD.md#method-identity): nothing here is
foundational, every clause names the principle that requires it (P0 to P6,
FOUNDATIONS §3), and each mechanism could be realised differently under the
same principles. The change classes a ticket records are
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes), which is the triage target
of every clause here that names a class; the step side of admission is
[ACTIVATION §1](ACTIVATION.md#admission); the generic law of claims,
independent assessment and acceptance is EVALUATION §1, §3 and §5; the
testing law is ASSURANCE. This member defines none of those twice. Its
family table (F13) opens §5.

## 1. Work carriers

### Goals

The product definition's `ticketing.goals` binding locates the current epic
layer; `GOALS.md` is the default file (PRODUCT_DEFINITION §1). Goals are
broader than one ticket, narrower and more current than the intent surface,
and the place to state the active work wave and what matters now. Goals are
not the durable unit of execution tracking (P2, P3).

### Ticket records

Tickets are the enduring work records. Each ticket is one durable record,
one markdown file being the default carrier; the source of truth for that
unit of work; durable across sessions; and typed, so that bugs and features
share one system. A ticket is used when work needs independent durable
identity: feature work, bug tracking, spikes and chores (P3, P4b).

### Sprints

Sprints are bounded execution batches. Each sprint is one manifest under
the product definition's optional `ticketing.sprints.root` binding,
`.ai-workspace/sprints/` being the default; a control surface for a bounded
body of work; a place to batch repeated authority references, closure law,
evidence expectations and deferred local compliance debt; and closed by an
explicit sprint-close review. Sprints are not constitutional authority: they
operate under SPEC_METHOD and the project surfaces they cite
([SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) states the
sprint boundary; this member states the mechanics) (P2, P6).

A sprint may contain durable tickets, manifest-local iteration entries, or
both. Tickets carry work items that need durable identity across sessions;
manifest-local iteration entries carry small changes whose only independent
value is traceability inside the sprint. The sprint is the batch authority;
it does not erase the need for paydown tickets when close review finds debt
that must survive past the sprint (P2, P4b).

### Comments

The product definition's `ticketing.comments.root` binding is the message
board; `.ai-workspace/comments/` is the default. Comments are for publishing
ideas, strategy notes, reviews, handoffs, closure summaries, and decisions
with their reasoning. Comments are not task status authority. A comment
is a post of [POSTING_GUIDE](POSTING_GUIDE.md), which states what it
carries, its structure and its discussion state. A decision recorded in a
comment takes its authority from the surface that owns the decision, once
it is adopted there ([POSTING_GUIDE §9](POSTING_GUIDE.md#9-ratification)),
and has none of its own (P6, P3).

### Execution contracts

Tickets are durable work authority. An execution contract is the run-scoped
admitted work surface derived from a ticket, from a sprint manifest plus an
included ticket or iteration entry, or drafted during intake when no durable
or sprint-local work identity is required. The three lifetimes differ: a
ticket survives sessions and work waves; a sprint survives one bounded
execution batch and its close review; an execution contract is the current
admitted execution function for one run. Execution contracts are not a
rival backlog or a second planning surface (P0, P3).

They exist so that the system can classify the work before execution; admit
or reject the drafted classification against deterministic criteria; record
the admitted execution basis on the selected durable work carrier, including
an event log where the execution binding requires one; assemble prompts
from admitted work law instead of from raw user phrasing; and evaluate
closure against the same admitted criteria. The intended loop: work
arrives; the system selects the smallest lawful work carrier for its
required lifetime (§5); an agent drafts one run-scoped execution contract
from that carrier; the system validates and admits or rejects the contract
(ACTIVATION §1, Admission); execution may proceed in the same invocation
under the admitted contract; closure is checked against that same contract;
the resulting state still flows through normal proof, gap analysis and
repricing (P6, P2).

### Milestones and phase-scoped truth (UP-006)

A ticket may contain several closure-bearing milestones without becoming
several tickets. Each milestone has stable identity, a bounded claim,
relevant dependencies, current state, required evidence, and an explicit
relation to ticket closure (P3).

Milestone acceptance proves only its declared claim. Accepted design does
not satisfy implementation, installed proof, qualification or release.
Ticket completion requires every closure-bearing milestone to be accepted;
optional or deferred work requires an explicit disposition and owner. Each
milestone is a work claim under §7 Condition-based closure and reuse, so
its acceptance follows that condition for its own declared claim, and a
ticket is complete only when the condition holds for each of them.
Commentary and generated summaries cannot mutate milestone or ticket truth
(P6, P4b).

## 2. Layout and authority

### Default layout

The starter file layout (P2, P3):

```text
stdo_default.json

specification/
├── GOALS.md

.ai-workspace/
├── sprints/
├── tickets/
│   ├── backlog/
│   ├── active/
│   └── completed/
└── comments/
    └── <agent-id>/
```

The applicable product definition resolves POSTING_GUIDE and this member
from its exact shared installed basis (PRODUCT_DEFINITION §4); their
absence from the project tree is not absence from the governing method. A
conforming `stdo_<label>.json` definition may bind the same ticket, comment
and sprint roles to existing directories, repository resources, tracker
collections, API endpoints or product-scoped queries without restructuring
the project (PRODUCT_DEFINITION §1).

### Bindings and projections

The bindings (P6, P3): `ticketing.goals` locates the epic
layer; `ticketing.sprints.root`, when present, is the bounded
execution-batch and sprint-close review layer;
`ticketing.tickets.lanes.backlog`, `.active` and `.completed` locate the
ticket authority; `ticketing.comments.root` locates the discussion and
publication layer. The paths of the default layout are the bindings
supplied by `stdo_default.json`. The definition locates these carriers and
does not own their ticket or comment content.

There is no separate mandatory `ACTIVE_TASKS.md` in this model. A project
that wants a board view may generate one from the bound ticket authority;
that board is a projection only and does not become the source of truth
unless the product definition explicitly rebinds the ticket authority to
that carrier and no rival remains (§7).

### Carrier substitution

The durable local-file model is the default and remains valid whenever it
is selected. Another carrier is not required to reproduce its folders, but
it preserves the same ticket authority and refusal laws (§3 and §4, one
durable record). Growth the model admits includes a generated active board,
ticket dependency checks, links from tickets to scenario, requirement or
ADR surfaces, external sync with a real ticketing system, and message-board
integration through a standard tool-protocol capability. Under the bindings
above, a generated board is a projection, and a tracker that holds tickets
is lawful only as an explicit rebinding of the ticket authority by the
product definition with no rival surface remaining, so neither growth
changes the authority or refusal laws (P2, P6).

## 3. Sprint rules

### One durable record per sprint

Each sprint has one durable manifest record; the default carrier is one
markdown file. Another bound carrier preserves the same identity, required
fields, history, closure law and one-truth relation (P3, P4b). For a local file, the filename should
carry a stable id and a short slug. Recommended local-file naming:
`SPRINT-2026-04-30-process-navigator.md` and
`SPRINT-2026-05-12-dashboard-density.md`.

### Manifest fields

Each sprint manifest records at least `id`, `title`, `status`, `goal`,
`opened_at`, `updated_at`, `authority_refs`, `scope`, `excluded_boundaries`,
`expected_change_classes`, `included_tickets` or `iterations`,
`closure_trigger`, `closure_law`, `proof_surface`, `deferred_compliance`,
`non_closure_conditions` and `paydown_policy` (P4b, P2).

`authority_refs` names the upstream goals, intent, product, requirement,
design or other governing surfaces the sprint operates under.
`excluded_boundaries` names what the sprint is not allowed to change;
typical exclusions are product truth, data contracts, runtime semantics,
governance and closure law, public carrier shape and release criteria.
`deferred_compliance` names any local proof, review, accessibility,
screenshot, walkthrough, test, design wording or trace cleanup
intentionally deferred until sprint close. `paydown_policy` states how
deferred debt becomes accepted, ticketed, repriced or removed during close
review (P6).

### Sprint status

The minimum sprint status model is `active`, `closing`, `closed` and
`superseded` (P5, P3). `active`: iteration is admitted
inside the sprint boundary. `closing`: new iteration is frozen while close
review and paydown classification run. `closed`: close review finished and
all remaining debt is accepted, ticketed, repriced or removed.
`superseded`: the sprint boundary was wrong and a new authority surface,
sprint or ticket set replaced it. A project may add `planned` or
`cancelled`; those states do not replace close review.

### Sprint admission

A sprint may admit work only when the manifest makes the boundary
reviewable. Admission requires a bounded scope, cited authority, expected
change classes, explicit excluded boundaries, a closure law, non-closure
conditions, and a paydown policy for deferred compliance (P6, P2).

The sprint may batch repeated closure criteria that would otherwise be
copied into every included ticket. It may not batch away intake triage:
substantive included tickets still record their lawful `change_class` and
`re_entry_point` (§4, Triage metadata). Manifest-local iteration entries
may rely on the sprint's declared class only while they remain inside the
sprint scope and excluded boundaries (P4b).

### Compliance escrow

A sprint may defer local compliance proof only when the manifest names the
deferred proof or cleanup class; the debt is local to the sprint's admitted
surface; the expected correction cost is lower than the per-change proof
cost; the sprint is short enough that the debt remains reviewable; and the
close review classifies and pays down the debt. Deferred compliance is not
silent debt: it is escrow held by the sprint, and
[SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) states that
escrow satisfies no method, release or product closure until paid down,
accepted or repriced (P2, P4b, P6).

The following may be eligible for escrow when the governing method allows
it: screenshots or
walkthrough capture; visual review; accessibility cleanup; replay proof for
product-meaningful user-interface interactions; design wording cleanup; trace cleanup;
local realisation cleanup. The following may not be hidden in escrow: new
product truth; new
or changed data contracts; new runtime, governance, closure, provenance or
evidence semantics; missing constructive carriers; changed public
published-function or public carrier contracts; law-changing work that
needs `goal_reprice`, `intent_reprice`, `product_reprice`,
`requirement_reprice` or `design_reframe`. If one of those appears during
the sprint, the sprint records the finding and the work exits the sprint
path through a standalone ticket, a repricing action or sprint supersession
(P6).

### Close review

Sprint close begins by moving the manifest to `status: closing`. While
closing: new iteration inside that sprint is frozen; every included ticket
or iteration entry is reviewed against the manifest; accumulated evidence
is checked for durability; changed surfaces are walked against cited
authority; deferred compliance is classified; paydown tickets are opened
where debt must survive past the close review (P6, P4b).

Each reviewed item is classified as one of `accepted` (compliant under the
sprint authority), `local_paydown` (local debt remains and is captured by a
paydown ticket), `design_reframe` (the work needs design repricing),
`requirement_reprice` (the work needs requirement repricing),
`product_reprice` (the work changes product definition) or `remove` (the
work should be backed out or kept out of closure) (P5). A sprint may move to
`closed` only when every item and every debt entry is classified and the
resulting paydown or repricing work is durable. Sprint close can accept
local paydown debt only when the governing method allows that debt to
survive as explicit follow-up; it cannot accept hidden authority drift
(P6).

Close classifications and the core. A close classification is the
outcome of close review for one reviewed item, made against the sprint
authority the manifest cites; the close review must classify, under that
authority. The classification uses
[ACTIVATION §3 Disposition](ACTIVATION.md#disposition) only for its
result mapping: the candidate is the reviewed item, its boundary is the
sprint's close under the cited authority, and the classification consumes
the core results of the item's review and stays separate from them, as
acceptance stays separate from assessment
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results)). Each classification
takes exactly one core value, for the predicate "the reviewed item is
accepted as compliant under the sprint authority", and the table names
the disposition whose condition it matches, where one does (P5, P6):

| Classification | Matching disposition | Core value | Ground, and how it narrows or differs from the disposition's condition |
|---|---|---|---|
| `accepted` | `accept` | satisfied | the item is compliant under the sprint authority |
| `local_paydown` | `local_repair` | falsified | local debt remains and is captured by a paydown ticket; the debt is the counterexample. The governing relation stays coherent, because an item whose governing authority must change takes a repricing classification instead. It differs from `local_repair` in where the repair is carried: by the paydown ticket, which survives the close where the method allows that debt to survive |
| `design_reframe` | `re_enter` | invalid_basis | the accepted design that governs the item must change, so the authority the sprint cites cannot support accepting it |
| `requirement_reprice` | `re_enter` | invalid_basis | a governing requirement must change, with the same consequence |
| `product_reprice` | `re_enter` | invalid_basis | the work changes the product definition, which the authority the sprint cites cannot support |
| `remove` | none | falsified | the work is backed out or kept out of closure; the reason for removal is the counterexample. No disposition of ACTIVATION §3 has this condition, because removal does not require a violated governing relation or a competing truth path |

The layer that `design_reframe`, `requirement_reprice` and
`product_reprice` name is a declared fact, not a further result: it is
the change class of [SPEC_METHOD §4](SPEC_METHOD.md#change-classes) at
which the work re-enters, and it travels with the core value as the
domain outcome (FOUNDATIONS §4 Results, Recording). The outcome of a
debt entry, accepted, ticketed, repriced or removed (Sprint status,
`closed`), is likewise classified by the close review and mapped at the
close boundary, for the predicate "the debt entry is accepted under the
sprint authority": accepted matches `accept` (`satisfied`), ticketed
matches `local_repair` (`falsified`), removed takes `falsified` with no
matching disposition, and repriced matches `re_enter`
(`invalid_basis`), on the grounds of `accepted`, `local_paydown`,
`remove` and the repricing classifications respectively. The mappings
add no disposition and no core value. The condition for `closed`
above requires an outcome for every item and debt entry, not a
`satisfied` one. 
Purpose and material relation: a consumer that combines close outcomes
with other results cannot read remaining debt, needed repricing or
removal as compliance (P5, P6).

## 4. Ticket rules

### One durable record per ticket

Each ticket has one durable authoritative record; the default carrier is
one markdown file. A repository or external tracker carrier is lawful only
when it preserves the required ticket contract, history, state transition,
stable identity, searchability and closure semantics without a co-equal
local copy (P3, P4b). For a local
file, the filename should carry a stable id and a short slug. Recommended
local-file naming:
`T-001-add-product-layer.md`, `B-002-fix-reset-manifest-id.md`,
`S-003-evaluate-integration-capability.md`,
`C-004-clean-up-trace-tags.md`.

### Multi-build-tenant independence

This clause consumes the build-tenancy bounded context
`urn:stdo:bounded-context:build-tenancy` declared by PRODUCT_DEFINITION §8.
This member owns the multi-build-tenant work-item and ticket-lifecycle
relation inside that context; it does not redefine build-tenant identity or
realisation meaning (P3, P1).

A multi-build-tenant work item is one admitted upstream work item with more
than one build-tenant execution line. The upstream authority and each
tenant-local ticket retain distinct identities and lifecycles. If one
source, product or design work item must be realised in more than one build
tenant, its tenant realisations are not tracked inside one ticket
lifecycle. The rule governs backlog and active tickets; it is not
retroactive for completed tickets unless a completed ticket is reopened or
explicitly repriced. It does not make every ticket multi-tenant: tenant
duplication is used only when the same admitted work item genuinely has
more than one tenant execution line (P3).

The three lawful cases: an upstream-only ticket (source, product or design
authority only; no tenant duplicate yet); a single-tenant ticket (one
tenant-local execution line; no sibling duplicate required); a multi-tenant
work item (one upstream authority ticket and one suffixed tenant-local
ticket per tenant execution line). For the multi-tenant case: keep the
upstream source, product or design ticket as its own authority surface;
duplicate the work item into one tenant-local ticket per build tenant;
append a build-tenant mnemonic to the base ticket id and filename; keep
status, proof, closure and reopen logic independent for each tenant.
Recommended examples: `B-030-publish-capability-profile...` as the
source ticket,
`B-030-T1-publish-capability-profile...` and
`B-030-T2-publish-capability-profile...` as the tenant tickets.

The law: one ticket does not claim closure for more than one build-tenant
lifecycle; a tenant-local blocker or false closure in one tenant is not
hidden by green status in another; tenant-local proof, repricing and
reopening remain tenant-local (P3, P6). If a tenant-local duplicate
exists, it should record `source_ticket` and `build_tenant`. The
`build_tenant` value identifies the
applicable entry in the product's `how.build_tenants` definition; a path
name, display alias or tracker label does not replace that identity unless
the product definition binds it as the identity. The unsuffixed base ticket
may remain the upstream product or design authority. If the work item is
multi-tenant, tenant execution and closure for backlog and active work live
on the suffixed duplicates; if it is single-tenant, no sibling duplicate is
required.

### Required fields

Each ticket records at least `id`, `title`, `type`, `ticket_category`,
`status`, `goal`, `change_intent`, `change_class`, `re_entry_point`,
`triaged_at`, `created_at` and `updated_at` (P4b, P3). Recommended additional fields: `priority`,
`dependencies`, `links`, `intake_source`, `affected_boundary`,
`source_ticket` when the ticket duplicates or derives from another ticket,
and `build_tenant` when the ticket is tenant-local.

For `ticket_category: implementation_migration` the ticket also carries
`migration_strategy` and `library_usage`; `governing_library` when
`library_usage` is `consume` or `extend`; and `library_rationale` when
`library_usage` is `none` (§6). A tenant-local implementation migration
also carries `build_tenant`, and `source_ticket` when it duplicates or
derives from an upstream source, product or design ticket.

For execution-contract admission the runtime-drafted contract should also
carry, at minimum, `target_truth`, `superseded_truth` when relevant,
`closure_law`, `evaluation_criteria`, `non_closure_conditions` and
`proof_surface` (§5).

### Types

The minimum common set of ticket types is `feature`, `bug`, `spike` and
`chore`. A project may add more; the default set should be enough for
most cases
(P3).

### Category

Ticket category is orthogonal to ticket type: type answers what kind of
work record this is; category answers what execution or migration
discipline governs the ticket (P3, P1). The minimum
common set is `ordinary` and `implementation_migration`, so a `feature`,
`bug`, `spike` or `chore` may carry either. `implementation_migration` is
used when the ticket is not "change code until tests pass" but a governed
replacement of one implementation truth path with another across producers,
consumers, projections and proof surfaces: a bug ticket that replaces an old
tracker or read-model family with one new authoritative carrier; a feature
ticket that introduces a new public interface and requires every producer
and consumer to migrate before closure; a refactor ticket that removes a
bridge path or compatibility facade from an authoritative contract family.

### Inside-out sequencing

For `ticket_category: implementation_migration`, ticket sequencing reflects
the inside-out rule of
[SPEC_METHOD §7](SPEC_METHOD.md#inside-out-first-sequencing) (P4b, P6). Tickets that publish or admit
the new authoritative source carrier are the upstream tickets in the wave.
Tickets that harden prompt assembly, projections, reports, dossiers, review
surfaces or other downstream consumers depend on those upstream source
tickets. A downstream ticket may carry exploratory work while the source
ticket is active, but that work is non-closure evidence until the source
carrier is admitted and authoritative. A downstream ticket does not close
while its upstream source-carrier ticket remains open. When one migration
wave introduces a new source carrier and then its prompt, projection or
read-model consumers, the dependency chain runs `source carrier ->
downstream consumers`, never the reverse.

### Change class

Ticket type and change class are orthogonal: type answers what kind of
work record this is; change class answers where the change lawfully
re-enters the constitutional chain. A ticket records the `change_class`
declared by intake triage, using the classes of
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes) (P4b, P2).

Common pairings: `feature` with `goal_reprice`, `intent_reprice`,
`product_reprice`, `requirement_reprice` or `design_reframe`; `bug` with
`requirement_reprice`, `design_reframe` or `realization_refactor`; `chore`
with `design_reframe` or `realization_refactor`; `spike` as exploratory
work that still carries the current triage class and should terminate
either in a more specific downstream ticket or in an explicit decision
that no further substantive change is required.

Ticket category and change class are also orthogonal: `change_class`
governs lawful constitutional re-entry; `ticket_category` governs ticket
execution and closure discipline. A ticket may therefore be `type: bug`,
`ticket_category: implementation_migration`, `change_class: design_reframe`
without contradiction (P3).

### Upward propagation check

Triage consumes the computed classification of
[SPEC_METHOD §4](SPEC_METHOD.md#computed-classification-and-treatment) for
the declared owner and layer traversal, the complete relevant public
membership and value delta, the accepted-design scope and trace coverage,
and the rule-determined treatment. The owning work carrier references that
exact result and its residuals; a new role does not repeat an unchanged
walk (P4b, P2).

Before declaring `realization_refactor` for a bug, establish that the
current requirement and the accepted realising design govern the affected
behaviour and remain sufficient for the authorised outcome. Their presence
proves no coverage. Missing or ambiguous evidence leaves the affected
treatment unknown; it is not proof that the governing layer itself is
absent (P6).

The re-entry rule is SPEC_METHOD §4's: the
[change classes](SPEC_METHOD.md#change-classes) with their re-entry
points, and the smallest lawful re-entry that step 4 of
[Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment)
exposes, with the paragraph after the four steps: a candidate's public
violation does not select a new contract, and the governing owner is
re-entered only for an explicitly changed desired outcome or an
established governing insufficiency. For a bug, this check
refines that rule into an upward walk from the realised surface that
checks each layer and stops at the highest layer found missing or
insufficient for the authorised outcome, and the class is the one that
re-enters there:

| Where the walk stops | Change class | Action |
|---|---|---|
| the governing requirement is missing or insufficient | `requirement_reprice` | re-enter the requirement's owner |
| the requirement is sufficient, and the realising design is missing or insufficient | `design_reframe` | re-enter Design |
| an actual upstream Goal, Intent or Product change | `goal_reprice`, `intent_reprice` or `product_reprice` | follow the change to its owner rather than stopping at a familiar file |
| the current requirement and accepted design suffice, and the implementation deviates | `realization_refactor` | repair or reject the candidate |

Unresolved meaning remains J and a reserved choice remains O, as that
paragraph states (P2, P6).

### Triage metadata

Because tickets are the durable authority surface for work tracking, a
ticket for substantive work carries the minimum metadata required by the
intake triage of [SPEC_METHOD §4](SPEC_METHOD.md#universal-intake-triage):
the declared `change_intent`, the lawful `change_class`, the lawful
`re_entry_point`, and when triage occurred in `triaged_at` (P4b, P2). The recorded values are those intake triage declared
(Change class and Upward propagation check above).

### Status

The minimum ticket status model is `backlog`, `active` and `completed`. A
project may add `blocked`, `cancelled` or other explicit local states; the
base method starts with the three (P5, P3).

The ticket statuses, any local state a project adds, the lanes below, the
sprint statuses of §3 and the `migration_strategy` and `library_usage`
values of §6 are declared states of their carriers, not results, and map
to no core value; the recorded `change_class` is a declared state under
[SPEC_METHOD §4](SPEC_METHOD.md#change-classes). The close
classifications and debt-entry outcomes of §3
Close review are results, mapped there. An evaluation that reads a
declared state returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a declared state is never combined as an evaluation result, so
a ticket marked `completed`, or a sprint marked `closed`, cannot stand in
for a `satisfied` result (P5, P1).

### Review findings and bug items

When findings from a review need a durable work carrier, record one linked bug
report for that review, with one entry per finding: stable identity, original
Reviewer severity and triage, exact subject/basis, violated claim, location and
chaseable evidence. Link it to the work item that issued the review. With no
findings, create no bug report. A sufficient existing direct-work carrier may
carry the same relations without a redundant ticket (P3, P2).

The Reviewer may record this report only when its activation grants the exact
artifact identity/path and effects. Otherwise it returns the findings and a
lawful Writer records them. Recording creates no repair, priority, admission or
closure authority. Keep the report within its evidence/read and visibility
restrictions: findings derived from a withheld capture are withheld from the
same recipients, including any report projection that reveals them. The
Product may bind a recognizable report naming pattern and exclusion route to
its actual access mechanism; a filename or separate lane alone enforces
nothing and grants no additional read (P6).

After Executive or other authorized decision-owner triage, the reviewed work
item carries a linked Bug items section. Each item records its identity,
original severity, assigned priority and reason, cause group, responsible owner,
source report/finding, disposition and state. The report remains the technical
finding source; the item is the decision and repair ledger. An actor/session
index, where used, points the Reviewer to its report and the triage/repair work
to the reviewed work item's ledger, rather than duplicating that truth (P3).

| Item state | Required trace |
|---|---|
| open | Finding and triage/disposition, with unresolved work named. |
| fixed | Exact repaired subject (commit or equivalent immutable identity) and repair evidence; not yet a claim of verification. |
| verified | The satisfied repair predicate and exact evidence; identify tests and, when required, the independent recheck/report. Tests alone are not labelled independent review. |

These are carrier states, not core evaluation results or acceptance. A required
recheck keeps its affected items unverified until the required result is
available and applicable. A test-verified fix needs no invented Reviewer when
the governing basis requires none; the optional Executive cadence is
[EXECUTIVE_BASELINE §12](EXECUTIVE_BASELINE.md#qa-cadence-and-repair-rechecks).
Retained or deferred findings stay linked until their selected boundary, or
transfer with owner, disposition and destination when the work item closes.
Changing priority does not erase the original severity or the obligation (P6,
P4b).

### Lanes

Backlog tickets live at the product definition's
`ticketing.tickets.lanes.backlog` binding, by default
`.ai-workspace/tickets/backlog/`; active tickets at
`ticketing.tickets.lanes.active`, by default `.ai-workspace/tickets/active/`;
completed tickets move to `ticketing.tickets.lanes.completed`, by default
`.ai-workspace/tickets/completed/` (P0, P3). `backlog`
is accepted durable work that should remain visible but is not part of the
current execution focus; `active` is the current bounded execution set;
`completed` is closed work retained as history. The lanes keep the live
execution set small enough that `rg` remains fast and readable without
forcing deferred work into comments or goals.

## 5. From carrier to execution

If a derived surface or projected frame of this member is insufficient,
the actor reads this member only for the named unresolved lifecycle or
proof question and cites the clauses used (P2, P6; prompt construction is
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope)).

Before the derivation table, the deciding routes are
[Carrier selection](#carrier-selection) for the work record and its lifetime;
[Execution contract admission](#execution-contract-admission) for execution;
[Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity)
for reusable judgments and repricing; and
[Condition-based closure and reuse](#condition-based-closure-and-reuse) for
completion. The table traces these owners; it does not decide their questions.

### Foundation to law: work carriers

This family (F13 in the index of
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law))
decides which record carries a piece of work, what that record may claim
and when the work closes. Its instance premises, which the commitments do
not supply, are named in the rows as follows: lifetimes, work and its
obligations last one run, one bounded batch or longer; several surfaces,
goals, tickets, comments, boards and summaries can each appear to state
the same work state; several tenants, one work item may be realised in
more than one build tenant; migrations, some work replaces one
authoritative truth path with another across producers, consumers and
proofs; carriers vary, a project may keep its carriers in files, trackers
or services. Each commitment's standing is written as the table of
commitments in FOUNDATIONS §3 states it.

| Premises, with standing | Consequence that follows | Rule in this member that states it | Added domain or policy choice, and its owner | Pillar |
|---|---|---|---|---|
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P2 (independent); P6 (independent); P0 (recovered); instance: lifetimes | By P0 an actor's context does not outlive its run, and by P4b a step-produced fact that is not recorded is lost, so an obligation that must outlive the run is recorded on a carrier whose lifetime covers it before the run returns. By P2 nothing is added that the outcome does not need, so every execution runs under one run-scoped contract drawn from the smallest such carrier (an admitted ticket, a sprint entry or the run itself), and a durable ticket is created only for state that must survive; by P6 creating one needs ticket-state authority. | [Carrier selection](#carrier-selection); §1 [Goals](#goals), [Ticket records](#ticket-records), [Execution contracts](#execution-contracts) | the carrier kinds and the selection table, which apply this order to named lifetimes: a policy of this member; where each carrier lives: the product definition ([PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers)) | 1, 8, 9 |
| P6 (independent); P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); instance: lifetimes | By P6 work needs an admitted authority, and a record's presence or prose creates none, so work executes only under admitted upstream work authority, and a carrier's presence, lane, status or prose is neither the admission of a contract nor the admission of a growth basis. By P3 execution and closure bind one exact basis, so both read the same admitted contract, which shows what counts as completion and what still counts as failure. | [Carrier selection](#carrier-selection); [Execution contract admission](#execution-contract-admission); [Evaluation criteria and non-closure conditions](#evaluation-criteria-and-non-closure-conditions) | the contract's minimum fields: this member; the admission mechanism and the result and evidence surface: the product definition. The step side of admission is law at [ACTIVATION §1](ACTIVATION.md#admission), not a choice | 1, 8, 9 |
| P6 (independent); P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P2 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P0 (recovered); instance: several surfaces, carriers vary | By P3 one state binds one authority and basis, and by P6 a projection is not authority, so work state has one authority chain: goals own the work wave, the ticket owns its state and milestone authority its milestones, and a board, comment, index or summary is a projection that answers one question. By P5 contradictory authorities cannot both be read as satisfied, so contradiction among them blocks closure; by P4b a milestone's acceptance establishes only its own claim. A comment is a post: provisional until its content is adopted into the owning surface, with its own discussion state. Another carrier is lawful only as an explicit rebinding with no rival left. | [One-truth state projection and drift refusal (UP-009)](#one-truth-state-projection-and-drift-refusal-up-009); §1 [Comments](#comments), [Milestones and phase-scoped truth (UP-006)](#milestones-and-phase-scoped-truth-up-006); §2 [Default layout](#default-layout), [Bindings and projections](#bindings-and-projections), [Carrier substitution](#carrier-substitution); §4 [Status](#status), [Lanes](#lanes); §9 [Relationship to other surfaces](#relationship-to-other-surfaces); [POSTING_GUIDE §2](POSTING_GUIDE.md#2-boundary), [§7](POSTING_GUIDE.md#7-discussion-state-and-mutability), [§9](POSTING_GUIDE.md#9-ratification) | the default layout, the lanes and the minimum status sets: domain choices of this member, which a project may extend; a rebinding of ticket authority: the product definition; the post categories, structure and discussion states: [POSTING_GUIDE](POSTING_GUIDE.md) | 1, 6, 9 |
| P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P3 (independent); instance: lifetimes | By P2 closure law repeated over one bounded scope can be applied once, so a sprint batches it; by P4b a deferred proof persists until paid, and by P6 closure needs its evidence, so a sprint defers only declared local proof, as escrow paid down at close review, and never batches away triage. Law-changing work re-enters at its own layer (P2), so it leaves the sprint. By P5 each close outcome is a result, so the sprint closes only when the close review has classified every item and debt entry, each classification mapped into the core, and the follow-up work is durable. | [§3](#3-sprint-rules); §1 [Sprints](#sprints) | the manifest fields, the sprint statuses, the escrow lists and the six close classifications and the debt outcomes with their mappings: domain choices of this member; whether debt may survive as follow-up: the governing method; the decision to offer a sprint as a batching carrier at all: a policy of this member | 1, 3, 9 |
| P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P2 (independent); P6 (independent); P3 (independent); P1 (independent) | By P4b the reason a ticket exists must survive the run, so a ticket records the triage that admitted it: change intent, change class and re-entry point. By P2 work re-enters where the authorised outcome is unmet, and by P1 a familiar file carries no authority, so the upward walk checks each layer and re-enters at the highest layer found missing or insufficient, never at a familiar file. | §4 [Required fields](#required-fields), [Types](#types), [Category](#category), [Change class](#change-class), [Upward propagation check](#upward-propagation-check), [Triage metadata](#triage-metadata), [One durable record per ticket](#one-durable-record-per-ticket) | the required fields and the minimum types and categories: domain choices of this member, which a project may extend; the change classes: domain choices of [SPEC_METHOD §4](SPEC_METHOD.md#4-change-management) | 1, 9 |
| P3 (independent); P6 (independent); P1 (independent); instance: several tenants | By P3 a lifecycle binds one exact subject, and each build tenant realises a separate subject, so one ticket closes at most one build-tenant lifecycle, and proof, closure, repricing and reopening stay tenant-local. By P6 one subject's evidence decides nothing for another, so one tenant's green status hides no other tenant's blocker. | §4 [Multi-build-tenant independence](#multi-build-tenant-independence); §6 [Multi-build-tenant review](#multi-build-tenant-review) | the suffixed ticket identifier and the `source_ticket` and `build_tenant` fields: domain choices of this member; tenant identity: the product definition's tenant registry | 1, 8, 9 |
| P6 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P3 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P2 (independent); P4a (independent); P1 (independent); instance: migrations | By P6 two truth paths cannot both hold authority over one scope, and by P5 an absence is shown only by evidence, so a migration ticket closes only when the old truth path no longer holds authority in its declared scope, shown by negative or structural proof. By P1 a proxy or wrapper that imitates the new path is not it, so mixed state, proxies, wrappers and green tests alone do not count; by P4a a downstream path depends on its source, so a downstream ticket does not close while its source-carrier ticket is open. By P2 each further local rebuild adds cost with no new route to the outcome, and by P3 similar code does not establish one identity, so a credible recurrence forces an explicit library or commonisation review, never an automatic merge. | §6 [Declaration and checklist](#declaration-and-checklist), [Closure of a migration ticket](#closure-of-a-migration-ticket), [Strategy requirements](#strategy-requirements), [Recurring realisation and library declaration](#recurring-realisation-and-library-declaration), [Review disambiguation](#review-disambiguation), [Impacted interface review checklist](#impacted-interface-review-checklist), [Break order and break-to-closure map](#break-order-and-break-to-closure-map), [Mixed-state negative proof](#mixed-state-negative-proof); §4 [Inside-out sequencing](#inside-out-sequencing) | the declaration, the checklist, the strategy and library values, the recurrence thresholds, the review questions and the break order: domain choices of this member. The migration law is [SPEC_METHOD §7](SPEC_METHOD.md#7-migration), not a choice | 4, 9 |
| P6 (independent); P1 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P5 (derived from P0 and P6, with P0's open-world premise); P0 (recovered); P2 (independent); P3 (independent) | By P6 authority to author is not independent authority to verify. By P1 and P3 a verdict means only the claim it binds, so a review verdict is bounded by its claim and traceable to it. By P0 and P4b a judgment or ruling must survive a change of actor, so it is recorded once, in its original terms, and reused while it applies; by P5 changed evidence invalidates what it affects. | §7 [Execution and verification authority separation (UP-007)](#execution-and-verification-authority-separation-up-007), [Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity) | the four repricing dispositions and the predicate and refinement for a material repricing decision: this member. The assessment protocol and the reuse law are [EVALUATION §3](EVALUATION.md#3-independent-assessment) and [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse), not choices | 7, 9 |
| P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise); P2 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable) | By P5 a claim is satisfied only by valid evidence for each obligation, under the conjunction of FOUNDATIONS §4, so a work claim is complete only when every applicable obligation is satisfied and no non-closure condition remains. By P6 review evaluates and does not decide, so its occurrence is not the closing event; by P6 a test's expected result needs work authority, so it comes from admitted work authority, never from the implementation. | §7 [Condition-based closure and reuse](#condition-based-closure-and-reuse), [Test case authority](#test-case-authority) | the five-step reconciliation order: this member. The conjunction and the general test law are [FOUNDATIONS §4](FOUNDATIONS.md#conjunction-of-results) and [ASSURANCE §3](ASSURANCE.md#3-test-authority), not choices | 3, 9 |
| P1 (independent); P3 (independent); P6 (independent); P5 (derived from P0 and P6, with P0's open-world premise) | By P1 a term's spelling carries no meaning, and by P3 it resolves under one context and basis, so a ticket's terms resolve under the project's semantic resolution. By P5 an unresolved or multiply resolved material term leaves the claim undecided, so it blocks admission and closure of the affected claim until its owner resolves it. | [Bounded-context term binding](#bounded-context-term-binding) | none here: the resolution law is [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution) | 2, 6 |
| P2 (independent); P6 (independent); P3 (independent); P4b (derived from P0 and P2, with P0's premise that step-produced facts are not re-acquirable); P0 (recovered); instance: carriers vary | By P2 the method fixes only what the outcome needs, so any carrier shape that keeps the required fields and sections is lawful. By P0 an actor holds only bounded context, so it reads this member only for the question a derived surface leaves open. | [§8](#8-recommended-shapes); §9 [Operating mode](#operating-mode); the opening paragraph of this section | the three recommended shapes, the default local-file carrier and its search commands: domain choices of this member; a policy of this member: an actor reads this member only for the question a derived surface leaves open, applying ACTIVATION §2 Acquisition | 1, 6 |

The standing of these consequences is stated in
[FOUNDATIONS §3 Foundation to law](FOUNDATIONS.md#foundation-to-law).
The table accounts for §1 to §9, and for POSTING_GUIDE §2, §7 and §9,
which have no family table of their own.

Consumers of these rows, where an actor enters them (FOUNDATIONS §3
Foundation to law, Consumers), one list per row, each consumer linked to
its own locus:

- Row 1, the carrier for a lifetime: [SPEC_METHOD §4 Carriers](SPEC_METHOD.md#carriers), which selects a change's carrier for its required lifetime and takes the smallest lawful carrier from Carrier selection; [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), which binds where each carrier kind lives and selects none; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 41, where a proposed change to work carriers is judged under Carrier selection; [Recorded judgment and owner-ruling continuity](#recorded-judgment-and-owner-ruling-continuity), whose record lives in the carrier selected under §5.
- Row 2, execution under admitted authority: [ACTIVATION §1 Admission](ACTIVATION.md#admission), where a contract carries the states this section names and a carrier's presence, lane or label is never admission; the [ODD family table](ODD.md#foundation-to-law), whose row for the manual walkthrough imports F13 for admission against deterministic criteria.
- Row 3, one authority chain and its projections: [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), whose `ticketing` bindings locate the carriers and keep the work wave with goals, ticket state with the ticket and commentary outside authority; [§8](#8-recommended-shapes), where another shape is bound under §2 only with the same fields.
- Row 4, sprints as batches: [SPEC_METHOD §4 Sprint execution boundary](SPEC_METHOD.md#sprint-execution-boundary), whose close review takes its mechanics, escrow and classifications from §3, and [Change classes](SPEC_METHOD.md#change-classes), where a close classification that names a layer is a result mapped at §3 and carries the class at which the work re-enters; [UX §12 UX sprint compliance escrow](UX.md#ux-sprint-compliance-escrow), where each finding takes one of the six close classifications, [UX §15](UX.md#15-results-of-this-profile), which maps none of them again, and the [UX family table](UX.md#foundation-to-law), whose row for scaffold, exemption and escrow imports F13; [CONFORMANCE §5](CONFORMANCE.md#5-discriminator-coverage), discriminator 48, where a sprint status or classification decides no admission, compliance or closure; [Status](#status), where the sprint statuses are declared states and the close classifications are results mapped at §3; [Condition-based closure and reuse](#condition-based-closure-and-reuse), where sprint-close law still applies to a result recorded without review; [§8](#8-recommended-shapes), whose sprint manifest carries the fields of §3.
- Row 5, the triage a ticket records and the upward walk: [SPEC_METHOD §4 Change classes](SPEC_METHOD.md#change-classes), which has the class recorded on the carrier under §4 Change class; [Sprint admission](#sprint-admission), whose included tickets still record their triage metadata; [Carrier selection](#carrier-selection), whose ticket-shaped contract carries the required fields of §4; [§8](#8-recommended-shapes), whose ordinary ticket carries the required fields and triage metadata.
- Row 6, tenant-local lifecycles: [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding), Development of several tenants, where the independence of each tenant's ticket lifecycle and the review of its tickets are this section's; [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers), which names the multi-build-tenant work-item relation in the build-tenancy context and whose tenant registry supplies tenant identity.
- Row 7, migration tickets: [DESIGN_MODULE §10 Recurrence extraction](DESIGN_MODULE.md#recurrence-extraction), which refines the recurrence rule of Recurring realisation and library declaration as a design-review obligation for a Product that adopts that profile; [Status](#status), where `migration_strategy` and `library_usage` are declared states of their carriers; [§8](#8-recommended-shapes), whose migration ticket carries the declaration and checklist of §6.
- Row 8, authority to author, to verify and to rule: [EVALUATION §3](EVALUATION.md#3-independent-assessment), which takes from UP-007 the boundaries at which independent assessment is required and relabels no self-review in a fresh context; [EXECUTIVE_BASELINE §10](EXECUTIVE_BASELINE.md#10-derived-reviewer-frame), [§12 step 4](EXECUTIVE_BASELINE.md#4-executive-evaluates-the-work-result) and [§17](EXECUTIVE_BASELINE.md#17-actor-binding-and-independence), and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for the Reviewer imports F13 for when independent assessment is required; [SPEC_METHOD §4 Computed classification and treatment](SPEC_METHOD.md#computed-classification-and-treatment), where the recorded J and O continuity rules are Recorded judgment and owner-ruling continuity's; [Recurring realisation and library declaration](#recurring-realisation-and-library-declaration), where a repricing input blocks no bounded claim unless the owning authority admits the follow-up.
- Row 9, closure by condition and test authority: [SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate), which applies the closure condition as the gate over a change span and the ticket-local test-case rule to a code and test mismatch, and [§9](SPEC_METHOD.md#9-evidence), which names the evidence the condition requires for a realisation claim; [EXECUTIVE_BASELINE §22](EXECUTIVE_BASELINE.md#22-closure), where a work item closes by this condition, and the [EXECUTIVE_BASELINE family table](EXECUTIVE_BASELINE.md#foundation-to-law), whose row for qualification and closure imports F13 for the closure condition; [ASSURANCE §3](ASSURANCE.md#3-test-authority), where the derivation of each test case from admitted work authority is Test case authority's; [Milestones and phase-scoped truth (UP-006)](#milestones-and-phase-scoped-truth-up-006), where each milestone is a work claim under the closure condition.
- Row 10, term binding: no separate consumer applies. The resolution law a ticket's terms resolve under is [PRODUCT_DEFINITION §5](PRODUCT_DEFINITION.md#5-bounded-context-semantic-resolution)'s, as the choice column states; the block on admission and closure acts inside Execution contract admission and Condition-based closure and reuse of this member, and no section of another member names this binding.
- Row 11, carrier shape and reading this member: no separate consumer applies. A project's carrier layout is bound under [PRODUCT_DEFINITION §8](PRODUCT_DEFINITION.md#8-what-how-and-work-carriers) and scaffolded by [§12](PRODUCT_DEFINITION.md#12-bootstrap), which name their own defaults and not these shapes; the reading rule applies ACTIVATION §2 Acquisition, as the choice column states, and no other section applies it.

Each consumer applies the rule and decides nothing the owning section does
not (P2, P6).

The [Review findings and bug items](#review-findings-and-bug-items) refinement
applies the same P3/P4b identity and retained-obligation premises to findings
that outlive review. P6 keeps the assessment source, decision ledger and
artifact effects distinct, and P2 avoids an empty report or redundant ticket.
One report per finding-bearing review, the item fields and the three item
states are explicit carrier choices of §4. Verification still uses EVALUATION
and the applicable cadence rather than treating a state label as proof. The
consumers are EVALUATION §4's report effect, EXECUTIVE_BASELINE §5/§12's triage
and repair decisions, §7's closure and §8's ticket shape.

### Carrier selection

Every execution governed by this method uses one run-scoped execution
contract. The required lifetime of the work or obligation selects the
smallest lawful source carrier: first establish the applicable upstream
work authority, then select the first matching row below. For work inside
an admitted sprint the local carrier boundary is that sprint; otherwise it
is the current run (P2, P4b, P6).

| Condition | Execution-contract source | Durable-ticket decision |
|---|---|---|
| no applicable upstream work authority exists | no execution contract is admitted | do not create a ticket as substitute authority; stop or re-enter |
| applicable authority exists and an existing admitted ticket covers the exact work | derive the run-scoped contract from that ticket | reuse it; do not create another ticket |
| applicable authority exists, no exact admitted ticket covers the work, and the work or an open obligation needs independent state beyond the local carrier boundary | one durable ticket plus the run-scoped contract | create or update the ticket only under ticket-state authority |
| applicable authority exists, no exact admitted ticket covers the work, and the work stays inside one admitted sprint with no state required after sprint close | the sprint manifest plus one manifest-local iteration entry | do not create a durable ticket |
| applicable authority exists, no exact admitted ticket or sprint covers the work, and the work ends in the current run with no independent surviving state | an intake-drafted run-scoped contract | do not create a durable ticket |

"Ticket-shaped" describes the categorisation, closure criteria, proof
surface, non-closure conditions and the other required execution-contract
fields (§4, Required fields). It creates no durable ticket identity and no
ticket-lane state (P3).

Absence of a durable ticket neither requires nor authorises creating one.
An exact product-authorised work instruction may supply the upstream work
authority for a one-run contract; a generic request or a model-widened
scope cannot. A durable ticket is created or updated only when the table
requires surviving state and the actor holds ticket-state authority. An
explicit instruction from ticket-state authority to create a durable record
selects that durability; it does not admit an execution contract or widen
its upstream work authority (P6, P2).

The step side of admission is [ACTIVATION §1](ACTIVATION.md#admission) and
is defined there once: drafting versus admission inside one invocation, the
condition under which execution may begin, what admission may never be
inferred from (including ticket or sprint presence, lane placement and
`active` status), the coordinates an admitted result carries, the recording
of every result, withheld closure and residual obligation before return,
and refusal when no durable result and evidence surface is available. This
member adds the carrier side (P6, P4b). The admission mechanism and the
durable result and evidence surface are the ones the product definition
binds. When that surface is the ticket or the sprint manifest, the admitted
result with its coordinates is recorded there. A carrier's lane, status or
prose that asserts admission without those coordinates is not admission
evidence, and the contract it describes remains drafted or rejected.

When admission is absent or rejected, ACTIVATION §1 returns the missing
work authority without execution. Before that return, an obligation that
must survive the run is carried as follows (P4b, P6): it becomes a
sprint-local entry when its lifetime stays inside the admitted sprint;
otherwise it is recorded as a durable ticket, only under ticket-state
authority; where that authority is absent, it is retained in the
contract's named durable result and evidence surface or in an
already-authorised enclosing carrier, closure is marked withheld on
ticket-state authority, and the required re-entry is returned.

Execution and closure use the same admitted categorisation, criteria,
proof surface and non-closure conditions. The resulting state still flows
through proof, gap analysis and repricing (P6, P2).

The selected carrier is also the work reference for context construction and
continuation: bind its current question, subject and basis, result and evidence
references, and surviving obligations. Apply
[ACTIVATION §2](ACTIVATION.md#2-context-construction-under-an-envelope) to that
bounded acquisition, [§5](ACTIVATION.md#5-work-state-and-restart) to current
work state, the disposable actor account and resumption, and
[§7](ACTIVATION.md#7-closed-result-and-reuse) to closed results and reuse.
The ticket retains its [work-state authority](#one-truth-state-projection-and-drift-refusal-up-009);
an actor's account cannot replace the carrier, governing sources or current
evidence. Preserve results, step-produced facts and owner rulings through
the named result and evidence surface under existing admission and
[continuity](#recorded-judgment-and-owner-ruling-continuity) law. This applies
those owners to the selected carrier; it creates no additional carrier
requirement and confers no ticket-state authority (P0, P3, P4b, P6).

### Execution contract admission

The runtime execution flow should treat a ticket, a sprint entry or a
drafted work contract as an admission candidate, never as automatic truth;
the contract carries at minimum the states named in ACTIVATION §1
(drafted, admitted, rejected, superseded). An admitted execution contract
should be recorded on the selected durable work carrier, including an event log
where the execution binding requires one. It is available to prompt assembly
where applicable, and to later closure checking, so that execution and
closure read the same admitted basis. A binding that requires an event log
still requires that log; a human or mixed binding may select another durable
carrier under [SPEC_METHOD §11](SPEC_METHOD.md#11-build-tenant-binding)
(P6, P4b). The refusal of self-certification
is ACTIVATION §1.

Admission validates a contract against its cited product outcome,
prerequisite or experiment basis and does not admit that basis (ACTIVATION
§1). Admission or renewal of the basis belongs to the authority owning the
selected goals work wave, or its explicitly bounded proxy, and stays
durably legible in the existing goals or ticket authority
([SPEC_METHOD §3](SPEC_METHOD.md#3-outcome-conservation)). A ticket's
`active` status, its lane, or an admitted or retained contract is therefore
never the admission of a growth basis (P6, P2).

### Evaluation criteria and non-closure conditions

An execution contract should expose both what counts as progress or
completion and what still counts as failure even when some local proof is
green. At minimum it should make `evaluation_criteria` and
`non_closure_conditions` visible. These are the local gain function for
the work (P6, P2).

For implementation migrations, typical non-closure conditions are: the old
authoritative path still passes in normal execution within the declared
affected scope; mixed old and new proof is still accepted; a proxy or
partial interface implementation still stands in the acceptance path;
competing or ambiguous executable authority remains reachable on the
claimed product acceptance path; ticket wording, product wording and proof
wording are not reconciled. These conditions are not optional commentary;
they are the anti-self-deception surface for execution (P6).

Residual implementation debt outside the claimed acceptance path is not by
itself a non-closure condition. It may be deferred only under the
path-relative authority and explicit disposition rules of
[SPEC_METHOD §7](SPEC_METHOD.md#constitutional-migration-options) (P2).

### Bounded-context term binding

Ticket and work-instruction terms resolve under the bounded-context
semantic resolution of PRODUCT_DEFINITION §5. A ticket may use an
unqualified term when its cited product, re-entry surface, execution basis
and affected scope select exactly one bounded-context meaning (P1, P3).

When a ticket spans contexts, or a material term has competing meanings,
the ticket cites the applicable product-definition disambiguation or the
owner-authorised import, translation, equivalence or disambiguation
carrier; it may reference that relation rather than duplicate it. Ticket
prose, actor familiarity, a matching glossary heading, tenant placement or
comment context cannot select meaning or transfer authority (P1, P6).

An unresolved or multiply resolved material term blocks execution-contract
admission and closure for the affected claim. Opening or updating the
ticket records the pressure and does not cure it; resolution re-enters at
the authority that owns the missing context or semantic relation (P1, P5).

## 6. Implementation migration

### Declaration and checklist

A ticket with `ticket_category: implementation_migration` carries both an
explicit migration declaration block and a hard migration checklist. Both
are part of the ticket authority, not optional commentary.
[SPEC_METHOD §7](SPEC_METHOD.md#7-migration) defines the migration law;
this category defines the minimum ticket-local declaration and checklist
that a reviewer can check before accepting a closure claim on one concrete
work item, and is the local enforcement surface for the inside-out
migration law of SPEC_METHOD §7 (P6, P4b, P3).

The declaration states: the migration strategy used for this work item; the
exact affected migration scope; every explicitly excluded or disjoint
product or compatibility scope with its deterministic routing relation; the
old truth path or superseded contract; the new truth path or authoritative
contract; the producer set for the old and the new path; the consumer set
for the old and the new path; every projection, report, status surface and
proof surface derived from that contract family; and the closure law for
the migration.

The ticket carries at least this checklist in live markdown form:

```md
## Migration Checklist

- [ ] exact affected migration scope is named
- [ ] excluded or disjoint Product and compatibility scopes are named with deterministic routing
- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority within the affected scope
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] recurring realization patterns are checked against existing library/commonization surfaces
- [ ] ticket declares library usage and names the governing library or rationale
- [ ] if the work exists in more than one build tenant, this backlog/active ticket carries only one tenant lifecycle and any sibling tenant work lives on its own suffixed ticket
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```

Where no excluded or disjoint scope exists, the second item is satisfied by
declaring that absence explicitly, as the migration example of §8 writes
it; silence does not satisfy it (P6).

The required fields are `migration_strategy`, with the values
`inside_out_hard_break` and `fundamental_re_adoption`, and
`library_usage`, with the values `none`, `consume` and `extend`. When
`library_usage` is `consume` or `extend`, the ticket names the governing
reusable library or commonisation surface in `governing_library`. When it
is `none`, the ticket explains in `library_rationale` that no existing
reusable surface applies, or that the pattern is still boundary-specific,
or that it is not yet a lawful recurrence or commonisation candidate (P3,
P2).

### Closure of a migration ticket

Closure is blocked while the old authoritative interface still passes in
normal execution within the declared affected scope, unless the ticket
explicitly declares a retained compatibility feature. A deterministically
routed, non-overlapping product scope outside the declared affected scope
remains governed by its own current authority (P6, P3). Accordingly: the
old path may not remain silently authoritative within the affected scope;
mixed old and new green tests do not count as migration completion; any
retained old path within the affected scope is named as compatibility
rather than current native truth; retained compatibility is justified in
the ticket itself, never inferred from surviving code; proxy or partial
implementations do not satisfy migration closure; and if a ticket was
marked `completed` and later review shows checked closure items are false
on the current tree, the ticket is reopened or an explicitly linked
successor ticket is created, because a false closure claim is a
ticket-method defect, not only a code defect (P6, P4b).

An intermediate product-slice milestone inside an open migration ticket may
be accepted under the path-relative promotion rule of SPEC_METHOD §7, which
also states how the slice's identity and acceptance criteria derive and
that ticket wording cannot narrow that authority away. The ticket-local
consequence: the ticket remains active and does not claim migration
closure until the migration checklist and the final closure law are
satisfied; its `active` status renews none of the accepted slice's
exhausted growth authority; and removal, demotion and closure-proof work
may continue within the bound SPEC_METHOD §7 states, further material
producer or consumer growth requiring another basis admitted under
SPEC_METHOD §3 (P2, P6; §1, Milestones).

### Strategy requirements

When `migration_strategy: inside_out_hard_break`, the ticket carries a full
best-guess interface inventory for the migrating contract family; the
ordered break sequence from the deepest source truth outward; the old seam
each break intentionally severs; and the negative proof expected for each
break (P4b, P6).

When `migration_strategy: fundamental_re_adoption`, the ticket carries the
explicit selection of fundamental re-adoption by the human product
authority; the comparison with bounded evolution across product value,
feedback latency, authority risk, reversibility, total cost and retained
predecessor semantics; the bounded abort or re-entry condition; the
sideways reference line or prior implementation boundary treated as source
material; the module and interface adjudication surface; and explicit
classifications for inherited modules, interfaces, carriers, projections
and proof surfaces, each `carry_across`, `redundant` or `rewrite`
([SPEC_METHOD §7](SPEC_METHOD.md#fundamental-migration) defines the three).
Unclassified inherited implementation blocks closure (P6, P3).

### Recurring realisation and library declaration

An implementation migration ticket declares whether the active boundary is
rebuilding a pattern locally, consuming an existing reusable library or
commonisation surface, or extending that surface before the local
implementation lands; `library_usage` records which (P2, P4a).

The recurrence rule is ticket law for every implementation migration
ticket, whichever profiles the Product adopts (P2, P4a): the second
credible recurrence forces an explicit
library or commonisation review; the third local rebuild is not acceptable
by default. If review shows the same realisation pattern already exists in
two module boundaries or tickets, a third local rebuild blocks
implementation unless the ticket declares `library_usage: consume`,
declares `library_usage: extend`, or links an explicit do-not-commonise
design decision in `library_rationale`. The preferred order is
boundary-local cleanup, then a tenant-local reusable library or
commonisation surface, then shared or common propagation only through
separate design re-entry (P2, P3). A Product that adopts DESIGN_MODULE
also applies its refinement,
[§10 Recurrence extraction](DESIGN_MODULE.md#recurrence-extraction),
which makes the same rule a design-review obligation and states what
counts as a commonisation candidate; it adds no rival threshold.

A reusable pattern discovered during the active ticket remains under the
second- and third-recurrence rules. Outside those rules and the current
claim's applicable hard stops it is repricing input: it does not block the
bounded claim or require a follow-up ticket unless the owning authority
admits that follow-up (P2; §7, Execution and verification authority
separation).

### Multi-build-tenant review

When the same work item is processed across several build tenants, review
of backlog and active tickets checks that each tenant has its own suffixed
ticket; each ticket names its `build_tenant`; each tenant ticket has its
own proof surface and closure law; one tenant's green proof does not stand
in for another tenant's closure; and reopening, repricing and successor
work remain tenant-local unless the upstream source, product or design
ticket itself must change (P3, P6;
§4, Multi-build-tenant independence).

### Review disambiguation

An implementation migration ticket makes the review problem concrete enough
that an implementor cannot land a rename, adapter, wrapper or happy-path
proof and claim source-truth migration (P6, P1). For a core-interface or
carrier migration the ticket should include a `Functional Review Criteria`
section, specific to the ticket, such that a reviewer should be able to
answer these generic questions:

1. Did the change replace control-flow-owned meaning with carrier-owned,
   algebra-owned, event-owned or otherwise admitted source truth?
2. Did the change reduce or remove a semantic centre, or only rename and
   relocate it behind helpers?
3. Is the new law expressed as a typed or closed carrier, contract or
   transition family rather than an open dict, string protocol or
   config-shaped surface?
4. Is the main step readable as a pure transform over admitted truth, or
   does it still contain orchestration that decides the law procedurally?
5. Are effects pushed to the edge, such as event emission, manifest
   publication, file or output publication, or operator delivery, instead
   of being mixed into source-truth interpretation?
6. Do downstream consumers pattern-match or otherwise consume the admitted
   carrier directly, or do they reconstruct truth from payloads,
   `.get(...)`, fallback defaults, raw text or legacy files?
7. Are projections and reports derived from event or source truth, or can
   they still close independently as a second authority surface?
8. If deterministic gates, validation or other deterministic checks exist,
   do they inform the current state without structurally blocking the
   lawful constructive or probabilistic path that the admitted contract
   permits?
9. If the same realisation pattern already exists elsewhere, does the
   ticket explicitly consume or extend a reusable library or commonisation
   surface rather than rebuild it locally again?

Passing tests do not satisfy this section by themselves. A slice that keeps
the same semantic centre alive behind typed wrappers, adapter-local policy,
old lists beside new algebra, fallback config or rehydrated dict payloads
still fails migration review even when public behaviour remains green
(P6).

### Impacted interface review checklist

For a core-interface, carrier or authoritative-contract migration, the
ticket includes an `Impacted Interface Review Checklist` before tests can be
used as closure evidence. The checklist is a named walk of every live
interface that can still bypass, reinterpret, replay or project the
migrating truth path (P4b, P6).
At minimum it should enumerate, where they exist: the source-carrier builder;
closure, register and projection builders; the deepest semantic kernel and
adapter boundaries; public wrappers and the bootstrap, replay, ingest,
resume and query entrypoints; prompt, report, projection and read-model
surfaces; constructor and materialisation paths; proof lanes and
negative-proof fixtures.

Each checklist item states what counts as closure for that interface, for
example:

- "`<conformance-module>::consume_projection` consumes the admitted carrier
  or projection and does not import raw helper authority"
- "`<query-module>::project_domain` exposes a read model only and does not
  silently rebuild the carrier when publication is absent"
- "`<gap-module>::build_canonical_gap` does not aggregate open payload rows
  into an independent closure decision"

Review rules (P6): a checked box asserts truth on the current tree, not
intended direction; if review shows a checked interface item is false, the
ticket is not closure-ready; an intentionally deferred interface either
names its successor ticket or stays unchecked; compatibility shims do not
satisfy the checklist unless explicitly justified as retained
compatibility; for `inside_out_hard_break` the checklist describes the
seam inventory before tests are used as closure evidence; for
`fundamental_re_adoption` the checklist covers the inherited modules and
interfaces being carried, dropped or rewritten, and implicit carry-forward
does not count.

### Break order and break-to-closure map

An implementation migration ticket that touches a core interface includes
a `Required Break Order` or an equivalent ordered execution section. The
order starts at the authoritative source carrier and moves outward
(P4b, P6;
[SPEC_METHOD §7](SPEC_METHOD.md#hard-break-discipline)):

1. discover the full best-guess interface family;
2. publish or admit the new source carrier;
3. deliberately sever one old authoritative seam and keep it broken;
4. rebind the deepest semantic kernel to that carrier;
5. remove or demote old producers;
6. rebind old consumers;
7. reprice projections, reports, prompts, delivery bindings and tests.

When the migration has several old interfaces, the ticket also includes a
`Break-To-Closure Map` stating which break closes which closure-law clause;
without it a partial landing can look like a full landing (P6).

Reviewers treat these as explicit defects: a typed wrapper that still
carries old semantic authority; a new carrier added beside the old
authoritative read model; a proxy or partial implementation that keeps the
old interface alive behind a new name; constructor, replay, ingest, resume,
bootstrap or public-wrapper paths that bypass admission; a projection or
test that can pass without the new carrier; a fallback path that invents
missing policy, identity, target or closure truth; a downstream proof that
passes while upstream source-carrier work remains open (P6, P3).

### Mixed-state negative proof

For a migration ticket, positive behaviour proof is not enough. The proof
surface should include at least one negative or structural proof that
the old path can no longer satisfy the closure law (P6, P5). Examples: the severed seam in the current
break is rejected before downstream repair is accepted as progress;
removing the new carrier makes advancement, closure, prompt assembly or
projection fail closed rather than silently fall back; a legacy payload
without the admitted carrier is rejected instead of rehydrated into current
truth; old and new truth intentionally disagree in a fixture and the new
truth wins or the run fails closed; a same-name carrier, published
function, route, policy or projection source with different structure fails
closed instead of being accepted as equivalent; required closure proof
does not depend on undeclared local fixtures or mutable sibling workspaces.

If the old path still works in normal execution within the declared
affected scope, or remains reachable on the claimed acceptance path, the
ticket remains open unless that path is explicitly specified as retained
compatibility. A deterministically routed, non-overlapping product scope
outside the declared affected scope remains governed by its own current
authority and does not block the migration merely because its path still
works (P3, P6).

For a ticket with an `Impacted Interface Review Checklist`, the negative
proof exercises the named public consumers that matter for closure. Proving
that one legacy shim is bypassed is not sufficient when the live authority
path already bypasses that shim through other helpers, loaders or rebuild
paths (P4b, P6).

## 7. Authority, judgment, closure and state

The generic law is tier 1: a constructor's self-review is construction
output and the independent-assessment protocol is
[EVALUATION §3](EVALUATION.md#3-independent-assessment); acceptance as the
decision owner's disposition, and closure by stated condition rather than
by reviewer approval, is [EVALUATION §5](EVALUATION.md#5-acceptance); reuse
of a closed result is [ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse).
This section states what those laws require of work carriers.

### Execution and verification authority separation (UP-007)

Authority to author or implement a change is not independent authority to
verify it. What counts as independent, including that the reviewer is
not the author of the reviewed subject, and the protocol an independent
assessment follows are
[EVALUATION §3](EVALUATION.md#3-independent-assessment). Where
independent review is required, the reviewer identifies the exact
subject, basis, scope, exclusions, evidence, verdict and unresolved
findings (P6). Review
findings must cite current authority and the code or proof paths they
rest on, not only historical commentary (P6, P1).

Self-review remains useful authoring evidence and cannot be relabelled as
independent. Human authority may accept or reject the claim; it does not
make implementer self-review independent. The boundaries at which this
method requires independent assessment are this member's policy, which
EVALUATION §3 names; a governing basis may add others, as that section
states. Independent review is required at
product, qualification, release and explicitly risk-bearing boundaries that
claim it, not for every local implementation step (P6, P2).

A claimed independent review may support promotion or closure only when its
exact subject and verdict are durably traceable through an existing ticket,
commentary, qualification or release-evidence carrier. A statement that
review occurred, an unbound conversation summary or an unavailable draft is
not the review verdict. This rule requires no separate receipt, carrier or
review round (P6, P4b).

A ticket's review verdict is bounded by the exact reviewed claim and its
applicable hard stops. When a finding blocks current promotion, and what a
valid observation outside that boundary does, are stated once at
[EVALUATION §5 When a finding blocks promotion](EVALUATION.md#when-a-finding-blocks-promotion);
this carrier applies that section to a ticket's review and adds no
trigger (P2, P6).

A direct or lawfully proxied human ruling receives a durable disposition
before the next affected acceptance boundary. Its source wording stays
distinct from agent interpretation. Opening a ticket records the
obligation and does not satisfy it, and an agent cannot widen the ruling
while recording it (P6, P4b).

Where the agentic construction relation applies (ACTIVATION §1, bound to
this method by [SPEC_METHOD §8](SPEC_METHOD.md#8-bounded-execution-in-this-method)),
the active work item identifies the selected execution basis, the bounded
affected relation set, the delegated construction and assessment authority,
and the re-entry conditions. It may point to accepted design and existing
evidence carriers rather than restate them. Ticket state, ticket prose or
an admitted execution contract cannot widen that basis or substitute for
the live-surface assessment the relation requires (P6, P0).

The reviewable transition (ACTIVATION §7, Transition evidence) may be
carried by an existing ticket, commentary, commit, qualification or
release-evidence surface. No new ticket state, document type, review round
or approval ceremony is required. This member carries selection and
traceability; ACTIVATION §1 and SPEC_METHOD §8 own the execution semantics
(P2, P6).

### Recorded judgment and owner-ruling continuity

A residual judgment that another activation needs is recorded once, with
its owning work, in the existing carrier selected under §5. The record
identifies the question; the exact subject and governing basis; the
supporting computed facts and evidence; the responsible actor and its
authority; the conclusion and its scope; the uncertainty; and a concrete
revising observation that lets a consumer determine whether the conclusion
still applies. A question settled by rule needs no invented J record (P4b,
P6; C, J and O are
the annotations of [SPEC_METHOD §4](SPEC_METHOD.md#computed-classification-and-treatment)).

Later roles and resumed runs recover the result and check its
applicability rather than re-author unchanged judgment. Reuse and
invalidation are
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse): changed material
inputs, a declared revising observation or a changed basis invalidate
the affected result, preserving the original result and its successor
relation and keeping only demonstrably independent results, and a new
role or conversation alone invalidates nothing. For a recorded judgment
the material inputs include its supporting computed facts and evidence,
and its declared revising observation is the one the record states;
reassessment covers what the change affects. The result may reference
current C outputs; reuse cannot silently turn unknown facts into
established premises (P4b, P5). Required independent assessment may consume valid C, but
its assessor acquires sufficient exact evidence and supplies its own
judgment under the actual independence condition; reusing the author's J
cannot satisfy that condition (P6; EVALUATION §3).

A direct or lawfully proxied owner ruling is recorded in its original
wording, with its owner, exact subject and basis, permitted scope and
effects, conditions and source, separately from agent interpretation. Later
work consumes that same ruling while it applies; it neither widens the
ruling nor requests unchanged authority again. New ambiguity or a
materially changed decision returns only the affected question to its
owner. J is not O, and recording either cannot create admission,
acceptance, effects or continuation beyond the original grant (P6, P3).

These results follow the lifetime of the existing run, sprint or durable
ticket and its named result and evidence surface. They require no separate
judgment registry, no ticket per judgment and no additional approval
ceremony (P2).

Repricing gives each affected obligation a disposition in that same
carrier: retained, superseded, deferred or withdrawn, with its owning
authority and applicable evidence links. Surviving work is preserved and
changed dependencies are explained; unaffected history is not copied into
a parallel ledger. An owner decision is presented as the short consequence
delta needed to decide it, with the original ruling preserved separately.
A general instruction to continue does not accept an undisclosed
architectural or scope change (P4b, P6, P2).

The four repricing dispositions are lifecycle states of an obligation,
set by its owning authority. A state label is not an evaluation result and
has no automatic core mapping. A material repricing decision is the separate
owner decision that establishes one such state for an exact obligation,
subject and basis. Its record names the chosen disposition, the decision
owner and grant, the governing conditions, evidence, affected dependencies,
remaining obligations and any conditions for revisiting the decision (P3,
P4b, P6).

A performed evaluation of that decision answers the predicate: **the named
owner lawfully establishes the recorded disposition for this exact
obligation, subject and basis, with every applicable condition satisfied
and every surviving obligation preserved.** This is the repricing predicate
owned here; it is not candidate acceptance under
[ACTIVATION §3 Disposition](ACTIVATION.md#disposition), and it does not claim
that the underlying work was delivered. The result retains the decision,
its chosen state and its evidence, and refines the core values of
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results) as follows:

| Repricing result | Core value | Meaning for the repricing predicate |
|---|---|---|
| `repricing_established` | satisfied | the exact applicable owner decision, authority, evidence and preservation of surviving obligations establish the predicate |
| `repricing_falsified` | falsified | a counterexample defeats the predicate, including a disposition outside the actor's grant or contrary to an applicable obligation |
| `repricing_indeterminate` | indeterminate | admissible evidence cannot decide whether the decision meets an applicable condition; the undecided condition and needed evidence remain explicit |
| `repricing_out_of_frame` | out_of_frame | a material relation or capability needed to evaluate the decision is undeclared in the frame; the missing relation or capability remains explicit |
| `repricing_invalid_basis` | invalid_basis | the decision is evaluated on an absent, stale, ambiguous or mismatched required basis that cannot support the predicate |

An evaluation that was not performed has no result. The evaluation records
all applicable failure grounds and supplies no decision authority; the
state changes only through the owner's authorised act. A lawful deferral
may therefore yield `repricing_established` while the delivery claim remains
failed or outstanding. An unauthorised `withdrawn` label cannot close an
obligation. Neither retention nor a satisfied repricing predicate establishes
delivery, and a superseded, deferred or withdrawn state cannot erase
unresolved obligations or evidence (P5, P1, P6).

### Condition-based closure and reuse

A work claim is complete only when every applicable declared obligation is
satisfied by valid evidence for its exact subject, basis and scope; every
required judgment and owner ruling is present and applicable; and no active
non-closure condition remains. A mandatory obligation whose applicability is
unknown, or whose evidence is insufficient, withholds the dependent claim;
evidence presence alone is not satisfaction. The existing owner decides any
reserved acceptance (P6, P5).
This condition is the
[conjunction of results](FOUNDATIONS.md#conjunction-of-results) with the
declared obligations as required coverage. This section owns the
closure condition of a work claim;
[SPEC_METHOD §4 Consistency gate](SPEC_METHOD.md#consistency-gate)
applies it as the gate over a declared change span.

Review evaluates these conditions; its occurrence is not the closing event.
Where applicable law requires no independent review or reserved
acceptance, a work claim is recorded as
[ACTIVATION §1 Roles and delegation](ACTIVATION.md#roles-and-delegation)
states in Recording a result without review, with the ticket as the
existing carrier. The conditions that still apply include sprint-close
law (§3) and the design profile's law (P6, P2).

An unchanged obligation reuses valid applicable evidence and recorded J
and O under the reuse rule of
[ACTIVATION §7](ACTIVATION.md#7-closed-result-and-reuse). For a work
claim, the changed material inputs and revising observations that rule
names include a material counterexample, changed evidence and a stated
revising observation of a recorded J; with a changed basis, each
invalidates the affected claim and its dependent results before further
reliance. An unrelated observation is retained as bounded repricing input;
it does not reopen a satisfied claim or expand the work automatically.
Closure recording preserves the exact evaluated scope, the satisfied
conditions, the evidence and the remaining residuals (P4b, P2).

Landing a candidate and releasing it are distinct from this condition; apply
[EVALUATION §5](EVALUATION.md#landing-closure-and-release) and any explicitly
declared Product acceptance gate. An open required review withholds the work
claim that depends on its complete coverage, not an independently authorized
landing merely because review is open. Keep the linked Bug items and their
verification provenance current; a report's existence closes none of them.

### Test case authority

Tests are proof projections from admitted work authority. Every
substantive test case should derive along this chain (P6, P2):

```text
ticket -> intake triage -> lawful re-entry point -> governing requirement,
design, module, published function, carrier, or closure surface -> test expectation
```

Tests do not derive authority from the current implementation. An
acceptance predicate also needs an applicable supported entry or state and
an obligation under the governing operating or threat model. Existing test
presence cannot authorise an excluded threat or retain a superseded guard.
When that responsibility changes, the affected predicates are audited, and
unsupported expectations are retired under the owning basis without
inventing a replacement guard. An actual conflict in live authority
requires re-entry, not a test-only waiver (P6, P2).

Implementation behaviour is evidence. The code is never the arbiter of a
test's expected result when code and test disagree (P6). When a ticket is
fixed and a mismatch appears between implementation behaviour and test
expectation, review reconciles the mismatch in this order:

1. the ticket's `change_intent`, `change_class`, `re_entry_point`,
   `target_truth`, `superseded_truth`, `closure_law`,
   `evaluation_criteria` and `non_closure_conditions`;
2. the ticket's intake triage and lawful owning re-entry;
3. the governing requirement, design, module, published-function, carrier
   or other cited authority surface;
4. the test case expectation;
5. the implementation.

The implementation may show that a test is stale, incomplete or too
narrow; it cannot by itself authorise changing the expected result.
Changing a test only because the current code behaves differently is a
ticket-method defect. A test that predates a lawful ticket repricing is
updated or removed only after naming the governing ticket and the authority
change that superseded the old expectation. If the ticket is stale,
ambiguous or missing the authority needed to decide the expectation, the
work re-enters triage (§4) before either the code or the test is treated as
correct. A passing test is closure evidence only when its expectation
traces back to the admitted ticket and its governing authority chain (P6,
P4b). The general test authority law is ASSURANCE §3; this clause is its
ticket-local rule.

### One-truth state projection and drift refusal (UP-009)

Work state has one authority chain: goals own the bounded work wave, the
ticket owns ticket state, milestone authority owns subordinate milestone
state (§1), and accepted design owns realisation decisions. Comments,
dashboards, registers, indexes and generated summaries are projections
(P6, P3).

Recency, visibility or repetition does not turn a projection into truth.
Contradiction between the owning ticket, its required milestones, the
current goals or the cited acceptance evidence blocks closure. Superseded
evidence remains history and cannot be projected as current acceptance
(P6, P4b).

## 8. Recommended shapes

These shapes are the recommended carriers of the fields and sections the
rules above require; a project may bind another shape that carries the
same fields (§2; P3, P4b).

The sprint manifest, carrying the fields of §3:

```md
# SPRINT-2026-04-30 Operational Projection UX Iteration

- id: SPRINT-2026-04-30-operational-projection
- status: active
- goal: operational-projection-ux
- opened_at: 2026-04-30T09:00:00Z
- updated_at: 2026-04-30T09:00:00Z

## Authority

- specification/GOALS.md#operational-projection-ux
- specification/PRODUCT.md#operational-projection
- <governing-design-surface>/OPERATIONAL_PROJECTION.md

## Scope

Iterate an operational projection surface for layout, readability,
interaction affordance, and visual evidence quality.

## Excluded Boundaries

- no product truth changes
- no data contract changes
- no runtime or governance semantics changes
- no new constructive carrier

## Expected Change Classes

- realization_refactor

## Iterations

- id: UXI-001
  intent: improve relation-line readability
  evidence_ref: screenshots/2026-04-30/UXI-001.png
  debt: accessibility contrast check pending

## Closure

- closure_trigger: timebox, changed surface volume, or design-lead close request
- closure_law: forensic walkthrough reviews each changed state against authority
- proof_surface: screenshots plus walkthrough notes
- deferred_compliance: screenshots, accessibility check, event-replay review
- non_closure_conditions: product truth or data contract drift remains hidden
- paydown_policy: open paydown tickets for accepted local debt; reprice authority drift
```

An ordinary ticket, carrying the required fields and triage metadata of §4:

```md
# T-001 Add Product Layer To SPEC_METHOD

- id: T-001
- type: feature
- ticket_category: ordinary
- status: active
- goal: methodology-bootstrap
- change_intent: make the product-definition layer explicit in the constitutional chain
- change_class: product_reprice
- re_entry_point: product
- triaged_at: 2026-04-07
- priority: high
- created_at: 2026-04-07
- updated_at: 2026-04-07

## Context

`SPEC_METHOD.md` included intent and requirements flow but omitted the explicit
product-definition layer.

## Acceptance

- `PRODUCT.md` is part of the constitutional chain
- bootstrap sequence includes `intent -> product -> requirements`
- examples and reconstruction logic reflect the new layer

## Links

- comment: `.ai-workspace/comments/<agent-id>/...`

## Bug items

Only when findings exist; use one row per triaged finding. The source report
owns the original assessment. The decision owner owns this item's priority
and disposition.

| ID | Source report/finding | Severity | Priority and reason | Cause group / owner | State | Repair subject / verification evidence | Disposition / retained destination |
|---|---|---|---|---|---|---|---|
| <item> | <exact report and finding> | <unchanged grade> | <decision> | <cause and owner> | <open/fixed/verified> | <identity; tests; required review if any> | <exact decision and link> |
```

An implementation migration ticket, carrying the declaration, fields and
checklist of §6:

```md
# B-010 Replace Mixed Gap Projection With One Authoritative Carrier

- id: B-010
- type: bug
- ticket_category: implementation_migration
- migration_strategy: inside_out_hard_break
- library_usage: none
- library_rationale: this migration is boundary-specific and does not establish a recurring realization pattern
- status: active
- goal: operator-gap-truth
- change_intent: replace the mixed operator gap truth with one authoritative declared carrier
- change_class: design_reframe
- re_entry_point: design_surface
- triaged_at: 2026-04-20
- created_at: 2026-04-20
- updated_at: 2026-04-20

## Migration Declaration

- affected_scope: gap projection on the declared operator-query acceptance path
- excluded_or_disjoint_scopes: none
- old_truth_path: fallback gap projection with synthetic convergence fields
- new_truth_path: explicit declared-obligation projection plus separately classified fallback gaps
- producers_old: `<gap-module>::build_fallback_gap`
- producers_new: `<obligation-module>::collect_declared_obligations`, `<gap-module>::build_canonical_gap`
- consumers_old: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- consumers_new: `<query-module>::project_gaps`, `<summary-module>::project_span`, `<review-surface>::render`
- derived_surfaces:
  - `<query-surface>::gaps`
  - `<summary-surface>::span`
  - `<proof-surface>::first_slice_negative`
- closure_law: migration closes only when the old projection is no longer authoritative within the affected scope and mixed old/new proof does not count as acceptance

## Migration Checklist

- [ ] exact affected migration scope is named
- [ ] excluded or disjoint Product and compatibility scopes are named with deterministic routing, or explicitly declared absent
- [ ] old truth path is named explicitly
- [ ] new truth path is named explicitly
- [ ] producer set for the new truth is listed
- [ ] consumer set for the new truth is listed
- [ ] projection/read-model surfaces are listed
- [ ] old truth path is removed or explicitly demoted from authority within the affected scope
- [ ] mixed-state behavior is no longer accepted as closure evidence
- [ ] tests proving mixed old/new behavior are removed or repriced
- [ ] recurring realization patterns are checked against existing library/commonization surfaces
- [ ] ticket declares library usage and names the governing library or rationale
- [ ] if the work exists in more than one build tenant, this backlog/active ticket carries only one tenant lifecycle and any sibling tenant work lives on its own suffixed ticket
- [ ] ticket wording, product wording, and proof claims are reconciled before closure
```

## 9. Operating mode and relationships

### Operating mode

The default local-file carrier assumes that humans and agents can read the
active ticket folder directly; that backlog remains searchable durable work
without competing with the active lane for immediate attention; that `rg`
is sufficient for finding active work; and that no database or board is
required (P0, P2). Typical commands for that carrier:

```bash
rg -n "^#|^- status:|^- type:|^- goal:".ai-workspace/tickets/active
rg -n "^#|^- status:|^- type:|^- goal:".ai-workspace/tickets/backlog
rg -n "T-001|B-002".ai-workspace/tickets
```

### Relationship to other surfaces

Each surface answers one question (P3, P6). The goals surface: what broad work wave
matters now. SPEC_METHOD: what constitutional change class and re-entry
point govern the work. Sprints: what bounded execution batch is currently
pricing proof, evidence and paydown. Tickets: what durable units of work
exist and what state they are in. Comments: what was proposed, argued,
decided, reviewed or handed off. POSTING_GUIDE: how comment-layer
publications are structured and named.

The separation prevents goals becoming an overloaded backlog; active work
being diluted by every deferred ticket; comments becoming informal task
status; and task boards becoming accidental authority (§2, §7).



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/RESULT.json
SHA256 856aab5b68856c6fbd2787784059bbaa43e92f2f116401ae8cd0f590cce394a8; 8096 bytes

{
  "profile": "stdo.visual-products-writer-result/1",
  "result": "satisfied",
  "claim": "Bounded delegated construction of three versioned visual Products and one fresh final-native-A-bound visual artifact; no independent semantic acceptance or publication claim",
  "activation": "WRITER_ACTIVATION.md",
  "candidate_root": "/Users/jim/src/apps/specification_methodology-3.1-release",
  "products": [
    {
      "product": "a_c",
      "public_manifest_sha256": "40b6e19214f40ba10ed38d90b11f98f0e62ecad6ef2e9b2ccf758ed9607f74af",
      "public_members": 30,
      "package_members": 48,
      "package_inventory_sha256": "aed353f70f1b18f8199b71e07bcf23e09888b6d34c259d92e61ffee5e8e6b6ed",
      "valid": true
    },
    {
      "product": "stdo_representation",
      "public_manifest_sha256": "f1e132063af09d266c9aef908ea778253d22ede665c1bcf6762d33b4d8e124e8",
      "public_members": 47,
      "package_members": 67,
      "package_inventory_sha256": "07ecf9a57550c1b701557de39bbf2fdc2827d5a40b024253ddd53f1406fc978d",
      "valid": true
    },
    {
      "product": "axiom_indexer",
      "public_manifest_sha256": "9d9bbe03ebd31ea7d114ef4c56dd1929e9107cd12ceb12dd4ecaa4fbc9f5dbed",
      "public_members": 3,
      "package_members": 24,
      "package_inventory_sha256": "f0630568efc7d794ceadbbfa9060942782d6306109bc8b787706268ae3fe1991",
      "valid": true
    }
  ],
  "represented_source": {
    "uri": "stdo://releases/v3.1.0-rc.1/",
    "manifest_sha256": "ddbd3910981a63f41c17879551f93ef58f369848bae81cc9726d77df55dc7faa",
    "release": {
      "commit": "c1e0faaa8437c169031a476343c764614135cd93",
      "cut": "v3.1.0-rc.1",
      "project_release_namespace": "specification_methodology",
      "project_subtree_root": "specification_methodology/v3",
      "project_subtree_tree": "31aab3cebc56ec308afb3c7312cd4b6d3315043e",
      "qualified_ref": "refs/tags/specification_methodology/v3.1.0-rc.1",
      "standards_tree": "78f97d798fabacf0b76c2e2e6a19d7257a75198d",
      "tag_object": "fca8d5e97cf2e945196aecdc33908bb190efdca5",
      "tree": "0ceecf8a106dff4c7b616849167757405f819610"
    }
  },
  "construction_basis": {
    "uri": "stdo://releases/v3.0.4/",
    "manifest_sha256": "102817a3f4bea4dca1d6fa0fc634b94404dd2ba82ba6d8c38b273402dda9f95b"
  },
  "artifact": "stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1",
  "model": {
    "id": "urn:a-c:generation:c8b565861ea509feddf2ebd4:model:3748671f0539880ef4616730",
    "sha256": "10f810f04d4fcf99424ea99631f461e108ee8030ce8145915eb5b9dbe8d14851"
  },
  "coverage": {
    "selected_visual_members": 3,
    "selected_visual_bytes": 255355,
    "selected_sections": 93,
    "dispositions": {
      "residual": 93
    },
    "selected_authored_annotations": 24,
    "records": {
      "concepts": 104,
      "relations": 99,
      "constraints": 8,
      "latitude": 1,
      "residuals": 94
    },
    "whole_method_semantic_coverage": false
  },
  "public_pipeline": {
    "prepare": "passed",
    "task": "passed",
    "submit": "passed",
    "build": "passed",
    "status": "passed",
    "matching_reuse": "passed",
    "stale_source": "refused as expected; copied source restored exactly"
  },
  "axiom": {
    "convert": "passed",
    "restore": "exact model value preserved",
    "validate": "passed",
    "project": "one selected materialized projection passed"
  },
  "browser": {
    "runtime": "1.66.0-alpha-2026-11-09",
    "browser": "157.0.8103.78",
    "checks_passed": 9,
    "http_requests": 0,
    "page_errors": 0,
    "scope": "Actual offline source-file reader, full conditional records, directed relationship and its qualifications, explicit residual, layered/2D/3D state preservation and visible rendered force canvases",
    "evidence": "browser-final-003/RESULT.json",
    "force_fit_observation": "browser-force-fit-001/RESULT.json",
    "writer_visually_inspected": [
      "browser-final-002/01-condition-reader.png",
      "browser-final-002/03-relation-qualifications.png",
      "browser-final-002/04-residual-layered.png",
      "browser-final-003/view-mode3.png",
      "browser-force-fit-001/mode3.png"
    ]
  },
  "tests": {
    "retained_visual_python": {
      "discovered": 182,
      "passed": 138,
      "skipped": 44,
      "skip_scope": "optional live pinned Graphify/bootstrap boundaries not selected"
    },
    "axiom_python": {
      "passed": 34
    },
    "direct_project_python": {
      "discovered": 16,
      "passed": 15,
      "skipped": 1
    }
  },
  "evidence": [
    "OPERATION.md",
    "PREREQUISITE.json",
    "PACKAGE_SELECTION.json",
    "FINAL-INVENTORY-READBACK.json",
    "PACKAGE_SOURCE_DELTA.json",
    "PREDECESSOR-ARTIFACT-CONSERVATION.json",
    "RECIPE-PREREQUISITE.json",
    "generation-001.log",
    "final-checks-001/RESULT.json",
    "final-checks-001/PROVIDERS.json",
    "browser-final-003/RESULT.json",
    "browser-force-fit-001/RESULT.json",
    "retained-visual-tests-001.log",
    "retained-visual-tests-002.log",
    "project-tests-001.log",
    "axiom-tests-001.log",
    "navigation-tests-001.log",
    "BROWSER-TOOL-ATTEMPT-001.json",
    "BROWSER-LOCAL-PREFLIGHT.json",
    "browser-final-001/RESULT.json",
    "browser-final-002/RESULT.json"
  ],
  "retained_first_failures": [
    {
      "subject": "MCP browser preflight",
      "cause": "Existing Chrome profile in use; no artifact was loaded",
      "disposition": "Separate local temporary Chrome profile used without altering existing browser"
    },
    {
      "subject": "First retained visual Python suite",
      "cause": "63 fixtures used /var symlink temp path and were refused by existing source guards",
      "disposition": "All 138 applicable cases passed with explicit resolved Product-local TMPDIR;44 optional live boundaries skipped"
    },
    {
      "subject": "Controlled DOM navigation harness",
      "cause": "Available jsdom28.1.0 differs from declared26.1.0 and fails Node require with ERR_REQUIRE_ASYNC_MODULE",
      "disposition": "This harness lane remains unperformed; actual final-artifact Chrome reading evidence used for the declared UI claim"
    },
    {
      "subject": "First actual browser assertion",
      "cause": "Harness expected unnumbered source text although reader intentionally displays line numbers",
      "disposition": "Original failed script/result retained; corrected assertion strips display line-number prefixes then compares complete source exactly; final runs passed"
    }
  ],
  "residuals": [
    "Distinct-family source-first assessment is root-owned and is not supplied by this Writer.",
    "No whole-method semantic coverage, current context engine, Lean/formal proof, subject-code correctness or general UX qualification.",
    "General non-STDO fidelity/usefulness and actual optional Graphify/code extraction integration are unobserved and excluded from integrated qualification claims.",
    "One compact latitude graph label uses generated identity; its complete allowed/forbidden payload is readable. Force views benefit from settling and Fit/pan/zoom; reading controls remain available.",
    "Model format retains its explicit 2.5.1-rc.2 calculus coordinate separately from construction3.0.4 and represented native3.1. Axiom points at the represented native calculus and preserves model metadata.",
    "Browser observation is source-file offline Chrome on this host; root owns packaged/public-download/install checks and required review."
  ],
  "historical_conservation": "All9 top-level current3.0.5-rc.1 model/carrier/view/control files are byte-conserved against original main. No historical meaning or verdict was rebound.",
  "no_effects": [
    "No Git/ref operation",
    "No global installation",
    "No remote publication",
    "No original-main Product mutation",
    "No other Product territory mutation"
  ],
  "return_consumer": "root release coordinator and independent final assessment operator",
  "validity": "Source, provider, recipe, model, native binding or package member changes require affected evidence re-entry; prior exact evidence is retained."
}



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/FINAL-INVENTORY-READBACK.json
SHA256 3466ba36a8c1b2dff6d63d9a2bb368cb9bcf693f2c3960a30505d75d280da985; 1027 bytes

{
  "providers_and_artifact": [
    {
      "product": "a_c",
      "public_manifest_sha256": "40b6e19214f40ba10ed38d90b11f98f0e62ecad6ef2e9b2ccf758ed9607f74af",
      "public_members": 30,
      "package_members": 48,
      "package_inventory_sha256": "aed353f70f1b18f8199b71e07bcf23e09888b6d34c259d92e61ffee5e8e6b6ed",
      "valid": true
    },
    {
      "product": "stdo_representation",
      "public_manifest_sha256": "f1e132063af09d266c9aef908ea778253d22ede665c1bcf6762d33b4d8e124e8",
      "public_members": 47,
      "package_members": 67,
      "package_inventory_sha256": "07ecf9a57550c1b701557de39bbf2fdc2827d5a40b024253ddd53f1406fc978d",
      "valid": true
    },
    {
      "product": "axiom_indexer",
      "public_manifest_sha256": "9d9bbe03ebd31ea7d114ef4c56dd1929e9107cd12ceb12dd4ecaa4fbc9f5dbed",
      "public_members": 3,
      "package_members": 24,
      "package_inventory_sha256": "f0630568efc7d794ceadbbfa9060942782d6306109bc8b787706268ae3fe1991",
      "valid": true
    }
  ],
  "valid": true
}



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/final-checks-001/RESULT.json
SHA256 b6aef3001d2ce4ffcd7be6175110dc9978af5240618e3b82ddde9b8156f1b60f; 1150 bytes

{
  "profile": "stdo.visual-finite-writer-checks/1",
  "model_file_sha256": "bf696c10177ffc393a3ae0279b3717fccb42d06d6092afd626d8efa245bc022f",
  "model_identity": "urn:a-c:generation:c8b565861ea509feddf2ebd4:model:3748671f0539880ef4616730",
  "source_files": 3,
  "grounding_occurrences_checked": 311,
  "section_dispositions": 93,
  "records": 306,
  "checks": [
    "public model/carrier validation",
    "exact carrier/model value equality",
    "public full-record condition and exception inspection",
    "every declared source quote resolves",
    "every selected section has an explicit residual disposition",
    "offline HTML embeds its sources and scripts",
    "stale copied-source refusal and exact restored status",
    "Axiom convert/restore exact value preservation",
    "Axiom public source validation and selected materialized projection"
  ],
  "source_restored_sha256": "a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8",
  "limits": [
    "Writer evidence, not independent source fidelity or acceptance",
    "No whole-method semantic coverage, external Graphify execution, Lean or subject-code execution"
  ]
}



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/browser-final-003/RESULT.json
SHA256 b3fe9ca9dfa6a93963b68d38a258858ea2ec7aa06eadb8032d8ed7ffca30c74d; 2696 bytes

{
  "profile": "stdo.visual-browser-observation/1",
  "artifact": "/Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/run/generation/proposal/explorer.html",
  "playwright": "1.66.0-alpha-2026-11-09",
  "browser": "157.0.8103.78",
  "checks": [
    {
      "name": "full conditional record reading",
      "detail": {
        "records": 306,
        "initialFamily": "constraints",
        "conditionAndExceptionVisible": true
      }
    },
    {
      "name": "source file navigation",
      "detail": {
        "path": "build_tenants/a_c/representation/stdo-v3.1.0-rc.1/source/standards/SDLC_DEFAULTS.md",
        "sha256": "a04335fe75f38c665055c8272f6707fe9e244b7fece5bed936332d0c82e1aac8"
      }
    },
    {
      "name": "authored relation direction",
      "detail": {
        "source": "urn:a-c:generation:c8b565861ea509feddf2ebd4:record:4b6828bb74fae32e117ae030189695b7",
        "target": "urn:a-c:generation:c8b565861ea509feddf2ebd4:record:36ddcb321e3a7291440d23259ff67b9e",
        "link": "relation:urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f793354343fab46e7b5121a2222477dd",
        "targetReached": true
      }
    },
    {
      "name": "relation qualifications",
      "detail": {
        "conditionAndExceptionVisible": true,
        "recordId": "urn:a-c:generation:c8b565861ea509feddf2ebd4:record:f793354343fab46e7b5121a2222477dd"
      }
    },
    {
      "name": "unrepresented meaning visible",
      "detail": {
        "family": "residuals",
        "sourceReentryConsequenceVisible": true
      }
    },
    {
      "name": "view state mode2",
      "detail": {
        "recordAndHashPreserved": true,
        "actualModeActive": true,
        "canvas": {
          "width": 744,
          "height": 956,
          "visible": true
        }
      }
    },
    {
      "name": "view state mode3",
      "detail": {
        "recordAndHashPreserved": true,
        "actualModeActive": true,
        "canvas": {
          "width": 744,
          "height": 956,
          "visible": true
        }
      }
    },
    {
      "name": "view state mode-layered",
      "detail": {
        "recordAndHashPreserved": true,
        "actualModeActive": true,
        "canvas": null
      }
    },
    {
      "name": "offline browser boundary",
      "detail": {
        "httpRequests": 0,
        "pageErrors": 0
      }
    }
  ],
  "errors": [],
  "requests": [
    "file:///Users/jim/src/apps/specification_methodology-3.1-release/stdo_representation/build_tenants/a_c/representation/stdo-v3.1.0-rc.1/run/generation/proposal/explorer.html"
  ],
  "limitations": [],
  "status": "passed"
}



## Exact file /Users/jim/src/apps/specification_methodology/.ai-workspace/work/STDO_3_1_RELEASE_2026-11-15/visual/PREDECESSOR-ARTIFACT-CONSERVATION.json
SHA256 9782dc68764da3e975432d5ee2629bb83e96953dc9faf6d6227bb1aedf78231a; 3129 bytes

{
  "predecessor": "v3.0.5-rc.1",
  "scope": "All nine top-level historical current visual artifact/control files unchanged from original main; no semantic verdict transfers to 3.1",
  "samples": [
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/carrier.json",
      "candidate_sha256": "642e2f52068d81d3772cdf1ca9e4f8c45b475042b22901eaef203fed735ad923",
      "original_sha256": "642e2f52068d81d3772cdf1ca9e4f8c45b475042b22901eaef203fed735ad923",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/coverage.json",
      "candidate_sha256": "92f0263660a5f8fc1c8e327d0e5a4c6d39306aa49dd1ba067995b100a1ca456d",
      "original_sha256": "92f0263660a5f8fc1c8e327d0e5a4c6d39306aa49dd1ba067995b100a1ca456d",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/current-binding.json",
      "candidate_sha256": "91ba805d8247c066b329ed56677734f27c51a2a9f0c4b9a3ca4658b4e253e4f5",
      "original_sha256": "91ba805d8247c066b329ed56677734f27c51a2a9f0c4b9a3ca4658b4e253e4f5",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/explorer.html",
      "candidate_sha256": "caea5840aedea0573483b74d753d0c830442489a3b10af9fef22f182ef0c95a2",
      "original_sha256": "caea5840aedea0573483b74d753d0c830442489a3b10af9fef22f182ef0c95a2",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/model.json",
      "candidate_sha256": "b40ecc595d1a58ad96a9ba0be4942e015123224adee1832a58a6c3b53f21eeb7",
      "original_sha256": "b40ecc595d1a58ad96a9ba0be4942e015123224adee1832a58a6c3b53f21eeb7",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/semantic-discriminators.json",
      "candidate_sha256": "96e7c4617f8974ac6e50baed8e787dc89bacffd5d271687ed32d24d5180ccc59",
      "original_sha256": "96e7c4617f8974ac6e50baed8e787dc89bacffd5d271687ed32d24d5180ccc59",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/semantic-reuse.json",
      "candidate_sha256": "2e9b4a7cd464b71b36a0a75d7da0567fe0832f2ba3a6aa28c006328e71e79640",
      "original_sha256": "2e9b4a7cd464b71b36a0a75d7da0567fe0832f2ba3a6aa28c006328e71e79640",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/source-freeze.json",
      "candidate_sha256": "76fab92d48a7907107ba717ecdb11c69963ae4ef2431874d4b9b2b6ed7228ff0",
      "original_sha256": "76fab92d48a7907107ba717ecdb11c69963ae4ef2431874d4b9b2b6ed7228ff0",
      "equal": true
    },
    {
      "path": "stdo_representation/build_tenants/a_c/representation/stdo-v3.0.5-rc.1/source-inventory.json",
      "candidate_sha256": "3ed65aa24e27b3a407d0351ec0fe5ef170a0ae3711804ff6bdf69545681abed5",
      "original_sha256": "3ed65aa24e27b3a407d0351ec0fe5ef170a0ae3711804ff6bdf69545681abed5",
      "equal": true
    }
  ]
}
