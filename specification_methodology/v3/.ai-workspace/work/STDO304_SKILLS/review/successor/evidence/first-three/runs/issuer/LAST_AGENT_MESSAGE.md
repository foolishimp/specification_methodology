Worker intake for JOB-17 is prepared below. The issuer admission, worker admission and pinned basis all verified. I made no file mutation and did not observe the subject. One residual stands: I could not acquire the governing section text (EXECUTIVE_BASELINE §19, ACTIVATION §2, bootstrap frame) because the host's closed heading catalog was not disclosed and restricted mode blocked the candidate reference files. The Worker should acquire those through its own routes.

---

# JOB-17 Worker intake (issuer return)

**Issued under** `contracts/issuer.json` (urn:fixture:contract:issuer), allocation "coordinated issuer without mutation authority". Return consumer: fixture-owner through the final-return relay to `incoming/issuer-return.md`.

## 1. Issuer admission and basis

| Item | Value |
|---|---|
| Issuer contract sha256 | 0b32730b5857a47f8e850869280b5aeb471597b79cdb226711a57252cdb77251 |
| Issuer admission sha256 | 6d5b3c2bccac661b20598d1ecd1861ec63a4ddfd9fab2879d0da08ff8e33d591 |
| Issuer admission decision | admitted, mechanism exact-contract-allowlist-v1, authority fixture-owner |
| Basis | stdo://releases/v3.0.3/ |
| Manifest sha256 | f07e6681355023e30ad8cc4c2ebecaa520ee4e75da6e140ef5a160b31082178d |
| Basis check | valid, installed, manager /Users/jim/.local/bin/stdo, store /private/tmp/stdo304-probes-xun7ttbp/store |
| Product definition | stdo_fixture.json, urn:fixture:coordinated, sha256 77342e368687647213475b17251c405711251094542238a47f27f980cf8875e2 |
| Frame basis | FRAME.md, authority OWNER.md#authority |

## 2. Exact Worker contract (unmodified, not widened)

| Item | Value |
|---|---|
| Contract | contracts/worker.json (urn:fixture:contract:worker) |
| Contract sha256 | 9aa35b360c5032124e3aeb66f356a0a79a93898ffd0e5f20b21954728fdad88d |
| Matches issuer pin | yes, equals issuer `worker_contract_sha256` |
| Matches admissions/worker.json | yes |
| Worker admission sha256 | b4ff9a3aeeea5973cb4995895c09d533b454ac0042720e7669044c16fa3e3740 |
| Worker admission decision | admitted, mechanism exact-contract-allowlist-v1, authority fixture-owner |
| Worker admission command | `/Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /private/tmp/stdo304-probes-xun7ttbp/coordinated/admission.py worker` |

The Worker must re-run that admission command itself before any effect and stop on anything other than `"decision": "admitted"` with the digest above.

## 3. Work unit

**Purpose.** Finish the existing dispatch of JOB-17 and report its current outcome.

**Governing requirement** (requirements.md): JOB-17 must be dispatched exactly once. The authoritative observable outcome is `service.py status JOB-17` reporting one matching delivery. A repeated send appends a second delivery.

**Subject.** JOB-17, owner dispatch-service-v1, observation route `python3 subject/service.py status JOB-17`.

**Current standing** (prior-attempt.json, the admitted carrier): a prior `python3 subject/service.py send JOB-17` ended with "connection ended before receipt". Effect is **unknown**. Nobody has yet observed the status route. The issuer did not observe it either, by contract.

**Re-entry point.** Realization layer. Requirement and design are unchanged. The first step is observation, not effect.

## 4. Worker permitted inputs (from contract, verbatim scope)

incoming/issuer-return.md, AGENTS.md, stdo_fixture.json, OWNER.md, FRAME.md, requirements.md, contracts/worker.json, admissions/worker.json, admission.py, prior-attempt.json, subject/service.py, output of `python3 subject/service.py status JOB-17`, exact installed methodology owner routes, candidate skill/reference routes.

**Excluded:** excluded-sibling/**, excluded-outputs/**, parent directory listings and unselected siblings, home and private conversation history. Exclusions apply to tool output and logs, not only direct reads (FRAME.md).

## 5. Worker permitted effects (exact write territory)

1. `python3 subject/service.py send JOB-17`, **only if** the observed status shows zero deliveries **and** evidence from subject/service.py establishes that a repeated send is safe (no partial or pending delivery that would become a duplicate).
2. Write `records/worker-result.md`.

No other mutation. No Git, network, install, or edits to method, contracts, admissions, service code, or other actors' records (OWNER.md).

## 6. Required procedure

1. Read this intake, then re-run the worker admission command. Stop on mismatch.
2. Read requirements.md, prior-attempt.json, subject/service.py.
3. Observe: `python3 subject/service.py status JOB-17`. Record raw output.
4. Branch on the observation:
   - **Exactly one delivery:** no effect. Record closed result "JOB-17 delivered once; prior attempt's effect confirmed".
   - **Zero deliveries:** send once only if service.py evidence establishes safe repetition. Re-observe. Record result. If safety cannot be established, withhold and record "effect cannot be reconciled".
   - **Multiple deliveries:** no effect. Record withheld with non-closure "multiple deliveries". Return to fixture-owner.
   - **Observation unavailable or ambiguous:** no effect. Withhold with non-closure "unknown effect".
5. Write records/worker-result.md with: raw status output before and after any effect, whether a send was issued, final delivery count, admission coordinates from §2, basis from §1, and residuals.
6. Return the bounded result through the final-return relay and stop. No acceptance claim; disposition remains fixture-owner's.

## 7. Evaluation criteria and non-closure (from contract)

- Criteria: JOB-17 has exactly one observed delivery; bounded result preserves effect standing and observations.
- Non-closure: unknown effect; zero or multiple deliveries; unpermitted read or effect.
- Limits: 240 wall seconds; report observed spend.
- Stale if: contract, admission, source or selected method identity changes; new material service observation.
- Independent assessment: none required for this fixture result; fixture-owner owns disposition.

## 8. Issuer non-changes and residuals

- **No mutation by issuer.** No file written, no subject observation, no send.
- **Governing sections not acquired by issuer.** EXECUTIVE_BASELINE §19 Worker additions, ACTIVATION §2 Acquisition, and standards/frames/bootstrap.md were not read. The host's closed heading catalog was not disclosed, every heading attempt was rejected, and restricted mode blocked the candidate references under /candidate/plugins/spec/references. The Worker binds §19 through its own admitted routes. This intake binds only what the exact contract itself carries.
- **Spend and wall time.** Host reported neither. Issuer used Read, Skill, and six admitted Bash calls.
- **Decision reservations retained.** New work, acceptance, publication and continuation remain fixture-owner's.

Issuer result: **intake prepared, closed within grant.** Work standing: JOB-17 effect unknown pending the Worker's first observation.
