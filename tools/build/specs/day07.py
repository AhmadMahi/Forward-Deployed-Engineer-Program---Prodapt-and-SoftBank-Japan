"""Day 07 spec. FastAPI Advanced, Security and MongoDB.
Source: MERGE archive/v1-40-day/Day08 + Day09 Sessions 1 and 2. NEW (v4) topics are marked.
"""
DAY = 7
FOLDER = "Day07-FastAPI-Advanced-Security-and-MongoDB"
SLUG = "FastAPI_Advanced_Security_and_MongoDB"
TITLE = "FastAPI Advanced, Security and MongoDB"
SUBTITLE = "Dependencies, middleware, JWT and OWASP API Top 10, MongoDB APIs, and a security check for AI-generated code"
DATE = "Tue 03 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 8: JavaScript fundamentals and async JavaScript."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 6"),
        ("Dependencies", "Depends(), middleware, exception handling"),
        ("Security", "JWT, hashing, OWASP API Top 10. NEW (v4)"),
        ("MongoDB APIs", "CRUD, aggregation, pagination"),
        ("NoSQL injection", "Validate every input. NEW (v4)"),
        ("Security check", "bandit, pip-audit, vulnerability report v1. NEW (v4)"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Inject dependencies", "Reuse DB access, settings and auth with Depends(); add middleware."),
        ("Secure endpoints", "Hash passwords, issue short-lived scoped JWTs, map risks to OWASP API Top 10."),
        ("Build Mongo APIs", "CRUD, aggregation and pagination with input validation."),
        ("Check AI code", "Scan with bandit and pip-audit and write a vulnerability report."),
    ]),

    dict(type="section", title="Dependencies, middleware and errors", sub="Session 1 | 1.5 Hrs | Ask for what you need, FastAPI provides it"),
    dict(type="compare", title="Without and with Depends()", left=dict(title="Without", bullets=[
        "Every endpoint opens its own DB connection", "Auth checks copied into each function", "Hard to swap in a fake for tests",
    ]), right=dict(title="With Depends()", bullets=[
        "Write the logic once as a function", "Declare it as a parameter", "FastAPI calls it for you",
        "Override it easily in tests",
    ])),
    dict(type="bullets_code", title="Dependencies, with and without yield", bullets=[
        "A dependency is just a function",
        "Its return value becomes the parameter",
        "Code after yield always runs: clean up",
        "Perfect for database sessions",
    ], code='''from fastapi import Depends, Query

def pagination(skip: int = Query(0, ge=0),
               limit: int = Query(10, ge=1, le=50)):
    return {"skip": skip, "limit": limit}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tickets")
def tickets(page=Depends(pagination), db=Depends(get_db)):
    ...'''),
    dict(type="flow", title="How middleware wraps a request", items=[
        ("Request in", "Middleware sees it first"),
        ("call_next", "Passes it to your endpoint"),
        ("Response", "Comes back through middleware"),
        ("Out", "Headers added, time logged"),
    ], note="Use it for logging, timing, request ids and CORS. Keep it fast."),
    dict(type="bullets_code", title="Middleware and exception handlers", bullets=[
        "@app.middleware(\"http\") wraps every request",
        "Add timing and request id headers",
        "@app.exception_handler turns your errors into clean JSON",
        "Never leak stack traces to clients",
    ], code='''@app.middleware("http")
async def timer(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    response.headers["X-Time-ms"] = f"{ms:.1f}"
    return response

class TicketLocked(Exception): ...

@app.exception_handler(TicketLocked)
def locked(request, exc):
    return JSONResponse(status_code=409,
        content={"detail": "Ticket is closed"})'''),

    dict(type="section", title="Authentication, JWT and API security", sub="Session 2 | 2 Hrs | Proving who you are, safely"),
    dict(type="compare", title="Authentication and authorisation", left=dict(title="Authentication", bullets=[
        "Who are you?", "Login with username and password", "Fails with 401 Unauthorized",
    ]), right=dict(title="Authorisation", bullets=[
        "What are you allowed to do?", "Roles and scopes such as agent or admin", "Fails with 403 Forbidden",
    ])),
    dict(type="table", title="Storing passwords", header=["Approach", "Safe?", "Why"], rows=[
        ["Plain text", "Never", "One leak exposes every account"],
        ["Simple hash (md5, sha1)", "No", "Fast to crack with lookup tables"],
        ["Slow salted hash", "Yes", "bcrypt, argon2, pbkdf2: slow and unique per user"],
    ], note="You can check a password against a hash, but never turn the hash back into the password."),
    dict(type="flow", title="The JWT login flow", greet="Himitsu (秘密): Secret. Keep the signing key safe!", items=[
        ("Login", "POST /token with username and password"),
        ("Verify", "Server checks the password hash"),
        ("Issue", "Server signs and returns a JWT"),
        ("Use", "Authorization: Bearer <token>"),
    ], note="The server checks the signature on every request. No session storage needed."),
    dict(type="bullets_code", title="Short-lived tokens with scopes", new=True, bullets=[
        "exp: 15 minutes, not days",
        "scope lists exactly what the token may do",
        "Check the scope on every protected route",
        "Signing key from the environment, never in code",
    ], code='''def create_token(sub, role, scopes, minutes=15):
    now = dt.datetime.now(dt.timezone.utc)
    return jwt.encode({"sub": sub, "role": role,
        "scope": " ".join(scopes),
        "iat": now,
        "exp": now + dt.timedelta(minutes=minutes)},
        SECRET, algorithm="HS256")

def require_scope(needed):
    def check(user=Depends(current_user)):
        if needed not in user["scopes"]:
            raise HTTPException(403, "Missing scope")
        return user
    return check'''),
    dict(type="table", title="OWASP API Security Top 10 (2023)", new=True, header=["ID", "Risk", "SmartDesk example"], rows=[
        ["API1", "Broken object level authorisation", "Agent reads another customer's ticket by id"],
        ["API2", "Broken authentication", "Tokens that never expire; no lockout"],
        ["API3", "Broken object property level authorisation", "Client sets role=admin when registering"],
        ["API4", "Unrestricted resource consumption", "limit=1000000 on a list endpoint"],
        ["API5", "Broken function level authorisation", "Member calls an admin-only route"],
        ["API6 to API10", "Business flows, SSRF, misconfiguration, inventory, unsafe API use", "Read the full list tonight"],
    ], note="Source: OWASP API Security Project, 2023 edition. Map every finding in your report to one of these."),
    dict(type="cards", title="Three defences you write today", new=True, items=[
        ("Check ownership (API1)", "Filter every query by owner, not only by id."),
        ("Allow-list fields (API3)", "Separate input models; never accept role from the client."),
        ("Cap everything (API4)", "le=50 on limit, max_length on strings, short token expiry."),
    ]),

    dict(type="section", title="FastAPI with MongoDB", sub="Session 3 | 2 Hrs | CRUD, aggregation, pagination"),
    dict(type="table", title="A tickets API on MongoDB", header=["Endpoint", "PyMongo call", "Success"], rows=[
        ["POST /tickets", "insert_one", "201"],
        ["GET /tickets", "find + skip + limit", "200"],
        ["GET /tickets/{id}", "find_one by ObjectId", "200 or 404"],
        ["PATCH /tickets/{id}", "update_one with $set", "200 or 404"],
        ["DELETE /tickets/{id}", "delete_one", "204 or 404"],
    ], note="Always validate the id with ObjectId.is_valid before querying. Convert _id to a string id."),
    dict(type="flow", title="An aggregation pipeline", greet="Shuukei (集計): Totals and summaries", items=[
        ("$match", "Filter documents, like WHERE"),
        ("$group", "Group and total, like GROUP BY"),
        ("$sort", "Order the results"),
        ("$project", "Shape the output fields"),
    ], note="Documents flow through each stage like water through filters."),
    dict(type="bullets_code", title="Tickets by priority, and pagination", bullets=[
        "$group counts per priority",
        "$sort -1 means highest first",
        "Offset pagination: skip and limit",
        "Cap size with Query(le=50)",
    ], code='''pipeline = [
    {"$match": {"status": {"$ne": "closed"}}},
    {"$group": {"_id": "$priority",
                "open": {"$sum": 1}}},
    {"$sort": {"open": -1}},
]
rows = list(tickets.aggregate(pipeline))

cur = (tickets.find().sort("_id", 1)
       .skip((page - 1) * size).limit(size))'''),
    dict(type="compare", title="NoSQL injection", new=True, left=dict(title="Vulnerable", bullets=[
        "Login body accepted as a raw dict", "password: {\"$ne\": \"\"} matches any user",
        "Search builds $regex from raw input", "Attacker logs in without a password",
    ]), right=dict(title="Defended", bullets=[
        "Pydantic model: username and password are str", "Operators in input are rejected with 422",
        "re.escape() user text before $regex", "Never pass request JSON straight into a query",
    ]), note="Same idea as SQL injection: data must never become query syntax."),
    dict(type="bullets_code", title="Input validation stops it at the door", new=True, bullets=[
        "Typed fields reject objects like {\"$ne\": \"\"}",
        "Patterns and lengths limit what is accepted",
        "Escape user text used in $regex",
        "Same 422 for every bad input",
    ], code='''class Login(BaseModel):
    username: str = Field(min_length=3, max_length=30,
                          pattern=r"^[a-z0-9_]+$")
    password: str = Field(min_length=8, max_length=128)

@app.get("/tickets/search")
def search(q: str = Query(min_length=2, max_length=40)):
    rx = {"$regex": re.escape(q), "$options": "i"}
    return [out(d) for d in tickets.find({"title": rx})]'''),

    dict(type="section", title="Security check for AI-generated code", sub="Session 4 | 1 Hr | bandit, pip-audit and vulnerability report v1", new=True),
    dict(type="cards", title="Why scan AI-generated code?", new=True, items=[
        ("It looks confident", "Generated code can include eval, shell=True or hard-coded secrets."),
        ("Old patterns", "Models learned from old code: md5, outdated library versions."),
        ("Supply chain", "A suggested package or pin may have known vulnerabilities."),
        ("You own it", "Whoever merges the code is responsible for it."),
    ]),
    dict(type="compare", title="Two tools, two jobs", new=True, left=dict(title="bandit (SAST)", bullets=[
        "Reads your Python source", "Finds risky patterns: eval, shell=True, md5, secrets",
        "bandit -r app/ -f json", "Severity and confidence per finding",
    ]), right=dict(title="pip-audit (dependencies)", bullets=[
        "Reads requirements.txt", "Checks packages against known vulnerability data",
        "pip-audit -r requirements.txt", "Fix: upgrade to a patched version",
    ])),
    dict(type="table", title="Vulnerability report v1", new=True, header=["Column", "What to write"], rows=[
        ["ID, finding, tool", "V-01, hard-coded secret, bandit B105"],
        ["Severity, affected file", "High, app/security.py:4"],
        ["Proposed fix", "Read SECRET_KEY from the environment"],
        ["Fixed by", "Human or Codex-assisted"],
        ["Verified, evidence", "Yes: re-scan clean, test passes"],
    ], note="Template: shared/templates/Vulnerability_Report_Template.md. You update it on Days 20, 23 to 25 and 30."),

    dict(type="cards", title="SmartDesk step 6: secure SmartDesk", items=[
        ("JWT login with roles", "customer, agent and admin roles; 15 minute scoped tokens."),
        ("Ownership", "Customers see only their own tickets (API1)."),
        ("Mongo analytics", "GET /analytics/by-priority with an aggregation pipeline."),
        ("Report v1", "Run bandit and pip-audit on your Codex-generated code and log every finding."),
    ]),
    dict(type="cards", title="Key takeaways", items=[
        ("Depends()", "Write shared logic once; inject it everywhere; override in tests."),
        ("Security", "Slow salted hashes; short-lived scoped JWTs; OWASP API Top 10 as a checklist."),
        ("MongoDB", "Validate ids and inputs; aggregate in the database; cap page size."),
        ("AI code", "Scan with bandit and pip-audit; record findings in the vulnerability report."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day07_Hotel_Lab.md: post-read, notebook, report v1."),
        ("Workbook", "Complete the Day 7 workbook."),
        ("Pre-read", "Skim the Day 8 pre-read on JavaScript."),
    ]),
]

