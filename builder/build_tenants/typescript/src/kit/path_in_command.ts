/**
 * Placing a path in a command: the path put where the command marks it, at
 * each mark, or added at its end where it has none. A check's command marks a
 * place by a name in braces; each word that holds the mark is written once for
 * each path the name is given.
 *
 * @carries H6
 */

/** The mark in a command where the path goes. */
const MARK = "{brief}"

/** The command with the path at each of its marks, or added at its end. */
export function withPath(command: readonly string[], path: string): readonly string[] {
  return command.some((w) => w.includes(MARK)) ? command.map((w) => w.split(MARK).join(path)) : [...command, path]
}

/** The command with each word that marks a name, `{name}`, written once for each of that name's paths. */
export function withPaths(command: readonly string[], paths: ReadonlyMap<string, readonly string[]>): readonly string[] {
  return command.flatMap((w) => {
    const name = [...paths.keys()].find((n) => w.includes(`{${n}}`))
    return name === undefined ? [w] : (paths.get(name) ?? []).map((path) => w.split(`{${name}}`).join(path))
  })
}
