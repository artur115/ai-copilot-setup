# 14 · New laptop: install everything at once

Moving to a new Mac, or starting fresh? Paste this into **Claude Code on the new Mac** (the
desktop app's Code tab, or `claude` in Terminal). It installs the tools, skills and plugins from
this guide in one pass, checks each one, and ends with a short list of the steps only you can do
(sign-ins, connectors, browser extensions). It's safe to run twice: anything already installed is
skipped.

```text
Set up this Mac with my AI co-pilot setup in one pass, using
https://github.com/artur115/ai-copilot-setup (read README.md, SKILLS.md and prompts/01-16 first).

RULES
- First show me the plan: every item below, approximate download size, and free disk space
  (df -h ~). Wait for my "go".
- Never ask me to paste a password, API key or token into chat. I sign in in the browser or the
  Claude app; keys go into .env files or the environment's credential form.
- Install nothing paid and sign up for nothing.
- Ask before each OPTIONAL item; install the CORE items after my "go".
- Check every install with a version or list command. At the end show a table:
  item | version | installed / already there / skipped / failed.
- If something fails: one line on why, skip it, continue.
- The /plugin lines are slash commands. Run each one in Terminal as `claude plugin ...` (for
  example `claude plugin marketplace add artur115/ai-copilot-setup`) if this Claude Code has
  that command; otherwise give me the exact lines to type into Claude Code myself.

CORE: TOOLS
1. Xcode Command Line Tools: xcode-select --install
2. Homebrew (brew.sh). Then: brew install git gh node python@3.13 pipx
3. Claude Code CLI with the official installer from the Claude Code docs.

CORE: SKILLS AND PLUGINS (in Claude Code)
4. My job-search kit (setup walkthrough, resume builder, ATS check, proof project):
     /plugin marketplace add artur115/ai-copilot-setup
     /plugin install job-search-kit@ai-copilot-setup
5. graphify, the knowledge graph (prompts/05):
     pipx install graphifyy && graphify install
6. Playwright's Chromium, used by the resume builder to print the PDF:
     npx playwright install chromium   (inside my resume repo, once it's cloned)
7. My repos into ~/Documents: ask me for the list (website, resume, proof projects).

RECOMMENDED: ASK ME FIRST
7a. Memory between sessions with claude-mem: follow prompts/15 exactly (audit, then I run
    `CLAUDE_MEM_ONLINE_OPTIN=false npx claude-mem install --provider claude` myself; no
    account, no trial; telemetry off; two-session memory test).
7b. Remote Control and long runs: walk me through prompts/16.

OPTIONAL: THE CODING SET (ask once; these don't overlap, see SKILLS.md)
8.  superpowers (the one coding method: brainstorm → plan → test-driven build → review):
      /plugin install superpowers@claude-plugins-official
9.  ponytail (keeps generated code short):
      /plugin marketplace add DietrichGebert/ponytail
      /plugin install ponytail@ponytail
10. addyosmani/agent-skills (/spec, /plan, /build, /test, /review, /ship; run only when typed):
      /plugin marketplace add addyosmani/agent-skills
      /plugin install agent-skills@addy-agent-skills
11. expo (React Native apps):
      /plugin install expo@claude-plugins-official
12. Project-only skills from glebis/claude-skills, inside that project's folder:
      npx skills add glebis/claude-skills --skill feature-factory   (and app-map, app-release)
13. Do NOT also install ECC, mattpocock-skills, andrej-karpathy-skills or tdd@glebis-skills:
    they overlap with superpowers (SKILLS.md, "Why I don't stack coding-style plugins").
    If any are already installed, offer the clean-up commands from SKILLS.md.
14. Sellbird for outreach (prompts/13): only clone and install, approval mode, no mailbox.

THEN GIVE ME
- The table.
- "Your part", numbered: claude login (Pro/Max); gh auth login; the Claude app's connectors
  (GitHub, Gmail, Google Calendar, Google Drive, Calendly: prompts/02); the Claude in Chrome
  extension (prompts/11); the Simplify extension (prompts/10); turning on the built-in skills I
  use in the Claude app's settings (docs, xlsx, pptx, pdf, google-workspace, deep-research,
  skill-creator); and anything that failed.
- Moving from an old Mac? List what git doesn't carry and how to copy it safely (AirDrop or an
  encrypted disk, never email or chat): every .env file in my repos, Sellbird's .env,
  sellbird.local.yaml and data/ folder (its do-not-email list must not be lost), and my
  SETUP-CHECKLIST.md if it isn't committed. Plugins live per Mac, so they're reinstalled above,
  not copied.
```
