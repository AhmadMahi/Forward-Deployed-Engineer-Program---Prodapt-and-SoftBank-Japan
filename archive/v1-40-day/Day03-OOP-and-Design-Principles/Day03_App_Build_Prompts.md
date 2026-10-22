# Day 3: App Build Prompts

**App of the day:** Mini Library Management System (OOP, command line)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 3: classes, inheritance, custom exceptions, decorators, generators and JSON files. No web framework yet.

---

## Prompt 1: Build the core with classes

```text
You are a senior Python mentor. Build a command line "Mini Library Management System".

Use OOP properly:
- @dataclass Book(id, title, author, is_available=True)
- class Member(id, name, borrowed: list)
- class PremiumMember(Member) that can borrow 5 books instead of 2 (override a max_books method)
- class Library that holds books and members (composition)

Library methods: add_book, add_member, borrow(member_id, book_id), return_book(member_id, book_id),
search(keyword), available_books() as a GENERATOR using yield.

Custom exceptions: BookNotFound, BookNotAvailable, BorrowLimitReached.
Add a @log_action decorator that prints the method name and arguments every time a Library method runs.

Persist books and members to library.json (save on every change, load on start).
Provide a simple menu loop. Follow the single responsibility principle: keep storage
in its own class (JsonStorage) so it could be replaced by a database later.
Include clear comments. Then show a sample run.
```

---

## Prompt 2: Apply SOLID and add tests

```text
Refactor the Library system:
1. Create an abstract base class Storage with load() and save(); JsonStorage implements it.
   Library receives a Storage object in its constructor (dependency inversion).
2. Add a FineCalculator class: 5 per day late for Member, 0 for PremiumMember (open/closed).
3. Write 6 simple tests using plain assert statements (no frameworks) covering borrow,
   return, limits and exceptions.
Show the full code and explain which SOLID principle each change applies.
```

---

## Prompt 3: Explain the design

```text
Explain this Library system to a beginner:
- Draw a simple text diagram of the classes and how they relate (inheritance vs composition).
- For each SOLID principle, point to where it appears in the code.
- Give 5 quiz questions with answers at the end.
```

---

## Stretch ideas (try on your own)

- Use NumPy to report the average number of borrowings per member.
- Add a due date to each borrowing using the datetime module.
- Add a reservations queue for books that are already borrowed.
