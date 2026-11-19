---
name: resume-builder
description: Builds or rebuilds a resume as one HTML file and prints it to an ATS-safe PDF with Playwright - single column, real selectable text, an embedded TrueType font, clickable links and a Projects section - then checks the PDF. Use when the user says "build my resume", "rewrite my resume", "make my resume ATS friendly", "turn my LinkedIn into a resume", "update my resume PDF", or "tailor my resume to this job".
---

# Resume builder

The resume lives as `resume.html` (the source you edit) and `<Name>_Resume.pdf` (what you send). Keep both in a repo so every change is tracked and one link always points to the latest PDF.

## 1. Gather the content

Ask for, in this order: the old resume or LinkedIn export, the target job titles, and 2 to 3 job descriptions they want. Then ask for missing facts: dates, team size, and **numbers** for each achievement. Never invent a number, title, employer or date. If a bullet has no number, ask; if there is none, write it without one.

## 2. Write it

Start from `assets/resume-template.html`. Rules:
- One column, sections in this order: name and contact, Summary (2 to 3 lines), Experience, Projects, Skills, Education.
- Each bullet: action verb, what changed, the number, and how. Two lines at most.
- Put the target job's exact skill words in Skills and in bullets where they are true.
- 1 page under about 8 years of experience, 2 pages at most above that.
- Links: site, LinkedIn, GitHub, and each project, as real `<a href>` links.
- Font: Liberation Sans, Arial or Helvetica. No icons, tables, text boxes, columns or images of text.

## 3. Print the PDF

```bash
npm i -D playwright && npx playwright install chromium   # once
node scripts/build_pdf.mjs resume.html Jordan_Lee_Resume.pdf
```

The script honours the `@page` size and margins in the HTML and writes a tagged PDF.

## 4. Check it

Run the `ats-resume-check` skill on the PDF if it is installed (`python3 ../ats-resume-check/scripts/check_resume.py <pdf>`). Fix every FIX line, rebuild, and check again. Then do the manual test: copy all text from the PDF into a plain note; it must read top to bottom in order.

## 5. Tailor per job (optional)

For a specific job: copy `resume.html` to `resume-<company>.html`, reorder bullets so the most relevant come first, and mirror the job's wording where it is true. Keep the original untouched. Show the user a diff of what changed before printing.

## Ship it

Commit the HTML and PDF, then update the PDF on the user's site, LinkedIn Featured section and job-board profiles (Simplify, LinkedIn application settings).
