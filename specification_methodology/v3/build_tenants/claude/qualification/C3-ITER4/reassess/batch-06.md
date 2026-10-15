# I4-04 reading batch 06

Rows: 20. Members: ['TICKET_METHOD.md', 'UX_METHOD.md']. Each row gives the predecessor section at the installed rc.2 and the successor locus text at the current tree, verbatim.


### Row `TICKET_METHOD.md#impacted-interface-review-checklist` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#impacted-interface-review-checklist` at rc.2:

```text
For a core-interface, carrier, or authoritative-contract migration, the ticket
must include an `Impacted Interface Review Checklist` before tests can be used
as closure evidence.

This checklist is a named walk of every live interface that can still bypass,
reinterpret, replay, or project the migrating truth path.

At minimum it should enumerate, when they exist:

- the source-carrier builder
- closure/register/projection builders
- deepest semantic kernel and adapter boundaries
- public wrappers, bootstrap, replay, ingest, resume, and query entrypoints
- prompt/report/projection/read-model surfaces
- constructor/materialization paths
- proof lanes and negative-proof fixtures

Each checklist item must state what counts as closure for that interface.

Examples:

- “`<conformance-module>::consume_projection` consumes the admitted carrier or
  projection and does not import raw helper authority”
- “`<query-module>::project_domain` exposes a read model only and does not
  silently rebuild the carrier when publication is absent”
- “`<gap-module>::build_canonical_gap` does not aggregate open payload rows into
  an independent closure decision”

Review rules:

- a checked box asserts truth on the current tree, not merely intended
  direction
- if review shows a checked interface item is false, the ticket is not
  closure-ready
- if an interface is intentionally deferred, the ticket must name the successor
  ticket or leave that item unchecked
- compatibility shims do not satisfy the checklist unless they are explicitly
  justified as retained compatibility
- for `inside_out_hard_break`, the checklist must describe the seam inventory
  before tests are used as closure evidence
- for `fundamental_re_adoption`, the checklist must cover inherited modules and
  interfaces being carried, dropped, or rewritten; implicit carry-forward does
  not count
```

Successor, `TICKETS.md#impacted-interface-review-checklist`:

```text
For a core-interface, carrier or authoritative-contract migration, the
ticket includes an `Impacted Interface Review Checklist` before tests can be
used as closure evidence. The checklist is a named walk of every live
interface that can still bypass, reinterpret, replay or project the
migrating truth path (P4b, P6; rc.2 #impacted-interface-review-checklist).
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
```


### Row `TICKET_METHOD.md#implementation-migration-category` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#implementation-migration-category` at rc.2:

```text
If `ticket_category: implementation_migration`, the ticket must carry both:

1. an explicit migration declaration block
2. a hard migration checklist

This is not optional commentary. It is part of the ticket authority.

`SPEC_METHOD.md` defines the migration law. This ticket category defines the
minimum ticket-local declaration and checklist that a reviewer can check before
accepting a closure claim on one concrete work item.

The ticket must explicitly declare:

- the migration strategy used for this work item
- the exact affected migration scope
- every explicitly excluded or disjoint Product or compatibility scope and its
  deterministic routing relation
- the old truth path or superseded contract
- the new truth path or authoritative contract
- the producer set for the old and new path
- the consumer set for the old and new path
- every projection, report, status surface, and proof surface derived from that
  contract family
- the closure law for the migration

At minimum, the ticket must carry this checklist in live markdown form:

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

This ticket category is the local ticket-method enforcement surface for the
inside-out migration law defined in `SPEC_METHOD.md`.

The required field is:

- `migration_strategy`
- `library_usage`

Allowed values are:

- `inside_out_hard_break`
- `fundamental_re_adoption`

Allowed `library_usage` values are:

- `none`
- `consume`
- `extend`

If `library_usage: consume` or `library_usage: extend`, the ticket must name
the governing reusable library/commonization surface in `governing_library`.

If `library_usage: none`, the ticket must explain in `library_rationale` why:

- no existing reusable surface applies, or
- the pattern is still boundary-specific, or
- this is not yet a lawful recurrence/commonization candidate

For `ticket_category: implementation_migration`, closure is blocked while the
old authoritative interface still passes in normal execution within the
declared affected scope unless the ticket explicitly declares a retained
compatibility feature. A deterministically routed, non-overlapping Product scope
outside the declared affected scope remains governed by its own current
authority.

That means:

- the old path may not remain silently authoritative within the affected scope
- mixed old/new green tests do not count as migration completion
- any retained old path within the affected scope must be named as
  compatibility rather than current native truth
- retained compatibility must be justified in the ticket itself rather than
  inferred from surviving code
- proxy or partial implementations do not satisfy migration closure
- if a ticket was marked `completed` and later review shows checked closure
  items are false on the current tree, the ticket must be reopened or an
  explicitly linked successor ticket must be created; a false closure claim is
  a ticket-method defect, not just a code defect

An intermediate Product-slice milestone inside an open implementation-migration
ticket may be accepted under the path-relative promotion rule in
`SPEC_METHOD.md`. Its identity and acceptance criteria must derive from Product
plus every causally applicable live requirement, accepted design relation, and
retained predecessor claim; ticket wording cannot narrow that authority away.
The ticket remains active and must not claim migration closure until the
migration checklist and final closure law are satisfied.

Active ticket status does not renew the accepted slice's exhausted growth
authority. Work that only discharges already admitted removal, demotion, and
migration-closure proof obligations may continue within their existing bound
without claiming further Product progress. Further material producer or
consumer growth requires another still-live basis admitted under
`STDO-UP-013`; ticket activity alone is not that basis.
```

Successor, `TICKETS.md#declaration-and-checklist`:

```text
A ticket with `ticket_category: implementation_migration` carries both an
explicit migration declaration block and a hard migration checklist. Both
are part of the ticket authority, not optional commentary.
[SPEC_METHOD §7](SPEC_METHOD.md#7-migration) defines the migration law;
this category defines the minimum ticket-local declaration and checklist
that a reviewer can check before accepting a closure claim on one concrete
work item, and is the local enforcement surface for the inside-out
migration law of SPEC_METHOD §7 (P6, P4b, P3; rc.2
#implementation-migration-category).

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
```

Successor, `TICKETS.md#closure-of-a-migration-ticket`:

```text
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
```

Successor, `SPEC_METHOD.md#constitutional-migration-options`:

