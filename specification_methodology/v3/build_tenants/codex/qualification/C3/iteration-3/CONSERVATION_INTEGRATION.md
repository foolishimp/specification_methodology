# Current conservation integration

Writer: `I3-R2-CONSERVATION-01`, admitted in common recording commit
`27634051885733c4a30d59f4280bada784c8bffd`, under `EC-CODEX-I3-02`.
Common input: `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd`.
Builder: installed `v2.5.1-rc.2`, manifest
`3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782`.
Document comparison subject: `f2cb3e593757d094d008102551925e871a0204ff`.
The complete package source and operative pins are pending finalization.

The current map retains the exact 691 unique stable IDs, their order and their
predecessor source facts. It proposes 639 conserved, 51 superseded and one not
applicable disposition. All are author proposals; none is accepted. The 47
preserved draft proposals are evaluated as 40 replacements and 7 conservations.
The actual revised compression/entry deltas add 11 replacement proposals and one
conserved index role. The other 632 rows retain inherited proposals with current
route and consumer accounting; this Writer did not perform a new 691-row semantic
audit. All rows retain an explicit independent semantic-assessment obligation.

## Facts, decisions and uncertainty

`DISPOSITION_REVISIONS.json` remains byte-identical. Its 47 proposals are evidence
inputs, not a patch whose dispositions overwrite the live map. The existing
historical map, reviews and trial artifacts are unchanged. Their observations,
qualified scopes and failure citations retain their original subjects.

The 33 old superseded rows no longer lack an account: 27 now have named proposed
replacement relations; six are proposed conservations with reasons. The six
known false conserved labels (Baseline Executive, worker return, disposition,
status/authority; Calculus provenance; Ticket execution contracts) are explicit
replacement proposals. The further frame-result, atomic-admission and general
realisation changes have their own relations. The World Model composition row
explicitly records a material modal change: the old prohibition on starting
with a central monolith becomes a mesh preference. The owner must decide that
meaning or select a source repair; this map does neither.

The current source has already restored the role/conversation non-invalidation
and affected-support invalidation rule in Foundations Workspace and context.
The current aggregate compression no longer mandates Code/Events for every
realisation, and the traversal compression no longer makes an absent/held
judgment fabricate refusal. These are current source observations, not proof of
complete conservation or a new acceptance of earlier fixes. The old finding and
trial subjects remain historical.

`history_correction` preserves the old synthesis statement and corrects its
claim that dispositions were unchanged. The exact transition from the historical
`a746559` map to `3ad1fca31dc93ba0847bbbbf308312a554daa1f6` changed 34 rows:
691 conserved became 657 conserved, 33 superseded and one not applicable.
The historical field is retained literally; the current correction is explicit.

The two broken draft routes are corrected: Frame closure uses the actual Frame
Position and shared conjunction owners; the tenant computational binding is in
Spec WHAT/HOW And Work Carriers, not an absent heading. Design admission's new
child clause is a distinct carrying locus. Baseline closure carries all named
deciding routes and its four testing-frame descendants. Generic localization
carries the Spec owner and Baseline consumer. Whole auxiliary members, selected
sections and the synthetic fourteen-member historical sentence retain distinct
selection scopes.

## Data and ownership interface

`CONSERVATION.json` is the authored current map. This Writer alone changes it and
`FRONTIER.json`; the packaging Writer reads their exact bytes and refuses a
changed preimage. No refresh imports a prior iteration to reconstruct semantic
fields. `refresh_conservation.py` reads the current map and may change only
`candidate_source_commit`, `pin_state`, `successor_member_pins`,
`successor_locus_pins` and each row's `successor_sha256`.

