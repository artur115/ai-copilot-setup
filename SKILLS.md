# Every skill and plugin I installed

Six sources live inside my project repos (1 to 6), a small non-overlapping set of plugins is installed on my Mac (see [My current set](#my-current-set)), and Anthropic's built-in skills come with the account. Numbers 8 to 10 are alternatives to superpowers, not extras. Number 11 is the marketing kit, curated from three more repos.

A **skill** is a folder with a `SKILL.md` file (and sometimes scripts). Claude reads it only when your request matches its description. A **plugin** bundles skills, slash commands, agents or hooks so they install in one step. A **marketplace** is a GitHub repo that lists plugins.

Three places a skill can live:

| Where | Scope | How it gets there |
|---|---|---|
| Your Claude account | Every chat and session | Built in, or uploaded in the Claude app's skills settings |
| `~/.claude/skills/` on your Mac | Every Claude Code session on that Mac | Copy the folder, or `npx skills add ...` |
| `<repo>/.claude/skills/` | Anyone who opens that repo | Commit the folder, so cloud sessions and teammates get it too |

I put the build-and-ship skills **inside the app's repo** so cloud sessions always have them.

## From GitHub repos

### 1. glebis/claude-skills
About 100 community skills by Gleb Kalinin, MIT licensed. Repo: <https://github.com/glebis/claude-skills>

I copied four of them into the Pillwave repo (`.claude/skills/`, from commit `4d37d3b`):

| Skill | What it does | When I use it |
|---|---|---|
| `feature-factory` | Takes one feature from intent to merge: a written goal contract, TDD, deterministic checks, and two human checkpoints (approve the goal, approve the merge) | "Let's build the reminder snooze feature" |
| `tdd` | Enforces red, green, refactor with small vertical slices; writes tests in a separate context from the code so the tests stay honest. Supports Jest, Vitest, pytest and others | Inside a feature, for logic that must not break |
| `app-map` | Inventories every screen and flow from the code, reads the real tests, and builds one HTML page with a ranked "test next" list | "What should we test next?" |
| `app-release` | Step-by-step iOS release to TestFlight and the App Store, including signing and App Privacy labels, and fixes for common upload errors | Shipping a build (macOS and Xcode) |

Install:

```bash
# tdd is published as a plugin
/plugin marketplace add glebis/claude-skills
/plugin install tdd@glebis-skills

# the others install as plain skills
npx skills add glebis/claude-skills --skill feature-factory
npx skills add glebis/claude-skills --skill app-map
npx skills add glebis/claude-skills --skill app-release
```

Or ask Claude: *"Copy feature-factory, tdd, app-map and app-release from glebis/claude-skills into this repo's .claude/skills and keep the MIT license file."*

### 2. Graphify-Labs/graphify
Turns a folder of code, docs, images or video into a knowledge graph Claude can query before it opens files. Repo: <https://github.com/Graphify-Labs/graphify> · PyPI package: `graphifyy`

- Writes `graphify-out/` with `graph.html` (interactive map), `GRAPH_REPORT.md` (summary) and `graph.json` (queryable graph).
- Adds hooks so Claude checks the graph before it searches or reads files.
- Commit `graphify-out/` so every new session starts with the map.

Install:

```bash
pip install graphifyy && graphify install    # on macOS, use pipx if pip refuses
```

Then type `/graphify .` in Claude Code.

### 3. addyosmani/agent-skills
"Production-grade engineering skills" by Addy Osmani: about 20 skills plus slash commands for each stage of building software: `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`, `/webperf`, `/a11y`. Repo: <https://github.com/addyosmani/agent-skills>

```
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

### 4. DietrichGebert/ponytail
A plugin that makes the agent write the shortest code that works, "the lazy senior dev", while still adding tests for risky logic. Repo: <https://github.com/DietrichGebert/ponytail>

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

### 5. expo/skills (through Anthropic's official marketplace)
Official Expo skills for React Native: Expo Router UI, data fetching, EAS builds, App Store and Play Store releases, and SDK upgrades. Listed in <https://github.com/anthropics/claude-plugins-official>, with the code at <https://github.com/expo/skills>.

```
/plugin install expo@claude-plugins-official
```

### 6. artur115/ai-copilot-setup (this repo)
My five skills for the job search itself. See [README](README.md#install-my-five-skills).

```
/plugin marketplace add artur115/ai-copilot-setup
/plugin install job-search-kit@ai-copilot-setup
```

## Plugins installed on my Mac (per computer)

Plugins installed in Claude Code on a Mac live on that Mac only (`claude plugin list` shows them). Install them again on each new laptop. Cloud sessions only get the plugins listed in a repo's `.claude/settings.json`.

### My current set

| Plugin | Job | Install |
|---|---|---|
| `superpowers` | **The one coding method:** brainstorm, plan, build test-first, review | `/plugin install superpowers@claude-plugins-official` |
| `ponytail` | Keeps generated code short | see [4](#4-dietrichgebertponytail) |
| `agent-skills` | `/spec` `/plan` `/build` `/test` `/review` `/ship`, which run only when you type them | see [3](#3-addyosmaniagent-skills) |
| `expo` | React Native / Expo apps | see [5](#5-exposkills-through-anthropics-official-marketplace) |
| `job-search-kit` | This repo's five skills | see [6](#6-artur115ai-copilot-setup-this-repo) |
| `marketing-kit` | Marketing: one skill per job | see [11](#11-marketing-kit-this-repo) |
| `claude-mem` | Memory between sessions | see below |
| `cloudflare` | Domains, DNS and deploys | `/plugin install cloudflare@cloudflare` |

Each one does a different job, so their instructions don't compete.

### Why I don't stack coding-style plugins

I used to have ECC, superpowers, mattpocock-skills, andrej-karpathy-skills and the glebis `tdd` plugin all enabled. I removed all but superpowers, because more of them doesn't mean a second opinion:

- **They don't take turns.** Every enabled plugin's instructions go into the same session. Claude reads them as one rulebook; nothing runs "after" another to check its work.
- **Their rules contradict each other.** "Brainstorm and plan in detail first" (superpowers), "make the smallest change, don't over-plan" (Karpathy), "state facts before the first edit" (ECC's GateGuard hook). Claude picks one each time, so behaviour gets inconsistent.
- **Several skills match the same request.** Ask "plan this feature" and four planning skills fit. You can't tell which one fires.
- **It costs more.** Every plugin adds its skill list to every session, and ECC adds hundreds of skills plus hooks on every action.

**A real double-check runs one after another:** Claude writes the change, then a separate review reads the result. Type `/review` (agent-skills) or ask *"review this diff for bugs before I commit"*.

Pick **one** coding method. If you prefer one of the alternatives below, install it **instead of** superpowers, not alongside it.

### claude-mem: memory between sessions
[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) (Apache-2.0). Hooks record what Claude does in each session, a small local worker summarizes it into a SQLite database in `~/.claude-mem`, and the next session in the same project starts with that context. The background summaries use your Claude plan (Haiku). Setup and the safe install flags are in [prompts/15](prompts/15-memory-claude-mem.md).

```bash
CLAUDE_MEM_ONLINE_OPTIN=false npx claude-mem install --provider claude
```

```bash
npx claude-mem telemetry disable
```

Don't use the plain `npx claude-mem install`: it pre-selects a paid plan with a card-required trial.

### 7. obra/superpowers (my pick)
A complete development method built from small skills: brainstorm, write a plan, then build in test-driven steps with reviews. About 15 skills. It already covers test-first work, so I don't also install the glebis `tdd` plugin on my Mac (Pillwave keeps its own copy in `.claude/skills`). Repo: <https://github.com/obra/superpowers>

```
/plugin install superpowers@claude-plugins-official
```

### Alternatives (choose one instead of superpowers)

#### 8. affaan-m/ECC (Everything Claude Code), the hackathon winner
Affaan Mustafa won the Anthropic x Forum Ventures hackathon (Sep 2025) and open-sourced his whole setup under MIT. Its README lists **327 skills, 72 agents and 98 commands**, plus hooks, memory, rules and the AgentShield security scanner. Repo: <https://github.com/affaan-m/ECC>

```
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

Its hooks change how Claude works on every action. When I installed it, Claude Code reported that ECC's helper packages were not installed ("its package.json sets overrides, which this install does not apply"), so some hooks may fail. Read its README's setup and opt-out settings first.

#### 9. mattpocock/skills
About 40 small, composable skills by Matt Pocock that you adapt to your own way of working. Repo: <https://github.com/mattpocock/skills>

```
/plugin install mattpocock-skills@claude-plugins-official
```

#### 10. forrestchang/andrej-karpathy-skills
One set of guidelines based on Andrej Karpathy's notes on common LLM coding mistakes: think before coding, keep it simple, change only what was asked. Repo: <https://github.com/forrestchang/andrej-karpathy-skills>

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

### Clean up a stacked setup

Already installed several of them? This removes the overlapping ones and adds the missing ones. Paste it into Terminal; it is safe to run twice:

```bash
for p in ecc@ecc mattpocock-skills@claude-plugins-official andrej-karpathy-skills@karpathy-skills tdd@glebis-skills; do
  if claude plugin list 2>/dev/null | grep -q "$p"; then claude plugin uninstall "$p"; fi
done
claude plugin marketplace add artur115/ai-copilot-setup
for p in superpowers@claude-plugins-official job-search-kit@ai-copilot-setup; do
  if claude plugin list 2>/dev/null | grep -q "$p"; then echo "already installed: $p"; else claude plugin install "$p"; fi
done
claude plugin list
```

Then restart Claude Code.

## Marketing skills

### 11. marketing-kit (this repo)
56 marketing skills in one plugin, at [plugins/marketing-kit](plugins/marketing-kit/README.md). I read five marketing skill repos and kept one skill per job, for the same reason I don't stack coding plugins:

| From | Kept | Left out |
|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT, 61k stars) | 50 of 53 skills: `product-marketing` (the brand profile every other skill reads), `copywriting`, `social`, `influencer-marketing`, `launch`, `offers`, `ads`, `ad-creative`, `seo-audit`, `analytics` and more | `emails`, `sms`, `cold-email`: the email bible does these in more depth |
| [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) (MIT) | The whole skill and its 16 reference files | Nothing |
| [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) (MIT) | 5 of 162: `tiktok-shop-ads`, `tiktok-shop-listing-optimization`, `tiktok-shop-affiliate-program`, `tiktok-shop-analytics`, `etsy-seo` | 88 are short placeholders with no guidance; the larger general ones repeat corey |
| [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) | Not bundled: no license file | Install it yourself once you run paid ads (skills only; its guide also adds a third-party ad-account connector) |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | Not bundled | Its `/market` reports repeat corey's jobs; use it instead of the kit, not with it |

```
/plugin install marketing-kit@ai-copilot-setup
```

Then: *"Set up my product marketing context."* Prompt: [prompts/18](prompts/18-marketing-kit.md).

I checked it against every plugin above: no shared skill names, no hooks, and the two near-overlaps (`launch`, `aso`) now name their engineering counterparts. Details: [Checked against the rest of this setup](plugins/marketing-kit/README.md#checked-against-the-rest-of-this-setup).

## An outreach tool (not a skill): Sellbird

[ethanplusai/sellbird](https://github.com/ethanplusai/sellbird), AGPL-3.0, Python 3.11+. An
open-source cold-email agent that runs through Claude Code on your Claude plan. For a job search,
its hiring signals find companies with your role open on their own job board, and it drafts a short
note to the person who decides. Everything waits for your approval. Setup: [prompts/13](prompts/13-outreach-sellbird.md).

## Is there a resume skill?

None of the sources above has a skill for building resumes. I built mine by hand, as `resume.html` printed to PDF with Playwright, so this repo now packages that method as the [`resume-builder`](skills/resume-builder/SKILL.md) skill, paired with [`ats-resume-check`](skills/ats-resume-check/SKILL.md). Community resume skills also exist (search "resume" on skills.sh). I haven't reviewed them, so read their SKILL.md before installing one.

## Built into my Claude account (no install needed)

These came with my account from Anthropic. You can turn each one on or off in the Claude app's settings.

| Skill | What it does |
|---|---|
| `docx`, `xlsx`, `pptx`, `pdf` | Create and edit Word, Excel, PowerPoint and PDF files |
| `google-workspace` | Edit Google Docs, Sheets and Slides in place through the Google connectors (this is how my presentation was built) |
| `docs` | Claude's own shareable documents |
| `deep-research` | Multi-source research with a written report |
| `skill-creator` | Writes and tests new skills for you |
| `chrome-browser` | Rules for Claude in Chrome (used for LinkedIn) |
| `built-in-browser`, `computer-use` | Rules for the desktop app's browser pane and screen control |
| `import-memory`, `morning` | Import memory from another assistant; a daily morning brief |

I also have one private skill of my own, `post-trade-analysis`, which grades alerts from a trading scanner I wrote. It isn't shared here.

## Agents (not skills)

The Pillwave marketing repo has 23 Claude **subagents** in `.claude/agents/`, one Markdown file per role: trend scout, content strategist, caption writer, email writer, ASO researcher, compliance checker, weekly planner and so on. An agent is a named helper with its own instructions and tools; Claude hands a task to it. To make your own, ask: *"Create a subagent in .claude/agents that reviews my cover letters against the job description."*

## Safety settings that go with all of this

- **Environments:** each cloud environment has a network allowlist. A session can only reach the sites you allowed.
- **Keys:** add API keys through the secure credential form, never in chat.
- **Privacy guard:** I run a plugin that stops Claude writing my email address into files or web requests unless I type it myself.