```text
Core interface and major implementation replacement work has two lawful
constitutional strategies (P3, P6; rc.2 #constitutional-migration-options).
Inside-out hard-break migration applies when the project remains on the
same implementation line and the authoritative source truth is being
replaced in place; the work proceeds from the source carrier outward
through a sequence of deliberate breaks and repairs. Fundamental
re-adoption migration applies when the rewrite is major and the project is
intentionally re-deriving itself on a materially different implementation
basis, such as a new runtime model, carrier model, type system, execution
substrate or realisation tree; the prior implementation is moved sideways
and treated as reference material, not live authority.

Where bounded evolution and fundamental re-adoption are both lawful and
feasible, and a working predecessor can reach the admitted product outcome
without retaining competing or ambiguous authority, evolution on the
supported product path is the rebuttable selection presumption. This does
not require continuing an unsafe or constitutionally inadmissible
predecessor path; it conserves accepted predecessor semantics and product
feedback, and it does not require preserving an internal implementation or
public mechanism that product authority explicitly supersedes. When bounded
evolution includes a core-interface migration, it uses the inside-out
hard-break strategy; bounded evolution is a strategy-selection presumption,
not a third strategy.

Fundamental re-adoption requires explicit selection by the human authority
owning the affected product boundary. The selection compares re-adoption
with bounded evolution across product value, feedback latency, authority
risk, reversibility, total cost and retained predecessor semantics, and
states a bounded abort or re-entry condition. Implementation scale or
architectural preference alone does not select re-adoption (P6, P2).

Both strategies share these non-negotiable rules: no proxy interface
partial implementation stands in for the new contract in any acceptance
path; no bridge or fallback path remains silently authoritative; promotion
of an affected product outcome requires one unambiguous authoritative path
for that outcome; competing or ambiguous executable authority on the
promoted acceptance path blocks that outcome; residual material from the
superseded interface family outside the promoted path may be deferred only
when it is explicitly non-authoritative for the promoted outcome or governs
an explicitly specified, disjoint product or compatibility scope with
deterministic routing, cannot falsify current or retained product claims,
and retains a bounded migration, qualification or release disposition;
tests are leak detectors and proof surfaces, not the migration plan.

For this rule the affected acceptance path is the full causal closure of
the outcome: every admitted entrypoint, producer, consumer, resolver,
fallback, shared state surface, event, projection and proof surface capable
of changing, interpreting or closing the outcome. Singular authority means
one governing authority across that closure, not one selected successful
trace. If the same request, fact, identity, state or projection is
admissible to old and new authority, authority is competing and promotion
blocks (P3).

Product-slice promotion and complete migration closure are distinct claims.
An intermediate product outcome may be promoted while its enclosing
migration remains open only when the outcome's acceptance path has singular
authority and the residual implementation satisfies the deferment rule
above. That promotion neither closes the migration nor waives its final
retirement criteria. The slice's identity and acceptance criteria derive
from the product plus every causally applicable live requirement, accepted
design relation and retained predecessor claim; ticket or review wording
cannot narrow that authority away. Active migration status does not renew
an accepted slice's exhausted growth authority: work that only discharges
already admitted removal, demotion and migration-closure proof obligations
may continue within that existing bound without claiming further product
progress; further material producer or consumer growth requires another
still-live basis admitted under §3, and ticket activity alone is not that
basis.
```


### Row `TICKET_METHOD.md#implementation-migration-review-disambiguation` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#implementation-migration-review-disambiguation` at rc.2:

```text
Implementation migration tickets must make the review problem concrete enough
that an implementor cannot land a rename, adapter, wrapper, or happy-path proof
and claim source-truth migration.

For a core-interface or carrier migration, the ticket should include a
`Functional Review Criteria` section. The criteria must be specific to the
ticket, but reviewers should be able to answer these generic questions:

1. Did the change replace control-flow-owned meaning with carrier-owned,
   algebra-owned, event-owned, or otherwise admitted source truth?
2. Did the change reduce or remove a semantic center, or only rename and
   relocate it behind helpers?
3. Is the new law expressed as a typed/closed carrier, contract, or transition
   family rather than an open dict, string protocol, or config-shaped surface?
4. Is the main step readable as a pure transform over admitted truth, or does it
   still contain orchestration that decides the law procedurally?
5. Are effects pushed to the edge, such as event emission, manifest
   publication, file/output publication, or operator delivery, instead of being
   mixed into source-truth interpretation?
6. Do downstream consumers pattern-match or otherwise consume the admitted
   carrier directly, or do they reconstruct truth from payloads, `.get(...)`,
   fallback defaults, raw text, or legacy files?
7. Are projections and reports derived from event/source truth, or can they
   still close independently as a second authority surface?
8. If deterministic gates, validation, or F_D-like checks exist, do they inform
   the current state without structurally blocking the lawful constructive or
   F_P-like path that the admitted contract permits?
9. If the same realization pattern already exists elsewhere, does the ticket
   explicitly consume or extend a reusable library/commonization surface rather
   than rebuilding it locally again?

Passing tests do not satisfy this section by themselves. A slice that keeps the
same semantic center alive behind typed wrappers, adapter-local policy, old
lists beside new algebra, fallback config, or rehydrated dict payloads still
fails migration review even if public behavior remains green.
```

Successor, `TICKETS.md#review-disambiguation`:

```text
An implementation migration ticket makes the review problem concrete enough
that an implementor cannot land a rename, adapter, wrapper or happy-path
proof and claim source-truth migration (P6, P1; rc.2
#implementation-migration-review-disambiguation). For a core-interface or
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
```


### Row `TICKET_METHOD.md#inside-out-first-ticket-sequencing` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#inside-out-first-ticket-sequencing` at rc.2:

```text
For `ticket_category: implementation_migration`, ticket sequencing must reflect
the inside-out rule from `SPEC_METHOD.md`.

That means:

- tickets that publish or admit the new authoritative source carrier are the
  upstream tickets in the wave
- tickets that harden prompt assembly, projections, reports, dossiers, review
  surfaces, or other downstream consumers must depend on those upstream source
  tickets
- downstream tickets may carry exploratory work while the source ticket is
  active, but that work is non-closure evidence until the source carrier is
  admitted and authoritative
- a downstream ticket must not close while its upstream source-carrier ticket
  remains open

In practice, if one migration wave introduces:

- a new source carrier
- then prompt/projection/read-model consumers of that carrier

the ticket dependency chain must run:

`source carrier -> downstream consumers`

not the reverse.
```

Successor, `TICKETS.md#inside-out-sequencing`:

```text
For `ticket_category: implementation_migration`, ticket sequencing reflects
the inside-out rule of
[SPEC_METHOD §7](SPEC_METHOD.md#inside-out-first-sequencing) (P4b, P6;
rc.2 #inside-out-first-ticket-sequencing). Tickets that publish or admit
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
```


