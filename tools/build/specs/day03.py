"""Day 03 spec. OOP + OpenAI Codex Walkthrough (half day).
Source: archive/v1-40-day/Day03 condensed to the morning. Afternoon is the new OpenAI Codex half day (brief 7.1).
SOLID, decorators and generators move to the post-read as self-study.
"""
DAY = 3
FOLDER = "Day03-OOP-and-OpenAI-Codex-Walkthrough"
SLUG = "OOP_and_OpenAI_Codex_Walkthrough"
TITLE = "OOP and OpenAI Codex Walkthrough"
SUBTITLE = "Classes, inheritance and exceptions in the morning; structured AI-assisted coding with OpenAI Codex in the afternoon"
DATE = "Wed 28 Oct 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 4: architecture, charts and MongoDB."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 2"),
        ("Session 1 (1.5 hrs)", "Classes, objects, inheritance, overriding"),
        ("Session 2 (1.5 hrs)", "Exceptions, modules, dependency hygiene"),
        ("Session 3 (1.5 hrs)", "OpenAI Codex in VS Code. NEW (v4)"),
        ("Session 4 (1.5 hrs)", "Codex rules, models, security, cost. NEW (v4)"),
        ("SmartDesk step 2", "Classes plus your first Codex feature"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Model with classes", "Create classes with __init__, methods, inheritance and overriding."),
        ("Fail safely", "Use try, except, else, finally, custom exceptions and pinned dependencies."),
        ("Use Codex well", "Explain, generate and test code with Codex, reviewing every diff."),
        ("Stay safe and cheap", "Pick the right model, check AI code for security, watch token use."),
    ]),

    dict(type="section", title="Classes and objects", sub="Session 1 (1.5 hrs): bundling data and behaviour"),
    dict(type="compare", title="Blueprint and building", left=dict(title="Class (blueprint)", bullets=[
        "Describes what something has and does", "Written once", "Example: Ticket with priority and close()",
    ]), right=dict(title="Object (building)", bullets=[
        "A real thing made from the blueprint", "Create as many as you need", "Example: t = Ticket(\"Mei\", \"No signal\")",
    ])),
    dict(type="bullets_code", title="Your first class", bullets=[
        "class defines the blueprint",
        "__init__ runs when an object is created",
        "self means \"this object\"",
        "Methods are functions inside a class",
    ], code='''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acc = BankAccount("Hana", 500)
print(acc.deposit(250))   # 750'''),
    dict(type="cards", title="The four pillars of OOP", items=[
        ("Encapsulation", "Keep data and the methods that change it together."),
        ("Abstraction", "Show what an object does, hide how it does it."),
        ("Inheritance", "Build new classes on top of existing ones."),
        ("Polymorphism", "Same method name, different behaviour per class."),
    ]),
    dict(type="bullets_code", title="Inheritance and overriding", bullets=[
        "Child class inherits everything from the parent",
        "super() calls the parent's version",
        "Override a method to change behaviour",
        "Polymorphism: same call, different result",
    ], code='''class Account:
    def fee(self):
        return 100

class Premium(Account):
    def fee(self):
        return super().fee() // 2

for a in [Account(), Premium()]:
    print(type(a).__name__, a.fee())

Output:
Account 100
Premium 50'''),
    dict(type="bullets_code", title="__str__ and properties", bullets=[
        "__str__ controls how print() shows an object",
        "@property makes a method read like an attribute",
        "A leading underscore signals \"internal\"",
        "Validate data in one place",
    ], code='''class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price_with_tax(self):
        return round(self._price * 1.18, 2)

    def __str__(self):
        return f"{self.name}: {self._price}"

p = Product("Mouse", 500)
print(p, p.price_with_tax)'''),

    dict(type="section", title="Exceptions, modules and dependencies", sub="Session 2 (1.5 hrs): expect the unexpected"),
    dict(type="flow", title="The try statement", items=[
        ("try", "Code that might fail"),
        ("except", "Runs only if a matching error happens"),
        ("else", "Runs only if no error happened"),
        ("finally", "Always runs, for clean up"),
    ], note="Catch specific errors like ValueError, never a bare except."),
    dict(type="bullets_code", title="Raising your own errors", bullets=[
        "Catch the specific error you expect",
        "raise signals a problem yourself",
        "Custom exceptions name your business rules",
        "Error messages should help the user",
    ], code='''class TicketNotFound(Exception):
    pass

def find(tickets, ticket_id):
    for t in tickets:
        if t.id == ticket_id:
            return t
    raise TicketNotFound(f"No ticket {ticket_id}")

try:
    find([], 42)
except TicketNotFound as e:
    print("Error:", e)'''),
    dict(type="bullets_code", title="Modules and packages", bullets=[
        "A module is any .py file",
        "import brings its code into yours",
        "A package is a folder of modules",
        "if __name__ == \"__main__\" runs only when executed directly",
    ], code='''# file: smartdesk/models.py
class Ticket: ...

# file: smartdesk/__init__.py   (makes a package)

# file: app.py
from smartdesk.models import Ticket
from math import sqrt'''),
    dict(type="cards", title="Dependency hygiene", new=True, items=[
        ("Virtual environments", "One venv per project, so libraries do not clash."),
        ("Pinned requirements", "requests==2.32.3, not requests. Same versions everywhere."),
        ("pip-audit", "Checks your packages against known vulnerabilities."),
        ("Why it matters", "AI tools happily add packages. You decide which ones stay."),
    ]),
    dict(type="code", title="Dependency hygiene in five commands", new=True, code='''# 1. Create the environment
python -m venv .venv
# 2. Activate it (Windows: .venv\\Scripts\\activate)
source .venv/bin/activate
# 3. Install a pinned version
pip install requests==2.32.3
# 4. Record exact versions
pip freeze > requirements.txt
# 5. Check for known vulnerabilities
pip install pip-audit && pip-audit -r requirements.txt''',
         note="Commit requirements.txt. Never commit .venv/ or .env (add them to .gitignore)."),

    dict(type="section", title="OpenAI Codex in VS Code", sub="Session 3 (1.5 hrs): your AI pair programmer", new=True),
    dict(type="cards", title="What OpenAI Codex is", new=True, items=[
        ("A coding agent", "Reads your files, proposes changes, can run commands and tests."),
        ("Inside VS Code", "Through the OpenAI Codex extension, next to your code."),
        ("Signed in with the program key", "Uses the program's OpenAI API key and approved models only."),
        ("You stay in charge", "Codex proposes. You review, run the tests and decide."),
    ]),
    dict(type="flow", title="Install and sign in", new=True, items=[
        ("Install", "VS Code, Python, Git"),
        ("Extension", "Add OpenAI Codex from the VS Code Marketplace"),
        ("Sign in", "Choose API key; paste the program key"),
        ("Check", "Pick the approved model; open your project folder"),
    ], note="Paste the key only into the sign-in box. Never into code, prompts, chat or AGENTS.md."),
    dict(type="cards", title="Four first tasks", new=True, items=[
        ("Explain code", "\"Explain this function line by line for a beginner.\""),
        ("Generate a function", "\"Write is_valid_priority(p) with three tests.\""),
        ("Run it", "Ask Codex to run the tests, or run them yourself."),
        ("Review every change", "Read the diff. Accept only what you can explain."),
    ]),
    dict(type="flow", title="Structured AI-assisted coding", new=True, items=[
        ("Describe", "Goal, inputs, outputs, rules"),
        ("Plan", "Ask for a plan; approve it first"),
        ("Small steps", "One function or file at a time"),
        ("Test", "Run tests after every step"),
    ], note="Small, reviewed steps beat one big generated program."),
    dict(type="compare", title="Vibe coding vs structured coding", new=True, left=dict(title="Vibe coding", bullets=[
        "\"Build me a ticket app\"", "Accept whatever comes back", "No tests, no plan",
        "Fine for a throwaway demo, risky for clients",
    ]), right=dict(title="Structured coding", bullets=[
        "Clear task with constraints", "Plan, then small steps", "Tests first, then code",
        "Every diff reviewed by a human",
    ]), note="As an FDE you ship to customers. Use structured coding."),
    dict(type="bullets_code", title="AGENTS.md basics", new=True, bullets=[
        "A plain Markdown file at the repo root",
        "Codex reads it before working",
        "Build, test and style commands",
        "Folders not to touch; security rules",
        "An open standard (Agentic AI Foundation)",
    ], code='''# AGENTS.md
## Commands
- Run tests: pytest -q
- Lint: ruff check .

## Style
- Python 3.12, type hints, short functions.

## Do not touch
- data/, .env, .venv/

## Rules
- Never put secrets in prompts or code.
- Add a test for every new function.'''),
    dict(type="bullets_code", title="Review the diff: spot the problems", new=True, bullets=[
        "Codex wrote search_tickets()",
        "It runs. Is it right?",
        "Case sensitive search misses \"mei\"",
        "eval() on user input is a security hole",
        "No test proves either behaviour",
    ], code='''- def search_tickets(tickets, text):
-     return []
+ def search_tickets(tickets, text):
+     results = []
+     for t in tickets:
+         if text in t.customer:
+             results.append(t)
+     if eval(text + " == ''"):
+         return tickets
+     return results'''),

    dict(type="section", title="Using Codex responsibly", sub="Session 4 (1.5 hrs): rules, models, security and cost", new=True),
    dict(type="compare", title="Codex do's and don'ts", new=True, left=dict(title="Do", bullets=[
        "Plan first, then small steps", "Include only the relevant files", "Write or generate tests first",
        "Read every diff", "Keep AGENTS.md updated", "Check daily token usage",
    ]), right=dict(title="Don't", bullets=[
        "Paste keys, customer data or credentials", "Use full-access or bypass modes",
        "Ask to \"improve everything\"", "Use a top-tier model for routine edits", "Merge AI code without tests and review",
    ])),
    dict(type="table", title="Which model for what purpose", new=True, header=["Task", "Model", "Effort"], rows=[
        ["Explain code, small edits, docstrings", "Lighter model, for example GPT-6 Luna (if approved)", "Low"],
        ["Most feature work", "Default Codex model: GPT-6.1 Sol", "Medium"],
        ["Hard debugging, large migrations", "GPT-6.1 Sol at high effort; GPT-6 Astra only with trainer approval", "High"],
        ["Security review and patches", "GPT-6.1 Sol, human verifies every fix", "Medium"],
        ["Retired models (for example GPT-5.5)", "Do not use", "n/a"],
    ], note="Model names checked 21 Oct 2026. Confirm against the approved model list. See docs/MODEL_GUIDE.md."),
    dict(type="cards", title="Reasoning effort", new=True, items=[
        ("Low", "Fast and cheap. Explanations, renames, docstrings."),
        ("Medium", "The default. Most features and tests."),
        ("High", "Slow and costly. Only when medium fails on a hard problem."),
    ], note="Higher effort uses more reasoning tokens, which are billed as output."),
    dict(type="cards", title="Security of AI-generated code", new=True, items=[
        ("Common mistakes", "eval(), shell=True, SQL built with f-strings, hard-coded keys."),
        ("Made-up packages", "Check every new dependency exists and is the one you meant."),
        ("Scan it", "pip-audit today; bandit on Day 7; security gates in CI on Day 20."),
        ("Sandbox", "Workspace-write with approvals. Read-only when exploring."),
    ]),
    dict(type="cards", title="Token cost of Codex use", new=True, items=[
        ("What you pay for", "Files Codex reads, your prompt, its answer and reasoning."),
        ("Keep it small", "Small tasks, few files, no \"paste the whole repo\"."),
        ("Daily usage check", "Look at your usage at the end of each day. Stop runaway tasks."),
        ("Budget", "Each learner has a budget on the program key. Approved models only."),
    ]),
    dict(type="cards", title="SmartDesk step 2", items=[
        ("Classes", "Ticket, Customer and Agent classes replace yesterday's dicts."),
        ("Exception", "TicketNotFound for a missing ticket id."),
        ("First Codex feature", "Ask Codex for search_tickets(text). Plan, review, test."),
        ("Review note", "One line: what you accepted, what you changed, tokens used."),
    ]),
    dict(type="callout", title="Hands-on time", text="Morning: build the Library classes with a custom exception. "
         "Afternoon: use Codex on your own Day 2 code, then add 'search tickets' to SmartDesk.",
         sub="Write your review note and the tokens used. Ask for help before you accept code you cannot explain.",
         greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("OOP", "Classes bundle data and behaviour. Inheritance reuses it."),
        ("Exceptions and deps", "Catch specific errors. Pin and audit your packages."),
        ("Codex workflow", "Describe, plan, small steps, test. Review every diff."),
        ("Safety and cost", "Approved model, right effort, no secrets, daily usage check."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day03_Hotel_Lab.md: classes, Codex search feature, review note."),
        ("Self-study", "SOLID, decorators and generators in the post-read."),
        ("Pre-read", "Skim the Day 4 pre-read on how apps talk and store data."),
    ]),
]

