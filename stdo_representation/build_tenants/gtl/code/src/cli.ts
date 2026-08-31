#!/usr/bin/env node

import {
  mkdtempSync,
  mkdirSync,
  readFileSync,
  renameSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import { basename, dirname, resolve } from "node:path";

import { canonicalJson, type JsonValue } from "./canonical.js";
import { constructStdoGtl } from "./construct.js";
import type { AcceptedBuildEvidence } from "./contracts.js";
import { parseUniqueJson } from "./io.js";

const REQUIRED = [
  "plan",
  "source-manifest",
  "profile",
  "frame-basis",
  "selection-ledger",
  "profile-acceptance",
  "frame-basis-acceptance",
  "selection-acceptance",
  "publisher-manifest",
  "publisher-artifact",
  "output-directory",
] as const;

function usage(): never {
  throw new TypeError(
    "usage: stdo-gtl build " +
      REQUIRED.map((name) => `--${name} <path>`).join(" "),
  );
}

function argumentsByName(argv: readonly string[]): Readonly<Record<string, string>> {
  if (argv[0] !== "build" || argv.length !== 1 + REQUIRED.length * 2) usage();
  const values: Record<string, string> = {};
  for (let index = 1; index < argv.length; index += 2) {
    const option = argv[index]!;
    const value = argv[index + 1];
    if (!option.startsWith("--") || value === undefined || value.startsWith("--")) usage();
    const name = option.slice(2);
    if (!(REQUIRED as readonly string[]).includes(name) || values[name] !== undefined) usage();
    values[name] = value;
  }
  for (const name of REQUIRED) if (values[name] === undefined) usage();
  return values;
}

function jsonFile(path: string, label: string): { value: unknown; bytes: Uint8Array } {
  const bytes = readFileSync(path);
  return { value: parseUniqueJson(bytes, label), bytes };
}

function main(): void {
  const options = argumentsByName(process.argv.slice(2));
  const plan = jsonFile(options.plan!, "build plan");
  const manifest = jsonFile(options["source-manifest"]!, "source manifest");
  const ledger = jsonFile(options["selection-ledger"]!, "selection ledger");
  const profileAcceptance = jsonFile(options["profile-acceptance"]!, "profile acceptance");
  const frameAcceptance = jsonFile(options["frame-basis-acceptance"]!, "frame-basis acceptance");
  const selectionAcceptance = jsonFile(options["selection-acceptance"]!, "selection acceptance");
  const publisherManifest = jsonFile(options["publisher-manifest"]!, "publisher manifest");
  const evidence: AcceptedBuildEvidence = {
    source_manifest: manifest.value,
    source_manifest_bytes: manifest.bytes,
    profile_bytes: readFileSync(options.profile!),
    frame_basis_bytes: readFileSync(options["frame-basis"]!),
    semantic_selection_ledger: ledger.value,
    semantic_selection_ledger_bytes: ledger.bytes,
    profile_acceptance: profileAcceptance.value,
    profile_acceptance_bytes: profileAcceptance.bytes,
    frame_basis_acceptance: frameAcceptance.value,
    frame_basis_acceptance_bytes: frameAcceptance.bytes,
    selection_acceptance: selectionAcceptance.value,
    selection_acceptance_bytes: selectionAcceptance.bytes,
    publisher_manifest: publisherManifest.value,
    publisher_manifest_bytes: publisherManifest.bytes,
    publisher_artifact_bytes: readFileSync(options["publisher-artifact"]!),
  };
  const result = constructStdoGtl(plan.value, evidence);
  const output = resolve(options["output-directory"]!);
  const parent = dirname(output);
  mkdirSync(parent, { recursive: true });
  const temporary = mkdtempSync(`${parent}/.${basename(output)}.tmp-`);
  try {
    writeFileSync(`${temporary}/stdo.gtl`, result.canonical_bytes, { flag: "wx" });
    writeFileSync(
      `${temporary}/build-receipt.json`,
      `${canonicalJson(result.receipt as unknown as JsonValue)}\n`,
      { flag: "wx" },
    );
    renameSync(temporary, output);
  } catch (error) {
    rmSync(temporary, { recursive: true, force: true });
    throw error;
  }
  process.stdout.write(
    `${JSON.stringify({ output_directory: output, ...result.receipt }, null, 2)}\n`,
  );
}

try {
  main();
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  process.stderr.write(`stdo-gtl: ${message}\n`);
  process.exitCode = 1;
}
