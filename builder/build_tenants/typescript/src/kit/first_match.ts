/**
 * First-match rule list: rules in a fixed order; the first whose condition
 * holds gives the result. The order is part of the definition.
 *
 * @carries C8
 */

export interface Rule<I, R> {
  readonly holds: (input: I) => boolean
  readonly gives: (input: I) => R
}

/** The result of the first rule that holds, or `otherwise` when none does. */
export function firstMatch<I, R>(rules: readonly Rule<I, R>[], input: I, otherwise: (input: I) => R): R {
  for (const rule of rules) if (rule.holds(input)) return rule.gives(input)
  return otherwise(input)
}
