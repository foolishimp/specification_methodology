# Coordinated Skill Handoff

Use this reference when issuing work to another activation or receiving its
packet. A direct invocation with sufficient context and authority follows the
skill's ordinary procedure. The active frame and grant decide the branch;
writing “Executive”, “Worker” or “receive” in a prompt grants nothing.

Resolve the named owners through [Product Basis Selection](PRODUCT_BASIS.md)
on the Product's exact basis. `REFERENCE_FRAME` §11 owns the packet;
`ACTIVATION` §1–3, §5 and §7 own admission, acquisition, effects and reuse;
`EXECUTIVE_BASELINE` §6, §12–13 and §19 apply where that profile is adopted.
This reference supplies their interaction route, not replacement authority.
A missing owner route is unresolved; do not substitute a neighbouring cut.

## Issue

1. **Select the authorized unit.** Verify the current outcome, checkpoint,
   selected basis, accepted frame configuration and applicable grant/admission. Use
   the applicable entry if the admitted contract supplies an activation
   table. Otherwise use its sufficient authorized intake. The carrier can
   be a ticket, sprint entry or run contract. Preserve applicable existing
   grants; an absent ticket does not require creating one. A missing unit or
   material scope change returns to its owning contract/admission route.
   Work admission, an assessment grant and read-only orientation are distinct:
   apply the relation the selected operation requires, not an automatic
   execution contract for every question.
2. **Bind the packet by reference.** Use exact source identities and locators
   in the existing carrier. Include only the instruction and material
   bindings the recipient needs; do not rewrite the target skill as a brief.

   | Binding | Recipient must be able to establish |
   |---|---|
   | Task | Activation/frame identity, purpose, requested skill, entry and bounded outcome |
   | Basis | Product Definition identity/path, immutable method URI and manifest digest, accepted frame basis and exact subject/checkpoint |
   | Authority | Contract/grant identity or digest, applicable admission decision/evidence, actor/role, inherited operations, mutation subject and write territory where applicable |
   | Acquisition | Authorized bootstrap/control sources, material read set and routes, tools/channels, exclusions and inline material's provenance |
   | Envelope | Required capability, context and resource limits; actual host/inheritance binding; applicable independence conditions |
   | Result | Result algebra, durable result/evidence surface, consumer, permitted return projection and any required conjunction/dependency results |
   | Continuation | Applicable predecessor's closed result, validity conditions, stop/re-entry conditions and the next decision boundary |

   A reference works only if the recipient may resolve it and its meaning is
   sufficient for this task. Names and hashes alone do not supply the missing
   contract. Inline text remains acquired information: it needs the same
   recipient eligibility and provenance as a referenced source. An issuer's
   wider access cannot authorize copying excluded information into the packet.
   Where the Product declares supported context, preflight, dispatch or evidence
   tools, use those contracts and retain their actual receipts. Do not replace
   required computation with a hand-written claim or invent tool success. A
   receipt keeps its bounded meaning; it neither grants authority nor replaces
   source/semantic judgment. Tooling availability creates no new dependency.
3. **Check the acquisition the packet prescribes.** Consider command output,
   diagnostics, logs, file lists and embedded context as well as direct reads.
   For example, requiring verbatim commit output while excluding filenames
   that command prints is a contradiction. Resolve it before dispatch using
   an already-permitted alternative, or return for the required re-entry.
   Redacting output after the recipient has seen it does not undo acquisition.
   This check establishes no general proof about arbitrary command behavior;
   an unresolved material output boundary prevents that command's use.
