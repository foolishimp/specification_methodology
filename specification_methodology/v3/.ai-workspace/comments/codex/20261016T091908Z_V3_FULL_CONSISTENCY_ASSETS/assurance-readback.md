# Additional readback: diagnosis before a selected rerun

Result: `satisfied` for this additional consistency question. No supported source defect is filed. The exact wording does not require a completed repair before every subsequent selected run, and its governing consumers explicitly permit evidence acquisition and bounded diagnostic continuation. A possible overstrict reading is recorded below as a clarity concern, not promoted to an inconsistency.

Subject remains `a3c43335e6d50bb7d6dd247c90de99e7404e1d1a` under the verified STDO 2.5.1-rc.2 basis from `assurance-review.md`. This follow-up was requested after that report closed. Its only new write grant is this note. The original report and expectations are preserved byte-identically. No other review report, tenant body, source edit, Git effect or execution trial is involved.

Paths and lines below are relative to `specification_methodology/v3/` at that frozen subject.

## Exact sentence and the two readings

`specification/requirements/ASSURANCE.md:121` ends:

> Failures feed causal diagnosis and repair before another selected run.

The grammatical action governed by “before” is “feed”: failures inform diagnosis and repair work before the next selected run. The sentence does not say “all failures are repaired”, “repair completes”, or “a successful repair is established” before the next run. Starting or informing a diagnosis/repair process is different from completing the resulting repair.

An overstrict reading expands this into: “After any test failure, a repair must be completed before any other selected execution, including an experiment needed to diagnose the failure.” That expansion adds a completion gate and a universal restriction on execution that the sentence does not state. It would also suppress the explicit evidence-acquisition branch in the governing construction contract.

The opposite weak reading would let an actor ignore the failure, rerun until it sees a pass, and treat the pass as disposal. The source does not permit that either. Feeding the failed evidence into diagnosis is consequential: the next action needs a supported purpose, authority and adequate observation/assurance basis, and the earlier failure or uncertainty keeps its standing until a supported disposition.

## Concrete counterexample to the overstrict reading

A frozen candidate fails a test. Three explanations remain live: a defect in the candidate, an incorrect expected answer, or a transient environmental disturbance. The work authority authorises one safe diagnostic rerun under fixed limits, preserving the failing run and its exact inputs. The rerun acquires a material observation needed to distinguish those explanations; it makes no qualification or repair-success claim.

No justified repair can yet be selected. A completed-repair-before-any-run gate would therefore prevent the very observation needed for causal diagnosis, or pressure the actor to change code or expectations without a supported cause. That would contradict the following deciding clauses:

- `specification/PRODUCT.md:76`: diagnosis determines whether to repair the realisation, acquire evidence or revise the governing model through its owner. Evidence acquisition is an explicit alternative to repair.
- `specification/requirements/README.md:110`: diagnosis preserves unresolved alternatives and routes each *supported* repair to its affected owner rather than deriving a repair from an intake label.
- `specification/requirements/README.md:112`: continuation may reduce uncertainty or test a bounded hypothesis; failure is handled through the applicable continuation, repair, recovery, re-entry, yield or stop. Repair is one possible response, not the mandatory response to every failed observation.
- `specification/conformance/README.md:76`: the consuming discriminator expressly requires correcting the supported affected relation **or acquiring evidence while retaining unresolved alternatives**.
- `specification/conformance/README.md:92`: insufficient observations require distinguishing evidence, justified narrowing or an indeterminate judgment. It does not require prior repair of the still-unknown cause.
- `specification/conformance/README.md:115`: integrated construction is evaluated through observation, diagnosis and lawful continuation or closure.

The diagnostic rerun can satisfy the exact sentence: its failed predecessor is retained and used to initiate diagnosis, assess the repair question, and select the next bounded observation. The unresolved repair question need not be falsely recorded as a completed repair. This interpretation uses the explicit governing alternatives rather than adding an unwritten exception.

It also applies when the observed output is certainly wrong but its cause is unknown. A known failure of a predicate is not itself a supported choice of which implementation, oracle or environmental relation to repair.

## The retained constraints

The rerun is not automatically lawful merely because it is called diagnostic:

- Its evidence needs a declared claim and supported observation binding. `ASSURANCE.md:47` keeps a reported failure at observational standing where oracle fidelity is unestablished, just as it does for an observed pass.
- The selected action must respect the risk, obligations, resource limits and authority in `ASSURANCE.md:74` and 95. Unknown effects must be resolved sufficiently for the next dependent action under `requirements/README.md:97` and 111. The hypothetical supplies safe effects and an existing grant; the sentence supplies neither.
- Failed and indeterminate results retain their standing under `ASSURANCE.md:109`. Line 115 preserves failures and citations until supported **repair, reassessment or authorised change of obligation** disposes them. That disjunction is direct evidence within the same owner that completed repair is not the sole possible next path.
- A later pass does not erase the earlier counterexample or establish a completed repair by itself. The applicability, observation and coverage obligations still decide what the new result supports.

## Disposition and limits

No required semantic correction follows from this counterexample. A reader might initially paraphrase “feed diagnosis and repair before another run” as a repair-first workflow. That is a local wording risk; the exact verb and the explicit governing alternatives resolve it without changing permitted work. If the coordinator chooses a clarity edit, its narrow purpose would be to make this existing distinction explicit at `ASSURANCE.md:121`, not introduce a new retry policy or weaken retention of failures. This readback supplies no source wording or acceptance of a future amendment.

The prior report's result and scope remain unchanged; this note records an additional tested case, not a retrospective claim that the original report explicitly covered the sentence. Findings, severity and correction owner are `not_applicable` for this readback. The case is reasoned source review, not evidence that a tenant implements lawful diagnostic reruns.

Reacquisition used frozen `git show` for ASSURANCE 39–47, 72–95 and 97–131; requirements index 97–118; Product 66–82; and the relevant conformance consumers at 74–82, 90–101 and 115–119. No source change or new basis was observed. Native spend and full host context remain uninstrumented; this note makes no context-fit or efficiency claim.

Preserved prior artifact identities:

- `assurance-expectations.md`: `d986848506074dbbc978abb908c4c59a8ff649e1cfd68654234648a2e93efadd`.
- `assurance-review.md`: `48a38a0b3abd098d9b9315c00c0972c4466740145f19a9c305c82748eb5aabbc`.
