"""Day 15 spec. Basics: Testing and Data Engineering Intro.
Source: archive/v1-40-day/Day13 (reused and updated). NEW (v4) topics are marked.
"""
DAY = 15
FOLDER = "Day15-Testing-and-Data-Engineering-Intro"
SLUG = "Testing_and_Data_Engineering_Intro"
TITLE = "Testing and Data Engineering Intro"
SUBTITLE = "PyTest and TestClient, tests drafted with Codex, React testing, ETL vs ELT, ingestion and data quality"
DATE = "Mon 16 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 16: data pipelines, Spark and PySpark."
CLOSING_GREET = "Otsukaresama deshita (お疲れ様でした): Thank you for your hard work today"

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 13"),
        ("PyTest and FastAPI", "Tests, fixtures, parametrize, TestClient"),
        ("Tests with Codex", "Draft, review, run. NEW (v4)"),
        ("React testing", "Test what the user sees"),
        ("Data engineering", "Lifecycle, ETL vs ELT, ingestion"),
        ("Data quality", "Checks and a tested pipeline"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Write PyTest tests", "Use asserts, fixtures and parametrize; test FastAPI with TestClient."),
        ("Review AI-drafted tests", "Let Codex draft tests, then check they test the right thing."),
        ("Describe data flow", "Walk through the data lifecycle, ETL and ELT."),
        ("Build a tested pipeline", "Ingest a messy CSV with pandas and prove its quality with tests."),
    ]),
    dict(type="table", title="How today is organised", header=["Session", "Duration", "Focus"], rows=[
        ["Session 1", "1.5 hrs", "FastAPI testing with PyTest and TestClient; tests drafted with Codex (NEW v4)"],
        ["Session 2", "1 hr", "React app testing basics"],
        ["Session 3", "2 hrs", "Data engineering basics; ingestion; ETL vs ELT; CSV ingestion with pandas"],
        ["Session 4", "2 hrs", "Data quality checks; testing a small pipeline"],
    ]),

    dict(type="section", title="Testing with PyTest", sub="Session 1 (1.5 hrs): proof that your code works, every time"),
    dict(type="cards", title="The testing pyramid", greet="Anshin (安心): Peace of mind", items=[
        ("Unit tests (many)", "One function at a time. Fast, run on every save."),
        ("Integration tests (some)", "Parts working together: API + database."),
        ("End-to-end tests (few)", "The whole app through the browser. Slow but realistic."),
    ]),
    dict(type="bullets_code", title="Your first PyTest", bullets=[
        "Files named test_*.py",
        "Functions named test_*",
        "Plain assert statements",
        "Run with: pytest -q",
    ], code='''# pricing.py
def with_gst(amount, rate=18):
    if amount < 0:
        raise ValueError("negative")
    return round(amount * (1 + rate / 100), 2)

# test_pricing.py
import pytest
from pricing import with_gst

def test_default_rate():
    assert with_gst(100) == 118.0

def test_negative_raises():
    with pytest.raises(ValueError):
        with_gst(-1)'''),
    dict(type="bullets_code", title="parametrize and fixtures", bullets=[
        "parametrize runs one test with many inputs",
        "A fixture prepares shared test data",
        "Tests ask for fixtures by name",
        "Same idea as FastAPI Depends()",
    ], code='''@pytest.mark.parametrize("amt, rate, out", [
    (100, 18, 118.0),
    (100, 5, 105.0),
    (0, 18, 0.0),
])
def test_rates(amt, rate, out):
    assert with_gst(amt, rate) == out

@pytest.fixture
def cart():
    return [{"price": 100}, {"price": 50}]

def test_cart_total(cart):
    assert sum(i["price"] for i in cart) == 150'''),
    dict(type="bullets_code", title="Testing a FastAPI app", bullets=[
        "TestClient calls the app directly",
        "A fixture gives every test a clean client",
        "Check status codes and JSON",
        "Test unhappy paths too: 404, 422",
    ], code='''from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_ticket(client):
    r = client.post("/tickets", json={"title": "x"})
    assert r.status_code == 201
    assert r.json()["status"] == "open"

def test_missing_ticket(client):
    r = client.get("/tickets/999")
    assert r.status_code == 404'''),
    dict(type="flow", title="Generate tests with Codex, then review and run", new=True, items=[
        ("Describe", "Name the function, rules and edge cases"),
        ("Draft", "Codex writes test_*.py"),
        ("Review", "Is each expectation right?"),
        ("Run", "pytest -q; read every failure"),
        ("Fix", "Fix the test or the code, never blindly"),
    ], note="A failing AI-drafted test means either the code or the test is wrong. You decide which."),
    dict(type="cards", title="Reviewing an AI-drafted test", new=True, items=[
        ("Right expectation?", "Check each expected value against the real rule, not the code."),
        ("Real assertions?", "Reject tests that only check \"is not None\" or call without asserting."),
        ("Edge cases?", "Boundaries, empty input, wrong types, error paths."),
        ("Independent?", "Each test sets up its own data; no order dependence."),
        ("Readable?", "Clear names; one behaviour per test."),
        ("Cost and safety", "Small prompt with only the relevant file; no secrets or customer data."),
    ]),
    dict(type="code", title="A Codex prompt for tests", new=True, code='''Write PyTest tests for grade(marks) in pricing.py.
Rules: 85-100 -> "A", 70-84 -> "B", 50-69 -> "C", 0-49 -> "Needs improvement".
Marks outside 0-100 raise ValueError.
Use one parametrized test for all boundaries (0, 49, 50, 69, 70, 84, 85, 100)
and one test for each error case. Do not change pricing.py.''',
         note="Give the rules, not just the code. Otherwise Codex tests what the code does, bugs included."),

    dict(type="section", title="Testing React", sub="Session 2 (1 hr): test what the user sees, not the internals"),
    dict(type="compare", title="Two levels of front end tests", left=dict(title="Unit tests (plain JS)", bullets=[
        "Pure functions: formatPrice, filters", "Fast, no browser needed", "node --test or Vitest",
    ]), right=dict(title="Component tests (RTL)", bullets=[
        "Render a component in a fake DOM", "Find elements like a user would", "Click, type, then check the screen",
    ])),
    dict(type="bullets_code", title="React Testing Library with Vitest", bullets=[
        "render the component",
        "screen finds elements by role or text",
        "userEvent simulates real clicks",
        "expect what the user should see",
    ], code='''import { render, screen } from
  "@testing-library/react";
import userEvent from
  "@testing-library/user-event";
import Counter from "./Counter";

test("increments on click", async () => {
  render(<Counter />);
  await userEvent.click(
    screen.getByRole("button", { name: "+1" }));
  expect(screen.getByText("Count: 1"))
    .toBeInTheDocument();
});'''),

    dict(type="section", title="Data engineering basics", sub="Session 3 (2 hrs): where data comes from and where it goes"),
    dict(type="flow", title="From raw data to decisions", items=[
        ("Generate", "Apps, sensors, forms, logs"),
        ("Ingest", "Collect into one place"),
        ("Store", "Lake or warehouse"),
        ("Process", "Clean, join, aggregate"),
        ("Serve", "Dashboards, APIs, AI"),
    ], note="Data engineers build and run the pipes between these stages."),
    dict(type="table", title="Who does what with data", header=["Role", "Main focus", "Typical output"], rows=[
        ["Data engineer", "Reliable pipelines and storage", "Clean tables on schedule"],
        ["Data analyst", "Answering business questions", "Reports and dashboards"],
        ["Data scientist", "Predictions and experiments", "Models and insights"],
        ["FDE", "Solving one customer's problem end to end", "Working solution in their environment"],
    ]),
    dict(type="compare", title="ETL and ELT", left=dict(title="ETL", bullets=[
        "Extract, Transform, then Load", "Clean before storing", "Good when storage is costly or rules strict",
        "Classic warehouses",
    ]), right=dict(title="ELT", bullets=[
        "Extract, Load raw, then Transform", "Transform inside the warehouse with SQL", "Keeps raw data for replays",
        "Modern cloud platforms",
    ])),
    dict(type="bullets_code", title="A tiny ETL with pandas", bullets=[
        "Extract from CSV",
        "Transform: clean, fix types, dedupe",
        "Load into a database table",
        "Each step is a small testable function",
    ], code='''import pandas as pd, sqlite3

def extract(path):
    return pd.read_csv(path)

def transform(df):
    df = df.drop_duplicates("ticket_id")
    df["minutes"] = pd.to_numeric(df["minutes"],
                                  errors="coerce")
    return df.dropna(subset=["minutes"])

def load(df, conn):
    df.to_sql("tickets", conn, if_exists="replace")

load(transform(extract("legacy_tickets.csv")),
     sqlite3.connect("smartdesk.db"))'''),
    dict(type="table", title="Ingestion patterns", header=["Pattern", "How", "When"], rows=[
        ["Batch full load", "Copy everything each run", "Small tables"],
        ["Incremental", "Only rows newer than last run", "Growing tables"],
        ["Streaming", "Process events as they arrive", "Real-time needs"],
        ["API pull", "Call an API on a schedule", "SaaS data sources"],
    ], note="Make pipelines idempotent: running twice must not create duplicates."),

    dict(type="section", title="Data quality and pipeline tests", sub="Session 4 (2 hrs): trust, then use"),
    dict(type="cards", title="Data quality checks", items=[
        ("Completeness", "No missing ids or required fields."),
        ("Uniqueness", "No duplicate keys after the load."),
        ("Validity", "Values in range: minutes >= 0, known priorities."),
        ("Freshness and volume", "Row count close to yesterday; latest date is recent."),
    ]),
    dict(type="bullets_code", title="Testing a small pipeline", bullets=[
        "Unit test each transform with a tiny DataFrame",
        "tmp_path gives each test its own database",
        "Assert quality rules on the loaded table",
        "Run twice to prove idempotency",
    ], code='''def test_no_duplicate_ids(loaded):
    ids = pd.read_sql("SELECT ticket_id FROM tickets",
                      loaded)["ticket_id"]
    assert ids.is_unique

def test_minutes_valid(loaded):
    df = pd.read_sql("SELECT minutes FROM tickets", loaded)
    assert (df.minutes >= 0).all()

def test_idempotent(tmp_path):
    conn = sqlite3.connect(tmp_path / "t.db")
    assert load_incremental(batch, conn) == 3
    assert load_incremental(batch, conn) == 0'''),
    dict(type="cards", title="SmartDesk step 13: tests and legacy import", items=[
        ("PyTest suite", "TestClient tests for every ticket endpoint, including 404 and 422."),
        ("Codex drafts, you review", "Ask Codex for tests from the rules; review each expectation."),
        ("Legacy CSV import", "ETL from the old helpdesk CSV into SmartDesk, idempotent."),
        ("Quality tests", "Unique ids, valid priorities, no negative minutes."),
    ]),
    dict(type="callout", title="Hands-on time",
         text="Write PyTest tests for your ticket API, review a Codex-drafted test file, then build and test a small "
              "ETL pipeline from a messy CSV into SQLite.",
         sub="Write the test first for at least one function today. Notice how it shapes your code.",
         greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("PyTest", "assert, fixtures, parametrize, TestClient for APIs."),
        ("AI-drafted tests", "Give rules, review every expectation, then run."),
        ("Lifecycle", "Generate, ingest, store, process, serve. ETL or ELT."),
        ("Data quality", "Complete, unique, valid, fresh. Every run idempotent."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day15_Hotel_Lab.md: PyTest cases and a messy CSV."),
        ("Workbook", "Complete the Day 15 workbook."),
        ("Pre-read", "Skim the Day 16 pre-read on big data and Spark."),
    ]),
]

