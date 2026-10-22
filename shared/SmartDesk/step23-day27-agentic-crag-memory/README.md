# SmartDesk step 23 (Day 27): Agentic assistant with CRAG, a supervisor and memory

**Increment:** Agentic assistant with corrective RAG, a supervisor and long-term memory of customer preferences

**Day folder:** [../../../Day27-Agentic-AI-Agentic-RAG-and-Memory/](../../../Day27-Agentic-AI-Agentic-RAG-and-Memory/) (see `Day27_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 22](../step22-day26-langgraph-support-assistant/) | Next: [step 24](../step24-day28-mcp-server-sandbox/)

## Goal

Build an agentic assistant that checks its own evidence (corrective RAG), routes work through a supervisor, and remembers customer preferences safely across sessions.

## What changed from the previous step

Adds CRAG (retrieve, grade, rewrite, escalate), a supervisor, and long-term per-user memory with TTL, consent, deletion and a memory-poisoning guard.

## Key files

- `agents.py`: CragFaq and Supervisor
- `memory.py`: PreferenceMemory on the LangGraph store
- `test_agents.py`: two-session memory, poisoning, expiry and deletion tests

## How to run

```bash
python -c "from agents import Supervisor; s = Supervisor(); print(s.handle('u1', 'prefer sms. router red light'))"
```

## How to test

```bash
python -m pytest -q
```

## Memory risks (NEW v4)

Memory poisoning (OWASP ASI06) means an attacker plants an instruction that the agent later trusts. We store only allow-listed preference types, reject instruction-like text, keep memories per user, expire them, ask for consent and delete on request. Managed options such as Vertex AI Agent Engine Memory Bank follow the same ideas.

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
