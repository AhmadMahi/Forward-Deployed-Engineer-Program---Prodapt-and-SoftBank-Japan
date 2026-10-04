# Day 26: App Build Prompts

**App of the day:** Agentic HR and Ops Assistant (CRAG + supervisor agents)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 26. Combines corrective RAG over policies with specialist agents for data and drafting, with guardrails.

---

## Prompt 1: Corrective RAG service

```text
You are a senior GenAI engineer. Build a corrective RAG service with LangGraph over a folder of policy documents:
retrieve (hybrid search from Day 23) -> grade each chunk with a small model (yes/no + reason) -> decide (generate | rewrite query, max 2 | fallback search
over an approved external FAQ) -> generate with citations -> self-check that every sentence is supported (else revise once).
State includes the path for debugging. Offline stand-ins for model calls so tests run without a key. Include tests for each routing decision.
```

---

## Prompt 2: Supervisor with specialists

```text
Add a supervisor LangGraph with specialists: researcher (the CRAG service), analyst (runs pandas on approved CSVs only),
writer (drafts for a chosen audience), checker (verifies numbers and citations). The supervisor routes based on what is missing in state, with a max of 8 hops.
Each specialist has only the tools it needs. Log every hop with latency and tokens.
```

---

## Prompt 3: Agents SDK version and comparison

```text
Rebuild the same assistant with the OpenAI Agents SDK: a triage agent with handoffs to Policy, Data and Writer agents,
function tools, an input guardrail that blocks requests for personal data of other employees, and tracing.
Then compare the LangGraph and Agents SDK versions in a short table: control, debugging, testing, flexibility.
```

---

## Stretch ideas (try on your own)

- Add long-term memory of user preferences (language, detail level).
- Add a cost cap per request.
- Evaluate the assistant on 10 tasks: success, steps and cost.
