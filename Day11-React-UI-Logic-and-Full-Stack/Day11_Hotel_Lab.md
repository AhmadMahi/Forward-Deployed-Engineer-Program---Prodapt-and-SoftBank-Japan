# Day 11 Hotel Lab: React UI Logic and Full Stack

**Total time:** 105 to 120 minutes | **Day:** Tue 10 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. `show_react()` renders React in the cell output (needs internet for the React CDN). The FastAPI cells run with `TestClient`, no server needed.
- VS Code is optional: run `uvicorn fullstack:app --reload` and open http://127.0.0.1:8000, or use a separate Vite app on port 5173.
- The secret-scanning cells use a **fake** key built at runtime. Never paste a real key into a notebook or a front-end file.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day11_PostRead_React_UI_Logic_and_Full_Stack_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then add loading, error and empty states to the fetch demo (try Retry until you see all four). | `Day11_React_UI_Logic_and_Full_Stack_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (conditional rendering and API integration problems). Stretch problem optional. | `Day11_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: front-end and back-end flow questions (Sections A to C). | `Day11_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 10: full-stack create, update and close tickets. OpenAI Codex allowed; review every line. | `Day11_App_Build_Prompts.md` |

## Submit

A **short screen recording or screenshots** showing a ticket being created, updated and closed, plus the scanner output showing no secrets in your build.

## Stuck?

- `CORS error` in the browser console: add the front end's exact origin (scheme, host and port) to `allow_origins`.
- A stray `0` appears on screen: change `{count && ...}` to `{count > 0 && ...}`.
- The list does not update after a PATCH: replace the item from the server reply with `prev.map(...)`.
- `422` from FastAPI: the body does not match the Pydantic model. Read the `detail` field in the response.
- The scanner finds a key: revoke it first if it was ever real, then move the call to the server.
