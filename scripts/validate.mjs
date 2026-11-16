import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const errors=[];
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const required=['README.md','GOVERNANCE.md','AGENTS.md','CONTRIBUTING.md','CHANGELOG.md','VERSION','LICENSE','ACKNOWLEDGEMENTS.md','evals/cases.json','evals/RESULTS.md','skills/robot-learning-paper-reading/SKILL.md','skills/robot-learning-paper-reading/agents/openai.yaml'];
for(const p of required) if(!fs.existsSync(path.join(root,p))) errors.push('Missing '+p);
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
const version=read('VERSION').trim();
if(!/^\d+\.\d+\.\d+$/.test(version))errors.push('Invalid VERSION');
if(!read('CHANGELOG.md').includes('## '+version+' ��'))errors.push('Version missing in changelog');
if(!read('README.md').includes(version))errors.push('README version drift');
const skillPath='skills/robot-learning-paper-reading/SKILL.md';
const skill=read(skillPath);
const front=skill.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
if(!front)errors.push('Missing YAML frontmatter');
else{
const lines=front[1].split(/\r?\n/);
if(lines.length!==2||lines[0]!=='name: robot-learning-paper-reading'||!lines[1].startsWith('description: ')||lines[1].length<80)errors.push('Unexpected skill frontmatter');
}
if(skill.split('\n').length>500)errors.push('Skill exceeds 500 lines');
if(/\[TODO|TBD:/.test(skill))errors.push('Unfilled template');
const meta=read('skills/robot-learning-paper-reading/agents/openai.yaml');
if(!meta.includes('$robot-learning-paper-reading'))errors.push('Default prompt lacks skill name');
function walk(dir){
for(const entry of fs.readdirSync(dir,{withFileTypes:true})){
if(['.git','node_modules','local'].includes(entry.name))continue;
const p=path.join(dir,entry.name);
if(entry.isDirectory())walk(p);
else if(entry.name.endsWith('.md')){
const s=fs.readFileSync(p,'utf8');
for(const m of s.matchAll(/\[[^\]]*\]\(([^)\s]+)\)/g)){
const target=m[1].split('#')[0];
if(!target||/^[a-z]+:/i.test(target))continue;
const resolved=path.resolve(path.dirname(p),target);
if(!resolved.startsWith(root+path.sep)||!fs.existsSync(resolved))errors.push('Broken/escaping link '+path.relative(root,p)+': '+target);
}
}
}
}
walk(root);
try{
const cases=JSON.parse(read('evals/cases.json'));
const seen=new Set();
for(const c of cases){
if(!c.id||seen.has(c.id)||typeof c.prompt!=='string'||!Array.isArray(c.rubric)||!c.rubric.length)errors.push('Invalid/duplicate eval case '+c.id);
seen.add(c.id);
}
if(cases.length<6)errors.push('Missing regression coverage');
}catch(e){errors.push('Invalid cases JSON: '+e.message);}
if(errors.length){console.error(errors.join('\n'));process.exit(1);}
console.log('PASS: structure, metadata, versions, local links and evaluation schema.');
console.log('Behavioral reading quality is NOT validated by this script.');
