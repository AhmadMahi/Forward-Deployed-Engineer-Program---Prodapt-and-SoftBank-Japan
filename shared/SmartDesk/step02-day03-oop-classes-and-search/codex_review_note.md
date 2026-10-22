# Codex review note (step 02)

- **Prompt:** "Add a search(text, status, priority) method to TicketStore. Case-insensitive match on customer and body. Add pytest tests."
- **Model:** approved default model (see docs/MODEL_GUIDE.md), reasoning effort low.
- **Tokens used:** record the number from your Codex usage view here (for example: 3,200 input, 600 output).
- **What I changed after review:** Codex first matched only the body. I asked it to include the customer name and to strip spaces.
- **Security check:** no secrets, no file writes, no new dependencies.
