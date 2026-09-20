# Work packet

This is a bounded software-project review task. All software effects in
`fixture.py` are in-memory. The observations are actual executions of that
fixture, not actual invocations of its hypothetical note-writing LLM.

## A. Inventory delivery

The Product accepts manifests of 1–200 uniquely identified items with nonnegative
integer quantities. Serialized input is untrusted. Native code and immutable
values returned by the declared owner constructor are trusted; defending against
hostile in-process reflection is excluded. Inventory identity is the exact
selected basis and item content. `construct_inventory` owns its facts. Delivery
appends the report only if the current destination generation equals the selected
predecessor. Changing a basis requires new relevant owner facts; changing the
destination does not change an immutable inventory. Opening a fresh process
requires construction from the retained raw manifest.

The current candidate is `fixture.py`. `prepare_report` and `resolve_delivery`
are called for each handoff. The migration note retains the final comparison
as a permanent production oracle with no owner, workload purpose or removal
trigger beyond “another check is safer.” A local review note proposes retaining
tests against forged native objects even though no supported raw entry uses
those objects. Independently, malformed serialized input and destination
advancement remain supported refusal conditions.

The accepted work envelope is: one inventory construction for an unchanged
manifest followed by three deliveries, including one current-generation
observation per attempted commit. One supported workload has 4 items and one has
200. The selected operational condition permits no item revisit solely for a
consumer handoff after the immutable owner facts exist. It does not constrain
necessary new-input validation, first construction or a fresh-process start.
There is no wall-clock or universal complexity quota. The proposed implementation
territory is `prepare_report` and `resolve_delivery`; the grant permits reading
the whole causal path. Findings outside that territory return to its owner.
The `item_visits` meter counts only iterations of the constructor's validation
loop; it excludes the separate identity-set, summation and serialization work.
It is a bounded work observation, not a total CPU or all-element-operations count.

Assess whether the candidate meets this bounded outcome. Account for retained
behavior, useful existing evidence, work performed, exceptions and remaining
owner decisions. Separately consider a call with an inventory from basis 17
against selected basis 18, and a destination whose generation advances between
selection and commit.

## B. Release notes

The supported public path is `public_note -> admit_note -> render_note`. The input is
a candidate containing a nonempty `summary` and unique `issueRefs`. References
must belong to the issue set admitted before this candidate under its selected
basis. An empty eligible set and an empty reference list are lawful. Inventing
a same-response issue or using a historical-only reference is not eligibility.
The public interface promises either an admitted rendered note or a typed
refusal with its cause; it does not promise that every candidate succeeds.

The ordinary author receives a task, the selected basis and the exact eligible
issue set or an accessible locator for it. The hypothetical normal author has
no access to consumer implementation or private helpers. A reviewer may inspect
the complete chain. `fixture.py` executes six retained records N1–N6 with actual
producer context, responses, selected consumer bases and observed exits.

The proposed release claim is: “All six observations demonstrate that ordinary
LLM users can write valid notes through the installed public interface.”
Evaluate that claim and the distinct narrower claims the evidence supports.
The fixture is the runnable subject; it is not an installed release and its
producer responses are recorded software values. Locate the supported causal
frontier of failed records and keep missing evidence explicit.

## C. Continuation record

Ticket W17 changes a report title to “Shipment summary” while preserving the
exported quantity. Exact C1 and C2 bytes are in `records/C1.md` and
`records/C2.md`; their retained record is `records/evidence.json`.
Owner ruling O1: “Continue the selected title change; preserve the quantity and
existing history. A separately recorded Writer may preserve this work as WIP.
Do not publish or change the Product or method basis.”

Existing authority selects method basis M1 for W17. A newer method M2 exists;
its availability selects no adoption. The standing fixture is runnable. A note
proposes restarting the project under M2 because all current artifacts are
re-derivable; it names no failed repair option or changed causal assumption.

Obligations: L1 title correctness; L2 quantity conservation; L3 author-independent
assessment of the exact title-bearing candidate. Candidate C1 has mechanical
E1, independent L2 result Q1 and author judgment J1. No L3 result exists. Q1's
recorded invalidator is a change to the quantity computation or its inputs;
that relation is unchanged in C2. C2 changes title markup materially, has current
E2 and author judgment J2. R1 independently reviewed C1 title markup only.

Evaluate these snapshots independently:

- S1: C1 is unchanged; a different conversation resumes the work. Its complete
  available evidence is O1/E1/Q1/J1. R1 and R2 are unavailable in this snapshot.
- S2: C2 is current; E2/Q1/J2 and old R1 are available.
- S3: The owner says only “continue”; a proposed status edit drops L3 and calls
  the Product accepted.
- S4: A current declared Writer grant covers one WIP checkpoint and the related
  ticket status sequence for C2, with included territory and parent identified.
  It records no concurrent Writer and preserves evidence with the checkpoint.
  The actor currently occupies Executive. No publication authority is granted.
- S5: Exact C2 receives a closed independent title review R2 with sufficient
  evidence, no findings and the named Executive return. E2/Q1 remain applicable;
  all W17 conditions now hold. No Product or release acceptance is delegated.

Prepare the smallest lawful continuation from S2. Retain original O1 separately
from interpretation; account for every obligation and the proposed restart.
Use the existing carrier. No actual checkpoint, status edit, actor launch,
publication or adoption is part of this native task.
