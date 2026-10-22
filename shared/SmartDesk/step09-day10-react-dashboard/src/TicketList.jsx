import { sortByPriority } from "./ticketUtils.js";

function PriorityBadge({ priority }) {
  const colours = { high: "#FF8A3D", medium: "#0FA3A3", low: "#3D7C82" };
  return <span style={{ background: colours[priority], color: "white", padding: "2px 8px", borderRadius: 8 }}>{priority}</span>;
}

export default function TicketList({ tickets, onSelect }) {
  return (
    <ul style={{ listStyle: "none", padding: 0 }}>
      {sortByPriority(tickets).map((t) => (
        <li key={t.id} onClick={() => onSelect(t)} style={{ padding: 8, borderBottom: "1px solid #E5E7EB", cursor: "pointer" }}>
          <PriorityBadge priority={t.priority} /> <strong>#{t.id}</strong> {t.customer}: {t.body}
        </li>
      ))}
    </ul>
  );
}
