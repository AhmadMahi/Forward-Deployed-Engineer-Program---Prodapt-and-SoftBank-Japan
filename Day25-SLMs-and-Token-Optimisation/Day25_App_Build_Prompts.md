# Day 25: App Build Prompts

**App of the day:** SmartDesk Cost-Aware Router (small model first, LLM on escalation) with a cost report

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your SmartDesk project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage. Today is about cost, so use the default model at low or medium reasoning effort.

> Uses Days 1 to 25. NEW (v4): a small open-weight model classifies every ticket, the LLM handles only hard cases, and a cost report shows the saving.

---

## Prompt 1: The small-model classifier

```text
You are a senior GenAI engineer mentoring beginners. In the SmartDesk back end, create app/slm_classifier.py.
- classify(text) -> (label, confidence) with labels billing, network, account, other.
- If the environment variable SLM_MODEL_ID is set and transformers is installed, load that model with a
  transformers text-generation pipeline (GPU if available, otherwise CPU) and parse a one-word label.
  An answer that does not parse returns ("other", 0.3).
- Otherwise use a clearly labelled offline keyword stand-in that returns a rough confidence.
- Load the model once, not on every call. Log latency in milliseconds.
Add pytest tests that run with the offline stand-in only.
```

## Prompt 2: The router

```text
Create app/router.py with route(ticket_text, threshold=0.7).
- Call the SLM classifier first. If confidence >= threshold, return its label with route="slm".
- Otherwise call our existing LLM client (app/llm_client.py, model from LLM_MODEL) with route="llm".
- Return label, route, input_tokens, output_tokens and est_cost using app/token_cost.py
  (PLACEHOLDER prices, labelled as placeholders; add an "slm" placeholder price for self-hosted compute).
- Read the threshold from the ROUTER_THRESHOLD environment variable.
Tests: a confident ticket stays on the SLM, an ambiguous ticket escalates, and costs are added for escalations.
```

## Prompt 3: Cache-friendly prompts and output limits

```text
Refactor the LLM reply prompt in SmartDesk so it is cache-friendly:
- Stable parts first (system rules, refund policy, tool list), variable parts last (FAQ chunks, ticket text).
- No timestamps or ticket IDs in the stable part.
- Retrieval top_k = 3 by default, configurable. max_tokens = 150 for replies.
- Log cached input tokens from the API usage report when they are present (0 offline).
Show me the old and new prompt token counts for one sample ticket.
```

## Prompt 4: Cost report endpoint

```text
Add GET /reports/cost to the SmartDesk API.
- Read token_log.csv. Return calls, tokens and est_cost per route (slm, llm) for today and the last 7 days.
- Return cost per 1,000 tickets and the escalation rate.
- Include "prices": "placeholder" in the response so nobody mistakes the numbers for real prices.
Add a "Cost" card to the React dashboard that shows cost per 1,000 tickets and the escalation rate.
```

---

## SmartDesk step 21: SLM for classification, LLM for complex answers, cost report

```text
SmartDesk step 21. Using the work above, make sure:
1. Every ticket is classified by the small model first; only low-confidence tickets or complex replies go to the LLM.
2. Every call (SLM and LLM) is logged with route, tokens and estimated cost (placeholder prices, labelled).
3. A script reports cost per 1,000 tickets before optimisation (all LLM) and after (caching, trimming, routing),
   and writes cost_report.md with an SLM vs LLM comparison table (accuracy, latency, cost).
4. All tests run with OFFLINE=1 and no key, and no model download.
5. AGENTS.md lists the new environment variables (SLM_MODEL_ID, ROUTER_THRESHOLD) and says "never put secrets in prompts".
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** no key in any file or prompt; every price is labelled a placeholder; the model ID and licence are noted in the README; tests pass offline; you can explain every line Codex wrote; you checked today's Codex token usage.
