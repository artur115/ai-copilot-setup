# 13 · Outreach to hiring companies with Sellbird (optional)

[Sellbird](https://github.com/ethanplusai/sellbird) is an open-source cold-email agent (AGPL-3.0,
Python 3.11+). It runs on your Mac through Claude Code on your Claude Pro/Max plan, so there's no
API bill. It was built for sales, but one of its features fits a job search well: it can find
companies **hiring for your role** (it reads their public Greenhouse, Lever, Ashby and Workable job
boards), find the person who decides on the company's own pages, verify one email address, and
draft a short, personal note. **By default nothing sends until you approve it.**

Use it alongside applications, not instead of them: apply through the job board, then send one
short note to the hiring manager.

**What it costs:** the software and the default company search are free. You need your Claude
plan, and a mailbox to send from. If you'll send more than about 10 emails a day, use a second
domain and a Google Workspace mailbox (about $12 a year plus $7 a month), so your main address
never lands in spam. An email verifier (optional, pay-as-you-go) lets more addresses count as
"verified".

Paste this into Claude Code on your Mac (not a cloud session: Sellbird keeps its data on your
computer), in an empty folder:

```text
Set up Sellbird for my job search, safely, in approval mode, with a dry run first.
Repo: https://github.com/ethanplusai/sellbird (use the latest release tag).

MY BRIEF (ask me for anything blank, never invent it):
- Target role and level: ______ (for example "Senior Marketing Analyst")
- Industries or company types: ______
- Location or "remote, US": ______
- My site / portfolio: ______ (Sellbird trains on it)
- One-line pitch, with a proof link: ______ (only claims I can back up)

RULES
1. Read README.md, CLAUDE.md, .env.example and docs/deliverability.md first. Tell me what it will
   install, which files it creates, which accounts it needs, and what AGPL-3.0 means (using it
   unmodified on my Mac: no obligations; if I modify it and host it for others, I must share my
   source). Wait for my "go".
2. Approval mode only. Never turn on autopilot. Show me the setting
   (channels.email.require_approval: true) as evidence.
3. No mailbox and no sending until I give a separate go-ahead. LinkedIn automation stays OFF
   (it breaks LinkedIn's terms).
4. Use Sellbird's hiring signals: set icp.hiring_signals to my target role so it looks for
   companies with that opening on their own job board. Let me confirm the signals myself.
5. Every draft must mention one real, checkable thing from that company's own site or job post
   (keep the URL), say in one line why I fit, and ask one low-pressure question. Under 100 words.
   If there's nothing real to mention, drop the company. Never claim a referral, a conversation
   or a skill I don't have.
6. Keep it human-scale: at most 10 sends a day, inside office hours, and stop on any "no" or
   "please don't email me" for good (Sellbird does this by default; keep a do-not-contact list
   with my current employer and anyone I already know).
7. Keys go only in Sellbird's .env, which is git-ignored. Never print them back to me.

DRY RUN
- Preflight: python3.13 (brew install python@3.13 if missing), claude signed in, git.
- Clone into ~/Documents/sellbird, then run its own setup: "set up Sellbird for me".
- Find up to 25 companies hiring for my role → read their sites → find who decides (max 2 per
  company) → verify one address each → draft notes for the top 10 into the Outbox.
- Report my REAL funnel: __ companies found → __ with a matching open role → __ people found →
  __ verified → __ drafts. Small numbers are fine; say so.
- Open the dashboard (sellbird dashboard, http://127.0.0.1:5555) and stop. I review every draft.

SENDING (only on my separate go-ahead)
- Help me pick: send from my own address at very low volume, or set up a second domain with
  SPF/DKIM/DMARC and 2 weeks of warmup first. Set my real mailing address in
  compliance.postal_address if I send at any volume.
- First batch: at most 5 emails, each approved by me. `sellbird sending pause` stops everything.
```

**Good to know**

- A job-inquiry email isn't advertising, but treat it the same way: a truthful subject, your real
  name, and an easy "not interested" that you honour immediately.
- Outside the US (Canada, the UK, the EU) the rules on unsolicited email are stricter. Keep to
  your own country unless you know the rules there.
- **Don't send cold email through a newsletter service** (Resend, Mailchimp, Kit, Amazon SES and
  similar). Their rules generally allow only email to people who signed up, so an account can be
  suspended, and Sellbird also needs a real mailbox it can read replies from (IMAP or Gmail/
  Microsoft sign-in), which those services don't give you. Use your own Gmail or Google
  Workspace mailbox. Check the service's acceptable-use page if you're unsure.
- Every "I noticed your site doesn't…" claim comes from an automated read of one page. Ask
  Claude to open the page and check it before you approve the draft.
