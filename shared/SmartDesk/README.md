# SmartDesk: the running project

SmartDesk is a customer support platform for a telecom operator. Learners build it step by step across the technical days of the FDE Program, from a command-line ticket logger on Day 2 to a monitored, agentic GenAI service on Day 35.

Each day's main app build stays the same as before. SmartDesk is the thread that connects the days, so learners see one product grow the way a real customer project does.

All data here is fictional. No real customers, policies or prices.

## Users

| User | Needs |
|---|---|
| Customer | Raise a ticket, get a fast and correct answer, choose how to be contacted |
| Support agent | See, search, update and close tickets; get AI summaries and suggested replies |
| Team lead | Approve refunds, watch SLAs, see analytics and costs |
| Admin | Manage users and roles, deployments, security and model versions |

## Architecture by stage

**Stage 1: CLI (Days 2 to 4)**
```
[agent at terminal] -> smartdesk.py -> tickets.json / MongoDB -> chart.png
```

**Stage 2: API and database (Days 5 to 7)**
```
[client] -> FastAPI (Pydantic, JWT roles) -> SQLite (SQLAlchemy) / MongoDB (analytics)
```

**Stage 3: Full stack (Days 8 to 11)**
```
[browser] -> React dashboard -> FastAPI ticket API -> SQLite
                             -> Express notification service
```

**Stage 4: GenAI and RAG (Days 12 to 22)**
```
[React] -> FastAPI -> llm_client (OpenAI API or offline stand-in) -> token log
                   -> RAG: FAQ index (vector + keyword) -> cited answer
CI (lint, tests, security gates) -> Docker image -> Azure Container Apps
```

**Stage 5: Agents (Days 23 to 28)**
```
[customer] -> supervisor -> SLM router -> LLM (escalation)
                         -> LangGraph assistant -> tools (tickets, outages, refunds + human approval)
                         -> CRAG over the FAQ -> long-term preference memory
                         -> MCP server (ticket tools), sandboxed analytics
```

**Stage 6: Production and LLMOps (Days 30 to 35)**
```
[client] -> LLM gateway (streaming, canary, rollback) -> guardrails -> resilient client (retries, fallback)
                 |                                                      |
                 +-> OpenTelemetry traces (tokens, cost) -> drift watch  +-> golden set + quality gate in CI
```

## The 30 steps

