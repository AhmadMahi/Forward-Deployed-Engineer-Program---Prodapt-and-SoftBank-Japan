// All calls go to our own API. No secrets or API keys ever live in front-end code.
const BASE = import.meta.env?.VITE_API_URL ?? "http://localhost:8000";

async function request(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, { headers: { "Content-Type": "application/json" }, ...options });
  if (!res.ok) throw new Error((await res.json().catch(() => ({}))).detail ?? `HTTP ${res.status}`);
  return res.json();
}

export const api = {
  list: () => request("/api/tickets"),
  create: (t) => request("/api/tickets", { method: "POST", body: JSON.stringify(t) }),
  update: (id, patch) => request(`/api/tickets/${id}`, { method: "PATCH", body: JSON.stringify(patch) }),
  close: (id) => request(`/api/tickets/${id}/close`, { method: "POST" }),
};
