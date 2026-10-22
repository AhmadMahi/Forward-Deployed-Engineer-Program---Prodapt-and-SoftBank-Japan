# Day 9 Hotel Lab: Node.js and Express

**Total time:** 105 to 120 minutes | **Day:** Thu 05 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. Colab already has Node.js and npm: `%%writefile` saves a file, `!node` runs it.
- The Express cells need `npm install` (internet). The supply chain cells work offline with the sample audit file.
- Postman: use the desktop app or the web version. With Colab, test the API from the notebook script instead.
- Tomorrow is Basics assessment 2 (SQLAlchemy, JavaScript, Node.js, React). Save 15 minutes to revise.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask tomorrow. | `Day09_PostRead_Nodejs_and_Express_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Then run the Express cells, add one route (for example `GET /tasks/stats`) and test it in Postman. | `Day09_Nodejs_and_Express_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (Express routing, CRUD and error handling problems). Stretch problem optional. | `Day09_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: Node.js and npm questions (Sections A and B), then Section C. | `Day09_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 8: Express notification service, Postman collection, npm audit. OpenAI Codex allowed; review every line. | `Day09_App_Build_Prompts.md` |

## Submit

Your **Postman collection export** (the `.postman_collection.json` file).

## Stuck?

- `Cannot find module 'express'`: run `npm install` in the same folder as `package.json`.
- `EADDRINUSE`: another server is using the port. Stop it, or use `PORT=3001 node src/server.js`.
- `req.body` is `undefined`: add `app.use(express.json())` and send the header `Content-Type: application/json`.
- `/tasks/stats` returns 404 "Task not found": register it before `/:id` in the router.
- `npm audit` hangs or fails: it needs internet. Practise with `sample_audit.json` from the notebook.
