# Day 25: App Build Prompts

**App of the day:** Customer Support Copilot (tool calling + LangGraph)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 25. A support assistant that looks up orders with tools, follows a workflow with retries, and asks a human before risky actions.

---

## Prompt 1: Tools and loop

```text
You are a senior GenAI engineer. Build the tool layer for a "Customer Support Copilot" in Python:
- Tools: get_order_status(order_id), calculate_refund(amount, days_late), search_policy(query), create_ticket(summary, priority), issue_refund(order_id, amount)
- Each tool has a JSON schema, a Pydantic argument model and a risk level (read | write). Write tools require human confirmation.
- run_tool with an allowlist, validation errors returned as text, timeouts and an audit log (time, tool, args, result, approved_by).
- A tool calling loop using the OpenAI chat completions API with a max step limit, plus an offline stand-in so tests run without a key.
Include unit tests for validation, the allowlist and the confirmation gate.
```

---

## Prompt 2: LangGraph workflow

```text
Build the workflow with LangGraph: classify (order, policy, complaint, other) -> specialised node -> draft answer -> quality check
-> (done | retry with rewritten query, max 2 | human handoff). Add a checkpointer and interrupt before issue_refund so a human can approve or reject.
Print the Mermaid diagram and show three example runs with their paths.
```

---

## Prompt 3: API and approvals UI

```text
Expose the copilot with FastAPI: POST /chat (returns answer, path, pending_approval if any), POST /approvals/{id} (approve or reject).
Build a small React page with the chat, a visible path trace, and an approvals panel. Explain how the approval resumes the paused graph.
```

---

## Stretch ideas (try on your own)

- Run independent tool calls in parallel.
- Add a daily report of failed answers to feed the knowledge base (the leverage point from the systems activity).
- Track cost and latency per conversation.