| Field | Requirement |
|---|---|
| `id`, `source_member`, `source_anchor`, `source_selection` | Immutable predecessor identity and selection; exactly the common 691 rows, unchanged order and source facts. |
| `disposition`, `disposition_standing`, `reason` | Current proposed assessment; unknown proof cannot become acceptance. Removal or accepted standing requires the exact owner decision. |
| `successor_locus`, `successor_loci` | Primary route plus every currently declared carrying locus; all resolve inside the package. Full semantic completeness remains a review question. |
| `successor_relation` | Every supersession has a unique ID, exact predecessor, explicit changed meaning, nonempty replacement loci and `proposed_pending_owner_decision` standing. |
| `consumer_bindings`, `consumer_binding_refs` | Named conditional shared-owner dependencies; each bound row carries those routes. A datum or heading does not become an evaluation merely because its member has Governing Relations. |
| `author_comparison` | Exact rc2 and frozen documentary section/member digests, lengths, granularity, local equality and bounded meaning assessment. Current or recorded-subject drift fails checking. |
| `semantic_review` | Current result remains indeterminate and lists surviving obligations. Byte equality and route validity do not establish semantic proof. |
| `draft_integration` | Exact input digest and one explicit decision for each preserved draft row. |
| `history_correction` | Exact historical 34-row delta and explicit correction, without altering historical fields. |
| `port_account_semantic_sha256` | Binds the five existing named contributions, one receiving owner each and their explicit frontier relations. Source fidelity remains indeterminate. |
| `semantic_sha256` | SHA-256 of compact sorted-key UTF-8 JSON excluding only the pin fields above and this digest itself. Pin finalization must preserve it exactly. |
| `FRONTIER.json` | Exact projection of current rows and current map identity/standing. It is not a second disposition owner. |

Section digests follow the common inventory: a claim ends at the next heading
of **any level**. Frame excerpts may include a subtree and are a different
selection. Explicit aliases immediately preceding headings resolve to that
heading. This distinction prevents an unchanged parent claim from inheriting
every later child addition as an unexplained rewrite.

`PORT_ACCOUNT.json` names exactly the five contributions already selected by
our own frozen Design Source contributions record: context/refinement, work
state/reuse, evidence/identity/conservation, profile binding, and cause-sensitive
result maps. Each has one receiving owner and explicit affected row IDs. Only
own recorded provenance and current receiving sources were read. No exact peer
section is invented, no new port is selected, and neither source fidelity nor
the ported-part acceptance/independence policy is established here.

## Commands and checking contract

From the tenant directory:

```sh
python3 -B qualification/C3/iteration-3/check_conservation.py --self-test
python3 -B qualification/C3/iteration-3/check_conservation.py --require-frozen --no-write
```

The first command writes only `CONSERVATION_CHECK.json`, emits the same report,
and exits zero for valid draft structure. `valid` is the selected mechanical
mode's result; `draft_valid` remains true when only frozen pins are pending.
`semantic_conservation` remains `indeterminate`, and `owner_acceptance` remains
`not_established`. `--no-write` makes the entire check read-only. `--self-test`
mutates only in-memory copies and tests duplicate IDs, secondary missing anchors,
missing replacement relations, unsupported acceptance, omitted historical
changes, unknown bindings, stale comparison digests, rewritten history,
FRONTIER drift and section granularity.

After the packaging Writer freezes the **complete** source, including current
interpretation and derived material, it supplies the full immutable commit and
its complete `CANDIDATE.json`. The conservation Writer runs:

```sh
python3 -B qualification/C3/iteration-3/refresh_conservation.py \
  --source-commit FULL_40_CHARACTER_COMMIT \
  --inventory qualification/C3/iteration-3/CANDIDATE.json \
  --expect-conservation-sha256 CURRENT_EXACT_MAP_SHA256 \
  --check-only
# Repeat the same invocation without --check-only to finalize the pins.
python3 -B qualification/C3/iteration-3/check_conservation.py --self-test --require-frozen
```

Finalization first requires that inventory source coordinates match the exact
commit, every current package file occurs exactly once, and each inventory
member's size/digest matches both current bytes and immutable Git bytes. It then
validates the authored map, generates member/section pins and primary file pins,
and asserts unchanged semantic digest before writing the map and its projection.
It never classifies rows. An old inventory, short commit, body drift or changed
map preimage refuses before map writes. A partial crash between the two writes
cannot pass the exact projection check; both outputs must agree before use.

Verified refusal cases: pending pins fail `--require-frozen` while draft validity
remains true; the old `1ea382a` subject fails finalization with the current
inventory. Both leave map, frontier and preserved draft bytes unchanged.
Mechanical validity does not prove that a replacement is semantically adequate,
a compression preserves all applicable law, an ordinary reader finds the route,
or an owner has approved a changed meaning.

## Remaining decision and evidence boundaries

Required next evaluations are independent source/conservation assessments of the
frozen package, a materially complete policy/replacement decision by the Product
owner, applicable port fidelity and independence decisions, and actual-use proofs.
This Writer is a repair/design contributor and cannot provide the later
independent review of these changes. Same-family reviews must disclose their
limits. Whole-corpus completeness and all six Product criteria remain open.

