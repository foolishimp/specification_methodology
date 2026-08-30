import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { resolve } from "node:path";
import test from "node:test";

test("test runner refuses an empty compiled-test inventory", () => {
  const emptyWorkspace = mkdtempSync(resolve(tmpdir(), "stdo-gtl-zero-tests-"));
  try {
    const runner = resolve("scripts/run-tests.mjs");
    const result = spawnSync(process.execPath, [runner], {
      cwd: emptyWorkspace,
      encoding: "utf8",
    });
    assert.equal(result.status, 1);
    assert.match(
      result.stderr,
      /refusing GTL qualification: zero compiled tests discovered/,
    );
  } finally {
    rmSync(emptyWorkspace, { recursive: true, force: true });
  }
});
