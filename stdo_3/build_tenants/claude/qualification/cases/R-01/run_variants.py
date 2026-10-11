#!/usr/bin/env python3
"""R-01 fixture operator: run every variant of the recoverability trial through the generic instrument.

Each variant is one fresh headless step actor whose whole context is the card,
the METHOD blocks of that variant (none, the STDO 3 route, the whole STDO 3
set, an author-selected rc.2 section set, or the four rc.2 members a reader
of the rc.2 README would open) and the TASK block. The instrument measures
and logs each context before the actor exists. The operator judges nothing.

usage: run_variants.py --run-dir DIR [--repeats 2] [--cap 400000] [--only V1 V3 ...] [--dry-run]
"""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TENANT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
INST = os.path.join(TENANT, "qualification", "instruments", "bounded_step.py")
CARD = os.path.join(HERE, "RECOVERY_CARD.md")
TASK = os.path.join(HERE, "subject", "TASK.md")
STD = os.path.join(TENANT, "standards")
RC2 = "/Users/jim/Library/Application Support/STDO/releases/v2.5.1-rc.2/standards"

def s3(name, slug=None):
    p = os.path.join(STD, name)
    return f"METHOD STDO 3 {name}" + (f"#{slug}" if slug else "") + "=" + p + (f"#{slug}" if slug else "")

def rc2(name, slug=None):
    p = os.path.join(RC2, name)
    return f"METHOD STDO 2.5.1-rc.2 {name}" + (f"#{slug}" if slug else "") + "=" + p + (f"#{slug}" if slug else "")

VARIANTS = {
    # no method documents: a control for what the documents add
    "V0": [],
    # the STDO 3 README route for a bounded evaluation step
    "V1": [s3("README.md"), s3("FOUNDATIONS.md"), s3("CALCULUS.md", "1-the-step"),
           s3("CALCULUS.md", "2-context-construction-under-an-envelope"), s3("CALCULUS.md", "3-result-algebra"),
           s3("EVALUATION.md")],
    # the whole STDO 3 set
    "V2": [s3(n) for n in ["README.md", "FOUNDATIONS.md", "CALCULUS.md", "EVALUATION.md", "SPEC_METHOD.md", "CONFORMANCE.md", "PROFILES.md"]],
    # rc.2 sections selected by the author as the ones a bounded evaluation step needs (private knowledge, declared)
    "V3": [rc2("README.md"),
           rc2("SPEC_METHOD.md", "agentic-construction-execution-stdo-up-020"),
           rc2("SPEC_METHOD.md", "proof-target-identity-and-adequacy-stdo-up-001"),
           rc2("SPEC_METHOD.md", "semantic-evidence-and-projection-separation-stdo-up-008"),
           rc2("SPEC_METHOD.md", "assurance-boundary-congruence-and-method-qualification-stdo-up-022"),
           rc2("SPEC_METHOD.md", "probabilistic-work-boundary"),
           rc2("REFERENCE_FRAME_METHOD.md", "rf-002-finite-attention"),
           rc2("REFERENCE_FRAME_METHOD.md", "rf-007-semantic-evidence-and-verdict-separation"),
           rc2("REFERENCE_FRAME_METHOD.md", "rf-012-closed-results"),
           rc2("REFERENCE_FRAME_METHOD.md", "rf-014-capability-fit"),
           rc2("REFERENCE_FRAME_METHOD.md", "engagement"),
           rc2("AXIOMATIC_CALCULUS.md", "ac-007-constraint-and-refusal"),
           rc2("AXIOMATIC_CALCULUS.md", "ac-010-material-closure"),
           rc2("AXIOMATIC_CALCULUS.md", "ac-011-projection"),
           rc2("AXIOMATIC_CALCULUS.md", "ac-014-judgment-separation"),
           rc2("STDO_REFERENCE_FRAME_BASELINE.md", "work-result"),
           rc2("STDO_REFERENCE_FRAME_BASELINE.md", "reviewer"),
           rc2("TICKET_METHOD.md", "execution-and-verification-authority-separation-stdo-up-007")],
    # the rc.2 members a reader of its README would open for governed construction and evaluation, whole
    "V4": [rc2("README.md"), rc2("SPEC_METHOD.md"), rc2("REFERENCE_FRAME_METHOD.md"),
           rc2("AXIOMATIC_CALCULUS.md"), rc2("STDO_REFERENCE_FRAME_BASELINE.md")],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--repeats", type=int, default=2)
    ap.add_argument("--cap", type=int, default=400000)
    ap.add_argument("--only", nargs="*", default=list(VARIANTS))
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.run_dir, exist_ok=True)
    if not a.dry_run:
        subprocess.run([sys.executable, "-I", INST, "--run-dir", a.run_dir, "--calibrate", "--model", a.model])
    for v in a.only:
        for k in range(1, a.repeats + 1):
            step = f"{v}-{k}"
            cmd = [sys.executable, "-I", INST, "--cap", str(a.cap), "--run-dir", a.run_dir, "--step-id", step,
                   "--card", CARD, "--model", a.model]
            for b in VARIANTS[v]:
                cmd += ["--block", b]
            cmd += ["--block", f"TASK={TASK}"]
            if a.dry_run:
                cmd.append("--dry-run")
            r = subprocess.run(cmd, capture_output=True, text=True)
            print(f"== {step} rc={r.returncode}")
            print((r.stdout.strip() or r.stderr.strip())[:400])
            sys.stdout.flush()
            if a.dry_run:
                break
    return 0


if __name__ == "__main__":
    sys.exit(main())
