# Day 32: App Build Prompts

**App of the day:** LLM Cost and Version Control Center

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 32. A small internal platform for tracking prompts, releases, cost and latency for every LLM feature, useful in your capstone.

---

## Prompt 1: Registry and manifests

```text
You are a senior LLMOps engineer. Build a FastAPI service "llm-control-center" with SQLite:
- prompt registry: create versions (id, text, sha, note, author, created_at), list, diff two versions, mark one as active per feature
- release manifests: bundle prompt version, model name and version, temperature, retrieval settings, golden set version, eval report path; promote and roll back
- every LLM call made through POST /complete is logged with request_id, feature, release, model, tokens in and out, latency, cost (prices from prices.yaml, clearly marked as configuration)
Offline fake model for tests.
```

---

## Prompt 2: Cost and latency dashboard

```text
Build a React dashboard for the control center: cost per feature per day (stacked bars), p50/p95 latency per model, top 10 most expensive requests,
cache hit rate, and a budget panel that turns orange at 80% and red at 100% of a daily budget per feature.
```

---

## Prompt 3: Optimisation experiments

```text
Add an experiments module: run the golden set with (a) current release, (b) shorter prompt, (c) small model, (d) routed small/large,
(e) exact cache enabled; report quality, cost and p95 latency for each in one table and recommend a configuration with reasons.
```

---

## Stretch ideas (try on your own)

- Add a semantic cache with a strict similarity threshold.
- Prepare a fine-tuning dataset export from approved conversations.
- Alert when tokens per request jump by more than 50% day over day.