PREREAD = dict(title="Blueprints, Good Habits and Your AI Pair Programmer",
               lede="A light read before Day 3. About 20 minutes. Includes the OpenAI Codex setup steps and the "
                    "do's and don'ts card.", sections=[
    dict(h="Why read this?", paras=[
        "As programs grow, they need structure, the same way a growing company needs teams and roles. In the morning "
        "you learn object-oriented programming (OOP). In the afternoon you start working with **OpenAI Codex**, an AI "
        "coding agent inside VS Code. Please do the setup steps below before class."]),
    dict(h="1. Blueprints and buildings", paras=[
        "An architect draws one blueprint and a builder uses it to build many houses. In programming the blueprint is "
        "a **class** and each house is an **object**."],
        table=[["Real world", "Things it has (data)", "Things it does (actions)"],
               ["Support ticket", "customer, issue, priority", "assign, close"],
               ["Bank account", "owner, balance", "deposit, withdraw"],
               ["Online order", "items, total, status", "add item, pay, cancel"]]),
    dict(h="2. Families of things and planning for problems", paras=[
        "A premium customer and a standard customer share most features but differ in a few rules. Describing the "
        "shared parts once is **inheritance**. A good restaurant has a plan for when an ingredient runs out; programs "
        "use **exception handling** to notice a problem and keep running."]),
    dict(h="3. Tidy toolboxes", new=True, paras=[
        "Every project needs its own set of libraries at known versions, like a labelled toolbox. A **virtual "
        "environment** keeps each project's tools separate. A **pinned requirements** file records exact versions. "
        "**pip-audit** checks those tools for known security problems."]),
    dict(h="4. Your AI pair programmer", new=True, paras=[
        "OpenAI Codex reads your code, explains it, writes new code and can run tests. It is fast but not always "
        "right. Think of it as a keen new colleague: helpful, but you review everything before it reaches a "
        "customer."]),
    dict(h="5. Codex setup checklist (do before class)", new=True, bullets=[
        "Install VS Code, Python 3.12 or newer and Git (see shared/Laptop_Setup_Guide.pdf).",
        "In VS Code, open Extensions and install **OpenAI Codex**.",
        "Have the program's OpenAI API key ready. Your trainer shares it securely. Paste it only into the Codex "
        "sign-in box when asked to sign in with an API key.",
        "Choose the approved default model. See docs/MODEL_GUIDE.md and docs/CODEX_GUIDE.md.",
        "Open a project folder (for example your Day 2 work) and ask Codex: \"Explain this file.\""]),
    dict(h="6. Do's and don'ts card", new=True, table=[
        ["Do", "Don't"],
        ["Plan first, then small steps", "Paste API keys, customer data or credentials"],
        ["Include only the relevant files", "Use full-access or bypass modes"],
        ["Write or generate tests first", "Ask to \"improve everything\""],
        ["Read every diff", "Use a top-tier model for routine edits"],
        ["Check your daily token usage", "Merge AI code without tests and review"],
    ], box="**Key idea:** the model proposes, the engineer decides."),
    dict(h="7. Think about these before class", bullets=[
        "Pick an app you use daily. What \"things\" does it manage, and what can each thing do?",
        "What could go wrong if you accepted AI-written code without reading it?",
        "Why might a project break when it uses a newer version of a library than yesterday?"],
        after=["Monozukuri (ものづくり): the craft of making things well"]),
])