### Row `TICKET_METHOD.md#migration-strategy-requirements` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#migration-strategy-requirements` at rc.2:

```text
If `migration_strategy: inside_out_hard_break`, the ticket must carry:

- a full best-guess interface inventory for the migrating contract family
- the ordered break sequence from deepest source truth outward
- the old seam each break intentionally severs
- the negative proof expected for each break

If `migration_strategy: fundamental_re_adoption`, the ticket must carry:

- the explicit human Product-authority selection of fundamental re-adoption
- the comparison with bounded evolution across Product value, feedback latency,
  authority risk, reversibility, total cost, and retained predecessor semantics
- the bounded abort or re-entry condition
- the sideways reference line or prior implementation boundary being treated as
  source material
- the module and interface adjudication surface
- explicit classifications for inherited modules, interfaces, carriers,
  projections, and proof surfaces

Allowed inherited-implementation classifications are:

- `carry_across`
- `redundant`
- `rewrite`

Unclassified inherited implementation blocks closure.
```

Successor, `TICKETS.md#strategy-requirements`:

```text
When `migration_strategy: inside_out_hard_break`, the ticket carries a full
best-guess interface inventory for the migrating contract family; the
ordered break sequence from the deepest source truth outward; the old seam
each break intentionally severs; and the negative proof expected for each
break (P4b, P6; rc.2 #migration-strategy-requirements).

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
```


### Row `TICKET_METHOD.md#mixed-state-negative-proof` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#mixed-state-negative-proof` at rc.2:

```text
For a migration ticket, positive behavior proof is not enough.

The proof surface should include at least one negative or structural proof that
the old path can no longer satisfy the closure law. Examples include:

- the severed seam in the current break is rejected before downstream repair is
  accepted as progress
- removing the new carrier makes advancement, closure, prompt assembly, or
  projection fail closed rather than silently falling back
- a legacy payload without the admitted carrier is rejected instead of
  rehydrated into current truth
- old and new truth intentionally disagree in a fixture and the new truth wins
  or the run fails closed
- a same-name carrier, graph function, route, policy, or projection source with
  different structure fails closed instead of being accepted as equivalent
- required closure proof does not depend on undeclared local fixtures or mutable
  sibling workspaces

If the old path still works in normal execution within the declared affected
scope, or remains reachable on the claimed acceptance path, the ticket remains
open unless that path is explicitly specified as retained compatibility. A
deterministically routed, non-overlapping Product scope outside the declared
affected scope remains governed by its own current authority and does not block
the migration merely because its path still works.

For tickets with an `Impacted Interface Review Checklist`, the negative proof
must exercise the named public consumers that matter for closure. Proving that
one legacy shim is bypassed is not sufficient when the live authority path
already bypasses that shim through other helpers, loaders, or rebuild paths.
```

Successor, `TICKETS.md#mixed-state-negative-proof`:

```text
For a migration ticket, positive behaviour proof is not enough. The proof
surface should include at least one negative or structural proof that
the old path can no longer satisfy the closure law (P6, P5; rc.2
#mixed-state-negative-proof). Examples: the severed seam in the current
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
```


### Row `TICKET_METHOD.md#one-durable-record-per-sprint` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#one-durable-record-per-sprint` at rc.2:

```text
Each sprint has one durable manifest record. The default carrier is one
markdown file. Another bound carrier must preserve the same identity, required
fields, history, closure law, and one-truth relation.

Recommended local-file naming:

- `SPRINT-2026-04-30-process-navigator.md`
- `SPRINT-2026-05-12-dashboard-density.md`

For a local file, the filename should carry:

- stable id
- short slug
```

Successor, `TICKETS.md#one-durable-record-per-sprint`:

```text
Each sprint has one durable manifest record; the default carrier is one
markdown file. Another bound carrier preserves the same identity, required
fields, history, closure law and one-truth relation (P3, P4b; rc.2
#one-durable-record-per-sprint). For a local file, the filename should
carry a stable id and a short slug. Recommended local-file naming:
`SPRINT-2026-04-30-process-navigator.md` and
`SPRINT-2026-05-12-dashboard-density.md`.
```


### Row `TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity` at rc.2:

```text
A residual judgment needed by another activation is recorded once with its
owning work in the existing carrier selected by Work-Carrier-To-Execution Rule.
It identifies the question, exact subject and governing basis, supporting
computed facts/evidence, responsible actor and authority, conclusion and
scope, uncertainty, and a concrete revising observation. That observation must
let a consumer determine whether the conclusion still applies. A rule-settled
question needs no invented J record.

Later roles and resumed runs recover the result and check applicability rather
than re-author unchanged judgment. Changed material evidence, basis or the
stated revising observation causes affected reassessment, preserving the
original result and its successor relation. Retain unrelated conclusions only
where their independence from the change is supported. A new role or
conversation alone is not an invalidator. The result may reference current C
outputs; reuse cannot silently turn unknown facts into established premises.

Required independent assessment may consume valid C, but its assessor acquires
sufficient exact evidence and supplies its own judgment under the actual
independence condition. Reusing the author's J cannot satisfy that condition.

Record a direct or lawfully proxied owner ruling in its original wording, with
its owner, exact subject/basis, permitted scope and effects, conditions and
source, separately from agent interpretation. Later work consumes that same
ruling while applicable; it neither widens it nor requests unchanged authority
again. New ambiguity or a materially changed decision returns only the affected
question to its owner. J is not O, and recording either cannot create admission,
acceptance, effects or continuation beyond the original grant.

These results follow the existing run, sprint or durable-ticket lifetime and
named result/evidence surface. They require no separate judgment registry,
ticket per judgment, or additional approval ceremony.

Repricing gives each affected obligation a disposition in that same carrier:
retained, superseded, deferred or withdrawn, with its owning authority and
applicable evidence links. Preserve surviving work and explain changed
dependencies; copy no unaffected history into a parallel ledger. Present an
owner decision as the short consequence delta needed to decide it while
preserving the original ruling separately. A general instruction to continue
does not accept an undisclosed architectural or scope change.
```

Successor, `TICKETS.md#recorded-judgment-and-owner-ruling-continuity`:

