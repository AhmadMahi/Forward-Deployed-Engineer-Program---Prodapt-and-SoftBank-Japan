"""Day 09 spec. Node.js and Express.
Source: REUSE archive/v1-40-day/Day10 Sessions 2 to 4 (npm, Express, Postman). NEW (v4): npm supply chain hygiene.
"""
DAY = 9
FOLDER = "Day09-Nodejs-and-Express"
SLUG = "Nodejs_and_Express"
TITLE = "Node.js and Express"
SUBTITLE = "The Node runtime, npm and supply chain hygiene, Express CRUD APIs, and testing with Postman"
DATE = "Thu 05 Nov 2026"
TRACK = "Basics"
NEXT = "See you tomorrow for Day 10: React basics, plus Basics assessment 2."

DECK = [
    dict(type="cards", title="Today's journey", greet="Ohayou gozaimasu (おはようございます): Good morning", items=[
        ("Quiz", "15 questions on Day 8"),
        ("Node.js and npm", "Runtime, packages, package.json"),
        ("Supply chain", "Lockfiles and npm audit. NEW (v4)"),
        ("Express", "Routes, controllers, CRUD APIs"),
        ("Postman", "Collections, environments, tests"),
        ("SmartDesk", "Express notification service"),
    ]),
    dict(type="cards", title="By the end of today you can", items=[
        ("Set up a Node project", "Use npm, package.json and scripts with confidence."),
        ("Keep dependencies safe", "Commit the lockfile, use npm ci, read npm audit output."),
        ("Build with Express", "Write a CRUD API with routes, controllers and status codes."),
        ("Test and handle errors", "Test with Postman and handle errors in async routes."),
    ]),
    dict(type="table", title="Today's sessions", header=["Session", "Duration", "Topics"], rows=[
        ["Opening", "30 min", "Kahoot / recap quiz on Day 8"],
        ["Session 1", "1.5 hrs", "Node runtime, npm, project structure, package.json; NEW (v4) lockfiles, npm audit"],
        ["Session 2", "2.5 hrs", "Express setup, routes, controllers, CRUD APIs"],
        ["Session 3", "2.5 hrs", "Postman testing; error handling in async routes"],
    ]),

    dict(type="section", title="The Node.js runtime", sub="Session 1 | 1.5 hrs | JavaScript outside the browser"),
    dict(type="cards", title="What Node.js gives you", items=[
        ("A runtime", "Runs JavaScript on servers and laptops, not only in browsers."),
        ("Built-in modules", "fs for files, http for servers, path, os, crypto."),
        ("The event loop", "One thread, non-blocking I/O: many requests at once (Day 8)."),
        ("npm", "The package manager and registry. npm is to Node.js what pip is to Python."),
    ]),
    dict(type="bullets_code", title="Modules: require and export", bullets=[
        "One file is one module",
        "module.exports shares functions",
        "require loads them in another file",
        "ES modules use import and export",
    ], code='''// store.js
let tasks = [];
const add = (title) => {
  const t = { id: tasks.length + 1,
              title };
  tasks.push(t);
  return t;
};
module.exports = { add };

// server.js
const { add } = require("./store");
console.log(add("Learn Express"));'''),
    dict(type="table", title="npm essentials", header=["Command or file", "What it does"], rows=[
        ["npm init -y", "Create package.json for a new project"],
        ["npm install express", "Add a package to node_modules and package.json"],
        ["npm install -D nodemon", "Add a development-only tool"],
        ["package.json", "Project name, scripts and dependency ranges"],
        ["node_modules/", "Installed packages: never commit to Git"],
        ["npm run dev", "Run a script defined in package.json"],
    ]),
    dict(type="bullets_code", title="A typical project structure", bullets=[
        "src/ for code, tests/ for tests",
        "routes call controllers",
        "controllers hold the logic",
        "scripts start and watch the server",
    ], code='''tasks-api/
  package.json
  package-lock.json
  .gitignore     # node_modules, .env
  src/
    app.js       # app and middleware
    server.js    # listen on a port
    routes/
      tasks.js
    controllers/
      tasks.js
  tests/'''),
    dict(type="section", title="npm supply chain hygiene", sub="Every package you install is code you trust", new=True),
    dict(type="cards", title="Why the supply chain matters", new=True, items=[
        ("Deep trees", "Installing one package can pull in dozens of other packages."),
        ("Real risks", "Known vulnerabilities, abandoned packages, typo-squatted names."),
        ("AI suggestions too", "Codex may suggest packages. Check each name and need before installing."),
        ("Your job", "Pin versions, review changes, scan, and patch quickly."),
    ]),
    dict(type="table", title="Version ranges and the lockfile", new=True, header=["In package.json", "Allows", "Risk"], rows=[
        ['"express": "5.1.0"', "Exactly 5.1.0", "No surprise updates"],
        ['"express": "~5.1.0"', "5.1.x patch releases", "Small changes"],
        ['"express": "^5.1.0"', "5.x.x minor and patch releases", "More drift between machines"],
        ["package-lock.json", "Records the exact version of every package", "Commit it to Git"],
    ], note="The lockfile makes every install identical. Use npm ci in CI and on servers."),
    dict(type="compare", title="npm install vs npm ci", new=True, left=dict(title="npm install", bullets=[
        "Adds or updates packages", "May update package-lock.json", "Use while developing",
    ]), right=dict(title="npm ci", bullets=[
        "Installs exactly what the lockfile says", "Fails if package.json and lockfile disagree",
        "Deletes node_modules first", "Use in CI pipelines and on servers",
    ])),
    dict(type="bullets_code", title="npm audit", new=True, bullets=[
        "Checks installed packages against known advisories",
        "Groups findings by severity",
        "npm audit fix applies safe upgrades",
        "Review and test before accepting fixes",
    ], code='''$ npm audit
# Lists each vulnerable package, its
# severity, and the fixed version.

$ npm audit --audit-level=high
# Exit code 1 if high or critical
# findings exist: use in CI (Day 20)

$ npm audit fix
# Upgrades within your ranges.
# Run your tests again afterwards.'''),
    dict(type="cards", title="Supply chain checklist", new=True, items=[
        ("Before installing", "Is it needed? Is the name spelt right? Is it maintained?"),
        ("Commit", "package.json and package-lock.json. Never node_modules or .env."),
        ("In CI", "npm ci, then npm audit --audit-level=high."),
        ("Record it", "Log findings in the vulnerability report template (Day 7)."),
    ]),

    dict(type="section", title="Express", sub="Session 2 | 2.5 hrs | A web server in a few lines"),
    dict(type="bullets_code", title="Your first Express server", bullets=[
        "express() creates the app",
        "express.json() parses JSON bodies",
        "app.get / post / put / delete define routes",
        "res.status().json() sends a response",
    ], code='''const express = require("express");
const app = express();
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000, () =>
  console.log("Listening on 3000"));'''),
    dict(type="table", title="Where request data comes from", header=["Source", "Example URL or body", "Read with"], rows=[
        ["Path parameter", "/tasks/7", "req.params.id"],
        ["Query string", "/tasks?done=true", "req.query.done"],
        ["JSON body", '{"title": "Call back"}', "req.body.title"],
        ["Headers", "Authorization: Bearer ...", 'req.get("authorization")'],
    ]),
    dict(type="bullets_code", title="CRUD routes in Express", bullets=[
        "Validate input, return 400 if wrong",
        "201 for created, 204 for deleted",
        "404 for unknown ids",
        "Same status codes as FastAPI",
    ], code='''app.post("/tasks", (req, res) => {
  const { title } = req.body;
  if (!title) {
    return res.status(400)
      .json({ error: "title is required" });
  }
  const task = { id: nextId++,
    title, done: false };
  tasks.push(task);
  res.status(201).json(task);
});'''),
    dict(type="bullets_code", title="Routers and controllers", bullets=[
        "Router groups routes for one resource",
        "Controllers hold the handler functions",
        "app.use mounts the router on a path",
        "Like FastAPI's APIRouter",
    ], code='''// routes/tasks.js
const express = require("express");
const router = express.Router();
const c = require("../controllers/tasks");
router.get("/", c.list);
router.get("/:id", c.getOne);
router.post("/", c.create);
module.exports = router;

// app.js
const tasks = require("./routes/tasks");
app.use("/tasks", tasks);'''),
    dict(type="compare", title="FastAPI and Express side by side", left=dict(title="FastAPI (Python)", bullets=[
        '@app.get("/tasks/{id}")', "Validation with Pydantic", "Automatic /docs", "Depends() for shared logic",
    ]), right=dict(title="Express (Node.js)", bullets=[
        'app.get("/tasks/:id", ...)', "Validate manually or with a library", "Docs added with extra tools",
        "Middleware with app.use()",
    ])),

    dict(type="section", title="Testing and async errors", sub="Session 3 | 2.5 hrs | Click, send, inspect, recover"),
    dict(type="flow", title="A Postman workflow", items=[
        ("Request", "Choose method, enter URL"),
        ("Body", "Body tab, raw, JSON"),
        ("Send", "Read status, time and JSON"),
        ("Test", "pm.test checks the status"),
        ("Save", "Add to a collection"),
    ], note="Use a {{baseUrl}} variable so one collection works locally and in the cloud."),
    dict(type="bullets_code", title="Postman tests", bullets=[
        "Tests run after every request",
        "Check status code and JSON shape",
        "Run the whole collection in one click",
        "A quick regression suite for any API",
    ], code='''pm.test("status is 201", () => {
  pm.response.to.have
    .status(201);
});

pm.test("has an id", () => {
  const body = pm.response.json();
  pm.expect(body.id).to.exist;
});'''),
    dict(type="bullets_code", title="Errors in async routes", bullets=[
        "Database and network calls are async",
        "Express 5 sends rejected promises to the error handler",
        "Express 4 needed try / catch or a wrapper",
        "One error middleware returns a clean 500",
    ], code='''app.get("/tasks/:id", async (req, res) => {
  const t = await store.get(req.params.id);
  if (!t) return res.status(404)
    .json({ error: "Not found" });
  res.json(t);
});

// error middleware: four arguments
app.use((err, req, res, next) => {
  console.error(err.message);
  res.status(500)
    .json({ error: "Something went wrong" });
});'''),
    dict(type="table", title="Status codes your API should use", header=["Code", "When", "Express"], rows=[
        ["200", "Read or update worked", "res.json(data)"],
        ["201", "Created", "res.status(201).json(item)"],
        ["204", "Deleted, no body", "res.status(204).end()"],
        ["400", "Bad input", 'res.status(400).json({ error })'],
        ["404", "Unknown id or route", "Catch-all handler at the end"],
        ["500", "Unexpected error", "Error middleware"],
    ]),
    dict(type="cards", title="SmartDesk step 8: notification service", items=[
        ("Goal", "A small Express service that sends ticket notifications (simulated)."),
        ("Endpoints", "POST /notifications, GET /notifications, GET /health."),
        ("Quality", "Validation, async error handling, Postman tests, npm audit clean."),
        ("Build with Codex", "Use Day09_App_Build_Prompts.md. Review every line Codex writes."),
    ]),
    dict(type="callout", title="Hands-on time", text="Build a Tasks API with Express: routes, controllers, async error "
         "handling and proper status codes. Then test it with Postman and run npm audit.",
         sub="Import the Postman collection generated in today's notebook to save time.",
         greet="Ganbatte (頑張って): Do your best"),
    dict(type="cards", title="Key takeaways", items=[
        ("Node and npm", "Modules, package.json, scripts. Never commit node_modules."),
        ("Supply chain", "Commit the lockfile, npm ci in CI, npm audit and patch."),
        ("Express", "Routers, controllers, express.json(), clear status codes."),
        ("Testing", "Postman collections with tests; error middleware for async routes."),
    ]),
    dict(type="cards", title="Before tomorrow", lead="Tomorrow starts with a 15 question quiz on today's topics, and "
         "Basics assessment 2.", items=[
        ("Hotel lab", "Follow Day09_Hotel_Lab.md: notebook, problems, Postman export."),
        ("Workbook", "Complete the Day 9 workbook."),
        ("Pre-read", "Skim the Day 10 pre-read on React. Revise Days 6 to 9."),
    ]),
]

