# csuite-agent

A reusable Tooensure LLC repository template for a PMCR-O governed virtual C-suite.

## Authority chain

`.claude/.grok/.cursor/.github -> .agents -> .pmcro`

`.pmcro` is canonical. `csuite-agent` is the meta-orchestrator. CEO, CFO, COO, CTO, CMO, CHRO, CISO, CLO, and Executive Council are specialized child agents with local trail ownership and bounded delegation. External side effects require separately registered domain agents and grants.

## Use this template

1. Create a repository from this GitHub template.
2. Run `python eng/init-business.py --company-id <id> --legal-name "<name>" --display-name "<name>" --apply`.
3. Run `python eng/sync-projections.py --apply`.
4. Run `python eng/validate.py`.
5. Connect only the domain agents the business has validated.

The durable queue is transport-neutral at the protocol level and ships with a filesystem-spool adapter for local/single-host use. Consumers are idempotent because delivery is at-least-once.
