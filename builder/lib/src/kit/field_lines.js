/**
 * Field lines: a text's fields, read from lines of the form `- field: value`,
 * as a ticket gives them, those lines written for given fields, and a text
 * without the lines of one field.
 *
 * @carries H5
 */
/**
 * The field lines of a text: each line of the form `- name: value` or
 * `name: value`, where the name is a word. The last line for a name gives its
 * value, so a ticket inducted again reads as its last induction. Every other line
 * is the text's own and is read as nothing.
 */
export function fieldsOf(written) {
    const fields = new Map();
    for (const line of written.split("\n")) {
        const m = FIELD.exec(line);
        if (m?.[1] !== undefined)
            fields.set(m[1], m[2] ?? "");
    }
    return fields;
}
/** A field line: its name and its value. */
const FIELD = /^(?:- )?([a-z_]+): *(.*?)\s*$/;
/** The text without any line `fieldsOf` reads as the field `name`; every other line as it is. */
/** Every value of the field `name`, in the order its lines are written. */
export function valuesOf(written, name) {
    return written.split("\n").flatMap((line) => {
        const m = FIELD.exec(line);
        return m?.[1] === name ? [m[2] ?? ""] : [];
    });
}
export function withoutField(written, name) {
    return written.split("\n").filter((line) => FIELD.exec(line)?.[1] !== name).join("\n");
}
/** The field lines that give these fields, in this order, as `fieldsOf` reads them. */
export function writeFields(fields) {
    return fields.map(([name, value]) => `- ${name}: ${value}\n`).join("");
}
