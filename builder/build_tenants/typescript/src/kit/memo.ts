/**
 * Memo by content key: the result of a function with no effects, or of a
 * check, which gives the same result on the same content, kept under the
 * identities of all its inputs and read under exactly that key.
 *
 * @carries C4
 */

export interface Memo<V> {
  /** The result kept under exactly this key, or undefined. */
  readonly lookup: (key: readonly string[]) => V | undefined
  /** Keeps the result under this key. */
  readonly keep: (key: readonly string[], value: V) => void
}

/** Each part is written with its length first, so two keys share a form only when they are equal. */
function form(key: readonly string[]): string {
  let text = ""
  for (const part of key) text += `${part.length}:${part};`
  return text
}

export function memo<V>(): Memo<V> {
  const kept = new Map<string, V>()
  return {
    lookup: (key) => kept.get(form(key)),
    keep: (key, value) => {
      kept.set(form(key), value)
    }
  }
}
