import assert from "node:assert/strict";
import test from "node:test";

import { canonicalJson } from "../src/canonical.js";

test("canonical JSON accepts Unicode scalar strings", () => {
  assert.equal(canonicalJson("plain"), '"plain"');
  assert.equal(canonicalJson("\u{1f642}"), '"🙂"');
  assert.equal(canonicalJson({ "\u{1f642}": "ok" }), '{"🙂":"ok"}');
});

test("canonical JSON refuses lone UTF-16 surrogates", () => {
  for (const value of ["\ud800", "\udfff", `a${"\ud800"}b`]) {
    assert.throws(
      () => canonicalJson(value),
      /canonical JSON strings must contain Unicode scalars/,
    );
  }
  assert.throws(
    () => canonicalJson({ ["\ud800"]: "invalid key" }),
    /canonical JSON strings must contain Unicode scalars/,
  );
});
