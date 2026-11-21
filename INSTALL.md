# Install AI co-pilot setup on your Mac

One prompt sets everything up. Claude does the installs. You do the sign-ins and clicks, so it never needs your passwords or keys.

## Before you start (5 minutes, your part)

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

CORE
1. Xcode Command Line Tools (xcode-select --install), Homebrew (brew.sh), then
   brew install git gh node python@3.13 pipx
2. The kit's four skills (setup walkthrough, resume builder, ATS check, proof project):
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
- A table: item | version | installed / already there / skipped / failed.
- "Your part", numbered: gh auth login; connectors in the Claude app (prompts/02);
  Claude in Chrome (prompts/11); Simplify (prompts/10); built-in skills to switch on.
- Save this as SETUP-REPORT.md in my home folder.
- Then ask if I want to start the job-search walkthrough (prompts/00).
```

It's safe to run twice. Anything already installed is skipped.

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
