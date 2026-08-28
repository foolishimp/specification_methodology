import { createHash } from "node:crypto";

export type JsonValue =
  | null
  | boolean
  | number
  | string
  | readonly JsonValue[]
  | Readonly<{ [key: string]: JsonValue }>;

export function compareUnicodeCodeUnits(left: string, right: string): number {
  return left < right ? -1 : left > right ? 1 : 0;
}

export function canonicalJson(value: JsonValue): string {
  if (value === null || typeof value === "boolean" || typeof value === "string") {
    return JSON.stringify(value);
  }
  if (typeof value === "number") {
    if (!Number.isSafeInteger(value) || value < 0 || Object.is(value, -0)) {
      throw new TypeError("STDO.gtl numbers must be non-negative safe integers");
    }
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) {
    return `[${value.map(canonicalJson).join(",")}]`;
  }
  if (typeof value === "object") {
    const record = value as Readonly<Record<string, JsonValue>>;
    const keys = Object.keys(record).sort(compareUnicodeCodeUnits);
    return `{${keys
      .map((key) => `${JSON.stringify(key)}:${canonicalJson(record[key]!)}`)
      .join(",")}}`;
  }
  throw new TypeError("value is not canonical JSON data");
}

export function sha256Bytes(bytes: string | Uint8Array): string {
  return `sha256:${createHash("sha256").update(bytes).digest("hex")}`;
}

export function sha256Canonical(value: JsonValue): string {
  return sha256Bytes(canonicalJson(value));
}

export function exactKeys(
  value: Readonly<Record<string, unknown>>,
  expected: readonly string[],
): boolean {
  return (
    Object.keys(value).sort(compareUnicodeCodeUnits).join("\0") ===
    [...expected].sort(compareUnicodeCodeUnits).join("\0")
  );
}

export function isRecord(value: unknown): value is Readonly<Record<string, unknown>> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
