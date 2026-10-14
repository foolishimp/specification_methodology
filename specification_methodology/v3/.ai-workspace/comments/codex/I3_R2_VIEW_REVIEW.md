# I3-R2 documentary view review

## Closed working result

**Verdict: `falsified`.** Within the source passages and views assessed below, the claim that the frozen documentary views preserve their owners' conditions, permissions, result meaning and authority is false. Two material counterexamples are established. Both concern compressed summaries; neither requires changing the governing source. No independent minor defect is established.

This is a bounded, nonauthor working review under activation `I3-R2-VIEW-REVIEW-01`, supplied as admitted in main `ab11cbc`. It is not member acceptance, an installed-v3 qualification result, an execution grant, or an Executive priority/disposition decision. The exact supplied activation was used without inspecting surrounding ticket history.

| Coordinate | Binding |
| --- | --- |
| Repository | `/Users/jim/src/apps/specification_methodology` |
| Documentary subject D | `f2cb3e593757d094d008102551925e871a0204ff` |
| Candidate prefix P | `specification_methodology/v3/build_tenants/codex/successor/` |
| Common basis B | `355aa8655cca9c6ba6cf5c414f9bea3032ae89fd` |
| Frame declaration | D:`specification_methodology/v3/build_tenants/codex/qualification/C3/iteration-3/FRAME_INPUTS.json` |
| Installed governing builder | `/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2` |
| Exact installed manifest SHA-256 | `3d860ff4c1746f06ac25295a9e205cffb8e7725869615ac77cf2304b70ff2782` |
| Result owner and permitted output | Working Reviewer; this report only |

Throughout this report, `D:P/...:Lx-Ly` means the specified lines of the immutable Git object, acquired with `git show D:P/...`, not a live candidate file. `B:` likewise identifies the immutable common basis. Installed references below are relative to the exact installed builder root.

The installed manifest hash matched the supplied digest. `stdo verify v2.5.1-rc.2 --manifest-sha256 <digest>` returned `valid: true` with no failures. The read-only `stdo status --definition specification_methodology/v3/stdo_3.json --verify` also resolved the specified Product Definition to this installed basis, with verification true and no failures. These checks establish the review's installed-v2 basis; they do not qualify the candidate as installed v3.

The installed Reviewer skill was used: [stdo-review/SKILL.md](</Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/plugins/spec/skills/stdo-review/SKILL.md>). Result and role treatment follow installed `standards/REFERENCE_FRAME_METHOD.md:409-441,1312-1329` and `standards/STDO_REFERENCE_FRAME_BASELINE.md:427-454,658-701,1386-1408`. Severity below uses the grant's material/minor distinction; no numerical scale, priority or boundary disposition is invented.

## Findings

### F1 — Material: traversal compression excludes a lawful core verdict

**Claim and evidence.** D:P/`standards/authority_compressions/traversal_occurrence_profile.compressed.md:83-86` says:

> Constraint predicates return only satisfied, falsified, indeterminate, or invalid basis.

The owner makes all five core verdicts available for evaluating an in-domain subject: D:P/`standards/TRAVERSAL_OCCURRENCE_PROFILE.md:748-753`. More specifically, its `:802-811` requires an in-domain evaluation missing material scope or capability to retain core `out_of_frame`, a stop reason `out_of_scope`, and an `unresolved_cause` residual naming the missing relation. Its corresponding decision remains `hold`, or `indeterminate` for `transition_evaluation`. These distinctions agree with D:P/`standards/FOUNDATIONS.md:304-424`, including the reason-sensitive domain mapping at `:391-408`.

**Concrete counterexample.** Consider an otherwise valid in-domain `semantic_cut_complete` constraint evaluated by `semantic_cut_admission`, with a valid subject and basis but without access to a material relation or the capability required to assess it. The owner permits and specifies `out_of_frame`, with the original `hold` decision, `out_of_scope` stop and `unresolved_cause` residual. The summary's exhaustive “only” list excludes that return. A consumer implementing that list must reject a lawful result or coerce it into a different result meaning. This is a documentary counterexample; no runtime occurrence is claimed.

