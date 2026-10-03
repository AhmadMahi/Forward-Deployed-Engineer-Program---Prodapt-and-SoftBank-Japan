# Day 11: App Build Prompts

**App of the day:** Personal Dashboard (React components, props, state and events)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses React basics only: components, props, children, useState and events. No data fetching yet; that comes on Day 12.

---

## Prompt 1: Build the dashboard

```text
You are a patient React mentor. My learners know Python, FastAPI and JavaScript basics, and today learned
React components, JSX, props, children, useState and events. Do NOT use useEffect, routing, context or libraries.

Build a "Personal Dashboard" with Vite + React (JavaScript, not TypeScript).
Components:
- Layout (header with the user's name, children area)
- Panel (title prop, children)
- Greeting (shows Good morning/afternoon/evening based on the hour)
- Counter widget "Glasses of water today" with +/- and limits 0 to 12
- QuickNotes: a controlled textarea with a character count and a Clear button
- MoodPicker: 4 emoji-free buttons (Great, Good, Okay, Tired); the selected one is highlighted
- FocusTimer: a simple start/stop with a count of completed sessions (no real timer needed; use buttons)

Give: the commands to create and run the project, each component in its own file under src/components,
App.jsx composing them, and a small CSS file with a teal theme. Comment each concept used (props, state, event).
```

---

## Prompt 2: Run it inside a notebook

```text
Convert the Personal Dashboard into a single HTML page that uses React 18 UMD, ReactDOM and Babel standalone
from unpkg, with all components in one <script type="text/babel"> block, so I can render it in Google Colab
with IPython.display inside an iframe srcdoc. Keep every component and behaviour the same.
```

---

## Prompt 3: Explain and quiz

```text
Explain to a beginner how data flows in the Personal Dashboard: which values are props, which are state,
and what happens step by step when the user clicks "+" on the water counter. Then give 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Lift the mood state up to App and show it in the header.
- Add a dark mode toggle using a state value and a CSS class.
- Add a simple to-do list using an array in state (copy, do not mutate).
