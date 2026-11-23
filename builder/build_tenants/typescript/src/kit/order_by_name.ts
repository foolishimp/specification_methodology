/**
 * Order by name: names in the order of their characters.
 *
 * @carries H2
 */

/** The names, in the order of their characters. */
export function byName(names: Iterable<string>): string[] {
  return [...names].sort()
}

/** Of the items, the one whose name comes first in the order of their characters. */
export function firstByName<T>(items: Iterable<T>, nameOf: (item: T) => string): T | undefined {
  let first: T | undefined
  for (const item of items) if (first === undefined || nameOf(item) < nameOf(first)) first = item
  return first
}
