# Day 27: App Build Prompts

**App of the day:** Enterprise Agent Hub (MCP servers + A2A-style agents + data agent)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 27. Exposes company systems through MCP, delegates between agents, hands off to humans and answers data questions safely.

---

## Prompt 1: MCP servers

```text
You are a senior GenAI engineer. Build two MCP servers with the Python MCP SDK (pin mcp<2, FastMCP):
1. orders_server: tools get_order_status, list_recent_orders(customer_id, limit<=20), calculate_refund; resource policy://refunds; prompt apology_email.
2. kb_server: tool search_policies(query, k) using hybrid search from Day 23; resource kb://index-stats.
Validate every input, return errors as JSON, write an audit log line per call. Include a client script that lists and calls everything, and tests.
```

---

## Prompt 2: Agents and handoffs

```text
Build a support agent (OpenAI Agents SDK or LangGraph, your choice) that uses both MCP servers' tools, delegates refund
calculations to a separate refund agent exposed with an agent card and a /tasks endpoint (A2A style), and hands off to a human with a
Pydantic Handoff payload when the refund exceeds a limit or the customer is upset. Show three example conversations with traces.
```

---

## Prompt 3: Data analysis agent

```text
Add a data analysis agent: the model writes pandas code for questions on approved CSVs; code is checked with an AST
allowlist and executed in a subprocess with a timeout and row limit; the answer shows the code, a result table and a one-sentence explanation.
Include tests proving that imports, file access, dunder attributes and long loops are blocked.
```

---

## Stretch ideas (try on your own)

- Serve one MCP server over HTTP instead of stdio.
- Keep a registry of agent cards and route by skill.
- Add a chart output to the data agent (Matplotlib PNG).