```text
A residual judgment that another activation needs is recorded once, with
its owning work, in the existing carrier selected under §5. The record
identifies the question; the exact subject and governing basis; the
supporting computed facts and evidence; the responsible actor and its
authority; the conclusion and its scope; the uncertainty; and a concrete
revising observation that lets a consumer determine whether the conclusion
still applies. A question settled by rule needs no invented J record (P4b,
P6; rc.2 #recorded-judgment-and-owner-ruling-continuity; C, J and O are
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

The four repricing dispositions are recorded states of the obligation,
set by its owning authority; they are not results and map to no core
value. Each records the standing the obligation keeps after repricing,
as the lifecycle statuses of
[SPEC_METHOD §2](SPEC_METHOD.md#requirement-categories-and-classification)
record a requirement's, and answers no predicate that an evaluation
decides on evidence. They differ from the disposition of an assessed
candidate ([ACTIVATION §3 Disposition](ACTIVATION.md#disposition)), which
is the acceptance result that FOUNDATIONS §4 Results places in the core,
because a repricing disposition accepts no candidate; and from the
disposition of a predecessor claim
([RELEASE §9](RELEASE.md#9-successor-baseline-conservation-stdo-up-015)),
which is a claim that qualification evaluates. An evaluation that reads
them returns its own core value with its predicate under
[FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Purpose and material
relation: a recorded disposition is never combined as an evaluation
result, so a retained obligation is never read as satisfied, and a
superseded, deferred or withdrawn one never as discharged (P5, P1, P6).
```


### Row `TICKET_METHOD.md#recurring-realization-and-library-declaration` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#recurring-realization-and-library-declaration` at rc.2:

```text
Implementation migration tickets must declare whether the active boundary is:

- rebuilding a pattern locally
- consuming an existing reusable library/commonization surface
- extending that surface before the local implementation lands

This is what `library_usage` records.

The recurrence rule is:

- the second credible recurrence forces an explicit library/commonization review
- the third local rebuild is not acceptable by default

If review shows the same realization pattern already exists in two module
boundaries or tickets, a third local rebuild blocks implementation unless the
ticket does one of these:

- declares `library_usage: consume`
- declares `library_usage: extend`
- links an explicit do-not-commonize design decision in `library_rationale`

Preferred order is:

1. boundary-local cleanup
2. tenant-local reusable library/commonization surface
3. shared/common propagation only through separate design re-entry

If a reusable pattern is discovered during the active ticket, the second- and
third-recurrence rules above still apply. Outside those rules and the current
claim's applicable hard stops, the pattern is repricing input. It does not block
the bounded claim or require a follow-up ticket unless the owning authority
admits that follow-up.
```

Successor, `TICKETS.md#recurring-realisation-and-library-declaration`:

```text
An implementation migration ticket declares whether the active boundary is
rebuilding a pattern locally, consuming an existing reusable library or
commonisation surface, or extending that surface before the local
implementation lands; `library_usage` records which (P2, P4a; rc.2
#recurring-realization-and-library-declaration).

The recurrence rule: the second credible recurrence forces an explicit
library or commonisation review; the third local rebuild is not acceptable
by default. If review shows the same realisation pattern already exists in
two module boundaries or tickets, a third local rebuild blocks
implementation unless the ticket declares `library_usage: consume`,
declares `library_usage: extend`, or links an explicit do-not-commonise
design decision in `library_rationale`. The preferred order is
boundary-local cleanup, then a tenant-local reusable library or
commonisation surface, then shared or common propagation only through
separate design re-entry (P2, P3).

A reusable pattern discovered during the active ticket remains under the
second- and third-recurrence rules. Outside those rules and the current
claim's applicable hard stops it is repricing input: it does not block the
bounded claim or require a follow-up ticket unless the owning authority
admits that follow-up (P2; §7, Execution and verification authority
separation).
```


### Row `TICKET_METHOD.md#required-break-order-and-break-to-closure-map` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#required-break-order-and-break-to-closure-map` at rc.2:

```text
Implementation migration tickets that touch a core interface must include a
`Required Break Order` or equivalent ordered execution section.

The order must start at the authoritative source carrier and move outward:

1. discover the full best-guess interface family
2. publish or admit the new source carrier
3. deliberately sever one old authoritative seam and keep it broken
4. rebind the deepest semantic kernel to that carrier
5. remove or demote old producers
6. rebind old consumers
7. reprice projections, reports, prompts, delivery bindings, and tests

The ticket must also include a `Break-To-Closure Map` when the migration has
multiple old interfaces. The map must state which break closes which
closure-law clause. Without that map, partial landing can look like full
landing.

Reviewers must treat the following as explicit defects:

- a typed wrapper that still carries old semantic authority
- a new carrier added beside the old authoritative read model
- a proxy or partial implementation that keeps the old interface alive behind a
  new name
- constructor, replay, ingest, resume, bootstrap, or public-wrapper paths that
  bypass admission
- a projection or test that can pass without the new carrier
- a fallback path that invents missing policy, identity, target, or closure
  truth
- a downstream proof that passes while upstream source-carrier work remains open
```

Successor, `TICKETS.md#break-order-and-break-to-closure-map`:

```text
An implementation migration ticket that touches a core interface includes
a `Required Break Order` or an equivalent ordered execution section. The
order starts at the authoritative source carrier and moves outward
(P4b, P6; rc.2 #required-break-order-and-break-to-closure-map;
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
```


### Row `TICKET_METHOD.md#required-fields` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#required-fields` at rc.2:

```text
Each ticket must record at least:

- `id`
- `title`
- `type`
- `ticket_category`
- `status`
- `goal`
- `change_intent`
- `change_class`
- `re_entry_point`
- `triaged_at`
- `created_at`
- `updated_at`

Recommended additional fields:

- `priority`
- `dependencies`
- `links`
- `intake_source`
- `affected_boundary`
- `source_ticket` when this ticket duplicates or derives from another ticket
- `build_tenant` when this ticket is tenant-local

For `ticket_category: implementation_migration`, also require:

- `migration_strategy`
- `library_usage`

For tenant-local implementation migrations, also require:

- `build_tenant`
- `source_ticket` when the tenant-local ticket duplicates or derives from an
  upstream source/product/design ticket

For `ticket_category: implementation_migration`, also conditionally require:

- `governing_library` when `library_usage: consume` or `library_usage: extend`
- `library_rationale` when `library_usage: none`

For execution-contract admission, the runtime-drafted contract should also
carry, at minimum:

- `target_truth`
- `superseded_truth` when relevant
- `closure_law`
- `evaluation_criteria`
- `non_closure_conditions`
- `proof_surface`
```

Successor, `TICKETS.md#required-fields`:

```text
Each ticket records at least `id`, `title`, `type`, `ticket_category`,
`status`, `goal`, `change_intent`, `change_class`, `re_entry_point`,
`triaged_at`, `created_at` and `updated_at` (P4b, P3; rc.2
#required-fields). Recommended additional fields: `priority`,
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
```


