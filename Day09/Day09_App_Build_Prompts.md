# Day 9: App Build Prompts

**App of the day:** Shop Analytics API (FastAPI + MongoDB) with a JavaScript data script

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Copy one prompt at a time into your AI coding assistant (Claude, ChatGPT, Copilot Chat or similar).
2. Run the generated code in Google Colab or VS Code.
3. Read every line. If something is unclear, ask the assistant to explain it before moving on.
4. Do not move to the next prompt until the current version runs without errors.

> Uses Days 1 to 9. The backend gains pagination, analytics and indexes. The JavaScript part prepares you for Node.js and React.

---

## Prompt 1: Build the analytics API

```text
You are a senior backend mentor. Build a "Shop Analytics API" with FastAPI and PyMongo.
Support USE_MOCK=1 (mongomock, for Colab) or MONGO_URI for a real MongoDB.

Collections: products {sku unique, name, category, price, stock}, orders {product_sku, category,
amount, status: paid|pending|cancelled, created_at}.

Endpoints:
- Full CRUD for products with Pydantic models, ObjectId validation and 404s.
- GET /products: page and size (max 50), filters category, min_price, max_price, sort by price or name.
  Response: {page, size, total, total_pages, items}.
- GET /products/feed?after=<sku>&limit=10 using cursor pagination.
- GET /stats/revenue-by-category (paid only, sorted), GET /stats/low-stock (stock < 5, grouped),
  GET /stats/daily-revenue (group by date string).
- On startup: create indexes (sku unique; category + price compound; status + created_at).
- A POST /seed endpoint that inserts realistic sample data.
Layered structure (routers, schemas, db). Tests with TestClient for pagination maths and stats.
```

---

## Prompt 2: JavaScript report script

```text
Write a Node.js script report.js (no libraries) that:
1. Fetches GET http://127.0.0.1:8000/products?size=50 using fetch.
2. Prints the number of products per category, the total stock value, and the 3 cheapest products.
3. Uses const/let, arrow functions, map, filter, reduce, destructuring and template literals.
Explain each JavaScript feature with a one-line comment. Also give a version that reads the
same data from a local products.json file for when the API is not running.
```

---

## Prompt 3: Explain and quiz

```text
Explain to a beginner: (1) how the revenue aggregation pipeline works stage by stage,
(2) why the compound index helps the product list query, (3) offset vs cursor pagination.
Then 5 quiz questions with answers, including two on JavaScript.
```

---

## Stretch ideas (try on your own)

- Add $lookup to show product names on orders.
- Add a text index and a /products/search?q= endpoint.
- Draw a revenue chart from /stats/revenue-by-category with Matplotlib.
