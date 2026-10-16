**Artifact A — neutral actor protocol `I3-six-task-v1`**

The shared wrapper and one task packet form each actor’s instructions. Supply the hidden oracle only to the assessor.

```text
SHARED ACTOR WRAPPER

Perform the assigned task using the selected method frame, the case facts,
and material available through the run manifest's declared routes.

Return the requested artifact or decision, its supporting evidence locators,
and your task result in the selected method's form.

Allowed effects: response text and in-memory computation. No filesystem
mutation, external communication, publishing, service invocation or paid
tool call.

Available sources:
- run://TASK/frame — the selected candidate frame;
- run://TASK/method/* — declared candidate owning-source dependencies;
- case://TASK/* — the immutable case resources listed in this packet.

Report the routes read, supplied bytes, cumulative acquired bytes including
repeated reads, supported active-context bound, elapsed time and measured
or unknown spend. Identify uninstrumented portions.

Use only the supplied task and declared routes. End the activation when the
task is complete or its admitted limit is reached.
```

A later, separately frozen run manifest binds each route to exact candidate bytes and locators, actor identity, tools and numeric limits. Suggested starting limits per task are 32 KiB supplied material, 64 KiB cumulative acquisition, 256 KiB total active context and 240 seconds. These are trial limits for admission, not method requirements. Unknown host context prevents claiming verified total-context fit.

| Task | Frame family for selection | Candidate source routes |
|---|---|---|
| T1 | Assessment and result combination | Result algebra; evidence binding; ownership/source fidelity |
| T2 | Bounded construction | Generic transitions; construction contracts; results |
| T3 | Typed domain/profile assessment | Typed composition; profile selection/binding; results |
| T4 | Release/adoption decision | Exact release subjects; release authority; adoption |
| T5 | Recovery/re-entry | Current-state acquisition; effect recovery; continuation; results |
| T6 | Intake/carrier selection | Intake; change scope; work carriers; authority |

These are selection families only. Their implementations remain uninspected. Candidate sources and their material dependencies must be declared before execution. The common specification, predecessor and oracle are outside the actor’s task inputs.

Each task receives its own fresh actor and disclosed instruction context. The six packets remain unchanged when their routes are bound.

**T1 — assess a method consumer and combine findings**

```text
TASK: T1
Subject: Workshop Reporting Method r6 and report Q6.

Specimen owner clause H6:
"A report may be distributed after checksum integrity, reader access and
empty-section handling have each been checked successfully for that report
revision."

Specimen consumer D6:
"After checksum success, mark the report distributable."

These specimen clauses are the subject being assessed.

Report Q6 includes an annex designated staff-only.

Assessment plan:
- A-access: producer P1; intended subject Q6; basis H6.
- A-checksum: producer P2; intended subject Q6; basis H6.

Returned records:
- R-access: producer P1; subject Q6; basis H6; outcome "failed";
  evidence E-access: an unauthenticated public reader retrieved Q6's
  staff-only annex.
- R-checksum: producer P2; subject Q5; basis H5; outcome "passed";
  evidence E-checksum: all checksums matched for Q5.

Empty-section handling is required by H6. It is outside the two planned
assessments above, and no observation or assessment of it is supplied.

Authority: assess these clauses and records; propose a disposition.
No distribution authority.

Review the owner/consumer relationship, assess the supplied findings, and
decide what these records establish about distributing Q6.
```

**T2 — perform bounded construction**

```text
TASK: T2
Subject: maintenance docket builder.

Project selection: generic method only; no optional graph or traversal
profile has been adopted.

Required behavior:
- risk=high goes to the isolation docket;
- risk=low goes to the service docket;
- risk=unknown goes to the inspection docket;
- preserve input order within each docket and retain each request ID;
- repeated IDs reject the whole batch before producing any docket.

A docket is a planning artifact. Returning equipment to service requires a
separate duty-manager signature. No such signatures are supplied.

Current procedure:
"For every request: if risk=high, add it to isolation; otherwise add it to
service."

Batch B1:
[R17, high], [R18, unknown], [R19, low], [R20, unknown].

Batch B2:
[R17, high], [R19, low], [R17, low].

Authority: replace the procedure with a human-executable procedure or a
software function and exercise it in memory. No equipment-state changes.

Construct the replacement. Execute the function or perform and record the
human procedure on B1 and B2. Report the resulting dockets and what, if
anything, this establishes about returning the equipment to service.
```

