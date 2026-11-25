/**
 * First-match rule list: rules in a fixed order; the first whose condition
 * holds gives the result. The order is part of the definition.
 *
 * @carries C8
 */
/** The result of the first rule that holds, or `otherwise` when none does. */
export function firstMatch(rules, input, otherwise) {
    for (const rule of rules)
        if (rule.holds(input))
            return rule.gives(input);
    return otherwise(input);
}
