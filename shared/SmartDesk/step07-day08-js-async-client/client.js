// SmartDesk step 07: a JavaScript client that reads the ticket API asynchronously.
// Run against the step 04 or 05 API:  API_URL=http://127.0.0.1:8000 node client.js

export async function fetchTickets(baseUrl, { status, fetchFn = fetch } = {}) {
  const url = new URL("/tickets", baseUrl);
  if (status) url.searchParams.set("status", status);
  const res = await fetchFn(url.toString());
  if (!res.ok) throw new Error(`API error ${res.status}`);
  return res.json();
}

export function summarise(tickets) {
  const byPriority = {};
  for (const t of tickets) byPriority[t.priority] = (byPriority[t.priority] ?? 0) + 1;
  const open = tickets.filter((t) => t.status !== "closed").length;
  return { total: tickets.length, open, byPriority };
}

export async function fetchWithRetry(fn, { retries = 2, delayMs = 200 } = {}) {
  for (let attempt = 0; ; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (attempt >= retries) throw err;
      await new Promise((r) => setTimeout(r, delayMs * 2 ** attempt));
    }
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const base = process.env.API_URL ?? "http://127.0.0.1:8000";
  try {
    const tickets = await fetchWithRetry(() => fetchTickets(base));
    console.log(JSON.stringify(summarise(tickets), null, 2));
  } catch (err) {
    console.error("Could not reach the API:", err.message);
    process.exitCode = 1;
  }
}
