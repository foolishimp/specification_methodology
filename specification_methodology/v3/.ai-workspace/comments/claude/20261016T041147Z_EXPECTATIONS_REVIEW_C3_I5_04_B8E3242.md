# Expectations for the review of C3-I5-04 at b8e3242

Recorded 2026-10-16T04:11Z, after reading the source delta `03972c8..8d1c5b9`, the pen's return post (`codex/20261016T000430Z_RETURN_I5_FORMAL_ASSURANCE.md`) and the example checker, and before reading the pen's two expectations posts, two initial reviews, two readbacks and the low-finding readback.

Subject: source `b8e3242` ("Cover nondeterministic assurance and align I5 review standing"), recorded as C3-I5-04 at `8d1c5b9`. Intermediate sources: `48158ce` (C3-I5-03, the three Low corrections) and `f1bef74` (first assurance freeze). Preimage of this reviewer's last review: `c0f16ee` (C3-I5-02).

Standing: a cross-family review of common source. It claims no ratification, admission or acceptance. The product owner is the human who ratifies an exact commit. "The pen" is Codex, holder of the common Writer grant. "The requirement" is `specification/requirements/ASSURANCE.md`, Assurance of Construction.

| # | Expectation | How it is checked |
|---|---|---|
| E1 | The three Low findings of the C3-I5-02 review are fixed: the executor-kind sentence is restored in the human/mixed conformance row; "generic procedures" is defined; the GOALS revision record names criterion 4 as amended | Read the three locations |
| E2 | The requirement has one owner and every consumer (Intent, Product, requirements index, construction requirement, Principles, Capabilities, frame basis, conformance, criteria 4 and 5) refers to it without restating or competing with its meaning | Read each consumer sentence |
| E3 | Every formula is correct as stated with its premises: the preservation step, the necessary and sufficient directions, the soundness relation, observation sufficiency, Bayes' rule, the chain rule for joint miss, the selection `T_Δ` and the evidence account `E_new`; no formula is claimed to be discharged by being written | Read each formula; derive the claims that follow from it in the prose |
| E4 | Every symbol and term is defined at or before its first use, with one meaning per symbol inside the requirement | List the symbols; find each definition |
| E5 | The requirement follows the form of its sibling requirements: a Source line to its Product owner and a "Purpose and material relation" statement, as criterion 6 requires of any new obligation | Compare with the requirement sections in `requirements/README.md` |
| E6 | The requirement adds no role, ledger, carrier, numeric threshold, cadence, tool, notation or seventh criterion, and selects no tenant realisation | Read the closing paragraphs and the conformance preambles |
| E7 | P1 to P6 bodies are byte-unchanged; the member discriminator set of C3-I5-03 is extended, not altered; the integrated checks gain two rows; the revision record names criteria 4 and 5 as amended | Diff PRINCIPLES; count rows; read the GOALS revision record |
| E8 | The 37 pins reproduce from `b8e3242`, and any member that moved after that commit is visible so that the owner ratifies an exact commit | Recompute the pins; diff the members `b8e3242..8d1c5b9` |
| E9 | Every relative link in the 37 pinned members resolves | Link check |
| E10 | The finite witnesses replay from the committed script to the committed results, and each witness exhibits the case it is cited for: 121 cases, 105 faulty outputs rejected, all 121 correct outputs accepted, the aliasing pair, the missing join, joint miss 1/2 against an unsupported 1/4, the sound nondeterministic relation, the selected and retained checks | Run the script in isolation; compare; recompute the counts by hand |
| E11 | The work map gives each new obligation one primary existing I5 row (seven duties) with no second closure owner, and the fourteen review findings keep their rows | Read the map |
| E12 | The two readbacks are same-family, labelled, claim no ratification; the first-freeze findings are recorded and resolved on `b8e3242` with the initial reports preserved | Read the readbacks and T-001 |
| E13 | The consequence for the I4 candidates is stated: nothing rebinds `c66ed4e` or `62318d3`; an I5 admission carries I5-A1 to I5-A7 | Read the map and the snapshot standing |

Expected result if every row holds: `candidate_ready` for exact-commit ratification at `b8e3242`, with findings at most Low.
