/**
 * Lossless encoding: a value written as text and read back is equal to the
 * value, one value has one written form, and reading refuses anything it does
 * not know. This is the one place that wraps Effect's schema module; the
 * shapes of written forms are built from the builders it gives.
 *
 * @carries C14
 */
import * as Schema from "effect/Schema"
import * as SchemaIssue from "effect/SchemaIssue"

/** The shape of a value whose written form is plain data of the same type. */
export type Shape<T> = Schema.Codec<T, T>

/** Builders for shapes. */
export const text = Schema.String
export const literal = Schema.Literal
export const list = Schema.Array
export const record = Schema.Struct
export const optional = Schema.optionalKey
export const oneOf = Schema.Union
export const later = Schema.suspend

/** A whole number above zero. */
export const count = Schema.Int.check(Schema.isGreaterThan(0))
/** A finite number. */
export const number = Schema.Finite
/** Any value at all: for a file another product owns and checks, of which only parts are read. */
export const anything = Schema.Unknown
/** Names, each with a value of one shape. */
export const names = <S extends Schema.Constraint>(value: S) => Schema.Record(Schema.String, value)

/** One thing reading refused: where in the written form, and what it says. */
export interface Refusal {
  readonly at: readonly (string | number)[]
  readonly says: string
}

export type Read<T> = { readonly value: T } | { readonly refused: readonly Refusal[] }

const strict = { onExcessProperty: "error", errors: "all" } as const
const formatter = SchemaIssue.makeFormatterStandardSchemaV1()

/** The one written form of a value: the shape's fields in their declared order, two spaces of indent and a final newline. */
export function write<S extends Schema.Codec<unknown, unknown, never, never>>(shape: S, value: S["Type"]): string {
  return `${JSON.stringify(Schema.encodeSync(shape)(value), null, 2)}\n`
}

/** The one written form of a value of a log's shape: one line, with no final newline. */
export function writeLine<S extends Schema.Codec<unknown, unknown, never, never>>(shape: S, value: S["Type"]): string {
  return JSON.stringify(Schema.encodeSync(shape)(value))
}

/** Reads a written form, refusing what is not data or not of the shape, with every key it does not know. */
export function read<S extends Schema.Codec<unknown, unknown, never, never>>(shape: S, written: string): Read<S["Type"]> {
  let data: unknown
  try {
    data = JSON.parse(written)
  } catch (error) {
    return { refused: [{ at: [], says: `not data: ${error instanceof Error ? error.message : String(error)}` }] }
  }
  try {
    return { value: Schema.decodeUnknownSync(shape, strict)(data) }
  } catch (error) {
    if (!Schema.isSchemaError(error)) throw error
    return {
      refused: formatter(error.issue).issues.map((issue) => ({
        at: (issue.path ?? []).map((key) => (typeof key === "number" ? key : String(key))),
        says: issue.message
      }))
    }
  }
}
