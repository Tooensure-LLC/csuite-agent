# Architecture

`csuite-agent` is a business-domain meta-orchestrator. Executive child agents own bounded decision domains and local trails. PMCR-O remains ORCHESTRATE -> PLAN -> MAKE -> CHECK -> REFLECT. A domain agent may itself orchestrate specialized children. A skill is an executable capability; it is not automatically an orchestrator.

Cross-agent handoffs reference source trail + digest and create a local receiving trail. Shared mutable trails are forbidden.
