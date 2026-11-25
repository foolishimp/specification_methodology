// The download of a release (REQ-INTERFACE-004, D234): one compressed file of the bundle, a ustar archive in gzip,
// written and read back by this module alone. The cut does not rest on the platform's tar, which on macOS adds a side
// file for a file's extended attributes and names the person who cut it on every member: this writer takes only the
// bytes of each file the bundle's manifest names, and writes each as a plain file with owner and group 0 and no name.
//
// pack(members, mtime)  members: [{ name, data, executable }] in their order; gives the gzip of the archive
// ofBundle(bundle, top)  the members of a bundle's download: each file its manifest names, and the manifest, under top/
// read(download)        every member of a download as it is written, with its header's fields, refused where a header
//                       does not read
// unpack(download, to)  writes every member of a download as a file under `to`, a member that is not a plain file
//                       included: so a side file that a reader keeps would be there to be found

import { mkdirSync, readFileSync, statSync, writeFileSync } from "node:fs"
import { dirname, join, normalize, sep } from "node:path"
import { gunzipSync, gzipSync } from "node:zlib"

const BLOCK = 512
const RECORD = 20 * BLOCK

const octal = (n, width) => `${n.toString(8).padStart(width - 1, "0")}\0`

/** A member's name split into ustar's prefix and name; a path that cannot be split so is refused. */
const split = (path) => {
  const bytes = Buffer.byteLength(path)
  if (bytes <= 100) return { prefix: "", name: path }
  for (let at = path.indexOf("/"); at !== -1; at = path.indexOf("/", at + 1)) {
    const prefix = path.slice(0, at)
    const name = path.slice(at + 1)
    if (Buffer.byteLength(prefix) <= 155 && Buffer.byteLength(name) <= 100 && name !== "") return { prefix, name }
  }
  throw new Error(`${path} is too long a path for the download: a ustar member's name holds at most 100 bytes after its last folder of at most 155`)
}

function header(path, size, mode, mtime) {
  const h = Buffer.alloc(BLOCK)
  const { prefix, name } = split(path)
  h.write(name, 0, 100, "utf8")
  h.write(octal(mode, 8), 100, 8, "ascii")
  h.write(octal(0, 8), 108, 8, "ascii")
  h.write(octal(0, 8), 116, 8, "ascii")
  h.write(octal(size, 12), 124, 12, "ascii")
  h.write(octal(mtime, 12), 136, 12, "ascii")
  h.write("        ", 148, 8, "ascii")
  h.write("0", 156, 1, "ascii")
  h.write("ustar\0", 257, 6, "ascii")
  h.write("00", 263, 2, "ascii")
  // The owner's and the group's names, at 265 and 297, are left empty.
  h.write(prefix, 345, 155, "utf8")
  let sum = 0
  for (const b of h) sum += b
  h.write(`${sum.toString(8).padStart(6, "0")}\0 `, 148, 8, "ascii")
  return h
}

export function pack(members, mtime) {
  const parts = []
  for (const m of members) {
    parts.push(header(m.name, m.data.length, m.executable ? 0o755 : 0o644, mtime), m.data)
    const pad = (BLOCK - (m.data.length % BLOCK)) % BLOCK
    if (pad > 0) parts.push(Buffer.alloc(pad))
  }
  parts.push(Buffer.alloc(2 * BLOCK))
  const length = parts.reduce((n, p) => n + p.length, 0)
  const rest = (RECORD - (length % RECORD)) % RECORD
  if (rest > 0) parts.push(Buffer.alloc(rest))
  return gzipSync(Buffer.concat(parts), { level: 9 })
}

export function ofBundle(bundle, top) {
  const files = [...JSON.parse(readFileSync(join(bundle, "manifest.json"), "utf8")).files.map((f) => f.path), "manifest.json"]
  return files.map((path) => ({ name: `${top}/${path}`, data: readFileSync(join(bundle, path)), executable: (statSync(join(bundle, path)).mode & 0o111) !== 0 }))
}

const text = (h, at, width) => {
  const field = h.subarray(at, at + width)
  const end = field.indexOf(0)
  return field.subarray(0, end === -1 ? width : end).toString("utf8")
}
const number = (h, at, width) => {
  const t = text(h, at, width).trim()
  if (!/^[0-7]*$/.test(t)) throw new Error(`a header of the download holds ${JSON.stringify(t)} where a number is written`)
  return t === "" ? 0 : parseInt(t, 8)
}

export function read(download) {
  const tar = gunzipSync(readFileSync(download))
  const members = []
  for (let at = 0; at + BLOCK <= tar.length;) {
    const h = tar.subarray(at, at + BLOCK)
    if (h.every((b) => b === 0)) break
    let sum = 0
    for (let i = 0; i < BLOCK; i++) sum += i >= 148 && i < 156 ? 32 : h[i]
    if (sum !== number(h, 148, 8)) throw new Error(`the header at byte ${at} of the download does not agree with its checksum`)
    const prefix = text(h, 345, 155)
    const name = `${prefix === "" ? "" : `${prefix}/`}${text(h, 0, 100)}`
    const size = number(h, 124, 12)
    members.push({
      name,
      type: text(h, 156, 1) === "" ? "0" : text(h, 156, 1),
      mode: number(h, 100, 8),
      uid: number(h, 108, 8),
      gid: number(h, 116, 8),
      uname: text(h, 265, 32),
      gname: text(h, 297, 32),
      data: tar.subarray(at + BLOCK, at + BLOCK + size)
    })
    at += BLOCK + Math.ceil(size / BLOCK) * BLOCK
  }
  return members
}

export function unpack(download, to) {
  for (const m of read(download)) {
    const path = normalize(m.name)
    if (path.startsWith("..") || path.startsWith(sep)) throw new Error(`${m.name} lies outside the folder it is unpacked into`)
    mkdirSync(dirname(join(to, path)), { recursive: true })
    writeFileSync(join(to, path), m.data, { mode: m.mode & 0o777 })
  }
}
