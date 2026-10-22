# Day 2 Hotel Lab: Python Basics, Functions and Files

**Total time:** 90 to 120 minutes | **Day:** Tue 27 Oct 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. VS Code is optional (use the Option B cells).
- OpenAI Codex is not needed today. Type the code yourself.
- Cells that would wait for typing (`input()`) use fixed values in Option A, so the notebook runs top to bottom.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read, including the self-study topics (comprehensions, lambda, map and filter). | `Day02_PostRead_Python_Basics_Functions_and_Files_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then change the inputs in each demo cell and predict the output before running. | `Day02_Python_Basics_Functions_and_Files_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core sets (loops, conditions, functions and list or dictionary problems). Stretch set optional. | `Day02_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: predict-the-output and fill-the-blank sections. | `Day02_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step: SmartDesk CLI: add, list and save tickets to JSON. | `Day02_App_Build_Prompts.md` |

## Submit

Workbook answers + CLI script.

## Stuck?

- `IndentationError`: use 4 spaces under every `if`, `for`, `while` and `def`.
- `ValueError` on `int(...)`: the text is not a number. Check what you passed in.
- `FileNotFoundError`: run the setup cell first so the notebook is in its `day2` folder.
- `KeyError`: use `.get("key", default)` when a key might be missing.
- Your tickets disappear: make sure `save_tickets()` runs after every change.
