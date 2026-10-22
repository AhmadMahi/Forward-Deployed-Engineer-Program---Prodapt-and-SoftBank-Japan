# Day 9: App Build Prompts

**App of the day:** Tasks API in Express with an async client and Postman tests

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.
6. **NEW (v4):** before installing any package Codex suggests, check the name, the need and that it is maintained. Commit `package-lock.json`.

> Uses Days 1 to 9. The same REST ideas from FastAPI, now in Node.js. On Days 10 and 11 a React app will call an API like this one.

---

## Prompt 1: Build the Express API

```text
You are a senior Node.js mentor teaching beginners who already know FastAPI.

Build a "Tasks API" with Node.js 20+ and Express 5 (CommonJS require syntax).
Structure:
  package.json (scripts: "start": "node src/server.js", "dev": "nodemon src/server.js", "test": "node tests/api_test.js")
  src/app.js          (create app, express.json(), logging middleware, routers, 404 and error handlers; export app)
  src/server.js       (listen on process.env.PORT or 3000)
  src/routes/tasks.js (express.Router)
  src/controllers/tasks.js (handler functions)
  src/store.js        (in-memory store with async functions that return promises, to simulate a database)

Task: { id, title (required, 1 to 100 chars), done (boolean), priority ("low" | "medium" | "high"), createdAt }
Endpoints: GET /tasks (filters done, priority; sort=createdAt or priority), GET /tasks/stats, GET /tasks/:id,
POST /tasks (400 with a clear message on invalid input, 201 on success), PUT /tasks/:id, PATCH /tasks/:id,
DELETE /tasks/:id (204).
Use async/await in every route and one error-handling middleware for unexpected errors (500).
Add comments comparing each Express idea to its FastAPI equivalent. Give npm commands to install and run.
Do not add any packages other than express and nodemon.
```

---

## Prompt 2: Tests, client script and Postman

```text
For the Tasks API:
1. Write tests/api_test.js that starts the app on port 0, calls every endpoint with fetch, checks status codes
   (201, 400, 200, 404, 204, 500 from a simulated store failure) and prints PASS or FAIL per check.
2. Write client.js using fetch and async/await that creates 5 tasks in parallel with Promise.all,
   updates two, deletes one, prints stats, and shows error handling for a 400 and a 404.
3. Generate a Postman collection v2.1 JSON with one request per endpoint, a {{baseUrl}} variable,
   and pm.test checks for status code and response shape on each request.
4. Explain how to import and run the collection in Postman in 5 short steps.
```

---

## Prompt 3: NEW (v4) Supply chain check

```text
Review the dependencies of this project as a security-minded reviewer:
1. Explain each entry in package.json and the difference between "^5.1.0", "~5.1.0" and "5.1.0".
2. Explain what package-lock.json records and why it must be committed.
3. Add a .gitignore with node_modules and .env.
4. Add an npm script "audit" that runs npm audit --audit-level=high.
5. Write audit_report.js that reads `npm audit --json` output and prints one row per finding in this format:
   ID | tool | severity | affected package | finding | proposed fix, and exits with code 1 on high or critical.
Do not run npm audit fix automatically. Tell me how to review and test a fix before accepting it.
```

---

## Prompt 4: Explain async errors in my code

```text
Walk through my Tasks API and explain, for a beginner:
- what happens in Express 5 when an async route throws or a promise rejects
- what would happen in Express 4 without a wrapper, and show the wrapper
- what would happen if I forgot await in one controller
Then 5 quiz questions with answers.
```

---

## SmartDesk step 8: Express notification service with Postman tests

```text
SmartDesk step 8. Create a separate service folder notify-service/ (Node.js 20+, Express 5, CommonJS).
- POST /notifications {ticketId (integer), channel ("email" | "sms" | "push"), message (1 to 300 chars)}
  validates input (400 with a list of errors), records the notification and returns 201. Sending is simulated:
  log the message, do not call any real provider. Any provider key would come from process.env, never from code.
- GET /notifications?ticketId=101 lists notifications, GET /health returns {status: "ok"}.
- notify_app.js exports the app; server.js listens on PORT or 4000.
- tests/notify_test.js starts the app on port 0 and checks 201, 400 and the list endpoint.
- A Postman collection with tests for every request, using {{baseUrl}}.
- package-lock.json committed, npm audit run, findings logged in the vulnerability report template.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** only the packages you expected are in `package.json`; `package-lock.json` is committed and `node_modules` is not; every route returns the right status code; you can explain every line Codex wrote.
