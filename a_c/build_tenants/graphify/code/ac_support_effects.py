"""Protected persistence and finite local effects for the support-tool tenant.

This module is the cooperative local POSIX effect membrane, not a scheduler.
Complete immutable envelopes precede dependent effects; observation, delivery,
process end and intended outcome remain different facts. Runtime authority and
all operation/predicate contracts are supplied by ac_support_core.
"""
from __future__ import annotations

import base64
from contextlib import contextmanager
import fcntl
import hashlib
import os
from pathlib import Path
import re
import selectors
import signal
import stat
import subprocess
import sys
import threading
import time
from typing import Iterator, cast
import uuid

import ac_support_core as c

__all__ = ["EvidenceStore", "execute_effect", "persist_outcome", "supervise"]

_SHA = re.compile(r"^[0-9a-f]{64}$")


def _fault(boundary: str) -> None:
    """Named post-validation fault boundaries; never caller-configurable."""


def _hash(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _product(runtime: c.Runtime) -> str:
    return c.text(c.as_object(runtime.policy["product"], "product")["definition_id"], "Product id")


def _policy_current(runtime: c.Runtime) -> None:
    if _hash(_regular(runtime.policy_path)) != runtime.policy_sha256:
        raise c.SupportError("basis_stale", "Operator-selected policy bytes changed; no silent policy substitution", [], [])


def _regular(path: Path) -> bytes:
    try:
        if not stat.S_ISREG(path.lstat().st_mode):
            raise c.SupportError("path_refused", "Expected a regular non-symlink file", [str(path)], [])
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, "rb") as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise c.SupportError("path_refused", "Opened input is not regular", [str(path)], [])
            return stream.read()
    except FileNotFoundError as error:
        raise c.SupportError("source_missing", "Required regular file is absent", [str(path)], []) from error


def _directory(path: Path, create: bool = False) -> None:
    if not path.is_absolute():
        raise c.SupportError("path_refused", "Protected directory must be absolute", [str(path)], [])
    cursor = Path(path.anchor)
    for part in path.parts[1:]:
        cursor /= part
        try:
            mode = cursor.lstat().st_mode
        except FileNotFoundError:
            if not create:
                raise c.SupportError("source_missing", "Protected directory is absent", [str(cursor)], [])
            try:
                cursor.mkdir(mode=0o700)
            except FileExistsError:
                pass
            mode = cursor.lstat().st_mode
        if not stat.S_ISDIR(mode):
            raise c.SupportError("path_refused", "Symlink or non-directory component refused", [str(cursor)], [])


