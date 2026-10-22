"""Day 08 spec. JavaScript Fundamentals and Async JavaScript.
Source: MERGE archive/v1-40-day/Day09 Sessions 3 and 4 (JavaScript basics) + Day10 Session 1 (async JavaScript).
"""
DAY = 8
FOLDER = "Day08-JavaScript-and-Async-JavaScript"
SLUG = "JavaScript_and_Async_JavaScript"
TITLE = "JavaScript and Async JavaScript"
SUBTITLE = "Variables, arrays, objects, functions and callbacks, then promises, async and await, fetch and JSON"
DATE = "Wed 04 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 9: Node.js, npm, Express and Postman."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 7"),
        ("JS fundamentals", "Variables, types, arrays, objects, loops"),
        ("Functions", "Arrow functions and callbacks"),
        ("Async thinking", "Why JavaScript never waits around"),
        ("Promises and await", "Values that arrive later, fetch, JSON"),
        ("SmartDesk", "An async client for the ticket API"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Write JavaScript", "Use const, let, arrays, objects and loops with confidence."),
        ("Use functions", "Write arrow functions and pass callbacks to other functions."),
        ("Explain async", "Describe the event loop and predict the order of output."),
        ("Call an API", "Use promises, async and await, fetch and JSON safely."),
    ]),
    dict(type="table", title="Today's sessions", header=["Session", "Duration", "Topics"], rows=[
        ["Opening", "30 min", "Kahoot / recap quiz on Day 7"],
        ["Session 1", "2 hrs", "Variables, data types, arrays, objects, loops"],
        ["Session 2", "2 hrs", "Functions, arrow functions, callbacks"],
        ["Session 3", "2.5 hrs", "Promises, async and await, fetch, JSON parse and stringify"],
    ], note="Run every example in today's notebook with Node.js (in Colab: !node file.js)."),

    dict(type="section", title="JavaScript fundamentals", sub="Session 1 | 2 hrs | The language every browser speaks"),
    dict(type="compare", title="Python and JavaScript side by side", left=dict(title="Python", bullets=[
        'name = "Mei"', "def add(a, b): return a + b", "items = [1, 2, 3]", 'user = {"name": "Mei"}',
        "if x > 5:  (indentation)",
    ]), right=dict(title="JavaScript", bullets=[
        'const name = "Mei";', "const add = (a, b) => a + b;", "const items = [1, 2, 3];",
        'const user = { name: "Mei" };', "if (x > 5) { ... }  (braces)",
    ]), note="If you know Python, most ideas carry over. The syntax is what changes."),
    dict(type="bullets_code", title="Variables and template literals", bullets=[
        "const for values that do not change",
        "let for values that do",
        "Avoid var in modern code",
        "Template literals use backticks and ${ }",
    ], code='''const city = "Pune";
let count = 3;
count += 1;

const msg = `${city} has ${count} open tickets`;
console.log(msg);
// Pune has 4 open tickets

console.log(typeof count, typeof city);
// number string'''),
    dict(type="table", title="Data types you will meet", header=["Type", "Example", "Note"], rows=[
        ["string", '"hello", `hi ${name}`', "Text; backticks allow ${ }"],
        ["number", "42, 3.14", "One type for whole and decimal numbers"],
        ["boolean", "true, false", "Lower case, unlike Python"],
        ["undefined", "let x;", "Declared but no value yet"],
        ["null", "let y = null;", "Deliberately empty"],
        ["object / array", "{ id: 1 }, [1, 2]", "Collections of values"],
    ]),
    dict(type="bullets_code", title="Arrays and objects", bullets=[
        "map transforms every item",
        "filter keeps matching items",
        "reduce folds a list into one value",
        "Destructuring pulls values out",
    ], code='''const prices = [120, 450, 80];
const withTax = prices.map(p => p * 1.18);
const cheap = prices.filter(p => p < 200);
const total = prices.reduce((s, p) => s + p, 0);

const ticket = { id: 7, priority: "high" };
const { id, priority } = ticket;
const copy = { ...ticket, status: "open" };

console.log(cheap, total, id, copy.status);
// [ 120, 80 ] 650 7 open'''),
    dict(type="bullets_code", title="Loops", bullets=[
        "for...of loops over array values",
        "for...in loops over object keys",
        "Classic for when you need the index",
        "while for unknown repeat counts",
    ], code='''const tickets = ["T1", "T2", "T3"];
for (const t of tickets) console.log(t);

const user = { name: "Ravi", role: "agent" };
for (const key in user) {
  console.log(key, "=", user[key]);
}

for (let i = 0; i < 3; i++) {
  console.log("Attempt", i + 1);
}'''),
    dict(type="table", title="Three JavaScript gotchas", header=["Gotcha", "Example", "Habit"], rows=[
        ["== converts types", '"5" == 5 is true', "Always use ==="],
        ["undefined vs null", "Missing value vs empty", "Check both when reading data"],
        ["Numbers are floats", "0.1 + 0.2 !== 0.3", "Round money values"],
    ], note="Run JavaScript with Node.js: node app.js. In Colab: !node app.js."),

    dict(type="section", title="Functions and callbacks", sub="Session 2 | 2 hrs | Passing behaviour around"),
    dict(type="bullets_code", title="Three ways to write a function", bullets=[
        "Function declaration: hoisted, named",
        "Function expression stored in a const",
        "Arrow function: short, common in modern code",
        "Default parameters work like Python",
    ], code='''function greet(name = "friend") {
  return `Hello, ${name}!`;
}

const square = function (n) { return n * n; };

const isUrgent = (t) => t.priority === "high";

console.log(greet(), square(4),
  isUrgent({ priority: "high" }));
// Hello, friend! 16 true'''),
    dict(type="cards", title="What is a callback?", greet="Tsugi (次): Next", items=[
        ("A function as a value", "Functions can be passed to other functions, like any value."),
        ("Called back later", "The receiver decides when to call it: per item, on an event, after a timer."),
        ("You already used them", "map, filter and reduce all take callbacks."),
    ]),
    dict(type="bullets_code", title="Callbacks in practice", bullets=[
        "forEach calls your function per item",
        "sort takes a compare callback",
        "setTimeout calls back after a delay",
        "Write your own: applyToAll(items, fn)",
    ], code='''const tickets = [{ id: 1, age: 5 }, { id: 2, age: 9 }];

tickets.forEach(t => console.log("Ticket", t.id));

const oldest = [...tickets].sort((a, b) => b.age - a.age);

function applyToAll(items, fn) {
  return items.map(fn);
}
console.log(applyToAll([1, 2, 3], n => n * 10));

setTimeout(() => console.log("Reminder sent"), 500);'''),
    dict(type="code", title="Callback pyramid: why promises were invented", code='''getCustomer(42, (err, customer) => {
  if (err) return console.log(err);
  getTickets(customer.id, (err, tickets) => {
    if (err) return console.log(err);
    getAgent(tickets[0].agentId, (err, agent) => {
      if (err) return console.log(err);
      console.log(agent.name);   // three levels deep already
    });
  });
});''', note="Nested callbacks are hard to read and easy to break. Promises flatten this."),

    dict(type="section", title="Async JavaScript", sub="Session 3 | 2.5 hrs | Do something useful while you wait"),
    dict(type="compare", title="The coffee shop", greet="Kissaten (喫茶店): Coffee shop",
         left=dict(title="Blocking (synchronous)", bullets=[
             "Barista takes one order", "Stands at the machine until it is done", "Next customer waits the whole time",
         ]), right=dict(title="Non-blocking (asynchronous)", bullets=[
             "Barista takes an order, starts the machine", "Takes the next order meanwhile",
             "Calls your name when it is ready",
         ])),
    dict(type="flow", title="The event loop", items=[
        ("Run", "Execute the current code"),
        ("Hand off", "Slow work (disk, network, timers) goes to the system"),
        ("Continue", "Keep running other code"),
        ("Callback", "When work finishes, its callback is queued and run"),
    ], note="One thread, never idle. This is why JavaScript handles many tasks at once."),
    dict(type="bullets_code", title="Order of execution", bullets=[
        "Synchronous code runs first",
        "setTimeout schedules for later, even at 0 ms",
        "The callback runs when the stack is clear",
        "Predict the output before running it",
    ], code='''console.log("1: order taken");

setTimeout(() => {
  console.log("3: coffee ready");
}, 0);

console.log("2: next customer");

// Output:
// 1: order taken
// 2: next customer
// 3: coffee ready'''),
    dict(type="table", title="The three states of a promise", header=["State", "Meaning", "Coffee shop"], rows=[
        ["pending", "Still working", "Your order is being made"],
        ["fulfilled", "Finished with a value", "Coffee handed over"],
        ["rejected", "Failed with an error", '"Sorry, we ran out of milk"'],
    ], note="A promise settles once: fulfilled or rejected, never both."),
    dict(type="bullets_code", title="Creating and using a promise", bullets=[
        "resolve(value) on success",
        "reject(error) on failure",
        ".then handles the value",
        ".catch handles any error in the chain",
    ], code='''function makeCoffee(type) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (type === "latte") resolve("Latte!");
      else reject(new Error("Unknown drink"));
    }, 500);
  });
}

makeCoffee("latte")
  .then(msg => console.log(msg))
  .catch(err => console.log(err.message));'''),
    dict(type="bullets_code", title="async and await", bullets=[
        "async functions always return a promise",
        "await pauses this function, not the program",
        "try / catch handles rejections",
        "Same idea as Python's async def",
    ], code='''async function serve() {
  try {
    const a = await makeCoffee("latte");
    console.log(a);
    const b = await makeCoffee("tea");
    console.log(b);
  } catch (err) {
    console.log("Problem:", err.message);
  }
}
serve();'''),
    dict(type="bullets_code", title="Running things in parallel", bullets=[
        "Awaiting one by one adds the times together",
        "Promise.all runs them together",
        "Fails fast if any one rejects",
        "allSettled reports every result",
    ], code='''// Sequential: about 1000 ms
await makeCoffee("latte");
await makeCoffee("latte");

// Parallel: about 500 ms
const drinks = await Promise.all([
  makeCoffee("latte"),
  makeCoffee("latte"),
]);
console.log(drinks.length);   // 2'''),
    dict(type="bullets_code", title="fetch: calling APIs from JavaScript", bullets=[
        "fetch returns a promise of a Response",
        "Check response.ok for 2xx",
        "response.json() is also a promise",
        "Built into browsers and Node.js 18+",
    ], code='''async function loadTickets() {
  const res = await fetch(
    "http://localhost:8000/tickets");
  if (!res.ok) {
    throw new Error(`HTTP ${res.status}`);
  }
  const tickets = await res.json();
  console.log(tickets.length, "tickets");
}'''),
    dict(type="bullets_code", title="JSON: parse and stringify", bullets=[
        "JSON.stringify: object to text",
        "JSON.parse: text to object",
        "Send text over HTTP, work with objects in code",
        "Wrap JSON.parse in try / catch",
    ], code='''const ticket = { id: 7, tags: ["sim", "5g"] };

const text = JSON.stringify(ticket);
console.log(text);   // {"id":7,"tags":["sim","5g"]}

const back = JSON.parse(text);
console.log(back.tags[1]);   // 5g

try {
  JSON.parse("{bad json}");
} catch (e) {
  console.log("Invalid JSON:", e.name);
}'''),
    dict(type="cards", title="SmartDesk step 7: an async ticket client", items=[
        ("Goal", "A JavaScript client that reads the SmartDesk ticket API asynchronously."),
        ("What it does", "fetch tickets, count by priority, list the oldest open ones."),
        ("Error handling", "Check res.ok, catch network errors, show a clear message."),
        ("Build with Codex", "Use Day08_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="callout", title="Hands-on time", text="Write JavaScript that processes SmartDesk ticket data, then an "
         "async client that loads the tickets from an API and summarises them.",
         sub="Predict the output of every async snippet before you run it.", greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Fundamentals", "const and let, === always, map, filter and reduce."),
        ("Functions", "Arrow functions and callbacks pass behaviour around."),
        ("Async", "The event loop never blocks. Promises: pending, fulfilled, rejected."),
        ("await and fetch", "Readable async code. Check res.ok. JSON in and out."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics.", items=[
        ("Hotel lab", "Follow Day08_Hotel_Lab.md: post-read, notebook, problems, async script."),
        ("Workbook", "Complete the Day 8 workbook, especially async ordering."),
        ("Pre-read", "Skim the Day 9 pre-read. Install Postman before class."),
    ]),
]

PREREAD = dict(title="A New Language That Never Waits",
               lede="A light read before Day 8. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "So far you have built back ends in Python. Today you meet **JavaScript**, the language that runs inside every "
        "web browser, and with a tool called Node.js, on servers too. You will also learn the one big idea that makes "
        "JavaScript different: it never sits idle waiting for slow things to finish."]),
    dict(h="1. Meet JavaScript", paras=[
        "If you know Python, JavaScript will feel familiar: it has variables, functions, lists (called **arrays**) and "
        "dictionaries (called **objects**). The main visible difference is that JavaScript uses curly braces { } "
        "instead of indentation."],
        table=[["Idea", "Python", "JavaScript"], ["A list of things", "list", "array"],
               ["Labelled information", "dict", "object"], ["Print something", "print()", "console.log()"],
               ["Group a block of code", "indentation", "{ curly braces }"]]),
    dict(h="2. Handing over instructions", paras=[
        "When you ask a friend to \"call me back when the parcel arrives\", you give them an instruction to follow "
        "later. In JavaScript you often pass a function to another function, to be called later. That function is "
        "called a **callback**."]),
    dict(h="3. The coffee shop", paras=[
        "Picture two coffee shops. In the first, the barista takes your order, makes the coffee, hands it over, and only "
        "then serves the next person. In the second, the barista takes your order, starts the machine, takes the next "
        "order, and calls your name when your coffee is ready. JavaScript works like the second shop. This is called "
        "**asynchronous** programming."]),
    dict(h="4. A receipt for something that is coming", paras=[
        "When you order, you get a buzzer. It is a **promise** that your coffee will arrive. Eventually you get your "
        "coffee, or you are told something went wrong. Two friendly words, **async** and **await**, let you write "
        "\"wait for the coffee, then add sugar\" in a natural top-to-bottom style."],
        table=[["Buzzer status", "Promise state"], ["Waiting", "pending"], ["Buzzes: coffee ready", "fulfilled"],
               ["Staff apologises: out of milk", "rejected"]],
        box="**Key idea:** start slow work, keep doing other things, and handle the result when it arrives."),
    dict(h="5. Think about these before class", bullets=[
        "Open any website, right-click and choose Inspect, then the Console tab. That is where JavaScript runs.",
        "Where else in daily life do you start something, do other things, and come back when it is ready?",
        "What should an app show you while it is waiting for data from the internet?"],
        after=["Before class, VS Code users: install Node.js LTS from nodejs.org.",
               "Hajimemashite (はじめまして): nice to meet you, said when meeting someone new, like JavaScript"]),
])