### Row `TICKET_METHOD.md#sprint-compliance-escrow` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#sprint-compliance-escrow` at rc.2:

```text
A sprint may defer local compliance proof only when:

- the manifest names the deferred proof or cleanup class
- the debt is local to the sprint's admitted surface
- expected correction cost is lower than per-change proof cost
- the sprint is short enough that the debt remains reviewable
- the close review must classify and pay down the debt

Deferred compliance is not silent debt. It is escrow held by the sprint.

The following may be eligible for escrow when the governing method allows it:

- screenshots or walkthrough capture
- visual review
- accessibility cleanup
- replay proof for product-meaningful UX interactions
- design wording cleanup
- trace cleanup
- local realization cleanup

The following may not be hidden in escrow:

- new product truth
- new or changed data contracts
- new runtime, governance, closure, provenance, or evidence semantics
- missing constructive carriers
- changed public graph functions or AssetSurface contracts
- law-changing work that needs `goal_reprice`, `intent_reprice`,
  `product_reprice`, `requirement_reprice`, or `design_reframe`

If one of those appears during the sprint, the sprint records the finding and
the work exits the sprint path through a standalone ticket, a repricing action,
or sprint supersession.
```

Successor, `TICKETS.md#compliance-escrow`:

```text
A sprint may defer local compliance proof only when the manifest names the
deferred proof or cleanup class; the debt is local to the sprint's admitted
surface; the expected correction cost is lower than the per-change proof
cost; the sprint is short enough that the debt remains reviewable; and the
close review classifies and pays down the debt. Deferred compliance is not
silent debt: it is escrow held by the sprint, and
[SPEC_METHOD §4](SPEC_METHOD.md#sprint-execution-boundary) states that
escrow satisfies no method, release or product closure until paid down,
accepted or repriced (P2, P4b, P6; rc.2 #sprint-compliance-escrow).

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
```


### Row `TICKET_METHOD.md#sprint-manifest-required-fields` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#sprint-manifest-required-fields` at rc.2:

```text
Each sprint manifest must record at least:

- `id`
- `title`
- `status`
- `goal`
- `opened_at`
- `updated_at`
- `authority_refs`
- `scope`
- `excluded_boundaries`
- `expected_change_classes`
- `included_tickets` or `iterations`
- `closure_trigger`
- `closure_law`
- `proof_surface`
- `deferred_compliance`
- `non_closure_conditions`
- `paydown_policy`

`authority_refs` names the upstream Goals, Intent, Product, Requirement,
Design, or other governing surfaces the sprint operates under.

`excluded_boundaries` names what the sprint is not allowed to change. Typical
exclusions include product truth, data contracts, runtime semantics,
governance/closure law, public carrier shape, and release criteria.

`deferred_compliance` names any local proof, review, accessibility, screenshot,
walkthrough, test, design wording, or trace cleanup intentionally deferred until
sprint close.

`paydown_policy` states how deferred debt becomes accepted, ticketed, repriced,
or removed during close review.
```

Successor, `TICKETS.md#manifest-fields`:

```text
Each sprint manifest records at least `id`, `title`, `status`, `goal`,
`opened_at`, `updated_at`, `authority_refs`, `scope`, `excluded_boundaries`,
`expected_change_classes`, `included_tickets` or `iterations`,
`closure_trigger`, `closure_law`, `proof_surface`, `deferred_compliance`,
`non_closure_conditions` and `paydown_policy` (P4b, P2; rc.2
#sprint-manifest-required-fields).

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
```


### Row `TICKET_METHOD.md#test-case-authority` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#test-case-authority` at rc.2:

```text
Tests are proof projections from admitted work authority.

Every substantive test case should derive from:

```text
ticket -> intake triage -> lawful re-entry point -> governing requirement,
design, module, graph, carrier, or closure surface -> test expectation
```

Tests do not derive authority from the current implementation.

An acceptance predicate also needs an applicable supported entry or state and
an obligation under the governing operating/threat model. Existing test presence
cannot authorize an excluded threat or retain a superseded guard. Audit the
affected predicates when changing that responsibility; retire unsupported
expectations under the owning basis without inventing a replacement guard.
An actual conflict in live authority requires re-entry, not a test-only waiver.

Implementation behavior is evidence. It is not the arbiter of the expected
result when code and tests disagree.

When a ticket is fixed and a mismatch appears between implementation behavior
and test expectation, review must reconcile the mismatch in this order:

1. the ticket's `change_intent`, `change_class`, `re_entry_point`,
   `target_truth`, `superseded_truth`, `closure_law`,
   `evaluation_criteria`, and `non_closure_conditions`
2. the ticket's intake triage and lawful owning re-entry
3. the governing requirement, design, module, graph-function, carrier, or
   other cited authority surface
4. the test case expectation
5. the implementation

The implementation may prove that a test is stale, incomplete, or too narrow,
but it cannot by itself authorize changing the expected result.

Changing a test only because the current code behaves differently is a
ticket-method defect.

If a test predates a lawful ticket repricing, update or remove the test only
after naming the governing ticket and the authority change that superseded the
old expectation.

If the ticket is stale, ambiguous, or missing the authority needed to decide the
test expectation, the work must re-enter triage before either the code or test
is treated as correct.

A passing test is closure evidence only when the test expectation can be traced
back to the admitted ticket and its governing authority chain.
```

Successor, `TICKETS.md#test-case-authority`:

```text
Tests are proof projections from admitted work authority. Every
substantive test case should derive along this chain (P6, P2; rc.2
#test-case-authority):

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
```


### Row `TICKET_METHOD.md#ticket-category` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#ticket-category` at rc.2:

```text
Ticket category is orthogonal to ticket type.

- ticket type answers: what kind of work record is this?
- ticket category answers: what execution discipline or migration discipline
  governs the ticket?

Minimum common set:

- `ordinary`
- `implementation_migration`

This means a `feature`, `bug`, `spike`, or `chore` may all carry:

- `ticket_category: ordinary`
- `ticket_category: implementation_migration`

Use `implementation_migration` when the ticket is not just “change code until
tests pass”, but a governed replacement of one implementation truth path with
another across producers, consumers, projections, and proof surfaces.

Typical examples:

- a bug ticket that must replace an old tracker/read-model family with one new
  authoritative carrier
- a feature ticket that introduces a new public interface and requires all
  producers/consumers to migrate to it before closure
- a refactor ticket that removes a bridge path or compatibility facade from an
  authoritative contract family
```

Successor, `TICKETS.md#category`:

