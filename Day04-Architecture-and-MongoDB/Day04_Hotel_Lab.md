# Day 4 Hotel Lab: Architecture and MongoDB

**Total time:** 105 to 120 minutes | **Day:** Thu 29 Oct 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. The notebook uses **mongomock**, an in-memory MongoDB, so nothing needs installing.
- VS Code with a real MongoDB or a free Atlas cluster is optional (use the Option B cell). Keep the connection string in `MONGO_URI`, never in code.
- OpenAI Codex is not needed tonight.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. | `Day04_PostRead_Architecture_and_MongoDB_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then insert 20 sample tickets with mongomock and run find, update and delete queries; plot a Matplotlib chart. | `Day04_Architecture_and_MongoDB_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core sets (CRUD queries, filters and index choices). Stretch set optional. | `Day04_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: MongoDB query and data-modelling questions. | `Day04_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step: store SmartDesk tickets in MongoDB; chart tickets by priority. | `Day04_App_Build_Prompts.md` |

## Submit

Query script + chart image.

## Stuck?

- `ModuleNotFoundError: mongomock`: run the setup cell again, then **Runtime > Restart session**.
- Your data vanished: mongomock lives in memory. Re-run the setup and insert cells after a restart.
- `DuplicateKeyError`: a unique index blocked a repeated value. That is the index doing its job.
- `$mul` not supported: mongomock does not support it. Loop over `find()` and use `$set`, as in the notebook.
- Chart does not appear: make sure `plt.show()` is the last line of the cell.
