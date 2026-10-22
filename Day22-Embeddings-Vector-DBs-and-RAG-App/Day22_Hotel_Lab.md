# Day 22 Hotel Lab: Embeddings, Vector DBs and the RAG App

**Total time:** 105 to 120 minutes | **Day:** Wed 25 Nov 2026 | **Track:** GenAI

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- If you have no API key, GenAI cells run in **offline demo mode**. Offline scores show how the code works, not real model quality.
- Never paste your API key into a notebook cell, a prompt or a chat. Use Colab Secrets or a git-ignored `.env` file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day22_PostRead_Embeddings_Vector_DBs_and_RAG_App_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then compare keyword, vector and hybrid search on ten questions; add re-ranking. | `Day22_Embeddings_Vector_DBs_and_RAG_App_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (embeddings, similarity and vector search). Stretch problem optional. | `Day22_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: embeddings and vector DB questions (Sections A to C). | `Day22_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 19: hybrid search and re-ranking. OpenAI Codex allowed; review every line. | `Day22_App_Build_Prompts.md` |

## Submit

**Hit-rate table for the ten questions:** hit@3 (and MRR if you can) for keyword, vector, hybrid and hybrid + re-rank.

## Stuck?

- `No module named faiss` or `rank_bm25`: run the install cell again, then **Runtime > Restart session**.
- Every method scores 1.0 offline: the sample questions share words with the answers. Add paraphrased questions to see differences.
- ANN recall looks low: random vectors are a hard case. Raise `efSearch` or `nprobe` and watch recall and time.
- Re-ranking made MRR worse: offline re-ranking only counts shared words. Try it online, or improve the overlap score.
