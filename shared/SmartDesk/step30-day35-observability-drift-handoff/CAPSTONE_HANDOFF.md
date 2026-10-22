# SmartDesk capstone hand-off

SmartDesk now covers the full FDE path: CLI, API and database, full stack, CI and Azure, RAG, agents, MCP, guardrails, evaluation, LLMOps, deployment and observability.

## What to reuse in the capstone (Days 36 to 40)
- `AGENTS.md` pattern for the team repo (build, test, style, never put secrets in prompts).
- Vulnerability report template and reports v1 to v3 (steps 6, 17, 25).
- Golden set, quality gate and cost metrics (steps 26 and 27).
- Gateway, canary and rollback (step 29), traces and drift alerts (step 30).

## Open items to pick up
- Replace pattern guardrails with a model-based classifier and track block rate.
- Calibrate an LLM judge against 50 human-labelled answers.
- Wire the drift alerts to a real channel and name an on-call owner.

## Checklist for the capstone baseline
- [ ] One modernisation step, done with tests first
- [ ] Security checklist mapped to the OWASP Top 10 for Agentic Applications
- [ ] Vulnerability report
- [ ] Token and cost report (placeholder prices labelled)
