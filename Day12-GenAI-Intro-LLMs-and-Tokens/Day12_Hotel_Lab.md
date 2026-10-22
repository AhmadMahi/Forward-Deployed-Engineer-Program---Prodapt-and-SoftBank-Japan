# Day 12 Hotel Lab: GenAI Intro, LLMs and Tokens

**Total time:** 105 to 120 minutes | **Day:** Wed 11 Nov 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- No API key? Every cell runs in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day12_PostRead_GenAI_Intro_LLMs_and_Tokens_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Make your first LLM call (or use offline demo mode). Print token counts for three prompts of your own. | `Day12_GenAI_Intro_LLMs_and_Tokens_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (GenAI concepts and token counting). Stretch problem optional. | `Day12_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: LLM and tokens questions (Sections A to C). | `Day12_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 11: ticket summariser with a token log. OpenAI Codex allowed; review every line. | `Day12_App_Build_Prompts.md` |

## Submit

Your **token log**: a table or CSV with prompt, input tokens, output tokens and estimated cost (placeholder prices, labelled as placeholders).

## Stuck?

- `ModuleNotFoundError`: run the install cell again, then **Runtime > Restart session**.
- Mode says OFFLINE but you added a key: check the Secret is named exactly `OPENAI_API_KEY` and notebook access is switched on.
- `tiktoken` cannot download its encoding: the helper falls back to about 4 characters per token. That is fine for tonight.
- Costs look tiny: they are per request. Multiply by requests per day to see the real picture.
