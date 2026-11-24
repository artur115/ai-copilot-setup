---
name: job-autopilot
description: Use when a job seeker wants Claude to find and apply to jobs on its own every day (LinkedIn, Built In), with recruiter outreach and a tracking sheet, and needs it set up once on their Mac - says "apply to jobs for me every day", "set up auto-apply", "job autopilot", "schedule my job applications", or a scheduled apply run keeps stopping to ask questions, can't upload a resume, or reads outdated files.
---

# Job autopilot

Sets up a scheduled task that, at least twice a day, finds matching jobs on LinkedIn and Built In, tailors the
resume, applies through Claude in Chrome, contacts the recruiter, and logs everything in a Google Sheet. You ask
the user questions **once**, during setup. Scheduled runs never ask anything: nobody is watching them.

The user may not be technical. Use plain words, one step at a time, and do every part you can yourself.

## Before you start

1. **This runs in Claude Code on the user's Mac** (desktop app, Local environment, or `claude` in Terminal),
   because the scheduled runs use the user's Chrome, files and Keychain. In a cloud session, stop and say so.
2. **Prerequisites** (from the `job-search-setup` skill; run those steps first if missing):
   - a private GitHub repo for the job search (`job-search`), cloned to `~/Documents/job-search` (use `git clone`,
     not a ZIP download: a ZIP has no git history and can't sync);
   - the resume as `resume.html` + PDF in a repo cloned to `~/Documents/resume` (`resume-builder` skill);
   - LinkedIn profile updated (step 11) and the new resume uploaded under LinkedIn → Settings → Job application settings.
3. Read `assets/questions.md`, `assets/routine-template.md`, `assets/profile-template.md`, `assets/playbook-seed.md`.

## Setup steps

| # | Step | Who |
|---|---|---|
| 1 | Ask the onboarding questions (`assets/questions.md`), in its 6 rounds | you ask, user answers |
| 2 | Write `applications/PROFILE.md` from `assets/profile-template.md` with their answers | you |
| 3 | Copy `assets/playbook-seed.md` to `applications/PLAYBOOK.md` | you |
| 4 | Fill `assets/routine-template.md` → `applications/ROUTINE.md` (every `{{...}}` replaced) | you |
| 5 | Add the permission lines they chose (below) to the repo's `CLAUDE.md` | you |
| 6 | Tracker sheet: create a Google Sheet "Job Applications" with the 14 header columns from the routine, or use theirs and check its headers | you (Google Drive/Sheets connector) |
| 7 | Connectors and Chrome (checklist below) | user clicks, you verify |
| 8 | Git auto-sync on the Mac (below) | you run, with their OK |
| 9 | Create the scheduled task (below) | you, or user clicks |
| 10 | First run, watched: "Run now", user clicks "Always allow" on every prompt | user watches, you check results |
| 11 | Commit and push, tick "17 Daily auto-apply" in `SETUP-CHECKLIST.md` | you |

### Step 4: filling the choice placeholders
| Placeholder | User chose | Text |
|---|---|---|
| `{{SUBMIT_RULE}}` | submit alone | Submit the application. |
| | shortlist | Don't submit: fill everything up to the last page, log "Ready - waiting for your OK", and list it in the summary. |
| `{{LINKEDIN_RULE}}` | send | Notes and messages you write from the resume are approved: send them, don't hold them for review. 1st-degree connection: send a 3-4 sentence message. Otherwise a connection request with a note under 200 characters (without a note if LinkedIn won't allow one). Max 15 requests and 20 messages a day, 80 requests a week, one person per job, nobody twice in 7 days, no InMail. Stop for the day at any LinkedIn warning and add it to the playbook. |
| | draft only | Don't send anything on LinkedIn; put the suggested note in the row's Next step. |
| | no | Skip LinkedIn outreach. |
| `{{ACCOUNT_RULE}}` | yes | Create one if needed. Prefer Sign in with Google/LinkedIn; otherwise PROFILE.md email + a random 20+ character password saved only with `security add-internet-password -s <domain> -a <email> -w '<password>' -U` (read back with `security find-internet-password -s <domain> -w`). Verification emails: open via Gmail. Never write a password anywhere else. |
| | no | Log "Needs manual apply (account needed)". |
| `{{HYBRID_RULE}}` | hybrid OK | apply and note "Hybrid (<city>) - ask about remote" |
| | not OK | skip |