Keep comparison subjects fixed at installed rc2 and prior candidate
`3ad1fca31dc93ba0847bbbbf308312a554daa1f6`. Ordinary entry and task expectations
must use equal conditions for those subjects and the new candidate, with a
candidate-independent oracle. Existing histories do not qualify current source.
Local map/inventory/frame checks are available; a separately activated native
fresh reviewer can assess the frozen source within its exact grant. External
paid CLI/actor trials require an applicable recorded allowance and known
remaining balance. No allowance reset or new arbitrary numeric cap is inferred.
No such trial, paid call, peer-source read or further delegation occurred here.

## Evaluated draft relations

| Stable row | Prior record | Current proposal | Relation |
|---|---|---|---|
| `AXIOMATIC_CALCULUS.md#position` | superseded | superseded | I3-R2-R001 |
| `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` | superseded | superseded | I3-R2-R002 |
| `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation` | superseded | superseded | I3-R2-R003 |
| `AXIOMATIC_CALCULUS.md#ac-016-typed-composition` | superseded | superseded | I3-R2-R004 |
| `DESIGN_MODULE_METHOD.md#2-position` | superseded | conserved | Retained obligation; carrying relation recorded |
| `DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016` | superseded | conserved | Retained obligation; carrying relation recorded |
| `DESIGN_MODULE_METHOD.md#cross-view-axiom-evaluation` | superseded | superseded | I3-R2-R007 |
| `DESIGN_MODULE_METHOD.md#9-effect-edge-rule` | superseded | superseded | I3-R2-R008 |
| `ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop` | superseded | superseded | I3-R2-R009 |
| `REFERENCE_FRAME_METHOD.md#position` | superseded | superseded | I3-R2-R010 |
| `REFERENCE_FRAME_METHOD.md#rf-002-finite-attention` | superseded | conserved | Retained obligation; carrying relation recorded |
| `REFERENCE_FRAME_METHOD.md#rf-012-closed-results` | superseded | superseded | I3-R2-R012 |
| `REFERENCE_FRAME_METHOD.md#method-functions` | superseded | superseded | I3-R2-R013 |
| `REFERENCE_FRAME_METHOD.md#select-and-activate` | superseded | superseded | I3-R2-R014 |
| `REFERENCE_FRAME_METHOD.md#result-conjunction` | superseded | superseded | I3-R2-R015 |
| `REFERENCE_FRAME_METHOD.md#closure` | superseded | conserved | Retained obligation; carrying relation recorded |
| `RELEASE_METHOD.md#exact-cut-qualification` | superseded | superseded | I3-R2-R017 |
| `SPEC_METHOD.md#what-how-and-work-carriers` | superseded | superseded | I3-R2-R018 |
| `SPEC_METHOD.md#constitutional-chain` | superseded | superseded | I3-R2-R019 |
| `SPEC_METHOD.md#universal-intake-triage` | superseded | superseded | I3-R2-R020 |
| `SPEC_METHOD.md#proportional-disposition` | superseded | superseded | I3-R2-R021 |
| `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` | superseded | superseded | I3-R2-R022 |
| `STDO_REFERENCE_FRAME_BASELINE.md#work-result` | superseded | superseded | I3-R2-R023 |
| `STDO_REFERENCE_FRAME_BASELINE.md#closure` | superseded | superseded | I3-R2-R024 |
| `TICKET_METHOD.md#execution-contract-admission` | superseded | superseded | I3-R2-R025 |
| `TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity` | superseded | superseded | I3-R2-R026 |
| `TICKET_METHOD.md#condition-based-closure-and-reuse` | superseded | conserved | Retained obligation; carrying relation recorded |
| `TICKET_METHOD.md#allowed-status` | superseded | conserved | Retained obligation; carrying relation recorded |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-constraint-judgment-residual-and-stop-kinds` | superseded | superseded | I3-R2-R029 |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation` | superseded | superseded | I3-R2-R030 |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation` | superseded | superseded | I3-R2-R031 |
| `UX_METHOD.md#6-effect-membrane-rule` | superseded | superseded | I3-R2-R032 |
| `WORLD_MODEL_METHOD.md#composition-law` | superseded | superseded | I3-R2-R033 |
| `STDO_REFERENCE_FRAME_BASELINE.md#executive` | conserved | superseded | I3-R2-R034 |
| `STDO_REFERENCE_FRAME_BASELINE.md#3-worker-returns-to-executive` | conserved | superseded | I3-R2-R035 |
| `STDO_REFERENCE_FRAME_BASELINE.md#7-executive-disposes-and-checkpoints` | conserved | superseded | I3-R2-R036 |
| `STDO_REFERENCE_FRAME_BASELINE.md#status-and-authority-boundary` | conserved | superseded | I3-R2-R037 |
| `AXIOMATIC_CALCULUS.md#derivation-provenance` | conserved | superseded | I3-R2-R038 |
| `TICKET_METHOD.md#execution-contracts` | conserved | superseded | I3-R2-R039 |
| `REFERENCE_FRAME_METHOD.md#reference-frame` | conserved | superseded | I3-R2-R040 |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#op-002-atomic-semantic-admission` | conserved | superseded | I3-R2-R041 |
| `SPEC_METHOD.md#position` | conserved | superseded | I3-R2-R042 |
| `SPEC_METHOD.md#manifesto` | conserved | superseded | I3-R2-R043 |
| `SPEC_METHOD.md#process-constitution` | conserved | superseded | I3-R2-R044 |
| `SPEC_METHOD.md#renewal-path` | conserved | superseded | I3-R2-R045 |
| `SPEC_METHOD.md#method` | conserved | superseded | I3-R2-R046 |
| `STDO_REFERENCE_FRAME_BASELINE.md#counterexample-localization` | conserved | conserved | Retained obligation; carrying relation recorded |

