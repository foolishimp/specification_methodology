**Closed result: `satisfied` for the bounded installed RC5 complete-update relation.**

Assessor: `/root/rc5_installed_review`, independent of fixture construction and
operation execution. This activation consumes the existing T030/T009 release
grant and evaluates installed-path, acceptance/refusal and subject/grant/effect
conservation. It grants no Product mutation, acceptance, adoption or publication.
The only assessor write is this review.

The evidence root, `E`, is
`stdo_representation/dogfood/t009-frame-projection/rc5-installed-update-001/`
relative to the coordinated repository root. Its handoff manifest SHA-256 is
`b199d92a26e6afbb52bb0be143118c24468b7356286e11c6283e197a1ccc4715`;
`E/execution.json` is
`63ca9d5464d7874ae33ee85d16a893d1ac8813dcf8f79b7ea16ecdcc755e4da3`.
Both were reacquired directly. The existing
[installed-update-evidence-checks.json](installed-update-evidence-checks.json),
SHA-256 `c773a2b71b779a797c00558670b5b21fd2bf52394c2a96efd150eaa470282fdf`,
supplies sufficient exact checks of 230 retained files, 16 actual installed
Product members, acceptance bindings, resulting state and map equality; it has
no failures. This assessment reuses those computations and separately reads
the raw operation records, outputs, grants and their producing script.

The subject is the actual manager
`/private/tmp/stdo-rc5-installed-manager-20260906/bin/stdo`, installed from STDO
commit A `c7888bb2dc9aee1f5a217985f6d1547cfe6465f0`, annotated tag object
`d4b7c7724944e02ce25c6e6ce69722491c349924`, installed RC5 manifest
`3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f`.
The actual launcher matches `E/installed-manager-subject.json`; all eleven
installed Python source files match both that record and exact commit A.
The child commit is `4560b4ec1ac18f7ff3dab09c5ca4e7629d467a94`, with Axiom tag
object `7813c9555ddde8f649d70870dc6ab9dabdd1d80c` and Representation tag object
`5edeb22233fb9625fbf3b386a2fb1e2f8f88fead`. The exact commit-B cohort carrier
SHA-256 is `ea9bcfbb3cb41222b30bb55c9b9250480f9fac08554942a44891b5d44bbaef00`.
The seven/nine-member installed inventories retain their distinct Product
identities and match the selected carrier.

| Evaluated relation | Result and exact evidence |
|---|---|
| Accepted positive update | `satisfied`. `E/cases/UAT-09-A/plan-acceptance.json` binds plan `a9517af720db3f20b37af4a611317dbe9da0cad859e0b2bc3ba4e62c1f1d311e`, its actual stdout bytes, definition preimage, selection and exact consumer. `observations/complete-apply.command.json` invokes the installed manager with that digest and exits 0; its raw stdout says `updated`, `complete: true`. The subsequent `resulting-basis-status` observation verifies exact RC5. |
| Installed Axiom causal path | `satisfied`. The positive case's `observations/installed-indexer-context-validation.command.json` invokes `P0/.products/axiom-indexer/build_tenants/core/code/ac.py` through the installed-manager Python. That route targets the selected immutable RC5 Axiom install; executable SHA-256 is `87c43389c619d9ca0e2d930a10e471a17545be9a0394d1c0f47db7e8e2c6d931`. Exit 0 and `installed-indexer-map.json` reproduce the retained map exactly. Earlier source-indexer preparation is separately visible and is not counted as this installed witness. |
| Missing and wrong acceptance | `satisfied`. UAT-09-B's `missing-operation-acceptance` exits 2 with the actual CLI required-argument refusal. `unaccepted-plan-digest` supplies 64 zeroes, exits 2 and reports that an unchanged explicitly accepted plan is required. Both use the installed CLI; pre/post consumer states are identical. Its successful dry-run remains `planned`, `complete: false`. |
| Stale source and preserved prior basis | `satisfied`. `source-digest-refusal/observations/complete-plan.stdout` reports `held`, `ready: false`, `complete: false` and the exact stale `repo://p0/SOURCE.md#handoff-note` route. The subsequent held apply exits 2 before effects. Consumer pre/post states are identical; verified RC4 basis and historical native routes remain. I also compared the actual historical installs to their retained setup snapshots: all 61 Axiom and 274 Representation entries are unchanged. This preserves the prior Install; it does not make the changed-source context current. |
| Subject, grant and effects | `satisfied` within the declared operation population. Each construction grant selects synthetic P0 and the isolated evidence territory. Positive acceptances are exact, single-application fixture decisions. The positive receipt and state delta agree on six selected links and `stdo_p0.json`; source, program, map, native entry, unrelated bytes and other definition fields remain conserved. Store/install destinations are inside the same evidence territory. No observed command selects a live consumer, fleet or publication effect. |

`E/observe_updates.py` records actual `subprocess.run` argv, working directory,
exit status and raw stdout/stderr digests, with a refusal to overwrite prior
command observations. It removes `PYTHONPATH` and `PYTHONHOME`. The actual
installed implementation checks held/accepted-plan conditions before its
consumer effect phase, rechecks source and consumer preimages after staging,
and verifies installed targets before reporting completion. This agrees with
the observed transitions. The retained initial schema refusal and bounded
fixture repair in `E/preparation-failure-001/repair.json` remain visible; they
are not successful-update evidence.

Two boundaries are material. UAT-09-C retains old authored meaning and performs
an actual reindex over changed source; its actual `planned`/ready result is
correct mechanical evidence only. It supplies no semantic-fidelity judgment
and applies no update. UAT-13-C supplies another actual successful installed
update under accepted plan
`9a7528f5aca9308e331ac390a0943b5adbe8d57e18c1aab3c43a797c537051d5`, but the
success and resulting route observations are custodian evidence. Its
`operator-observation-scope.json`, `attempt-visible.json` and
`first-result-visible.json` deliberately withhold those facts from the native
operator. This review does not infer the operator's knowledge or grade native
behavior from custodian success.

Coverage is finite: these isolated installed executions establish the selected
positive and pre-effect refusal paths. They do not establish native LLM
outcomes, public reacquisition, live-consumer adoption, universal semantic
correctness, all updater combinations, concurrent-writer protection or abrupt
multi-path crash recovery. Command records and snapshots are not a complete
system-call trace; final equality is not evidence that all transient effects
were absent. Those broader claims are outside this activation, with no new
release gate added. There is no unsatisfied or indeterminate condition within
the selected installed-update question. Return this closed result to the
existing release coordination.
