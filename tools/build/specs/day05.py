"""Day 05 spec. API Fundamentals and FastAPI Core (Assessment day).
Source: MERGE archive/v1-40-day/Day05 + Day06 Sessions 1 to 3. NEW (v4) topics are marked.
"""
DAY = 5
FOLDER = "Day05-API-Fundamentals-and-FastAPI-Core"
SLUG = "API_Fundamentals_and_FastAPI_Core"
TITLE = "API Fundamentals and FastAPI Core"
SUBTITLE = "REST, HTTP and status codes, then FastAPI routing, parameters, Pydantic models and CRUD"
DATE = "Fri 30 Oct 2026"
TRACK = "Basics"
NEXT = "See you on Monday for Day 6: SQLAlchemy, relationships and API docs."
CLOSING_GREET = "Yoi shuumatsu wo (良い週末を): Have a great weekend"

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 4"),
        ("REST and HTTP", "Methods, status codes, the request-response lifecycle"),
        ("FastAPI setup", "Uvicorn, routing, path and query parameters"),
        ("Pydantic and CRUD", "Data contracts and a full in-memory API"),
        ("Codex endpoint", "Generate, review and test. NEW (v4)"),
        ("Assessment", "Basics assessment 1, 1.5 hours"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain REST", "Describe resources, URLs, methods and stateless requests."),
        ("Use HTTP well", "Pick the right method and status code for each action."),
        ("Build a FastAPI app", "Routes, path and query parameters, Pydantic models, full CRUD."),
        ("Review AI code", "Generate an endpoint with Codex, then review and test every line."),
    ]),

    dict(type="section", title="How the web talks", sub="Session 1 | 1 Hr | REST, HTTP methods and status codes"),
    dict(type="flow", title="Anatomy of an HTTP exchange", items=[
        ("Method", "What to do: GET, POST..."),
        ("URL", "Which resource: /products/42"),
        ("Headers", "Extra info: content type, auth"),
        ("Body", "Data sent, usually JSON"),
        ("Response", "Status code + JSON body"),
    ], note="The request-response lifecycle: client sends, server validates, acts, and replies with a status code."),
    dict(type="bullets_code", title="A request and a response", bullets=[
        "The request line holds method and path",
        "Headers describe the content",
        "The body carries JSON data",
        "The response starts with a status code",
    ], code='''POST /products HTTP/1.1
Host: api.shop.com
Content-Type: application/json

{"name": "Pen", "price": 20}

HTTP/1.1 201 Created
Content-Type: application/json

{"id": 7, "name": "Pen", "price": 20}'''),
    dict(type="cards", title="Five REST ideas", items=[
        ("Resources", "Everything is a noun: products, orders, users."),
        ("URLs identify", "/products/42 points to one product."),
        ("Methods act", "The HTTP method says what to do with it."),
        ("Stateless", "Each request carries all it needs."),
        ("JSON in and out", "A common, readable format for data."),
        ("Consistent", "Same patterns everywhere, fewer surprises."),
    ]),
    dict(type="table", title="HTTP methods and CRUD", header=["Method", "CRUD", "Example", "Has body?"], rows=[
        ["GET", "Read", "GET /products", "No"],
        ["POST", "Create", "POST /products", "Yes"],
        ["PUT", "Replace", "PUT /products/42", "Yes"],
        ["PATCH", "Partial update", "PATCH /products/42", "Yes"],
        ["DELETE", "Delete", "DELETE /products/42", "Usually no"],
    ], note="GET must never change data. GET, PUT and DELETE are idempotent; POST is not."),
    dict(type="compare", title="Good and poor URL design", left=dict(title="Avoid", bullets=[
        "/getAllProducts", "/createProduct", "/deleteProduct?id=42", "/Products_List",
    ]), right=dict(title="Prefer", bullets=[
        "GET /products", "POST /products", "DELETE /products/42", "Plural nouns, lowercase, no verbs",
    ])),
    dict(type="table", title="Status codes you will use daily", header=["Code", "Meaning", "When"], rows=[
        ["200 OK", "Success", "GET, PUT, PATCH worked"],
        ["201 Created", "New resource made", "POST worked"],
        ["204 No Content", "Success, nothing to return", "DELETE worked"],
        ["400 / 422", "Bad request or invalid data", "Missing or wrong fields"],
        ["401 / 403", "Not logged in / not allowed", "Auth problems"],
        ["404 Not Found", "Resource does not exist", "Wrong id"],
        ["5xx", "Server error", "We broke something"],
    ], note="The first digit tells you who should fix it: 2xx fine, 4xx the client, 5xx the server."),

    dict(type="section", title="FastAPI setup and routing", sub="Session 2 | 2 Hrs | Uvicorn, routes, path and query parameters"),
    dict(type="cards", title="Why FastAPI?", items=[
        ("Type hints", "Uses the Python type hints you met on Day 2."),
        ("Auto validation", "Bad data is rejected with clear 422 errors."),
        ("Free docs", "Interactive Swagger page at /docs."),
        ("Fast", "One of the quickest Python frameworks."),
    ]),
    dict(type="flow", title="Setting up FastAPI", items=[
        ("Install", "pip install fastapi uvicorn"),
        ("Write", "main.py with app = FastAPI()"),
        ("Run", "uvicorn main:app --reload"),
        ("Open", "127.0.0.1:8000/docs"),
    ], note="In Colab we test with TestClient, which calls the API without a running server."),
    dict(type="bullets_code", title="Your first API", greet="Kantan (簡単): Easy! That is a complete API.", bullets=[
        "app = FastAPI() creates the application",
        "@app.get is a decorator (Day 3)",
        "The function's return becomes JSON",
        "Path parameters come from the URL",
    ], code='''from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, API"}

@app.get("/products/{pid}")
def get_product(pid: int):
    return {"id": pid, "name": "Pen"}'''),
    dict(type="table", title="Three kinds of parameters", header=["Kind", "Where it lives", "Use it for", "Example"], rows=[
        ["Path", "In the URL path", "Identify one resource", "/books/{book_id}"],
        ["Query", "After ? in the URL", "Filter, sort, paginate", "/books?author=Ito"],
        ["Body", "JSON in the request", "Data to create or update", '{"title": "..."}'],
    ], note="FastAPI decides by type: simple types not in the path are query; Pydantic models are body."),
    dict(type="bullets_code", title="Path and query parameters", bullets=[
        "Path params are required",
        "Query params with defaults are optional",
        "None means not provided",
        "Query() adds rules like ge and le",
    ], code='''from fastapi import Query

@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {"id": book_id}

@app.get("/books")
def list_books(
    author: str | None = None,
    limit: int = Query(10, ge=1, le=100),
):
    return {"author": author, "limit": limit}'''),
    dict(type="bullets_code", title="APIRouter and the right status code", bullets=[
        "One router per resource, with a prefix and tags",
        "Set status_code on the decorator",
        "Raise HTTPException for errors",
        "FastAPI turns it into a JSON error",
    ], code='''from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/quotes", tags=["Quotes"])
quotes = {1: "Small steps every day."}

@router.get("/{qid}")
def read(qid: int):
    if qid not in quotes:
        raise HTTPException(404, "Quote not found")
    return {"id": qid, "text": quotes[qid]}

app.include_router(router)'''),

    dict(type="section", title="Pydantic models and CRUD", sub="Session 3 | 2 Hrs | Data contracts and an in-memory API"),
    dict(type="compare", title="Why a data contract?", left=dict(title="Plain dict", bullets=[
        "Any field, any type, anything goes", "Bugs appear deep in the code", "No documentation for clients",
    ]), right=dict(title="Pydantic model", bullets=[
        "Fields and types are declared", "Bad data rejected at the door with 422", "Shows up in /docs automatically",
    ])),
    dict(type="bullets_code", title="Request and response models", bullets=[
        "Inherit from BaseModel",
        "Field() adds rules and examples",
        "response_model shapes what is returned",
        "Invalid input never reaches your code",
    ], code='''from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str
    pages: int = Field(gt=0)

class Book(BookCreate):
    id: int

@app.post("/books", response_model=Book,
          status_code=201)
def create(data: BookCreate):
    book = Book(id=len(books) + 1, **data.model_dump())
    books[book.id] = book
    return book'''),
    dict(type="cards", title="Separate models for separate jobs", lead="This pattern protects private fields and keeps clients simple.", items=[
        ("Create", "What the client sends to create: no id."),
        ("Update", "All fields optional for PATCH."),
        ("Response", "What we send back: with id, never passwords."),
    ]),
    dict(type="table", title="A complete books API", header=["Method and path", "Body", "Success", "Errors"], rows=[
        ["GET /books", "None", "200 list", "None"],
        ["GET /books/{id}", "None", "200 Book", "404"],
        ["POST /books", "BookCreate", "201 Book", "422"],
        ["PATCH /books/{id}", "BookUpdate", "200 Book", "404, 422"],
        ["DELETE /books/{id}", "None", "204", "404"],
    ]),
    dict(type="bullets_code", title="Partial updates with PATCH", greet="Renshuu (練習): Practice. Try sending only one field!", bullets=[
        "Update model has all fields optional",
        "exclude_unset keeps only sent fields",
        "model_copy(update=...) merges them",
        "404 if the id does not exist",
    ], code='''class BookUpdate(BaseModel):
    title: str | None = None
    pages: int | None = Field(default=None, gt=0)

@app.patch("/books/{bid}", response_model=Book)
def update(bid: int, data: BookUpdate):
    if bid not in books:
        raise HTTPException(404, "Book not found")
    ch = data.model_dump(exclude_unset=True)
    books[bid] = books[bid].model_copy(update=ch)
    return books[bid]'''),

    dict(type="section", title="Generate an endpoint with Codex", sub="Session 3 | Review it, test it, own it", new=True),
    dict(type="flow", title="Describe, generate, review, test", new=True, items=[
        ("Describe", "Method, path, models, status codes, errors"),
        ("Generate", "Codex writes one endpoint, not the app"),
        ("Review", "Read every line of the diff"),
        ("Test", "TestClient: happy path and errors"),
        ("Accept", "Only code you can explain"),
    ], note="Small, specific prompts give small, reviewable diffs and use fewer tokens."),
    dict(type="code", title="A good prompt for Codex", new=True, code='''Add a PATCH /books/{book_id} endpoint to app/main.py.
- Body: BookUpdate (all fields optional). Use model_dump(exclude_unset=True).
- 404 with detail "Book not found" if the id is missing.
- Return the updated Book with status 200.
- Do not change any other endpoint.
- Add three TestClient tests: one field updated, unknown id, invalid pages (0).''',
         note="Name the file, the contract, the errors and the tests. Never paste keys or customer data."),
    dict(type="cards", title="Review checklist for AI-generated endpoints", new=True, items=[
        ("Contract", "Right method, path, status codes and response model?"),
        ("Validation", "Pydantic rules match the business rules?"),
        ("Errors", "404 and 422 handled, no stack traces leaked?"),
        ("Side effects", "Did it change files or endpoints you did not ask for?"),
        ("Tests", "Do the tests fail when the code is wrong?"),
        ("Explain it", "Can you explain every line to a teammate?"),
    ]),
    dict(type="compare", title="A typical bug Codex can write", new=True, left=dict(title="Generated", bullets=[
        "ch = data.model_dump()", "Sends None for every field not supplied", "PATCH {pages: 250} wipes the title",
    ]), right=dict(title="Reviewed", bullets=[
        "ch = data.model_dump(exclude_unset=True)", "Only fields the client sent are changed",
        "A test proves the title survives",
    ]), note="It runs, it looks right, and it is wrong. Tests catch it; reading the diff catches it sooner."),

    dict(type="cards", title="SmartDesk step 4: FastAPI ticket API", items=[
        ("Goal", "Turn the SmartDesk tickets into a REST API."),
        ("Models", "TicketCreate, TicketUpdate and Ticket with Pydantic rules."),
        ("Endpoints", "Full CRUD under /tickets with the right status codes."),
        ("Build with Codex", "Use Day05_App_Build_Prompts.md. Review every line."),
    ]),
    dict(type="callout", title="Assessment: Basics assessment 1", text="1.5 hours. MCQs and short coding tasks on Python basics, OOP, MongoDB and FastAPI core.",
         sub="Read every question twice. Attempt everything; partial answers still earn marks.",
         greet="Ganbatte kudasai (頑張ってください): Please do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("HTTP and REST", "Nouns in URLs, methods for actions, stateless requests, clear status codes."),
        ("FastAPI", "Decorated functions become endpoints with free docs."),
        ("Pydantic", "Models validate input and shape output; separate Create, Update, Response."),
        ("Codex", "Small prompts, read every diff, prove it with tests."),
    ]),
    dict(type="cards", title="Before Monday", lead="Monday starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day05_Hotel_Lab.md: post-read, notebook, problems."),
        ("Workbook", "Complete the Day 5 workbook."),
        ("Pre-read", "Skim the Day 6 pre-read on relationships and docs."),
    ]),
]

