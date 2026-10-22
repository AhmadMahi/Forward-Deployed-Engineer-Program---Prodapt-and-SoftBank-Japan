# Day 7: App Build Prompts

**App of the day:** Secure Notes API (FastAPI, JWT, MongoDB), plus vulnerability report v1 on your Codex-generated code

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, signing secrets, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 7. Production-style structure with authentication. Today you also scan what Codex wrote and record the findings.

---

## Prompt 1: Build the secure API

```text
You are a senior FastAPI and security mentor. Build a "Secure Notes API".
Stack: Python 3.12, FastAPI, Pydantic v2, PyJWT, bcrypt, PyMongo. Support USE_MOCK=1 to use mongomock
(for Google Colab); otherwise read MONGO_URI. Read SECRET_KEY from the environment (never hard-code it).
Structure:
app/main.py, app/config.py (settings from env), app/db.py (client + get_users/get_notes dependencies),
app/security.py (hash_password and verify_password with bcrypt, create_access_token with a 15 minute exp
and a scope claim, current_user, require_scope and require_role dependencies),
app/routers/auth.py (/register 201 or 409, /token with OAuth2PasswordRequestForm, /me),
app/routers/notes.py (CRUD on notes owned by the current user, 404 for others' notes),
app/routers/admin.py (admin-only list of all notes, 403 for members).
Rules: /register must NOT accept a role from the client. Every notes query filters by owner.
Page size at most 50. Strings have max_length.
Middleware: request timing header and an X-Request-ID header. CORS for http://localhost:5173.
A custom exception handler that returns clean JSON errors without stack traces.
Return ObjectId as string. Add tags and summaries for /docs. Show the plan first.
```

---

## Prompt 2: Tests for the unhappy paths

```text
Write pytest tests using TestClient for the Secure Notes API (USE_MOCK=1) that check:
duplicate registration 409, register with role=admin still creates a member, wrong password 401,
missing token 401, expired token 401 (create one with a negative expiry), read-only token on a write route 403,
other user's note 404, member on admin route 403, limit=1000 gives 422,
and that dependency_overrides can replace current_user.
```

---

## Prompt 3: Validate inputs against NoSQL injection (NEW v4)

```text
Review every endpoint in app/routers for NoSQL injection.
- No endpoint may accept a raw dict or pass request JSON straight into a Mongo query.
- Any user text used in $regex must go through re.escape and have a max length.
- Add tests that send {"$ne": ""} and {"$gt": ""} payloads to /token and to search, expecting 422 or no results.
Report what you changed in a table: file, line, issue, fix. Show the diff.
```

---

## Prompt 4: Security review mapped to OWASP API Top 10 (NEW v4)

```text
Act as a security reviewer for the Secure Notes API. Do not edit files.
For each of OWASP API Security Top 10 (2023) API1 to API5, say whether the app is exposed, where, and the fix.
Also check: password storage, token expiry and scopes, secret handling, CORS, error messages that leak information,
and missing rate limiting on /token. Give a table of finding, OWASP id, risk (low/medium/high) and fix.
```

---

## Prompt 5: Scan and write vulnerability report v1 (NEW v4)

```text
Run these commands and show me the output (do not fix anything yet):
  python -m bandit -r app -f json -o bandit.json
  pip-audit -r requirements.txt
Then create docs/vulnerability_report_v1.md from shared/templates/Vulnerability_Report_Template.md with one row per
finding: ID, finding, tool, severity, affected file, proposed fix, fixed by, verified, evidence.
```

After that, fix at least two findings one at a time ("Fix V-02 only, then re-run bandit"). Update **Fixed by** (human or Codex-assisted), **Verified** and **Evidence** for each.

---

## SmartDesk step 6: JWT login with roles, Mongo analytics, vulnerability report v1

```text
SmartDesk step 6.
1. Add JWT login with roles customer, agent and admin. Tokens expire in 15 minutes and carry scopes
   (tickets:read, tickets:write, analytics:read, admin). Register always creates a customer.
2. Customers see and change only their own tickets; agents see all tickets; admins can manage users.
3. Store tickets in MongoDB (mongomock when USE_MOCK=1) and add GET /analytics/by-priority
   (open tickets per priority, highest first) for agents and admins only.
4. Validate all inputs: typed Pydantic models, max lengths, escaped regex, page size at most 50.
5. Run bandit and pip-audit, and create docs/vulnerability_report_v1.md from the template.
6. Tests for 401, 403, 404 (other owner), 422 (injection payloads) and the analytics result.
Show the plan first. Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** SECRET_KEY comes from the environment; no endpoint accepts a raw dict; every query filters by owner where it should; tokens expire; the report lists every finding with a fix; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add refresh tokens with a separate longer expiry and a revocation list.
- Add rate limiting to /token (max 5 attempts per minute per username).
- Log every login attempt to a login_events collection and add an index on username.
