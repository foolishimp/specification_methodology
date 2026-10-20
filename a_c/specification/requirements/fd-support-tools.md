# Deterministic Support Tools for F_P Actors

**Family**: REQ-AC-FD-*
**Status**: Active
**Category**: Capability

This family specifies additional tools supporting F_P Executives, Workers and
Reviewers. Active records T-008's operative HOW and provisional implementation,
with bounded implementation/review/technical integration complete; it asserts
neither requirement satisfaction nor complete qualification. Earlier Deferred
wording describes T-007's specification-only cut. Current evidence and gaps are
in the [handoff](../../.ai-workspace/qualification/t008/handoff-001/README.md). STDO3.0 owns the methodology and its contracts. The
[source-owner map](fd-source-owner-map.md) binds the exact provisional derivation
reference and the owner clauses cited below. Runtime use consumes the caller's
exact selected method/profile through a declared supported binding, without
adopting that provisional candidate or changing a_c's installed builder basis.

Every operation has an exact versioned input/output contract and reproducible
checks over its supplied inputs. External observations retain their identity,
scope and time. A named source/carrier/dispatch/write operation is distinct from
an `F_D[v]` evaluation/proof returning a judgment; neither makes the invoked
F_P operation or its semantic answer deterministic. Existing AC-R-001..015 and
the separate F_P source-to-model authoring capability remain applicable.

### REQ-AC-FD-001 — Discover supported tool contracts

