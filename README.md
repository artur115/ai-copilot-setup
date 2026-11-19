# AI job search setup

How I set up an AI-assisted job search on a MacBook in five days, written so a friend can repeat it. You get copy-paste prompts for every step, a list of every skill and plugin I installed (with the GitHub repo each came from), four small skills of my own you can install in one command, and the design sites I use for web and app ideas.

What the setup produced for me:

| Piece | Result |
|---|---|
| Website | [arturkochetkov.dev](https://arturkochetkov.dev): own `.dev` domain, auto-deploys on every push |
| Booking | A Calendly page for 30-minute Google Meet calls, synced with Google Calendar |
| Resume | An ATS-safe PDF built from HTML: [artur115/resume](https://github.com/artur115/resume) |
| Proof projects | [social-commerce-ltv](https://github.com/artur115/social-commerce-ltv) and [marketing-data-reliability](https://github.com/artur115/marketing-data-reliability) |
| App | [Pillwave](https://pillwave.app), an iPhone medication-reminder app |

## Start here

1. Get **Claude Pro** ($20/month, or $17/month billed yearly; see [claude.com/pricing](https://claude.com/pricing)) and install the Mac app from [claude.com/download](https://claude.com/download).
2. Open **Claude Code** in the app and start a cloud session.
3. Paste [`prompts/00-start-here.md`](prompts/00-start-here.md). Claude reads the rest of this repo and walks you through it, one step at a time.

Prefer to drive it yourself? Run the prompts in order:

| # | Prompt | What you end up with |
|---|---|---|
| 00 | [Start here](prompts/00-start-here.md) | Claude knows your goal and walks you through the rest |
| 01 | [Accounts and the Claude app](prompts/01-accounts-and-claude.md) | Claude Pro, GitHub, Google, Claude Code ready |
| 02 | [Connectors](prompts/02-connectors.md) | Claude can work in GitHub, Gmail, Calendar, Drive and more |
| 03 | [Environments and keys](prompts/03-environments-and-keys.md) | A safe network allowlist; keys stored outside chat |
| 04 | [Install skills and plugins](prompts/04-install-skills.md) | The same skills I use (see [SKILLS.md](SKILLS.md)) |
| 05 | [Knowledge graph](prompts/05-knowledge-graph.md) | graphify maps a repo so Claude reads less |
| 06 | [Domain and website](prompts/06-domain-and-website.md) | `yourname.dev` live on Cloudflare |
| 07 | [Booking page](prompts/07-booking-calendly.md) | A Calendly link on your site and LinkedIn |
| 08 | [ATS-safe resume](prompts/08-ats-resume.md) | A resume PDF that parses cleanly |
| 09 | [Proof project](prompts/09-proof-project.md) | A public repo that backs up your strongest resume claim |
| 10 | [Applications](prompts/10-applications-simplify.md) | Simplify autofill on Greenhouse and similar forms |
| 11 | [LinkedIn with Claude in Chrome](prompts/11-linkedin-chrome.md) | Profile, Featured section and resume updated |
| 12 | [Weekly routine](prompts/12-weekly-routine.md) | A small loop you repeat every week |

## Install my four skills

In Claude Code, run:

```
/plugin marketplace add artur115/ai-job-search-setup
/plugin install job-search-kit@ai-job-search-setup
```

| Skill | What it does | Say this to use it |
|---|---|---|
| [`job-search-setup`](skills/job-search-setup/SKILL.md) | Walks you through steps 01 to 12, checks each one is done, and keeps a checklist | "help me set up my job search" |
| [`ats-resume-check`](skills/ats-resume-check/SKILL.md) | Checks a resume PDF for fonts, selectable text and links, and reports what to fix | "check my resume PDF for ATS problems" |
| [`proof-project`](skills/proof-project/SKILL.md) | Turns one resume claim into a small public project with synthetic data and tests | "build a proof project for this resume line" |
| [`resume-builder`](skills/resume-builder/SKILL.md) | Writes your resume as one HTML file and prints an ATS-safe PDF with Playwright; includes a template | "build my resume" |

## Every skill and plugin I installed

See [SKILLS.md](SKILLS.md) for the full list with sources, descriptions and install commands. In short:

| Source repo | What I took from it |
|---|---|
| [glebis/claude-skills](https://github.com/glebis/claude-skills) | feature-factory, tdd, app-map, app-release |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | graphify, the code knowledge graph |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | agent-skills plugin: /spec, /plan, /build, /test, /review, /ship |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | ponytail plugin: keeps generated code short |
| [expo/skills](https://github.com/expo/skills) (via [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)) | expo plugin for React Native apps |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Everything Claude Code, the Anthropic hackathon winner: 327 skills, 72 agents (on my Mac) |
| [obra/superpowers](https://github.com/obra/superpowers) | Brainstorm, plan, test-driven build method (on my Mac) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Small engineering skills you adapt (on my Mac) |
| [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Karpathy-style coding guidelines (on my Mac) |
| Anthropic built-in skills | Docs, Slides, Sheets, PDF, Word, Excel, PowerPoint, skill-creator, deep research |

## Design sites for web and app ideas

See [DESIGN-RESOURCES.md](DESIGN-RESOURCES.md): the galleries I use to pick a layout before asking Claude to build a site or app screen.

## Ground rules

- **Never paste API keys into chat.** Use the secure credential form in the environment settings.
- **Review before you submit.** Autofill and AI drafts save time; you still read every field.
- **Keep claims provable.** If a number is on your resume, link a project or write-up that shows the method.

Prices and product details were checked on 19 November 2026 and change often.

Built with Claude. Questions: [arturkochetkov.dev/book](https://arturkochetkov.dev/book).
