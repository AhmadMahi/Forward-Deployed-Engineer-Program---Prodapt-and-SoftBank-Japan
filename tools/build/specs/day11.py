"""Day 11 spec. React UI Logic and Full-Stack Integration.
Source: REUSE archive/v1-40-day/Day12. NEW (v4): never ship API keys in front-end code.
"""
DAY = 11
FOLDER = "Day11-React-UI-Logic-and-Full-Stack"
SLUG = "React_UI_Logic_and_Full_Stack"
TITLE = "React UI Logic and Full Stack"
SUBTITLE = "Conditional rendering, lists and keys, loading data safely, keeping keys off the front end, and React with FastAPI"
DATE = "Tue 10 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 12: the first GenAI day. Introduction to GenAI, LLMs and tokens."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 10"),
        ("Conditional UI", "Show the right thing at the right time"),
        ("Lists and keys", "Render arrays of data"),
        ("Fetch states", "Loading, error, empty and data"),
        ("Keys stay server-side", "Never ship API keys to the browser. NEW (v4)"),
        ("React + FastAPI", "SmartDesk full stack, end to end"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Branch the UI", "Use &&, ternaries and early returns to show the right view."),
        ("Render lists", "Map arrays to components with stable keys."),
        ("Fetch data safely", "Handle loading, error and empty states, and keep secrets on the server."),
        ("Go full stack", "Create, update and close SmartDesk tickets from React through FastAPI."),
    ]),
    dict(type="table", title="Today's sessions", header=["Session", "Duration", "Topics"], rows=[
        ["Opening", "30 min", "Kahoot / recap quiz on Day 10"],
        ["Session 1", "1.5 hrs", "Conditional rendering, lists and keys"],
        ["Session 2", "2 hrs", "Fetch with loading, error and empty states; NEW (v4) never ship API keys in front-end code"],
        ["Session 3", "3 hrs", "Full stack: React app consuming FastAPI with CRUD"],
    ]),

    dict(type="section", title="Conditional rendering and lists", sub="Session 1 | 1.5 hrs | Different data, different screen"),
    dict(type="table", title="Three ways to show things conditionally", header=["Pattern", "Use when", "Example"], rows=[
        ["&&", "Show something or nothing", "{isAdmin && <AdminPanel />}"],
        ["? :", "Choose between two things", "{loggedIn ? <Logout /> : <Login />}"],
        ["Early return", "Whole component changes", "if (loading) return <Spinner />;"],
    ], note="Careful: {count && <p>...</p>} shows 0 when count is 0. Use {count > 0 && ...}."),
    dict(type="bullets_code", title="Early returns for clear screens", bullets=[
        "Handle special cases first",
        "The main view stays simple",
        "Every state has a clear screen",
        "Users always know what is happening",
    ], code='''function Tickets({ loading, error, tickets }) {
  if (loading) return <p>Loading tickets...</p>;
  if (error) return <p>Error: {error}</p>;
  if (tickets.length === 0)
    return <p>No tickets yet.</p>;

  return <p>{tickets.length} tickets</p>;
}'''),
    dict(type="bullets_code", title="Rendering a list with map", bullets=[
        "map turns each item into JSX",
        "Every item needs a unique key",
        "Use an id from your data",
        "Avoid the array index if items move",
    ], code='''const tickets = [
  { id: 1, title: "No signal", done: true },
  { id: 2, title: "Double charge", done: false },
];

<ul>
  {tickets.map(t => (
    <li key={t.id}
        className={t.done ? "done" : ""}>
      {t.title}
    </li>
  ))}
</ul>'''),
    dict(type="cards", title="Why keys matter", greet="Hitotsu hitotsu (一つ一つ): One by one", items=[
        ("Identity", "Keys tell React which item is which between renders."),
        ("Efficiency", "React updates only the items that changed."),
        ("Correctness", "Without stable keys, inputs and checkboxes can jump between rows."),
    ]),
    dict(type="bullets_code", title="Filter, sort and derive", bullets=[
        "Keep the original list in state",
        "Derive the visible list when rendering",
        "No extra state for computed values",
        "Search boxes work this way",
    ], code='''const [query, setQuery] = useState("");
const [hideClosed, setHide] = useState(false);

const visible = tickets
  .filter(t => !hideClosed || t.status !== "closed")
  .filter(t => t.title.toLowerCase()
    .includes(query.toLowerCase()))
  .sort((a, b) =>
    a.title.localeCompare(b.title));'''),

    dict(type="section", title="Loading data", sub="Session 2 | 2 hrs | useEffect, fetch and the four states"),
    dict(type="flow", title="Life of a data-loading component", items=[
        ("First render", "Show loading state"),
        ("useEffect runs", "After the screen is drawn"),
        ("fetch", "Request JSON from the API"),
        ("setState", "Save data or error, React re-renders"),
    ]),
    dict(type="bullets_code", title="useEffect + fetch", bullets=[
        "The empty [] means: run once on mount",
        "Track loading and error in state",
        "Check res.ok before reading JSON",
        "Always show something for each state",
    ], code='''const [tickets, setTickets] = useState([]);
const [loading, setLoading] = useState(true);
const [error, setError] = useState(null);

useEffect(() => {
  fetch(API + "/api/tickets")
    .then(res => {
      if (!res.ok) throw new Error(res.status);
      return res.json();
    })
    .then(setTickets)
    .catch(err => setError(err.message))
    .finally(() => setLoading(false));
}, []);'''),
    dict(type="table", title="Design all four states", header=["State", "What the user sees", "SmartDesk example"], rows=[
        ["Loading", "A short message or spinner", "Loading tickets..."],
        ["Error", "A clear message and a Retry button", "Could not load tickets [Retry]"],
        ["Empty", "A friendly message with a next step", "No open tickets. Create one?"],
        ["Data", "The actual content", "12 tickets, newest first"],
    ], note="Great apps design all four states, not just the happy one."),
    dict(type="section", title="Never ship API keys in front-end code", sub="Session 2 | Everything in the browser is public", new=True),
    dict(type="cards", title="Why front-end keys always leak", new=True, items=[
        ("The bundle is public", "Every user downloads your JavaScript. Anyone can open it in DevTools."),
        ("Build variables are inlined", "Vite replaces VITE_ variables with their values at build time."),
        ("Network tab", "Headers sent from the browser, including Authorization, are visible."),
        ("Real cost", "A leaked LLM key can be used by anyone, on your bill, until it is revoked."),
    ]),
    dict(type="compare", title="Unsafe and safe patterns", new=True, left=dict(title="Unsafe: key in the browser", bullets=[
        "VITE_OPENAI_KEY in .env", "fetch to the LLM API from React", "Key visible in dist/assets/*.js",
        "Anyone can copy and reuse it",
    ]), right=dict(title="Safe: key on your server", bullets=[
        "Key in the server's environment or a secret store", "React calls your own API: /api/...",
        "FastAPI calls the LLM and returns only the answer", "Add auth and rate limits on your endpoint",
    ]), note="The browser should only ever hold short-lived user tokens, never provider keys."),
    dict(type="flow", title="The safe request path", new=True, items=[
        ("React", "Calls your API: /api/.../suggest"),
        ("FastAPI", "Checks the user, validates input"),
        ("Server secret", "Reads OPENAI_API_KEY from env"),
        ("LLM API", "Called from the server only"),
        ("Response", "Only the answer goes back"),
    ], note="You will use exactly this path from Day 12, when SmartDesk makes its first LLM call."),
    dict(type="bullets_code", title="Check your build for secrets", new=True, bullets=[
        "Build, then search the dist folder",
        "Look for key patterns and env names",
        "Run it in CI (Day 20)",
        "Found one? Revoke it first, then fix",
    ], code='''$ npm run build
$ grep -rE "sk-|VITE_.*KEY|Bearer " dist/

# Nothing should be found.
# If a real key was ever shipped:
# 1. Revoke it now
# 2. Move the call to the server
# 3. Create a new key, store it safely'''),

    dict(type="section", title="React + FastAPI", sub="Session 3 | 3 hrs | Two halves of one app"),
    dict(type="flow", title="A full stack request", items=[
        ("React (5173)", "Agent clicks Close"),
        ("fetch PATCH", "JSON to the API"),
        ("FastAPI (8000)", "Validates with Pydantic, saves"),
        ("200 + JSON", "React updates the list"),
    ], note="Two different ports means two different origins, so the browser asks the API for CORS permission."),
    dict(type="bullets_code", title="Sending data with POST and PATCH", bullets=[
        "Same fetch, with method and body",
        "Set Content-Type to JSON",
        "Update state with the server's reply",
        "Disable the button while saving",
    ], code='''async function closeTicket(t) {
  const res = await fetch(
    `${API}/api/tickets/${t.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json" },
      body: JSON.stringify({ status: "closed" }),
    });
  if (!res.ok) throw new Error("Save failed");
  const updated = await res.json();
  setTickets(prev => prev.map(
    x => x.id === t.id ? updated : x));
}'''),
    dict(type="bullets_code", title="Enabling CORS in FastAPI", bullets=[
        "List the front end's origin",
        "Allow the methods and headers you use",
        "Never use * with credentials in production",
        "Same setting you saw on Day 7",
    ], code='''from fastapi.middleware.cors import (
    CORSMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)'''),
    dict(type="compare", title="Two ways to run the full stack", left=dict(title="Separate (real projects)", bullets=[
        "Vite dev server on port 5173", "FastAPI on port 8000", "CORS configured on the API",
        "Deployed separately later (Week 5)",
    ]), right=dict(title="Served together (today's notebook)", bullets=[
        "FastAPI also serves index.html", "React calls /api/... on the same origin", "No CORS needed",
        "Works in Colab with one port",
    ])),
    dict(type="cards", title="SmartDesk step 10: full-stack tickets", items=[
        ("Create", "A form posts a new ticket; it appears after the 201 reply."),
        ("Update", "Change priority with PATCH; the list updates from the reply."),
        ("Close", "A Close button sets status to closed; closed tickets can be hidden."),
        ("Build with Codex", "Use Day11_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="callout", title="Hands-on time", text="Connect the SmartDesk React dashboard to the FastAPI ticket API: "
         "load, create, update and close tickets, with loading, error and empty states.",
         sub="Open your browser's DevTools Network tab and watch every request. Check that no key ever appears.",
         greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Conditional UI", "&&, ternary, early returns. One clear screen per state."),
        ("Lists", "map to JSX with stable keys from your data."),
        ("Keys stay server-side", "Anything in the browser is public. Call your own API."),
        ("Full stack", "React calls FastAPI; CORS when origins differ."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day11_Hotel_Lab.md: notebook, problems, screenshots."),
        ("Workbook", "Complete the Day 11 workbook."),
        ("Pre-read", "Skim the Day 12 pre-read: how AI writes. GenAI starts tomorrow."),
    ]),
]

PREREAD = dict(title="Showing the Right Thing",
               lede="A light read before Day 11. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "On Day 10 you built screens from components. Today those screens come alive with real data from your own API. "
        "You will also learn to show the right thing at the right moment, and one rule that protects every app that "
        "uses AI: secret keys never go to the browser."]),
    dict(h="1. Screens change with the situation", paras=[
        "A food delivery app shows a \"Log in\" button when you are logged out and your name when you are logged in. It "
        "shows \"Your cart is empty\" when there is nothing in it. Choosing what to show based on the data is called "
        "**conditional rendering**."]),
    dict(h="2. One template, many items", paras=[
        "A shop with 500 products does not design 500 cards. It designs one card and repeats it for each product. Each "
        "item needs a unique label, called a **key**, so React can keep track of which card is which, like roll numbers "
        "in a class."]),
    dict(h="3. Waiting politely", table=[
        ["Situation", "What a good app shows"],
        ["Data is on its way", "A loading message or spinner"],
        ["Something went wrong", "A clear error and a way to try again"],
        ["Nothing to show yet", "A friendly empty message with a next step"],
        ["Data has arrived", "The actual content"],
    ], box="**Key idea:** every screen has at least four states. Great apps design all four, not just the happy one."),
    dict(h="4. Keys belong in the safe, not on the shop window", new=True, paras=[
        "Many services, including AI services, give you a secret **API key**. Whoever has the key can use the service "
        "and you pay the bill. Everything sent to a browser can be read by the person using it, so a key placed in "
        "front-end code is like taping the safe's key to the shop window. The key stays on your server; the browser "
        "asks your server, and your server asks the service."]),
    dict(h="5. Two halves of one app", paras=[
        "The React screen runs in the user's browser. The FastAPI back end runs on a server. They talk by sending JSON "
        "over HTTP. Browsers are careful about which websites may talk to which servers; the server must say \"yes, "
        "this website may call me\". That permission is called **CORS**."]),
    dict(h="6. Think about these before class", bullets=[
        "Find an app screen that shows a loading state. Was it helpful or annoying?",
        "What should a support dashboard show when there are no tickets?",
        "If you could open any website's code in your browser, what should you never find there?"],
        after=["Omotenashi (おもてなし): wholehearted hospitality, anticipating what the guest needs"]),
])

