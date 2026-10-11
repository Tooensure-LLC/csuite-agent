from pathlib import Path
import hashlib,json,sys
R=Path(__file__).resolve().parents[1];fail=[];passed=[]
def ok(v,m):(passed if v else fail).append(m);print(('PASS ' if v else 'FAIL ')+m)
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
meta=j(R/'.pmcro/control/project.json');ok(meta['id']=='csuite-agent','project id');ok(meta['canonical']=='.pmcro' and meta['projection']=='.agents','authority chain')
life=j(R/'.pmcro/control/lifecycle.json');ok(life['autonomous'] and not life['questionGate'] and life['checker']['independent'],'autonomous independent checker')
routing=j(R/'.pmcro/control/routing.json');ok(not routing['questionGate'] and routing['unresolvedAmbiguity']['askUser'] is False,'no clarification gate')
reg=j(R/'.pmcro/agents/registry.json');ok(len(reg['agents'])==9,'nine executive child agents')
for row in j(R/'.pmcro/control/catalog.json')['skills']:
 s=R/'.pmcro/plugins'/row['plugin']/'skills'/row['id'];ok((s/'SKILL.md').is_file(),f"{row['plugin']}/{row['id']} SKILL.md")
 for d in ['agents','scripts','references','assets','tests']:ok((s/d).is_dir() and any(x.is_file() for x in (s/d).rglob('*')),f"{row['plugin']}/{row['id']} {d}")
for n in ['catalog.json','index.json','routing.json','lifecycle.json','grants.json','project.json','queue.json']:
 a=(R/'.agents'/n).read_bytes();c=(R/'.pmcro/control'/n).read_bytes();ok(a==c,f'.agents/{n} exact projection')
 for h in ['.claude','.grok','.cursor','.github']:ok((R/h/n).read_bytes()==a,f'{h}/{n} mirrors .agents')
q=R/'.pmcro/queue';ok((q/'scripts/enqueue.ps1').is_file() and (q/'scripts/claim.ps1').is_file() and (q/'scripts/ack.ps1').is_file(),'queue scripts present')
ag=j(R/'.pmcro/protocol/agent-agreement.schema.json');ok(ag['sharedMutableTrail'] is False and ag['receiverCreatesLocalTrail'] is True,'local trail agreement')
k=j(R/'.pmcro/protocol/message-kinds.json')['kinds'];ok(all(x in k for x in ['executive.advice','executive.decision','executive.delegation','executive.review','executive.escalation','governance.audit.reference','outcome.attestation']),'C-suite queue message kinds')
cq=j(R/'.pmcro/protocol/csuite-queue-contract.json');ok(cq['delegation']['externalMutationByExecutive'] is False and cq['governanceEvidence']['copyAuditLog'] is False,'C-suite delegation/audit boundary')
pp=j(R/'.pmcro/protocol/product-provenance.json');ok(pp['rawTrailIsPrimaryUX'] is False and 'outcome' in pp['productObjects'],'product provenance model')
print(f'SUMMARY pass={len(passed)} fail={len(fail)}');raise SystemExit(1 if fail else 0)
