# Day 34: App Build Prompts

**App of the day:** Production LLM Gateway (FastAPI, async, streaming, canary)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 34. A gateway that your capstone app and agents call instead of calling providers directly.

---

## Prompt 1: Build the gateway

```text
You are a senior platform engineer mentoring beginners. Build "llm-gateway" with FastAPI:
- Settings from environment (pydantic-settings) for dev, test and prod; secrets required in prod (fail fast); never log secret values.
- POST /v1/chat and POST /v1/chat/stream (server-sent events) with a pipeline: validate (client key header, size limits, input guardrail),
  enrich (optional retrieval hook), generate (provider adapter with timeout, retries and circuit breaker from Day 33), check (output guardrail), respond.
- Client keys stored only as sha256 hashes. A model allow-list from config (docs/MODEL_GUIDE.md). Daily token budgets per team (placeholder numbers).
- Async with a per-provider semaphore; return 429 with Retry-After when a per-client rate limit or budget is exceeded.
- Per-stage timings, tokens and cost in a JSON log line per request, with the release id.
- Canary routing by stable user hash with CANARY_PERCENT, and feature flags from a YAML file.
Offline fake provider for tests (OFFLINE=1). Include a Dockerfile (small base image, non-root user) and docker-compose.
```

## Prompt 2: Short-lived tokens and a stateless MCP endpoint (NEW v4)

```text
Add a token service to the gateway:
- POST /tokens issues an HMAC- or JWT-signed token for an agent with scopes (for example tickets.read, refunds.write) and a 5-minute expiry.
  Only the gateway holds the provider key and the signing key, both read from Key Vault through managed identity in Azure.
- A stateless /mcp endpoint for SmartDesk ticket tools that checks the token and its scope on every call and keeps no session.
Tests: expired token -> 401, missing scope -> 403, valid call -> 200. Note in the README that Day 28 uses the real MCP SDK.
```

## Prompt 3: Versioning and rollback

```text
Add a release registry: each release manifest records prompt id and hash, golden set version, embedding model, chunk settings and index id.
POST /admin/promote/{env}/{release} and POST /admin/rollback/{env}. Promotion warns when the embedding model changes (full re-index needed).
Write the rollback test notes as Markdown: what you changed, what you watched, and the exact rollback command.
```

## Prompt 4: Load test and release on Azure

```text
Write a load test script (asyncio + httpx) that ramps from 10 to 200 concurrent users against the gateway with the fake provider and reports
throughput, p50/p95 latency, error rate and time to first token. Then write Azure Container Apps steps with two revisions for canary traffic
splitting, secrets from Key Vault, and a pipeline stage that rolls back automatically if the canary error rate is more than 2x the baseline.
```

---

## SmartDesk step 29: Production gateway with streaming and canary on Azure

```text
SmartDesk step 29. Using the work above:
1. Every SmartDesk LLM call and every agent tool call goes through the gateway. No provider key anywhere else.
2. The SmartDesk agent gets short-lived scoped tokens; the ticket MCP endpoint is stateless.
3. Streaming answers in the React dashboard via /v1/chat/stream.
4. Deploy to Azure Container Apps (Azure window 2) with 10% canary traffic; record the rollback test.
5. All tests pass with OFFLINE=1. Show me the diff and a three-line summary.
```

**Review checklist before you commit:** no key in code, images, YAML or prompts; tokens expire; budgets and prices labelled as placeholders; rollback tested; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Add a job queue for long summarisation requests with a status endpoint.
- Add shadow mode that logs answers from a candidate model without returning them.
- Add a data retention setting per team (days to keep full prompts).
