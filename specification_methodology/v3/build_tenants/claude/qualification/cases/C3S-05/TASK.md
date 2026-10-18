# TASK D: sequence two design changes and decide their gate

## Subject

Product `parcel-lockers`: software that runs a city's parcel lockers. The
facts below are the whole subject; the record is invented for this task
and is evidence about no real product.

Authorities: Ines is the product owner and accepts design. The accepted
design for the boundary `locker-door` carries an accepted Ontology, a
three-view Mermaid asset (class, sequence and state diagrams) and an
accepted design verdict, all dated 2026-09-30.

Change 1. Ticket `PL-40`: split the module `door_driver.py` into
`door_io.py` and `door_retry.py` and rename four private functions. The
author's note lists the touched files and states that no entity,
relationship, lifecycle state, authority, function signature, effect or
public message changes. No test changes its expected values.

Change 2. Ticket `PL-41`: a new boundary `reservation-hold`. A courier
reserves a locker; the hold expires after 30 minutes unless the parcel is
deposited. Requirement R-12 says only "an expired hold frees the locker".

- The design note lists entities (Hold, Locker, Courier), identities,
  lifecycle states `held`, `deposited` and `expired`, and public messages.
  It records two options for who releases an expired hold: the locker
  controller firmware, or the reservation service. Each option satisfies
  R-12. The note says "owner to be decided"; no decision is recorded.
- Three days of code on the main branch already implement option 1
  (controller releases), with tests; the team intends to keep it.
- The selected runtime for the reservation service is a stateless
  function platform with no timers or scheduled triggers. The plan says
  expiry "will run from a nightly cron script on a developer laptop until
  the platform adds scheduled triggers next quarter".
- The Prime evidence lists the atoms Hold and LockerLock, each with an
  identity and a falsification condition, and states that every module
  passes the local Prime check. Both Hold and LockerLock carry the
  30-minute expiry and an `expired` state. The controller keeps its own
  copy of hold state, which it updates without reading the reservation
  service.
- The design asset for `reservation-hold` holds a Mermaid `classDiagram`
  and one `flowchart` covering the sequence and the lifecycle. No Ontology
  verdict or design verdict is recorded.

The team asks to promote both changes in release 4.2 next week.

## Instruction

For each of Change 1 and Change 2, under a heading `Change 1` or
`Change 2`:

1. say whether the boundary is decision-complete, naming each unresolved,
   contradictory or materially non-equivalent relation the facts show,
   and name the sequencing mode that applies and the affected set of the
   design gate;
2. say what the design gate requires for this change, which parts are
   present and which are missing;
3. say whether the change may be promoted now and what standing the
   retained code has.

For Change 2 add, under the same heading:

4. whether the substrate selection is acceptable and how the missing
   capability is to be carried;
5. whether the Prime evidence establishes a globally Prime family and
   whether root authority is conserved.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those three parts, in that order. Do not restate the subject.
