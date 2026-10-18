# Deterministic Support Tool Qualification

**Family**: REQ-AC-FDV-*
**Status**: Deferred
**Category**: Verification

This family qualifies the [additional tools](fd-support-tools.md), not the
STDO3.0 methodology or F_P actor judgments. Design, implementation and executed
qualification remain pending. Owners are the exact provisional clauses in the
[source-owner map](fd-source-owner-map.md), consumed through the caller-selected
operative method rather than adopted as a new a_c builder basis.

### REQ-AC-FDV-001 — Qualify observable tool contracts on a real use path

For each claimed operation, bind exact inputs, deterministic output/check
predicate, scope, expected counterexample and method-owner contract. Verify
reproducibility over frozen inputs and preserve the scope/time of external
observations. Exercise the documented ordinary interfaces with F_P Executive,
Worker and Reviewer callers on one real bounded development task, including
actual context/source acquisition, executor boundary, proof/review evidence
and durable return/recording routes selected for that task. Distinguish
contract sufficiency, actual boundary exchanges, runnable path and actor
usability; do not substitute private study success or fixture knowledge. F_P
assessment, required independence and owner disposition are provided by their
existing owners, not by the tools. Each unexercised operation/variant remains
an explicit qualification gap. Owners: [EVAL](fd-source-owner-map.md#eval)
§1/3/6; [ASSURE](fd-source-owner-map.md#assure) §3/13–16.

### REQ-AC-FDV-002 — Qualify refusal, unknown and recovery discriminators

Execute positive and relevant negative/control cases for the inventory below,
with exact tool/method/profile/candidate identities, assertion and execution
provenance, actual supplied context/settings, raw attempts, expected observable
checks/refusals and retained unknowns. Different source conditions must yield
the owner-contract distinctions; an always-refuse or always-pass implementation
cannot qualify them. Demonstrate handoff/resumption from named durable sources
without hidden actor context. These scenarios test the tool response to supplied
rules and observations, not an a_c-owned workflow or semantic truth oracle.
An independent tenant can apply the same carrier-neutral contract without
Graphify, a V3 runtime dependency or study-private machinery. Owners:
[ACT](fd-source-owner-map.md#act) §1 Applicability/2/3/5/7;
[FOUND](fd-source-owner-map.md#found) Results/Conjunction of results;
[ASSURE](fd-source-owner-map.md#assure) §3/13.

### REQ-AC-FDV-003 — Evaluate accepted-result benefit separately

Before claiming improved discovery, quality, consistency or efficiency, compare
matched real tasks with/without the declared tool support under exact
source/method, actor/envelope/settings and outcome/acceptance criteria. Retain
semantic/coverage/acceptance evidence and all material acquisition, F_P authoring,
context preparation, refresh, invocation, failed attempts/retries, repair,
review and decision effort, with measurement boundaries and unknowns. Report
observed differences and limitations rather than inferring a general benefit
from count, graph size, fit or structural success. Owners:
[ACT](fd-source-owner-map.md#act) §6;
[EVAL](fd-source-owner-map.md#eval) §1;
[FOUND](fd-source-owner-map.md#found) Assertions and observation/Change impact
and evidence reuse.

## Scenario and requirement trace

The following is written test-case authority, not executed evidence. FD-nnn
expands to `REQ-AC-FD-nnn`; FDV-nnn expands to `REQ-AC-FDV-nnn`. Each case supplies
the exact applicable upstream contract; the table does not redefine its states,
role duties, result values, applicability or admission policy.

| Scenario | Supplied input/variation and required observable tool response | Trace |
|---|---|---|
| SC-AC-FD-001 Real actor use | One actual bounded task uses ordinary documented operations for Executive preparation/dispatch, Worker source/proof acquisition and Reviewer independent candidate/source/proof access, then captures supplied actor/owner results through the selected carrier. All effective inputs and effect evidence are traceable; no tool-generated semantic/owner verdict appears. | FD-001..013; FDV-001 |
| SC-AC-FD-002 Contract discovery/bases | Exact supported request returns its contract/checked fragment. Unknown operation, unsupported method/profile and ambiguous Product selection refuse with reasons. Tool builder, consumer method and represented v3 subject stay distinct; equal model labels do not create a join. | FD-001,002,004; FDV-002 |
| SC-AC-FD-003 Dirty current state | Relevant dirty/untracked bytes or dependency/configuration change after observation without changing HEAD. A dependent preflight detects the changed supplied precondition; a branch/commit match cannot hide it or silently rebase the request. | FD-002,006,007; FDV-002 |
| SC-AC-FD-004 Grounding and incomplete coverage | Give exact source/record references plus a missing mapping, inferred code edge and methodology-only model. Return actual payload/content or a named gap and coverage boundaries. No inferred governing relation, complete-workspace claim or unaffectedness conclusion follows. | FD-003,004; FDV-002 |
| SC-AC-FD-005 Supplied conditional predicates | Evaluate a declared supported applicability predicate on true, false and missing-premise inputs, plus missing/wrong-subject prerequisite evidence. Preserve the method's exact distinction and F_P judgments separately; no semantic frontier/re-entry choice is made by the query. | FD-004,008,010; FDV-002 |
| SC-AC-FD-006 Context and envelope | Supply locator-only versus acquired records/source, governing closure with qualifications/residuals, exact permitted late reads, denied acquisition, exceeded capacity and unknown host context. Assemble/check the selected packet, measure only the declared boundary and preserve gaps/owner refusals without silent trimming or sufficiency claims. | FD-003,005; FDV-002 |
| SC-AC-FD-007 Admission and grants | Candidate packet/ticket/role without the selected admission evidence or granted effect refuses dispatch. Exact Product-bound mechanism/allowed override and supplied grant permit only the named tools/territory. Unauthorized recording/Executive or Reviewer mutation refuses under the selected role contract. | FD-006,007,011; FDV-002 |
| SC-AC-FD-008 Transport and uncertain effect | Distinguish receipt, schema-valid output, F_P return, observed effect and observed end. Lost response/timeout/cancel/interruption with partial write preserves upstream unknown-effect evidence and material retry preconditions. A termination request never proves completion/rollback. | FD-007,008,012,013; FDV-002 |
| SC-AC-FD-009 Closed return binding | Capture exact valid, stale, wrong-subject/basis, duplicate and conflicting returns. Preserve raw original predicates/domain outcomes; report consumer-binding errors and gaps without rewriting old verdicts, counting duplicate independence or fabricating unperformed results. | FD-008,010; FDV-002 |
| SC-AC-FD-010 Independent review acquisition | Under supplied exposure/independence conditions, record source-derived expectations before candidate exposure and permit a nonauthor Reviewer to acquire exact candidate, tests/fixtures, governing source and comparisons directly. Author summary/new session is not certified independent. The tool returns acquisition/diff facts, never review severity or disposition. | FD-003,005,009; FDV-001,002 |
| SC-AC-FD-011 Declared checks/conjunction | Execute a qualified supplied structural/proof predicate and method-owned operator. Preserve wrong-basis inputs, missing planned assessments, uncovered obligations, original domain outcomes and conflicts exactly. A necessary-condition pass cannot satisfy a stronger predicate; unsupported operations refuse. | FD-001,004,008,010; FDV-002 |
| SC-AC-FD-012 Existing state and authorized records | Project the named work/evidence carrier and apply one already-authorized actor/owner record through its Writer interface with preimage/grant checks. Preserve original ruling versus interpretation; a recommendation/commit/review event supplies no automatic disposition/closure/release, and generated views do not own work state. | FD-011; FDV-002 |
| SC-AC-FD-013 Refresh and fresh-actor handoff | Edit material source/frame inputs and compute affected support under supplied impact/reuse rules. Preserve originals/frozen studies and demonstrably valid survivors; incomplete dependencies leave uncertainty. A fresh actor resumes from current named sources without replay or blind retry of unreconciled effects. | FD-002,004,012; FDV-002 |
| SC-AC-FD-014 Notifications and resource evidence | Deliver return/exception/basis-change/checkpoint events and test declared bounded fallback when notifications fail. Retain failed/partial/retried attempts, units, unknown backend usage, elapsed versus summed intervals and selected limit checks without double counting or universal quotas. | FD-007,013; FDV-002 |
| SC-AC-FD-015 Matched usefulness | Compare matched tasks with/without support and retain bounded source/semantic/accepted-outcome and total cost evidence, including acquisition/authoring/refresh/repair/review and unknowns. Report actual results without extrapolating savings from fewer calls. | FD-013; FDV-003 |

This inventory adds no tool implementation, passing scenario, semantic
acceptance, method adoption, operational qualification or release claim.
