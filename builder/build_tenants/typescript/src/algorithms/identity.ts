/**
 * `identity`: the content identity of an asset, read from the identities git
 * gives of the workspace's files and folders (C1). Files git ignores are no
 * part of them; no content is read or kept.
 *
 * @uses C1
 * @is REQ-ALG-001
 */
import type { IdentityMap } from "../kit/content_addressing.js"
import { pathsOf, type Node } from "../graph/terms.js"

/**
 * The asset's identity: that of the file or folder at its place, or undefined
 * when nothing is there. An asset at several paths has the identities of those
 * that are there, each after its path, one to a line, as a folder's names and
 * identities make the folder's.
 */
export function identity(asset: Node, tree: IdentityMap): string | undefined {
  const paths = pathsOf(asset)
  if (paths.length === 1) return tree.get(paths[0] ?? "")
  const there = paths.flatMap((path) => (tree.has(path) ? [`${path} ${tree.get(path) ?? ""}`] : []))
  return there.length === 0 ? undefined : there.join("\n")
}

/** The identity git gives the file or folder at each path of an asset, read back from the asset's identity: the inverse of `identity`. */
export function byPath(asset: Node, id: string | undefined): IdentityMap {
  if (id === undefined) return new Map()
  const paths = pathsOf(asset)
  if (paths.length === 1) return new Map([[paths[0] ?? "", id]])
  return new Map(id.split("\n").map((line) => [line.slice(0, line.lastIndexOf(" ")), line.slice(line.lastIndexOf(" ") + 1)]))
}
