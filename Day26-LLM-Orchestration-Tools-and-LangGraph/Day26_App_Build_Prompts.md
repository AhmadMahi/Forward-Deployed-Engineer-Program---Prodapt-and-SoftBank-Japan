# Day 26: App Build Prompts

**App of the day:** Customer Support Assistant (tool calling + LangGraph). This is the v1 Day 25 support app under its v4 name.

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 26. A support assistant that looks up orders with tools, follows a workflow with retries, and pauses for a human before risky actions.

---

## Prompt 1: Tools and the direct API loop

```text
You are a senior GenAI engineer. Build the tool layer for a "Customer Support Assistant" in Python:
- Tools: get_order_status(order_id), calculate_refund(amount, days_late), search_policy(query), create_ticket(summary, priority), issue_refund(order_id, amount)
- Each tool has a lean JSON schema (verb-noun name, one-line description with an example value), a Pydantic argument model and a risk level (read | write).
- run_tool with an allowlist, validation errors returned as text, timeouts and an audit log (time, tool, args, result, approved_by).
- A tool calling loop using the OpenAI API with a max step limit. Model name from LLM_MODEL; key from the environment.
- An offline stand-in model so tests run with OFFLINE=1 and no key.
- A function tool_schema_tokens() that counts the tokens of all tool definitions with tiktoken.
Include unit tests for validation, the allowlist and the step limit.
```

## Prompt 2: LangChain v1 agent with middleware

```text
Rebuild the assistant with LangChain v1: create_agent(model, tools, system_prompt, middleware, checkpointer).
- Middleware: a @before_model logger, a @wrap_tool_call audit log, ModelCallLimitMiddleware(run_limit=6),
  and HumanInTheLoopMiddleware(interrupt_on={"issue_refund": True, "create_ticket": False}).
- Use InMemorySaver for tests; leave a comment on how to switch to a database checkpointer in production.
- Do not use AgentExecutor, initialize_agent or LLMChain (legacy).
Tests: the agent pauses before issue_refund; resume with approve and with reject; the call limit stops a loop.
```

## Prompt 3: LangGraph workflow with durable approval

```text
Build the workflow with LangGraph: classify (order, policy, complaint, other) -> specialised node -> draft answer -> quality check
-> (done | retry with rewritten query, max 2 | human handoff).
- An approve_refund node that calls interrupt() and defaults to "no" unless the reviewer says "yes".
- Compile with a checkpointer. Show: pause, list checkpoints with get_state_history, resume with Command(resume=...).
- Show recovery: a payment node that fails once, then the same thread resumes without rerunning finished steps.
Print the Mermaid diagram and three example runs with their paths.
```

## Prompt 4: API and approvals UI

```text
Expose the assistant with FastAPI: POST /chat (returns answer, path, pending_approval if any), POST /approvals/{thread_id} (approve or reject).
Build a small React page with the chat, a visible path trace, and an approvals panel. The front end calls only our API; no key in the browser.
Explain in the README how an approval resumes the paused graph.
```

---

## SmartDesk step 22: Support assistant with tools in a LangGraph flow

```text
SmartDesk step 22. Add a support assistant to SmartDesk:
1. Tools: get_ticket(ticket_id), get_customer_plan(customer_id), search_faq(query) (the RAG from Day 22), issue_credit(customer_id, amount) marked risky.
2. A LangGraph flow: classify -> tools -> answer -> check; retry once; otherwise hand off to a human agent.
3. issue_credit pauses with interrupt() and needs a human "yes"; every decision is logged.
4. Log tokens per run, including tool schema tokens, to the token log from Day 12.
5. Tests run with OFFLINE=1. Update AGENTS.md with the new test command.
Show me the plan first, then the diff, then a three-line summary of what changed.
```

**Review checklist before you commit:** risky tools cannot run without approval; tool arguments are validated; the step limit is set; tests pass offline; you can explain every line Codex wrote.
