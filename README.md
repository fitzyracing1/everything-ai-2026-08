# everything-ai

**Build Everything in AI** — Autonomous AI system builder delivered by persistent-self-coder.

Bootstrapped 2026-08-06 in Grok sandbox from the request: "Build everything in ai"

## Vision
A self-contained, local-first AI runtime that can interpret high-level goals and autonomously generate, compose, test, and deliver working software, simulations, documents, and agents — using only the sandbox resources and the collection of specialized skills present in the environment.

## Current Capabilities (MVP)
- Goal → plan → code generation loop
- Tool composition inspired by Starfit (header grabbing + body welding)
- Persistent log of decisions and deliveries
- Modular agent registry (perception, planning, execution, critique)
- Ready for extension with any of the local skills (BMD conceptual agents, ternary trees, rest-api sandboxes, etc.)

## Quick Start
```bash
cd /home/workdir/artifacts/everything-ai
python3 -m src.ai.main "build a simple REST API mock for todo items"
python3 -m src.ai.main "create a ternary search tree demo"
```

## Architecture
- `src/ai/core/` — runtime, planner, executor
- `src/ai/agents/` — specialized agents
- `src/ai/builders/` — domain-specific generators
- Generated outputs land under `generated/`

## Self-Delivery Origin
This entire repository was created and is being extended by the persistent-self-coder skill in response to an open-ended request. Every new module is accompanied by a log entry explaining the presumed need and evidence.

## Next Autonomous Steps
1. Implement full Starfit-compatible tool registry
2. Wire in subsumption architecture priority stack
3. Add decision-audit-log integration
4. Generate example agents for farming-almanac, cloud-attack-monitor, and conceptual BMD simulation

## Documentation

- In-repo docs: [docs/](docs/index.md)
- Wiki: [https://github.com/fitzyracing1/everything-ai-2026-08/wiki](https://github.com/fitzyracing1/everything-ai-2026-08/wiki)