**Why material.** This changes the closed result domain and can erase the difference between an unassessed material relation and an inconclusive assessment. The summary has a current source digest. Its general source-routing preamble at `:16-21` makes the owner available, but cannot make the contradictory exhaustive list faithful. Owner fallback contains the risk; exact source identity does not remove the mismatch.

**Technical triage.** Confidence is high because the conflicting statements and a specific lawful case are explicit. Potential exposure includes users deriving or evaluating traversal constraints through this summary, including the relevant transform/design-depth/review-grade families. Actual execution frequency and installed consumer impact were not measured. The existing owner and foundation result mapping provide containment. The apparent correction locus is this derived summary; no source-rule change is indicated. Textual repair appears small, but downstream closure and regression exposure have not been demonstrated. A useful independent readback would distinguish all five core returns and retain the owner's reason, decision, stop and residual conditions.

### F2 — Material: aggregate compression removes explicit ticket-owner selection of durability

**Claim and evidence.** D:P/`standards/authority_compressions/stdo_compressed.md:383-387` says:

> Create or update a ticket only when work or an obligation outlives the local carrier boundary: the admitted sprint when inside one, otherwise the current run, and only under ticket-state authority.

The governing lifetime table is D:P/`standards/TICKET_METHOD.md:713-739`. Its explicit exception at `:737-739` says:

> An explicit instruction from ticket-state authority to create a durable record selects that durability. It does not admit an execution contract or widen its upstream work authority.

The more specific D:P/`standards/authority_compressions/ticket_method.compressed.md:45-52` preserves both the ordinary lifetime selection and this exception. The aggregate therefore conflicts with the owner and with another current summary of that owner.

**Concrete counterexample.** Authorized work and its work obligations end in the current run, while the competent ticket-state owner explicitly instructs the worker to create a durable record. The owner permits that selected durability while keeping execution admission and upstream work authority separate. The aggregate's “only when” excludes the case unless the worker invents a longer-lived work obligation or overrides the aggregate by returning to the owner. The explicit instruction does not itself admit the work or grant unrelated effects.

**Why material.** This narrows an actual owner's permission and can prevent compliance with that owner's explicit instruction. It does not establish a universal obligation to create tickets, nor does absence of a ticket confer permission to create one. The defect is omission of the source's particular exception from a categorical restriction.

**Technical triage.** Confidence is high from the direct source, aggregate and specific-summary comparison. Potential exposure is carrier/durability selection performed from the aggregate summary. Actual affected executions were not measured. The governing ticket section and its specific compression provide containment. The apparent correction locus is the aggregate derivation; no governing-source change is indicated. Textual repair appears small, while consumer/regression closure remains unassessed. A useful readback would exercise both the ordinary lifetime rule and the explicit competent-owner instruction, preserving the separation from execution admission.

## What the successful checks establish

All nine compression headers identify current owner digests at D. The six declared frame files also match their declared file digests. An independently constructed, read-only comparator checked all **98 selected source blocks** against their owners. It recognized headings outside fenced code, selected sections through the next same-or-higher-level heading, resolved relative Markdown links to their actual targets, and ignored trailing horizontal separators and whitespace. All 98 blocks matched. No comparator script or other file was persisted.

The narrow claim “these declared selected bodies and link targets reproduce their specified owners under that normalization” receives **`satisfied`**. This does not establish that the selected sections suffice for every task, that an actor acquired or understood them, or that ordinary entry has successfully exercised them. The material findings above survive these successful identity checks.

