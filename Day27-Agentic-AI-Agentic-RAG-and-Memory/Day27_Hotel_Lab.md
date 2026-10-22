# Day 27 Hotel Lab: Agentic AI, Agentic RAG and Memory

**Total time:** 105 to 120 minutes | **Day:** Wed 02 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.
- Never store real customer data in a demo memory store.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day27_PostRead_Agentic_AI_Agentic_RAG_and_Memory_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Add a corrective RAG step, then add a long-term memory store that recalls a customer's preference in a second session. | `Day27_Agentic_AI_Agentic_RAG_and_Memory_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (agent design, CRAG and multi-agent). Stretch problem optional. | `Day27_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: agent components questions. | `Day27_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 23: agentic assistant with memory of customer preferences. OpenAI Codex allowed; review every line. | `Day27_App_Build_Prompts.md` |

## Submit

A **two-session transcript** showing memory (session 1 states a preference, session 2 on a new thread uses it), plus **one memory-poisoning test** and its result.

## Stuck?

- Session 2 does not remember: check you used the same `user_id` but a different `thread_id`, and compiled the graph with `store=store`.
- `NotImplementedError: TTL is not supported`: `InMemoryStore` has no native TTL. Store `expires_at` and filter on read, as in the notebook.
- Another customer sees the memory: your namespace is missing the user id. Use `(user_id, "memories")`.
- The Agents SDK cell says offline: it needs a key. The MiniAgent cell shows the same loop without one.
