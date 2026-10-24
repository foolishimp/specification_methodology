#!/usr/bin/env python3
"""Bounded read-only Claude semantic assessment; private output stays outside publication."""
import argparse, json, os, signal, subprocess, time
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument("--prompt",required=True); p.add_argument("--output",required=True); p.add_argument("--cwd",required=True); a=p.parse_args()
out=Path(a.output); out.mkdir(parents=True,exist_ok=False)
cmd=["/Users/jim/.local/bin/claude","-p","--safe-mode","--strict-mcp-config","--mcp-config",'{"mcpServers":{}}',"--setting-sources","","--tools","Read,Glob,Grep","--allowedTools","Read,Glob,Grep","--no-session-persistence","--disable-slash-commands","--model","claude-opus-5-5","--effort","max","--max-budget-usd","30","--output-format","stream-json","--verbose","--add-dir","/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2","--add-dir","/Users/jim/Library/Application Support/STDO/releases/v3.0.0-rc.1"]
(out/"invocation.json").write_text(json.dumps({"argv":cmd,"cwd":a.cwd,"prompt":str(Path(a.prompt).resolve()),"timeout_seconds":1800,"tools":"Read,Glob,Grep only"},indent=2)+"\n")
start=time.monotonic()
with open(a.prompt,"rb") as inp, (out/"events.jsonl").open("wb") as stdout, (out/"stderr.txt").open("wb") as stderr:
 proc=subprocess.Popen(cmd,cwd=a.cwd,stdin=inp,stdout=stdout,stderr=stderr,start_new_session=True)
 print(json.dumps({"started_pid":proc.pid,"output":str(out)}),flush=True)
 timed_out=False
 try: code=proc.wait(timeout=1800)
 except subprocess.TimeoutExpired:
  timed_out=True; os.killpg(proc.pid,signal.SIGTERM)
  try: code=proc.wait(timeout=10)
  except subprocess.TimeoutExpired: os.killpg(proc.pid,signal.SIGKILL); code=proc.wait(timeout=10)
record={"exit_code":code,"timed_out":timed_out,"elapsed_seconds":round(time.monotonic()-start,3)}
(out/"completion.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record),flush=True)
raise SystemExit(code if code>=0 else 1)
