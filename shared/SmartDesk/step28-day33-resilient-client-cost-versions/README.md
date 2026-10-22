# SmartDesk step 28 (Day 33): Resilient LLM client with cost and version tracking

**Increment:** Resilient LLM client; cost and version dashboard

**Day folder:** [../../../Day33-LLMOps/](../../../Day33-LLMOps/) (see `Day33_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 27](../step27-day32-ci-quality-gate/) | Next: [step 29](../step29-day34-production-gateway-canary/)

## Goal

Keep SmartDesk working when the provider is slow or down, and track cost and versions per release.

## What changed from the previous step

Adds retries with backoff, model fallback and a circuit breaker; an AgentOps registry for model, prompt, tools, skill and MCP server versions; cost by version; and a deprecation runbook.

## Key files

- `resilient_client.py`: retries, fallback, circuit breaker
- `registry.py`: release versions, retired models, cost by version
- `DEPRECATION_RUNBOOK.md`: what to do when a model retires
- `test_resilience.py`: failure simulations

## How to run

```bash
python -c "from registry import *; print(check_release(RELEASES['2026.12.1']))"
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
