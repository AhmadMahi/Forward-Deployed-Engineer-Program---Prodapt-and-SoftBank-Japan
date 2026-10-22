// Pure helpers used by the dashboard. Tested with node --test.
export const PRIORITY_ORDER = { high: 0, medium: 1, low: 2 };

export function sortByPriority(tickets) {
  return [...tickets].sort((a, b) => PRIORITY_ORDER[a.priority] - PRIORITY_ORDER[b.priority] || a.id - b.id);
}

export function filterTickets(tickets, { status = "all", text = "" } = {}) {
  const q = text.trim().toLowerCase();
  return tickets.filter((t) => (status === "all" || t.status === status)
    && (!q || t.body.toLowerCase().includes(q) || t.customer.toLowerCase().includes(q)));
}
