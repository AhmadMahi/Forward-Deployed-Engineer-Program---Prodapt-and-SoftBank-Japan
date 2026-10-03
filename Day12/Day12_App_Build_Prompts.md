# Day 12: App Build Prompts

**App of the day:** Full Stack Task Board (React + FastAPI)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 12. First full stack app: a React front end with loading, error and empty states, talking to a FastAPI back end.

---

## Prompt 1: Build the back end

```text
You are a senior full stack mentor. Build the FastAPI back end for a "Task Board".
Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0 with SQLite.
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
reading the base URL from import.meta.env.VITE_API_URL (default http://127.0.0.1:8000).
Handle loading, error (with Retry), empty and data states. Use keys from task ids.
Derive the visible list during render. Make the done toggle optimistic with rollback on failure.
Simple CSS with a teal theme. Give run instructions for both servers.
```

---

## Prompt 3: Single-file version for Colab

```text
Give me a version of the Task Board where FastAPI also serves a single index.html (React 18 UMD + Babel standalone
from unpkg) at "/", and React calls the API on the same origin with relative URLs, so I can run it in Google Colab with
google.colab.output.serve_kernel_port_as_iframe(8000). Keep all behaviour the same.
```

---

## Stretch ideas (try on your own)

- Add drag-free reordering with up and down buttons and a position field.
- Show a progress bar of done vs total tasks.
- Persist the search text in the URL query string.
