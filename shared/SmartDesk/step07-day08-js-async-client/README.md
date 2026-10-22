# SmartDesk step 07 (Day 8): JavaScript async client

**Increment:** JavaScript client that reads the API asynchronously

**Day folder:** [../../../Day08-JavaScript-and-Async-JavaScript/](../../../Day08-JavaScript-and-Async-JavaScript/) (see `Day08_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 06](../step06-day07-jwt-roles-analytics/) | Next: [step 08](../step08-day09-express-notifications/)

## Goal

Read the SmartDesk API from JavaScript using fetch, async and await, with error handling and retries.

## What changed from the previous step

Adds a Node.js client next to the Python API. No libraries: built-in `fetch` and `node:test`.

## Key files

- `client.js`: fetchTickets, summarise and fetchWithRetry
- `client.test.js`: tests with a fake fetch

## How to run

```bash
# start the step 04 API first, then:
API_URL=http://127.0.0.1:8000 node client.js
```

## How to test

```bash
node --test
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
