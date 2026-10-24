"""Synthetic mechanics controls. No native cut, actor call or semantic receipt is created."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import json
import shutil
import sys
import tarfile
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(APP))
sys.path.insert(0, str(APP / "release_tools"))
import application_contract as c
import bundle_check as checks
import public_receipts as receipts
import package_release as package
import freeze_sources as freeze
import run_generation as runner
import checkpoint_files


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n")


def synthetic_source(root):
    """Small independently named SIMULATION, with an added semantic annex."""
    shutil.copyfile(APP / "application.json", root / "application.json")
    shutil.copytree(APP / "implementation", root / "implementation")
    owner = b"# Fixture owner\n\nThis is synthetic source for mechanical tests only.\n"
    frame = b"# Fixture frame\n\nThis is a synthetic derived frame.\n"
    frame_inputs = {"frames": [{"path": "standards/frames/fixture.md", "bytes": len(frame), "sha256": c.sha(frame),
        "routes": [{"owner": "standards/ACTIVATION.md", "owner_sha256": c.sha(owner), "anchor": "fixture-owner", "section_sha256": c.sha(owner)}]}]}
    contents = {"standards/ACTIVATION.md": owner, "standards/CONFORMANCE_ANNEX.md": b"# Fixture annex\n\nAdditional synthetic source.\n",
                "standards/examples/deterministic_contracts.py": b"# SIMULATION: semantic code companion\ndef double(n):\n    return n * 2\n",
                "standards/frames/fixture.md": frame, "standards/frames/FRAME_INPUTS.json": c.canonical(frame_inputs), "LICENSE": b"Synthetic license marker.\n"}
    rows = []
    for name, raw in sorted(contents.items()):
        target = root / "source" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        rows.append({"path": name, "bytes": len(raw), "sha256": c.sha(raw), "git_mode": "100644",
                     "git_blob": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()})
    selection = {"kind": "a_c.stdo301.native-source-selection/1", "subject_uri": "urn:fixture:simulation:stdo301",
        "native": {"commit": "1" * 40, "package_path": "native", "package_tree": "2" * 40, "cut": "v3.0.1-rc.1",
                   "qualified_ref": "refs/tags/specification_methodology/v3.0.1-rc.1", "tag_object": "3" * 40, "manifest_sha256": "4" * 64},
        "source_candidate": {"commit": "5" * 40, "package_path": "candidate", "package_tree": "6" * 40},
        "files": rows, "file_count": len(rows), "total_bytes": sum(row["bytes"] for row in rows),
        "inventory_sha256": c.digest(c.inventory_rows(rows)), "standing": "test_candidate_not_accepted"}
    source = {"commit": "1" * 40, "payload_commit": "5" * 40, "package_root": "native", "package_tree": "2" * 40,
              "qualified_ref": selection["native"]["qualified_ref"], "tag_object": "3" * 40, "native_manifest_sha256": "4" * 64}
    common = {"subject_id": selection["subject_uri"], "source": source}
    primary = [row for row in rows if c.selection_class(row["path"]) == "primary_semantic"]
    write(root / "source-selection.json", selection)
    write(root / "package-custody.json", {**common, "members": rows, "member_count": len(rows), "bytes": selection["total_bytes"], "inventory_digest": selection["inventory_sha256"]})
    write(root / "source-manifest.json", {**common, "files": primary, "member_count": len(primary), "bytes": sum(row["bytes"] for row in primary), "inventory_digest": c.digest(c.inventory_rows(primary))})
    classes = {}
    for group in ("primary_semantic", "derived_frames", "host_legal_release_metadata"):
        selected = [row for row in rows if c.selection_class(row["path"]) == group]
        classes[group] = {"paths": [row["path"] for row in selected], "member_count": len(selected), "bytes": sum(row["bytes"] for row in selected)}
    write(root / "source-classification.json", {**common, "classes": classes, "derived_frame_sources": frame_inputs})
    app = c.application(root)
    sections, count = freeze.source_sections(root, primary, contents, selection["subject_uri"], app["generation"])
    write(root / "release_tools/source-sections.json", {"sections": sections})
    (root / "SOURCE-READINESS.md").write_text(freeze.readiness(app, selection, primary))
    contract = {"kind": "a_c.stdo301.frozen-source/1", "subject_id": selection["subject_uri"], "source": source,
        "artifact": app["artifact"], "builder": app["builder"], "generation": app["generation"],
        "application_sha256": c.sha((root / "application.json").read_bytes()),
        "implementation_manifest_sha256": c.sha((root / "implementation/manifest.json").read_bytes()),
        "section_count": len(sections), "chunk_count": count, "metadata_sha256": {}}
    for name in ("source-selection.json", "package-custody.json", "source-manifest.json", "source-classification.json", "release_tools/source-sections.json", "SOURCE-READINESS.md"):
        contract["metadata_sha256"][name] = c.sha((root / name).read_bytes())
    write(root / "source-contract.json", contract)
    return contract


class TemporaryFixture(unittest.TestCase):
    def setUp(self):
        (APP / "test_env/.tmp").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="synthetic-", dir=APP / "test_env/.tmp")
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def source(self):
        return synthetic_source(self.root)

    def reseal(self, name):
        contract = c.load(self.root / "source-contract.json")
        contract["metadata_sha256"][name] = c.sha((self.root / name).read_bytes())
        write(self.root / "source-contract.json", contract)


class ApplicationTests(TemporaryFixture):
    def test_exact_snapshot_unchanged(self):
        self.assertEqual(len(c.implementation(APP)["files"]), 11)

    def test_freeze_missing_selection_refuses_before_source_effects(self):
        shutil.copyfile(APP / "application.json", self.root / "application.json")
        shutil.copytree(APP / "implementation", self.root / "implementation")
        selection = self.root / "bad-selection.json"; write(selection, {})
        with self.assertRaisesRegex(ValueError, "digest"):
            freeze.freeze(self.root, self.root, selection, "9" * 64)
        self.assertFalse((self.root / "source").exists())
        self.assertFalse((self.root / "source-contract.json").exists())

    def test_dynamic_extent_and_added_annex(self):
        self.source()
        result = c.check_sources(self.root)
        self.assertEqual((result["files"], result["semantic_files"], result["frame_owner_bindings"]), (6, 3, 1))
        self.assertIn("standards/examples/deterministic_contracts.py", [row["path"] for row in c.load(self.root / "source-manifest.json")["files"]])
        self.assertEqual(len(checks.check_sections(self.root)), c.load(self.root / "source-contract.json")["section_count"])

    def test_source_bytes_and_extra_members_refuse(self):
        self.source()
        path = self.root / "source/standards/ACTIVATION.md"
        original = path.read_bytes(); path.write_bytes(original + b"tamper")
        with self.assertRaisesRegex(ValueError, "source bytes"):
            c.check_sources(self.root)
        path.write_bytes(original)
        (self.root / "source/extra.md").write_text("extra")
        with self.assertRaisesRegex(ValueError, "inventory"):
            c.check_sources(self.root)

    def test_source_symlink_refuses(self):
        self.source()
        p = self.root / "source/standards/ACTIVATION.md"; p.unlink(); p.symlink_to(self.root / "application.json")
        with self.assertRaisesRegex(ValueError, "redirected"):
            c.check_sources(self.root)

    def test_source_coordinate_duplicates_refuse_after_metadata_refresh(self):
        self.source()
        custody = c.load(self.root / "package-custody.json"); custody["source"]["commit"] = "7" * 40
        write(self.root / "package-custody.json", custody); self.reseal("package-custody.json")
        with self.assertRaisesRegex(ValueError, "coordinate"):
            c.check_sources(self.root)

    def test_root_contract_pin_refuses_resealing(self):
        self.source()
        pin = c.sha((self.root / "source-contract.json").read_bytes())
        value = c.load(self.root / "source-contract.json"); value["chunk_count"] += 1
        write(self.root / "source-contract.json", value)
        with self.assertRaisesRegex(ValueError, "digest differs"):
            c.check_sources(self.root, pin)

    def test_section_line_and_identity_checks(self):
        self.source()
        path = self.root / "release_tools/source-sections.json"
        value = c.load(path); value["sections"][0]["start_line"] = 0
        write(path, value); self.reseal("release_tools/source-sections.json")
        with self.assertRaisesRegex(ValueError, "line range"):
            checks.check_sections(self.root)

    def test_native_tag_must_be_annotated(self):
        self.source(); selection = c.load(self.root / "source-selection.json")
        with patch.object(freeze, "git", side_effect=[b"3" * 40 + b"\n", b"commit\n"]):
            with self.assertRaisesRegex(ValueError, "annotated"):
                freeze.verify_selection(self.root, selection)

    def test_python_parser_absence_refuses_before_run_outputs(self):
        self.source()
        with patch.object(runner, "ROOT", self.root), patch.object(runner, "RUN", self.root / "run"), patch.object(runner.importlib.util, "find_spec", return_value=None):
            with self.assertRaisesRegex(ValueError, "Python semantic source"):
                runner.prepare(self.root / "unused-upstream")
        self.assertFalse((self.root / "run").exists())

    def test_stale_frame_owner_refuses_in_preflight(self):
        self.source()
        rows = c.load(self.root / "package-custody.json")["members"]
        frames = c.load(self.root / "source/standards/frames/FRAME_INPUTS.json")
        frames["frames"][0]["routes"][0]["owner_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "owner binding"):
            c.check_frame_routes(rows, frames)

    def test_readiness_is_portable_exact_and_idempotent(self):
        self.source(); raw = (self.root / "SOURCE-READINESS.md").read_bytes()
        with patch.object(package, "ROOT", self.root):
            self.assertEqual(package.source_readiness_projection(raw).encode(), raw)
            self.assertEqual(package.source_readiness_projection(raw).encode(), raw)
            for changed in (raw + b"changed", b"projected: true\n"):
                with self.assertRaisesRegex(ValueError, "readiness"):
                    package.source_readiness_projection(changed)
        self.assertIn(b"v3.0.0-rc.1", raw)
        self.assertNotIn(b"35fb4824", raw)

    def test_failure_continuation_needs_exact_acknowledgment(self):
        current = {"non_strict_originals": [{"latest_author": "actors/author/a/attempt-001", "result_sha256": "a" * 64}]}
        with self.assertRaisesRegex(ValueError, "failure stop"):
            runner.require_acknowledged_failures({}, current)
        runner.require_acknowledged_failures({"acknowledged_failures": {"actors/author/a/attempt-001": "a" * 64}}, current)
        current["non_strict_originals"][0]["result_sha256"] = None
        with self.assertRaisesRegex(ValueError, "unfinished"):
            runner.require_acknowledged_failures({}, current)

    def test_grant_digest_and_operation_bind_source(self):
        self.source()
        path = self.root / "grant.json"
        value = {"kind": "a_c.stdo301.generation-grant/1", "grant_id": "SIMULATION", "issuer": "/root",
                 "source_contract_sha256": c.sha((self.root / "source-contract.json").read_bytes()),
                 "scheduler_sha256": c.sha(Path(runner.__file__).read_bytes()), "operations": ["prepare"], "max_new_calls": 0}
        write(path, value); pin = c.sha(path.read_bytes())
        with patch.object(runner, "ROOT", self.root):
            self.assertEqual(runner.grant(path, pin, "prepare"), value)
            with self.assertRaisesRegex(ValueError, "operation"):
                runner.grant(path, pin, "initial-batch")
            with self.assertRaisesRegex(ValueError, "digest"):
                runner.grant(path, "0" * 64, "prepare")

    def test_call_budget_and_shared_reservation_cap(self):
        private = self.root / "private"; private.mkdir()
        with patch.object(runner, "PRIVATE", private), patch.object(runner, "RUN", self.root):
            grant = {"max_new_calls": 3, "grant_id": "SIMULATION", "source_contract_sha256": "c" * 64}
            for n in range(3):
                folder = runner.reserve(grant, "a" * 64, "initial-batch" if n == 0 else "repair-batch", [{"chunk": "fixture", "family": "author" if n == 0 else "repair"}])
                (self.root / c.load(folder / "plan.json")["selections"][0]["attempt"]).mkdir(parents=True)
                write(folder / "result.json", {"state": "batch_complete"})
            with self.assertRaisesRegex(ValueError, "three-call"):
                runner.reserve({**grant, "max_new_calls": 100}, "b" * 64, "retry-batch", [{"chunk": "fixture"}])
            with self.assertRaisesRegex(ValueError, "call budget"):
                runner.reserve(grant, "a" * 64, "remaining-batch", [{"chunk": "other"}])

    def test_unfinished_and_exception_batches_stop(self):
        private = self.root / "private"; private.mkdir()
        grant = {"max_new_calls": 5, "grant_id": "SIMULATION", "source_contract_sha256": "c" * 64}
        with patch.object(runner, "PRIVATE", private):
            folder = runner.reserve(grant, "a" * 64, "initial-batch", [{"chunk": "a"}])
            with self.assertRaisesRegex(ValueError, "unfinished"):
                runner.reserve(grant, "a" * 64, "remaining-batch", [{"chunk": "b"}])
            write(folder / "result.json", {"state": "exception_stop"})
            with self.assertRaisesRegex(ValueError, "exception stop"):
                runner.reserve(grant, "a" * 64, "remaining-batch", [{"chunk": "b"}])

    def test_actual_counter_reader_retains_failures_and_refuses_tampering(self):
        attempt = self.root / "actors/author/fixture/attempt-001"; attempt.mkdir(parents=True)
        usage = {"input_tokens": 7, "output_tokens": 3}
        events = json.dumps({"type": "turn.completed", "usage": usage}) + "\n"
        (attempt / "events.jsonl").write_text(events); (attempt / "stderr.txt").write_bytes(b"")
        result = {"events_sha256": c.sha(events.encode()), "stderr_sha256": c.sha(b""), "usage_events": [usage],
                  "failures": ["process_timeout"], "status": "failed", "elapsed_seconds": 0.1,
                  "cli_version": "SIMULATION", "settings": {"model": "SIMULATION"}, "answer_sha256": None}
        write(attempt / "result.json", result); write(attempt / "usage.json", {"usage_events": [usage]})
        calls = {"fixture": [{"family": "author", "attempt": "actors/author/fixture/attempt-001", "invocation_recorded": True}]}
        with patch.object(runner, "RUN", self.root), patch.object(runner, "checkpoint", return_value=({"subject_id": "urn:fixture:simulation"}, [{"id": "fixture"}])), patch.object(runner, "inventory", return_value=calls):
            report = runner.accounting()
            self.assertEqual(report["attempts"][0]["status"], "failed")
            self.assertEqual(report["reported_scalar_counter_totals"], usage)
            (attempt / "stderr.txt").write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "events/stderr changed"):
                runner.accounting()

    def test_dispatch_exception_before_actor_directory_retains_reservation(self):
        run = self.root / "run"; run.mkdir()
        private = self.root / "private"; private.mkdir()
        chunk = {"id": "fixture"}
        plan = {"subject_id": "urn:fixture:simulation"}
        grant = {"max_new_calls": 3, "grant_id": "SIMULATION", "source_contract_sha256": "c" * 64}
        metadata = {"settings": {"model": "SIMULATION"}, "cli_version": "SIMULATION"}
        with patch.object(runner, "RUN", run), patch.object(runner, "PRIVATE", private), \
             patch.object(runner, "checkpoint", return_value=(plan, [chunk])), \
             patch.object(runner, "actor_preflight", return_value=(metadata, {})), \
             patch.object(runner.g, "author_prompt", return_value="SIMULATION"), \
             patch.object(runner.g, "run_actor", side_effect=RuntimeError("SIMULATION before actor directory")) as actor:
            with self.assertRaisesRegex(RuntimeError, "before actor directory"):
                runner.author_batch("initial-batch", grant, "a" * 64, "SIMULATION", [])
            actor.assert_called_once()
            self.assertFalse((run / "actors").exists())
            current, account = runner.status(), runner.accounting()
            self.assertEqual(current["state"], "failure_stop")
            self.assertEqual(current["never_attempted"], [])
            self.assertEqual(current["calls_including_reservations"], 1)
            self.assertEqual(account["calls_including_reservations"], 1)
            self.assertEqual(account["actual_invocations_recorded"], 0)
            self.assertFalse(account["complete_attempt_account"])
            self.assertEqual(account["attempts"][0]["status"], "unknown_reservation_handoff")
            result_path = private / "batches/batch-001/result.json"
            before = result_path.read_bytes()
            self.assertEqual(c.load(result_path)["state"], "exception_stop")
            reconciled = {**grant, "reconciled_batches": {"batch-001": c.sha(before)}}
            runner.require_acknowledged_failures(reconciled, current)
            # Acknowledgment never reassigns the old missing handoff to a later call.
            with self.assertRaisesRegex(ValueError, "handoff cannot be reused"):
                runner.reserve(reconciled, "b" * 64, "retry-batch", [{"chunk": "fixture", "family": "author"}])
            self.assertEqual(result_path.read_bytes(), before)
            self.assertEqual(runner.accounting(), account)

    def test_scheduler_and_actual_author_repair_attempts_join_without_double_count(self):
        run = self.root / "run"; run.mkdir()
        private = self.root / "private"; private.mkdir()
        chunks = [{"id": family} for family in ("author", "repair")]
        grant = {"max_new_calls": 3, "grant_id": "SIMULATION", "source_contract_sha256": "c" * 64}
        with patch.object(runner, "RUN", run), patch.object(runner, "PRIVATE", private), \
             patch.object(runner, "checkpoint", return_value=({"subject_id": "urn:fixture:simulation"}, chunks)):
            for family in ("author", "repair"):
                folder = runner.reserve(grant, "a" * 64, "SIMULATION", [{"chunk": family, "family": family}])
                selection = c.load(folder / "plan.json")["selections"][0]
                attempt = run / selection["attempt"]
                actor = attempt if family == "author" else attempt / "actor"
                actor.mkdir(parents=True)
                write(actor / "invocation.json", {"simulation": True})
                usage = {"input_tokens": 7, "output_tokens": 3}
                events = json.dumps({"type": "turn.completed", "usage": usage}) + "\n"
                (actor / "events.jsonl").write_text(events); (actor / "stderr.txt").write_bytes(b"")
                write(actor / "result.json", {"events_sha256": c.sha(events.encode()), "stderr_sha256": c.sha(b""),
                    "usage_events": [usage], "failures": ["process_timeout"], "status": "failed", "elapsed_seconds": 0.1,
                    "cli_version": "SIMULATION", "settings": {"model": "SIMULATION"}, "answer_sha256": None})
                write(actor / "usage.json", {"usage_events": [usage]})
                self.assertFalse(runner.accounting()["complete_attempt_account"])
                write(folder / "result.json", {"state": "failure_stop"})
            account = runner.accounting()
            self.assertEqual(account["calls_including_reservations"], 2)
            self.assertEqual(account["actual_invocations_recorded"], 2)
            self.assertEqual(account["reported_scalar_counter_totals"], {"input_tokens": 14, "output_tokens": 6})
            self.assertTrue(account["complete_attempt_account"])
            self.assertTrue(all(row["reservation"]["state"] == "failure_stop" for row in account["attempts"]))

    def test_original_grounding_failure_is_retained_without_relabeling(self):
        chunk = {"id": "fixture"}
        def fake_actor(prompt, schema, attempt, codex, timeout, settings):
            self.assertEqual(timeout, 1800)
            attempt.mkdir(parents=True)
            write(attempt / "answer.json", {})
            result = {"status": "completed", "failures": [], "elapsed_seconds": 0.1, "usage_events": [{"input_tokens": 1}]}
            write(attempt / "result.json", result)
            return result
        with patch.object(runner, "RUN", self.root), patch.object(runner.g, "author_prompt", return_value="SIMULATION"), patch.object(runner.g, "run_actor", side_effect=fake_actor), patch.object(runner.g, "author_check", side_effect=runner.g.GenerationError("synthetic invalid locator")), patch.object(runner.g, "actor_evidence") as evidence:
            result = runner.author_one({}, chunk, "SIMULATION", {})
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["failures"], ["source_or_semantic_fragment_validation"])
        self.assertFalse((self.root / "actors/author/fixture/attempt-001/validation.json").exists())
        evidence.assert_not_called()

    def test_private_files_never_enter_checkpoint_inventory(self):
        (self.root / "application.json").write_text("{}")
        for name in ("run", "private", "bundle", "dist"):
            (self.root / name).mkdir(); (self.root / name / "secret.txt").write_text("PRIVATE FIXTURE")
        rows = checkpoint_files.inventory(self.root)["files"]
        self.assertEqual([row["path"] for row in rows], ["application.json"])
        (self.root / "unclassified.txt").write_text("unknown")
        with self.assertRaisesRegex(ValueError, "unclassified"):
            checkpoint_files.inventory(self.root)


class PackagingTests(TemporaryFixture):
    def refuse_build(self, bundle, dist):
        with patch.object(package, "preparation", side_effect=AssertionError("input processing reached")):
            with self.assertRaisesRegex(ValueError, "overlap|outside|preserve|already exists"):
                package.build(SimpleNamespace(bundle=bundle, dist=dist))

    def test_archive_equal_nested_and_dotdot_outputs_refuse_before_effects(self):
        for suffix in ("", "dist", "missing/../dist"):
            bundle = self.root / "bundle"
            self.refuse_build(bundle, bundle / suffix)
            self.assertFalse(bundle.exists())

    def test_archive_symlink_alias_and_ancestor_outputs_refuse(self):
        real = self.root / "real"; real.mkdir(); alias = self.root / "alias"; alias.symlink_to(real, target_is_directory=True)
        self.refuse_build(real / "bundle", alias / "bundle/dist")
        self.refuse_build(self.root / "dist" / (package.ARTIFACT + ".tar.gz") / "bundle", self.root / "dist")
        self.assertFalse((self.root / "dist").exists())

    def test_existing_bundle_archive_and_checksum_preserved(self):
        for name in ("bundle", "archive", "checksum"):
            parent = self.root / name; parent.mkdir(); bundle = parent / "bundle"; dist = parent / "dist"
            if name == "bundle":
                bundle.mkdir(); marker = bundle / "marker"
            else:
                dist.mkdir(); marker = dist / (package.ARTIFACT + ".tar.gz" + (".sha256" if name == "checksum" else ""))
            marker.write_bytes(b"keep")
            self.refuse_build(bundle, dist)
            self.assertEqual(marker.read_bytes(), b"keep")

    def test_direct_archive_overlap_refuses(self):
        bundle = self.root / "bundle"; bundle.mkdir(); (bundle / "one.txt").write_bytes(b"one")
        with self.assertRaisesRegex(ValueError, "overlap"):
            package.archive(bundle, bundle / "dist/archive.tar.gz")
        self.assertEqual([p.name for p in bundle.iterdir()], ["one.txt"])

    def test_safe_archive_is_reproducible_and_complete(self):
        results = []
        for name in ("a", "b"):
            bundle = self.root / name / "bundle"; bundle.mkdir(parents=True); (bundle / "one.txt").write_bytes(b"one")
            output = self.root / name / "archive.tar.gz"
            report = package.archive(bundle, output)
            with tarfile.open(output) as archive:
                self.assertEqual(archive.getnames(), [package.ARTIFACT + "/one.txt"])
                self.assertEqual(archive.extractfile(archive.getmembers()[0]).read(), b"one")
            self.assertEqual(report["sha256"], c.sha(output.read_bytes())); results.append(output.read_bytes())
        self.assertEqual(*results)

    def synthetic_receipts(self):
        expected = {"source": {"subject_id": "urn:fixture:simulation", "commit": "1" * 40, "package_tree": "2" * 40}, "model": {"id": "urn:fixture:model", "sha256": "a" * 64}, "artifacts": {}}
        common = {"bindings": expected, "scope": "SIMULATION: receipt grammar test; no actual construction or assessment.", "details": {"simulation": True}}
        author = {**common, "kind": receipts.CONSTRUCTION, "receipt_id": "urn:fixture:author-receipt", "issuer": "urn:fixture:author", "construction_state": "complete", "private_material_included": False}
        review = {**common, "kind": receipts.REVIEW, "receipt_id": "urn:fixture:review-receipt", "issuer": "urn:fixture:reviewer", "review_state": "closed", "outcome": "SIMULATION", "independence": {"simulation": True}, "reports": []}
        write(self.root / "evidence/authoring-public.json", author)
        write(self.root / "evidence/reviews/review-001/receipt.json", review)
        release = {"public_receipt_contract": [receipts.CONSTRUCTION, receipts.REVIEW], "subject": expected["source"]["subject_id"], "model": expected["model"], "source_commit": expected["source"]["commit"], "package_tree": expected["source"]["package_tree"],
                   "public_authoring_receipt_sha256": c.sha((self.root / "evidence/authoring-public.json").read_bytes()),
                   "review_receipts": [{"path": "evidence/reviews/review-001/receipt.json", "sha256": c.sha((self.root / "evidence/reviews/review-001/receipt.json").read_bytes()), "receipt_id": review["receipt_id"], "reports": []}]}
        write(self.root / "RELEASE.json", release)
        return expected, release

    def test_exact_synthetic_receipt_bindings_validate(self):
        expected, _ = self.synthetic_receipts()
        self.assertEqual(receipts.bundle_evidence(self.root, expected)["bounded_review_receipts"], 1)

    def test_wrong_missing_source_index_fields_refuse(self):
        expected, release = self.synthetic_receipts()
        for key in ("source_commit", "package_tree"):
            for absent in (False, True):
                changed = dict(release)
                if absent: del changed[key]
                else: changed[key] = "0" * 40
                write(self.root / "RELEASE.json", changed)
                with self.assertRaisesRegex(ValueError, "source commit/package tree"):
                    receipts.bundle_evidence(self.root, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