PREREAD = dict(title="Checking Your Work and Moving Data",
               lede="A light read before Day 15. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Today has two halves. In the morning you learn to write tests: small programs that check your programs. In "
        "the afternoon you step into data engineering: how raw data travels from where it is created to where it "
        "helps people decide."]),
    dict(h="1. Tests are like a pilot's checklist", paras=[
        "Before every flight, pilots run through a checklist even though they have flown thousands of times. It takes "
        "minutes and prevents disasters. Automated tests are a checklist for code. Every time you change something, "
        "the computer re-checks everything in seconds."],
        box="**Key idea:** tests give you the confidence to change code without fear of breaking what already works."),
    dict(h="2. Three sizes of test", table=[
        ["Test size", "Everyday example"],
        ["Small (unit)", "Checking that one light switch works."],
        ["Medium (integration)", "Checking that the switch, wiring and bulb work together."],
        ["Large (end to end)", "Walking into the room at night and seeing the light come on."]]),
    dict(h="3. An assistant can draft the checklist", new=True, paras=[
        "OpenAI Codex can write a first draft of your tests in seconds. But a checklist is only useful if every line "
        "checks the right thing. You still read each test and ask: is this really what the rule says?"]),
    dict(h="4. The journey of data", paras=[
        "Think of water. It falls as rain (data is generated by apps and devices), flows into reservoirs (data is "
        "collected, or ingested), is stored, then cleaned at a treatment plant (data is processed), and finally "
        "arrives at your tap (dashboards, reports and AI models). Data engineers build and maintain the pipes."]),
    dict(h="5. Clean first, or store first?", paras=[
        "**ETL** cleans data before storing it, like washing vegetables before putting them in the fridge. **ELT** "
        "stores everything first and cleans it later inside a powerful database, like putting the shopping away "
        "quickly and preparing it when you cook. Both are valid; modern cloud platforms often prefer ELT."]),
    dict(h="6. Think about these before class", bullets=[
        "What checks do you do before submitting an important document at work?",
        "Name three places where data about you is generated every day.",
        "What could go wrong if the same support ticket were loaded into a report twice?"],
        after=["Anshin (安心): peace of mind"]),
])

