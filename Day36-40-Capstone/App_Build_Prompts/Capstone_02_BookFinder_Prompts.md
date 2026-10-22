# Capstone 02: BookFinder App Build Prompts

**Project:** BookFinder: Library Book Finder with Natural Language Search

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
You are a senior full stack and GenAI engineer helping a team build "BookFinder" in 5 days.
Customer: The Sakura City Library network: 5 branches in Bengaluru and Tokyo, 8,000 titles in English and Japanese.
Problem: Members find the catalogue search frustrating: it needs exact titles. Librarians spend hours answering "I want something like..." questions. The library wants natural-language search, explainable recommendations and live availability across branches.

Create a monorepo:
  api/   FastAPI (Python 3.11), Pydantic v2, SQLAlchemy 2.0 and/or PyMongo, pytest
  web/   React (Vite), with loading, error and empty states
  ai/    AI services (retrieval, models, tools, guardrails) behind clear interfaces, with an offline stand-in when no API key is set
  data/  generators and sample data (from our starter notebook)
  eval/  golden set (JSONL) and evaluation scripts
  ops/   Dockerfiles, docker-compose.yml, azure-pipelines.yml
Must-have features:
- Catalogue and loans data model in SQL (books, copies, branches, members, loans) with SQLAlchemy relationships
- Hybrid search (BM25 + embeddings) over title, author, summary and subjects with filters (language, branch, available now)
- Recommendation explanations generated from catalogue data with citations to book ids, no invented books
- Reservation flow with transaction safety (no double booking)
- React UI: search, results with availability, book page, my loans
- Evaluation: search hit rate@5 on a golden set of 25 natural-language queries
Start with: folder structure, data models, API endpoint list with request and response schemas, and an architecture description.
Do not write all features yet. Include a README skeleton and an AGENTS.md with commands and conventions.
NEW (v4) baseline for every project:
- AGENTS.md at the repo root: build, test and style commands, folders not to touch, "never put secrets in prompts".
- Modernisation step: The starter notebook includes legacy_import(), a CSV catalogue import that builds SQL strings by hand. Write characterisation tests, then migrate it to SQLAlchemy models with parameterised writes, in small verified steps.
- docs/security_checklist.md mapped to the OWASP Top 10 for Agentic Applications (copy shared/templates/OWASP_Agentic_Checklist.md).
- docs/vulnerability_report.md (copy shared/templates/Vulnerability_Report_Template.md).
- Every model call logs input, output and reasoning tokens and an estimated cost (placeholder prices, labelled).
```

---

## Prompt 2: Build the AI core (Day 37)

```text
Implement the AI core for BookFinder.
Approach: Embeddings and hybrid search with RRF (Day 22); grounded explanations (Day 18); optional query rewriting (Day 27).
Requirements:
- Every model call goes through one client with timeouts, retries with backoff, a fallback and JSON logging (request id, release, tokens, latency).
- Facts such as prices, stock, availability, order details or numbers must come from the database or tools, never from the model.
- Provide an offline stand-in so tests run without an API key.
Write unit tests for the core logic and an evaluation script that runs the golden set and prints metrics.
Acceptance checks we must pass:
- Search beats keyword-only on hit rate@5
- Every recommended book exists in the catalogue
- Reservation is atomic under concurrent requests
- Japanese queries evaluated separately
```

---

## Prompt 3: Front end, guardrails and quality gate (Day 38)

```text
For BookFinder:
1. Build the React screens for these user stories:
   - As a member, I search "a gentle mystery set in Kyoto" and get relevant books with a one-line reason each.
   - As a member, I see which branch has a copy available now and can reserve it.
   - As a member, I get "if you liked this" suggestions based on my loans.
   - As a librarian, I see searches that returned nothing, so I know what to buy.
   - As a branch manager, I see loan trends by subject and language.
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
For BookFinder:
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

- Reading lists generated for themes
- Accessibility features (large text, screen reader labels)
- Weekly drift report on search topics
