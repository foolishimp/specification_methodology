#!/usr/bin/env python3
# Read-only package verifier for the Claude STDO Skills tenant candidate.
# Run with: python3 -I -B build_tenants/claude/tests/check_package.py
# Checks frontmatter, name/dir agreement, no symlinks, intra-directory
# reference resolution, absence of other-tenant/personal-config paths, and
# INVENTORY.md agreement with files on disk. Exit 0 iff every check passes.
import os, sys, re, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)  # build_tenants/claude
EXPECTED_SKILLS = ["stdo-workspace-change", "stdo-tool-operations",
                   "stdo-delegate-review", "stdo-continuation",
                   "stdo-release-install"]
FORBIDDEN = ["~/.claude", "$HOME/.claude", "build_tenants/codex"]
results = []
def check(ok, msg):
    results.append((bool(ok), msg))

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out = {}
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return out
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", lines[i])
        if m:
            out[m.group(1)] = m.group(2).strip()
    return None

# 1. No symlinks anywhere in the package.
symlinks = []
for root, dirs, files in os.walk(PKG):
    dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
    for name in list(dirs) + files:
        full = os.path.join(root, name)
        if os.path.islink(full):
            symlinks.append(os.path.relpath(full, PKG))
check(not symlinks, "no symlinks in package" + ("" if not symlinks else ": " + ", ".join(symlinks)))

# 2. Each expected skill directory has a SKILL.md with valid frontmatter.
for name in EXPECTED_SKILLS:
    sp = os.path.join(PKG, "skills", name, "SKILL.md")
    if not os.path.isfile(sp):
        check(False, "skill present: " + name + " (SKILL.md missing)")
        continue
    text = open(sp, encoding="utf-8").read()
    fm = parse_frontmatter(text)
    if fm is None:
        check(False, "frontmatter parses: " + name)
        continue
    nm = fm.get("name", "")
    desc = fm.get("description", "")
    check(nm == name, "name equals directory: " + name + " (name=" + nm + ")")
    check(bool(re.match(r"^[a-z0-9][a-z0-9-]*$", nm)), "name is lowercase-hyphen: " + name)
    check(len(desc) >= 40, "description present and substantive: " + name + " (len=" + str(len(desc)) + ")")
    check("disable-model-invocation: true" not in text, "model invocation not disabled: " + name)

# 3. No other-tenant or personal-config path anywhere in the package text files.
for root, dirs, files in os.walk(PKG):
    dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
    for name in files:
        full = os.path.join(root, name)
        rel = os.path.relpath(full, PKG)
        if rel == os.path.relpath(__file__, PKG):
            continue  # the verifier legitimately names FORBIDDEN tokens
        try:
            text = open(full, encoding="utf-8").read()
        except (UnicodeError, OSError):
            continue
        hits = [tok for tok in FORBIDDEN if tok in text]
        check(not hits, "no forbidden path in " + rel + ("" if not hits else ": " + ", ".join(hits)))

# 4. Markdown links do not escape their skill directory.
escapes = []
for root, dirs, files in os.walk(os.path.join(PKG, "skills")):
    for name in files:
        if not name.endswith(".md"):
            continue
        full = os.path.join(root, name)
        text = open(full, encoding="utf-8").read()
        for m in re.finditer(r"\]\(([^)]+)\)", text):
            tgt = m.group(1).strip()
            if tgt.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if tgt.startswith("/") or tgt.startswith("../"):
                escapes.append(os.path.relpath(full, PKG) + " -> " + tgt)
check(not escapes, "no skill reference escapes its directory" + ("" if not escapes else ": " + ", ".join(escapes)))

# 5. INVENTORY.md matches the files on disk.
inv_path = os.path.join(PKG, "INVENTORY.md")
if not os.path.isfile(inv_path):
    check(False, "INVENTORY.md present")
else:
    expected = {}
    for line in open(inv_path, encoding="utf-8"):
        m = re.match(r"^\|\s*(\S+)\s*\|\s*([0-9a-f]{64})\s*\|", line)
        if m:
            expected[m.group(1)] = m.group(2)
    actual = {}
    for root, dirs, files in os.walk(PKG):
        dirs[:] = [d for d in dirs if d != "__pycache__" and not d.startswith(".")]
        for name in files:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, PKG)
            if rel == "INVENTORY.md":
                continue
            actual[rel] = sha256_file(full)
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    mismatch = sorted(p for p in (set(expected) & set(actual)) if expected[p] != actual[p])
    check(not missing, "no inventory entries missing from disk" + ("" if not missing else ": " + ", ".join(missing)))
    check(not extra, "no disk files missing from inventory" + ("" if not extra else ": " + ", ".join(extra)))
    check(not mismatch, "inventory digests match disk" + ("" if not mismatch else ": " + ", ".join(mismatch)))
    check(len(expected) > 0, "inventory is non-empty (" + str(len(expected)) + " entries)")

passed = sum(1 for ok, _ in results if ok)
failed = [m for ok, m in results if not ok]
for ok, msg in results:
    print(("PASS " if ok else "FAIL ") + msg)
print("SUMMARY: " + str(passed) + "/" + str(len(results)) + " checks passed")
sys.exit(0 if not failed else 1)
