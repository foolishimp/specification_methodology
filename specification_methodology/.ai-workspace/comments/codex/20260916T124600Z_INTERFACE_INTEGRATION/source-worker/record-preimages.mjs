import {readFile,writeFile,mkdir,copyFile,stat} from 'node:fs/promises';
import {join,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';
const evidence=dirname(fileURLToPath(import.meta.url)),root='/Users/jim/src/apps/specification_methodology/specification_methodology';
const sha=b=>createHash('sha256').update(b).digest('hex');
const paths=['specification/standards/STDO_REFERENCE_FRAME_BASELINE.md','specification/standards/authority_compressions/stdo_compressed.md','specification/standards/authority_compressions/stdo_bootstrap.md','tests/test_reference_frame_boundaries.py'];
const rows=[];for(const path of paths){const bytes=await readFile(join(root,path));await mkdir(dirname(join(evidence,'preimages',path)),{recursive:true});await copyFile(join(root,path),join(evidence,'preimages',path));rows.push({path,bytes:bytes.length,sha256:sha(bytes)})}
const newPath='tests/test_interface_integration_frame.py';try{await stat(join(root,newPath));throw Error('new test exists')}catch(error){if(error.code!=='ENOENT')throw error}
const protectedPaths=['specification/standards/REFERENCE_FRAME_METHOD.md','specification/PRODUCT.md','specification/REFERENCE_FRAME_BASIS.md','stdo_default.json','AGENTS.md','CLAUDE.md'];
const protectedRows=[];for(const path of protectedPaths)protectedRows.push({path,sha256:sha(await readFile(join(root,path)))});
const proposal='.ai-workspace/comments/codex/20260916T122500Z_STRATEGY_end_to_end_interface_integration_frame.md',proposalSha256=sha(await readFile(join(root,proposal)));
assert.equal(proposalSha256,'9625194d4b51af53df61c55665dbfb463a03f74d0aebe6c149f34dafe268e589');
await writeFile(join(evidence,'preimages.json'),JSON.stringify({recordedAt:new Date().toISOString(),canonical:rows,newPath,protectedRows,proposal,proposalSha256},null,2)+'\n');console.log(JSON.stringify(rows,null,2));