PREREAD = dict(title="Borrowing Tools Safely",
               lede="A light read before Day 9. About 15 minutes, no code required.", sections=[
    dict(h="Why read this?", paras=[
        "Yesterday you wrote JavaScript and learned how it handles waiting. Today you build a real web server in "
        "JavaScript with Node.js and a popular tool called Express, then test it without writing any screens."]),
    dict(h="1. JavaScript leaves the browser", paras=[
        "JavaScript was born inside web browsers. **Node.js** lets the same language run on servers and laptops. That "
        "means one language for the screens and the server, which is why many teams use it."]),
    dict(h="2. Borrowing tools: npm", paras=[
        "Nobody builds everything from scratch. **npm** is a huge free library of ready-made JavaScript tools, like an "
        "app store for code. A file called **package.json** is your shopping list: it says which tools your project "
        "needs."]),
    dict(h="3. Checking what you borrow", new=True, paras=[
        "When you borrow a ladder from a neighbour, you check it is safe before you climb. Code packages are the same. "
        "One package often brings many others with it. A file called the **lockfile** records exactly which versions "
        "you used, so everyone gets the same thing. A tool called **npm audit** checks your packages against a list of "
        "known security problems."],
        box="**Key idea:** every package you install is code you trust. Install only what you need, record exact "
            "versions, and check them regularly."),
    dict(h="4. A web server in a few lines", paras=[
        "**Express** is a small tool for building web servers in Node.js. You will write the same kind of API you built "
        "with FastAPI: create, read, update and delete items, with clear status codes."]),
    dict(h="5. Testing without building a screen", paras=[
        "How do you test an API before anyone builds the app screens? You use **Postman**, a free tool where you type "
        "an address, pick GET or POST, press Send, and see the reply."],
        box="**Before class:** install Postman (desktop or web) and, for VS Code users, Node.js LTS from nodejs.org."),
    dict(h="6. Think about these before class", bullets=[
        "Why might two laptops get different results from the same project if versions are not recorded?",
        "Would you install a package with a name that is one letter different from a popular one? Why not?",
        "Why is it useful to test an API before the app screens exist?"],
        after=["Dougu (道具): tools"]),
])