| Declared frame | Blocks matched | Scope and material dependency checks performed |
| --- | ---: | --- |
| `EVALUATION_CONJUNCTION` | 11/11 | For combining declared material predicates, traced core result/conjunction, applicability, material coverage, authentication and minimum-result routes. A valid falsifying contribution remains visible when another required contribution is missing; incompatible or invalid contributions do not erase an independently valid finding. No acceptance or repair grant is supplied. |
| `CONSTITUTIONAL_DERIVATION` | 23/23 | For bounded WHAT-to-HOW and producer/consumer derivation, traced transformation admission, producer/consumer authority, seam/totality and source-determination routes. A shape-correct product with a stale predecessor or missing admitting owner does not acquire admission. Explicitly coherent multi-basis arrangements remain possible. The frame does not create an upstream-change grant or a universal runtime mandate. |
| `DOMAIN_BINDING` | 18/18 | For the declared continuation/projection/Markov-overlay selection, traced configuration, ODD continuation/adoption, UX projection/replay, Markov definition/proof and traversal adoption conditions. Publication of a Markov candidate does not prove the statistical conditional-independence gate; precedence does not confer authority. This is not whole-domain or whole probabilistic-model qualification. |
| `RELEASE_ADOPTION` | 12/12 | Traced immutable identities, publication, exact-cut qualification, successor disposition and consumer adoption. Publication, acceptance and consumer adoption remain distinct. A removed predecessor claim is not silently conserved; the actual owning decision remains required. No effect grant follows from the excerpt. |
| `WORK_RECOVERY` | 15/15 | Traced workspace/work-recovery, bounded-work, computed treatment, ticket closure and required result routes. Lost acknowledgement leaves effect occurrence unresolved before repetition; context loss does not reset work; a sufficient direct-writer grant remains usable. The selection declares itself nondeciding, requires actual activation/outcome-domain acquisition, and does not adopt the optional baseline by inclusion. |
| `TRIAGE_CARRIER` | 19/19 | Traced intake/upward handoff, carrier/execution admission, triage and actual subject/basis/authority routes. Missing upstream authority cannot be repaired by creating a substitute ticket. A human override does not overwrite the admission finding. The copied ticket owner section includes the explicit durability instruction relevant to F2. |

These are bounded logical route checks against the stated tasks, not six whole-frame acceptances. In the listed cases, the declared routes expose the deciding dependencies examined. No additional material route omission was established within this coverage. Other cases needing coupled profiles or additional owner sections must follow the declared re-entry rather than infer permission from absence. For example, the selected domain frame does not by itself settle all Markov construction or UX local-ephemera/adoption cases. This review does not convert that bounded selection into a requirement that every frame include every domain clause.

The broad claim that these routes suffice for all possible instances of their families remains **`indeterminate`**: that scope exceeds the acquired and reasoned cases, and practical use was not run. Exact excerpt copies alone are insufficient evidence for the broad claim.

## Ordinary entry and authority boundaries

D:P/`plugins/spec/skills/stdo-work/SKILL.md` was read in full (138 lines; 8,555 bytes). Its Product selection and verified installed basis do not grant work (`:11-16`). Its entry instructions acquire current subject/context, responsibility frame and material source references, with task-specific routing for recovery, triage/carrier and constitutional handoff (`:18-58`). Existing exact grants are usable without asking again; carrier/execution admitting owners remain prerequisites where required (`:80-97`). Source intake/computed treatment, direct-writer conditions, independent assessments and effect/proof ownership are retained (`:62-76,101-138`). The entry does not automatically invoke durable-ticket creation.

D:P/`standards/README.md:42-44,81-90,100-119` supplies material coupled-owner re-entry, distinguishes views from authority, and permits selected task-relevant acquisition rather than universal full-corpus loading. Together these instructions expose routes that can recover omitted detail. They do not make F1 or F2 accurate statements, and they do not prove that an actor followed the routes.

The frozen interpretation links intentionally target a subsequent dependent generation. Their known intermediate absence is **excluded from documentary-semantic findings**, as directed by the grant. Their eventual actual-entry use is subsequent proof. No installed-v3 invocation, native-host trigger proof, or practical actor-attention qualification was attempted here.

## Coverage and acquisition record

The deciding-owner acquisition preceded inspection of the corresponding compression/view claims; later targeted owner re-entry resolved specific comparisons. `FRAME_INPUTS.json` was used only for frame/route/scope declarations. Author compression-review commentary was excluded. Frozen blobs were acquired with `git show`; no live changed candidate files, author rationale, prior reviews, peer implementation or oracle expectations were used. There were no paid calls, Git mutations or subdelegation.

