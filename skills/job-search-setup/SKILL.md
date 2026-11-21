---
name: job-search-setup
description: Walks a beginner through setting up an AI-assisted job search with Claude, one step at a time - accounts, Claude Code, connectors, safe environments and keys, skills, a .dev domain and website on Cloudflare, a Calendly booking page, an ATS-safe resume, a public proof project, Simplify autofill, and LinkedIn updates through Claude in Chrome - and keeps a checklist. Use when the user says "help me set up my job search", "walk me through the AI job search setup", "what's the next setup step", or asks to repeat Artur's setup.
---

# Job search setup

Guide the user through the steps in this repo's `prompts/` folder (01 to 12, plus the optional 13, 15 and 16). Step 14 is a one-shot install for a new Mac; offer it when the user is setting up a fresh laptop. Steps 15 (memory with claude-mem) and 16 (Remote Control and long runs) set up the Mac itself; offer them after step 04, and run them only in Claude Code on the user's Mac. In a cloud session, skip them when choosing the next step and remind the user to do them later on the Mac. The user is usually a beginner on a Mac, so explain plainly and do one step at a time.

## How to run a step

1. Read the matching file in `prompts/` (for example `prompts/06-domain-and-website.md`).
2. Tell the user in two sentences what the step gives them and what it costs.
3. Split the step into:
   - **Their part:** sign-ups, payments, browser clicks, anything on their own computer. Give numbered steps and wait for "done".
   - **Your part:** everything you can do with the connectors and tools in this session. Do it, then show the result.
4. Check the step really worked (for example: open the live URL, list the Calendly event, run the resume check).
5. Tick it off in `SETUP-CHECKLIST.md` in the user's job-search repo and commit.

## Checklist file

Create `SETUP-CHECKLIST.md` on first use if it doesn't exist:

```markdown
# Job search setup checklist
- [ ] 01 Accounts and Claude app
- [ ] 02 Connectors
- [ ] 03 Environments and keys
- [ ] 04 Skills and plugins
- [ ] 05 Knowledge graph (optional)
- [ ] 06 Domain and website
- [ ] 07 Booking page
- [ ] 08 ATS-safe resume
- [ ] 09 Proof project
- [ ] 10 Applications with Simplify
- [ ] 11 LinkedIn with Claude in Chrome
- [ ] 12 Weekly routine
- [ ] 13 Outreach with Sellbird (optional)
- [ ] 15 Memory between sessions with claude-mem (on the Mac only, optional)
- [ ] 16 Remote Control and long runs (on the Mac only, optional)
```

On "what's next?", read the checklist and continue with the first unticked step that can run here (skip 15 and 16 in a cloud session).

## Rules

- Plugins: recommend one coding method (superpowers) plus non-overlapping helpers, as in SKILLS.md "My current set". Don't install ECC, mattpocock-skills, andrej-karpathy-skills or tdd@glebis-skills alongside superpowers; explain the overlap instead.
- Never ask the user to paste a password, API key or token into chat. Keys go through the environment's secure credential form.
- Don't write the user's email address or phone number into files or web requests unless they type it in the same message.
- Don't send email, submit applications, buy anything or publish anything without the user's explicit OK for that action.
- claude-mem: never run the plain `npx claude-mem install`, which pre-selects a paid plan with a card-required trial. Use `--provider claude` with `CLAUDE_MEM_ONLINE_OPTIN=false` as in prompts/15, and let the user run it.
- Cloud sessions can't reach the user's browser or local files. Steps that need them (Claude in Chrome, LinkedIn) run on the user's Mac.
- Prices change. Say the price is approximate and point to the official pricing page.
- Never invent results or resume claims. Ask the user for numbers; if they can't back a claim, suggest softening it.
