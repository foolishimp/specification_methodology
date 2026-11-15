# Pure/local Python refactoring context

Use this recipe only for the declared Python purpose. For SDLC work, QA, triage
and boundary decisions, use [SDLC workflow](sdlc-workflow.md).

## Bind and consume the matching Python index

1. Run `python3 -B <cli> indexes --public-manifest-sha256 <public-sha>`. It verifies the manifest and actual public members and shows each index's exact method, ordered source members, purpose and family guard. Match those to the actual work. The `python-pure-refactor/2` successor supplies preconstruction method constraints for pure/local Python 3.12 realization refactoring under adopted DESIGN_MODULE, including conditional ODD/UX law, over sixteen exact selected owners. The selected release-target entry binds STDO 3.1.0-rc.2; its 3.0.5 and 3.0.4 predecessors and four-owner P1 entry remain exact for older consumers. The family retains its permitted branches. Match the actual caller basis rather than automatically selecting the newest entry. No entry covers all builds, SDLC purposes, Product-specific law or STDO 3.* releases.

2. Bind the caller's actual installation. The following example is for a caller that explicitly selected 3.1.0-rc.2. A 3.0.4 caller uses the retained 3.0.4 entry and exact manifest shown by `indexes`; do not change its basis to fit this example:

   ```sh
   python3 -B <cli> bind --index-id stdo-3.1.0-rc.2-python-pure-refactor-v2 --source-root <selected-installed-method-root> --method-uri stdo://releases/v3.1.0-rc.2/ --method-manifest-sha256 b691b0249c82ff39033ae636c4eaa0ab44bafee3732c79a227eb9409d53776c4 --public-manifest-sha256 <public-sha> --out context-work
   ```

   `source-root` contains `manifest.json` and `standards/`; it is not the standards directory. Bind hashes the actual manifest, checks selected-member declarations and hashes all sixteen actual source files in catalog order. It does not substitute a historical corpus or a different release. Whole-install qualification remains the existing method manager's responsibility.

3. Write `QUERY.json` as `{id, purpose_id, facts}` using the declared meanings in `context-work/PURPOSE.json`. Obtain each family fact from the actual task/adoption/design/activation state. Do not copy the catalog's expected values as unverified defaults. Missing, null or wrong-type deciding facts remain unknown. `target_product`, `task` and `grant` can distinguish consumers without changing corpus identity.

   ```sh
   python3 -B <cli> select --bundle context-work --query QUERY.json --index-id stdo-3.1.0-rc.2-python-pure-refactor-v2 --public-manifest-sha256 <public-sha>
   python3 -B <cli> consume --bundle context-work --query QUERY.json --index-id stdo-3.1.0-rc.2-python-pure-refactor-v2 --public-manifest-sha256 <public-sha> --assessment <independently-selected-exact-query-assessment.json> --byte-budget 262144 --out delivery
   ```

   The assessed path uses an independently selected supported assessment for this exact canonical index, corpus and query (including query ID). Obtain that judgment through the applicable governing assessment contract; do not author it merely to make coverage true. A fixture assessment applies only to its exact subject and cannot qualify a changed query. Selection refuses identity drift and false family applicability. Unknown family applicability returns `incomplete` (exit 3), no selected index or delivery. Successful selection exposes all matches and the exact `index_path`. Consumption rechecks them and reuses the same authored index through the shared compiler. Repeat with a new actual query for another eligible task/project; no reauthoring is needed.

4. Check the actual files against the independently supplied expected inputs, using the same assessment supplied to consumption:

   ```sh
   python3 -B <cli> check --bundle context-work --index <selected-index-path> --query QUERY.json --assessment <independently-selected-exact-query-assessment.json> --byte-budget 262144 --context delivery/CONTEXT.json --markdown delivery/CONTEXT.md
   ```

   These examples retain the comparison's 262144-byte complete-result bound. The prior 3.0.4 successor's unassessed controlled fixture body measured 209425 bytes; its ODD-and-UX branch control measured 250844 bytes. Assessment metadata and caller coordinates can change the actual size, so measure the actual complete result. Select the recipient's actual bound explicitly. Overflow refuses the whole body without truncation; do not strip required meaning to make it fit. Separately establish full task/context receipt before relying on native consumption.

If no applicable assessment exists, existing authorized experimental use can retain the explicit trial path without requesting a new permission merely for lack of coverage:

