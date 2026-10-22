# Day 11: App Build Prompts

**App of the day:** Full Stack Task Board (React + FastAPI)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests and click through every screen state after each step. Do not move on until it works.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.
6. **NEW (v4):** never accept front-end code that contains a provider key or calls an LLM API directly. Keys stay on the server.

> Uses Days 1 to 11. First full stack app: a React front end with loading, error and empty states, talking to a FastAPI back end.

---

## Prompt 1: Build the back end

```text
You are a senior full stack mentor. Build the FastAPI back end for a "Task Board".
Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 with SQLite.
Task: id, title (1 to 100 chars), done (bool), priority (low|medium|high), created_at.
Endpoints under /api: GET /tasks (filters done, priority, q for title search), POST /tasks (201),
PATCH /tasks/{id}, DELETE /tasks/{id} (204), DELETE /tasks?done=true (clear completed, returns count).
Enable CORS for http://localhost:5173. Include TestClient tests for every endpoint.
```

---

## Prompt 2: Build the React front end

```text
Build the React front end for the Task Board with Vite (JavaScript).
Components: App, TaskForm (controlled input + priority select, disabled while saving),
Filters (search box, "hide done" checkbox, priority dropdown), TaskList, TaskItem (checkbox, title, priority badge, delete).
Data: a small api.js with async functions getTasks, createTask, updateTask, deleteTask, clearDone using fetch,
reading only the API base URL from import.meta.env.VITE_API_URL (default http://127.0.0.1:8000).
No secrets of any kind in the front end.
Handle loading, error (with Retry), empty and data states. Use keys from task ids.
Derive the visible list during render. Make the done toggle optimistic with rollback on failure.
Simple CSS with a teal theme. Give run instructions for both servers.
```

---

## Prompt 3: NEW (v4) Keep keys off the front end

```text
Review my React project for secrets:
1. List every environment variable the front end reads and say whether it is safe to be public.
2. Explain what Vite does with VITE_ variables at build time.
3. Write scripts/scan_dist.py that searches dist/ after npm run build for key prefixes, "Bearer " tokens
   and VITE_ names ending in KEY, SECRET or TOKEN, prints file:line for each hit, and exits 1 if any are found.
4. If any feature needs a provider key, move that call into a FastAPI endpoint that reads the key from the
   server environment and returns only the result. Show the new endpoint and the new front-end call.
```

---

## Prompt 4: Single-file version for Colab

```text
Give me a version of the Task Board where FastAPI also serves a single index.html (React 18.3.1 UMD + Babel standalone
from unpkg, exact versions) at "/", and React calls the API on the same origin with relative URLs, so I can run it in
Google Colab with google.colab.output.serve_kernel_port_as_iframe(8000). Keep all behaviour the same.
```

---

## SmartDesk step 10: Full-stack create, update and close tickets

```text
SmartDesk step 10. Connect the SmartDesk React dashboard (web/, from step 9) to the SmartDesk FastAPI.
Back end: make sure these exist with Pydantic validation and tests:
  GET /api/tickets, POST /api/tickets (201), PATCH /api/tickets/{id} (title, priority, status:
  "open" | "pending" | "closed"; 404 for unknown ids, 422 for bad values). CORS for http://localhost:5173.
  If the API uses JWT (step 6), the React app sends the user's token in the Authorization header; the token is
  kept in memory, never hard-coded.
Front end: web/src/api.js with getTickets, createTicket, updateTicket; App loads tickets on mount with loading,
error (Retry) and empty states; a create form; a priority dropdown and a Close button per ticket that PATCH the API
and update the list from the reply; a "Hide closed" checkbox.
After npm run build, run scripts/scan_dist.py and confirm no secrets are in dist/.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** no provider keys or tokens in front-end code or `.env` files that start with `VITE_`; every fetch checks `res.ok`; every screen has loading, error, empty and data states; keys in lists come from ids; you can explain every line Codex wrote.
