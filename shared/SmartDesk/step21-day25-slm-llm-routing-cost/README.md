# SmartDesk step 21 (Day 25): SLM for classification, LLM for complex answers

**Increment:** SLM for classification, LLM for complex answers; cost report

**Day folder:** [../../../Day25-SLMs-and-Token-Optimisation/](../../../Day25-SLMs-and-Token-Optimisation/) (see `Day25_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 20](../step20-day23-patch-and-modernise/) | Next: [step 22](../step22-day26-langgraph-support-assistant/)

## Goal

Cut cost by routing simple work to a small model and escalating only unsure cases, and prove the saving in a cost report.

## What changed from the previous step

Adds an SLM-first router with a confidence threshold and a cost report showing caching, trimming, output limits and routing step by step.

## Key files

- `router.py`: SLM first, LLM on escalation
- `cost_report.py`: cost per 1,000 tickets before and after
- `token_cost.py`: placeholder prices
- `test_router.py`: tests

## How to run

```bash
python cost_report.py
SLM_BACKEND=hf python -c "from router import route; print(route('No signal at home'))"   # Day 25 notebook
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
