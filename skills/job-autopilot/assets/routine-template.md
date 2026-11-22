Job autopilot run for {{NAME}}. Nobody is watching this run: never ask questions (no AskUserQuestion), decide,
act, and record each decision in the sheet and the summary. Use Claude in Chrome (my logins to LinkedIn,
Built In and Gmail are there).

Files: my local clone of my job-search repo, ~/Documents/job-search (if it's not there, use the folder under
~/Documents that contains applications/PROFILE.md). Read and write files there directly. Don't use the GitHub API,
and don't run git: the Mac syncs the folder on its own.
First check the files are current: applications/PROFILE.md must have a real email under "Contact for forms".
If it doesn't, say so at the top of the summary and still apply wherever email/phone aren't required.

Read first: CLAUDE.md, applications/PLAYBOOK.md (follow its lessons), applications/PROFILE.md, the resume
(~/Documents/resume/resume.html), and the tracker sheet: {{SHEET_URL}}

If another Mac also runs this task: right before applying, re-read the sheet; if the job is there (any status), skip
it; otherwise add its row at once with Status "Applying (<`scutil --get ComputerName`>)" and update it when done.
Rows stuck on "Applying" for 2+ hours can be retried. Daily caps are counted from today's sheet rows.

1. Find jobs on both sites, posted in the past week, newest first; each run continues where the last one stopped.
   - LinkedIn Jobs: recommendations, then searches for: {{TITLES}}. Filters: {{LOCATION_FILTERS}}.
   - Built In (builtin.com/jobs): the same searches and locations. Apply on the company's own site it links to.
   Rotate: first the searches the previous run's report lists under "Not done", then the rest; both sites every run.
   Pace LinkedIn: open postings one at a time, about 20 per run, never in parallel; use ATS board APIs (playbook)
   for originals and pay. At any LinkedIn 429 or warning, stop LinkedIn for the day and continue on Built In.
   Ignore aggregator reposts; find the original posting.
   Apply to every role at these levels: {{LEVELS}}. A missing tool, different stack, years stretch or required
   certification is a gap to note, not a reason to skip.
   Skip only: already applied (sheet or Gmail confirmation); {{HARD_SKIPS}}; posted base max under {{MIN_BASE}}.
   Hybrid outside my area: {{HYBRID_RULE}}.
2. Tailor the resume, then apply. Up to {{PER_RUN}} applications per run; at most 25 LinkedIn Easy Apply per day.
   - Copy ~/Documents/resume/resume.html to ~/Documents/tailored-resumes/<YYYY-MM-DD>-<company>/resume.html.
     Change only, and always do all three: the summary's last sentence (name the target role), the order of bullets
     and skills (most relevant first), and wording that uses the posting's terms where the resume already supports them.
     Never add a tool, employer, title, number, date or responsibility that isn't in resume.html. Max 2 pages.
   - Print: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer
     --print-to-pdf=<folder>/{{PDF_NAME}} <folder>/resume.html. Upload that PDF (see the playbook for uploads).
     Never put tailored copies in a git repo.
   - Contact fields: email and phone from PROFILE.md "Contact for forms"; never write them anywhere else.
   - Accounts: {{ACCOUNT_RULE}}
   - Questions: answer from PROFILE.md (answer bank, then learned answers) and the resume. Not covered: write the
     best answer from the resume and good judgement, submit, append "question → answer" to PROFILE.md "Learned
     answers", and note "Generated answers: <list>" in the row's Next step. Never claim experience the resume
     doesn't support. A new legal question not in the answer bank: log "Needs your answers" and move on.
   - {{SUBMIT_RULE}}
   - Bot checks (CAPTCHA, emailed human-check codes, "if you're an LLM..." fields): never fill or bypass; log
     "Needs you: bot check" with the resume path. Only the site's confirmation page or email proves submission.
   - Never pay or accept premium upsells. If a site needs a permission approval, note it and move on.
3. Recruiter outreach for each application. Find the person: "Meet the hiring team" / job poster first, otherwise
   search LinkedIn for "<company> technical recruiter" or the hiring manager.
   - LinkedIn: {{LINKEDIN_RULE}}
   - Gmail: a 4-6 sentence email (the role, one matching resume win, one link: {{LINK_FOR_OUTREACH}}, a request
     for a short chat), saved as a DRAFT, never sent. To: only if the address is published; otherwise blank, and note
     the LinkedIn URL.
4. Log every job as a row in the sheet, 14 columns:
   Date applied | Company | Title | Work type | Pay range (base) | Status | What the job is | Why I'm a good fit |
   Gaps to prep for interview | Recruiter / contact on LinkedIn | Next step | Follow-up date (+7 days) | Job link |
   LinkedIn people search.
   Job link = the direct posting URL (linkedin.com/jobs/view/<id> or the company's page), never a search page.
   Status: Applied / Skipped (<exact rule>) / Needs your answers / Needs manual apply (<why>).
   Gaps name the missing requirements. Next step says what was tailored, "Gmail draft ready", and LinkedIn
   actions with dates. "Why I'm a good fit" uses resume facts only.
   Also work rows whose contact is empty or "Not yet - searching": find the person, do step 3 (up to 15 per run).
5. Retry: rows marked Needs manual apply, Skipped for a reason these rules now allow, or stuck on Applying,
   if the posting is still open. Fix links that point to search pages.
6. Learn: add every new lesson to applications/PLAYBOOK.md (a site quirk and its workaround, a blocker, a limit hit).
   Try the playbook's workarounds before marking "Needs manual apply".
7. Summary (include "Not done": searches and steps this run skipped, so the next run starts there), appended to applications/daily/<YYYY-MM-DD>-<ComputerName>.md: applied (company, role, link),
   skipped and why, questions for me, drafts created, LinkedIn requests/messages sent, lessons added.
