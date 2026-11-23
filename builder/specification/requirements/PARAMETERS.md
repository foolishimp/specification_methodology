# Parameters

**Family**: REQ-PARAM-*
**Status**: Active
**Category**: Constraint / Guarantee

The algorithms and flows say what the product does. This page says how much,
how fast and for how many. Every number is stated here and nowhere else.

### REQ-PARAM-001 The scale the product is built for

| Parameter | Value | Counted how |
|---|---|---|
| Address spaces the framework runs in | 1 | It is not distributed: no part of it runs anywhere else |
| Users of one workspace | 1 | |
| Active tickets | 1. With REQ-FLOW-009 in force: as the settings file says, and 3 where it says nothing | Counted on main |
| Runs under way on one ticket | 1 | |
| Sessions at work on one ticket | 1 | At any moment |
| Vectors in a governing graph | up to 200 | Inner vectors included |
| Files in a workspace | up to 100,000 | Files git ignores not counted |
| Entries in an event log | up to 100,000 | |
| Size of a brief | up to 100 lines | |

Acceptance:

- Every figure below holds at every size in this table.

From: product definition, "The framework runs within a single address space"
and "Several tickets may be active at once".

### REQ-PARAM-002 What the framework's own work may cost

| Parameter | Value | Counted how |
|---|---|---|
| The framework's own time for a step | up to 10 seconds | Within one run: from one session's return to the next session's start, less the time the vector's checks take |
| Its growth with the event log | under 1 second | Between a log of 100 entries and one of 10,000 |
| Time to answer `stands` | up to 10 seconds | From the command to its answer |

Acceptance:

- Measured with a stand-in agent, on a workspace and an event log at the sizes
  of REQ-PARAM-001, each figure holds.

From: product definition, "The framework's own work for a step is small and
does not grow with the history of the work."

### REQ-PARAM-003 Limits on a step and on a run

| Parameter | Value | Counted how |
|---|---|---|
| Attempts at one vector | as the graph declares; 3 where it declares none | Each no of an evaluation or of the user at the vector, in the run that made the evaluation or asked the user |
| Time for one session | as the graph declares; 60 minutes where it declares none | From its start to its return |
| Sessions or time for one run | no limit, unless the settings file sets one | A run that reaches it ends as stopped |

Acceptance:

- A run limited to three sessions ends as stopped after the third.

From: product definition, "Build"; the user, in ticket 261123-100659-a0d5.
