# Explicit frame-index use

Use this reference when the exact selected Axiom dependency supplies `project`
and the selected STDO program declares frame indexes. For the RC6 successor,
resolve the exact cohort release record or manifest, its same-version Axiom
Product dependency, and these paths from the Representation Product root:

```text
build_tenants/axiom_indexer/representation/stdo-v2.5.0-rc.6/
  axiomatic-program.json
  logical-constraint-map.json
```

Verify the selected record's program, map, source and dependency digests before
use. Supply invocation-local bindings to the exact represented Source STDO
Install. Released use needs no dogfood directory or construction manifest.
An explicitly selected working candidate instead supplies its own exact subject,
path bases and construction grant; it cannot replace an installed dependency.
Before the immutable child cut exists, use only the selected exact construction
candidate under that grant. Historical RC4 supplies no `project` operation.
A file location or successful command supplies no authority. Missing or
mismatched inputs return a bounded hold, not a mutable sibling substitution.

Start from the map's explicit `frame_indexes` declarations. Inspect the bound
frame URI, governed scope, selected clause/residual roots and source routes.
Choose the smallest applicable index set yourself and state why. The map does
not infer task applicability. The T009 example offers:

- `urn:stdo-representation:frame-index:t009:complete-update-worker`: bounded
  construction/self-validation under an existing exact grant;
- `urn:stdo-representation:frame-index:t009:complete-update-reviewer`: evaluation
  of an exact claimed result under the declared assessment/independence scope.

Both bind source-owned frames and share update-plan, source-refusal, evidence
and authority constraints. Selecting both does not create a two-actor workflow
or grant construction to a Reviewer. Direct sufficient work keeps its declared
consumer; coordinated work returns through its selected Executive relation.

For read-only use, omit `--output`: the dependency writes the view to stdout.
Every supplied `--output` value is a file path, including `-`, which names a
literal file and does not select stdout. File output requires an applicable
write grant for that path.

With the exact paths bound by that subject, inspect a view without file output:

```sh
python3 <exact-axiom-ac.py> project \
  --program <axiomatic-program.json> \
  --map <logical-constraint-map.json> \
  --bindings <bindings.json> \
  --frame-index urn:stdo-representation:frame-index:t009:complete-update-worker \
  --mode reference-only
```

When the applicable grant includes the output file, a materialized view can be
written to that path:

```sh
python3 <exact-axiom-ac.py> project \
  --program <axiomatic-program.json> \
  --map <logical-constraint-map.json> \
  --bindings <bindings.json> \
  --frame-index urn:stdo-representation:frame-index:t009:complete-update-worker \
  --mode materialized --output <worker-content.json>
```

Repeat `--frame-index` only for additional explicitly selected indexes. Keep
outputs separate from program, map, bindings and source inputs. Use the same
selection and exact subject for a comparison of the two modes. Reference-only
content resolves by item URI against the exact program; materialized rows are
unchanged authored content. Neither view is a separately editable program.

Read the preserved ordered relations and literal qualifications. Follow all
supporting premises, conditions, exceptions and affected residuals. Supply or
recover the actual C facts, applicable J and original owner ruling separately,
where that ruling exists or is required. Do not invent a universal O condition.
An absent premise prevents the dependent conclusion; an applicable exception
changes its supported disposition. An unknown condition stays unknown.
An exact existing evidence or construction grant may still permit a bounded
discriminator or first candidate while unknown treatment holds dependent
reliance; return to that grant's declared consumer.
Unchanged valid C/J can survive a role/context switch, while a required
independent assessor supplies its own judgment rather than copying author J.

For the complete-update example, a plan digest alone does not permit effects;
stale selected source evidence holds the update; and completion requires every
selected resulting binding and companion to be verified. These rules must be
evaluated from exact task evidence. The projection itself supplies none of that
evidence and cannot authorize an actual consumer operation.

If an invocation was attempted but its resulting state is unavailable, hold
completion claims and automatic retry. That observation gap proves neither a
caught failure, crash or lost rollback storage, changed preimages, nor invalid
original authority or acceptance. Do not substitute any of those facts for the
unknown effect state.

Within an existing observation grant, obtain actual effect evidence first.
Then apply the supported completion, recovery or retry conditions, preserving
the original grant and exact acceptance while they remain applicable. Unknown
applicability remains unknown; it is neither established validity nor proven
revocation. Return to the owner only for a materially changed or newly ambiguous
reserved decision. The existing failure/recovery clause and its source routes
still govern an actual failure, changed preimages or unavailable rollback;
an observation gap alone does not establish that those conditions occurred.

On missing dependencies, stale source observations, a mismatched map or an
unresolved selection, consume the dependency's diagnostic and withhold the
affected view. Re-enter the source or candidate owner; do not hand-edit a map or
projection to bypass the refusal. The source owner determines any required
semantic re-authoring.

For a delegated request, include only the selected view, exact subject, frame
details, sufficient source/evidence routes, grant and return conditions. Author
the ordered text yourself and use the same dependency's unchanged pure joiner.
The target-specific Codex/Claude reference controls presentation only.
