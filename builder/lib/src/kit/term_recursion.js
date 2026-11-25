/**
 * Structural recursion over terms, with a normal form: a function of a tree of
 * terms follows the shape of the terms, and two rewrites give the normal form
 * (a sequence inside a sequence is flattened; a term that does nothing is
 * dropped from a sequence).
 *
 * @carries C5
 */
/** Folds a term from its leaves up: each term is given the results of its parts. */
export function fold(shape, term, f) {
    return f(term, shape.parts(term).map((part) => fold(shape, part, f)));
}
/** The normal form of a term, in one pass over its terms. */
export function normal(shape, term) {
    const parts = shape.parts(term).map((part) => normal(shape, part));
    if (!shape.isSequence(term))
        return shape.rebuild(term, parts);
    const kept = [];
    for (const part of parts) {
        if (shape.isSequence(part))
            kept.push(...shape.parts(part));
        else if (!shape.isInert(part))
            kept.push(part);
    }
    return shape.rebuild(term, kept);
}
