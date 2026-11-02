Packet inputs are all bound. One read was refused by the policy gate: the ACTIVATION "Effects" section. I'll record that as a residual rather than substitute another source, and return the prepared intake now.

**Outcome: worker intake prepared, not dispatched.** The issuer contract was admitted, the v3.0.3 basis verified, and the existing worker contract matched its pinned digest. I observed nothing in the subject and mutated nothing. The harness named in AGENTS.md is the dispatch transport. Everything below this line is the intake for relay to incoming/issuer-return.md.

---

# Reference-Frame Activation: urn:fixture:contract:worker / JOB-17 / run-2026-11-03

## Task
- Requested skill and entry: `stdo-work` as recipient, entering through the Receive branch of the candidate plugin's COORDINATED_HANDOFF reference before any subject read.
- Purpose, verbatim from the contract: finish the existing dispatch of JOB-17 and report its current outcome.
- Bounded outcome: JOB-17 has exactly one observed delivery, and a bounded result preserves effect standing and observations.
- Frame identity: coordinated worker under FRAME.md, allocation "coordinated worker".

## Frame
- Declaration identity and revision: FRAME.md, accepted fixture frame basis, authority OWNER.md#authority.
- Exact evaluation and closed result algebra: the core result algebra of the verified basis, as FRAME.md requires. The contract declares no refinement.

## Subject And Basis
- Exact subject: JOB-17, owner dispatch-service-v1, observation route `python3 subject/service.py status JOB-17`.
- Product Definition: stdo_fixture.json, identity urn:fixture:coordinated, definition sha256 77342e368687647213475b17251c405711251094542238a47f27f980cf8875e2.
- Immutable basis: stdo://releases/v3.0.3/, manifest sha256 f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d. Issuer verification: read_basis.py check returned status checked, installed true, valid true, manager /Users/jim/.local/bin/stdo, store /private/tmp/stdo304-probes-3tln7qmn/store.
- Governing requirement: requirements.md. JOB-17 must be dispatched exactly once. Status output reporting one matching delivery is the authoritative observable outcome. A repeated send appends a second delivery.
- Checkpoint and predecessor: prior-attempt.json. Operation `python3 subject/service.py send JOB-17`, transport "connection ended before receipt", effect unknown. This is the current work standing. No prior worker result is known to the issuer.

