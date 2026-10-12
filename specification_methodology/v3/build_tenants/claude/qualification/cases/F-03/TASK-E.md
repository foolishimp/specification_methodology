# TASK E: decide edge closures, a composition and two negative proofs

## Subject

Product `parcel-router`: a graph-native product that assigns parcels to
delivery depots. The facts below are the whole subject; the record is
invented for this task and is evidence about no real product.

Edges. Each edge below was just evaluated by `evaluate_action` on the
basis `B-31` (requirement `R-7` version 2, design `D-4`, admitted
evidence ledger at event 880).

- `E-13` (geocode 300 addresses). The geocoding worker was stopped after
  40 minutes without a heartbeat. 120 of 300 rows were geocoded and
  admitted as progress. The resume point is recorded in the event log. No
  evidence has been admitted against the edge's obligations, and the same
  action is still lawful on `B-31`.
- `E-14` (normalise postcodes). The output fails obligation `O-2`: 17
  postcodes keep a trailing space. The fault is in the function's code;
  running the same action unchanged gives the same output. `R-7` and
  `D-4` are unchanged and consistent with each other.
- `E-15` (assign depots). Since `B-31` was fixed, `R-7` version 3 has
  been accepted by its owner and has superseded version 2. Version 3
  changes the depot catchment rule that `E-15`'s obligations rest on.
- `E-16` (assign depots for Ireland). Finishing this edge would need
  Irish addresses to be routed. No selected outcome and no admitted bound
  covers Ireland. The product owner, Ana, has not been asked.

Composition. The GTL module publishes three graph functions in a line:
`parse_address` returns `raw_address` and `parsed_address`;
`normalise` takes `parsed_address` and returns `normal_address`;
`route` needs `normal_address` and, for its audit trail, `raw_address`.
Every function's published input is "the output of the previous
function". No function declares `environment.requires`,
`environment.provides` or `environment.carries`.

Negative proofs offered for the claim "a tenant whose token is revoked
cannot dispatch a parcel":

- `N-1`: a fixture constructs a `DispatchRefused` event, appends it to a
  test log, and asserts that the gaps view shows `refused`.
- `N-2`: the public `parcel dispatch` command is run with a revoked
  tenant token. The ABG event log shows the refusal derived by the
  admitted composition, before any dispatch effect is recorded. The
  legacy HTTP endpoint `/v1/dispatch` still ships in the installed
  package and was not exercised.

## Instruction

1. For each of `E-13`, `E-14`, `E-15` and `E-16`, give the closure
   decision, the core result member it maps to, and the fact that selects
   both.
2. For the composition, say whether `route` may lawfully obtain
   `raw_address`, and what the method says about the line as it is
   published.
3. For each of `N-1` and `N-2`, say whether it is closure-grade negative
   evidence, naming each required element that is present or missing.

Then, under a heading `No method source`, list anything the task needed
that the METHOD block did not supply; write `none` if nothing.

Return only those four parts, in that order. Do not restate the subject.
