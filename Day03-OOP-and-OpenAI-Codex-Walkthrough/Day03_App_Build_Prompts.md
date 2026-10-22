# Day 3: App Build Prompts

**App of the day:** Mini Library Management System (OOP, command line)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

From today you build with **OpenAI Codex** in VS Code. See `docs/CODEX_GUIDE.md` for setup.

1. Open your project folder in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 2 and 3: classes, inheritance, custom exceptions, modules and JSON files. No web framework yet.

---

## Prompt 1: Build the core with classes

```text
You are a senior Python mentor. Build a command line "Mini Library Management System".
Show me a short plan first and wait for my approval.

Use OOP properly:
- @dataclass Book(id, title, author, is_available=True)
- class Member(id, name, borrowed: list)
- class PremiumMember(Member) that can borrow 5 books instead of 2 (override a max_books method)
- class Library that holds books and members (composition)
Library methods: add_book, add_member, borrow(member_id, book_id), return_book(member_id, book_id), search(keyword).
Custom exceptions: BookNotFound, BookNotAvailable, BorrowLimitReached.
Persist books and members to library.json (save on every change, load on start).
Keep storage in its own class (JsonStorage) so it could be replaced by a database later.
Provide a simple menu loop. Python 3.12, no external libraries.
```

---

## Prompt 2: Tests first

```text
Before changing any code, write pytest tests in tests/test_library.py for:
borrow, return, the borrow limit for Member and PremiumMember, and each custom exception.
Run the tests and show me the results. Then fix only what is needed to make them pass.
Do not add new dependencies other than pytest. Show the diff.
```

---

## Prompt 3: Explain the design

```text
Explain this Library system to a beginner:
- Draw a simple text diagram of the classes and how they relate (inheritance vs composition).
- Point out where each OOP pillar appears in the code.
- Give 5 quiz questions with answers at the end.
```

---

## Prompt 4: Codex on your own Day 2 code

```text
Open my Day 2 file (expense tracker or ticket logger).
1. Explain the function load_tickets (or load_expenses) line by line for a beginner.
2. Plan, then add input validation to one function, with two pytest tests.
Make the smallest change. Do not add dependencies. Show the diff and run the tests.
```

Write a review note: what Codex changed, what you accepted, what you rejected and why, and the tokens used.

---

## SmartDesk step 2: Ticket, Customer and Agent classes; first Codex feature (search)

```text
SmartDesk step 2. Work in the SmartDesk folder. Read AGENTS.md first.
Goal: replace the ticket dicts from step 1 with classes, then add search.
Files you may change: smartdesk/models.py, smartdesk/cli.py, tests/test_models.py, tests/test_search.py.

1. Create Customer(name, plan), Agent(name, team) and Ticket(customer, issue, priority, status="open")
   with assign(agent), close() and __str__. Reject priorities other than low, medium, high with ValueError.
2. Add a TicketNotFound exception and find_ticket(tickets, ticket_id).
3. Keep saving tickets to tickets.json (convert objects to dicts and back).
4. Write tests first for search_tickets(tickets, text): case insensitive, matches customer name
   or issue, returns an empty list when nothing matches.
5. Then implement search_tickets. No eval or exec. No new dependencies.
Show me a plan first. After each step, run pytest and show the diff.
```

**Review note (submit tonight):** one line on what you accepted or changed, plus the tokens used for this task.

**Review checklist before you commit:** no secrets in any file or prompt; tests pass; no new packages you did not ask for; you can explain every line Codex wrote.

---

## Stretch ideas (try on your own)

- Ask Codex to add a due date to each borrowing using the datetime module, with tests.
- Ask Codex to review your code for security problems. Check each suggestion yourself.
- Compare the tokens used for the same task with low and medium reasoning effort.
