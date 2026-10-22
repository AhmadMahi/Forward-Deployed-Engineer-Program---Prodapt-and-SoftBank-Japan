# Day 10 Hotel Lab: React Basics

**Total time:** 105 to 120 minutes | **Day:** Fri 06 Nov 2026 | **Track:** Basics

## Before you start

- Work in Google Colab in the browser. `show_react()` renders each React app in the cell output. The rendered app loads React from a CDN, so keep the internet on.
- VS Code is optional: create a Vite project (`npm create vite@latest my-app -- --template react`) and paste the code into `src/App.jsx`.
- Monday 9 Nov is the Deepavali holiday. You can split this lab across the long weekend.

## Steps

| # | Time | Task | File |
|---|---|---|---|
| 1 | 15 min | Read the post-read. Note one question to ask on Tuesday. | `Day10_PostRead_React_Basics_Recap_and_Beyond.pdf` |
| 2 | 30 min | Run the Option A cells top to bottom. Render the dashboard with `show_react()`, then add one prop and one state value (for example an agent name prop and a search box). | `Day10_React_Basics_Colab.ipynb` |
| 3 | 30 to 45 min | Warm-up and core problems (components, props, state and event problems). Stretch problem optional. | `Day10_HandsOn_Problem_Statements.pdf` |
| 4 | 15 min | Workbook: JSX and state questions (Sections A to C). | `Day10_Workbook_Interactive.docx` |
| 5 | 20 min (optional) | SmartDesk step 9: React dashboard with the ticket list. OpenAI Codex allowed; review every line. | `Day10_App_Build_Prompts.md` |

## Submit

A **screenshot** of your dashboard and the **component file** you changed (for example `TicketList.jsx`, or the notebook cell).

## Stuck?

- Blank output in Colab: the CDN scripts did not load. Check your connection and run the cell again.
- `Adjacent JSX elements must be wrapped`: return one parent element, or wrap in `<>...</>`.
- The screen does not update: you changed state directly. Use the setter and a new array or object.
- `Each child in a list should have a unique "key" prop`: add `key={ticket.id}` to the element returned from `map`.