def _sync_directory(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _atomic(path: Path, raw: bytes, *, tag: str, replace: bool = False, mode: int = 0o600) -> None:
    """Publish one complete same-directory unit; no non-atomic fallback.

    Failure after publication may leave complete visible bytes. The caller must
    retain/reconstruct that uncertainty; this function never rolls back.
    """
    _directory(path.parent)
    stage = path.parent / (".stage-" + uuid.uuid4().hex)
    published = False
    _fault(tag + ":before_stage")
    fd = os.open(stage, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode)
    try:
        with os.fdopen(fd, "wb") as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(raw)
            stream.flush()
            _fault(tag + ":before_stage_fsync")
            os.fsync(stream.fileno())
        _fault(tag + ":after_stage_fsync")
        _fault(tag + ":before_publish")
        if replace:
            os.replace(stage, path)
        else:
            os.link(stage, path, follow_symlinks=False)
        published = True
        _fault(tag + ":after_publish")
        _fault(tag + ":before_directory_fsync")
        _sync_directory(path.parent)
        _fault(tag + ":after_directory_fsync")
    finally:
        # This is the private staging link, never committed evidence/target.
        if published and stage.exists():
            stage.unlink()


def _ref(value: c.JSON) -> c.Object:
    ref = c.as_object(value, "ArtifactRef")
    c.exact_keys(ref, ("id", "sha256"), label="ArtifactRef")
    sha = c.text(ref["sha256"], "ArtifactRef.sha256")
    if not _SHA.fullmatch(sha) or ref["id"] != "sha256:" + sha:
        raise c.SupportError("digest_mismatch", "Artifact identity and digest disagree", [ref], [])
    return ref


def _support_fields(value: c.JSON, fields: tuple[tuple[str, str], ...]) -> list[c.Object]:
    """Follow only declared coordinates, never the shape of arbitrary JSON."""
    refs: list[c.Object] = []
    for path, kind in fields:
        frontier = [value]
        for coordinate in path.split("."):
            selected: list[c.JSON] = []
            for parent in frontier:
                if coordinate == "*" and isinstance(parent, list):
                    selected.extend(parent)
                elif isinstance(parent, dict) and coordinate in parent:
                    selected.append(parent[coordinate])
            frontier = selected
        for member in frontier:
            refs.extend(_typed_support(member, kind))
    return refs


def _typed_support(value: c.JSON, kind: str) -> list[c.Object]:
    if value is None:
        return []  # Declared nullable support, not an absent required artifact.
    if kind == "ArtifactRef":
        return [_ref(value)]
    if kind == "Envelope":
        envelope = c.as_object(value, "complete support envelope")
        c.exact_keys(envelope, ("schema", "kind", "provenance", "payload"), label="complete support envelope")
        if envelope["schema"] != c.ARTIFACT or envelope["kind"] not in c.KINDS:
            raise c.SupportError("contract_violation", "Unsupported complete support envelope", [], [])
        sha = c.digest(envelope)
        return [{"id": "sha256:" + sha, "sha256": sha}]
    if kind == "SourceRef":
        source = c.validate_content(value, "SourceRef")
        if source["engine"] == "retained-evidence":
            return [_ref({"id": source["path"], "sha256": source["sha256"]})]
        return []  # Files/Git objects are sources, not protected ArtifactRefs.
    if kind == "AcquiredRef":
        acquired = c.as_object(value, "AcquiredRef")
        return _typed_support(value, "SourceRef" if "engine" in acquired else "ArtifactRef")
    if kind == "Judgment":
        judgment = c.as_object(value, "judgment")
        refs = _support_fields(judgment, (("basis", "Basis"), ("evidence.*", "AcquiredRef")))
        # Finite guard names and byte-fit predicates are strings. Source-bound
        # actual predicate judgments have a declared SourceRef instead.
        if isinstance(judgment.get("predicate"), dict):
            refs.extend(_typed_support(judgment["predicate"], "SourceRef"))
        return refs  # Subject Identity and domain_outcome remain data.
    definitions: dict[str, tuple[tuple[str, str], ...]] = {
        "ModelRef": (("source", "SourceRef"),),
        "Basis": (("observations.*", "ArtifactRef"),),
        "JudgmentRef": (("record", "ArtifactRef"),),
        "Recheck": (("product_definition", "SourceRef"), ("method_profile", "SourceRef"), ("sources.*", "SourceRef"), ("observations.*", "ArtifactRef"), ("executor_dependencies.*", "SourceRef")),
        "Resource": (("owner.record", "ArtifactRef"), ("samples.*.owner.record", "ArtifactRef"), ("samples.*.raw_source", "AcquiredRef")),
    }
    if kind in definitions:
        return _support_fields(value, definitions[kind])
    if kind in ("observation", "attempt", "event"):
        return _payload_support("raw" if kind == "event" else kind, value)
    raise c.SupportError("unsupported_contract", "Unknown internal typed support coordinate", [kind], [])


def _result_support(operation: str, result: c.JSON) -> list[c.Object]:
    if result is None:
        return []
    record = c.as_object(result, "result")
    refs = _support_fields(record, (("artifact", "ArtifactRef"),))
    value = record.get("value")
    if operation in ("workspace.observe", "contract.preflight", "return.capture"):
        refs.extend(_payload_support({"workspace.observe": "observation", "contract.preflight": "preflight", "return.capture": "return"}[operation], value))
    fields: dict[str, tuple[tuple[str, str], ...]] = {
        "source.read": (("source", "SourceRef"),),
        "work.project": (("source", "SourceRef"),),
        "dispatch.start": (("attempt", "ArtifactRef"),),
        "dispatch.cancel": (("attempt", "ArtifactRef"), ("request_event", "ArtifactRef")),
        "dispatch.observe": (("attempt", "ArtifactRef"), ("anchor", "attempt"), ("events.*", "event"), ("output.stdout", "ArtifactRef"), ("output.stderr", "ArtifactRef")),
        "events.wait": (("attempt", "ArtifactRef"), ("anchor", "attempt"), ("events.*", "event"), ("output.stdout", "ArtifactRef"), ("output.stderr", "ArtifactRef")),
        "evidence.read": (("artifact", "ArtifactRef"),),
        "checks.evaluate": (("judgment", "Judgment"),),
        "return.check": (("checks.*", "Judgment"), ("duplicates.*", "ArtifactRef")),
        "results.conjoin": (("judgment", "Judgment"), ("plan", "SourceRef"), ("originals.*.record", "ArtifactRef"), ("applicable.*.result.return", "ArtifactRef")),
        "review.prepare": (("claim", "SourceRef"), ("acquired.*.source", "SourceRef"), ("expectations", "ArtifactRef"), ("exposure.*.acquisition", "ArtifactRef"), ("independence.selected_policy", "SourceRef")),
        "refresh.prepare": (("handoff.previous", "ArtifactRef"), ("handoff.current", "ArtifactRef"), ("handoff.declarations", "SourceRef"), ("handoff.original_results.*", "ArtifactRef"), ("retention.*.original", "JudgmentRef")),
        "resources.aggregate": (("roots.*", "ArtifactRef"), ("resources.*", "Resource"), ("limit_judgments.*", "Judgment")),
    }
    refs.extend(_support_fields(value, fields.get(operation, ())))
    if operation == "relations.query":
        refs.extend(_support_fields(value, (("declarations", "SourceRef"), ("model", "ModelRef"), ("basis", "Basis"))))
        if isinstance(value, dict):
            for fact in c.as_list(value.get("applicability", [])):
                actual = c.as_object(fact)
                # An unresolved candidate may quote a nonexistent judgment.
                # Only an actual checked judgment supports this result.
                if actual.get("core_value") is not None:
                    refs.extend(_support_fields(actual, (("judgment", "JudgmentRef"), ("condition.predicate", "SourceRef"))))
    return refs


def _outcome_support(operation: str, outcome: c.Object) -> list[c.Object]:
    return [*_result_support(operation, outcome.get("result")), *_support_fields(outcome, (("artifacts.*", "Envelope"), ("acquisitions.*", "ArtifactRef"), ("operation_outcome.evidence.*", "AcquiredRef")))]


def _payload_support(kind: str, value: c.JSON) -> list[c.Object]:
    if not isinstance(value, dict):
        return []
    payload = value
    fields: dict[str, tuple[tuple[str, str], ...]] = {
        "observation": (("bindings.product_definition", "SourceRef"), ("bindings.method_profile", "SourceRef")),
        "context": (("observations.*", "ArtifactRef"), ("packet.subject_basis.observations.*", "ArtifactRef"), ("sources.*.source", "SourceRef"), ("projections.*.model", "ModelRef")),
        "preflight": (("context", "ArtifactRef"), ("state_evidence.*", "AcquiredRef"), ("mechanism.source", "SourceRef"), ("authority.owner_record", "SourceRef"), ("authority.mechanism.source", "SourceRef"), ("recheck", "Recheck"), ("evaluations.*", "Judgment")),
        "attempt": (("preflight", "ArtifactRef"), ("context", "ArtifactRef"), ("retry_of", "ArtifactRef"), ("reconciliation", "ArtifactRef"), ("notification.binding.authority_source", "SourceRef")),
        "return": (("attempt", "ArtifactRef"), ("raw_payload", "ArtifactRef"), ("return_contract", "SourceRef"), ("producer.attempt", "ArtifactRef")),
        "expectation": (("claim", "SourceRef"), ("source_inputs.*", "ArtifactRef"), ("exposure_check.prior.*.acquisition", "ArtifactRef"), ("exposure_check.history.refs.*", "ArtifactRef")),
        "resource": (("owner.record", "ArtifactRef"), ("samples.*.owner.record", "ArtifactRef"), ("samples.*.raw_source", "AcquiredRef")),
        "operation": (("artifacts.*", "ArtifactRef"), ("acquisitions.*", "ArtifactRef"), ("resources.*", "ArtifactRef")),
    }
    refs = _support_fields(payload, fields.get(kind, ()))
    schema = payload.get("schema")
    if kind == "context":
        host = _at(payload, "fit.host_context")
        if isinstance(host, dict) and host.get("state") in ("known", "bounded") and host.get("bytes") is not None:
            refs.extend(_support_fields(host, (("evidence", "SourceRef"),)))
    if kind == "preflight" and isinstance(payload.get("authority"), dict) and "engine" in c.as_object(payload["authority"]):
        refs.extend(_typed_support(payload["authority"], "SourceRef"))
    if kind == "operation":
        response = c.as_object(payload.get("response_without_evidence", {}))
        operation = response.get("operation")
        if isinstance(operation, str):
            refs.extend(_result_support(operation, response.get("result")))
        refs.extend(_support_fields(response, (("operation_outcome.evidence.*", "AcquiredRef"),)))
        return refs  # Original request, refusal/gaps and quoted results are data.
    if kind == "acquisition":
        if schema == "a_c.fd-support.transport-observation/1":
            refs.extend(_support_fields(payload, (("operation", "ArtifactRef"), ("acquisitions.*", "ArtifactRef"))))
        elif schema == "a_c.fd-support.acquisition/1":
            refs.extend(_support_fields(payload, (("source", "SourceRef"), ("model", "ModelRef"))))
        return refs
    if kind in ("raw", "qualification") and schema == "a_c.fd-support.operator-qualification/1":
        refs.extend(_support_fields(payload, (("dependencies.*", "SourceRef"), ("proof_sources.*", "AcquiredRef"))))
    if kind != "raw":
        return refs
    raw_fields: dict[str, tuple[tuple[str, str], ...]] = {
        "a_c.fd-support.request-claim/1": (("selected_policy", "ArtifactRef"),),
        "a_c.fd-support.writer-intent/1": (("recheck", "Recheck"), ("plan.record.provenance", "SourceRef"), ("plan.interpretation.author", "SourceRef")),
        "a_c.fd-support.writer-result/1": (("intent", "ArtifactRef"), ("record.provenance", "SourceRef"), ("interpretation.author", "SourceRef")),
        "a_c.fd-support.writer-recovery/1": (("intent", "ArtifactRef"),),
        "a_c.fd-support.process-output/1": (("attempt", "ArtifactRef"),),
        "a_c.fd-support.notification/1": (("attempt", "ArtifactRef"), ("event", "ArtifactRef")),
        "a_c.fd-support.attempt-event/1": (("attempt", "ArtifactRef"), ("previous", "ArtifactRef")),
    }
    if isinstance(schema, str):
        refs.extend(_support_fields(payload, raw_fields.get(schema, ())))
    if schema == "a_c.fd-support.effect-outcome/1":
        request = c.as_object(payload["request"])
        refs.extend(_outcome_support(c.text(request["operation"]), c.as_object(payload["outcome"])))
    elif schema == "a_c.fd-support.attempt-event/1":
        event_fields: dict[str, tuple[tuple[str, str], ...]] = {
            "context_delivery": (("context", "ArtifactRef"),),
            "output_finalized": (("stdout", "ArtifactRef"), ("stderr", "ArtifactRef")),
            "notification_failure": (("event", "ArtifactRef"),),
            "reconciliation_verified": (("predecessor", "ArtifactRef"), ("basis", "Basis"), ("history.refs.*", "ArtifactRef"), ("selected.*.results.*", "Judgment")),
            "file_postimages_observed": (("observation", "observation"),),
            "basis_change": (("observations.*", "observation"),),
            "effect_observation": (("observations.observations.*", "observation"),),
        }
        event_kind = c.text(payload["kind"], "event kind")
        refs.extend(_support_fields(payload.get("data"), event_fields.get(event_kind, ())))
    # Unknown raw/qualification bodies and original actor/source payloads do
    # not acquire support authority by containing identity-shaped JSON.
    return refs


def _references(value: c.JSON) -> list[c.Object]:
    """Declared support edges of an envelope, not every quoted identity."""
    if not isinstance(value, dict) or value.get("schema") != c.ARTIFACT:
        return []
    refs = _support_fields(value, (("provenance.attempt", "ArtifactRef"),))
    refs.extend(_payload_support(c.text(value["kind"]), value["payload"]))
    return refs


def _at(value: c.JSON, dotted: str) -> c.JSON:
    current = value
    for part in dotted.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


class EvidenceStore:
    """Complete immutable envelopes; no mutable hash-bound domain records."""

    def __init__(self, runtime: c.Runtime) -> None:
        self.runtime = runtime
        self.root = runtime.evidence_root
        _directory(self.root, create=True)
        for name in ("objects", "locks", "requests", "attempts", "events", "diagnostics"):
            _directory(self.root / name, create=True)

    def resolve(self, reference: c.Object) -> bytes:
        ref = _ref(reference)
        sha = c.text(ref["sha256"], "sha256")
        _directory(self.root / "objects")
        raw = _regular(self.root / "objects" / (sha + ".json"))
        if _hash(raw) != sha:
            raise c.SupportError("digest_mismatch", "Protected artifact bytes changed", [ref], [])
        envelope = c.as_object(c.parse_json(raw), "artifact")
        c.exact_keys(envelope, ("schema", "kind", "provenance", "payload"), label="artifact")
        if envelope["schema"] != c.ARTIFACT or envelope["kind"] not in c.KINDS or c.canonical(envelope) != raw:
            raise c.SupportError("contract_violation", "Invalid complete artifact envelope", [ref], [])
        if c.as_object(envelope["provenance"], "provenance").get("product_id") != _product(self.runtime):
            raise c.SupportError("acquisition_denied", "Artifact belongs to another Product", [ref], [])
        return raw

    def retain(self, envelope: c.Object) -> c.Object:
        # Participating readers acquire the same lock: an ordinary concurrent
        # publication is not mistaken for an abandoned/unknown history prefix.
        # A stage left by an interrupted publisher is still an explicit gap.
        with self._lock("store:objects"):
            return self._retain(envelope)

    def _retain(self, envelope: c.Object) -> c.Object:
        c.exact_keys(envelope, ("schema", "kind", "provenance", "payload"), label="artifact")
        if envelope["schema"] != c.ARTIFACT or envelope["kind"] not in c.KINDS:
            raise c.SupportError("contract_violation", "Only complete core envelopes may be retained", [envelope.get("kind")], [])
        raw = c.canonical(envelope)
        reference: c.Object = {"id": "sha256:" + _hash(raw), "sha256": _hash(raw)}
        provenance = c.as_object(envelope["provenance"], "provenance")
        checked_envelope, _ = c.make_artifact(c.text(envelope["kind"]), envelope["payload"], provenance)
        if checked_envelope != envelope:
            raise c.SupportError("contract_violation", "Complete envelope differs from its core construction", [], [])
        if provenance.get("product_id") != _product(self.runtime):
            raise c.SupportError("result_surface_denied", "Wrong Product evidence surface", [], [])
        for dependency in _references(envelope):
            if dependency == reference:
                raise c.SupportError("contract_violation", "Artifact cannot reference itself", [reference], [])
            self.resolve(dependency)
        path = self.root / "objects" / (c.text(reference["sha256"], "sha256") + ".json")
        if path.exists():
            if self.resolve(reference) != raw:
                raise c.SupportError("target_conflict", "Immutable artifact identity conflict", [reference], [])
            return reference
        try:
            _atomic(path, raw, tag="artifact:" + c.text(envelope["kind"], "kind"))
        except FileExistsError:
            if self.resolve(reference) != raw:
                raise c.SupportError("target_conflict", "Concurrent immutable artifact conflict", [reference], [])
        except OSError as error:
            raise c.SupportError("evidence_publication_failed", "Complete artifact publication not established", [str(error), {"artifact": reference, "visible_complete": path.exists()}], []) from error
        return reference

    def query_artifacts(self, kind: str, exact_match_fields: c.Object) -> c.Object:
        with self._lock("store:objects"):
            return self._query_artifacts(kind, exact_match_fields)

    def _query_artifacts(self, kind: str, exact_match_fields: c.Object) -> c.Object:
        if kind not in c.KINDS:
            raise c.SupportError("unsupported_contract", "Unknown artifact kind", [kind], [])
        refs: list[c.JSON] = []
        gaps: list[c.JSON] = []
        try:
            population = sorted((self.root / "objects").iterdir())
        except OSError as error:
            population = []
            gaps.append({"history_enumeration": str(error)})
        for path in population:
            if path.name.startswith(".stage-"):
                gaps.append({"in_flight_or_orphan_stage": path.name})
                continue
            sha = path.stem
            if path.suffix != ".json" or not _SHA.fullmatch(sha):
                gaps.append({"unrecognized_history_member": path.name})
                continue
            ref: c.Object = {"id": "sha256:" + sha, "sha256": sha}
            try:
                envelope = c.as_object(c.parse_json(self.resolve(ref)), "artifact")
                if envelope["kind"] == kind and all(_at(envelope, key) == value for key, value in exact_match_fields.items()):
                    refs.append(ref)
            except (c.SupportError, OSError) as error:
                gaps.append({"unreadable_history": path.name, "detail": str(error)})
        maximum = _limit(self.runtime, "max_history_records")
        if maximum is not None and len(population) > maximum:
            gaps.append({"history_population_exceeds_selected_limit": maximum, "observed": len(population)})
        return {"refs": refs, "complete": not gaps, "gaps": gaps, "scope": {"product_id": _product(self.runtime), "evidence_root": str(self.root), "kind": kind}, "observed_at_ns": time.time_ns()}

    @contextmanager
    def _lock(self, identity: str, *, nonblocking: bool = False) -> Iterator[None]:
        path = self.root / "locks" / (_hash(identity.encode("utf-8")) + ".lock")
        fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        try:
            flags = fcntl.LOCK_EX | (fcntl.LOCK_NB if nonblocking else 0)
            try:
                fcntl.flock(fd, flags)
            except BlockingIOError as error:
                raise c.SupportError("target_conflict", "Another participating Writer owns the target lock", [identity], []) from error
            yield
        finally:
            os.close(fd)


def _bound(runtime: c.Runtime) -> tuple[c.Runtime, EvidenceStore]:
    store = EvidenceStore(runtime)
    return runtime.with_callbacks(store.resolve, store.query_artifacts), store


def _artifact(runtime: c.Runtime, request: c.Object, kind: str, payload: c.Object, *, target: str | None = None, attempt: c.Object | None = None, started: int | None = None) -> tuple[c.Object, c.Object]:
    end = time.time_ns()
    return c.make_artifact(kind, payload, c.provenance(runtime, request, end if started is None else started, end, target=target, attempt=attempt))


def _selected_policy(runtime: c.Runtime, request: c.Object) -> tuple[c.Object, c.Object]:
    raw = _regular(runtime.policy_path)
    if _hash(raw) != runtime.policy_sha256:
        raise c.SupportError("basis_stale", "Selected policy source advanced before exact acquisition", [], [])
    return _artifact(runtime, request, "raw", {"schema": "a_c.fd-support.selected-policy/1", "startup_path": str(runtime.policy_path), "sha256": runtime.policy_sha256, "bytes_base64": base64.b64encode(raw).decode("ascii"), "authority": "Existing operator-selected source only; retention grants no authority."})


def _ok(request: c.Object, value: c.JSON, artifacts: list[c.JSON] | None = None, reference: c.Object | None = None, acquisitions: list[c.JSON] | None = None) -> c.CoreOutcome:
    return {"result": {"artifact": reference, "value": value}, "artifacts": [] if artifacts is None else artifacts, "operation_outcome": c.operation_outcome(c.text(request["operation"], "operation")), "refusal": None, "acquisitions": [] if acquisitions is None else acquisitions}


def _publish_graph(store: EvidenceStore, envelopes: list[c.JSON]) -> list[c.JSON]:
    pending = [c.as_object(item, "artifact") for item in envelopes]
    published: list[c.JSON] = []
    while pending:
        progress = False
        for envelope in list(pending):
            dependencies = _references(envelope)
            try:
                for ref in dependencies:
                    store.resolve(ref)
            except c.SupportError as error:
                if error.code == "source_missing":
                    continue
                raise
            published.append(store.retain(envelope))
            pending.remove(envelope)
            progress = True
        if not progress:
            raise c.SupportError("basis_missing", "Outgoing artifact graph has missing or cyclic dependencies", [_hash(c.canonical(item)) for item in pending], [])
    return published


def persist_outcome(runtime: c.Runtime, request: c.Object, outcome: c.CoreOutcome) -> c.Object:
    """Retain exact final envelopes and the one nonrecursive response wrapper."""
    started = time.time_ns()
    response: c.Object = {"schema": "a_c.fd-support.response/1", "id": request.get("id"), "operation": request.get("operation"), "status": "error", "result": outcome.get("result"), "refusal": outcome.get("refusal"), "operation_outcome": outcome.get("operation_outcome"), "evidence": None}
    try:
        c.exact_keys(outcome, ("result", "artifacts", "operation_outcome", "refusal", "acquisitions"), label="CoreOutcome")
        boundary = c.as_object(outcome["operation_outcome"], "operation_outcome")
        boundary_value = c.text(boundary["value"], "operation_outcome.value")
        if boundary_value == "returned":
            response["status"] = "ok"
            if outcome["refusal"] is not None:
                raise c.SupportError("contract_violation", "Returned outcome must have null refusal", [], [])
        elif boundary_value.startswith("refused("):
            response["status"] = "refused"
        elif boundary_value not in ("held(observation)", "held(effect)"):
            raise c.SupportError("contract_violation", "Unknown operation boundary value", [boundary_value], [])
        if boundary_value != "returned" and outcome["refusal"] is None:
            raise c.SupportError("contract_violation", "Unavailable output requires exact refusal evidence", [], [])
        runtime, store = _bound(runtime)
        refs = _publish_graph(store, c.as_list(outcome["artifacts"], "artifacts"))
        selected_policy, selected_policy_ref = _selected_policy(runtime, request)
        store.retain(selected_policy)
        refs.append(selected_policy_ref)
        for ref in _result_support(c.text(request["operation"], "operation"), outcome["result"]):
            store.resolve(ref)
        acquisitions: list[c.JSON] = []
        for value in c.as_list(outcome["acquisitions"], "acquisitions"):
            acquisition_ref = _ref(value)
            c.load_artifact(runtime, acquisition_ref, "acquisition")
            acquisitions.append(acquisition_ref)
        interval: c.Object = {"started_ns": started, "ended_ns": time.time_ns(), "clock": "unix_ns"}
        operation: c.Object = {"schema": "a_c.fd-support.operation/1", "request": request, "response_without_evidence": response.copy(), "artifacts": refs, "acquisitions": acquisitions, "interval": interval, "resources": [], "gaps": []}
        envelope, reference = _artifact(runtime, request, "operation", operation, started=started)
        store.retain(envelope)
        response["evidence"] = reference
        # Operation-owned samples are subsequent records, avoiding a self-cycle.
        resource: c.Object = {"schema": "a_c.fd-support.resource/1", "owner": {"kind": "operation", "record": reference}, "samples": [], "interval": interval, "gaps": ["Backend token/cache/cost counters were not observed; they are unknown, not zero."]}
        resource_envelope, _ = _artifact(runtime, request, "resource", resource, started=started)
        store.retain(resource_envelope)
        return response
    except (OSError, c.SupportError) as error:
        original = error if isinstance(error, c.SupportError) else c.SupportError("evidence_publication_failed", "Evidence publication failed", [str(error)], [])
        # A computed ref is never returned as durable after publication failure.
        response["status"] = "error"
        response["result"] = None
        response["evidence"] = None
        response["refusal"] = {"code": "evidence_publication_failed", "reason": "Output durable publication is not established", "gaps": [original.code, original.reason, *original.gaps], "source_refs": original.source_refs}
        response["operation_outcome"] = c.operation_outcome(c.text(request["operation"], "operation"), code="evidence_publication_failed")
        return response


def _limit(runtime: c.Runtime, name: str) -> int | None:
    limits = c.as_object(runtime.policy["limits"], "limits")
    value = limits.get(name)
    return None if value is None else c.integer(value, "limits." + name, 1)


def _key(runtime: c.Runtime, request: c.Object) -> str:
    return c.digest({"product": _product(runtime), "principal": runtime.principal_id, "id": request["id"]})


def _marker(store: EvidenceStore, path: Path) -> c.Object | None:
    if not path.exists():
        return None
    raw = _regular(path)
    ref: c.Object = {"id": "sha256:" + _hash(raw), "sha256": _hash(raw)}
    if store.resolve(ref) != raw:
        raise c.SupportError("digest_mismatch", "Protected marker changed", [str(path)], [])
    return c.as_object(c.parse_json(raw), "marker")


def _mark(store: EvidenceStore, path: Path, envelope: c.Object, tag: str) -> c.Object:
    reference = store.retain(envelope)
    raw = c.canonical(envelope)
    try:
        _atomic(path, raw, tag=tag)
    except FileExistsError:
        if _regular(path) != raw:
            raise c.SupportError("request_identity_conflict", "Protected identity already has different complete bytes", [str(path)], [])
    return reference


def _fresh(runtime: c.Runtime, store: EvidenceStore, request: c.Object, recheck: c.Object) -> list[c.JSON]:
    result = c.check_preconditions(runtime, recheck)
    refs: list[c.JSON] = []
    for payload in c.as_list(result["observations"], "fresh observations"):
        envelope, reference = _artifact(runtime, request, "observation", c.as_object(payload))
        store.retain(envelope)
        refs.append(reference)
    if c.as_list(result["changes"], "changes"):
        raise c.SupportError("basis_stale", "Material inputs changed before the dependent effect", [*c.as_list(result["changes"]), {"fresh_observations": refs}], [])
    if c.as_list(result["gaps"], "gaps"):
        raise c.SupportError("basis_missing", "Material input recheck has unresolved premises", [*c.as_list(result["gaps"]), {"fresh_observations": refs}], [])
    return refs


def _check_plan(runtime: c.Runtime, request: c.Object, plan: c.EffectPlan) -> None:
    c.exact_keys(plan, ("schema", "operation", "request_id", "request_sha256", "requester_principal", "target_principal", "policy_sha256", "recheck", "payload"), label="EffectPlan")
    if plan["schema"] != "a_c.fd-support.effect-plan/1" or plan["operation"] != request["operation"] or plan["request_id"] != request["id"] or plan["request_sha256"] != c.digest(request) or plan["policy_sha256"] != runtime.policy_sha256 or plan["requester_principal"] != runtime.principal_id:
        raise c.SupportError("contract_violation", "Prepared effect does not bind this exact request/policy/principal", [], [])


def _owner_binding(runtime: c.Runtime, request: c.Object, envelope: c.Object,
                   schema: str) -> None:
    payload = c.as_object(envelope["payload"])
    provenance = c.as_object(envelope["provenance"])
    c.make_artifact(c.text(envelope["kind"]), payload, provenance)
    if payload.get("schema") != schema:
        raise c.SupportError("history_incomplete", "Committed owner has an unexpected carrier", [], [])
    saved = c.validate_request(payload["request"])
    if provenance["request_id"] != saved["id"] or provenance["request_sha256"] != c.digest(saved):
        raise c.SupportError("history_incomplete", "Committed owner request/provenance is incoherent", [], [])
    if schema == "a_c.fd-support.request-claim/1" and payload["policy_sha256"] != provenance["policy_sha256"]:
        raise c.SupportError("history_incomplete", "Committed claim policy/provenance is incoherent", [], [])
    product = c.as_object(runtime.policy["product"])
    expected: c.Object = {"product_id": product["definition_id"], "definition_sha256": c.as_object(product["definition"])["sha256"], "requester_principal": runtime.principal_id, "policy_sha256": runtime.policy_sha256, "method_profile_sha256": c.PROFILE_SHA256, "actor": runtime.principal}
    if saved != request or any(provenance[name] != value for name, value in expected.items()):
        raise c.SupportError("request_identity_conflict", "Committed owner binds different effective request/Product/principal/policy", [request["id"]], [])


def _identity_history(runtime: c.Runtime, store: EvidenceStore, request: c.Object,
                      schemas: tuple[str, ...]) -> c.Object:
    refs: list[c.JSON] = []; gaps: list[c.JSON] = []
    for schema in schemas:
        kind = "attempt" if schema == "a_c.fd-support.attempt/1" else "raw"
        query = store.query_artifacts(kind, {"provenance.product_id": _product(runtime),
            "provenance.requester_principal": runtime.principal_id,
            "payload.request.id": request["id"], "payload.schema": schema})
        refs.extend(c.as_list(query["refs"]))
        if query["complete"] is not True:
            gaps.append(query)
    return {"refs": refs, "complete": not gaps, "gaps": gaps,
            "scope": {"product_id": _product(runtime), "principal": runtime.principal_id, "request_id": request["id"]}}


def _claim(runtime: c.Runtime, store: EvidenceStore, request: c.Object) -> str:
    key = _key(runtime, request)
    path = store.root / "requests" / (key + ".claim.json")
    owners: dict[str, c.Object] = {}
    schemas = {"claim": "a_c.fd-support.request-claim/1", "outcome": "a_c.fd-support.effect-outcome/1", "intent": "a_c.fd-support.writer-intent/1", "attempt": "a_c.fd-support.attempt/1"}
    for suffix, schema in schemas.items():
        old = _marker(store, store.root / "requests" / (key + "." + suffix + ".json"))
        if old is not None:
            _owner_binding(runtime, request, old, schema)
            owners[suffix] = old
    if "claim" in owners:
        return key
    if owners:
        raise c.SupportError("history_incomplete", "Required request claim owner is absent; no reconstruction or new reservation", [request["id"]], [])
    history = _identity_history(runtime, store, request, tuple(schemas.values()))
    if history["complete"] is not True or c.as_list(history["refs"]):
        raise c.SupportError("history_incomplete", "Stable request identity has unresolved owner/history absence", [history], [])
    selected_policy, selected_policy_ref = _selected_policy(runtime, request)
    store.retain(selected_policy)
    envelope, _ = _artifact(runtime, request, "raw", {"schema": "a_c.fd-support.request-claim/1", "request": request, "policy_sha256": runtime.policy_sha256, "selected_policy": selected_policy_ref})
    _mark(store, path, envelope, "request_reservation")
    return key


def _completed(runtime: c.Runtime, store: EvidenceStore, request: c.Object, key: str) -> c.CoreOutcome | None:
    old = _marker(store, store.root / "requests" / (key + ".outcome.json"))
    if old is None:
        return None
    _owner_binding(runtime, request, old, "a_c.fd-support.effect-outcome/1")
    return c.as_object(c.as_object(old["payload"])["outcome"], "retained CoreOutcome")


def _verify_support_graph(store: EvidenceStore, references: list[c.Object]) -> None:
    """Verify historical typed support without treating quoted data as edges."""
    pending = list(references)
    verified: set[str] = set()
    while pending:
        reference = pending.pop()
        identity = c.text(reference["id"])
        if identity in verified:
            continue
        envelope = c.as_object(c.parse_json(store.resolve(reference)))
        verified.add(identity)
        pending.extend(_references(envelope))


def _complete(runtime: c.Runtime, store: EvidenceStore, request: c.Object, key: str, outcome: c.CoreOutcome) -> c.CoreOutcome:
    _publish_graph(store, c.as_list(outcome["artifacts"], "artifacts"))
    envelope, _ = _artifact(runtime, request, "raw", {"schema": "a_c.fd-support.effect-outcome/1", "request": request, "outcome": outcome})
    _mark(store, store.root / "requests" / (key + ".outcome.json"), envelope, "effect_outcome")
    return outcome


def _preflight(runtime: c.Runtime, store: EvidenceStore, request: c.Object, plan: c.EffectPlan) -> c.CoreOutcome:
    # A reconstructed historical receipt is returned unchanged, never re-admitted.
    previous = store.query_artifacts("preflight", {"provenance.requester_principal": runtime.principal_id, "provenance.request_sha256": c.digest(request)})
    refs = c.as_list(previous["refs"])
    if len(refs) > 1:
        raise c.SupportError("basis_ambiguous", "Multiple receipt identities for one exact activation request", refs, [])
    if refs:
        ref = c.as_object(refs[0])
        payload = c.load_artifact(runtime, ref, "preflight")["payload"]
        return _ok(request, payload, reference=ref)
    if previous["complete"] is not True:
        raise c.SupportError("history_incomplete", "Cannot establish absence of an earlier complete receipt", c.as_list(previous["gaps"]), [])
    with store._lock("scope:" + _product(runtime)):
        _fresh(runtime, store, request, c.as_object(plan["recheck"]))
        payload = c.as_object(plan["payload"]).copy()
        if payload.get("contract_state") != "drafted" or payload.get("decision") is not None:
            raise c.SupportError("contract_violation", "Core preflight plan must be a draft, not caller-supplied admission", [], [])
        evaluations = c.as_list(payload["evaluations"])
        accepted = not c.as_list(payload["gaps"]) and all(c.as_object(item).get("core_value") == "satisfied" for item in evaluations)
        payload["contract_state"] = "admitted" if accepted else "rejected"
        payload["decision"] = payload["contract_state"]
        # State evidence contains actual checked source/evaluation evidence; no
        # self-reference is inserted into its own immutable receipt.
        envelope, ref = _artifact(runtime, request, "preflight", payload, target=cast(str | None, plan["target_principal"]))
        store.retain(envelope)
        return _ok(request, payload, [envelope], ref)


def _target_state(path: Path) -> c.Object:
    try:
        raw = _regular(path)
        return {"exists": True, "sha256": _hash(raw), "bytes": len(raw), "type": "regular", "mode": stat.S_IMODE(path.stat().st_mode)}
    except c.SupportError as error:
        if error.code == "source_missing":
            return {"exists": False, "sha256": None, "bytes": 0, "type": "absent", "mode": None}
        raise


def _write_recovery(runtime: c.Runtime, store: EvidenceStore, request: c.Object,
                    old: c.Object, path: Path, target: c.Object) -> c.CoreOutcome:
    """Observe an earlier intent under the request/Product/target locks."""
    old_payload = c.as_object(old["payload"])
    saved = c.as_object(old_payload["plan"])
    if old_payload["request"] != request or saved["target"] != target or saved["requester"] != runtime.principal_id:
        raise c.SupportError("request_identity_conflict", "Writer intent does not bind the exact request/principal", [], [])
    state = _target_state(path)
    intended = saved["intended_sha256"]
    observation: c.Object = {"schema": "a_c.fd-support.writer-recovery/1", "intent": {"id": "sha256:" + c.digest(old), "sha256": c.digest(old)}, "target": target, "current": state, "matches_intended_postimage": state["sha256"] == intended, "effect": {"value": "completion_unknown", "end_established": False, "residual": "Original publication/result acknowledgment is not established; observed present bytes do not replay the operation."}, "repeated": False}
    envelope, ref = _artifact(runtime, request, "raw", observation)
    store.retain(envelope)
    outcome = c.refusal_outcome(runtime, request, c.SupportError("effect_unreconciled", "Earlier Writer intent requires reconciliation before any repeated effect", [observation], []))
    outcome["result"] = {"artifact": ref, "value": observation}
    outcome["artifacts"] = [envelope]
    return outcome


def _recover_write(runtime: c.Runtime, store: EvidenceStore, request: c.Object,
                   key: str) -> c.CoreOutcome | None:
    old = _marker(store, store.root / "requests" / (key + ".intent.json"))
    if old is None:
        history = _identity_history(runtime, store, request, ("a_c.fd-support.writer-intent/1", "a_c.fd-support.effect-outcome/1"))
        if history["complete"] is not True or c.as_list(history["refs"]):
            raise c.SupportError("history_incomplete", "Cannot establish absence of an earlier Writer intent/owner", [history], [])
        return None
    _owner_binding(runtime, request, old, "a_c.fd-support.writer-intent/1")
    _verify_support_graph(store, _references(old))
    saved = c.as_object(c.as_object(old["payload"])["plan"])
    target = c.as_object(c.as_object(request["arguments"])["target"])
    path = c.source_path(runtime, target, write=True, allow_absent=True)
    if saved["path"] != str(path):
        raise c.SupportError("path_refused", "Retained Writer intent path differs from its target", [], [])
    with store._lock("scope:" + _product(runtime)), store._lock("target:" + str(path), nonblocking=True):
        return _write_recovery(runtime, store, request, old, path, target)


def _write(runtime: c.Runtime, store: EvidenceStore, request: c.Object, plan: c.EffectPlan, key: str) -> c.CoreOutcome:
    payload = c.as_object(plan["payload"], "Writer plan")
    path = Path(c.text(payload["path"], "Writer target path"))
    target = c.as_object(payload["target"], "Writer target")
    if path != c.source_path(runtime, target, write=True, allow_absent=True):
        raise c.SupportError("path_refused", "Writer plan path differs from its validated target", [], [])
    if runtime.principal["role"] != "Worker":
        raise c.SupportError("role_effect_denied", "Only the directly activated Worker can perform Writer effects", [], [])
    intent_path = store.root / "requests" / (key + ".intent.json")
    with store._lock("scope:" + _product(runtime)), store._lock("target:" + str(path), nonblocking=True):
        old = _marker(store, intent_path)
        if old is not None:
            return _write_recovery(runtime, store, request, old, path, target)
        _fresh(runtime, store, request, c.as_object(plan["recheck"]))
        before = _target_state(path)
        expected = target["sha256"]
        if before["sha256"] != expected or (expected is None and before["exists"] is not False):
            raise c.SupportError("target_conflict", "Writer target preimage changed inside the target lock", [before], [])
        try:
            raw = base64.b64decode(c.text(payload["intended_base64"]), validate=True)
        except ValueError as error:
            raise c.SupportError("contract_violation", "Writer plan postimage encoding is invalid", [], []) from error
        if _hash(raw) != payload["intended_sha256"]:
            raise c.SupportError("digest_mismatch", "Writer plan postimage bytes disagree", [], [])
        intent: c.Object = {"schema": "a_c.fd-support.writer-intent/1", "request": request, "plan": payload, "recheck": plan["recheck"], "preimage": before}
        envelope, intent_ref = _artifact(runtime, request, "raw", intent)
        _mark(store, intent_path, envelope, "writer_intent")
        started = time.time_ns()
        try:
            _fault("writer:before_target_publication")
            _atomic(path, raw, tag="writer_target", replace=before["exists"] is True, mode=c.integer(before["mode"]) if before["mode"] is not None else 0o600)
            _fault("writer:after_target_publication")
            after = _target_state(path)
            if after["sha256"] != payload["intended_sha256"]:
                raise c.SupportError("effect_completion_unknown", "Actual target postimage does not establish the intended record", [after], [])
            result: c.Object = {"schema": "a_c.fd-support.writer-result/1", "intent": intent_ref, "target": target, "preimage": before, "postimage": after, "record": payload["record"], "interpretation": payload["interpretation"], "grant_id": payload["grant_id"], "effect": {"value": "completed", "core_value": "satisfied", "end_established": True, "scope": "one qualified atomic target-file publication", "observed_interval": {"started_ns": started, "ended_ns": time.time_ns(), "clock": "unix_ns"}}}
            _fault("writer:before_result_observation")
            result_envelope, ref = _artifact(runtime, request, "raw", result, started=started)
            store.retain(result_envelope)
            _fault("writer:after_result_observation")
            return _ok(request, result, [result_envelope], ref)
        except (OSError, c.SupportError) as error:
            state = _target_state(path)
            detail = error.document() if isinstance(error, c.SupportError) else {"external_failure": str(error)}
            outcome = c.refusal_outcome(runtime, request, c.SupportError("effect_completion_unknown", "Writer publication/evidence is not fully established; no rollback or retry occurred", [{"intent": intent_ref, "current": state, "failure": detail}], []))
            outcome["result"] = {"artifact": intent_ref, "value": {"current": state, "intended_sha256": payload["intended_sha256"], "repeated": False}}
            return outcome


def _attempt(runtime: c.Runtime, ref: c.Object) -> tuple[c.Object, c.Object]:
    envelope = c.load_artifact(runtime, ref, "attempt")
    payload = c.as_object(envelope["payload"], "Attempt")
    if payload.get("schema") != "a_c.fd-support.attempt/1":
        raise c.SupportError("basis_missing", "Not a complete Attempt anchor", [], [])
    return envelope, payload


def _events(runtime: c.Runtime, store: EvidenceStore, ref: c.Object) -> tuple[list[c.Object], list[c.JSON]]:
    query = store.query_artifacts("raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.attempt.id": ref["id"]})
    events = [c.load_artifact(runtime, c.as_object(item), "raw") for item in c.as_list(query["refs"])]
    events.sort(key=lambda event: c.integer(c.as_object(event["payload"])["cursor"]))
    gaps = list(c.as_list(query["gaps"]))
    previous: c.Object | None = None
    for index, event in enumerate(events):
        payload = c.as_object(event["payload"])
        if payload["attempt"] != ref or payload["cursor"] != index + 1 or payload["previous"] != previous:
            gaps.append({"event_chain_gap_or_conflict": payload})
        previous = {"id": "sha256:" + c.digest(event), "sha256": c.digest(event)}
    return events, gaps


