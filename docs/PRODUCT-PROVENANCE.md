# Product provenance

The raw PMCR-O trail is **not required to be the primary product UI**. Product views are reconstructed from queue messages, local trails, governance audit references, receipts, and checker outcome attestations.

Recommended product objects: decisions, delegations, approvals, executions, outcomes, incidents, and audits.

`governance.audit.reference` points to the governance provider's tamper-evident record; PMCR-O does not duplicate that audit log. `outcome.attestation` is produced by independent CHECK because governance authorization evidence and real-world outcome evidence are different facts.
