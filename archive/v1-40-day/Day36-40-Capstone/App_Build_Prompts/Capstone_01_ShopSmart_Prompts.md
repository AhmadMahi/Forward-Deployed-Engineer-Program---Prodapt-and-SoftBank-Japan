# Capstone 01: ShopSmart App Build Prompts

**Project:** ShopSmart: E-commerce Recommendation and Shopping Assistant

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
You are a senior full stack and GenAI engineer helping a team build "ShopSmart" in 5 days.
Customer: Sakura Home, an online home goods retailer in India and Japan with 2,000 products and 30,000 customers.
Problem: Customers struggle to find relevant products; the home page shows the same best sellers to everyone and search only matches exact words. Sakura Home wants personalised recommendations and a shopping assistant that answers product questions accurately, without inventing prices or stock.

Create a monorepo:
  api/   FastAPI (Python 3.11), Pydantic v2, SQLAlchemy 2.0 and/or PyMongo, pytest
  web/   React (Vite), with loading, error and empty states
  ai/    AI services (retrieval, models, tools, guardrails) behind clear interfaces, with an offline stand-in when no API key is set
  data/  generators and sample data (from our starter notebook)
  eval/  golden set (JSONL) and evaluation scripts
  ops/   Dockerfiles, docker-compose.yml, azure-pipelines.yml
Must-have features:
- Product catalogue API with search (keyword + semantic hybrid)
- Recommendations: popularity baseline, item-to-item co-purchase, and content-based with embeddings
- Shopping assistant (RAG over product descriptions and FAQs) that cites product ids and reads price and stock from the database, never from the model
- React storefront: home recommendations, search, product page with "also bought", assistant panel
- Offline evaluation: precision@k and hit rate@k on held-out purchases; golden set for the assistant
Start with: folder structure, data models, API endpoint list with request and response schemas, and an architecture description.
Do not write all features yet. Include a README skeleton and an AGENTS.md with commands and conventions.
```

---

## Prompt 2: Build the AI core (Day 37)

```text
Implement the AI core for ShopSmart.
Approach: Embeddings for product descriptions; hybrid search with RRF (Day 23); item-item co-occurrence; grounded assistant with tool calls for price and stock (Days 22, 25).
Requirements:
- Every model call goes through one client with timeouts, retries with backoff, a fallback and JSON logging (request id, release, tokens, latency).
- Facts such as prices, stock, availability, order details or numbers must come from the database or tools, never from the model.
- Provide an offline stand-in so tests run without an API key.
Write unit tests for the core logic and an evaluation script that runs the golden set and prints metrics.
Acceptance checks we must pass:
- Recommendations beat the popularity baseline on hit rate@10
- Assistant answers include product ids; prices come from the database
- Guardrail blocks requests for other customers' orders
- Latency p95 under 3 s for the assistant
```

---

## Prompt 3: Front end, guardrails and quality gate (Day 38)

```text
For ShopSmart:
1. Build the React screens for these user stories:
   - As a shopper, I see products recommended for me based on what I viewed and bought.
   - As a shopper, I ask "a quiet kettle for a small Tokyo apartment under 6,000 JPY" and get matching products with reasons.
   - As a shopper, I see "customers also bought" on a product page.
   - As a merchandiser, I see which recommendations are clicked and bought.
   - As support, I trust that the assistant never invents prices or stock.
2. Add input and output guardrails (injection scan, PII redaction, allowlisted tools, human approval for risky actions where relevant).
3. Extend the golden set to at least 20 items (include tricky and unanswerable cases and, where relevant, Japanese inputs) and add a quality gate
   script that exits with code 1 when thresholds fail. Add it to the CI pipeline.
```

---

## Prompt 4: Deploy, observe and prepare the demo (Day 39)

```text
For ShopSmart:
1. Write production Dockerfiles (non-root, health checks) and docker-compose for local runs.
2. Write azure-pipelines.yml: Test, Evaluate (quality gate), Build (images), DeployDev, DeployProd with approval.
3. Add a monitoring view: requests, p95 latency, error rate, cost, and a quality signal (feedback or refusal rate), plus one drift or data quality check.
4. Draft an 8 to 12 slide demo outline: problem, users, live demo script, results with numbers, limits, next steps.
5. Write a runbook for the most likely production incident.
```

---

## Stretch ideas

- A/B test design for two recommenders
- Re-ranking by margin or stock
- Basket completion suggestions
