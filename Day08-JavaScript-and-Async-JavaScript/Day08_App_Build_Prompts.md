# Day 8: App Build Prompts

**App of the day:** JavaScript data script for the ticket API (plain JavaScript, Node.js, no libraries)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the script after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 8. The same list, filter and total ideas you used in Python, now in JavaScript, then the async patterns that every front end and Node.js server depends on.

---

## Prompt 1: Ticket data script

```text
You are a patient JavaScript mentor. My learners know Python and FastAPI and learned JavaScript today.
Write a Node.js script ticket_report.js (no libraries, CommonJS) that:
1. Reads tickets from a local tickets.json file with fs.readFileSync and JSON.parse
   (fields: id, title, priority "low" | "medium" | "high", status "open" | "pending" | "closed", ageHours).
2. Prints the count per status and per priority using reduce.
3. Prints the open high-priority tickets, sorted oldest first, as a numbered list.
4. Prints the average age of open tickets, rounded to one decimal.
Use const/let, arrow functions, map, filter, reduce, destructuring and template literals.
Add a one-line comment explaining each JavaScript feature. Also generate a sample tickets.json with 10 tickets.
```

---

## Prompt 2: Callbacks you write yourself

```text
Add a small utils.js module with:
- groupBy(items, keyFn) where keyFn is a callback that returns the group name
- countBy(items, keyFn) built on groupBy
- retryLater(fn, ms) that calls fn after ms milliseconds using setTimeout
Use them in ticket_report.js to group tickets by status and by "old" or "new" (older than 24 hours).
Explain in comments what a callback is and where each callback is called.
```

---

## Prompt 3: The async version

```text
Rewrite the data loading part of ticket_report.js so it is asynchronous:
1. loadTickets() returns a promise (use fs/promises readFile), then an async/await version.
2. Show the same report using .then/.catch, then using async/await with try/catch.
3. Load three files (tickets.json, agents.json, customers.json) sequentially and then with Promise.all,
   printing how long each approach takes with Date.now().
Explain the event loop in three short comments where it matters.
```

---

## Prompt 4: Explain and quiz

```text
Explain to a beginner, using my ticket_report.js:
(1) what happens step by step when an async function awaits a promise,
(2) why setTimeout(fn, 0) runs after the next console.log,
(3) the difference between JSON.parse and JSON.stringify.
Then give 5 quiz questions with answers, including two predict-the-output questions on async ordering.
```

---

## SmartDesk step 7: JavaScript client that reads the API asynchronously

```text
SmartDesk step 7. My SmartDesk FastAPI (from Days 5 to 7) runs on http://127.0.0.1:8000 and has GET /tickets
and GET /tickets/{id}. Write clients/ticket_client.js (Node.js 18+, no libraries) that:
1. Reads BASE_URL from process.env with a default of http://127.0.0.1:8000.
2. Has an async getJSON(path) helper that uses fetch, throws an Error with the status when res.ok is false,
   and gives a friendly message when the server is not running.
3. Loads all tickets, prints counts by priority and status, and the five oldest open tickets.
4. Loads two tickets in parallel with Promise.all.
5. If the API needs a JWT (Day 7), reads it from the SMARTDESK_TOKEN environment variable, never from the code.
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** no tokens or keys in the file; every fetch checks `res.ok`; errors are caught and shown clearly; you can explain every line Codex wrote, including where the code waits.
