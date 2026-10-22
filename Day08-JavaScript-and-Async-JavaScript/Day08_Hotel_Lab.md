# Day 8 Hotel Lab: JavaScript and Async JavaScript

**Total time:** 105 to 120 minutes | **Day:** Wed 04 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. Colab already has Node.js: `%%writefile` saves a JavaScript file and `!node` runs it.
- VS Code is optional: install Node.js LTS, use the Option B lines and run `node file.js` in the terminal.
- No API key is needed tonight. The notebook starts its own small ticket API, so everything runs offline.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day08_PostRead_JavaScript_and_Async_JavaScript_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run the JavaScript cells again and rewrite one callback (or `.then` chain) as `async` and `await`. | `Day08_JavaScript_and_Async_JavaScript_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (arrays, objects, functions and promise problems). Stretch problem optional. | `Day08_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: predict-the-output on async ordering (Section C), then Sections A and B. | `Day08_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 7: JavaScript script that fetches tickets from the API asynchronously. OpenAI Codex allowed; review every line. | `Day08_App_Build_Prompts.md` |

## Submit

Your **script file** (for example `ticket_client.js` or your async rewrite from step 2).

## Stuck?

- `ReferenceError: x is not defined`: check spelling and that you declared it with `const` or `let` before use.
- Output order surprises you: synchronous code runs first, then promise callbacks, then timers.
- `fetch failed` or `ECONNREFUSED`: the API is not running. In the notebook the server starts inside the same script.
- A promise never prints: you forgot `await`, `.then` or to call the async function.