POSTREAD = dict(title="Testing and Data Engineering: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Testing pyramid", "Many unit tests, some integration tests, few end-to-end tests."],
        ["PyTest basics", "test_*.py files, test_* functions, plain assert, pytest -q."],
        ["parametrize and fixtures", "One test, many cases; reusable setup injected by name."],
        ["API tests", "TestClient + fixtures; check status codes and JSON, including errors."],
        ["Tests with Codex (NEW v4)", "Give the rules, review every expectation, run, then fix code or test."],
        ["React tests", "Vitest + React Testing Library: render, find by role or text, click, expect."],
        ["Data lifecycle", "Generate, ingest, store, process, serve."],
        ["ETL vs ELT", "Transform before loading vs load raw then transform in the warehouse."],
        ["Data quality", "Complete, unique, valid, fresh. Pipelines must be idempotent."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Test coverage", paras=[
        "Coverage shows which lines your tests never run. High coverage is a guide, not a goal; a few meaningful "
        "tests beat many shallow ones. AI-drafted tests can raise coverage without checking anything useful."],
        code="pip install pytest-cov\npytest --cov=. --cov-report=term-missing"),
    dict(sub="2. Test-driven development (TDD)", paras=[
        "Write a failing test, write just enough code to pass it, then tidy the code. Red, green, refactor. It pairs "
        "well with Codex: you write or approve the test, Codex writes code until it passes."]),
    dict(sub="3. Mocking external calls", paras=["Replace slow or paid calls (such as an LLM API) in tests:"],
         code='def test_summary(monkeypatch):\n    monkeypatch.setattr("app.llm", lambda p: "short summary")\n'
              '    assert app.summarise("long text") == "short summary"'),
    dict(sub="4. Data quality tools", paras=[
        "Tools such as Great Expectations or dbt tests formalise quality rules and run them on every load."]),
    dict(sub="5. Lakes, warehouses and lakehouses", paras=[
        "A lake stores raw files cheaply. A warehouse stores clean tables for fast SQL. A lakehouse combines both, "
        "which is what Spark is often used for; you meet Spark tomorrow."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why should most tests be unit tests?",
        "What does a fixture do?",
        "Why should you give Codex the rules, not only the code, when asking for tests?",
        "Give one advantage of ELT over ETL.",
        "What does idempotent mean for a pipeline?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Reach 10 PyTest tests for your SmartDesk ticket API, including every error case.",
        "Ask Codex to draft tests for one function, then write a review note on each test.",
        "Add a data quality test that fails if any ticket has a negative handling time."],
        after=["**Coming up on Day 16:** batch data pipelines, Apache Spark and PySpark.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems: four on testing, three on data pipelines. Run PyTest with !python -m pytest -q in "
                    "Colab or pytest -q in the VS Code terminal.", problems=[
    dict(title="First Tests", level="Warm-up", concepts="assert, pytest.raises",
         text="Write a module with is_valid_email(s), discount(price, pct) and grade(marks). Write at least two tests "
              "per function, including one error case.",
         sample="pytest -q\n7 passed in 0.03s", hints=["Name files test_*.py and functions test_*."]),
    dict(title="Parametrize the Boundaries", level="Easy", concepts="pytest.mark.parametrize",
         text="Test grade(marks) with one parametrized test covering 0, 49, 50, 69, 70, 84, 85 and 100, plus a test "
              "that 101 raises ValueError.",
         sample="9 passed", hints=["Boundary values are where bugs hide."]),
    dict(title="Ticket API Test Suite", level="Medium", concepts="fixtures, TestClient",
         text="Write a client fixture and 8 tests for a Tickets API: list, create (201), invalid create (422), get, "
              "missing (404), patch status, delete (204), delete twice (404).",
         sample="8 passed", hints=["Reset the in-memory store in a fixture so tests do not affect each other."]),
    dict(title="Review a Codex-Drafted Test File", level="Medium", concepts="AI-assisted testing, review",
         new=True,
         text=["The notebook contains a test file drafted by an AI assistant for sla_minutes(priority). Run it, then "
               "review every test against the written rules. For each test, mark keep, fix or delete, with a reason.",
               "Then ask Codex (or use the notebook's online cell) to draft tests for your own function, and repeat "
               "the review."],
         sample="drafted: 6 tests -> 4 passed, 2 failed\nreview: keep 3, fix 2 (wrong expectation), delete 1 (no assert)\n"
                "after review: 8 passed",
         hints=["A failing test can be right. Check the rule before changing the code.",
                "Note the prompt you used and roughly how many tokens it took."]),
    dict(title="Messy Data ETL", level="Medium", concepts="pandas extract, transform, load",
         text="Given legacy_tickets.csv with duplicates, blank minutes, mixed date formats and extra spaces, write "
              "extract, transform and load functions that produce a clean tickets table in SQLite.",
         sample="Raw rows: 12 -> Clean rows: 8\nLoaded 8 rows into smartdesk.db.tickets",
         hints=['drop_duplicates, str.strip, pd.to_numeric(errors="coerce"), pd.to_datetime(format="mixed")']),
    dict(title="ELT Version", level="Challenging", concepts="load raw, transform with SQL",
         text="Load the raw CSV as-is into a raw_tickets table, then create a clean tickets_clean table with a SQL "
              "query inside SQLite. Compare row counts with your ETL result.",
         sample="raw_tickets: 12 rows\ntickets_clean: 8 rows (matches ETL)",
         hints=["CREATE TABLE tickets_clean AS SELECT DISTINCT ... WHERE minutes IS NOT NULL"]),
    dict(title="Idempotent Load with Quality Tests", level="Stretch", concepts="incremental ingestion, data quality",
         text="Write load_incremental(new_df, conn) that inserts only tickets not already present. Prove that "
              "running it twice keeps the same row count, and add PyTest data quality tests (unique ids, valid "
              "priorities, no negative minutes).",
         sample="Run 1: inserted 3\nRun 2: inserted 0\n4 passed",
         hints=["Read existing ids with pd.read_sql, then filter with ~df.ticket_id.isin(ids)."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "PyTest test files must be named starting with ________.",
        "To check that code raises an error, use pytest.________.",
        "To run one test with many inputs, use @pytest.mark.________.",
        "Reusable setup for tests is provided by a ________.",
        "FastAPI apps are tested without a server using ________.",
        "When Codex drafts tests, you must review each expected ________ against the rule.",
        "React Testing Library finds elements the way a ________ would.",
        "ETL stands for Extract, ________, Load.",
        "In ELT, data is transformed ________ it is loaded.",
        "A pipeline that gives the same result when run twice is ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the testing pyramid and why it has that shape.",
        "Codex drafted a test that fails. Describe how you decide whether the code or the test is wrong.",
        "When would you choose ETL, and when ELT?",
        "Name four data quality checks for a SmartDesk tickets table.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'import pytest\n@pytest.mark.parametrize("x", [1, 2, 3])\ndef test_pos(x):\n    assert x > 1\n'
        "# how many pass and how many fail?",
        'import pandas as pd\ndf = pd.DataFrame({"id": [1, 1, 2], "amt": ["10", "x", "5"]})\n'
        'df = df.drop_duplicates("id")\ndf["amt"] = pd.to_numeric(df["amt"], errors="coerce")\nprint(df["amt"].sum())',
        "def test_total():\n    result = sum([10, 20])\n    result is not None\n"
        "# An AI drafted this test. Does it pass? Does it check anything?",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a PyTest test for a function add(a, b), including one parametrized case list."),
        dict(q="Write a Codex prompt that asks for tests of sla_minutes(priority), giving the rules and edge cases."),
        dict(q="Write a pandas transform that removes rows with missing email and lowercases emails."),
        dict(q="Write a PyTest data quality test that fails if any ticket_id is duplicated."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="PyTest and TestClient, tests drafted with Codex, JavaScript unit tests, ETL vs ELT, "
                         "incremental loads and data quality", cells=[
    ("md", "## 1. Setup"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q pytest fastapi httpx pandas openai tiktoken scikit-learn
!node --version

# ===== Option B: VS Code / local (run in your activated venv terminal) =====
# pip install pytest fastapi httpx pandas openai tiktoken scikit-learn
# node --version
import os
os.makedirs("day15", exist_ok=True)
os.chdir("day15")
print("Working in", os.getcwd())'''),
    ("md", "## 2. PyTest basics"),
    ("code", '''%%writefile pricing.py
def with_gst(amount, rate=18):
    if amount < 0:
        raise ValueError("amount must not be negative")
    return round(amount * (1 + rate / 100), 2)

def grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("marks must be 0 to 100")
    if marks >= 85:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 50:
        return "C"
    return "Needs improvement"'''),
    ("code", '''%%writefile test_pricing.py
import pytest
from pricing import with_gst, grade

def test_default_rate():
    assert with_gst(100) == 118.0

def test_negative_raises():
    with pytest.raises(ValueError):
        with_gst(-1)

@pytest.mark.parametrize("amount, rate, expected", [(100, 18, 118.0), (100, 5, 105.0), (0, 18, 0.0)])
def test_rates(amount, rate, expected):
    assert with_gst(amount, rate) == expected

@pytest.mark.parametrize("marks, expected", [(0, "Needs improvement"), (49, "Needs improvement"), (50, "C"),
                                             (69, "C"), (70, "B"), (84, "B"), (85, "A"), (100, "A")])
def test_grade_boundaries(marks, expected):
    assert grade(marks) == expected

def test_grade_out_of_range():
    with pytest.raises(ValueError):
        grade(101)'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!python -m pytest -q test_pricing.py

# ===== Option B: VS Code =====
# Terminal: pytest -q    (or use the Testing panel, the flask icon in the sidebar)'''),
    ("md", "## 3. Testing a FastAPI app with fixtures\nA small SmartDesk-style tickets API."),
    ("code", '''%%writefile tickets_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
tickets: dict[int, dict] = {}

class TicketIn(BaseModel):
    title: str = Field(min_length=1)
    priority: str = Field(default="medium", pattern="^(low|medium|high)$")

@app.get("/tickets")
def list_tickets():
    return list(tickets.values())

@app.post("/tickets", status_code=201)
def create(t: TicketIn):
    tid = max(tickets, default=0) + 1
    tickets[tid] = {"id": tid, "title": t.title, "priority": t.priority, "status": "open"}
    return tickets[tid]

@app.get("/tickets/{tid}")
def get(tid: int):
    if tid not in tickets:
        raise HTTPException(404, "Ticket not found")
    return tickets[tid]

@app.delete("/tickets/{tid}", status_code=204)
def delete(tid: int):
    if tickets.pop(tid, None) is None:
        raise HTTPException(404, "Ticket not found")'''),
    ("code", '''%%writefile test_tickets_api.py
import pytest
from fastapi.testclient import TestClient
import tickets_api

@pytest.fixture
def client():
    tickets_api.tickets.clear()          # every test starts with an empty store
    return TestClient(tickets_api.app)

def test_starts_empty(client):
    assert client.get("/tickets").json() == []

def test_create_returns_201(client):
    r = client.post("/tickets", json={"title": "No signal"})
    assert r.status_code == 201
    assert r.json() == {"id": 1, "title": "No signal", "priority": "medium", "status": "open"}

def test_empty_title_is_422(client):
    assert client.post("/tickets", json={"title": ""}).status_code == 422

def test_bad_priority_is_422(client):
    assert client.post("/tickets", json={"title": "x", "priority": "urgent!!"}).status_code == 422

def test_missing_is_404(client):
    assert client.get("/tickets/999").status_code == 404

def test_delete_twice(client):
    client.post("/tickets", json={"title": "x"})
    assert client.delete("/tickets/1").status_code == 204
    assert client.delete("/tickets/1").status_code == 404'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!python -m pytest -q test_tickets_api.py

# ===== Option B: VS Code =====
# Terminal: pytest -q test_tickets_api.py'''),
    ("md", "### TODO 1: Add a test that creating two tickets gives ids 1 and 2, and that GET /tickets returns both."),
    ("code", "# TODO: write your code here"),
    ("md", "## 4. NEW (v4): Generate tests with Codex, then review and run them\n"
           "In VS Code you would ask OpenAI Codex for tests. Here, the cell below drafts tests with the LLM when a key "
           "is set, or loads a saved AI draft in offline mode. Either way, **you** review and run them.\n\n"
           "The rules for `sla_minutes(priority)` are: high = 60, medium = 240, low = 1440 minutes. Any other priority "
           "raises `ValueError`. Priority is case-insensitive."),
    ("helpers",),
    ("code", '''%%writefile sla.py
def sla_minutes(priority):
    p = priority.strip().lower()
    table = {"high": 60, "medium": 240, "low": 1440}
    if p not in table:
        raise ValueError(f"unknown priority: {priority}")
    return table[p]'''),
    ("code", '''RULES = """sla_minutes(priority): high = 60, medium = 240, low = 1440 minutes.
Any other priority raises ValueError. Priority is case-insensitive."""

SAVED_AI_DRAFT = """import pytest
from sla import sla_minutes

def test_high():
    assert sla_minutes("high") == 60

def test_medium():
    assert sla_minutes("medium") == 120

def test_low():
    assert sla_minutes("low") == 1440

def test_upper_case():
    assert sla_minutes("HIGH") == 60

def test_unknown():
    sla_minutes("urgent")

def test_returns_something():
    assert sla_minutes("low") is not None
"""

prompt = ("Write PyTest tests for this function. Rules:\\n" + RULES +
          "\\nUse plain asserts and pytest.raises. Return only Python code.\\n\\n" + open("sla.py").read())
draft = llm(prompt) if ONLINE else SAVED_AI_DRAFT
draft = draft.strip().removeprefix("```python").removesuffix("```").strip() + "\\n"
open("test_sla_ai_draft.py", "w").write(draft)
print(f"Prompt tokens: {count_tokens(prompt)} | Draft saved ({'live model' if ONLINE else 'saved offline draft'})")
print(draft)'''),
    ("code", '''# Run the AI draft as is. Failures are information, not a reason to edit the code.
!python -m pytest -q test_sla_ai_draft.py || true'''),
    ("md", "### Review notes (offline draft)\n"
           "| Test | Verdict | Reason |\n|---|---|---|\n"
           "| test_high, test_low, test_upper_case | keep | Match the rules. |\n"
           "| test_medium | **fix** | The rule says 240, not 120. The test is wrong, the code is right. |\n"
           "| test_unknown | **fix** | It calls the function without `pytest.raises`, so the expected ValueError makes the test fail. Wrap it in `pytest.raises`. |\n"
           "| test_returns_something | **delete** | Checks nothing useful. |\n\n"
           "Below is the reviewed version. Notice we did not change `sla.py`."),
    ("code", '''%%writefile test_sla.py
import pytest
from sla import sla_minutes

@pytest.mark.parametrize("priority, minutes", [("high", 60), ("medium", 240), ("low", 1440),
                                               ("HIGH", 60), (" Low ", 1440)])
def test_rules(priority, minutes):
    assert sla_minutes(priority) == minutes

@pytest.mark.parametrize("bad", ["urgent", "", "p1"])
def test_unknown_priority_raises(bad):
    with pytest.raises(ValueError):
        sla_minutes(bad)'''),
    ("code", "!python -m pytest -q test_sla.py"),
    ("md", "## 5. JavaScript unit tests with Node's built-in runner\nNo installation needed. In a React project you "
           "would use Vitest and React Testing Library (see the deck); the ideas are the same."),
    ("code", '''%%writefile tickets.mjs
export function formatMinutes(n) {
  return n >= 60 ? `${Math.floor(n / 60)} h ${n % 60} min` : `${n} min`;
}

export function openCount(tickets) {
  return tickets.filter((t) => t.status === "open").length;
}'''),
    ("code", '''%%writefile tickets.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { formatMinutes, openCount } from "./tickets.mjs";

test("formats minutes under an hour", () => {
  assert.equal(formatMinutes(45), "45 min");
});

test("formats hours and minutes", () => {
  assert.equal(formatMinutes(130), "2 h 10 min");
});

test("counts only open tickets", () => {
  assert.equal(openCount([{ status: "open" }, { status: "closed" }, { status: "open" }]), 2);
});'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node --test tickets.test.mjs

# ===== Option B: VS Code =====
# Terminal: node --test tickets.test.mjs'''),
    ("md", "## 6. A tiny ETL pipeline: legacy ticket import\nA deliberately messy export from the old helpdesk, the "
           "kind real systems produce."),
    ("code", '''%%writefile legacy_tickets.csv
ticket_id,customer,minutes,opened,priority
1001, Asha ,25,2026-11-01,high
1002,Kenji,120,2026-11-01,medium
1002,Kenji,120,2026-11-01,medium
1003,Mei,,2026-11-02,low
1004,Ravi,abc,2026-11-02,medium
1005,Priya,56,02/11/2026,HIGH
1006, Hana,90,2026-11-03,low
1007,Arjun,310,2026-11-03,medium
1007,Arjun,310,2026-11-03,medium
1008,Yuki,45,2026-11-04,high
1009,Sara,78,2026-11-04,low
1010,Ken,15,2026-11-05,medium'''),
    ("code", '''import pandas as pd, sqlite3

def extract(path):
    return pd.read_csv(path)

def transform(df):
    df = df.drop_duplicates("ticket_id").copy()
    df["customer"] = df["customer"].str.strip()
    df["priority"] = df["priority"].str.strip().str.lower()
    df["minutes"] = pd.to_numeric(df["minutes"], errors="coerce")
    df["opened"] = pd.to_datetime(df["opened"], format="mixed", dayfirst=True).dt.date.astype(str)
    return df.dropna(subset=["minutes"])

def load(df, conn, table="tickets"):
    df.to_sql(table, conn, if_exists="replace", index=False)
    return len(df)

raw = extract("legacy_tickets.csv")
clean = transform(raw)
conn = sqlite3.connect("smartdesk.db")
print("Raw rows:", len(raw), "-> Clean rows:", len(clean))
print("Loaded", load(clean, conn), "rows")
print(pd.read_sql("SELECT priority, COUNT(*) n, AVG(minutes) avg_min FROM tickets GROUP BY priority", conn))'''),
    ("md", "## 7. The ELT version: load raw, transform with SQL"),
    ("code", '''raw.to_sql("raw_tickets", conn, if_exists="replace", index=False)
conn.executescript("""
DROP TABLE IF EXISTS tickets_clean;
CREATE TABLE tickets_clean AS
SELECT DISTINCT ticket_id, TRIM(customer) AS customer, CAST(minutes AS REAL) AS minutes, opened,
       LOWER(TRIM(priority)) AS priority
FROM raw_tickets
WHERE minutes IS NOT NULL AND CAST(minutes AS REAL) > 0;
""")
print("raw_tickets:", pd.read_sql("SELECT COUNT(*) n FROM raw_tickets", conn).n[0])
print("tickets_clean:", pd.read_sql("SELECT COUNT(*) n FROM tickets_clean", conn).n[0])'''),
    ("md", "## 8. Idempotent incremental load"),
    ("code", '''def load_incremental(new_df, conn, table="tickets"):
    existing = set(pd.read_sql(f"SELECT ticket_id FROM {table}", conn)["ticket_id"])
    fresh = new_df[~new_df["ticket_id"].isin(existing)]
    fresh.to_sql(table, conn, if_exists="append", index=False)
    return len(fresh)

new_batch = pd.DataFrame([
    {"ticket_id": 1010, "customer": "Ken", "minutes": 15.0, "opened": "2026-11-05", "priority": "medium"},
    {"ticket_id": 1011, "customer": "Zara", "minutes": 99.0, "opened": "2026-11-06", "priority": "low"},
])
print("Run 1 inserted:", load_incremental(new_batch, conn))
print("Run 2 inserted:", load_incremental(new_batch, conn))
print("Total rows:", pd.read_sql("SELECT COUNT(*) n FROM tickets", conn).n[0])
conn.close()'''),
    ("md", "## 9. Data quality tests on the loaded table"),
    ("code", '''%%writefile test_quality.py
import sqlite3
import pandas as pd
import pytest

@pytest.fixture
def tickets():
    with sqlite3.connect("smartdesk.db") as conn:
        return pd.read_sql("SELECT * FROM tickets", conn)

def test_ids_unique(tickets):
    assert tickets["ticket_id"].is_unique

def test_no_missing_minutes(tickets):
    assert tickets["minutes"].notna().all()

def test_minutes_not_negative(tickets):
    assert (tickets["minutes"] >= 0).all()

def test_priorities_valid(tickets):
    assert set(tickets["priority"]) <= {"low", "medium", "high"}'''),
    ("code", "!python -m pytest -q test_quality.py"),
    ("md", "### TODO 2 (SmartDesk step 13): add a freshness test (latest `opened` date is not older than 30 days "
           "from the newest ticket) and a test that the row count did not drop after the incremental load."),
    ("code", "# TODO: write your code here"),
])
