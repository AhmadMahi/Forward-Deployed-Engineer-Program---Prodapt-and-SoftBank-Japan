"""Day 02 spec. Python Basics + Functions, Data Structures and Files.
Source: archive/v1-40-day/Day01 (Python basics) + Day02 (functions, data structures, files), merged into one day.
"""
DAY = 2
FOLDER = "Day02-Python-Basics-Functions-and-Files"
SLUG = "Python_Basics_Functions_and_Files"
TITLE = "Python Basics, Functions and Files"
SUBTITLE = "Variables, conditions and loops, reusable functions, lists and dictionaries, and saving data to CSV and JSON"
DATE = "Tue 27 Oct 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 3: OOP and the OpenAI Codex walkthrough."

DECK = [
    dict(type="cards", title="Today's journey", greet="Hajimemashou (始めましょう): Let's begin", items=[
        ("Kahoot and setup check", "Is Colab working for everyone?"),
        ("Session 1 (1.5 hrs)", "Variables, types, conditions, loops, casting"),
        ("Session 2 (1.5 hrs)", "Functions, parameters, return, built-ins"),
        ("Session 3 (2 hrs)", "Lists, tuples, sets, dicts, nested data"),
        ("Session 4 (1.5 hrs)", "Files: CSV and JSON, read and write"),
        ("SmartDesk step 1", "A CLI ticket logger that saves to JSON"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Write basic Python", "Use variables, types, if/elif/else and loops in Colab."),
        ("Write functions", "Define functions with parameters, defaults and return values."),
        ("Pick a structure", "Choose list, tuple, set or dict, and loop through nested data."),
        ("Persist data", "Save and load records with CSV and JSON files."),
    ]),
    dict(type="cards", title="Self-study before and after today", items=[
        ("Pre-read (self-study)", "Python setup in Colab and VS Code, syntax basics: print, comments, indentation."),
        ("Post-read (self-study)", "Comprehensions, lambda, map and filter."),
        ("Why", "Class time goes to practice. The pre-read covers what you can learn alone."),
    ], note="Stuck on setup? Use shared/Laptop_Setup_Guide.pdf and ask in the morning slot."),

    dict(type="section", title="Python basics", sub="Session 1 (1.5 hrs): variables, types, conditions, loops, casting"),
    dict(type="compare", title="A program is a recipe", left=dict(title="In the kitchen", bullets=[
        "A recipe lists exact steps in order", "Ingredients are measured and labelled",
        "\"If the dough is sticky, add flour\"", "\"Stir 10 times\"",
    ]), right=dict(title="In Python", bullets=[
        "A program lists exact instructions in order", "Data is stored in named variables",
        "if conditions choose what happens next", "Loops repeat a step as many times as needed",
    ])),
    dict(type="bullets_code", title="Variables are labelled boxes", bullets=[
        "A variable is a name that points to a value",
        "= means \"store\", not \"equals\"",
        "You can change the value later",
        "Python works out the type for you",
    ], code='''city = "Bengaluru"
students = 30
fee = 499.50
is_open = True

students = students + 5
print(students)
print(f"{city}: {students} students, fee {fee:.2f}")

Output:
35
Bengaluru: 35 students, fee 499.50'''),
    dict(type="table", title="The four basic data types", header=["Type", "What it holds", "Example"], rows=[
        ["int", "Whole numbers", "age = 28"],
        ["float", "Numbers with decimals", "price = 99.5"],
        ["str", "Text, always in quotes", "name = \"Asha\""],
        ["bool", "True or False only", "is_member = True"],
    ], note="Check any value with type(). For example, type(99.5) gives <class 'float'>."),
    dict(type="table", title="Type casting: input() always gives you text", header=["Function", "Converts to", "Example and result"], rows=[
        ["int()", "Whole number", "int(\"42\") gives 42, int(7.9) gives 7"],
        ["float()", "Decimal number", "float(\"3.5\") gives 3.5"],
        ["str()", "Text", "str(100) gives \"100\""],
        ["bool()", "True or False", "bool(0) is False, bool(\"hi\") is True"],
    ], note="\"5\" + \"5\" gives \"55\". int(\"hello\") raises a ValueError."),
    dict(type="bullets_code", title="if, elif, else", bullets=[
        "Python checks conditions from top to bottom",
        "The first True block runs, the rest are skipped",
        "else catches everything left over",
        "Notice the colon and the indentation",
        "and, or, not combine conditions",
    ], code='''marks = 72

if marks >= 85:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Keep practising")

Output:
Grade B'''),
    dict(type="compare", title="for and while loops", left=dict(title="for: a known number of times", bullets=[
        "Walks through each item in a sequence", "range(1, 6) gives 1 to 5",
        "The stop number is not included", "Great for lists and counting",
    ]), right=dict(title="while: until something changes", bullets=[
        "Runs while the condition is True", "Always change something inside",
        "break exits the loop early", "continue skips to the next round",
    ]), note="An infinite loop is a while loop whose condition never becomes False."),
    dict(type="table", title="Common beginner errors", header=["Error", "Usually means", "Quick fix"], rows=[
        ["SyntaxError", "Missing colon, quote or bracket", "Check the end of the line"],
        ["IndentationError", "Spaces are inconsistent", "Use 4 spaces per level"],
        ["NameError", "Variable used before it exists", "Check spelling and order"],
        ["TypeError", "Mixing incompatible types", "Cast with int(), str()"],
        ["ValueError", "Bad value for a conversion", "Validate the input first"],
    ], note="Read the last line of an error message first: it tells you what went wrong."),

    dict(type="section", title="Functions", sub="Session 2 (1.5 hrs): write once, use many times"),
    dict(type="compare", title="Why functions?", left=dict(title="Without functions", bullets=[
        "Same steps copied in many places", "One bug must be fixed everywhere", "Long scripts that are hard to read",
    ]), right=dict(title="With functions", bullets=[
        "Steps written once, called by name", "Fix in one place, fixed everywhere",
        "Small named blocks that explain themselves",
    ])),
    dict(type="bullets_code", title="Defining and calling a function", bullets=[
        "def starts a function definition",
        "Parameters are the inputs",
        "Defaults are used when nothing is passed",
        "return sends a result back",
    ], code='''def add_gst(price, rate=18):
    """Return the price including GST."""
    tax = price * rate / 100
    return price + tax

print(add_gst(1000))
print(add_gst(1000, rate=5))

Output:
1180.0
1050.0'''),
    dict(type="table", title="Function vocabulary", header=["Term", "Meaning", "Example"], rows=[
        ["Parameter", "Name in the definition", "def greet(name)"],
        ["Argument", "Value passed in the call", "greet(\"Mei\")"],
        ["Default value", "Used when nothing is passed", "rate=18"],
        ["Return value", "Result handed back", "return total"],
        ["Scope", "Where a variable is visible", "local vs global"],
    ], note="A function without return gives back None."),
    dict(type="table", title="Built-in functions you will use every day", header=["Function", "What it does", "Example"], rows=[
        ["len()", "Number of items", "len([3, 5, 7]) gives 3"],
        ["sum(), min(), max()", "Add up, smallest, largest", "max([3, 9, 4]) gives 9"],
        ["sorted()", "New sorted list", "sorted([3, 1, 2]) gives [1, 2, 3]"],
        ["round()", "Round a number", "round(3.14159, 2) gives 3.14"],
        ["enumerate()", "Position and item together", "for i, x in enumerate(items, start=1)"],
        ["range()", "A sequence of numbers", "range(0, 10, 2)"],
    ]),

    dict(type="section", title="Data structures", sub="Session 3 (2 hrs): four ways to organise many values"),
    dict(type="table", title="The four built-in collections", header=["Type", "Looks like", "Ordered", "Changeable", "Duplicates"], rows=[
        ["list", "[1, 2, 2]", "Yes", "Yes", "Yes"],
        ["tuple", "(1, 2, 2)", "Yes", "No", "Yes"],
        ["set", "{1, 2}", "No", "Yes", "No"],
        ["dict", "{\"a\": 1}", "Yes", "Yes", "Keys: No"],
    ], note="Choose by asking: do I need order, changes, uniqueness or lookup by name?"),
    dict(type="bullets_code", title="Lists: your everyday collection", bullets=[
        "Index from 0, negative counts from the end",
        "append() adds, remove() deletes",
        "Slicing [start:stop] copies a part",
        "len() gives the size",
    ], code='''fruits = ["apple", "mango", "kiwi"]
fruits.append("banana")
print(fruits[0], fruits[-1])
print(fruits[1:3])
print(len(fruits))

Output:
apple banana
['mango', 'kiwi']
4'''),
    dict(type="compare", title="Tuples and sets", left=dict(title="Tuple ( )", bullets=[
        "Ordered and cannot change", "Good for fixed records: (lat, lon)", "Can be unpacked: x, y = point",
    ]), right=dict(title="Set { }", bullets=[
        "Unique items only, no order", "Remove duplicates: set(my_list)", "Fast membership test: x in s",
        "Union |, intersection &",
    ])),
    dict(type="bullets_code", title="Dictionaries: look up by key", bullets=[
        "Key value pairs, like a real dictionary",
        "Keys must be unique",
        "get() avoids errors for missing keys",
        "items() loops over pairs",
    ], code='''student = {"name": "Yuki", "score": 88}
student["city"] = "Chennai"
print(student["name"])
print(student.get("age", "N/A"))

for key, value in student.items():
    print(key, ":", value)'''),
    dict(type="bullets_code", title="Nested data: how real data looks", greet="Renshuu (練習): Practice. Add a third order!", bullets=[
        "A list of dictionaries is like a table",
        "Each dict is one row, keys are columns",
        "Loop and access fields by name",
        "This is exactly the shape of JSON",
    ], code='''orders = [
    {"id": 1, "item": "Pen", "qty": 3},
    {"id": 2, "item": "Book", "qty": 1},
]
for o in orders:
    print(o["item"], "x", o["qty"])

total = sum(o["qty"] for o in orders)
print("Total items:", total)'''),

    dict(type="section", title="File handling", sub="Session 4 (1.5 hrs): keep data after the program ends"),
    dict(type="flow", title="Working with a file", items=[
        ("Open", "open(path, mode) with r, w or a"),
        ("Read or write", "read(), readlines(), write()"),
        ("Close", "with closes the file for you"),
    ], note="Always prefer: with open(\"notes.txt\", \"w\") as f:"),
    dict(type="bullets_code", title="CSV files: spreadsheets as text", bullets=[
        "CSV stores rows, comma separated",
        "csv.DictWriter writes dicts as rows",
        "csv.DictReader reads rows as dicts",
        "Values come back as text: cast numbers",
    ], code='''import csv
rows = [{"name": "Ana", "marks": 81},
        {"name": "Ken", "marks": 67}]
with open("marks.csv", "w", newline="") as f:
    w = csv.DictWriter(f, ["name", "marks"])
    w.writeheader()
    w.writerows(rows)

with open("marks.csv") as f:
    for r in csv.DictReader(f):
        print(r["name"], int(r["marks"]))'''),
    dict(type="bullets_code", title="JSON files: the language of APIs", bullets=[
        "JSON looks like Python dicts and lists",
        "json.dump writes, json.load reads",
        "indent=2 makes it human friendly",
        "You will use JSON in every API in this course",
    ], code='''import json
ticket = {"id": 1, "customer": "Mei",
          "issue": "No signal",
          "tags": ["network", "urgent"]}
with open("tickets.json", "w") as f:
    json.dump([ticket], f, indent=2)

with open("tickets.json") as f:
    data = json.load(f)
print(data[0]["tags"][0])'''),
    dict(type="table", title="CSV or JSON?", header=["Question", "CSV", "JSON"], rows=[
        ["Shape of data", "Flat rows and columns", "Nested objects and lists"],
        ["Opens in Excel", "Yes", "Not directly"],
        ["Used by web APIs", "Rarely", "Almost always"],
        ["Data types", "Everything is text", "Numbers, bools, null kept"],
    ], note="Rule of thumb: tables go to CSV, structured records go to JSON."),

    dict(type="cards", title="SmartDesk: our running project", items=[
        ("What it is", "A customer support platform for a telecom operator."),
        ("How it grows", "One step per technical day, from a CLI to an agentic AI app."),
        ("Step 1 today", "A CLI ticket logger: add, list and save tickets to JSON."),
        ("Where", "shared/SmartDesk/ and Day02_App_Build_Prompts.md."),
    ]),
    dict(type="bullets_code", title="SmartDesk step 1: CLI ticket logger", bullets=[
        "Each ticket is a dict",
        "Functions: load, save, add, list",
        "Tickets saved to tickets.json",
        "Survives a restart",
    ], code='''def add_ticket(tickets, customer, issue,
               priority="medium"):
    ticket = {"id": len(tickets) + 1,
              "customer": customer,
              "issue": issue,
              "priority": priority,
              "status": "open"}
    tickets.append(ticket)
    return ticket'''),
    dict(type="callout", title="Hands-on time", text="Build the contact book, then the SmartDesk ticket logger: "
         "functions first, then the data, then save it to a file.",
         sub="Test each function on its own before connecting them together. Work in pairs and explain your code "
             "out loud.", greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Basics", "Variables, types, casting, if/elif/else, for and while."),
        ("Functions", "def, parameters, defaults, return. Small, named and reusable."),
        ("Collections", "list ordered, tuple fixed, set unique, dict key value."),
        ("Files", "with open() for text, csv for tables, json for nested records."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day02_Hotel_Lab.md: post-read, notebook, problems, workbook."),
        ("Workbook", "Complete the Day 2 workbook."),
        ("Pre-read", "Read the Day 3 pre-read: objects, good habits and OpenAI Codex setup."),
    ]),
]

PREREAD = dict(title="Talking to Computers and Organising Things",
               lede="A light read before Day 2. About 20 minutes, no code to memorise. This includes the self-study "
                    "topics: Python setup and syntax basics.", sections=[
    dict(h="Why read this?", paras=[
        "Tomorrow you write your first Python, then learn to group instructions, organise information and save it "
        "so it is still there the next day. This note gives you the big ideas in everyday language, so the class "
        "feels familiar instead of new."]),
    dict(h="1. What is a program?", paras=[
        "A program is a list of instructions that a computer follows exactly, in order. Think of a recipe: what you "
        "need, the steps, and what to do if something changes (\"if the batter is too thick, add milk\"). A computer "
        "never guesses. It does exactly what you write."],
        box="**Key idea:** computers are not smart, they are obedient. Clear instructions give clear results."),
    dict(h="2. Self-study: setup and syntax basics", paras=[
        "We use **Google Colab**, which runs Python in your browser, and **VS Code** on your laptop from Day 3. "
        "Please do these before class:"], bullets=[
        "Sign in to a Google account and open colab.research.google.com once.",
        "Create a notebook, type print(\"Hello, Python!\") and press Shift + Enter.",
        "Lines starting with # are comments. Python ignores them.",
        "Indentation matters: use 4 spaces to group lines under if, for, while and def.",
        "Python is case sensitive: name, Name and NAME are three different things.",
        "Follow shared/Laptop_Setup_Guide.pdf to install Python 3.12 or newer and VS Code."]),
    dict(h="3. Words you will hear", table=[
        ["Word", "Everyday meaning"],
        ["Variable", "A labelled jar that holds a piece of information"],
        ["Condition", "A yes or no question that decides what happens next"],
        ["Loop", "Doing the same step again until the job is done"],
        ["Function", "A kitchen appliance: inputs go in, a result comes out"],
        ["File", "A notebook that keeps data after the program ends"],
    ]),
    dict(h="4. Four ways to organise things", table=[
        ["Real life", "Python name", "What makes it special"],
        ["A shopping list", "list", "Ordered; you can add, remove or change items"],
        ["Your date of birth", "tuple", "Fixed; it does not change"],
        ["Unique stamps in a collection", "set", "No duplicates allowed"],
        ["A phone contact", "dictionary", "Find information by a label, called a key"],
    ]),
    dict(h="5. Why save to files?", paras=[
        "When a program ends, everything in memory disappears, like a whiteboard that gets wiped. Saving to a file is "
        "like writing it in a notebook. **CSV** is a simple table that opens in Excel. **JSON** stores labelled, "
        "nested information and is used by almost every app and API."]),
    dict(h="6. Think about these before class", bullets=[
        "Write down the steps for making a cup of tea. How many \"if\" decisions did you include?",
        "Write down the details you store for one contact on your phone. Which are labels and which are values?",
        "A customer calls a telecom helpdesk. What details would you write on the ticket?"],
        after=["Kaizen (改善): continuous improvement, one small step at a time"]),
])

POSTREAD = dict(title="Python Basics, Functions and Files: Recap and Beyond",
                lede="What we covered today, plus self-study topics and ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Variables and types", "int, float, str, bool. = stores, == compares. Check with type()."],
        ["Type casting", "input() returns text. Use int(), float(), str() to convert."],
        ["Conditions", "if, elif, else. Only the first True branch runs. Colon and indentation required."],
        ["Loops", "for over a sequence, while until a condition changes. break and continue."],
        ["Functions", "def name(params): ... return value. No return means None."],
        ["Collections", "list ordered, tuple fixed, set unique, dict key value. get() for safe lookups."],
        ["Nested data", "A list of dicts is a table of records and the shape of JSON."],
        ["Files", "with open(path, mode). csv.DictReader / DictWriter. json.load / json.dump."],
    ]),
    dict(h="Part B: Self-study topics", sub="1. List comprehensions", paras=[
        "Build a new list in one readable line: [expression for item in items if condition]."],
        code='prices = [120, 450, 80, 990]\nwith_tax = [round(p * 1.18, 2) for p in prices]\ncheap = [p for p in prices if p < 200]   # [120, 80]'),
    dict(sub="2. Dictionary and set comprehensions",
         code='names = ["ana", "ken", "ana"]\nlengths = {n: len(n) for n in names}    # {\'ana\': 3, \'ken\': 3}\nunique = {n.upper() for n in names}     # {\'ANA\', \'KEN\'}'),
    dict(sub="3. lambda, map and filter", paras=[
        "A lambda is a tiny one-line function. map applies a function to every item; filter keeps items where the "
        "function returns True. Comprehensions often read better, but you will see both."],
        code='square = lambda x: x * x\nprint(list(map(square, [1, 2, 3])))            # [1, 4, 9]\nprint(list(filter(lambda p: p < 200, prices)))  # [120, 80]\ntop = sorted(tickets, key=lambda t: t["priority"])'),
    dict(h="Part C: Going beyond today", sub="1. Mutable default arguments: a classic trap", paras=[
        "Never use a list or dict as a default value. It is created once and shared between calls. Use None."],
        code="def add_item(item, basket=None):\n    if basket is None:\n        basket = []\n    basket.append(item)\n    return basket"),
    dict(sub="2. Safe casting with try and except", paras=[
        "If a user types \"abc\" where a number is expected, int() raises a ValueError. Catch it and ask again. "
        "Exceptions are covered fully on Day 3."]),
    dict(sub="3. pathlib and type hints", paras=[
        "Path(\"data\") / \"marks.csv\" builds paths safely on any operating system. Type hints such as "
        "def average(marks: list[float]) -> float do not change how code runs, but editors and FastAPI (Day 5) use "
        "them heavily."]),
    dict(h="Part D: Check yourself", bullets=[
        "What is the difference between = and ==?",
        "What is the difference between a parameter and an argument?",
        "When would you choose a tuple over a list, and a dict over a list?",
        "Why does json.dump keep numbers as numbers but CSV does not?",
        "What does the with statement do for you?"]),
    dict(h="Part E: Practice ideas for tonight", bullets=[
        "Print 1 to 30, with \"Fizz\" for multiples of 3 and \"Buzz\" for multiples of 5.",
        "Read a CSV of expenses and print the total per category.",
        "Add a \"close ticket\" function to your SmartDesk ticket logger."],
        after=["**Coming up on Day 3:** classes and objects, exceptions, dependency hygiene, and your first afternoon "
               "with OpenAI Codex in VS Code.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Nine problems from warm-up to stretch. Solve them in the Day 2 notebook or in a .py file in "
                    "VS Code.", problems=[
    dict(title="Temperature Converter", level="Warm-up", concepts="variables, float(), arithmetic, f-strings",
         text="Store a temperature in Celsius and print it in Fahrenheit. Formula: F = C x 9 / 5 + 32. Round to "
              "1 decimal place. Then make it read the value with input().",
         sample="36.6 C is 97.9 F",
         hints=["input() returns text, so cast it with float().", "round(value, 1) rounds to one decimal place."]),
    dict(title="Grade Calculator", level="Easy", concepts="if/elif/else, comparison operators",
         text="Given marks out of 100, print the grade: 85 and above is A, 70 to 84 is B, 50 to 69 is C, below 50 "
              "is \"Needs improvement\". Marks below 0 or above 100 print \"Invalid marks\".",
         sample="marks = 78  ->  Grade: B\nmarks = 120 ->  Invalid marks",
         hints=["Check the invalid range first.", "Order your elif checks from highest to lowest."]),
    dict(title="Number Guessing Game", level="Medium", concepts="while loop, break, conditions",
         text="Store a secret number between 1 and 20. Allow up to 5 guesses. Say \"Too high\" or \"Too low\" after "
              "each wrong guess; stop when correct. Test it with a fixed list of guesses first.",
         sample="Guess 10: Too low\nGuess 15: Too high\nGuess 13: Correct! You got it in 3 attempts.",
         hints=["Keep an attempts counter.", "Use break when the guess is correct."]),
    dict(title="Area Helpers", level="Easy", concepts="def, parameters, return",
         text="Write rectangle_area(l, w), circle_area(r) and triangle_area(b, h). Call each and print the result "
              "rounded to 2 decimals.",
         sample="rectangle_area(4, 5) -> 20\ncircle_area(3)       -> 28.27\ntriangle_area(6, 4)  -> 12.0",
         hints=["import math and use math.pi."]),
    dict(title="Word Counter", level="Medium", concepts="dict, split, functions, sorted",
         text="Write count_words(text) that returns a dict of each word and how often it appears (ignore case). "
              "Print the three most common words.",
         sample="count_words(\"the cat and the hat and the bat\")\n{'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}\nTop 3: the, and, cat",
         hints=["text.lower().split()", "sorted(d.items(), key=lambda kv: kv[1], reverse=True)"]),
    dict(title="Student Report", level="Medium", concepts="list of dicts, functions",
         text="Store five students as a list of dicts with name and marks. Write average(students) and "
              "topper(students). Print the class average and the topper.",
         sample="Class average: 74.4\nTopper: Priya (92)",
         hints=["max(students, key=lambda s: s[\"marks\"])"]),
    dict(title="Expenses to CSV", level="Challenging", concepts="csv module, dicts",
         text="Write a list of expenses (date, category, amount) to expenses.csv. Read it back and print the total "
              "spent per category.",
         sample="Food: 1450.0\nTravel: 800.0\nBills: 2200.0",
         hints=["Values read from CSV are text: cast with float().", "Accumulate totals in a dict."]),
    dict(title="Contact Book with JSON", level="Challenging", concepts="functions, dict, json, files",
         text="Build add_contact, find_contact, save_contacts and load_contacts. Contacts are stored in "
              "contacts.json so they survive restarts.",
         sample="add_contact(\"Mei\", \"98450 11111\")\nsave_contacts()\n# restart\nload_contacts()\nfind_contact(\"Mei\") -> 98450 11111",
         hints=["load returns an empty dict if the file does not exist yet."]),
    dict(title="SmartDesk Ticket Logger", level="Stretch", concepts="functions, list of dicts, json, CLI loop",
         text="SmartDesk step 1. Write load_tickets(), save_tickets(tickets), add_ticket(tickets, customer, issue, "
              "priority) and list_tickets(tickets, status=None). Tickets are saved to tickets.json. Add a menu: 1) Add "
              "2) List 3) Exit. Reject priorities other than low, medium, high.",
         sample="1) Add 2) List 3) Exit > 1\nCustomer: Mei\nIssue: No signal at home\nPriority: high\nSaved ticket #1\n"
                "> 2\n#1 [high] Mei: No signal at home (open)",
         hints=["Each ticket is a dict with id, customer, issue, priority, status.",
                "Save after every change so nothing is lost."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "The input() function always returns a value of type ________.",
        "To convert the text \"42\" into a whole number, use ________.",
        "In Python, ________ stores a value and ________ compares two values.",
        "range(1, 6) produces the numbers 1 to ________.",
        "The keyword ________ stops a loop immediately.",
        "The keyword used to define a function is ________.",
        "A function with no return statement returns ________.",
        "A ________ is ordered but cannot be changed after creation.",
        "To read a dict key safely without an error, use the ________ method.",
        "json.________ writes Python data to a JSON file.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Why do we need type casting when working with input()?",
        "When would you choose a while loop instead of a for loop?",
        "When would you use a dictionary instead of a list? Give a SmartDesk example.",
        "Give one situation where CSV is better than JSON, and one where JSON is better.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'x = "5"\ny = "3"\nprint(x + y)',
        "for i in range(2, 10, 3):\n    print(i)",
        "def f(a, b=2):\n    return a * b\nprint(f(3), f(3, 3))",
        "nums = [1, 2, 3, 4, 5]\nprint(nums[1:4], nums[-2])",
        'd = {"a": 1, "b": 2}\nd["a"] = 10\nprint(d.get("c", 0) + d["a"])',
        "print([x * 2 for x in range(4) if x % 2 == 0])",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Print all even numbers from 2 to 20 using a for loop."),
        dict(q="Write a function is_even(n) that returns True or False."),
        dict(q="Write a function that returns the largest number in a list without using max()."),
        dict(q="Write save_tickets(tickets) and load_tickets() for SmartDesk using json.",
             starter="import json\n\ndef save_tickets(tickets, path=\"tickets.json\"):\n    ...\n\ndef load_tickets(path=\"tickets.json\"):\n    ..."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Variables, conditions and loops, functions, data structures, and CSV and JSON files", cells=[
    ("md", "## 1. Setup check and working folder"),
    ("code", '''# ===== Option A: Google Colab (active) =====
import os, sys, platform
IN_COLAB = "google.colab" in sys.modules
base = "/content/day2" if IN_COLAB else "day2"
os.makedirs(base, exist_ok=True)
os.chdir(base)
print("Python", platform.python_version(), "| Colab:", IN_COLAB, "| Working in:", os.getcwd())

# ===== Option B: VS Code / local Jupyter =====
# The same cell works locally: it creates a day2 folder next to this notebook.
# print("Python location:", sys.executable)   # confirm VS Code picked the right interpreter'''),
    ("md", "**VS Code setup reminder** (one time only, see `shared/Laptop_Setup_Guide.pdf`)\n"
           "1. Install Python 3.12 or newer from python.org (tick *Add Python to PATH* on Windows).\n"
           "2. Install VS Code, then the **Python** and **Jupyter** extensions.\n"
           "3. Open this `.ipynb` file and choose your Python interpreter at the top right (*Select Kernel*)."),
    ("md", "# Session 1: Python basics\n## 2. Variables and data types"),
    ("code", '''city = "Bengaluru"     # str
students = 30          # int
fee = 499.50           # float
is_open = True         # bool

print(city, students, fee, is_open)
print(type(city), type(students), type(fee), type(is_open))

students = students + 5    # variables can change
print(f"{city} batch has {students} students. Fee: {fee:.2f}")'''),
    ("md", "### TODO 1: Create four variables about yourself (name, city, years of experience, likes_python) and print them with an f-string."),
    ("code", "# TODO: write your code here"),
    ("md", "## 3. Type casting and `input()`\n`input()` always returns text. In class we use a fixed value so the notebook "
           "runs top to bottom; switch to Option B to type your own."),
    ("code", '''# ===== Option A: fixed value (active) =====
age = "27"

# ===== Option B: interactive input (uncomment to use) =====
# age = input("Your age: ")

print("Type before casting:", type(age))
age = int(age)
print("Next year you will be", age + 1)

print(int("42"), int(7.9), float("3.5"), str(100), bool(0), bool("hi"))
print("5" + "5")            # joins text: 55
print(int("5") + int("5"))  # adds numbers: 10'''),
    ("md", "## 4. Conditions: `if`, `elif`, `else`"),
    ("code", '''marks = 72
if marks >= 85:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Keep practising")

age, has_id = 20, True
print("Can enter:", age >= 18 and has_id)'''),
    ("md", "### TODO 2: Given a number, print whether it is positive, negative or zero."),
    ("code", "# TODO: write your code here"),
    ("md", "## 5. Loops"),
    ("code", '''for n in range(1, 6):
    print("5 x", n, "=", 5 * n)
print(list(range(2, 11, 2)))   # start, stop (excluded), step

attempts = 0
while attempts < 3:
    attempts += 1
    print("Attempt", attempts)

for n in range(1, 11):
    if n == 4:
        continue      # skip 4
    if n == 8:
        break         # stop at 8
    print(n, end=" ")'''),
    ("md", "### Mini challenge: number guessing game\nOption A uses a fixed list of guesses so it runs on its own."),
    ("code", '''secret = 13
# ===== Option A: fixed guesses (active) =====
guesses = [10, 15, 13]
# ===== Option B: interactive (uncomment, and use input() inside the loop) =====
# guesses = None

attempts = 0
while attempts < 5:
    guess = guesses[attempts] if guesses else int(input("Guess (1-20): "))
    attempts += 1
    if guess == secret:
        print(f"{guess}: Correct! You got it in {attempts} attempts.")
        break
    print(guess, ": Too low" if guess < secret else ": Too high")
else:
    print("Out of attempts. The number was", secret)'''),
    ("md", "# Session 2: Functions\n## 6. Defining and calling functions"),
    ("code", '''def add_gst(price, rate=18):
    """Return the price including GST."""
    tax = price * rate / 100
    return price + tax

print(add_gst(1000))
print(add_gst(1000, rate=5))
print(add_gst.__doc__)

def greet(name):
    print("Hello", name)      # no return

print(greet("Mei"))           # prints Hello Mei, then None'''),
    ("md", "### Built-in functions"),
    ("code", '''marks = [72, 85, 90, 64]
print(len(marks), sum(marks), min(marks), max(marks), round(sum(marks) / len(marks), 1))
print(sorted(marks, reverse=True))
for position, m in enumerate(marks, start=1):
    print(position, m)'''),
    ("md", "### Scope: local vs global"),
    ("code", '''count = 10          # global
def show():
    count = 99      # local, a different variable
    print("inside:", count)
show()
print("outside:", count)'''),
    ("md", "### TODO 3: Write `celsius_to_fahrenheit(c)` that returns the converted value, then call it for 0, 37 and 100."),
    ("code", "# TODO: write your code here"),
    ("md", "# Session 3: Data structures\n## 7. Lists, tuples and sets"),
    ("code", '''fruits = ["apple", "mango", "kiwi"]
fruits.append("banana")
fruits.insert(1, "grape")
fruits.remove("kiwi")
print(fruits, fruits[0], fruits[-1], fruits[1:3], len(fruits))

point = (12.97, 77.59)
lat, lon = point          # unpacking
print(lat, lon)

emails = ["a@x.com", "b@x.com", "a@x.com"]
unique = set(emails)
print(unique, "a@x.com" in unique)
python_team, ai_team = {"Ana", "Ken", "Ravi"}, {"Ken", "Mei"}
print("Both:", python_team & ai_team, "| Either:", python_team | ai_team)'''),
    ("md", "## 8. Dictionaries and nested data"),
    ("code", '''student = {"name": "Yuki", "score": 88}
student["city"] = "Chennai"
print(student["name"], student.get("age", "N/A"))
for key, value in student.items():
    print(key, ":", value)

orders = [
    {"id": 1, "item": "Pen", "qty": 3, "price": 20},
    {"id": 2, "item": "Book", "qty": 1, "price": 350},
]
for o in orders:
    print(f'{o["item"]:<6} x{o["qty"]}  = {o["qty"] * o["price"]}')
print("Order value:", sum(o["qty"] * o["price"] for o in orders))'''),
    ("md", "### TODO 4: Add a third order and print only orders worth more than 100."),
    ("code", "# TODO: write your code here"),
    ("md", "# Session 4: Files\n## 9. Text, CSV and JSON files"),
    ("code", '''with open("notes.txt", "w") as f:
    f.write("Day 2\\n")
    f.write("Functions\\n")
with open("notes.txt", "a") as f:
    f.write("Files\\n")
with open("notes.txt") as f:
    for line in f:
        print(line.strip())'''),
    ("code", '''import csv
rows = [{"name": "Ana", "marks": 81}, {"name": "Ken", "marks": 67}, {"name": "Mei", "marks": 92}]
with open("marks.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(rows)

with open("marks.csv") as f:
    data = list(csv.DictReader(f))
print(data)
print("Average:", sum(int(r["marks"]) for r in data) / len(data))   # values are text: cast them'''),
    ("code", '''import json
config = {"app": "Planner", "version": 2, "tags": ["study", "python"], "active": True}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
with open("config.json") as f:
    loaded = json.load(f)
print(loaded["tags"][0], type(loaded["version"]), loaded["active"])'''),
    ("md", "### Download your files\nIn Colab, files live in the session and disappear when it ends."),
    ("code", '''# ===== Option A: Google Colab =====
# from google.colab import files
# files.download("marks.csv")      # uncomment to download in Colab

# ===== Option B: VS Code / local =====
# Files are already saved in the day2 folder next to this notebook.
print(sorted(os.listdir(".")))'''),
    ("md", "## 10. SmartDesk step 1: CLI ticket logger\nSmartDesk is our running project: a support platform for a "
           "telecom operator. Today it is a set of functions that save tickets to JSON."),
    ("code", '''import json, os
TICKETS_FILE = "tickets.json"
PRIORITIES = {"low", "medium", "high"}

def load_tickets():
    """Return the saved tickets, or an empty list on first run."""
    if not os.path.exists(TICKETS_FILE):
        return []
    with open(TICKETS_FILE) as f:
        return json.load(f)

def save_tickets(tickets):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=2)

def add_ticket(tickets, customer, issue, priority="medium"):
    if priority not in PRIORITIES:
        raise ValueError(f"priority must be one of {sorted(PRIORITIES)}")
    ticket = {"id": len(tickets) + 1, "customer": customer, "issue": issue,
              "priority": priority, "status": "open"}
    tickets.append(ticket)
    save_tickets(tickets)
    return ticket

def list_tickets(tickets, status=None):
    for t in tickets:
        if status is None or t["status"] == status:
            print(f'#{t["id"]} [{t["priority"]}] {t["customer"]}: {t["issue"]} ({t["status"]})')

if os.path.exists(TICKETS_FILE):
    os.remove(TICKETS_FILE)          # start fresh for the demo
tickets = load_tickets()
add_ticket(tickets, "Mei", "No signal at home", "high")
add_ticket(tickets, "Ravi", "Charged twice this month")
print("Reloaded from disk:", len(load_tickets()), "tickets")
list_tickets(load_tickets())'''),
    ("md", "### CLI menu\nOption A runs a scripted set of choices so the cell finishes on its own. Option B is the "
           "real interactive menu."),
    ("code", '''# ===== Option A: scripted choices (active) =====
script = iter(["1", "Aiko", "Cannot log in to the app", "low", "2", "3"])
ask = lambda prompt: next(script)
# ===== Option B: interactive (uncomment to use) =====
# ask = input

while True:
    choice = ask("1) Add  2) List  3) Exit > ")
    if choice == "1":
        t = add_ticket(tickets, ask("Customer: "), ask("Issue: "), ask("Priority: "))
        print("Saved ticket #", t["id"])
    elif choice == "2":
        list_tickets(tickets)
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option, please try again")'''),
    ("md", "### TODO 5: Add a `close_ticket(tickets, ticket_id)` function and a menu option for it."),
    ("code", "# TODO: write your code here"),
])
