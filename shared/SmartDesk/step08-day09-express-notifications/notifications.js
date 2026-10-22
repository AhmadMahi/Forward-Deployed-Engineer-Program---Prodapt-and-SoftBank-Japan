// Pure notification logic, kept separate from Express so it is easy to test.
const CHANNELS = ["email", "sms"];

export function validateNotification(body) {
  const errors = [];
  if (!Number.isInteger(body?.ticketId)) errors.push("ticketId must be an integer");
  if (!CHANNELS.includes(body?.channel)) errors.push(`channel must be one of ${CHANNELS.join(", ")}`);
  if (typeof body?.message !== "string" || !body.message.trim()) errors.push("message is required");
  if (body?.message?.length > 300) errors.push("message must be 300 characters or fewer");
  return errors;
}

export function createStore() {
  const items = [];
  return {
    add(n) {
      const item = { id: items.length + 1, status: "queued", createdAt: new Date().toISOString(), ...n };
      items.push(item);
      return item;
    },
    list(ticketId) {
      return ticketId ? items.filter((i) => i.ticketId === ticketId) : [...items];
    },
    markSent(id) {
      const item = items.find((i) => i.id === id);
      if (!item) return null;
      item.status = "sent";
      return item;
    },
  };
}