The common obligations used include B:`specification_methodology/v3/specification/requirements/README.md:14-18,82-94,109-150` and B:`specification_methodology/v3/specification/conformance/README.md:21-43,49,58-59,76-78`. These require preservation of source triggers/modalities/exceptions, material coverage and result distinctions; they distinguish source comparison, exact-copy mechanics and practical use. Applicable instruction routing, Product Definition and reference-frame basis were also acquired. The Product's independent review and acceptance ownership remain separate; this bounded working result does not claim the member's six acceptance criteria are satisfied.

The following are the unique source intervals acquired and assessed. Bytes count source text for those intervals, including line endings, without terminal line-number prefixes or repeated acquisitions.

| Deciding owner under D:P/`standards/` | Acquired line intervals | Unique bytes |
| --- | --- | ---: |
| `FOUNDATIONS.md` | 1-666 | 45,675 |
| `TRANSFORMATION_LIBRARY.md` | 1-398 | 28,081 |
| `REFERENCE_FRAME_METHOD.md` | 120-259; 344-542; 645-790; 1418-1440 | 25,150 |
| `SPEC_METHOD.md` | 101-234; 290-335; 476-659; 877-935; 1349-1565; 1593-2092; 2670-2682 | 67,538 |
| `TICKET_METHOD.md` | 101-149; 179-200; 671-955; 1001-1025 | 21,319 |
| `DESIGN_MODULE_METHOD.md` | 3-36; 190-255; 550-593; 794-896; 1971-1995 | 16,399 |
| `UX_METHOD.md` | 4-539; 603-629 | 30,447 |
| `ODD_METHOD.md` | 4-42; 751-783; 1462-1475 | 5,743 |
| `AXIOMATIC_CALCULUS.md` | 3-68; 401-542; 715-775; 857-885; 927-1010; 1046-1061 | 19,180 |
| `TRAVERSAL_OCCURRENCE_PROFILE.md` | 4-84; 693-846; 894-1247 | 32,327 |
| `WORLD_MODEL_METHOD.md` | 287-456; 679-703; 1425-1452 | 10,276 |
| `RELEASE_METHOD.md` | 65-96; 206-306; 334-386; 611-671 | 14,486 |
| `STDO_REFERENCE_FRAME_BASELINE.md` | 89-166; 1665-1683 | 7,283 |
| **Deciding-owner passage total** | **13 owners** | **323,904** |

The full standards index added 7,785 bytes, yielding **331,689 bytes** of unique acquired owner/index passages. These are acquisition/coverage measurements, not a claim of uniform line-by-line semantic verification of every sentence. Earlier truncated output was not treated as read; necessary passages were reacquired in bounded sections.

The mechanical extraction/hash check loaded **814,165 bytes** of unique complete owner blobs and **360,304 bytes** across the six frame files. The complete blobs support extraction and digest checking; their unselected text is not thereby semantically reviewed. Frame sizes in table order were 44,141; 69,445; 54,985; 46,999; 63,001; and 81,733 bytes.

Nine compression files total **182,837 bytes**. Full bodies of `stdo_bootstrap.md`, `spec_method.compressed.md`, `ticket_method.compressed.md`, `design_module_method.compressed.md`, `axiomatic_calculus.compressed.md`, `traversal_occurrence_profile.compressed.md`, `odd_method.compressed.md`, and `ux_method.compressed.md` were acquired; semantic comparison was bounded by the deciding source coverage above. For the 76,548-byte `stdo_compressed.md`, semantic inspection covered approximately lines 1-198, 216-271, 374-440, 884-1077 and 1142-1164, plus targeted heading/match scans. The remaining aggregate body is unassessed. The compression index (2,912 bytes) and ordinary entry (8,555 bytes) were also read.

