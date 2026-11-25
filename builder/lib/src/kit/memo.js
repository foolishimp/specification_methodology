/**
 * Memo by content key: the result of a function with no effects, or of a
 * check, which gives the same result on the same content, kept under the
 * identities of all its inputs and read under exactly that key.
 *
 * @carries C4
 */
/** Each part is written with its length first, so two keys share a form only when they are equal. */
function form(key) {
    let text = "";
    for (const part of key)
        text += `${part.length}:${part};`;
    return text;
}
export function memo() {
    const kept = new Map();
    return {
        lookup: (key) => kept.get(form(key)),
        keep: (key, value) => {
            kept.set(form(key), value);
        }
    };
}
