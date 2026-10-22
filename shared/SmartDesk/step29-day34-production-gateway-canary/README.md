# SmartDesk step 29 (Day 34): Production gateway with streaming and canary

**Increment:** Production gateway with streaming and canary on Azure

**Day folder:** [../../../Day34-LLM-Deployment-and-Lifecycle/](../../../Day34-LLM-Deployment-and-Lifecycle/) (see `Day34_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 28](../step28-day33-resilient-client-cost-versions/) | Next: [step 30](../step30-day35-observability-drift-handoff/)

## Goal

Serve SmartDesk through a production gateway that streams answers, releases new versions to a small canary group and rolls back in one call.

## What changed from the previous step

Adds an async streaming endpoint, sticky canary routing by user, a protected rollback switch, Container Apps settings with Key Vault references and rollback test notes.

## Key files

- `gateway.py`: streaming, canary, rollback
- `azure-container-app.yaml`: deployment settings
- `ROLLBACK_TEST_NOTES.md`: rollback test
- `test_gateway.py`: tests

## How to run

```bash
ADMIN_TOKEN=<from Key Vault> uvicorn gateway:app
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
