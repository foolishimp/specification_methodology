# STRATEGY: I5 construction from A to Z under finite resources

## Proposed direction

The organising problem is how to construct an acceptable outcome from the current state under finite resources and incomplete knowledge. The specification supplies the reference model of required conditions. The workspace and observations of material external state supply the evidence about reality. The method selects, composes, executes and evaluates bounded transitions between them.

Feedback is part of that construction: observe, compare, diagnose, select a response, act and observe again. It supports approaching the required conditions and maintaining them as circumstances change. A bug is a category of feature or change work within this same mechanism. Its cause determines the appropriate correction.

This records the product owner's I5 direction and a proposed scope for its implementation. It does not amend the ratified I4 specification, admit tenant I5 construction, or settle the outstanding I4 acceptance obligations.

## The construction problem

A describes the observed current state, including the limits of what is known. Z denotes the constraints on acceptable outcomes; several realised states may satisfy them. An available proof or a complete known path from A to Z cannot be assumed.

The computational problem includes discovering a candidate path, carrying out its operations, acquiring missing observations and establishing what its results support. Planning, construction and assurance all consume resources. The path may branch, execute independent work concurrently, or change in response to observations.

The core account needs these distinctions:

| Part | Responsibility |
|---|---|
| Current state and knowledge | Identify the material subject, relevant observations and explicit unknowns. An actor's account remains correctable against reality. |
| Required outcome | Bind the destination constraints, their meaning and the authority for changing them. |
| Transformations and composition | State admissible operations, preconditions, effects, preserved obligations and valid joins. |
| Execution binding | Relate the operations to a human, machine or mixed environment and its resource costs and limitations. |
| Strategy | Choose decomposition, ordering, concurrency and the timing of observation and assurance against the outcome and declared tradeoffs. |
| Evaluation and correction | Distinguish satisfaction, failure, missing information and the work needed next; preserve applicable results and uncertain effects. |

These are responsibilities to consolidate at the existing owners. They do not prescribe six documents or a new controller.

The specification is an internal reference model of what must hold. Predicting what an intervention will do may require a further causal model and observations. Desired conditions, predictions and observations must remain distinguishable.

## Strategies over the same problem

Steel thread, waterfall and iterative delivery can be described as alternative strategies for arranging construction and assurance. For example, a steel thread selects a bounded end-to-end path to expose its joins; a phased strategy groups work by successive descriptions or construction stages. Their suitability depends on the task and assumptions.

The common method should let a realisation explain the expected cost, time to useful feedback, uncertainty, integration exposure, rework and assurance of its chosen strategy. Those considerations can conflict. A claim that one strategy is best needs a declared comparison and evidence; finite resources alone select no universal winner.

An end-to-end feature retains its outer obligations while its work is decomposed. Completion of internal tasks does not establish delivery without the necessary joins and outcome evidence. Reference frames bound the context needed for the selected work. Coordination arrangements follow from its dependencies, resources and assurance needs.

## Recursion, proof and execution

Recursive decomposition and repair require an account of both preservation and progress. Correctness of one step, or preservation of an invariant through repeated steps, does not establish that repetition reaches Z. A particular recursive construction may admit an inductive correctness argument and a termination argument. Recursion alone makes neither proof impossible.

Hoare's program logic provides a useful precise distinction: composition and iteration can establish properties conditional on successful termination; termination needs further justification. [Hoare, 1969](https://sites.cs.ucsb.edu/~kemm/courses/cs266/acmhoare69.pdf)

There is also no general decision procedure for unrestricted termination questions. That limit concerns a universal decision procedure; it does not preclude proving particular programs or using decidable bounded models. [Turing, 1936](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)

For the method, absent proof becomes an explicit construction or assurance obligation. Bounded execution can discover a path, expose a counterexample or produce evidence for a particular result. A successful run supports the properties and scope it actually establishes; it does not automatically prove all future executions correct.

A feature-delivery episode needs an explicit completion condition. An ongoing maintenance process may legitimately continue. In either case the enclosing control handles exhaustion, failure, uncertainty, recovery and stopping without fabricating delivery. A resource stop establishes that the current attempt ended, not that Z was reached or is unreachable.

The proposed universal construction account therefore concerns a common way to state and govern construction problems across realisations. It makes no claim that every destination is reachable, every proof discoverable, or every strategy optimal.