def _sink(runtime: c.Runtime, store: EvidenceStore, request: c.Object, anchor: c.Object, event: c.Object, ref: c.Object) -> None:
    _policy_current(runtime)
    notification = c.as_object(anchor["notification"])
    binding = c.as_object(notification["binding"])
    sink_id = c.text(notification["sink_id"])
    registered = c.as_object(c.as_object(runtime.policy["event_sinks"])[sink_id])
    if binding != registered:
        raise c.SupportError("basis_stale", "Sealed notification sink binding changed", [sink_id], [])
    c.read_source(runtime, c.as_object(binding["authority_source"]))
    if binding["kind"] != "durable-file-events" or binding["retention"] != "indefinite":
        raise c.SupportError("unsupported_contract", "Unsupported registered sink", [sink_id], [])
    relative = Path(c.text(binding["directory"]))
    if relative.is_absolute() or any(part in ("", ".", "..") for part in c.text(binding["directory"]).split("/")):
        raise c.SupportError("path_refused", "Sink path escapes its protected root", [], [])
    directory = store.root / relative
    _directory(directory, create=True)
    payload: c.Object = {"schema": "a_c.fd-support.notification/1", "consumer": binding["consumer"], "attempt": event["attempt"], "event": ref, "kind": event["kind"], "cursor": event["cursor"], "delivery": "local-publication-only", "consumption": "unobserved"}
    envelope, _ = _artifact(runtime, request, "raw", payload, attempt=c.as_object(event["attempt"]))
    store.retain(envelope)
    path = directory / (c.text(c.as_object(event["attempt"])["sha256"]) + "-" + str(event["cursor"]) + ".json")
    try:
        _atomic(path, c.canonical(envelope), tag="sink")
    except FileExistsError:
        if _regular(path) != c.canonical(envelope):
            raise c.SupportError("target_conflict", "Notification cursor conflict", [], [])


