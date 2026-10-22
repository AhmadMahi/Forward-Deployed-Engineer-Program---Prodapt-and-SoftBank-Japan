import { useEffect, useState } from "react";
import { api } from "./api.js";

export default function TicketBoard() {
  const [tickets, setTickets] = useState([]);
  const [state, setState] = useState("loading");        // loading | error | ready
  const [error, setError] = useState("");
  const [form, setForm] = useState({ customer: "", category: "network", priority: "medium", body: "" });

  useEffect(() => {
    api.list().then((data) => { setTickets(data); setState("ready"); })
      .catch((e) => { setError(e.message); setState("error"); });
  }, []);

  async function submit(e) {
    e.preventDefault();
    try {
      const created = await api.create(form);
      setTickets((prev) => [...prev, created]);
      setForm({ ...form, body: "" });
    } catch (e) { setError(e.message); }
  }

  async function close(id) {
    const updated = await api.close(id);
    setTickets((prev) => prev.map((t) => (t.id === id ? updated : t)));
  }

  if (state === "loading") return <p>Loading tickets...</p>;
  if (state === "error") return <p role="alert">Could not load tickets: {error}</p>;
  return (
    <section>
      <form onSubmit={submit}>
        <input placeholder="Customer" value={form.customer} onChange={(e) => setForm({ ...form, customer: e.target.value })} />
        <input placeholder="Describe the problem" value={form.body} onChange={(e) => setForm({ ...form, body: e.target.value })} />
        <button disabled={!form.customer || !form.body}>Create</button>
      </form>
      {tickets.length === 0 ? <p>No tickets yet.</p> : (
        <ul>{tickets.map((t) => (
          <li key={t.id}>#{t.id} [{t.status}] {t.customer}: {t.body}
            {t.status !== "closed" && <button onClick={() => close(t.id)}>Close</button>}</li>))}
        </ul>)}
    </section>
  );
}
