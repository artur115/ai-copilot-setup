# 17 · Daily auto-apply (job autopilot)

Claude finds jobs on LinkedIn and Built In at least twice a day, tailors your resume for each one, applies, contacts
the recruiter, and logs everything in a Google Sheet. You answer its questions once; after that it runs on its own.

**Do steps 08 (resume) and 11 (LinkedIn) first.** This step runs **on your Mac**, in the Claude app (Claude Code,
Local) with the Claude in Chrome extension, because it uses your Chrome logins. Your Mac must be awake with the
Claude app open at the run times.

**Costs:** nothing extra beyond your Claude plan. **Risk:** LinkedIn limits automated activity; the routine keeps
daily caps and stops at any warning, but an account restriction is possible.

Paste this into Claude Code on your Mac:

```text
Set up job autopilot for me with the job-autopilot skill from the job-search-kit plugin.
Ask me all the questions once, help me turn on the connectors and Chrome permissions,
create the scheduled task, and do the first run with me watching.
```

When it's done you'll have:

| Piece | Where |
|---|---|
| Your answers for every application form | `applications/PROFILE.md` in your private job-search repo |
| The daily routine | `applications/ROUTINE.md` and a scheduled task in the Claude app |
| What it learns from each run | `applications/PLAYBOOK.md` |
| Every application, link and recruiter | Your "Job Applications" Google Sheet |
| A report after each run | `applications/daily/` |
