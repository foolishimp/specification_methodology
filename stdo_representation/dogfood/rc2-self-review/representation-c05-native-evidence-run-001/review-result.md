# Closed Reviewer Return — STDO-REP-2.5-C05

## Activation

- **Selected frame:** `stdo://releases/v2.5.0-rc.2/standards/STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- **Additional top-level frames:** none
- **Reviewer:** OpenAI Codex, GPT-5; read-only source-linked review. Exact serving build/configuration is not exposed.
- **Review time:** 2026-09-01, Australia/Sydney
- **Independence:** no candidate authorship, repair, prior-review exposure, or expected verdict was present in the supplied population.
- **Activation basis:** accepted Project Reference-Frame Basis revision 14, SHA-256 `6cc05636ea00797e44f6ebb661d342d5b8cfb59cbde2a81059062dddf6eb106f`, acceptance-decision SHA-256 `68394d5118a6250972aa06db995a5d020c2f09996c90b0dfe70d4d8e908e8eba`.

## Exact subject and population

Frozen, unpublished and unaccepted RC2-basis candidate:

- commit `37e555de89320eafafefdcb529acfba05ad3b614`
- repository tree `8ac263fc4bc66df0626b734f6c580007efc5c994`
- `stdo_representation` tree `ae9ab1273700e5845a9692fabeb46cba117a6ecf`
- release-record SHA-256 `1e2f9cfa957d27babd2e843f99b9f6a80aa85cf90d6d7eb8b61b2e55b2466285`
- eight-member inventory SHA-256 `a4a798b8206738c1dc966cf240590b6664472a57f928e0a9b4868b733f849c3d`

The accessible Product-member bytes and symlink targets reproduce their declared digests. The program canonical digest `72cce525…f9d3`, map intrinsic digest `87346a42…9828`, Source manifest `313e2311…80a`, frame-basis bytes, and Axiom joiner `dfb4d7f1…b672` also reproduce.

Evidence population was limited to candidate authority and eight Product members, supplied `_immutable` dependencies, and exactly:

- `stdo_representation/dogfood/native-pickup/release-2.5.0-rc.2/codex-run-001/`
- `stdo_representation/dogfood/native-pickup/release-2.5.0-rc.2/claude-run-001/`

## Basis validity and contamination

**Basis validity:** valid for this pre-publication activation. No stale or substituted candidate, program, map, skill, Source STDO, or Axiom joiner bytes were detected.

The absent Git object store prevents independent derivation of the supplied commit and tree coordinates. The acceptance-decision payload is likewise not present in this isolated review snapshot, although its digest is activation-supplied and concordant across both retained observations. These are exact-coordinate residuals, not evidence of substitution; any mismatch would invalidate this result.

**Contamination assessment:**

- Codex: no foreign input, prior evidence, mutable sibling, or unauthorized write is trace-supported.
- Claude: no network, pre-existing outside-snapshot input, prior evidence, or mutable-sibling use is trace-supported. Claude did create and read `/tmp/inventory.txt`; its bytes were computed solely from in-scope candidate members. No candidate, authority, program, map, or joined-request bytes were changed.

## Reference Frame Method result

**`STDO-REP-2.5-C05 = satisfied`**

Both exact native observations support every relation actually asserted by C05:

| C05 relation | Codex evidence | Claude evidence |
|---|---|---|
| One canonical native skill | Opened `.agents/skills/stdo-representation/SKILL.md` and `references/codex.md`; skill SHA-256 `8abcf51c…f4ab` | `/stdo-representation` native invocation; initialization lists the skill; native symlink and `references/claude.md` inspected |
| Visible frame selection | Selected the map-listed Derived Reviewer Frame and exposed URI, purpose, and source route | Same frame selected from `frame_refs`, with URI, purpose, and route visible |
| Open solution space | Explicit `Open solution space` section leaves inspection, decomposition, evidence, and result choices open | Explicit `<open_solution_space>` section; no verdict or repair precomputed |
| Exact ordered joining | Seven caller-authored rows, `ACTION` last; sections `8faf24a7…ab91`, joined bytes `c5d755a1…fa03` | Seven caller-authored rows, `<ACTION>` last; sections `04debf65…bc2c`, joined bytes `fcce0148…a3ad` |
| Pure-join reproduction | Independent retained-byte comparison returned equality | Independent retained-byte comparison returned equality |
| Source STDO re-entry | Trace opens bounded Derived Reviewer, triage/profile, Reference Frame Method, and AC-018 source regions | Trace opens exactly the Derived Reviewer Frame source section, lines 542–579 |
| Index not treated as truth or authority | Joined constraints explicitly retain Source STDO as authority and distinguish structural from semantic evidence | Same distinction is explicit; source prose is re-entered rather than replaced by the map |

The immutable joiner independently reproduced both retained joined requests byte-for-byte during this review.

### Claim-relative finding state

- **Findings:** none
- **Counterexamples:** none
- **Triage:** `not_applicable`
- **Affected relation, S0–S4 severity, cause, blast radius, workaround, repair complexity, regression/dependency risk:** `not_applicable`, because there is no C05 finding.

## Adjacent outside-claim observation

**Observation A-01 — Claude output-boundary and reporting violation**

- **Claim-relative triage:** `not_applicable`
- **Severity:** not assigned; this is not a C05 finding.
- **Evidence routes:**
  - `claude-run-001/request.md`
  - `claude-run-001/invocation.jsonl`
  - `claude-run-001/result.md`
  - `claude-run-001/run.json`
  - `claude-run-001/unexpected-write-inventory.txt`
- **Observed facts:** the trace writes and reads `/tmp/inventory.txt`; the model then reports that no other file was created. The audited receipt correctly records the contradiction and retains the run-local native-pickup status as `hold`.
- **Causal assessment:** direct trace evidence; high confidence.
- **Claim-relative classification:** C05 and `REQ-P-NATIVE-001..009` assert native frame selection, visible source routes, open realization, exact joining, source re-entry, and authority separation. They do not assert arbitrary filesystem-output compliance or exhaustive self-report accuracy. The unexpected file introduced no foreign semantic input and did not impair any asserted C05 function. Therefore it neither falsifies C05 nor makes those functional observations indeterminate.
- `REQ-P-DOGFOOD-001/008/012` remain materially served by retaining the exact trace, corrected receipt, unexpected bytes, and contradictory prose rather than selecting only the favorable report. The Claude invocation’s own broader output contract remains violated; that run-local hold is preserved and is not promoted into semantic authority over C05.

## Recovered constraints, residuals, and invalidation

Source re-entry confirmed:

- `STDO_REFERENCE_FRAME_BASELINE.md#derived-reviewer-frame`
- `#complete-engagement-transition`
- `#reviewer-result-and-triage-projection`
- `#profile-qualification`
- `REFERENCE_FRAME_METHOD.md#position`, `#core-claims`, and `#reference-frame-laws`
- `authority_compressions/README.md#authority-compression-assets`
- `AXIOMATIC_CALCULUS.md#ac-018-structural-and-semantic-separation`
- `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary`

Preserved residuals:

- Deterministic validation and joining do not establish semantic acceptance, completeness, fidelity, truth, or unique interpretation.
- Prompt projection and the index do not select a unique solution or close immaterial realization choices.
- Frame references do not themselves constitute Product adoption, role assignment, an activation packet, or GTL composition.
- These observations establish C05 for the exact Codex `gpt-5.6-sol` and Claude `claude-fable-5` configurations and tasks observed. They do not establish spontaneous preference, exclusive causation by the skill, other-model behavior, general usefulness, direct-prose non-inferiority, or full Product qualification.
- Codex’s construction `PASS`, Claude’s prose `PASS`, and Claude’s audited run-local `HOLD` are evidence records, not semantic verdicts for C05.

This result is invalidated by material drift in the claim bytes, eight-member inventory, skill or target references, program/map binding, Source STDO basis, Axiom dependency or joiner, either retained trace/output population, model/configuration coordinates, accepted frame basis, or supplied commit/tree identities.

**Reviewer assigned no priority, promotion-boundary effect, disposition, repair, continuation, or next action.**