POSTREAD = dict(title="Node.js and Express: Recap and Beyond",
                lede="What we covered today, plus ideas to stretch your understanding.", sections=[
    dict(h="Part A: Summary of today", table=[
        ["Topic", "What to remember"],
        ["Node.js", "A JavaScript runtime with built-in modules (fs, http, path) and the event loop."],
        ["Modules", "module.exports and require (CommonJS), or export and import (ES modules)."],
        ["npm", "npm init -y, npm install pkg, npm install -D tool, npm run script."],
        ["package.json", "Name, scripts and dependency ranges. Never commit node_modules."],
        ["Lockfile (NEW v4)", "package-lock.json records exact versions. Commit it. npm ci installs from it."],
        ["npm audit (NEW v4)", "Finds known vulnerabilities. --audit-level=high fails CI. Test after npm audit fix."],
        ["Express", "express(), app.use(express.json()), routers, controllers, res.status().json()."],
        ["Request data", "req.params (path), req.query (query string), req.body (JSON), req.get (headers)."],
        ["Async errors", "Express 5 forwards rejected promises to the error middleware (err, req, res, next)."],
        ["Postman", "Requests, JSON bodies, {{baseUrl}} environments, pm.test checks, collection runs."],
    ]),
    dict(h="Part B: Going beyond today", sub="1. nodemon for auto reload", paras=[
        "npm install -D nodemon, then add \"dev\": \"nodemon src/server.js\" to scripts. It restarts the server on every "
        "save, like uvicorn --reload."]),
    dict(sub="2. Environment variables", code='''const PORT = process.env.PORT || 3000;
// Secrets come from the environment or a git-ignored .env file, never from the code.''') ,
    dict(sub="3. Validation libraries", paras=[
        "Instead of many if checks, a schema library validates the whole body at once, similar to Pydantic. Check the "
        "package carefully before adding it, as you learned today."]),
    dict(sub="4. Overrides for a vulnerable sub-dependency", paras=[
        "Sometimes the vulnerable package is deep in the tree and the top package has not released a fix yet. npm "
        "\"overrides\" in package.json can force a fixed version. Test well, and remove the override once the top "
        "package updates."]),
    dict(sub="5. Testing Express without Postman", paras=[
        "Start the app on a random port in a test script and call it with fetch, or use a test library. On Day 15 you "
        "will automate API tests for FastAPI with PyTest; the same idea applies here."]),
    dict(h="Part C: Check yourself", bullets=[
        "Why should node_modules not be committed to Git, but package-lock.json should?",
        "What is the difference between npm install and npm ci?",
        "What does ^5.1.0 allow that 5.1.0 does not?",
        "Where do req.params, req.query and req.body come from?",
        "What happens in Express 5 when an async route throws an error?"]),
    dict(h="Part D: Practice ideas for tonight", bullets=[
        "Add PATCH and filtering by done=true or false to your Express Tasks API.",
        "Add Postman tests to every request in your collection and run the whole collection.",
        "Run npm audit on your project and write one line per finding in the vulnerability report template."],
        after=["**Coming up on Day 10:** React basics: single page apps, JSX, components, props, state and events, "
               "building the SmartDesk dashboard with Codex, and Basics assessment 2.",
               "Otsukaresama deshita (お疲れ様でした): thank you for your hard work today"]),
])