def _event(runtime: c.Runtime, store: EvidenceStore, request: c.Object, ref: c.Object, kind: str, data: c.Object, *, notify: bool = True) -> c.Object:
    _, anchor = _attempt(runtime, ref)
    with store._lock("event:" + c.text(ref["id"])):
        events, gaps = _events(runtime, store, ref)
        if gaps:
            raise c.SupportError("history_incomplete", "Cannot append to incomplete Attempt event chain", gaps, [])
        previous: c.JSON = None if not events else {"id": "sha256:" + c.digest(events[-1]), "sha256": c.digest(events[-1])}
        payload: c.Object = {"schema": "a_c.fd-support.attempt-event/1", "attempt": ref, "cursor": len(events) + 1, "kind": kind, "data": data, "previous": previous, "observed_at_ns": time.time_ns()}
        envelope, event_ref = _artifact(runtime, request, "raw", payload, target=cast(str, anchor["target"]), attempt=ref)
        store.retain(envelope)
    if notify:
        try:
            _sink(runtime, store, request, anchor, payload, event_ref)
        except (OSError, c.SupportError) as error:
            failure = error.document() if isinstance(error, c.SupportError) else {"external_failure": str(error)}
            _event(runtime, store, request, ref, "notification_failure", {"event": event_ref, "failure": failure, "fallback": "events.wait with caller-declared finite scope", "consumer_receipt": "unknown"}, notify=False)
    return event_ref


