# 08 · ATS-safe resume

Use the resume-builder skill from this repo if it is installed.

```text
Rebuild my resume as resume.html in a public repo called "resume", then print
it to PDF with Playwright. Requirements:
- One or two pages, single column, real selectable text, no text in images.
- An embedded TrueType font (for example Liberation Sans). No Type 3 fonts.
- Clickable links to my site, LinkedIn, GitHub and each project.
- A Projects section that links each big claim to public proof.
Commit both files. Then run the ats-resume-check skill on the PDF and fix
anything it flags.
```

Quick manual test: open the PDF, select all, copy, paste into a plain note. If it reads in order, an ATS can read it too.
