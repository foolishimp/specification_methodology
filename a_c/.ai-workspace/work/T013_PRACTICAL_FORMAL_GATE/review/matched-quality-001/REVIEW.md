# T013 independent neutral A/B task-quality review

Changes are needed in both outputs. A has an S2 numeric-preservation defect; B has an S3 numeric-parser boundary defect. B better preserves finite numeric values on the additional cases inspected. Both pass the complete predeclared hidden set and supplied examples, so those results alone would not have distinguished their quality. This is a quality-only assessment before disclosure of the arm mapping or operational costs.

Selected handoff SHA-256: `8aa45c66afae9b0725b3b3d2a099b5812c918ef2a0fe7892e7312eb58fdd4c40`.
Selected input pins: `335e9b465d1fbe5a0acf632b09256e03def0055f49c335972646b1426d61cfff`.
The 17 files in each frozen tree match, and all 12 common input files are byte-identical. TASK remains `33e08813021b43a259dc72aa35f904f82b370de25faff64488f29ee4d4495829`; the original PROTOCOL remains `547a73826a8bd28721661361106d5a8e53844ca3a3a8b2a10dd5b66d7a2ae4f6`. The eight-family evaluator and all 17 inputs match the original preparation pins, rather than a newly authored replacement.

## Findings

**S2 — A changes finite input values and can report a negative elapsed observation as zero.** At `A/gate_report.py:27`, `finite_float` converts every decimal JSON token to a binary float. The later test at `A/gate_report.py:61` classifies that converted value. For the exact input in `case-inputs/I-number-negative-underflow.json`, `observations.elapsed_seconds` is `-1e-400`. TASK requires retaining that negative number in `reported` and returning `{"state":"invalid","value":null}` in the cost summary. The actual CLI exits 0, changes both original numeric values to `-0.0`, and returns `{"state":"reported","value":-0.0}`. This collapses a required negative/zero distinction and silently alters the subject being reported.

The same conversion rounds `0.123456789012345678901` to `0.12345678901234568`, turns positive `1e-400` into zero, and refuses the finite JSON number `1e400` as “non-finite.” These are one underlying defect, not separate findings. The task expressly requires every original field and value to survive and distinguishes a genuinely numeric zero from other observations. The raw digest remains correct, but does not repair the changed `reported` value. A's own test at `A/test_gate_report.py:77` classifies finite `1e999` as invalid, preserving the same mistaken numeric boundary. Actual stdout/stderr and commands are retained under `runs/A/I-number-*/`.

**S3 — B's Decimal parsing failure escapes the CLI error contract.** `B/gate_report.py:34` passes JSON decimal tokens directly to `Decimal`; `B/gate_report.py:88` does not catch `decimal.InvalidOperation`. The 83-byte `case-inputs/I-number-decimal-exponent-boundary.json` contains a valid, finite JSON number, `1e9999999999999999999`, in an unknown extension field. It requires no allocation of the represented magnitude. The actual CLI exits 1 with a 1,510-byte traceback, ending in `decimal.InvalidOperation`. The task declares no finite-number exponent limit, so faithful reporting is the specified outcome. Even if the implementation treated its numeric-capacity limit as invalid input, the required error surface would be exit 2, empty stdout and a concise error; exit 1 is neither supported outcome. The actual evidence is under `runs/B/I-number-decimal-exponent-boundary/`.

This is a remote numeric boundary, hence S3. B correctly preserves the ordinary precision case, `±1e-400`, and `1e400`, including the negative-cost classification that A gets wrong. Its own `1e9999` test also passes. Neither output was repaired or fed a review finding.

No S0, S1 or S4 finding was identified. These are disposable task-output findings, not defects in the Lean theorem library, formal gate or source representation.

## Behavior independently established

