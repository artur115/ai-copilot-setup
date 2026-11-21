# Install everything

Run this in **Claude Code on your own Mac** (Claude app → Code tab, a local folder, not a cloud session). Plugins install per computer. Needs a paid Claude plan. Node.js (for `npx`) and Python 3.10+ are only needed for steps 4 and 5; Claude will help install them if they're missing.

## Instructions for Claude

Set up this Mac for an AI-assisted job search, following https://github.com/artur115/ai-job-search-setup (read README.md and SKILLS.md first).

Run the commands below in the terminal, one at a time. Tell the user what each one did. If one fails, explain the error in plain words and continue with the rest. Never ask the user to paste a password or API key into chat.

```bash
# 1. Artur's job-search kit (setup guide, resume builder, ATS check, proof project)
claude plugin marketplace add artur115/ai-job-search-setup
claude plugin install job-search-kit@ai-job-search-setup

# 2. Everything Claude Code (ECC), the Anthropic hackathon winner: 327 skills, 72 agents.
#    Before installing, read its README and tell the user which hooks it turns on
#    (for example GateGuard) and how to switch them off.
claude plugin marketplace add https://github.com/affaan-m/ECC
claude plugin install ecc@ecc

# 3. Engineering method plugins
claude plugin install superpowers@claude-plugins-official
claude plugin install mattpocock-skills@claude-plugins-official
claude plugin marketplace add forrestchang/andrej-karpathy-skills
claude plugin install andrej-karpathy-skills@karpathy-skills
claude plugin marketplace add addyosmani/agent-skills
claude plugin install agent-skills@addy-agent-skills
claude plugin marketplace add DietrichGebert/ponytail
claude plugin install ponytail@ponytail

# 4. glebis/claude-skills: build-and-ship skills
claude plugin marketplace add glebis/claude-skills
claude plugin install tdd@glebis-skills
npx skills add glebis/claude-skills --skill feature-factory
npx skills add glebis/claude-skills --skill app-map
npx skills add glebis/claude-skills --skill app-release

# 5. graphify: code knowledge graph (use pipx if pip refuses)
pipx install graphifyy || pip install graphifyy
graphify install

# 6. Optional, only for an iPhone app built with Expo
# claude plugin install expo@claude-plugins-official
```

When everything is done:
- show a table: what was installed, where it came from, and anything that failed;
- tell the user to restart Claude Code so the plugins load;
- after the restart, use the job-search-setup skill to walk the user through the 12 setup steps, starting with step 01.

Only want the job-search part? Step 1 is enough. Steps 2 to 5 are for building projects and apps.
