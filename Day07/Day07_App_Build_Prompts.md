# Day 7: App Build Prompts

**App of the day:** Library API v2: authors, books, tags and loans

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 7. Builds on the Day 6 Library Books API: add relationships, a transactional loan flow and professional docs.

---

## Prompt 1: Add relationships and loans

```text
You are a senior FastAPI mentor. Extend my Library Books API (FastAPI, Pydantic v2,
SQLAlchemy 2.0, SQLite) into "Library API v2".

New models:
- Author (unique name) one-to-many Book
- Tag many-to-many Book via association table book_tags
- Member (name, email unique)
- Loan (member_id, book_id, borrowed_at, returned_at nullable)

Endpoints:
- CRUD for authors and tags, attach/detach tags on a book: POST/DELETE /books/{id}/tags/{tag_id}
- GET /books returns author name and tag names; support ?tag= and ?author= filters
- POST /loans borrows a book: in ONE transaction, check the book is not already on loan,
  create the Loan, and fail with 409 Conflict if unavailable
- POST /loans/{id}/return sets returned_at
Use selectinload to avoid N+1 queries. Keep the layered structure (routers, schemas, models, database).
```

---

## Prompt 2: Make the docs excellent

```text
Improve the OpenAPI documentation of Library API v2:
- app title, version, description with a short "how to get started"
- openapi_tags with a description for each tag
- summary, description and documented error responses (404, 409, 422) on every endpoint
- examples on every Pydantic model using Field(examples=[...]) or json_schema_extra
Then write a script that exports openapi.json and prints all paths with their methods.
```

---

## Prompt 3: Test the transaction

```text
Write tests with fastapi.testclient for Library API v2 that prove:
1. Borrowing an available book returns 201.
2. Borrowing the same book again returns 409 and creates no extra Loan row.
3. Returning then borrowing again works.
Use a fresh SQLite database per test run. Explain each test in one line.
```

---

## Stretch ideas (try on your own)

- Add an overdue report endpoint listing loans older than 14 days.
- Add pagination to GET /books with limit and offset.
- Generate a TypeScript client from openapi.json with openapi-generator (research task).
