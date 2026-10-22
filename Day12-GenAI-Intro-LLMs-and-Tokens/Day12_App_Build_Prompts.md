# Day 12: App Build Prompts

**App of the day:** SmartDesk Ticket Summariser with a token log (FastAPI + OpenAI API)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open your SmartDesk project in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 12. Your first LLM feature: a ticket summariser behind your own API, with every call logged in tokens and estimated cost.

---

## Prompt 1: The LLM client

```text
You are a senior GenAI engineer mentoring beginners. In the SmartDesk back end, create app/llm_client.py.
- Read OPENAI_API_KEY from the environment (a git-ignored .env file is fine). Never hard-code or print it.
- Read the model name from LLM_MODEL with a default taken from docs/MODEL_GUIDE.md.
- If OFFLINE=1 or there is no key, use a clearly labelled offline stand-in that returns "[offline demo] ..." so tests run without a key.
- Function summarise(text) -> (summary, usage) where usage has input_tokens and output_tokens.
- Timeouts of 20 seconds and one retry on rate-limit errors.
Add pytest tests that run in offline mode only.
```

## Prompt 2: Token counting and cost

```text
Create app/token_cost.py.
- count_tokens(text) using tiktoken (o200k_base), falling back to len(text) / 4.
- PRICE_PER_1M dict with input, cached_input and output keys. Add a comment: PLACEHOLDER prices, replace with the approved price sheet.
- cost(input_t, output_t, cached_t=0, reasoning_t=0) where reasoning tokens are billed as output.
Tests: a known short sentence, an empty string, and a cost calculation checked by hand.
```

## Prompt 3: The summarise endpoint and token log

```text
Add POST /tickets/{id}/summary to the SmartDesk FastAPI app.
- Load the ticket, call summarise(), save the summary on the ticket.
- Append a row to token_log.csv: timestamp, ticket_id, model, input_tokens, output_tokens, est_cost.
- Return 404 for a missing ticket, 422 for an empty body, 503 with a friendly message if the LLM call fails.
- GET /usage/today returns total calls, total tokens and total estimated cost for today.
TestClient tests for each status code, in offline mode.
```

## Prompt 4: Show it in the dashboard

```text
In the SmartDesk React dashboard, add a "Summarise" button on each ticket.
- It calls our own back end, never the OpenAI API directly. No key in the front end.
- Show loading, error and success states. Show the summary under the ticket title.
- Add a small "Today's usage" card that reads GET /usage/today.
```

---

## SmartDesk step 11: First LLM call with token logging

```text
SmartDesk step 11. Using the work above, make sure:
1. Every LLM call goes through app/llm_client.py.
2. Every call is logged to token_log.csv with an estimated cost (placeholder prices, labelled).
3. The app and all tests run with OFFLINE=1 and no key.
4. AGENTS.md lists the test command and says "never put secrets in prompts".
Then show me the diff and a three-line summary of what changed.
```

**Review checklist before you commit:** the key is not in any file or prompt; prices are labelled as placeholders; tests pass offline; you can explain every line Codex wrote.
