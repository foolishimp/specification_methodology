import { parse, printParseErrorCode, visit, type ParseError } from "jsonc-parser";

export function parseUniqueJson(bytes: Uint8Array, label: string): unknown {
  let text: string;
  try {
    text = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  } catch {
    throw new TypeError(`${label}: is not valid UTF-8`);
  }
  const objectKeys: Set<string>[] = [];
  let duplicate: string | null = null;
  const visitorErrors: ParseError[] = [];
  visit(
    text,
    {
      onObjectBegin: () => {
        objectKeys.push(new Set());
      },
      onObjectProperty: (name) => {
        const keys = objectKeys.at(-1);
        if (keys === undefined) {
          throw new TypeError(`${label}: parser lost object scope`);
        }
        if (keys.has(name) && duplicate === null) duplicate = name;
        keys.add(name);
      },
      onObjectEnd: () => {
        objectKeys.pop();
      },
      onError: (error, offset, length) => {
        visitorErrors.push({ error, offset, length });
      },
    },
    { allowTrailingComma: false, disallowComments: true },
  );
  if (duplicate !== null) {
    throw new TypeError(`${label}: duplicate JSON object name ${duplicate}`);
  }
  const errors: ParseError[] = [...visitorErrors];
  const value = parse(text, errors, { allowTrailingComma: false, disallowComments: true });
  if (errors.length !== 0) {
    const first = errors[0]!;
    throw new TypeError(
      `${label}: invalid JSON at byte ${first.offset}: ${printParseErrorCode(first.error)}`,
    );
  }
  return value;
}
