/**
 * Map difference: from two maps of path to identity, the paths added, removed
 * and changed, in one pass over each map.
 *
 * @carries C2
 */
export function difference(before, after) {
    const removed = [];
    const changed = [];
    for (const [path, identity] of before) {
        const now = after.get(path);
        if (now === undefined)
            removed.push(path);
        else if (now !== identity)
            changed.push(path);
    }
    const added = [];
    for (const path of after.keys())
        if (!before.has(path))
            added.push(path);
    return { added, removed, changed };
}
/** Every path of the difference: the removed and changed, then the added. */
export function paths(d) {
    return [...d.removed, ...d.changed, ...d.added];
}
export function isEmpty(d) {
    return d.added.length === 0 && d.removed.length === 0 && d.changed.length === 0;
}
