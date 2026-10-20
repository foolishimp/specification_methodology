# Proposed Claude-direct RC9 semantic correction

This application contains one F_P-authored correction to the reviewed
Claude-direct RC9 representation. It is a separate **unaccepted proposal**.
The four frozen RC9 representations and their construction evidence are
unchanged.

The parent constraint says an unresolved applicability premise requiring an
undeclared relation returns `out_of_frame` **rather than** `indeterminate`.
The exact source permits either value when both grounds coexist. The proposed
replacement preserves that permission and requires the returned value to name
its ground. The source and the unchanged target statement continue to prohibit
false applicability and exclusion from unresolved premises.

The sole semantic change is
`predicate.exceptions[0]` in constraint
`urn:a-c:generation:63c64519947babe1e3fec509:record:613311974eb7d572ca277ccf96b8f339`:

> A missing or ambiguous premise requiring an undeclared frame relation can
> have both lawful out_of_frame and indeterminate grounds when the admissible
> evidence cannot decide the claim. The result names the value it returns and
> that ground; neither value is excluded.

The new model identifies this correction with its own model identity,
interpretation contract, Worker interpreter and correction provenance. Original
CLI invocation coordinates remain historical parent evidence; no original CLI
run is claimed to have authored the replacement. The deterministic packager
applies supplied F_P text and checks custody and the exact allowed delta. It
does not infer the replacement or perform the tenant's unsupported generic
`transform` operation.

All other 1,979 records, their order, the signature, subject basis and inventory,
source selection dispositions, target grounding, residuals, dependency contract
and empty execution populations remain unchanged. The target's existing exact
ACTIVATION grounding already permits `indeterminate` or `out_of_frame`;
FOUNDATIONS supplies the explicit coexistence clarification in the correction
evidence. No source anchor or selection decision is changed.

Read these artifacts:

- [Explicit semantic patch](semantic-patch.json): exact parent, field and
  before/after text.
- [Deciding source manifest](source-manifest.json): frozen source revision,
  custody checkpoint, full corpus manifest and exact line witnesses.
- [Authoring record](authoring-record.json): F_P judgment, source-first oracle,
  Worker activation, provenance and limits.
- [Interpretation contract](interpretation-contract.json) and
  [interpreter](interpreter.json): current proposal scope and retained authority.
- [Proposed model](proposal/model.json),
  [proposal carrier](proposal/carrier.json),
  [exact delta](proposal/delta.json),
  [coverage and limits](proposal/coverage.json), and
  [mechanical result](proposal/result.json).
- [Provenance resolution](provenance-resolution.json): local paths for new
  coordinates, with canonical JSON and raw file digests distinguished.
- [Worker qualification evidence](../../.ai-workspace/qualification/t008/review-fixes-001/semantic/):
  activation, source-first expectations, frozen-file guard, public codec return
  and exact recovery, application controls and closure.

From `a_c/`, recompute the proposal without changing files:

```sh
.venv/bin/python -B dogfood/stdo-v3-generation-rc9-review-correction/build_correction.py --check
.venv/bin/python -B build_tenants/graphify/code/ac_graph.py validate dogfood/stdo-v3-generation-rc9-review-correction/proposal/model.json
```

The packager's default construction command writes only its new `proposal/`
directory and refuses an existing destination. `--check` recomputes the explicit
patch, all 49 frozen source checks, allowed delta, structural validation and
carrier recovery against the retained artifacts. A changed parent, codec,
source, oracle or contract refuses; it does not repin historical evidence.

The original processing coverage and author-declared limitations remain parent
evidence. This application does not regenerate the corpus, qualify global
semantic closure, establish complete calculus conformance, or measure
accepted-result benefit. It makes no fresh upstream Graphify build/export,
Product acceptance, installation, RC or release claim. Independent semantic
assessment and owner disposition are separate work.
