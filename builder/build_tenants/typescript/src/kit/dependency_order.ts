/**
 * Dependency order: items and the things they need and produce form a graph.
 * Each time, the first item in declared order whose every need is produced by
 * no other item still left is taken next. So every item comes after the
 * producers of what it needs, and the items left when none can be taken lie on
 * a cycle of needs, or need what such an item produces. Over that order, each
 * item's needs through any others are known in one pass (`needed`).
 *
 * @carries C7
 */

export interface Dependencies<V> {
  readonly needs: (item: V) => readonly string[]
  readonly produces: (item: V) => readonly string[]
}

/** The items in dependency order, and those left on a cycle of needs or below one. */
export function ordered<V>(items: readonly V[], deps: Dependencies<V>): { readonly order: readonly V[]; readonly left: readonly V[] } {
  const order: V[] = []
  let left: readonly V[] = items
  for (;;) {
    const ready = left.find((item) =>
      deps.needs(item).every((thing) => left.every((other) => other === item || !deps.produces(other).includes(thing))))
    if (ready === undefined) return { order, left }
    order.push(ready)
    left = left.filter((other) => other !== ready)
  }
}

/** Each item of a dependency order, in that order, with every item that produces what it needs, through any others: those of its producers are known when it is reached. */
export function needed<V>(order: readonly V[], deps: Dependencies<V>): ReadonlyMap<V, ReadonlySet<V>> {
  const below = new Map<V, ReadonlySet<V>>()
  for (const item of order) {
    const producers = order.filter((other) => other !== item && deps.needs(item).some((thing) => deps.produces(other).includes(thing)))
    below.set(item, new Set(producers.flatMap((p) => [p, ...(below.get(p) ?? [])])))
  }
  return below
}
