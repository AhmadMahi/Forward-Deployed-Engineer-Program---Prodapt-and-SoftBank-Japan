"""Day 10 spec. React Basics (assessment day).
Source: REUSE archive/v1-40-day/Day11 (React basics), plus a Codex build session for the SmartDesk dashboard.
"""
DAY = 10
FOLDER = "Day10-React-Basics"
SLUG = "React_Basics"
TITLE = "React Basics"
SUBTITLE = "Single page apps, JSX, components, props, state and events, and the SmartDesk dashboard built with Codex"
DATE = "Fri 06 Nov 2026"
TRACK = "Basics"
NEXT = "Monday 9 Nov is the Deepavali holiday. See you on Tuesday for Day 11: React UI logic and full stack."
CLOSING_GREET = "Yoi shuumatsu wo (良い週末を): Have a great weekend, and Happy Deepavali"

REACT = '''<script src="https://unpkg.com/react@18.3.1/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.development.js"></script>
<script src="https://unpkg.com/@babel/standalone@7.24.7/babel.min.js"></script>'''

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 9"),
        ("SPAs and JSX", "Why modern web apps feel instant"),
        ("Components and props", "Reusable building blocks"),
        ("State and events", "Screens that react to users"),
        ("SmartDesk with Codex", "Build the ticket dashboard, review every line"),
        ("Assessment", "Basics assessment 2"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Explain SPAs", "Describe how a single page app differs from classic websites."),
        ("Compose components", "Write JSX, split a screen into components and pass props."),
        ("Handle interaction", "Use useState and event handlers to update the screen."),
        ("Build with Codex", "Generate a React dashboard with Codex and review it line by line."),
    ]),
    dict(type="table", title="Today's sessions", header=["Session", "Duration", "Topics"], rows=[
        ["Opening", "30 min", "Kahoot / recap quiz on Day 9"],
        ["Session 1", "1.5 hrs", "React overview, SPA, components, JSX, props"],
        ["Session 2", "2 hrs", "State vs props, useState, events"],
        ["Session 3", "1.5 hrs", "Building the SmartDesk dashboard with Codex"],
        ["Assessment", "1.5 hrs", "Basics assessment 2 (SQLAlchemy, JavaScript, Node.js, React)"],
    ]),

    dict(type="section", title="React, SPAs and JSX", sub="Session 1 | 1.5 hrs | One page, many screens"),
    dict(type="compare", title="Classic website and SPA", left=dict(title="Classic multi-page", bullets=[
        "Every click loads a whole new page", "Server builds the HTML", "Screen flashes white between pages",
    ]), right=dict(title="Single page app (SPA)", bullets=[
        "Loads once, then updates parts of the page", "Browser builds the UI with JavaScript",
        "Fetches only data (JSON) from APIs", "Feels like a native app",
    ])),
    dict(type="flow", title="How a React SPA works", items=[
        ("Load", "Browser downloads HTML, JS and CSS once"),
        ("Render", "React builds the UI from components"),
        ("Interact", "User clicks; state changes"),
        ("Update", "React re-renders only what changed"),
    ], note="React keeps a virtual copy of the page and patches the real one efficiently."),
    dict(type="bullets_code", title="Your first component", bullets=[
        "A component is a function that returns JSX",
        "Names start with a capital letter",
        "Return one parent element",
        "Curly braces run JavaScript expressions",
    ], code='''function Welcome() {
  const name = "Aiko";
  const today = new Date().toDateString();
  return (
    <div className="card">
      <h1>Hello, {name}!</h1>
      <p>Today is {today}</p>
    </div>
  );
}'''),
    dict(type="table", title="JSX rules that trip people up", header=["HTML habit", "JSX version", "Why"], rows=[
        ['class="box"', 'className="box"', "class is a JS keyword"],
        ['<img src="a.png">', '<img src="a.png" />', "Every tag must close"],
        ['onclick="..."', "onClick={handler}", "camelCase, pass a function"],
        ['style="color: red"', 'style={{ color: "red" }}', "Style is an object"],
        ["Two top-level tags", "Wrap in <>...</>", "One parent per return"],
    ]),
    dict(type="cards", title="Think in components", greet="Tsumiki (積み木): Building blocks", items=[
        ("Split the screen", "Header, list, list item, footer: each is a component."),
        ("Reuse", "Write TicketCard once, show it 100 times."),
        ("Nest", "Components contain other components, like boxes in boxes."),
    ]),
    dict(type="bullets_code", title="Props: passing data down", bullets=[
        "Props are the inputs to a component",
        "Passed like HTML attributes",
        "Read them with destructuring",
        "Props are read-only inside the child",
    ], code='''function TicketCard({ title, priority }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <p>Priority: {priority}</p>
    </div>
  );
}

<TicketCard title="No signal" priority="high" />
<TicketCard title="Change plan" priority="low" />'''),
    dict(type="bullets_code", title="Children and composition", bullets=[
        "children is a special prop",
        "It holds whatever is between the tags",
        "Great for layouts and wrappers",
        "Compose small pieces into screens",
    ], code='''function Panel({ title, children }) {
  return (
    <section className="panel">
      <h2>{title}</h2>
      {children}
    </section>
  );
}

<Panel title="Today">
  <p>Quiz, React basics, assessment</p>
</Panel>'''),

    dict(type="section", title="State and events", sub="Session 2 | 2 hrs | Making the screen respond"),
    dict(type="compare", title="Props and state", left=dict(title="Props", bullets=[
        "Come from the parent", "Read-only for the child", "Like function arguments",
    ]), right=dict(title="State", bullets=[
        "Owned by the component itself", "Changed with a setter function", "A change triggers a re-render",
    ])),
    dict(type="bullets_code", title="useState: a counter", bullets=[
        "useState returns [value, setter]",
        "Call the setter to change the value",
        "React re-renders with the new value",
        "Never change state directly",
    ], code='''import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Clicked {count} times</p>
      <button onClick={() =>
          setCount(c => c + 1)}>
        Click me
      </button>
    </div>
  );
}'''),
    dict(type="bullets_code", title="Controlled inputs", bullets=[
        "The input's value comes from state",
        "onChange updates the state",
        "React is the single source of truth",
        "Easy to validate as the user types",
    ], code='''function NameForm() {
  const [name, setName] = useState("");
  return (
    <div>
      <input value={name}
        onChange={e =>
          setName(e.target.value)} />
      <p>{name ? `Hi, ${name}` : "Type"}</p>
    </div>
  );
}'''),
    dict(type="table", title="Common events", header=["Event", "Fires when", "Typical use"], rows=[
        ["onClick", "An element is clicked", "Buttons, cards"],
        ["onChange", "An input value changes", "Forms, search boxes"],
        ["onSubmit", "A form is submitted", "Login, create ticket"],
        ["onKeyDown", "A key is pressed", "Shortcuts, Enter to add"],
    ], note="In onSubmit, call e.preventDefault() so the page does not reload."),
    dict(type="bullets_code", title="State with objects and arrays: copy, do not mutate", bullets=[
        "React compares old and new values",
        "Mutating in place may not re-render",
        "Spread to copy objects and arrays",
        "filter and map return new arrays",
    ], code='''// Objects
setUser({ ...user, city: "Osaka" });

// Arrays
setTickets([...tickets, newTicket]);
setTickets(tickets.filter(
  t => t.id !== id));

// Not this:
tickets.push(newTicket);   // no re-render'''),
    dict(type="flow", title="Setting up a real React project", items=[
        ("Create", "npm create vite@latest my-app -- --template react"),
        ("Install", "cd my-app, npm install"),
        ("Run", "npm run dev"),
        ("Edit", "src/App.jsx, saves reload instantly"),
    ], note="In Colab we render React directly in the notebook output, no setup needed."),

    dict(type="section", title="SmartDesk dashboard with Codex", sub="Session 3 | 1.5 hrs | Describe, plan, small steps, test"),
    dict(type="flow", title="The structured Codex workflow (from Day 3)", items=[
        ("Describe", "Components, props, state, data"),
        ("Plan", "Ask Codex for a plan first"),
        ("Small steps", "One component per prompt"),
        ("Review", "Read every diff, run it"),
        ("Test", "Click every state on screen"),
    ], note="Codex writes the first draft. You own the code you commit."),
    dict(type="table", title="SmartDesk step 9: the dashboard", header=["Component", "Props", "State"], rows=[
        ["App", "none", "tickets, filter"],
        ["Header", "agentName, openCount", "none"],
        ["FilterBar", "filter, onChange", "none"],
        ["TicketList", "tickets", "none"],
        ["TicketCard", "id, title, priority, status", "none"],
    ], note="State lives in App. Children get data and callbacks as props."),
    dict(type="cards", title="Reviewing React code from Codex", items=[
        ("Keys", "Every list item has a stable key from the data, not the index."),
        ("No mutation", "State changes use the setter and new arrays or objects."),
        ("No secrets", "No API keys or tokens anywhere in front-end code."),
        ("No raw HTML", "No dangerouslySetInnerHTML with user data."),
        ("Small components", "One job each; props named clearly."),
        ("You can explain it", "If you cannot explain a line, ask Codex or remove it."),
    ]),
    dict(type="callout", title="Assessment: Basics assessment 2", text="MCQ and coding on SQLAlchemy, JavaScript, "
         "Node.js and React. 1.5 hours.",
         sub="Read each question carefully. For coding tasks, get a working version first, then improve it. "
             "Codex is not allowed during the assessment.",
         greet="Ganbatte kudasai (頑張ってください): Please do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("SPA", "Load once, update parts of the page with data from APIs."),
        ("JSX and props", "className, closed tags, {expressions}; data flows down."),
        ("State", "useState + setter; copy, do not mutate; changes re-render."),
        ("Codex", "Plan, build in small steps, review every line of the dashboard."),
    ]),
    dict(type="cards", title="Before Tuesday", lead="Monday is the Deepavali holiday. Tuesday starts with a 15 question "
         "quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day10_Hotel_Lab.md: notebook, problems, dashboard screenshot."),
        ("Workbook", "Complete the Day 10 workbook."),
        ("Pre-read", "Skim the Day 11 pre-read on lists, loading data and API keys."),
    ]),
]

