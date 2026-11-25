/**
 * Order by name: names in the order of their characters.
 *
 * @carries H2
 */
/** The names, in the order of their characters. */
export function byName(names) {
    return [...names].sort();
}
/** Of the items, the one whose name comes first in the order of their characters. */
export function firstByName(items, nameOf) {
    let first;
    for (const item of items)
        if (first === undefined || nameOf(item) < nameOf(first))
            first = item;
    return first;
}
