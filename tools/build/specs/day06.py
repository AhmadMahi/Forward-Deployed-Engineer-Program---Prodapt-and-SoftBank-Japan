"""Day 06 spec. SQLAlchemy, Relationships and API Docs.
Source: MERGE archive/v1-40-day/Day06 Session 4 (ORM intro) + Day07 (relationships, transactions, docs).
"""
DAY = 6
FOLDER = "Day06-SQLAlchemy-and-API-Docs"
SLUG = "SQLAlchemy_and_API_Docs"
TITLE = "SQLAlchemy, Relationships and API Docs"
SUBTITLE = "ORM concepts, models and column types, one-to-many relationships, transactions, and Swagger / OpenAPI docs"
DATE = "Mon 02 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 7: FastAPI advanced, security and MongoDB."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 5"),
        ("ORM basics", "Engine, session, models, column types"),
        ("Relationships", "One-to-many, foreign keys, joins"),
        ("Transactions", "Commit, rollback, error handling"),
        ("API docs", "Swagger UI and the OpenAPI contract"),
        ("SmartDesk", "SQLite persistence and Swagger docs"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Map objects to tables", "Define SQLAlchemy models with types and constraints."),
        ("Link data", "Build one-to-many relationships and query across them."),
        ("Stay consistent", "Use commit and rollback to keep data correct."),
        ("Document APIs", "Write clear Swagger docs from your OpenAPI schema."),
    ]),

    dict(type="section", title="ORM concepts and SQLAlchemy", sub="Session 1 | 1.5 Hrs | Engine, session, models, column types"),
    dict(type="compare", title="Raw SQL and ORM", left=dict(title="Raw SQL", bullets=[
        "Write SQL strings by hand", "Map rows to objects yourself", "Easy to make typos and injection bugs",
    ]), right=dict(title="ORM (SQLAlchemy)", bullets=[
        "Python classes map to tables", "Objects map to rows", "Queries written in Python",
        "Switch SQLite to PostgreSQL with one URL",
    ])),
    dict(type="table", title="A translator between two languages", header=["Python side", "Database side", "Example"], rows=[
        ["Class", "Table", "class Book -> books"],
        ["Attribute", "Column", "title -> title VARCHAR(200)"],
        ["Object", "Row", "Book(title=\"Ikigai\")"],
        ["Session", "Transaction", "s.add(...); s.commit()"],
    ]),
    dict(type="bullets_code", title="SQLAlchemy in five steps", bullets=[
        "Engine: connection to the database",
        "Base: parent of all models",
        "Model: class = table, attribute = column",
        "Session: a unit of work, then commit",
    ], code='''from sqlalchemy import create_engine
from sqlalchemy.orm import (DeclarativeBase,
    Mapped, mapped_column, Session)

engine = create_engine("sqlite:///library.db")
class Base(DeclarativeBase): pass

class BookRow(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

Base.metadata.create_all(engine)
with Session(engine) as s:
    s.add(BookRow(title="Ikigai")); s.commit()'''),
    dict(type="table", title="Column types and options", header=["Option", "What it does", "Example"], rows=[
        ["primary_key", "Unique id for each row", "id: Mapped[int]"],
        ["String(n), Integer, DateTime", "Column type and size", "mapped_column(String(200))"],
        ["unique", "No two rows share the value", "email unique=True"],
        ["nullable", "Whether the value may be empty", "Mapped[str | None]"],
        ["default", "Value used when none is given", "default=0"],
        ["ForeignKey", "Points to a row in another table", "ForeignKey(\"authors.id\")"],
    ], note="Constraints are a safety net: even buggy code cannot save invalid rows."),
    dict(type="bullets_code", title="Querying in SQLAlchemy 2.0 style", bullets=[
        "select() builds a query",
        "where() filters, order_by() sorts",
        "s.scalars() returns model objects",
        "s.get() fetches one row by primary key",
    ], code='''from sqlalchemy import select

with Session(engine) as s:
    stmt = (select(BookRow)
            .where(BookRow.pages > 200)
            .order_by(BookRow.title))
    for b in s.scalars(stmt):
        print(b.title)

    book = s.get(BookRow, 1)
    book.pages = 210          # update
    s.delete(s.get(BookRow, 4))
    s.commit()'''),

    dict(type="section", title="Relationships and joins", sub="Session 2 | 2 Hrs | One-to-many and foreign keys"),
    dict(type="cards", title="Three relationship shapes", lead="Ask: how many of B can one A have, and how many of A can one B have?", items=[
        ("One-to-one", "A user has one profile."),
        ("One-to-many", "An author writes many books; a book has one author."),
        ("Many-to-many", "A book has many tags; a tag is on many books. Needs a link table."),
    ]),
    dict(type="bullets_code", title="One-to-many", bullets=[
        "ForeignKey lives on the many side",
        "relationship() gives Python navigation",
        "back_populates links both directions",
        "author.books and book.author just work",
    ], code='''class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    books: Mapped[list["Book"]] = relationship(
        back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id"))
    author: Mapped[Author] = relationship(
        back_populates="books")''', greet="Tsunagari (繋がり): Connection. Data linked together"),
    dict(type="bullets_code", title="Using relationships", bullets=[
        "Create objects and link them in Python",
        "One commit saves the whole graph",
        "Navigate with dot notation",
        "No manual joins for simple cases",
    ], code='''with Session(engine) as s:
    ito = Author(name="Ito")
    ito.books = [Book(title="Tokyo Nights"),
                 Book(title="Rain in Kyoto")]
    s.add(ito)
    s.commit()

    print([b.title for b in ito.books])
    print(ito.books[0].author.name)'''),
    dict(type="bullets_code", title="Joins and the N+1 problem", bullets=[
        "join() filters across tables",
        "Touching book.author in a loop can fire one query per row",
        "selectinload() loads related rows up front",
        "Check the SQL with echo=True",
    ], code='''from sqlalchemy.orm import selectinload

# books by one author: a join
stmt = (select(Book).join(Book.author)
        .where(Author.name == "Rao"))

# authors with books, in 2 queries, not N+1
stmt = select(Author).options(
    selectinload(Author.books))'''),

    dict(type="section", title="Transactions", sub="Session 3 | 1.5 Hrs | Commit, rollback, error handling"),
    dict(type="flow", title="A money transfer", items=[
        ("Begin", "Start a transaction"),
        ("Debit", "Take 500 from account A"),
        ("Credit", "Add 500 to account B"),
        ("Commit or rollback", "Both happen, or neither"),
    ], note="If the credit fails after the debit, rollback puts the money back."),
    dict(type="table", title="ACID in plain words", header=["Letter", "Property", "Meaning"], rows=[
        ["A", "Atomic", "All steps happen or none do"],
        ["C", "Consistent", "Rules and constraints always hold"],
        ["I", "Isolated", "Parallel transactions do not mix"],
        ["D", "Durable", "Once committed, it survives crashes"],
    ]),
    dict(type="bullets_code", title="Commit and rollback in code", bullets=[
        "try the whole unit of work",
        "commit only at the end",
        "rollback on any error",
        "IntegrityError means a constraint said no",
    ], code='''from sqlalchemy.exc import IntegrityError

with Session(engine) as s:
    try:
        a = s.get(Account, 1)
        b = s.get(Account, 2)
        if a.balance < 500:
            raise ValueError("Low balance")
        a.balance -= 500
        b.balance += 500
        s.commit()
    except (ValueError, IntegrityError):
        s.rollback()
        raise'''),

    dict(type="section", title="Swagger UI and OpenAPI", sub="Session 4 | 1 Hr | Documentation that writes itself"),
    dict(type="compare", title="OpenAPI and Swagger UI", left=dict(title="OpenAPI", bullets=[
        "A standard JSON description of your API", "Lists paths, parameters, models",
        "FastAPI serves it at /openapi.json", "Tools generate clients from it",
    ]), right=dict(title="Swagger UI and ReDoc", bullets=[
        "Swagger UI at /docs: try requests live", "ReDoc at /redoc: clean reading view",
        "Both read the same OpenAPI file", "Always in sync with your code",
    ])),
    dict(type="bullets_code", title="Making docs genuinely useful", bullets=[
        "Title, version and description on the app",
        "summary and docstring per endpoint",
        "tags group related routes",
        "Document error responses and Field examples",
    ], code='''app = FastAPI(
    title="Library API",
    version="1.2.0",
    description="Books, authors and loans.")

@app.get("/books/{bid}", tags=["Books"],
    summary="Get one book",
    response_model=BookOut,
    responses={404: {"description":
               "Book not found"}})
def get_book(bid: int):
    """Returns a book with its author."""
    ...'''),
    dict(type="cards", title="Codex can help with docs too", items=[
        ("Ask for summaries", "\"Add a summary and 404 response to every route in routers/books.py.\""),
        ("Ask for examples", "\"Add Field examples to the Book models.\""),
        ("Review the diff", "Docs must match what the code really does."),
        ("Read /docs fresh", "Read it as a new teammate who has never seen the code."),
    ]),

    dict(type="cards", title="SmartDesk step 5: SQLite and Swagger", items=[
        ("Goal", "Tickets survive a restart: store them in SQLite with SQLAlchemy."),
        ("Relationships", "Customer has many Tickets; Ticket has many Comments."),
        ("Transactions", "Closing a ticket and adding the closing comment commit together."),
        ("Docs", "Tags, summaries and error responses in /docs. Build with Codex, review every line."),
    ]),
    dict(type="callout", title="Hands-on time", text="Extend the Library API with authors and books, a safe transaction for bulk imports, and documentation a new teammate could use without asking you.",
         sub="Open /docs and read it as if you had never seen the code.", greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("ORM", "Classes are tables, objects are rows, sessions commit work."),
        ("Relationships", "ForeignKey on the many side + relationship() with back_populates."),
        ("Transactions", "Commit together or roll back together."),
        ("Docs", "OpenAPI is generated; you add summaries, tags, errors and examples."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day06_Hotel_Lab.md: post-read, notebook, problems."),
        ("Workbook", "Complete the Day 6 workbook."),
        ("Pre-read", "Skim the Day 7 pre-read on security and access."),
    ]),
]

