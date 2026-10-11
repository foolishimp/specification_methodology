"""Local qualification fixture provider, not an STDO runtime or Product feature."""

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def transfer(state, request, permissions):
    """One selected finite relation; reject unsupported ownership/permission."""
    if state is None:
        return None, {"judgment": "indeterminate", "cause": "current state unavailable"}
    if set(state) != {"t0", "t1", "t2"} or any(v not in {"Ada", "Bea"} for v in state.values()):
        return deepcopy(state), {"judgment": "invalid_basis", "cause": "invalid token domain"}
    token = request["token"]
    required = (state.get(token), token, request["destination"], request["operation"])
    if request["source"] != state.get(token) or required not in permissions:
        return deepcopy(state), {"judgment": "falsified", "cause": "current-owner permission absent", "effect": False}
    result = deepcopy(state)
    result[token] = request["destination"]
    return result, {"judgment": "satisfied", "effect": True}


def admit_receipt(grant, request):
    fields = ("operation", "brief_sha256", "revision")
    if not grant.get("live") or any(grant.get(k) != request.get(k) for k in fields):
        return {"admitted": False, "cause": "no live exact operation/revision/subject grant", "effect": False}
    return {"admitted": True}


def issue_receipt(store, request, grant, lose_response=False):
    admission = admit_receipt(grant, request)
    if not admission["admitted"]:
        return admission
    rows = json.loads(store.read_text()) if store.exists() else []
    if any(row["operation"] == request["operation"] for row in rows):
        return {"admitted": False, "cause": "operation already observed; reconcile current receipt", "effect": False}
    rows.append(dict(request))
    save(store, rows)
    if lose_response:
        raise ConnectionError("controlled response loss after persistent receipt write")
    return {"admitted": True, "effect": True, "receipt": request}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=("tokens", "receipt"), required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--brief", type=Path)
    args = parser.parse_args()
    allowed = Path(__file__).resolve().parent
    out = args.out.resolve()
    if not out.is_relative_to(allowed) or out.exists():
        raise SystemExit("exclusive initially absent fixture output required")
    source = allowed.parent / "TASKS.md"
    source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
    if source_sha != "a97e1308b02b2bee9037f30b16b3826917feb8cb9f63bda4b0ff9467c380409a":
        raise SystemExit("task source drift")
    out.mkdir(parents=True)
    trace = {"source_sha256": source_sha, "started_utc": datetime.now(timezone.utc).isoformat(), "operations": []}
    if args.case == "tokens":
        initial = {"t0": "Ada", "t1": "Ada", "t2": "Bea"}
        cases = [
            ("positive", {"operation": "positive-t1", "source": "Ada", "token": "t1", "destination": "Bea"}, [("Ada", "t1", "Bea", "positive-t1")]),
            ("refusal", {"operation": "unpermitted-t2", "source": "Ada", "token": "t2", "destination": "Ada"}, [("Ada", "t2", "Ada", "unpermitted-t2")]),
            ("uncertain", {"operation": "uncertain-t0", "source": "Ada", "token": "t0", "destination": "Bea"}, [("Ada", "t0", "Bea", "uncertain-t0")]),
        ]
        for name, request, permissions in cases:
            directory = out / name
            save(directory / "initial.json", initial)
            save(directory / "request.json", request)
            save(directory / "permissions.json", permissions)
            current, response = transfer(initial, request, permissions)
            save(directory / "current.json", current)
            entry = {"branch": name, "request": request, "provider_result": response, "current_sha256": hashlib.sha256((directory / "current.json").read_bytes()).hexdigest()}
            if name == "uncertain":
                try:
                    raise ConnectionError("controlled response loss after persistent ownership write")
                except ConnectionError as exc:
                    entry["transport"] = str(exc)
                entry["consumer_access"] = "authoritative current locator withheld for selected interval"
            else:
                save(directory / "response.json", response)
            trace["operations"].append(entry)
    else:
        if args.brief is None:
            raise SystemExit("exact frozen brief required")
        brief_hash = hashlib.sha256(args.brief.read_bytes()).hexdigest()
        request = {"operation": "cost-v1-receipt", "brief_sha256": brief_hash, "revision": "cost-brief/source-v1", "currency": "AUD", "amounts": {"Harbor": "106.00", "Cove": "148.00"}}
        grant = {**request, "live": True}
        save(out / "grant.json", grant)
        save(out / "request.json", request)
        try:
            issue_receipt(out / "store.json", request, grant, lose_response=True)
        except ConnectionError as exc:
            trace["operations"].append({"request": request, "transport": str(exc), "store_sha256": hashlib.sha256((out / "store.json").read_bytes()).hexdigest()})
        wrong = {**request, "revision": "cost-brief/source-v2"}
        for occurrence in (1, 2):
            result = issue_receipt(out / "store.json", wrong, grant)
            trace["operations"].append({"occurrence": occurrence, "request": wrong, "admission": result})
    trace["finished_utc"] = datetime.now(timezone.utc).isoformat()
    save(out / "HARNESS.json", trace)
    print(json.dumps({"case": args.case, "out": str(out), "operations": len(trace["operations"]), "fixture_only": True}))


if __name__ == "__main__":
    main()