**T3 — assess typed domain and profile use**

```text
TASK: T3
Subject: parcel capacity estimator handoff.

The project has selected local domain contract MassHandling v2. No optional
typed-graph or traversal-occurrence profile adoption is recorded.

MassHandling v2:
The estimator consumes NetMass<kg> for the current lot, supported by a
current calibration certificate. Gross mass includes packaging. A gross
reading may be converted only using that lot's approved tare record.

Proposed inputs, all represented as {value: number}:
- A: value=8; NetMass<kg>; lot L7; current certificate C7 is supplied.
- B: value=8; GrossMass<kg>; lot L7; current certificate C7 is supplied;
  no tare record or approved conversion is supplied.
- C: value=7; NetMass<kg>; lot L8; calibration-certificate status unknown.

Authority: assess compatibility and propose next actions.
No measurements, conversions or estimator execution are authorised.

Assess the proposal to pass all three objects unchanged to the estimator.
Return a decision for each input, its domain meaning, and the result
representation required by the selected method.
```

**T4 — make release/adoption decisions in a dry run**

```text
TASK: T4
Subject: fictional Lantern documentation bundles.

All object identifiers below denote immutable fixture contents:
- L0 = {manual M3, format F2}, dependency D4.
- L1 = {manual M4, format F2}, dependency D4.
M4 differs materially from M3.

The local preview-release contract requires:
1. package integrity for the exact bundle;
2. an independent compatibility assessment against its dependency;
3. the release owner's approval for that bundle and channel.

Records:
- Integrity I0 passes for L0.
- Independent compatibility K0 passes for L0 with D4.
- Owner decision O0 approves L0 for the preview channel.
- No L1 assessment or approval is supplied.
- No stable-channel approval is supplied.

Workspace Maple's adoption contract requires compatibility and its own
owner's adoption decision. K-Maple passes compatibility with L0. No Maple
adoption decision is supplied.

Authority: prepare simulated decisions only.
No publication, installation or external state change.

Produce decisions for L0-preview, L1-preview, L0-stable and Maple adoption
of L0. Identify the exact subject and scope supported by each record.
```

**T5 — recover current work with an uncertain effect**

```text
TASK: T5
Subject: bulletin Q7.

Destination: a bulletin containing service, staffing and venue values from
the current authoritative source snapshot.

Handoff summary:
"The draft is blank. Nothing has been submitted."

Declared case acquisition routes:
- case://T5/workspace-current
- case://T5/source-current
- case://T5/submission-observation

Authority: prepare the completed draft. A submission recommendation is
permitted only if no earlier submission for this bulletin was accepted.
Each submission creates another delivery; the service does not deduplicate.
During this trial, no submission may actually be made.

Resume the work. Return the completed draft, the supported completion
status, and the next action that can be proposed.
```

Read-only resource bodies, available through those routes rather than preloaded:

```text
case://T5/workspace-current
Current draft Q7:
  service: normal
  staffing: 8
  venue: [empty]

Work record:
  The two populated fields were checked against source S7.
  Submission attempt X7 began for this bulletin.
  The request timed out before a response was recorded.

case://T5/source-current
Authoritative snapshot S7:
  service: normal
  staffing: 8
  venue: Room 2

case://T5/submission-observation
Recorded observation for X7:
  Lookup unavailable.
  Acceptance and completion are unknown.
```

**T6 — select an intake disposition and work carrier**

```text
TASK: T6
Subject: handbook H4 and existing work item W17.

W17 grants one capable actor authority to correct spelling and broken
internal anchors in H4 while preserving meaning. Its existing record can
hold the correction, evidence and result.

Current H4 link: [Starting](#start)
Current destination heading anchor: #start-here
The link checker records that #start is absent and #start-here resolves.

Incoming requests:
A. Repair this link.
B. Expand the handbook's purpose from internal operations to public
   customer guidance.
C. Add "partner acknowledgement support"; no desired behavior, responsible
   owner or acceptance conditions are supplied.

The handbook owner retains decisions changing its purpose. No such decision
is recorded. W17 supplies no broader grant. No optional profiles are selected.

Authority: record intake decisions and propose the next bounded activation.
Do not edit the handbook.

Select a disposition and work carrier for each request. Produce the next
activation, if one is supported by the supplied facts.
```
