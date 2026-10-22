# Capstone 03: PolicyPal App Build Prompts

**Project:** PolicyPal: Enterprise HR and IT Policy Chatbot

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
You are a senior full stack and GenAI engineer helping a team build "PolicyPal" in 5 days.
Customer: Sakura Logistics, 4,000 employees in India and Japan, with HR and IT policies spread across 120 documents.
Problem: HR and IT help desks receive hundreds of repetitive questions a week. Employees cannot find answers in long PDFs and sometimes act on outdated information. The company wants an assistant that answers from current policies with citations, refuses when unsure, protects personal data, and hands over to a human with context.

Create a monorepo:
  api/   FastAPI (Python 3.11), Pydantic v2, SQLAlchemy 2.0 and/or PyMongo, pytest
  web/   React (Vite), with loading, error and empty states
  ai/    AI services (retrieval, models, tools, guardrails) behind clear interfaces, with an offline stand-in when no API key is set
  data/  generators and sample data (from our starter notebook)
  eval/  golden set (JSONL) and evaluation scripts
  ops/   Dockerfiles, docker-compose.yml, azure-pipelines.yml
Must-have features:
- Ingestion pipeline for Markdown and PDF policies with structure-aware chunking and metadata (Day 18)
- Hybrid retrieval with re-ranking and corrective RAG (Days 22, 27)
- Grounded answers with citations; refusal below a relevance threshold
- Guardrails: injection scanning on documents and inputs, PII redaction on outputs (Day 30)
- Human handoff creating a ticket with a structured payload (Day 28)
- Golden set of 30 items and a CI quality gate (Days 31, 32)
- React chat UI with citations and feedback buttons
Start with: folder structure, data models, API endpoint list with request and response schemas, and an architecture description.
Do not write all features yet. Include a README skeleton and an AGENTS.md with commands and conventions.
NEW (v4) baseline for every project:
- AGENTS.md at the repo root: build, test and style commands, folders not to touch, "never put secrets in prompts".
- Modernisation step: The starter notebook includes legacy_faq_answer(), a keyword if/else FAQ bot. Write characterisation tests, then replace it with the RAG service behind the same function signature, keeping the refusal behaviour.
- docs/security_checklist.md mapped to the OWASP Top 10 for Agentic Applications (copy shared/templates/OWASP_Agentic_Checklist.md).
- docs/vulnerability_report.md (copy shared/templates/Vulnerability_Report_Template.md).
- Every model call logs input, output and reasoning tokens and an estimated cost (placeholder prices, labelled).
```

---

## Prompt 2: Build the AI core (Day 37)

```text
Implement the AI core for PolicyPal.
Approach: Context engineering and chunking (Day 18), hybrid search and re-ranking (Day 22), CRAG (Day 27), guardrails (Day 30), evaluation and gates (Days 31, 32).
Requirements:
- Every model call goes through one client with timeouts, retries with backoff, a fallback and JSON logging (request id, release, tokens, latency).
- Facts such as prices, stock, availability, order details or numbers must come from the database or tools, never from the model.
- Provide an offline stand-in so tests run without an API key.
Write unit tests for the core logic and an evaluation script that runs the golden set and prints metrics.
Acceptance checks we must pass:
- Faithfulness on the golden set at least 0.9
- Unanswerable questions refused
- Injection test suite: block rate at least 90%, false alarms at most 10%
- Citations point to the right section
```

---

## Prompt 3: Front end, guardrails and quality gate (Day 38)

```text
For PolicyPal:
1. Build the React screens for these user stories:
   - As an employee, I ask "Can I carry forward my leave?" and get a short answer with the policy section cited.
   - As an employee, when the assistant cannot answer, I am handed to a human with my question summarised.
   - As a policy owner, I upload an updated policy and answers change the same day.
   - As security, I see that personal data is redacted and injection attempts are blocked.
   - As the help desk lead, I see the most common unanswered topics each week.
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
For PolicyPal:
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

- Role-based access to confidential policies
- Conversation memory with summaries
- Teams or Slack integration design
