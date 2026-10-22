# Day 5: App Build Prompts

**App of the day:** Quotes and Notes REST API (FastAPI, Pydantic, in memory)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 5. Data is kept in memory (a dict) on purpose; on Day 6 you add a database.

---

## Prompt 1: Build the API

```text
You are a senior backend mentor. Build a REST API with FastAPI called "Notes API".
Requirements:
- Single file main.py, Python 3.12, FastAPI, Pydantic v2, data stored in an in-memory dict.
- Models: NoteCreate (title 1 to 100 chars, content, tags list of str), NoteUpdate (all fields optional),
  Note (adds id and created_at as an ISO string).
- Endpoints on an APIRouter with prefix /notes and tag Notes (plural nouns, no verbs in URLs):
  GET    /notes              list notes, optional query params tag and limit (1 to 50, default 10)
  GET    /notes/{note_id}    one note, 404 if missing
  POST   /notes              create, return 201 and the created note
  PUT    /notes/{note_id}    replace, 404 if missing
  PATCH  /notes/{note_id}    update only provided fields (model_dump(exclude_unset=True))
  DELETE /notes/{note_id}    delete, return 204
  GET    /health             {"status": "ok"}
- Use HTTPException with clear detail messages and response_model on every route.
- Add a short docstring to each endpoint so it appears in /docs.
Also give: the run command, and test_main.py using fastapi.testclient with at least 10 assert based tests,
including 404 and 422 cases.
```

---

## Prompt 2: Make it Colab friendly

```text
Show me how to run and test the Notes API inside Google Colab:
1. Use %%writefile to save main.py.
2. Test with TestClient.
3. Optionally start uvicorn in the background with subprocess and call it with requests.
Explain each step in one sentence.
```

---

## Prompt 3: Generate one endpoint, then review it (NEW v4)

```text
Add GET /notes/search to main.py.
- Query parameter q (2 to 50 chars) matches title or content, case insensitive.
- Returns a list of Note, empty list if nothing matches (status 200).
- Place it above /notes/{note_id} so it matches first.
- Do not change any other endpoint.
- Add three TestClient tests: a match, no match, q too short (422).
Show me the plan first, then the diff.
```

After Codex answers, review the diff with the class checklist: contract, validation, errors, side effects, tests, can you explain it. Write a two-line review note.

---

## Prompt 4: Review against REST rules

```text
Review my Notes API against REST best practices.
For each endpoint, confirm the method, URL, success status code and error codes are correct.
List any problems in a table: endpoint, issue, fix. Do not edit files; only report.
```

---

## SmartDesk step 4: FastAPI ticket API with Pydantic models

```text
SmartDesk step 4. Turn the SmartDesk ticket store into a FastAPI app in app/main.py.
- Models: TicketCreate (title 3 to 120 chars, description, priority low|medium|high, customer_id),
  TicketUpdate (all optional), Ticket (adds id, status open|in_progress|closed, created_at).
- APIRouter prefix /tickets, tag Tickets: GET list (filters status, priority; limit 1 to 50),
  GET one (404), POST (201), PATCH (only sent fields), DELETE (204, 404).
- Keep data in memory for today (MongoDB and SQLite come later).
- tests/test_tickets.py with TestClient covering every status code.
- Update AGENTS.md with the run and test commands.
Show the plan first. Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** every route has the right status code; PATCH uses `exclude_unset=True`; tests fail if you break the code; no secrets in any file; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add a /v1 prefix using APIRouter.
- Return an X-Total-Count header on the list endpoint.
- Add a priority Enum so /docs shows a dropdown.