POSTREAD = dict(title="OOP and OpenAI Codex: Recap and Beyond",
                lede="What we covered today, plus today's self-study topics: SOLID, decorators and generators.",
                sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["class and object", "A class is a blueprint; objects are instances. __init__ sets up; self is the object."],
        ["Inheritance", "class Child(Parent). super() calls the parent. Override to change behaviour."],
        ["Exceptions", "try / except / else / finally. Catch specific errors. raise for your own rules."],
        ["Modules", "Any .py file can be imported. A package is a folder of modules."],
        ["Dependency hygiene (NEW v4)", "One venv per project, pinned requirements, pip-audit."],
        ["Codex workflow (NEW v4)", "Describe, plan, small steps, test. Review every diff."],
        ["AGENTS.md (NEW v4)", "Commands, style, folders not to touch, security rules."],
        ["Models and effort (NEW v4)", "Light for routine, default for features, top tier only with approval."],
        ["Security and cost (NEW v4)", "Scan AI code, never paste secrets, check daily token usage."],
    ]),
    dict(h="Part B: Self-study topics", sub="1. SOLID in plain English", table=[
        ["Letter", "Principle", "In one line"],
        ["S", "Single responsibility", "One class, one job"],
        ["O", "Open / closed", "Extend with new code, do not edit old code"],
        ["L", "Liskov substitution", "Child classes can stand in for parents"],
        ["I", "Interface segregation", "Small focused interfaces, not giant ones"],
        ["D", "Dependency inversion", "Depend on abstractions, not concrete classes"],
    ]),
    dict(sub="2. Decorators: wrap a function", paras=[
        "A decorator takes a function and returns a new one that adds behaviour, such as logging or timing. FastAPI "
        "routes on Day 5 are decorators. Use functools.wraps to keep the original name."],
        code='''from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b'''),
    dict(sub="3. Generators: values on demand", paras=[
        "yield returns one value and pauses. The next call resumes. Generators use almost no memory, which is ideal "
        "for reading big log files line by line."],
        code='''def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))          # [3, 2, 1]
squares = (i * i for i in range(10**6))
print(next(squares), next(squares))   # 0 1'''),
    dict(h="Part C: Going beyond today", sub="1. Dataclasses", paras=[
        "@dataclass writes __init__, __repr__ and __eq__ for you. Pydantic models (Day 5) follow the same idea with "
        "validation added."]),
    dict(sub="2. Lockfiles and hashes", paras=[
        "Tools such as pip-tools or uv produce lockfiles with exact versions and hashes for every dependency, "
        "including indirect ones. You will meet npm lockfiles on Day 9."]),
    dict(sub="3. Layered AGENTS.md", paras=[
        "Large repos can have an AGENTS.md in a sub-folder with extra rules for that folder. Codex reads the nearest "
        "one as well as the root file. Keep each one short and specific."]),
    dict(h="Part D: Check yourself", bullets=[
        "What is the difference between a class and an object?",
        "Why should you avoid a bare except:?",
        "Why pin dependency versions, and what does pip-audit check?",
        "Name the four steps of structured AI-assisted coding.",
        "Give two things you must never paste into a Codex prompt."]),
    dict(h="Part E: Practice ideas for tonight", bullets=[
        "Model a Shape base class with Circle and Rectangle subclasses that each implement area().",
        "Write a @timer decorator and a Fibonacci generator.",
        "Write an AGENTS.md for your SmartDesk folder using shared/templates/AGENTS_learner_template.md."],
        after=["**Coming up on Day 4:** client server architecture, charts with Matplotlib, and storing SmartDesk "
               "tickets in MongoDB.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Eight problems. Problems 1 to 4 run in the Day 3 notebook. Problems 5 to 8 use OpenAI Codex in "
                    "VS Code; write a short review note for each.", problems=[
    dict(title="Student Class", level="Warm-up", concepts="class, __init__, methods, __str__",
         text="Create a Student class with name and a list of marks. Add add_mark(m) and average(). Add __str__ so "
              "print(student) shows name and average.",
         sample='s = Student("Aiko")\ns.add_mark(80); s.add_mark(90)\nprint(s)   # Aiko (avg 85.0)',
         hints=["Start marks as an empty list inside __init__."]),
    dict(title="Customers and Polymorphism", level="Easy", concepts="inheritance, overriding, super()",
         text="Create a Customer class with monthly_fee() returning 500. Create PremiumCustomer (half price, using "
              "super()) and StaffCustomer (free). Loop over a list of customers and print each fee.",
         sample="Customer         500\nPremiumCustomer  250\nStaffCustomer    0",
         hints=["type(obj).__name__ gives the class name."]),
    dict(title="Bank Account with Rules", level="Medium", concepts="encapsulation, custom exceptions, finally",
         text="Build BankAccount with deposit and withdraw. Raise InsufficientFunds when withdrawing too much and "
              "ValueError for negative amounts. Keep a transaction history list.",
         sample="acc.withdraw(5000)\nInsufficientFunds: Balance 1200, requested 5000",
         hints=["class InsufficientFunds(Exception): pass"]),
    dict(title="Pin and Check Your Dependencies", level="Easy", concepts="venv, requirements.txt, pip-audit", new=True,
         text="Given a requirements list, write check_pinned(lines) that returns the packages that are not pinned "
              "with ==. Then, in VS Code, create a venv for your SmartDesk folder, pin your packages and run pip-audit.",
         sample='check_pinned(["requests==2.32.3", "pandas", "numpy>=1.26"])\n-> [\'pandas\', \'numpy>=1.26\']\n\n$ pip-audit -r requirements.txt\nNo known vulnerabilities found',
         hints=["A line is pinned only if it contains ==.", "Add .venv/ to .gitignore."]),
    dict(title="Codex on Your Own Day 2 Code", level="Medium", concepts="Codex explain, generate, review", new=True,
         text="Open your Day 2 expense tracker or ticket logger in VS Code. Ask Codex to (1) explain one function, "
              "(2) add input validation to one function with a test. Read the diff before accepting.",
         bullets=["Write a review note: what Codex changed, what you accepted, what you rejected and why.",
                  "Record the tokens used from your usage page or the Codex panel."],
         sample="Review note: Codex added a date check and one test. Accepted the check. Rejected a new\n"
                "dependency (python-dateutil) because datetime is enough. Tokens used: about 3,400.",
         hints=["Ask Codex for a plan first.", "Include only the file you are changing."]),
    dict(title="SmartDesk: Search Tickets with Codex", level="Medium", concepts="structured AI-assisted coding", new=True,
         text="SmartDesk step 2. Convert tickets to Ticket, Customer and Agent classes. Then use Codex to add "
              "search_tickets(tickets, text): case insensitive, matches customer name or issue, returns a list.",
         bullets=["Describe the task, ask for a plan, approve it, then let Codex build it in small steps.",
                  "Ask Codex to write three tests first. Run them. Review the diff.",
                  "Write a one-line review note and the tokens used."],
         sample='search_tickets(tickets, "SIGNAL") -> [#1 Mei: No signal at home]\nsearch_tickets(tickets, "zzz")    -> []\n3 passed',
         hints=["Use text.lower() in both places.", "Reject any use of eval() in the generated code."]),
    dict(title="Spot the Security Problems", level="Challenging", concepts="security of AI-generated code", new=True,
         text="The notebook contains three functions \"written by an AI tool\". Find every security problem (for "
              "example eval, shell=True, a hard-coded key, SQL built with f-strings), explain the risk and rewrite "
              "each function safely.",
         sample="1. eval(user_text)        -> code injection. Use int() or a lookup table.\n"
                "2. API_KEY = \"...\"         -> secret in code. Read from the environment.\n"
                "3. f\"SELECT ... {name}\"    -> SQL injection. Use parameters.",
         hints=["Run the notebook's simple scanner first, then read the code yourself."]),
    dict(title="Codex Cost Estimate", level="Stretch", concepts="tokens, model choice, daily budget", new=True,
         text="Use the notebook's token estimator to estimate tokens for three Codex tasks of different sizes. Pick "
              "a model tier and reasoning effort for each, and estimate the daily cost with the placeholder prices.",
         sample="explain one function  : light,   low    ->  2,100 tokens\n"
                "add search + tests    : default, medium ->  9,800 tokens\n"
                "refactor 6 files      : default, high   -> 41,000 tokens",
         hints=["Prices are placeholders. Label them.", "Fewer files in context means fewer tokens."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "A ________ is a blueprint and an ________ is a real thing made from it.",
        "The method that runs when an object is created is ________.",
        "To call the parent class version of a method, use ________().",
        "The block that always runs, error or not, is ________.",
        "To signal an error yourself, use the keyword ________.",
        "A ________ environment keeps one project's packages separate from another's.",
        "The tool that checks installed packages for known vulnerabilities is ________.",
        "The Markdown file that tells Codex your build, test and style rules is ________.",
        "The four steps of structured AI-assisted coding are describe, plan, small steps and ________.",
        "Higher reasoning effort uses more ________ tokens.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain inheritance using a real-world example.",
        "Why should you catch specific exceptions instead of using a bare except?",
        "What is the difference between vibe coding and structured coding? When is each acceptable?",
        "List three things you check in a Codex diff before you accept it.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'class A:\n    def hi(self):\n        return "A"\nclass B(A):\n    def hi(self):\n        return "B" + super().hi()\nprint(B().hi())',
        'try:\n    x = int("abc")\nexcept ValueError:\n    print("bad")\nelse:\n    print("good")\nfinally:\n    print("end")',
        'lines = ["fastapi==0.115.0", "pandas", "numpy>=1.26"]\nprint([l for l in lines if "==" not in l])',
    ]),
    dict(title="Section D: Write the code: classes", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a Ticket class with customer, issue, priority and status='open', a close() method and __str__."),
        dict(q="Write a custom exception TicketNotFound and a function find_ticket(tickets, ticket_id) that raises it."),
        dict(q="Write PremiumCustomer(Customer) that overrides monthly_fee() using super()."),
        dict(q="Write the Codex prompt you would use to add search_tickets(), following describe, plan, small steps, test."),
    ]),
    dict(title="Section E: Reflection", kind="reflection", items=[
        "The idea that clicked best for me today:",
        "One thing Codex did well, and one thing I had to fix:",
        "Tokens I used today with Codex, and how I could use fewer:",
    ]),
])

