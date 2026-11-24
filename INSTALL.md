# Install AI co-pilot setup on your Mac

One prompt sets everything up. Claude does the installs. You do the sign-ins and clicks, so it never needs your passwords or keys.

## Before you start (5 minutes, your part)

0. **Check which Mac you have.** Apple menu > **About This Mac**. "Chip: Apple M1" (M2, M3 and so on) means an **Apple-chip Mac**. "Processor: ... Intel" means an **Intel Mac**. Also note the **macOS** version: Claude Code needs **macOS 13 Ventura or newer**. Both kinds of Mac work; the install prompt checks this again and picks the right path (see [Intel Macs](#intel-macs) below).
1. Get **Claude Pro** or Max at [claude.com/pricing](https://claude.com/pricing). Claude Code is included.
2. Install the Mac app from [claude.com/download](https://claude.com/download), drag it to Applications and sign in.
3. Open **Terminal** and install Claude Code with the official installer from the [Claude Code docs](https://code.claude.com/docs). Then run `claude` once and sign in.

## The install prompt

Open Terminal, go to your home folder (`cd ~`), run `claude`, and paste this:

```text
Install the AI co-pilot setup from https://github.com/artur115/ai-copilot-setup on this Mac.
Read its README.md, INSTALL.md, SKILLS.md and prompts/ (01-16) first.

RULES
- Plan first: show every item below, approximate download size, and free disk space
  (df -h ~). Wait for my "go".
- Never ask me to paste a password, API key or token into chat. I sign in in the browser
  or the Claude app. Keys go into .env files or an environment's credential form.
- Install nothing paid and sign up for nothing. If any installer asks for a card, a trial
  or an account, stop and show me what it says.
- Install CORE items after my "go". Ask before each OPTIONAL item.
- Check each install with a version or list command. If something fails: one line on why,
  skip it, keep going.
- /plugin lines are Claude Code slash commands. Run them as `claude plugin ...` in Terminal
  if that works here; otherwise give me the exact lines to type myself.

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

CORE
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
2. The kit's six skills (setup walkthrough, resume builder, ATS check, proof project, job autopilot setup and run):
     /plugin marketplace add artur115/ai-copilot-setup
     /plugin install job-search-kit@ai-copilot-setup
3. graphify, the code map (prompts/05): pipx install graphifyy && graphify install

RECOMMENDED (ask me first)
4. Memory between sessions with claude-mem. Follow prompts/15 exactly: audit, then give me
   the command to run myself with --provider claude and CLAUDE_MEM_ONLINE_OPTIN=false, then
   verify, turn telemetry off, and run the two-session memory test.
5. Remote Control and long runs: walk me through prompts/16 (desktop app setting,
   spawn mode same-dir, caffeinate, the Battery setting, permission modes).

CODING SET (ask once for the whole set; these don't overlap)
6. superpowers (the one coding method), ponytail (short code), agent-skills (/review and
   other commands I type), expo (React Native apps). Install commands are in SKILLS.md.
   Project-only skills from glebis/claude-skills (feature-factory, app-map, app-release) go
   into a project's .claude/skills with npx skills add, only when I start that project.

DO NOT STACK (read SKILLS.md "Why I don't stack coding-style plugins")
7. ECC, mattpocock-skills, andrej-karpathy-skills and the glebis tdd plugin overlap with
   superpowers. Don't install them alongside it. If I ask for one, explain the overlap and
   offer it instead of superpowers, not in addition. If any are already installed, offer
   the clean-up commands from SKILLS.md "Clean up a stacked setup".

FINISH WITH
- A table: item | version | installed / already there / skipped / failed, with this
  Mac's chip, macOS version and the path used (A or B) on top.
- "Your part", numbered: gh auth login; connectors in the Claude app (prompts/02);
  Claude in Chrome (prompts/11); Simplify (prompts/10); built-in skills to switch on.
- Save this as SETUP-REPORT.md in my home folder.
- Then ask if I want to start the job-search walkthrough (prompts/00).
```

It's safe to run twice. Anything already installed is skipped.

## Intel Macs

Some MacBooks have an **Intel** processor instead of an Apple chip (most Macs sold before 2021). The install prompt checks this first and changes one thing: **on an Intel Mac it skips Homebrew** and installs Node.js, Python, pipx and the GitHub CLI from their official installers.

Why: Homebrew still runs on Intel Macs with macOS 11 to 26, but only with "Tier 3" support. It no longer ships prebuilt packages for Intel, so installs compile from source (slow, and some fail), and Homebrew plans to end Intel support around September 2027. It doesn't run at all on macOS 10.15 or older. Sources: [Homebrew support tiers](https://docs.brew.sh/Support-Tiers), [Homebrew 5.0.0](https://brew.sh/2025/11/12/homebrew-5.0.0).

| | Apple-chip Mac | Intel Mac |
|---|---|---|
| Claude Code | Yes, macOS 13+ | Yes, macOS 13+ |
| Homebrew | Yes, in `/opt/homebrew` | Not used: official installers instead |
| Node.js, Python, pipx, gh | `brew install ...` | `.pkg` installers from nodejs.org, python.org, cli.github.com; pipx with pip |
| Everything else (kit, plugins, graphify, claude-mem) | Same | Same |

On macOS 12 or older, Claude Code doesn't install. Update macOS if Software Update offers it; otherwise use Claude in the browser (claude.ai, and cloud sessions at claude.ai/code), which needs nothing installed.

If an Apple-chip Mac reports `x86_64`, Terminal is running under Rosetta: quit it, untick "Open using Rosetta" in Terminal's Get Info window, and reopen it before installing anything.

## Already installed the old `ai-job-search-setup` kit?

The repo was renamed to `ai-copilot-setup`. In Claude Code, run:

```
/plugin marketplace remove ai-job-search-setup
/plugin marketplace add artur115/ai-copilot-setup
/plugin install job-search-kit@ai-copilot-setup
```

## After install: what to say to Claude

| You want to | Say |
|---|---|
| Start the job-search setup | "help me set up my job search" |
| Continue where you left off | "what's the next setup step?" |
| Build or update your resume | "build my resume", then "check my resume PDF for ATS problems" |
| Prove a resume claim | "build a proof project for this resume line: …" |
| Recall past work (claude-mem) | "what did we decide about … last week?" |
| Plan your week | paste prompts/12 on Monday |
