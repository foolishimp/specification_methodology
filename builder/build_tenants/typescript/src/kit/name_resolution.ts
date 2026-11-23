/**
 * Name resolution with cycle refusal: each name is followed to its definition,
 * and a name that leads back to itself is refused, in one pass over the names
 * and the references between them.
 *
 * @carries C6
 */

export interface Resolution {
  /** Names used that have no definition, each once, in the order first met. */
  readonly unknown: readonly string[]
  /** Names that lead back to themselves, each once, in the order first met. */
  readonly cyclic: readonly string[]
}

/**
 * The definition a name comes to, following each definition that is itself
 * only another name (`onlyName` gives that name). Undefined where a name has
 * no definition or leads back to itself.
 */
export function definitionOf<D>(name: string, definitions: ReadonlyMap<string, D>, onlyName: (definition: D) => string | undefined): D | undefined {
  const met = new Set<string>()
  let at = name
  while (!met.has(at)) {
    met.add(at)
    const definition = definitions.get(at)
    if (definition === undefined) return undefined
    const next = onlyName(definition)
    if (next === undefined) return definition
    at = next
  }
  return undefined
}

/**
 * Follows every name in `used`, and every name each definition uses in turn.
 * `namesIn` gives the names a definition uses.
 */
export function resolve<D>(
  used: readonly string[],
  definitions: ReadonlyMap<string, D>,
  namesIn: (definition: D) => readonly string[]
): Resolution {
  const unknown = new Set<string>()
  const cyclic = new Set<string>()
  const state = new Map<string, "following" | "done">()
  const follow = (name: string): void => {
    const now = state.get(name)
    if (now === "done") return
    if (now === "following") {
      cyclic.add(name)
      return
    }
    const definition = definitions.get(name)
    if (definition === undefined) {
      unknown.add(name)
      state.set(name, "done")
      return
    }
    state.set(name, "following")
    for (const inner of namesIn(definition)) follow(inner)
    state.set(name, "done")
  }
  for (const name of used) follow(name)
  return { unknown: [...unknown], cyclic: [...cyclic] }
}