`{{PDF_NAME}}` is `First_Last.pdf`. An optional answer the user skipped (e.g. `{{ADDRESS}}`) becomes "not given". `{{HARD_SKIPS}}` lists their round-1 skips (e.g. "contract; security clearance;
fully on-site outside <their city>"). Before saving, `grep -c "{{" applications/ROUTINE.md applications/PROFILE.md` must print 0 for both.

If `applications/PROFILE.md` already exists, the user set this up before: read it, ask only the questions whose
answers are missing, and update files and the existing scheduled task instead of creating a second one.

### Step 5: permission lines for CLAUDE.md
Write only what the user chose in round 6 of the questions, dated, for example:
```
- Job applications: you may submit them without asking (<name>'s OK, <date>) when the role matches applications/ROUTINE.md.
- Application forms and ATS accounts may use the email and phone in applications/PROFILE.md; nowhere else.
- ATS accounts: may be created. Prefer Sign in with Google/LinkedIn; otherwise a random password saved only in the macOS Keychain.
- LinkedIn: may send connection requests and messages, written by Claude from the resume, to the recruiter or hiring manager of a job applied to, within ROUTINE.md limits. Send them; don't hold them for review. No InMail, nothing paid.
- Recruiter emails stay Gmail drafts, never sent.
```
The contact details go into PROFILE.md only when the user types them in the chat during setup.

### Step 7: connectors and Chrome checklist
Have the user do each item, then check it yourself where you can:
- [ ] Claude connectors on: **Gmail**, **Google Drive**, **Google Sheets** (claude.ai → Settings → Connectors). Check: list Gmail drafts, read the sheet.
- [ ] **Claude in Chrome** extension installed, pinned and signed in (Chrome Web Store → "Claude in Chrome").
- [ ] In that Chrome, signed in to **LinkedIn**, **Built In** (builtin.com, free account) and **Gmail**.
- [ ] If more than one Chrome is connected, pick one now (it must be the Chrome on the Mac that will run the task).
- [ ] Mac stays awake at run times: plugged in; System Settings → Battery → Options → "Prevent automatic sleeping when the display is off". The Claude app must be open.

### Step 8: git auto-sync
Scheduled runs often can't run git themselves (lock files, "Operation not permitted"), so the Mac syncs on its own.
With the user's OK, run:
```bash
(crontab -l 2>/dev/null; echo '*/30 * * * * cd $HOME/Documents/job-search && git add -A && git commit -qm "Auto-sync"; git pull -q --no-edit -X theirs && git push -q') | crontab -
```
Check it after 30 minutes with `git -C ~/Documents/job-search log -1`. If nothing synced, macOS blocked cron from
Documents: System Settings → Privacy & Security → Full Disk Access → + → `/usr/sbin/cron`.
The repo must be private (it holds contact details and form answers).

### Step 9: the scheduled task
- Name "Job autopilot", working folder `~/Documents`, permission mode **auto**.
- Schedule: the times from round 6 (at least 2 a day, for example 8:17 AM and 4:17 PM local; avoid :00), plus a
  catch-up run after 6 PM (for example 7:17 PM) that finishes what the day's runs left undone.
- Prompt: the whole of `applications/ROUTINE.md`.
- If you have a tool that creates scheduled tasks, use it. Otherwise give the user the clicks: Claude app → Scheduled
  (or Routines) → New task → paste the prompt → set folder, times and permission mode → Save.
- On a second Mac: clone the repo there too, then add a task at different times (the routine handles two Macs).
- To change the prompt later, the user edits the task on that Mac (a task bound to a Mac can't be edited from a cloud session).

### Step 10: the first run
Run it now while the user watches. Every site or tool approval they click "Always allow" on now won't stop later
runs: linkedin.com, builtin.com, greenhouse.io, lever.co, ashbyhq.com, myworkdayjobs.com, Gmail, Sheets, Keychain.
Afterwards check: new sheet rows have direct job links, specific reasons and real dates; a report exists in
`applications/daily/`; nothing was claimed that isn't on the resume. Fix the routine if not, then tell the user
in 5 lines what it did and when it runs next.

## Common mistakes (seen in real runs)

| Symptom | Cause | Fix |
|---|---|---|
| Run stops to ask "which browser?" or for a phone number | Questions not answered at setup, or the run read an old copy of the files | Answer everything in setup; auto-sync (step 8); the routine checks PROFILE.md first |
| Run says it has no access to the repo | Prompt told it to use GitHub online | The routine reads the local clone only |
| "Not a git repository" | Repo was downloaded as ZIP | Delete it, `git clone` |
| Resume upload refused | Run tried a path it isn't allowed to read | Stage the file first (playbook) |
| Few applications, many "weak fit" skips | Skip rules too strict | Only hard skips; tailor the resume instead |
| Sheet links point to search pages | No link rule | Direct posting URL required |
| LinkedIn returns HTTP 429, then blocks the day | Too many fast or parallel job fetches | ~20 sequential fetches per run; ATS board APIs for the rest |
| 0 LinkedIn messages sent "for your review" | Permission line didn't say run-written notes are OK | Use the CLAUDE.md line above |
| Same titles searched every run, others never | No rotation | Report "Not done"; next run starts there |
| Runs end with only searching done; outreach and cleanup never happen | Too much scope per run | Half the time cap on searching; evening catch-up run |
| Chrome fills up with old "Job autopilot" tab groups | Each run opens a new group and leaves it | Routine reuses one group and closes its tabs at the end |
| "Submitted" but no confirmation email | Simplify popup, or a bot check stopped it | Trust only the confirmation page or email |
| Several jobs "Needs manual apply (account)" | Run couldn't create a password account | Expected on some big-company sites; the user finishes them in one sitting with the saved resumes |
| Answers with numbers not on the resume | No source rule | Resume and PROFILE.md only; generated answers are logged for review |

## Honesty and safety rules (always)
- Never claim a tool, title, certification, degree, number of years or result that the resume doesn't support.
- Never pay, never use InMail or paid credits, never send email (drafts only), never put passwords in files or chat.
- LinkedIn limits automated activity; keep the caps in the routine and stop for the day at any warning. Tell the
  user once, at setup, that automated applying and messaging can get a LinkedIn account restricted.