PREREAD = dict(title="Building Screens from Blocks",
               lede="A light read before Day 10. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "For two weeks you built the back end: the kitchen of the restaurant. Today you start on the dining room, the "
        "screens people actually see and touch. You will use **React**, the most popular tool for building web app "
        "screens, and you will build the first SmartDesk dashboard with OpenAI Codex."]),
    dict(h="1. Apps that never reload", paras=[
        "Old websites reloaded the whole page every time you clicked, like reprinting a full newspaper to fix one "
        "headline. Modern apps load once and then update only the part that changed. These are called **single page "
        "applications**, or SPAs."]),
    dict(h="2. Screens made of building blocks", paras=[
        "Look at any app screen. It is made of repeated pieces: a header, a search bar, cards, a button. React calls "
        "each piece a **component**. You build a ticket card once and reuse it for every ticket, just like stacking "
        "the same toy block many times."]),
    dict(h="3. Inputs and memory", table=[
        ["Idea", "React name", "Everyday example"],
        ["Information handed to a block", "props", "A name badge printed with your name"],
        ["Information a block remembers", "state", "A scoreboard that changes during a match"],
        ["Something the user does", "event", "Pressing a button or typing"],
    ], paras=["When the user does something (an event), the component updates its memory (state), and React redraws "
              "that part of the screen automatically."],
        box="**Key idea:** you describe what the screen should look like for the current data. React works out how "
            "to update it."),
    dict(h="4. About today's assessment", paras=[
        "Today includes Basics assessment 2, with multiple choice and coding questions on SQLAlchemy, JavaScript, "
        "Node.js and React basics. Re-read your post-reads for Days 6, 8 and 9 and re-run one notebook."]),
    dict(h="5. Think about these before class", bullets=[
        "Open your favourite app and list five components you can see on one screen.",
        "Which parts of that screen change when you tap something, and which stay the same?",
        "If Codex wrote a screen for you, how would you check it is correct and safe?"],
        after=["Tsumiki (積み木): building blocks"]),
])

