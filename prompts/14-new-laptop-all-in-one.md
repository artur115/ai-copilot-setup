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
  item | version | installed / already there / skipped / failed, with the chip, macOS
  version and path (A or B) on top.
- If something fails: one line on why, skip it, continue.
- The /plugin lines are slash commands. Run each one in Terminal as `claude plugin ...` (for
  example `claude plugin marketplace add artur115/ai-copilot-setup`) if this Claude Code has
  that command; otherwise give me the exact lines to type into Claude Code myself.

0. CHECK THIS MAC FIRST, changing nothing. Run these and show me a table
   (chip, macOS version, memory, free disk, Rosetta):
     uname -m                                  # arm64 = Apple chip, x86_64 = Intel
     sysctl -n machdep.cpu.brand_string        # "Apple M..." or "Intel(R) Core(TM) ..."
     sysctl -n sysctl.proc_translated          # 1 = Terminal runs under Rosetta; missing/0 = no
     sw_vers -productVersion
     sysctl -n hw.memsize
     df -h ~
   Then pick the path, and say which one in one line:
   - macOS older than 13: stop. Claude Code needs macOS 13 Ventura or newer. Tell me to check
     System Settings > General > Software Update. If this Mac can't update, I use Claude in
     the browser (claude.ai and claude.ai/code) instead of installing anything locally.
   - proc_translated is 1 (an Apple-chip Mac with Terminal running under Rosetta): stop.
     Tell me to quit Terminal, untick "Open using Rosetta" in Terminal's Get Info window,
     reopen it and run the check again. Otherwise Homebrew lands in the wrong place.
   - arm64: PATH A (Apple chip). x86_64 with an Intel CPU: PATH B (Intel Mac).

CORE: TOOLS
1. Xcode Command Line Tools (xcode-select --install; gives git), then:
   PATH A, Apple chip: Homebrew from brew.sh (it installs to /opt/homebrew; add the shellenv
     line it prints to ~/.zprofile), then: brew install git gh node python@3.13 pipx
   PATH B, Intel Mac: skip Homebrew. Homebrew gives Intel Macs only Tier 3 support: no
     prebuilt packages, so installs compile from source, take long and can fail, and Intel
     support ends around September 2027. Use the official installers instead. Give me each
     link, wait while I open the .pkg, then check it:
       - Node.js LTS, "macOS Installer (.pkg)" from nodejs.org          -> node -v
       - Python 3.13, "macOS 64-bit universal2 installer" from python.org -> python3.13 --version
       - pipx: python3.13 -m pip install --user pipx && python3.13 -m pipx ensurepath,
         then open a new Terminal tab                                    -> pipx --version
       - GitHub CLI, the macOS installer from cli.github.com             -> gh --version
     If I insist on Homebrew anyway, warn me about the above first (on Intel it installs
     to /usr/local).
2. Check the tools: git --version, node -v, python3.13 --version, pipx --version, gh --version.
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
