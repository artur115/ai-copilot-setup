# 15 · Memory between sessions (claude-mem)

Claude Code forgets everything when a session ends. [claude-mem](https://github.com/thedotmack/claude-mem) (open source, Apache-2.0) fixes that on your Mac. It records what Claude does in each session and saves short summaries in a local database. The next session in the same project folder starts with that context.

**What it costs:** the plugin is free. Its background note-taker uses your Claude plan (the small Haiku model), so long sessions use your plan's limits a little faster. It has a paid cloud option with a 30-day trial that asks for a card. The prompt below skips it.

**Where it runs:** on your Mac only. Cloud sessions don't have it.

Paste this into **Claude Code on your Mac**, from your home folder:

```text
Install claude-mem (github.com/thedotmack/claude-mem) on this Mac so Claude remembers my
work between sessions. Audit first, install second. I run the install command myself.

1. Check and show me a table, changing nothing: macOS version and chip, free disk (df -h ~),
   node --version (needs 20.19+ or 22.12+), claude --version, whether bun and uv exist,
   whether ~/.claude-mem exists, and whether anything is listening on ports 37700-37777
   (lsof -nP -iTCP -sTCP:LISTEN | grep 377). Read the claude-mem README and flag anything that
   differs from this prompt. Wait for my "go".
2. Give me this exact command to run myself. Do not run the plain `npx claude-mem install`:
   it pre-selects a paid plan and opens a trial checkout page.
     CLAUDE_MEM_ONLINE_OPTIN=false npx claude-mem install --provider claude
   `--provider claude` keeps memory local, runs on my own Claude plan, and needs no
   claude-mem account. If anything asks me to sign in, start a trial or enter a card, stop.
   Never use `npm install -g claude-mem`. It installs only the library, not the hooks.
3. After I restart Claude Code, verify and show me evidence:
   npx claude-mem status, npx claude-mem doctor (run `npx claude-mem repair` if it warns),
   the viewer URL it prints (usually http://localhost:37701), and that these settings are
   empty (print lengths only, never values): CLOUD_SYNC_TOKEN, PRO_MEMORY_KEY.
4. Turn off anonymous analytics: npx claude-mem telemetry disable, then show telemetry status.
5. Memory test: tell me to open my project folder, start `claude`, and save one fact
   (for example "test phrase violet-otter-42"). Then /exit, start a new session in the same
   folder and ask for it. It must answer without me re-explaining.
6. Write MEMORY-SETUP.md in my home folder: versions, data size (du -sh ~/.claude-mem),
   worker RAM, test result, and how to pause and uninstall.
```

## How to use it day to day

- **Nothing to do.** Work in a project folder as usual. Memory builds as you go, and the next session starts with it.
- **Same folder = same memory.** Memory is named after the folder (or the git repo). Rename a folder and you start a new memory, unless you merge it: `npx claude-mem project merge old-name new-name`.
- **Ask it to look back:** "What did we decide about the reminder screen last week?" Claude searches memory first.
- **See what it saved:** open the viewer URL from `npx claude-mem status`.
- **Keep secrets out:** wrap anything private in `<private>…</private>` and it isn't stored. Don't ask Claude to print `.env` files or keys. Everything it sees can end up in memory.
- **Ignore the "30 Day Free Trial" line** that shows when a session starts. It's an ad for the paid plan.

## Check, pause, remove

```bash
npx claude-mem status
npx claude-mem doctor
npx claude-mem stop          # pause the worker; a new session may start it again
npx claude-mem uninstall     # removes plugin and hooks; keeps your data in ~/.claude-mem
rm -rf ~/.claude-mem         # deletes all memory, permanently
```

To pause it fully, open `/plugin` in Claude Code and disable claude-mem.