PREREAD = dict(title="The Web's Postal Service", lede="A light read before Day 5. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Yesterday you saw that clients talk to servers through APIs. Today you learn the language they speak, called "
        "HTTP, the rules that make an API pleasant to use, called REST, and you build your first API with FastAPI. "
        "Today also includes Basics assessment 1."]),
    dict(h="1. HTTP is like sending a letter", table=[
        ["Letter", "HTTP request", "Example"],
        ["Address on the envelope", "URL", "shop.com/products/42"],
        ["What you want done", "Method", "Please send me (GET), please add (POST)"],
        ["Notes on the envelope", "Headers", "Language, who you are"],
        ["The letter inside", "Body", "Details of a new order"],
        ["The reply letter", "Response", "Status code plus the information"],
    ]),
    dict(h="2. Five common requests", bullets=[
        "**GET:** show me something. Like looking at a menu.",
        "**POST:** create something new. Like placing an order.",
        "**PUT:** replace something completely. Like rewriting your address.",
        "**PATCH:** change one detail. Like fixing a typo in your address.",
        "**DELETE:** remove something. Like cancelling an order."]),
    dict(h="3. The reply always starts with a number", paras=[
        "Every response comes with a three digit status code. You already know one: 404 Not Found."],
        table=[["Starts with", "Meaning", "Everyday version"], ["2", "Success", "Your parcel was delivered."],
               ["4", "Your mistake", "Wrong address on the parcel."], ["5", "Their mistake", "The post office lost it."]]),
    dict(h="4. Forms with rules", paras=[
        "A good booking form refuses \"abc\" as the number of guests. In FastAPI, a tool called **Pydantic** lets you "
        "write these rules once. Bad data is turned away at the door, with a clear message explaining why."],
        box="**Key idea:** describe the shape of your data once, and let the tool check every request for you."),
    dict(h="5. A helper that writes code", new=True, paras=[
        "Today you ask **OpenAI Codex** to write one endpoint for you. Think of it as a fast junior colleague: helpful, "
        "but you check its work. You read every line, run the tests, and only keep code you can explain."]),
    dict(h="6. About today's assessment", paras=[
        "Today includes a 1.5 hour assessment on Python, OOP, MongoDB and FastAPI basics. Revise your post-reads and "
        "workbooks, and re-run the notebooks. Focus on understanding, not memorising."]),
    dict(h="7. Think about these before class", bullets=[
        "When you search on a shopping site, which request type do you think your browser sends?",
        "What status code might you get if you try to open someone else's private account page?",
        "If a helper wrote code for you, how would you check it is correct?"],
        after=["Ganbatte kudasai (頑張ってください): please do your best, for the assessment"]),
])

