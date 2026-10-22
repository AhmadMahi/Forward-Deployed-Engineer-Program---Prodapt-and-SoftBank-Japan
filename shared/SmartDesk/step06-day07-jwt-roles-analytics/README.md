# SmartDesk step 06 (Day 7): JWT login with roles and Mongo analytics

**Increment:** JWT login with roles; Mongo analytics endpoint; vulnerability report v1

**Day folder:** [../../../Day07-FastAPI-Advanced-Security-and-MongoDB/](../../../Day07-FastAPI-Advanced-Security-and-MongoDB/) (see `Day07_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 05](../step05-day06-sqlite-relationships-docs/) | Next: [step 07](../step07-day08-js-async-client/)

## Goal

Secure the API with short-lived JWTs and role scopes, add a Mongo analytics endpoint, and write vulnerability report v1.

## What changed from the previous step

Adds login, password hashing, scopes per role (agent, lead), input validation against NoSQL injection, pagination, an aggregation endpoint and `vulnerability_report_v1.md`.

## Key files

- `app/security.py`: hashing and JWTs
- `app/main.py`: login, scopes, safe queries, analytics
- `tests/test_auth.py`: valid, expired, missing token and injection tests
- `vulnerability_report_v1.md`: report v1

## How to run

```bash
export JWT_SECRET=<from your .env, never committed>
uvicorn app.main:app --reload
bandit -r app
pip-audit -r requirements.txt
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