| Predeclared discriminator | A | B | Consequence checked |
|---|---|---|---|
| H1 minimal unsupported | Pass | Pass | No invented successful assessment or missing-field failure. |
| H2 budget and unchecked claim | Pass | Pass | Budget refusal stays distinct; requested-only claim is not counted as checked. |
| H3 new refusal reason | Pass | Pass | Exact matching; an added qualifier remains `other_refusal`. |
| H4 incomplete check | Pass | Pass | Partial successful stages do not promote the saved result. |
| H5 zero/null/boolean/negative cost | Pass | Pass | The declared cost distinctions hold for these predeclared values. |
| H6 supplied-view mismatch | Pass | Pass | Four checked and five requested claims survive, without condemning the parent model. |
| H7 raw custody and whitespace pair | Pass | Pass | Same parsed subject, different exact raw digest/length. |
| H8 malformed/duplicate/nonfinite/type rejection | Pass | Pass | Exit 2, empty stdout and an input error. |

Both also pass all seven supplied examples independently through their public CLIs. Additional checks cover minimal results for every status, all known optional field-type guards, null versus absence, ordered extension data and identities, unknown token/money cost, stage-only elapsed observations, exact refusal matching, malformed UTF-8, escaped duplicate keys, non-object roots, `Infinity`/`-Infinity`, and no/missing/extra CLI arguments. Known boolean fields are compared with type-sensitive equality; `false` cannot pass as numeric zero in the evaluator.

There were 75 CLI cases per output: 17 predeclared hidden, seven supplied examples and 51 additional cases including CLI argument controls. A passed 70 and failed five manifestations of its numeric boundary; B passed 74 and failed the one exponent-boundary case. Counts describe this selected test population, not acceptance or general reliability. The independent evaluator parses ordinary numeric values with Decimal and compares the complete expected report, including every `reported` field; it does not reuse either implementation or its tests as the oracle.

Both delivered self-test suites reproduce in disposable copies: A's six and B's seven tests pass. Their tests meaningfully cover the task's statuses, refusal distinctions, preservation, CLI behavior and typed failures, but miss the noted defects. The original empty `scratch/` directories were copied unchanged, so this reproduction did not silently add a missing task precondition.

The READMEs supply the command, exit distinction, useful supplied-view example, unknown-cost treatment and report-only boundary. Both implementations always emit the three false standing flags, retain source limitations in `reported`, and make no claim that their output authenticates the saved input or grants permission, semantic acceptance or owner closure. Source inspection shows they read only the named input file and do not follow embedded evidence paths or URIs. CLI execution left the disposable input/output trees unchanged; original frozen file hashes also remain exact. Candidate-manifest artifact hashes and stated self-test outcomes are consistent with the frozen files and reproduced tests, but remain construction evidence.

## Bounded comparison and blinding

For this specific task, B provides stronger numeric fidelity through its Decimal parsing and serialization, while A's binary-float conversion loses distinctions required by the contract. Their behavior is otherwise equivalent on the selected substantive reporting obligations. B still needs its exceptional numeric parsing path handled consistently; neither artifact is declared fully conforming or accepted here.

I did not read `operational/`, the arm mapping, actual Worker costs or raw transcripts. No explicit gated/ungated identity was visible in the delivered implementation, README, candidate manifest or test output inspected. Those files are unedited, and the common protocol describes the two arms, so complete blinding is not claimed. This comparison makes no claim about which arm produced either result, whether the formal gate caused a difference, or overall cost/benefit. Exposure, transport, actual delivered-context binding and operational claims remain for the separate post-quality assessment.

`evaluate.py`, `CASE-MANIFEST.json`, `RESULTS.json` and per-command raw outputs/receipts retain the independent execution. Python 3.12.8 was run in isolated mode using only the standard library, with disposable copies and temporary files confined to this review territory. The retained durations are Reviewer check costs, not Worker performance observations. There were no repairs, installs, network acquisitions, builds, compiler/proof runs, model/agent calls, origin reads, live-source mutations or Git effects. This review provides no Product acceptance or adoption authority.
