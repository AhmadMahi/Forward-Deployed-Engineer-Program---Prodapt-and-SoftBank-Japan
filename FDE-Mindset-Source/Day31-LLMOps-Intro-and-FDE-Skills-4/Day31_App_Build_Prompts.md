# Day 31: App Build Prompts

**App of the day:** Resilient LLM Client and Incident Toolkit

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 31. A small library and dashboard that makes any LLM feature in your capstone more reliable and easier to support.

---

## Prompt 1: Resilient client library

```text
You are a senior platform engineer. Build a Python package "resilient_llm":
- LLMClient with providers configured in YAML (primary, fallback), timeouts per call, retries with exponential backoff and jitter
  for transient errors only (429, 5xx, timeouts), a circuit breaker per provider, an optional response cache for identical prompts,
  and idempotency keys for action-triggering calls
- every call logs a JSON line: request_id, provider, model, latency_ms, tokens_in, tokens_out, status, retries, breaker_state
- an offline fake provider with a configurable failure rate for tests
Include unit tests that prove retries, breaker transitions and fallback behaviour.
```

---

## Prompt 2: Incident dashboard

```text
Build a FastAPI + React mini dashboard that reads the JSON logs and shows: error rate per hour by status code,
p50/p95 latency, tokens per request per day, breaker state changes, and a button that generates an escalation draft
(what, impact, evidence, actions, ask, next update) from the selected time window.
```

---

## Prompt 3: Runbooks

```text
Write three runbooks in Markdown for an LLM support assistant: (1) rate-limit storm, (2) provider outage, (3) quality regression after
a model update. Each: symptoms, how to confirm, immediate actions, communication template, recovery checks, follow-up actions.
```

---

## Stretch ideas (try on your own)

- Alert when the error rate exceeds 5% for 5 minutes.
- Add a status page endpoint.
- Write a blameless review template generator.
