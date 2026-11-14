# Exact-subject assessment of the final `python-pure-refactor/2` and `sdlc-workflow/1` queries

**Result:** I judge both exact queries **supported**, with the residuals listed below. I found no material omission and no false strengthening for either exact query. That judgment covers only governing-method constraints before construction, read against the stated source closure. It does not cover task success, code equivalence, a typing pass, host behaviour, release or acceptance. I make no release, acceptance or publication verdict.

## 0. Who assessed, what was received, and the limits

- **Actor.** I am a Claude activation; the environment reports `claude-opus-5-5`, and the CLI metadata is the authoritative identity. I authored no part of either candidate. The Writers and the packet operator are OpenAI/Codex-family, so this judgment is cross-family. It is not independent of two earlier Claude activations: the one that wrote CLAUDE_EXPECTATIONS, and the native assessor of the 3.0.5 Python index. Reusing that Python judgment as cited support carries a confirmation-bias risk.
- **Tools.** I used no tools. This session exposed an "advisor" tool that would forward the transcript to another model; I did not call it. I recomputed no hashes. All SHA-256 values below are taken from the packet and readback as given.
- **Source-first order.** In this session the governing sources and the candidates arrived in one packet. My own reading order therefore was not enforced source-first. The only expectations fixed before exposure are the earlier Claude expectations file, which predates the candidate. I used it as fixed context, not as my verdict.
- **What I read.**
  - Every supplied file was received complete; I saw no clipping marker in the supplied bytes.
  - For both queries I compared all selected rules, the guards on excluded rules, the changed rules and the deciding source sections against the full owners.
  - For the Python index I did not re-derive every one of the roughly 1.6 MB of unchanged owner clauses clause by clause. For the 112 rule objects that are equal to the predecessor over 15 byte-identical owners, I relied on that equality plus my own targeted re-reading. Owner-side applicability of that reuse is shown by RELEASE §9 and FOUNDATIONS change-impact.
  - I cannot establish adequate attention or receipt beyond that.

## 1. Whether each exact query has sufficient governing constraints

### Python query (index `717857…`, corpus `159389…`, query `8ac9eb…`)