def _observe(runtime: c.Runtime, store: EvidenceStore, request: c.Object) -> c.CoreOutcome:
    args = c.as_object(request["arguments"])
    ref = _ref(args["attempt"])
    _, anchor = _attempt(runtime, ref)
    events, gaps = _events(runtime, store, ref)
    cursor = c.integer(args["after_event"])
    selected: list[c.JSON] = []
    process_end: c.JSON = None
    effect: c.JSON = {"value": "completion_unknown", "core_value": "indeterminate", "end_established": False, "residuals": ["No qualified intended-effect completion observation.", "Descendant/external end is unobserved."]}
    output: c.JSON = None
    for envelope in events:
        payload = c.as_object(envelope["payload"])
        if c.integer(payload["cursor"]) > cursor:
            selected.append(payload)
        if payload["kind"] == "output_finalized":
            data = c.as_object(payload["data"])
            process_end = data["process_end"]
            output = data
        elif payload["kind"] == "effect_observation":
            effect = c.as_object(payload["data"])["effect"]
    value: c.Object = {"attempt": ref, "anchor": anchor, "events": selected, "cursor": len(events), "process_end": process_end, "output": output, "effect": effect, "history_gaps": gaps, "consumer_receipt": "unknown", "limits": ["Process exit alone proves neither intended outcome nor descendant/external end."]}
    return _ok(request, value)


def _cancel(runtime: c.Runtime, store: EvidenceStore, request: c.Object) -> c.CoreOutcome:
    args = c.as_object(request["arguments"])
    ref = _ref(args["attempt"])
    _, anchor = _attempt(runtime, ref)
    receipt = c.as_object(c.load_artifact(runtime, c.as_object(anchor["preflight"]), "preflight")["payload"])
    grant = c.as_object(c.as_object(runtime.policy["grants"])[c.text(receipt["grant_id"])])
    if runtime.principal_id not in c.as_list(grant["principals"]) or "dispatch.cancel" not in c.as_list(grant["operations"]):
        raise c.SupportError("authority_missing", "Existing attempt grant does not authorize this cancellation requester", [], [])
    for authority in c.as_list(grant["authority_sources"]):
        c.read_source(runtime, c.as_object(authority))
    prior = store.query_artifacts("raw", {"payload.schema": "a_c.fd-support.attempt-event/1", "payload.attempt.id": ref["id"], "payload.kind": "cancel_requested", "provenance.request_sha256": c.digest(request)})
    prior_refs = c.as_list(prior["refs"])
    if prior["complete"] is not True:
        raise c.SupportError("history_incomplete", "Cancellation history cannot establish exact replay", c.as_list(prior["gaps"]), [])
    if len(prior_refs) > 1:
        raise c.SupportError("basis_ambiguous", "Conflicting cancellation identities require reconciliation", prior_refs, [])
    if prior_refs:
        return _ok(request, {"attempt": ref, "request_event": prior_refs[0], "effect": "completion_unknown", "end_established": False, "limits": ["Existing cancellation request returned without another signal request."]})
    event = _event(runtime, store, request, ref, "cancel_requested", {"reason": args["reason"], "requester": runtime.principal_id, "signal_delivery": "not-yet-observed", "end_established": False})
    return _ok(request, {"attempt": ref, "request_event": event, "effect": "completion_unknown", "end_established": False, "limits": ["The live supervisor may deliver the request; cancellation is not completion or rollback."]})


