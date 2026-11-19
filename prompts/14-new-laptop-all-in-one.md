# 14 · New laptop: install everything at once

Moving to a new Mac, or starting fresh? Paste this into **Claude Code on the new Mac** (the
desktop app's Code tab, or `claude` in Terminal). It installs the tools from steps 01 to 13 in
one pass, checks each one, and leaves the steps only you can do (sign-ins, payments) as a short
list at the end. It's safe to run twice: anything already installed is skipped.

```text
Set up this Mac for my AI job search in one pass, using the guide at
https://github.com/artur115/ai-job-search-setup (read README.md, SKILLS.md and prompts/01-13 first).

RULES
- Show me the full list of what you'll install, with approximate sizes, before installing anything,
  and wait for my "go".
- Never ask me to paste a password, API key or token into chat. Sign-ins happen in the browser or
  the app; keys go in a .env file or the environment's credential form.
- Install nothing paid. Anything that costs money (domain, Workspace, Calendly paid tier): list it
  for me instead.
- Check each install with a version command and show me the results as a table at the end.
- If something fails, stop on that item, tell me why in one line, and continue with the rest.

INSTALL (skip anything already present)
1. Xcode Command Line Tools (xcode-select --install), then Homebrew (from brew.sh).
2. With Homebrew: git, gh, node (LTS), python@3.13, ffmpeg. Also the Docker Desktop app only if
   I say I'll run Sellbird with Docker or other local services.
3. Claude Code CLI (official installer from the Claude Code docs), then remind me to run
   `claude login` with my Pro/Max account.
4. Clone my repos into ~/Documents (ask me for the list; mine are my website, resume and proof
   projects).
5. Skills and plugins from SKILLS.md: the job-search kit
   (/plugin marketplace add artur115/ai-job-search-setup, then
   /plugin install job-search-kit@ai-job-search-setup) and the others it lists for the Mac.
6. graphify (prompts/05), if I want the knowledge graph.
7. Playwright's Chromium for the resume builder (npx playwright install chromium in the resume
   repo).
8. Optional, only if I say yes: Sellbird (prompts/13) in ~/Documents/sellbird with python3.13,
   in approval mode, with no mailbox connected.

THEN GIVE ME
- A table: tool, version, status (installed / already there / failed).
- "Your part" as a numbered list: claude login, gh auth login, Google/GitHub/Calendly sign-ins
  in the Claude app's connectors (prompts/02), Claude in Chrome extension (prompts/11), Simplify
  extension (prompts/10), and anything that failed.
- If I'm moving from an old Mac: a list of what to copy over that git doesn't carry (every .env
  file, Sellbird's data/ folder and sellbird.local.yaml, browser sign-ins), and how to copy it
  safely (AirDrop or an encrypted disk, never email or chat).
```
