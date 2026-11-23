/**
 * Structural recursion over terms, with a normal form: a function of a tree of
 * terms follows the shape of the terms, and two rewrites give the normal form
 * (a sequence inside a sequence is flattened; a term that does nothing is
 * dropped from a sequence).
 *
 * @carries C5
 */

/** What the recursion needs to know of a kind of term. */
export interface Shape<T> {
  /** The terms directly inside a term, in order. */
  readonly parts: (term: T) => readonly T[]
  /** The same term with its parts replaced. */
  readonly rebuild: (term: T, parts: readonly T[]) => T
  /** A sequence: its parts are spliced into a sequence that holds it. */
  readonly isSequence: (term: T) => boolean
  /** A term that does nothing. */
  readonly isInert: (term: T) => boolean
}

/** Folds a term from its leaves up: each term is given the results of its parts. */
export function fold<T, R>(shape: Shape<T>, term: T, f: (term: T, inner: readonly R[]) => R): R {
  return f(term, shape.parts(term).map((part) => fold(shape, part, f)))
}

/** The normal form of a term, in one pass over its terms. */
export function normal<T>(shape: Shape<T>, term: T): T {
  const parts = shape.parts(term).map((part) => normal(shape, part))
  if (!shape.isSequence(term)) return shape.rebuild(term, parts)
  const kept: T[] = []
  for (const part of parts) {
    if (shape.isSequence(part)) kept.push(...shape.parts(part))
    else if (!shape.isInert(part)) kept.push(part)
  }
  return shape.rebuild(term, kept)
}