def _wait(runtime: c.Runtime, store: EvidenceStore, request: c.Object) -> c.CoreOutcome:
    args = c.as_object(request["arguments"])
    timeout = c.integer(args["timeout_ms"])
    cadence = c.integer(args["cadence_ms"], "cadence_ms", 1)
    maximum = _limit(runtime, "max_wait_ms")
    minimum = _limit(runtime, "min_poll_ms")
    if (maximum is not None and timeout > maximum) or (minimum is not None and cadence < minimum):
        raise c.SupportError("budget_exceeded", "Bounded fallback exceeds selected deployment observation limits", [], [])
    c.text(args["purpose"], "fallback purpose")
    c.text(args["stop_condition"], "fallback stop_condition")
    end = time.monotonic_ns() + timeout * 1_000_000
    while True:
        observation_request = request.copy()
        observation_request["arguments"] = {"attempt": args["attempt"], "after_event": args["after_event"]}
        outcome = _observe(runtime, store, observation_request)
        result = c.as_object(c.as_object(outcome["result"])["value"])
        if c.as_list(result["events"]) or time.monotonic_ns() >= end:
            result["fallback"] = {"purpose": args["purpose"], "stop_condition": args["stop_condition"], "timeout_ms": timeout, "cadence_ms": cadence, "timed_out": not c.as_list(result["events"])}
            return _ok(request, result)
        remaining = max(0, end - time.monotonic_ns())
        time.sleep(min(cadence * 1_000_000, remaining) / 1_000_000_000)


def _pin(path: Path) -> c.Object:
    actual = path.resolve(strict=True)
    return {"path": str(actual), "sha256": _hash(_regular(actual))}


def _verify_pin(pin: c.Object) -> Path:
    path = Path(c.text(pin["path"]))
    if _hash(_regular(path)) != pin["sha256"]:
        raise c.SupportError("dependency_changed", "Pinned executable/helper bytes changed", [pin], [])
    return path


def _supervisor_binding(runtime: c.Runtime, ref: c.Object) -> c.Object:
    directory = Path(__file__).resolve().parent
    python = _pin(Path(sys.executable))
    modules: list[c.JSON] = [_pin(directory / name) for name in ("ac_support.py", "ac_support_core.py", "ac_support_effects.py")]
    entry = directory / "ac_support.py"
    argv: list[c.JSON] = [python["path"], str(entry), "_supervise", "--policy", str(runtime.policy_path), "--policy-sha256", runtime.policy_sha256, "--principal", runtime.principal_id, "--attempt-id", ref["id"], "--attempt-sha256", ref["sha256"]]
    return {"python": python, "modules": modules, "argv_template": "fixed-private-entry-with-anchor", "startup": {"python": str(Path(sys.executable)), "policy": str(runtime.policy_path), "policy_sha256": runtime.policy_sha256, "principal": runtime.principal_id}, "argv": argv}


def _verify_supervisor(binding: c.Object, runtime: c.Runtime, ref: c.Object) -> list[str]:
    python = _verify_pin(c.as_object(binding["python"]))
    directory = Path(__file__).resolve().parent
    pins = [c.as_object(item) for item in c.as_list(binding["modules"])]
    expected = {str((directory / name).resolve()) for name in ("ac_support.py", "ac_support_core.py", "ac_support_effects.py")}
    if {c.text(item["path"]) for item in pins} != expected or len(pins) != 3:
        raise c.SupportError("dependency_changed", "Supervisor module population differs from the sealed shipped entry", [], [])
    for item in pins:
        _verify_pin(item)
    # The anchor cannot contain its own digest. Only the fixed anchor coordinate
    # suffix is instantiated here; interpreter/module/content pins never change.
    argv = [str(python), str(directory / "ac_support.py"), "_supervise", "--policy", str(runtime.policy_path), "--policy-sha256", runtime.policy_sha256, "--principal", runtime.principal_id, "--attempt-id", c.text(ref["id"]), "--attempt-sha256", c.text(ref["sha256"])]
    return argv


def _executor(runtime: c.Runtime, executor_id: str) -> c.Object:
    registry = c.as_object(runtime.policy["executors"])
    if executor_id not in registry:
        raise c.SupportError("unsupported_executor", "Executor is not registered", [executor_id], [])
    executor = c.as_object(registry[executor_id])
    _verify_pin(c.as_object(executor["executable"]))
    argv = c.as_list(executor["argv"])
    if not argv or any(not isinstance(item, str) for item in argv):
        raise c.SupportError("contract_violation", "Registered executor must supply complete fixed string argv", [], [])
    environment = c.as_object(executor["environment"])
    if any(not isinstance(value, str) for value in environment.values()):
        raise c.SupportError("contract_violation", "Registered environment must be an exact string map", [], [])
    _directory(Path(c.text(executor["cwd"])))
    for value in c.as_list(executor["observers"]):
        observer = c.as_object(value, "registered observer")
        if observer.get("kind") == "process-end":
            c.exact_keys(observer, ("kind",), label="process-end observer")
        elif observer.get("kind") == "file-postimages":
            c.exact_keys(observer, ("kind", "scope", "expected"), label="file-postimages observer")
            c.as_list(observer["scope"])
            for expected in c.as_list(observer["expected"]):
                c.validate_content(expected, "SourceRef")
        else:
            raise c.SupportError("unsupported_executor", "Unknown registered observation capability", [observer.get("kind")], [])
    return executor


def _postimages(runtime: c.Runtime, store: EvidenceStore, request: c.Object, ref: c.Object, executor: c.Object) -> None:
    for value in c.as_list(executor["observers"]):
        observer = c.as_object(value)
        if observer["kind"] != "file-postimages":
            continue
        scope = c.as_list(observer["scope"])
        observation = c.observe(runtime, scope)
        checks: list[c.JSON] = []
        for expected_value in c.as_list(observer["expected"]):
            expected = c.as_object(expected_value)
            if expected["engine"] != "workspace-regular-file" or expected["selector"] is not None:
                raise c.SupportError("unsupported_executor", "Postimage observer supports exact whole regular files", [], [])
            relative = Path(c.text(expected["path"]))
            if not any(c.as_object(item)["root"] == expected["root"] and (c.as_object(item)["path"] == expected["path"] or (c.as_object(item)["kind"] == "directory" and relative.is_relative_to(Path(c.text(c.as_object(item)["path"]))))) for item in scope):
                raise c.SupportError("contract_violation", "Expected postimage is outside the declared observer scope", [expected], [])
            actual = next((c.as_object(item) for item in c.as_list(observation["entries"]) if c.as_object(item)["root"] == expected["root"] and c.as_object(item)["path"] == expected["path"]), None)
            holds = actual is not None and actual.get("sha256") == expected["sha256"] and actual.get("type") == "file"
            checks.append({"expected": expected, "actual": actual, "core_value": "satisfied" if holds else "falsified", "predicate": "exact declared regular-file postimage equality"})
        _event(runtime, store, request, ref, "file_postimages_observed", {"observation": observation, "checks": checks, "limits": ["File equality is a scoped observed predicate; it does not establish semantic work or all descendant/external effect end."]})


def _reconcile(runtime: c.Runtime, predecessor: c.Object, evidence: c.Object, grant: c.Object, context: c.Object) -> c.Object:
    selected = c.as_object(c.as_object(context["packet"])["subject_basis"])
    basis: c.Object = {"method_profile": selected["method_profile"], "observations": selected["observations"]}
    return c.verify_reconciliation(runtime, evidence, predecessor, grant, basis)


def _activation_attempts(runtime: c.Runtime, store: EvidenceStore, packet: c.Object) -> list[c.JSON]:
    # Context envelopes include acquisition/provenance observations. Reassembly
    # can change their artifact identity without changing the activated Packet.
    # Derive the source-owned identity through retained Contexts, including old
    # anchors; an absent optional index must never look like absent history.
    history = store.query_artifacts("attempt", {})
    if history["complete"] is not True:
        raise c.SupportError("history_incomplete", "Cannot establish activation attempt population", c.as_list(history["gaps"]), [])
    identity = c.activation_identity(packet)
    previous: list[c.JSON] = []
    for value in c.as_list(history["refs"]):
        ref = _ref(value)
        try:
            _, anchor = _attempt(runtime, ref)
            context = c.as_object(c.load_artifact(runtime, _ref(anchor.get("context")), "context")["payload"])
            retained = c.as_object(context.get("packet"), "retained Attempt Packet")
            c.text(c.as_object(retained.get("activation"), "retained activation").get("id"), "retained activation id")
            if c.activation_identity(retained) == identity:
                previous.append(ref)
        except c.SupportError as error:
            raise c.SupportError("history_incomplete", "Retained Attempt activation identity is unavailable", [ref, error.document()], []) from error
    return previous


