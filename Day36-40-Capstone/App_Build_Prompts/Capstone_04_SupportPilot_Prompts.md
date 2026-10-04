# Capstone 04: SupportPilot App Build Prompts

**Project:** SupportPilot: Agentic Customer Support Copilot

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Run the prompts in order with your AI coding assistant, one per working session.
2. Review every file it produces. You must be able to explain all of it on demo day.
3. Commit after each prompt with a clear message, through a pull request.
4. Record in your README which parts were generated and how you checked them.

---

## Prompt 1: Scaffold the project (Day 36)

```text
You are a senior full stack and GenAI engineer helping a team build "SupportPilot" in 5 days.
Customer: Sakura Home's customer service team: 25 agents handling 3,000 tickets a day about orders, deliveries, returns and refunds.
Problem: Agents switch between five systems to answer one ticket, and refund rules are applied inconsistently. The team wants a copilot that looks up orders, applies refund policy correctly, drafts replies, and asks a human before any money moves.

Create a monorepo:
  api/   FastAPI (Python 3.11), Pydantic v2, SQLAlchemy 2.0 and/or PyMongo, pytest
  web/   React (Vite), with loading, error and empty states
  ai/    AI services (retrieval, models, tools, guardrails) behind clear interfaces, with an offline stand-in when no API key is set
  data/  generators and sample data (from our starter notebook)
  eval/  golden set (JSONL) and evaluation scripts
  ops/   Dockerfiles, docker-compose.yml, azure-pipelines.yml
Must-have features:
- Orders, customers, tickets and refunds data with an API (FastAPI + SQL or MongoDB)
- Tool calling with validated arguments: get_order, get_customer_history, calculate_refund, search_policy, draft_reply, issue_refund (Day 25)
- LangGraph workflow: classify ticket, gather facts, decide, draft, human approval for risky actions (Days 25, 26)
- Policy RAG for refund and delivery rules with citations
- An MCP server exposing order tools (Day 27)
- Approval queue UI in React and a full audit log
- Red-team tests for injection in ticket text (Day 28)
Start with: folder structure, data models, API endpoint list with request and response schemas, and an architecture description.
Do not write all features yet. Include a README skeleton and an AGENTS.md with commands and conventions.
```

---

## Prompt 2: Build the AI core (Day 37)

```text
Implement the AI core for SupportPilot.
Approach: Tool calling and LangGraph (Day 25), agents and handoffs (Days 26, 27), MCP (Day 27), guardrails and approvals (Day 28).
Requirements:
- Every model call goes through one client with timeouts, retries with backoff, a fallback and JSON logging (request id, release, tokens, latency).
- Facts such as prices, stock, availability, order details or numbers must come from the database or tools, never from the model.
- Provide an offline stand-in so tests run without an API key.
Write unit tests for the core logic and an evaluation script that runs the golden set and prints metrics.
Acceptance checks we must pass:
- Refund amounts match policy on all labelled tickets
- No refund executed without approval
- Injection tickets never trigger tools outside the allowlist
- Every action appears in the audit log
```

---

## Prompt 3: Front end, guardrails and quality gate (Day 38)

```text
For SupportPilot:
1. Build the React screens for these user stories:
   - As an agent, I paste a ticket and get the order status, the applicable policy and a draft reply in seconds.
   - As an agent, refunds above a limit go to my team lead for one-click approval.
   - As a team lead, I see every action the copilot proposed and who approved it.
   - As a manager, I see resolution time and refund amounts by week.
   - As security, I know the copilot cannot be tricked into issuing refunds.
2. Add input and output guardrails (injection scan, PII redaction, allowlisted tools, human approval for risky actions where relevant).
3. Extend the golden set to at least 20 items (include tricky and unanswerable cases and, where relevant, Japanese inputs) and add a quality gate
   script that exits with code 1 when thresholds fail. Add it to the CI pipeline.
```

---

## Prompt 4: Deploy, observe and prepare the demo (Day 39)

```text
For SupportPilot:
1. Write production Dockerfiles (non-root, health checks) and docker-compose for local runs.
2. Write azure-pipelines.yml: Test, Evaluate (quality gate), Build (images), DeployDev, DeployProd with approval.
3. Add a monitoring view: requests, p95 latency, error rate, cost, and a quality signal (feedback or refusal rate), plus one drift or data quality check.
4. Draft an 8 to 12 slide demo outline: problem, users, live demo script, results with numbers, limits, next steps.
5. Write a runbook for the most likely production incident.
```

---

## Stretch ideas

- A2A-style delegation to a separate refunds agent
- Sentiment trend dashboard
- Multilingual replies (English and Japanese)
