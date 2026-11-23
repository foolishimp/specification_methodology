/**
 * Name resolution with cycle refusal: each name is followed to its definition,
 * and a name that leads back to itself is refused, in one pass over the names
 * and the references between them.
 *
 * @carries C6
 */
/**
 * The definition a name comes to, following each definition that is itself
 * only another name (`onlyName` gives that name). Undefined where a name has
 * no definition or leads back to itself.
 */
export function definitionOf(name, definitions, onlyName) {
    const met = new Set();
    let at = name;
    while (!met.has(at)) {
        met.add(at);
        const definition = definitions.get(at);
        if (definition === undefined)
            return undefined;
        const next = onlyName(definition);
        if (next === undefined)
            return definition;
        at = next;
    }
    return undefined;
}
/**
 * Follows every name in `used`, and every name each definition uses in turn.
 * `namesIn` gives the names a definition uses.
 */
export function resolve(used, definitions, namesIn) {
    const unknown = new Set();
    const cyclic = new Set();
    const state = new Map();
    const follow = (name) => {
        const now = state.get(name);
        if (now === "done")
            return;
        if (now === "following") {
            cyclic.add(name);
            return;
        }
        const definition = definitions.get(name);
        if (definition === undefined) {
            unknown.add(name);
            state.set(name, "done");
            return;
        }
        state.set(name, "following");
        for (const inner of namesIn(definition))
            follow(inner);
        state.set(name, "done");
    };
    for (const name of used)
        follow(name);
    return { unknown: [...unknown], cyclic: [...cyclic] };
}