HANDSON = dict(lede="Seven problems. Run Node.js scripts in Colab with !node file.js, or in the VS Code terminal. "
                    "Test the API with Postman or a client script.", problems=[
    dict(title="Modules Warm-up", level="Warm-up", concepts="module.exports, require, fs/promises",
         text="Create store.js that exports add(title), list() and save(path). save writes the tasks to a JSON file "
              "with fs/promises. Use it from main.js to add three tasks, save them and print the file contents.",
         sample="Added 3 tasks\nSaved to tasks.json\n[{\"id\":1,\"title\":\"Read post-read\"}, ...]",
         hints=["const fs = require(\"fs/promises\");", "await fs.writeFile(path, JSON.stringify(tasks, null, 2))"]),
    dict(title="Read the Lockfile", level="Easy", concepts="package.json ranges, package-lock.json", new=True,
         text="Install express in a new project. Compare the range in package.json with the exact version in "
              "package-lock.json. Write check_lock.js that prints every top-level dependency with its range and its "
              "locked version.",
         sample="express   range ^5.1.0   locked 5.1.0\nnodemon   range ^3.1.0   locked 3.1.10 (dev)",
         hints=["JSON.parse(fs.readFileSync(\"package-lock.json\", \"utf8\")).packages[\"node_modules/express\"].version"]),
    dict(title="Audit and Report", level="Medium", concepts="npm audit, severity, vulnerability report", new=True,
         text="Run npm audit --json on your project (or use the sample audit file from the notebook). Write a script "
              "that counts findings by severity and prints one row per package in the vulnerability report format: "
              "finding, tool, severity, affected package, proposed fix.",
         sample="critical 0 | high 1 | moderate 2 | low 0\nV-01 | npm audit | high | example-pkg | upgrade to 2.4.1",
         hints=["Exit with code 1 when high or critical findings exist, so CI can fail the build."]),
    dict(title="Express Tasks API", level="Medium", concepts="Express routes, express.json, status codes",
         text="Build GET /tasks, GET /tasks/:id, POST /tasks (400 without title, 201 on success), PUT /tasks/:id and "
              "DELETE /tasks/:id (204). Return 404 for unknown ids. Use a router and a controller file.",
         sample="POST /tasks {} -> 400 {\"error\": \"title is required\"}\nDELETE /tasks/1 -> 204",
         hints=["Number(req.params.id) converts the id.", "res.status(204).end()"]),
    dict(title="Logging Middleware and 404s", level="Easy", concepts="app.use, next()",
         text="Add middleware that logs method, path, status and time taken for every request, and a catch-all 404 "
              "handler for unknown routes.",
         sample="POST /tasks 201 3ms\nGET /nope 404 1ms",
         hints=["res.on(\"finish\", ...) runs after the response is sent."]),
    dict(title="Async Errors", level="Challenging", concepts="async routes, error middleware",
         text="Make the store async (every function returns a promise after a short delay). Add a route that throws "
              "when the store is \"down\". Show that the error middleware returns a clean 500 JSON response and that "
              "the server keeps running.",
         sample="GET /tasks?simulate=down -> 500 {\"error\": \"Something went wrong\"}\nGET /health -> 200",
         hints=["Error middleware has four arguments: (err, req, res, next).",
                "On Express 4 wrap handlers: const wrap = fn => (req, res, next) => fn(req, res, next).catch(next);"]),
    dict(title="Postman Collection", level="Stretch", concepts="Postman, environments, tests",
         text="Create a collection with one request per endpoint using {{baseUrl}}. Add at least one test per request "
              "that checks the status code. Run the whole collection and export it.",
         sample="Collection run: 8 requests, 8 tests passed",
         hints=["Import the collection generated in the notebook as a starting point."]),
])

