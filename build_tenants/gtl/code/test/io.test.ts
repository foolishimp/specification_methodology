import assert from "node:assert/strict";
import test from "node:test";

import { parseUniqueJson } from "../src/io.js";

const encoder = new TextEncoder();

test("JSON admission rejects duplicate object names", () => {
  assert.throws(
    () => parseUniqueJson(encoder.encode('{"kind":"one","kind":"two"}'), "fixture"),
    /duplicate JSON object name kind/u,
  );
});

test("JSON admission rejects comments and trailing commas", () => {
  assert.throws(
    () => parseUniqueJson(encoder.encode('{"kind":"one",}'), "fixture"),
    /invalid JSON/u,
  );
  assert.throws(
    () => parseUniqueJson(encoder.encode('{// comment\n"kind":"one"}'), "fixture"),
    /invalid JSON/u,
  );
});
