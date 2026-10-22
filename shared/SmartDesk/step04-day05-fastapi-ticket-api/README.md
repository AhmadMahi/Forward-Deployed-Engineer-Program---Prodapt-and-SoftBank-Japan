# SmartDesk step 04 (Day 5): FastAPI ticket API

**Increment:** FastAPI ticket API with Pydantic models

**Day folder:** [../../../Day05-API-Fundamentals-and-FastAPI-Core/](../../../Day05-API-Fundamentals-and-FastAPI-Core/) (see `Day05_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 03](../step03-day04-mongodb-and-chart/) | Next: [step 05](../step05-day06-sqlite-relationships-docs/)

## Goal

Expose SmartDesk tickets through a REST API with validated Pydantic request and response models.

## What changed from the previous step

Moves from a CLI to a FastAPI service. Storage is an in-memory dict for now (SQLite arrives in step 05).

## Key files

- `app/main.py`: routes, Pydantic models, status codes
- `tests/test_api.py`: TestClient tests
- `requirements.txt`: pinned versions (example pins; update with pip-audit)

## How to run

```bash
uvicorn app.main:app --reload
# open http://127.0.0.1:8000/docs
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
