# 16 · Remote Control and long runs

**Remote Control** lets you start and steer Claude Code sessions that run **on your Mac** from your phone (the Claude app) or from claude.ai/code. Those sessions use your Mac's files, tools and memory (prompt 15). A cloud session can't do that.

## Turn it on (your part, about 2 minutes)

1. Update the Claude desktop app: **Claude menu → Check for Updates**.
2. Open **Settings → Claude Code → Remote Control** and add the folder of the project you work on (for example `~/Documents/myproject`). Add the project folder itself, not your whole home folder or `Documents`.
3. On your phone, open the Claude app → Code. Your Mac and that folder show up there. Start a session and it runs on the Mac.

No desktop app? Do it from Terminal instead. Use the app *or* Terminal for a folder, not both. If you try both, Terminal says "This folder is already served by the Claude app":

```bash
cd ~/Documents/myproject && claude remote-control
```

When it asks for **spawn mode**, pick `same-dir` (the default). Sessions then work in your real folder and share one memory. `worktree` gives each session its own copy of the folder, which is useful for parallel tasks, but memory can end up split across the copies.

## Keep the Mac awake for long runs

A sleeping Mac stops every session. In a Terminal window, run this and leave the window open:

```bash
caffeinate -dims
```

It keeps the Mac awake until you press Ctrl+C or close the window. For longer runs, also:

- **System Settings → Battery → Options →** turn on *Prevent automatic sleeping on power adapter when the display is off*, and keep the charger plugged in.
- **Keep the lid open.** Closing the lid puts the Mac to sleep, unless it's on power with an external display.

## Fewer interruptions

- Press **Shift+Tab** in Claude Code to switch modes. **Auto mode** lets Claude work without asking at every step. It still stops before risky actions.
- Don't use `--dangerously-skip-permissions` on your everyday Mac. It removes every check.
- For a task that repeats, use `/loop`, for example `/loop 30m check the build and fix failures`.

## Prompt: set it up with Claude's help

Paste into **Claude Code on your Mac**:

```text
Help me run Claude on this Mac for long tasks I can steer from my phone.
1. Show me numbered steps to turn on Remote Control in the Claude desktop app for
   my project folder (ask me which folder), and wait for "done".
2. Check the folder isn't my home folder or a hidden folder, and tell me which spawn mode
   to pick and why (same-dir unless I want parallel tasks).
3. Explain caffeinate -dims and the Battery setting that stops sleep on power,
   and tell me to keep the lid open.
4. Explain the permission modes (Shift+Tab) and recommend one for unattended work.
   Don't change my settings yourself.
5. Remind me that long runs use my Claude plan faster (and claude-mem's background
   note-taker too, if installed), and where to watch usage (/usage).
```