POSTREAD = dict(title="React Basics: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["SPA", "Loads once, updates parts of the page, fetches JSON from APIs."],
        ["Component", "A function returning JSX. Capitalised name. One parent element."],
        ["JSX", "{expressions}, className, self-closing tags, camelCase events, style objects."],
        ["Props", "Inputs from the parent, read-only. Destructure: function Card({ title })."],
        ["children", "Whatever sits between a component's tags; great for layouts."],
        ["State", "const [value, setValue] = useState(initial). Change only via the setter."],
        ["Copy, do not mutate", "setItems([...items, x]); setUser({ ...user, city })."],
        ["Events", "onClick, onChange, onSubmit (call e.preventDefault())."],
        ["Project setup", "npm create vite@latest app -- --template react, npm install, npm run dev."],
        ["Codex for React", "Plan first, one component per prompt, review keys, state, secrets, raw HTML."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Updating state from the previous value", code='''setCount(c => c + 1);   // safe even when several updates happen quickly'''),
    dict(sub="2. Lifting state up", paras=[
        "When two sibling components need the same data, move the state to their closest common parent and pass it "
        "down as props, along with functions to change it. The SmartDesk FilterBar and TicketList do exactly this."]),
    dict(sub="3. Prop types with TypeScript (preview)", code='''type CardProps = { title: string; priority: "low" | "medium" | "high" };
function TicketCard({ title, priority }: CardProps) { ... }''',
         paras=["Many teams use TypeScript with React to catch wrong props before the app runs."]),
    dict(sub="4. React DevTools", paras=[
        "Install the React Developer Tools browser extension to inspect components, their props and state while the "
        "app runs. It is the fastest way to check what Codex built."]),
    dict(sub="5. Accessibility basics", paras=[
        "Use real buttons for actions, labels for inputs and enough colour contrast. Ask Codex to review a component "
        "for accessibility, then check its suggestions yourself."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why do component names start with a capital letter?",
        "What is the difference between props and state?",
        "Why should you never write count = count + 1 for state?",
        "Why is setItems([...items, x]) better than items.push(x)?",
        "Name three things you check when reviewing React code from Codex."]),
    dict(h="Part D: Practice ideas for the long weekend", bullets=[
        "Build a ProfileCard component and render three cards with different props.",
        "Add a search box to the SmartDesk dashboard that filters tickets by title.",
        "Ask Codex to explain your dashboard's data flow, then correct anything it gets wrong."],
        after=["**Coming up on Day 11:** conditional rendering, lists and keys, loading data with loading, error and "
               "empty states, never shipping API keys in front-end code, and React talking to FastAPI.",
               "Yoi shuumatsu wo (良い週末を): have a great weekend, and Happy Deepavali"]),
])

