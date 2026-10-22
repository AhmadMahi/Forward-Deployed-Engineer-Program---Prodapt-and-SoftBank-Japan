# Day 10: App Build Prompts

**App of the day:** Tasks API in Express with an async client and Postman tests

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 10. The same REST ideas from FastAPI, now in Node.js. On Days 11 and 12 a React app will call an API like this one.

---

## Prompt 1: Build the Express API

```text
You are a senior Node.js mentor teaching beginners who already know FastAPI.

Build a "Tasks API" with Node.js 18+ and Express (CommonJS require syntax).
Structure:
  package.json (scripts: "start": "node src/server.js", "dev": "nodemon src/server.js")
  src/server.js       (create app, express.json(), logging middleware, routers, 404 and error handlers)
  src/routes/tasks.js (express.Router)
  src/store.js        (in-memory store with async functions that return promises, to simulate a database)

Task: { id, title (required, 1 to 100 chars), done (boolean), priority ("low" | "medium" | "high"), createdAt }
Endpoints: GET /tasks (filters done, priority; sort=createdAt or priority), GET /tasks/:id,
POST /tasks (400 with a clear message on invalid input, 201 on success), PUT /tasks/:id, PATCH /tasks/:id,
DELETE /tasks/:id (204), GET /tasks/stats.
Use async/await in every route and an error-handling middleware for unexpected errors (500).
Add comments comparing each Express idea to its FastAPI equivalent. Give npm commands to install and run.
```

---

## Prompt 2: Client script and Postman

```text
For the Tasks API:
1. Write client.js using fetch and async/await that creates 5 tasks in parallel with Promise.all,
   updates two, deletes one, prints stats, and shows error handling for a 400 and a 404.
2. Generate a Postman collection v2.1 JSON with one request per endpoint, a {{baseUrl}} variable,
   and pm.test checks for status code and response shape on each request.
3. Explain how to import and run the collection in Postman in 5 short steps.
```

---

## Prompt 3: Explain async in my code

```text
Walk through my Tasks API and client code and explain, for a beginner:
- where the code is asynchronous and why
- what would happen if I forgot await in one route
- the difference between Promise.all and sequential awaits in client.js, with timings
Then 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Persist tasks to a JSON file with fs/promises (readFile, writeFile).
- Add input validation with a small helper or a library such as zod.
- Add a due date and a GET /tasks/overdue endpoint.