PREREAD = dict(title="Keys, Guards and Helpers", lede="A light read before Day 7. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "So far, anyone could call your API and do anything. Today you add what every real application needs: shared "
        "helpers, a checkpoint around every request, a secure way to prove who someone is, and a habit of checking "
        "code for security problems, including code written by AI."]),
    dict(h="1. Asking for what you need", paras=[
        "In a hospital, a surgeon does not fetch instruments; they ask and a nurse hands them over. In FastAPI, an "
        "endpoint can simply say \"I need the database\" or \"I need the logged-in user\", and FastAPI hands it over. "
        "This is called **dependency injection**. **Middleware** is the reception desk every request passes."]),
    dict(h="2. Who are you, and what may you do?", table=[
        ["Question", "Name", "Office example", "Error if it fails"],
        ["Who are you?", "Authentication", "Showing your ID at reception", "401"],
        ["What may you do?", "Authorisation", "Your badge opens some doors, not all", "403"],
    ]),
    dict(h="3. Never keep passwords in a drawer", paras=[
        "A responsible company never stores your actual password. It stores a scrambled fingerprint of it, called a "
        "**hash**. If the database is ever stolen, the real passwords are not in it."]),
    dict(h="4. A visitor pass that expires", new=True, paras=[
        "After you log in, the server gives you a **token**: a visitor pass with your name, what you may do (its "
        "**scopes**) and an expiry time, stamped with a seal. A pass that lasts 15 minutes and opens only the doors you "
        "need does far less harm if someone copies it."]),
    dict(h="5. A list of the usual mistakes", new=True, paras=[
        "The **OWASP API Security Top 10** lists the most common ways APIs get attacked, such as reading someone "
        "else's data by changing an id in the URL. Security teams use it as a checklist. So will you."]),
    dict(h="6. Spell-check for security", new=True, paras=[
        "Tools like **bandit** and **pip-audit** read code and its list of libraries, and flag risky patterns and known "
        "vulnerable versions. You run them on everything, including code written by OpenAI Codex, and record what you "
        "find in a **vulnerability report**."],
        box="**Key idea:** code that works is not the same as code that is safe. Check both."),
    dict(h="7. Think about these before class", bullets=[
        "Why do websites ask you to log in again after some time?",
        "What could go wrong if changing /tickets/41 to /tickets/42 in a URL showed someone else's ticket?",
        "Why might a coding assistant suggest an old, unsafe pattern?"],
        after=["Anzen daiichi (安全第一): safety first"]),
])

