# Verification

**Family**: REQ-VERIFY-*
**Status**: Active
**Category**: Verification

These requirements say how the product is shown to work. The scenarios are in
[SCENARIOS.md](SCENARIOS.md).

### REQ-VERIFY-001 The product is shown to work by scenarios

Each scenario in [SCENARIOS.md](SCENARIOS.md) is run from its start to its end.
Scenario S1 is the first thing built. No later change to this product is
accepted while S1 does not end as it should.

Acceptance:

- The history of this product shows both.

From: goals, "First build".

### REQ-VERIFY-002 A scenario is driven by a user, on the installed product

**Status**: Deferred: the user put it off on 23 November 2026, in ticket
261124-055459-1851.

A scenario is run on the product as a user installs it, in a new folder, with a
live LLM agent doing the work unless the scenario names a stand-in. It is
driven by a person, or by an LLM agent standing in for one. The driver is given
the product's instructions for users and the scenario's stated inputs, and
nothing else. The driver does only what a user may and the scenario says: it
starts runs, writes tickets, gives answers, and changes or deletes a file by
hand where the scenario says so. It repairs nothing, and it neither reads nor
changes the framework's source. The sample products that scenarios build are
inputs to the scenarios and no part of this product.

Acceptance:

- Scenario S1 is run a second time, by a driver that has not seen the first
  run, and ends as it should.

From: intent, outcome 5.

### REQ-VERIFY-003 A scenario is judged from the workspace it leaves

**Status**: Deferred: the user put it off on 23 November 2026, in ticket
261124-055459-1851.

Whether a scenario ended as it should is decided from the workspace it leaves.
Where a scenario compares the workspace with an earlier state, or must show
that something survived an interruption, the driver records that state or
places a marker beforehand.

Acceptance:

- A second person, given only that workspace and what the driver recorded,
  reaches the same verdict.

From: intent, outcome 3.

### REQ-VERIFY-004 Each algorithm is tested by its value

Each algorithm in [ALGORITHMS.md](ALGORITHMS.md) is tested apart from any
session: for stated inputs, the product returns the stated output. The stated
outputs are worked out by hand from the requirement, not taken from the
product.

Acceptance:

- For each algorithm there is at least one such test for each of its laws.
- The tests name nothing of the technology stack.

From: intent, guard rail 1; [how work is done](../REFERENCE_FRAME_BASIS.md),
"How the product is specified and built".
