# Day 1: App Build Prompts

**App of the day:** Smart Study Planner (command line app in Python)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, use Prompt 3 to ask for an explanation.
4. Do not move to the next prompt until the current version runs without errors.

> Today the app uses **only Day 1 concepts**: variables, data types, `input()`, type casting, `if/elif/else`, `for` and `while` loops. No functions, lists or files yet. We will refactor it on Day 2.

---

## Prompt 1: Build the first version

```text
You are a patient Python mentor helping a beginner on their first day of learning Python.

Build a command line app called "Smart Study Planner" in a single Python file.

Use ONLY these concepts: variables, int/float/str/bool, print(), f-strings, input(),
int() and float() casting, if/elif/else, comparison and logical operators, for loops
with range(), while loops, break and continue.
Do NOT use functions (def), lists, dictionaries, classes, imports or file handling.

Features:
1. Greet the user and ask for their name.
2. Show a menu inside a while loop:
   1) Plan my study hours
   2) Check my quiz grade
   3) Print a revision countdown
   4) Exit
3. Option 1: ask how many hours they can study per day and how many days are left
   before an exam. Print total hours. If total is under 10, print a friendly warning,
   10 to 30 print "Good plan", above 30 print "Excellent commitment".
4. Option 2: ask for marks out of 100. Reject values below 0 or above 100.
   Print grade A (85+), B (70 to 84), C (50 to 69) or "Needs improvement".
5. Option 3: ask for a number of days and use a for loop to print
   "Day X: revise and practise" for each day, counting down to 1.
6. Option 4: print a goodbye message using the user's name and stop the loop.
7. Any other menu choice prints "Invalid option, please try again".

Code style:
- Add short comments above each block explaining what it does, in simple English.
- Use clear variable names in lowercase_with_underscores.
- Keep it under 100 lines.

After the code, show one sample run of the program.
```

---

## Prompt 2: Make it robust

```text
Improve the Smart Study Planner you just wrote, still without using functions,
lists, imports or classes.

1. If the user types something that is not a number where a number is expected,
   do not crash. Use a while loop with try/except ValueError to ask again.
   Add a one line comment explaining what try/except does, since this is new for me.
2. Limit hours per day to between 0.5 and 16. Ask again if it is outside that range.
3. Keep a counter of how many menu actions the user completed and show it on exit.
4. Format all decimal results to 1 decimal place using f-strings.

Show the full updated code, then list exactly what changed in 4 short bullet points.
```

---

## Prompt 3: Explain it like I am new

```text
Explain the Smart Study Planner code line by line for a complete beginner.

For each block:
- Say in one simple sentence what it does.
- Point out which Day 1 concept it uses (variable, casting, condition, loop, break).
- Mention one common mistake a beginner might make in that block.

Finish with 5 short quiz questions about the code (with answers at the end) so I can
test my understanding.
```

---

## Stretch ideas (try on your own)

- Add a fifth menu option that converts study minutes to hours and minutes using `//` and `%`.
- Add a simple "motivation of the day" that changes based on the number of days left.
- Add a password check (3 attempts) before the menu appears.