def _dispatch(runtime: c.Runtime, store: EvidenceStore, request: c.Object, key: str) -> c.CoreOutcome:
    args = c.as_object(request["arguments"])
    receipt_ref = _ref(args["preflight"])
    receipt_envelope = c.load_artifact(runtime, receipt_ref, "preflight")
    receipt = c.as_object(receipt_envelope["payload"])
    if receipt.get("contract_state") != "admitted" or receipt.get("decision") != "admitted":
        raise c.SupportError("authority_missing", "Dispatch requires an actual admitted complete receipt", [receipt_ref], [])
    if receipt["requester"] != runtime.principal_id or c.as_object(receipt_envelope["provenance"])["policy_sha256"] != runtime.policy_sha256:
        raise c.SupportError("authority_missing", "Receipt is bound to another requester/policy", [], [])
    old = _marker(store, store.root / "requests" / (key + ".attempt.json"))
    if old is not None:
        ref: c.Object = {"id": "sha256:" + c.digest(old), "sha256": c.digest(old)}
        return _ok(request, {"attempt": ref, "reservation": "existing", "launch": "consult retained observations; never repeated"}, reference=ref)
    grant = c.as_object(c.as_object(runtime.policy["grants"])[c.text(receipt["grant_id"])])
    if "dispatch.start" not in c.as_list(grant["operations"]) or runtime.principal_id not in c.as_list(grant["principals"]):
        raise c.SupportError("authority_missing", "Selected grant does not permit this dispatch requester", [], [])
    target = c.text(receipt["target"])
    if target not in c.as_list(grant["targets"]):
        raise c.SupportError("authority_missing", "Activated target is not granted", [], [])
    context_ref = _ref(receipt["context"])
    context = c.as_object(c.load_artifact(runtime, context_ref, "context")["payload"])
    packet = c.as_object(context["packet"])
    executor_id = c.text(receipt["executor_id"])
    executor = _executor(runtime, executor_id)
    sink_id = grant["notification_sink"]
    if not isinstance(sink_id, str) or sink_id not in c.as_object(runtime.policy["event_sinks"]):
        raise c.SupportError("contract_violation", "Dispatch requires its exact Grant-selected sink", [], [])
    sink = c.as_object(c.as_object(runtime.policy["event_sinks"])[sink_id])
    if sink["consumer"] != c.as_object(packet["evidence_relations"])["consumer"]:
        raise c.SupportError("contract_violation", "Sink consumer differs from the activated return consumer", [], [])
    rendered = cast(str, context["rendered_utf8"]).encode("utf-8")
    if _hash(rendered) != context["rendered_sha256"]:
        raise c.SupportError("digest_mismatch", "Retained Context rendering changed", [], [])
    activation = c.as_object(packet["activation"])
    with store._lock("activation:" + c.text(activation["id"])):
        previous = _activation_attempts(runtime, store, packet)
        retry = args.get("retry_of")
        reconciliation = args.get("reconciliation")
        if previous and retry is None:
            raise c.SupportError("effect_unreconciled", "A new attempt of this activation requires its predecessor and reconciliation", previous, [])
        if retry is not None:
            predecessor = _ref(retry)
            if predecessor not in previous or reconciliation is None:
                raise c.SupportError("effect_unreconciled", "Retry does not bind an existing predecessor/reconciliation", [], [])
            _reconcile(runtime, predecessor, _ref(reconciliation), grant, context)
        with store._lock("scope:" + _product(runtime)):
            _fresh(runtime, store, request, c.as_object(receipt["recheck"]))
            # Seal own-code/startup pins before the immutable anchor exists.
            # Anchor arguments are a fixed template, instantiated after hashing.
            binding = _supervisor_binding(runtime, {"id": "anchor-coordinate", "sha256": "anchor-coordinate"})
            binding["argv"] = [*c.as_list(binding["argv"])[:-4], "--attempt-id", "<immutable-anchor-id>", "--attempt-sha256", "<immutable-anchor-sha256>"]
            invocation: c.Object = {"executable": executor["executable"], "argv": executor["argv"], "cwd": executor["cwd"], "environment": executor["environment"], "settings": executor["settings"], "stdin_sha256": context["rendered_sha256"], "stdin_bytes": len(rendered), "supervisor": binding}
            anchor: c.Object = {"schema": "a_c.fd-support.attempt/1", "preflight": receipt_ref, "context": context_ref, "request": request, "requester": runtime.principal_id, "target": target, "executor": executor_id, "invocation": invocation, "notification": {"sink_id": sink_id, "binding": sink}, "result_key": receipt["result_key"], "retry_of": retry, "reconciliation": reconciliation}
            envelope, reference = _artifact(runtime, request, "attempt", anchor, target=target)
            _mark(store, store.root / "requests" / (key + ".attempt.json"), envelope, "attempt_reservation")
        _event(runtime, store, request, reference, "reserved", {"invocation": invocation, "launch": "not-yet-established"})
        argv = _verify_supervisor(binding, runtime, reference)
        diagnostics = store.root / "diagnostics"
        prefix = c.text(reference["sha256"])
        try:
            _fault("supervisor:before_spawn")
            with open(diagnostics / (prefix + ".stdout"), "xb") as out, open(diagnostics / (prefix + ".stderr"), "xb") as err:
                process = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=out, stderr=err, cwd=str(Path(__file__).resolve().parent), env={"PATH": os.defpath}, start_new_session=True, close_fds=True)
                # This local reaper only releases a Popen OS resource. Durable
                # Attempt/events remain the sole reconstruction evidence.
                threading.Thread(target=process.wait, name="a_c-supervisor-reaper", daemon=True).start()
            _fault("supervisor:after_spawn")
            _event(runtime, store, request, reference, "supervisor_spawned", {"pid": process.pid, "argv": cast(c.JSON, argv), "actor_launch": "not-established-by-supervisor-receipt"})
        except (OSError, c.SupportError) as error:
            failure = error.document() if isinstance(error, c.SupportError) else {"external_failure": str(error)}
            _event(runtime, store, request, reference, "supervisor_launch_uncertain", {"failure": failure, "effect": "completion_unknown", "repeat_permitted": False})
        return _ok(request, {"attempt": reference, "reservation": "complete", "launch": "consult retained observations", "unknowns": ["Supervisor receipt is not an actor result or external completion."]}, [envelope], reference)


def execute_effect(runtime: c.Runtime, request: c.Object, plan: c.EffectPlan | None) -> c.CoreOutcome:
    """Public effect boundary; Writer plans follow locked authority/history."""
    request = c.validate_request(request)
    operation = c.text(request["operation"])
    c.require_operation(runtime, operation)
    _policy_current(runtime)
    if operation not in ("contract.preflight", "dispatch.start", "dispatch.observe", "dispatch.cancel", "events.wait", "work.write"):
        raise c.SupportError("unsupported_contract", "Operation is not a named effect entry", [operation], [])
    if operation == "contract.preflight":
        if plan is None:
            raise c.SupportError("basis_missing", "Named effect requires its core-prepared plan", [], [])
        _check_plan(runtime, request, plan)
    elif plan is not None:
        raise c.SupportError("contract_violation", "This named effect accepts no plan", [], [])
    runtime, store = _bound(runtime)
    with store._lock("request:" + _key(runtime, request)):
        if operation == "work.write":
            c.check_writer_authority(runtime, request)
        key = _claim(runtime, store, request)
        if operation == "work.write":
            claim = _marker(store, store.root / "requests" / (key + ".claim.json"))
            if claim is None:
                raise c.SupportError("history_incomplete", "Writer claim is unavailable after reservation", [], [])
            _verify_support_graph(store, _references(claim))
        previous = _completed(runtime, store, request, key)
        if previous is not None:
            if operation == "work.write":
                _verify_support_graph(store, _outcome_support(operation, previous))
            return previous
        try:
            if operation == "contract.preflight":
                outcome = _preflight(runtime, store, request, cast(c.EffectPlan, plan))
            elif operation == "work.write":
                recovered = _recover_write(runtime, store, request, key)
                if recovered is None:
                    # Planning can acquire sources/history. It runs inside the
                    # identity lock, before any Product/target/publication lock.
                    prepared = c.prepare_write(runtime, request)
                    _check_plan(runtime, request, prepared)
                    outcome = _write(runtime, store, request, prepared, key)
                else:
                    outcome = recovered
            elif operation == "dispatch.start":
                outcome = _dispatch(runtime, store, request, key)
            elif operation == "dispatch.observe":
                outcome = _observe(runtime, store, request)
            elif operation == "dispatch.cancel":
                outcome = _cancel(runtime, store, request)
            else:
                outcome = _wait(runtime, store, request)
            return _complete(runtime, store, request, key, outcome)
        except c.SupportError as error:
            return c.refusal_outcome(runtime, request, error)
        except OSError as error:
            return c.refusal_outcome(runtime, request, c.SupportError("observation_unavailable", "Named effect observation failed; intent/partial effects remain retained", [str(error)], []))


