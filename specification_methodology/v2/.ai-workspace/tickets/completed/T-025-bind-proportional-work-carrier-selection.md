# T-025 - Bind Proportional Work-Carrier Selection

- id: T-025
- title: Bind proportional work-carrier selection and prohibit automatic ticket creation
- type: bug
- ticket_category: ordinary
- status: completed
- review_status: satisfied
- goal: downstream-stdo-operability
- change_intent: >-
    Make carrier lifetime decide whether governed work uses a durable ticket,
    sprint-local entry, or run-scoped execution contract so admission remains
    explicit without generating ticket or interaction churn.
- change_class: requirement_reprice
- re_entry_point: specification/standards/TICKET_METHOD.md#work-carrier-to-execution-rule
- triaged_at: 2026-09-01
- created_at: 2026-09-01
- updated_at: 2026-09-01
- completed_at: 2026-09-01
- priority: current
- owner: specification_methodology
- pen_holder: codex
- work_authorization: direct_human_authorization_2026-09-01
- target_truth: >-
    Every governed execution uses one admitted run-scoped contract, while a
    durable ticket is created only when work or an obligation needs independent
    identity, coordination, state, or closure beyond its admitted sprint or,
    outside a sprint, beyond the current run.
- superseded_truth: >-
    Ticket-shaped execution-contract wording can be interpreted as requiring a
    durable ticket and separate turn for ordinary one-run work.
- closure_law: >-
    Close only when raw Ticket Method, its authority compressions, downstream
    guide and skills, and focused scenario checks select the smallest lawful
    carrier; prohibit automatic ticket creation and model self-admission; permit
    same-invocation draft, admission, and execution; and preserve durable
    obligations beyond the run.

## Evaluation Criteria

1. Existing admitted tickets are reused rather than duplicated.
2. Small work inside an admitted sprint may use a manifest-local iteration
   entry without a durable ticket.
3. One-run work under existing authority may use a run-scoped contract without
   creating a durable ticket or mandatory additional turn.
4. Work or an obligation that must outlive its admitted sprint or, outside a
   sprint, its current run receives one authorized durable ticket.
5. Ticket creation, location, lane, and `active` status never imply execution
   admission.
6. A drafted or rejected contract cannot reach construction, and a model cannot
   infer admission from its own draft or widen an exact human override.

## Non-Closure Conditions

- invoking `stdo work` automatically creates a durable ticket;
- same-invocation admission is refused only because drafting happened in that
  invocation;
- a sprint-local change receives a duplicate durable ticket;
- an obligation outlives its applicable run-or-sprint boundary without a
  durable carrier;
- ticket state is treated as execution-contract state;
- compressed or onboarding projections retain the ambiguous automatic-ticket
  path; or
- tests prove only phrase presence without the carrier-selection relation and
  refusal cases.

## Proof Surface

- exact raw-to-compression digest and semantic-congruence checks;
- a parsed carrier-selection decision table with exact positive and refusal
  rows;
- focused guide and skill assertions;
- fresh no-ticket, reuse-ticket, sprint-local, durable-obligation, drafted-stop,
  and same-invocation forward scenarios; and
- full normal and optimized repository tests plus formatting and diff hygiene.

## Release Boundary

This ticket changes mutable successor Ticket Method bytes and their subordinate
projections. It does not alter RC2 or itself accept a release cut. Direct human
Product authority separately authorizes publication of the exact aligned
`specification_methodology/v2.5.0-rc.3` successor after candidate closure and
exact-cut qualification.

## Completion Evidence

- Exact Ticket Method SHA-256:
  `6924e3284be3375af3514cdf0f810b53e8ac282cb96116ea2d721e9b84b75ba3`.
- Ticket Method compression SHA-256:
  `c551c3fd8851c2a1a2f885eb41b5694886c3ade38948d6caf5fdf895351d91ff`.
- Aggregate STDO compression SHA-256:
  `f0f135162231543d4448a6f335db401a36f0c391e2e72b968c09df9c4d679085`.
  Both compression headers bind the exact raw Ticket Method digest.
- Focused executable tests parse and prove the ordered first-match relation for
  missing upstream authority, exact-ticket reuse, boundary-crossing durable
  state, admitted-sprint-local work, and one-run intake. They also prove
  distinct admission evidence, same-invocation execution after admission,
  drafted/rejected stop, and durable residual preservation without automatic
  ticket creation.
- Independent cold review of the frozen raw/compression/skill relation returned
  `satisfied`; P0, P1, and P2 are all zero. It specifically confirmed that no
  compression-only Product-policy trigger or overlapping selector row remains.
- The exact 52-member standards aggregate is
  `8492f66bba93a1e4559b2275f01df277b5e49c24bc0a76feb028e85e4bdf5c2f`.
- The full candidate suite passes 119 tests normally and 119 under Python
  optimization, with only the expected unpublished-RC3 exact-tag check
  skipped. Ruff, Black, and diff hygiene pass.

The proportional carrier law is closed. It does not itself publish or accept
RC3; T-026 owns the authorized release transition.
