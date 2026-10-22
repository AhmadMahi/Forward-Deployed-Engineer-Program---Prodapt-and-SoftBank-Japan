# Capstone 05: InsightDesk App Build Prompts

**Project:** InsightDesk: Retail Sales Pipeline and Natural Language Data Agent

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Run the prompts in order with OpenAI Codex in VS Code (program API key, approved models only), one per working session. Ask Codex for a plan first, then build in small steps.
2. Review every diff before you accept it. You must be able to explain all of it on demo day.
3. Commit after each prompt with a clear message, through a reviewed pull request. Keep CI green.
4. Record in your README which parts were generated and how you checked them.
5. Never paste API keys, customer data or credentials into a prompt or AGENTS.md. Check your daily token usage.

---

## Prompt 1: Scaffold the project (Day 36)

```text
You are a senior full stack and GenAI engineer helping a team build "InsightDesk" in 5 days.
Customer: Sakura Retail, 40 stores across India and Japan, with daily sales files from point-of-sale systems.
Problem: Store managers wait a week for Excel reports built by hand, and numbers often disagree between teams. The company wants a reliable daily pipeline, trusted gold tables, and a way for managers to ask questions in plain language and get answers with the working shown.

Create a monorepo:
  api/   FastAPI (Python 3.11), Pydantic v2, SQLAlchemy 2.0 and/or PyMongo, pytest
  web/   React (Vite), with loading, error and empty states
  ai/    AI services (retrieval, models, tools, guardrails) behind clear interfaces, with an offline stand-in when no API key is set
  data/  generators and sample data (from our starter notebook)
  eval/  golden set (JSONL) and evaluation scripts
  ops/   Dockerfiles, docker-compose.yml, azure-pipelines.yml
Must-have features:
- PySpark medallion pipeline (bronze, silver, gold) with explicit schemas, quality checks, rejects and an idempotent run per date (Day 16)
- Gold tables: daily store revenue, product category performance, customer segments; served by a FastAPI API
- Natural-language data agent that writes SQL or pandas, checks it (AST or SQL allowlist), runs it in a sandbox and shows code and result (Day 28)
- React dashboard with key charts and the question box
- Pipeline and agent tests; scheduled run design (Days 15, 20)
- Evaluation: 25 business questions with expected numbers
Start with: folder structure, data models, API endpoint list with request and response schemas, and an architecture description.
Do not write all features yet. Include a README skeleton and an AGENTS.md with commands and conventions.
NEW (v4) baseline for every project:
- AGENTS.md at the repo root: build, test and style commands, folders not to touch, "never put secrets in prompts".
- Modernisation step: The starter notebook includes legacy_daily_report(), a pandas script that appends to a global list and duplicates rows on re-run. Write characterisation tests, then migrate it to an idempotent gold table job with reconciliation.
- docs/security_checklist.md mapped to the OWASP Top 10 for Agentic Applications (copy shared/templates/OWASP_Agentic_Checklist.md).
- docs/vulnerability_report.md (copy shared/templates/Vulnerability_Report_Template.md).
- Every model call logs input, output and reasoning tokens and an estimated cost (placeholder prices, labelled).
```

---

## Prompt 2: Build the AI core (Day 37)

```text
Implement the AI core for InsightDesk.
Approach: Data agent with sandboxed code (Day 28), evaluation of numeric answers (Days 31, 32), drift detection (Day 35).
Requirements:
- Every model call goes through one client with timeouts, retries with backoff, a fallback and JSON logging (request id, release, tokens, latency).
- Facts such as prices, stock, availability, order details or numbers must come from the database or tools, never from the model.
- Provide an offline stand-in so tests run without an API key.
Write unit tests for the core logic and an evaluation script that runs the golden set and prints metrics.
Acceptance checks we must pass:
- Gold revenue reconciles with silver within 0.01
- Re-running a date leaves counts unchanged
- Agent answers match expected numbers on at least 80% of questions
- Generated code with imports or file access is blocked
```

---

## Prompt 3: Front end, guardrails and quality gate (Day 38)

```text
For InsightDesk:
1. Build the React screens for these user stories:
   - As a manager, I ask "Which Osaka stores grew fastest last month?" and see the answer, a chart and the query used.
   - As finance, I trust that daily revenue matches the source files (reconciliation).
   - As a data engineer, I can re-run any day without creating duplicates.
   - As a manager, I get alerted when a store's data is missing or looks wrong.
   - As an analyst, I see which questions the agent could not answer.
2. Add input and output guardrails (injection scan, PII redaction, allowlisted tools, human approval for risky actions where relevant).
3. Extend the golden set to at least 20 items (include tricky and unanswerable cases and, where relevant, Japanese inputs) and add a quality gate
   script that exits with code 1 when thresholds fail. Add it to the CI pipeline.
4. NEW (v4): Run bandit, pip-audit and npm audit; add them as CI gates. Log every finding in docs/vulnerability_report.md
   (finding, tool, severity, file, fix, fixed by human or Codex-assisted, verified, evidence). Fill in docs/security_checklist.md
   for the OWASP Top 10 for Agentic Applications with one line of evidence per item.
5. NEW (v4): Finish the modernisation step: characterisation tests green before and after, one reviewed PR per step.
```

---

## Prompt 4: Deploy, observe and prepare the demo (Day 39)

```text
For InsightDesk:
1. Write production Dockerfiles (non-root, health checks) and docker-compose for local runs.
2. Write azure-pipelines.yml: Test, Evaluate (quality gate), Build (images), DeployDev, DeployProd with approval.
3. Add a monitoring view: requests, p95 latency, error rate, cost, and a quality signal (feedback or refusal rate), plus one drift or data quality check.
4. Draft an 8 to 12 slide demo outline: problem, users, live demo script, results with numbers, limits, next steps.
5. Write a runbook for the most likely production incident.
6. NEW (v4): Write docs/token_cost_report.md: tokens and estimated cost per request and per 1,000 requests from the token log,
   then apply one optimisation (prompt caching layout, context trimming, smaller model or routing) and show before and after.
   Label every price as a placeholder.
```

---

## Stretch ideas

- Forecast for next week per store
- Explanations of anomalies
- Export to Excel
