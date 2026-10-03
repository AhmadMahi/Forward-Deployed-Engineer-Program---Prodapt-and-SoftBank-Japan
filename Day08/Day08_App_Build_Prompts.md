# Day 8: App Build Prompts

**App of the day:** Secure Notes API (FastAPI + JWT + MongoDB)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 8. Production-style structure with authentication. This becomes the backend for the React app on Days 11 and 12.

---

## Prompt 1: Build the secure API

```text
You are a senior FastAPI and security mentor. Build a "Secure Notes API".

Stack: Python 3.11, FastAPI, Pydantic v2, PyJWT, PyMongo. Support USE_MOCK=1 to use mongomock
(for Google Colab); otherwise read MONGO_URI. Read SECRET_KEY from the environment.

Structure:
app/main.py, app/config.py (settings from env), app/db.py (client + get_users/get_notes dependencies),
app/security.py (hash_password, verify_password with hashlib.pbkdf2_hmac and a random salt,
create_access_token with exp, current_user and require_role dependencies),
app/routers/auth.py (/register 201 or 409, /token with OAuth2PasswordRequestForm, /me),
app/routers/notes.py (CRUD on notes owned by the current user, 404 for others' notes),
app/routers/admin.py (admin-only list of all notes, 403 for members).

Middleware: request timing header and an X-Request-ID header. CORS for http://localhost:3000.
Return ObjectId as string. Add tags and summaries for /docs.
Give the run command and how to use the Authorize button in Swagger.
```

---

## Prompt 2: Tests for the unhappy paths

```text
Write pytest-free tests (plain asserts, runnable with python tests.py) using TestClient for the
Secure Notes API that check: duplicate registration 409, wrong password 401, missing token 401,
expired token 401 (create one with a negative expiry), other user's note 404, member on admin route 403,
and that dependency_overrides can replace current_user. Use USE_MOCK=1.
```

---

## Prompt 3: Security review

```text
Act as a security reviewer for the Secure Notes API. Check: password storage, token expiry,
secret handling, CORS settings, error messages that leak information, and missing rate limiting.
Give a table of finding, risk (low/medium/high) and fix. Then 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Add refresh tokens with a separate longer expiry.
- Add rate limiting to /token (max 5 attempts per minute per username).
- Log every login attempt to a login_events collection.