```text
Ticket category is orthogonal to ticket type: type answers what kind of
work record this is; category answers what execution or migration
discipline governs the ticket (P3, P1; rc.2 #ticket-category). The minimum
common set is `ordinary` and `implementation_migration`, so a `feature`,
`bug`, `spike` or `chore` may carry either. `implementation_migration` is
used when the ticket is not "change code until tests pass" but a governed
replacement of one implementation truth path with another across producers,
consumers, projections and proof surfaces: a bug ticket that replaces an old
tracker or read-model family with one new authoritative carrier; a feature
ticket that introduces a new public interface and requires every producer
and consumer to migrate before closure; a refactor ticket that removes a
bridge path or compatibility facade from an authoritative contract family.
```


### Row `TICKET_METHOD.md#triage-metadata` (modal; disposition `conserved`)

Predecessor, `TICKET_METHOD.md#triage-metadata` at rc.2:

```text
Because tickets are the durable authority surface for work tracking, a ticket
for substantive work must carry the minimum metadata required by
`SPEC_METHOD.md` intake triage.

That means the ticket must record at least:

- the declared `change_intent`
- the lawful `change_class`
- the lawful `re_entry_point`
- when triage occurred via `triaged_at`
```

Successor, `TICKETS.md#triage-metadata`:

```text
Because tickets are the durable authority surface for work tracking, a
ticket for substantive work carries the minimum metadata required by the
intake triage of [SPEC_METHOD §4](SPEC_METHOD.md#universal-intake-triage):
the declared `change_intent`, the lawful `change_class`, the lawful
`re_entry_point`, and when triage occurred in `triaged_at` (P4b, P2; rc.2
#triage-metadata). The recorded values are those intake triage declared
(Change class and Upward propagation check above).
```


### Row `UX_METHOD.md#13a-scaffold-and-exemption-law` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#13a-scaffold-and-exemption-law` at rc.2:

```text
A UX surface is governed by this method by default when any of these are true:

- it is reachable from the product shell
- it is used as proof for a ticket, requirement, design module, release, or
  review
- it can mutate product truth
- it can spawn, attach, resume, or dispatch work
- it can change Context, selection authority, closure, continuation, evidence,
  or provenance

A scaffold, prototype, debug pane, or temporary proof surface may be exempt only
when the design module or ticket records:

- the exemption scope
- the permitted operations
- whether mutation is forbidden or explicitly bounded
- a visible scaffold/debug label where user-facing
- the authoritative surface that will supersede it
- the retirement condition and owning ticket
- the non-closure condition preventing release if the scaffold remains

An exempt scaffold cannot become the production UX by accumulation. It must be
retired, repriced into a governed UX surface, or kept outside product closure.
```

Successor, `UX.md#scaffold-and-exemption`:

```text
A UX surface is governed by this profile by default when any of these are
true (P6, P5; rc.2 #13a-scaffold-and-exemption-law):

- it is reachable from the product shell;
- it is used as proof for a ticket, requirement, design module, release or
  review;
- it can mutate product truth;
- it can spawn, attach, resume or dispatch work;
- it can change Context, selection authority, closure, continuation,
  evidence or provenance.

A scaffold, prototype, debug pane or temporary proof surface may be
exempt only when the design module or ticket records (P6, P4b):

- the exemption scope;
- the permitted operations;
- whether mutation is forbidden or explicitly bounded;
- a visible scaffold or debug label where user-facing;
- the authoritative surface that will supersede it;
- the retirement condition and owning ticket;
- the non-closure condition preventing release if the scaffold remains.

An exempt scaffold cannot become the production UX by accumulation. It is
retired, repriced into a governed UX surface, or kept outside product
closure (P4b, P6).
```


### Row `UX_METHOD.md#13b-ux-sprint-compliance-escrow` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#13b-ux-sprint-compliance-escrow` at rc.2:

```text
UX is the primary governed use case for sprint compliance escrow.

Under `SPEC_METHOD.md` and `TICKET_METHOD.md`, a UX sprint may defer local UX
compliance proof during a short iteration window when per-change proof cost is
higher than expected correction cost.

This is a cost-optimization rule. It does not weaken the UX process model.

A UX sprint may escrow:

- screenshots or walkthrough capture
- visual review
- copy, spacing, density, and layout cleanup
- accessibility review and remediation
- Msg-replay proof updates for product-meaningful interaction families
- design-module wording cleanup
- trace cleanup between changed UX states and governing authority

A UX sprint may not escrow:

- product-truth-changing `Msg` variants that lack an admitted carrier
- new or changed `AssetSurface` contracts or equivalent typed product contracts
- new navigation, information architecture, or selection authority that changes
  product meaning
- runtime, governance, closure, continuation, lineage, provenance, or evidence
  semantics
- release criteria or method law

If one of those appears, the sprint records the finding and the work exits the
UX sprint path through standalone repricing or sprint supersession. The UX layer
must still not become the hidden constructive carrier.

A UX sprint should close when continued iteration is more expensive or less
trustworthy than review. Valid close triggers include:

- the declared timebox ends
- accumulated changed states are too numerous for casual review
- screenshots or walkthrough evidence no longer explain the current surface
- interaction behavior changed beyond visual polish
- reviewer uncertainty makes more iteration unsafe without reconciliation

UX sprint close is a forensic walkthrough. The walkthrough reviews each changed
screen, state, and product-meaningful interaction against the cited authority.

Each finding is classified as:

- `accepted`: compliant with this method and the cited design
- `local_paydown`: local UX debt remains and is captured by a paydown ticket
- `design_reframe`: design authority must change
- `requirement_reprice`: requirement authority must change
- `product_reprice`: product definition must change
- `remove`: the change should be backed out or kept out of closure

The sprint may close with explicit local paydown tickets only where the debt is
local to UX realization and the governing method allows follow-up. It may not
close while product-truth carrier gaps, hidden state continuation, or authority
drift remain unclassified.

Method closure for a product UX surface still requires the §8A Msg-replay proof
and §11 accessibility obligations unless an explicit exemption is recorded. The
sprint can defer those obligations during iteration; it cannot erase them.

---
```

Successor, `UX.md#ux-sprint-compliance-escrow`:

