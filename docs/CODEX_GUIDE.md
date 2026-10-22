# OpenAI Codex Guide for Learners

OpenAI Codex is the AI coding tool for this program. You use it through the VS Code extension, signed in with the program's OpenAI API key. It is introduced on the afternoon of Day 3 and used from then on. Codex is not required on Days 1, 2, 4 and the FDE Mindset days.

A printable two-page version is in [shared/Codex_Setup_and_Dos_Donts.pdf](../shared/Codex_Setup_and_Dos_Donts.pdf).

## 1. Set up (Day 3)

1. Install VS Code, Git and Python 3.12 or newer (see [ACCESS_AND_INSTALL.md](ACCESS_AND_INSTALL.md)).
2. In VS Code, open Extensions and install the OpenAI Codex extension published by OpenAI.
3. Open the Codex panel and choose to sign in with an API key. Paste the program key into the sign-in prompt only. Never paste it into a file, a prompt or a chat.
4. Pick the approved default model (see [MODEL_GUIDE.md](MODEL_GUIDE.md)).
5. Set the sandbox to workspace-write with approvals. Use read-only when you only want to explore.
6. Open your project folder and add an `AGENTS.md` from the [learner template](../shared/templates/AGENTS_learner_template.md).

## 2. The structured workflow

| Step | What you do | What Codex does |
|---|---|---|
| Describe | State the goal, the files involved and how you will know it works. | Asks questions if the goal is unclear. |
| Plan | Ask for a plan first. Approve or edit it. | Proposes small steps. |
| Small steps | Approve one step at a time. | Edits a few files per step. |
| Test | Run the tests after every step. | Can write tests first if you ask. |
| Review | Read every diff. Accept only code you can explain. | Explains any line you ask about. |

**Vibe coding vs structured coding.** Vibe coding means accepting whatever the tool writes until it seems to work. It is fine for a throwaway prototype. In this program, and with customers, use structured coding: a clear goal, a plan, small steps, tests and a human review of every diff.

## 3. AGENTS.md basics

`AGENTS.md` is a plain Markdown file at the root of a repository. Codex reads it before it works. Put in it:

- how to build, test and lint (exact commands)
- code style rules
- folders not to touch
- security rules, for example "never put secrets in prompts or files"

Keep it short and keep it up to date. This repository has its own [AGENTS.md](../AGENTS.md).

## 4. Security of AI-generated code

- Treat Codex output as code from a new colleague: review it, test it, scan it.
- Run `bandit` (Python), `pip-audit` (Python dependencies) and `npm audit` (JavaScript dependencies). Log findings in the [vulnerability report template](../shared/templates/Vulnerability_Report_Template.md).
- Watch for hard-coded secrets, SQL or NoSQL injection, missing input validation, unpinned or unknown packages.
- Never run Codex in full-access or bypass mode on a laptop with real credentials.

## 5. Token cost and daily usage

- Every Codex request costs tokens: the files it reads, your prompt, its reasoning and its output.
- Small, focused tasks with only the relevant files are cheaper and give better results.
- Use the light model for routine edits and the default for feature work. Raise reasoning effort only when the default fails.
- Check your daily usage at the end of each day. Stop runaway tasks. Your trainer will share the per-learner budget.

## 6. Do's and don'ts

See the full list in [MODEL_GUIDE.md](MODEL_GUIDE.md#openai-codex-dos-and-donts).