POSTREAD = dict(title="JavaScript and Async JavaScript: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Variables", "const by default, let when reassigning, avoid var."],
        ["Types", "string, number, boolean, undefined, null, object, array. typeof checks a type."],
        ["Collections", "Arrays with map, filter, reduce; objects with keys; destructuring and spread."],
        ["Loops", "for...of over values, for...in over keys, classic for with an index."],
        ["Equality", "Always === and !==."],
        ["Functions", "Declarations, expressions and arrow functions. Default parameters."],
        ["Callbacks", "Functions passed to other functions: forEach, sort, setTimeout."],
        ["Event loop", "One thread runs your code; finished background work queues callbacks."],
        ["Promises", "pending, then fulfilled (value) or rejected (error). .then / .catch / .finally."],
        ["async / await", "await pauses that function only. try / catch for errors. Promise.all for parallel."],
        ["fetch and JSON", "await fetch(url); check res.ok; await res.json(). JSON.parse and JSON.stringify."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. Promise.allSettled and Promise.race", code='''const results = await Promise.allSettled([taskA(), taskB()]);
results.forEach(r => console.log(r.status));   // fulfilled or rejected''',
         paras=["allSettled never fails fast. race returns whichever finishes first, useful for timeouts."]),
    dict(sub="2. Optional chaining and nullish coalescing", code='''const zip = order?.address?.zip;          // undefined instead of an error
const pageSize = settings.size ?? 10;     // 10 only when size is null or undefined'''),
    dict(sub="3. Timeouts with AbortController", paras=[
        "A fetch can hang if the server is slow. AbortController lets you cancel it after a few seconds, so your app "
        "can show a friendly error instead of waiting forever."]),
    dict(sub="4. Microtasks and macrotasks", paras=[
        "Promise callbacks (.then) run before timer callbacks (setTimeout), even a 0 ms timer. Try it: log from a "
        "resolved promise and a 0 ms timer and see which prints first."]),
    dict(sub="5. Modules", paras=[
        "Split code into files with export and import (or module.exports and require in older Node.js code). You will "
        "use both styles on Day 9 and in React."]),
    dict(h="Part C: Check yourself", bullets=[
        "What is the difference between const and let?",
        "Why should you prefer === over ==?",
        "What is a callback? Give two examples from today.",
        "Why does setTimeout(fn, 0) still run after the next console.log?",
        "What is the difference between awaiting two calls one after another and using Promise.all?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Rewrite one callback example from the notebook with async and await.",
        "Write groupBy(items, key) and group SmartDesk tickets by priority.",
        "Write a script that fetches the SmartDesk tickets and prints the three oldest open ones."],
        after=["**Coming up on Day 9:** Node.js, npm and supply chain hygiene, building a CRUD API with Express, and "
               "testing APIs with Postman.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems: three on JavaScript fundamentals and callbacks, four on async JavaScript. Run "
                    "JavaScript with Node.js (in Colab: !node file.js).", problems=[
    dict(title="JavaScript Warm-up", level="Warm-up", concepts="const, let, functions, template literals",
         text="Write functions to convert Celsius to Fahrenheit, check if a number is even, and build a greeting "
              "with a template literal. Print the results with console.log.",
         sample="37 C = 98.6 F\n7 is odd\nHello, Aiko! Welcome to Day 8.",
         hints=["const toF = (c) => c * 9 / 5 + 32;"]),
    dict(title="Ticket Array Workout", level="Easy", concepts="map, filter, reduce, objects",
         text="Given an array of SmartDesk ticket objects (id, title, priority, ageHours, status), print the titles of "
              "open high-priority tickets, the average age of open tickets, and the oldest ticket.",
         sample="High and open: No signal at home, Double charge\nAverage open age: 13.7 h\nOldest: T-104 (30 h)",
         hints=["reduce((max, t) => t.ageHours > max.ageHours ? t : max)"]),
    dict(title="Group By with a Callback", level="Medium", concepts="callbacks, objects as maps",
         text="Write groupBy(items, keyFn) where keyFn is a callback that returns the group name. Use it to group "
              "tickets by status, then by \"old\" or \"new\" (older than 24 hours).",
         sample="{ open: 4, pending: 2, closed: 1 }\n{ old: 2, new: 5 }",
         hints=["Start with {} and push into acc[keyFn(item)] ??= []."]),
    dict(title="Predict the Order", level="Easy", concepts="event loop, setTimeout",
         text="Write a script with three console.log calls and two setTimeout calls (0 ms and 100 ms) mixed in. "
              "Predict the output on paper, then run it and compare.",
         sample="A\nC\nB (timeout 0)\nD (timeout 100)",
         hints=["Synchronous code always finishes before any timer callback."]),
    dict(title="Promise Kitchen", level="Medium", concepts="new Promise, then, catch",
         text="Write cook(dish, ms) that resolves after ms milliseconds, or rejects if dish is \"pizza\" (out of "
              "cheese). Chain three dishes with then and handle the error with catch.",
         sample="rice ready\ncurry ready\nError: out of cheese for pizza",
         hints=["return new Promise((resolve, reject) => setTimeout(...))"]),
    dict(title="Sequential vs Parallel", level="Medium", concepts="async/await, Promise.all, timing",
         text="Cook three dishes of 500 ms each sequentially with await, then in parallel with Promise.all. Print how "
              "long each approach took.",
         sample="Sequential: 1503 ms\nParallel: 502 ms",
         hints=["const start = Date.now(); ... Date.now() - start"]),
    dict(title="Async Ticket Client", level="Stretch", concepts="fetch, JSON, async/await, error handling",
         text="Using the small ticket server from the notebook, write client.js that fetches /tickets, prints a count "
              "per priority, and fetches /tickets/999 to show a clean error for a 404. Use JSON.stringify to print one "
              "ticket.",
         sample="Loaded 6 tickets\n{ high: 2, medium: 3, low: 1 }\nError: HTTP 404 for /tickets/999",
         hints=["if (!res.ok) throw new Error(`HTTP ${res.status}`)", "Wrap the whole flow in try / catch."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "In JavaScript, use ________ for values that are never reassigned.",
        "JavaScript's version of print() is ________.",
        "The array method ________ keeps only items that match a condition.",
        "Always compare in JavaScript with ________ instead of ==.",
        "A function passed to another function to be called later is a ________.",
        "Code that starts slow work and keeps running is called ________.",
        "A promise that has not finished yet is in the ________ state.",
        "Inside an async function, ________ pauses until a promise settles.",
        "To run several promises in parallel, use Promise.________().",
        "JSON.________ turns a JavaScript object into a JSON string.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "List three similarities and two differences between Python and JavaScript.",
        "Explain callbacks using an everyday example, then a code example.",
        "Explain asynchronous code with the coffee shop example.",
        "When should you use Promise.all instead of awaiting one by one?",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write exactly what it prints or returns.", items=[
        'const nums = [1, 2, 3, 4];\nconsole.log(nums.map(n => n * 10).filter(n => n > 15));',
        'console.log("A");\nsetTimeout(() => console.log("B"), 0);\nconsole.log("C");',
        'Promise.resolve(5)\n  .then(x => x * 2)\n  .then(x => console.log(x));',
        'Promise.reject(new Error("no"))\n  .then(() => console.log("yes"))\n  .catch(e => console.log(e.message));',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write an arrow function that returns the largest number in an array."),
        dict(q="Write a function repeat(n, fn) that calls the callback fn n times with the index."),
        dict(q="Write a function wait(ms) that returns a promise resolving after ms milliseconds."),
        dict(q="Write an async function that fetches a URL and returns the parsed JSON, throwing on non-2xx."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="Variables, arrays, objects, functions and callbacks, then promises, async and await, fetch "
                         "and JSON", cells=[
    ("md", "## 1. Setup\nGoogle Colab already has Node.js. In each section, `%%writefile` saves a JavaScript file and "
           "`!node` runs it.\n\n**VS Code:** install Node.js LTS from nodejs.org, save each file, then run "
           "`node file.js` in the terminal."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node --version

# ===== Option B: VS Code =====
# In the VS Code terminal:
#   node --version'''),
    ("md", "## 2. Variables, types and template literals (Session 1)"),
    ("code", '''%%writefile basics.js
// Variables
const city = "Pune";
let count = 3;
count += 1;
console.log(`${city} has ${count} open tickets`);

// Types
console.log(typeof count, typeof city, typeof true, typeof undefined, typeof null, typeof [1, 2]);

// Functions preview
const toF = (c) => c * 9 / 5 + 32;
const isEven = (n) => n % 2 === 0;
console.log(`37 C = ${toF(37).toFixed(1)} F`);
console.log(`7 is ${isEven(7) ? "even" : "odd"}`);

// Gotchas
console.log("5" == 5, "5" === 5);
console.log(0.1 + 0.2, (0.1 + 0.2).toFixed(2));'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node basics.js

# ===== Option B: VS Code =====
# node basics.js'''),
    ("md", "## 3. Arrays, objects and loops with SmartDesk tickets"),
    ("code", '''%%writefile tickets.js
const tickets = [
  { id: "T-101", title: "No signal at home", priority: "high", ageHours: 20, status: "open" },
  { id: "T-102", title: "Double charge", priority: "high", ageHours: 9, status: "open" },
  { id: "T-103", title: "Change plan", priority: "low", ageHours: 3, status: "closed" },
  { id: "T-104", title: "Slow 5G data", priority: "medium", ageHours: 30, status: "pending" },
  { id: "T-105", title: "SIM not activated", priority: "medium", ageHours: 12, status: "open" },
];

module.exports = { tickets };

// Only print when run directly (node tickets.js), not when required by another file
if (require.main === module) {
  const highOpen = tickets.filter(t => t.priority === "high" && t.status === "open").map(t => t.title);
  const open = tickets.filter(t => t.status === "open");
  const avgAge = open.reduce((sum, t) => sum + t.ageHours, 0) / open.length;
  const oldest = tickets.reduce((max, t) => (t.ageHours > max.ageHours ? t : max));
  const { id, ageHours } = oldest;

  console.log("High and open:", highOpen.join(", "));
  console.log("Average open age:", avgAge.toFixed(1), "h");
  console.log(`Oldest: ${id} (${ageHours} h)`);

  for (const t of tickets) {
    if (t.ageHours > 24) console.log("Escalate:", t.id);
  }
  for (const key in oldest) console.log(" ", key, "=", oldest[key]);

  const updated = { ...oldest, status: "escalated" };
  console.log(oldest.status, "->", updated.status);
}'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node tickets.js

# ===== Option B: VS Code =====
# node tickets.js'''),
    ("md", "### TODO 1: Print the number of tickets per status using a `for...of` loop and an object as a counter."),
    ("code", "# TODO: write your code here (use %%writefile and !node)"),
    ("md", "## 4. Functions and callbacks (Session 2)"),
    ("code", '''%%writefile callbacks.js
const { tickets } = require("./tickets.js");

// Three ways to write a function
function greet(name = "friend") { return `Hello, ${name}!`; }
const square = function (n) { return n * n; };
const isUrgent = (t) => t.priority === "high";
console.log(greet(), greet("Aiko"), square(4));

// Your own function that takes a callback
function groupBy(items, keyFn) {
  return items.reduce((acc, item) => {
    (acc[keyFn(item)] ??= []).push(item);
    return acc;
  }, {});
}
const byStatus = groupBy(tickets, t => t.status);
const byAge = groupBy(tickets, t => (t.ageHours > 24 ? "old" : "new"));
const counts = (g) => Object.fromEntries(Object.entries(g).map(([k, v]) => [k, v.length]));
console.log(counts(byStatus), counts(byAge));

// Built-in functions that take callbacks
tickets.filter(isUrgent).forEach(t => console.log("Urgent:", t.id));
const byOldest = [...tickets].sort((a, b) => b.ageHours - a.ageHours).map(t => t.id);
console.log("Oldest first:", byOldest.join(" "));
setTimeout(() => console.log("Reminder: follow up on T-104"), 200);
console.log("This line prints before the reminder");'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node callbacks.js

# ===== Option B: VS Code =====
# node callbacks.js'''),
    ("md", "## 5. The event loop: predict, then run (Session 3)"),
    ("code", '''%%writefile order.js
console.log("1: order taken");
setTimeout(() => console.log("4: coffee ready (timer 100 ms)"), 100);
setTimeout(() => console.log("3: tea ready (timer 0 ms)"), 0);
console.log("2: next customer");'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node order.js

# ===== Option B: VS Code =====
# node order.js'''),
    ("md", "## 6. Promises"),
    ("code", '''%%writefile promises.js
function cook(dish, ms = 300) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (dish === "pizza") reject(new Error(`out of cheese for ${dish}`));
      else resolve(`${dish} ready`);
    }, ms);
  });
}

cook("rice")
  .then(msg => { console.log(msg); return cook("curry"); })
  .then(msg => { console.log(msg); return cook("pizza"); })
  .then(msg => console.log(msg))
  .catch(err => console.log("Error:", err.message))
  .finally(() => console.log("Kitchen closed"));'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node promises.js

# ===== Option B: VS Code =====
# node promises.js'''),
    ("md", "## 7. async / await and Promise.all"),
    ("code", '''%%writefile async_demo.js
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));
const cook = async (dish) => { await wait(500); return `${dish} ready`; };

async function main() {
  let start = Date.now();
  await cook("rice");
  await cook("curry");
  await cook("dal");
  console.log(`Sequential: ${Date.now() - start} ms`);

  start = Date.now();
  const dishes = await Promise.all([cook("rice"), cook("curry"), cook("dal")]);
  console.log(`Parallel:   ${Date.now() - start} ms`, dishes);

  try {
    await Promise.reject(new Error("burnt toast"));
  } catch (err) {
    console.log("Caught:", err.message);
  }
}
main();'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node async_demo.js

# ===== Option B: VS Code =====
# node async_demo.js'''),
    ("md", "### TODO 2: Use `Promise.allSettled` with one dish that fails, and print the status of each result."),
    ("code", "# TODO: write your code here (use %%writefile and !node)"),
    ("md", "## 8. JSON: parse and stringify"),
    ("code", '''%%writefile json_demo.js
const ticket = { id: 7, title: "Slow 5G data", tags: ["5g", "speed"], customer: { name: "Mei" } };

const text = JSON.stringify(ticket);
console.log(text, "|", typeof text);
console.log(JSON.stringify(ticket, null, 2));

const back = JSON.parse(text);
console.log(back.customer.name, back.tags.length);

try {
  JSON.parse("{bad json}");
} catch (e) {
  console.log("Invalid JSON:", e.name);
}'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node json_demo.js

# ===== Option B: VS Code =====
# node json_demo.js'''),
    ("md", "## 9. fetch: an async client for a ticket API (SmartDesk step 7)\nTo keep this notebook self-contained, the "
           "script starts a tiny ticket API with Node's built-in `http` module, then an async client calls it with "
           "`fetch`. On your laptop, point `BASE` at your SmartDesk FastAPI instead (for example "
           "`http://127.0.0.1:8000`)."),
    ("code", '''%%writefile client.js
const http = require("http");
const tickets = [
  { id: 1, title: "No signal at home", priority: "high", status: "open" },
  { id: 2, title: "Double charge", priority: "high", status: "open" },
  { id: 3, title: "Change plan", priority: "low", status: "closed" },
  { id: 4, title: "Slow 5G data", priority: "medium", status: "pending" },
  { id: 5, title: "SIM not activated", priority: "medium", status: "open" },
  { id: 6, title: "Roaming question", priority: "medium", status: "open" },
];

// A tiny stand-in API: GET /tickets and GET /tickets/:id
const server = http.createServer((req, res) => {
  const match = req.url.match(/^\\/tickets(?:\\/(\\d+))?$/);
  res.setHeader("Content-Type", "application/json");
  if (!match) { res.statusCode = 404; return res.end(JSON.stringify({ error: "Route not found" })); }
  if (!match[1]) return res.end(JSON.stringify(tickets));
  const t = tickets.find(x => x.id === Number(match[1]));
  if (!t) { res.statusCode = 404; return res.end(JSON.stringify({ error: "Ticket not found" })); }
  res.end(JSON.stringify(t));
});

async function getJSON(base, path) {
  const res = await fetch(base + path);
  if (!res.ok) throw new Error(`HTTP ${res.status} for ${path}`);
  return res.json();
}

server.listen(0, async () => {
  const BASE = process.env.BASE_URL || `http://127.0.0.1:${server.address().port}`;
  try {
    const all = await getJSON(BASE, "/tickets");
    console.log("Loaded", all.length, "tickets");
    const byPriority = all.reduce((acc, t) => ({ ...acc, [t.priority]: (acc[t.priority] || 0) + 1 }), {});
    console.log(byPriority);
    const [first, second] = await Promise.all([getJSON(BASE, "/tickets/1"), getJSON(BASE, "/tickets/2")]);
    console.log("In parallel:", first.title, "|", second.title);
    console.log(JSON.stringify(first));
    await getJSON(BASE, "/tickets/999");
  } catch (err) {
    console.log("Error:", err.message);
  } finally {
    server.close();
  }
});'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node client.js

# ===== Option B: VS Code =====
# node client.js
# Or, with your SmartDesk API running:  BASE_URL=http://127.0.0.1:8000 node client.js'''),
    ("md", "### TODO 3: Add a function that prints the open tickets as a numbered list, sorted by priority (high first)."),
    ("code", "# TODO: write your code here (use %%writefile and !node)"),
    ("md", "## 10. Check yourself\n1. Why did the reminder in section 4 print last?\n"
           "2. Why was Promise.all faster in section 7?\n3. What would happen in section 9 without the `res.ok` check?"),
])
