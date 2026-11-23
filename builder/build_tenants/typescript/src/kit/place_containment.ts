/**
 * Place containment: whether a path is a given place or lies below it. Places
 * and paths are relative to one folder, their parts joined by "/".
 *
 * @carries H1
 */

/** The place covers the path: the path is the place, or lies below it. */
export function covers(place: string, path: string): boolean {
  return path === place || path.startsWith(`${place}/`)
}
