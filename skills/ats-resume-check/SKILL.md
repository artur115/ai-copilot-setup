---
name: ats-resume-check
description: Checks a resume PDF for problems that break applicant tracking systems (ATS) - Type 3 or non-embedded fonts, text that can't be extracted, a scrambled reading order, missing clickable links, too many pages - and reports what to fix. Use when the user says "check my resume", "is my resume ATS friendly", "why does my resume parse badly", or uploads a resume PDF before applying.
---

# ATS resume check

## Run the check

```bash
pip install pypdf          # once
python3 scripts/check_resume.py path/to/resume.pdf
```

The script prints the page count, every font with its type and whether it's embedded, the number of words it can extract, the first lines as a parser would read them, the clickable links, and a list of fixes. Exit code 0 means no problems were found.

## Read the result with the user

- **Type 3 fonts:** the most common silent failure. Some parsers turn them into gibberish. Re-export from the source with a TrueType font (Liberation Sans, Arial, Inter), or print HTML to PDF with Playwright or Chrome.
- **Few extractable words:** the PDF is an image or the text was outlined. Rebuild from a text source.
- **Reading order:** if the first lines are not name, then contact line, then headline, the layout probably has columns or text boxes. Use a single column.
- **No links:** add the site, LinkedIn, GitHub and project links as real links.
- **Pages:** 1 page early in a career, 2 at most for senior roles.

Then do the manual test: select all text in the PDF, copy, paste into a plain note. It should read top to bottom in order.

## If the user wants it fixed

Offer to rebuild the resume as `resume.html` and print it to PDF with Playwright (`page.pdf()` with print backgrounds on, Letter size). Re-run the check on the new PDF and show the before and after.

Don't change the user's claims or numbers while fixing the format.
