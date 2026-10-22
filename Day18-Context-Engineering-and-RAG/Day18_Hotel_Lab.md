# Day 18 Hotel Lab: Context Engineering and RAG

**Total time:** 105 to 120 minutes | **Day:** Thu 19 Nov 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Day 20. | `Day18_PostRead_Context_Engineering_and_RAG_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then change chunk size and overlap; compare retrieved chunks and citations. | `Day18_Context_Engineering_and_RAG_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (chunking, retrieval and context budget). Stretch problem optional. | `Day18_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: context engineering questions (Sections A to C). | `Day18_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 16: RAG over the telecom FAQ with citations. OpenAI Codex allowed; review every line. | `Day18_App_Build_Prompts.md` |

## Submit

**Three Q&A pairs with citations** (question, answer, cited chunk ids). Include at least one "I don't know" case.

## Stuck?

- `ModuleNotFoundError`: run the install cell again, then **Runtime > Restart session**.
- Every answer is "I don't know": offline embeddings only match shared words. Reword the question to use words from the FAQ, or lower the threshold slightly.
- Chunk ids change after you change chunk size: that is expected. Re-check your citations after every change.
- Compaction never triggers: lower `BUDGET` or add more turns.