def supervise(runtime: c.Runtime, attempt_ref: c.Object) -> int:
    """Private fixed-CLI reentry. Its integer is only an OS exit code."""
    runtime, store = _bound(runtime)
    ref = _ref(attempt_ref)
    _, anchor = _attempt(runtime, ref)
    request = c.validate_request(anchor["request"])
    if request["operation"] != "dispatch.start" or anchor["requester"] != runtime.principal_id:
        raise c.SupportError("authority_missing", "Supervisor anchor does not bind this requester/dispatch", [], [])
    receipt_envelope = c.load_artifact(runtime, c.as_object(anchor["preflight"]), "preflight")
    receipt = c.as_object(receipt_envelope["payload"])
    context = c.as_object(c.load_artifact(runtime, c.as_object(anchor["context"]), "context")["payload"])
    invocation = c.as_object(anchor["invocation"])
    _verify_supervisor(c.as_object(invocation["supervisor"]), runtime, ref)
    with store._lock("supervision:" + c.text(ref["id"]), nonblocking=True):
        events, gaps = _events(runtime, store, ref)
        if gaps:
            raise c.SupportError("history_incomplete", "Supervisor cannot rely on incomplete event history", gaps, [])
        if any(c.as_object(event["payload"])["kind"] in ("actor_launch_intent", "actor_started", "output_finalized") for event in events):
            return 0  # Existing uncertain/observed launch is never repeated.
        if any(c.as_object(event["payload"])["kind"] == "cancel_requested" for event in events):
            _event(runtime, store, request, ref, "cancel_observed", {"launch": "not-performed", "end_established": False, "scope": "Cancellation observed before any retained launch intent; no child started by this reentry."})
            return 0
        if receipt.get("decision") != "admitted" or receipt.get("contract_state") != "admitted":
            raise c.SupportError("authority_missing", "Supervisor requires the admitted receipt", [], [])
        grant = c.as_object(c.as_object(runtime.policy["grants"])[c.text(receipt["grant_id"])])
        if runtime.principal_id not in c.as_list(grant["principals"]) or anchor["target"] not in c.as_list(grant["targets"]):
            raise c.SupportError("authority_missing", "Current grant does not bind requester and target", [], [])
        sink = c.as_object(c.as_object(runtime.policy["event_sinks"])[c.text(grant["notification_sink"])])
        if anchor["notification"] != {"sink_id": grant["notification_sink"], "binding": sink}:
            raise c.SupportError("basis_stale", "Current Grant sink differs from the immutable anchor", [], [])
        executor = _executor(runtime, c.text(anchor["executor"]))
        for name in ("executable", "argv", "cwd", "environment", "settings"):
            if invocation[name] != executor[name]:
                raise c.SupportError("dependency_changed", "Registered invocation differs from the sealed anchor", [name], [])
        raw = cast(str, context["rendered_utf8"]).encode("utf-8")
        if _hash(raw) != invocation["stdin_sha256"] or len(raw) != invocation["stdin_bytes"]:
            raise c.SupportError("digest_mismatch", "Actual stdin differs from its sealed Context", [], [])
        process: subprocess.Popen[bytes] | None = None
        try:
            # Quiescence guards this actual launch edge. Holding it throughout
            # actor thought/IO would deadlock an independently granted Writer
            # invoked through the actor's own public tool child.
            with store._lock("scope:" + _product(runtime)):
                _fresh(runtime, store, request, c.as_object(receipt["recheck"]))
                _verify_supervisor(c.as_object(invocation["supervisor"]), runtime, ref)
                if anchor["retry_of"] is not None:
                    checked = _reconcile(runtime, _ref(anchor["retry_of"]), _ref(anchor["reconciliation"]), grant, context)
                    _event(runtime, store, request, ref, "reconciliation_verified", checked)
                _event(runtime, store, request, ref, "actor_launch_intent", {"invocation": invocation, "external_effect": "not-transactionally-coupled-to-evidence"})
                _fault("actor:before_spawn")
                process = subprocess.Popen([c.text(item) for item in c.as_list(executor["argv"])], executable=c.text(c.as_object(executor["executable"])["path"]), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=c.text(executor["cwd"]), env={key: cast(str, value) for key, value in c.as_object(executor["environment"]).items()}, start_new_session=True, close_fds=True)
                _fault("actor:after_spawn")
                _event(runtime, store, request, ref, "actor_started", {"pid": process.pid, "executable": executor["executable"], "settings": executor["settings"], "receipt_scope": "local-process-start-only"})
            # The per-Attempt supervision lock still spans the invocation; only
            # the Product input/Writer lock has ended here.
            return _run_process(runtime, store, request, ref, anchor, executor, process, raw)
        except (OSError, c.SupportError) as error:
            if process is not None:
                # A lost post-spawn observation cannot be retried. Close
                # this wrapper's pipe handles, preserving uncertainty over
                # whatever the actual child/descendants may still do.
                for pipe in (process.stdin, process.stdout, process.stderr):
                    if pipe is not None and not pipe.closed:
                        pipe.close()
                threading.Thread(target=process.wait, name="a_c-uncertain-child-reaper", daemon=True).start()
            failure = error.document() if isinstance(error, c.SupportError) else {"external_failure": str(error)}
            _event(runtime, store, request, ref, "exception", {"failure": failure, "effect": "completion_unknown", "descendant_end": "unknown", "automatic_retry": False})
            return 1


def _run_process(runtime: c.Runtime, store: EvidenceStore, request: c.Object, ref: c.Object, anchor: c.Object, executor: c.Object, process: subprocess.Popen[bytes], stdin: bytes) -> int:
    started = time.time_ns()
    assert process.stdin is not None and process.stdout is not None and process.stderr is not None
    selector = selectors.DefaultSelector()
    for stream, name, mode in ((process.stdin, "stdin", selectors.EVENT_WRITE), (process.stdout, "stdout", selectors.EVENT_READ), (process.stderr, "stderr", selectors.EVENT_READ)):
        os.set_blocking(stream.fileno(), False)
        selector.register(stream, mode, name)
    output = {"stdout": bytearray(), "stderr": bytearray()}
    totals = {"stdout": 0, "stderr": 0}
    truncated = {"stdout": False, "stderr": False}
    offset = 0
    input_started: int | None = None
    signaled = False
    settings = c.as_object(executor["settings"])
    duration = settings.get("timeout_ms")
    timeout = None if duration is None else c.integer(duration, "executor timeout_ms", 1)
    maximum = _limit(runtime, "max_attempt_ms")
    if maximum is not None:
        timeout = maximum if timeout is None else min(timeout, maximum)
    cap = _limit(runtime, "max_output_bytes")
    grace_value = settings.get("termination_grace_ms")
    grace = None if grace_value is None else c.integer(grace_value, "termination_grace_ms", 1)
    sent_at: int | None = None
    tick = (_limit(runtime, "min_poll_ms") or 100) / 1000
    try:
        while selector.get_map() or process.poll() is None:
            now = time.time_ns()
            timed_out = timeout is not None and now - started >= timeout * 1_000_000
            events, gaps = _events(runtime, store, ref)
            cancelled = any(c.as_object(event["payload"])["kind"] == "cancel_requested" for event in events)
            if (timed_out or cancelled) and not signaled and process.poll() is None:
                _event(runtime, store, request, ref, "deadline" if timed_out else "cancel_observed", {"signal": "SIGTERM-request", "end_established": False, "partial_output": True})
                process.terminate()
                sent_at = time.time_ns()
                signaled = True
                _event(runtime, store, request, ref, "signal_delivery", {"signal": "SIGTERM", "scope": "Popen local process", "end_established": False})
            if sent_at is not None and grace is not None and now - sent_at >= grace * 1_000_000 and process.poll() is None:
                process.kill()
                sent_at = None
                _event(runtime, store, request, ref, "signal_delivery", {"signal": "SIGKILL", "scope": "Popen local process", "end_established": False})
            for selected, _ in selector.select(tick):
                selected_stream = selected.fileobj
                name = cast(str, selected.data)
                fd = selected.fd
                if name == "stdin":
                    if input_started is None:
                        input_started = time.time_ns()
                    try:
                        written = os.write(fd, stdin[offset:offset + 65536]) if offset < len(stdin) else 0
                    except BrokenPipeError:
                        written = 0
                    offset += written
                    if offset >= len(stdin) or written == 0:
                        selector.unregister(selected_stream)
                        process.stdin.close()
                        _event(runtime, store, request, ref, "context_delivery", {"context": anchor["context"], "recipient": anchor["target"], "rendered_sha256": _hash(stdin), "bytes": offset, "complete": offset == len(stdin), "interval": {"started_ns": input_started, "ended_ns": time.time_ns(), "clock": "unix_ns"}, "scope": "local child stdin write; mental attention/remote consumer receipt unknown"})
                else:
                    try:
                        chunk = os.read(fd, 65536)
                    except BlockingIOError:
                        continue
                    if not chunk:
                        selector.unregister(selected_stream)
                        continue
                    totals[name] += len(chunk)
                    remaining = len(chunk) if cap is None else max(0, cap - len(output[name]))
                    output[name].extend(chunk[:remaining])
                    if remaining < len(chunk):
                        truncated[name] = True
                    _event(runtime, store, request, ref, "output_chunk", {"stream": name, "bytes_base64": base64.b64encode(chunk[:remaining]).decode("ascii"), "observed_bytes": len(chunk), "retained_bytes": min(remaining, len(chunk)), "complete_slot": False})
            if process.poll() is not None and selector.get_map():
                # Descendants may hold pipes open. Never wait indefinitely for
                # their EOF or infer their end from the observed parent's exit.
                # A prior signal cannot disable this path; selected timeout or
                # cancellation also bounds an always-readable descendant tail.
                if timed_out or cancelled or not selector.select(0):
                    for selected in list(selector.get_map().values()):
                        selector.unregister(selected.fileobj)
                    _event(runtime, store, request, ref, "pipe_tail_unknown", {"descendant_end": "unknown", "output_tail": "unobserved after parent process end"})
                    truncated["stdout"] = True
                    truncated["stderr"] = True
        returncode = process.wait()
    finally:
        selector.close()
        for stream in (process.stdin, process.stdout, process.stderr):
            if not stream.closed:
                stream.close()
    ended = time.time_ns()
    producer: c.Object = {"principal_id": anchor["target"], "actor": c.as_object(runtime.policy["principals"])[c.text(anchor["target"])], "executor_id": anchor["executor"], "executable": executor["executable"]}
    output_refs: c.Object = {}
    for name in ("stdout", "stderr"):
        payload: c.Object = {"schema": "a_c.fd-support.process-output/1", "attempt": ref, "stream": name, "slot": "final_stdout_object" if name == "stdout" else None, "bytes_base64": base64.b64encode(bytes(output[name])).decode("ascii"), "complete": not truncated[name], "decoder": executor["stdout_decoder"] if name == "stdout" else None, "producer": producer, "interval": {"started_ns": started, "ended_ns": ended, "clock": "unix_ns"}}
        envelope, output_ref = _artifact(runtime, request, "raw", payload, target=c.text(anchor["target"]), attempt=ref, started=started)
        store.retain(envelope)
        output_refs[name] = output_ref
    output_refs["process_end"] = {"observed": True, "returncode": returncode, "ended_ns": ended, "descendants": "unknown"}
    output_refs["observed_bytes"] = cast(c.JSON, totals)
    _fault("actor:before_final_output_observation")
    _event(runtime, store, request, ref, "output_finalized", output_refs)
    _fault("actor:after_final_output_observation")
    recheck = c.as_object(c.as_object(c.load_artifact(runtime, c.as_object(anchor["preflight"]), "preflight")["payload"])["recheck"])
    # Reacquire only for this finite post-effect observation. This reports its
    # actual interval; it does not pretend inputs were frozen during the actor.
    with store._lock("scope:" + _product(runtime)):
        current = c.check_preconditions(runtime, recheck)
        if c.as_list(current["changes"]) or c.as_list(current["gaps"]):
            _event(runtime, store, request, ref, "basis_change", current)
        _postimages(runtime, store, request, ref, executor)
        _event(runtime, store, request, ref, "effect_observation", {"effect": {"value": "completion_unknown", "core_value": "indeterminate", "end_established": False, "process_end_established": True, "residuals": ["Generic process/return does not establish intended semantic outcome or all external/descendant effect end."]}, "observations": current})
    resource: c.Object = {"schema": "a_c.fd-support.resource/1", "owner": {"kind": "attempt", "record": ref}, "samples": [], "interval": {"started_ns": started, "ended_ns": ended, "clock": "unix_ns"}, "gaps": ["Provider usage/cache/cost counters were not observed."]}
    resource_envelope, _ = _artifact(runtime, request, "resource", resource, target=c.text(anchor["target"]), attempt=ref, started=started)
    store.retain(resource_envelope)
    return 0
