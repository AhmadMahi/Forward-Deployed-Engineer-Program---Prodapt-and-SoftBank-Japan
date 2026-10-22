"""Day 04 spec. Architecture and MongoDB.
Source: archive/v1-40-day/Day04, reused and updated to the v4 session plan (indexes, data modelling, Compass, SmartDesk).
"""
DAY = 4
FOLDER = "Day04-Architecture-and-MongoDB"
SLUG = "Architecture_and_MongoDB"
TITLE = "Architecture and MongoDB"
SUBTITLE = "Frontend, backend and APIs, charts with Matplotlib, NoSQL and BSON, MongoDB CRUD, indexes and data modelling"
DATE = "Thu 29 Oct 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 5: REST APIs, FastAPI and Basics assessment 1."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 3"),
        ("Session 1 (1 hr)", "Frontend, backend, middleware, APIs; Matplotlib"),
        ("Session 2 (2.5 hrs)", "NoSQL, MongoDB, documents, BSON, ObjectId, Compass"),
        ("Session 3 (2.5 hrs)", "CRUD, indexes, embed vs reference"),
        ("SmartDesk step 3", "Tickets in MongoDB; chart by priority"),
        ("Hands-on", "Inventory Dashboard"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain architecture", "Describe frontend, backend, middleware, clients, servers and APIs."),
        ("Visualise data", "Draw line, bar and pie charts with Matplotlib."),
        ("Use MongoDB", "Insert, find, update and delete documents with PyMongo."),
        ("Design documents", "Add indexes and choose between embedding and referencing."),
    ]),

    dict(type="section", title="Architecture and charts", sub="Session 1 (1 hr): how modern apps are wired together"),
    dict(type="compare", title="Frontend and backend", left=dict(title="Frontend (client side)", bullets=[
        "What the user sees and clicks", "Runs in the browser or on the phone", "React, HTML, CSS, JavaScript",
        "Never holds secrets",
    ]), right=dict(title="Backend (server side)", bullets=[
        "Business rules and data access", "Runs on a server you control", "Python FastAPI, Node.js Express",
        "Talks to the database",
    ])),
    dict(type="flow", title="A request's journey", items=[
        ("Client", "Browser or app sends a request"),
        ("Internet", "Travels over HTTP"),
        ("Middleware", "Logging, auth, CORS checks"),
        ("Server", "API code runs the rules"),
        ("Database", "Data is read or saved"),
    ], note="The response travels back the same way, usually as JSON."),
    dict(type="cards", title="The restaurant analogy", greet="Irasshaimase (いらっしゃいませ): Welcome!", items=[
        ("Customer = client", "Asks for what they want from the menu."),
        ("Waiter = API", "Takes the order, follows the rules, brings back the result."),
        ("Kitchen = server", "Does the real work out of sight."),
        ("Pantry = database", "Where ingredients, the data, are stored."),
    ]),
    dict(type="compare", title="Monolith and layered APIs", left=dict(title="Everything in one file", bullets=[
        "UI, logic and data access mixed", "Hard to test and change", "One bug can affect everything",
    ]), right=dict(title="Layered architecture", bullets=[
        "Routes: receive requests", "Services: business rules", "Repositories: talk to the database",
        "Middleware: cross-cutting checks",
    ]), note="API-based architecture: every client uses the same API, so web and mobile stay consistent."),
    dict(type="bullets_code", title="Matplotlib basics", bullets=[
        "import matplotlib.pyplot as plt",
        "plot() for lines, bar() for bars",
        "Always add a title and axis labels",
        "show() displays, savefig() saves",
    ], code='''import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
tickets = [120, 150, 90, 180]

plt.plot(months, tickets, marker="o")
plt.title("Tickets per month")
plt.xlabel("Month")
plt.ylabel("Tickets")
plt.show()'''),
    dict(type="table", title="Pick the right chart", header=["Question you are asking", "Chart", "Function"], rows=[
        ["How does it change over time?", "Line", "plt.plot()"],
        ["How do categories compare?", "Bar", "plt.bar()"],
        ["How is it spread out?", "Histogram", "plt.hist()"],
        ["Is there a relationship?", "Scatter", "plt.scatter()"],
        ["What share does each part have?", "Pie (few parts)", "plt.pie()"],
    ], note="Good charts answer one question clearly."),

    dict(type="section", title="NoSQL and MongoDB", sub="Session 2 (2.5 hrs): storing data as documents"),
    dict(type="compare", title="SQL and NoSQL", left=dict(title="SQL (relational)", bullets=[
        "Tables with fixed columns", "Relationships via joins", "Strong structure up front",
        "Examples: PostgreSQL, MySQL, SQLite",
    ]), right=dict(title="NoSQL (document)", bullets=[
        "Flexible JSON-like documents", "Related data often nested together", "Schema can evolve over time",
        "Examples: MongoDB, Firestore",
    ])),
    dict(type="flow", title="MongoDB architecture", items=[
        ("Server", "mongod process or an Atlas cluster"),
        ("Database", "For example smartdesk"),
        ("Collection", "For example tickets"),
        ("Document", "One ticket, stored as BSON"),
    ], note="Atlas runs MongoDB for you in the cloud. A replica set keeps copies for safety."),
    dict(type="table", title="MongoDB vocabulary", header=["SQL world", "MongoDB world", "Example"], rows=[
        ["Database", "Database", "smartdesk"],
        ["Table", "Collection", "tickets"],
        ["Row", "Document", "{\"customer\": \"Mei\"}"],
        ["Column", "Field", "priority"],
        ["Primary key", "_id", "ObjectId(...)"],
    ]),
    dict(type="bullets_code", title="JSON, BSON and ObjectId", bullets=[
        "You write documents like JSON",
        "MongoDB stores them as BSON (Binary JSON)",
        "BSON adds types: dates, ObjectId, decimals",
        "ObjectId: 12 bytes, unique, includes a timestamp",
    ], code='''{
  "_id": ObjectId("6720f1c2a1b2c3d4e5f60718"),
  "customer": "Mei",
  "issue": "No signal at home",
  "priority": "high",
  "tags": ["network", "5g"],
  "created": ISODate("2026-10-29T09:30:00Z")
}'''),
    dict(type="cards", title="MongoDB Compass", items=[
        ("What it is", "A free desktop app to see and query your data visually."),
        ("Connect", "Paste a connection string: local or Atlas."),
        ("Explore", "Browse collections, filter documents, view indexes."),
        ("Optional", "Colab uses mongomock, so Compass is not required."),
    ], note="Connection strings contain passwords. Keep them in an environment variable, never in code."),

    dict(type="section", title="CRUD, indexes and data modelling", sub="Session 3 (2.5 hrs): create, read, update, delete"),
    dict(type="bullets_code", title="Connect and create", bullets=[
        "MongoClient connects to the server",
        "Databases and collections appear on first insert",
        "insert_one for one, insert_many for many",
        "The result tells you the new _id",
    ], code='''import os
from pymongo import MongoClient

client = MongoClient(os.environ.get(
    "MONGO_URI", "mongodb://localhost:27017"))
tickets = client["smartdesk"]["tickets"]

tickets.insert_one({"customer": "Mei",
                    "priority": "high"})
tickets.insert_many([
    {"customer": "Ravi", "priority": "low"},
    {"customer": "Aiko", "priority": "medium"},
])'''),
    dict(type="bullets_code", title="Read with filters", bullets=[
        "find_one returns the first match",
        "find returns all matches",
        "Operators: $gt, $lt, $in, $regex",
        "Projection picks which fields come back",
    ], code='''tickets.find_one({"customer": "Mei"})

urgent = tickets.find({"priority": {"$in": ["high"]}})
for t in urgent:
    print(t["customer"])

tickets.find({}, {"_id": 0, "customer": 1})
tickets.count_documents({"status": "open"})'''),
    dict(type="bullets_code", title="Update and delete", greet="Chuui (注意): Caution. delete_many({}) deletes everything!", bullets=[
        "update_one / update_many need a filter and an operator",
        "$set changes fields, $inc adds to numbers",
        "$push adds to an array",
        "Always test your filter with find first",
    ], code='''tickets.update_one(
    {"customer": "Mei"},
    {"$set": {"status": "closed"}}
)
tickets.update_many({}, {"$inc": {"reopened": 0}})
tickets.update_one({"customer": "Ravi"},
                   {"$push": {"tags": "billing"}})

tickets.delete_one({"customer": "Aiko"})'''),
    dict(type="bullets_code", title="Indexes: find fast", bullets=[
        "Without an index MongoDB scans every document",
        "An index is a sorted lookup on one or more fields",
        "Index the fields you filter and sort on",
        "Unique indexes stop duplicates",
        "Each index slows writes a little",
    ], code='''tickets.create_index("customer")
tickets.create_index([("status", 1),
                      ("priority", -1)])
tickets.create_index("ticket_no", unique=True)

print(tickets.index_information().keys())'''),
    dict(type="compare", title="Data modelling: embed or reference?", left=dict(title="Embed", bullets=[
        "Store related data inside the document", "Read together, in one query",
        "Bounded size (comments on a ticket)", "Example: ticket with its notes",
    ]), right=dict(title="Reference", bullets=[
        "Store the other document's _id", "Data shared by many documents",
        "Large or growing without limit", "Example: ticket points to a customer",
    ]), note="Rule of thumb: embed what you read together; reference what you share."),
    dict(type="bullets_code", title="SmartDesk step 3: tickets in MongoDB", bullets=[
        "A tickets collection with an index on status",
        "Customers referenced by customer_id",
        "Notes embedded inside each ticket",
        "Count tickets by priority, then chart it",
    ], code='''counts = {}
for t in tickets.find({"status": "open"}):
    p = t["priority"]
    counts[p] = counts.get(p, 0) + 1

plt.bar(counts.keys(), counts.values())
plt.title("Open tickets by priority")
plt.show()'''),
    dict(type="callout", title="Hands-on time", text="Build the Inventory Dashboard: store products in MongoDB, "
         "query them with filters, add an index, and chart stock value per category.",
         sub="In Colab we use mongomock, a practice MongoDB that runs in memory. The same code works with a real "
             "MongoDB or a free Atlas cluster.", greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Architecture", "Frontend, backend, middleware, API, database. Layers keep code clean."),
        ("Charts", "Pick the chart that answers your question. Label everything."),
        ("Documents", "Flexible JSON-like records stored as BSON with an ObjectId."),
        ("CRUD and design", "Test filters first. Index what you query. Embed or reference."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow: quiz on today, FastAPI, then Basics assessment 1.", items=[
        ("Hotel lab", "Follow Day04_Hotel_Lab.md: 20 tickets, queries and a chart."),
        ("Workbook", "Complete the Day 4 workbook."),
        ("Pre-read", "Skim the Day 5 pre-read on how the web talks."),
    ]),
]

