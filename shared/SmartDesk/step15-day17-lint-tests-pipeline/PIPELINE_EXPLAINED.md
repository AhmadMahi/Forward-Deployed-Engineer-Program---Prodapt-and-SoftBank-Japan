# What each pipeline stage does

1. **Trigger:** runs on pushes and pull requests to `main`.
2. **Install tools:** a clean agent installs only what the job needs.
3. **Lint (ruff):** style and common bugs. The `S` rules flag risky code early.
4. **SAST (bandit):** scans the code for security issues such as hard-coded secrets. Part of DevSecOps (NEW v4).
5. **Unit tests:** pytest must pass. Results are published even when the job fails.

Dependency scanning (pip-audit) and secret scanning join in step 17 (Day 20).
