# Day 33: App Build Prompts

**Apps of the day:** Resilient LLM Client and Incident Toolkit + LLM Cost and Version Control Center

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 33. A small library and control centre that make any LLM feature in your capstone more reliable, versioned and affordable.

---

## Prompt 1: Resilient client library

```text
You are a senior platform engineer mentoring beginners. Build a Python package "resilient_llm":
- LLMClient with providers configured in YAML (primary, fallback), a timeout per call, retries with exponential backoff and jitter
  for transient errors only (429, 5xx, timeouts), a circuit breaker per provider, an optional response cache for identical prompts,
  and idempotency keys for action-triggering calls.
- The model name comes from LLM_MODEL (see docs/MODEL_GUIDE.md); the key from the environment. Never log the key.
- Every call logs a JSON line: request_id, release, provider, model, latency_ms, tokens_in, tokens_out, status, retries, breaker_state.
- An offline fake provider with a configurable failure rate for tests (OFFLINE=1).
Include pytest tests that prove retries, breaker transitions and fallback behaviour.
```

## Prompt 2: AgentOps release manifests (NEW v4)

```text
Add a module "agentops" to the control centre:
- build_manifest(agent_dir, release) reads the agent's prompts, tool schemas, SKILL.md files, AGENTS.md, MCP server versions
  and model settings, and writes release_manifest.json with a short sha256 hash per part.
- diff_manifests(a, b) lists exactly which parts changed (for example tools.refund_tool).
- A CLI: python -m agentops build | diff | rollback <release>.
Tests: changing one tool description changes only that part's hash.
```

## Prompt 3: Model deprecation runbook (NEW v4)

```text
Add "deprecation.py":
- Input: a deprecation notice (model, retirement date) and all release manifests.
- Output: the affected releases, a golden set run on a candidate model from the approved list (offline stand-in in tests),
  a decision (CANARY or HOLD) using a pass-rate threshold, and a Markdown runbook entry with the six steps:
  watch, inventory, evaluate, canary, switch, record.
Exit with code 1 when any affected release has no passing candidate.
```

## Prompt 4: Cost and latency dashboard

```text
Build a FastAPI + React dashboard for the control centre: cost per feature per day (stacked bars) by release id, p50/p95 latency per
model, top 10 most expensive requests, cache hit rate, breaker state changes, and a budget panel that turns orange at 80% and red at
100% of a daily budget per feature. Prices come from prices.yaml with a comment: PLACEHOLDER prices, replace with the approved price sheet.
```

---

## SmartDesk step 28: Resilient LLM client; cost and version dashboard

```text
SmartDesk step 28. Using the work above:
1. Route every SmartDesk LLM call through resilient_llm with a fallback model and a circuit breaker.
2. Generate release_manifest.json for the SmartDesk agent (prompts, tools, skills, MCP servers, model) and log its release id on every request.
3. Add the cost and version dashboard page to SmartDesk, filtered by release.
4. Run the deprecation drill against SmartDesk's current model and save the runbook entry in docs/.
5. All tests pass with OFFLINE=1. Show me the diff and a three-line summary.
```

**Review checklist before you commit:** no key in code, logs or prompts; prices labelled as placeholders; retries only on transient errors; every manifest part has a hash; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Alert when the error rate exceeds 5% for 5 minutes.
- Add a semantic cache with a strict similarity threshold.
- Export approved conversations as a fine-tuning dataset (PII removed).
