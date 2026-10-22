# SmartDesk step 26 (Day 31): Golden set and evaluation dashboard

**Increment:** Golden set and evaluation dashboard

**Day folder:** [../../../Day31-GenAI-System-Evaluation/](../../../Day31-GenAI-System-Evaluation/) (see `Day31_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 25](../step25-day30-guardrail-gateway-redteam/) | Next: [step 27](../step27-day32-ci-quality-gate/)

## Goal

Measure SmartDesk answers on a fixed golden set, slice the results by category and look at failures.

## What changed from the previous step

Adds a 12-question golden set, retrieval, citation, fact, faithfulness and relevance metrics, a pass^k check for agent trajectories and a Markdown dashboard.

## Key files

- `golden_set.jsonl`: questions, expected source and must-include facts
- `evaluate.py`: metrics, slices, pass^k, dashboard
- `rag.py`: copied from step 16 (the system under test)
- `test_evaluate.py`: tests

## How to run

```bash
python evaluate.py       # writes eval_dashboard.md
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
