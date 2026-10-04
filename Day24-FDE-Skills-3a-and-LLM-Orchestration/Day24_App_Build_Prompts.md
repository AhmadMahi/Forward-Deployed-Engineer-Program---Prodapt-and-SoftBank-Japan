# Day 24: App Build Prompts

**App of the day:** Meeting Notes Assistant (LangChain chains + FastAPI)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 24. Practical for FDE work: turn messy meeting notes into a summary per audience, action items and decisions.

---

## Prompt 1: Build the chains

```text
You are a senior GenAI engineer. Using LangChain (langchain-core + langchain-openai) build a "Meeting Notes Assistant":
- summary chain: notes + audience (sponsor, engineer, end user) -> 3 bullets for that audience
- actions chain: with_structured_output into a Pydantic list of ActionItem(owner, task, due_date or null)
- decisions chain: list of Decision(decision, rationale, door_type: one_way|two_way)
- a router that detects whether input is meeting notes, an email, or a question, and sends it to the right chain
Provide an offline fallback model (RunnableLambda) so tests run without an API key.
```

---

## Prompt 2: Wrap it in an API

```text
Expose the chains with FastAPI: POST /summarise, POST /actions, POST /decisions, POST /process (runs all three in parallel
with RunnableParallel). Validate outputs with Pydantic, return 502 with a clear message if the model output fails validation twice.
Add TestClient tests using the offline model.
```

---

## Prompt 3: Codex-ready repository

```text
Write an AGENTS.md for this repository and three task briefs suitable for an AI coding agent:
(1) add a Markdown export of the processed notes, (2) add tests for the router, (3) add retry with exponential backoff on model calls.
Each brief: goal, files to touch, acceptance criteria, tests, out of scope.
```

---

## Stretch ideas (try on your own)

- Stream the summary token by token to a React page.
- Add a negotiation-prep chain that drafts interests, options and BATNA from a scenario.
- Log every chain run with latency and input size.
