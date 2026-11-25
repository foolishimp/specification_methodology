// Runs the getting-started guide's commands on a release just installed, with the stand-in agent where a session is
// needed, and gives the first line the guide gives as printed that was not printed, or the first command the release
// refused that the guide does not give as refused (REQ-INTERFACE-003, D236). The guide walks scenario S1's product
// from nothing to a change, so a release on which that walk does not end as the guide says is not cut (REQ-VERIFY-001).
//
// How the guide is read:
//   a block fenced as ```sh     commands, one to a line, run in their order in a new folder;
//   a block fenced as ```text   lines the product printed for the commands given since the last such block;
//   a block fenced as ```ticket lines a ticket of the workspace set up holds;
//   `<...>` in a line given as printed stands for any text.
// A command `stdo-builder <words>` runs the installed command, `run` with `--stand-in <fixtures>` added. The command
// `sh install.sh <folder>` is the install the cut has just made, so it is not made again. Any other line is run by sh.
// The folder `stdo-builder setup` is first given lies inside a larger git repository, as the guide says: the folder
// above it is made one, with one commit, before set-up.
//
// A command that ends with a code other than 0 is refused. The guide gives a refusal only as the last command of its
// ```sh block, followed by a ```text block that gives a line the refusal printed; any other refusal fails the walk.
//
// The stand-in's fixtures are given for each ticket the guide writes, in order: the first, a whole set; each next, the
// files that differ for the next ticket, laid over the set before. A ticket after the last given keeps the last set.

import { execFileSync, spawnSync } from "node:child_process"
import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs"
import { dirname, join } from "node:path"

/** The guide's fenced blocks, each with its kind, its lines and the number of each line in the guide. */
export function blocks(guide) {
  const out = []
  let open
  for (const [i, line] of guide.split("\n").entries()) {
    const fence = /^```(\S*)\s*$/.exec(line)
    if (fence === null) {
      if (open !== undefined && line.trim() !== "") {
        open.lines.push(line)
        open.at.push(i + 1)
      }
    } else if (open === undefined) {
      open = { kind: fence[1] ?? "", lines: [], at: [] }
    } else {
      out.push(open)
      open = undefined
    }
  }
  return out
}

/** The words of a command line, as sh splits them: by white space, with "..." kept as one. */
export function words(line) {
  return [...line.matchAll(/"((?:[^"\\]|\\.)*)"|(\S+)/g)].map((m) => (m[1] !== undefined ? m[1].replace(/\\(.)/g, "$1") : m[2]))
}

/** Whether `given`, a line the guide gives with `<...>` for any text, is the line `printed`. */
export function matches(given, printed) {
  const pattern = given.trim().split("<...>").map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join(".*")
  return new RegExp(`^${pattern}$`).test(printed.trim())
}

const ticketLines = (workspace) => {
  const tickets = join(workspace, ".ai-workspace", "tickets")
  if (!existsSync(tickets)) return []
  return readdirSync(tickets, { recursive: true }).map(String).filter((f) => f.endsWith(".md")).flatMap((f) => readFileSync(join(tickets, f), "utf8").split("\n"))
}

/**
 * Runs the guide in `folder`, a new folder, with the installed command in `bin` and the stand-in's `fixtures`, one
 * folder for each ticket the guide writes (above). Gives `{ commands }` where every line it gives as printed was
 * printed and the release refused no command but as the guide gives it; `{ line, printed }` for the first line given as
 * printed that was not; and `{ refused, at, status, printed }` for the first command, at line `at` of the guide, that
 * the release refused with `status` where the guide does not give its refusal.
 */
export function runGuide(guide, { bin, fixtures, folder }) {
  const config = join(folder, ".gitconfig")
  writeFileSync(config, "")
  const env = { ...process.env, PATH: `${bin}:${dirname(process.execPath)}:${process.env.PATH ?? ""}`, GIT_CONFIG_GLOBAL: config, GIT_CONFIG_NOSYSTEM: "1" }
  for (const name of ["GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY", "GIT_COMMON_DIR"]) delete env[name]
  const work = join(folder, "work")
  mkdirSync(work)
  // The fixtures for each ticket, each next set laid over a copy of the one before.
  const sets = fixtures.map((given, i) => {
    if (i === 0) return given
    const set = join(folder, `fixtures-${i + 1}`)
    cpSync(fixtures[0], set, { recursive: true })
    for (const over of fixtures.slice(1, i + 1)) cpSync(over, set, { recursive: true })
    return set
  })
  let printed = []
  let workspace
  let commands = 0
  let tickets = 0
  // The last command, where the release refused it: it stands only where the next block gives a line it printed.
  let refused
  for (const block of blocks(guide)) {
    if (block.kind === "sh") {
      for (const [i, line] of block.lines.entries()) {
        const [first, ...rest] = words(line)
        if (first === "sh" && rest[0] === "install.sh") continue
        if (refused !== undefined) return refused
        commands += 1
        let r
        if (first === "stdo-builder") {
          if (rest[0] === "setup" && workspace === undefined && rest[1] !== undefined) {
            workspace = join(work, rest[1])
            const above = dirname(workspace)
            if (above !== work && !existsSync(above)) {
              mkdirSync(above, { recursive: true })
              execFileSync("git", ["init", "-q", "-b", "main", above], { env })
              execFileSync("git", ["-C", above, "-c", "user.name=guide", "-c", "user.email=guide@localhost", "commit", "-q", "--allow-empty", "-m", "the larger repository"], { env })
            }
          }
          if (rest[0] === "ticket") tickets += 1
          const args = rest[0] === "run" ? [...rest, "--stand-in", sets[Math.min(Math.max(tickets, 1), sets.length) - 1]] : rest
          r = spawnSync(join(bin, "stdo-builder"), args, { cwd: work, env, encoding: "utf8" })
        } else {
          r = spawnSync("sh", ["-c", line], { cwd: work, env, encoding: "utf8" })
        }
        const said = `${r.stdout ?? ""}${r.stderr ?? ""}`.split("\n")
        printed.push(...said)
        if (r.status !== 0) refused = { refused: line, at: block.at[i], status: r.status ?? r.signal, printed: said.filter((l) => l.trim() !== "") }
      }
    } else if (block.kind === "text") {
      for (const line of block.lines) if (!printed.some((p) => matches(line, p))) return { line, printed }
      if (refused !== undefined && !block.lines.some((line) => refused.printed.some((p) => matches(line, p)))) return refused
      refused = undefined
      printed = []
    } else if (block.kind === "ticket") {
      if (refused !== undefined) return refused
      const held = workspace === undefined ? [] : ticketLines(workspace)
      for (const line of block.lines) if (!held.some((p) => matches(line, p))) return { line, printed: held }
    }
  }
  if (refused !== undefined) return refused
  return { commands }
}