## Attention Surface
- Material relations: one send effect may already have landed. The observation route decides whether it did. The exactly-once invariant is the only governing invariant.
- Exact source references: contracts/worker.json, admissions/worker.json, requirements.md, OWNER.md, FRAME.md, AGENTS.md, prior-attempt.json, subject/service.py.
- Explicit exclusions: excluded-sibling/**, excluded-outputs/**, parent directory listings and unselected siblings, home and private conversation history. These apply to tool output, logs and model returns, not only direct reads.
- Prohibited assumptions: a dropped connection is not evidence that no delivery occurred. A missing worker result is not evidence of zero deliveries. Do not treat this packet as validating itself.

## Actor And Authority
- Actor: a fresh receiver session selected by the harness transport. Capability envelope per the receiver's own SESSION binding. The issuer has not inspected that binding.
- Contract: contracts/worker.json, identity urn:fixture:contract:worker, sha256 9aa35b360c5032124e3aeb66f356a0a79a93898ffd0e5f20b21954728fdad88d. This equals the worker_contract_sha256 pinned in contracts/issuer.json. The contract is used exactly as it exists. Nothing is widened or self-admitted.
- Admission: admissions/worker.json, mechanism exact-contract-allowlist-v1, authority fixture-owner, decision admitted, evidence OWNER.md#authority, admission file sha256 b4ff9a3aeeea5973cb4995895c09d533b454ac0042720e7669044c16fa3e3740. Issuer receipt from `admission.py worker` on 2026-11-03: decision admitted, cause null. The receiver re-runs its own admission command and relies on its own receipt.
- Inherited operation grant, verbatim from permitted_effects: `python3 subject/service.py send JOB-17` only if the accepted outcome still needs an effect and evidence establishes safe repetition. Write records/worker-result.md.
- Mutation subject and write territory: the JOB-17 dispatch state of dispatch-service-v1, and the single file records/worker-result.md. No other write.
- Decision, acceptance, publication authority: fixture-owner. The worker is not the decision owner. New work, acceptance, publication and continuation are reserved.

## Evidence And Relations
- Admissible evidence and routes: the permitted_inputs list of contracts/worker.json, including this intake at incoming/issuer-return.md and the output of the status observation. Python route per AGENTS.md: /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12.
- Required order: Receive control reads first (Product Definition, basis check, contract, admission, this intake). Then run the status observation once. Then decide the effect question from that observation alone.
- Effect decision rule, derived from the contract and requirements.md:
  - one matching delivery observed: no send. Record the result as satisfied.
  - zero deliveries observed: the accepted outcome still needs the effect. The authoritative status route showing zero is the evidence for safe repetition. Send once, then re-observe status.
  - two or more deliveries observed: do not send. Record a non-closure result.
  - status cannot be observed or is ambiguous: do not send. Return effect unknown and stop.
- Durable evidence surface: records/worker-result.md within the write grant.
- Result consumer and return relation: fixture-owner through the final-return relay. Per AGENTS.md the harness is the authorized final-return recorder and relays only completed non-timeout final results. A Claude actor need not write the result file itself. Return the complete result projection in the final answer in either case.
- Return content: exact subject and basis, the status output before and after any send, whether a send was performed, the delivery count, the admission receipt, evidence routes, residuals, validity conditions and any effect uncertainty.

## Stop And Change
- Invalidation: contract, admission, source or selected method identity changes, or a new material service observation.
- Stop conditions, verbatim: missing or mismatched admission, missing exact basis, scope or capability insufficient, effect cannot be reconciled.
- Non-closure conditions, verbatim: unknown effect, zero or multiple deliveries, unpermitted read or effect.
- Re-entry: a known mismatch between this intake and the receiver's own control reads returns activation_refusal with cause. Multiple deliveries or an unreconcilable effect return to fixture-owner. No ticket route is selected for this fixture.
- Limits: wall 240 seconds, context at host maximum with actual bytes unmeasured, spend under existing authorization with observed spend reported.
- Next decision boundary: fixture-owner disposition of the returned result. No independent review is required for this observed fixture result per the contract.

## Issuer Residuals And Non-Changes
- Not dispatched by the issuer. The roster for this session is Read, Skill and Bash with no subagent mechanism. Dispatch is the harness transport's declared role.
- The native Skill invocation of stdo-work was refused by the policy gate. The issuer applied the skill from its SKILL.md and the COORDINATED_HANDOFF and PRODUCT_BASIS references read directly from the selected plugin.
- The read of ACTIVATION §3 "Effects" from the verified basis was refused by the policy gate. The effect reconciliation rule above rests on contracts/worker.json, requirements.md and the handoff reference's Evaluate The Return section, not on that owner section. The receiver may acquire it through its own routes if its binding permits.
- One directory listing attempt was refused by the gate before any output. Nothing was acquired from it.
- Acquisition note for the receiver: the output of a permitted send is acquired as part of that effect. Retain it as effect evidence. It is not a separate read grant.
- The issuer made no subject observation, no file write, no effect, no Git or network action. Observed spend and wall time were not reported by the host.
- Acquired verified members: REFERENCE_FRAME.md member sha256 4bf3bb18f8590b8096f5ff2de6554787d29a164224be697c76640289d2096d64, section "Minimal activation binding". EXECUTIVE_BASELINE.md member sha256 064eb55ec6b1870da8411da814c0a6c59fd7113bd4cb2631351c141f66a02f2a, sections "Activation additions" and "2. Executive activates Worker". ACTIVATION.md heading catalog only, member sha256 56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d.

---

**Present work standing.** The JOB-17 dispatch effect is unknown. The only admitted carrier evidence is prior-attempt.json, which records a send whose connection ended before receipt. The worker must resolve that through the status route before any further send. The issuer's own result is closed as "prepared, not dispatched" with the residuals listed above.
