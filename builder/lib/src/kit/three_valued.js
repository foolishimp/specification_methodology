/**
 * Three-valued conjunction: of results yes, no and cannot, the result is
 * cannot if any is cannot, else no if any is no, else yes.
 *
 * @carries C3
 */
/** The conjunction of the results. No results at all give yes. */
export function all(results) {
    let sum = "yes";
    for (const result of results) {
        if (result === "cannot")
            return "cannot";
        if (result === "no")
            sum = "no";
    }
    return sum;
}