4. **Bind the host and dispatch.** Apply [Host Binding](#host-binding) and send
   the packet to the selected actor with the instruction to invoke this same
   skill as its recipient. Do not transfer ambient conversation by default
   where the frame excludes it. Record the dispatch/activation identity and
   actual mechanism in the existing carrier through its authorized Writer.
   If no available authorized mechanism meets the required boundary, retain
   the packet and return “not dispatched” with the missing capability. A
   prepared packet is not an active Worker or a work result.

The issuer remains in its coordinating frame. It acquires no mutation grant
by arranging the work. Where one same-actor role transition is sufficient and
permitted, bind and record that transition explicitly; do not pretend it
cleared information already acquired (`EXECUTIVE_BASELINE` §6 and §17).

## Receive

Do this **before the skill's general discovery, classification or subject
reads**, and before effects. The packet permits only its authorized control
reads while activation is being checked; it does not validate itself.

1. Identify the packet's requested frame, consumer and acquisition boundary.
   Read only the named, authorized control inputs needed to verify it: the
   Product Definition, exact installed basis, accepted frame basis, contract/grant,
   applicable admission evidence and required predecessor result. Apply
   [Product Basis Selection](PRODUCT_BASIS.md) inside that search boundary;
   do not broaden discovery to find a more convenient definition. If these
   control reads cannot lawfully resolve the binding, return the mismatch or
   unavailable input without reading the work subject.
2. Compare the actual subject/checkpoint, contract, admission, actor/grants,
   permitted acquisition and required host properties with the packet. Check
   referenced digests/currentness and predecessor validity. Check commands
   and inline material against the same recipient boundary as the issuer.
   A known mismatch returns `activation_refusal` with its cause and the core
   result prescribed by `ACTIVATION` §3; do not manufacture a Worker result
   for an activation that never occurred. Keep an unresolved required binding
   unresolved and return the owning missing-input/capability re-entry.
3. On a valid binding, run this skill's ordinary procedure within the packet's
   frame and grant. Reuse the verified selection and still-valid facts; do not
   ask for admission again merely because a new actor received the work. A
   request to edit, run a command or read another source still needs the
   operation/acquisition authority already bound to it.
4. Record the skill's closed result on the named surface within its write
   grant, then send the permitted return projection to the named consumer.
   A read-only recipient returns through the declared read-only channel; an
   authorized recorder owns any required persistent write. Include exact
   subject/basis, evidence routes, residuals, validity and effect uncertainty.
   If the named result relation cannot be fulfilled, report the obstruction;
   do not redirect the result to an arbitrary file or claim closure. Stop at
   the packet's return boundary.

## Evaluate The Return

The issuer checks activation identity, exact subject/basis, result variant,
evidence scope and invalidators before relying on the return. It acquires
only the return projection its own frame permits; a link to a full artifact
does not authorize reading it. A digest authenticates bytes, not their claims.

Reconcile an effect whose completion or end remains unknown before retry or
any dependent action (`ACTIVATION` §3 Effects and §5). A timeout, missing
message or lost context is not evidence that no effect occurred. Retain valid
progress; do not replay a step merely because its actor changed.

Apply the governing result/disposition relation and determine whether the
exact candidate requires independent review. Issue `stdo-review` separately
where required. Reviewer severity remains its technical assessment; the
decision owner assigns priority and boundary effect within its grant
(`EXECUTIVE_BASELINE` §12 steps 4–7). Do not turn a closed result into implicit
authority to repair, accept, publish or start the next stage.

For an admitted sequence, each continuation uses the previous closed result
and current bindings. Retain the boundaries the contract actually declares:
neither a new human check-in at every pass nor review only at the end is a
universal rule. Refresh affected bindings on material change, not every
unchanged status observation (`ACTIVATION` §1 Roles and delegation; §7).

## Host Binding

Use the host's actually available delegation or separate-session mechanism.
Record the selected actor/model where exposed, worksite, supplied packet,
inherited history/instructions, available tool/permission settings and return
channel. Respect the admitted context/resource envelope. Unknown required
properties withhold dispatch; optional unobserved properties are explicit
limits. Tool availability alone grants no operation.

- **Codex:** inspect the exposed delegation/session controls. Where the host
  offers conversation inheritance or forking, choose a packet-only context
  when the frame requires it and bind any other automatically supplied
  instructions. A resumed actor retains its earlier context; use it only
  when that context is permitted. Return and wait through the actual actor
  identity, not an invented worker name. If this host has no suitable
  delegation mechanism, return the prepared packet without claiming dispatch.
- **Claude:** select the available subagent/session mechanism and inspect the
  selected agent definition, inherited instructions, tool permissions and
  worksite. Supply the packet and target skill explicitly. A subagent label
  or a resumed session does not establish a clean context. Return through
  the actual task/result mechanism; if its properties cannot meet a required
  boundary, return the unsupported activation rather than silently executing
  in the issuer's context.

Neither host's fresh context alone proves information-flow enforcement or
independent assessment. Independence additionally uses `EVALUATION` §3's
authorship and evidence conditions and the Product's actor-family policy.
Do not broaden permissions, change host configuration or install a runtime
to make a dispatch work without the existing authority for those effects.

## Invocation Examples

These are requests to the skill, not substitutes for their referenced grants.
Use the host's installed skill invocation syntax or open its exact entrypoint.

```text
Use stdo-work as issuer for the admitted W1 entry in <carrier at exact identity>.
Keep my Executive frame. Issue its permitted packet and evaluate the return.
```

```text
Use stdo-work as recipient of <packet at exact identity>.
Check its control bindings before subject reads, execute its authorized unit,
and return through the packet's result relation.
```

```text
Use stdo-review to issue the required review of <exact candidate> under
<assessment grant>. Preserve its independence conditions and return boundary.
```

For direct work, “Use stdo-work for <authorized bounded change>” continues to
use the ordinary direct path when the accepted configuration permits it.
