# Day 33 Hotel Lab: LLMOps

**Total time:** 105 to 120 minutes | **Day:** Thu 10 Dec 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day33_PostRead_LLMOps_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then simulate provider failures and check retries; compare the cost of two model choices (prices are placeholders). | `Day33_LLMOps_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (resilience, versioning and cost). Stretch problem optional. | `Day33_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: LLMOps questions (technical sections). | `Day33_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 28: resilient client and cost dashboard. OpenAI Codex allowed; review every line. | `Day33_App_Build_Prompts.md` |

## Submit

Your **cost comparison**: the cost of serving the FAQ bot with two model choices, with the placeholder prices labelled as placeholders, plus one sentence on which you would choose and why.

## Stuck?

- `ModuleNotFoundError`: run the install cell again, then **Runtime > Restart session**.
- Success rates differ slightly from the sample: the provider is random. Keep the seed cells as they are to match.
- The circuit breaker never closes: the cool-down is tiny on purpose; requests must arrive over time (the `time.sleep` line).
- Costs look small: they are in placeholder units. Compare shares and ratios, not absolute numbers.