HANDSON = dict(lede="Seven problems. In Colab, use show_react() from the notebook. In VS Code, use a Vite React "
                    "project and edit src/App.jsx.", problems=[
    dict(title="Hello Component", level="Warm-up", concepts="component, JSX expressions",
         text="Create a Greeting component that shows your name, today's date and a message that says \"Good "
              "morning\" or \"Good evening\" based on the current hour.",
         sample="Hello, Aiko!\nToday is Fri Nov 06 2026\nGood morning",
         hints=["new Date().getHours() < 12"]),
    dict(title="Ticket Cards", level="Easy", concepts="props, reuse",
         text="Create TicketCard with props id, title and priority. Render three cards for three different SmartDesk "
              "tickets. High priority cards show a red border.",
         sample="[T-101 | No signal at home | high]\n[T-102 | Double charge | medium]\n[T-103 | Change plan | low]",
         hints=["style={{ borderLeft: priority === \"high\" ? \"4px solid #C2410C\" : \"none\" }}"]),
    dict(title="Counter with Limits", level="Easy", concepts="useState, onClick",
         text="Build a counter with +1, -1 and Reset buttons. The count must never go below 0 or above 10; disable "
              "buttons at the limits.",
         sample="Count: 10 [+1 disabled] [-1] [Reset]",
         hints=["disabled={count === 10}"]),
    dict(title="Live Converter", level="Medium", concepts="controlled input, derived values",
         text="Build a Celsius input that shows Fahrenheit and Kelvin as you type. Show \"Enter a number\" when the "
              "input is empty or not a number.",
         sample="Celsius: 37\nFahrenheit: 98.6 | Kelvin: 310.15",
         hints=["Number(value) and Number.isNaN()"]),
    dict(title="Layout with children", level="Medium", concepts="children prop, composition",
         text="Create a Panel component with a title prop and children. Build a page with three panels: About, Skills "
              "and Contact, each with different content.",
         sample="Three styled panels, each with a heading and custom content",
         hints=["function Panel({ title, children })"]),
    dict(title="Review the Codex Dashboard", level="Challenging", concepts="code review, keys, state, secrets",
         text="Ask Codex to generate the SmartDesk dashboard (App, Header, FilterBar, TicketList, TicketCard). Review "
              "it with the checklist from the deck: keys, no mutation, no secrets, no raw HTML, small components. "
              "Write a review note with at least two issues you found or confirmed absent, and fix them.",
         sample="Review note\n1. TicketList used the array index as key -> changed to ticket.id\n"
                "2. Filter mutated the tickets array with sort() -> now sorts a copy\n3. No secrets found",
         hints=["Ask Codex: \"List every place this code uses state, and how it changes it.\""]),
    dict(title="Mini Signup Form", level="Stretch", concepts="multiple controlled inputs, onSubmit, validation",
         text="Build a form with name, email and password. Show validation messages as the user types (email must "
              "contain @, password at least 8 characters). On submit, show a welcome message instead of the form.",
         sample="Password must be at least 8 characters\n... after submit: Welcome, Mei!",
         hints=["Use one state object: const [form, setForm] = useState({ name: \"\", email: \"\", password: \"\" })",
                "e.preventDefault() in onSubmit"]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "SPA stands for Single ________ Application.",
        "A React component is a function that returns ________.",
        "Component names must start with a ________ letter.",
        "In JSX, the HTML attribute class is written as ________.",
        "Data passed from a parent to a child component is called ________.",
        "Data a component remembers and can change is called ________.",
        "useState returns an array with the current value and a ________ function.",
        "The event used for button clicks is ________.",
        "To stop a form from reloading the page, call e.________().",
        "Each item in a rendered list needs a stable ________ prop.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain the difference between a classic website and an SPA.",
        "Explain props and state using a SmartDesk example.",
        "Why must you use the setter function instead of changing state directly?",
        "Describe how you reviewed the dashboard Codex generated. What did you check?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what appears on screen.", items=[
        "function A({ n }) { return <p>{n * 2}</p>; }\n// rendered as <A n={21} />",
        'const items = ["a", "b"];\n// <p>{items.length > 1 ? "many" : "one"}</p>',
        "const [c, setC] = useState(5);\n// button onClick={() => setC(c + 2)} clicked twice\n// what does {c} show?",
        'const tickets = [{ id: 1, priority: "high" }, { id: 2, priority: "low" }];\n// <p>{tickets.filter(t => t.priority === "high").length} urgent</p>',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write a Badge component that shows a label prop in a span."),
        dict(q="Write a component with a button that toggles between \"Show\" and \"Hide\"."),
        dict(q="Write a controlled input that shows the typed text in uppercase below it."),
        dict(q="Write a FilterBar component that receives filter and onChange props and renders All, Open and Closed "
               "buttons."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

SHOW_REACT = '''# Renders a small React app inside the notebook output (works in Colab and VS Code notebooks).
# It loads React from a CDN, so the rendered output needs internet. The Python cell itself runs anywhere.
import html
from IPython.display import HTML, display

def show_react(app_code, height=320):
    page = f"""<!doctype html><html><head>
''' + REACT + '''
<style>
  body {{ font-family: system-ui, sans-serif; margin: 16px; color: #0E3B43; }}
  .card {{ background: #E3F6F5; border-radius: 10px; padding: 12px 16px; margin: 8px 0; }}
  .high {{ border-left: 4px solid #C2410C; }}
  button {{ background: #0FA3A3; color: white; border: 0; border-radius: 6px; padding: 8px 14px; cursor: pointer; margin-right: 6px; }}
  button.active {{ background: #FF8A3D; }}
  button:disabled {{ opacity: 0.4; cursor: default; }}
  input {{ padding: 8px; border: 1px solid #9ED9D4; border-radius: 6px; margin-right: 6px; }}
</style></head><body><div id="root"></div>{app_code}</body></html>"""
    display(HTML(f'<iframe srcdoc="{html.escape(page, quote=True)}" style="width:100%;height:{height}px;border:1px solid #9ED9D4;border-radius:8px"></iframe>'))

print("show_react() is ready")'''

NOTEBOOK = dict(subtitle="Single page apps, JSX, components, props, state and events, and the SmartDesk dashboard",
                cells=[
    ("md", "## 1. Setup\nReact runs in the browser. In this notebook, `show_react()` renders a small React app right in "
           "the cell output.\n\n**VS Code (real project):** install Node.js LTS, then:\n```\n"
           "npm create vite@latest my-app -- --template react\ncd my-app\nnpm install\nnpm run dev\n```\n"
           "Paste the code inside each `<script type=\"text/babel\">` into `src/App.jsx` (replace "
           "`const { useState } = React;` with `import { useState } from \"react\";` and export your component with "
           "`export default App;`)."),
    ("code", SHOW_REACT),
    ("md", "## 2. Your first component and JSX (Session 1)"),
    ("code", '''show_react("""
<script type="text/babel">
function Welcome() {
  const name = "Aiko";
  const hour = new Date().getHours();
  return (
    <div className="card">
      <h1>Hello, {name}!</h1>
      <p>Today is {new Date().toDateString()}</p>
      <p>{hour < 12 ? "Good morning" : "Good evening"}</p>
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<Welcome />);
</script>
""", height=200)'''),
    ("md", "## 3. Props and composition"),
    ("code", '''show_react("""
<script type="text/babel">
function TicketCard({ id, title, priority }) {
  return (
    <div className={priority === "high" ? "card high" : "card"}>
      <b>{id}</b> {title} <small>({priority})</small>
    </div>
  );
}

function Panel({ title, children }) {
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}

function App() {
  return (
    <Panel title="Today's tickets">
      <TicketCard id="T-101" title="No signal at home" priority="high" />
      <TicketCard id="T-102" title="Double charge" priority="medium" />
      <TicketCard id="T-103" title="Change plan" priority="low" />
    </Panel>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<App />);
</script>
""", height=300)'''),
    ("md", "### TODO 1: Add a `ProfileCard` with name, role and city props and render three of them."),
    ("code", "# TODO: write your code here using show_react"),
    ("md", "## 4. State and events: counter with limits (Session 2)"),
    ("code", '''show_react("""
<script type="text/babel">
const { useState } = React;

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div className="card">
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(c => c + 1)} disabled={count === 10}>+1</button>
      <button onClick={() => setCount(c => c - 1)} disabled={count === 0}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
      {count === 10 && <p>Maximum reached</p>}
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
</script>
""", height=200)'''),
    ("md", "## 5. Controlled inputs: live converter"),
    ("code", '''show_react("""
<script type="text/babel">
const { useState } = React;

function Converter() {
  const [celsius, setCelsius] = useState("");
  const c = Number(celsius);
  const valid = celsius !== "" && !Number.isNaN(c);
  return (
    <div className="card">
      <label>Celsius: </label>
      <input value={celsius} onChange={e => setCelsius(e.target.value)} placeholder="e.g. 37" />
      <p>
        {valid
          ? `Fahrenheit: ${(c * 9 / 5 + 32).toFixed(1)} | Kelvin: ${(c + 273.15).toFixed(2)}`
          : "Enter a number"}
      </p>
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<Converter />);
</script>
""", height=170)'''),
    ("md", "## 6. Forms: signup with validation"),
    ("code", '''show_react("""
<script type="text/babel">
const { useState } = React;

function Signup() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [done, setDone] = useState(false);
  const update = e => setForm({ ...form, [e.target.name]: e.target.value });

  const errors = [];
  if (form.email && !form.email.includes("@")) errors.push("Email must contain @");
  if (form.password && form.password.length < 8) errors.push("Password must be at least 8 characters");
  const canSubmit = form.name && form.email && form.password && errors.length === 0;

  const submit = e => {
    e.preventDefault();
    setDone(true);
  };

  if (done) return <div className="card"><h2>Welcome, {form.name}!</h2></div>;
  return (
    <form onSubmit={submit} className="card">
      <input name="name" placeholder="Name" value={form.name} onChange={update} />
      <input name="email" placeholder="Email" value={form.email} onChange={update} />
      <input name="password" type="password" placeholder="Password" value={form.password} onChange={update} />
      <button type="submit" disabled={!canSubmit}>Sign up</button>
      {errors.map(err => <p key={err} style={{ color: "#C2410C" }}>{err}</p>)}
    </form>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<Signup />);
</script>
""", height=220)'''),
    ("md", "### TODO 2: Build a like button that toggles its label and keeps a total likes count."),
    ("code", "# TODO: write your code here using show_react"),
    ("md", "## 7. SmartDesk step 9: the ticket dashboard (Session 3)\nThis is the kind of dashboard you will ask "
           "Codex to build. State lives in `App`; `FilterBar` and `TicketList` receive data and callbacks as props. "
           "There is no data fetching yet: that comes on Day 11."),
    ("code", '''DASHBOARD = """
<script type="text/babel">
const { useState } = React;

const SAMPLE_TICKETS = [
  { id: "T-101", title: "No signal at home", priority: "high", status: "open" },
  { id: "T-102", title: "Double charge", priority: "high", status: "open" },
  { id: "T-103", title: "Change plan", priority: "low", status: "closed" },
  { id: "T-104", title: "Slow 5G data", priority: "medium", status: "open" },
  { id: "T-105", title: "SIM not activated", priority: "medium", status: "closed" },
];

function Header({ agentName, openCount }) {
  return <h2>SmartDesk | {agentName} | {openCount} open</h2>;
}

function FilterBar({ filter, onChange }) {
  return (
    <div>
      {["all", "open", "closed"].map(f => (
        <button key={f} className={f === filter ? "active" : ""} onClick={() => onChange(f)}>{f}</button>
      ))}
    </div>
  );
}

function TicketCard({ id, title, priority, status }) {
  return (
    <div className={priority === "high" ? "card high" : "card"}>
      <b>{id}</b> {title} <small>({priority}, {status})</small>
    </div>
  );
}

function TicketList({ tickets }) {
  if (tickets.length === 0) return <p>No tickets match.</p>;
  return tickets.map(t => <TicketCard key={t.id} {...t} />);
}

function App() {
  const [tickets] = useState(SAMPLE_TICKETS);
  const [filter, setFilter] = useState("all");
  const visible = filter === "all" ? tickets : tickets.filter(t => t.status === filter);
  const openCount = tickets.filter(t => t.status === "open").length;
  return (
    <div>
      <Header agentName="Aiko" openCount={openCount} />
      <FilterBar filter={filter} onChange={setFilter} />
      <TicketList tickets={visible} />
    </div>
  );
}
ReactDOM.createRoot(document.getElementById("root")).render(<App />);
</script>
"""
show_react(DASHBOARD, height=380)'''),
    ("md", "### A quick review helper for Codex-generated React code\nA script cannot replace your review, but it can "
           "flag common problems before you read line by line. It checks for index keys, missing keys on `map`, "
           "mutation of state arrays, raw HTML and anything that looks like a secret."),
    ("code", r'''import re

def review_react(code):
    findings = []
    for n, line in enumerate(code.splitlines(), 1):
        if re.search(r"key=\{\s*(i|index|idx)\s*\}", line):
            findings.append((n, "uses the array index as key; use an id from the data"))
        if ".map(" in line and "<" in line and "key=" not in line and "{...t}" not in line:
            findings.append((n, "map returns JSX without a key"))
        if re.search(r"\b(tickets|items|tasks)\.(push|splice|sort|reverse)\(", line):
            findings.append((n, "mutates a state array in place; copy it first"))
        if "dangerouslySetInnerHTML" in line:
            findings.append((n, "raw HTML: never with user data"))
        if re.search(r"(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]\w{8,}", line, re.I):
            findings.append((n, "looks like a hard-coded secret"))
    return findings or [(0, "no automatic findings: now read every line yourself")]

risky = """
{tickets.map((t, i) => <TicketCard key={i} {...t} />)}
const sorted = tickets.sort((a, b) => a.id - b.id);
const apiKey = "abcd1234efgh5678";
"""
for label, code in [("Dashboard above", DASHBOARD), ("Risky sample", risky)]:
    print(label)
    for n, msg in review_react(code):
        print(f"  line {n}: {msg}")'''),
    ("md", "**TODO (SmartDesk step 9):** ask Codex for the same dashboard as a Vite project (one file per component), "
           "paste its `TicketList.jsx` into `review_react()`, then read every line yourself and write a two-line "
           "review note."),
    ("md", "## 8. The same app as a Vite project file\nThis cell writes `App.jsx` exactly as it would look in "
           "`src/App.jsx` of a Vite project."),
    ("code", '''%%writefile App.jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h2>Count: {count}</h2>
      <button onClick={() => setCount(c => c + 1)}>+1</button>
    </div>
  );
}

export default function App() {
  return (
    <main>
      <h1>My first Vite + React app</h1>
      <Counter />
    </main>
  );
}'''),
    ("md", "## 9. Check yourself\n1. In the dashboard, which values are props and which are state?\n"
           "2. Why does `TicketList` not need its own state?\n3. What did `review_react()` flag in the risky sample, "
           "and how would you fix each finding?"),
], sign_off="Yoi shuumatsu wo (良い週末を): *Have a great weekend, and Happy Deepavali*")
