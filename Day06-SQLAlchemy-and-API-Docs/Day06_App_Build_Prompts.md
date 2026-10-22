# Day 6: App Build Prompts

**App of the day:** Library Books API (FastAPI, Pydantic, SQLAlchemy, SQLite), then Library API v2 (authors, books, tags and loans)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 6. Prompts 1 and 2 build the Library Books API; Prompts 3 to 5 grow it into Library API v2.

---

## Prompt 1: Build the API with a database

```text
You are a senior FastAPI mentor. Build a "Library Books API".
Stack: Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Mapped / mapped_column style), SQLite.
Project structure:
app/
  main.py          (create app, include routers, create tables on startup)
  database.py      (engine, SessionLocal, Base, get_db dependency that yields a session)
  models.py        (SQLAlchemy Book table: id, title, author, pages, year, created_at)
  schemas.py       (BookCreate, BookUpdate with all optional fields, BookOut with from_attributes)
  routers/books.py (APIRouter prefix /books, tag Books)
Endpoints:
GET /books (query params: author, min_pages, limit 1 to 100 default 20, offset default 0)
GET /books/{id} (404 if missing), POST /books (201), PATCH /books/{id}, DELETE /books/{id} (204)
Rules: validation with Field (pages > 0, year 1450 to 2026, title not empty).
Give the run command and tests with fastapi.testclient covering every endpoint and the error cases.
Show me the plan first.
```

---

## Prompt 2: Explain the request flow

```text
Explain, for a beginner, what happens step by step when a client sends POST /books with a JSON body:
routing, Pydantic validation, the database session, the ORM insert, commit, and the response model.
Do not edit any files.
```

---

## Prompt 3: Add relationships and loans

```text
Extend my Library Books API into "Library API v2". Keep the layered structure.
New models:
- Author (unique name) one-to-many Book
- Tag many-to-many Book via association table book_tags
- Member (name, email unique)
- Loan (member_id, book_id, borrowed_at, returned_at nullable)
Endpoints:
- CRUD for authors; GET /authors/{id} returns the author with their books (404 if missing)
- GET /books returns author name and tag names; support ?tag= and ?author= filters
- POST /loans borrows a book: in ONE transaction, check the book is not already on loan,
  create the Loan, and fail with 409 Conflict if unavailable
- POST /loans/{id}/return sets returned_at
Use selectinload to avoid N+1 queries. Show the plan first, then one file at a time.
```

---

## Prompt 4: Make the docs excellent

```text
Improve the OpenAPI documentation of Library API v2:
- app title, version, description with a short "how to get started"
- openapi_tags with a description for each tag
- summary, docstring and documented error responses (404, 409, 422) on every endpoint
- examples on every Pydantic model using Field(examples=[...])
Then write a script that exports openapi.json and prints all paths with their methods.
Do not change any endpoint behaviour.
```

---

## Prompt 5: Test the transaction

```text
Write tests with fastapi.testclient for Library API v2 that prove:
1. Borrowing an available book returns 201.
2. Borrowing the same book again returns 409 and creates no extra Loan row.
3. Returning then borrowing again works.
Use a fresh SQLite database per test run. Explain each test in one line.
```

---

## SmartDesk step 5: SQLite persistence with relationships and Swagger docs

```text
SmartDesk step 5. Move SmartDesk from in-memory storage to SQLite with SQLAlchemy 2.0.
- Models: Customer (name, email unique) one-to-many Ticket; Ticket one-to-many Comment (body, author, created_at).
- app/database.py with get_db dependency; keep the existing /tickets endpoints and status codes unchanged.
- New: GET /customers/{id}/tickets, POST /tickets/{id}/comments (201, 404).
- POST /tickets/{id}/close sets status closed AND adds a closing comment in ONE transaction; roll back on any error.
- Swagger: app title, version, description, tags with descriptions, summary and 404 responses on every route.
- Tests: existing tests still pass; new tests for comments, close and a forced rollback.
Show the plan first. Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** the foreign key is on the many side; the close flow commits once; tests still pass; /docs reads well to someone new; no secrets in any file; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add an overdue report endpoint listing loans older than 14 days.
- Add pagination to GET /books with limit and offset, and an X-Total-Count header.
- Add cascade="all, delete-orphan" to Ticket.comments and prove it works with a test.
