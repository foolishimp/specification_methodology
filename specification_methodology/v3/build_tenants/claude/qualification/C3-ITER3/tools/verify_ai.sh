#!/bin/bash
set -e
SP=$1; AI=$SP/axiom_indexer_v2.5.1-rc.2; rm -rf "$AI"; mkdir -p "$AI"
cd /Users/jim/src/apps/specification_methodology-claude
TAG=refs/tags/axiom_indexer/v2.5.1-rc.2
echo "tag $(git rev-parse $TAG) commit $(git rev-parse "${TAG}^{commit}") tree $(git rev-parse "${TAG}^{tree}") subtree $(git rev-parse "${TAG}:axiom_indexer")"
for f in build_tenants/core/code/ac.py skills/axiomatize-corpus/SKILL.md skills/axiomatize-corpus/agents/openai.yaml skills/axiomatize-corpus/references/output-contract.md skills/axiomatize-corpus/references/program.schema.json; do
  mkdir -p "$AI/$(dirname $f)"; git show "${TAG}:axiom_indexer/$f" > "$AI/$f"; done
for l in .agents/skills/axiomatize-corpus .claude/skills/axiomatize-corpus; do mkdir -p "$AI/$(dirname $l)"; ln -s ../../skills/axiomatize-corpus "$AI/$l"; done
echo "$AI"
