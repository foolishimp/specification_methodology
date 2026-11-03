# Final independent review — bounded Unicode/ATX reader repair

**Result: satisfied for the selected Unicode line, fence and adjacent empty-ATX selector repair. No current actionable S0–S4 finding remains within this reviewed boundary.** This conclusion is about the exact source and exercised syntax cases, not general CommonMark correctness, native-host qualification or release.

The prior `STDO304_SKILLS/review/FINAL_REVIEW.md` at SHA256 `77ed471319ee80b12301ea528a193dd841488a6ef4cb70f532c29acc9fedbf47` is explicitly superseded for its no-actionable conclusion and OP-02 closure concerning this source reader. Its original bytes, failures, successful observations and their limits remain intact. This review supplies the new bounded disposition; it does not rewrite that history.

## Exact subject and expectation

Final subject is `SOURCE_DELTA_02.json`, SHA256 `6f129f5e680b620bd20ad5d493586eb6326a0dcac1bff5eaca148f57941c45a6`, composed over first delta `6cd82322ac23d4dfe8ce7d8bf0df73fd2d3ffcbe06f3f70be8925d27e22dc523` and prior source freeze `86afcb8a1d9e0d73297414fc935125dfb107f3cfad732be4694ec96ce8ce8c2b`. Baseline HEAD is `0aa00244602293d8e0fd384b7a280ae443afcd7d`.

The final reader is `df7730a1f661a8be7a3144feff474f83197987ebfd1cce4063aa9c5504e75c41`; tests are `b2bc411ff716de57222aed64969bcaca6d2670d1325a45e4f061d8087f31d2fa`. Only reader/tests differ from delta01; the full repair changes reader, tests and the bounded design clarification from the Git predecessor. All 116 composite source pins and exact 110-member payload inventory match before and after. Original freeze, first-delta bytes, prior review and old 673-file evidence seal remain unchanged.

`EXPECTATIONS.md` was frozen before successor exposure at `f0336e8307faf7068d88706f09f446cd05775ba16ef4b565c2de7e7ccf04f7bd`. CS-09 requires an exact verified source projection or explicit failure; a verified file digest cannot justify invented headings. The syntax oracle was [CommonMark0.31.2 characters/lines](https://spec.commonmark.org/0.31.2/#characters-and-lines), [fences](https://spec.commonmark.org/0.31.2/#fenced-code-blocks), and adjacent [ATX headings](https://spec.commonmark.org/0.31.2/#atx-headings). The helper may refuse syntax outside its supported subset. Reviewer expectations were not derived from Writer implementation or repair rationale.

## Findings and correction evidence

| Finding | Original evidence and causal location | Final disposition |
|---|---|---|
| OP-02 Unicode reopening, S2 | Predecessor `read_basis.py:101,166` used Python splitlines, creating headings and false line coordinates at U+2028 and other non-CommonMark separators. At `:104`, Unicode whitespace falsely closed a fence followed by NBSP. Actual CLI returned checked catalogs and invented sections. `PREDECESSOR_FINDING.md` and `predecessor_RESULTS.json` preserve this result. | Corrected. Final `read_basis.py:89–91` supplies the common physical-line representation; `:106` and `:171` use it for scanning/extraction. Fence closure at `:109` admits only the intended space/tab suffix. U+2028 remains within the exact source line and projection, false selection refuses, and the NBSP-terminated unclosed fence refuses the whole projection. |
| Adjacent empty closing-hash ATX selector, S2 | First successor `read_basis.py:159–163` admitted `## ###` but cataloged false name `###`; the CLI positively selected it and refused the real empty name. The tab variant behaved likewise. This pre-existing adjacent defect was independently confirmed under frozen U-05 and separately selected by the Executive. `ADJACENT_ATX_FINDING.md` and `ADJACENT_ATX.json` preserve it. | Corrected. Final `read_basis.py:159–163` separates the opening delimiter, title and optional closing delimiter. Both exact specimens now catalog/select the empty heading and refuse `###`. Adjacent NBSP content remains literal, and returned source bytes, digests and line coordinates match. |

The original Unicode fix passed the frozen matrix before the adjacent finding; that success was not used to conceal the remaining defect. No candidate repair was performed by this reviewer.

The final independent reviewer checks are:

- 42 source-derived cases, frozen before successor exposure, through 126 actual helper CLI calls: all give the correct projection or explicit refusal. These cover the reported counterexamples, eight Python-only separators, NBSP and adjacent fence suffixes, valid ASCII closers, LF/CRLF/CR/mixed terminators, exact UTF-8 projection digests and coordinates, catalog/selection agreement, and bounded title discriminators. There are 80 checked projections and 46 explicit refusals; this is not an all-refusal success.
- Four separately retained adjacent ATX cases through 12 CLI calls: all pass on delta02. Empty selectors succeed, invented selectors refuse, and NBSP-before/after controls preserve content. Ordinary titles, escaped hashes and genuine hash titles were also inspected in the added regression tests.
- The exact 35-test helper suite was independently run on a reviewer-owned frozen copy, with temporary writes restricted to the review directory: all pass. This includes retained container/comment/HTML refusals and existing identity/gate controls.

The raw specimen tests use a declared controlled manager double while executing the shipped helper's real CLI verification/projection path. They do not establish real installation. Separately, the tester replayed all 33 retained successful helper inputs through the real manager and explicit retained stores using only the new reader path. I independently compared every complete JSON result with the original retained tool result and prior replay: all equal, with zero exit failures. The population is 32 actual native helper calls plus one mechanical EF-03 reproduction, including all 13 direct-case and 11 final issuer/recipient inputs. `REPLAY_REVIEW_002.json` pins that comparison; no new native actor ran.

## Consumed evidence and limits

The final test report `ae00a05afaa9bb34bcc589587289a0c71973a142c3df9c720578e173a0a3118f` accurately separates predecessor failures, first successor, final successor and native limits. All 53 members of test seal `929edf1169d6f99c9a1594785fc8597f8121348ba700b1051dca6fedb9d497c4` independently verify. The retained replay is `1208654abc73611253ddd7607ff2f4518408eea40b48843fe126829aa792ce6d`. The tester's separate 78 CLI observations and package/reference/skill checks are bounded evidence; 110 members/6,091 references and five skill validations are structural results, not semantic or native qualification. Bookkeeping corrections in delta composition and payload ordering are disclosed; they were not candidate failures or additional actor runs. This review also records its corrected delta-overlay precheck separately.

This remains a closed ATX/source-projection subset with explicit unsupported-structure refusals. The reviewed cases and retained outputs do not qualify every Unicode/Markdown combination. No source-law, basis or host-gate change was made: construction remains on its installed 2.5.1-rc.2 basis; released3.0.3 remains the separate comparison/fixture basis.

Prior successful Claude issuer/recipient observations belong to revision4. Revision5 and this repair receive only bounded retained-input compatibility evidence. Those native actors loaded exact skill/reference files after denied native Skill calls; the declared harness supplied dispatch and durable recording. Their direct-call guard was not a transitive-program/OS/managed-context isolation proof. Original timeouts, overreads and evidence corrections remain failures or bounded observations under their original labels. Other complete skill modes and broad workloads remain unqualified by those live trials.

Reviewer is `/root/stdo304_skills_review`, same-family nonauthor. This is independent working review, not cross-family method qualification or Product acceptance. Writes were confined to this new review territory and one new Codex commentary post; no source, Git or original evidence mutation occurred. The Executive retains Product disposition and any next authorized action. No new approval or release gate is introduced.

Frozen at 2026-11-03T00:32:46.456937+00:00