PREREAD = dict(title="How Apps Talk and Remember", lede="A light read before Day 4. About 15 minutes, no code required.",
               sections=[
    dict(h="Why read this?", paras=[
        "When you raise a complaint in a telecom app, your phone, the company's servers and a database all work "
        "together in a second or two. Tomorrow you will see how that works, draw your first charts and store "
        "SmartDesk tickets in a modern database called MongoDB."]),
    dict(h="1. Front of house and back of house", paras=[
        "The **frontend** is what you see: screens, buttons and forms. The **backend** is the part you never see: the "
        "rules, the calculations and the data. Between them, **middleware** checks every request on the way in, like "
        "a security desk in an office building."]),
    dict(h="2. The restaurant model of an app", table=[
        ["Restaurant", "App world", "Job"],
        ["Customer", "Client (phone, browser)", "Asks for something"],
        ["Waiter", "API", "Carries requests and responses, follows the menu rules"],
        ["Kitchen", "Server", "Does the actual work"],
        ["Pantry", "Database", "Stores the ingredients, which is the data"],
    ], after=["The customer never walks into the kitchen. In the same way, apps never touch the database directly. "
              "They talk to an API that follows agreed rules."]),
    dict(h="3. Pictures make numbers speak", paras=[
        "A table of 365 daily ticket counts is hard to read. A simple line chart shows the trend instantly. We will "
        "use a Python tool called **Matplotlib** to draw charts."]),
    dict(h="4. Two ways to store information", paras=[
        "Some databases store data in neat tables, like a spreadsheet. Others store each record as a flexible "
        "**document**, like a filled-in form that can have extra sections when needed. MongoDB is a document database."],
        box="**Example:** one customer has two phone numbers and another has five. A document simply holds a list of "
            "numbers, without needing a separate table."),
    dict(h="5. Finding things fast", paras=[
        "A book's index lets you jump to a topic without reading every page. A database **index** does the same for "
        "your data. It makes searches fast, at the cost of a little extra work every time you add data."]),
    dict(h="6. Four actions on any data: CRUD", bullets=[
        "**Create:** log a new support ticket.", "**Read:** search for a customer's tickets.",
        "**Update:** change a ticket's status to closed.", "**Delete:** remove a test ticket."]),
    dict(h="7. Think about these before class", bullets=[
        "Pick an app you used today. What was the client, and what data did it ask for?",
        "What information would you store on a support ticket? Is any of it a list?",
        "Which chart would you use to show tickets per priority?"],
        after=["Irasshaimase (いらっしゃいませ): welcome, said to customers in shops and restaurants"]),
])

