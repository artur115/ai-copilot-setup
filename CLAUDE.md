# ai-copilot-setup

## Keeping sessions cheap

Every turn re-reads the whole conversation, so long sessions get expensive.
- PR watching: after opening a PR, don't subscribe to its activity or schedule "Re-check PR" check-ins unless I ask for it in that conversation. Give me the link and stop.
- One task per session: when a task is finished (PR merged, question answered), tell me in one line to start a new session for the next topic, and offer a short handoff note to paste into it.
- If the session's context is past about 200K tokens, suggest `/compact` before starting new work.
- Send broad code or file searches to a subagent so only its summary lands here; don't paste long logs or whole files into the conversation.