POSTREAD = dict(title="React and APIs: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["&&", "Render something or nothing. Beware of 0: use count > 0 &&."],
        ["Ternary and early return", "cond ? A : B to choose; if (loading) return ... keeps the main view simple."],
        ["Lists", "items.map(i => <Item key={i.id} />). Keys must be stable and unique."],
        ["Derived data", "Filter and sort while rendering; do not store computed copies in state."],
        ["useEffect", "Runs after render. [] means once on mount. Use it to start fetching."],
        ["Fetch states", "loading, error, empty and data. Design a screen for each."],
        ["Keys off the front end (NEW v4)", "Anything in the bundle is public. VITE_ variables are inlined. Call your own API."],
        ["POST and PATCH from React", "fetch with method, JSON headers and body; update state with the reply."],
        ["CORS", "Needed when front end and API have different origins (ports count)."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Cleaning up effects", code='''useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal }).then(...);
  return () => controller.abort();   // runs if the component disappears
}, [url]);'''),
    dict(sub="2. A tiny custom hook", code='''function useFetch(url) {
  const [state, setState] = useState({ loading: true, data: null, error: null });
  useEffect(() => { ... }, [url]);
  return state;
}''', paras=["Custom hooks package reusable logic, much like FastAPI dependencies."]),
    dict(sub="3. Optimistic updates", paras=[
        "Update the screen immediately when the agent closes a ticket, then call the API. If the call fails, undo the "
        "change and show an error. Apps feel much faster this way."]),
    dict(sub="4. Secret scanning", paras=[
        "Tools can scan your repository and build output for secrets on every commit. You will add secret scanning to "
        "the CI pipeline on Day 20. If a key ever leaks, revoke it first, then fix the code."]),
    dict(sub="5. Backend for front end (BFF)", paras=[
        "A small server made just for one front end. It holds secrets, combines calls to several services and returns "
        "exactly what the screen needs. Your FastAPI app plays this role for SmartDesk."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why can {count && <p>Items</p>} show a stray 0?",
        "What problem do keys solve?",
        "Name the four states every data screen should handle.",
        "Why is a VITE_ environment variable not a safe place for an API key?",
        "Why does a React app on port 5173 need CORS to call FastAPI on port 8000?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add a Retry button to the error state of your ticket list.",
        "Run npm run build on your React app and search dist/ for anything that looks like a key.",
        "Add an edit mode: double click a ticket title to edit it, then PATCH it."],
        after=["**Coming up on Day 12:** the first GenAI day: how LLMs generate text, the 2026 model landscape, tokens "
               "and cost, and your first LLM API call, made safely from the server.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems building the SmartDesk full stack. In Colab, use show_react() and the served app "
                    "from the notebook.", problems=[
    dict(title="Login Banner", level="Warm-up", concepts="ternary, &&",
         text="Build a component with a loggedIn state and a toggle button. Show \"Welcome back, Mei\" or \"Please log "
              "in\", and show a badge with the open ticket count only when it is above 0.",
         sample="Welcome back, Mei [3 open]\n... toggle ...\nPlease log in",
         hints=["{open > 0 && ...}"]),
    dict(title="Ticket List", level="Easy", concepts="map, keys",
         text="Render an array of 6 tickets as cards, sorted by priority (high first). Closed tickets show "
              "\"Closed\" and a greyed style.",
         sample="T-101 No signal at home (high)\nT-104 Slow 5G data (medium)\nT-103 Change plan (Closed)",
         hints=["Sort a copy: [...tickets].sort(...)"]),
    dict(title="Search and Filter", level="Medium", concepts="controlled input, derived list",
         text="Add a search box and a \"Hide closed\" checkbox to the ticket list. Show \"No tickets match\" when the "
              "filtered list is empty.",
         sample="Search: \"sim\" -> SIM not activated\nNo tickets match",
         hints=["Derive visible tickets during render; no extra state."]),
    dict(title="Four States", level="Medium", concepts="useEffect, loading, error, empty",
         text="Create a fake API function that resolves after 1 second, randomly fails 30 percent of the time, and "
              "sometimes returns an empty list. Show a loading, error (with Retry), empty and data view.",
         sample="Loading tickets...\nCould not load tickets [Retry]\nNo tickets yet\n3 tickets loaded",
         hints=["Retry can increment a counter used in the useEffect dependency array."]),
    dict(title="Find the Leaked Key", level="Medium", concepts="build output, secret scanning", new=True,
         text="Use the notebook's simulated Vite build: put a fake key in a VITE_ variable, build, and write "
              "scan_for_secrets(folder) that reports every file and line that looks like a key. Then move the call "
              "behind a FastAPI endpoint and show that the new bundle is clean.",
         sample="Before: dist/assets/app.js:3 looks like an API key\nAfter: no secrets found in dist/",
         hints=["Search for key prefixes, \"Bearer \" and VITE_ names ending in KEY or SECRET.",
                "Build fake keys at runtime (\"sk-\" + \"demo\" * 6) so no key-like text is saved in your files."]),
    dict(title="SmartDesk Tickets API", level="Challenging", concepts="FastAPI CRUD, CORS",
         text="Build GET, POST and PATCH /api/tickets in FastAPI with Pydantic models (status open, pending or "
              "closed; priority low, medium or high) and CORS for http://localhost:5173. Test with TestClient.",
         sample="POST /api/tickets {\"title\": \"No signal\"} -> 201\nPATCH /api/tickets/1 {\"status\": \"closed\"} -> 200\n"
                "PATCH /api/tickets/1 {\"status\": \"done\"} -> 422",
         hints=["Use Literal[\"open\", \"pending\", \"closed\"] for the status field."]),
    dict(title="Connect React to FastAPI", level="Stretch", concepts="fetch GET, POST, PATCH; optimistic UI",
         text="Load tickets from the API on mount, create new tickets with POST, change priority and close tickets "
              "with PATCH. Make Close optimistic: update the screen first, then roll back with an error message if "
              "the request fails.",
         sample="Close -> ticket greyed instantly -> API fails -> ticket restored + \"Could not save\"",
         hints=["Keep the previous list in a variable before changing state."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "Showing different UI based on data is called ________ rendering.",
        "The expression {ok ? <A /> : <B />} uses the ________ operator.",
        "To render an array of items, use the array method ________.",
        "Each item in a rendered list needs a unique ________ prop.",
        "The hook used to load data after a component appears is ________.",
        "Before reading JSON, check that res.________ is true.",
        "Every data screen should handle loading, error, empty and ________ states.",
        "Vite replaces VITE_ variables with their ________ at build time, so they are public.",
        "A provider API key should live only on the ________.",
        "A browser on port 5173 calling an API on port 8000 needs ________ to be enabled.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Describe the four states of a data screen with a SmartDesk example.",
        "Why should keys come from data ids rather than the array index?",
        "Explain why an API key in front-end code is always public, and describe the safe pattern.",
        "Explain step by step what happens when an agent clicks Close on a ticket.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what appears on screen or in the bundle.", items=[
        "const n = 0;\n// <div>{n && <p>Items</p>}</div>  what appears?",
        'const xs = [3, 1, 2];\n// <p>{[...xs].sort().join("-")}</p>  and what is xs after?',
        'function V({ loading, items }) {\n  if (loading) return <p>Wait</p>;\n  return <p>{items.length || "Empty"}</p>;\n}\n// <V loading={false} items={[]} />',
        '// .env:  VITE_API_URL=https://api.smartdesk.example\n// App.jsx: fetch(import.meta.env.VITE_API_URL + "/tickets")\n// After npm run build, what text appears in dist/assets/*.js?',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write JSX that shows \"Admin\" only when isAdmin is true."),
        dict(q="Write a useEffect that fetches /api/tickets once and stores the result, with loading and error state."),
        dict(q="Write a FastAPI endpoint POST /api/tickets/{id}/suggest that reads the provider key from the "
               "environment on the server and returns only the suggestion."),
        dict(q="Write the FastAPI CORS setup for http://localhost:5173."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

SHOW_REACT = '''# Renders a small React app inside the notebook output (works in Colab and VS Code notebooks).
# It loads React from a CDN, so the rendered output needs internet. The Python cell itself runs anywhere.
import html
from IPython.display import HTML, display