PREREAD = dict(title="Connections, Promises and Manuals", lede="A light read before Day 6. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "On Day 5 your API kept data in memory, so it vanished on restart. Today you connect it to a real database, "
        "link related data, make sure changes are safe, and write documentation that others enjoy reading."]),
    dict(h="1. A translator between two languages", paras=[
        "Python thinks in objects. Most databases think in tables. An **ORM** (Object Relational Mapper) is a "
        "translator between them. You work with Python objects, and the ORM writes the database commands for you. "
        "We use one called **SQLAlchemy**."],
        table=[["Python side", "Database side"], ["Class", "Table"], ["Attribute", "Column"], ["Object", "Row"]]),
    dict(h="2. How things relate", table=[
        ["Relationship", "Everyday example"],
        ["One-to-one", "One person has one passport."],
        ["One-to-many", "One teacher teaches many classes; each class has one teacher."],
        ["Many-to-many", "Students join many clubs, and each club has many students."],
    ], after=["For many-to-many, you need a register in the middle: a sign-up sheet that lists which student joined "
              "which club. Databases use exactly this idea, called a link table."]),
    dict(h="3. All or nothing", paras=[
        "When you transfer money, two things must happen: your account goes down and your friend's goes up. If only "
        "the first step happened, money would vanish. Databases protect you with **transactions**: a group of steps "
        "that either all succeed or are all undone."],
        box="**Key idea:** commit means \"make it permanent\". Rollback means \"undo everything since we started\"."),
    dict(h="4. A manual that is always up to date", paras=[
        "FastAPI builds its documentation directly from your code, so it is always current. The standard behind it is "
        "called **OpenAPI**, and the interactive page at /docs is called **Swagger UI**. Good documentation answers "
        "three questions quickly: what can I do, what must I send, and what will I get back?"]),
    dict(h="5. Think about these before class", bullets=[
        "List three relationships in a telecom support desk (customers, tickets, agents) and classify each.",
        "Describe a situation in your job where a half-finished change would cause problems.",
        "What makes a manual or guide easy to follow?"],
        after=["Tsunagari (繋がり): connection, the links between things"]),
])

