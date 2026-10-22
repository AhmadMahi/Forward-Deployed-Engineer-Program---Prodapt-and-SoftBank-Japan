# Day 28 Hotel Lab: Agent Protocols (MCP, A2A) and Advanced Agents

**Total time:** 105 to 120 minutes | **Day:** Thu 03 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- The Docker sandbox cell needs Docker Desktop on your laptop. In Colab, use the subprocess sandbox cell instead.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Monday. | `Day28_PostRead_Agent_Protocols_MCP_and_A2A_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Run the MCP server demo on the current SDK, call a tool from the agent, and run the data agent in the sandbox. | `Day28_Agent_Protocols_MCP_and_A2A_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (MCP, A2A and data agent). Stretch problem optional. | `Day28_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: protocol questions. | `Day28_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 24: MCP server for ticket tools. OpenAI Codex allowed; review every line. | `Day28_App_Build_Prompts.md` |

## Submit

Your MCP server's **tool list** (from `list_tools()`) and **one agent run log** showing which MCP tool the agent called and the answer.

## Stuck?

- `ModuleNotFoundError: No module named 'mcp.server.fastmcp'`: you are on mcp 2.x. Use `from mcp.server.mcpserver import MCPServer`.
- `SyntaxError: 'await' outside function`: run the cell in a notebook (top-level `await` works there), or wrap the code in `async def main()` and call `asyncio.run(main())` in a script.
- The stdio client hangs: check the server file ends with `mcp.run()` and that you started it with the same Python (`sys.executable`).
- Sandbox says `KILLED`: that is the time or CPU limit working. Make the query smaller.
