/**
 * White-space test: whether a name holds white space.
 *
 * @carries H3
 */
/** The name holds a character of white space. */
export function holdsWhiteSpace(name) {
    return /\s/.test(name);
}
