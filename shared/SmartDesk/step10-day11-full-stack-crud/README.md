# SmartDesk step 10 (Day 11): Full-stack create, update and close

**Increment:** Full-stack create, update and close tickets

**Day folder:** [../../../Day11-React-UI-Logic-and-Full-Stack/](../../../Day11-React-UI-Logic-and-Full-Stack/) (see `Day11_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 09](../step09-day10-react-dashboard/) | Next: [step 11](../step11-day12-llm-summary-token-log/)

## Goal

Connect the React dashboard to FastAPI so agents can create, update and close tickets.

## What changed from the previous step

Adds a real API client in React with loading, error and empty states, plus PATCH and close endpoints with CORS.

## Key files

- `backend/main.py`: CRUD, close, CORS
- `frontend/src/api.js`: fetch wrapper, no keys
- `frontend/src/TicketBoard.jsx`: loading, error, empty and data states
- `tests/test_backend.py`: API and no-key tests

## How to run

```bash
uvicorn backend.main:app --reload --port 8000
cd frontend && npm create vite@latest . -- --template react && npm run dev   # copy src/ files in
```

## How to test

```bash
python -m pytest -q
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