```text
UX is the primary governed use case for sprint compliance escrow. This
subsection is the profile's statement, which SPEC_METHOD §4 Sprint
execution boundary admits, of when that escrow is an appropriate cost
optimisation for UX; the generic escrow law and the close mechanics are
TICKETS §3 Compliance escrow and Close review (P2, P6;
rc.2 #13b-ux-sprint-compliance-escrow). A UX sprint may defer local UX
compliance proof during a short iteration window when per-change proof
cost is higher than expected correction cost. This is a cost-optimisation
rule; it does not weaken the UX process model (P2).

A UX sprint may escrow (P2, P4b):

- screenshots or walkthrough capture;
- visual review;
- copy, spacing, density and layout cleanup;
- accessibility review and remediation;
- Msg-replay proof updates for product-meaningful interaction families;
- design-module wording cleanup;
- trace cleanup between changed UX states and governing authority.

A UX sprint may not escrow (P6):

- product-truth-changing Msg variants that lack an admitted carrier;
- new or changed AssetSurface contracts or equivalent typed product
  contracts;
- new navigation, information architecture or selection authority that
  changes product meaning;
- runtime, governance, closure, continuation, lineage, provenance or
  evidence semantics;
- release criteria or method law.

If one of those appears, the sprint records the finding and the work
exits the UX sprint path through standalone repricing or sprint
supersession. The UX layer still does not become the hidden constructive
carrier (P6; §3).

A UX sprint should close when continued iteration is more expensive or
less trustworthy than review. Valid close triggers include (P2, P6):

- the declared timebox ends;
- accumulated changed states are too numerous for casual review;
- screenshots or walkthrough evidence no longer explain the current
  surface;
- interaction behaviour changed beyond visual polish;
- reviewer uncertainty makes more iteration unsafe without
  reconciliation.

UX sprint close is a forensic walkthrough: it reviews each changed
screen, state and product-meaningful interaction against the cited
authority (P6). Each finding takes one of the six classifications of
TICKETS §3 Close review (`accepted`, `local_paydown`, `design_reframe`,
`requirement_reprice`, `product_reprice`, `remove`); for a UX finding,
`accepted` reads as compliant with this profile and the cited design,
and `local_paydown` as local UX debt captured by a paydown ticket (P6,
P5). The sprint may close with explicit local paydown tickets only where
the debt is local to UX realisation and the governing method allows
follow-up. It may not close while product-truth carrier gaps, hidden
state continuation or authority drift remain unclassified (P6, P4b).

Closure under this profile for a product UX surface still requires the
§8 Msg-replay proof and the §11 accessibility obligations unless an
explicit exemption is recorded. The sprint can defer those obligations
during iteration; it cannot erase them (P4b, P6).
```

Successor, `TICKETS.md#3-sprint-rules`:

```text

```


### Row `UX_METHOD.md#3a-ux-projection-and-constructive-carrier-boundary` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#3a-ux-projection-and-constructive-carrier-boundary` at rc.2:

```text
UX surfaces are projection and control surfaces. They render admitted truth and
emit typed messages.

A UX-local `Msg` may govern view-local concerns such as expansion state, sort
order, filter text, focus movement, or draft input.

A UX `Msg` that changes product truth is not merely a UX concern. Product-truth
changes include:

- writing, creating, moving, or deleting assets
- changing Context, selection authority, pinning, or global product state
- spawning, attaching, or resuming sessions
- dispatching agents, jobs, workorders, graph calls, or runtime commands
- changing closure, approval, continuation, lineage, provenance, or evidence
- publishing, accepting, rejecting, or superseding product records

Such a message must map to one admitted product carrier:

- an `AssetSurface` action
- a published graph function or lawful graph-function composition
- a workorder, job, or runtime command admitted by the product's design
- an ABG event or command boundary where ABG is the runtime authority
- another typed product contract named by the design module

The UX layer must not become the hidden constructive carrier. If no admitted
carrier exists for a product-truth-changing message, the UX surface is blocked
until the carrier is authored or the requirement is repriced.

---
```

Successor, `UX.md#3-product-truth-and-admitted-carriers`:

```text
UX surfaces are projection and control surfaces: they render admitted
truth and emit typed messages (P6, P0;
rc.2 #3a-ux-projection-and-constructive-carrier-boundary). A UX-local Msg
may govern view-local concerns such as expansion state, sort order,
filter text, focus movement or draft input. A Msg that changes product
truth is not merely a UX concern. Product-truth changes include:

- writing, creating, moving or deleting assets;
- changing Context, selection authority, pinning or global product state;
- spawning, attaching or resuming sessions;
- dispatching agents, jobs, workorders, graph calls or runtime commands;
- changing closure, approval, continuation, lineage, provenance or
  evidence;
- publishing, accepting, rejecting or superseding product records.

Such a message maps to one admitted product carrier (P6, P4a):

- an AssetSurface action;
- a published graph function or lawful graph-function composition;
- a workorder, job or runtime command admitted by the product's design;
- an ABG event or command boundary where ABG is the runtime authority;
- another typed product contract named by the design module.

The UX layer does not become the hidden constructive carrier. If no
admitted carrier exists for a product-truth-changing message, the UX
surface is blocked until the carrier is authored or the requirement is
repriced (P6, P5; §15 states the result).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```


### Row `UX_METHOD.md#8a-msg-replay-proof-requirement` (modal; disposition `conserved`)

Predecessor, `UX_METHOD.md#8a-msg-replay-proof-requirement` at rc.2:

```text
Every product UX surface must carry at least one executable Msg-replay proof for
each product-meaningful interaction family before claiming method closure.

A replay proof includes:

- an initial `State` fixture
- an ordered `Msg` log
- the expected final `State`
- the expected ordered `Cmd` values
- the success and failure `Msg` values returned by interpreted `Cmd`s
- injected deterministic values for time, randomness, generated ids, and
  external payloads

The proof fails if correctness depends on:

- DOM state not represented in `State`
- mutable refs, module variables, closures, timers, or effect-handler memory
- network or file results that bypass typed `Msg`
- view-local state that changes product behavior after unmount or replay

For a pure projection-only surface, the replay proof may be a no-effect proof:
`Msg` log plus final `State` and empty `Cmd` sequence.

---
```

Successor, `UX.md#msg-replay-proof`:

```text
Every product UX surface carries at least one executable Msg-replay proof
for each product-meaningful interaction family before claiming closure
under this profile (P4b, P6; rc.2 #8a-msg-replay-proof-requirement).
Purpose and material relation: the Msg log is the surface's recorded work
state, and replay is resumption from it
([ACTIVATION §5 The workspace and an actor's account](ACTIVATION.md#the-workspace-and-an-actors-account)).
A surface whose behaviour cannot be reproduced from its log holds state
that no later actor or session can recover or check, so the proof is the
evidence that the view owns no hidden continuation (P0, P4b). A
replay proof includes:

- an initial State fixture;
- an ordered Msg log;
- the expected final State;
- the expected ordered Cmd values;
- the success and failure Msg values returned by interpreted Cmds;
- injected deterministic values for time, randomness, generated ids and
  external payloads.

The proof fails if correctness depends on (P5, P4b):

- DOM state not represented in State;
- mutable refs, module variables, closures, timers or effect-handler
  memory;
- network or file results that bypass typed Msg;
- view-local state that changes product behaviour after unmount or
  replay.

For a pure projection-only surface, the replay proof may be a no-effect
proof: a Msg log plus the final State and an empty Cmd sequence (P2).
```