WORKBOOK = dict(sections=[
    dict(title="Section A: Fill in the blanks", kind="blanks", items=[
        "Node.js is a JavaScript ________ that runs outside the browser.",
        "In CommonJS, a file shares functions with module.________.",
        "The command ________ creates a package.json file.",
        "The folder ________ should never be committed to Git.",
        "The file that records the exact installed version of every package is ________.",
        "In CI, install dependencies with npm ________ so the lockfile is followed exactly.",
        "The command npm ________ checks packages for known vulnerabilities.",
        "In Express, ________ parses JSON request bodies.",
        "In Express, path parameters are read from req.________.",
        "In Postman, a saved group of requests is called a ________.",
    ]),
    dict(title="Section B: Answer in your own words", kind="short", items=[
        "Explain why committing package-lock.json makes builds repeatable.",
        "What would you check before installing a package that Codex suggested?",
        "Compare how FastAPI and Express define a GET route with a path parameter.",
        "Describe what happens when an async Express 5 route throws an error.",
    ]),
    dict(title="Section C: Predict the output", kind="predict",
         intro="Read each snippet carefully and write the status code and body, or what is printed.", items=[
        'app.post("/tasks", (req, res) => {\n  if (!req.body.title) return res.status(400).json({ error: "title is required" });\n  res.status(201).json({ id: 1, title: req.body.title });\n});\n// POST /tasks with body {}',
        'app.get("/tasks/:id", (req, res) => res.json({ id: req.params.id, type: typeof req.params.id }));\n// GET /tasks/7',
        '// package.json: "express": "^5.1.0"\n// Which of these could npm install choose?\n// 5.1.0, 5.4.2, 6.0.0, 4.21.0',
        'app.get("/boom", async () => { throw new Error("db down"); });\napp.use((err, req, res, next) => res.status(500).json({ error: "Something went wrong" }));\n// GET /boom on Express 5',
    ]),
    dict(title="Section D: Write small code", kind="code",
         intro="Write your code in the box, then test it in today's notebook.", items=[
        dict(q="Write the scripts section of a package.json with start and dev (nodemon) scripts."),
        dict(q="Write an Express GET /hello/:name route that returns a JSON greeting."),
        dict(q="Write an Express error-handling middleware that logs the error and returns 500 JSON."),
        dict(q="Write a pm.test that checks the status is 201 and the body has an id."),
    ]),
    dict(title="Section E: Reflection", kind="reflection"),
])

