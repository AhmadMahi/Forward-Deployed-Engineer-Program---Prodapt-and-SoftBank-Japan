# Day 4: App Build Prompts

**App of the day:** Inventory Dashboard (Python + MongoDB + Matplotlib)

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

OpenAI Codex is **not required today**. You can build these yourself in Colab, or use Codex in VS Code if you want practice.

1. Read each prompt as a specification and build one feature at a time.
2. If you use Codex: open the project folder in VS Code, paste one prompt at a time, ask for a plan first, and read every diff before you accept it.
3. Run your code after every step. Do not move to the next prompt until the current version runs without errors.
4. Never paste API keys, connection strings, customer data or credentials into a prompt. Read `MONGO_URI` from the environment.

> Uses Days 2 to 4: OOP, exceptions, MongoDB CRUD with PyMongo (or mongomock in Colab), indexes and Matplotlib. This is the data layer you will put behind an API on Day 5.

---

## Prompt 1: Build the data layer and CLI

```text
You are a senior Python mentor. Build an "Inventory Dashboard" command line app.
Tech: Python 3.12, PyMongo. Support two modes chosen by an environment variable:
- USE_MOCK=1 uses mongomock (for Google Colab)
- otherwise connect to MongoDB using MONGO_URI (default mongodb://localhost:27017)
Structure (layered, one responsibility each):
- db.py: get_collection() returns the products collection and creates indexes
  (unique on sku, compound on category + price)
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

## Prompt 3: Review my data model

```text
Act as a code reviewer for the Inventory Dashboard:
- Draw a text diagram of the layers and how a "restock" request flows through them.
- Suggest a price history design: embed a list of changes or reference a separate collection? Explain.
- List the indexes you would add and the queries each one speeds up.
Finish with 5 quiz questions with answers.
```

---

## SmartDesk step 3: Tickets in MongoDB; chart by priority

```text
SmartDesk step 3. Move SmartDesk tickets from tickets.json into MongoDB.
- Use mongomock when USE_MOCK=1, otherwise MONGO_URI from the environment. Never hard-code a connection string.
- Collections: customers and tickets. A ticket references its customer by customer_id and
  embeds its notes: [{by, text, at}].
- Indexes: unique on ticket_no, and on status.
- TicketRepository with add, get, list_by_status, add_note, close.
- A one-off migrate_json.py that loads tickets.json from step 2 and inserts them.
- charts.py: bar chart of open tickets by priority, saved as tickets_by_priority.png.
Keep the Ticket, Customer and Agent classes from step 2; convert to and from documents in the repository.
Show the folder structure and a sample run.
```

**Check before you finish:** inserting a duplicate ticket_no is rejected; the chart matches a manual count; no connection string in the code.

---

## Stretch ideas (try on your own)

- Seed 50 random products and time the same query with and without an index on a real MongoDB (use explain()).
- Add a price history list to each product using $push on every price change.
- Export the low stock report to CSV.
