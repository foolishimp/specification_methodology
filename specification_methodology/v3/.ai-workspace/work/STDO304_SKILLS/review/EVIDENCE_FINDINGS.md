# Findings on qualification evidence, first observations

These findings concern the observed test relation, not new defects proved in the frozen plugin source. Priority, promotion-boundary effect and disposition remain the Executive's.

## EF-01 — S2: the harness records a return outside its contracted result surface

Exact subject: `evidence/test-protocol-01/run_probe.py` as hashed in that directory's INPUTS.json, the initial fixture contracts produced by its matching prepare_fixtures.py, and `evidence/observed-runs/direct/`.

Location: `testing/run_probe.py:130` (the pinned copy has the same line), plus `prepare_fixtures.py:51-53,165,185-186`. The relay maps direct output to `records/direct-relay.md` and receiver output to `records/worker-relay.md`. The contracts name `records/direct-result.md` and `records/worker-result.md`. OWNER says the harness writes host final output to its contract's named surface before considering the invocation returned.

Causal example: the first Codex direct task returns a basis-unavailable refusal without writing files. The harness writes only `records/direct-relay.md` (`observed-runs/direct/CHANGES.json`); the contracted result surface is absent. A consumer following the exact contract therefore cannot recover its required durable result even though the final-return artifact exists elsewhere. The receiver mapping has the same latent mismatch; no receiver run is claimed by this observation.

Source contract: frozen expectation E02/E08/E13; candidate COORDINATED_HANDOFF Receive:100-107 requires the named result relation, and released REFERENCE_FRAME RF-012/013 plus ACTIVATION §7 require a result sufficient for its declared consumer. The source candidate correctly requires that boundary; this harness does not currently exercise it.

Confidence: high from code, contract and actual artifact delta. Impact: invalidates any assertion that this initial direct run exercised the contracted durable return and makes the planned receiver relay unsuitable for that claim. Blast radius: this test harness and these original observations, not the native plugin source or production work. Containment: retain original raw returns as bounded host observations without claiming named-surface completion. Complexity/risk: local test binding correction; new observations must retain their own identities and cannot repair the original run retroactively.

## EO-01 — observed issuer noncompliance and timeout, source cause unestablished

The first Claude issuer succeeds in invoking the packaged skills, but successfully lists the excluded parent and reads an unlisted PROMPT-RECEIVER.txt. The issuer's own FRAME/contract permits only listed inputs and excludes parent directories; this is not a recipient restriction projected onto the issuer. See `SEMANTIC_REVIEW.md` for exact trace coordinates and the pinned `evidence/issuer-interim/` inputs. The run then times out at 180.605 seconds with no final intake and no file changes. It does not establish a complete issuer/recipient path or adequate attention in the trial envelope.

The candidate does not prescribe these forbidden reads. The raw actor trace establishes actual acquisition and noncompliance, while a specific defective instruction, host influence and behavior frequency are unestablished. Hidden host/global instructions are unmeasured. Do not call this a source-text defect solely because a trial failed; do not call it a successful native-use trial because discovery and admission checks ran.

## EO-02 — direct task observes a different manager/store route than the harness intended

The isolated store verification passed before the run. The first Codex direct task's actual manager command reported v3.0.3 absent, and the actor withheld effects instead of installing or using mutable source. This supports a bounded negative-path observation only. The intended positive direct-work predicate and intended exact isolated-store path remain unexercised by this run. The prior Codex CLI option failure is a separate launch failure, not a skill result.
