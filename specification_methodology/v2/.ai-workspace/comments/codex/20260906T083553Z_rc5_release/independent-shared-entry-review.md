**Closed result: `satisfied` for all four selected shared-plugin native contexts.**

Assessor: `/root/rc5_installed_review`, independent of fixture construction and
native execution. This is the separately delegated T030 shared-entry assessment;
the [installed-update result](independent-installed-update-review.md) remains a
different closed relation.

The exact oracle is [T030-RC5-SHARED-ENTRY-O1](t030-shared-entry-001/independent-oracle-review.md),
SHA-256 `d29e82ad058f4f00a767675dd75e543088863b5d30c7a5dc3a859a469e64973b`,
frozen before exposure. `contexts.json` remains
`8ce9e9520a7a5b74fd0ef4c970446cb004650a2f7dd02420dce101fbb03d8ad6` and the
pre-exposure result-capture amendment remains
`b4a63c71c28a6d0bed9dadb94991b3a9e85fa12d29e7521028b3d91de8cf2df6`.
No oracle or native artifact was changed during this assessment.

Each provisioned source-only `spec` plugin contains the exact 17 files from
STDO A `c7888bb2dc9aee1f5a217985f6d1547cfe6465f0`; every file was compared
directly to that commit. The actual native traces load `stdo-work` and
`PRODUCT_BASIS` and invoke the installed manager to verify the one P0 Definition
at RC5 manifest
`3fb89aeb80c65403debf1eba1705fde614556520bf1ce1a08a39033b6d98a50f`.
Custodian preflights are not used as substitutes for those operator calls.

| Native context | Closed finding | Decisive raw evidence within `t030-shared-entry-001/<context>/` |
|---|---|---|
| `t030-direct-work-codex` | `satisfied`: direct admitted Writer work; only `cache.py` changed; exact probe returns counts 1 and 0; complete Public values, root/upstream and D0/A0 relations conserved; actual result returned through the owner-named capture. | `stdout.jsonl` lines 7/21 load the two shared references; line 28 verifies P0; lines 58/62 compare grant, design, complete Public and root relations; line 60 records the one file change; line 64 contains the successful actual probe. `final.txt` SHA-256 `f56b48aadd0210f8aeb6318fd64519131ca8dd9bffc6595e9cbedcf539b7aec7`. |
| `t030-direct-work-claude` | `satisfied`: same admitted finite outcome on its separate host; one exact edit, fresh before/after probe, preserved other files and declared relations, no extra ticket/review/approval cycle. | `stdout.jsonl` lines 41/49 load the shared references, 234/235 verify P0, 361/362 perform the edit, 374/375 report the successful actual probe, and 378/381 verify conservation. `final.txt` SHA-256 `d88e3ad17884c5e6b884378fcb9eaf8093dd36fcca9d7b90b2c303ca79892ae8`. |
| `t030-drafted-refusal-codex` | `satisfied`: identifies inspection-only requester authority and missing admission/operation grant, retains the draft and candidate, returns owner re-entry without construction or carrier mutation. | `stdout.jsonl` lines 6/18 load the shared references, 29 verifies P0, 56 records the actual failing current-cache probe, and 61 binds the absent authority and conserved current relations. `final.txt` SHA-256 `ea14cc620f827bcca686960fde03ae885d12fbdc31c196d4b9557790abcc6c95`; pre/post snapshots are identical. |
| `t030-drafted-refusal-claude` | `satisfied`: same warranted refusal and next owner action; no candidate edit, self-admission or ticket promotion. The current-cache defect is observed separately from authority to repair it. | `stdout.jsonl` lines 61/69 load the shared references, 186/187 verify P0, 219/220 contain the actual current-cache probe, and the final return withholds construction/admission. `final.txt` SHA-256 `a3291e3d1cdd2d4957a8d9060b1ab906b9329dfb4b85e10cb60e7833376ce574`; pre/post snapshots are identical. |

I read the complete tool-operation histories, including failed calls, and
checked every per-run `execution-result.json` file binding against its retained
bytes. All four process exits are 0 without timeout. Actual current worksite
files and symlinks match their after-snapshots. Both positive candidates have
SHA-256 `3ffaa03164c3d08430fd4231dcd80f9192f00457161ae3dbc2e79da68d5ac1f5`;
both refusals retain baseline
`48073f6207c881324ba2d71c75831ecd87bfce40cc806be999d1011e5eee1ecd`.
The immutable raw trace SHA-256 values, in table order, are:

- `d213fa963499ee1c13249bcf63582aae2f9c706c5e9a5830b02a84bb846ed193`
- `1adf1b5b82b8c2aad685ae0f7d9f9aca25a5fa1345362c0347de540c77923a29`
- `c2df90c2da8dd28752fd7f61315866f16ce194635d17f8c0231cf44388e027fa`
- `af90991b71acdeb5ffce35053c287fe1433fac522fb1508cf7de991e01c97eb9`

The actual outer sandbox profiles are the paths in each `command.json`, under
the retained `20260906-native-rc5-001/shared-entry-handoff/` carrier. They match
the profile digests in the passing actual `confinement-preflight.json` records.
The separate earlier `sandbox.sb` copies are not substituted for those actual
execution profiles. The probed source/oracle, prior-session and sibling
boundaries passed; observed tools do not read another actor's task, expected
answers or prior context. The histories show only the two granted `cache.py`
edits and permitted reads/computations. Host transport and the authorized
editor's temporary-file mechanism remain distinct from extra Product effects.
Snapshot equality alone is not the basis for this conclusion.

There are no material unsatisfied findings in these four questions. Retained
host friction includes Codex's initial absent `PRODUCT_BASIS` locator and denied
shell heredoc temporary-file creation, and Claude's restricted `Read`/`Grep`
attempts against installed source files. Subsequent allowed reads recover the
exact required inputs, and all required actual manager/probe calls succeed.
Those denied calls receive no read or execution credit and are not erased.

This result qualifies the four exact, explicitly requested native uses on
Codex CLI 0.153.4 (`gpt-6-astra`) and Claude Code 2.1.263
(`claude-fable-5-1`). It does not establish automatic plugin triggers, other
shared verbs, Representation outcomes, consumer updating, universal sandbox
containment or model reliability, Product acceptance, publication or adoption.
No additional execution or new qualification gate is requested.