NOTEBOOK = dict(subtitle="The Node runtime, npm and supply chain hygiene, Express CRUD APIs, and testing with Postman",
                cells=[
    ("md", "## 1. Setup\nGoogle Colab already has Node.js and npm. `%%writefile` saves a file and `!node` runs it.\n\n"
           "**VS Code:** install Node.js LTS from nodejs.org, then run the same files with `node file.js` in the "
           "terminal."),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node --version
!npm --version

# ===== Option B: VS Code =====
# In the VS Code terminal:
#   node --version
#   npm --version'''),
    ("md", "## 2. The Node runtime: modules and files (Session 1)"),
    ("code", '''%%writefile store.js
const fs = require("fs/promises");

let tasks = [];
let nextId = 1;

function add(title) {
  const task = { id: nextId++, title, done: false };
  tasks.push(task);
  return task;
}
const list = () => [...tasks];
async function save(path) {
  await fs.writeFile(path, JSON.stringify(tasks, null, 2));
  return path;
}
module.exports = { add, list, save };'''),
    ("code", '''%%writefile main.js
const { add, list, save } = require("./store");
const fs = require("fs/promises");

async function main() {
  ["Read post-read", "Install Postman", "Run npm audit"].forEach(add);
  console.log("Added", list().length, "tasks");
  const path = await save("tasks.json");
  console.log("Saved to", path);
  console.log(await fs.readFile(path, "utf8"));
  console.log("Node", process.version, "on", process.platform);
}
main();'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node main.js

# ===== Option B: VS Code =====
# node main.js'''),
    ("md", "## 3. npm and package.json"),
    ("code", '''%%writefile package.json
{
  "name": "tasks-api",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "test": "node tests/api_test.js",
    "audit": "npm audit --audit-level=high"
  },
  "dependencies": {
    "express": "^5.1.0"
  },
  "devDependencies": {
    "nodemon": "^3.1.0"
  }
}'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!npm install --silent
!npm ls --depth=0

# ===== Option B: VS Code =====
# npm install
# npm ls --depth=0'''),
    ("md", "## 4. NEW (v4): npm supply chain hygiene\n`package.json` holds **ranges**. `package-lock.json` holds the "
           "**exact** versions that were installed. Commit the lockfile, never `node_modules`. This script explains "
           "each range and shows the locked version when a lockfile exists."),
    ("code", '''%%writefile check_lock.js
const fs = require("fs");
const pkg = JSON.parse(fs.readFileSync("package.json", "utf8"));
const lock = fs.existsSync("package-lock.json")
  ? JSON.parse(fs.readFileSync("package-lock.json", "utf8")) : null;

function explain(range) {
  if (range.startsWith("^")) return `same major (${range.slice(1).split(".")[0]}.x.x)`;
  if (range.startsWith("~")) return `same minor (${range.slice(1).split(".").slice(0, 2).join(".")}.x)`;
  return "exact version only";
}

const all = { ...pkg.dependencies, ...pkg.devDependencies };
for (const [name, range] of Object.entries(all)) {
  const locked = lock?.packages?.[`node_modules/${name}`]?.version ?? "not installed";
  const dev = name in (pkg.devDependencies || {}) ? " (dev)" : "";
  console.log(`${name.padEnd(9)} range ${range.padEnd(8)} -> ${explain(range).padEnd(22)} locked ${locked}${dev}`);
}
console.log(lock ? "Lockfile found: commit it." : "No lockfile yet: run npm install, then commit package-lock.json.");'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node check_lock.js

# ===== Option B: VS Code =====
# node check_lock.js'''),
    ("md", "### npm audit\nThe real command needs internet access to the npm registry. Run it in Colab or VS Code:"),
    ("code", '''# ===== Option A: Google Colab (active) =====
!npm audit
!npm audit --audit-level=high; echo "exit code: $?"

# ===== Option B: VS Code =====
# npm audit
# npm audit --audit-level=high''', ["skip-offline-check"]),
    ("md", "To practise reading audit output offline, the next cell writes a **made-up sample** in the same JSON shape "
           "as `npm audit --json`. The package names are fictional. Then a script turns it into vulnerability report "
           "rows (the template from Day 7)."),
    ("code", '''%%writefile sample_audit.json
{
  "vulnerabilities": {
    "example-parser": {"name": "example-parser", "severity": "high", "isDirect": false,
                       "via": [{"title": "Sample: prototype pollution in example-parser"}],
                       "fixAvailable": {"name": "example-parser", "version": "2.4.1"}},
    "demo-logger": {"name": "demo-logger", "severity": "moderate", "isDirect": true,
                    "via": [{"title": "Sample: log injection in demo-logger"}],
                    "fixAvailable": true},
    "toy-template": {"name": "toy-template", "severity": "moderate", "isDirect": false,
                     "via": [{"title": "Sample: regular expression denial of service"}],
                     "fixAvailable": false}
  }
}'''),
    ("code", '''%%writefile audit_report.js
const fs = require("fs");
const file = process.argv[2] || "sample_audit.json";
const { vulnerabilities } = JSON.parse(fs.readFileSync(file, "utf8"));
const levels = ["critical", "high", "moderate", "low"];
const counts = Object.fromEntries(levels.map(l => [l, 0]));

const rows = Object.values(vulnerabilities).map((v, i) => {
  counts[v.severity] += 1;
  const fix = v.fixAvailable === false ? "no fix yet: consider overrides or replacing"
    : v.fixAvailable === true ? "npm audit fix" : `upgrade to ${v.fixAvailable.version}`;
  const title = typeof v.via[0] === "string" ? v.via[0] : v.via[0].title;
  return `V-${String(i + 1).padStart(2, "0")} | npm audit | ${v.severity} | ${v.name}${v.isDirect ? "" : " (indirect)"} | ${title} | ${fix}`;
});

console.log(levels.map(l => `${l} ${counts[l]}`).join(" | "));
console.log("ID | tool | severity | affected package | finding | proposed fix");
rows.forEach(r => console.log(r));
process.exitCode = counts.critical + counts.high > 0 ? 1 : 0;
console.log(process.exitCode ? "Gate: FAIL (high or critical found)" : "Gate: PASS");'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node audit_report.js sample_audit.json
# With real data:  !npm audit --json > audit.json; node audit_report.js audit.json

# ===== Option B: VS Code =====
# node audit_report.js sample_audit.json'''),
    ("md", "## 5. Express: routes, controllers and CRUD (Session 2)\nThe app is split into `src/app.js` (middleware "
           "and routers), `src/routes`, `src/controllers` and an async `src/store.js` that simulates a database."),
    ("code", '''import os
os.makedirs("src/routes", exist_ok=True)
os.makedirs("src/controllers", exist_ok=True)
os.makedirs("tests", exist_ok=True)
print("Folders ready:", sorted(os.listdir("src")))'''),
    ("code", '''%%writefile src/store.js
// Async in-memory store: every function returns a promise, like a real database driver.
const wait = (ms) => new Promise(r => setTimeout(r, ms));
let tasks = [];
let nextId = 1;

module.exports = {
  async list(filter = {}) {
    await wait(5);
    if (filter.simulate === "down") throw new Error("database unavailable");
    return filter.done === undefined ? tasks : tasks.filter(t => String(t.done) === filter.done);
  },
  async get(id) { await wait(5); return tasks.find(t => t.id === Number(id)); },
  async create(title) { await wait(5); const t = { id: nextId++, title, done: false }; tasks.push(t); return t; },
  async update(id, data) {
    const t = await this.get(id);
    if (t) Object.assign(t, { title: data.title ?? t.title, done: data.done ?? t.done });
    return t;
  },
  async remove(id) {
    const t = await this.get(id);
    if (t) tasks = tasks.filter(x => x !== t);
    return Boolean(t);
  },
};'''),
    ("code", '''%%writefile src/controllers/tasks.js
const store = require("../store");

exports.list = async (req, res) => res.json(await store.list(req.query));

exports.getOne = async (req, res) => {
  const task = await store.get(req.params.id);
  if (!task) return res.status(404).json({ error: "Task not found" });
  res.json(task);
};

exports.create = async (req, res) => {
  const { title } = req.body ?? {};
  if (!title || typeof title !== "string" || title.length > 100) {
    return res.status(400).json({ error: "title is required (1 to 100 characters)" });
  }
  res.status(201).json(await store.create(title));
};

exports.update = async (req, res) => {
  const task = await store.update(req.params.id, req.body ?? {});
  if (!task) return res.status(404).json({ error: "Task not found" });
  res.json(task);
};

exports.remove = async (req, res) => {
  if (!(await store.remove(req.params.id))) return res.status(404).json({ error: "Task not found" });
  res.status(204).end();
};'''),
    ("code", '''%%writefile src/routes/tasks.js
const router = require("express").Router();
const c = require("../controllers/tasks");

router.get("/", c.list);
router.get("/:id", c.getOne);
router.post("/", c.create);
router.put("/:id", c.update);
router.delete("/:id", c.remove);

module.exports = router;'''),
    ("code", '''%%writefile src/app.js
const express = require("express");
const app = express();
app.use(express.json());

// Logging middleware: method, path, status, time
app.use((req, res, next) => {
  const start = Date.now();
  res.on("finish", () => console.log(`  ${req.method} ${req.originalUrl} ${res.statusCode} ${Date.now() - start}ms`));
  next();
});

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.use("/tasks", require("./routes/tasks"));

// Catch-all 404 for unknown routes
app.use((req, res) => res.status(404).json({ error: "Route not found" }));

// Error middleware (four arguments). Express 5 sends rejected promises from async routes here.
app.use((err, req, res, next) => {
  console.error("  error:", err.message);
  res.status(500).json({ error: "Something went wrong" });
});

module.exports = app;'''),
    ("code", '''%%writefile src/server.js
const app = require("./app");
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Tasks API on http://localhost:${PORT}`));'''),
    ("md", "## 6. Test the API from a script (Session 3)\nThe test starts the app on a free port, calls every endpoint "
           "with `fetch`, checks the status codes, and stops the server. It needs Express installed (section 3)."),
    ("code", '''%%writefile tests/api_test.js
const app = require("../src/app");

async function run() {
  const server = app.listen(0);
  const base = `http://127.0.0.1:${server.address().port}`;
  const call = async (method, path, body) => {
    const res = await fetch(base + path, { method, headers: { "Content-Type": "application/json" },
                                           body: body ? JSON.stringify(body) : undefined });
    return { status: res.status, body: res.status === 204 ? null : await res.json() };
  };
  const checks = [
    ["POST /tasks", await call("POST", "/tasks", { title: "Learn Express" }), 201],
    ["POST /tasks without title", await call("POST", "/tasks", {}), 400],
    ["GET /tasks", await call("GET", "/tasks"), 200],
    ["PUT /tasks/1", await call("PUT", "/tasks/1", { done: true }), 200],
    ["GET /tasks?done=true", await call("GET", "/tasks?done=true"), 200],
    ["GET /tasks/999", await call("GET", "/tasks/999"), 404],
    ["GET /tasks?simulate=down", await call("GET", "/tasks?simulate=down"), 500],
    ["DELETE /tasks/1", await call("DELETE", "/tasks/1"), 204],
    ["GET /nope", await call("GET", "/nope"), 404],
  ];
  let passed = 0;
  for (const [name, r, expected] of checks) {
    const ok = r.status === expected;
    passed += ok;
    console.log(`${ok ? "PASS" : "FAIL"} ${name} -> ${r.status}${r.body ? " " + JSON.stringify(r.body) : ""}`);
  }
  console.log(`${passed}/${checks.length} checks passed`);
  server.close();
}
run();'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node tests/api_test.js

# ===== Option B: VS Code =====
# npm test
# To run the server for Postman:  npm run dev   (then use http://localhost:3000)''', ["skip-offline-check"]),
    ("md", "### TODO 1: Add `GET /tasks/stats` returning total, done and pending counts. Register it **before** "
           "`/:id` in the router so it matches first, then add a check for it in `tests/api_test.js`."),
    ("code", "# TODO: write your code here"),
    ("md", "## 7. A ready-made Postman collection\nThis cell writes `tasks_api.postman_collection.json`. In Postman: "
           "**Import**, choose the file, then set the collection variable `baseUrl` to `http://localhost:3000`."),
    ("code", '''import json

def req(name, method, path, body=None, status=200):
    item = {"name": name, "request": {"method": method,
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "url": {"raw": "{{baseUrl}}" + path, "host": ["{{baseUrl}}"],
                    "path": [p for p in path.split("?")[0].split("/") if p]}},
            "event": [{"listen": "test", "script": {"type": "text/javascript",
                       "exec": [f'pm.test("status is {status}", () => pm.response.to.have.status({status}));']}}]}
    if body is not None:
        item["request"]["body"] = {"mode": "raw", "raw": json.dumps(body, indent=2)}
    return item

collection = {
    "info": {"name": "Day 9 Tasks API", "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"},
    "variable": [{"key": "baseUrl", "value": "http://localhost:3000"}],
    "item": [
        req("Health", "GET", "/health"),
        req("Create task", "POST", "/tasks", {"title": "Learn Express"}, 201),
        req("Create task without title", "POST", "/tasks", {}, 400),
        req("List tasks", "GET", "/tasks"),
        req("Get task 1", "GET", "/tasks/1"),
        req("Update task 1", "PUT", "/tasks/1", {"done": True}),
        req("Delete task 1", "DELETE", "/tasks/1", status=204),
        req("Get missing task", "GET", "/tasks/999", status=404),
    ],
}
with open("tasks_api.postman_collection.json", "w") as f:
    json.dump(collection, f, indent=2)
print("Saved with", len(collection["item"]), "requests")

# ===== Option A: Google Colab, download the file (uncomment to use) =====
# from google.colab import files
# files.download("tasks_api.postman_collection.json")

# ===== Option B: VS Code =====
# The file is already in your project folder.'''),
    ("md", "## 8. SmartDesk step 8: notification service\nA small Express service that records ticket notifications. "
           "Sending is simulated: it logs the message instead of calling an SMS or email provider. Any provider key "
           "would come from `process.env`, never from the code."),
    ("code", '''%%writefile notify_app.js
const express = require("express");
const app = express();
app.use(express.json());

const CHANNELS = ["email", "sms", "push"];
const sent = [];

app.get("/health", (req, res) => res.json({ status: "ok", service: "smartdesk-notify" }));

app.post("/notifications", async (req, res) => {
  const { ticketId, channel, message } = req.body ?? {};
  const errors = [];
  if (!Number.isInteger(ticketId)) errors.push("ticketId must be an integer");
  if (!CHANNELS.includes(channel)) errors.push(`channel must be one of ${CHANNELS.join(", ")}`);
  if (!message || message.length > 300) errors.push("message is required (max 300 characters)");
  if (errors.length) return res.status(400).json({ errors });
  const item = { id: sent.length + 1, ticketId, channel, message, sentAt: new Date().toISOString() };
  sent.push(item);                               // simulated send
  res.status(201).json(item);
});

app.get("/notifications", (req, res) => {
  const { ticketId } = req.query;
  res.json(ticketId ? sent.filter(n => n.ticketId === Number(ticketId)) : sent);
});

app.use((req, res) => res.status(404).json({ error: "Route not found" }));
app.use((err, req, res, next) => res.status(500).json({ error: "Something went wrong" }));
module.exports = app;

if (require.main === module) {
  const PORT = process.env.PORT || 4000;
  app.listen(PORT, () => console.log(`SmartDesk notify service on http://localhost:${PORT}`));
}'''),
    ("code", '''%%writefile notify_test.js
const app = require("./notify_app");
const server = app.listen(0, async () => {
  const base = `http://127.0.0.1:${server.address().port}`;
  const post = (body) => fetch(base + "/notifications", { method: "POST",
    headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
  let r = await post({ ticketId: 101, channel: "sms", message: "Your ticket T-101 is now in progress." });
  console.log(r.status, await r.json());
  r = await post({ ticketId: "x", channel: "fax" });
  console.log(r.status, await r.json());
  r = await fetch(base + "/notifications?ticketId=101");
  console.log(r.status, (await r.json()).length, "notification(s) for ticket 101");
  server.close();
});'''),
    ("code", '''# ===== Option A: Google Colab (active) =====
!node notify_test.js

# ===== Option B: VS Code =====
# node notify_test.js
# node notify_app.js   (then test with Postman on http://localhost:4000)''', ["skip-offline-check"]),
    ("md", "**TODO (SmartDesk step 8):** generate a Postman collection for the notification service with the "
           "`req()` helper above (health, valid post, invalid post, list by ticket), and run `npm audit` on the "
           "project."),
    ("md", "## 9. Check yourself\n1. Which file pins exact versions, and which file holds ranges?\n"
           "2. Why does the router register `/stats` before `/:id`?\n"
           "3. What did the error middleware return for `?simulate=down`, and why did the server keep running?"),
], sign_off="Ganbatte (頑張って): *Do your best*")
