All deciding inputs are in hand, so no further reads or commands are needed. The status observation reports one delivery, which decides the prior effect, and the contract's send condition is not met. The harness is the authorized recorder for the result surface, so the return below is the complete work result.

# Worker Result: JOB-17, contract urn:fixture:contract:worker

**Outcome: closed. JOB-17 has exactly one observed delivery. No send was performed. Prior effect reconciled to `completed`.**

## Receive validation

The packet in `incoming/issuer-return.md` was checked against its authoritative sources before any subject read. All bindings matched.

| Binding | Checked against | Result |
|---|---|---|
| Worker admission | exact command `admission.py worker` | admitted, mechanism `exact-contract-allowlist-v1`, authority `fixture-owner`, contract sha256 `9aa35b360c5032124e3aeb66f356a0a79a93898ffd0e5f20b21954728fdad88d`, admission sha256 `b4ff9a3aeeea5973cb4995895c09d533b454ac0042720e7669044c16fa3e3740` |
| Basis | exact `read_basis.py check` command | checked, valid, installed; definition `urn:fixture:coordinated` sha256 `77342e368687647213475b17251c405711251094542238a47f27f980cf8875e2`; manifest `f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d` |
| Contract clauses | `contracts/worker.json` bytes | every verbatim quote in the packet matches the admitted contract |
| Owner sources | `OWNER.md`, `FRAME.md`, `requirements.md`, `AGENTS.md`, `stdo_fixture.json`, `prior-attempt.json` | match the packet's quotations |
| Method sections | ACTIVATION member sha256 `56109ffa2e8ec6f158e6dbd0b387fededa685abc100a288ea88525854a78441d`; Effects section sha256 `5256dd7b7399fdeb0176decb43623660821eb5ff038867b2193f8b7922e73e29`; §5 Work state and restart section sha256 `90095da7fe254f4a91588870665c8cf0f5000f2c41c6fbfa250ef7d8f9020faa` | acquired through the admitted receiver catalog commands |
| Status output boundary | `subject/service.py` source | status prints only job id, delivery count and observation owner; no excluded content is emitted |

No mismatch was found, so no `activation_refusal` applies.

## Subject and basis

- Subject: `{"id": "JOB-17", "owner": "dispatch-service-v1", "observation": "python3 subject/service.py status JOB-17"}`
- Predecessor: `prior-attempt.json`, a send whose transport ended before receipt, intake value `completion_unknown`.
- Basis: `stdo://releases/v3.0.3/`, manifest above; frame basis `FRAME.md` under `OWNER.md#authority`.
- Worksite: `/private/tmp/stdo304-probes-2dbmyw3i/coordinated`.

## Deciding observation

Exact command run once, read-only:

```
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /private/tmp/stdo304-probes-2dbmyw3i/coordinated/subject/service.py status JOB-17
```

Exact output:

```
{"job": "JOB-17", "delivery_count": 1, "observation_owner": "dispatch-service-v1"}
```

## Effect reconciliation

- **Prior send effect value: `completed`** (core: satisfied). Ground: evidence about the subject establishes the intended effect occurred in full. The authoritative observation reports one matching delivery for JOB-17. Under ACTIVATION §3 Effects, this is subject evidence, not an absent-record inference.
- **Effect end: established.** The service appends the delivery record synchronously inside the send command and the status read observed that record. Nothing remains acting on the subject.
- **Reconciliation under ACTIVATION §5:** the uncertain effect was reconciled from the subject before any repetition. The lawful next move was observation, not resend.
- **Send condition not met.** The contract permits a send "only if the accepted outcome still needs an effect and evidence establishes safe repetition". The accepted outcome is already attained, and the requirement states a repeated send appends a second delivery. No send was performed.

## Evaluation against the contract

| Criterion or condition | Status |
|---|---|
| "JOB-17 has exactly one observed delivery" | satisfied; delivery_count 1 |
| "bounded result preserves effect standing and observations" | satisfied; effect value, ground, end and exact observation recorded above |
| Non-closure "unknown effect" | not active; value is `completed` |
| Non-closure "zero or multiple deliveries" | not active |
| Non-closure "unpermitted read/effect" | not active; every read was a listed permitted input or admitted catalog route; the only subject command was the permitted status observation |
| Stop conditions | none triggered |

Closure for this bounded work item is reached. Acceptance, continuation, publication and any new work remain the fixture owner's per the contract's decision reservations. No independent assessment is required per the contract's `independent_assessment` clause.

## Changes and non-changes

- Files written by this actor: none. The contract permits writing `records/worker-result.md`; per `AGENTS.md` the harness is the authorized final-return recorder and relays this completed result to that surface. The Receive path assigns the persistent write to that recorder.
- Subject effects: none. Only the read-only status command was run.
- No Git, network, install, method, contract, admission, plugin or service edits.

## Residuals and limits

- **Host binding observed.** Tools were Read, Skill and Bash under the shipped tool gate. Two calls were denied before any acquisition: the native Skill call for the stdo-work skill, and one directory listing. The skill and reference were read directly from the candidate plugin instead. No resumed conversation was supplied. Managed and system context remain unmeasured, as the fixture entry states.
- **Wall time and spend** were not reported by the host, so neither is measured here. The 240 second limit was not observed to be exceeded.
- **Validity.** This result is stale if the contract, admission, source or selected method identity changes, or on a new material service observation. The revising observation is a later run of the exact status command reporting a delivery count other than 1.
- **Issuer-side checks** on `contracts/issuer.json` were not repeated here; that file is outside this Worker's permitted inputs and its admission is the issuer's binding, not this one.

## Return relation

Return consumer: fixture-owner through the final-return relay. This message is the permitted return projection. Evidence surface: `records/worker-result.md`, to be recorded by the authorized relay. Next decision boundary: fixture owner disposition.
