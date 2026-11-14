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
