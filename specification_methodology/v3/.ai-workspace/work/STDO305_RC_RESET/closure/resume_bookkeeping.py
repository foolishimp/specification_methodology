"""Continue the unchanged final transaction after classifying retained HTTP headers."""
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path

R = Path.cwd()
O = Path(__file__).resolve().parent
Q = O.parent
C = Q / "release-tools/cohort-002"
P = Q / "public-qualification-001"
G = ["git", "-c", "gc.auto=0", "-c", "maintenance.auto=false"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def ref(path):
    data = path.read_bytes()
    return {"path": str(path.relative_to(R)), "sha256": digest(data), "bytes": len(data),
            "mode": "100755" if path.stat().st_mode & 0o111 else "100644"}


def save(path, value):
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return ref(path)


def git(*args):
    result = subprocess.run([*G, *args], cwd=R, capture_output=True)
    assert result.returncode == 0, (args, result.stderr.decode())
    return result.stdout


def remote():
    raw = git("ls-remote", "--heads", "--tags", "https://github.com/foolishimp/specification_methodology.git")
    return raw, {line.split("\t")[1]: line.split("\t")[0] for line in raw.decode().splitlines()}


assert digest((O / "PLAN.json").read_bytes()) == "b8e54d6dfc091d385c4eb575d81ba1ab9fa1e90e8f56d41bc40e43683a77f358"
plan = load(O / "PLAN.json")
carrier = plan["parent"]
assert git("rev-parse", "HEAD").decode().strip() == carrier
assert os.statvfs(R).f_bavail * os.statvfs(R).f_frsize >= 2 * 1024**3
assert load(P / "LATEST_CONFIRMED.json")["status"] == "confirmed_latest"
for row in load(O / "PATHS.json")["files"]:
    assert ref(R / row["path"]) == row, row["path"]
expected = {p for p in (O / "stage-paths.z").read_bytes().split(b"\0") if p}
assert {p for p in git("diff", "--cached", "--name-only", "-z").split(b"\0") if p} == expected

warnings = [line for line in (O / "diff-check.txt").read_text().splitlines()
            if re.match(r"^[^+].+:\d+: ", line)]
warning_paths = {re.split(r":\d+: ", line, maxsplit=1)[0] for line in warnings}
headers = {str((P / "acquisition" / (name + ".headers")).relative_to(R)) for name in (
    "release.json", "stack-release-v3.0.5-rc.1.json", "stdo-manager-constraints-v3.0.5-rc.1-python313.txt",
    "stdo-manager-runtime-v3.0.5-rc.1-macos-arm64-cp313.zip", "stdo-v3.0.5-rc.1-manifest.json",
    "stdo_toolchain-3.0.5rc1-py3-none-any.whl")}
logs = {str((C / name).relative_to(R)) for name in (
    "manifest-reconciliation-001/diff-check.txt", "publication-execution/005-atomic-push/stderr.txt")}
assert warning_paths == headers | logs
for name in headers:
    assert b"\r\n" in (R / name).read_bytes()

selected = load(C / "manifest-reconciliation-002/RESULT.json")["selected"]
forms = load(C / "publication/OPERATION_TEMPLATES.json")
raw, before = remote()
assert all(before.get(k) == v for k, v in selected.items())
assert all(before.get(k) == v for k, v in forms["preserved_immutable_refs"].items())

additional = [Path(__file__).resolve(), O / "diff-check.txt", O / "remote-before.txt"]
continuation = save(O / "CONTINUATION.json", {
    "kind": "stdo.bookkeeping-operator-reconciliation/1", "parent": carrier,
    "original_plan": ref(O / "PLAN.json"), "original_stage_paths": len(expected),
    "observed_failure": {"returncode": 1, "stage": "before commit, after exact staging",
        "basis": "Observed tool output: final_bookkeeping.py line 73 refused acquisition/release.json.headers:1 trailing whitespace. Its suffix classifier omitted immutable HTTP headers; no Git commit or remote mutation occurred."},
    "disposition": "Apply the already authorized distinction for byte-preserved command evidence. The six curl header files retain HTTP CRLF, and the two raw log files retain their original bytes. No source whitespace defect, evidence rewrite or qualification change.",
    "warning_count": len(warnings), "accepted_exact_warning_paths": sorted(warning_paths),
    "additional_selected_files": [ref(p) for p in additional],
    "effects": "Same one bookkeeping commit, sole parent D, exact leased main push and remote/tracking verification; all immutable refs, B, assets and builder remain unchanged."})
additional.append(O / "CONTINUATION.json")
git("add", "-f", "--", *(str(p.relative_to(R)) for p in additional))
expected |= {str(p.relative_to(R)).encode() for p in additional}
assert {p for p in git("diff", "--cached", "--name-only", "-z").split(b"\0") if p} == expected
check = subprocess.run([*G, "diff", "--cached", "--check"], cwd=R, capture_output=True)
assert check.returncode == 2 and check.stdout == (O / "diff-check.txt").read_bytes()
print("CONTINUATION", continuation["sha256"], "STAGE_PATHS", len(expected), flush=True)
(O / "commit.stdout").write_bytes(git("commit", "-m", "Record public STDO 3.0.5 RC1 qualification and closure"))
commit = git("rev-parse", "HEAD").decode().strip()
assert git("show", "-s", "--format=%P", commit).decode().strip() == carrier
assert not git("diff", "--cached", "--name-only") and not git("diff", "--name-only")
assert digest((R / "stack_release.json").read_bytes()) == plan["preserve"]["manifest_sha256"]
assert all(git("rev-parse", name).decode().strip() == oid for name, oid in plan["preserve"]["refs"].items())
argv = [*G, "push", "--atomic", "--force-with-lease=refs/heads/main:" + carrier,
        "https://github.com/foolishimp/specification_methodology.git", commit + ":refs/heads/main"]
save(O / "push-invocation.json", {"argv": argv, "cwd": str(R), "parent": carrier, "commit": commit})
print("BOOKKEEPING_COMMIT", commit, flush=True)
with (O / "push.stdout").open("xb") as out, (O / "push.stderr").open("xb") as err:
    result = subprocess.run(argv, cwd=R, stdout=out, stderr=err)
save(O / "push-execution.json", {"returncode": result.returncode, "stdout": ref(O / "push.stdout"),
    "stderr": ref(O / "push.stderr"), "commit": commit})
assert result.returncode == 0, "Failed/uncertain push: preserve and reconcile, no automatic retry."
raw, after = remote()
(O / "remote-after.txt").write_bytes(raw)
assert after.get("refs/heads/main") == commit
assert all(after.get(k) == v for k, v in plan["preserve"]["refs"].items())
assert all(after.get(k) == v for k, v in forms["preserved_immutable_refs"].items())
git("fetch", "--no-tags", "origin", "main:refs/remotes/origin/main")
assert git("rev-parse", "origin/main").decode().strip() == commit
assert git("rev-list", "--left-right", "--count", "HEAD...origin/main").decode().strip() == "0\t0"
result = save(O / "GIT_COMPLETION.json", {"status": "pushed_verified", "bookkeeping_commit": commit,
    "release_carrier": carrier, "remote_main": after["refs/heads/main"], "tracking_main": commit,
    "ahead_behind": [0, 0], "continuation": continuation,
    "immutable_refs_unchanged": plan["preserve"]["refs"],
    "limits": "Selected navigation/evidence is committed and pushed. Unrelated inherited artifacts, private origins/runtime/cache and duplicate proof ZIPs remain preserved locally; no clean-worktree claim."})
print("GIT_COMPLETION", result["sha256"], commit, flush=True)