```sh
python3 -B <cli> consume --bundle context-work --query QUERY.json --index-id stdo-3.1.0-rc.2-python-pure-refactor-v2 --public-manifest-sha256 <public-sha> --trial-binding <existing-authorized-scope> --byte-budget 262144 --out trial-delivery
python3 -B <cli> check --bundle context-work --index <selected-index-path> --query QUERY.json --trial-binding <existing-authorized-scope> --byte-budget 262144 --context trial-delivery/CONTEXT.json --markdown trial-delivery/CONTEXT.md
```

That path reports `covered: false` and experimental use; it does not bypass a task's actual required assessment or acceptance. With neither assessment nor an authorized trial binding, use remains withheld. An unknown requested premise still prevents coverage even when an assessment is supplied.

## Apply the coverage predicate

For purpose `python-pure-refactor/2`, coverage concerns the applicable governing method constraints before construction. It does not say the task is admitted, its concrete Product/design inputs are complete, or its future candidate has passed typing, no-delta proof, review or acceptance. Follow the selected rules to acquire those task inputs and establish those separate predicates before their dependent actions. A complete conditional obligation can be retained without asserting its future result.

Use `public_semantics_change_authorized`, `authority_change_authorized` and `effects_change_authorized` for what the request allows; false forbids change and does not claim a future candidate already preserved it. Resolve `profile_odd`, `profile_ux` and `realizes_ux_surface` from actual adopted scope/surface evidence. Pure/local Python does not make those branches false. A realized UX surface includes the default-trigger/exemption rules, without the selector inventing adoption or an exemption.

The three `*_requested` permission facts distinguish an ordinary-constraint request from a request to rely on a mutable semantic-carrier exception, a failure-carrier practicality departure or a typing escape. False grants no specific exception or conformance finding. A local name, temporary lifetime or scratch label supplies no exemption: classify the value's actual carrier/source-truth and authority role from accepted design and use. The source does not require eliminating all imperative operations, so assignment alone is not that classification either. If an exception is requested, supply all its exact source-required evidence premises; missing premises remain unknown. Reconstruct the context before later relying on a newly requested permission. Never use these facts to conceal a departure already planned or necessary for the task.

The [historical 3.0.4 successor gap dispositions](../indexes/stdo-3.0.4-python-pure-refactor-v2/GAP-DISPOSITIONS.json) account individually for the predecessor's 45 rule unknowns and six global entries. Those are authored source interpretations, not independent judgments. A separately selected assessment still binds the exact canonical index, corpus and query, including query ID. Reuse its exact query only when it actually describes the same subject; a changed query needs its own applicable assessment. Other Product-specific or separately adopted governing law remains an explicit task input and cannot be invented by this index.

The [prior 3.0.4 coverage record](../indexes/stdo-3.0.4-python-pure-refactor-v2/COVERAGE-STANDING.json)
links the externally supported exact-query judgment and preserved failed
predecessor. Its evidence references are retained source-work records, not
portable runtime dependencies. The catalog's unchanged authoring provenance
records its historical pending state; use the external judgment for current
standing and supply its exact assessment separately when applicable.


For release-target authoring and final-cut packaging, follow the
[method-target policy](method-targets.md). It separates the latest
selected semantic source from this Product's construction basis and from an
older consumer's actual basis. The historical 3.0.5 entry's [provenance](../indexes/stdo-3.0.5-rc.1-python-pure-refactor-v2/PROVENANCE.json)
and source delta preserve the 3.0.4 evidence without inheriting its assessment.
Any supported new-subject assessment remains separately supplied; the mere
presence of the new entry does not establish coverage.

The [historical 3.0.5 coverage record](../indexes/stdo-3.0.5-rc.1-python-pure-refactor-v2/COVERAGE-STANDING.json) binds the admitted external
assessment for the exact 3.0.5-rc.1 index/corpus/new Q0 and retains its
prior-evidence reuse limits and residuals. Author-stage candidate or pending
wording above and in frozen provenance is historical; this separate record
supplies current standing. New queries inherit no verdict, and task success
and final release qualification remain separate.

The 3.1 entry's source delta records exact source changes, conserved grounds and
the carrier/context clarification. Its public provenance stays unassessed; any
current external exact-query judgment is selected separately. Obtain the native
manifest pin from the selected catalog entry and verify the same cut through its
manager. A 3.0.5 query assessment is refused for this new index and corpus.
