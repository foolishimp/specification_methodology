/**
 * Three-valued conjunction: of results yes, no and cannot, the result is
 * cannot if any is cannot, else no if any is no, else yes.
 *
 * @carries C3
 */

export type Tri = "yes" | "no" | "cannot"

/** The conjunction of the results. No results at all give yes. */
export function all(results: Iterable<Tri>): Tri {
  let sum: Tri = "yes"
  for (const result of results) {
    if (result === "cannot") return "cannot"
    if (result === "no") sum = "no"
  }
  return sum
}
