**Provisional source review findings — before final freeze**

F01 · S3 · proof declaration boundaries and named instance coverage.

At `build_tenants/common-tools/proof_reader.py:105` and the source-catalog command loop near line 155, the named-declaration pattern omits `instance`, and instance commands do not end a preceding declaration. The exact eight selected Lean sources therefore produce `AC.Witness` at lines 30–44 of `AC/Closure.lean`; its displayed statement includes the separately authored `instance witnessDecidable` header at line 34. That named instance has no catalog entry. `AC.Closed` (19–24) and `AC.CertificateValid` (45–52) also absorb following anonymous instances and acquire their lexical occurrences.

This is a PR-02/PR-04 source-navigation metadata defect. It changes neither original Lean bytes nor the historical kernel result. The full source remains available. The bounded repair is to recognize named instances and make all instance commands terminate the preceding declaration; anonymous instances may remain source-only if that inventory boundary is explicit. Add exact-profile range/reference controls rather than broadening to a general Lean parser.

The finding was sent promptly to Root and the proof-reader Writer. No candidate repair was made by the Reviewer. Status: open while Writer is repairing; final freeze and successor assessment are pending.

Observed source SHA-256: `2cb68e4acc1bc3e952404a3deeb2a9f6a8f3c1787e0c76caf1fda9a071be1438`.

**Successor assessment — discharged.** On the Writer's frozen generator `37a74b721347635ddfdf1032cbed124c97c46aabbfd5f4fd919aca19f9cdf457`, the Reviewer independently replayed the exact produced eleven-member payload, page SHA-256 `f7729208c0396473389a0322039d3b724ef2a1c006a56885ab916b0e3c5f4418`. `AC.Closed` is 19–20, `AC.Witness` is 30–32, named `AC.witnessDecidable` is an Instance at 34–41, and `AC.CertificateValid` is 45–47. Each occurrence is inside its own declaration range. All 484 catalog entries have bounded source coordinates and resolvable local reference targets. All eight sources remain byte-identical to their retained originals and historical report hashes. The independent actual-page DOM probe also exercised each corrected entry, all four curated questions and thirteen linked declarations, source navigation, Back/trail, all kind/module filters, exact full text and report, and no-network controls. F01 is closed for this frozen proof-reader successor; installed integration and the final overall review remain separate.

Observed catalog excerpt:

```json
{
  "named_instance_present": false,
  "Witness": {
    "id": "AC.Witness",
    "name": "Witness",
    "kind": "Definition",
    "file": "AC/Closure.lean",
    "start_line": 30,
    "namespace": "AC",
    "end_line": 44,
    "statement": "def Witness (d : Dependencies) (known : Finset Nat) : List Nat \u2192 Prop\n  | [] => True\n  | x :: rest => (\u2203 parent \u2208 known, x \u2208 d parent) \u2227 Witness d (insert x known) rest\n\ninstance witnessDecidable (d : Dependencies) (known : Finset Nat) (trace : List Nat) :\n    Decidable (Witness d known trace)",
    "references": [
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 30
      },
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 34
      }
    ]
  },
  "Closed": {
    "id": "AC.Closed",
    "name": "Closed",
    "kind": "Definition",
    "file": "AC/Closure.lean",
    "start_line": 19,
    "namespace": "AC",
    "end_line": 24,
    "statement": "def Closed (d : Dependencies) (s : Finset Nat) : Prop",
    "references": [
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 19
      },
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 22
      }
    ]
  },
  "CertificateValid": {
    "id": "AC.CertificateValid",
    "name": "CertificateValid",
    "kind": "Definition",
    "file": "AC/Closure.lean",
    "start_line": 45,
    "namespace": "AC",
    "end_line": 52,
    "statement": "def CertificateValid (d : Dependencies) (universeKeys seeds : Finset Nat) (trace : List Nat) : Prop",
    "references": [
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 45
      },
      {
        "target": "AC.traceSet",
        "token": "traceSet",
        "line": 46
      },
      {
        "target": "AC.Witness",
        "token": "Witness",
        "line": 47
      },
      {
        "target": "AC.Closed",
        "token": "Closed",
        "line": 47
      },
      {
        "target": "AC.traceSet",
        "token": "traceSet",
        "line": 47
      },
      {
        "target": "AC.Dependencies",
        "token": "Dependencies",
        "line": 49
      }
    ]
  }
}
```

