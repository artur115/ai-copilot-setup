#!/usr/bin/env node
// Print an HTML resume to an ATS-safe PDF with headless Chromium.
// Usage: node build_pdf.mjs resume.html Your_Name_Resume.pdf
// Needs: npm i -D playwright && npx playwright install chromium
import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const [, , input = 'resume.html', output = 'resume.pdf'] = process.argv;
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(resolve(input)).href, { waitUntil: 'networkidle' });
await page.emulateMedia({ media: 'print' });
await page.pdf({
  path: output,
  format: 'Letter',
  printBackground: true,
  preferCSSPageSize: true, // honour @page size and margins in the HTML
  tagged: true,            // tagged PDF: better reading order for parsers and screen readers
  outline: false,
});
await browser.close();
console.log(`Wrote ${output}`);
