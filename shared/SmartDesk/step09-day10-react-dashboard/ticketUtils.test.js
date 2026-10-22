import test from "node:test";
import assert from "node:assert/strict";
import { filterTickets, sortByPriority } from "./src/ticketUtils.js";

const t = [
  { id: 2, priority: "low", status: "open", customer: "Rin", body: "Store hours" },
  { id: 1, priority: "high", status: "closed", customer: "Aiko", body: "No signal" },
  { id: 3, priority: "high", status: "open", customer: "Kenji", body: "Login fails" },
];

test("sorts high priority first, then by id", () => {
  assert.deepEqual(sortByPriority(t).map((x) => x.id), [1, 3, 2]);
});

test("filters by status and text", () => {
  assert.deepEqual(filterTickets(t, { status: "open" }).map((x) => x.id), [2, 3]);
  assert.deepEqual(filterTickets(t, { text: "SIGNAL" }).map((x) => x.id), [1]);
});
