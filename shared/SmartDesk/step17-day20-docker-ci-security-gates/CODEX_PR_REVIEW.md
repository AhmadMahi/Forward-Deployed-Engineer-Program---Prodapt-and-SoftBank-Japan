# AI pull request review with Codex, human approval (NEW v4)

1. Open the PR diff in VS Code and ask Codex: "Review this diff for bugs, security issues and missing tests. List findings with file and line."
2. Treat Codex findings as suggestions. Check each one yourself.
3. A human reviewer must approve before merge. Branch policy: one approval, all gates green.
4. Never paste secrets, customer data or full logs into the review prompt.