UTC measurement began at **2026-10-14 10:48:17**. Assessment and normalization checks completed by **10:58:45**, an elapsed **628 seconds**. The subsequent report-preparation measurement at **11:01:10** gives **773 seconds** from start; final serialization follows that measurement. These timings and byte counts do not measure model tokens, total repeated transport, cost, user attention or production efficiency. Installed/common/instruction acquisition is additional and is not included in the candidate source-byte totals.

## Limits, residuals and re-entry

This was a fresh nonauthor review in the same model family and host environment as the parent workflow. It independently acquired the frozen source and did not inspect author reasoning or prior reviews, but it does not establish independent model-family, host, toolchain or administrative assurance. Parent-supplied subject/grant coordinates are trusted activation inputs. No independent reproduction of installed-v3 behavior, different-host use or paid model execution is claimed.

Unassessed scope includes the rest of the raw corpus and aggregate summary, complete formal/schema encodings, all possible dependency paths, all owner-specific domain cases, actual runtime/native-host invocation, actor attention/comprehension, practical interpretation-entry proof, downstream consumer impact, member acceptance and release qualification. A bounded documentary route check must not be promoted to any of these claims.

The overall fidelity result is `falsified` despite the satisfied narrow copy/digest checks. The two findings preserve their exact original subject D. A successor's repair or readback cannot retroactively alter this result; it requires its own exact subject. Changes to the subject bytes, source owners, frame selection/routes, governing installed/common basis, claimed task scope or assurance assumptions invalidate reuse beyond the matching coordinates. Actual use can reveal additional material dependencies not established by this review.

This result returns to the Executive for disposition. The apparent owning re-entry is the affected derived-summary generation under the unchanged governing owners, followed by whatever scoped independent review is separately admitted. No repair, acceptance, priority, next activation, or effect authority is conferred here.

## D2 scoped successor readback — I3-R2-VIEW-REPAIR-FREEZE-01

**Verdict: `satisfied`, only for the claim that D2 repairs F1 and F2 above.** The exact successor is `6bcc4126efd54c41e412affc29e3801dc9deeb5b`, acquired from `/Users/jim/src/apps/specification_methodology-codex`. The installed STDO v2.5.1-rc.2 and common B bindings remain those recorded above; this readback did not repeat the installed verification. The original D=`f2cb3e593757d094d008102551925e871a0204ff` result remains **`falsified`**. The successor result neither replaces that result nor extends its coverage.

The supplied readback grant selects only the two findings, their raw owners and the affected summaries. The applicable workspace/repository/v3 instructions were acquired. Raw owner passages were read before the repaired summary passages. All candidate acquisition used immutable `git show` objects; live changed candidate bytes, peer material, author rationale, oracle expectations and account data were not acquired. No candidate repair, Git mutation or subdelegation occurred. The only write is this appended result.

Here `D2:P/...:Lx-Ly` uses the same candidate prefix and immutable-source notation as the original report, with the successor commit above.

### F1 successor result: satisfied

D2:P/`standards/TRAVERSAL_OCCURRENCE_PROFILE.md:748-753,802-812` still allows all five core verdicts and still requires the specific `out_of_frame` diagnosis for an in-domain subject missing material scope or capability. The complete owner file is byte-identical to D.

D2:P/`standards/authority_compressions/traversal_occurrence_profile.compressed.md:83-89` now lists `satisfied`, `falsified`, `indeterminate`, `invalid_basis` and `out_of_frame`. It explicitly preserves `out_of_frame` and its cause for the missing-material-scope/capability case, distinguishes the outside-domain invocation boundary, and retains exact judgment evidence, stop, residual and re-entry law. Its source digest at `:5` matches the acquired owner.

The original counterexample—a valid in-domain `semantic_cut_admission` assessment lacking a required material relation or capability—is no longer excluded by the summary. It can retain `out_of_frame` and the owner's `hold` decision, `out_of_scope` stop and `unresolved_cause` residual; the owner's distinct `transition_evaluation` decision remains `indeterminate`. The repair does not create a second result algebra or turn unperformed evaluation into success. No new material or minor defect is established in this changed passage. Confidence is high from the explicit text and unchanged owner.