POSTREAD = dict(title="Advanced FastAPI, Security and MongoDB: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Depends()", "Declare a function as a dependency; yield for setup and clean up; override in tests."],
        ["Middleware and errors", "Wrap every request for timing and ids; exception handlers return clean JSON."],
        ["Authn vs authz", "Who you are (401) vs what you may do (403)."],
        ["Passwords", "Slow, salted hashes (bcrypt, argon2, pbkdf2). Never plain text."],
        ["JWT (NEW v4: scopes)", "Signed, readable, short-lived (exp), with scopes checked per route."],
        ["OWASP API Top 10 (NEW v4)", "API1 object authorisation, API3 property authorisation, API4 resource limits..."],
        ["MongoDB APIs", "Validate ObjectId; aggregation with $match, $group, $sort, $project; skip and limit."],
        ["NoSQL injection (NEW v4)", "Typed Pydantic input; escape regex; never pass raw JSON into a query."],
        ["bandit and pip-audit (NEW v4)", "Scan source and dependencies; log findings in the vulnerability report."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Overriding dependencies in tests", code='''app.dependency_overrides[current_user] = lambda: {"sub": "tester", "role": "admin",
                                                   "scopes": ["tickets:read"]}'''),
    dict(sub="2. Access and refresh tokens", paras=[
        "Short-lived access tokens (15 minutes) limit damage if stolen. A longer-lived refresh token, stored more "
        "carefully and revocable, gets a new access token without logging in again."]),
    dict(sub="3. Secrets belong in the environment", paras=[
        "Load SECRET_KEY and MONGO_URI from environment variables or a git-ignored .env file. bandit flags hard-coded "
        "secrets as B105."]),
    dict(sub="4. Rate limiting", paras=[
        "Protect /token from password guessing by limiting attempts per user or IP (OWASP API4). Libraries such as "
        "slowapi plug into FastAPI."]),
    dict(sub="5. Indexes", paras=[
        "Index the fields you filter and sort on most (status, priority, owner). Faster reads, slightly slower writes."]),
    dict(sub="6. Scanning in CI", paras=[
        "On Day 20 the same bandit and pip-audit commands run in your pipeline as security gates: the build fails until "
        "findings are fixed. That is vulnerability report v2."]),
    dict(h="Part C: Check yourself", bullets=[
        "What runs after the yield in a dependency, and when?",
        "Why must password hashing be slow?",
        "Which OWASP API risk is \"changing the id in the URL shows another user's data\"?",
        "How does {\"$ne\": \"\"} bypass a password check, and how does Pydantic stop it?",
        "What is the difference between what bandit and pip-audit check?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a require_scope(\"tickets:write\") dependency to every write route.",
        "Try three injection payloads against your search and login endpoints and record the results.",
        "Ask Codex to fix one bandit finding, then re-scan and mark it verified in your report."],
        after=["**Coming up on Day 8:** JavaScript fundamentals and async JavaScript.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Nine problems building a secure SmartDesk-style API. mongomock in Colab, a real MongoDB in VS Code.", problems=[
    dict(title="Map the Risks", level="Warm-up", concepts="OWASP API Security Top 10", new=True,
         text="For six SmartDesk scenarios (for example: changing a ticket id in the URL shows another customer's "
              "ticket; limit=100000 on a list; a member calls DELETE /admin/users), name the OWASP API risk and one fix.",
         sample="Change id in URL      -> API1 Broken object level authorisation -> filter by owner\n"
                "limit=100000          -> API4 Unrestricted resource consumption -> Query(le=50)",
         hints=["Use the 2023 list from the deck."]),
    dict(title="Shared Pagination", level="Easy", concepts="Depends(), reusable dependency",
         text="Write a pagination dependency (skip >= 0, limit 1 to 50) and use it on two endpoints. Show that invalid "
              "values return 422.",
         sample='GET /items?skip=0&limit=5 -> {"skip": 0, "limit": 5}\nGET /items?limit=500 -> 422',
         hints=["Use Query() inside the dependency for rules."]),
    dict(title="Timing, Request Id and Clean Errors", level="Easy", concepts="middleware, exception handlers",
         text="Add middleware that sets X-Process-Time-ms and X-Request-ID on every response. Add a custom exception "
              "TicketLocked with a handler that returns 409 and a short message.",
         sample="GET /health 200 1.3 ms  X-Request-ID: 3f2a...\nPATCH closed ticket -> 409 {\"detail\": \"Ticket is closed\"}",
         hints=["import uuid; str(uuid.uuid4())", "@app.exception_handler(TicketLocked)"]),
    dict(title="Hash and Verify", level="Easy", concepts="bcrypt or pbkdf2, salt",
         text="Write hash_password(pw) and verify_password(pw, stored). Show that the same password gives different "
              "hashes for two users.",
         sample='verify_password("secret1", stored) -> True\nverify_password("wrong", stored) -> False',
         hints=["bcrypt.hashpw(pw.encode(), bcrypt.gensalt())"]),
    dict(title="Short-lived Scoped Tokens", level="Medium", concepts="PyJWT, exp, scopes", new=True,
         text="Create tokens with sub, role, scope and a 15 minute expiry. Add require_scope(\"tickets:write\"). Show "
              "a valid token works, an expired token gives 401, and a read-only token gives 403 on a write route.",
         sample="valid write token   -> 201\nexpired token       -> 401\nread-only token     -> 403",
         hints=["Create an expired token with minutes=-1."]),
    dict(title="Protected Tickets in MongoDB", level="Challenging", concepts="current_user, ownership, PyMongo",
         text="Add register, login and GET/POST/DELETE /tickets stored in MongoDB. Each ticket stores its owner; users "
              "see and delete only their own. Registration must not accept a role from the client.",
         sample="Hana sees 2 tickets, Ravi sees 1\nRavi deleting Hana's ticket -> 404\nregister with role=admin -> role stays customer",
         hints=["Filter every query by {\"owner\": user}.", "This is API1 and API3 in practice."]),
    dict(title="Analytics and Pagination", level="Medium", concepts="aggregation, skip and limit",
         text="Add GET /analytics/by-priority (count of open tickets per priority, highest first) and paginate "
              "GET /tickets with page and size (size at most 50), returning items and total.",
         sample='[{"priority": "high", "open": 7}, {"priority": "medium", "open": 4}]\n{"page": 2, "size": 5, "total": 12, ...}',
         hints=["$match, $group, $sort, $project"]),
    dict(title="Break It, Then Fix It: NoSQL Injection", level="Challenging", concepts="NoSQL injection, input validation", new=True,
         text="Run the deliberately vulnerable login and search endpoints from the notebook. Log in as admin without "
              "the password using an operator payload, and dump all tickets with a regex payload. Then fix both with "
              "Pydantic models and re.escape, and prove the payloads now return 422 or no results.",
         sample='vulnerable login {"password": {"$ne": ""}} -> 200 (bad)\nfixed login same payload             -> 422\n'
                'fixed search q=".*"                  -> 0 results',
         hints=["Only ever test injection on your own local code."]),
    dict(title="Vulnerability Report v1", level="Stretch", concepts="bandit, pip-audit, reporting", new=True,
         text="Run bandit on the code you generated with Codex today and pip-audit on its requirements. Record every "
              "finding in the vulnerability report template, fix at least two (Codex-assisted is fine), re-scan, and "
              "mark them verified with evidence.",
         sample="| V-01 | Hard-coded secret | bandit B105 | Low | app/security.py:4 | env var | Codex-assisted | Yes | re-scan clean |",
         hints=["python -m bandit -r app -f json", "pip-audit -r requirements.txt"]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "In FastAPI, shared logic is injected into endpoints with ________().",
        "In a dependency, code after ________ runs as clean up.",
        "Authentication failures return status ________; authorisation failures return ________.",
        "Passwords should be stored as slow, salted ________.",
        "The JWT claim that sets the expiry time is ________.",
        "A JWT claim listing exactly what the token may do is often called ________.",
        "OWASP API1 is Broken ________ Level Authorisation.",
        "MongoDB's _id is an ________ and must be converted to a string for JSON.",
        "The aggregation stage that groups and totals documents is ________.",
        "bandit checks source code; pip-audit checks ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain dependency injection using an everyday example.",
        "Why should access tokens be short-lived and scoped?",
        "Explain NoSQL injection and how input validation prevents it.",
        "Why should you scan code written by OpenAI Codex before you merge it?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'def dep():\n    print("setup")\n    yield 5\n    print("cleanup")\n# endpoint returns the value it receives from dep\n# What prints, and what is returned?',
        'import jwt\nt = jwt.encode({"sub": "ana"}, "k", algorithm="HS256")\ntry:\n    jwt.decode(t, "other", algorithms=["HS256"])\nexcept jwt.InvalidSignatureError:\n    print("invalid")',
        'from pydantic import BaseModel, ValidationError\nclass Login(BaseModel):\n    username: str\n    password: str\ntry:\n    Login(username="admin", password={"$ne": ""})\nexcept ValidationError:\n    print("rejected")',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a middleware that adds an X-Request-ID header to every response."),
        dict(q="Write create_token(sub, scopes) with a 15 minute expiry and a require_scope dependency."),
        dict(q="Write an aggregation pipeline that counts open tickets per priority, highest first."),
        dict(q="Write one row of a vulnerability report for a bandit B602 (shell=True) finding."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Dependencies, middleware, JWT with scopes, OWASP API Top 10, MongoDB APIs, NoSQL injection and bandit", cells=[
    ("md", "## 1. Setup\nColab uses mongomock (in-memory MongoDB). VS Code can use a real MongoDB by setting environment variables."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q fastapi httpx pyjwt bcrypt mongomock pymongo python-multipart bandit pip-audit
import os
os.environ["USE_MOCK"] = "1"

# ===== Option B: VS Code with real MongoDB (uncomment to use) =====
# pip install fastapi uvicorn httpx pyjwt bcrypt pymongo python-multipart bandit pip-audit   (in your terminal)
# import os
# os.environ["USE_MOCK"] = "0"
# os.environ["MONGO_URI"] = "mongodb://localhost:27017"   # or your Atlas URI

os.environ.setdefault("SECRET_KEY", "dev-only-change-me-use-32-plus-random-bytes")   # demo only: use a real secret from .env or Secrets
print("Mock mode:", os.environ["USE_MOCK"])'''),
    ("md", "## 2. Dependency injection basics"),
    ("code", '''from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.testclient import TestClient

demo = FastAPI()

def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=50)):
    return {"skip": skip, "limit": limit}

def get_resource():
    print("  setup: open resource")
    yield {"name": "fake-db"}
    print("  cleanup: close resource")

@demo.get("/items")
def items(page=Depends(pagination), res=Depends(get_resource)):
    return {"page": page, "resource": res["name"]}

c = TestClient(demo)
print(c.get("/items", params={"limit": 5}).json())
print("Invalid limit:", c.get("/items", params={"limit": 500}).status_code)'''),
    ("md", "## 3. Middleware and exception handlers"),
    ("code", '''import time, uuid
from fastapi.responses import JSONResponse

timed = FastAPI()

class TicketLocked(Exception):
    pass

@timed.exception_handler(TicketLocked)
def locked_handler(request, exc):
    return JSONResponse(status_code=409, content={"detail": "Ticket is closed"})

@timed.middleware("http")
async def timing(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time-ms"] = f"{ms:.1f}"
    response.headers["X-Request-ID"] = str(uuid.uuid4())
    print(f"  {request.method} {request.url.path} -> {response.status_code} in {ms:.1f} ms")
    return response

@timed.get("/ping")
def ping():
    return {"pong": True}

@timed.patch("/tickets/{tid}")
def edit(tid: int):
    raise TicketLocked()

tc = TestClient(timed)
r = tc.get("/ping")
print({k: v for k, v in r.headers.items() if k.startswith("x-")})
print(tc.patch("/tickets/1").status_code, tc.patch("/tickets/1").json())'''),
    ("md", "## 4. Password hashing"),
    ("code", '''import bcrypt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, stored: str) -> bool:
    return bcrypt.checkpw(password.encode(), stored.encode())

h1, h2 = hash_password("secret123"), hash_password("secret123")
print("Same password, different hashes:", h1[:20], "...", h2[:20], "...")
print(verify_password("secret123", h1), verify_password("wrong", h1))'''),
    ("md", "## 5. NEW (v4): Short-lived JWTs with scopes"),
    ("code", '''import jwt, datetime as dt
SECRET = os.environ["SECRET_KEY"]

def create_token(sub, role="customer", scopes=("tickets:read",), minutes=15):
    now = dt.datetime.now(dt.timezone.utc)
    payload = {"sub": sub, "role": role, "scope": " ".join(scopes), "iat": now,
               "exp": now + dt.timedelta(minutes=minutes)}
    return jwt.encode(payload, SECRET, algorithm="HS256")

token = create_token("hana", scopes=["tickets:read", "tickets:write"])
print("Decoded:", jwt.decode(token, SECRET, algorithms=["HS256"]))

try:
    jwt.decode(create_token("hana", minutes=-1), SECRET, algorithms=["HS256"])
except jwt.ExpiredSignatureError:
    print("Expired token rejected")
try:
    jwt.decode(token, "a-different-key-that-is-32-bytes-long", algorithms=["HS256"])
except jwt.InvalidSignatureError:
    print("Forged token rejected")'''),
    ("md", "## 6. The secure SmartDesk tickets API (FastAPI + JWT + MongoDB)\n"
           "Ownership checks (OWASP API1), no role from the client (API3), capped page size (API4), "
           "admin-only route (API5), scopes on write routes."),
    ("code", '''%%writefile secure_tickets.py
import datetime as dt, os, re
import bcrypt, jwt
from bson import ObjectId
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

SECRET = os.environ.get("SECRET_KEY", "dev-only-change-me-use-32-plus-random-bytes")
if os.environ.get("USE_MOCK", "1") == "1":
    import mongomock
    client = mongomock.MongoClient()
else:
    from pymongo import MongoClient
    client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017"))
db = client["smartdesk"]
app = FastAPI(title="SmartDesk secure API")

ROLE_SCOPES = {"customer": ["tickets:read", "tickets:write"],
               "agent": ["tickets:read", "tickets:write", "analytics:read"],
               "admin": ["tickets:read", "tickets:write", "analytics:read", "admin"]}

def create_token(sub, role, minutes=15):
    now = dt.datetime.now(dt.timezone.utc)
    return jwt.encode({"sub": sub, "role": role, "scope": " ".join(ROLE_SCOPES[role]),
                       "iat": now, "exp": now + dt.timedelta(minutes=minutes)}, SECRET, algorithm="HS256")

oauth2 = OAuth2PasswordBearer(tokenUrl="token")

def current_user(token: str = Depends(oauth2)):
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid or expired token", headers={"WWW-Authenticate": "Bearer"})
    return {"username": data["sub"], "role": data["role"], "scopes": data["scope"].split()}

def require_scope(needed):
    def check(user=Depends(current_user)):
        if needed not in user["scopes"]:
            raise HTTPException(403, f"Missing scope {needed}")
        return user
    return check

class Register(BaseModel):                       # no role field: clients cannot make themselves admin (API3)
    username: str = Field(min_length=3, max_length=30, pattern=r"^[a-z0-9_]+$")
    password: str = Field(min_length=8, max_length=128)

class TicketIn(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    priority: str = Field(pattern="^(low|medium|high)$")

def out(doc):
    return {"id": str(doc["_id"]), "title": doc["title"], "priority": doc["priority"],
            "status": doc["status"], "owner": doc["owner"]}

@app.post("/register", status_code=201, tags=["Auth"])
def register(user: Register):
    if db.users.find_one({"username": user.username}):
        raise HTTPException(409, "Username already taken")
    db.users.insert_one({"username": user.username, "role": "customer",
                         "password": bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode()})
    return {"username": user.username, "role": "customer"}

@app.post("/token", tags=["Auth"])
def login(form: OAuth2PasswordRequestForm = Depends()):
    u = db.users.find_one({"username": form.username})
    if not u or not bcrypt.checkpw(form.password.encode(), u["password"].encode()):
        raise HTTPException(401, "Wrong username or password")
    return {"access_token": create_token(u["username"], u["role"]), "token_type": "bearer"}

@app.post("/tickets", status_code=201, tags=["Tickets"])
def create_ticket(t: TicketIn, user=Depends(require_scope("tickets:write"))):
    doc = {**t.model_dump(), "status": "open", "owner": user["username"]}
    doc["_id"] = db.tickets.insert_one(doc).inserted_id
    return out(doc)

@app.get("/tickets", tags=["Tickets"])
def my_tickets(page: int = Query(1, ge=1), size: int = Query(10, ge=1, le=50),
               user=Depends(require_scope("tickets:read"))):
    flt = {} if user["role"] in ("agent", "admin") else {"owner": user["username"]}   # API1
    total = db.tickets.count_documents(flt)
    cur = db.tickets.find(flt).sort("_id", 1).skip((page - 1) * size).limit(size)
    return {"page": page, "size": size, "total": total, "items": [out(d) for d in cur]}

@app.delete("/tickets/{tid}", status_code=204, tags=["Tickets"])
def delete_ticket(tid: str, user=Depends(require_scope("tickets:write"))):
    if not ObjectId.is_valid(tid):
        raise HTTPException(404, "Ticket not found")
    res = db.tickets.delete_one({"_id": ObjectId(tid), "owner": user["username"]})   # API1
    if res.deleted_count == 0:
        raise HTTPException(404, "Ticket not found")

@app.get("/tickets/search", tags=["Tickets"])
def search(q: str = Query(min_length=2, max_length=40), user=Depends(require_scope("tickets:read"))):
    rx = {"$regex": re.escape(q), "$options": "i"}
    return [out(d) for d in db.tickets.find({"title": rx, "owner": user["username"]})]

@app.get("/analytics/by-priority", tags=["Analytics"])
def by_priority(user=Depends(require_scope("analytics:read"))):
    rows = db.tickets.aggregate([
        {"$match": {"status": {"$ne": "closed"}}},
        {"$group": {"_id": "$priority", "open": {"$sum": 1}}},
        {"$sort": {"open": -1}},
        {"$project": {"_id": 0, "priority": "$_id", "open": 1}},
    ])
    return list(rows)'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
import importlib, secure_tickets
importlib.reload(secure_tickets)
api = TestClient(secure_tickets.app)

# ===== Option B: VS Code =====
# Terminal: uvicorn secure_tickets:app --reload
# Open /docs, use POST /register, then the green Authorize button to log in.

for u in ["hana", "ravi"]:
    print(api.post("/register", json={"username": u, "password": u + "-pass-123"}).json())
print("Try to self-register as admin:",
      api.post("/register", json={"username": "mallory", "password": "mallory-pass", "role": "admin"}).json())
secure_tickets.db.users.insert_one({"username": "agent1", "role": "agent",
    "password": secure_tickets.bcrypt.hashpw(b"agent-pass-123", secure_tickets.bcrypt.gensalt()).decode()})

def login(u, p):
    r = api.post("/token", data={"username": u, "password": p})
    return {"Authorization": f"Bearer {r.json()['access_token']}"} if r.status_code == 200 else r.status_code

print("Wrong password:", login("hana", "nope"))
hana, ravi, agent = login("hana", "hana-pass-123"), login("ravi", "ravi-pass-123"), login("agent1", "agent-pass-123")'''),
    ("code", '''t1 = api.post("/tickets", json={"title": "No signal at home", "priority": "high"}, headers=hana).json()
api.post("/tickets", json={"title": "Charged twice", "priority": "medium"}, headers=hana)
api.post("/tickets", json={"title": "SIM not activated", "priority": "high"}, headers=ravi)

print("Hana sees:", [t["title"] for t in api.get("/tickets", headers=hana).json()["items"]])
print("Ravi sees:", [t["title"] for t in api.get("/tickets", headers=ravi).json()["items"]])
print("No token:", api.get("/tickets").status_code)
print("Ravi deletes Hana's ticket (API1):", api.delete(f"/tickets/{t1['id']}", headers=ravi).status_code)
print("Page size 1000 (API4):", api.get("/tickets", params={"size": 1000}, headers=hana).status_code)
print("Customer on analytics (scope):", api.get("/analytics/by-priority", headers=hana).status_code)
print("Agent analytics:", api.get("/analytics/by-priority", headers=agent).json())'''),
    ("md", "### Testing with dependency overrides"),
    ("code", '''app = secure_tickets.app
app.dependency_overrides[secure_tickets.current_user] = lambda: {
    "username": "tester", "role": "admin", "scopes": secure_tickets.ROLE_SCOPES["admin"]}
print(TestClient(app).get("/analytics/by-priority").status_code)   # no token needed in tests
app.dependency_overrides.clear()
print(TestClient(app).get("/analytics/by-priority").status_code)   # back to normal: 401'''),
    ("md", "## 7. NEW (v4): NoSQL injection, break it then fix it\n"
           "The app below is **deliberately vulnerable**. It accepts raw JSON and passes it into queries. "
           "Only ever try this against your own local code."),
    ("code", '''import mongomock
from fastapi import Body

weak_db = mongomock.MongoClient()["weak"]
weak_db.users.insert_one({"username": "admin", "password": "S3cret-not-hashed"})
weak_db.tickets.insert_many([{"title": "Router reset", "owner": "hana"},
                             {"title": "VIP outage at HQ", "owner": "admin"}])
weak = FastAPI()

@weak.post("/login")
def weak_login(body: dict = Body(...)):                       # raw dict: any shape accepted
    user = weak_db.users.find_one({"username": body.get("username"), "password": body.get("password")})
    return {"ok": bool(user)}

@weak.get("/search")
def weak_search(q: str):
    return [t["title"] for t in weak_db.tickets.find({"title": {"$regex": q}}, {"_id": 0})]

w = TestClient(weak)
print("Operator payload login:", w.post("/login", json={"username": "admin", "password": {"$ne": ""}}).json())
print("Regex payload search:", w.get("/search", params={"q": ".*"}).json())'''),
    ("code", '''import re
from pydantic import BaseModel, Field

class Login(BaseModel):
    username: str = Field(min_length=3, max_length=30, pattern=r"^[a-z0-9_]+$")
    password: str = Field(min_length=8, max_length=128)

fixed = FastAPI()

@fixed.post("/login")
def fixed_login(body: Login):
    user = weak_db.users.find_one({"username": body.username})
    return {"ok": bool(user) and user["password"] == body.password}   # demo only: real code checks a hash

@fixed.get("/search")
def fixed_search(q: str = Query(min_length=2, max_length=40)):
    rx = {"$regex": re.escape(q), "$options": "i"}
    return [t["title"] for t in weak_db.tickets.find({"title": rx, "owner": "hana"}, {"_id": 0})]

f = TestClient(fixed)
print("Operator payload login:", f.post("/login", json={"username": "admin", "password": {"$ne": ""}}).status_code)
print("Regex payload search:", f.get("/search", params={"q": ".*"}).json())
print("Normal search:", f.get("/search", params={"q": "router"}).json())'''),
    ("md", "### TODO 1: Add a third payload of your own (for example `{\"$gt\": \"\"}`) and show that the fixed app rejects it."),
    ("code", "# TODO: write your code here"),
    ("md", "## 8. NEW (v4): Security check for AI-generated code with bandit\n"
           "This file imitates code an assistant might produce in a hurry. bandit reads the source and flags risky patterns."),
    ("code", '''%%writefile ai_generated_helpers.py
import hashlib
import subprocess

SECRET_KEY = "super-secret-123"


def run_report(name):
    return subprocess.run(f"python make_report.py {name}", shell=True)


def fingerprint(password):
    return hashlib.md5(password.encode()).hexdigest()


def calculate(expr):
    return eval(expr)'''),
    ("code", '''import json, subprocess, sys
res = subprocess.run([sys.executable, "-m", "bandit", "-q", "-f", "json", "ai_generated_helpers.py"],
                     capture_output=True, text=True)
findings = json.loads(res.stdout)["results"]
for f_ in findings:
    print(f"{f_['test_id']}  {f_['issue_severity']:<6} line {f_['line_number']:<3} {f_['issue_text'][:70]}")'''),
    ("md", "## 9. NEW (v4): Dependency check with pip-audit\n"
           "pip-audit checks pinned packages against known vulnerability data. It needs internet, so this cell is "
           "optional in the offline check. Old pins such as `PyYAML==5.3.1` are reported with an advisory id and a "
           "fixed version to upgrade to."),
    ("code", '''%%writefile requirements_demo.txt
fastapi
PyYAML==5.3.1'''),
    ("code", '''# ===== Option A: Google Colab =====
!pip-audit --no-deps --disable-pip -r requirements_demo.txt

# ===== Option B: VS Code terminal =====
# pip-audit --no-deps --disable-pip -r requirements_demo.txt''', ["skip-offline-check"]),
    ("md", "## 10. NEW (v4): Vulnerability report v1\n"
           "Turn the findings into rows of the report. Columns follow `shared/templates/Vulnerability_Report_Template.md`."),
    ("code", '''FIXES = {"B105": "Read SECRET_KEY from the environment", "B602": "Pass a list and shell=False",
         "B324": "Use bcrypt for passwords (sha256 for non-security ids)", "B307": "Use ast.literal_eval or a parser",
         "B404": "Keep subprocess, but never with shell=True"}
rows = ["| ID | Finding | Tool | Severity | Affected file | Proposed fix | Fixed by | Verified | Evidence |",
        "|---|---|---|---|---|---|---|---|---|"]
for i, f_ in enumerate(findings, 1):
    rows.append(f"| V-{i:02d} | {f_['issue_text'][:45]} | bandit {f_['test_id']} | {f_['issue_severity'].title()} | "
                f"{f_['filename']}:{f_['line_number']} | {FIXES.get(f_['test_id'], 'Review')} | (human or Codex-assisted) | No | |")
report = "# Vulnerability report v1\\n\\n" + "\\n".join(rows)
open("vulnerability_report_v1.md", "w").write(report)
print(report)'''),
    ("md", "### TODO 2: Fix two findings in `ai_generated_helpers.py` (you may ask Codex), re-run the bandit cell, "
           "and update the Verified and Evidence columns."),
    ("code", "# TODO: write your code here"),
])
