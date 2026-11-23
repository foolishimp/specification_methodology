/**
 * Bounded loop with a measure: a loop goes on while its measure strictly falls
 * and its bound is not reached, so it ends within the bound.
 *
 * @carries C9
 */
/** The measure strictly falls. With no earlier measure, the first round counts as falling. */
export function falls(before, now) {
    return before === undefined || now < before;
}
/** The bound is not reached: another round may follow the `used` rounds made so far, measure aside. */
export function within(used, bound) {
    return used < bound;
}
/** Whether another round may follow the `used` rounds made so far. */
export function goesOn(before, now, used, bound) {
    return within(used, bound) && falls(before, now);
}
