# Day 23: App Build Prompts

**App of the day (NEW (v4)):** Patch and Modernise: scan, patch with Codex, prove with tests and modernise the TelcoDesk Legacy starter repo. Assignment due **Day 25, 09:30**.

Prepared by **Ahmed** | [linkedin.com/in/ahmed-al-imaad](https://www.linkedin.com/in/ahmed-al-imaad)

---

## How to use these prompts

1. Open the starter repo (`shared/PatchAndModernise_Starter/`, copied into your own branch) in VS Code and open the OpenAI Codex panel (signed in with the program API key, approved model only).
2. Copy one prompt at a time into Codex. Ask Codex to show a plan first for anything with more than one file.
3. Read every diff before you accept it. If something is unclear, ask Codex to explain it before moving on.
4. Run the tests after every step. Do not move to the next prompt until the current version runs without errors.
5. Never paste API keys, customer data or credentials into a prompt. Check your daily token usage.

> Uses Days 1 to 23. You act as an FDE offering Patching as a Service and Code Modernisation as a Service to a telecom customer. The model proposes; you decide. Every fix needs a test.

**Before you start:** run `python -m pytest -q`. All 14 tests must pass. Save the output as your "before" evidence.

---

## Prompt 1: Explain the codebase (read-only)

```text
Work in read-only mode. Do not change any file.
Read this repository and explain it to me as a new engineer:
1. What each module in ticketing/ and notifier/ does, in one line each.
2. How data flows from the legacy CSV file into the database.
3. Any code that looks risky or outdated, with file and line. Do not fix anything yet.
Keep the answer under 300 words.
```

## Prompt 2: Triage the scan results

```text
I ran bandit, pip-audit and npm audit on this repository. The raw output is pasted below.
For each finding, give: ID, finding, tool, severity (critical, high, medium, low), affected file,
whether it is reachable from user input, and a proposed fix in one sentence.
Return a Markdown table using the columns of shared/templates/Vulnerability_Report_Template.md.
Do not change any code.

<paste the scanner output here, with nothing secret in it>
```

## Prompt 3: Patch one finding, test first

```text
Fix finding <ID> only. Follow these steps and stop after each one to show me the diff:
1. Write a pytest test that fails today because of the vulnerability.
2. Run it and show me that it fails.
3. Make the smallest code change that fixes it.
4. Run the full test suite and show me that everything passes.
Do not touch tests/test_legacy_import.py. Do not change unrelated code.
```

Repeat Prompt 3 for each finding. For the dependency upgrade, add: "Read the library's changelog for breaking changes and update our code where the API changed."

## Prompt 4: Remove the hard-coded secret

```text
Move the signing secret out of ticketing/auth.py.
- Read it from the TELCODESK_SECRET environment variable.
- In tests, set it with monkeypatch. Never write a real secret in a file.
- If the variable is missing, raise a clear error at startup.
- Also reduce the token lifetime to 15 minutes and add a test that an expired token is rejected.
```

## Prompt 5: Modernise the legacy importer in small steps

```text
Modernise ticketing/legacy_csv_import.py in small steps. The characterisation tests in
tests/test_legacy_import.py must stay green after every step. Show me a plan first, then do one step at a time:
1. Use the csv module with delimiter=";" instead of manual split.
2. Use timezone-aware UTC dates instead of datetime.utcnow().
3. Remove the module-level imported_count global (return a count instead).
4. Use a context manager to open the file.
After each step run the full test suite and stop for my review.
If a characterisation test fails, undo the step. Do not edit the test.
```

## Prompt 6 (stretch): A FastAPI upload endpoint

```text
Add a small FastAPI app with POST /imports that accepts a CSV upload and uses the modernised parse function.
Return the number of imported tickets and a list of skipped lines with reasons.
Limit uploads to 1 MB. Add TestClient tests. Keep the CLI working.
```

## Prompt 7: Draft the service note

```text
Using our vulnerability report and the commits on this branch, draft a one-page note for a telecom customer:
1. What we found and how we rated it.
2. How we patched and proved each fix.
3. How we modernised the importer safely.
4. Risks that remain.
5. What a monthly Patching and Modernisation service would include (scope, cadence, approvals, reporting).
Plain English, no hype, no promises of outcomes. Mark anything that is an estimate.
```

Edit the draft yourself. You are the author.

---

## SmartDesk step 20: Patch, modernise and place on the maturity ladder

```text
SmartDesk step 20. Apply the same method to SmartDesk:
1. Run bandit, pip-audit and npm audit on SmartDesk. Add the findings to our vulnerability report.
2. Write characterisation tests for SmartDesk's legacy CSV import module (from step 13), then modernise it
   in small steps with the tests green after each step.
3. Create docs/maturity.md: place SmartDesk on the maturity ladder (experiment, pilot, production, scaled,
   agentic) and list the three gaps that block the next level.
4. Fill in shared/templates/OWASP_Agentic_Checklist.md for the SmartDesk assistant, including the agent
   permissions table with deny by default.
Show me the plan first, then the diff for each step.
```

**Review checklist before you commit:** every fix has a test that failed before and passes after; the characterisation tests are unchanged and green; no secret is in any file or prompt; scans re-run and recorded; you can explain every line Codex wrote; tokens used are noted.
