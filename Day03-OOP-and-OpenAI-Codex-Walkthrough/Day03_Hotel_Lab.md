# Day 3 Hotel Lab: OOP and OpenAI Codex Walkthrough

**Total time:** 105 to 120 minutes | **Day:** Wed 28 Oct 2026 | **Track:** Basics

## Before you start

- Steps 1 to 4 run in Google Colab in the browser. VS Code is optional for them (use the Option B cells).
- Step 5 needs VS Code with the OpenAI Codex extension, signed in with the program API key. Approved models only.
- Never paste your API key into a notebook, a prompt or a chat. Paste it only into the Codex sign-in box.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read, including the self-study topics (SOLID, decorators, generators). | `Day03_PostRead_OOP_and_OpenAI_Codex_Walkthrough_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom, then add one subclass and one custom exception to the class demo. | `Day03_OOP_and_OpenAI_Codex_Walkthrough_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core sets (class design, inheritance and exception handling problems). Stretch set optional. | `Day03_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: write-the-code section on classes (Section D). | `Day03_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step: use Codex in VS Code to add 'search tickets'; review the diff; note tokens used. | `Day03_App_Build_Prompts.md` |

## Submit

Class file + one-line Codex review note.

## Stuck?

- `TypeError: __init__() missing 1 required positional argument`: check the arguments you pass when creating the object.
- `AttributeError: ... has no attribute`: did you forget `self.` when storing the value in `__init__`?
- Codex does not appear in VS Code: reload the window, then check the extension is installed and enabled.
- Codex asks to run a command you do not understand: say no and ask it to explain first.
- Codex changed more files than you asked: reject the diff and ask for the smallest change to one file.
- You cannot find your token usage: ask your trainer where the program usage page is. Note an estimate for now.
