from pathlib import Path
import json, shutil, sys
R=Path(__file__).resolve().parents[1]
APPLY='--apply' in sys.argv
if not APPLY:
 print('DRY-RUN regenerate .agents and host projections from .pmcro; pass --apply'); raise SystemExit(0)
def cp(s,d):
 d.parent.mkdir(parents=True,exist_ok=True)
 if s.is_dir(): shutil.copytree(s,d)
 else: shutil.copy2(s,d)
for n in ['.agents','.claude','.grok','.cursor']:
 p=R/n
 if p.exists(): shutil.rmtree(p)
# preserve workflow/plugin subtrees in .github, remove generated files only
g=R/'.github'
for n in ['agents','skills']:
 p=g/n
 if p.exists(): shutil.rmtree(p)
for n in ['catalog.json','index.json','routing.json','lifecycle.json','grants.json','project.json','queue.json','README.md','STRUCTURE.md']:
 p=g/n
 if p.exists(): p.unlink()
a=R/'.agents';a.mkdir()
for n in ['catalog.json','index.json','routing.json','lifecycle.json','grants.json','project.json','queue.json']: cp(R/'.pmcro/control'/n,a/n)
cp(R/'.pmcro/control/marketplace.json',a/'plugins/marketplace.json');cp(R/'.pmcro/agents',a/'agents')
cat=json.loads((R/'.pmcro/control/catalog.json').read_text(encoding='utf-8-sig'))
for row in cat['skills']:
 s=R/'.pmcro/plugins'/row['plugin']/'skills'/row['id']/'SKILL.md'
 if s.is_file():
  d=a/'skills'/row['plugin']/row['id']/'SKILL.md';cp(s,d);(d.parent/'projection.json').write_text(json.dumps({'canonical':f".pmcro/plugins/{row['plugin']}/skills/{row['id']}",'generated':True},indent=2)+'\n',encoding='utf-8')
(a/'README.md').write_text('# Agent projection\n\nGenerated from `.pmcro`; do not edit as authority.\n',encoding='utf-8')
for host in ['.claude','.grok','.cursor','.github']:
 h=R/host;h.mkdir(parents=True,exist_ok=True)
 for n in ['catalog.json','index.json','routing.json','lifecycle.json','grants.json','project.json','queue.json']:cp(a/n,h/n)
 cp(a/'agents',h/'agents');cp(a/'skills',h/'skills')
 (h/'README.md').write_text(f'# {host} host surface\n\nGenerated projection. Authority: `{host} -> .agents -> .pmcro`.\n',encoding='utf-8')
 (h/'STRUCTURE.md').write_text(f'# Structure\n\n`{host} -> .agents -> .pmcro`\n',encoding='utf-8')
print('SYNC-PASS')
