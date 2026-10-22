# Day 28: App Build Prompts

**App of the day:** Enterprise Agent Hub (MCP servers on the current SDK + A2A-style agents + sandboxed data agent)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 28. Exposes tools once through MCP, delegates work to other agents with verified Agent Cards, and runs model-written code only in a sandbox.

---

## Prompt 1: MCP servers on the current SDK

```text
You are a senior GenAI engineer. Build two MCP servers with the current Python MCP SDK (mcp 2.x). Do NOT pin mcp<2 and do NOT use FastMCP:
use `from mcp.server.mcpserver import MCPServer`.
1. orders_server: tools get_order_status, list_recent_orders(customer_id, limit<=20), calculate_refund; resource policy://refunds; prompt apology_email.
2. kb_server: tool search_policies(query, k) using hybrid search from Day 22; resource kb://index-stats.
Validate every input, return errors as JSON, write an audit log line per call.
Tests use `mcp.Client(server)` in-process. Add a client script that connects over stdio with StdioServerParameters and prints the protocol version.
```

## Prompt 2: Remote, stateless and secured

```text
Make kb_server available remotely: mcp.run("streamable-http", stateless_http=True).
Add OAuth 2.1 bearer-token checks with a TokenVerifier and AuthSettings(required_scopes=["kb:read"], resource_server_url=..., validate_token_resource=True).
In tests, use a fake verifier that accepts one short-lived test token and rejects expired or wrong-audience tokens.
Add a slow export_policies tool and describe how it would use MCP Tasks (working -> completed, cancel, TTL).
```

## Prompt 3: Agents, signed Agent Cards and handoffs

```text
Build a support agent (LangChain create_agent or the OpenAI Agents SDK) that uses both MCP servers' tools by wrapping list_tools() results as agent tools.
It delegates refund calculations to a separate refund agent that publishes a signed Agent Card at /.well-known/agent-card.json and accepts /tasks (A2A style).
Sign the card with Ed25519 over the canonical JSON; the support agent verifies it against an approved registry of public keys and refuses unverified cards.
Hand off to a human with a Pydantic Handoff payload when the refund exceeds a limit or the customer is upset. Show three example conversations with traces.
```

## Prompt 4: Sandboxed data analysis agent

```text
Add a data analysis agent: the model writes pandas code for questions on approved CSVs; code is checked with an AST
allowlist and executed in a separate process with CPU, memory and time limits and an empty environment.
Add a Docker runner: an image with pandas pre-installed, run with --network none --read-only --memory 256m --cpus 0.5, data mounted read-only.
The answer shows the code, a result table and a one-sentence explanation.
Include tests proving that imports, file access, dunder attributes and long loops are blocked or killed.
```

---

## SmartDesk step 24: MCP server for ticket tools; sandboxed analytics agent

```text
SmartDesk step 24.
1. Create smartdesk_mcp/server.py with MCPServer: tools get_ticket, list_open_tickets, update_status (write, needs approval); resource policy://sla.
2. Point the Day 27 assistant at these tools through mcp.Client instead of calling the database directly.
3. Add the server to my local Codex configuration as a read-only server for development, and document the steps in the README.
4. Add an analytics agent that answers questions about ticket CSVs with sandboxed pandas code.
5. Tests run with OFFLINE=1 and use the in-process Client.
Show me the plan first, then the diff, then a three-line summary of what changed.
```

**Review checklist before you commit:** no `mcp<2` pin or FastMCP import; inputs validated and logged; remote server needs a valid token; unverified Agent Cards are refused; generated code never runs in your main process; you can explain every line Codex wrote.