POSTREAD = dict(title="SQLAlchemy, Relationships and Docs: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["ORM", "Classes map to tables, objects to rows. Engine, Base, models, Session, commit."],
        ["Columns", "primary_key, unique, nullable, default, ForeignKey. Enforced by the database."],
        ["Queries", "select(Model).where(...).order_by(...); s.scalars(stmt); s.get(Model, id)."],
        ["One-to-many", "ForeignKey on the many side, relationship() with back_populates on both."],
        ["Many-to-many", "Association table of id pairs, relationship(secondary=table)."],
        ["Transactions", "A unit of work: commit on success, rollback on error. ACID."],
        ["OpenAPI", "Machine-readable API contract at /openapi.json."],
        ["Swagger and ReDoc", "/docs to try requests, /redoc to read. Both from the same schema."],
        ["Better docs", "App title, version, description; tags, summary, responses, Field examples."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. from_attributes: ORM object to Pydantic", code='''class BookOut(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    title: str

BookOut.model_validate(book_row)    # works with SQLAlchemy objects'''),
    dict(sub="2. Cascades", paras=[
        "relationship(back_populates=\"author\", cascade=\"all, delete-orphan\"): deleting an author now deletes their "
        "books too. Powerful, so use it deliberately."]),
    dict(sub="3. Migrations with Alembic", paras=[
        "create_all only creates missing tables; it never changes existing ones. In real projects, Alembic records "
        "every schema change as a versioned migration script you can apply or undo."]),
    dict(sub="4. session.begin() context manager", code='''with Session(engine) as s, s.begin():
    s.add(order)
    s.add(payment)
# commits automatically, or rolls back if an exception is raised'''),
    dict(sub="5. Why ORMs prevent SQL injection", paras=[
        "Building SQL by joining strings with user input lets attackers inject commands. ORMs send values separately "
        "from the SQL text (parameterised queries), which closes this hole. You meet injection again on Day 7."]),
    dict(sub="6. Generating clients from OpenAPI", paras=[
        "Tools such as openapi-generator read /openapi.json and produce a client library for TypeScript, Java or Python."]),
    dict(h="Part C: Check yourself", bullets=[
        "On which table does the foreign key go in a one-to-many relationship?",
        "Why does many-to-many need an extra table?",
        "What happens to the data if an exception occurs before commit?",
        "What is the difference between /docs and /openapi.json?",
        "Name three things that make API docs genuinely useful."]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a Comment model to tickets (one-to-many) and list comments for one ticket.",
        "Write a bulk import function that rolls back if any single record is invalid.",
        "Add descriptions, examples and error responses to every endpoint in your Library API."],
        after=["**Coming up on Day 7:** dependency injection, middleware, JWT, OWASP API Top 10, and FastAPI with MongoDB.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems that grow one Library API. SQLite works the same in Colab and VS Code.", problems=[
    dict(title="Spot the Relationship", level="Warm-up", concepts="relationship design",
         text="For each pair, write the relationship type and where the foreign key or link table goes: customer and "
              "ticket, ticket and comment, user and profile, agent and ticket, book and tag.",
         sample="customer - ticket: one-to-many, FK customer_id on tickets\nbook - tag: many-to-many, link table book_tags",
         hints=["Ask how many of each side the other can have."]),
    dict(title="First ORM Model", level="Easy", concepts="engine, model, session, select",
         text="Create a BookRow model in SQLite. Insert 5 books, query those with more than 200 pages sorted by title, "
              "update one, and delete one.",
         sample="Books over 200 pages: Atomic Habits, Deep Work, Ikigai",
         hints=["select(BookRow).where(BookRow.pages > 200).order_by(BookRow.title)"]),
    dict(title="Authors and Books", level="Easy", concepts="one-to-many, back_populates",
         text="Create Author and Book models with a one-to-many relationship. Add 3 authors with 2 books each, then "
              "print each author with their book titles, and all books by one author using a join.",
         sample="Ito: Tokyo Nights, Rain in Kyoto\nRao: Monsoon Code, Chai Stories",
         hints=["relationship(back_populates=...) on both classes"]),
    dict(title="Constraints in Action", level="Medium", concepts="unique, nullable, IntegrityError",
         text="Make author name unique and book title not nullable. Try to break each rule and catch IntegrityError, "
              "rolling back each time.",
         sample="Duplicate author -> IntegrityError, rolled back\nMissing title -> IntegrityError, rolled back",
         hints=["from sqlalchemy.exc import IntegrityError"]),
    dict(title="Safe Transfer", level="Challenging", concepts="transactions, rollback",
         text="Create an Account table. Write transfer(from_id, to_id, amount) that rolls back if the balance is too "
              "low or an account is missing. Prove the balances are unchanged after a failed transfer.",
         sample="transfer(1, 2, 9999) -> failed, balances still 1000 and 500",
         hints=["Do both updates, then commit once at the end."]),
    dict(title="Nested Responses", level="Challenging", concepts="FastAPI + relationships + Pydantic",
         text="Add GET /authors/{id} returning the author with a list of their books, and GET /books returning each "
              "book with its author name. Return 404 for a missing author.",
         sample='{"id": 1, "name": "Ito", "books": [{"id": 1, "title": "Tokyo Nights"}]}',
         hints=["Nested Pydantic models with from_attributes=True", "selectinload to avoid N+1"]),
    dict(title="Docs a Teammate Can Use", level="Stretch", concepts="OpenAPI metadata, Codex",
         text="Add app title, version and description; tags with descriptions; summary and 404 responses on every "
              "endpoint; and examples on models. You may ask Codex to draft them; check each one matches the code. "
              "Export /openapi.json to a file.",
         sample="openapi.json saved, /docs shows grouped, described endpoints",
         hints=["FastAPI(openapi_tags=[...])", "json.dump(app.openapi(), f, indent=2)"]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "In an ORM, a Python class maps to a database ________.",
        "In SQLAlchemy, the ________ manages a unit of work and commits changes.",
        "In a one-to-many relationship, the foreign key goes on the ________ side.",
        "A many-to-many relationship needs an extra ________ table.",
        "relationship(________=\"books\") links both sides of a relationship.",
        "The column option ________=True stops duplicate values.",
        "To undo changes in a failed transaction, call ________.",
        "The A in ACID stands for ________.",
        "FastAPI serves its OpenAPI schema at the path ________.",
        "Loading related rows up front with selectinload avoids the ________ query problem.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "What problem does an ORM solve? Name two benefits.",
        "Explain one-to-many and many-to-many with SmartDesk examples.",
        "Why are transactions important for a payment or billing system?",
        "What would you add to an endpoint so a new developer understands it without reading code?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        "# authors: Ito has books A, B; Rao has book C\nfor a in session.scalars(select(Author).order_by(Author.name)):\n    print(a.name, len(a.books))",
        "# balance starts at 100\ntry:\n    acc.balance -= 50\n    raise ValueError(\"fail\")\n    session.commit()\nexcept ValueError:\n    session.rollback()\nprint(session.get(Account, 1).balance)",
        "app = FastAPI(title=\"Shop\", version=\"2.0\")\nprint(app.openapi()[\"info\"])",
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write SQLAlchemy models for Customer and Ticket (one-to-many)."),
        dict(q="Write a query that returns all high priority tickets for one customer, newest first."),
        dict(q="Write a function that saves two objects in one transaction with rollback on error."),
        dict(q="Write a FastAPI endpoint with a summary, tags and a 404 response description."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="ORM basics, relationships, transactions and Swagger / OpenAPI docs", cells=[
    ("md", "## 1. Setup"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q fastapi httpx sqlalchemy pydantic

# ===== Option B: VS Code / local (run in your activated venv terminal) =====
# pip install fastapi uvicorn httpx sqlalchemy pydantic
import sqlalchemy
print("SQLAlchemy", sqlalchemy.__version__)'''),
    ("md", "## 2. ORM basics: one table\nSQLite is a database stored in a single file. No server needed, so it works in Colab and VS Code alike."),
    ("code", '''import os
from sqlalchemy import create_engine, select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

if os.path.exists("intro.db"):
    os.remove("intro.db")
engine0 = create_engine("sqlite:///intro.db", echo=False)   # echo=True prints the SQL

class Base0(DeclarativeBase):
    pass

class BookRow(Base0):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str]
    pages: Mapped[int]

Base0.metadata.create_all(engine0)
with Session(engine0) as s:
    s.add_all([BookRow(title="Ikigai", author="Garcia", pages=208),
               BookRow(title="Deep Work", author="Newport", pages=296),
               BookRow(title="Atomic Habits", author="Clear", pages=320),
               BookRow(title="The Little Prince", author="Saint-Exupery", pages=96)])
    s.commit()

with Session(engine0) as s:
    stmt = select(BookRow).where(BookRow.pages > 200).order_by(BookRow.title)
    print([b.title for b in s.scalars(stmt)])
    book = s.get(BookRow, 1)
    book.pages = 210                  # update: change the attribute
    s.delete(s.get(BookRow, 4))       # delete
    s.commit()
    print([(b.title, b.pages) for b in s.scalars(select(BookRow))])'''),
    ("md", "### TODO 1: Turn on `echo=True` in `create_engine` and rerun a query. Read the SQL that SQLAlchemy writes for you."),
    ("code", "# TODO: write your code here"),
    ("md", "## 3. Models with relationships"),
    ("code", '''%%writefile models.py
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

book_tags = Table(
    "book_tags", Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    books: Mapped[list["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    pages: Mapped[int] = mapped_column(default=0)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[Author] = relationship(back_populates="books")
    tags: Mapped[list["Tag"]] = relationship(secondary=book_tags, back_populates="books")

class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    books: Mapped[list[Book]] = relationship(secondary=book_tags, back_populates="tags")

class Account(Base):
    __tablename__ = "accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str]
    balance: Mapped[int]'''),
    ("code", '''import importlib, models
importlib.reload(models)
from models import Base, Author, Book, Tag, Account
from sqlalchemy.orm import selectinload

if os.path.exists("library.db"):
    os.remove("library.db")
engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)
print(list(Base.metadata.tables))'''),
    ("md", "## 4. Create linked data"),
    ("code", '''with Session(engine) as s:
    fiction, travel, tech = Tag(name="fiction"), Tag(name="travel"), Tag(name="tech")
    ito = Author(name="Ito")
    rao = Author(name="Rao")
    ito.books = [Book(title="Tokyo Nights", pages=240, tags=[fiction, travel]),
                 Book(title="Rain in Kyoto", pages=180, tags=[fiction])]
    rao.books = [Book(title="Monsoon Code", pages=320, tags=[tech]),
                 Book(title="Chai Stories", pages=150, tags=[fiction, travel])]
    s.add_all([ito, rao])
    s.commit()

with Session(engine) as s:
    stmt = select(Author).options(selectinload(Author.books).selectinload(Book.tags))
    for a in s.scalars(stmt):
        for b in a.books:
            print(f"{a.name:<4} | {b.title:<14} | {[t.name for t in b.tags]}")'''),
    ("md", "## 5. Query across relationships"),
    ("code", '''with Session(engine) as s:
    stmt = select(Book).join(Book.author).where(Author.name == "Rao")
    print("By Rao:", [b.title for b in s.scalars(stmt)])

    stmt = select(Book).join(Book.tags).where(Tag.name == "fiction").order_by(Book.title)
    print("Fiction:", [b.title for b in s.scalars(stmt)])'''),
    ("md", "## 6. Constraints and IntegrityError"),
    ("code", '''from sqlalchemy.exc import IntegrityError
with Session(engine) as s:
    try:
        s.add(Author(name="Ito"))        # name must be unique
        s.commit()
    except IntegrityError as e:
        s.rollback()
        print("Rejected:", str(e.orig))'''),
    ("md", "## 7. Transactions: a safe transfer"),
    ("code", '''with Session(engine) as s:
    s.add_all([Account(owner="Hana", balance=1000), Account(owner="Arjun", balance=500)])
    s.commit()

def transfer(from_id, to_id, amount):
    with Session(engine) as s:
        try:
            a, b = s.get(Account, from_id), s.get(Account, to_id)
            if a is None or b is None:
                raise ValueError("Account not found")
            a.balance -= amount
            if a.balance < 0:
                raise ValueError("Insufficient balance")
            b.balance += amount
            s.commit()
            print(f"Transferred {amount}")
        except ValueError as e:
            s.rollback()
            print("Failed:", e)

def balances():
    with Session(engine) as s:
        return [(x.owner, x.balance) for x in s.scalars(select(Account))]

transfer(1, 2, 300); print(balances())
transfer(1, 2, 9999); print(balances())   # unchanged after rollback
transfer(1, 7, 10); print(balances())'''),
    ("md", "### TODO 2: Add a `transfer_log` list that records successful transfers only."),
    ("code", "# TODO: write your code here"),
    ("md", "## 8. A documented FastAPI app on top"),
    ("code", '''%%writefile library_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload
from models import Author, Book

engine = create_engine("sqlite:///library.db")

tags_metadata = [
    {"name": "Books", "description": "Browse books with their author and tags."},
    {"name": "Authors", "description": "Authors and the books they wrote."},
]
app = FastAPI(title="Library API", version="1.2.0",
              description="A small library service built in the Day 6 class.",
              openapi_tags=tags_metadata)

class BookShort(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    title: str = Field(examples=["Tokyo Nights"])

class BookOut(BookShort):
    pages: int
    author_name: str
    tags: list[str]

class AuthorOut(BaseModel):
    model_config = {"from_attributes": True}
    id: int
    name: str
    books: list[BookShort]

@app.get("/books", tags=["Books"], summary="List all books", response_model=list[BookOut])
def list_books():
    """Returns every book with its author name and tag names."""
    with Session(engine) as s:
        rows = s.scalars(select(Book).options(selectinload(Book.author), selectinload(Book.tags)))
        return [BookOut(id=b.id, title=b.title, pages=b.pages, author_name=b.author.name,
                        tags=[t.name for t in b.tags]) for b in rows]

@app.get("/authors/{author_id}", tags=["Authors"], summary="Get one author with books",
         response_model=AuthorOut, responses={404: {"description": "Author not found"}})
def get_author(author_id: int):
    """Returns one author and the short list of their books."""
    with Session(engine) as s:
        a = s.get(Author, author_id, options=[selectinload(Author.books)])
        if a is None:
            raise HTTPException(404, "Author not found")
        return AuthorOut.model_validate(a)'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
import library_api
importlib.reload(library_api)
from fastapi.testclient import TestClient
client = TestClient(library_api.app)

# ===== Option B: VS Code =====
# Terminal: uvicorn library_api:app --reload
# Then open http://127.0.0.1:8000/docs and http://127.0.0.1:8000/redoc

print(client.get("/books").json()[0])
print(client.get("/authors/1").json())
print(client.get("/authors/99").status_code)'''),
    ("md", "## 9. Look inside the OpenAPI contract"),
    ("code", '''import json
spec = library_api.app.openapi()
print(spec["info"])
print("Paths:", list(spec["paths"]))
print("Schemas:", list(spec["components"]["schemas"]))
print("404 documented:", "404" in spec["paths"]["/authors/{author_id}"]["get"]["responses"])
with open("openapi.json", "w") as f:
    json.dump(spec, f, indent=2)
print("Saved openapi.json")'''),
    ("md", "### TODO 3: Add a `GET /tags/{name}/books` endpoint with a summary, a tag and a 404 response, then check it appears in the spec."),
    ("code", "# TODO: write your code here"),
    ("md", "### TODO 4 (SmartDesk step 5): model `Customer` (one-to-many) `Ticket` (one-to-many) `Comment` in SQLite, "
           "and close a ticket plus add its closing comment in one transaction."),
    ("code", "# TODO: write your code here"),
])
