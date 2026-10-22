# SmartDesk step 25 (Day 30): Guardrail gateway and red-team suite

**Increment:** Guardrail gateway and red-team suite; vulnerability report v3

**Day folder:** [../../../Day30-LLM-Security-and-Guardrails/](../../../Day30-LLM-Security-and-Guardrails/) (see `Day30_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 24](../step24-day28-mcp-server-sandbox/) | Next: [step 26](../step26-day31-golden-set-eval-dashboard/)

## Goal

Put a guardrail gateway in front of SmartDesk, prove it with a red-team suite, and write vulnerability report v3.

## What changed from the previous step

Adds input and output guardrails (direct and indirect injection, PII, secrets, promises), scoped short-lived approval tokens for the refund tool, a 10-case red-team suite and report v3.

## Key files

- `guardrails.py`: input and output checks
- `gateway.py`: FastAPI gateway, approvals, refund tool
- `redteam_suite.py`: attack cases with expected results
- `vulnerability_report_v3.md`: report v3

## How to run

```bash
uvicorn gateway:app --reload
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
