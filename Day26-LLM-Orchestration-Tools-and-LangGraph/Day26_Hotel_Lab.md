# Day 26 Hotel Lab: LLM Orchestration, Tool Calling and LangGraph

**Total time:** 105 to 120 minutes | **Day:** Tue 01 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day26_PostRead_LLM_Orchestration_Tools_and_LangGraph_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add one tool to the assistant and an interrupt for human approval in the LangGraph flow. | `Day26_LLM_Orchestration_Tools_and_LangGraph_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (tool calling and LangGraph). Stretch problem optional. | `Day26_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: orchestration questions (technical sections). | `Day26_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 22: support assistant with tools. OpenAI Codex allowed; review every line. | `Day26_App_Build_Prompts.md` |

## Submit

Your **graph diagram** (the Mermaid output from `app.get_graph().draw_mermaid()`) and a **run log** showing the path, the pause for approval and the resumed result.

## Stuck?

- `ModuleNotFoundError: langchain` or `langgraph`: run the install cell again, then **Runtime > Restart session**.
- The graph never pauses: check the node calls `interrupt(...)` and the graph was compiled with a checkpointer.
- Resume does nothing: use the same `thread_id` in the config for the first call and for `Command(resume=...)`.
- Old tutorials use `AgentExecutor` or `initialize_agent`: those are legacy in LangChain v1. Use `create_agent`.
