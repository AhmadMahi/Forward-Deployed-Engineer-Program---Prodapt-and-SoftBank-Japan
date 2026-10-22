import test from "node:test";
import assert from "node:assert/strict";
import { fetchTickets, fetchWithRetry, summarise } from "./client.js";

const sample = [
  { id: 1, priority: "high", status: "open" },
  { id: 2, priority: "low", status: "closed" },
  { id: 3, priority: "high", status: "in_progress" },
];

test("summarise counts by priority and open", () => {
  assert.deepEqual(summarise(sample), { total: 3, open: 2, byPriority: { high: 2, low: 1 } });
});

test("fetchTickets builds the URL and parses JSON", async () => {
  let called = "";
  const fakeFetch = async (url) => { called = url; return { ok: true, json: async () => sample }; };
  const data = await fetchTickets("http://api.test", { status: "open", fetchFn: fakeFetch });
  assert.equal(called, "http://api.test/tickets?status=open");
  assert.equal(data.length, 3);
});

test("fetchTickets throws on HTTP errors", async () => {
  const fakeFetch = async () => ({ ok: false, status: 500 });
  await assert.rejects(() => fetchTickets("http://api.test", { fetchFn: fakeFetch }), /API error 500/);
});

test("fetchWithRetry retries then succeeds", async () => {
  let n = 0;
  const result = await fetchWithRetry(async () => { if (++n < 3) throw new Error("down"); return "ok"; }, { delayMs: 1 });
  assert.equal(result, "ok");
  assert.equal(n, 3);
});
