# Day 33: App Build Prompts

**App of the day:** Production LLM Gateway (FastAPI, async, streaming, canary)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 33. A gateway that your capstone app can call instead of calling providers directly.

---

## Prompt 1: Build the gateway

```text
You are a senior platform engineer. Build "llm-gateway" with FastAPI:
- settings from environment (pydantic-settings) for dev, test, prod; secrets required in prod (fail fast); never log secret values
- POST /v1/chat and POST /v1/chat/stream (server-sent events) with a pipeline: validate (auth via API key header, size limits, input guardrail),
  enrich (optional retrieval hook), generate (provider adapter with timeout, retries, circuit breaker from Day 31), check (output guardrail), respond
- async with a per-provider semaphore; return 429 with Retry-After when a per-client rate limit is exceeded
- per-stage timings, tokens and cost in a JSON log line per request
- canary routing by stable user hash with CANARY_PERCENT, and feature flags from a YAML file
Offline fake provider for tests. Include a Dockerfile and docker-compose.
```

---

## Prompt 2: Load test and tune

```text
Write a load test script (asyncio + httpx) that ramps from 10 to 200 concurrent users against the gateway with the fake provider,
reports throughput, p50/p95 latency, error rate and time to first token, and recommends semaphore and replica settings.
```

---

## Prompt 3: Deploy and release

```text
Write Azure deployment steps for the gateway on Container Apps with secrets from Key Vault, two revisions for canary traffic splitting,
and a pipeline stage that runs smoke tests and an automated rollback if the canary's error rate exceeds the baseline by 2x.
```

---

## Stretch ideas (try on your own)

- Add a job queue for long summarisation requests with a status endpoint.
- Add per-team budgets enforced at the gateway.
- Add shadow mode that logs answers from a candidate model without returning them.
