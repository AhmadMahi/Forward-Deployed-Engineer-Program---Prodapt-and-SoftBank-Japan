# SmartDesk step 08 (Day 9): Express notification service

**Increment:** Express notification service with Postman tests

**Day folder:** [../../../Day09-Nodejs-and-Express/](../../../Day09-Nodejs-and-Express/) (see `Day09_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 07](../step07-day08-js-async-client/) | Next: [step 09](../step09-day10-react-dashboard/)

## Goal

Build a small Node.js and Express service that queues customer notifications, tested in Postman.

## What changed from the previous step

Adds a second service in Node.js. Business logic sits in `notifications.js` so it can be unit tested without Express.

## Key files

- `server.js`: routes, async error handling
- `notifications.js`: validation and store
- `notifications.test.js`: unit tests
- `postman_collection.json`: Postman tests
- `package.json`: scripts including npm audit

## How to run

```bash
npm install          # creates package-lock.json: commit it
npm audit --audit-level=high
npm start
```

## How to test

```bash
node --test           # unit tests, no install needed
# then run postman_collection.json in Postman against the running server
```

## Supply chain hygiene (NEW v4)

- Commit `package-lock.json` so every install gets the same versions.
- Run `npm audit` before each pull request and log findings in your vulnerability report.

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
