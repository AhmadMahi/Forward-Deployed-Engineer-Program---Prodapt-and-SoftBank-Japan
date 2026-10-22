# Day 4: App Build Prompts

**App of the day:** Inventory Dashboard (Python + MongoDB + Matplotlib)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 4: OOP, exceptions, MongoDB CRUD with PyMongo (or mongomock in Colab) and Matplotlib. This is the data layer you will put behind an API on Day 5 and 6.

---

## Prompt 1: Build the data layer and CLI

```text
You are a senior Python mentor. Build an "Inventory Dashboard" command line app.

Tech: Python 3.11, PyMongo. Support two modes chosen by an environment variable:
- USE_MOCK=1 uses mongomock (for Google Colab)
- otherwise connect to MongoDB using MONGO_URI (default mongodb://localhost:27017)

Structure (layered, one responsibility each):
- db.py: get_collection() returns the products collection
- repository.py: ProductRepository with add, get, list(filters), update, delete
- service.py: InventoryService with business rules (price > 0, stock >= 0, unique SKU,
  raise custom exceptions ValidationError and NotFoundError)
- main.py: menu loop: add product, list all, filter by category or max price,
  restock, change price, delete, low stock report (stock < 5)

Product document: {sku, name, category, price, stock, created_at}
Include comments, then show a sample run and the folder structure.
```

---

## Prompt 2: Add charts and reports

```text
Extend the Inventory Dashboard:
1. reports.py with functions that use Matplotlib:
   - bar chart of stock value (price x stock) per category
   - pie chart of product count per category
   - horizontal bar chart of the 5 lowest stock items
   Save each as PNG in a reports/ folder and also show it.
2. Add menu option "Generate reports".
3. Add sorting and a limit to the list command (for example: top 10 by price).
Show only the new and changed files.
```

---

## Prompt 3: Review my architecture

```text
Act as a code reviewer. For the Inventory Dashboard:
- Draw a text diagram of the layers and how a "restock" request flows through them.
- Point out one place where the code breaks single responsibility, if any, and fix it.
- Explain what would need to change to put this behind a REST API tomorrow.
Finish with 5 quiz questions with answers.
```

---

## Stretch ideas (try on your own)

- Seed 50 random products using the random module and time how long the queries take.
- Add a price history list to each product using $push on every price change.
- Export the low stock report to CSV.
