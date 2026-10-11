from pathlib import Path
import argparse,json,re
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--company-id',required=True);p.add_argument('--legal-name',required=True);p.add_argument('--display-name',required=True);p.add_argument('--industry',default='unspecified');p.add_argument('--timezone',default='UTC');p.add_argument('--apply',action='store_true');a=p.parse_args()
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',a.company_id):raise SystemExit('company-id must be kebab-case')
t=json.loads((R/'.pmcro/company/business.template.json').read_text());t.update({'companyId':a.company_id,'legalName':a.legal_name,'displayName':a.display_name,'industry':a.industry,'timezone':a.timezone})
out=R/'.pmcro/company/business.json'
if not a.apply: print(json.dumps(t,indent=2));print('DRY-RUN; pass --apply');raise SystemExit(0)
out.write_text(json.dumps(t,indent=2)+'\n',encoding='utf-8');print(f'WROTE {out}')
