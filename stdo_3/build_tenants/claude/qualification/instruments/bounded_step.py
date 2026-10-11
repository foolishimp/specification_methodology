#!/usr/bin/env python3
"""Generic instrument: run one bounded step as a fresh headless actor.

Successor of cases/T-01/step_actor.py, generalised for later cases. The
step's whole context (system line, card, named blocks) is assembled here,
measured in bytes, compared with the cap and logged before any actor
exists. A context over the cap is refused and no actor is started.
Otherwise a fresh `claude -p` process with no tools, no MCP servers and no
session memory receives exactly that context on stdin, returns its output,
and ends. Every event is appended to <run-dir>/lifecycle.jsonl with a UTC
stamp; the exact input and output of each step are kept under
<run-dir>/steps/.

Changes from the T-01 instrument: blocks are any file or any heading
section of a file (LABEL=PATH or LABEL=PATH#slug, slug by the Axiom Indexer
rule); every block's SHA-256 is logged in the measurement so a later actor
can re-check invalidators; the logged output digest is over the bytes of
the written .out.md file; --calibrate runs one minimal step and logs the
framework overhead the headless CLI adds, in tokens, as a `calibration`
event.

Usage:
  bounded_step.py --cap BYTES --run-dir DIR --step-id ID --card PATH
                  [--block LABEL=PATH[#slug] ...] [--model sonnet] [--dry-run]
  bounded_step.py --run-dir DIR --calibrate [--model sonnet]
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

SYSTEM = ("You are a bounded step actor with no tools and no memory. Your whole "
          "context is this line and the card that follows. Do only what the card "
          "instructs and return only what it asks for.")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
CALIBRATION_INPUT = "CALIBRATION | reply with exactly the single word: ok\n"


def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slug_of(title: str) -> str:
    base = title.strip().lower()
    base = re.sub(r"[^\w\- ]", "", base, flags=re.UNICODE)
    return re.sub(r"[\s\-]+", "-", base).strip("-")


def sections(text: str):
    lines = text.splitlines(keepends=True)
    heads = []
    occurrences = {}
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if not m:
            continue
        base = slug_of(m.group(2))
        n = occurrences.get(base, 0)
        occurrences[base] = n + 1
        heads.append((i, len(m.group(1)), base if n == 0 else f"{base}-{n}"))
    out = {}
    for k, (start, level, slug) in enumerate(heads):
        end = len(lines)
        for j in range(k + 1, len(heads)):
            if heads[j][1] <= level:
                end = heads[j][0]
                break
        out[slug] = "".join(lines[start:end])
    return out


def resolve_block(spec: str):
    """LABEL=PATH[#slug] -> (label, text) or (label, None) when unresolved."""
    label, _, target = spec.partition("=")
    path, _, slug = target.partition("#")
    if not os.path.isfile(path):
        return label, None, path, slug
    text = open(path, encoding="utf-8").read()
    if slug:
        secs = sections(text)
        if slug not in secs:
            return label, None, path, slug
        text = secs[slug]
    return label, text, path, slug


def log(run_dir, entry):
    entry = {"ts": utc(), **entry}
    with open(os.path.join(run_dir, "lifecycle.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def run_actor(run_dir, step_id, model, context):
    """Start one fresh headless actor on `context`; log start and end; return (exit, result)."""
    steps = os.path.join(run_dir, "steps")
    os.makedirs(steps, exist_ok=True)
    in_path = os.path.join(steps, f"{step_id}.in.md")
    with open(in_path, "w", encoding="utf-8") as fh:
        fh.write(context)
    cmd = ["claude", "-p", "--model", model, "--output-format", "json", "--tools", "",
           "--system-prompt", SYSTEM, "--no-session-persistence",
           "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    log(run_dir, {"event": "actor_started", "step": step_id, "model_requested": model,
                  "input_sha256": sha256(context.encode()),
                  "input_bytes": len(context.encode()) + len(SYSTEM.encode())})
    r = subprocess.run(cmd, input=context, capture_output=True, text=True, cwd=steps)
    try:
        d = json.loads(r.stdout)
    except json.JSONDecodeError:
        log(run_dir, {"event": "actor_failed", "step": step_id, "stderr": r.stderr[-2000:], "stdout": r.stdout[-2000:]})
        print(f"FAILED {step_id}: non-JSON output from actor", file=sys.stderr)
        return 4, None
    result = d.get("result", "")
    usage = d.get("usage", {})
    model_ids = sorted((d.get("modelUsage") or {}).keys())
    out_path = os.path.join(steps, f"{step_id}.out.md")
    out_bytes = (result if result.endswith("\n") else result + "\n").encode("utf-8")
    with open(out_path, "wb") as fh:
        fh.write(out_bytes)
    with open(os.path.join(steps, f"{step_id}.usage.json"), "w", encoding="utf-8") as fh:
        json.dump({"usage": usage, "modelUsage": d.get("modelUsage"), "total_cost_usd": d.get("total_cost_usd"),
                   "duration_api_ms": d.get("duration_api_ms"), "num_turns": d.get("num_turns"),
                   "is_error": d.get("is_error"), "session_id": d.get("session_id")}, fh, indent=2)
    context_tokens = (usage.get("input_tokens", 0) + usage.get("cache_creation_input_tokens", 0)
                      + usage.get("cache_read_input_tokens", 0))
    log(run_dir, {"event": "actor_ended", "step": step_id, "is_error": d.get("is_error"),
                  "model_ids": model_ids, "context_tokens": context_tokens,
                  "output_tokens": usage.get("output_tokens"), "total_cost_usd": d.get("total_cost_usd"),
                  "duration_api_ms": d.get("duration_api_ms"), "output_sha256": sha256(out_bytes),
                  "output_bytes": len(out_bytes)})
    return (0 if not d.get("is_error") else 5), result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cap", type=int, help="whole-context cap in bytes")
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--step-id")
    ap.add_argument("--card")
    ap.add_argument("--block", action="append", default=[], help="LABEL=PATH or LABEL=PATH#slug")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--calibrate", action="store_true",
                    help="run one minimal step and log the CLI's framework overhead in tokens")
    a = ap.parse_args()
    os.makedirs(os.path.join(a.run_dir, "steps"), exist_ok=True)

    if a.calibrate:
        step_id = a.step_id or "calibrate"
        context = CALIBRATION_INPUT
        log(a.run_dir, {"event": "measured", "step": step_id, "cap": None,
                        "total_bytes": len(context.encode()) + len(SYSTEM.encode()), "fits": True,
                        "components": [{"name": "system", "bytes": len(SYSTEM.encode())},
                                       {"name": "calibration", "bytes": len(context.encode())}],
                        "blocks": [], "model": a.model, "dry_run": False, "calibration": True})
        code, result = run_actor(a.run_dir, step_id, a.model, context)
        if result is not None:
            ended = [json.loads(l) for l in open(os.path.join(a.run_dir, "lifecycle.jsonl"))][-1]
            log(a.run_dir, {"event": "calibration", "step": step_id, "model_ids": ended["model_ids"],
                            "input_bytes_total": len(context.encode()) + len(SYSTEM.encode()),
                            "framework_overhead_context_tokens": ended["context_tokens"],
                            "output_tokens": ended["output_tokens"], "reply": result.strip()[:40]})
            print(f"CALIBRATION {step_id}: context_tokens={ended['context_tokens']} on "
                  f"{len(context.encode()) + len(SYSTEM.encode())} input bytes; reply={result.strip()[:40]!r}")
        return code

    if a.cap is None or not a.step_id or not a.card:
        ap.error("--cap, --step-id and --card are required unless --calibrate")
    card = open(a.card, encoding="utf-8").read()
    components = [("system", SYSTEM.encode(), None), ("card", card.encode(), sha256(card.encode()))]
    body = [card]
    block_names = []
    for spec in a.block:
        label, text, path, slug = resolve_block(spec)
        if text is None:
            log(a.run_dir, {"event": "refused", "step": a.step_id,
                            "reason": f"unresolved block {label}: {path}" + (f"#{slug}" if slug else "")})
            print(f"REFUSED {a.step_id}: unresolved block {label} ({path}#{slug})", file=sys.stderr)
            return 2
        block = f"\n===== {label} =====\n{text}"
        components.append((f"block:{label}", block.encode(), sha256(text.encode())))
        body.append(block)
        block_names.append(label)

    body_bytes = sum(len(b) for _, b, _ in components)
    header = ""
    for _ in range(2):
        total = body_bytes + len(header.encode())
        header = (f"STEP {a.step_id} | cap {a.cap} bytes | measured {total} bytes | "
                  f"{'fits' if total <= a.cap else 'over cap'}\n"
                  f"BLOCKS: {', '.join(block_names) if block_names else 'none'}\n")
    total = body_bytes + len(header.encode())
    fits = total <= a.cap
    log(a.run_dir, {
        "event": "measured", "step": a.step_id, "cap": a.cap, "total_bytes": total, "fits": fits,
        "components": [{"name": n, "bytes": len(b), "sha256": h} for n, b, h in components]
                      + [{"name": "header", "bytes": len(header.encode()), "sha256": None}],
        "blocks": a.block, "model": a.model, "dry_run": a.dry_run,
    })
    if not fits:
        log(a.run_dir, {"event": "refused", "step": a.step_id, "reason": f"measured {total} > cap {a.cap}"})
        print(f"REFUSED {a.step_id}: measured {total} bytes > cap {a.cap}; components "
              + ", ".join(f"{n}={len(b)}" for n, b, _ in components), file=sys.stderr)
        return 3
    if a.dry_run:
        print(f"DRY {a.step_id}: measured {total} bytes <= cap {a.cap}; no actor started")
        return 0
    context = header + "".join(body)
    code, result = run_actor(a.run_dir, a.step_id, a.model, context)
    if result is not None:
        print(result)
    return code


if __name__ == "__main__":
    sys.exit(main())
