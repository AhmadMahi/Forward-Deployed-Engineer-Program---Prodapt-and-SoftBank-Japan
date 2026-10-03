# Day 2: App Build Prompts

**App of the day:** Personal Expense Tracker (command line, saves to JSON)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses only Day 1 and Day 2 concepts: functions, lists, dicts, loops, conditions, and CSV or JSON files. No classes or external libraries yet.

---

## Prompt 1: Build the first version

```text
You are a patient Python mentor helping a learner on Day 2 of a Python course.

Build a command line "Personal Expense Tracker" in a single Python file.

Allowed concepts: functions (def, parameters, return), lists, tuples, sets, dicts,
list comprehensions, loops, conditions, f-strings, and the json and csv modules.
Do NOT use classes, decorators, external libraries or databases.

Design:
- Each expense is a dict: {"id": int, "date": "YYYY-MM-DD", "category": str, "amount": float, "note": str}
- All expenses are stored in a list and saved to expenses.json.

Write these functions, each with a one line docstring:
load_expenses(), save_expenses(expenses), add_expense(expenses), list_expenses(expenses),
total_by_category(expenses) -> dict, delete_expense(expenses, expense_id), export_csv(expenses)

Main menu (inside a while loop):
1) Add  2) List  3) Totals by category  4) Delete  5) Export to CSV  6) Exit

Rules:
- Load existing data on start, save after every change.
- Show amounts with 2 decimal places.
- Keep it under 150 lines, with simple comments.

After the code, show a sample run that adds two expenses and prints totals.
```

---

## Prompt 2: Add validation and insights

```text
Improve the Expense Tracker without adding classes or libraries.

1. Validate the date format (YYYY-MM-DD) and that amount is a positive number. Ask again if invalid.
2. Restrict category to a fixed set: {"Food", "Travel", "Bills", "Shopping", "Other"}.
3. Add a menu option "Monthly summary" that asks for a month (YYYY-MM) and prints
   total spent and the top category for that month.
4. Add "Search by keyword" that searches the note field, case insensitive.

Show the full updated code, then list what changed in short bullet points.
```

---

## Prompt 3: Explain it and quiz me

```text
Explain the Expense Tracker code for a beginner.
For each function: what it does, what it takes in, what it returns, and which Day 2 concept it uses.
Then give me 5 short questions about the code, with answers at the end.
```

---

## Stretch ideas (try on your own)

- Add a monthly budget per category saved in budget.json and warn when a category goes over budget.
- Import expenses from a bank style CSV file.
- Print a simple text bar chart of spending per category using the * character.
