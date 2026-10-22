# SmartDesk step 11 (Day 12): Ticket summary with token logging

**Increment:** First LLM call: ticket summary with token logging

**Day folder:** [../../../Day12-GenAI-Intro-LLMs-and-Tokens/](../../../Day12-GenAI-Intro-LLMs-and-Tokens/) (see `Day12_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 10](../step10-day11-full-stack-crud/) | Next: [step 12](../step12-day13-structured-classification/)

## Goal

Make the first LLM call: summarise a ticket through our own API and log tokens and estimated cost.

## What changed from the previous step

Adds `llm_client.py` (online or offline), `token_cost.py` (placeholder prices) and a summarise endpoint with a CSV token log.

## Key files

- `llm_client.py`: one place for every LLM call; offline stand-in
- `token_cost.py`: placeholder prices and cost()
- `app.py`: POST /summarise, GET /usage/today
- `test_app.py`: tests

## How to run

```bash
export OPENAI_API_KEY=...   # from .env; or skip it for offline demo mode
uvicorn app:app --reload
```

## How to test

```bash
python -m pytest -q        # always offline
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
