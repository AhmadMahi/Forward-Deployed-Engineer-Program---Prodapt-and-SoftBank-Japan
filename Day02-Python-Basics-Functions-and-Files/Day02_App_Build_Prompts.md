# Day 2: App Build Prompts

**Apps of the day:** Smart Study Planner (Python CLI) and Personal Expense Tracker (CLI, saves to JSON)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

OpenAI Codex is **not required today**. You set it up tomorrow (Day 3). Today, type the code yourself in Google Colab: that is how the basics stick.

1. Read each prompt as a specification. Build it yourself, one feature at a time.
2. Run your code in Google Colab (or VS Code if it is already set up).
3. Read every line you write. If something is unclear, ask your trainer or a partner.
4. Do not move to the next prompt until the current version runs without errors.
5. From Day 3 you can paste these same prompts into OpenAI Codex in VS Code and compare its answer with yours. Review every line it writes.

> Uses only Day 2 concepts: variables, conditions, loops, functions, lists, dicts, and CSV or JSON files. No classes or external libraries yet.

---

## Prompt 1: Smart Study Planner

```text
You are a patient Python mentor helping a beginner on Day 2 of a Python course.

Build a command line app called "Smart Study Planner" in a single Python file.
Use only: variables, int/float/str/bool, print(), f-strings, input(), int() and float() casting,
if/elif/else, for loops with range(), while loops, break and continue, and small functions (def).
Do NOT use classes, imports or file handling.

Features (a menu inside a while loop):
1) Plan my study hours: ask hours per day and days left before an exam. Print total hours.
   Under 10 prints a friendly warning, 10 to 30 prints "Good plan", above 30 "Excellent commitment".
2) Check my quiz grade: marks out of 100. Reject values below 0 or above 100.
   A (85+), B (70 to 84), C (50 to 69), otherwise "Needs improvement".
3) Print a revision countdown: for each day, "Day X: revise and practise", counting down to 1.
4) Exit with a goodbye message using the user's name.
Any other choice prints "Invalid option, please try again".

Put each option in its own function. Use clear lowercase_with_underscores names and short comments.
Keep it under 100 lines. After the code, show one sample run.
```

---

## Prompt 2: Personal Expense Tracker

```text
Build a command line "Personal Expense Tracker" in a single Python file.
Allowed: functions (def, parameters, return), lists, tuples, sets, dicts, list comprehensions,
loops, conditions, f-strings, and the json and csv modules. No classes, decorators or libraries.

- Each expense is a dict: {"id": int, "date": "YYYY-MM-DD", "category": str, "amount": float, "note": str}
- All expenses are stored in a list and saved to expenses.json.
Functions (one line docstring each): load_expenses(), save_expenses(expenses), add_expense(expenses),
list_expenses(expenses), total_by_category(expenses) -> dict, delete_expense(expenses, expense_id),
export_csv(expenses)
Menu: 1) Add 2) List 3) Totals by category 4) Delete 5) Export to CSV 6) Exit
Load on start, save after every change, show amounts with 2 decimal places, keep it under 150 lines.
After the code, show a sample run that adds two expenses and prints totals.
```

---

## Prompt 3: Add validation and insights

```text
Improve the Expense Tracker without adding classes or libraries.
1. Validate the date format (YYYY-MM-DD) and that amount is a positive number. Ask again if invalid.
2. Restrict category to a fixed set: {"Food", "Travel", "Bills", "Shopping", "Other"}.
3. Add "Monthly summary": ask for YYYY-MM and print the total and the top category for that month.
4. Add "Search by keyword" on the note field, case insensitive.
List what changed in short bullet points.
```

---

## SmartDesk step 1: CLI ticket logger with functions; tickets saved as JSON

```text
SmartDesk is a customer support platform for a telecom operator. This is step 1 of 30.

Build smartdesk.py, a command line ticket logger. Use only Day 2 concepts.
- Each ticket is a dict: {"id": int, "customer": str, "issue": str,
  "priority": "low" | "medium" | "high", "status": "open" | "closed"}.
- Functions with one line docstrings: load_tickets(), save_tickets(tickets),
  add_ticket(tickets, customer, issue, priority="medium"), list_tickets(tickets, status=None),
  close_ticket(tickets, ticket_id).
- Tickets are saved to tickets.json after every change and loaded on start, so they survive a restart.
- Menu inside a while loop: 1) Add 2) List 3) List open only 4) Close 5) Exit.
- Reject an empty customer or issue and any priority outside low, medium, high.
After the code, show a sample run that adds two tickets, closes one and lists open tickets.
```

**Check before you finish:** tickets.json exists and reloads after a restart; bad input does not crash the program; every function does one job.

---

## Stretch ideas (try on your own)

- Add a "Search tickets" option by customer name. (Tomorrow you will build this with OpenAI Codex and compare.)
- Count tickets per priority and print a simple text bar chart using the * character.
- Export open tickets to open_tickets.csv.
