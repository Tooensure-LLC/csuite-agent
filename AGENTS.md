# Agent instructions

Read `.agents/project.json` and `.agents/catalog.json` first. `.agents` points to `.pmcro`; it does not own authority. Never discover credentials, widen grants, skip CHECK, or make the Maker its own Checker. Cross-agent work uses immutable handoff messages and local trails, not one shared mutable trail. If required authority/capability is absent, HALT or route to the registered skill creator; do not invent functionality.
