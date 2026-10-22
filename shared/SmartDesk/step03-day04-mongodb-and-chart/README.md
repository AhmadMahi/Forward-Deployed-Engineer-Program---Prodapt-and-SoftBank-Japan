# SmartDesk step 03 (Day 4): Tickets in MongoDB with a chart

**Increment:** Tickets in MongoDB; chart by priority

**Day folder:** [../../../Day04-Architecture-and-MongoDB/](../../../Day04-Architecture-and-MongoDB/) (see `Day04_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 02](../step02-day03-oop-classes-and-search/) | Next: [step 04](../step04-day05-fastapi-ticket-api/)

## Goal

Move tickets into a MongoDB collection, query them, and chart tickets by priority.

## What changed from the previous step

Replaces the JSON file with a MongoDB collection (mongomock offline), adds indexes, an aggregation and a Matplotlib chart.

## Key files

- `repo_mongo.py`: collection, indexes, CRUD, aggregation and chart
- `test_repo_mongo.py`: tests with mongomock

## How to run

```bash
python repo_mongo.py              # mongomock
MONGO_URI=mongodb+srv://... python repo_mongo.py   # real cluster (URI from .env, never committed)
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
