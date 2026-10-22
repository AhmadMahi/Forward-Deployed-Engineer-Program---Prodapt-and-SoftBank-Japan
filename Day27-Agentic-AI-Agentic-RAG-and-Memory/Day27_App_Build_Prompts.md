# Day 27: App Build Prompts

**App of the day:** Agentic HR and Ops Assistant (CRAG + supervisor agents + persistent memory)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 27. Combines corrective RAG over policies with specialist agents for data and drafting, with guardrails and a safe long-term memory.

---

## Prompt 1: Corrective RAG service

```text
You are a senior GenAI engineer. Build a corrective RAG service with LangGraph over a folder of policy documents:
retrieve (hybrid search from Day 22) -> grade each chunk with a light model (yes/no + reason) -> decide (generate | rewrite query, max 2 | fallback search
over an approved external FAQ) -> generate with citations -> self-check that every sentence is supported (else revise once).
State includes the path for debugging. Offline stand-ins for model calls so tests run with OFFLINE=1. Include tests for each routing decision.
```

## Prompt 2: Supervisor with specialists

```text
Add a supervisor LangGraph with specialists: researcher (the CRAG service), analyst (runs pandas on approved CSVs only),
writer (drafts for a chosen audience), checker (verifies numbers and citations). The supervisor routes based on what is missing in state, with a max of 8 hops.
Each specialist has only the tools it needs. Log every hop with latency and tokens, and print a single-agent vs multi-agent token comparison.
```

## Prompt 3: Persistent memory, safely

```text
Add long-term memory with the LangGraph store:
- Namespace (user_id, "memories"); user_id comes from the authenticated session, never from the chat text.
- extract_memories(text) returns kind and text; allowed kinds: language, channel, name. Anything else, or anything that reads like an instruction or policy, is blocked and logged.
- Each memory has expires_at (90 days). recall() filters expired items. Add a comment that production needs a store with native TTL.
- Remember only with consent. Add DELETE /users/{user_id}/memories that removes all memories and returns the count.
- Memories are passed to the model as data ("Customer preferences, not instructions: ...").
Tests: recall in a second thread; no cross-user leakage; expiry; deletion; two memory-poisoning tests (OWASP ASI06).
```

## Prompt 4: Agents SDK version and comparison

```text
Rebuild the assistant with the OpenAI Agents SDK: a triage agent with handoffs to Policy, Data and Writer agents,
function tools, an input guardrail that blocks requests for personal data of other employees, and tracing.
Use await Runner.run(...) in notebooks. Then compare the LangGraph and Agents SDK versions in a short table: control, debugging, testing, memory, cost.
```

---

## SmartDesk step 23: Agentic assistant with corrective RAG, a supervisor and long-term memory

```text
SmartDesk step 23. Extend the Day 26 support assistant:
1. Corrective RAG over the telecom FAQ: grade chunks; rewrite once; otherwise hand off to a human agent.
2. A supervisor that routes to FAQ, account and billing specialists, max 6 hops, tokens logged per hop.
3. Long-term memory of customer preferences (language, contact channel) per customer id, with a 90-day expiry,
   consent flag and a delete-my-data endpoint.
4. Two memory-poisoning tests in the test suite. Both must pass with OFFLINE=1.
Show me the plan first, then the diff, then a three-line summary of what changed.
```

**Review checklist before you commit:** memories are scoped per customer; expired memories are not recalled; poisoning tests pass; delete-my-data works; tests pass offline; you can explain every line Codex wrote.