## What I4 already supplies

The ratified common input is C3-I4-03 at `3c4c503d291e7cb19ba21333ba6caf6167be77c9`. This examination used main at `3800be50936048f2eb1f5a6455fb6d573f81e0f8` and the Codex I4 package at `903f1198ac038b05c941c0cbc2abeceb9b3978fd`, with final return at `9a93c5a3834837283b62f97cabe7182c60245114`. The live peer tenant was not inspected.

The common [Intent](../../../specification/INTENT.md#executive-summary) and [Product](../../../specification/PRODUCT.md#construction-and-context-management) already state A, Z, bounded transitions, finite context and attention, recoverable work and authorised destination changes. The [frame requirement](../../../specification/requirements/README.md#bounded-transitions-and-reference-frames) and [conformance cases](../../../specification/conformance/README.md) cover current-state acquisition, invalidation, unknowns and re-entry.

Within the frozen Codex package, paths below are relative to `specification_methodology/v3/build_tenants/codex/successor/standards/`:

| Existing owner | Existing contribution |
|---|---|
| `FOUNDATIONS.md`, Workspace and context; Bounded construction | Acquisition, operation, observation and reacquisition; A/Z; preserved work; total control handling; no automatic convergence claim. |
| `SPEC_METHOD.md`, Universal Intake Triage; Computed Classification And Treatment | One intake for bugs and features; causal diagnosis; candidate correction distinguished from changed governing meaning. |
| `SPEC_METHOD.md`, Proportional Method And Delivery; Checkpoint, Continuation, Progress, And Churn | Resource-sensitive priority, useful feedback, continuation and scrutiny of repeated failure. |
| `TICKET_METHOD.md`, Upward Propagation Check | Carries the owning classification into work at the appropriate requirement, design or realisation boundary. |
| `STDO_REFERENCE_FRAME_BASELINE.md`, Technical triage, severity, priority, and boundary effect | Separates consequence, ordering and authorised disposition within the selected operational configuration. |

This is not evidence that I4 lacks a feedback loop. It already contains substantial parts of this account. The proposed I5 change makes their composition the organising requirement and tests whether it reduces the decisions and joins needed to deliver a feature. Adding a name for the existing cycle would not demonstrate that improvement.

## Bounded I5 work

1. Revise the common Intent and Product around the construction problem and its resource, strategy, observation and assurance relationships. Connect the existing pillars without turning a preferred strategy or role arrangement into an axiom.
2. Bind the end-to-end feedback relation at its shared owner. Consolidate its consumers: intake, work selection, triage, realisation, evaluation, continuation and closure. Preserve distinctions between a defective realisation, an inadequate specification and insufficient observation.
3. Extend the existing conformance cases and use one bounded feature to exercise the composition. Carry supported I4 evidence with its applicability limits.
4. Review and ratify the exact common successor before dependent tenant construction. Each tenant implements the common outcome on its own line and supplies the affected interpretation and use evidence.

The bug list is a view of the existing work state. A ticket carries work that needs durable independent state. Neither needs a second truth surface merely because an observation is called a bug.

Proposed discriminators:

| Case | Required distinction |
|---|---|
| Implementation violates an adequate requirement | Diagnose and repair the affected realisation; verify the original counterexample and affected joins. |
| A user need exposes an inadequate requirement | Revise the model through its owner and carry the changed obligations forward. The new destination does not establish achievement of the old one. |
| The observation cannot distinguish failure from missing evidence | Acquire discriminating evidence or retain uncertainty; avoid inventing either success or a defect. |
| A later observation invalidates an accepted condition | Reopen affected work while retaining independently applicable progress. |
| Repair recurs or is interrupted | Check causal change and progress, reacquire current reality, reconcile uncertain effects and continue within authority or stop explicitly. |
| Two strategies address the same feature | Compare equivalent outcome obligations under stated resources and assumptions, including assurance and rework costs. |
| Local steps pass but the end-to-end feature fails | Preserve the outer failure; task completion cannot substitute for the required composition. |

The test of I5 is a simpler, coherent account governing actual delivery decisions. Outstanding I4 member acceptance, interpretation fidelity, practical comparison and release qualification remain separate obligations.