NOTEBOOK = dict(subtitle="Classes, inheritance, exceptions and dependency hygiene, then structured coding with OpenAI Codex",
                cells=[
    ("md", "## 1. Setup"),
    ("code", '''# ===== Option A: Google Colab (active) =====
import sys, platform
print("Python", platform.python_version(), "| Colab:", "google.colab" in sys.modules)

# ===== Option B: VS Code / local =====
# Work inside a virtual environment (see section 7):
#   python -m venv .venv  ->  source .venv/bin/activate  (Windows: .venv\\Scripts\\activate)
#   pip install -r requirements.txt'''),
    ("md", "# Session 1: Classes and objects\n## 2. Your first class"),
    ("code", '''class BankAccount:
    bank_name = "Sakura Bank"          # class attribute, shared

    def __init__(self, owner, balance=0):
        self.owner = owner              # instance attributes
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def __str__(self):
        return f"{self.owner}: {self.balance}"

a = BankAccount("Hana", 500)
b = BankAccount("Ravi")
a.deposit(250)
print(a, "|", b, "|", BankAccount.bank_name)'''),
    ("md", "## 3. Inheritance, overriding and polymorphism"),
    ("code", '''class Account:
    def __init__(self, owner):
        self.owner = owner
    def fee(self):
        return 100

class Premium(Account):
    def fee(self):
        return super().fee() // 2

class Student(Account):
    def fee(self):
        return 0

for acc in [Account("A"), Premium("B"), Student("C")]:
    print(f"{type(acc).__name__:<8} fee = {acc.fee()}")'''),
    ("md", "## 4. Properties and encapsulation"),
    ("code", '''class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price          # goes through the setter below

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def price_with_tax(self):
        return round(self._price * 1.18, 2)

p = Product("Mouse", 500)
print(p.price, p.price_with_tax)
try:
    p.price = -10
except ValueError as e:
    print("Blocked:", e)'''),
    ("md", "### TODO 1: Add a `Corporate(Account)` subclass with a fee of 300 and add it to the loop above."),
    ("code", "# TODO: write your code here"),
    ("md", "# Session 2: Exceptions, modules and dependencies\n## 5. Exception handling"),
    ("code", '''def to_int(text):
    try:
        value = int(text)
    except ValueError:
        print(f"'{text}' is not a number")
        return None
    else:
        print("Converted OK")
        return value
    finally:
        print("Finished checking", repr(text))

print(to_int("42"))
print(to_int("abc"))'''),
    ("code", '''class InsufficientFunds(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds(f"Balance {balance}, requested {amount}")
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFunds as e:
    print("Error:", e)'''),
    ("md", "### TODO 2: Create a custom exception `NegativeAmount` and raise it from `withdraw` when `amount < 0`."),
    ("code", "# TODO: write your code here"),
    ("md", "## 6. Modules\nWe write a small module file, then import it."),
    ("code", '''%%writefile pricing.py
GST = 0.18

def with_tax(amount):
    return round(amount * (1 + GST), 2)

if __name__ == "__main__":
    print("Running pricing.py directly")'''),
    ("code", '''import pricing
from math import sqrt
print(pricing.with_tax(100), pricing.GST, sqrt(49))'''),
    ("md", "## 7. NEW (v4): Dependency hygiene\n"
           "**Virtual environment** (run in a VS Code terminal, not in Colab):\n"
           "```\npython -m venv .venv\nsource .venv/bin/activate        # Windows: .venv\\Scripts\\activate\n"
           "pip install requests==2.32.3\npip freeze > requirements.txt\n```\n"
           "Commit `requirements.txt`. Add `.venv/` and `.env` to `.gitignore`.\n\n"
           "Below: a small checker for unpinned requirements, then `pip-audit` (needs internet)."),
    ("code", '''requirements = """\\
fastapi==0.115.0
pydantic==2.9.2
requests
numpy>=1.26
# comments are ignored
"""

def check_pinned(lines):
    """Return requirement lines that are not pinned with ==."""
    out = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#") and "==" not in line:
            out.append(line)
    return out

with open("requirements.txt", "w") as f:
    f.write(requirements)
print("Not pinned:", check_pinned(requirements.splitlines()))'''),
    ("code", '''# ===== Option A: Google Colab (needs internet) =====
!pip install -q pip-audit
!pip-audit -r requirements.txt --progress-spinner off || echo "Fix the findings above, or pin the missing versions first"

# ===== Option B: VS Code terminal, inside your venv =====
# pip install pip-audit
# pip-audit -r requirements.txt''', ["skip-offline-check"]),
    ("md", "# Session 3: NEW (v4): OpenAI Codex in VS Code\n"
           "Codex runs in VS Code, not in Colab. Follow these steps on your laptop (details in `docs/CODEX_GUIDE.md`):\n"
           "1. Install VS Code, Python 3.12 or newer and Git.\n"
           "2. Extensions: search for **OpenAI Codex** and install it.\n"
           "3. Sign in with the program's **API key** (paste it only into the sign-in box).\n"
           "4. Select the approved default model (`docs/MODEL_GUIDE.md`). Keep the sandbox on workspace-write with approvals.\n"
           "5. Open your Day 2 folder and ask: *\"Explain `add_ticket` line by line for a beginner.\"*\n"
           "6. Ask: *\"Write `is_valid_priority(p)` that accepts low, medium, high, with three pytest tests. Show a plan first.\"*\n"
           "7. Read the diff. Run the tests. Accept only code you can explain.\n\n"
           "The cells below practise the skills you need around Codex: reviewing diffs, scanning for risky code and "
           "estimating tokens."),
    ("md", "## 8. NEW (v4): SmartDesk classes (step 2)"),
    ("code", '''class TicketNotFound(Exception):
    pass

class Customer:
    def __init__(self, name, plan="standard"):
        self.name, self.plan = name, plan

class Agent:
    def __init__(self, name, team="general"):
        self.name, self.team = name, team

class Ticket:
    PRIORITIES = ("low", "medium", "high")
    _next_id = 1

    def __init__(self, customer, issue, priority="medium"):
        if priority not in self.PRIORITIES:
            raise ValueError(f"priority must be one of {self.PRIORITIES}")
        self.id = Ticket._next_id
        Ticket._next_id += 1
        self.customer, self.issue, self.priority = customer, issue, priority
        self.status, self.agent = "open", None

    def assign(self, agent):
        self.agent = agent

    def close(self):
        self.status = "closed"

    def __str__(self):
        return f"#{self.id} [{self.priority}] {self.customer.name}: {self.issue} ({self.status})"

def find_ticket(tickets, ticket_id):
    for t in tickets:
        if t.id == ticket_id:
            return t
    raise TicketNotFound(f"No ticket {ticket_id}")

tickets = [Ticket(Customer("Mei"), "No signal at home", "high"),
           Ticket(Customer("Ravi", "premium"), "Charged twice this month"),
           Ticket(Customer("Aiko"), "Cannot log in to the app", "low")]
tickets[0].assign(Agent("Kenji", "network"))
for t in tickets:
    print(t)
try:
    find_ticket(tickets, 99)
except TicketNotFound as e:
    print("Error:", e)'''),
    ("md", "## 9. NEW (v4): Review the diff\nImagine Codex proposed this `search_tickets`. It runs. Is it right? "
           "We show the diff, then run tests that a careful reviewer would write."),
    ("code", '''import difflib
before = """def search_tickets(tickets, text):
    return []
"""
proposed = """def search_tickets(tickets, text):
    results = []
    for t in tickets:
        if text in t.customer.name:
            results.append(t)
    return results
"""
print("".join(difflib.unified_diff(before.splitlines(True), proposed.splitlines(True),
                                   fromfile="before.py", tofile="codex_proposal.py")))

ns = {}
exec(proposed, ns)        # load the proposal so we can test it (never do this with untrusted input)
search = ns["search_tickets"]
checks = {
    "finds Mei":            len(search(tickets, "Mei")) == 1,
    "case insensitive":     len(search(tickets, "mei")) == 1,
    "searches the issue":   len(search(tickets, "signal")) == 1,
    "no match is empty":    search(tickets, "zzz") == [],
}
for name, ok in checks.items():
    print("PASS" if ok else "FAIL", name)'''),
    ("md", "**Your fix** (this is what you would ask Codex for, then review again):"),
    ("code", '''def search_tickets(tickets, text):
    """Case insensitive search on customer name and issue."""
    q = text.lower().strip()
    return [t for t in tickets if q in t.customer.name.lower() or q in t.issue.lower()]

assert len(search_tickets(tickets, "mei")) == 1
assert len(search_tickets(tickets, "SIGNAL")) == 1
assert search_tickets(tickets, "zzz") == []
print("3 passed")'''),
    ("md", "## 10. NEW (v4): Structured prompt template\nDescribe, plan, small steps, test. Fill it in and paste it into Codex."),
    ("code", '''def codex_prompt(goal, files, rules, tests):
    return f"""Goal: {goal}
Files you may change: {", ".join(files)}
Rules: {"; ".join(rules)}
Tests first: {"; ".join(tests)}
Step 1: show me a short plan and wait for my approval.
Step 2: make the smallest change, then run the tests and show the diff."""

print(codex_prompt(
    goal="Add search_tickets(tickets, text) to SmartDesk",
    files=["smartdesk/models.py", "tests/test_search.py"],
    rules=["case insensitive", "match customer name or issue", "no new dependencies", "no eval or exec"],
    tests=["finds by name", "finds by issue", "empty list when no match"]))'''),
    ("md", "## 11. NEW (v4): AGENTS.md basics\nA starter file for your SmartDesk repo (template: `shared/templates/AGENTS_learner_template.md`)."),
    ("code", '''%%writefile AGENTS.md
# AGENTS.md: SmartDesk (learner repo)

## Commands
- Run tests: pytest -q
- Run the app: python smartdesk.py

## Style
- Python 3.12, type hints, short functions with docstrings.
- British spelling in user messages.

## Do not touch
- .env, .venv/, data/

## Rules
- Never put secrets, API keys or customer data in prompts or code.
- Add or update a test for every change.
- No new dependencies without asking; pin versions in requirements.txt.'''),
    ("md", "# Session 4: NEW (v4): Using Codex responsibly\n## 12. Security of AI-generated code\n"
           "Three functions below look like they came from an AI tool. A tiny scanner flags risky patterns. "
           "Real tools (bandit, pip-audit, secret scanning) come on Day 7 and Day 20."),
    ("code", '''import re
ai_code = {
    "calc.py":  'def calc(user_text):\\n    return eval(user_text)\\n',
    "client.py": 'API_KEY = "sk-live-not-a-real-key"\\nheaders = {"Authorization": API_KEY}\\n',
    "repo.py":  'def find(cur, name):\\n    cur.execute(f"SELECT * FROM tickets WHERE customer = \\'{name}\\'")\\n',
}
RULES = {
    r"\\beval\\(|\\bexec\\(": "code injection: never eval user input",
    r"shell\\s*=\\s*True": "shell injection: pass a list of arguments",
    r"(API_KEY|SECRET|PASSWORD)\\s*=\\s*[\\"']": "secret in code: read it from the environment",
    r"execute\\(f[\\"']": "SQL injection: use query parameters",
}
for fname, src in ai_code.items():
    for pattern, why in RULES.items():
        if re.search(pattern, src):
            print(f"{fname:<10} {why}")'''),
    ("md", "### TODO 3: Rewrite the three functions safely and re-run the scanner until it prints nothing."),
    ("code", "# TODO: write your code here"),
    ("md", "## 13. NEW (v4): Which model, which effort?\nFrom `docs/MODEL_GUIDE.md`. Names checked 21 Oct 2026; confirm "
           "against the approved model list before class."),
    ("code", '''GUIDE = [   # (keywords, model, effort)
    (("explain", "docstring", "rename", "small"), "lighter model (for example GPT-6 Luna, if approved)", "low"),
    (("debug", "migrate", "design", "large"),     "GPT-6.1 Sol at high effort (GPT-6 Astra only with trainer approval)", "high"),
    (("security", "patch", "vulnerab"),           "GPT-6.1 Sol, human verifies every fix", "medium"),
]
def pick(task):
    t = task.lower()
    for words, model, effort in GUIDE:
        if any(w in t for w in words):
            return model, effort
    return "GPT-6.1 Sol (default Codex model)", "medium"

for task in ["Explain this function", "Add search with tests", "Debug a failing migration",
             "Review a security patch"]:
    model, effort = pick(task)
    print(f"{task:<28} -> {effort:<6} {model}")'''),
    ("md", "## 14. NEW (v4): Token cost of Codex use\nCodex reads files and writes answers in tokens. Fewer files in "
           "context means fewer tokens. Prices are **placeholders**."),
    ("code", '''def estimate_tokens(text):
    try:
        import tiktoken
        return len(tiktoken.get_encoding("o200k_base").encode(text))
    except Exception:
        return max(1, round(len(text) / 4))        # about 4 characters per token

PRICE_PER_1M = {"input": 1.00, "output": 4.00}    # PLACEHOLDER prices, not real
REASONING = {"low": 0.5, "medium": 1.5, "high": 4.0}   # rough multiplier on output, for teaching only

def codex_task_cost(prompt, files_text, expected_output_tokens, effort="medium"):
    inp = estimate_tokens(prompt) + estimate_tokens(files_text)
    out = expected_output_tokens * (1 + REASONING[effort])
    cost = (inp * PRICE_PER_1M["input"] + out * PRICE_PER_1M["output"]) / 1_000_000
    return inp, int(out), cost

one_file = open("pricing.py").read() * 20       # stand-in for one source file
tasks = [("explain one function", one_file, 300, "low"),
         ("add search + tests", one_file * 3, 900, "medium"),
         ("refactor 6 files", one_file * 6, 2500, "high")]
daily_budget = 0.50                                # placeholder budget
total = 0
for name, files, out_t, effort in tasks:
    i, o, c = codex_task_cost("Please do: " + name, files, out_t, effort)
    total += c
    print(f"{name:<22} effort={effort:<6} in={i:>6} out={o:>6} cost={c:.4f} (placeholder)")
print(f"Total {total:.4f} of a daily budget of {daily_budget} (placeholder units)")'''),
    ("md", "### Daily usage check\nAt the end of each day, open your usage page for the program key and note the "
           "tokens used. If one task used far more than you expected, find out why (too many files, high effort, a "
           "loop) before you continue tomorrow."),
])