REACT_CDN = """<script src="https://unpkg.com/react@18.3.1/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone@7.24.7/babel.min.js"></script>"""

def show_react(app_code, height=320):
    page = f"""<!doctype html><html><head>{REACT_CDN}
<style>
  body {{ font-family: system-ui, sans-serif; margin: 16px; color: #0E3B43; }}
  .card {{ background: #E3F6F5; border-radius: 10px; padding: 12px 16px; margin: 8px 0; }}
  .closed {{ opacity: 0.5; }}
  button {{ background: #0FA3A3; color: white; border: 0; border-radius: 6px; padding: 8px 14px; cursor: pointer; margin-right: 6px; }}
  input {{ padding: 8px; border: 1px solid #9ED9D4; border-radius: 6px; margin-right: 6px; }}
</style></head><body><div id="root"></div>{app_code}</body></html>"""
    display(HTML(f'<iframe srcdoc="{html.escape(page, quote=True)}" style="width:100%;height:{height}px;border:1px solid #9ED9D4;border-radius:8px"></iframe>'))

print("show_react() is ready")'''

NOTEBOOK = dict(subtitle="Conditional rendering, lists and keys, loading data safely, keeping keys off the front end, "
                         "and React with FastAPI", cells=[
    ("md", "## 1. Setup"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!pip install -q fastapi uvicorn httpx

# ===== Option B: VS Code / local =====
# pip install fastapi uvicorn httpx   (in your activated venv)
# For the separate React project: npm create vite@latest smartdesk-web -- --template react
print("Ready")'''),
    ("code", SHOW_REACT),
    ("md", "## 2. Conditional rendering and lists (Session 1)"),
    ("code", '''show_react("""
<script type="text/babel">
const { useState } = React;

const tickets = [
  { id: 1, title: "No signal at home", priority: "high", status: "open" },
  { id: 2, title: "Change plan", priority: "low", status: "closed" },
  { id: 3, title: "Slow 5G data", priority: "medium", status: "open" },
  { id: 4, title: "Double charge", priority: "high", status: "pending" },
];
const rank = { high: 0, medium: 1, low: 2 };

function App() {
  const [loggedIn, setLoggedIn] = useState(true);
  const open = tickets.filter(t => t.status !== "closed").length;
  const sorted = [...tickets].sort((a, b) => rank[a.priority] - rank[b.priority]);
  return (
    <div>
      <p>
        {loggedIn ? "Welcome back, Mei" : "Please log in"}{" "}
        {loggedIn && open > 0 && <b>[{open} open]</b>}
      </p>
      <button onClick={() => setLoggedIn(!loggedIn)}>{loggedIn ? "Log out" : "Log in"}</button>
      {sorted.map(t => (
        <div key={t.id} className={t.status === "closed" ? "card closed" : "card"}>
          T-{100 + t.id} {t.title} ({t.priority}) {t.status === "closed" && <em>Closed</em>}
        </div>
      ))}
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<App />);
</script>
""", height=330)'''),
    ("md", "## 3. The four states with a fake API (Session 2)\nThe fake API waits 1 second, fails 30% of the time and "
           "sometimes returns nothing. Click Retry a few times to see every state."),
    ("code", '''show_react("""
<script type="text/babel">
const { useState, useEffect } = React;

function fakeApi() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const r = Math.random();
      if (r < 0.3) reject(new Error("Server unavailable"));
      else if (r < 0.5) resolve([]);
      else resolve([{ id: 1, title: "No signal at home" }, { id: 2, title: "Double charge" }]);
    }, 1000);
  });
}

function Tickets() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [attempt, setAttempt] = useState(0);

  useEffect(() => {
    setLoading(true);
    setError(null);
    fakeApi()
      .then(setTickets)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, [attempt]);

  const retry = <button onClick={() => setAttempt(a => a + 1)}>Retry</button>;
  if (loading) return <p>Loading tickets...</p>;
  if (error) return <div className="card">Could not load tickets: {error} {retry}</div>;
  if (tickets.length === 0) return <div className="card">No tickets yet. {retry}</div>;
  return (
    <div>
      {tickets.map(t => <div key={t.id} className="card">{t.title}</div>)}
      {retry}
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<Tickets />);
</script>
""", height=220)'''),
    ("md", "## 4. NEW (v4): Never ship API keys in front-end code\nVite replaces every `import.meta.env.VITE_...` "
           "with its value when you run `npm run build`. The result is plain text in a JavaScript file that every user "
           "downloads. The cells below **simulate** that build step in Python so you can see it happen, then scan the "
           "output for secrets. The fake key is built at runtime and is not a real key."),
    ("code", r'''import os, re, pathlib

FAKE_KEY = "sk-" + "demo" * 6            # not a real key; built at runtime so no key-like text is saved in files
pathlib.Path("web/src").mkdir(parents=True, exist_ok=True)
pathlib.Path("web/.env").write_text(f"VITE_API_URL=http://127.0.0.1:8000\nVITE_OPENAI_KEY={FAKE_KEY}\n")
pathlib.Path("web/src/unsafe_assist.js").write_text("""export async function suggestReply(ticket) {
  const res = await fetch("https://llm.provider.example/v1/chat", {
    headers: { Authorization: "Bearer " + import.meta.env.VITE_OPENAI_KEY },
    method: "POST", body: JSON.stringify({ prompt: ticket.title }),
  });
  return res.json();
}
""")

def fake_vite_build(src_dir, env_file, out_dir):
    """Imitates what a bundler does with VITE_ variables: it pastes their values into the output."""
    env = dict(line.split("=", 1) for line in pathlib.Path(env_file).read_text().split() if "=" in line)
    out = pathlib.Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    for f in pathlib.Path(src_dir).glob("*.js"):
        code = re.sub(r"import\.meta\.env\.(VITE_\w+)", lambda m: repr(env.get(m.group(1), "")), f.read_text())
        (out / f.name).write_text(code)
    return sorted(p.name for p in out.iterdir())

print("Built:", fake_vite_build("web/src", "web/.env", "web/dist/assets"))
print(pathlib.Path("web/dist/assets/unsafe_assist.js").read_text())'''),
    ("code", r'''SECRET_PATTERNS = {
    "API key prefix": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}"),
    "Bearer token in code": re.compile(r"Bearer\s+['\"]?[A-Za-z0-9._-]{16,}"),
    "Secret-looking env name": re.compile(r"VITE_\w*(KEY|SECRET|TOKEN)\b"),
}

def scan_for_secrets(folder):
    hits = []
    for path in pathlib.Path(folder).rglob("*"):
        if path.is_file():
            for n, line in enumerate(path.read_text(errors="ignore").splitlines(), 1):
                for name, rx in SECRET_PATTERNS.items():
                    if rx.search(line):
                        hits.append(f"{path}:{n}: {name}")
    return hits or [f"no secrets found in {folder}"]

for hit in scan_for_secrets("web/dist"):
    print(hit)'''),
    ("md", "### The safe pattern: the key stays on the server\nReact calls **your** API. FastAPI reads the key from "
           "its own environment, calls the provider, and returns only the answer. Here the provider call is an "
           "offline stand-in, so no key is needed to run it."),
    ("code", r'''%%writefile assist_api.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk assist (safe pattern)")

class SuggestIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)

def call_llm(prompt: str) -> str:
    key = os.getenv("OPENAI_API_KEY")           # read on the server, never sent to the browser
    if not key or os.getenv("OFFLINE") == "1":
        return f"[offline demo] Suggested reply for: {prompt}"
    from openai import OpenAI                    # real call (Day 12 covers this properly)
    client = OpenAI(api_key=key)
    r = client.chat.completions.create(model=os.getenv("LLM_MODEL", "gpt-6.1-sol"),
                                       messages=[{"role": "user", "content": prompt}])
    return r.choices[0].message.content

@app.post("/api/tickets/{tid}/suggest")
def suggest(tid: int, body: SuggestIn):
    try:
        return {"ticket": tid, "suggestion": call_llm(f"Draft a short, polite reply about: {body.title}")}
    except Exception:
        raise HTTPException(503, "Assistant unavailable, please try again")'''),
    ("code", r'''import importlib, assist_api
importlib.reload(assist_api)
from fastapi.testclient import TestClient

os.environ["OPENAI_API_KEY"] = FAKE_KEY        # pretend the server has a key
os.environ["OFFLINE"] = "1"                    # but stay offline in this demo
api = TestClient(assist_api.app)
r = api.post("/api/tickets/7/suggest", json={"title": "Slow 5G data"})
print(r.status_code, r.json())
print("Key in response?", FAKE_KEY in r.text)
del os.environ["OPENAI_API_KEY"]

# The safe front-end code only knows your own API's address
pathlib.Path("web/src/unsafe_assist.js").unlink()
pathlib.Path("web/.env").write_text("VITE_API_URL=http://127.0.0.1:8000\n")
pathlib.Path("web/src/assist.js").write_text("""export async function suggestReply(ticket) {
  const res = await fetch(import.meta.env.VITE_API_URL + `/api/tickets/${ticket.id}/suggest`, {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: ticket.title }),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}
""")
import shutil; shutil.rmtree("web/dist")
print("Rebuilt:", fake_vite_build("web/src", "web/.env", "web/dist/assets"))
for hit in scan_for_secrets("web/dist"):
    print(hit)'''),
    ("md", "**TODO:** run `npm run build` on a real Vite project (VS Code) and run `scan_for_secrets(\"dist\")` on it."),
    ("md", "## 5. SmartDesk step 10: full stack tickets (Session 3)\nFastAPI serves both the API (`/api/tickets`) and "
           "the React page (`/`). Because they share one origin, no CORS is needed here; CORS is still added for the "
           "separate Vite setup."),
    ("code", '''%%writefile index.html
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>SmartDesk</title>
  <script src="https://unpkg.com/react@18.3.1/umd/react.development.js"></script>
  <script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js"></script>
  <script src="https://unpkg.com/@babel/standalone@7.24.7/babel.min.js"></script>
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; color: #0E3B43; max-width: 680px; }
    .card { background: #E3F6F5; border-radius: 10px; padding: 10px 14px; margin: 8px 0; display: flex; gap: 8px; align-items: center; }
    .closed { opacity: 0.5; text-decoration: line-through; }
    button { background: #0FA3A3; color: #fff; border: 0; border-radius: 6px; padding: 6px 12px; cursor: pointer; }
    button.close { background: #FF8A3D; margin-left: auto; }
    input, select { padding: 8px; border: 1px solid #9ED9D4; border-radius: 6px; }
  </style>
</head>
<body>
<div id="root"></div>
<script type="text/babel">
const { useState, useEffect } = React;
const API = "";   // same origin. With Vite on port 5173, use import.meta.env.VITE_API_URL instead

async function api(method, path, body) {
  const r = await fetch(API + path, { method, headers: { "Content-Type": "application/json" },
                                      body: body ? JSON.stringify(body) : undefined });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}

function SmartDesk() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [title, setTitle] = useState("");
  const [saving, setSaving] = useState(false);
  const [hideClosed, setHideClosed] = useState(false);

  useEffect(() => {
    api("GET", "/api/tickets").then(setTickets).catch(e => setError(e.message)).finally(() => setLoading(false));
  }, []);

  async function create(e) {
    e.preventDefault();
    if (!title.trim()) return;
    setSaving(true);
    try { const t = await api("POST", "/api/tickets", { title }); setTickets(prev => [...prev, t]); setTitle(""); }
    catch (err) { setError(err.message); }
    setSaving(false);
  }

  async function update(t, changes) {
    const updated = await api("PATCH", `/api/tickets/${t.id}`, changes);
    setTickets(prev => prev.map(x => x.id === t.id ? updated : x));
  }

  if (loading) return <p>Loading tickets...</p>;
  if (error) return <p>Could not load tickets: {error}</p>;
  const visible = tickets.filter(t => !hideClosed || t.status !== "closed");

  return (
    <div>
      <h1>SmartDesk</h1>
      <form onSubmit={create}>
        <input value={title} onChange={e => setTitle(e.target.value)} placeholder="New ticket title" />{" "}
        <button disabled={saving}>{saving ? "Saving..." : "Create"}</button>
      </form>
      <p><label><input type="checkbox" checked={hideClosed} onChange={e => setHideClosed(e.target.checked)} /> Hide closed</label></p>
      {visible.length === 0 && <p>No tickets to show.</p>}
      {visible.map(t => (
        <div key={t.id} className="card">
          <span className={t.status === "closed" ? "closed" : ""}>T-{t.id} {t.title}</span>
          <select value={t.priority} onChange={e => update(t, { priority: e.target.value })}>
            <option>low</option><option>medium</option><option>high</option>
          </select>
          {t.status !== "closed" && <button className="close" onClick={() => update(t, { status: "closed" })}>Close</button>}
        </div>
      ))}
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<SmartDesk />);
</script>
</body>
</html>'''),
    ("code", '''%%writefile fullstack.py
from pathlib import Path
from typing import Literal
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="SmartDesk API")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
                   allow_methods=["*"], allow_headers=["*"])

Priority = Literal["low", "medium", "high"]
Status = Literal["open", "pending", "closed"]

class TicketIn(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    priority: Priority = "medium"

class TicketPatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    priority: Priority | None = None
    status: Status | None = None

class Ticket(BaseModel):
    id: int
    title: str
    priority: Priority = "medium"
    status: Status = "open"

tickets: dict[int, Ticket] = {
    1: Ticket(id=1, title="No signal at home", priority="high"),
    2: Ticket(id=2, title="Double charge on November bill", priority="high"),
    3: Ticket(id=3, title="Change to family plan", priority="low", status="closed"),
}

@app.get("/", response_class=HTMLResponse)
def page():
    return Path("index.html").read_text()

@app.get("/api/tickets", response_model=list[Ticket])
def list_tickets():
    return list(tickets.values())

@app.post("/api/tickets", response_model=Ticket, status_code=201)
def create(data: TicketIn):
    new_id = max(tickets, default=0) + 1
    tickets[new_id] = Ticket(id=new_id, **data.model_dump())
    return tickets[new_id]

@app.patch("/api/tickets/{tid}", response_model=Ticket)
def patch(tid: int, data: TicketPatch):
    if tid not in tickets:
        raise HTTPException(404, "Ticket not found")
    tickets[tid] = tickets[tid].model_copy(update=data.model_dump(exclude_unset=True))
    return tickets[tid]'''),
    ("md", "### Test the API first"),
    ("code", '''import importlib, fullstack
importlib.reload(fullstack)
from fastapi.testclient import TestClient
c = TestClient(fullstack.app)

print([t["title"] for t in c.get("/api/tickets").json()])
print("Create:", c.post("/api/tickets", json={"title": "SIM not activated", "priority": "high"}).status_code)
print("Close:", c.patch("/api/tickets/1", json={"status": "closed"}).json())
print("Bad status:", c.patch("/api/tickets/1", json={"status": "done"}).status_code)
print("Missing:", c.patch("/api/tickets/99", json={"status": "closed"}).status_code)
print("Empty title:", c.post("/api/tickets", json={"title": ""}).status_code)
print("Page served:", "text/babel" in c.get("/").text)
r = c.options("/api/tickets", headers={"Origin": "http://localhost:5173", "Access-Control-Request-Method": "PATCH"})
print("CORS allowed origin:", r.headers.get("access-control-allow-origin"))'''),
    ("md", "### Run the full stack app\n**Colab:** the cell below starts the server and opens the app inside the "
           "notebook.\n\n**VS Code:** run `uvicorn fullstack:app --reload` in the terminal and open "
           "http://127.0.0.1:8000 in your browser."),
    ("code", '''# ===== Option A: Google Colab (active) =====
import subprocess, time
server = subprocess.Popen(["uvicorn", "fullstack:app", "--port", "8000"])
time.sleep(3)
from google.colab import output
output.serve_kernel_port_as_iframe(8000, height=500)

# ===== Option B: VS Code =====
# Terminal: uvicorn fullstack:app --reload
# Browser:  http://127.0.0.1:8000''', ["skip-offline-check"]),
    ("md", "### TODO 1: Add a `DELETE /api/tickets?status=closed` endpoint that removes closed tickets and returns "
           "the count, and a \"Clear closed\" button in the page."),
    ("code", "# TODO: write your code here"),
    ("md", "## 6. The separate Vite version (VS Code)\nIn a real project, React lives in its own Vite app. Copy the "
           "`SmartDesk` component into `src/App.jsx`, add `import { useState, useEffect } from \"react\";`, set "
           "`const API = import.meta.env.VITE_API_URL;` (only the API address, never a key), and export it with "
           "`export default SmartDesk;`. Run `npm run dev` and `uvicorn fullstack:app --reload` side by side. CORS is "
           "already configured for port 5173."),
    ("md", "## 7. Check yourself\n1. Which patterns did the scanner flag in the unsafe build, and why was the "
           "rebuilt bundle clean?\n2. Why does the page update from the PATCH reply instead of changing state "
           "first?\n3. What status code did the API return for `{\"status\": \"done\"}`, and which line caused it?"),
])
