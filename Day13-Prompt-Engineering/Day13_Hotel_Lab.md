# Day 13 Hotel Lab: Prompt Engineering

**Total time:** 105 to 120 minutes | **Day:** Thu 12 Nov 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Monday. | `Day13_PostRead_Prompt_Engineering_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then rewrite one prompt three ways (zero shot, few shot, structured output) and compare outputs and tokens. | `Day13_Prompt_Engineering_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (prompt engineering from warm-up to stretch). Stretch set optional. | `Day13_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: prompt components and technique matching. | `Day13_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 12: category classifier with JSON Schema output. OpenAI Codex allowed; review every line. | `Day13_App_Build_Prompts.md` |

## Submit

Your **prompt comparison table**: one row per version (zero shot, few shot, structured output) with the output, prompt tokens and one line on what changed.

## Stuck?

- `ValidationError`: print the raw reply. The fallback should set `needs_review=True`, not crash.
- Accuracy is the same for zero shot and few shot offline: expected. The offline stand-in is a keyword rule, not a model.
- Mode says OFFLINE but you added a key: check the Secret is named exactly `OPENAI_API_KEY` and notebook access is on.
- The injection ticket changed your label: check the ticket is inside `<ticket>` tags and the category is an allowed list.
