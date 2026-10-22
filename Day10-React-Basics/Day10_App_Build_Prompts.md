# Day 10: App Build Prompts

**App of the day:** Personal Dashboard (React components, props, state and events)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the app after every step and click through every state. Do not move to the next prompt until it works.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.
6. Codex is not allowed during the Basics assessment. Use these prompts after it.

> Uses React basics only: components, props, children, useState and events. No data fetching yet; that comes on Day 11.

---

## Prompt 1: Plan the dashboard

```text
You are a patient React mentor. My learners know Python, FastAPI and JavaScript, and today learned
React components, JSX, props, children, useState and events. Do NOT use useEffect, routing, context or libraries.

I want a "Personal Dashboard" with Vite + React (JavaScript, not TypeScript).
Before writing any code, give me a plan: the component tree, the props of each component,
which component owns which state, and the files you will create. Wait for my approval.
```

## Prompt 2: Build it in small steps

```text
Build the approved plan one component at a time, starting with Layout and Panel:
- Layout (header with the user's name, children area)
- Panel (title prop, children)
- Greeting (Good morning/afternoon/evening based on the hour)
- Counter widget "Glasses of water today" with +/- and limits 0 to 12
- QuickNotes: a controlled textarea with a character count and a Clear button
- MoodPicker: 4 buttons (Great, Good, Okay, Tired); the selected one is highlighted
- FocusTimer: start/stop buttons with a count of completed sessions (no real timer needed)
Each component in its own file under src/components, App.jsx composing them, and a small CSS file with a teal theme.
Comment each concept used (props, state, event). After each component, stop so I can run and review it.
```

## Prompt 3: Run it inside a notebook

```text
Convert the Personal Dashboard into a single HTML page that uses React 18.3.1 UMD, ReactDOM and Babel standalone
from unpkg (exact versions), with all components in one <script type="text/babel"> block, so I can render it in
Google Colab with IPython.display inside an iframe srcdoc. Keep every component and behaviour the same.
```

## Prompt 4: Explain and quiz

```text
Explain to a beginner how data flows in the Personal Dashboard: which values are props, which are state,
and what happens step by step when the user clicks "+" on the water counter. Then give 5 quiz questions with answers.
```

---

## SmartDesk step 9: React dashboard with the ticket list

```text
SmartDesk step 9. In the SmartDesk repo, create a Vite + React (JavaScript) front end in web/.
First give me a plan (component tree, props, state). Then build, one component per step:
- App owns the state: tickets (start with 8 sample telecom tickets: id, title, priority, status, customer) and filter.
- Header {agentName, openCount}, FilterBar {filter, onChange} with All / Open / Closed,
  TicketList {tickets} that shows "No tickets match" when empty, TicketCard {id, title, priority, status}
  with a coloured border for high priority.
- Keys come from ticket.id. State is never mutated. No dangerouslySetInnerHTML. No API keys or tokens anywhere.
- No data fetching yet (Day 11 adds it).
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** keys come from the data; no state is mutated in place; no secrets in front-end code; no raw HTML; every component has one job; you can explain every line Codex wrote. Write a two-line review note for your submission.
