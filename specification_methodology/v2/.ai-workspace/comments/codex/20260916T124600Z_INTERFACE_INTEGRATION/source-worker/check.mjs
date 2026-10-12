import {spawn} from 'node:child_process';
import {mkdir,writeFile,readFile} from 'node:fs/promises';
import {join,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const evidence=dirname(fileURLToPath(import.meta.url)),root='/Users/jim/src/apps/specification_methodology/specification_methodology';
const sha=b=>createHash('sha256').update(b).digest('hex');
const output=process.argv[2]??'proof';if(!['proof','proof-final'].includes(output))throw Error('explicit proof-local output');
await mkdir(join(evidence,output),{recursive:true});await mkdir(join(evidence,'tmp'),{recursive:true});
const commands=[
  ['frame-boundaries','python3',['-B','-m','unittest','discover','-s','tests','-p','test_reference_frame_boundaries.py','-v']],
  ['interface-frame','python3',['-B','-m','unittest','discover','-s','tests','-p','test_interface_integration_frame.py','-v']],
  ['compression','python3',['-B','-m','unittest','discover','-s','tests','-p','test_compressions.py','-v']],
  ['diff-check','git',['diff','--check','--','specification/standards/STDO_REFERENCE_FRAME_BASELINE.md','specification/standards/authority_compressions/stdo_compressed.md','specification/standards/authority_compressions/stdo_bootstrap.md','tests/test_reference_frame_boundaries.py']],
];
const results=[];
for(const[name,command,args]of commands){
  const started=Date.now(),result=await new Promise(resolve=>{
    const child=spawn(command,args,{cwd:root,env:{...process.env,PYTHONDONTWRITEBYTECODE:'1',TMPDIR:join(evidence,'tmp')},stdio:['ignore','pipe','pipe']});
    let stdout='',stderr='';const timer=setTimeout(()=>child.kill('SIGTERM'),60000);
    child.stdout.on('data',b=>{stdout+=b;process.stdout.write(b)});child.stderr.on('data',b=>{stderr+=b;process.stderr.write(b)});
    child.on('close',(code,signal)=>{clearTimeout(timer);resolve({pid:child.pid,code,signal,stdout,stderr})});
  });
  const bytes=result.stdout+result.stderr;await writeFile(join(evidence,output,name+'.log'),bytes);
  results.push({name,command:[command,...args],cwd:root,startedAt:new Date(started).toISOString(),elapsedMs:Date.now()-started,pid:result.pid,code:result.code,signal:result.signal,outputSha256:sha(bytes)});
  await writeFile(join(evidence,output,'commands.json'),JSON.stringify(results,null,2)+'\n');
  if(result.code!==0)process.exit(result.code??1);
}
console.log(JSON.stringify({passed:true,commands:results.length},null,2));