**F02 · S3 · extracted Codex current-route check is not closed by the 190-member archive.**

The first actual installed-tooling qualification reached the extracted Codex package check and refused at `verify_package.py:71`: missing `stdo_skills/.ai-workspace/tickets/active/T-003-project-representation.md`. This is a currently selected source route, pinned to `9ae14567a5886e550524b3fd963bf71edb247900e2229e5f47875e1ac0c4bb7e`. The initial source selection deliberately omitted all work records. The failed operation is preserved in `tooling-integration-001/installed-tooling.log`; preceding representation and code-overlay public operations reached the package check, but the overall qualification did not complete. This observation came from the Writer's actual consumer-path log, independently checked against the current route checker and selected archive membership, rather than a claimed independent rerun of the entire first attempt.

This affects TOOL-03/TOOL-05 and the guide's runnable source-package-check claim when `--repository` nominates the extracted tree. The existing portable checker can instead report external verification `not_performed`; that must not be called checked current sources. A bounded selected documentary dependency may close the route without admitting arbitrary work records or making them executable dependencies. Sent to Root and Writer before final freeze. Status: successor pending.

**F03 · S2 · filesystem case aliases bypass protected-release overlap refusal.**

At `build_tenants/common-tools/tooling_materialize.py:144–146`, observed SHA-256 `bcaaac95920da015b59acb6c94c471a5a7a43ae9655307da669ead6d2ba0af02`, protection uses the caller's lexical spelling, first to identify a `standards` parent and then through `Path.is_relative_to`. `ordinary_path` excludes symlinks but retains case spelling. On this actual case-insensitive filesystem the Reviewer independently reproduced both failures with copied 191-member bundles inside temporary directories beneath this review directory:

1. Actual bundle `<temp>/Release/standards/tooling`, destination `<temp>/release/review-should-refuse`. `release.exists()` is true; the path denotes `Release`, but lexical overlap comparison is false. `materialize` returned `status: materialized`, `source_files: 191`; the newly extracted tree existed beneath the actual protected release.
2. Actual bundle `<temp>/release/standards/tooling`, invoked through alias `<temp>/release/STANDARDS/tooling`, ordinary destination `<temp>/release/review-should-refuse`. The case-sensitive parent-name test selected only the tooling directory as protected. Again `materialize` succeeded inside the actual release.

These are TOOL-02/TOOL-04 failures, affecting the explicit promise to refuse extraction beneath the immutable installation. Both copied fixtures were cleaned; no real installed release was changed. Reported promptly to Root and Writer. The bounded repair must compare physical identity of existing ancestors and recognize the protected installed root through aliases before creating output, retaining traversal and symlink refusal. Status: successor pending.

**Final successor closure for F02 and F03.** Both are discharged on the final technical freeze `1b65cf946b15d2c500080e3f39d4cd0f2a74f42f6c98997d56e74065690fc5c8`. The 191-file archive binds the sole public T-003 record exception to the exact selected Git blob and SHA-256 above. Independent extracted Codex `--repository` execution checks all thirteen current routes. Materializer `1618537d414f195a08bbbe8cd0148b265158574e0fe31a985eb2799cfe21ad4e` refuses both original physical-alias reproductions before output with unchanged copied-release bytes. The final actual installed public-path replay also refuses both aliases, completes all thirty expected operations and leaves installation/source copies unchanged. See [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md), [consumer-replay.json](consumer-replay.json) and [negative-controls.json](negative-controls.json) for the closed result and scope.
