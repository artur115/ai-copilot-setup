# AI co-pilot setup

Set up a MacBook with Claude as your AI co-pilot: it remembers your work between sessions, runs long tasks you can steer from your phone, and helps you run a job search from start to finish. This is how I set mine up, written so a friend can repeat it. You get one install prompt, copy-paste prompts for every step, a list of every skill and plugin I use (with the GitHub repo each came from), five small skills of my own, and the design sites I use for web and app ideas.

*Formerly `ai-job-search-setup`. Old links redirect here.*

## What it does for you

| You get | What that means day to day |
|---|---|
| **A co-pilot on your Mac** | Ask in plain English; Claude plans, edits files and asks before risky steps |
| **Memory between sessions** | Close Claude tonight; tomorrow it already knows what you did ([claude-mem](prompts/15-memory-claude-mem.md)) |
| **Remote Control** | Start and steer sessions on your Mac from your phone ([prompt 16](prompts/16-remote-control-always-on.md)) |
| **Skills and plugins** | Tested recipes for resumes, test-first coding, app releases and more ([SKILLS.md](SKILLS.md)) |
| **A job-search toolkit** | Website, booking page, ATS-safe resume, proof projects, faster applications |

## Install

Paste one prompt into Claude Code on your Mac: **[INSTALL.md](INSTALL.md)**. It works on Apple-chip and Intel Macs: it checks your chip first and skips Homebrew on Intel ([why](INSTALL.md#intel-macs)). It installs the tools, the kit, memory (optional) and Remote Control (optional), checks every step, and ends with a short list of what only you can do.

What the setup produced for me:

| Piece | Result |
|---|---|
| Website | [arturkochetkov.dev](https://arturkochetkov.dev): own `.dev` domain, auto-deploys on every push |
| Booking | A Calendly page for 30-minute Google Meet calls, synced with Google Calendar |
| Resume | An ATS-safe PDF built from HTML: [artur115/resume](https://github.com/artur115/resume) |
| Proof projects | [social-commerce-ltv](https://github.com/artur115/social-commerce-ltv) and [marketing-data-reliability](https://github.com/artur115/marketing-data-reliability) |
| App | [Pillwave](https://pillwave.app), an iPhone medication-reminder app |

## Job search: start here

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
| 13 | [Outreach with Sellbird](prompts/13-outreach-sellbird.md) (optional) | Short, personal notes to hiring managers at companies hiring for your role, each approved by you |
| 14 | [New laptop: install everything](prompts/14-new-laptop-all-in-one.md) | One prompt that installs the tools, skills and plugins from this guide on a fresh Mac |
| 15 | [Memory with claude-mem](prompts/15-memory-claude-mem.md) (on your Mac) | Claude remembers your work between sessions, stored locally |
| 16 | [Remote Control and long runs](prompts/16-remote-control-always-on.md) (on your Mac) | Steer Mac sessions from your phone; the Mac stays awake |
| 17 | [Daily auto-apply](prompts/17-daily-auto-apply.md) (on your Mac) | Claude applies to matching jobs on its own twice a day or more, contacts recruiters and keeps your tracker sheet up to date |

## Install my five skills

In Claude Code, run:

```
/plugin marketplace add artur115/ai-copilot-setup
/plugin install job-search-kit@ai-copilot-setup
```

| Skill | What it does | Say this to use it |
|---|---|---|
| [`job-search-setup`](skills/job-search-setup/SKILL.md) | Walks you through steps 01 to 17, checks each one is done, and keeps a checklist | "help me set up my job search" |
| [`ats-resume-check`](skills/ats-resume-check/SKILL.md) | Checks a resume PDF for fonts, selectable text and links, and reports what to fix | "check my resume PDF for ATS problems" |
| [`proof-project`](skills/proof-project/SKILL.md) | Turns one resume claim into a small public project with synthetic data and tests | "build a proof project for this resume line" |
| [`job-autopilot`](skills/job-autopilot/SKILL.md) | Asks you its questions once, sets up connectors and Chrome, then applies to jobs on LinkedIn and Built In at least twice a day with a tailored resume, messages recruiters and logs it all in a Google Sheet | "set up job autopilot" |
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
| [obra/superpowers](https://github.com/obra/superpowers) | My one coding method: brainstorm, plan, test-driven build (on my Mac) |
| [affaan-m/ECC](https://github.com/affaan-m/ECC), [mattpocock/skills](https://github.com/mattpocock/skills), [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | Alternatives to superpowers. Pick one, don't stack them ([why](SKILLS.md#why-i-dont-stack-coding-style-plugins)) |
| Anthropic built-in skills | Docs, Slides, Sheets, PDF, Word, Excel, PowerPoint, skill-creator, deep research |

## Design sites for web and app ideas

See [DESIGN-RESOURCES.md](DESIGN-RESOURCES.md): the galleries I use to pick a layout before asking Claude to build a site or app screen.

## Ground rules

- **Keep secrets out of memory.** claude-mem stores what Claude sees in plain text on your Mac. Wrap private text in `<private>…</private>` and never ask Claude to print `.env` files.
- **Never paste API keys into chat.** Use the secure credential form in the environment settings.
- **Review before you submit.** Autofill and AI drafts save time; you still read every field.
- **Keep claims provable.** If a number is on your resume, link a project or write-up that shows the method.

Prices and product details were checked on 19 November 2026 and change often.

Built with Claude. Questions: [arturkochetkov.dev/book](https://arturkochetkov.dev/book).