| Step | Day | Increment | Reference solution |
|---|---|---|---|
| 1 | [2](../../Day02-Python-Basics-Functions-and-Files/) | CLI ticket logger with functions; tickets saved as JSON | [step01-day02-cli-ticket-logger](step01-day02-cli-ticket-logger/) |
| 2 | [3](../../Day03-OOP-and-OpenAI-Codex-Walkthrough/) | Ticket, Customer and Agent classes; first Codex feature (search) | [step02-day03-oop-classes-and-search](step02-day03-oop-classes-and-search/) |
| 3 | [4](../../Day04-Architecture-and-MongoDB/) | Tickets in MongoDB; chart by priority | [step03-day04-mongodb-and-chart](step03-day04-mongodb-and-chart/) |
| 4 | [5](../../Day05-API-Fundamentals-and-FastAPI-Core/) | FastAPI ticket API with Pydantic models | [step04-day05-fastapi-ticket-api](step04-day05-fastapi-ticket-api/) |
| 5 | [6](../../Day06-SQLAlchemy-and-API-Docs/) | SQLite persistence with relationships; Swagger docs | [step05-day06-sqlite-relationships-docs](step05-day06-sqlite-relationships-docs/) |
| 6 | [7](../../Day07-FastAPI-Advanced-Security-and-MongoDB/) | JWT login with roles; Mongo analytics endpoint; vulnerability report v1 | [step06-day07-jwt-roles-analytics](step06-day07-jwt-roles-analytics/) |
| 7 | [8](../../Day08-JavaScript-and-Async-JavaScript/) | JavaScript client that reads the API asynchronously | [step07-day08-js-async-client](step07-day08-js-async-client/) |
| 8 | [9](../../Day09-Nodejs-and-Express/) | Express notification service with Postman tests | [step08-day09-express-notifications](step08-day09-express-notifications/) |
| 9 | [10](../../Day10-React-Basics/) | React dashboard with the ticket list | [step09-day10-react-dashboard](step09-day10-react-dashboard/) |
| 10 | [11](../../Day11-React-UI-Logic-and-Full-Stack/) | Full-stack create, update and close tickets | [step10-day11-full-stack-crud](step10-day11-full-stack-crud/) |
| 11 | [12](../../Day12-GenAI-Intro-LLMs-and-Tokens/) | First LLM call: ticket summary with token logging | [step11-day12-llm-summary-token-log](step11-day12-llm-summary-token-log/) |
| 12 | [13](../../Day13-Prompt-Engineering/) | Category classification with structured output and prompt templates | [step12-day13-structured-classification](step12-day13-structured-classification/) |
| 13 | [15](../../Day15-Testing-and-Data-Engineering-Intro/) | PyTest suite; legacy CSV import (ETL) | [step13-day15-pytest-and-csv-etl](step13-day15-pytest-and-csv-etl/) |
| 14 | [16](../../Day16-Data-Pipelines-Spark-and-PySpark/) | PySpark SLA metrics pipeline | [step14-day16-pyspark-sla-metrics](step14-day16-pyspark-sla-metrics/) |
| 15 | [17](../../Day17-DevOps-and-Cloud-Fundamentals/) | Lint, tests and pipeline YAML | [step15-day17-lint-tests-pipeline](step15-day17-lint-tests-pipeline/) |
| 16 | [18](../../Day18-Context-Engineering-and-RAG/) | RAG over the telecom FAQ with citations | [step16-day18-rag-faq-citations](step16-day18-rag-faq-citations/) |
| 17 | [20](../../Day20-Git-CI-CD-and-Docker/) | Docker images; CI with security gates; vulnerability report v2 | [step17-day20-docker-ci-security-gates](step17-day20-docker-ci-security-gates/) |
| 18 | [21](../../Day21-Azure-Deployment-and-CD/) | Deployed to Azure with CD | [step18-day21-azure-cd](step18-day21-azure-cd/) |
| 19 | [22](../../Day22-Embeddings-Vector-DBs-and-RAG-App/) | Hybrid search and re-ranking | [step19-day22-hybrid-search-rerank](step19-day22-hybrid-search-rerank/) |
| 20 | [23](../../Day23-Industry-Use-Cases-and-Agentic-Security-SME/) | Patch and modernise SmartDesk's legacy CSV module (SME assignment); map SmartDesk to a maturity level | [step20-day23-patch-and-modernise](step20-day23-patch-and-modernise/) |
| 21 | [25](../../Day25-SLMs-and-Token-Optimisation/) | SLM for classification, LLM for complex answers; cost report | [step21-day25-slm-llm-routing-cost](step21-day25-slm-llm-routing-cost/) |
| 22 | [26](../../Day26-LLM-Orchestration-Tools-and-LangGraph/) | Support assistant with tools in a LangGraph flow | [step22-day26-langgraph-support-assistant](step22-day26-langgraph-support-assistant/) |
| 23 | [27](../../Day27-Agentic-AI-Agentic-RAG-and-Memory/) | Agentic assistant with corrective RAG, a supervisor and long-term memory of customer preferences | [step23-day27-agentic-crag-memory](step23-day27-agentic-crag-memory/) |
| 24 | [28](../../Day28-Agent-Protocols-MCP-and-A2A/) | MCP server for ticket tools; sandboxed analytics agent | [step24-day28-mcp-server-sandbox](step24-day28-mcp-server-sandbox/) |
| 25 | [30](../../Day30-LLM-Security-and-Guardrails/) | Guardrail gateway and red-team suite; vulnerability report v3 | [step25-day30-guardrail-gateway-redteam](step25-day30-guardrail-gateway-redteam/) |
| 26 | [31](../../Day31-GenAI-System-Evaluation/) | Golden set and evaluation dashboard | [step26-day31-golden-set-eval-dashboard](step26-day31-golden-set-eval-dashboard/) |
| 27 | [32](../../Day32-LLM-Evaluation-and-Quality-Gates/) | Quality gate in CI with cost metrics | [step27-day32-ci-quality-gate](step27-day32-ci-quality-gate/) |
| 28 | [33](../../Day33-LLMOps/) | Resilient LLM client; cost and version dashboard | [step28-day33-resilient-client-cost-versions](step28-day33-resilient-client-cost-versions/) |
| 29 | [34](../../Day34-LLM-Deployment-and-Lifecycle/) | Production gateway with streaming and canary on Azure | [step29-day34-production-gateway-canary](step29-day34-production-gateway-canary/) |
| 30 | [35](../../Day35-Observability-Drift-and-Optimisation/) | Observability and drift watch; capstone hand-off | [step30-day35-observability-drift-handoff](step30-day35-observability-drift-handoff/) |

## How to use SmartDesk with each day

1. Start from the [starter](starter/) on Day 2, or from the previous step's reference solution if you fell behind.
2. Open the day folder and its `DayNN_App_Build_Prompts.md`. The last prompt in each file is the **SmartDesk step** prompt.
3. Build the step yourself with OpenAI Codex in VS Code. Ask for a plan first, then small steps.
4. Run the tests. Compare with the step folder here only after you have tried.
5. Each step folder is compact: it holds the key files for that increment, not the whole app.

## Rules

- **OpenAI Codex** is the AI coding tool, signed in with the program API key and approved models only (see `docs/MODEL_GUIDE.md`).
- **Review every diff.** Accept only code you can explain. Run the tests after every change.
- **No secrets.** Keys come from Colab Secrets, a git-ignored `.env` file or Key Vault. Never put keys, customer data or credentials in code, prompts or `AGENTS.md`.
- **Offline mode.** Every Python step runs and tests with `OFFLINE=1` and no API key. Offline output shows how the code works, not real model quality.
- **Placeholder prices.** Every cost number uses placeholder prices and says so.

## Run all tests

```bash
bash shared/SmartDesk/run_all_tests.sh              # every step
bash shared/SmartDesk/run_all_tests.sh step16-day18-rag-faq-citations
```

Python steps need the packages from the course (fastapi, sqlalchemy, pymongo, mongomock, pandas, scikit-learn, pyjwt, langgraph, mcp, opentelemetry-sdk, and pyspark with Java 17 for step 14). JavaScript steps use Node.js 22 and `node --test`; no `npm install` is needed for the tests.

## Folder map

- `starter/`: Day 2 starting point.
- `data/`: fictional tickets, the telecom FAQ and a messy legacy CSV.
- `stepNN-dayMM-*/`: one reference solution per step.
- `run_all_tests.sh`: runs every step's tests in offline mode.
