import { useState } from "react";
import TicketList from "./TicketList.jsx";
import { filterTickets } from "./ticketUtils.js";
import sample from "../../data/tickets.json";

export default function App() {
  const [status, setStatus] = useState("all");
  const [text, setText] = useState("");
  const [selected, setSelected] = useState(null);
  const visible = filterTickets(sample, { status, text });

  return (
    <main style={{ fontFamily: "Calibri, sans-serif", maxWidth: 900, margin: "0 auto" }}>
      <h1 style={{ color: "#0E3B43" }}>SmartDesk dashboard</h1>
      <input placeholder="Search tickets" value={text} onChange={(e) => setText(e.target.value)} />
      <select value={status} onChange={(e) => setStatus(e.target.value)}>
        {["all", "open", "in_progress", "closed"].map((s) => <option key={s}>{s}</option>)}
      </select>
      <p>{visible.length} ticket(s)</p>
      <TicketList tickets={visible} onSelect={setSelected} />
      {selected && <aside><h2>Ticket #{selected.id}</h2><p>{selected.body}</p></aside>}
    </main>
  );
}