### F2 successor result: satisfied

D2:P/`standards/TICKET_METHOD.md:713-739` retains the ordinary carrier-lifetime partition and the particular explicit ticket-state instruction selecting durable recording. Its execution-admission separation remains at `:737-745`. The complete owner file is byte-identical to D.

D2:P/`standards/authority_compressions/stdo_compressed.md:383-389` now says an explicit instruction from ticket-state authority “may also select a durable record” and immediately preserves that the instruction neither admits an execution contract nor widens upstream work authority. Read with its ordinary selection rule at `:375-387`, this states the missing exception rather than making lifetime the sole possible basis for durability.

The original counterexample—authorized work ending this run, without independently surviving work state, accompanied by the competent ticket-state owner's explicit durable-record instruction—is now permitted by the summary. Mere ticket absence or a generic work request still supplies no such instruction, and durability still supplies no execution admission. No new material or minor defect is established in this changed passage. Confidence is high from the explicit exception and unchanged owner.

### Exact acquisition and limits

| Frozen D2 file under P | Complete bytes | SHA-256 | Semantically read lines and bytes |
| --- | ---: | --- | --- |
| `standards/TRAVERSAL_OCCURRENCE_PROFILE.md` | 80,238 | `94028abaa169bfe043e4bd047a19485bac60037ca4a22b9fc36ef26a1f793d7a` | 740-815; 6,326 bytes |
| `standards/TICKET_METHOD.md` | 71,236 | `d4c54b1cb2b49a3240ddd40adf68fd67d31d1712a0f294bafe2e852d7d8f6d3d` | 705-745; 3,191 bytes |
| `standards/authority_compressions/traversal_occurrence_profile.compressed.md` | 13,388 | `1c3861e2c49644eec28ff85e661b2e2b81902e6e2d6e3bf3e2b38403e54a2907` | 1-25 and 76-100; 2,348 bytes |
| `standards/authority_compressions/stdo_compressed.md` | 76,728 | `7ba1dab413b38338c915b539cf40620491905cfba7dd3bc521662d3160fd0cc9` | 1-35 and 375-405; 3,499 bytes |

The deciding-owner passages total **9,517 bytes**; inspected summary passages total **5,847 bytes**, for **15,364 bytes** of selected text. Complete D2 blobs total **241,590 bytes**, loaded for exact hashing and comparison. Full-blob acquisition is not full-body semantic review. The corresponding original blobs were acquired for comparison; repeated transport, instruction reads, report reads and the original blobs are not included in that D2 byte total. Comparison of each complete affected summary with D showed exactly its one repair hunk and no other changes within those two files. Both complete owner files compared equal. Frame selections were outside this readback and were not rechecked.

The original report's preserved preimage is **20,243 bytes**, SHA-256 `3f5746b24e0dc7b6ad1ab683c03c972f3b182836539d3e854fcca6ce92bbeefd`. The append was verified against that exact byte prefix.

Readback timing began at **2026-10-14 11:39:53 UTC**. Frozen acquisition and comparison completed by **11:40:37 UTC**; the assessment/result-preparation measurement was **11:41:07 UTC**, **74 seconds** after start. Final report serialization follows that measurement. Token usage, paid cost, repeated transport and production attention were not measured; no paid calls were made.

This is the same nonauthor Reviewer following up its own original findings, in the same model family and host context. It supplies no additional model-family, host or administrative independence and no independent runtime execution. The initial nine-summary/98-excerpt checks were not repeated or promoted to a new whole-candidate result. Other summaries, routes, source domains, practical entry, interpretation generation, installed-v3 behavior and downstream impact remain outside this readback.

The two documentary counterexamples are resolved on D2; Executive disposition remains separate. Reuse is limited to these exact summary/owner bytes, the inherited governing basis and this two-finding claim. A change to those coordinates or a wider claim requires its own evaluation. This `satisfied` result supplies no whole-candidate acceptance, member acceptance, installed-v3 qualification, release decision or effect grant.
