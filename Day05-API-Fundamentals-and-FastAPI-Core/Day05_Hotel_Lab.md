# Day 5 Hotel Lab: API Fundamentals and FastAPI Core

**Total time:** 105 to 120 minutes | **Day:** Fri 30 Oct 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- `TestClient` calls your API inside the notebook, so no server is needed. The two cells that need internet or a running server are optional.
- Today was an assessment day. Keep tonight light and focus on the core problems.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Monday. | `Day05_PostRead_API_Fundamentals_and_FastAPI_Core_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then call each endpoint from the notebook client and add one new GET endpoint. | `Day05_API_Fundamentals_and_FastAPI_Core_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (REST design, status codes, path vs query parameters). Stretch set optional. | `Day05_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: HTTP and FastAPI short answers. | `Day05_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 4: FastAPI ticket API with Pydantic models. OpenAI Codex allowed; review every line. | `Day05_App_Build_Prompts.md` |

## Submit

Your **notebook link** plus your **endpoint list** (method, path, success status code, error codes).

## Stuck?

- `ModuleNotFoundError: main`: run the `%%writefile main.py` cell first, then the cell that imports it.
- A new route is never reached: FastAPI matches routes in order. Put `/quotes/random` above `/quotes/{qid}`.
- 422 when you expected 200: read the `detail` in the response. It says which field failed and why.
- Your change does not show: re-run the `%%writefile` cell, then the `importlib.reload(...)` cell.
