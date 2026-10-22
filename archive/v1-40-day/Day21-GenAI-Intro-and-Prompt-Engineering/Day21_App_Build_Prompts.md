# Day 21: App Build Prompts

**App of the day:** Prompt Playground (FastAPI + React) with prompt templates

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 21. A small internal tool to write, test and compare prompts, the starting point for the GenAI weeks.

---

## Prompt 1: Build the API

```text
You are a senior GenAI engineer mentoring beginners. Build a FastAPI "Prompt Playground" back end.
- Reads OPENAI_API_KEY and LLM_MODEL from the environment; if no key, uses a clearly labelled offline stub so the app still runs.
- POST /run: {template, variables, temperature, system} -> fills the template, calls the model, returns output, latency_ms, token estimates.
- POST /compare: runs the same input through two templates and returns both outputs side by side.
- CRUD /templates stored in SQLite with name, description, template text and version number (each edit creates a new version).
- POST /react-demo: a small ReAct loop with two safe tools (price lookup, calculator using ast-based evaluation, not eval).
Include Pydantic models, error handling for API failures and timeouts, and TestClient tests that run in offline mode.
```

---

## Prompt 2: Build the React UI

```text
Build a React (Vite) UI for the Prompt Playground: template editor with {variable} highlighting,
auto-generated inputs for each variable, temperature slider, system prompt box, Run and Compare buttons, results with latency,
and a templates sidebar with version history. Loading, error and empty states. Teal theme.
```

---

## Prompt 3: Prompt review

```text
Here is a prompt I wrote: <paste>. Review it against role, task, context, format, examples and constraints.
Rewrite it, explain each change in one line, and suggest three test inputs including one tricky edge case.
```

---

## Stretch ideas (try on your own)

- Add a token counter that warns when the prompt is near the context limit.
- Add self-consistency: run 5 times and show the majority answer.
- Export a template and its test cases as JSON.
