# TASK H: judge two entity cuts and their attributes

## Subject

Builder project `harbourworks` constructs a world model of a port
authority's operating model. The facts below are the whole subject; the
record is invented for this task and is evidence about no real product.

Cut `C-1` "Berth" (published 2026-09-02):

- identity: the berth code (for example `B-07`) assigned in the harbour
  master's berth register, edition 2026-3;
- boundary: the quay length between two bollard numbers as the register
  records it; the cut states that lay-by quays, physically similar, are
  never allocated to vessels and are therefore not berths;
  this rests on the register text, not on any intervention;
- authority: the harbour master's office;
- state: `available`, `allocated` or `closed`, from the allocation system;
- evidence: register 2026-3 and the allocation system's berth table;
- treatment: the pilotage domain treats a berth as a destination
  (pilotage manual section 2);
- covariance: "no covariance study performed; none claimed";
- ambiguity: "berths B-07 and B-08 share bollard 41; unresolved".

Cut `C-2` "Vessel call" (draft):

- identity: the call id from the port community system;
- boundary: the list of columns of the table `calls`;
- authority: the field is empty;
- state: `expected`, `alongside`, `departed`, from the port community
  system;
- evidence: the `calls` table;
- treatment: "customs treats a call as an import declaration", written
  by the builder from general knowledge; no customs source was consulted;
- covariance: the cut has no covariance field;
- ambiguity: "none".

Attributes published on `C-1`:

- `max_draught = 11.2 m` has a ledger entry: value, register 2026-3 page
  4, authority harbour master, observed 2026-03-01, published 2026-09-02;
- `tug_required = true` appears on the published cut and has no ledger
  entry; the builder reports it came from a conversation with a pilot.

On 2026-10-05 the builder edited the published `C-1` in place, moving the
boundary of `B-07` to end at bollard 42, under the same cut identity.

## Instruction

1. For each of `C-1` and `C-2`, take the eight admissibility surfaces in
   turn and say whether each is a stated value, a stated absence, a stated
   non-applicability or none of these. Then say whether the cut is
   discriminated from a plausible alternative, and on what kind of
   evidence.
2. For `max_draught` and `tug_required`, say whether each has a lawful
   claim record and what follows for `C-1`.
3. Say whether the edit of 2026-10-05 is lawful and what publication
   requires instead.
4. Give each profile verdict reached in 1 to 3, with its core member and
   the counterexample where there is one.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those five parts, in that order. Do not restate the subject.
