import { readdirSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { resolve } from "node:path";

const testRoot = resolve("build/test");
let testFiles = [];
try {
  testFiles = readdirSync(testRoot, { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".test.js"))
    .map((entry) => resolve(testRoot, entry.name))
    .sort();
} catch (error) {
  if (error?.code !== "ENOENT") throw error;
}

if (testFiles.length === 0) {
  console.error("refusing GTL qualification: zero compiled tests discovered");
  process.exit(1);
}

const result = spawnSync(process.execPath, ["--test", ...testFiles], {
  stdio: "inherit",
});
if (result.error) throw result.error;
process.exit(result.status ?? 1);