POSTREAD = dict(title="APIs and FastAPI Core: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["HTTP request and response", "Method + URL + headers + optional body; status code + JSON back."],
        ["REST", "Plural nouns, methods as verbs, stateless, consistent."],
        ["Status codes", "200, 201, 204, 400/422, 401/403, 404, 5xx."],
        ["FastAPI", "app = FastAPI(); @app.get(...) decorators; uvicorn main:app --reload; /docs."],
        ["Parameters", "Path identifies, query filters, body carries data. Query() adds rules."],
        ["APIRouter", "Group routes by feature with prefix and tags, then include_router."],
        ["Pydantic", "BaseModel with typed fields; Field() for rules; invalid data returns 422."],
        ["PATCH pattern", "model_dump(exclude_unset=True) then model_copy(update=...)."],
        ["Codex review (NEW v4)", "Small prompt, read every diff, prove it with TestClient tests."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Idempotency explained", paras=[
        "Pressing \"pay\" twice should not charge twice. PUT and DELETE are idempotent; POST is not, so real payment "
        "APIs accept an idempotency key header to detect duplicates."]),
    dict(sub="2. Custom validators", code='''from pydantic import BaseModel, field_validator

class BookCreate(BaseModel):
    isbn: str

    @field_validator("isbn")
    @classmethod
    def check_isbn(cls, v):
        if len(v.replace("-", "")) != 13:
            raise ValueError("ISBN must have 13 digits")
        return v'''),
    dict(sub="3. Enums for fixed choices", paras=[
        "class Genre(str, Enum) with a fixed list of values: only listed values are accepted, and /docs shows a dropdown."]),
    dict(sub="4. API versioning", paras=[
        "Prefix routes with /v1 so you can change things later without breaking existing apps."]),
    dict(sub="5. Tests as a safety net for AI code", paras=[
        "Write the test before you ask Codex for the endpoint. If the generated code passes a test you wrote yourself, "
        "you have real evidence. If you let Codex write both, read the tests extra carefully: a test that cannot fail "
        "proves nothing."]),
    dict(h="Part C: Check yourself", bullets=[
        "Which method would you use to change only the price of a product?",
        "What is the difference between 401 and 403?",
        "How does FastAPI decide whether a parameter is path, query or body?",
        "Why do we use separate Create and Response models?",
        "Name two things you check in every Codex diff."]),
    dict(h="Part D: Practice ideas for the weekend", bullets=[
        "Add GET /quotes/random and POST /quotes returning 201; return 404 for unknown ids.",
        "Add a genre Enum and a validator that rejects titles in all capitals.",
        "Ask Codex for one endpoint, then write a test that would have caught a mistake in it."],
        after=["**Coming up on Day 6:** SQLAlchemy models, relationships, transactions and Swagger docs.",
               "Yoi shuumatsu wo (良い週末を): have a great weekend"]),
])

