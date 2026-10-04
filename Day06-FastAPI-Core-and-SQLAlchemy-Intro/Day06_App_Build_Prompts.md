# Day 6: App Build Prompts

**App of the day:** Library Books API (FastAPI + Pydantic + SQLAlchemy + SQLite)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 6. You will extend this same API with relationships and better docs on Day 7.

---

## Prompt 1: Build the API with a database

```text
You are a senior FastAPI mentor. Build a "Library Books API".

Stack: Python 3.11, FastAPI, Pydantic v2, SQLAlchemy 2.0 (Mapped / mapped_column style), SQLite.

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
Add docstrings so /docs is clear. Give the run command and a tests file with
fastapi.testclient covering every endpoint and the error cases.
```

---

## Prompt 2: Make it run in Colab

```text
Show how to run the Library Books API in Google Colab:
write each file with %%writefile (create the folders first), then test it with TestClient.
Keep explanations to one line per step.
```

---

## Prompt 3: Explain the request flow

```text
Explain, for a beginner, what happens step by step when a client sends
POST /books with a JSON body: routing, Pydantic validation, the database session,
the ORM insert, commit, and the response model. Then list 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Add a genre Enum and filter by genre.
- Add a search endpoint that matches part of the title (case insensitive).
- Return the total count in an X-Total-Count header.
