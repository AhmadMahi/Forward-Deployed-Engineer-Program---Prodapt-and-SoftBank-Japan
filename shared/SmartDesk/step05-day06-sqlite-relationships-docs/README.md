# SmartDesk step 05 (Day 6): SQLite persistence and Swagger docs

**Increment:** SQLite persistence with relationships; Swagger docs

**Day folder:** [../../../Day06-SQLAlchemy-and-API-Docs/](../../../Day06-SQLAlchemy-and-API-Docs/) (see `Day06_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 04](../step04-day05-fastapi-ticket-api/) | Next: [step 06](../step06-day07-jwt-roles-analytics/)

## Goal

Persist tickets with SQLAlchemy 2.0, model relationships, use transactions safely, and publish clear API docs.

## What changed from the previous step

Replaces the in-memory dict from step 04 with SQLite. Adds Customer and Comment models, a join report, a rollback example and documented tags and examples in Swagger.

## Key files

- `app/db.py`: engine and session
- `app/models.py`: one-to-many relationships
- `app/main.py`: routes, joins, transaction with rollback, Swagger metadata
- `tests/`: tests on an in-memory database

## How to run

```bash
uvicorn app.main:app --reload
# Swagger UI: http://127.0.0.1:8000/docs
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