POSTREAD = dict(title="Architecture and MongoDB: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Frontend and backend", "Frontend shows and collects; backend holds rules, data and secrets."],
        ["Middleware", "Code that runs on every request: logging, auth, CORS."],
        ["API-based architecture", "All clients use the same API contract, usually JSON over HTTP."],
        ["Matplotlib", "plot, bar, hist, scatter, pie. Title, labels, legend. show() or savefig()."],
        ["NoSQL and BSON", "Flexible documents stored as Binary JSON with types such as ObjectId and dates."],
        ["CRUD", "insert_one/many, find with filters, update with $set/$inc/$push, delete. Test filters first."],
        ["Indexes", "create_index on fields you filter or sort by. Unique indexes stop duplicates."],
        ["Embed vs reference", "Embed what you read together; reference what is shared or grows without limit."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Subplots: several charts in one figure",
         code="fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))\nax1.bar(cats, totals)\nax2.plot(months, sales)\nfig.tight_layout()"),
    dict(sub="2. Upserts", paras=["If no document matches, upsert=True inserts one. Useful for syncing data."],
         code='tickets.update_one({"ticket_no": "T-100"}, {"$set": {"status": "open"}}, upsert=True)'),
    dict(sub="3. Aggregation preview", paras=[
        "The aggregation pipeline groups and counts inside the database, instead of in Python. You will use it on "
        "Day 7 for the SmartDesk analytics endpoint."],
        code='tickets.aggregate([{"$group": {"_id": "$priority", "n": {"$sum": 1}}}])'),
    dict(sub="4. Checking an index is used", paras=[
        "On a real MongoDB, find(...).explain() shows whether a query used an index (IXSCAN) or scanned the whole "
        "collection (COLLSCAN). mongomock does not support explain, so try this on Atlas."]),
    dict(sub="5. Connection strings and secrets", paras=[
        "An Atlas connection string contains a password. Never hard-code it or push it to GitHub. Read it from an "
        "environment variable: os.environ[\"MONGO_URI\"]."]),
    dict(sub="6. Stateless servers", paras=[
        "Good APIs do not remember anything between requests; every request carries what it needs. This lets you "
        "run many copies of a server behind a load balancer."]),
    dict(h="Part C: Check yourself", bullets=[
        "What is the difference between frontend, backend and middleware?",
        "What does BSON add that JSON does not have?",
        "What is the difference between $set and $inc?",
        "Why does every extra index slow down writes a little?",
        "Would you embed or reference a ticket's customer? Why?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Create a free MongoDB Atlas cluster and connect to it using the Option B cell.",
        "Design documents for a movie app: movies, reviews and users. Decide what to embed and what to reference.",
        "Chart SmartDesk tickets per day for a week."],
        after=["**Coming up on Day 5:** REST, HTTP and FastAPI, then Basics assessment 1 (Python, MongoDB, FastAPI core).",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Eight problems. Colab users: use mongomock as in the notebook. VS Code users: use a local "
                    "MongoDB or a free Atlas cluster.", problems=[
    dict(title="Expense Chart", level="Warm-up", concepts="Matplotlib bar chart",
         text="Given categories [\"Food\", \"Rent\", \"Travel\", \"Fun\"] and amounts [6000, 15000, 2500, 3000], draw "
              "a bar chart with a title, axis labels and the value on top of each bar.",
         sample="A bar chart titled \"Monthly expenses\" with 4 labelled bars",
         hints=["ax.bar_label(bars) places the values."]),
    dict(title="Architecture Sketch", level="Easy", concepts="frontend, backend, middleware, layers",
         text="For a telecom support app, write down the clients, at least 5 API endpoints, the middleware checks, the "
              "server layers and the collections. No code needed.",
         sample="Clients: customer app, agent web console\nEndpoints: GET /tickets, POST /tickets, ...\n"
                "Middleware: logging, auth\nCollections: customers, tickets, agents",
         hints=["Think about what each screen in the app needs."]),
    dict(title="Ticket Catalogue: Create and Read", level="Easy", concepts="insert_many, find, filters, projection",
         text="Insert 20 sample tickets with customer, issue, priority, status and created date. Print all open "
              "tickets, all high-priority tickets, and the count of tickets per status.",
         sample="Open: 14\nHigh: Mei, Kenji, Priya ...\nBy status: {'open': 14, 'closed': 6}",
         hints=["{\"priority\": {\"$in\": [\"high\"]}}", "count_documents(filter)"]),
    dict(title="Update and Delete Safely", level="Medium", concepts="update_one, update_many, $set, $push, delete",
         text="Close every ticket older than 7 days, add a \"stale\" tag to them with $push, then delete tickets "
              "marked as test. Print the filter's matches with find before each change.",
         sample="Will close: 5\nClosed: 5\nWill delete: ['TEST-1']\nDeleted: 1",
         hints=["Always run find(filter) before update_many or delete_many."]),
    dict(title="Indexes", level="Medium", concepts="create_index, unique index",
         text="Create an index on status, a compound index on (status, priority) and a unique index on ticket_no. "
              "Show that inserting a duplicate ticket_no raises DuplicateKeyError.",
         sample="Indexes: ['_id_', 'status_1', 'status_1_priority_-1', 'ticket_no_1']\nDuplicateKeyError: ticket_no T-001",
         hints=["from pymongo.errors import DuplicateKeyError"]),
    dict(title="Embed or Reference?", level="Medium", concepts="data modelling",
         text="Design documents for SmartDesk customers, tickets, ticket notes and agents. For each relationship, "
              "decide embed or reference and give a one-line reason. Then insert one example of each.",
         sample="ticket -> notes     : embed (read together, small)\nticket -> customer  : reference (shared by many tickets)",
         hints=["Ask: read together? shared? grows without limit?"]),
    dict(title="SmartDesk: Chart by Priority", level="Challenging", concepts="MongoDB read + Matplotlib",
         text="SmartDesk step 3. Store tickets in a tickets collection. Count open tickets per priority in Python and "
              "draw a bar chart. Save it as tickets_by_priority.png.",
         sample="{'high': 5, 'medium': 6, 'low': 3}\ntickets_by_priority.png saved",
         hints=["Accumulate counts in a dict, then plt.bar(keys, values)."]),
    dict(title="Repository Class", level="Stretch", concepts="OOP + MongoDB, layered design",
         text="Write a TicketRepository with add, get, list_by_status, close and delete. The rest of your code should "
              "only call the repository, never the collection directly.",
         sample='repo = TicketRepository(db["tickets"])\nrepo.add({...})\nrepo.list_by_status("open")',
         hints=["Pass the collection into __init__ so it can be swapped for a real database later."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "The part of an app the user sees is the ________; the part that holds the rules and data is the ________.",
        "Code that runs on every request, such as logging or auth, is called ________.",
        "In Matplotlib, the function ________ draws a line chart.",
        "In MongoDB, a table is called a ________ and a row is called a ________.",
        "MongoDB stores documents internally as ________.",
        "Every MongoDB document has a unique field called ________.",
        "To change a field value in an update, use the operator ________.",
        "To find tickets with more than 3 replies, the filter is {\"replies\": {\"________\": 3}}.",
        "An ________ makes queries on a field fast but slows writes a little.",
        "Data that is read together and small is usually ________; data that is shared is usually ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the client, API, server and database using the restaurant analogy.",
        "When would you choose MongoDB over a SQL database?",
        "Which fields would you index in a SmartDesk tickets collection, and why?",
        "Should a ticket embed or reference its customer? Explain your choice.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'data = [{"n": "A", "p": 50}, {"n": "B", "p": 150}]\nprint([d["n"] for d in data if d["p"] > 100])',
        '# tickets has 3 docs with replies 1, 2, 3\ntickets.update_many({}, {"$inc": {"replies": 2}})\nprint(tickets.count_documents({"replies": {"$gt": 3}}))',
        'doc = {"customer": "Mei", "tags": ["network"]}\ndoc["tags"].append("urgent")\nprint(len(doc["tags"]), doc["tags"][-1])',
    ]),
    dict(title="Section D: MongoDB queries and data modelling", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Insert one ticket document for yourself into a tickets collection."),
        dict(q="Find all open high-priority tickets and print only the customer names."),
        dict(q="Close a ticket by ticket_no, then delete all tickets tagged \"test\"."),
        dict(q="Create a unique index on ticket_no and an index on status."),
        dict(q="Sketch documents for a ticket with embedded notes and a referenced customer."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Frontend, backend and APIs, Matplotlib, NoSQL and BSON, MongoDB CRUD, indexes and data modelling",
                cells=[
    ("md", "## 1. Setup\nColab uses **mongomock**, an in-memory practice MongoDB. VS Code can use a real MongoDB "
           "(local or a free Atlas cluster). The CRUD code is identical."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q mongomock pymongo
import mongomock
client = mongomock.MongoClient()

# ===== Option B: VS Code with real MongoDB (uncomment to use) =====
# %pip install pymongo
# import os
# from pymongo import MongoClient
# uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017")   # or your Atlas URI, from an env variable
# client = MongoClient(uri)

db = client["shop"]
products = db["products"]
products.delete_many({})       # start fresh each run
print("Connected. Collections:", db.list_collection_names())'''),
    ("md", "# Session 1: Architecture and charts\n## 2. A request's journey, in code\nA tiny simulation of client, "
           "middleware, route, service and repository. Each function has one job."),
    ("code", '''FAKE_DB = {"tickets": [{"id": 1, "customer": "Mei", "status": "open"}]}

def repository_list(status):                 # data access only
    return [t for t in FAKE_DB["tickets"] if t["status"] == status]

def service_open_tickets():                  # business rules
    return sorted(repository_list("open"), key=lambda t: t["id"])

def route_get_tickets(request):              # receives the request, returns a response
    return {"status": 200, "body": service_open_tickets()}

def middleware(handler):                     # runs on every request
    def wrapped(request):
        print("LOG", request["method"], request["path"])
        if request.get("token") != "demo":
            return {"status": 401, "body": "unauthorised"}
        return handler(request)
    return wrapped

api = middleware(route_get_tickets)
print(api({"method": "GET", "path": "/tickets", "token": "demo"}))
print(api({"method": "GET", "path": "/tickets"}))'''),
    ("md", "## 3. Matplotlib basics"),
    ("code", '''import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
tickets_2025 = [120, 150, 90, 180, 210, 190]
tickets_2026 = [140, 160, 130, 200, 260, 240]
plt.figure(figsize=(7, 4))
plt.plot(months, tickets_2025, marker="o", label="2025")
plt.plot(months, tickets_2026, marker="o", label="2026")
plt.title("Support tickets per month")
plt.xlabel("Month")
plt.ylabel("Tickets")
plt.legend()
plt.grid(alpha=0.3)
plt.show()'''),
    ("code", '''cats = ["Food", "Rent", "Travel", "Fun"]
amounts = [6000, 15000, 2500, 3000]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
bars = ax1.bar(cats, amounts, color="#0FA3A3")
ax1.bar_label(bars)
ax1.set_title("Expenses by category")
ax2.pie(amounts, labels=cats, autopct="%1.0f%%")
ax2.set_title("Share of spending")
fig.tight_layout()
plt.savefig("expenses.png")
plt.show()'''),
    ("md", "### TODO 1: Plot a histogram of these resolution times (hours) with 5 bins: `[4, 7, 2, 8, 9, 5, 3, 6, 8, 10, 1]`"),
    ("code", "# TODO: write your code here"),
    ("md", "# Session 2: NoSQL and MongoDB\n## 4. Documents, BSON and ObjectId"),
    ("code", '''from bson import ObjectId
from datetime import datetime, timezone

oid = ObjectId()
print("ObjectId:", oid, "| created at:", oid.generation_time)

doc = {"name": "Mechanical Keyboard", "price": 3499, "tags": ["electronics", "office"],
       "stock": {"bengaluru": 12, "tokyo": 4}, "added": datetime.now(timezone.utc)}
result = products.insert_one(doc)
print("Inserted _id:", result.inserted_id, type(result.inserted_id).__name__)
print(products.find_one({"_id": result.inserted_id}, {"_id": 0}))'''),
    ("md", "**MongoDB Compass (optional):** install Compass, paste your Atlas or local connection string, then browse "
           "the `shop` database. In Colab, mongomock lives only in memory, so Compass cannot see it."),
    ("md", "# Session 3: CRUD, indexes and data modelling\n## 5. Create: insert documents"),
    ("code", '''products.delete_many({})
result = products.insert_one({"name": "Pen", "category": "Stationery", "price": 20, "stock": 100})
print("New id:", result.inserted_id)

products.insert_many([
    {"name": "Notebook", "category": "Stationery", "price": 80, "stock": 40},
    {"name": "Mouse", "category": "Electronics", "price": 500, "stock": 15},
    {"name": "Keyboard", "category": "Electronics", "price": 1500, "stock": 4},
    {"name": "Monitor", "category": "Electronics", "price": 9000, "stock": 3},
    {"name": "Mug", "category": "Home", "price": 250, "stock": 0, "tags": ["gift", "kitchen"]},
    {"name": "Lamp", "category": "Home", "price": 1200, "stock": 7},
])
print("Total documents:", products.count_documents({}))'''),
    ("md", "## 6. Read: find with filters and projections"),
    ("code", '''print(products.find_one({"name": "Mouse"}))

print("\\nUnder 1000:")
for p in products.find({"price": {"$lt": 1000}}, {"_id": 0, "name": 1, "price": 1}):
    print(" ", p)

print("\\nElectronics or Home with stock < 5:")
query = {"category": {"$in": ["Electronics", "Home"]}, "stock": {"$lt": 5}}
for p in products.find(query):
    print(" ", p["name"], p["stock"])

print("\\nTop 3 most expensive:")
for p in products.find().sort("price", -1).limit(3):
    print(" ", p["name"], p["price"])'''),
    ("md", "## 7. Update and delete"),
    ("code", '''products.update_one({"name": "Pen"}, {"$set": {"price": 25}})
for p in products.find({"category": "Electronics"}):      # +10% price (mongomock has no $mul)
    products.update_one({"_id": p["_id"]}, {"$set": {"price": round(p["price"] * 1.1)}})
products.update_many({"stock": 0}, {"$set": {"active": False}})
products.update_one({"name": "Mug"}, {"$push": {"tags": "ceramic"}})

print("Will delete:", [p["name"] for p in products.find({"active": False})])   # check first!
res = products.delete_many({"active": False})
print("Deleted:", res.deleted_count, "| Remaining:", products.count_documents({}))'''),
    ("md", "## 8. Indexes\nIndex the fields you filter and sort on. A unique index stops duplicates."),
    ("code", '''from pymongo.errors import DuplicateKeyError

products.create_index("category")
products.create_index([("category", 1), ("price", -1)])
products.create_index("sku", unique=True, sparse=True)
print("Indexes:", list(products.index_information().keys()))

products.update_one({"name": "Pen"}, {"$set": {"sku": "P-100"}})
try:
    products.insert_one({"name": "Pen copy", "category": "Stationery", "price": 20, "stock": 1, "sku": "P-100"})
except DuplicateKeyError:
    print("Blocked duplicate sku P-100")'''),
    ("md", "## 9. Data modelling: embed vs reference\nA ticket **embeds** its notes (small, read together) and "
           "**references** its customer by `_id` (shared by many tickets)."),
    ("code", '''customers = db["customers"]
customers.delete_many({})
mei_id = customers.insert_one({"name": "Mei", "plan": "5G Unlimited", "city": "Osaka"}).inserted_id

ticket = {"customer_id": mei_id,                         # reference
          "issue": "No signal at home", "priority": "high", "status": "open",
          "notes": [{"by": "Kenji", "text": "Checked tower status"},      # embedded
                    {"by": "Kenji", "text": "Asked customer to restart"}]}
tid = db["support"].insert_one(ticket).inserted_id

t = db["support"].find_one({"_id": tid})
c = customers.find_one({"_id": t["customer_id"]})        # second lookup for the reference
print(f'{c["name"]} ({c["plan"]}): {t["issue"]}, {len(t["notes"])} notes')'''),
    ("md", "## 10. From database to chart"),
    ("code", '''value_by_cat = {}
for p in products.find():
    value_by_cat[p["category"]] = value_by_cat.get(p["category"], 0) + p["price"] * p["stock"]
print(value_by_cat)

plt.figure(figsize=(6, 4))
plt.bar(value_by_cat.keys(), value_by_cat.values(), color=["#0FA3A3", "#FF8A3D", "#0B5D63"])
plt.title("Stock value by category")
plt.ylabel("Value")
plt.show()'''),
    ("md", "## 11. SmartDesk step 3: tickets in MongoDB, chart by priority"),
    ("code", '''import random
from datetime import timedelta

tickets = db["tickets"]
tickets.delete_many({})
tickets.create_index("status")
tickets.create_index("ticket_no", unique=True)

random.seed(4)
names = ["Mei", "Ravi", "Aiko", "Kenji", "Priya", "Hana", "Arjun", "Yuki"]
issues = ["No signal at home", "Charged twice", "Cannot log in", "Slow data", "SIM not activated"]
now = datetime.now(timezone.utc)
tickets.insert_many([{
    "ticket_no": f"T-{i:03d}", "customer": random.choice(names), "issue": random.choice(issues),
    "priority": random.choice(["low", "medium", "medium", "high"]),
    "status": random.choice(["open", "open", "closed"]),
    "created": now - timedelta(days=random.randint(0, 14))} for i in range(1, 21)])
print("Tickets:", tickets.count_documents({}), "| open:", tickets.count_documents({"status": "open"}))

counts = {}
for t in tickets.find({"status": "open"}):
    counts[t["priority"]] = counts.get(t["priority"], 0) + 1
order = [p for p in ["high", "medium", "low"] if p in counts]
print({p: counts[p] for p in order})

plt.figure(figsize=(5, 3.5))
bars = plt.bar(order, [counts[p] for p in order], color=["#FF8A3D", "#0FA3A3", "#0B5D63"][:len(order)])
plt.bar_label(bars)
plt.title("Open SmartDesk tickets by priority")
plt.savefig("tickets_by_priority.png")
plt.show()'''),
    ("md", "## 12. A layered design: repository class"),
    ("code", '''class TicketRepository:
    def __init__(self, collection):
        self.col = collection

    def add(self, ticket):
        return self.col.insert_one(ticket).inserted_id

    def list_by_status(self, status):
        return list(self.col.find({"status": status}, {"_id": 0, "ticket_no": 1, "customer": 1}))

    def close(self, ticket_no):
        return self.col.update_one({"ticket_no": ticket_no}, {"$set": {"status": "closed"}}).modified_count

repo = TicketRepository(tickets)
repo.add({"ticket_no": "T-021", "customer": "Mei", "issue": "Roaming not working", "priority": "high",
          "status": "open", "created": now})
print("Open:", len(repo.list_by_status("open")), "| closed T-021:", repo.close("T-021"))'''),
    ("md", "### TODO 2: Add a `delete_by_ticket_no` method to the repository and test it."),
    ("code", "# TODO: write your code here"),
])
