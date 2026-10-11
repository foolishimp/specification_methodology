#!/usr/bin/env python3
"""T-01 successor instrument: run one bounded step as a fresh headless actor.

The step's whole context (system line, step card, tenant paragraphs, rc.2
sections) is assembled here, measured in bytes, compared with the cap and
logged before any actor exists. A context over the cap is refused and no
actor is started. Otherwise a fresh `claude -p` process with no tools, no
MCP servers and no session memory receives exactly that context on stdin,
returns its output, and ends. Every event is appended to
<run-dir>/lifecycle.jsonl with a UTC stamp; the exact input and output of
each step are kept under <run-dir>/steps/.

Usage:
  step_actor.py --cap BYTES --run-dir DIR --step-id ID
                [--para P1 ...] [--route MEMBER.md:slug ...]
                [--model sonnet] [--card STEP_CARD.md] [--dry-run]

--dry-run measures and logs only; no actor is started.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FRAG = os.path.join(HERE, "fragment.py")
TENANT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
FOUNDATIONS = os.path.join(TENANT, "standards", "FOUNDATIONS.md")
RC2 = "/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards"
SYSTEM = ("You are a bounded step actor with no tools and no memory. Your whole "
          "context is this line and the card that follows. Do only what the card "
          "instructs and return only what it asks for.")


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section3_paragraphs():
    """Return {label: paragraph_text} for FOUNDATIONS §3, keyed by P0..P6."""
    text = open(FOUNDATIONS, encoding="utf-8").read()
    lines = text.splitlines(keepends=True)
    start = next(i for i, l in enumerate(lines) if l.startswith("## 3. Commitments"))
    end = next(i for i, l in enumerate(lines) if l.startswith("## 4."))
    section = "".join(lines[start:end])
    paras = {}
    for p in re.split(r"\n\s*\n", section):
        if p.strip() and not p.startswith("## "):
            paras[p.split()[0]] = p.strip() + "\n"
    return paras


def fragment_text(member, slug):
    r = subprocess.run([sys.executable, "-I", FRAG, "--file", os.path.join(RC2, member),
                        "--slug", slug, "--text"], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return r.stdout


def log(run_dir, entry):
    entry = {"ts": utc(), **entry}
    with open(os.path.join(run_dir, "lifecycle.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, required=True, help="whole-context cap in bytes")
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--step-id", required=True)
    ap.add_argument("--para", action="append", default=[], help="FOUNDATIONS §3 paragraph label, e.g. P4b")
    ap.add_argument("--route", action="append", default=[], help="MEMBER.md:slug")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--card", default=os.path.join(HERE, "STEP_CARD.md"))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    os.makedirs(os.path.join(a.run_dir, "steps"), exist_ok=True)
    card = open(a.card, encoding="utf-8").read()
    paras = section3_paragraphs()
    components = [("system", SYSTEM.encode()), ("card", card.encode())]
    body = [card]
    for label in a.para:
        if label not in paras:
            log(a.run_dir, {"event": "refused", "step": a.step_id, "reason": f"no paragraph {label} in FOUNDATIONS §3"})
            print(f"REFUSED {a.step_id}: no paragraph {label}", file=sys.stderr)
            return 2
        block = f"\n===== TENANT PARAGRAPH {label} (FOUNDATIONS §3) =====\n{paras[label]}"
        components.append((f"para:{label}", block.encode()))
        body.append(block)
    for route in a.route:
        member, _, slug = route.partition(":")
        text = fragment_text(member, slug)
        if text is None:
            log(a.run_dir, {"event": "refused", "step": a.step_id, "reason": f"unresolved {member}#{slug}"})
            print(f"REFUSED {a.step_id}: unresolved {member}#{slug}", file=sys.stderr)
            return 2
        block = f"\n===== RC.2 SECTION {member}#{slug} =====\n{text}"
        components.append((f"route:{member}#{slug}", block.encode()))
        body.append(block)

    body_bytes = sum(len(b) for _, b in components)
    # the header carries the measurement itself; fix its length by one re-measure
    header = ""
    for _ in range(2):
        total = body_bytes + len(header.encode())
        header = (f"STEP {a.step_id} | cap {a.cap} bytes | measured {total} bytes | "
                  f"{'fits' if total <= a.cap else 'over cap'}\n"
                  f"ROUTES: {', '.join(a.route) if a.route else 'none'}\n")
    total = body_bytes + len(header.encode())
    fits = total <= a.cap
    measurement = {
        "event": "measured", "step": a.step_id, "cap": a.cap, "total_bytes": total, "fits": fits,
        "components": [{"name": n, "bytes": len(b)} for n, b in components] + [{"name": "header", "bytes": len(header.encode())}],
        "paras": a.para, "routes": a.route, "model": a.model, "dry_run": a.dry_run,
    }
    log(a.run_dir, measurement)
    if not fits:
        log(a.run_dir, {"event": "refused", "step": a.step_id, "reason": f"measured {total} > cap {a.cap}"})
        print(f"REFUSED {a.step_id}: measured {total} bytes > cap {a.cap}; components "
              + ", ".join(f"{n}={len(b)}" for n, b in components), file=sys.stderr)
        return 3
    if a.dry_run:
        print(f"DRY {a.step_id}: measured {total} bytes <= cap {a.cap}; no actor started")
        return 0

    context = header + "".join(body)
    in_path = os.path.join(a.run_dir, "steps", f"{a.step_id}.in.md")
    with open(in_path, "w", encoding="utf-8") as fh:
        fh.write(context)
    cmd = ["claude", "-p", "--model", a.model, "--output-format", "json", "--tools", "",
           "--system-prompt", SYSTEM, "--no-session-persistence",
           "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    started = log(a.run_dir, {"event": "actor_started", "step": a.step_id, "model_requested": a.model,
                              "input_sha256": sha256(context.encode()), "input_bytes": len(context.encode()) + len(SYSTEM.encode())})
    r = subprocess.run(cmd, input=context, capture_output=True, text=True, cwd=os.path.join(a.run_dir, "steps"))
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        log(a.run_dir, {"event": "actor_failed", "step": a.step_id, "stderr": r.stderr[-2000:], "stdout": r.stdout[-2000:]})
        print(f"FAILED {a.step_id}: non-JSON output from actor", file=sys.stderr)
        return 4
    result = d.get("result", "")
    usage = d.get("usage", {})
    model_ids = sorted((d.get("modelUsage") or {}).keys())
    out_path = os.path.join(a.run_dir, "steps", f"{a.step_id}.out.md")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(result if result.endswith("\n") else result + "\n")
    with open(os.path.join(a.run_dir, "steps", f"{a.step_id}.usage.json"), "w", encoding="utf-8") as fh:
        json.dump({"usage": usage, "modelUsage": d.get("modelUsage"), "total_cost_usd": d.get("total_cost_usd"),
                   "duration_api_ms": d.get("duration_api_ms"), "num_turns": d.get("num_turns"),
                   "is_error": d.get("is_error"), "session_id": d.get("session_id")}, fh, indent=2)
    log(a.run_dir, {"event": "actor_ended", "step": a.step_id, "is_error": d.get("is_error"),
                    "model_ids": model_ids, "context_tokens": (usage.get("input_tokens", 0) + usage.get("cache_creation_input_tokens", 0) + usage.get("cache_read_input_tokens", 0)),
                    "output_tokens": usage.get("output_tokens"), "total_cost_usd": d.get("total_cost_usd"),
                    "duration_api_ms": d.get("duration_api_ms"), "output_sha256": sha256(result.encode())})
    print(result)
    return 0 if not d.get("is_error") else 5


if __name__ == "__main__":
    sys.exit(main())
