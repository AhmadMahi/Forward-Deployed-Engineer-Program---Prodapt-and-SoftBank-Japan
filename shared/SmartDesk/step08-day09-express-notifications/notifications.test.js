import test from "node:test";
import assert from "node:assert/strict";
import { createStore, validateNotification } from "./notifications.js";

test("valid notification has no errors", () => {
  assert.deepEqual(validateNotification({ ticketId: 1, channel: "sms", message: "We are on it" }), []);
});

test("invalid notification lists every error", () => {
  assert.equal(validateNotification({ ticketId: "1", channel: "fax", message: "" }).length, 3);
});

test("store adds, filters and marks sent", () => {
  const s = createStore();
  s.add({ ticketId: 1, channel: "email", message: "a" });
  s.add({ ticketId: 2, channel: "sms", message: "b" });
  assert.equal(s.list(2).length, 1);
  assert.equal(s.markSent(1).status, "sent");
  assert.equal(s.markSent(99), null);
});
