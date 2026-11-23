#!/bin/sh
# Installs the STDO bundle into the folder you name: sh install.sh <folder>
# It checks every file against manifest.json first and installs nothing where one differs.
# The standards go into <folder>/standards/<their release>, and STDO Builder into
# <folder>/lib and <folder>/bin by its own install script. Nothing is written anywhere
# else and nothing is fetched over the network.
set -eu
[ "$#" -eq 1 ] && [ -n "$1" ] || { echo "Name the folder to install into: sh install.sh <folder>" >&2; exit 2; }
here=$(cd "$(dirname "$0")" && pwd -P)
node -e '
const {createHash}=require("node:crypto"),fs=require("node:fs"),path=require("node:path")
const root=process.argv[1],m=JSON.parse(fs.readFileSync(path.join(root,"manifest.json"),"utf8"))
const seen=new Set(["manifest.json"]);let bad=0
const walk=d=>{for(const e of fs.readdirSync(path.join(root,d),{withFileTypes:true})){const p=d?d+"/"+e.name:e.name
 if(e.isDirectory())walk(p);else if(p!=="manifest.json"){const f=m.files.find(x=>x.path===p)
 if(!f){console.error("not in the manifest: "+p);bad++}else{seen.add(p)
 if(e.isSymbolicLink()||createHash("sha256").update(fs.readFileSync(path.join(root,p))).digest("hex")!==f.sha256){console.error("differs from the manifest: "+p);bad++}}}}}
walk("");for(const f of m.files)if(!seen.has(f.path)){console.error("missing: "+f.path);bad++}
if(bad)process.exit(4);console.log(m.name+"-"+m.version+": every file agrees with the manifest")
' "$here"
mkdir -p "$1"; dest=$(cd "$1" && pwd -P)
mv=$(node -p "require('$here/manifest.json').standards.release")
mkdir -p "$dest/standards"; rm -rf "$dest/standards/$mv"; cp -R "$here/standards" "$dest/standards/$mv"
sh "$here/builder/install.sh" "$dest"
echo "The standards are at $dest/standards/$mv. Put $dest/bin on your PATH, then read $here/builder/GETTING_STARTED.md."
