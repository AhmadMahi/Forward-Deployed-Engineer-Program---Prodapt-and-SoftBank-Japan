// Minimal tests with no extra libraries: node test.js
const assert = require("assert");
const { buildMessage } = require("./index");

assert.strictEqual(
  buildMessage({ id: 4, customer: "Ken", status: "closed", priority: "medium" }),
  "Ticket 4 for Ken is now closed."
);
assert.strictEqual(
  buildMessage({ id: 1, customer: "Aiko", status: "open", priority: "high" }),
  "[URGENT] Ticket 1 for Aiko is now open."
);
console.log("notifier tests passed");
