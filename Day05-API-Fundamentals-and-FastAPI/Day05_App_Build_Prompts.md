# Day 5: App Build Prompts

**App of the day:** Quotes and Notes REST API (FastAPI, in memory)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 5. Data is kept in memory (a dict) on purpose; tomorrow you add Pydantic models and a database.

---

## Prompt 1: Build the API

```text
You are a senior backend mentor. Build a REST API with FastAPI called "Notes API".

Requirements:
- Single file main.py, Python 3.11, FastAPI, data stored in an in-memory dict.
- A note has: id (int), title (str), content (str), tags (list of str), created_at (ISO string).
- Endpoints (follow REST naming, plural nouns, no verbs in URLs):
  GET    /notes              list all notes, optional query param tag to filter
  GET    /notes/{note_id}    one note, 404 if missing
  POST   /notes              create, return 201 and the created note
  PUT    /notes/{note_id}    replace, 404 if missing
  PATCH  /notes/{note_id}    update only provided fields
  DELETE /notes/{note_id}    delete, return 204
  GET    /health             {"status": "ok"}
- Use HTTPException with clear detail messages.
- Accept the request body as a plain dict for now (we learn Pydantic tomorrow).
- Add a short docstring to each endpoint so it appears in /docs.

Also give: the command to run it, and a test file test_main.py using fastapi.testclient
with at least 8 assert based tests (run with: python test_main.py).
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

## Prompt 3: Review against REST rules

```text
Review my Notes API against REST best practices.
For each endpoint, confirm the method, URL, success status code and error codes are correct.
List any problems in a table: endpoint, issue, fix.
Finish with 5 quiz questions about HTTP methods and status codes, with answers.
```

---

## Stretch ideas (try on your own)

- Add GET /notes/search?q=word that searches title and content.
- Add a /v1 prefix using APIRouter.
- Return an X-Total-Count header on the list endpoint.
