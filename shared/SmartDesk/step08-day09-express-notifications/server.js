// SmartDesk step 08: Express notification service.
// npm install && npm start, then import postman_collection.json into Postman.
import express from "express";
import { createStore, validateNotification } from "./notifications.js";

const app = express();
app.use(express.json({ limit: "10kb" }));
const store = createStore();

app.get("/health", (req, res) => res.json({ status: "ok" }));

app.post("/notifications", (req, res) => {
  const errors = validateNotification(req.body);
  if (errors.length) return res.status(400).json({ errors });
  res.status(201).json(store.add(req.body));
});

app.get("/notifications", (req, res) => {
  const ticketId = req.query.ticketId ? Number(req.query.ticketId) : undefined;
  res.json(store.list(ticketId));
});

app.post("/notifications/:id/send", async (req, res, next) => {
  try {
    const item = store.markSent(Number(req.params.id));
    if (!item) return res.status(404).json({ error: "Not found" });
    res.json(item);
  } catch (err) {
    next(err);                         // async errors go to the error handler
  }
});

app.use((err, req, res, next) => {
  console.error(err);
  res.status(500).json({ error: "Internal error" });
});

const port = process.env.PORT ?? 3001;
app.listen(port, () => console.log(`Notifications on http://localhost:${port}`));
