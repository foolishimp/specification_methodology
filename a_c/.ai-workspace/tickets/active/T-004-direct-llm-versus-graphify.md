# T-004 Direct LLM versus Graphify-assisted a_c

Status: completed bounded dogfood evaluation; broader F-USEFULNESS and owner
disposition remain open. Re-entry: goal_reprice, F-USEFULNESS.

## Owner instruction and basis

Jim requests a quality/benefit comparison of a_c using the LLM directly and
augmented with Graphify, creating baseline representations of both candidates.
This authorizes preparation, bounded fresh LLM trials and reporting through
existing local CLI authentication. It introduces no new paid service or global
installation. The preceding owner instruction keeps this work as dogfood;
RC formalisation waits for a later instruction.

Use the verified a_c Product Definition's installed STDO 2.5.1-rc.2 basis.
Reuse T-003 frozen Codex package d1b33480b46f45bb46198a2f63ca197e84e40e55
and Claude package af3b8b7107c92a216cc53d629ddeefecd7f77fca. Both V3
worktrees and previous Graphify artifacts are read-only inputs.

## Outcome

Create self-contained native baselines of the original LLM-authored a_c
content, sources, signature and coverage. Matched assisted access has that same
content plus actual pinned Graphify discovery and acquisition. Content parity
alone cannot establish improved semantic quality. Fresh tasks include bounded
representation authoring and application; entire-method re-authoring is outside
this pilot. Compare conditions within each candidate, preserving unequal scope.

Initial design: two fresh runs per condition/candidate (eight actor runs), four
source-grounded tasks per run, common output schema and resource envelope.
Freeze questions and source expectations before answers; hide condition labels
when grading. Record failures rather than replacing poor runs. Measure calls,
emitted bytes, tokens/cache, elapsed time, graph creation and startup separately.
Do not invent dollar costs without backend accounting or a pinned applicable
pricing basis. Benchmark-passing answers are not owner-accepted results.

## Activations and territories

- Executive /root coordinates exact inputs, protocol and bounded results;
  it performs no mutation in that role.
- Writer /root creates this ticket and owns
  a_c/dogfood/stdo-v3-i5-evaluation/ except delegated paths below: baseline
  artifacts, protocol, isolated run invocation records, assessment packets,
  report, and completion links in a_c README/Goals. Temporary isolated run
  directories and CLI-authenticated evaluation sessions are permitted. No Git
  mutation, original-candidate or original-Graphify effects are granted.
- Worker /root/ac_eval_harness owns tools/, tests/ and the output schema under
  that evaluation root. Implement bounded common source access, actual pinned
  Graphify assistance and exact emission/usage logging. No oracle/grade access
  or actor runs before protocol freeze.
- Worker /root/ac_eval_oracle owns only private/tasks.json,
  private/oracle.json and private/ORACLE.md under the evaluation root. Read
  exact documentary sources before answers; no Graphify-derived oracle.
- A nonauthor design reviewer and blind assessor receive separately bounded
  activations. They author no evaluated answers and grant no acceptance.
- Nonauthor reviewer `/root/ac_eval_design_review` completed read-only
  prelaunch source/protocol assessment; its supported repairs are recorded in
  the study evidence. It saw no actor answers.
- Workers `/root/ac_eval_codex_grade` and `/root/ac_eval_claude_grade` are
  activated only after all actor runs terminate, in fresh contexts with no
  inherited schedule/history. Each may read only its `grading/<candidate>/`
  packet and `baselines/<candidate>/sources/`, and may write only its own
  `grading/<candidate>/grades.json`. Grade exact source meaning under the
  frozen rubric; no actor answer, protocol, source, run or mapping effects.

## Exploratory actual-use extension

The primary access-policy pilot showed little graph uptake; its only observed
actual graph user in round one timed out after retrieval. This leaves actual
Graphify-assisted answer quality unresolved. The nonauthor design reviewer
supports four additional bounded fresh runs, one per condition/candidate, on
the unchanged C3/L3 question and oracle. Root Writer owns `followup/` and its
separate protocol/freeze/prompts/runs and compliance evidence; it reuses the
unchanged frozen harness. Same model, source and 24-call/160,000-byte/720-second
envelope. Assisted requires successful relevant query/selector-manifest/source
reading; no privileged source or selector hints. No original run is replaced.
The fresh blind assessors may additionally read their candidate's followup
packet and write its `grades.json` under `followup/grading/<candidate>/` only.
Report the two series separately, with explicit exploratory/repeated-question
standing. This extension changes no source, implementation, Product or RC grant.

## Completed return

[Report](../../../dogfood/stdo-v3-i5-evaluation/README.md),
[paired baselines](../../../dogfood/stdo-v3-i5-evaluation/paired-baselines.json),
[primary results](../../../dogfood/stdo-v3-i5-evaluation/results.json) and
[actual-use results](../../../dogfood/stdo-v3-i5-evaluation/followup/results.json)
are ready for review. Twelve actor runs attempted 36 repeated task answers;
eleven returned 32 answers. The one primary timeout is preserved, with unknown
backend usage and no replacement. All output citations reproduce and were
observed; 288 criterion and 108 prohibition judgments were condition blind.
Both actual-use candidate pairs meet the frozen source criteria. Graphify
used more input tokens, with mixed output-token and elapsed-time effects;
no quality gain or consistent efficiency gain was demonstrated.

The 17 harness tests and actual pinned-upstream checks pass. Baseline custody
and lossless native recovery reproduce. Pre-answer protocols/oracle and blind
grades remain frozen; uniform citation-parser corrections are documented.
No actor answer, original candidate or prior Graphify implementation was
changed by this evaluation. No Git mutations were performed. All evaluation
actors/readers have terminated. Semantic
acceptance, full-calculus conformance, corrected/accepted-result total cost,
installed qualification, integration and RC/release remain separately owned.

Return the baseline representations, reproducible matched runs, source-grounded
quality judgments, acquisition/usage/time measurements and a bounded benefit
assessment. Preserve infrastructure failures and unresolved questions. No
calculus amendment, V3 acceptance, RC or release follows from this experiment.