- **Mechanical observations (from the packet).** 94 rules are selected and 19 excluded (O01–O10 and U01–U09), with no gaps. All 16 owners are bound to native A. 15 owners are byte-identical to 3.0.5-rc.1; only TICKETS changed (`86fefd…` → `2e601f…`). In the rules, C04 changed in text and source_refs. C14, C17 and C23 moved only in source_refs (+15 lines), with equal span bytes. That matches the 15-line insertion at TICKETS line 727.
- **Exclusions and unknown facts (my judgment).**
  - ODD and UX are excluded on explicit `false` facts that the fixture supports (FRAME_BASIS: no ODD or UX adoption; REQUIREMENTS: no UX surface). They are not inferred from purity.
  - The exception premises are absent (`explicit_failure_carrier_practical`, the `mutation_*` evidence facts and the four `typing_escape_*` premises). They correctly leave the exceptions `false`, because the matching request flags are `false` and a conjunction with a false member is false. A false request grants no exception, and the D05, D06 and D08 bodies tell the actor to requery if a departure becomes necessary. This meets PC-R13.
  - The deciding constraints for this refactor are all selected and faithful to source. That set is S03 and D25 (realization_refactor and no-delta proof, with accepted design available), D05 and D06 (scratch labels and imperative code are neither exempt nor forbidden, read with DESIGN.md's statement on subordinate iteration), D07, D08 and D09 (typing), D15 (purity), D18, E06 and C01 (no equivalence claimed from examples), A02 to A04, and C03, C04 and C10.
- **Judgment.** Supported.

### SDLC query (index `05b5d1…`, corpus `49470f…`, query `07c7e6…`)

- **Mechanical observations (from the packet).** 20 rules are delivered. W09 and W10 are rendered visibly as false dependencies of W12, so 18 apply. Excluded are W11, W13–W22, W25–W32 and W35. All 12 owners are byte-identical to the ticket-trial owners and to A. Relative to the 9-case trial, W01 changed in text and W12 lost its `recurring_failure` guard; W36–W40 are new.
- **Exclusions (my judgment).** Each exclusion follows from a fact grounded in the fixture:
  - no finding, repair, review, reuse or source change;
  - the Executive profile is not adopted (FRAME_BASIS);
  - the boundary is `none` (WORK_CONTRACT keeps acceptance with Root).
- **What the work decision needs, and the rules that carry it.**
  - Binding to the admitted run carrier: W01 and W03, with W36 directing to the sufficient run carrier.
  - Incremental QA: W07 and W08.
  - Closure without an invented Reviewer, and landing, closure and acceptance kept separate: W23 and W24.
  - Bounded context, and capacity measurement against the declared 262,144-byte budget with whole-step fit kept `indeterminate`: W37 and W38.
  - Durable recording into WORK_RESULT.md, and continuation without the prior conversation: W39 and W40.
  - Stopping and acquisition of Product law: W33 and W34.
  - Results and conjunction: W05 and W06.
- **Source closure.** DESIGN_MODULE is outside the 12-owner closure. The purpose routes it through W34, and the companion Python index carries it. I accept that under the purpose's explicit exclusion of specialist law.
- **Judgment.** Supported, with the residuals F1, F2, F5 and F6 below.

## 2. The C04/TICKETS clarification and the W01 change

- **TICKETS paragraph (source meaning).** The new paragraph applies three existing owners to the selected carrier: ACTIVATION §2 (context), §5 (work state and restart) and §7 (reuse). It keeps the ticket's work-state authority (UP-009). It says the paragraph "creates no additional carrier requirement and confers no ticket-state authority". I find no new obligation in it: its bind and preserve duties already exist in ACTIVATION's intake, admission and continuity rules. ACTIVATION remains the single owner. The placement is correct.
- **C04 (my judgment).** C04 is a faithful compression. It omits the explicit sentence "ticket retains work-state authority", but its clause "an actor account cannot replace the carrier, governing sources or current evidence" covers that meaning for this query. This is residual F7.
- **W01.** The development-only clause ("not a selectable partial constitution, immutable release or implicit migration") is replaced by "a source projection or purpose index cannot substitute for the complete operative constitution or implicitly migrate a consumer." For released native source this keeps the meaning of PRODUCT_DEFINITION §11 and SDLC_DEFAULTS' rule that finding or installing selects nothing. Dropping "immutable release" is correct now. W01 is not deciding in any reused trial decision.
- **Whether the TICKETS change is "conserved" or "superseded" under RELEASE §9.** That is a release-record claim and is not judged here.

## 3. Which prior finite decisions remain applicable

- **Three-case ticket trial (TC01–TC03).** Applicable to T-01 through T-06 as observations on their original subjects.
  - **Why it carries.** All 12 owner bytes, the native `stdo-work`, `PRODUCT_BASIS` and `COORDINATED_HANDOFF` bytes, and the meanings of W02–W40 are equal to A. The only changes are W01 (not deciding in any of the three cases), the corpus/index/purpose identities, and the binding route (installed-method-root replacing the development source and the 3.0.5 consumer basis). That route is a mechanical delivery path, not a decision path.
  - **Limits to preserve.**
    - TC03 observed staged measurement: per-body measurement before each read, then a cumulative fit before the context was received. A single initial whole-boundary preflight was not observed.
    - The native source-currentness corroboration happened after the case returns.
    - One sequential actor ran all three cases; they were not separate cold activations.
    - Acquisition limits were instruction-bound, not enforced isolation.
    - Clipping recovery and the failed command `025` are retained as recorded.
    - The provider in TC02 is a fixture only.
    - All contexts are `covered: false`. The semantic judgments from that trial (`unknown`) do not transfer.
- **Nine-case SDLC trial (S01–S09).** Applicable only as decision-level support for the causal-route, boundary, unrelated-finding, reuse, capability and scope-change classes (N-05 to N-13), on the subjects it actually used.
  - **What changed, and why it does not defeat reuse.**
    - W12's guard was removed. That only widens where W12 applies; no decision relied on W12 being absent, and S05's open W12 item becomes applicable consistently.
    - The added W36–W40 and the new SDLC_DEFAULTS continuity text contradict none of the nine decisions.
  - **Applicability not established.**
    - The trial ran on native `stdo-work` `ee0aac3b…` and `stdo-review` `8ccbec09…`; A has `b7ed03fe…` and `a694b9d0…`. No delta was supplied.
    - So I cannot establish that the native-skill causal path was unchanged. Under the change-impact rule, an unknown impact becomes an explicit residual or widens re-evaluation; it does not establish that the change defeats reuse.
    - It is not a clean successor pass.
- **3.0.5-rc.1 Python native judgment.** Cited support only, through owner byte-equality and rule equality. Its low residuals carry over. Its verdict does not.

**New trials required:** none, because no material changed causal path is established to defeat reuse for the bounded claims. Two observations remain unperformed and may only be claimed if performed:

- current-native-skill execution of the nine SDLC decision classes;
- the planned final-use-01 run, in which a native actor uses the final installed Skills path.

## 4. Where the default, ticket, Skills and context duties are owned

- **SDLC_DEFAULTS.** A selectable projection. It names its deciding owners, and selection belongs to the Product basis; the fixture selects it explicitly.
- **Durable work state.** Owned by TICKETS. Context, restart and reuse are owned by ACTIVATION.
- **Native skills.** `stdo-work`, `stdo-review` and `stdo-ticket` project those owners and state that they do.
- **Purpose Context.** Owns the runtime and catalog.
- **Skills adapter.** Only binds the dependency, and leaves ticket-state writes to the granted Writer.
- **Default projection identity.** The default projection is `a04335…`, the same bytes in A and in all three frame-basis citations.
- **Cross-Product interaction.** I found no authority leak.

## 5. Findings

Severities use the 1 (highest) to 5 (lowest) convention; that the Product binds this scale is assumed, not confirmed.

- **F1 (SDLC, severity 4).**
  - **Issue.** W11 carries the change class, the first changed layer and the no-upstream-drift duty. It is gated on `repair_planned`. But SPEC_METHOD §4 makes intake triage apply to every substantive change, and an `action=work` refactor receives no explicit change-class duty from the SDLC context.
  - **Containment for this exact query.** The admitted contract (W03), DESIGN.md and the companion Python S03 and D25 carry it.
  - **Would revise.** An `action=work` query with no admitted classification.
- **F2 (SDLC, severity 5).** W03 does not state that admission refuses when no durable result surface is available; C03 does, and W39 partly covers it.
- **F3 (Python, severity 5).** C10 triggers measurement "where fit is claimed", which is weaker than ACTIVATION §2 step 3's rule that measurement applies where a capacity is declared. It also lacks the distinction between measured-boundary fit and whole-step fit. W38 in the companion context contains this.
- **F4 (Python, severity 5).** No named fixture input grounds `language_version=3.12`. The fact basis omits it, and the fact is used only to select the family.
- **F5 (SDLC, severity 5).** W12's trigger now lives in its text rather than its guard. That is lawful and more conservative.
- **F6 (SDLC, severity 5).** The meanings of the `adopted_defaults` and `operative_basis` facts changed while the purpose ID `sdlc-workflow/1` stayed the same. The change is declared and the purpose hash changed, so exact-binding reuse of the predecessor is refused.
- **F7 (Python, severity 5).** C04 omits the explicit ticket work-state-authority sentence (§2 above).
- **Adjacent, not judged here.**
  - The v3 SDLC_DEFAULTS requirements file still says "gains no release identity".
  - The README rule counts do not match (35 versus 40 rules, item X-08).

```json
{
  "subjects": [
    {
      "name": "python",
      "index_sha256": "717857ed027b6624f053bbc9bdf4c7319139769d9352c7ca00adc6859ad6ca52",
      "corpus_sha256": "159389bfd1449c9a529c14d3914a112225511eb102cd48b4f85d63e468633b1e",
      "query_sha256": "8ac9ebeaa0b606dd7eb1551543b4008565d596f0aaefaf5ca319f48e646ccf64",
      "status": "supported",
      "evaluator": "Claude activation (environment-reported claude-opus-5-5; CLI metadata authoritative). Cross-family to the OpenAI/Codex Writers. Same family as the prior expectations author and the prior 3.0.5 Python native assessor. No tools used; the exposed advisor tool was not called; no hashes recomputed.",
      "evidence": [
        "INDEX.json raw 4c9ebc08...; CONTEXT.md 98ff870d... (94 selected rules re-read)",
        "SOURCE-DELTA.json 49794291... (only C04 changed in meaning; C14/C17/C23 moved spans with equal span bytes; 15 owners equal)",
        "PRIOR_SOURCE_DELTA.patch 80b81f4c... (TICKETS paragraph inserted at line 727)",
        "Full native A owners: DESIGN_MODULE 741b798e..., TICKETS 2e601f70..., ACTIVATION 56109ffa..., SPEC_METHOD 06d5e8cb..., EVALUATION b856cf04..., FOUNDATIONS 7fe9ecf2..., ASSURANCE 5f6740a3..., others per SOURCES.json",
        "fixture INPUT_FREEZE 2db6a616...; queries/python.json abba1057...",
        "Cited support only: 3.0.5 COVERAGE-STANDING f3a2a9e7...; NATIVE-PARSED ab2b4bd9..."
      ],
      "scope": "Governing-method constraint sufficiency before construction, for the Worker / adopted-DESIGN_MODULE / pure-local Python 3.12 realization_refactor family on this exact query and native A. Excludes future code, typing pass, equivalence, task admission or acceptance, host pickup and release.",
      "residuals": [
        "F3 C10 capacity trigger and fit-distinction wording",
        "F4 language_version grounding",
        "F7 C04 omits explicit ticket-authority sentence",
        "Retained 3.0.5 low residuals (R26, R28, R30, R33, R48, R53, R58, D05 reading)",
        "Unchanged-owner meaning partly reliant on prior Claude judgment (confirmation-bias risk); no exhaustive clause-by-clause re-derivation; attention adequacy unclaimed"
      ]
    },
    {
      "name": "sdlc",
      "index_sha256": "05b5d132a3e2e36f2e021d9b059108eccf646faa78a6a1fc0cffca6627b99cb2",
      "corpus_sha256": "49470f7ac2cecb5dff40ab051ffb03f2bd6bdce07ce158bb3126115ef8527915",
      "query_sha256": "07c7e60fd1d6f9ec89f945959fdb0bf6bc61a5b8eddc148bf7b428e6a3f56598",
      "status": "supported",
      "evaluator": "Claude activation (environment-reported claude-opus-5-5; CLI metadata authoritative). Cross-family to the OpenAI/Codex Writers. No prior supported SDLC verdict was reused. No tools used.",
      "evidence": [
        "INDEX.json raw fe82297b... (all 40 rules read); CONTEXT.md a9c85fda... (20 delivered, W09 and W10 visibly false)",
        "SOURCE-DELTA.json 5cf12b4a... (W01 text and two fact wordings changed; 39 rule objects equal)",
        "REUSE_CUSTODY_AND_DELTA 71351cf1... (W12 guard removed; W36-W40 added vs the 9-case trial)",
        "Full owners: SDLC_DEFAULTS a04335fe..., TICKETS 2e601f70..., ACTIVATION 56109ffa..., EVALUATION b856cf04..., REFERENCE_FRAME 4bf3bb18..., FOUNDATIONS 7fe9ecf2..., others per SOURCES.json",
        "fixture FRAME_BASIS 8d154297..., WORK_CONTRACT ae7bede7...; queries/sdlc.json 5e925a06..."
      ],
      "scope": "Workflow constraint sufficiency before the decision, for executing and recording the admitted bounded refactor through the run carrier under native A defaults (no Executive profile, boundary none). Excludes specialist or technical law (routed via W34 and the Python index), task success and acceptance.",
      "residuals": [
        "F1 change-class / no-drift duty gated on repair_planned",
        "F2 W03 lacks explicit refusal when no durable result surface exists",
        "F5 W12 condition carried in text",
        "F6 fact meanings changed under same purpose ID",
        "Intake-time facts: a test failure discovered during work requires requery (W09/W10 visible only as false dependencies)",
        "Attention adequacy unclaimed"
      ]
    }
  ],
  "findings": [
    {"id": "F1", "subject": "sdlc", "severity": 4, "status": "residual, not falsifying for this exact query", "summary": "W11 gated by repair_planned; action=work receives no explicit SPEC_METHOD §4 change-class / no-upstream-drift duty; contained by W03 admitted contract, DESIGN.md and companion Python S03/D25"},
    {"id": "F2", "subject": "sdlc", "severity": 5, "summary": "W03 omits ACTIVATION Admission's refusal when no durable result surface exists (C03 carries it; W39 partial)"},
    {"id": "F3", "subject": "python", "severity": 5, "summary": "C10 'where fit is claimed' trigger weaker than ACTIVATION §2 step 3 capacity-declared trigger; whole-step/measured-boundary distinction absent; contained by W38"},
    {"id": "F4", "subject": "python", "severity": 5, "summary": "language_version=3.12 not grounded in a named fixture input; affects family selection only"},
    {"id": "F5", "subject": "sdlc", "severity": 5, "summary": "W12 guard removed; trigger kept in text; conservative and lawful"},
    {"id": "F6", "subject": "sdlc", "severity": 5, "summary": "adopted_defaults/operative_basis meanings changed under unchanged purpose_id; declared, and purpose hash change refuses predecessor reuse"},
    {"id": "F7", "subject": "python", "severity": 5, "summary": "C04 compresses the TICKETS paragraph without the explicit ticket work-state-authority sentence; meaning preserved by the actor-account clause"},
    {"id": "ADJ-1", "subject": "adjacent", "severity": null, "summary": "v3 requirements SDLC_DEFAULTS 'gains no release identity' and README rule-count mismatch (X-08); release-facing, not judged"}
  ],
  "source_owner_placement": {
    "SDLC_DEFAULTS": "Selectable projection installed in native A (a04335...); names deciding owners; selected by the Product basis (fixture FRAME_BASIS); not a second constitution",
    "TICKETS_section5_paragraph": "Correctly placed application of ACTIVATION §2/§5/§7 to the selected carrier; ACTIVATION is the single owner; no new carrier requirement or ticket-state authority; RELEASE §9 disposition not judged here",
    "W01": "Faithful rebinding to released native source; non-substitution and no implicit migration preserved",
    "native_skills": "stdo-work, stdo-review and stdo-ticket project TICKETS and ACTIVATION; create no authority; direct Writer sufficiency preserved",
    "purpose_context_and_skills": "Purpose Context owns index, runtime and catalog; the Skills adapter binds only and defers ticket writes to the granted Writer; no cross-Product authority leak found",
    "default_projection_identity": "a04335... identical across A and the three frame-basis citations"
  },
  "prior_evidence_applicability": [
    {"evidence": "Ticket 3-case trial (TC01-TC03; freeze d1d0d270...)", "applicability": "applicable as observations on original subjects for T-01 through T-06", "basis": "12 owner bytes, native work/coordination instructions and W02-W40 meanings equal to A; W01 not deciding; binding-route change is mechanical", "limits": "TC03 staged measurement, not an initial whole-boundary preflight; native source-currentness corroborated after returns; single sequential actor; instruction-bound isolation; fixture provider; clipping/recovery and failed command 025 retained; covered false; semantic unknown not transferred"},
    {"evidence": "SDLC 9-case decision trial (S01-S09; freeze ecfb570b...)", "applicability": "partially applicable as decision-level support for N-05 to N-13 classes; not a clean successor pass", "basis": "Deciding rules W02-W11 and W13-W35 equal; W12 guard removal and W36-W40 additions do not contradict any decision", "limits": "Native stdo-work ee0aac3b vs b7ed03fe and stdo-review 8ccbec09 vs a694b9d0 differ with no supplied delta (explicit residual); decision-use under supplied facts only; dev source and 3.0.5 basis; contexts unassessed"},
    {"evidence": "3.0.5-rc.1 Python native assessment", "applicability": "cited support only via 15 equal owners and 112 equal rule objects; verdict not transferred", "limits": "same-family-as-me confirmation bias; prior low residuals retained"},
    {"evidence": "Ticket-trial exact-query assessments (unknown) and host replay", "applicability": "historical subjects; delivery-mechanics observation only", "limits": "no coverage verdict transfers"}
  ],
  "required_new_trials": [],
  "unperformed_or_excluded": [
    "Current native actor on final installed Skills path using both final-use-01 contexts (unperformed; required only if that actor claim is made)",
    "Nine SDLC decision classes on current native skill bytes (unperformed; residual, not a defeated reuse)",
    "Missing-admission case (no admitted contract) observation; only missing correction authority (TC01) and no-ticket (TC03) were observed",
    "Automatic host pickup (Q06) and native review/handoff on live installed hosts (Q07)",
    "Initial single whole-boundary capacity preflight",
    "Real external-provider effects",
    "Code execution, typing pass, equivalence, task acceptance",
    "Release, tag, asset and publication closure (B); whole-method/C3; universal effectiveness; complete host-context fit; adequate attention",
    "Exception, ODD/UX and live/release branches (excluded by fixture facts)"
  ]
}
```