## Historical disposition changes

These facts are generated from the two immutable historical maps; they are not current dispositions.

| Stable row | Before | After |
|---|---|---|
| `AXIOMATIC_CALCULUS.md#position` | conserved | superseded |
| `AXIOMATIC_CALCULUS.md#ac-007-constraint-and-refusal` | conserved | superseded |
| `AXIOMATIC_CALCULUS.md#ac-014-judgment-separation` | conserved | superseded |
| `AXIOMATIC_CALCULUS.md#ac-016-typed-composition` | conserved | superseded |
| `DESIGN_MODULE_METHOD.md#2-position` | conserved | superseded |
| `DESIGN_MODULE_METHOD.md#transformation-admission-completeness-stdo-up-016` | conserved | superseded |
| `DESIGN_MODULE_METHOD.md#cross-view-axiom-evaluation` | conserved | superseded |
| `DESIGN_MODULE_METHOD.md#9-effect-edge-rule` | conserved | superseded |
| `ODD_METHOD.md#115d-constructive-evaluation-and-yield-loop` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#position` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#rf-002-finite-attention` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#rf-012-closed-results` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#method-functions` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#select-and-activate` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#result-conjunction` | conserved | superseded |
| `REFERENCE_FRAME_METHOD.md#closure` | conserved | superseded |
| `RELEASE_METHOD.md#exact-cut-qualification` | conserved | superseded |
| `SPEC_METHOD.md#what-how-and-work-carriers` | conserved | superseded |
| `SPEC_METHOD.md#constitutional-chain` | conserved | superseded |
| `SPEC_METHOD.md#universal-intake-triage` | conserved | superseded |
| `SPEC_METHOD.md#proportional-disposition` | conserved | superseded |
| `STDO_REFERENCE_FRAME_BASELINE.md#executive-attention-evaluation-and-action` | conserved | superseded |
| `STDO_REFERENCE_FRAME_BASELINE.md#work-result` | conserved | superseded |
| `STDO_REFERENCE_FRAME_BASELINE.md#closure` | conserved | superseded |
| `TICKET_METHOD.md#execution-contract-admission` | conserved | superseded |
| `TICKET_METHOD.md#recorded-judgment-and-owner-ruling-continuity` | conserved | superseded |
| `TICKET_METHOD.md#condition-based-closure-and-reuse` | conserved | superseded |
| `TICKET_METHOD.md#allowed-status` | conserved | superseded |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#closed-constraint-judgment-residual-and-stop-kinds` | conserved | superseded |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#candidate-judgment-event-and-relation-separation` | conserved | superseded |
| `TRAVERSAL_OCCURRENCE_PROFILE.md#mutable-subject-effect-relation` | conserved | superseded |
| `UX_METHOD.md#6-effect-membrane-rule` | conserved | superseded |
| `WORLD_MODEL_METHOD.md#composition-law` | conserved | superseded |
| `release/release-note.md` | conserved | not applicable |
