/**
 * Map difference: from two maps of path to identity, the paths added, removed
 * and changed, in one pass over each map.
 *
 * @carries C2
 */

export interface Difference {
  /** In the second map only, in its order. */
  readonly added: readonly string[]
  /** In the first map only, in its order. */
  readonly removed: readonly string[]
  /** In both, with another identity, in the first map's order. */
  readonly changed: readonly string[]
}

export function difference(
  before: ReadonlyMap<string, string>,
  after: ReadonlyMap<string, string>
): Difference {
  const removed: string[] = []
  const changed: string[] = []
  for (const [path, identity] of before) {
    const now = after.get(path)
    if (now === undefined) removed.push(path)
    else if (now !== identity) changed.push(path)
  }
  const added: string[] = []
  for (const path of after.keys()) if (!before.has(path)) added.push(path)
  return { added, removed, changed }
}

/** Every path of the difference: the removed and changed, then the added. */
export function paths(d: Difference): readonly string[] {
  return [...d.removed, ...d.changed, ...d.added]
}

export function isEmpty(d: Difference): boolean {
  return d.added.length === 0 && d.removed.length === 0 && d.changed.length === 0
}
