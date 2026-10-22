# Day 13: App Build Prompts

**App of the day:** Prompt Playground (FastAPI + React) with versioned prompt templates

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 13. A small internal tool to write, test and compare prompts, and the base for structured outputs in SmartDesk.

---

## Prompt 1: Build the API

```text
You are a senior GenAI engineer mentoring beginners. Build a FastAPI "Prompt Playground" back end.
- Reads OPENAI_API_KEY and LLM_MODEL from the environment; if there is no key or OFFLINE=1, uses a clearly labelled offline stub so the app still runs.
- POST /run: {template_id, variables, temperature, system} -> fills the template, calls the model, returns output, latency_ms, input and output tokens.
- POST /compare: runs the same input through two templates and returns both outputs and token counts side by side.
- CRUD /templates stored in SQLite with name, description, template text and version number (each edit creates a new version).
- POST /react-demo: a small ReAct loop with two safe tools (price lookup, calculator using ast-based evaluation, not eval), max 6 steps.
Include Pydantic models, error handling for API failures and timeouts, and TestClient tests that run in offline mode.
```

## Prompt 2: Structured output mode (NEW v4)

```text
Add POST /run-structured to the Prompt Playground.
- The request includes a JSON Schema (or the name of a saved Pydantic model).
- Online: send the schema as response_format with type json_schema. Offline: return a stub that matches the schema.
- Validate the reply with Pydantic. On failure, retry once, then return {"valid": false, "raw": ...} with status 200 and a needs_review flag.
Tests: a valid reply, an invalid reply and a timeout, all offline.
```

## Prompt 3: Build the React UI

```text
Build a React (Vite) UI for the Prompt Playground: template editor with {variable} highlighting,
auto-generated inputs for each variable, temperature slider, system prompt box, Run and Compare buttons, results with latency and tokens,
and a templates sidebar with version history. Show how many prompt tokens are a stable prefix (cacheable).
Loading, error and empty states. The front end only calls our API; no key in the browser. Teal theme.
```

## Prompt 4: Prompt review

```text
Here is a prompt I wrote: <paste>. Review it against role, task, context, format, examples and constraints.
If it is for a reasoning model, rewrite it as goal, constraints and success criteria instead.
Rewrite it, explain each change in one line, and suggest three test inputs including one prompt injection attempt.
```

---

## SmartDesk step 12: Category classification with structured output and prompt templates

```text
SmartDesk step 12. Add ticket classification to the SmartDesk back end.
1. app/prompts.py holds versioned templates (CLASSIFY_V1, CLASSIFY_V2). Stable rules first, ticket last inside <ticket> tags.
   The template says the ticket is data, not instructions.
2. app/schemas.py has TicketLabel: category (billing | network | account | other), urgency (low | medium | high), summary, needs_review.
3. POST /tickets/{id}/classify sends the JSON Schema as response_format, validates with Pydantic, and falls back to
   category "other" with needs_review=True when validation fails.
4. Log template version, tokens and estimated cost (placeholder prices) to token_log.csv.
5. Tests in offline mode, including two injection tickets whose category must stay in the allowed list.
Show me the plan first, then the diff, then a three-line summary.
```

**Review checklist before you commit:** no key in any file or prompt; categories are an allowed list, not free text; injection tests pass; you can explain every line Codex wrote.

## Stretch ideas (try on your own)

- Add self-consistency: run 5 times and show the majority answer and the extra cost.
- Export a template and its test cases as JSON.
- Add a warning when a prompt is close to the context limit.