**Input:** an optional requested operation, exact method/profile and capability
query. **Output/checks:** a versioned inventory of public operations, input/output
contracts, compatible method/profile bindings, supported representations,
checked fragments, effect/access prerequisites, qualification scope and explicit
unsupported cases. Unknown or unsupported requests return their exact reason
and unmet contract. **Limit:** availability selects no method, frame, role,
workflow or next action; the interface must be usable by all three F_P actors
without private study knowledge. Protocol, CLI/MCP, schema and provider are HOW.
Owners: [PDEF](fd-source-owner-map.md#pdef) §8/11;
[RF](fd-source-owner-map.md#rf) RF-016;
[ASSURE](fd-source-owner-map.md#assure) §13.

### REQ-AC-FD-002 — Bind and observe exact workspace inputs

**Input:** caller-selected Product scope/definition, exact operative method and
optional profile, declared material observation scope and access grant.
**Output/checks:** resolved identities/content digests and observation evidence
for the selected definition, method, subject, configuration/dependencies and
current relevant workspace bytes, including dirty/untracked content. Distinguish
the tool's builder basis, consumer operating basis and represented subject cuts;
report ambiguous, inaccessible, changed or unsupported bindings without
substitution. Reobservation compares the supplied material preconditions before
a dependent tool effect. **Limit:** branch/HEAD alone is not mutable state;
observation establishes only the acquired scope/time and neither adopts latest
nor composes sibling Products/bases. Owners:
[PDEF](fd-source-owner-map.md#pdef) §4/12;
[RF](fd-source-owner-map.md#rf) RF-005;
[ACT](fd-source-owner-map.md#act) §5/7.

### REQ-AC-FD-003 — Resolve records, source and grounding

**Input:** exact model/record/source identities, selected mappings or search
scope and permitted acquisition routes. **Output/checks:** found record payloads,
actual source content and their exact routes/digests, original grounding,
owner/mapping coordinates, coverage dispositions and unresolved boundaries.
Literal/structural searches identify their scope; missing, ambiguous, stale,
wrong-basis or ungrounded references return the relevant gap. Workers and
Reviewers can acquire raw deciding source directly rather than relying on an
Executive/author summary. **Limit:** a locator or manifest is distinct from
acquired content. Search, code edges and extraction confidence cannot author
semantic/governing mappings or establish fidelity. Owners:
[ACT](fd-source-owner-map.md#act) §2 Acquisition/Standalone scope;
[PDEF](fd-source-owner-map.md#pdef) §11;
[EVAL](fd-source-owner-map.md#eval) §1–3.

### REQ-AC-FD-004 — Query declared dependencies, impact and coverage

**Input:** exact selected model(s), caller-selected seeds, authored typed
dependency/impact/coverage relations, conditional predicates or already-recorded
applicability, and explicit cross-model identity/translation rules where used.
**Output/checks:** reproducible closure/path/impact/coverage results, included
and missing declared obligations/dependencies, predicate results only for the
supported supplied decidable contract, and qualifications/residuals/boundaries.
Show computed facts separately from supplied F_P judgments and owner rulings.
**Limit:** F_P selects material relations and interprets unresolved applicability;
the tool does not infer semantic edges, prescribe re-entry or select a frontier.
An absent path in incomplete coverage cannot establish non-influence. Owners:
[FOUND](fd-source-owner-map.md#found) Change impact and evidence reuse;
[RF](fd-source-owner-map.md#rf) §6/8/10;
[ACT](fd-source-owner-map.md#act) §1 Applicability;
[SPEC](fd-source-owner-map.md#spec) §4.

### REQ-AC-FD-005 — Assemble and check selected actor context

**Input:** caller-selected frame/configuration and exact method packet contract,
subject/basis, seeds and governing dependency semantics, allowed acquisition
routes, supplied role/authority and actor envelope. **Output/checks:** an exact
projection of the supplied binding with actual acquired record/source content,
source references, declared closure and boundaries; a manifest of what was
supplied versus still to be acquired; and scoped completeness/identity/fit
checks under the selected contract. Where context capacity is declared, measure
its stated boundary/unit before read, retaining any unmeasured/unknown host
context. Preserve the selected method's qualifications, result relation and
stop/refusal semantics. **Limit:** do not invent packet fields as a second method,
silently truncate required content or claim semantic sufficiency from closure,
size or schema. Exact late acquisition is visible and follows the supplied
method contract. Owners: [RF](fd-source-owner-map.md#rf) §11, RF-013/014;
[ACT](fd-source-owner-map.md#act) §2;
[EXEC](fd-source-owner-map.md#exec) §19 only when that profile is selected.

### REQ-AC-FD-006 — Preflight a Product-bound execution contract

**Input:** caller-supplied work contract, governing outcome/grant, exact admission
binding/checks and any existing admission or permitted override evidence,
operation/tools/territory/envelope and named durable result/evidence surface.
**Output/checks:** deterministic preflight findings over those inputs and
admission evidence obtained from the selected Product-bound mechanism where
invoked, bound to exact contract identity and decision authority. Report missing
or mismatched required support before dispatch; retain draft and admitted
coordinates separately under the method's own contract. **Limit:** a successful
shape/context check, role name, ticket state or tool invocation cannot mint
admission or work authority. The tool neither drafts a new grant nor admits the
upstream outcome. Owners: [ACT](fd-source-owner-map.md#act) §1 Admission;
[TICK](fd-source-owner-map.md#tick) §5.

### REQ-AC-FD-007 — Dispatch, notify and observe under a supplied grant

**Input:** exact preflighted activation/admission, selected executor operation,
existing grant, permitted tools/territory, material preconditions, effective
context/settings and selected attempt/resource/observation conditions.
**Output/checks:** invocation identity, actual supplied payload/settings,
acknowledgments, output/partial-output and effect/termination observations with
scope/time, retained attempts and decision-relevant return/exception/basis-change
notifications. Check material bindings before the named effect and expose
changed preconditions without silent rebase. **Limit:** the deterministic
wrapper does not make F_P output deterministic or semantic evidence of success.
Requests, delivery, evaluation, intended effects and their observed end remain
separate under the selected method; timeout/cancel/interruption preserve its
unknown-effect semantics. Fallback observation is bounded by supplied conditions,
not a mandatory polling controller. Owners: [ACT](fd-source-owner-map.md#act)
§1/3 Effects/5; [EXEC](fd-source-owner-map.md#exec) §6 if selected.

### REQ-AC-FD-008 — Capture and check a closed return

**Input:** returned payload/transport evidence, original activation and return
contract, expected consumer, exact subject/basis and supplied currentness,
dependency and independence predicates/evidence. **Output/checks:** preserved raw
return and provenance, deterministic binding/format/currentness findings and
the exact declared evaluations, predicates, domain outcomes and residuals that
were actually returned. Identify stale/wrong-subject/wrong-basis, missing,
duplicate and conflicting evidence without dropping it; expose non-consumable
support/gaps to the declared consumer. **Limit:** do not relabel a historical
verdict as a new verdict, manufacture a result for an unperformed evaluation or
treat schema validity as semantic assessment/acceptance. A transport failure is
reported separately using the selected method contract. Owners:
[FOUND](fd-source-owner-map.md#found) Results/Conjunction of results;
[RF](fd-source-owner-map.md#rf) RF-012;
[ACT](fd-source-owner-map.md#act) §3/7;
[EVAL](fd-source-owner-map.md#eval) §4.

### REQ-AC-FD-009 — Prepare independently acquirable review evidence

**Input:** exact review claim/candidate and composition boundary, caller-selected
source, comparison subjects, proof/evidence population and method-owned
independence/exposure contract. **Output/checks:** independently resolvable raw
authority/candidate/proof acquisition routes, acquired content where requested,
exact byte/record comparisons, and separate assertion/expected-result versus
execution provenance. Support expectation recording before candidate exposure
and preserve the actual acquisition/exposure record under the supplied contract.
Workers can acquire their implementation/proof context; Reviewers can inspect
the actual candidate, tests/fixtures and source without author-only privileges.
**Limit:** diffs and trace/binding checks are not semantic findings, an independent
verdict or adoption of a review recommendation as disposition. Owners:
[EVAL](fd-source-owner-map.md#eval) §1–4/6;
[ASSURE](fd-source-owner-map.md#assure) §3/10/13–16;
[EXEC](fd-source-owner-map.md#exec) §9/10/17/19 if selected.

### REQ-AC-FD-010 — Execute declared checks and method-owned joins

**Input:** exact subject/observations, selected executable or reproducible
decidable predicate/proof contract and its provenance/domain/limits, or a
selected method-owned conjunction/translation with required coverage and inputs.
**Output/checks:** reproducible `F_D[v]` judgments for the properties actually
evaluated, counterexamples/gaps, and joins computed only under the supplied
qualified operator. Preserve source predicate, original domain outcomes,
not-performed assessments, uncovered obligations and incompatibilities as the
owner contract requires. Retain assertion/observation and execution identities.
**Limit:** do not invent an algebra or stronger claim, turn a necessary-condition
pass into full satisfaction, execute an unsupported arbitrary calculus operation
or replace F_P/owner judgment. Owners: [AC](fd-source-owner-map.md#ac) §5;
[FOUND](fd-source-owner-map.md#found) Results/Conjunction of results/Assertions
and observation; [EVAL](fd-source-owner-map.md#eval) §1/2;
[ASSURE](fd-source-owner-map.md#assure) §10.

### REQ-AC-FD-011 — Project and record existing work/evidence facts

**Input:** selected authoritative work/evidence carriers, caller-selected view,
or an already-authorized actor/owner record and exact named Writer interface,
grant, target preimage and update conditions. **Output/checks:** source-linked
projections of existing work, progress/support, residuals and next-action
scope/support/owner; for an authorized write, the exact applied record and
observed effect/result identity or refusal. Preserve original owner wording
separately from interpretation and method-owned distinctions among verdict,
recommendation, disposition, checkpoint, closure and release. **Limit:** create
no rival task ledger, owner decision, role transition or continuation grant;
the tool records a supplied decision, never mechanically adopts a review
recommendation or mutates as an F_P Executive/Reviewer. Owners:
[PDEF](fd-source-owner-map.md#pdef) §8;
[TICK](fd-source-owner-map.md#tick) §7;
[ACT](fd-source-owner-map.md#act) §5;
[EVAL](fd-source-owner-map.md#eval) §4;
[EXEC](fd-source-owner-map.md#exec) §6 if selected.

### REQ-AC-FD-012 — Compute affected refresh and prepare reusable handoff

**Input:** old/current source observations, exact dependency/impact declarations,
declared invalidators, existing results/rulings and caller-selected recovery or
reuse contract. **Output/checks:** source/derived differences, affected projection
and evidence candidates, missing dependency coverage, method-prescribed
invalidation/applicability check results where decidable, and a reconstructable
handoff of still-applicable support, original records/successors, residuals and
unreconciled effects. Reacquire named current inputs for the next dependent
action; retain partial writes rather than assuming a reset. **Limit:** do not
erase history/frozen studies, rewrite old judgments onto new subjects, infer
unaffectedness from absent edges, or require replay/rebuild of valid unchanged
support merely because a session/role changed. F_P resolves unsupported semantic
impact or preservation premises. Owners: [FOUND](fd-source-owner-map.md#found)
Change impact and evidence reuse; [RF](fd-source-owner-map.md#rf) §10;
[ACT](fd-source-owner-map.md#act) §5/7;
[TICK](fd-source-owner-map.md#tick) §7.

### REQ-AC-FD-013 — Retain attempt, usage and uncertainty evidence

**Input:** invocation/acquisition/check/refresh/repair/review attempt observations
and selected accounting/resource contract. **Output/checks:** bound attempt and
cost records with units, measured scope, elapsed versus summed actor intervals,
available usage/cache counters, partial/failed calls, unknown counters and any
declared limit-check result. Aggregation is reproducible without double counting;
anticipated costs remain separate from observations. **Limit:** unavailable
backend usage stays unknown, selected limits are not universal quotas, and
fewer calls or faster deterministic checks do not prove lower accepted-result
cost or improved F_P quality. Owners: [ACT](fd-source-owner-map.md#act) §6;
[EVAL](fd-source-owner-map.md#eval) §1;
[SPEC](fd-source-owner-map.md#spec) §8.