Successor, `UX.md#15-results-of-this-profile`:

```text
This section owns this profile's refinements of the core result algebra
of [FOUNDATIONS §4 Results](FOUNDATIONS.md#results). Each refinement names
the question it answers and the predicate its mapping is for, and maps
each of its values to exactly one core value. The predicate travels with
the value, so a `satisfied` for one predicate never counts toward another
([FOUNDATIONS §4 Conjunction of results](FOUNDATIONS.md#conjunction-of-results)),
and no mapping raises a result's standing: nothing is coerced to
`satisfied` (P5, P6). The refinements are new in this corpus. Purpose and
material relation: this profile's verdicts decide closure of a UX surface
and enter conjunctions with the results of other members, which combine
only in the core, so a review, a proof, a closure claim and a carrier
check are each read for their own predicate and none is read as another
(P5, P6).

| Refinement | Question | Predicate of the mapping |
|---|---|---|
| surface review | does the surface comply with this profile (§4 Realisation discretion, §13, §14) | the UX surface complies with this profile on the exact basis |
| replay proof | does a Msg-replay proof hold (§8 Msg-replay proof) | the Msg-replay proof reproduces its expected final State and ordered Cmd values, and its correctness depends on nothing that §8 Msg-replay proof lists |
| closure obligations | where closure of a product UX surface is claimed, are the obligations met that closure requires (§12 UX sprint compliance escrow) | each product-meaningful interaction family of the surface carries its Msg-replay proof and the surface carries its §11 declarations, unless a recorded exemption covers the obligation |
| carrier admission | does each product-truth-changing message have an admitted carrier (§3, §7) | every product-truth-changing message or action of the surface maps to an admitted product carrier or typed product contract |

| Refinement | Value | Core value | Ground |
|---|---|---|---|
| surface review | `compliant` | satisfied | §4 to §10 hold under inspection and no §13 failure pattern is present (§4 Realisation discretion), and every §14 review question is answered from the design module. The first part is the stricter of the two compliance tests of §4, which disagree: §4 Process model without stack mandate counts a realisation that preserves §4 to §8 as compliant. The choice between them is pending the product owner's ruling and is not settled by this mapping; while it is pending, this mapping applies the stricter test under the fail-closed rule of §1 Authority. The last part, every §14 review question answered from the design module, is in neither test: it is the basis condition that separates `compliant` from `design_module_incomplete` |
| surface review | `violation` | falsified | the test of `compliant` fails: a §13 failure pattern is present, a realisation that §4 Process model without stack mandate rejects is used, or a rule of §4 to §10 does not hold under inspection; the pattern, realisation or rule is the counterexample |
| surface review | `design_module_incomplete` | invalid_basis | no counterexample of `violation` is found, and a §14 review question cannot be answered from the design module, so the design module, on which the review rests, cannot support the evaluation; the value names the unanswered question |
| replay proof | `replay_passes` | satisfied | the proof reproduces its expected final State and ordered Cmd values on its injected deterministic values, and no dependency that §8 lists decides its correctness |
| replay proof | `replay_fails` | falsified | the proof diverges from its expected final State or Cmd values, or its correctness depends on something §8 lists; the divergence or the dependency is the counterexample |
| closure obligations | `closure_obligations_met` | satisfied | every product-meaningful interaction family carries its Msg-replay proof and the surface its accessibility declarations, or a recorded exemption covers the obligation |
| closure obligations | `closure_unproven` | falsified | an interaction family lacks its proof or the surface an accessibility declaration, with no recorded exemption; that family or obligation is the counterexample. Inside an open UX sprint closure is not claimed, and a deferred obligation is escrow under §12 |
| carrier admission | `carrier_admitted` | satisfied | each product-truth-changing message or action maps to an admitted carrier of §3 and binds under §7 to an AssetSurface contract where the product publishes one, otherwise to the equivalent typed contract its design module names |
| carrier admission | `carrier_missing` | falsified | a product-truth-changing message or action has no admitted carrier or typed contract (§13 pattern 13); that message or action is the counterexample |

Where none of these values applies, the evaluation returns a core value
directly under [FOUNDATIONS §4 Results](FOUNDATIONS.md#results):
`indeterminate` where the admissible evidence cannot decide its predicate,
naming the evidence that would decide; `out_of_frame` where its claim
needs a relation or capability that its frame does not declare; and
`invalid_basis` where its subject or basis cannot support it on a ground
other than `design_module_incomplete` (P5).

Fail closed (§1 Authority). Where this profile is ambiguous for a case,
the surface review applies the stricter interpretation and returns its
value under it; the ambiguity alone never yields `compliant`. Where the
ambiguity leaves a term the review depends on undefined, so that no
stricter interpretation is fixed, the review returns
`out_of_frame` and names the term and its owner
([FOUNDATIONS §4 Results](FOUNDATIONS.md#results), Out of frame or
indeterminate, first case). A reprice or a scoped exemption, the other
two exits of §1 Authority, is a re-entry or a scope recorded in the
design module, not a value of this section (P5, P6).

Blocked for want of a carrier (§3, §7). The surface's carrier admission
returns `carrier_missing`, and its review returns `violation` (§13 pattern
13), each for its own predicate. A construction step that needs the
missing carrier stops with `re_entry_requested(authority)`, which
[ACTIVATION §3 Construction availability](ACTIVATION.md#construction-availability)
maps; the stop names the missing carrier, its owner in the product's
design and the re-entry, which is to author the carrier or to reprice the
requirement (P5, P6).

Two collisions are resolved here (P1): "blocked" for want of a carrier is
not the ambiguity outcome `blocked` of
[ACTIVATION §3 Ambiguity outcome](ACTIVATION.md#ambiguity-outcome), and
`design_module_incomplete` is not the value `incomplete` of ACTIVATION §3
Construction availability. An exempt scaffold is a recorded scope (§12),
not a result; evaluations outside its recorded scope proceed under this
section. The six close classifications of §12 belong to TICKETS §3 and are
not mapped here (P6).
```