HANDSON = dict(lede="Eight problems. Use TestClient in Colab, or run uvicorn and use /docs in VS Code.", problems=[
    dict(title="Design the Endpoints", level="Warm-up", concepts="REST design, methods, status codes",
         text="For a library app with books and members, list 8 endpoints with method, URL, purpose and success status "
              "code. No code needed.",
         sample="GET /books           list books      200\nPOST /books          add a book      201\n"
                "DELETE /books/{id}   remove a book   204",
         hints=["Use plural nouns and no verbs in URLs."]),
    dict(title="Hello API", level="Easy", concepts="FastAPI setup, GET",
         text="Create a FastAPI app with GET / returning a welcome message and GET /health returning {\"status\": "
              "\"ok\"}. Run it and open /docs.",
         sample='GET /health -> 200 {"status": "ok"}',
         hints=["uvicorn main:app --reload", "In Colab: TestClient(app).get(\"/health\").json()"]),
    dict(title="Parameters Playground", level="Easy", concepts="path, query, Query()",
         text="Add GET /square/{n} returning n and n squared, and GET /books with an optional author and a limit "
              "between 1 and 50 (default 10). Try invalid values and note the status codes.",
         sample='GET /square/7 -> {"n": 7, "square": 49}\nGET /square/abc -> 422\nGET /books?limit=500 -> 422',
         hints=["limit: int = Query(10, ge=1, le=50)"]),
    dict(title="Quotes API", level="Medium", concepts="GET list, GET by id, 404, POST 201, DELETE 204",
         text="Store 5 quotes in a dict. Add GET /quotes, GET /quotes/{id} (404 if missing), GET /quotes/random, "
              "POST /quotes (201) and DELETE /quotes/{id} (204).",
         sample='GET /quotes/99 -> 404 {"detail": "Quote not found"}\nDELETE /quotes/6 -> 204',
         hints=["Put /quotes/random above /quotes/{qid} so it matches first."]),
    dict(title="Book Models", level="Easy", concepts="Pydantic BaseModel, Field",
         text="Define BookCreate (title min 1 char, author, pages > 0, year between 1450 and 2026), BookUpdate (all "
              "optional) and Book (adds id). Create valid and invalid objects and print the errors.",
         sample='BookCreate(title="", ...) -> ValidationError: title too short',
         hints=["from pydantic import ValidationError"]),
    dict(title="Books CRUD", level="Challenging", concepts="POST body, response_model, PATCH, 404, APIRouter",
         text="Build full CRUD for books in a dict, on an APIRouter with prefix /books and tag Books. PATCH must change "
              "only the fields sent.",
         sample="PATCH /books/1 {\"pages\": 250} -> 200 with only pages changed\nGET /books/99 -> 404",
         hints=["data.model_dump(exclude_unset=True)"]),
    dict(title="Review a Codex Endpoint", level="Medium", concepts="AI code review, tests", new=True,
         text="Ask OpenAI Codex for a DELETE /books/{id} endpoint using a precise prompt (method, path, status codes, "
              "errors, tests). Review the diff with the checklist from class. Write down one thing you changed or "
              "confirmed, and add a test that fails if the endpoint returns 200 instead of 204.",
         sample="Review note: Codex returned 200 with a body; changed to status_code=204.\n"
                "test_delete_returns_204 ... passed\ntest_delete_unknown_404 ... passed",
         hints=["Ask for one endpoint at a time.", "Run the test against the unreviewed code first. Does it fail?"]),
    dict(title="Test Everything", level="Stretch", concepts="TestClient, assertions",
         text="Write at least 10 assert-based tests with TestClient that check status codes and bodies for all your "
              "endpoints, including error cases.",
         sample="assert client.get(\"/books/99\").status_code == 404\nAll 10 tests passed",
         hints=["from fastapi.testclient import TestClient"]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "HTTP stands for HyperText Transfer ________.",
        "The method used to read data without changing it is ________.",
        "The method that updates only some fields is ________.",
        "Status code ________ means a new resource was created.",
        "Status codes starting with 5 mean a ________ error.",
        "In REST, URLs should use plural ________, not verbs.",
        "To run a FastAPI app in development, use uvicorn main:app ________.",
        "Parameters after the ? in a URL are called ________ parameters.",
        "When Pydantic rejects data, FastAPI returns status code ________.",
        "model_dump(________=True) keeps only fields the client sent.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the parts of an HTTP request using the letter analogy.",
        "Explain path, query and body parameters with your own example.",
        "Why should a Response model not include a password field?",
        "You asked Codex for an endpoint and it runs. What else must you check before accepting it?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'from fastapi import FastAPI\nfrom fastapi.testclient import TestClient\napp = FastAPI()\n@app.get("/double/{n}")\n'
        'def d(n: int):\n    return {"r": n * 2}\nprint(TestClient(app).get("/double/21").json())\n'
        'print(TestClient(app).get("/double/x").status_code)',
        'from pydantic import BaseModel\nclass P(BaseModel):\n    name: str\n    qty: int = 1\nprint(P(name="Pen").model_dump())',
        'class U(BaseModel):\n    a: int | None = None\n    b: int | None = None\nprint(U(a=5).model_dump(exclude_unset=True))',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a FastAPI endpoint GET /greet/{name} that returns a greeting."),
        dict(q="Write a Pydantic model Student with name, age (>= 16) and email."),
        dict(q="Write a POST endpoint that accepts a Student and returns it with status 201."),
        dict(q="Write the prompt you would give Codex for a GET /students/{id} endpoint, including errors and tests."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="REST, HTTP, FastAPI routing, Pydantic models, CRUD and reviewing a Codex endpoint",
                sign_off="Yoi shuumatsu wo (良い週末を): *Have a great weekend*", cells=[
    ("md", "## 1. Setup"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q fastapi uvicorn httpx requests pydantic

# ===== Option B: VS Code / local (run once in the terminal, not here) =====
# python -m venv .venv
# .venv\\Scripts\\activate        (Windows)   |   source .venv/bin/activate   (macOS/Linux)
# pip install fastapi uvicorn httpx requests pydantic
import fastapi, pydantic
print("FastAPI", fastapi.__version__, "| Pydantic", pydantic.__version__)'''),
    ("md", "## 2. HTTP from the client side\nThis cell calls a free public test API. It needs internet access."),
    ("code", '''import requests
r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
print("Status:", r.status_code)
print("Content-Type:", r.headers["Content-Type"])
print("Body:", r.json())

r = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "Hi", "body": "Day 5", "userId": 1}, timeout=10)
print(r.status_code, r.json())''', ["skip-offline-check"]),
    ("md", "## 3. Your first FastAPI app\n`%%writefile` saves the cell as `main.py`. The same file works in VS Code."),
    ("code", '''%%writefile main.py
from fastapi import APIRouter, FastAPI, HTTPException, Query

app = FastAPI(title="Quotes API", version="1.0")
router = APIRouter(prefix="/quotes", tags=["Quotes"])

quotes = {
    1: {"text": "Small steps every day.", "author": "Unknown"},
    2: {"text": "Fall seven times, stand up eight.", "author": "Japanese proverb"},
}

@app.get("/")
def home():
    return {"message": "Welcome to the Quotes API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@router.get("")
def list_quotes(author: str | None = None, limit: int = Query(10, ge=1, le=50)):
    items = [{"id": k, **v} for k, v in quotes.items() if author is None or v["author"] == author]
    return items[:limit]

@router.get("/{qid}")
def get_quote(qid: int):
    if qid not in quotes:
        raise HTTPException(status_code=404, detail="Quote not found")
    return {"id": qid, **quotes[qid]}

@router.post("", status_code=201)
def create_quote(text: str, author: str = "Unknown"):
    qid = max(quotes, default=0) + 1
    quotes[qid] = {"text": text, "author": author}
    return {"id": qid, **quotes[qid]}

@router.delete("/{qid}", status_code=204)
def delete_quote(qid: int):
    if qid not in quotes:
        raise HTTPException(status_code=404, detail="Quote not found")
    del quotes[qid]

app.include_router(router)'''),
    ("md", "## 4. Call the API\n**Option A (Colab):** `TestClient` calls the app directly, no server needed.\n\n"
           "**Option B (VS Code):** run `uvicorn main:app --reload` in the terminal and open http://127.0.0.1:8000/docs"),
    ("code", '''# ===== Option A: Google Colab (active) =====
import importlib, main
importlib.reload(main)
from fastapi.testclient import TestClient
client = TestClient(main.app)

# ===== Option B: VS Code with uvicorn running (uncomment to use) =====
# import requests
# class _Client:
#     base = "http://127.0.0.1:8000"
#     def get(self, p, **k): return requests.get(self.base + p, **k)
#     def post(self, p, **k): return requests.post(self.base + p, **k)
#     def delete(self, p, **k): return requests.delete(self.base + p, **k)
# client = _Client()

print(client.get("/").json())
print(client.get("/quotes/2").json())
print(client.get("/quotes", params={"author": "Unknown"}).json())'''),
    ("code", '''r = client.post("/quotes", params={"text": "Keep learning", "author": "Ahmed"})
print("POST:", r.status_code, r.json())
print("Missing:", client.get("/quotes/99").status_code, client.get("/quotes/99").json())
print("Wrong type:", client.get("/quotes/abc").status_code)
print("Limit too big:", client.get("/quotes", params={"limit": 500}).status_code)
print("DELETE:", client.delete("/quotes/1").status_code)'''),
    ("md", "## 5. Status code check\nIf nothing prints except the final message, every rule holds."),
    ("code", '''assert client.get("/health").status_code == 200
assert client.post("/quotes", params={"text": "Hi"}).status_code == 201
assert client.get("/quotes/999").status_code == 404
assert client.get("/quotes/abc").status_code == 422
print("All status code checks passed")'''),
    ("md", "### TODO 1: Add `GET /quotes/random` and a test for it. Tip: put it above `/quotes/{qid}` so the path matches first."),
    ("code", "# TODO: write your code here"),
    ("md", "## 6. Pydantic on its own"),
    ("code", '''from pydantic import BaseModel, Field, ValidationError

class BookCreate(BaseModel):
    title: str = Field(min_length=1, examples=["Ikigai"])
    author: str
    pages: int = Field(gt=0)
    year: int = Field(ge=1450, le=2026)

ok = BookCreate(title="Ikigai", author="Garcia", pages=208, year=2016)
print(ok.model_dump())

try:
    BookCreate(title="", author="X", pages=-5, year=3000)
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])'''),
    ("md", "## 7. A Books API with a router, models and full CRUD"),
    ("code", '''%%writefile books_api.py
from fastapi import APIRouter, FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str
    pages: int = Field(gt=0)

class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1)
    author: str | None = None
    pages: int | None = Field(default=None, gt=0)

class Book(BookCreate):
    id: int

books: dict[int, Book] = {}
router = APIRouter(prefix="/books", tags=["Books"])

@router.get("", response_model=list[Book])
def list_books(author: str | None = None, limit: int = Query(10, ge=1, le=100)):
    result = [b for b in books.values() if author is None or b.author == author]
    return result[:limit]

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(404, "Book not found")
    return books[book_id]

@router.post("", response_model=Book, status_code=201)
def create_book(data: BookCreate):
    new_id = max(books, default=0) + 1
    books[new_id] = Book(id=new_id, **data.model_dump())
    return books[new_id]

@router.patch("/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookUpdate):
    if book_id not in books:
        raise HTTPException(404, "Book not found")
    changes = data.model_dump(exclude_unset=True)
    books[book_id] = books[book_id].model_copy(update=changes)
    return books[book_id]

@router.delete("/{book_id}", status_code=204)
def delete_book(book_id: int):
    if books.pop(book_id, None) is None:
        raise HTTPException(404, "Book not found")

app = FastAPI(title="Books API")
app.include_router(router)'''),
    ("code", '''import importlib, books_api
importlib.reload(books_api)
bc = TestClient(books_api.app)

r = bc.post("/books", json={"title": "Ikigai", "author": "Garcia", "pages": 208})
print(r.status_code, r.json())
bc.post("/books", json={"title": "Deep Work", "author": "Newport", "pages": 296})
print("PATCH:", bc.patch("/books/1", json={"pages": 210}).json())
print("Bad data:", bc.post("/books", json={"title": "", "author": "X", "pages": 0}).status_code)
print("Missing:", bc.get("/books/99").status_code)
print("Delete:", bc.delete("/books/2").status_code)
print("Left:", [b["title"] for b in bc.get("/books").json()])'''),
    ("md", "### TODO 2: Add a `year` field (1450 to 2026) to the models and a query filter `min_pages` to the list endpoint."),
    ("code", "# TODO: write your code here"),
    ("md", "## 8. NEW (v4): Generate an endpoint with Codex, then review and test it\n"
           "Below is the kind of code an AI assistant often produces for the prompt "
           "\"add a PATCH endpoint for tickets\". It runs. Read it before you run the tests: can you spot the bug?\n\n"
           "In VS Code, try it for real: open the OpenAI Codex panel, paste the prompt from the deck, and review the diff."),
    ("code", '''%%writefile tickets_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    title: str = Field(min_length=3)
    priority: str = Field(pattern="^(low|medium|high)$")
    status: str = "open"

class TicketUpdate(BaseModel):
    title: str | None = None
    priority: str | None = Field(default=None, pattern="^(low|medium|high)$")
    status: str | None = None

class Ticket(TicketCreate):
    id: int

tickets: dict[int, Ticket] = {1: Ticket(id=1, title="No signal at home", priority="high")}
app = FastAPI(title="SmartDesk tickets")

# ---- generated by an AI assistant, not yet reviewed ----
@app.patch("/tickets/{tid}")
def update_ticket(tid: int, data: TicketUpdate):
    ticket = tickets.get(tid)
    changes = data.model_dump()
    tickets[tid] = ticket.model_copy(update=changes)
    return tickets[tid]'''),
    ("code", '''import importlib, tickets_api
importlib.reload(tickets_api)
tc = TestClient(tickets_api.app, raise_server_exceptions=False)

def review_tests(c):
    results = {}
    r = c.patch("/tickets/1", json={"status": "closed"})
    results["only status changes"] = r.status_code == 200 and r.json()["title"] == "No signal at home"
    results["unknown id gives 404"] = c.patch("/tickets/99", json={"status": "closed"}).status_code == 404
    results["bad priority gives 422"] = c.patch("/tickets/1", json={"priority": "urgent"}).status_code == 422
    for name, ok in results.items():
        print("PASS" if ok else "FAIL", name)
    return all(results.values())

print("All passed:", review_tests(tc))'''),
    ("md", "Two tests fail. `model_dump()` sends `None` for every field the client did not send, so the title is wiped. "
           "And a missing ticket crashes with a 500 instead of a clean 404. Here is the reviewed version."),
    ("code", '''%%writefile tickets_reviewed.py
from fastapi import FastAPI, HTTPException
from tickets_api import Ticket, TicketUpdate

tickets: dict[int, Ticket] = {1: Ticket(id=1, title="No signal at home", priority="high")}
app = FastAPI(title="SmartDesk tickets (reviewed)")

# ---- reviewed: 404 for unknown ids, only sent fields change, typed response ----
@app.patch("/tickets/{tid}", response_model=Ticket)
def update_ticket(tid: int, data: TicketUpdate):
    if tid not in tickets:
        raise HTTPException(404, "Ticket not found")
    changes = data.model_dump(exclude_unset=True)
    tickets[tid] = tickets[tid].model_copy(update=changes)
    return tickets[tid]'''),
    ("code", '''import tickets_reviewed
importlib.reload(tickets_reviewed)
print("All passed:", review_tests(TestClient(tickets_reviewed.app)))'''),
    ("md", "**Review note template** (paste into your pull request):\n\n"
           "* Prompt used: ...\n* What I checked: contract, validation, errors, side effects, tests\n"
           "* What I changed: ...\n* Tests added: ...\n* Tokens used today (from the Codex usage view): ..."),
    ("md", "### TODO 3 (SmartDesk step 4): add `POST /tickets` (201) and `DELETE /tickets/{tid}` (204, 404) with tests."),
    ("code", "# TODO: write your code here"),
    ("md", "## 9. Optional: run a real server inside Colab\nThis starts uvicorn in the background and calls it over HTTP."),
    ("code", '''# ===== Option A: Google Colab =====
import subprocess, time, requests
server = subprocess.Popen(["uvicorn", "main:app", "--port", "8000"])
time.sleep(3)
print(requests.get("http://127.0.0.1:8000/health").json())
server.terminate()

# ===== Option B: VS Code =====
# Just run in the terminal: uvicorn main:app --reload''', ["skip-offline-check"]),
])
