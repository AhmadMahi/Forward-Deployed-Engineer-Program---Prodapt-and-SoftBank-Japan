# SmartDesk step 09 (Day 10): React dashboard

**Increment:** React dashboard with the ticket list

**Day folder:** [../../../Day10-React-Basics/](../../../Day10-React-Basics/) (see `Day10_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 08](../step08-day09-express-notifications/) | Next: [step 10](../step10-day11-full-stack-crud/)

## Goal

Show SmartDesk tickets in a React dashboard with components, props, state and events.

## What changed from the previous step

Adds the first front end (Vite + React). Reads the sample tickets for now; it calls the API in step 10.

## Key files

- `src/App.jsx`: state for search, filter and selection
- `src/TicketList.jsx`: list with keys and a badge component
- `src/ticketUtils.js`: pure sort and filter helpers
- `ticketUtils.test.js`: tests

## How to run

```bash
npm install
npm run dev      # http://localhost:5173
```

## How to test

```bash
node --test      # tests the pure helpers, no install needed
```

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
