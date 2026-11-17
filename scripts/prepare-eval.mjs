import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const out=path.join(root,'local','eval-inputs');
fs.mkdirSync(out,{recursive:true});
const cases=JSON.parse(fs.readFileSync(path.join(root,'evals','cases.json'),'utf8'));
for(const c of cases){
  const input={id:c.id,prompt:c.prompt,input_files:(c.input_files||[]).map(p=>path.resolve(root,p))};
  fs.writeFileSync(path.join(out,c.id+'.json'),JSON.stringify(input,null,2)+'\n');
}
console.log(`Prepared ${cases.length} prompt-only inputs in local/eval-inputs. Rubrics withheld.`);
