# SmartDesk step 24 (Day 28): MCP server for ticket tools and a sandboxed analytics agent

**Increment:** MCP server for ticket tools; sandboxed analytics agent

**Day folder:** [../../../Day28-Agent-Protocols-MCP-and-A2A/](../../../Day28-Agent-Protocols-MCP-and-A2A/) (see `Day28_App_Build_Prompts.md`, SmartDesk step prompt)

Previous: [step 23](../step23-day27-agentic-crag-memory/) | Next: [step 25](../step25-day30-guardrail-gateway-redteam/)

## Goal

Expose SmartDesk ticket tools through an MCP server on the current SDK, use them from an agent and from OpenAI Codex, and run agent-written analytics code in a sandbox.

## What changed from the previous step

Adds an MCP server (MCPServer, SDK v2), an agent that discovers and calls tools, a Codex config example and a sandbox runner with limits and no secrets.

## Key files

- `mcp_server.py`: three tools with typed input and output (structured content)
- `agent_demo.py`: tool discovery and calling, online or offline
- `sandbox.py`: isolated process with CPU, memory and time limits
- `codex_config_example.toml`: use the server from Codex
- `test_mcp.py`: tool, validation and sandbox tests

## How to run

```bash
python mcp_server.py           # stdio server for Codex or other MCP clients
python agent_demo.py
```

## How to test

```bash
python -m pytest -q
```

## MCP 2026-07-28 notes (NEW v4)

- SDK v2 renamed `FastMCP` to `MCPServer`. Old v1 code pinned `mcp<2`; that pin is removed.
- Servers are stateless by default and remote servers use OAuth 2.1 for authorisation.
- Long-running work can use Tasks. A2A v1.0 signed Agent Cards cover agent-to-agent calls.

## Notes

- This is a compact reference solution. It holds only the key files for this increment, not the full app.
- Build your own version with OpenAI Codex using the day's prompts. Review every diff before you accept it.
- Never put API keys or customer data in code or prompts.
