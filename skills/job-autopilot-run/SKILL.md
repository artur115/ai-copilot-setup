---
name: job-autopilot-run
description: Use when a scheduled job-autopilot run starts ("run job autopilot", "run the job-autopilot-run skill"), or someone asks to run one now - finds jobs on LinkedIn and Built In, tailors the resume, applies, contacts recruiters and logs it, using the settings in the user's job-search repo.
---

# Job autopilot: one run

Nobody is watching this run. Never ask questions (no AskUserQuestion): decide, act, and record each decision in the
sheet and the summary. Use Claude in Chrome (the user's logins to LinkedIn, Built In and Gmail are there).

## Files
- Repo: the user's job-search repo clone, normally `~/Documents/job-search` (otherwise the folder under ~/Documents
  that contains `applications/SETTINGS.md`). Read and write files there directly. Don't use the GitHub API and don't
  run git: the Mac's auto-sync commits, pulls and pushes every 30 minutes.
- Read first: `CLAUDE.md`, `applications/SETTINGS.md` (this user's choices: everything below marked *Settings*),
  `applications/PROFILE.md`, `applications/PLAYBOOK.md`, `applications/LEADS.md`, the resume
  (*Settings: resume folder*), and the tracker sheet (*Settings: sheet*).
- Stale check: PROFILE.md must have a real email under "Contact for forms". If not, say so at the top of the summary
  and still apply wherever email/phone aren't required.
- `SETTINGS.md` "Extra rules" override anything here.

## Chrome tabs
Work in ONE tab group named "Job autopilot". At the start, close tabs left in groups with that name from earlier runs
and reuse one group. Keep at most 3 tabs open, close each job's tab when done, and close every tab this run opened at
the end. Never touch other tab groups or tabs the user opened.

## More than one Mac
Before applying, re-read the sheet; if the job is there (any status), skip it. Otherwise add its row at once with
Status "Applying (<`scutil --get ComputerName`>)" and update it when done. Rows stuck on "Applying" for 2+ hours can be
retried. Daily caps are counted from today's sheet rows. Keychain passwords are per Mac: if an account exists but this
Mac has no password, use "Forgot password" (Gmail) and save the new one here.

## Steps
0. **Kind of run.** The last scheduled run of the day (after 6 PM local) is the CATCH-UP run: no new searching; it
   works only the "Not done" lists in today's reports (unscreened leads, missed searches, outreach for earlier
   applications, step 5). Other runs do steps 1-4, spend at most half their time searching (screen, then apply, then
   outreach), and list what they didn't reach under "Not done".
1. **Find jobs.** First every unchecked link in `applications/LEADS.md`: open it, take out every job, screen and apply,
   then mark the link `[x]` with the date and counts. For a list of companies, run
   `python3 <this skill's folder>/scripts/screen_boards.py <saved list or post> <out.json>`: it checks each company's
   public Greenhouse/Ashby/Lever board at once.
   Then LinkedIn Jobs (recommendations, then *Settings: titles* with *Settings: locations*, past week) and Built In
   (builtin.com/jobs, same searches, newest first). Start with searches the last report lists under "Not done";
   both sites every run. Pace LinkedIn: one posting at a time, about 20 per run, never in parallel; at any 429 or
   warning stop LinkedIn for the day and continue on Built In. Use ATS board APIs (playbook) for originals and pay.
   Ignore aggregator reposts. Apply to every role at *Settings: levels*. A missing tool, different stack, years
   stretch or required certification is a gap to note, not a reason to skip.
   Skip only: already applied (sheet or Gmail confirmation); *Settings: hard skips*; posted base max under
   *Settings: minimum base*. Jobs in *Settings: local cities* count as local. Hybrid elsewhere: *Settings: hybrid rule*.
2. **Tailor, then apply.** Up to *Settings: applications per run*; at most 25 LinkedIn Easy Apply per day.
   - Copy the resume's `resume.html` to `~/Documents/tailored-resumes/<YYYY-MM-DD>-<company>/resume.html`. Always do all
     three: name the target role in the summary's last sentence; put the most relevant bullets and skills first; use
     the posting's terms where the resume already supports them. Never add a tool, employer, title, number, date or
     responsibility that isn't in resume.html. Max 2 pages. Never put tailored copies in a git repo.
   - Print: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer
     --print-to-pdf=<folder>/<Settings: PDF name> <folder>/resume.html`, then upload it (playbook: uploads).
   - Contact fields: email and phone from PROFILE.md "Contact for forms"; never write them anywhere else.
   - Accounts: *Settings: accounts*. If yes: prefer Sign in with Google/LinkedIn; otherwise the PROFILE.md email and a
     random 20+ character password saved only with `security add-internet-password -s <domain> -a <email> -w
     '<password>' -U` (read back: `security find-internet-password -s <domain> -w`). Verification emails: via Gmail.
     Never write a password anywhere else.
   - Questions: PROFILE.md answer bank, then learned answers, then the resume. Not covered: write the best answer from
     the resume and good judgement, submit, append "question → answer" to PROFILE.md "Learned answers", and note
     "Generated answers: <list>" in the row. Never claim experience the resume doesn't support. A new legal question
     not in the answer bank: log "Needs your answers" and move on.
   - Bot checks (CAPTCHA, emailed human codes, "if you're an LLM..." fields): never fill or bypass; log
     "Needs you: bot check" with the resume path. Only the site's confirmation page or email proves a submission.
   - Submit: *Settings: submit*. Never pay or accept upsells. A site needing a permission approval: note it, move on.
3. **Outreach** for each application: find the hiring team / job poster, otherwise "<company> technical recruiter" or
   the hiring manager on LinkedIn.
   - LinkedIn: *Settings: LinkedIn*. When sending: notes and messages written from the resume are approved, send them.
     1st-degree: a 3-4 sentence message; otherwise a connection request with a note under 200 characters (without a
     note if LinkedIn won't allow one). Max 15 requests and 20 messages a day, 80 requests a week, one person per job,
     nobody twice in 7 days, no InMail or paid credits. Stop LinkedIn for the day at any warning; add it to the playbook.
   - Gmail: a 4-6 sentence email (role, one matching resume win, *Settings: outreach link*, ask for a short chat) as a
     DRAFT, never sent. To: only if the address is published; otherwise blank, with the LinkedIn URL noted.
4. **Log** every job as a sheet row with these 14 columns: Date applied | Company | Title | Work type | Pay range (base) |
   Status | What the job is | Why I'm a good fit | Gaps to prep for interview | Recruiter / contact on LinkedIn |
   Next step | Follow-up date (+7 days) | Job link | LinkedIn people search.
   Job link = the direct posting URL, never a search page. Status: Applied / Skipped (<exact rule>) / Needs your
   answers / Needs manual apply (<why>). Gaps name the missing requirements. Next step says what was tailored, "Gmail
   draft ready", and LinkedIn actions with dates. "Why I'm a good fit" uses resume facts only.
   Also rows whose contact is empty or "Not yet - searching": find the person and do step 3 (up to 15 per run).
5. **Retry and clean up:** rows marked Needs manual apply, Skipped for a reason these rules now allow, or stuck on
   Applying, if the posting is still open; links pointing to search pages; vague reasons.
6. **Learn:** add each new lesson to `applications/PLAYBOOK.md` (a site quirk and its workaround, a blocker, a limit
   hit). Try the playbook's workarounds before marking "Needs manual apply".
7. **Summary**, appended to `applications/daily/<YYYY-MM-DD>-<ComputerName>.md`: applied (company, role, link), skipped
   and why, questions for the user, drafts created, LinkedIn requests/messages sent, lessons added, and "Not done".
