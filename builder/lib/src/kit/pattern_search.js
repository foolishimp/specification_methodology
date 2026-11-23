/**
 * Pattern search: the names of a given form in a text, for the check of
 * traceability. A form is a regular expression, given as text.
 *
 * @carries H4
 */
/** The form of the text given, or undefined where the text is no form. */
export function formOf(text) {
    try {
        return { pattern: new RegExp(text, "g") };
    }
    catch {
        return undefined;
    }
}
/** Every name of the form in the text, in the order they stand, as often as each stands. */
export function namesIn(text, form) {
    return [...text.matchAll(form.pattern)].map((m) => m[0]);
}
